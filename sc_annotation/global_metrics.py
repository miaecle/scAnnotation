"""Global gene-level quantitative metrics for single-cell annotation.

Writes the following to ``adata``:

Layers
~~~~~~
- ``lognorm``     — library-size-normalised (10 000 counts/cell) + log1p expression.
  Same sparsity as raw counts (log1p(0) = 0).  Used by all downstream scoring.

``adata.var`` columns
~~~~~~~~~~~~~~~~~~~~~
- ``mean_expr``   — mean log-normalised expression across cells
- ``std_expr``    — std  of log-normalised expression across cells
- ``pct_cells``   — fraction of cells with non-zero raw expression
- ``idf``         — ``-log(pct_cells)``; IDF component of TF-IDF
- ``is_low_expr`` — ``True`` when ``pct_cells < min_cells_pct``
- ``is_hvg``      — highly variable gene (scanpy Seurat dispersion on lognorm)
- ``gini``        — Gini index of log-normalised expression (0 = uniform, 1 = focal)

Boolean gene-type flags (``is_mt``, ``is_ribo``, ``is_hb``, etc.) are handled
by :func:`sc_annotation.filtering.annotate_genes`.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import scipy.sparse as sp
import anndata as ad
from tqdm import tqdm


# ---------------------------------------------------------------------------
# Log-normalisation layer
# ---------------------------------------------------------------------------

def _compute_lognorm_layer(
    adata: ad.AnnData,
    X_raw: sp.spmatrix | np.ndarray,
    target_sum: float = 1e4,
) -> None:
    """Compute library-size-normalised log1p counts and store in ``adata.layers['lognorm']``.

    Normalisation: each cell's counts are scaled so the total equals
    ``target_sum``, then log1p-transformed.  The result is sparse if the input
    is sparse (zeros stay zero after log1p).

    Does **not** modify ``adata.X``.
    """
    if sp.issparse(X_raw):
        # Use CSR + in-place row scaling to avoid large temporary allocations
        # from sparse broadcast multiply on very large matrices.
        X_csr = X_raw.tocsr(copy=True).astype(np.float32)
        cell_totals = np.asarray(X_csr.sum(axis=1), dtype=np.float32).ravel()
        safe_totals = np.where(cell_totals > 0, cell_totals, 1.0).astype(np.float32, copy=False)
        scale = (np.float32(target_sum) / safe_totals).astype(np.float32, copy=False)

        row_nnz = np.diff(X_csr.indptr)
        X_csr.data *= np.repeat(scale, row_nnz)
        np.log1p(X_csr.data, out=X_csr.data)
        adata.layers["lognorm"] = X_csr
    else:
        X_f = np.asarray(X_raw, dtype=np.float32)
        cell_totals = X_f.sum(axis=1, keepdims=True)
        safe_totals = np.where(cell_totals > 0, cell_totals, 1.0).astype(np.float32, copy=False)
        X_norm = X_f * (np.float32(target_sum) / safe_totals)
        np.log1p(X_norm, out=X_norm)
        adata.layers["lognorm"] = X_norm


def _sparse_col_mean_std_chunked(
    X: sp.spmatrix,
    n_genes: int,
    n_cells: int,
    chunk_size: int = 5_000_000,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute per-gene mean/std for sparse matrices without large temporary arrays.

    The implementation accumulates weighted bincounts over chunks of non-zero
    entries, avoiding memory-heavy sparse matrix algebra that can duplicate
    ``data`` for very large matrices.
    """
    X_csr = X.tocsr(copy=False)
    idx_all = X_csr.indices
    data_all = X_csr.data

    sums = np.zeros(n_genes, dtype=np.float64)
    sums_sq = np.zeros(n_genes, dtype=np.float64)

    nnz = data_all.shape[0]
    for start in range(0, nnz, chunk_size):
        end = min(start + chunk_size, nnz)
        idx = idx_all[start:end]
        vals = data_all[start:end].astype(np.float64, copy=False)
        sums += np.bincount(idx, weights=vals, minlength=n_genes)
        sums_sq += np.bincount(idx, weights=vals * vals, minlength=n_genes)

    mean_expr = sums / float(n_cells)
    var_expr = np.maximum(sums_sq / float(n_cells) - mean_expr * mean_expr, 0.0)
    std_expr = np.sqrt(var_expr)
    return mean_expr, std_expr


# ---------------------------------------------------------------------------
# HVG via scanpy (uses stored lognorm layer — no re-normalisation)
# ---------------------------------------------------------------------------

def _compute_hvg_mask(
    adata: ad.AnnData,
    n_top: int,
    pct_cells: np.ndarray,
    min_cells_pct: float,
) -> np.ndarray:
    """Select HVGs using scanpy's Seurat dispersion method on the lognorm layer.

    Returns a boolean array of length ``n_genes``.
    """
    import scanpy as sc
    import pandas as pd

    expressed_mask = pct_cells >= min_cells_pct
    n_expressed = int(expressed_mask.sum())
    if n_expressed == 0:
        return np.zeros(adata.n_vars, dtype=bool)

    X_sub = adata.layers["lognorm"][:, expressed_mask]
    if not sp.issparse(X_sub):
        X_sub = np.asarray(X_sub, dtype=float)

    tmp = ad.AnnData(X=X_sub)
    tmp.var_names = pd.Index(adata.var_names[expressed_mask])
    sc.pp.highly_variable_genes(
        tmp,
        n_top_genes=min(n_top, n_expressed),
        flavor="seurat",
    )

    is_hvg = np.zeros(adata.n_vars, dtype=bool)
    is_hvg[expressed_mask] = tmp.var["highly_variable"].values
    return is_hvg


# ---------------------------------------------------------------------------
# Gini helper
# ---------------------------------------------------------------------------

def _gini_col(nz_data: np.ndarray, n_cells: int) -> float:
    """Gini index for one gene given its non-zero expression values."""
    if len(nz_data) == 0:
        return 0.0
    total = float(nz_data.sum())
    if total == 0.0:
        return 0.0
    n_zero = n_cells - len(nz_data)
    sorted_vals = np.sort(nz_data).astype(float)
    inner_ranks = np.arange(1, len(nz_data) + 1, dtype=float)
    numerator = 2.0 * (n_zero * total + float(np.dot(inner_ranks, sorted_vals)))
    return numerator / (n_cells * total) - (n_cells + 1) / n_cells


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def compute_global_metrics(
    adata: ad.AnnData,
    n_top_hvg: int = 2000,
    min_cells_pct: float = 0.01,
    layer: Optional[str] = None,
    compute_gini: bool = True,
    gini_scope: str = "expressed",
    inplace: bool = True,
) -> ad.AnnData:
    """Compute and store global gene-level quantitative metrics in ``adata``.

    All downstream scoring reads from ``adata.layers['lognorm']`` which is
    computed here.  Boolean gene-type flags (``is_mt``, etc.) are the
    responsibility of :func:`sc_annotation.filtering.annotate_genes`.

    Args:
        adata: AnnData with raw counts in ``adata.X`` (or ``layer``).
        n_top_hvg: Number of HVGs to flag.
        min_cells_pct: Threshold below which genes are flagged as low-expression.
        layer: Raw count layer to use instead of ``adata.X``.
        compute_gini: Whether to compute the Gini index.
        gini_scope: Genes for Gini: ``"hvg"`` (fast), ``"expressed"``, ``"all"``.
        inplace: Operate on ``adata`` in place; return a copy if ``False``.

    Returns:
        Annotated AnnData.
    """
    if not inplace:
        adata = adata.copy()

    X_raw = adata.layers[layer] if layer else adata.X
    n_cells, n_genes = adata.shape

    # ------------------------------------------------------------------ #
    # 1. Log-normalisation layer
    # ------------------------------------------------------------------ #
    print("INFO: Computing lognorm layer...")
    _compute_lognorm_layer(adata, X_raw)

    # ------------------------------------------------------------------ #
    # 2. pct_cells from raw counts (sparsity pattern unchanged by lognorm,
    #    but explicit about "expressed" meaning raw > 0)
    # ------------------------------------------------------------------ #
    print("INFO: Computing population statistics...")
    if sp.issparse(X_raw):
        pct_cells = np.asarray(X_raw.getnnz(axis=0)).ravel().astype(float) / n_cells
    else:
        pct_cells = (np.asarray(X_raw) > 0).mean(axis=0)

    # ------------------------------------------------------------------ #
    # 3. mean_expr / std_expr from lognorm
    # ------------------------------------------------------------------ #
    X_ln = adata.layers["lognorm"]
    if sp.issparse(X_ln):
        mean_expr, std_expr = _sparse_col_mean_std_chunked(X_ln, n_genes=n_genes, n_cells=n_cells)
        X_csc = None
    else:
        X_arr = np.asarray(X_ln, dtype=np.float32)
        mean_expr = X_arr.mean(axis=0)
        std_expr = X_arr.std(axis=0)
        X_csc = None

    with np.errstate(divide="ignore", invalid="ignore"):
        idf = np.where(pct_cells > 0, -np.log(pct_cells), 0.0)

    adata.var["mean_expr"] = mean_expr
    adata.var["std_expr"] = std_expr
    adata.var["pct_cells"] = pct_cells
    adata.var["idf"] = idf
    adata.var["is_low_expr"] = pct_cells < min_cells_pct

    # ------------------------------------------------------------------ #
    # 4. HVGs (uses lognorm layer — no re-normalisation needed)
    # ------------------------------------------------------------------ #
    print("INFO: Computing highly variable genes...")
    adata.var["is_hvg"] = _compute_hvg_mask(adata, n_top_hvg, pct_cells, min_cells_pct)

    # ------------------------------------------------------------------ #
    # 5. Gini on lognorm expression
    # ------------------------------------------------------------------ #
    print("INFO: Computing Gini index...")
    gini_vals = np.zeros(n_genes, dtype=float)
    if compute_gini:
        if gini_scope == "hvg":
            candidate_mask = adata.var["is_hvg"].values.astype(bool)
        elif gini_scope == "expressed":
            candidate_mask = ~adata.var["is_low_expr"].values.astype(bool)
        else:
            candidate_mask = np.ones(n_genes, dtype=bool)

        gene_indices = np.where(candidate_mask)[0]

        if sp.issparse(X_ln):
            if X_csc is None:
                X_csc = X_ln.tocsc().astype(np.float32)
            for j in tqdm(gene_indices, desc=f"Gini ({gini_scope} genes)"):
                s, e = X_csc.indptr[j], X_csc.indptr[j + 1]
                gini_vals[j] = _gini_col(X_csc.data[s:e], n_cells)
        else:
            for j in tqdm(gene_indices, desc=f"Gini ({gini_scope} genes)"):
                col = X_arr[:, j]
                gini_vals[j] = _gini_col(col[col > 0], n_cells)

    adata.var["gini"] = gini_vals

    return adata
