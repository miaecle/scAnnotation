"""Evaluation metrics for cell type annotation results."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TYPE_CHECKING, Any, Callable

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from tqdm import tqdm

from .backends.base import complete_with_retry

if TYPE_CHECKING:
    from .backends.base import LLMBackend


# --------------------------------------------------------------------------- #
# Parsing helpers
# --------------------------------------------------------------------------- #

def extract_cell_type(response: str) -> str:
    """Extract the cell type label from the first line of an LLM response.

    The expected response format is::

        Cell Type Name
        Brief rationale (one or more lines)

    Args:
        response: Raw LLM response string.

    Returns:
        First non-empty line, stripped of whitespace.
    """
    for line in response.strip().splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return response.strip()


def extract_rationale(response: str) -> str:
    """Extract the rationale (everything after the first line) from an LLM response."""
    lines = response.strip().splitlines()
    return "\n".join(lines[1:]).strip()


def parse_results(
    results_df: pd.DataFrame,
    pred_col: str = "pred_label",
) -> pd.DataFrame:
    """Add ``pred_celltype`` and ``pred_rationale`` columns by parsing ``pred_col``.

    Args:
        results_df: DataFrame with a column containing raw LLM responses.
        pred_col: Name of the column with raw LLM responses.

    Returns:
        Copy of ``results_df`` with two new columns added.
    """
    df = results_df.copy()
    df["pred_celltype"] = df[pred_col].apply(extract_cell_type)
    df["pred_rationale"] = df[pred_col].apply(extract_rationale)
    return df


# --------------------------------------------------------------------------- #
# Matching strategies
# --------------------------------------------------------------------------- #

def accuracy(y_true: list[str], y_pred: list[str], case_sensitive: bool = False) -> float:
    """Overall accuracy of predicted cell type labels.

    Args:
        y_true: Ground-truth cell type labels.
        y_pred: Predicted cell type labels.
        case_sensitive: If False (default), comparison ignores case and strips whitespace.

    Returns:
        Fraction of correct predictions in [0, 1].
    """
    if not case_sensitive:
        y_true = [s.strip().lower() for s in y_true]
        y_pred = [s.strip().lower() for s in y_pred]
    return float(accuracy_score(y_true, y_pred))


def per_class_metrics(
    y_true: list[str],
    y_pred: list[str],
    case_sensitive: bool = False,
) -> pd.DataFrame:
    """Per-class precision, recall, F1, and support.

    Args:
        y_true: Ground-truth labels.
        y_pred: Predicted labels.
        case_sensitive: If False, normalises case before computing.

    Returns:
        DataFrame indexed by cell type with columns
        ['precision', 'recall', 'f1-score', 'support'].
    """
    if not case_sensitive:
        y_true = [s.strip().lower() for s in y_true]
        y_pred = [s.strip().lower() for s in y_pred]

    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    df = pd.DataFrame(report).T
    # keep only per-class rows (drop macro/weighted avg rows)
    avg_rows = {"accuracy", "macro avg", "weighted avg"}
    df = df[~df.index.isin(avg_rows)].copy()
    df["support"] = df["support"].astype(int)
    return df.sort_values("f1-score", ascending=False)


def annotation_report(
    results_df: pd.DataFrame,
    true_col: str = "true_label",
    pred_col: str = "pred_label",
    case_sensitive: bool = False,
) -> dict:
    """Compute a full evaluation report from an annotated results DataFrame.

    Args:
        results_df: DataFrame with true and predicted label columns.
        true_col: Column name for ground-truth labels.
        pred_col: Column name for predicted labels.
        case_sensitive: If False, normalises case before computing.

    Returns:
        Dictionary with keys:
          - 'overall_accuracy': float
          - 'per_class': pd.DataFrame (precision/recall/F1 per cell type)
          - 'confusion_matrix': pd.DataFrame (rows=true, cols=predicted)
    """
    y_true = results_df[true_col].tolist()
    y_pred = results_df[pred_col].tolist()

    if not case_sensitive:
        y_true_norm = [s.strip().lower() for s in y_true]
        y_pred_norm = [s.strip().lower() for s in y_pred]
    else:
        y_true_norm, y_pred_norm = y_true, y_pred

    labels = sorted(set(y_true_norm) | set(y_pred_norm))

    cm = confusion_matrix(y_true_norm, y_pred_norm, labels=labels)
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)

    return {
        "overall_accuracy": float(accuracy_score(y_true_norm, y_pred_norm)),
        "per_class": per_class_metrics(y_true, y_pred, case_sensitive=case_sensitive),
        "confusion_matrix": cm_df,
    }


def keyword_accuracy(
    y_true: list[str],
    y_pred: list[str],
    min_word_len: int = 1,
    auto_extract: bool = True,
) -> float:
    """Keyword-matching accuracy.

    A prediction is counted as correct if at least one content word from the
    true label appears in the predicted cell type string.  Generic biological
    terms (cell, cells, type, …) are treated as stopwords and ignored.

    Short abbreviations such as ``B``, ``NK``, ``DC``, ``CD4`` are kept
    because they carry biological meaning.

    Args:
        y_true: Ground-truth cell type labels.
        y_pred: Predicted labels (raw LLM responses or extracted cell types).
        min_word_len: Minimum token length to consider (default 1 keeps all).
        auto_extract: If True, apply :func:`extract_cell_type` to each element
                      of ``y_pred`` before matching (handles multi-line responses).

    Returns:
        Fraction of predictions with at least one keyword match, in [0, 1].
    """
    _STOPWORDS = {
        "cell", "cells", "type", "types", "the", "and", "or", "of",
        "in", "a", "an", "is", "are", "be", "with", "for", "other",
    }

    correct = 0
    for true, pred in zip(y_true, y_pred):
        pred_ct = extract_cell_type(pred) if auto_extract else pred
        true_tokens = {
            t.lower().strip("+()/αβγδ")
            for t in true.split()
            if len(t) >= min_word_len and t.lower() not in _STOPWORDS
        }
        pred_lower = pred_ct.lower()
        if any(tok and tok in pred_lower for tok in true_tokens):
            correct += 1

    keyword_accuracy = correct / len(y_true) if y_true else 0.0
    return keyword_accuracy


_LLM_JUDGE_SYSTEM = (
    "You are an expert in single-cell annotation evaluating cell type label "
    "consistency. Provide brief reasoning, then end with a line formatted "
    "exactly as Judgment: [Category]. The category must be one of: "
    "Major correct, Subtype correct, Partially correct, Incorrect."
)

_LLM_JUDGE_BINARY_SYSTEM = (
    "You are an expert in single-cell annotation evaluating cell type label "
    "consistency. Compare the reference label and predicted label, then answer "
    "with exactly one token: YES or NO."
)

_LLM_JUDGE_TEMPLATE_PREFIX = (
    "I am working on a single-cell transcriptomic cell type annotation task. "
    "The reference label (A) may be an abbreviation or a marker-based "
    "description of a cell type. Both the reference label (A) and the model's "
    "predicted label (B) have been standardized and mapped to Cell Ontology "
    "terms whenever possible. As an expert in single-cell annotation, please "
    "evaluate whether my model's predicted label (B) is accurate, according "
    "to the following criteria:\n"
    "- Major correct: A and B belong to the same major cell type category "
    "(e.g., T cells), but are different subtypes (e.g., CD4+ vs CD8+), or A "
    "is a subtype of B, and B is the major category of A (e.g., A = CD4+ T "
    "cells, B = T cells);\n"
    "- Subtype correct: A and B refer to the same cell subtype, despite "
    "differences in naming conventions (e.g., abbreviation vs marker gene "
    "expression), or B is a subtype of A (e.g., A = B cells, B = "
    "class-switched memory B cells);\n"
    "- Partially correct: B contains multiple possible cell types (e.g., "
    "\"celltypeA or celltypeB\"), and one of them matches A (either Major or "
    "Subtype correct), but others are incorrect or unrelated, making the "
    "prediction ambiguous;\n"
    "- Incorrect: B and A belong to entirely different cell lineages (e.g., "
    "labeling a neuron as an epithelial cell), or B includes multiple "
    "predictions and none of them match A;\n"
    "Please follow the output format below:\n"
    "- First, provide a brief reasoning explaining your judgment.\n"
    "- End with a line formatted exactly as Judgment: [Category], where the "
    "category must be one of: Major correct / Subtype correct / Partially "
    "correct / Incorrect.\n"
    "- Example output:\n"
    "Reasoning: A and B are both T cell types, but A is CD4+ and B is CD8+, "
    "indicating different subtypes within the same major category.\n"
    "Judgment: Major correct\n"
)

_LLM_JUDGE_CASE_TEMPLATE = (
    "Now evaluate the following case:\n"
    "Reference label (A): {true}\n"
    "Predicted label (B): {pred}"
)

_LLM_JUDGE_TEMPLATE = _LLM_JUDGE_TEMPLATE_PREFIX + _LLM_JUDGE_CASE_TEMPLATE

_LLM_JUDGE_BINARY_TEMPLATE_PREFIX = (
    "I am working on a single-cell transcriptomic cell type annotation task. "
    "The reference label (GT) may be an abbreviation or a marker-based "
    "description of a cell type. The model prediction (PRED) has been "
    "standardized whenever possible. As an expert in single-cell annotation, "
    "please determine whether PRED is correct for GT.\n"
    "Evaluation rule:\n"
    "- YES: PRED is biologically correct for GT (same subtype, equivalent name, "
    "or an acceptable naming variant that clearly refers to the same cell type).\n"
    "- NO: PRED is not correct for GT (different lineage/type, ambiguous mixed "
    "prediction, or otherwise inconsistent with GT).\n"
    "Please follow the output format strictly:\n"
    "- Output exactly one token: YES or NO.\n"
    "- Do not output any explanation, punctuation, or extra text.\n"
)

_LLM_JUDGE_BINARY_CASE_TEMPLATE = (
    "Now evaluate the following case:\n"
    "Reference label (GT): {true}\n"
    "Predicted label (PRED): {pred}"
)


def _build_llm_judge_prompt(true_label: str, pred_label: str) -> str:
    return _LLM_JUDGE_CASE_TEMPLATE.format(true=true_label, pred=pred_label)


def _build_llm_judge_binary_prompt(true_label: str, pred_label: str) -> str:
    return _LLM_JUDGE_BINARY_CASE_TEMPLATE.format(true=true_label, pred=pred_label)


def _judge_complete_kwargs(backend: "LLMBackend") -> dict[str, Any] | None:
    if backend.__class__.__name__ != "GeminiBackend":
        return None
    return {
        "cached_user_prefix": _LLM_JUDGE_TEMPLATE_PREFIX,
        "cache_key": "llm_judge_template_v1",
    }


def _judge_binary_complete_kwargs(backend: "LLMBackend") -> dict[str, Any] | None:
    if backend.__class__.__name__ != "GeminiBackend":
        return None
    return {
        "cached_user_prefix": _LLM_JUDGE_BINARY_TEMPLATE_PREFIX,
        "cache_key": "llm_judge_binary_template_v1",
    }

_LLM_JUDGMENT_SCORES = {
    "Subtype correct": 1.0,
    "Major correct": 0.5,
    "Partially correct": 0.25,
    "Incorrect": 0.0,
}


def _validate_llm_judge_output_strict(response: str) -> None:
    """Validate strict rubric-judge output format.

    Required structure:
    - At least two non-empty lines.
    - First line starts with ``Reasoning:``.
    - Last line starts with ``Judgment:``.
    - Judgment value is exactly one of the rubric labels.
    """
    text = str(response).strip()
    if not text:
        raise ValueError("LLM judge response is empty.")

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError(
            "LLM judge response must contain at least two lines: "
            "'Reasoning: ...' and 'Judgment: ...'."
        )

    if not lines[0].lower().startswith("reasoning:"):
        raise ValueError("LLM judge response must start with 'Reasoning:'.")

    if not lines[-1].lower().startswith("judgment:"):
        raise ValueError("LLM judge response must end with 'Judgment:'.")

    candidate = lines[-1].split(":", 1)[1].strip().strip(".。*` ")
    if candidate not in _LLM_JUDGMENT_SCORES:
        valid = " | ".join(_LLM_JUDGMENT_SCORES)
        raise ValueError(
            f"Invalid judgment label {candidate!r}. Expected one of: {valid}."
        )


def _validate_llm_judge_binary_output_strict(response: str) -> None:
    """Validate strict binary-judge output format: exactly YES or NO."""
    token = str(response).strip()
    if token not in {"YES", "NO"}:
        raise ValueError(
            f"LLM binary judge response must be exactly 'YES' or 'NO', got: {response!r}"
        )


def parse_llm_judge_response(response: str) -> tuple[str, float, str]:
    """Parse the rubric-based LLM judge response.

    Returns a tuple of ``(judgment, score, reasoning)``. The response must
    contain a valid ``Judgment: ...`` line; otherwise a ``ValueError`` is raised.
    """
    text = str(response).strip()
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    judgment: str | None = None
    judgment_line_idx: int | None = None
    judgment_marker_pos: int | None = None
    for idx in range(len(lines) - 1, -1, -1):
        line = lines[idx]
        lower_line = line.lower()
        marker_pos = lower_line.rfind("judgment:")
        if marker_pos < 0:
            continue

        candidate = line[marker_pos + len("judgment:") :].strip().strip(".。*` ")
        for valid in _LLM_JUDGMENT_SCORES:
            if candidate.lower().startswith(valid.lower()):
                judgment = valid
                judgment_line_idx = idx
                judgment_marker_pos = marker_pos
                break
        if judgment is not None:
            break

    if judgment is None:
        valid = " | ".join(_LLM_JUDGMENT_SCORES)
        raise ValueError(
            "Could not parse LLM judge response. Expected a final line like "
            f"'Judgment: <{valid}>', got: {response!r}"
        )

    reasoning_lines = []
    for idx, line in enumerate(lines):
        if judgment_line_idx is not None and idx == judgment_line_idx:
            assert judgment_marker_pos is not None
            prefix = line[:judgment_marker_pos].strip()
            if prefix:
                if prefix.lower().startswith("reasoning:"):
                    reasoning_lines.append(prefix.split(":", 1)[1].strip())
                else:
                    reasoning_lines.append(prefix)
            break
        if line.lower().startswith("reasoning:"):
            reasoning_lines.append(line.split(":", 1)[1].strip())
        else:
            reasoning_lines.append(line)
    reasoning = "\n".join(part for part in reasoning_lines if part).strip()

    return judgment, _LLM_JUDGMENT_SCORES[judgment], reasoning


def parse_llm_judge_binary_response(response: str) -> tuple[str, int]:
    """Parse binary LLM-judge response into a YES/NO decision and 0/1 score."""
    text = str(response).strip()
    if text == "YES":
        return "YES", 1
    if text == "NO":
        return "NO", 0
    raise ValueError(
        "Could not parse LLM binary judge response. Expected 'YES' or 'NO', "
        f"got: {response!r}"
    )


def llm_judge_accuracy(
    y_true: list[str],
    y_pred: list[str],
    backend: "LLMBackend",
    auto_extract: bool = True,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
) -> float:
    """LLM-as-judge average rubric score.

    Uses the provided backend to decide, for each (true, pred) pair, whether
    the prediction is correct under a four-level rubric.

    Args:
        y_true: Ground-truth cell type labels.
        y_pred: Predicted labels (raw LLM responses or extracted cell types).
        backend: :class:`~sc_annotation.backends.base.LLMBackend` instance used
                 as the judge.
        auto_extract: If True, extract first line from each ``y_pred`` entry.

    Returns:
        Mean rubric score in [0, 1].
    """
    scores: list[float] = []
    complete_kwargs = _judge_complete_kwargs(backend)
    for i, (true, pred) in enumerate(zip(y_true, y_pred)):
        pred_ct = extract_cell_type(pred) if auto_extract else pred
        prompt = _build_llm_judge_prompt(true, pred_ct)
        response = complete_with_retry(
            backend,
            prompt,
            system_message=_LLM_JUDGE_SYSTEM,
            usage_sink=usage_sink,
            complete_kwargs=complete_kwargs,
            response_validator=_validate_llm_judge_output_strict,
            usage_context={
                "step": "llm_judge",
                "phase": "evaluation",
                "pair_index": i,
            },
        )
        _, score, _ = parse_llm_judge_response(response)
        scores.append(score)
    return float(np.mean(scores)) if scores else 0.0


def llm_judge_binary_accuracy(
    y_true: list[str],
    y_pred: list[str],
    backend: "LLMBackend",
    auto_extract: bool = True,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
) -> float:
    """LLM-as-judge binary accuracy where the model outputs YES/NO."""
    scores: list[int] = []
    complete_kwargs = _judge_binary_complete_kwargs(backend)
    for i, (true, pred) in enumerate(zip(y_true, y_pred)):
        pred_ct = extract_cell_type(pred) if auto_extract else pred
        prompt = _build_llm_judge_binary_prompt(true, pred_ct)
        response = complete_with_retry(
            backend,
            prompt,
            system_message=_LLM_JUDGE_BINARY_SYSTEM,
            usage_sink=usage_sink,
            complete_kwargs=complete_kwargs,
            response_validator=_validate_llm_judge_binary_output_strict,
            usage_context={
                "step": "llm_judge_binary",
                "phase": "evaluation",
                "pair_index": i,
            },
        )
        _, score = parse_llm_judge_binary_response(response)
        scores.append(score)
    return float(np.mean(scores)) if scores else 0.0


def _aggregate_per_sample(
    per_sample_df: pd.DataFrame,
    enabled: set[str],
    hierarchy_max_depth: int | None = None,
) -> dict[str, float]:
    """Reduce a per-sample evaluation DataFrame to scalar metric means."""
    n = len(per_sample_df)
    records: dict[str, float] = {}
    if "exact" in enabled and "acc" in per_sample_df.columns:
        records["exact"] = float(per_sample_df["acc"].mean()) if n else 0.0
    if "keyword" in enabled and "keyword" in per_sample_df.columns:
        records["keyword"] = float(per_sample_df["keyword"].mean()) if n else 0.0
    if "hierarchy" in enabled and "hierarchy_depth" in per_sample_df.columns:
        records["hierarchy_depth"] = float(per_sample_df["hierarchy_depth"].mean()) if n else 0.0
        max_depth = hierarchy_max_depth
        if max_depth is None:
            max_depth = int(per_sample_df["hierarchy_depth"].max()) if n else 0
        # match_pct at level k = fraction of samples matching true/pred through level k;
        # level 0 is the complement (fraction with no match at any level)
        hierarchy_counts = per_sample_df["hierarchy_depth"].value_counts()
        cumulative_counts = {
            depth: int(hierarchy_counts[hierarchy_counts.index >= depth].sum())
            for depth in range(1, max_depth + 1)
        }
        cumulative_counts[0] = int(hierarchy_counts.get(0, 0))
        for level in range(0, max_depth + 1):
            records[f"hierarchy_level_{level}_match_pct"] = (
                cumulative_counts[level] / n if n else 0.0
            )
    if "llm_score" in per_sample_df.columns:
        records["llm_judge"] = float(per_sample_df["llm_score"].mean()) if n else 0.0
    if "llm_binary" in per_sample_df.columns:
        records["llm_judge_binary"] = float(per_sample_df["llm_binary"].mean()) if n else 0.0
    return records


def bootstrap_metrics(
    per_sample_df: pd.DataFrame,
    true_labels: pd.Series,
    strategies: list[str] | None = None,
    n_bootstrap: int = 1000,
    seed: int | None = None,
    ci: float = 0.95,
    hierarchy_max_depth: int | None = None,
) -> pd.DataFrame:
    """Stratified bootstrap uncertainty estimates for aggregate metrics.

    For each of ``n_bootstrap`` iterations, resamples cells *with replacement*
    independently within each true cell-type group (so class proportions are
    preserved), assembling a combined set the same size as the full
    evaluation, then recomputes each metric's mean. The resulting empirical
    distribution of the metric estimates its uncertainty.

    Args:
        per_sample_df: Output of :func:`evaluate_per_sample`.
        true_labels: Ground-truth cell type label per row, aligned to
            ``per_sample_df.index`` (used to stratify the resampling).
        strategies: Which strategies' metrics to bootstrap.
        n_bootstrap: Number of bootstrap resamples.
        seed: Random seed for reproducibility.
        ci: Confidence level for the percentile interval (e.g. 0.95 → 2.5/97.5).
        hierarchy_max_depth: Fixed number of hierarchy levels, so per-resample
            ``hierarchy_level_{k}_match_pct`` keys stay consistent.

    Returns:
        Single-row DataFrame with ``{metric}_std``, ``{metric}_ci_low`` and
        ``{metric}_ci_high`` columns for each aggregate metric.
    """
    enabled = {str(s).lower() for s in (strategies or ["exact", "keyword"])}
    if len(per_sample_df) == 0 or n_bootstrap <= 0:
        return pd.DataFrame([{}])

    labels = true_labels.reindex(per_sample_df.index).astype(str).str.strip().str.lower()
    group_positions = [np.flatnonzero((labels == label).to_numpy()) for label in labels.unique()]

    rng = np.random.default_rng(seed)
    boot_values: dict[str, list[float]] = {}
    for _ in range(n_bootstrap):
        sampled_positions = np.concatenate(
            [rng.choice(pos, size=len(pos), replace=True) for pos in group_positions]
        )
        resampled_df = per_sample_df.iloc[sampled_positions]
        for key, value in _aggregate_per_sample(resampled_df, enabled, hierarchy_max_depth).items():
            boot_values.setdefault(key, []).append(value)

    alpha = (1.0 - ci) / 2.0
    records: dict[str, float] = {}
    for key, values in boot_values.items():
        arr = np.asarray(values)
        records[f"{key}_std"] = float(arr.std(ddof=1)) if len(arr) > 1 else 0.0
        records[f"{key}_ci_low"] = float(np.percentile(arr, 100 * alpha))
        records[f"{key}_ci_high"] = float(np.percentile(arr, 100 * (1 - alpha)))
    return pd.DataFrame([records])


def evaluate_all(
    results_df: pd.DataFrame,
    true_col: str = "true_label",
    pred_col: str = "pred_label",
    judge_backend: "LLMBackend | None" = None,
    per_sample_df: pd.DataFrame | None = None,
    strategies: list[str] | None = None,
    concurrency: int = 1,
    hierarchy_paths: dict[str, tuple[str, ...]] | None = None,
    hierarchy_max_depth: int | None = None,
    n_bootstrap: int = 0,
    bootstrap_seed: int | None = None,
) -> pd.DataFrame:
    """Run all available evaluation strategies and return a summary DataFrame.

    Strategies computed (only when included in ``strategies``):
    - ``exact``   : exact string match (case-insensitive, after extracting first line)
    - ``keyword`` : keyword overlap match
    - ``llm_judge`` : mean rubric score from the LLM judge (only if ``judge_backend`` is provided)
    - ``llm_judge_binary`` : mean binary score from the LLM judge (YES=1, NO=0)

    Args:
        results_df: DataFrame with true and predicted label columns.
        true_col: Column name for ground-truth labels.
        pred_col: Column name for raw LLM responses.
        judge_backend: Optional backend for LLM-judge evaluation.
        n_bootstrap: If > 0, run a stratified bootstrap (resampling cells with
            replacement within each true cell type) to estimate uncertainty,
            adding ``{metric}_std``/``_ci_low``/``_ci_high`` columns.
        bootstrap_seed: Random seed for the bootstrap.

    Returns:
        Single-row DataFrame with columns for each strategy's accuracy (plus
        bootstrap uncertainty columns when ``n_bootstrap`` > 0).
    """
    if per_sample_df is None:
        per_sample_df = evaluate_per_sample(
            results_df=results_df,
            true_col=true_col,
            pred_col=pred_col,
            judge_backend=judge_backend,
            strategies=strategies,
            concurrency=concurrency,
            hierarchy_paths=hierarchy_paths,
        )

    enabled = {str(s).lower() for s in (strategies or ["exact", "keyword"])}
    n = len(per_sample_df)
    if "hierarchy" in enabled and "hierarchy_depth" in per_sample_df.columns and hierarchy_max_depth is None:
        hierarchy_max_depth = int(per_sample_df["hierarchy_depth"].max()) if n else 0
    records: dict[str, float] = _aggregate_per_sample(per_sample_df, enabled, hierarchy_max_depth)

    if "hierarchy" in enabled and "hierarchy_depth" in per_sample_df.columns:
        hierarchy_counts = per_sample_df["hierarchy_depth"].value_counts()
        for depth in range(hierarchy_max_depth + 1):
            records[f"hierarchy_depth_{depth}_count"] = int(hierarchy_counts.get(depth, 0))

    if n_bootstrap > 0 and n:
        boot_df = bootstrap_metrics(
            per_sample_df,
            true_labels=results_df.loc[per_sample_df.index, true_col],
            strategies=strategies,
            n_bootstrap=n_bootstrap,
            seed=bootstrap_seed,
            hierarchy_max_depth=hierarchy_max_depth,
        )
        records.update(boot_df.iloc[0].to_dict())

    return pd.DataFrame([records])


def evaluate_per_sample(
    results_df: pd.DataFrame,
    true_col: str = "true_label",
    pred_col: str = "pred_label",
    judge_backend: "LLMBackend | None" = None,
    usage_sink: Callable[[dict[str, Any]], None] | None = None,
    strategies: list[str] | None = None,
    concurrency: int = 1,
    hierarchy_paths: dict[str, tuple[str, ...]] | None = None,
) -> pd.DataFrame:
    """Compute per-sample evaluation outcomes.

    Returns columns (only those requested by ``strategies`` and available):
    - ``acc``: exact match after case-insensitive normalization
    - ``keyword``: keyword overlap match
    - ``hierarchy_depth``: shared hierarchy depth between true and predicted labels
    - ``llm_judgment``: rubric category assigned by the LLM judge
    - ``llm_score``: numeric rubric score
    - ``llm_reasoning``: judge rationale text
    - ``llm_binary_judgment``: binary judge decision (YES/NO)
    - ``llm_binary``: binary judge score (1/0)
    """
    y_true = results_df[true_col].tolist()
    y_pred_raw = results_df[pred_col].tolist()

    _STOPWORDS = {
        "cell", "cells", "type", "types", "the", "and", "or", "of",
        "in", "a", "an", "is", "are", "be", "with", "for", "other",
    }

    acc_flags: list[int] = []
    keyword_flags: list[int] = []
    hierarchy_depths: list[int] = []
    llm_judgments: list[str] = []
    llm_scores: list[float] = []
    llm_reasonings: list[str] = []
    llm_binary_judgments: list[str] = []
    llm_binary_scores: list[int] = []
    enabled = {str(s).lower() for s in (strategies or ["exact", "keyword"])}
    use_exact = "exact" in enabled
    use_keyword = "keyword" in enabled
    use_hierarchy = "hierarchy" in enabled
    use_llm_judge = judge_backend is not None and "llm_judge" in enabled
    use_llm_judge_binary = judge_backend is not None and "llm_judge_binary" in enabled
    use_any_llm_judge = use_llm_judge or use_llm_judge_binary
    judge_complete_kwargs = _judge_complete_kwargs(judge_backend) if use_llm_judge else None
    judge_binary_complete_kwargs = _judge_binary_complete_kwargs(judge_backend) if use_llm_judge_binary else None

    if use_hierarchy and hierarchy_paths is None:
        raise ValueError("The 'hierarchy' strategy requires hierarchy_paths.")

    max_workers = max(1, int(concurrency or 1))

    def _evaluate_one(i: int, true: Any, pred_raw: Any) -> tuple[int, dict[str, Any]]:
        true_norm = str(true).strip().lower()
        pred_ct = extract_cell_type(str(pred_raw))
        pred_norm = pred_ct.strip().lower()

        record: dict[str, Any] = {}
        if use_exact:
            record["acc"] = int(true_norm == pred_norm)

        if use_keyword:
            true_tokens = {
                t.lower().strip("+()/αβγδ")
                for t in str(true).split()
                if len(t) >= 1 and t.lower() not in _STOPWORDS
            }
            record["keyword"] = int(any(tok and tok in pred_norm for tok in true_tokens))

        if use_hierarchy:
            true_path = hierarchy_paths.get(true_norm)
            pred_path = hierarchy_paths.get(pred_norm)
            if true_path is None or pred_path is None:
                record["hierarchy_depth"] = 0
                print(f"[Evaluation WARN] Missing hierarchy path for true={true_norm!r} or pred={pred_norm!r}")
            else:
                common_depth = 0
                for true_level, pred_level in zip(true_path, pred_path):
                    if true_level != pred_level:
                        break
                    common_depth += 1
                record["hierarchy_depth"] = common_depth

        if use_llm_judge:
            try:
                prompt = _build_llm_judge_prompt(true, pred_ct)
                response = complete_with_retry(
                    judge_backend,
                    prompt,
                    system_message=_LLM_JUDGE_SYSTEM,
                    usage_sink=usage_sink,
                    complete_kwargs=judge_complete_kwargs,
                    response_validator=_validate_llm_judge_output_strict,
                    usage_context={
                        "step": "llm_judge",
                        "phase": "evaluation",
                        "sample_pos": i,
                        "result_index": results_df.index[i],
                    },
                )
                judgment, score, reasoning = parse_llm_judge_response(response)
            except Exception as exc:
                print(
                    f"[Evaluation SKIP] llm_judge failed at sample_pos={i}, "
                    f"result_index={results_df.index[i]}: {type(exc).__name__}: {exc}"
                )
                judgment, score, reasoning = "SKIPPED", np.nan, "Skipped due to LLM judge error."

            record["llm_judgment"] = judgment
            record["llm_score"] = score
            record["llm_reasoning"] = reasoning
        if use_llm_judge_binary:
            try:
                binary_prompt = _build_llm_judge_binary_prompt(true, pred_ct)
                binary_response = complete_with_retry(
                    judge_backend,
                    binary_prompt,
                    system_message=_LLM_JUDGE_BINARY_SYSTEM,
                    usage_sink=usage_sink,
                    complete_kwargs=judge_binary_complete_kwargs,
                    response_validator=_validate_llm_judge_binary_output_strict,
                    usage_context={
                        "step": "llm_judge_binary",
                        "phase": "evaluation",
                        "sample_pos": i,
                        "result_index": results_df.index[i],
                    },
                )
                binary_judgment, binary_score = parse_llm_judge_binary_response(binary_response)
            except Exception as exc:
                print(
                    f"[Evaluation SKIP] llm_judge_binary failed at sample_pos={i}, "
                    f"result_index={results_df.index[i]}: {type(exc).__name__}: {exc}"
                )
                binary_judgment, binary_score = "SKIPPED", np.nan

            record["llm_binary_judgment"] = binary_judgment
            record["llm_binary"] = binary_score

        return i, record

    records_by_pos: list[dict[str, Any] | None] = [None] * len(y_true)
    if max_workers == 1 or not use_any_llm_judge:
        for i, (true, pred_raw) in enumerate(
            tqdm(zip(y_true, y_pred_raw), total=len(y_true), desc="Evaluating samples")
        ):
            row_pos, record = _evaluate_one(i, true, pred_raw)
            records_by_pos[row_pos] = record
    else:
        rows = list(enumerate(zip(y_true, y_pred_raw)))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(_evaluate_one, i, true, pred_raw): i
                for i, (true, pred_raw) in rows
            }
            progress = tqdm(total=len(rows), desc="Evaluating samples", leave=True)
            try:
                for future in as_completed(futures):
                    row_pos, record = future.result()
                    records_by_pos[row_pos] = record
                    progress.update(1)
            finally:
                progress.close()

    for record in records_by_pos:
        if record is None:
            raise RuntimeError("Evaluation produced an incomplete result set.")
        if use_exact:
            acc_flags.append(int(record["acc"]))
        if use_keyword:
            keyword_flags.append(int(record["keyword"]))
        if use_hierarchy:
            hierarchy_depths.append(int(record["hierarchy_depth"]))
        if use_llm_judge:
            llm_judgments.append(str(record["llm_judgment"]))
            llm_scores.append(record["llm_score"])
            llm_reasonings.append(str(record["llm_reasoning"]))
        if use_llm_judge_binary:
            llm_binary_judgments.append(str(record["llm_binary_judgment"]))
            llm_binary_scores.append(record["llm_binary"])

    data: dict[str, list] = {}
    if use_exact:
        data["acc"] = acc_flags
    if use_keyword:
        data["keyword"] = keyword_flags
    if use_hierarchy:
        data["hierarchy_depth"] = hierarchy_depths
    if use_llm_judge:
        data["llm_judgment"] = llm_judgments
        data["llm_score"] = llm_scores
        data["llm_reasoning"] = llm_reasonings
    if use_llm_judge_binary:
        data["llm_binary_judgment"] = llm_binary_judgments
        data["llm_binary"] = llm_binary_scores

    return pd.DataFrame(data, index=results_df.index)


def format_eval_report(eval_df: pd.DataFrame) -> str:
    """Render a one-row ``evaluate_all`` result as a compact, readable report.

    Groups each base metric with its bootstrap ``_std``/``_ci_low``/``_ci_high``
    columns (if present) into a single ``value ± std [ci_low, ci_high]`` line,
    instead of printing everything as one wide, hard-to-read table.
    """
    row = eval_df.iloc[0].to_dict()
    suffixes = ("_std", "_ci_low", "_ci_high")
    base_keys = [k for k in row if not k.endswith(suffixes)]
    if not base_keys:
        return eval_df.to_string(index=False)

    label_width = max(len(k) for k in base_keys)
    lines = []
    for key in base_keys:
        value = row[key]
        line = f"{key:<{label_width}} : {value:.4f}" if isinstance(value, float) else f"{key:<{label_width}} : {value}"
        std = row.get(f"{key}_std")
        ci_low = row.get(f"{key}_ci_low")
        ci_high = row.get(f"{key}_ci_high")
        if std is not None and ci_low is not None and ci_high is not None:
            line += f"  ± {std:.4f}  [95% CI: {ci_low:.4f}, {ci_high:.4f}]"
        lines.append(line)
    return "\n".join(lines)
