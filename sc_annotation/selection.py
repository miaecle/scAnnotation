"""Feature selection strategies (Axis 4 — Feature Selection).

Unified interface
-----------------
All ``score_by_*`` functions and ``compute_scores`` share the same contract:

- **Input**  ``cell_indices`` — single ``int`` or any sequence of ``int``\\ s.
  A scalar is silently promoted to a one-element list.

- **Layer**  All functions accept a ``layer`` parameter (default ``'lognorm'``).
  Pass ``layer='clr'`` to score ADT proteins from a CITE-seq AnnData.

- **Aggregation**  For a group of cells the per-feature expression is
  summarised by :func:`_group_aggregate`, which dispatches on layer type:

  - ``'lognorm'`` — :func:`_group_mean_lognorm`: average in *pre-log*
    (normalized count) space, then re-apply ``log1p``:
    ``log1p(mean(expm1(lognorm)))``.
  - ``'clr'`` — average raw counts across cells, then re-apply CLR to the
    mean vector.  This produces the CLR score for a "merged pseudocell".
  - other — arithmetic mean in the layer's own space (fallback).

  Exception: :func:`score_by_de` uses arithmetic mean in layer space for
  LFC, consistent with the stored ``mean_expr`` population baseline.

- **Output** ``pd.Series(scores, index=feature_names)`` — length
  ``n_features``, indexed by gene symbol (RNA) or protein name (ADT).
  Features with zero group-mean expression or excluded by the filter mask
  carry ``-inf`` and will not appear in :func:`select_genes` output.

``select_genes(scores, n_top)`` consumes a score Series and returns the
top-N ``(name, score)`` list — works for both genes and proteins.

Population-level statistics
-----------------------------
``mean_expr``, ``std_expr``, and ``idf`` are read from ``adata.var``.
For RNA, they are pre-computed by
:func:`~sc_annotation.global_metrics.compute_global_metrics`.
For ADT, they are pre-computed by
:func:`~sc_annotation.adt.compute_adt_stats` (called automatically by
:func:`~sc_annotation.adt.normalize_adt`).
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from typing import Optional
import yaml

import numpy as np
import pandas as pd
import scipy.sparse as sp
import anndata as ad


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _normalise_indices(cell_indices) -> list[int]:
    """Coerce scalar int or any sequence to a plain list of ints."""
    if isinstance(cell_indices, (int, np.integer)):
        return [int(cell_indices)]
    return [int(i) for i in cell_indices]


def _extract_layer_2d(adata: ad.AnnData, cell_indices, layer: str = "lognorm") -> np.ndarray:
    """Extract a named layer for ``cell_indices`` as a 2-D float array.

    Returns shape ``(n_cells, n_features)``.
    """
    if layer not in adata.layers:
        raise ValueError(
            f"Layer '{layer}' not found — ensure it has been computed first "
            "(run compute_global_metrics for RNA or normalize_adt for ADT)."
        )
    idx = _normalise_indices(cell_indices)
    X = adata.layers[layer][idx]
    if sp.issparse(X):
        X = np.asarray(X.todense())
    return np.asarray(X, dtype=float)


def _to_series(scores: np.ndarray, adata: ad.AnnData) -> pd.Series:
    """Wrap a 1-D score array as a ``pd.Series`` indexed by gene name."""
    names = (
        adata.var["gene_symbol"].values
        if "gene_symbol" in adata.var.columns
        else np.asarray(adata.var_names)
    )
    return pd.Series(scores, index=names, dtype=float)


def _apply_gene_mask(scores: np.ndarray, gene_mask: Optional[np.ndarray]) -> np.ndarray:
    if gene_mask is not None:
        return np.where(gene_mask, scores, -np.inf)
    return scores


def _group_mean_lognorm(X: np.ndarray) -> np.ndarray:
    """Aggregate lognorm expression for a group of cells by averaging in pre-log space.

    Computes ``log1p(mean(expm1(X)))`` — converts each cell back to normalized
    counts, takes the mean, then re-applies log1p.  For a single cell this
    reduces to the identity (``log1p(expm1(x)) == x``).  For groups it gives
    the log-expression of the merged pseudocell rather than the mean of
    log-expressions (which would underestimate due to Jensen's inequality).

    Args:
        X: 2-D float array of shape ``(n_cells, n_features)`` from the lognorm layer.

    Returns:
        1-D float array of shape ``(n_features,)``.
    """
    return np.log1p(np.expm1(X).mean(axis=0))


def _group_aggregate(adata: ad.AnnData, cell_indices, layer: str) -> np.ndarray:
    """Aggregate a group of cells into a single score vector, dispatching on layer.

    Implements the "pre-transform mean" philosophy for each layer type:

    - ``'lognorm'``: :func:`_group_mean_lognorm` — average normalized counts
      (expm1), then re-log.
    - ``'clr'``: average raw counts across cells, then re-apply CLR to the
      mean vector.  This is correct because CLR cannot be inverted via expm1
      (it is centered, not a plain log1p of raw counts).
    - other: arithmetic mean in the layer's own space.

    For a single cell, all paths return the stored layer value directly.

    Args:
        adata: AnnData with ``adata.layers[layer]`` present.  For ``'clr'``,
            ``adata.X`` must contain raw counts.
        cell_indices: Single int or sequence of ints.
        layer: Name of the normalized layer to aggregate.

    Returns:
        1-D float array of shape ``(n_features,)``.
    """
    idx = _normalise_indices(cell_indices)
    X = _extract_layer_2d(adata, idx, layer)

    if len(idx) == 1:
        return X[0]

    if layer == "lognorm":
        return _group_mean_lognorm(X)

    if layer == "clr":
        # Average raw counts, then re-apply CLR — mirrors _group_mean_lognorm for RNA
        X_raw = adata.X[idx]
        if sp.issparse(X_raw):
            X_raw = X_raw.toarray()
        mean_raw = np.asarray(X_raw, dtype=float).mean(axis=0)
        log1p_m = np.log1p(mean_raw)
        return log1p_m - log1p_m.mean()

    return X.mean(axis=0)


# ---------------------------------------------------------------------------
# Score functions
# ---------------------------------------------------------------------------

def score_by_expr(
    adata: ad.AnnData,
    cell_indices,
    layer: str = "lognorm",
    mask_zeros: bool = True,
) -> pd.Series:
    """Normalized expression score.

    Score = aggregated layer value via :func:`_group_aggregate`.  Entries with
    zero (or below-background for CLR) group-mean are ``-inf``.

    Args:
        adata: AnnData with the named layer present.
        cell_indices: Single int or list of ints.
        layer: Normalized layer to use (``'lognorm'`` for RNA, ``'clr'`` for ADT).

    Returns:
        ``pd.Series`` indexed by feature name.
    """
    expr = _group_aggregate(adata, cell_indices, layer)
    if mask_zeros:
        scores = np.where(expr > 0, expr, -np.inf)
    else:
        scores = expr
    return _to_series(scores, adata)


def score_by_zscore(
    adata: ad.AnnData,
    cell_indices,
    layer: str = "lognorm",
    mask_zeros: bool = True,
) -> pd.Series:
    """Z-score of group expression relative to the population.

    Group expression is computed via :func:`_group_aggregate`.  Z-score is
    taken against ``mean_expr`` / ``std_expr`` in ``adata.var``, which are
    population statistics in the same layer space (lognorm for RNA, CLR for ADT).

    Args:
        adata: AnnData with the named layer and ``mean_expr`` / ``std_expr``
            in ``var``.
        cell_indices: Single int or list of ints.
        layer: Normalized layer to use (``'lognorm'`` for RNA, ``'clr'`` for ADT).

    Returns:
        ``pd.Series`` indexed by feature name.  Zero/below-background entries
        are ``-inf``.
    """
    for col in ("mean_expr", "std_expr"):
        if col not in adata.var.columns:
            raise ValueError(
                f"'{col}' missing — run compute_global_metrics (RNA) or "
                "normalize_adt (ADT) first."
            )

    expr = _group_aggregate(adata, cell_indices, layer)
    mean_e = adata.var["mean_expr"].values.astype(float)
    std_e = adata.var["std_expr"].values.astype(float)
    z = (expr - mean_e) / np.where(std_e > 0, std_e, 1.0)
    if mask_zeros:
        scores = np.where(expr > 0, z, -np.inf)
    else:
        scores = z
    return _to_series(scores, adata)


def score_by_tfidf(
    adata: ad.AnnData,
    cell_indices,
    layer: str = "lognorm",
    mask_zeros: bool = True,
) -> pd.Series:
    """TF-IDF score computed on mean pre-transform expression.

    - TF  = ``norm_mean / Σ norm_mean`` where ``norm_mean = mean(expm1(layer))``
    - IDF = ``adata.var['idf']`` = ``-log(pct_cells)`` (pre-computed global)

    ``expm1`` of a lognorm layer gives normalized counts; ``expm1`` of a CLR
    layer gives counts scaled by the per-cell geometric mean — both are valid
    relative measures for TF calculation.

    Args:
        adata: AnnData with the named layer and ``idf`` in ``var``.
        cell_indices: Single int or list of ints.
        layer: Normalized layer to use (``'lognorm'`` for RNA, ``'clr'`` for ADT).

    Returns:
        ``pd.Series`` indexed by feature name.

    Warns:
        If the group total normalized expression sums to zero.
    """
    if "idf" not in adata.var.columns:
        raise ValueError(
            "'idf' missing — run compute_global_metrics (RNA) or "
            "normalize_adt (ADT) first."
        )

    X = _extract_layer_2d(adata, cell_indices, layer)
    norm_mean = np.expm1(X).mean(axis=0)   # pre-transform mean
    total = norm_mean.sum()
    if total == 0:
        warnings.warn(
            "Group has zero total normalized expression; TF-IDF scores set to -inf.",
            stacklevel=3,
        )
        return _to_series(np.full(adata.n_vars, -np.inf), adata)
    idf = adata.var["idf"].values.astype(float)
    tf = norm_mean / total
    if mask_zeros:
        scores = np.where(norm_mean > 0, tf * idf, -np.inf)
    else:
        scores = tf * idf
    return _to_series(scores, adata)


def score_by_de(
    adata: ad.AnnData,
    cell_indices,
    layer: str = "lognorm",
    min_pct_group: float = 0.1,
    mask_zeros: bool = True,
) -> pd.Series:
    """Log fold-change of a cell group vs the rest of the population.

    Score = ``mean_layer(group) − mean_layer(rest)`` where both means are
    arithmetic means in the layer's own space.  Consistent with the stored
    ``adata.var['mean_expr']`` (population arithmetic mean in layer space),
    which is used to derive ``mean_rest`` without reading the full matrix.

    For RNA (``layer='lognorm'``): standard scRNA-seq LFC.
    For ADT (``layer='clr'``): LFC in CLR space — positive values indicate
    the protein is more expressed in this group relative to the rest.

    Args:
        adata: AnnData with the named layer and ``mean_expr`` in ``var``.
        cell_indices: Single int or list of ints forming the group.
        layer: Normalized layer to use (``'lognorm'`` for RNA, ``'clr'`` for ADT).
        min_pct_group: Features with fewer than this fraction of group cells
            expressing them (layer value > 0) receive score ``-inf``.

    Returns:
        ``pd.Series`` indexed by feature name.
    """
    if "mean_expr" not in adata.var.columns:
        raise ValueError(
            "'mean_expr' missing — run compute_global_metrics (RNA) or "
            "normalize_adt (ADT) first."
        )

    X = _extract_layer_2d(adata, cell_indices, layer)   # (n_group, n_features)
    n_group = X.shape[0]
    n_total = adata.n_obs

    # Arithmetic mean in layer space — consistent with stored mean_expr
    mean_group = X.mean(axis=0)
    pct_group = (X > 0).mean(axis=0)

    mean_all = adata.var["mean_expr"].values.astype(float)
    mean_rest = (mean_all * n_total - mean_group * n_group) / max(n_total - n_group, 1)

    log_fc = mean_group - mean_rest
    if mask_zeros:
        scores = np.where(pct_group >= min_pct_group, log_fc, -np.inf)
    else:
        scores = log_fc
    return _to_series(scores, adata)


# ---------------------------------------------------------------------------
# Unified dispatcher
# ---------------------------------------------------------------------------

def compute_scores(
    adata: ad.AnnData,
    cell_indices,
    strategy: str,
    gene_mask: Optional[np.ndarray] = None,
    min_pct_group: float = 0.1,
    layer: str = "lognorm",
    mask_zeros: bool = True,
) -> pd.Series:
    """Compute per-feature scores for a cell or group of cells.

    Works for both RNA (``layer='lognorm'``) and ADT proteins (``layer='clr'``).
    For ADT, call :func:`~sc_annotation.adt.normalize_adt` first to populate
    the layer and population statistics in ``adata.var``.

    Args:
        adata: AnnData with the named layer and global metrics in ``var``.
        cell_indices: Single int or list of ints.  Multiple indices are
            aggregated before scoring (see :func:`_group_aggregate`).
        strategy: One of ``"expr"``, ``"zscore"``, ``"tfidf"``, ``"de"``.
        gene_mask: Boolean inclusion mask from
            :func:`~sc_annotation.filtering.build_gene_mask`.
            Excluded features are set to ``-inf``.  Typically ``None`` for ADT.
        min_pct_group: Minimum fraction of group cells expressing the feature;
            ``"de"`` only.
        layer: Normalized layer to score from.  Default ``'lognorm'`` for RNA;
            pass ``'clr'`` for ADT proteins.

    Returns:
        ``pd.Series`` indexed by feature name (gene symbol or protein name).

    Raises:
        ValueError: Unknown strategy or missing ``adata.var`` columns.
    """
    if strategy == "expr":
        scores = score_by_expr(adata, cell_indices, layer=layer, mask_zeros=mask_zeros)
    elif strategy == "zscore":
        scores = score_by_zscore(adata, cell_indices, layer=layer, mask_zeros=mask_zeros)
    elif strategy == "tfidf":
        scores = score_by_tfidf(adata, cell_indices, layer=layer, mask_zeros=mask_zeros)
    elif strategy == "de":
        scores = score_by_de(
            adata,
            cell_indices,
            layer=layer,
            min_pct_group=min_pct_group,
            mask_zeros=mask_zeros,
        )
    else:
        raise ValueError(
            f"Unknown strategy: {strategy!r}. Choose: expr | zscore | tfidf | de"
        )

    if gene_mask is not None:
        scores = pd.Series(
            np.where(gene_mask, scores.values, -np.inf),
            index=scores.index,
            dtype=float,
        )
    return scores


# ---------------------------------------------------------------------------
# Selection step
# ---------------------------------------------------------------------------

def select_genes(scores: pd.Series, n_top: int) -> list[tuple[str, float]]:
    """Select top-N genes from a score Series.

    Args:
        scores: ``pd.Series`` from :func:`compute_scores`, indexed by gene
            name.  Entries with value ``-inf`` are excluded.
        n_top: Maximum number of genes to return.

    Returns:
        List of ``(gene_name, score)`` sorted by score descending.
    """
    finite = scores[np.isfinite(scores.values)]
    if finite.empty:
        return []
    return list(finite.nlargest(n_top).items())


# ---------------------------------------------------------------------------
# Marker panel (structured — not score-based)
# ---------------------------------------------------------------------------

@dataclass
class MarkerPanel:
    """Curated positive/negative lineage markers.

    Load from YAML::

        panel = MarkerPanel.from_yaml('configs/markers/pbmc_broad_lineage.yaml')
    """

    positive: list[str] = field(default_factory=list)
    negative: list[str] = field(default_factory=list)
    description: str = ""

    @classmethod
    def from_yaml(cls, path: str) -> "MarkerPanel":
        with open(path) as fh:
            d = yaml.safe_load(fh)
        return cls(
            positive=d.get("positive", []),
            negative=d.get("negative", []),
            description=d.get("description", ""),
        )


def select_by_marker_panel(
    adata: ad.AnnData,
    cell_indices,
    marker_panel: MarkerPanel,
    gene_mask: Optional[np.ndarray] = None,
) -> tuple[list[tuple[str, float]], list[tuple[str, float]]]:
    """Evaluate a marker panel against a cell or group mean.

    Args:
        adata: AnnData with ``lognorm`` layer.
        cell_indices: Single int or list of ints.
        marker_panel: :class:`MarkerPanel` instance.
        gene_mask: Boolean inclusion mask; masked genes are omitted.

    Returns:
        ``(pos_expressed, neg_expressed)`` — ``(gene_name, mean_lognorm)``
        for positive markers that are expressed and negative markers that are
        (unexpectedly) expressed.
    """
    scores = score_by_expr(adata, cell_indices)  # pd.Series indexed by gene name

    name_to_val: dict[str, float] = scores.to_dict()

    def _lookup(gene: str):
        val = name_to_val.get(gene)
        if val is None:
            upper_map = {g.upper(): g for g in name_to_val}
            canonical = upper_map.get(gene.upper())
            if canonical is None:
                return None
            val = name_to_val[canonical]
            gene = canonical
        if gene_mask is not None:
            idx = np.where(
                adata.var["gene_symbol"].values == gene
                if "gene_symbol" in adata.var.columns
                else np.asarray(adata.var_names) == gene
            )[0]
            if len(idx) and not gene_mask[idx[0]]:
                return None
        if val <= 0 or not np.isfinite(val):
            return None
        return (gene, float(val))

    pos = [r for g in marker_panel.positive if (r := _lookup(g)) is not None]
    neg = [r for g in marker_panel.negative if (r := _lookup(g)) is not None]
    return pos, neg
