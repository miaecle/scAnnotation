"""Cell-level expression smoothing (Axis 2 — Input Entity).

Three modes are supported:

``single_cell``
    Use the raw expression vector of one cell (default).

``knn_smoothed``
    Average expression over a cell's *k* nearest neighbours (plus itself).
    Call :func:`build_knn_index` once, then :func:`get_knn_indices` per cell
    to get the group of indices to pass to :func:`~sc_annotation.selection.compute_scores`.

``pseudobulk``
    Average all cells of the same true label.
    Call :func:`compute_pseudobulk` once to get a ``{label: [idx, ...]}`` mapping,
    then pass the relevant index list to :func:`~sc_annotation.selection.compute_scores`.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import scipy.sparse as sp
import anndata as ad


# ---------------------------------------------------------------------------
# kNN index
# ---------------------------------------------------------------------------

def build_knn_index(
    adata: ad.AnnData,
    k: int,
    use_rep: Optional[str] = "X_pca",
    inplace: bool = True,
) -> np.ndarray:
    """Build a kNN index and return a neighbour-index matrix of shape ``(n_cells, k)``.

    Results are cached in ``adata.uns`` under the key
    ``'knn_k{k}_{use_rep}'`` so repeated calls are free.

    Args:
        adata: AnnData object.
        k: Number of nearest neighbours (the cell itself is excluded).
        use_rep: Key in ``adata.obsm`` to use as the embedding.
            ``'X_pca'`` is the default; if not found, PCA is computed on
            the fly from log1p-normalised HVG expression and stored in
            ``adata.obsm['X_pca']`` for future calls.
            Pass ``None`` to always compute PCA on the fly.
        inplace: If True, cache the neighbour matrix in ``adata.uns``.

    Returns:
        Integer array of shape ``(n_cells, k)`` — neighbour cell indices.
    """
    cache_key = f"knn_k{k}_{use_rep}"
    if cache_key in adata.uns:
        return np.asarray(adata.uns[cache_key])

    X_embed = _get_embedding(adata, use_rep)

    from sklearn.neighbors import NearestNeighbors
    nn = NearestNeighbors(n_neighbors=k + 1, algorithm="auto", n_jobs=-1)
    print(f"INFO: Building kNN index with k={k} on embedding '{use_rep}'...")
    nn.fit(X_embed)
    _, indices = nn.kneighbors(X_embed)
    neighbors = indices[:, 1:]  # drop column 0 (self)

    if inplace:
        adata.uns[cache_key] = neighbors.tolist()

    return neighbors


def _get_embedding(adata: ad.AnnData, use_rep: Optional[str] = "X_pca") -> np.ndarray:
    """Return the cell embedding; compute PCA if ``use_rep`` is not in obsm."""
    if use_rep is not None and use_rep in adata.obsm:
        return np.asarray(adata.obsm[use_rep])
    return _compute_pca_embedding(adata)


def _compute_pca_embedding(adata: ad.AnnData, n_comps: int = 50) -> np.ndarray:
    """Compute PCA on HVGs of the lognorm layer, store in ``adata.obsm['X_pca']``, and return it.

    Uses ``adata.layers['lognorm']`` if available; otherwise falls back to
    normalising ``adata.X`` on the fly.
    """
    import warnings
    import anndata as _ad
    import scanpy as sc

    if "lognorm" in adata.layers:
        X_ln = adata.layers["lognorm"]
        if "is_hvg" in adata.var.columns:
            hvg_mask = adata.var["is_hvg"].values.astype(bool)
            X_ln = X_ln[:, hvg_mask]
        tmp = _ad.AnnData(X=X_ln.copy() if sp.issparse(X_ln) else np.asarray(X_ln, dtype=float).copy())
    else:
        tmp = _ad.AnnData(X=adata.X.copy() if sp.issparse(adata.X) else np.asarray(adata.X, dtype=float).copy())
        tmp.var_names = adata.var_names
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sc.pp.normalize_total(tmp, target_sum=1e4)
            sc.pp.log1p(tmp)
        if "is_hvg" in adata.var.columns:
            hvg_mask = adata.var["is_hvg"].values.astype(bool)
            tmp = tmp[:, hvg_mask]
        elif tmp.n_vars > 3000:
            X_arr = tmp.X
            if sp.issparse(X_arr):
                var_g = np.asarray(
                    X_arr.power(2).mean(axis=0) - np.asarray(X_arr.mean(axis=0)) ** 2
                ).ravel()
            else:
                var_g = X_arr.var(axis=0)
            tmp = tmp[:, np.argpartition(var_g, -3000)[-3000:]]

    n_comps_actual = min(n_comps, tmp.n_vars - 1)
    print(f"INFO: Computing PCA embedding with {n_comps_actual} components...")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sc.pp.pca(tmp, n_comps=n_comps_actual)

    embedding = np.asarray(tmp.obsm["X_pca"])
    adata.obsm["X_pca"] = embedding
    return embedding


# ---------------------------------------------------------------------------
# kNN group indices
# ---------------------------------------------------------------------------

def get_knn_indices(
    cell_idx: int,
    neighbor_matrix: np.ndarray,
    k: Optional[int] = None,
) -> list[int]:
    """Return a cell and its k nearest neighbours as a list of indices.

    The returned list can be passed directly to
    :func:`~sc_annotation.selection.compute_scores` as ``cell_indices``.

    Args:
        cell_idx: Integer index of the target cell.
        neighbor_matrix: ``(n_cells, max_k)`` neighbour index matrix from
            :func:`build_knn_index`.
        k: Use only the first ``k`` neighbours.  If None, use all columns.

    Returns:
        ``[cell_idx, nn_0, nn_1, ..., nn_{k-1}]``
    """
    nn = neighbor_matrix[cell_idx]
    if k is not None:
        nn = nn[:k]
    return [cell_idx] + [int(_nn) for _nn in list(nn)]


# ---------------------------------------------------------------------------
# Pseudobulk group indices
# ---------------------------------------------------------------------------

def compute_pseudobulk(
    adata: ad.AnnData,
    label_col: str,
) -> dict[str, list[int]]:
    """Return cell indices grouped by cell type label.

    Each value is the list of row indices in ``adata`` that share that label.
    Pass the list for a given label directly to
    :func:`~sc_annotation.selection.compute_scores` as ``cell_indices`` to
    compute pseudobulk scores.

    Args:
        adata: AnnData with labels in ``obs``.
        label_col: Column in ``obs`` containing cell type labels.

    Returns:
        ``{label: [idx, ...]}`` — one list of ints per unique label.
    """
    labels = adata.obs[label_col]
    return {
        ct: list(np.where(labels == ct)[0])
        for ct in sorted(labels.unique())
    }
