"""ADT / protein count handling for CITE-seq data.

Provides a parallel AnnData for protein expression that mirrors the RNA
pipeline's layer-based design, while using ADT-appropriate normalization.

Workflow
--------
1. :func:`build_adt_adata` — extract protein counts from ``adata.obsm`` into
   a standalone AnnData (same cell order, proteins as vars).
2. :func:`normalize_adt` — normalize in place; stores result in a named layer
   (default ``'clr'``).
3. :func:`get_top_proteins` — query top-N proteins for a cell or group of cells,
   using the same ``cell_indices: list[int]`` interface as
   :func:`~sc_annotation.selection.compute_scores`.

Normalization methods
---------------------
``clr`` (default)
    Centered log-ratio per cell:
    ``clr_ij = log1p(x_ij) − mean_k log1p(x_ik)``
    where k indexes proteins.  Proteins expressed above the cell's own
    background get a positive score; the result is cell-centered, making
    it robust to differences in total ADT capture between cells.
    Standard for CITE-seq (Seurat / scanpy default for ADT).

``lognorm``
    Library-size normalise to 10 000 counts/cell then log1p — analogous
    to the RNA pipeline.  Less common for ADT but available as a simple
    baseline.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd
import anndata as ad

from .selection import compute_scores, select_genes


# ---------------------------------------------------------------------------
# CLR helper
# ---------------------------------------------------------------------------

def _clr_per_cell(X_raw: np.ndarray) -> np.ndarray:
    """Centered log-ratio normalization, applied row-wise (per cell).

    ``clr_ij = log1p(x_ij) − mean_k log1p(x_ik)``

    Args:
        X_raw: 2-D float array ``(n_cells, n_proteins)`` of raw counts.

    Returns:
        CLR-transformed array of the same shape.
    """
    log1p_X = np.log1p(X_raw)
    return log1p_X - log1p_X.mean(axis=1, keepdims=True)


# ---------------------------------------------------------------------------
# Build parallel AnnData
# ---------------------------------------------------------------------------

def build_adt_adata(
    adata: ad.AnnData,
    protein_key: str = "protein_counts",
    protein_names_key: str = "ADT_names",
) -> ad.AnnData:
    """Extract protein counts from ``adata.obsm`` into a standalone AnnData.

    The returned object has the same cell order as ``adata`` (matching
    ``obs_names``) and proteins as variables.  Raw counts are stored in
    ``X``; normalized layers are added by :func:`normalize_adt`.

    Args:
        adata: Source AnnData with protein counts in ``obsm``.
        protein_key: Key in ``adata.obsm`` for the protein count matrix.
        protein_names_key: Key in ``adata.uns`` for the protein name array.

    Returns:
        AnnData of shape ``(n_cells, n_proteins)`` with raw counts in ``X``.

    Raises:
        KeyError: If ``protein_key`` or ``protein_names_key`` are absent.
    """
    if protein_key not in adata.obsm:
        raise KeyError(
            f"'{protein_key}' not found in adata.obsm. "
            f"Available keys: {list(adata.obsm.keys())}"
        )
    if protein_names_key not in adata.uns:
        raise KeyError(
            f"'{protein_names_key}' not found in adata.uns. "
            f"Available keys: {list(adata.uns.keys())}"
        )

    X = np.asarray(adata.obsm[protein_key], dtype=float)
    protein_names = np.asarray(adata.uns[protein_names_key], dtype=str)

    return ad.AnnData(
        X=X,
        obs=pd.DataFrame(index=adata.obs_names),
        var=pd.DataFrame(index=pd.Index(protein_names, name="protein")),
    )


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def normalize_adt(
    adt_adata: ad.AnnData,
    method: str = "clr",
    inplace: bool = True,
) -> ad.AnnData:
    """Normalize ADT protein counts and compute population statistics.

    Stores the normalized layer in ``adt_adata.layers[method]`` and then
    calls :func:`compute_adt_stats` to populate ``adt_adata.var`` with
    ``mean_expr``, ``std_expr``, ``pct_cells``, and ``idf`` — the same
    column names used by the RNA scoring pipeline, enabling
    :func:`~sc_annotation.selection.compute_scores` to work directly on
    ``adt_adata`` with ``layer=method``.

    Args:
        adt_adata: AnnData with raw protein counts in ``X`` (from
            :func:`build_adt_adata`).
        method: ``'clr'`` (centered log-ratio, default) or ``'lognorm'``
            (library-size + log1p).
        inplace: Modify ``adt_adata`` in place; return a copy if ``False``.

    Returns:
        Annotated AnnData with the normalized layer and population stats added.

    Raises:
        ValueError: Unknown normalization method.
    """
    if not inplace:
        adt_adata = adt_adata.copy()

    X_raw = np.asarray(adt_adata.X, dtype=float)

    if method == "clr":
        adt_adata.layers["clr"] = _clr_per_cell(X_raw)
    elif method == "lognorm":
        cell_totals = X_raw.sum(axis=1, keepdims=True)
        safe_totals = np.where(cell_totals > 0, cell_totals, 1.0)
        adt_adata.layers["lognorm"] = np.log1p(X_raw / safe_totals * 1e4)
    else:
        raise ValueError(
            f"Unknown normalization method: {method!r}. Choose: clr | lognorm"
        )

    compute_adt_stats(adt_adata, layer=method, inplace=True)
    return adt_adata


def compute_adt_stats(
    adt_adata: ad.AnnData,
    layer: str = "clr",
    inplace: bool = True,
) -> ad.AnnData:
    """Compute population statistics for ADT proteins and store in ``var``.

    Mirrors :func:`~sc_annotation.global_metrics.compute_global_metrics` for
    RNA.  After this call, :func:`~sc_annotation.selection.compute_scores`
    can be used directly on ``adt_adata`` with ``layer=layer`` to run any of
    the four scoring strategies (``expr``, ``zscore``, ``tfidf``, ``de``).

    Columns added to ``adt_adata.var``:

    ============  ============================================================
    ``mean_expr`` Population arithmetic mean per protein (in layer space).
    ``std_expr``  Population std per protein (in layer space).
    ``pct_cells`` Fraction of cells with layer value > 0 (above background).
    ``idf``       ``-log(pct_cells)`` — rarity weight used by TF-IDF scoring.
    ============  ============================================================

    Args:
        adt_adata: AnnData with ``adt_adata.layers[layer]`` present.
        layer: Normalized layer to compute statistics from.
        inplace: Modify in place; return a copy if ``False``.

    Returns:
        AnnData with population statistics added to ``var``.
    """
    if not inplace:
        adt_adata = adt_adata.copy()
    if layer not in adt_adata.layers:
        raise ValueError(
            f"Layer '{layer}' not found — run normalize_adt(method='{layer}') first."
        )

    X = np.asarray(adt_adata.layers[layer], dtype=float)
    adt_adata.var["mean_expr"] = X.mean(axis=0)
    adt_adata.var["std_expr"] = X.std(axis=0)
    pct = (X > 0).mean(axis=0)
    adt_adata.var["pct_cells"] = pct
    safe_pct = np.where(pct > 0, pct, 1.0)
    adt_adata.var["idf"] = -np.log(safe_pct)
    return adt_adata


# ---------------------------------------------------------------------------
# Per-cell / per-group query
# ---------------------------------------------------------------------------

def get_top_proteins(
    adt_adata: ad.AnnData,
    cell_indices,
    n_top: int = 20,
    layer: str = "clr",
    strategy: str = "expr",
) -> list[tuple[str, float]]:
    """Return the top-N proteins for a cell or group.

    Thin wrapper over :func:`~sc_annotation.selection.compute_scores` +
    :func:`~sc_annotation.selection.select_genes` — the same pipeline used
    for RNA gene scoring, unified via the ``layer`` parameter.

    Group aggregation is handled by
    :func:`~sc_annotation.selection._group_aggregate`: for ``layer='clr'``
    this averages raw counts and re-applies CLR; for ``layer='lognorm'`` it
    averages in pre-log normalized-count space.

    Requires :func:`normalize_adt` to have been called (which populates
    ``adt_adata.var`` with population statistics needed by ``zscore`` / ``de``).

    Args:
        adt_adata: AnnData from :func:`build_adt_adata` after
            :func:`normalize_adt`.
        cell_indices: Single ``int`` or list of ``int``\\s.
        n_top: Maximum number of proteins to return.
        layer: Normalized layer to score from (``'clr'`` default, ``'lognorm'``
            also supported).
        strategy: Scoring strategy — ``'expr'``, ``'zscore'``, ``'tfidf'``,
            or ``'de'``.  Mirrors the RNA ``compute_scores`` strategies.

    Returns:
        List of ``(protein_name, score)`` sorted by score descending.
        Below-background proteins (layer value ≤ 0) are excluded.

    Raises:
        ValueError: If ``layer`` is not present or population stats are missing.
    """
    scores = compute_scores(adt_adata, cell_indices, strategy, layer=layer)
    return select_genes(scores, n_top)
