"""Prompt builders for LLM-based cell type annotation."""

from __future__ import annotations

SYSTEM_PROMPT = """\
You are an expert computational biologist specializing in single-cell transcriptomics and proteomics. \
Your task is to identify cell types based on their gene and protein expression profiles. \
Respond with the cell type name in the first line, then in the second line provide very brief explanation (<100 words). \
"""


def build_naive_prompt(
    genes: list[tuple[str, float]],
    proteins: list[tuple[str, float]] | None = None,
    tissue: str | None = None,
) -> str:
    """Build a naive baseline prompt from top expressed genes (and optionally proteins).

    Args:
        genes: List of (gene_name, count) sorted by expression descending.
        proteins: Optional list of (protein_name, count) sorted by count descending.
        tissue: Optional tissue context (e.g. 'PBMC', 'lymph node').

    Returns:
        User-facing prompt string.
    """
    parts: list[str] = []

    if tissue:
        parts.append(f"Tissue context: {tissue}\n")

    parts.append("Top expressed genes (ranked by expression level):")
    for rank, (gene, count) in enumerate(genes, 1):
        parts.append(f"  {rank:3d}. {gene} ({int(count)})")

    if proteins:
        parts.append("\nTop expressed surface proteins / ADT markers (ranked by count):")
        for rank, (protein, count) in enumerate(proteins, 1):
            parts.append(f"  {rank:3d}. {protein} ({int(count)})")

    parts.append(
        "\nBased on the expression profile above, what is the cell type? "
        "Respond with the cell type name in the first line, then in the second line provide very brief explanation (<100 words)."
    )

    return "\n".join(parts)


def build_enriched_prompt(
    genes_by_expr: list[tuple[str, float]] | None = None,
    genes_by_zscore: list[tuple[str, float]] | None = None,
    genes_by_tfidf: list[tuple[str, float]] | None = None,
    proteins: list[tuple[str, float]] | None = None,
    tissue: str | None = None,
    genes: list[tuple[str, float]] | None = None,
) -> str:
    """Build an enriched prompt using both expression-ranked and z-score-ranked genes.

    MT, ribosomal, and low-expression genes should already be excluded from
    both lists (see :func:`sc_annotation.data.get_top_genes_filtered` and
    :func:`sc_annotation.data.get_top_genes_by_zscore`).

    Args:
        genes_by_expr: Top genes ranked by raw expression (name, count).
            Can also be passed as ``genes`` (alias, for drop-in compatibility
            with :func:`build_naive_prompt`).
        genes_by_zscore: Top genes ranked by z-score (name, z_score).
            When provided, shown as a second ranked list in the prompt.
        genes_by_tfidf: Top genes ranked by TF-IDF (name, tfidf_score).
            When provided, shown as a third ranked list in the prompt.
        proteins: Optional list of (protein_name, count) sorted descending.
        tissue: Optional tissue context string.
        genes: Alias for ``genes_by_expr`` (used when called via
               :class:`~sc_annotation.annotator.CellAnnotator` as ``prompt_fn``).

    Returns:
        User-facing prompt string.
    """
    if genes is not None and genes_by_expr is None:
        genes_by_expr = genes
    if genes_by_expr is None:
        genes_by_expr = []
    parts: list[str] = []

    if tissue:
        parts.append(f"Tissue context: {tissue}\n")

    parts.append(
        "Top expressed genes (ranked by raw expression; "
        "mitochondrial, ribosomal, and low-expression genes excluded):"
    )
    for rank, (gene, count) in enumerate(genes_by_expr, 1):
        parts.append(f"  {rank:3d}. {gene} ({int(count)})")

    if genes_by_zscore:
        parts.append(
            "\nTop cell-specific genes (ranked by z-score vs. all cells; "
            "higher z-score = more specific to this cell relative to the population):"
        )
        for rank, (gene, z) in enumerate(genes_by_zscore, 1):
            parts.append(f"  {rank:3d}. {gene} (z={z:.2f})")

    if genes_by_tfidf:
        parts.append(
            "\nTop cell-specific genes (ranked by TF-IDF vs. all cells; "
            "higher TF-IDF = more specific to this cell relative to the population):"
        )
        for rank, (gene, score) in enumerate(genes_by_tfidf, 1):
            parts.append(f"  {rank:3d}. {gene}")

    if proteins:
        parts.append("\nTop expressed surface proteins / ADT markers (ranked by count):")
        for rank, (protein, count) in enumerate(proteins, 1):
            parts.append(f"  {rank:3d}. {protein} ({int(count)})")

    parts.append(
        "\nBased on the expression profile above, what is the cell type? "
        "Respond with the cell type name in the first line, then in the second line provide very brief explanation (<100 words)."
    )

    return "\n".join(parts)


def build_marker_panel_prompt(
    pos_expressed: list[tuple[str, float]],
    neg_expressed: list[tuple[str, float]],
    top_genes: list[tuple[str, float]] | None = None,
    proteins: list[tuple[str, float]] | None = None,
    tissue: str | None = None,
    genes: list[tuple[str, float]] | None = None,
) -> str:
    """Build a prompt centred on a curated lineage-marker panel.

    Args:
        pos_expressed: (gene, count) for positive-panel genes detected.
        neg_expressed: (gene, count) for negative-panel genes detected (surprising).
        top_genes: Optional additional ranked genes for supplementary context.
        proteins: Optional ADT protein counts.
        tissue: Optional tissue context.
        genes: Alias for top_genes (drop-in compat with other prompt fns).

    Returns:
        User-facing prompt string.
    """
    if genes is not None and top_genes is None:
        top_genes = genes

    parts: list[str] = []
    if tissue:
        parts.append(f"Tissue context: {tissue}\n")

    parts.append("Lineage marker expression panel:")
    if pos_expressed:
        parts.append("  Positive-panel markers detected (expression level):")
        for gene, count in sorted(pos_expressed, key=lambda x: -x[1]):
            fmt = int(count) if count >= 1 else f"{count:.3f}"
            parts.append(f"    {gene}: {fmt}")
    else:
        parts.append("  Positive-panel markers: (none detected)")

    if neg_expressed:
        parts.append("  Negative-panel markers unexpectedly detected:")
        for gene, count in sorted(neg_expressed, key=lambda x: -x[1]):
            fmt = int(count) if count >= 1 else f"{count:.3f}"
            parts.append(f"    {gene}: {fmt}")

    if top_genes:
        parts.append("\nTop additional expressed genes (supplementary context):")
        for rank, (gene, val) in enumerate(top_genes, 1):
            fmt = int(val) if val >= 1 else f"{val:.3f}"
            parts.append(f"  {rank:3d}. {gene} ({fmt})")

    if proteins:
        parts.append("\nTop expressed surface proteins / ADT markers:")
        for rank, (protein, count) in enumerate(proteins, 1):
            parts.append(f"  {rank:3d}. {protein} ({int(count)})")

    parts.append(
        "\nBased on the marker expression profile above, what is the cell type? "
        "Respond with the cell type name in the first line, then in the second line provide very brief explanation (<100 words)."
    )
    return "\n".join(parts)
