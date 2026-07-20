"""Stage-2 cell type refinement: LLM-queried gene programs, pathway scoring, final reasoning.

Workflow
--------
1. :func:`make_gemini_json_caller` — build a reusable JSON-mode caller (once per session).
2. :func:`query_subtype_programs` — ask the LLM for fine-grained subtype programs based
   on a stage-1 label. Also includes commonly confused neighboring cell types so pathway
   scoring can confirm or override the stage-1 call.
3. :func:`filter_programs_to_panel` — intersect gene lists with the dataset's gene panel.
4. :func:`score_gene_programs` — compute mean z-score per program for a cell.
5. :func:`build_stage2_prompt` — build the final prompt combining genes, proteins, and
   pathway scores; instructs the LLM to confirm or correct the stage-1 label.
"""

from __future__ import annotations

import json
from typing import Optional

import numpy as np
import anndata as ad


# ─── Backend factory ────────────────────────────────────────────────────────

def make_gemini_json_caller(
    model: str = "gemini-2.5-flash",
    api_key: str | None = None,
    max_output_tokens: int = 8192,
    thinking_budget: int | None = 0,
):
    """Return a callable ``(prompt, system_message) -> dict`` that queries Gemini in JSON mode.

    Using ``response_mime_type='application/json'`` activates constrained decoding,
    which guarantees structurally valid JSON output regardless of content length.

    Args:
        model: Gemini model ID (e.g. ``'gemini-2.5-flash'``, ``'gemini-2.0-flash'``).
        api_key: Google API key. Reads ``GOOGLE_API_KEY`` env var if ``None``.
        max_output_tokens: Total output token budget for each call.
        thinking_budget:
            ``0``    — disable thinking entirely (recommended for structured lookups;
                       avoids the Gemini 2.5 series consuming most of the output budget
                       on hidden chain-of-thought before a single JSON token is written).
            ``None`` — use the model default (problematic on 2.5-series with small budgets).
            ``int>0`` — explicit cap for tasks that benefit from light reasoning.
    """
    from google import genai
    from google.genai import types as _gtypes

    client = genai.Client(api_key=api_key)

    def _call(prompt: str, system_message: str = "") -> dict:
        cfg: dict = dict(
            max_output_tokens=max_output_tokens,
            temperature=0.0,
            response_mime_type="application/json",
        )
        if system_message:
            cfg["system_instruction"] = system_message
        if thinking_budget is not None:
            cfg["thinking_config"] = _gtypes.ThinkingConfig(thinking_budget=thinking_budget)

        resp = client.models.generate_content(
            model=model,
            contents=prompt,
            config=_gtypes.GenerateContentConfig(**cfg),
        )
        try:
            return json.loads(resp.text)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Gemini returned invalid JSON: {exc}\n\n"
                f"Raw response (first 500 chars):\n{resp.text[:500]}"
            ) from exc

    return _call


# ─── Step 1: query gene programs ────────────────────────────────────────────

_PROGRAM_SYSTEM = (
    "You are an expert computational biologist specializing in single-cell transcriptomics. "
    "Respond ONLY with a valid JSON object."
)


def query_subtype_programs(
    stage1_label: str,
    json_caller,
    tissue: str = "PBMC",
    n_genes: int = 50,
    stage1_reasoning: str | None = None,
) -> dict:
    """Query the LLM for fine-grained subtype programs based on a stage-1 annotation.

    The returned programs cover:
    - Fine-grained subtypes of the predicted cell type.
    - The most commonly confused neighboring cell types in the same tissue.

    This means pathway scoring can both confirm the stage-1 label (if the predicted
    subtype scores highest) and detect outright misclassifications (if a neighboring
    type scores much higher).

    Args:
        stage1_label: Cell type string from stage-1 annotation (may be approximate /
            verbose, e.g. "CD8+ Cytotoxic T Cell (likely memory/effector)").
        json_caller: Callable from :func:`make_gemini_json_caller`.
        tissue: Tissue context, e.g. ``"PBMC"``, ``"lymph node"``.
        n_genes: Requested number of marker genes per program.
        stage1_reasoning: Full rationale text from the stage-1 LLM response.
            When provided, the LLM can use it to understand *which* genes and
            proteins drove the stage-1 call, and therefore which subtypes or
            confused neighbors are most relevant to include.

    Returns:
        Raw dict ``{subtype_name: {"genes": [...], "description": "..."}}``.
        Call :func:`filter_programs_to_panel` before passing to :func:`score_gene_programs`.
    """
    reasoning_block = (
        f"\nStage-1 reasoning that led to this annotation:\n{stage1_reasoning}\n"
        if stage1_reasoning
        else ""
    )
    prompt = (
        f'A single cell in {tissue} was annotated in a first pass as: "{stage1_label}"\n'
        f"{reasoning_block}"
        f"This annotation may have minor inaccuracies, or may have been confused with a neighboring type.\n\n"
        f"Return a JSON object with gene programs for:\n"
        f"  1. The fine-grained subtypes of this cell type commonly found in {tissue}.\n"
        f"  2. The most commonly confused neighboring cell types in {tissue} — especially any\n"
        f"     types hinted at by the stage-1 reasoning above.\n\n"
        f"Each key is a subtype/cell-type name; each value contains:\n"
        f'  "genes": list anywhere from 20 to {n_genes} genes most specifically UPREGULATED in that '
        f"subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)\n"
        f'  "description": one-sentence biological description\n\n'
        f"Include 5–8 subtypes total. Focus on subtypes commonly found in {tissue}.\n"
        f"Return only the JSON."
    )
    return json_caller(prompt, _PROGRAM_SYSTEM)


# ─── Step 2: filter programs to panel ───────────────────────────────────────

def filter_programs_to_panel(programs: dict, adata: ad.AnnData) -> dict:
    """Intersect each program's gene list with genes present in ``adata``.

    Uses ``adata.var['gene_symbol']`` when available, otherwise ``adata.var_names``.

    Returns:
        ``{subtype: [genes_in_panel, ...]}``.
    """
    symbols = (
        set(adata.var["gene_symbol"].dropna().values)
        if "gene_symbol" in adata.var.columns
        else set(adata.var_names)
    )
    return {
        subtype: [g for g in info["genes"] if g in symbols]
        for subtype, info in programs.items()
    }


# ─── Step 3: pathway scoring ─────────────────────────────────────────────────

def score_gene_programs(
    adata: ad.AnnData,
    cell_indices,
    programs_in_data: dict,
    gene_mask: np.ndarray,
    min_genes: int = 3,
    method: str = "tirosh",
    n_background: int = 50,
    random_state: int = 0,
) -> dict:
    """Score a cell against gene programs.

    Three methods are supported, selectable via ``method``:

    ``'mean_z'``
        Mean of ``(expr - μ) / σ`` over program genes (vs. full dataset population).
        Simple and fast; no background correction.  Can be inflated for globally
        active cells unless the gene_mask already removes housekeeping genes.

    ``'tirosh'`` *(default)*
        Replicates Scanpy ``score_genes`` (Tirosh 2016 / AddModuleScore):
        score = mean_z(program_genes) − mean_z(control_genes), where control
        genes are randomly sampled from the same expression-level bins as the
        program genes.  This cancels out global transcriptional activity bias and
        is the standard in cell type annotation workflows.

    ``'ucell'``
        Mann-Whitney U statistic on per-cell gene ranks, normalised to [0, 1].
        rank(g) = position of gene g in the descending expression ranking of all
        genes in the cell.  U = (Σ rank(g) − n*(n+1)/2) / (n * N) where n =
        program genes, N = total expressed genes.  Rank-based and dropout-robust;
        best practice per 2024 benchmarks (Massimo et al., Bioinformatics 2024).

    Args:
        programs_in_data: ``{subtype: [gene_symbols_in_panel]}``.
        gene_mask: Boolean array ``(n_vars,)`` — True = gene passes filter.
        min_genes: Minimum scoreable genes; returns NaN otherwise.
        method: One of ``'mean_z'``, ``'tirosh'``, ``'ucell'``.
        n_background: (``'tirosh'`` only) control genes per expression bin.
        random_state: (``'tirosh'`` only) seed for background sampling.

    Returns:
        ``{subtype: float}`` — NaN when fewer than ``min_genes`` genes are scoreable.
    """
    from sc_annotation.selection import compute_scores

    if method not in ("mean_z", "tirosh", "ucell"):
        raise ValueError(f"method must be 'mean_z', 'tirosh', or 'ucell'; got {method!r}")

    if method == "ucell":
        return _score_ucell(adata, cell_indices, programs_in_data, gene_mask, min_genes)

    z = compute_scores(adata, cell_indices, "zscore", gene_mask, mask_zeros=False)
    assert np.all(np.isfinite(z[gene_mask])), "infinite z-scores identified"

    # Precompute bin mapping once — shared across all programs in this call
    if method == "tirosh":
        rng = np.random.default_rng(random_state)
        mean_expr = adata.var["mean_expr"][gene_mask]
        bin_ids = _gene_to_bin(mean_expr)
        gene_to_bin_map = {g: int(b) for g, b in bin_ids.items() if not np.isnan(b)}
        bin_pool = _build_background_pool(mean_expr)

    out: dict = {}
    for subtype, genes in programs_in_data.items():
        valid = [g for g in genes if g in z.index and np.isfinite(z[g])]
        if len(valid) < min_genes:
            out[subtype] = float("nan")
            continue

        prog_score = float(z[valid].mean())
        if method == "tirosh":
            ctrl = _sample_background(valid, gene_to_bin_map, bin_pool, n_background, rng)

            if ctrl:
                ctrl_vals = z[ctrl].values
                assert np.all(np.isfinite(ctrl_vals)), "infinite z-scores identified in control genes"
                ctrl_score = float(ctrl_vals.mean())
            else:
                ctrl_score = 0.0
            out[subtype] = prog_score - ctrl_score
        else:
            out[subtype] = prog_score
    return out


def _gene_to_bin(z: "pd.Series", n_bins: int = 25) -> "pd.Series":
    """Map each finite-z gene to an expression-level bin index (0-based).

    Uses quantile bins (equal-population per bin) so no bin is empty,
    which avoids a common failure mode of equal-width binning on skewed data.
    """
    import pandas as pd

    finite = z[np.isfinite(z)]
    return pd.qcut(finite, q=n_bins, labels=False, duplicates="drop")


def _build_background_pool(z: "pd.Series", n_bins: int = 25) -> dict:
    """Return {bin_id: [gene_symbols]} for all expressed genes."""
    bin_ids = _gene_to_bin(z, n_bins)
    pool: dict = {}
    for gene, b in bin_ids.items():
        if not np.isnan(b):
            pool.setdefault(int(b), []).append(gene)
    return pool


def _sample_background(
    program_genes: list,
    gene_to_bin_map: dict,
    bin_pool: dict,
    n_per_gene: int,
    rng: "np.random.Generator",
) -> list:
    """For each program gene, draw n_per_gene controls from the same expression bin."""
    prog_set = set(program_genes)
    ctrl: list = []
    for g in program_genes:
        b = gene_to_bin_map.get(g)
        if b is None:
            continue
        candidates = [c for c in bin_pool.get(b, []) if c not in prog_set]
        if candidates:
            k = min(n_per_gene, len(candidates))
            ctrl.extend(rng.choice(candidates, size=k, replace=False).tolist())
    return list(set(ctrl))


def _score_ucell(
    adata: ad.AnnData,
    cell_indices,
    programs_in_data: dict,
    gene_mask: np.ndarray | None,
    min_genes: int,
) -> dict:
    """UCell: normalised Mann-Whitney U on per-cell z-score ranks.

    For a program of n genes ranked among N genes with finite z-score:
        U_norm = 1 − (sum_of_ranks − n*(n+1)/2) / (n * N)
    Score is in [0, 1]; 1.0 means all program genes rank at the top of the cell.

    Ranking is done on population z-scores (using the pre-computed mean_expr /
    std_expr in adata.var) rather than raw expression, so that constitutively
    highly-expressed housekeeping genes do not dominate the ranking — consistent
    with how mean_z and tirosh treat cell-specific signal.

    The rank universe is all genes with a finite z-score (gene_mask=None so N is
    stable across programs). The mask is used only to decide which program genes
    are eligible to contribute to a program's score.
    """
    from sc_annotation.selection import compute_scores

    # Z-score the cell against the full population — uses pre-computed mean_expr /
    # std_expr, consistent with mean_z and tirosh.  No mask here so N is the full
    # set of expressed genes and ranks are comparable across programs.
    #
    # mask_zeros=False is required for correctness: with masking, unexpressed genes
    # become -inf, which .rank() still orders (so ranks span all n_vars genes) while
    # N below counts only the finite ones.  The mismatched denominator pushed scores
    # far outside [0, 1] and made them scale with each cell's expressed-gene count.
    # Unmasked, every z is finite, N == len(ranks), and unexpressed genes are ordered
    # by their z-score instead of collapsing into a single bottom tie.
    z_unmasked = compute_scores(adata, cell_indices, "zscore", gene_mask=None, mask_zeros=False)

    # Rank descending: rank 1 = highest z-score (most cell-specific)
    ranks = z_unmasked.rank(ascending=False, method="average")
    N = int(np.isfinite(z_unmasked.values).sum())  # genes with a finite z-score

    # Build set of allowed gene symbols from gene_mask
    if gene_mask is not None:
        var_names = (
            adata.var["gene_symbol"].values
            if "gene_symbol" in adata.var.columns
            else np.asarray(adata.var_names)
        )
        allowed = set(var_names[gene_mask])
    else:
        allowed = None

    out: dict = {}
    for subtype, genes in programs_in_data.items():
        valid = [
            g for g in genes
            if g in ranks.index
            and (allowed is None or g in allowed)
        ]
        
        if len(valid) < min_genes or N == 0:
            out[subtype] = float("nan")
            continue
            
        n = len(valid)
        sum_ranks = float(ranks[valid].sum())
        u_norm = 1.0 - (sum_ranks - n * (n + 1) / 2) / (n * N)
        out[subtype] = float(u_norm)
    return out


# ─── Step 4: stage-2 prompt ──────────────────────────────────────────────────

def build_stage2_prompt(
    stage1_label: str,
    pathway_scores: dict,
    *,
    stage1_reasoning: str | None = None,
    genes_by_expr: list | None = None,
    genes_by_zscore: list | None = None,
    genes_by_tfidf: list | None = None,
    proteins: list | None = None,
    tissue: str = "PBMC",
    n_genes: int = 30,
    n_proteins: int = 15,
) -> str:
    """Build a stage-2 cell type refinement prompt.

    Combines the full stage-1 output (label + reasoning), per-modality gene lists
    (expression, z-score, TF-IDF), optional surface protein markers, and the
    pathway score table. The LLM is instructed to confirm or override the stage-1
    call based on the complete evidence.

    Args:
        stage1_label: Stage-1 predicted cell type (may be verbose / approximate).
        pathway_scores: ``{subtype: score}`` from :func:`score_gene_programs`.
        stage1_reasoning: Full rationale text from the stage-1 LLM response.
            Shown as prior context so the LLM can see what evidence the first
            pass already interpreted.
        genes_by_expr: ``[(gene, expr), ...]`` sorted by raw expression descending.
        genes_by_zscore: ``[(gene, z_score), ...]`` sorted by z-score descending.
        genes_by_tfidf: ``[(gene, tfidf), ...]`` sorted by TF-IDF descending.
        proteins: Optional ``[(protein, z_score), ...]`` from ADT.
        tissue: Tissue context string.
        n_genes: Number of top genes to include per modality.
        n_proteins: Number of top proteins to include.

    Returns:
        User-facing prompt string.
    """
    parts: list[str] = []
    parts.append(f"Tissue context: {tissue}\n")

    parts.append(
        f'Stage-1 annotation: "{stage1_label}"'
        f" — may have minor inaccuracies. "
        f"Use the evidence below to confirm or correct it."
    )
    if stage1_reasoning:
        parts.append(f"\nStage-1 reasoning:\n{stage1_reasoning}")

    if genes_by_expr:
        parts.append(f"\nTop {n_genes} genes by raw expression:")
        for rank, (gene, val) in enumerate(genes_by_expr[:n_genes], 1):
            parts.append(f"  {rank:3d}. {gene:<10s}  ({int(val)})")

    if genes_by_zscore:
        parts.append(
            f"\nTop {n_genes} cell-specific genes by z-score vs. population "
            f"(higher = more specific to this cell):"
        )
        for rank, (gene, z) in enumerate(genes_by_zscore[:n_genes], 1):
            parts.append(f"  {rank:3d}. {gene:<10s}  z={z:+.2f}")

    if genes_by_tfidf:
        parts.append(
            f"\nTop {n_genes} cell-specific genes by TF-IDF "
            f"(weights by rarity across cells — highlights rare but highly expressed genes):"
        )
        for rank, (gene, _) in enumerate(genes_by_tfidf[:n_genes], 1):
            parts.append(f"  {rank:3d}. {gene}")

    if proteins:
        parts.append("\nSurface proteins (z-score vs. population):")
        for rank, (prot, z) in enumerate(proteins[:n_proteins], 1):
            parts.append(f"  {rank:3d}. {prot:<15s}  z={z:+.2f}")

    valid = sorted(
        [(k, v) for k, v in pathway_scores.items() if np.isfinite(v)],
        key=lambda x: -x[1],
    )
    parts.append(
        "\nPathway scores (LLM-defined gene programs scored against this cell; "
        "higher = more active program):"
    )
    for subtype, score in valid:
        parts.append(f"  {subtype:<25s}: {score:+.3f}")

    parts.append(
        "\nConsidering all of the above — genes (across all scoring methods), "
        "surface proteins, pathway scores, and the stage-1 reasoning — "
        "confirm or correct the stage-1 annotation and give the most specific subtype. "
        "Trust direct gene/protein evidence over the stage-1 label when they conflict.\n"
        "Line 1: final cell type / subtype.  Line 2: brief rationale (<100 words)."
    )
    return "\n".join(parts)
