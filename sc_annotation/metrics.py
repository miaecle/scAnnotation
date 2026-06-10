"""Evaluation metrics for cell type annotation results."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

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
    return correct / len(y_true) if y_true else 0.0


_LLM_JUDGE_SYSTEM = (
    "You are evaluating single-cell annotation results. "
    "Decide whether a predicted cell type is semantically equivalent to the "
    "true cell type. Answer ONLY with 'yes' or 'no', nothing else."
)

_LLM_JUDGE_TEMPLATE = (
    "True cell type: {true}\n"
    "Predicted cell type: {pred}\n"
    "Are these the same cell type (allowing for minor naming differences)? "
    "Answer yes or no."
)


def llm_judge_accuracy(
    y_true: list[str],
    y_pred: list[str],
    backend: "LLMBackend",
    auto_extract: bool = True,
) -> float:
    """LLM-as-judge accuracy.

    Uses the provided backend to decide, for each (true, pred) pair, whether
    the prediction is semantically correct.  The LLM is prompted to answer
    ``yes`` or ``no`` only.

    Args:
        y_true: Ground-truth cell type labels.
        y_pred: Predicted labels (raw LLM responses or extracted cell types).
        backend: :class:`~sc_annotation.backends.base.LLMBackend` instance used
                 as the judge.
        auto_extract: If True, extract first line from each ``y_pred`` entry.

    Returns:
        Fraction of pairs judged as correct, in [0, 1].
    """
    correct = 0
    for true, pred in zip(y_true, y_pred):
        pred_ct = extract_cell_type(pred) if auto_extract else pred
        prompt = _LLM_JUDGE_TEMPLATE.format(true=true, pred=pred_ct)
        response = backend.complete(prompt, system_message=_LLM_JUDGE_SYSTEM)
        if response.strip().lower().startswith("yes"):
            correct += 1
    return correct / len(y_true) if y_true else 0.0


def evaluate_all(
    results_df: pd.DataFrame,
    true_col: str = "true_label",
    pred_col: str = "pred_label",
    judge_backend: "LLMBackend | None" = None,
) -> pd.DataFrame:
    """Run all available evaluation strategies and return a summary DataFrame.

    Strategies computed:
    - ``exact``   : exact string match (case-insensitive, after extracting first line)
    - ``keyword`` : keyword overlap match
    - ``llm``     : LLM-as-judge (only if ``judge_backend`` is provided)

    Args:
        results_df: DataFrame with true and predicted label columns.
        true_col: Column name for ground-truth labels.
        pred_col: Column name for raw LLM responses.
        judge_backend: Optional backend for LLM-judge evaluation.

    Returns:
        Single-row DataFrame with columns for each strategy's accuracy.
    """
    y_true = results_df[true_col].tolist()
    y_pred_raw = results_df[pred_col].tolist()
    y_pred_ct = [extract_cell_type(p) for p in y_pred_raw]

    records: dict[str, float] = {
        "exact": accuracy(y_true, y_pred_ct, case_sensitive=False),
        "keyword": keyword_accuracy(y_true, y_pred_raw, auto_extract=True),
    }

    if judge_backend is not None:
        records["llm_judge"] = llm_judge_accuracy(
            y_true, y_pred_raw, backend=judge_backend, auto_extract=True
        )

    return pd.DataFrame([records])
