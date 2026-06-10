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

import os
import time
from typing import Optional

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
from .data import sample_cells
from .adt import build_adt_adata, normalize_adt, get_top_proteins as get_top_proteins_adt
from .metrics import parse_results, evaluate_all
from .backends.base import LLMBackend


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
    raise ValueError(f"Unknown backend: {llm_config.backend!r}. Choose gemini | claude | openai.")


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


def _build_prompt(gene_sel: dict, sel_cfg, proteins: list, tissue: Optional[str]) -> str:
    """Dispatch to the correct prompt builder based on selection strategy."""
    s = sel_cfg.strategy
    if s == "combined":
        return build_enriched_prompt(
            genes_by_expr=gene_sel["primary"],
            genes_by_zscore=gene_sel["secondary"],
            proteins=proteins,
            tissue=tissue,
        )
    if s == "marker_panel":
        return build_marker_panel_prompt(
            pos_expressed=gene_sel["pos_markers"],
            neg_expressed=gene_sel["neg_markers"],
            top_genes=gene_sel["primary"],
            proteins=proteins,
            tissue=tissue,
        )
    # expr / zscore / tfidf / de — single ranked list
    return build_naive_prompt(
        genes=gene_sel["primary"],
        proteins=proteins,
        tissue=tissue,
    )


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
    6. Evaluate with all configured strategies.
    7. Save results + config snapshot to ``config.output.results_dir``.

    Args:
        adata: AnnData object.  Global metrics are added in-place if missing.
        config: Experiment configuration.
        backend: Pre-built LLM backend.  Built from ``config.llm`` if None.

    Returns:
        Results DataFrame with columns:
        ``cell_idx``, ``cell_barcode``, ``true_label``,
        ``pred_label``, ``pred_celltype``, ``pred_rationale``.
    """
    print(f"\n{'='*60}")
    print(f"Experiment: {config.output.experiment_name}")
    print(config.summary())
    print("="*60)

    # ------------------------------------------------------------------ #
    # 0. Backend
    # ------------------------------------------------------------------ #
    if backend is None:
        backend = build_backend(config.llm)
    print(f"Backend: {backend}")

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
    sample_df = sample_cells(
        adata,
        label_col=config.evaluation.label_col,
        n_per_class=config.evaluation.n_per_class,
        seed=config.evaluation.seed,
    )
    n_types = sample_df["true_label"].nunique()
    print(f"Sampled {len(sample_df)} cells from {n_types} cell types")

    # ------------------------------------------------------------------ #
    # 7. Annotate
    # ------------------------------------------------------------------ #
    preds: list[str] = []
    for row in tqdm(sample_df.itertuples(), total=len(sample_df), desc="Annotating"):
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

        prompt = _build_prompt(gene_sel, config.selection, proteins, config.tissue)
        response = backend.complete(prompt, system_message=SYSTEM_PROMPT)
        preds.append(response)

    results_df = sample_df.copy()
    results_df["pred_label"] = preds
    results_df = parse_results(results_df)

    # ------------------------------------------------------------------ #
    # 7. Evaluate
    # ------------------------------------------------------------------ #
    judge_backend: Optional[LLMBackend] = None
    if "llm_judge" in config.evaluation.strategies:
        if (
            config.evaluation.judge_backend
            and config.evaluation.judge_backend != config.llm.backend
        ):
            from dataclasses import replace
            judge_llm = replace(config.llm, backend=config.evaluation.judge_backend)
            judge_backend = build_backend(judge_llm)
        else:
            judge_backend = backend

    eval_df = evaluate_all(
        results_df,
        judge_backend=judge_backend if "llm_judge" in config.evaluation.strategies else None,
    )
    print("\n=== Evaluation ===")
    print(eval_df.to_string(index=False))

    # ------------------------------------------------------------------ #
    # 8. Save
    # ------------------------------------------------------------------ #
    if config.output.save_results:
        os.makedirs(config.output.results_dir, exist_ok=True)
        name = config.output.experiment_name

        results_path = os.path.join(config.output.results_dir, f"{name}_results.csv")
        results_df.to_csv(results_path, index=False)

        eval_path = os.path.join(config.output.results_dir, f"{name}_eval.csv")
        eval_df.to_csv(eval_path, index=False)

        config_path = os.path.join(config.output.results_dir, f"{name}_config.yaml")
        config.to_yaml(config_path)

        print(f"\nSaved → {config.output.results_dir}/  ({name}_results.csv, _eval.csv, _config.yaml)")

    return results_df
