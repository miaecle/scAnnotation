"""End-to-end experiment pipeline driven by :class:`~sc_annotation.config.ExperimentConfig`.

Typical usage::

    from sc_annotation.config import ExperimentConfig
    from sc_annotation.pipeline import run_experiment
    from sc_annotation.data import load_dataset

    config = ExperimentConfig.from_yaml('configs/pbmc_l1_zscore_gemini.yaml')
    adata  = load_dataset(config.dataset_path)
    results = run_experiment(adata, config)
"""

from __future__ import annotations

from dataclasses import replace
from datetime import datetime
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import json
import os
import threading
import time
from typing import Any, Optional

import numpy as np
import pandas as pd
import anndata as ad
from tqdm.auto import tqdm

from .config import ExperimentConfig
from .global_metrics import compute_global_metrics
from .filtering import annotate_genes, build_gene_mask
from .selection import (
    compute_scores, select_genes, select_by_marker_panel, MarkerPanel,
)
from .smoothing import build_knn_index, get_knn_indices, compute_pseudobulk
from .prompts import (
    SYSTEM_PROMPT, build_naive_prompt, build_enriched_prompt,
    build_marker_panel_prompt,
)
from .data import inspect_cells, sample_cells
from .adt import build_adt_adata, normalize_adt, get_top_proteins as get_top_proteins_adt
from .metrics import (
    parse_results, evaluate_all, evaluate_per_sample,
    extract_cell_type, extract_rationale,
)
from .visualization import save_confusion_matrix
from .backends.base import LLMBackend, complete_with_retry
from .pretty_reports import save_inspect_pretty, save_stage2_program_cache_pretty
from .stage2 import (
    make_gemini_json_caller,
    make_openai_json_caller,
    query_subtype_programs,
    filter_programs_to_panel,
    score_gene_programs,
    build_stage2_prompt,
)


# ---------------------------------------------------------------------------
# Backend factory
# ---------------------------------------------------------------------------

def build_backend(llm_config) -> LLMBackend:
    """Instantiate an :class:`~sc_annotation.backends.base.LLMBackend` from an
    :class:`~sc_annotation.config.LLMConfig`."""
    api_key: Optional[str] = None
    if llm_config.api_key_env:
        api_key = os.environ.get(llm_config.api_key_env)

    b = llm_config.backend.lower()
    if b == "gemini":
        from .backends.gemini import GeminiBackend
        return GeminiBackend(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_tokens=llm_config.max_tokens,
            api_key=api_key,
            use_context_cache=llm_config.use_context_cache,
            context_cache_ttl_seconds=llm_config.context_cache_ttl_seconds,
        )
    if b == "claude":
        from .backends.claude import ClaudeBackend
        return ClaudeBackend(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_tokens=llm_config.max_tokens,
            api_key=api_key,
        )
    if b == "openai":
        from .backends.openai import OpenAIBackend
        return OpenAIBackend(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_tokens=llm_config.max_tokens,
            api_key=api_key,
        )
    if b == "deepseek":
        from .backends.deepseek import DeepSeekBackend
        return DeepSeekBackend(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_tokens=llm_config.max_tokens,
            api_key=api_key,
        )
    if b == "openrouter":
        from .backends.openrouter import OpenRouterBackend
        return OpenRouterBackend(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_tokens=llm_config.max_tokens,
            api_key=api_key,
        )
    raise ValueError(f"Unknown backend: {llm_config.backend!r}. Choose gemini | claude | openai | deepseek | openrouter.")


# ---------------------------------------------------------------------------
# Global metrics guard
# ---------------------------------------------------------------------------

_REQUIRED_METRIC_COLS = frozenset(["mean_expr", "std_expr", "pct_cells", "idf",
                                    "is_low_expr", "is_hvg"])
_REQUIRED_FLAG_COLS = frozenset(["is_mt", "is_ribo", "is_hb", "is_tcr_vdj", "is_sex_chr"])


def ensure_global_metrics(adata: ad.AnnData, gm_config) -> None:
    """Run gene annotation and global metrics if not already present."""
    if not _REQUIRED_FLAG_COLS.issubset(set(adata.var.columns)):
        print("Annotating genes …")
        annotate_genes(adata)

    if not _REQUIRED_METRIC_COLS.issubset(set(adata.var.columns)):
        print("Computing global metrics (first time only) …")
        t0 = time.time()
        compute_global_metrics(
            adata,
            n_top_hvg=gm_config.n_top_hvg,
            min_cells_pct=gm_config.min_cells_pct,
            compute_gini=gm_config.compute_gini,
            gini_scope=gm_config.gini_scope,
            inplace=True,
        )
        print(f"  Done in {time.time() - t0:.1f}s  |  var cols: {list(adata.var.columns)}")


# ---------------------------------------------------------------------------
# Per-cell gene selection
# ---------------------------------------------------------------------------

def _build_stage2_skip_record(
    cell_idx: int,
    cell_barcode: str,
    true_label: str,
    stage1_label: str,
    stage1_reasoning: Optional[str],
    stage1_response: str,
    stage1_prompt: str,
    tissue: str,
    n_genes: int,
    exc: Exception,
) -> dict[str, Any]:
    """Build a record for a cell that failed stage-2 processing.
    
    Reconstructs the complete stage-2 prompt (prefix + prompt) for logging.
    """
    cached_user_prefix = (
        f"This annotation may have minor inaccuracies, or may have been confused with a neighboring type.\n\n"
        f"Return a JSON object with gene programs for:\n"
        f"  1. The fine-grained subtypes of this cell type commonly found in {tissue}.\n"
        f"  2. The most commonly confused neighboring cell types in {tissue}.\n\n"
        f"Each key is a subtype/cell-type name; each value contains:\n"
        f'  "genes": list anywhere from 20 to {n_genes} genes most specifically UPREGULATED in that '
        f"subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)\n"
        f'  "description": one-sentence biological description\n\n'
        f"Include 3-5 subtypes total. Focus on subtypes commonly found in {tissue}.\n"
        f"Return only the JSON."
    )
    stage2_prompt = (
        f'A single cell in {tissue} was annotated in a first pass as: "{stage1_label}"\n'
    )
    full_stage2_prompt = f"{cached_user_prefix}\n\n{stage2_prompt}"
    
    return {
        "cell_idx": int(cell_idx),
        "cell_barcode": str(cell_barcode),
        "true_label": str(true_label),
        "stage1_label": stage1_label,
        "stage1_reasoning": stage1_reasoning,
        "stage1_response": stage1_response,
        "stage1_prompt": stage1_prompt,
        "stage2_prefix": cached_user_prefix,
        "stage2_prompt": stage2_prompt,
        "stage2_full_prompt": full_stage2_prompt,
        "error_type": type(exc).__name__,
        "error_message": str(exc),
    }


def _resolve_cell_indices(
    adata: ad.AnnData,
    cell_idx: int,
    input_cfg,
    neighbor_matrix: Optional[np.ndarray],
    label_to_indices: Optional[dict],
    label_col: str,
) -> list[int]:
    """Return the list of cell indices to aggregate for scoring.

    - ``single_cell``: just ``[cell_idx]``
    - ``knn_smoothed``: cell + its k nearest neighbours
    - ``pseudobulk``: all cells sharing the same true label
    """
    mode = input_cfg.mode
    if mode == "single_cell":
        return [cell_idx]

    if mode == "knn_smoothed":
        if neighbor_matrix is None:
            raise RuntimeError("neighbor_matrix required for knn_smoothed mode.")
        return get_knn_indices(cell_idx, neighbor_matrix, k=input_cfg.knn_k)

    if mode == "pseudobulk":
        if label_to_indices is None:
            raise RuntimeError("label_to_indices required for pseudobulk mode.")
        true_label = adata.obs[label_col].iloc[cell_idx]
        return label_to_indices.get(true_label, [cell_idx])

    raise ValueError(f"Unknown input mode: {mode!r}")


def _select_genes(
    adata: ad.AnnData,
    cell_indices: list[int],
    sel_cfg,
    gene_mask: np.ndarray,
    marker_panel: Optional[MarkerPanel],
) -> dict:
    """Compute scores then select top genes for one cell or group."""
    s = sel_cfg.strategy
    n = sel_cfg.n_top

    if s == "combined":
        scores_expr = compute_scores(adata, cell_indices, "expr", gene_mask)
        scores_z = compute_scores(adata, cell_indices, "zscore", gene_mask)
        primary = select_genes(scores_expr, n)
        secondary = select_genes(scores_z, sel_cfg.n_top_secondary)
        return {"primary": primary, "secondary": secondary,
                "pos_markers": [], "neg_markers": []}

    if s == "marker_panel":
        scores = compute_scores(adata, cell_indices, "expr", gene_mask)
        primary = select_genes(scores, n)
        pos_markers, neg_markers = select_by_marker_panel(
            adata, cell_indices, marker_panel, gene_mask,
        ) if marker_panel is not None else ([], [])
        return {"primary": primary, "secondary": [],
                "pos_markers": pos_markers, "neg_markers": neg_markers}

    scores = compute_scores(adata, cell_indices, s, gene_mask)
    primary = select_genes(scores, n)
    return {"primary": primary, "secondary": [],
            "pos_markers": [], "neg_markers": []}


def _build_prompt(gene_sel: dict, sel_cfg, proteins: list, tissue: Optional[str], cell_type_list: Optional[list] = None) -> str:
    """Dispatch to the correct prompt builder based on selection strategy."""
    s = sel_cfg.strategy
    if s == "combined":
        return build_enriched_prompt(
            genes_by_expr=gene_sel["primary"],
            genes_by_zscore=gene_sel["secondary"],
            proteins=proteins,
            tissue=tissue,
            cell_type_list=cell_type_list,
        )
    if s == "marker_panel":
        return build_marker_panel_prompt(
            pos_expressed=gene_sel["pos_markers"],
            neg_expressed=gene_sel["neg_markers"],
            top_genes=gene_sel["primary"],
            proteins=proteins,
            tissue=tissue,
            cell_type_list=cell_type_list,
        )
    # expr / zscore / tfidf / de — single ranked list
    return build_naive_prompt(
        genes=gene_sel["primary"],
        proteins=proteins,
        tissue=tissue,
        cell_type_list=cell_type_list,
    )


def _complete_with_list_constraint(
    backend: LLMBackend,
    prompt: str,
    system_message: str,
    cell_type_list: list,
    usage_sink,
    usage_context: dict,
    max_constraint_retries: int = 3,
) -> str:
    """Call the LLM and retry if the returned cell type is not in cell_type_list.

    Each retry appends a correction message reminding the model to pick from
    the provided list.
    """
    correction_suffix = (
        "\n\nYour previous answer was not one of the allowed cell types. "
        "You MUST choose exactly one name from the list provided. "
        "Respond again with the correct cell type name in the first line."
    )
    current_prompt = prompt
    for attempt in range(max_constraint_retries + 1):
        response = complete_with_retry(
            backend,
            current_prompt,
            system_message=system_message,
            usage_sink=usage_sink,
            usage_context=usage_context,
        )
        predicted = extract_cell_type(response)
        if any(predicted.strip().lower() == ct.strip().lower() for ct in cell_type_list):
            return response
        if attempt < max_constraint_retries:
            print(
                f"  [constraint retry {attempt + 1}/{max_constraint_retries}] "
                f'Response "{predicted}" not in cell type list — retrying.'
            )
            current_prompt = prompt + correction_suffix
        else:
            print(
                f'  [constraint retry] Giving up after {max_constraint_retries} retries; '
                f'keeping last response "{predicted}".'
            )
    return response


def _build_stage2_gene_lists(
    adata: ad.AnnData,
    cell_indices: list[int],
    gene_mask: np.ndarray,
    n_top: int,
    mode: str,
    strategy: str,
) -> tuple[list[tuple[str, float]], list[tuple[str, float]], list[tuple[str, float]]]:
    """Build the expr / zscore / tfidf lists used by stage-2 prompting."""
    if mode == "combined":
        genes_by_expr = select_genes(compute_scores(adata, cell_indices, "expr", gene_mask), n_top)
        genes_by_zscore = select_genes(compute_scores(adata, cell_indices, "zscore", gene_mask), n_top)
        genes_by_tfidf = select_genes(compute_scores(adata, cell_indices, "tfidf", gene_mask), n_top)
        return genes_by_expr, genes_by_zscore, genes_by_tfidf
    elif mode == "strict":
        if strategy == "expr":
            genes_by_expr = select_genes(compute_scores(adata, cell_indices, "expr", gene_mask), n_top)
            return genes_by_expr, [], []
        elif strategy == "zscore":
            genes_by_zscore = select_genes(compute_scores(adata, cell_indices, "zscore", gene_mask), n_top)
            return [], genes_by_zscore, []
        elif strategy == "tfidf":
            genes_by_tfidf = select_genes(compute_scores(adata, cell_indices, "tfidf", gene_mask), n_top)
            return [], [], genes_by_tfidf
    else:
        raise ValueError(f"Unknown stage-2 mode: {mode!r}. Choose 'combined' or 'strict'.")            


# ---------------------------------------------------------------------------
# Main experiment runner
# ---------------------------------------------------------------------------

def run_experiment(
    adata: ad.AnnData,
    config: ExperimentConfig,
    backend: Optional[LLMBackend] = None,
) -> pd.DataFrame:
    """Run a complete annotation experiment from an :class:`~sc_annotation.config.ExperimentConfig`.

    Steps:

    1. Compute global metrics (skipped if already present).
    2. Build the gene inclusion mask from ``config.filter``.
    3. Optionally compute kNN index or pseudobulk (``config.input.mode``).
    4. Sample cells (``config.evaluation``).
    5. For each cell: get expression vector → select genes → build prompt → call LLM.
    6. Optionally refine with stage-2 (``config.stage2.enabled``).
    7. Evaluate with all configured strategies.
    8. Save results + config snapshot to ``config.output.results_dir``.

    Args:
        adata: AnnData object.  Global metrics are added in-place if missing.
        config: Experiment configuration.
        backend: Pre-built LLM backend.  Built from ``config.llm`` if None.

    Returns:
        Results DataFrame with columns:
        ``cell_idx``, ``cell_barcode``, ``true_label``,
        ``pred_label``, ``pred_celltype``, ``pred_rationale``,
        plus per-sample eval columns such as ``acc`` / ``keyword`` and optional
        LLM judge outputs.
    """
    print(f"\n{'='*60}")
    print(f"Experiment: {config.output.experiment_name}")
    print(config.summary())
    print("="*60)
    
    # Record start time
    start_time = time.time()
    start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Start time: {start_time_str}")

    # ------------------------------------------------------------------ #
    # 0. Backend
    # ------------------------------------------------------------------ #
    if backend is None:
        backend = build_backend(config.llm)
    print(f"Backend: {backend}")
    usage_lock = threading.Lock()

    usage_attempts_path = os.path.join(
        config.output.results_dir,
        "logs",
        f"{config.output.experiment_name}_usage_attempts.jsonl",
    )

    def _usage_sink(record: dict[str, Any]) -> None:
        """Write one usage-attempt record immediately (thread-safe, append-only)."""
        if not config.output.save_results:
            return
        payload = dict(record)
        payload.setdefault("recorded_at_unix", time.time())
        with usage_lock:
            os.makedirs(os.path.dirname(usage_attempts_path), exist_ok=True)
            with open(usage_attempts_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(payload, ensure_ascii=False) + "\n")

    stage2_backend: Optional[LLMBackend] = None
    json_caller = None
    if config.stage2.enabled:
        stage2_llm = replace(
            config.llm,
            model=config.stage2.model or config.llm.model,
            temperature=config.stage2.temperature,
            max_tokens=config.stage2.max_tokens,
        )
        stage2_backend = build_backend(stage2_llm)

        api_key = os.environ.get(config.llm.api_key_env) if config.llm.api_key_env else None
        stage2_backend_name = stage2_llm.backend.lower()
        if stage2_backend_name == "gemini":
            json_caller = make_gemini_json_caller(
                model=stage2_llm.model,
                api_key=api_key,
                max_output_tokens=config.stage2.program_query_max_output_tokens,
                thinking_budget=config.stage2.program_query_thinking_budget,
                use_context_cache=stage2_llm.use_context_cache,
                context_cache_ttl_seconds=stage2_llm.context_cache_ttl_seconds,
                usage_sink=_usage_sink,
            )
        elif stage2_backend_name in ("openai", "deepseek", "openrouter"):
            if stage2_backend_name == "deepseek":
                base_url = "https://api.deepseek.com"
            elif stage2_backend_name == "openrouter":
                base_url = "https://openrouter.ai/api/v1"
            else:
                base_url = None
            json_caller = make_openai_json_caller(
                model=stage2_llm.model,
                api_key=api_key,
                base_url=base_url,
                max_output_tokens=config.stage2.program_query_max_output_tokens,
                usage_sink=_usage_sink,
            )
        else:
            raise ValueError(
                f"Stage-2 JSON querying is not supported for backend {config.llm.backend!r}. "
                "Choose gemini, openai, deepseek, or openrouter."
            )
        print(f"Stage-2: enabled (model={stage2_llm.model}, score={config.stage2.score_method})")
        if stage2_backend is None or json_caller is None:
            raise RuntimeError("Stage-2 backend initialization failed.")
        print(f"Stage-2 backend: {stage2_backend}")
        print(f"Stage-2 JSON caller: {json_caller}")
        print(f"======Stage-2 initialization completed======")
    else:
        print(f"Stage-2: disabled")

    inspect_enabled = bool(getattr(config.inspect, "enabled", False))
    inspect_cell_list: list[int] = []
    inspect_cell_set: set[int] = set()
    inspect_records: list[dict[str, Any]] = []
    inspect_lock = threading.Lock()
    inspect_path = (
        config.inspect.save_path
        if getattr(config.inspect, "save_path", None)
        else os.path.join(
            config.output.results_dir,
            "logs",
            f"{config.output.experiment_name}_inspect.jsonl",
        )
    )
    if inspect_enabled:
        try:
            inspect_cell_list = [int(idx) for idx in getattr(config.inspect, "cell_indices", [])]
            inspect_cell_set = set(inspect_cell_list)
        except Exception as exc:
            raise ValueError(
                "inspect.cell_indices must be a list of integers (global cell_idx values)."
            ) from exc
        print(
            f"Inspect mode: enabled (tracking {len(inspect_cell_set)} cell_idx values)"
        )
    else:
        print("Inspect mode: disabled")

    def _inspect_enabled_for_cell(cell_idx: int) -> bool:
        return inspect_enabled and (cell_idx in inspect_cell_set)

    def _append_inspect(record: dict[str, Any]) -> None:
        with inspect_lock:
            inspect_records.append(dict(record))

    def _sorted_inspect_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Return inspect records in a deterministic read-friendly order."""
        stage_order = {
            "stage1_annotation": 0,
            "stage2_program_query": 1,
            "stage2_program_query_error": 2,
            "stage2_refinement": 3,
        }

        def _key(r: dict[str, Any]) -> tuple[int, int, int, int, str]:
            row_idx = r.get("row_idx")
            row_key = int(row_idx) if isinstance(row_idx, (int, np.integer)) else 10**9
            stage = str(r.get("stage", ""))
            stage_key = stage_order.get(stage, 999)
            cell_idx = r.get("cell_idx")
            cell_key = int(cell_idx) if isinstance(cell_idx, (int, np.integer)) else 10**9
            return row_key, stage_key, cell_key, len(stage), stage

        return sorted(records, key=_key)

    # ------------------------------------------------------------------ #
    # 1. Global metrics
    # ------------------------------------------------------------------ #
    ensure_global_metrics(adata, config.global_metrics)

    # ------------------------------------------------------------------ #
    # 2. Gene mask
    # ------------------------------------------------------------------ #
    gene_mask = build_gene_mask(adata, config.filter)
    n_included = int(gene_mask.sum())
    print(f"Gene mask: {n_included}/{adata.n_vars} genes included")

    # ------------------------------------------------------------------ #
    # 3. Marker panel (optional)
    # ------------------------------------------------------------------ #
    marker_panel: Optional[MarkerPanel] = None
    if config.selection.marker_panel_path:
        marker_panel = MarkerPanel.from_yaml(config.selection.marker_panel_path)
        print(f"Marker panel: {len(marker_panel.positive)} positive, {len(marker_panel.negative)} negative genes")

    # ------------------------------------------------------------------ #
    # 4. ADT / protein data (optional)
    # ------------------------------------------------------------------ #
    adt_adata: Optional[ad.AnnData] = None
    if "adt" in config.selection.modalities:
        try:
            adt_adata = build_adt_adata(adata)
            normalize_adt(adt_adata, method="clr", inplace=True)
            print(f"ADT: {adt_adata.n_vars} proteins, CLR-normalized")
        except KeyError as e:
            print(f"ADT skipped — {e}")
            adt_adata = None

    # ------------------------------------------------------------------ #
    # 5. Input mode setup
    # ------------------------------------------------------------------ #
    neighbor_matrix: Optional[np.ndarray] = None
    label_to_indices: Optional[dict] = None

    if config.input.mode == "knn_smoothed":
        k = config.input.knn_k
        print(f"Building kNN index (k={k}) …")
        t0 = time.time()
        neighbor_matrix = build_knn_index(
            adata, k=k, use_rep=config.input.knn_use_rep, inplace=True,
        )
        print(f"  Done in {time.time()-t0:.1f}s")

    elif config.input.mode == "pseudobulk":
        print("Computing pseudobulk index …")
        label_to_indices = compute_pseudobulk(adata, config.evaluation.label_col)
        print(f"  {len(label_to_indices)} cell-type groups indexed")

    # ------------------------------------------------------------------ #
    # 6. Sample cells
    # ------------------------------------------------------------------ #
    name = config.output.experiment_name
    tables_dir = os.path.join(config.output.results_dir, "tables")
    logs_dir = os.path.join(config.output.results_dir, "logs")
    plots_dir = os.path.join(config.output.results_dir, "plots")
    stage2_dir = os.path.join(config.output.results_dir, "stage2")
    meta_dir = os.path.join(config.output.results_dir, "meta")
    tmp_dir = os.path.join(config.output.results_dir, "tmp")

    results_path = os.path.join(tables_dir, f"{name}_results.csv")
    eval_path = os.path.join(tables_dir, f"{name}_eval.csv")
    usage_path = os.path.join(logs_dir, f"{name}_llm_usage.csv")
    usage_failures_path = os.path.join(logs_dir, f"{name}_llm_usage_failures.csv")
    usage_summary_path = os.path.join(logs_dir, f"{name}_llm_usage_summary.csv")

    config_path = os.path.join(meta_dir, f"{name}_config.yaml")
    timing_path = os.path.join(meta_dir, f"{name}_timing.csv")

    cm_path = os.path.join(plots_dir, f"{name}_confusion_matrix.png")
    skipped_path = os.path.join(stage2_dir, f"{name}_stage2_skipped.csv")
    stage2_program_cache_path = os.path.join(stage2_dir, f"{name}_stage2_program_cache.json")

    checkpoint_every = 10
    annotation_stream_path: Optional[str] = None
    annotation_buffer: list[dict[str, Any]] = []
    annotation_chunks: list[pd.DataFrame] = []
    resume_from_idx = 0
    flushed_count = 0

    if config.output.save_results:
        os.makedirs(config.output.results_dir, exist_ok=True)
        for d in (tables_dir, logs_dir, plots_dir, stage2_dir, meta_dir, tmp_dir):
            os.makedirs(d, exist_ok=True)
        annotation_stream_path = os.path.join(tmp_dir, f"{name}_annotation_stream.csv")

    def _flush_usage_records(force: bool = False) -> None:
        # Usage attempts are written synchronously in _usage_sink.
        _ = force
        return

    def _flush_annotation_buffer(force: bool = False) -> None:
        nonlocal annotation_buffer, flushed_count
        if not annotation_buffer:
            return
        if (not force) and len(annotation_buffer) < checkpoint_every:
            return

        chunk_df = pd.DataFrame(annotation_buffer)
        if annotation_stream_path is not None:
            write_header = not os.path.exists(annotation_stream_path)
            chunk_df.to_csv(
                annotation_stream_path,
                mode="a",
                header=write_header,
                index=False,
            )
        else:
            annotation_chunks.append(chunk_df)

        flushed_count += len(annotation_buffer)
        print(f"  Checkpoint saved: {flushed_count} annotated cells")
        annotation_buffer = []
        _flush_usage_records(force=True)

    cell_type_list = []
    if inspect_enabled:
        sample_df = inspect_cells(
            adata,
            label_col=config.evaluation.label_col,
            cell_indices=inspect_cell_list,
            cell_type_list=cell_type_list,
        )
        print(
            "Inspect mode sample override applied: "
            f"{len(sample_df)} cells extracted directly from adata.obs using inspect.cell_indices."
        )
    else:
        effective_n_per_class = config.evaluation.n_per_class
        if config.input.mode == "pseudobulk":
            if effective_n_per_class != 1:
                print(
                    "Input mode is pseudobulk; overriding "
                    f"evaluation.n_per_class={effective_n_per_class} to 1."
                )
            effective_n_per_class = 1

        sample_df = sample_cells(
            adata,
            label_col=config.evaluation.label_col,
            n_per_class=effective_n_per_class,
            seed=config.evaluation.seed,
            cell_type_list=cell_type_list
        )

    if annotation_stream_path is not None and os.path.exists(annotation_stream_path):
        try:
            prev_stream_df = pd.read_csv(annotation_stream_path)
            if "pred_label" in prev_stream_df.columns:
                max_check = min(len(sample_df), len(prev_stream_df))
                for i in tqdm(range(max_check), desc="resuming from existing annotations", unit="cell"):
                    cur = sample_df.iloc[i]
                    old = prev_stream_df.iloc[i]

                    same_cell_idx = str(cur.get("cell_idx", "")) == str(old.get("cell_idx", ""))
                    same_barcode = str(cur.get("cell_barcode", "")) == str(old.get("cell_barcode", ""))
                    same_true = str(cur.get("true_label", "")) == str(old.get("true_label", ""))
                    has_pred = pd.notna(old.get("pred_label")) and str(old.get("pred_label", "")).strip() != ""

                    if same_cell_idx and same_barcode and same_true and has_pred:
                        resume_from_idx += 1
                    else:
                        print(
                            f"  [annotation stream mismatch at row {i}] cur: {cur}, old: {old}"
                        )
                        # Only a contiguous matched prefix is resumable.
                        break

                flushed_count = resume_from_idx
                if resume_from_idx < len(prev_stream_df):
                    if resume_from_idx > 0:
                        prev_stream_df.iloc[:resume_from_idx].to_csv(annotation_stream_path, index=False)
                    else:
                        os.remove(annotation_stream_path)
                    print(
                        f"Found stale rows in annotation stream; truncated to {resume_from_idx} completed cells."
                    )

                if resume_from_idx > 0:
                    print(
                        f"Resuming annotation from existing stream: "
                        f"{resume_from_idx}/{len(sample_df)} cells already completed."
                    )
        except Exception as exc:
            print(f"Annotation stream resume check skipped: {type(exc).__name__}: {exc}")

    n_types = sample_df["true_label"].nunique()
    print(f"Sampled {len(sample_df)} cells from {n_types} cell types")

    #------------------------------------------------------------------ #
    # Stage-2 program cache
    #------------------------------------------------------------------ #

    stage2_program_cache: dict[str, dict[str, Any]] = {}
    stage2_program_cache_lock = threading.Lock()

    def _normalize_stage2_cache_key(label: str) -> str:
        # Normalize whitespace/case so equivalent labels share one cache entry.
        return " ".join(str(label).strip().split()).lower()

    if config.stage2.enabled:
        unique_cell_types: list[str] = []
        seen_cache_keys: set[str] = set()
        for cell_type in cell_type_list:
            cache_key = _normalize_stage2_cache_key(cell_type)
            if cache_key and cache_key not in seen_cache_keys:
                seen_cache_keys.add(cache_key)
                unique_cell_types.append(str(cell_type))

        if unique_cell_types:
            print(
                "Precomputing stage-2 gene programs once per cell type "
                f"({len(unique_cell_types)} total) ..."
            )
            for cell_type in tqdm(unique_cell_types, desc="stage2 program precompute", unit="cell_type"):
                cache_key = _normalize_stage2_cache_key(cell_type)
                if not cache_key:
                    continue
                try:
                    raw_programs = query_subtype_programs(
                        cell_type,
                        json_caller,
                        tissue=config.tissue or "PBMC",
                        n_genes=config.stage2.n_program_genes,
                        usage_sink=_usage_sink,
                        usage_context={
                            "step": "stage2_program_query",
                            "phase": "precompute",
                            "cell_idx": -1,
                            "cell_barcode": "<precompute>",
                            "stage1_label": str(cell_type),
                        },
                    )
                    with stage2_program_cache_lock:
                        stage2_program_cache[cache_key] = raw_programs
                except Exception as exc:
                    print(
                        "[Stage-2 precompute warning] "
                        f"label={cell_type!r}: {type(exc).__name__}: {exc}"
                    )

            print(
                "Stage-2 precompute complete: "
                f"{len(stage2_program_cache)}/{len(unique_cell_types)} cell types cached."
            )

            if config.output.save_results:
                with stage2_program_cache_lock:
                    stage2_cache_payload = {
                        "tissue": config.tissue or "PBMC",
                        "n_program_genes": int(config.stage2.n_program_genes),
                        "n_cached_cell_types": int(len(stage2_program_cache)),
                        "programs_by_cell_type": dict(sorted(stage2_program_cache.items())),
                    }
                with open(stage2_program_cache_path, "w", encoding="utf-8") as fh:
                    json.dump(stage2_cache_payload, fh, ensure_ascii=False, indent=2)
                print(f"Stage-2 precomputed programs saved → {stage2_program_cache_path}")
                save_stage2_program_cache_pretty(stage2_cache_payload, stage2_program_cache_path)

    # ------------------------------------------------------------------ #
    # 7. Annotate
    # ------------------------------------------------------------------ #
    stage2_skipped_records: list[dict[str, Any]] = []
    max_workers = max(1, int(getattr(config.llm, "concurrency", 1) or 1))
    print(f"Annotation concurrency: {max_workers}")

    def _annotate_one(row_idx: int, row) -> tuple[int, str, Optional[dict[str, Any]]]:
        cell_idx = row.cell_idx

        cell_indices = _resolve_cell_indices(
            adata, cell_idx, config.input,
            neighbor_matrix, label_to_indices, config.evaluation.label_col,
        )

        gene_sel = _select_genes(
            adata, cell_indices, config.selection,
            gene_mask, marker_panel,
        )

        proteins: list = []
        if adt_adata is not None:
            proteins = get_top_proteins_adt(adt_adata, cell_indices, n_top=20)

        prompt = _build_prompt(gene_sel, config.selection, proteins, config.tissue, cell_type_list)
        _stage1_usage_ctx = {
            "step": "stage1_annotation",
            "phase": "annotation",
            "cell_idx": int(cell_idx),
            "cell_barcode": str(row.cell_barcode),
        }
        if cell_type_list:
            stage1_response = _complete_with_list_constraint(
                backend, prompt, SYSTEM_PROMPT,
                cell_type_list, _usage_sink, _stage1_usage_ctx,
            )
        else:
            stage1_response = complete_with_retry(
                backend, prompt,
                system_message=SYSTEM_PROMPT,
                usage_sink=_usage_sink,
                usage_context=_stage1_usage_ctx,
            )

        if _inspect_enabled_for_cell(int(cell_idx)):
            _append_inspect(
                {
                    "stage": "stage1_annotation",
                    "row_idx": int(row_idx),
                    "cell_idx": int(cell_idx),
                    "cell_barcode": str(row.cell_barcode),
                    "true_label": str(row.true_label),
                    "prompt": prompt,
                    "output": stage1_response,
                }
            )

        final_response = stage1_response
        if config.stage2.enabled:
            stage1_label = extract_cell_type(stage1_response)
            stage1_reasoning = extract_rationale(stage1_response) or None
            stage2_cache_key = _normalize_stage2_cache_key(stage1_label)
            raw_programs: Optional[dict[str, Any]] = None
            with stage2_program_cache_lock:
                raw_programs = stage2_program_cache.get(stage2_cache_key)
            stage2_program_cache_hit = raw_programs is not None

            try:
                if raw_programs is None:
                    raw_programs = query_subtype_programs(
                        stage1_label,
                        json_caller,
                        tissue=config.tissue or "PBMC",
                        n_genes=config.stage2.n_program_genes,
                        usage_sink=_usage_sink,
                        usage_context={
                            "step": "stage2_program_query",
                            "phase": "annotation",
                            "cell_idx": int(cell_idx),
                            "cell_barcode": str(row.cell_barcode),
                            "stage1_label": str(stage1_label),
                        },
                    )
                    if stage2_cache_key:
                        with stage2_program_cache_lock:
                            stage2_program_cache.setdefault(stage2_cache_key, raw_programs)

                if _inspect_enabled_for_cell(int(cell_idx)):
                    stage2_program_prefix = (
                        f"This annotation may have minor inaccuracies, or may have been confused with a neighboring type.\n\n"
                        f"Return a JSON object with gene programs for:\n"
                        f"  1. The fine-grained subtypes of this cell type commonly found in {config.tissue or 'PBMC'}.\n"
                        f"  2. The most commonly confused neighboring cell types in {config.tissue or 'PBMC'}.\n\n"
                        f"Each key is a subtype/cell-type name; each value contains:\n"
                        f'  "genes": list anywhere from 20 to {config.stage2.n_program_genes} genes most specifically UPREGULATED in that '
                        f"subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)\n"
                        f'  "description": one-sentence biological description\n\n'
                        f"Include 3-5 subtypes total. Focus on subtypes commonly found in {config.tissue or 'PBMC'}.\n"
                        f"Return only the JSON."
                    )
                    stage2_program_prompt = (
                        f'A single cell in {config.tissue or "PBMC"} was annotated in a first pass as: "{stage1_label}"\n'
                    )
                    stage2_program_full_prompt = f"{stage2_program_prefix}\n\n{stage2_program_prompt}"
                    _append_inspect(
                        {
                            "stage": "stage2_program_query",
                            "row_idx": int(row_idx),
                            "cell_idx": int(cell_idx),
                            "cell_barcode": str(row.cell_barcode),
                            "true_label": str(row.true_label),
                            "stage1_label": stage1_label,
                            "stage1_reasoning": stage1_reasoning,
                            "program_cache_hit": stage2_program_cache_hit,
                            "prompt_prefix": stage2_program_prefix,
                            "prompt": stage2_program_prompt,
                            "full_prompt": stage2_program_full_prompt,
                            "output": raw_programs,
                        }
                    )
            except Exception as _stage2_exc:
                skip_record = _build_stage2_skip_record(
                    cell_idx=cell_idx,
                    cell_barcode=row.cell_barcode,
                    true_label=row.true_label,
                    stage1_label=stage1_label,
                    stage1_reasoning=stage1_reasoning,
                    stage1_response=stage1_response,
                    stage1_prompt=prompt,
                    tissue=config.tissue or "PBMC",
                    n_genes=config.stage2.n_program_genes,
                    exc=_stage2_exc,
                )
                print(
                    f"\n[Stage-2 SKIP] cell_idx={cell_idx}, barcode={row.cell_barcode}: "
                    f"{type(_stage2_exc).__name__}: {_stage2_exc}. "
                    f"Falling back to stage-1 response.\n"
                    f"Full Stage-2 prompt:\n{skip_record['stage2_full_prompt']}\n"
                )
                if _inspect_enabled_for_cell(int(cell_idx)):
                    _append_inspect(
                        {
                            "stage": "stage2_program_query_error",
                            "row_idx": int(row_idx),
                            "cell_idx": int(cell_idx),
                            "cell_barcode": str(row.cell_barcode),
                            "true_label": str(row.true_label),
                            "stage1_label": stage1_label,
                            "prompt_prefix": skip_record["stage2_prefix"],
                            "prompt": skip_record["stage2_prompt"],
                            "full_prompt": skip_record["stage2_full_prompt"],
                            "error_type": skip_record["error_type"],
                            "error_message": skip_record["error_message"],
                            "output": stage1_response,
                        }
                    )
                return row_idx, stage1_response, skip_record
            programs_in_data = filter_programs_to_panel(raw_programs, adata)
            pathway_scores = score_gene_programs(
                adata,
                cell_indices,
                programs_in_data,
                gene_mask,
                min_genes=config.stage2.score_min_genes,
                method=config.stage2.score_method,
                n_background=config.stage2.score_n_background,
                random_state=config.stage2.score_random_state,
            )
            genes_by_expr, genes_by_zscore, genes_by_tfidf = _build_stage2_gene_lists(
                adata, cell_indices, gene_mask, config.stage2.n_top_genes,
                mode=config.stage2.mode, strategy=config.selection.strategy
            )

            stage2_prompt = build_stage2_prompt(
                stage1_label,
                pathway_scores,
                stage1_reasoning=stage1_reasoning,
                genes_by_expr=genes_by_expr,
                genes_by_zscore=genes_by_zscore,
                genes_by_tfidf=genes_by_tfidf,
                proteins=proteins,
                tissue=config.tissue or "PBMC",
                n_genes=config.stage2.n_top_genes,
                n_proteins=config.stage2.n_top_proteins,
                cell_type_list=cell_type_list,
            )
            _stage2_usage_ctx = {
                "step": "stage2_refinement",
                "phase": "annotation",
                "cell_idx": int(cell_idx),
                "cell_barcode": str(row.cell_barcode),
            }
            if cell_type_list:
                final_response = _complete_with_list_constraint(
                    stage2_backend, stage2_prompt, SYSTEM_PROMPT,
                    cell_type_list, _usage_sink, _stage2_usage_ctx,
                )
            else:
                final_response = complete_with_retry(
                    stage2_backend, stage2_prompt,
                    system_message=SYSTEM_PROMPT,
                    usage_sink=_usage_sink,
                    usage_context=_stage2_usage_ctx,
                )
            if _inspect_enabled_for_cell(int(cell_idx)):
                _append_inspect(
                    {
                        "stage": "stage2_refinement",
                        "row_idx": int(row_idx),
                        "cell_idx": int(cell_idx),
                        "cell_barcode": str(row.cell_barcode),
                        "true_label": str(row.true_label),
                        "stage1_label": stage1_label,
                        "prompt": stage2_prompt,
                        "output": final_response,
                    }
                )

        return row_idx, final_response, None

    if max_workers == 1:
        total_to_annotate = max(0, len(sample_df) - resume_from_idx)
        rows = sample_df.iloc[resume_from_idx:].itertuples()
        for row_idx, row in enumerate(tqdm(rows, total=total_to_annotate, desc="Annotating"), start=resume_from_idx):
            _row_idx, response, skip_record = _annotate_one(row_idx, row)
            row_payload = sample_df.iloc[_row_idx].to_dict()
            row_payload["pred_label"] = response
            annotation_buffer.append(row_payload)
            _flush_annotation_buffer()
            if skip_record is not None:
                stage2_skipped_records.append(skip_record)
    else:
        total_to_annotate = max(0, len(sample_df) - resume_from_idx)
        max_pending_results = checkpoint_every * 5
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            next_submit_idx = resume_from_idx
            in_flight: dict[Any, int] = {}

            def _submit_next() -> bool:
                nonlocal next_submit_idx
                if next_submit_idx >= len(sample_df):
                    return False
                row = sample_df.iloc[next_submit_idx]
                future = executor.submit(_annotate_one, next_submit_idx, row)
                in_flight[future] = next_submit_idx
                next_submit_idx += 1
                return True

            pending_results: dict[int, tuple[str, Optional[dict[str, Any]]]] = {}
            next_write_idx = resume_from_idx
            while len(in_flight) < max_workers and _submit_next():
                pass

            progress = tqdm(total=total_to_annotate, desc="Annotating", leave=True)
            try:
                while in_flight:
                    done, _ = wait(set(in_flight.keys()), return_when=FIRST_COMPLETED)
                    for future in done:
                        in_flight.pop(future, None)
                        _row_idx, response, skip_record = future.result()
                        pending_results[_row_idx] = (response, skip_record)
                        progress.update(1)

                    # Flush only contiguous rows to keep checkpoint order stable.
                    while next_write_idx in pending_results:
                        _response, _skip_record = pending_results.pop(next_write_idx)
                        row_payload = sample_df.iloc[next_write_idx].to_dict()
                        row_payload["pred_label"] = _response
                        annotation_buffer.append(row_payload)
                        _flush_annotation_buffer()
                        if _skip_record is not None:
                            stage2_skipped_records.append(_skip_record)
                        next_write_idx += 1

                    # Backpressure: do not keep submitting when out-of-order buffer is full.
                    while (
                        len(in_flight) < max_workers
                        and len(pending_results) < max_pending_results
                        and _submit_next()
                    ):
                        pass
            finally:
                progress.close()

    _flush_annotation_buffer(force=True)
    _flush_usage_records(force=True)

    if annotation_stream_path is not None and os.path.exists(annotation_stream_path):
        results_df = pd.read_csv(annotation_stream_path)
    elif annotation_chunks:
        results_df = pd.concat(annotation_chunks, ignore_index=True)
    else:
        results_df = sample_df.copy()
        results_df["pred_label"] = ""

    results_df = parse_results(results_df)

    if config.output.save_results:
        results_df.to_csv(results_path, index=False)
        print(f"Annotation results saved → {results_path}")
        # Ensure evaluation consumes the persisted CSV instead of in-memory data.
        results_df = pd.read_csv(results_path)

    # ------------------------------------------------------------------ #
    # 8. Evaluate
    # ------------------------------------------------------------------ #
    judge_backend: Optional[LLMBackend] = None
    use_llm_judge = "llm_judge" in config.evaluation.strategies
    use_llm_judge_binary = "llm_judge_binary" in config.evaluation.strategies
    use_any_llm_judge = use_llm_judge or use_llm_judge_binary

    if use_any_llm_judge:
        if (
            config.evaluation.judge_backend
            and config.evaluation.judge_backend != config.llm.backend
        ):
            judge_llm = replace(config.llm, backend=config.evaluation.judge_backend)
            judge_backend = build_backend(judge_llm)
        else:
            judge_backend = backend

    per_sample_eval_df = evaluate_per_sample(
        results_df,
        judge_backend=judge_backend if use_any_llm_judge else None,
        usage_sink=_usage_sink,
        strategies=config.evaluation.strategies,
        concurrency=config.evaluation.concurrency,
    )
    _flush_usage_records(force=True)
    final_results_df = pd.concat([results_df, per_sample_eval_df], axis=1)

    print("\nEvaluating overall performance …")
    eval_df = evaluate_all(
        final_results_df,
        judge_backend=judge_backend if use_any_llm_judge else None,
        per_sample_df=per_sample_eval_df,
        strategies=config.evaluation.strategies,
        concurrency=config.evaluation.concurrency,
    )
    _flush_usage_records(force=True)
    print("\n=== Evaluation ===")
    print(eval_df.to_string(index=False))

    # ------------------------------------------------------------------ #
    # 9. Save
    # ------------------------------------------------------------------ #
    if config.output.save_results:
        print(f"\nSaving results to {config.output.results_dir} …")
        final_results_df.to_csv(results_path, index=False)
        eval_df.to_csv(eval_path, index=False)
        config.to_yaml(config_path)

        if annotation_stream_path is not None and os.path.exists(annotation_stream_path):
            os.remove(annotation_stream_path)
            print(f"Removed temporary annotation stream → {annotation_stream_path}")

        _flush_usage_records(force=True)
        usage_rows: list[dict[str, Any]] = []
        if os.path.exists(usage_attempts_path):
            with open(usage_attempts_path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        usage_rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        usage_df = pd.DataFrame(usage_rows)
        if "cache_used" in usage_df.columns:
            usage_df["cache_used"] = usage_df["cache_used"].fillna(False).astype(bool)
            usage_df["cache_hits"] = usage_df["cache_used"].astype(int)

        # Keep prompt/response in a dedicated failure file; keep llm_usage.csv compact.
        failure_statuses = {"retry_error", "format_error", "final_failure"}
        if "attempt_status" in usage_df.columns:
            usage_failures_df = usage_df[usage_df["attempt_status"].isin(failure_statuses)].copy()
        else:
            usage_failures_df = pd.DataFrame()

        if not usage_failures_df.empty:
            usage_failures_df.to_csv(usage_failures_path, index=False)
        elif os.path.exists(usage_failures_path):
            os.remove(usage_failures_path)

        compact_df = usage_df.copy()
        for col in ("prompt_user_message", "prompt_system_message", "response_text"):
            if col in compact_df.columns:
                compact_df = compact_df.drop(columns=[col])
        compact_df.to_csv(usage_path, index=False)

        if not compact_df.empty:
            group_cols = [
                c for c in ["step", "phase", "provider", "backend", "model", "attempt_status"]
                if c in compact_df.columns
            ]
            token_cols = [
                c for c in compact_df.columns
                if ("token" in c.lower()) or c in {"cache_hits"}
            ]
            if group_cols:
                usage_summary_df = (
                    compact_df[group_cols + token_cols]
                    .groupby(group_cols, dropna=False)
                    .sum(numeric_only=True)
                    .reset_index()
                )
                attempts_df = (
                    compact_df[group_cols]
                    .groupby(group_cols, dropna=False)
                    .size()
                    .reset_index(name="attempt_count")
                )
                usage_summary_df = usage_summary_df.merge(attempts_df, on=group_cols, how="left")
            else:
                usage_summary_df = pd.DataFrame(
                    [{"attempt_count": int(len(compact_df))}]
                )
                for col in token_cols:
                    usage_summary_df[col] = pd.to_numeric(compact_df[col], errors="coerce").fillna(0).sum()
        else:
            usage_summary_df = pd.DataFrame()
        usage_summary_df.to_csv(usage_summary_path, index=False)

        save_confusion_matrix(final_results_df, cm_path, cell_type_list)

        if stage2_skipped_records:
            pd.DataFrame(stage2_skipped_records).to_csv(skipped_path, index=False)
            print(f"Stage-2 skipped cells ({len(stage2_skipped_records)}) saved → {skipped_path}")

        print(f"\nSaved organized outputs under: {config.output.results_dir}/")
        print(f"  tables/: {name}_results.csv, {name}_eval.csv")
        print(f"  logs/: {name}_usage_attempts.jsonl, {name}_llm_usage.csv, {name}_llm_usage_failures.csv, {name}_llm_usage_summary.csv")
        print(f"  plots/: {name}_confusion_matrix.png")
        print(f"  stage2/: {name}_stage2_program_cache.json, {name}_stage2_skipped.csv")
        print(f"  meta/: {name}_config.yaml, {name}_timing.csv")

    if inspect_enabled:
        sorted_records = _sorted_inspect_records(inspect_records)
        os.makedirs(os.path.dirname(inspect_path) or ".", exist_ok=True)
        with open(inspect_path, "w", encoding="utf-8") as fh:
            for record in sorted_records:
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"Inspect traces saved ({len(sorted_records)} records) → {inspect_path}")
        save_inspect_pretty(sorted_records, inspect_path)
    
    # Record completion time
    end_time = time.time()
    end_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    duration_seconds = end_time - start_time
    duration_minutes = duration_seconds / 60
    
    print(f"\nEnd time: {end_time_str}")
    print(f"Duration: {duration_minutes:.2f} minutes ({duration_seconds:.0f} seconds)")
    
    # Save timing information
    timing_data = {
        "experiment_name": [config.output.experiment_name],
        "start_time": [start_time_str],
        "end_time": [end_time_str],
        "duration_seconds": [duration_seconds],
        "duration_minutes": [duration_minutes],
    }
    timing_df = pd.DataFrame(timing_data)
    if config.output.save_results:
        timing_df.to_csv(timing_path, index=False)
        print(f"Timing saved → {timing_path}")

    return final_results_df
