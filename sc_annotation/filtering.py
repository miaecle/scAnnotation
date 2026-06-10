"""Gene-level boolean annotation and filter masks (Axis 3 — Feature Filtering).

Two-step usage
--------------
1. :func:`annotate_genes` — writes boolean flags to ``adata.var`` based on gene
   names.  Idempotent; called automatically by :func:`build_gene_mask`.
2. :func:`build_gene_mask` — combines stored flags and quantitative thresholds
   from ``adata.var`` (set by
   :func:`~sc_annotation.global_metrics.compute_global_metrics`) into a
   boolean inclusion mask.

Flags written by :func:`annotate_genes`
-----------------------------------------
- ``is_mt``      — mitochondrial (``MT-`` prefix)
- ``is_ribo``    — ribosomal large/small subunit (``RPL``/``RPS`` prefix)
- ``is_hb``      — haemoglobin subunit (curated list)
- ``is_tcr_vdj`` — TCR/Ig variable, joining, and diversity segments (curated prefixes)
- ``is_sex_chr`` — sex-chromosome markers (curated list)
"""

from __future__ import annotations

import numpy as np
import anndata as ad


# ---------------------------------------------------------------------------
# Curated gene lists
# ---------------------------------------------------------------------------

_HB_GENES: frozenset[str] = frozenset([
    "HBA1", "HBA2", "HBB", "HBD", "HBE1", "HBG1", "HBG2",
    "HBM", "HBQ1", "HBZ", "HBZP1",
])

_SEX_CHR_GENES: frozenset[str] = frozenset([
    "XIST", "TSIX",
    "RPS4Y1", "RPS4Y2", "DDX3Y", "UTY", "TMSB4Y", "NLGN4Y",
    "KDM5D", "ZFY", "USP9Y", "EIF1AY", "PRKY", "PCDH11Y",
    "AMELY", "SRY", "DAZ1", "DAZ2", "DAZ3", "DAZ4",
])

_TCR_VDJ_PREFIXES: tuple[str, ...] = (
    "TRAV", "TRBV", "TRDV", "TRGV",
    "TRAJ", "TRBJ", "TRDJ", "TRGJ",
    "TRBD", "TRDD",
)

# Constant-region Ig genes (IGHG*, IGHA*, IGHM, IGKC, IGLC*) are intentionally
# kept — they are informative cell-type markers (e.g. plasma cells).
_IG_VDJ_PREFIXES: tuple[str, ...] = (
    "IGHV", "IGKV", "IGLV",
    "IGHJ", "IGKJ", "IGLJ",
)

_IG_DIVERSITY_PREFIX = "IGHD"


def _is_ig_diversity(name: str) -> bool:
    """True for IGHD diversity segments (e.g. IGHD3-10), not the IGHD isotype gene."""
    if name.startswith(_IG_DIVERSITY_PREFIX) and len(name) > len(_IG_DIVERSITY_PREFIX):
        return name[len(_IG_DIVERSITY_PREFIX)].isdigit()
    return False


def _gene_upper(adata: ad.AnnData) -> np.ndarray:
    names = (
        adata.var["gene_symbol"].values
        if "gene_symbol" in adata.var.columns
        else np.asarray(adata.var_names)
    )
    return np.array([str(g).upper() for g in names])


# ---------------------------------------------------------------------------
# Gene annotation
# ---------------------------------------------------------------------------

_ANNOTATION_COLS: frozenset[str] = frozenset(
    ["is_mt", "is_ribo", "is_hb", "is_tcr_vdj", "is_sex_chr"]
)


def annotate_genes(adata: ad.AnnData, inplace: bool = True) -> ad.AnnData:
    """Annotate ``adata.var`` with boolean gene-type flags based on gene names.

    Idempotent — safe to call multiple times.  Writes five columns:

    - ``is_mt``      — ``True`` for mitochondrial genes (``MT-`` prefix)
    - ``is_ribo``    — ``True`` for ribosomal genes (``RPL``/``RPS`` prefix)
    - ``is_hb``      — ``True`` for haemoglobin subunit genes
    - ``is_tcr_vdj`` — ``True`` for TCR / Ig variable, joining, and diversity
      segments.  Ig constant-region genes are **not** flagged.
    - ``is_sex_chr`` — ``True`` for sex-chromosome marker genes

    These flags are consumed by :func:`build_gene_mask`.  Call this function
    (or let :func:`build_gene_mask` call it automatically) before filtering.

    Args:
        adata: AnnData object.
        inplace: Modify ``adata`` in place.  If ``False``, return a copy.

    Returns:
        Annotated AnnData (same object when ``inplace=True``).
    """
    if not inplace:
        adata = adata.copy()

    gu = _gene_upper(adata)

    adata.var["is_mt"] = np.array([g.startswith("MT-") for g in gu])
    adata.var["is_ribo"] = np.array(
        [g.startswith("RPL") or g.startswith("RPS") for g in gu]
    )
    adata.var["is_hb"] = np.array([g in _HB_GENES for g in gu])
    adata.var["is_tcr_vdj"] = np.array([
        any(g.startswith(p) for p in _TCR_VDJ_PREFIXES + _IG_VDJ_PREFIXES)
        or _is_ig_diversity(g)
        for g in gu
    ])
    adata.var["is_sex_chr"] = np.array([g in _SEX_CHR_GENES for g in gu])

    return adata


def _ensure_annotated(adata: ad.AnnData) -> None:
    if not _ANNOTATION_COLS.issubset(set(adata.var.columns)):
        annotate_genes(adata)


# ---------------------------------------------------------------------------
# Filter mask
# ---------------------------------------------------------------------------

def build_gene_mask(adata: ad.AnnData, filter_config) -> np.ndarray:
    """Build a boolean gene inclusion mask from a
    :class:`~sc_annotation.config.FilterConfig`.

    ``True`` at index *j* means gene *j* should be included in LLM prompts.

    Calls :func:`annotate_genes` automatically if the flag columns are absent.
    Quantitative thresholds (``is_low_expr``, ``gini``) are read from
    ``adata.var`` when present — they require
    :func:`~sc_annotation.global_metrics.compute_global_metrics` to have been
    called first.

    Args:
        adata: AnnData object.
        filter_config: :class:`~sc_annotation.config.FilterConfig` instance.

    Returns:
        Boolean ndarray of shape ``(n_genes,)``.
    """
    _ensure_annotated(adata)

    mask = np.ones(adata.n_vars, dtype=bool)
    var = adata.var

    # Name-based flags (from annotate_genes)
    if filter_config.exclude_mt:
        mask &= ~var["is_mt"].values.astype(bool)
    if filter_config.exclude_ribo:
        mask &= ~var["is_ribo"].values.astype(bool)
    if filter_config.exclude_hb:
        mask &= ~var["is_hb"].values.astype(bool)
    if filter_config.exclude_tcr_ig:
        mask &= ~var["is_tcr_vdj"].values.astype(bool)
    if filter_config.exclude_sex_chr:
        mask &= ~var["is_sex_chr"].values.astype(bool)

    # Quantitative thresholds (from compute_global_metrics)
    if filter_config.exclude_low_expr and "is_low_expr" in var.columns:
        mask &= ~var["is_low_expr"].values.astype(bool)

    if filter_config.gini_min is not None and "gini" in var.columns:
        gini = var["gini"].values.astype(float)
        mask &= ~((gini > 0) & (gini < filter_config.gini_min))

    return mask


def summarise_mask(adata: ad.AnnData, mask: np.ndarray) -> dict:
    """Return a human-readable breakdown of how many genes each filter removed.

    Args:
        adata: AnnData with gene flags and quantitative metrics in ``var``.
        mask: Boolean inclusion mask as returned by :func:`build_gene_mask`.

    Returns:
        Dict with keys ``total``, ``included``, and ``excluded_by`` sub-dict.
    """
    _ensure_annotated(adata)
    excluded = ~mask
    summary: dict = {"total": adata.n_vars, "included": int(mask.sum()), "excluded_by": {}}

    var = adata.var
    for col in ("is_mt", "is_ribo", "is_hb", "is_tcr_vdj", "is_sex_chr",
                "is_low_expr"):
        if col in var.columns:
            summary["excluded_by"][col] = int(
                (var[col].values.astype(bool) & excluded).sum()
            )

    if "gini" in var.columns:
        gini = var["gini"].values.astype(float)
        summary["excluded_by"]["gini_housekeeping"] = int(
            ((gini > 0) & excluded).sum()
        )

    return summary
