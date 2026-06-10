"""Data loading and preparation utilities for single-cell annotation."""

from __future__ import annotations

import numpy as np
import pandas as pd
import scipy.sparse as sp
import anndata as ad
from typing import Optional


def load_dataset(
    h5ad_path: str,
    labels_path: Optional[str] = None,
    label_col: Optional[str] = None,
) -> ad.AnnData:
    """Load an AnnData dataset, optionally attaching labels from a CSV file.

    Args:
        h5ad_path: Path to .h5ad file.
        labels_path: Optional path to a CSV with cell labels (index = cell barcodes).
        label_col: Column in labels CSV to use as primary label. If None, all
                   columns from the CSV are merged into obs.

    Returns:
        AnnData with labels attached to obs when labels_path is provided.
    """
    adata = ad.read_h5ad(h5ad_path)

    if labels_path is not None:
        labels_df = pd.read_csv(labels_path, index_col=0)
        # align on index
        labels_df = labels_df.reindex(adata.obs_names)
        for col in labels_df.columns:
            adata.obs[col] = labels_df[col].values

    return adata



def get_top_proteins(
    adata: ad.AnnData,
    cell_idx: int,
    n_top: int = 20,
    protein_key: str = "protein_counts",
    protein_names_key: str = "ADT_names",
) -> list[tuple[str, float]]:
    """Return the top-N most highly expressed proteins for a single cell.

    Returns an empty list if no protein data is available.

    Args:
        adata: AnnData object with protein counts stored in obsm.
        cell_idx: Integer index of the cell.
        n_top: Number of top proteins to return.
        protein_key: Key in adata.obsm for protein counts.
        protein_names_key: Key in adata.uns for protein names array.

    Returns:
        List of (protein_name, count) tuples sorted by count descending,
        or [] if the dataset has no protein data.
    """
    if protein_key not in adata.obsm:
        return []

    counts = np.asarray(adata.obsm[protein_key][cell_idx]).squeeze()
    protein_names = np.asarray(adata.uns[protein_names_key])

    top_idx = np.argsort(counts)[::-1][:n_top]
    top_idx = [i for i in top_idx if counts[i] > 0][:n_top]

    return [(protein_names[i], float(counts[i])) for i in top_idx]



def sample_cells(
    adata: ad.AnnData,
    label_col: str,
    n_per_class: int = 5,
    cell_types: Optional[list[str]] = None,
    seed: int = 42,
) -> pd.DataFrame:
    """Sample cells from each cell type.

    Args:
        adata: AnnData object with labels in obs.
        label_col: Column in obs containing cell type labels.
        n_per_class: Number of cells to sample per class.
        cell_types: If provided, only sample from these cell types.
        seed: Random seed for reproducibility.

    Returns:
        DataFrame with columns ['cell_idx', 'cell_barcode', 'true_label'],
        where cell_idx is the integer position in adata.
    """
    rng = np.random.default_rng(seed)
    labels = adata.obs[label_col]

    if cell_types is None:
        cell_types = sorted(labels.unique().tolist())

    records = []
    for ct in cell_types:
        mask = labels == ct
        positions = np.where(mask)[0]
        if len(positions) == 0:
            continue
        chosen = rng.choice(
            positions,
            size=min(n_per_class, len(positions)),
            replace=False,
        )
        for idx in chosen:
            records.append(
                {
                    "cell_idx": int(idx),
                    "cell_barcode": adata.obs_names[idx],
                    "true_label": ct,
                }
            )

    return pd.DataFrame(records)
