"""Data loading and preparation utilities for single-cell annotation."""

from __future__ import annotations

import numpy as np
import pandas as pd
import scipy.sparse as sp
import anndata as ad
from typing import Optional


def load_dataset(
    h5ad_path: str,
    tissue: Optional[str] = None,
    labels_path: Optional[str] = None,
    label_col: Optional[str] = None,
) -> ad.AnnData:
    """Load an AnnData dataset, optionally attaching labels from a CSV file.

    Args:
        h5ad_path: Path to .h5ad file.
        tissue: Optional tissue context.
        labels_path: Optional path to a CSV with cell labels (index = cell barcodes).
        label_col: Column in labels CSV to use as primary label. If None, all
                   columns from the CSV are merged into obs.

    Returns:
        AnnData with labels attached to obs when labels_path is provided.
    """
    adata = ad.read_h5ad(h5ad_path, backed="r")

    if h5ad_path.endswith("hlca_core.h5ad"):
        # For HLCA, we want to filter to the specified tissue context
        if tissue is not None and str(tissue).strip():
            if "tissue" not in adata.obs.columns:
                raise ValueError(
                    f"Dataset {h5ad_path} does not have a 'tissue' column in obs."
                )
            mask = (adata.obs["tissue"] == tissue).to_numpy()
            if mask.sum() == 0:
                raise ValueError(
                    f"No cells found for tissue '{tissue}' in dataset {h5ad_path}."
                )
            adata = adata[mask].to_memory()
            print(f"  Filtered to tissue '{tissue}': {adata.shape[0]:,} / {mask.sum():,} cells remain.")
        else:
            raise ValueError(
                f"Dataset {h5ad_path} is HLCA, but no tissue context was provided."
            )
    else: 
        adata = adata.to_memory() 

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
    cell_type_list: Optional[list[str]] = None,

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
        cell_type_list.append(ct)
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


def inspect_cells(
    adata: ad.AnnData,
    label_col: str,
    cell_indices: list[int],
    cell_type_list: Optional[list[str]] = None,
) -> pd.DataFrame:
    """Extract specific cells by global cell_idx for inspect mode.

    Args:
        adata: AnnData object with labels in obs.
        label_col: Column in obs containing cell type labels.
        cell_indices: Global integer cell indices to extract.

    Returns:
        DataFrame with columns ['cell_idx', 'cell_barcode', 'true_label'],
        preserving the input order after removing duplicates.
    """
    if not cell_indices:
        raise ValueError(
            "inspect.enabled=true but inspect.cell_indices is empty. "
            "Please provide at least one global cell_idx to inspect."
        )

    invalid_indices = [idx for idx in cell_indices if idx < 0 or idx >= adata.n_obs]
    if invalid_indices:
        raise ValueError(
            "inspect.cell_indices contains out-of-range cell_idx values: "
            f"{invalid_indices}"
        )

    labels = adata.obs[label_col]

    ordered_unique_indices: list[int] = []
    seen_indices: set[int] = set()
    for cell_idx in cell_indices:
        if cell_idx not in seen_indices:
            ordered_unique_indices.append(cell_idx)
            seen_indices.add(cell_idx)

    records = []
    for cell_idx in ordered_unique_indices:
        cell_type = labels.iloc[cell_idx]
        if cell_type not in cell_type_list:
            cell_type_list.append(cell_type)
        records.append(
            {
                "cell_idx": int(cell_idx),
                "cell_barcode": adata.obs_names[cell_idx],
                "true_label": labels.iloc[cell_idx],
            }
        )

    return pd.DataFrame(records)
