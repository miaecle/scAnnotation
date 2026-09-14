"""Experiment configuration — dataclasses + YAML serialisation.

Quick start::

    config = ExperimentConfig.from_yaml('configs/pbmc_l1_zscore_gemini.yaml')
    config.to_yaml('results/my_run_config.yaml')   # snapshot for reproducibility

All fields have sensible defaults so a minimal YAML only needs to specify
``dataset_path`` and whichever axes differ from the default.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, asdict
from typing import Any, Optional

import yaml


# ---------------------------------------------------------------------------
# Sub-configs
# ---------------------------------------------------------------------------

@dataclass
class GlobalMetricsConfig:
    """Parameters for :func:`~sc_annotation.global_metrics.compute_global_metrics`."""
    n_top_hvg: int = 2000
    min_cells_pct: float = 0.01
    compute_gini: bool = True
    gini_scope: str = "hvg"  # hvg | expressed | all


@dataclass
class FilterConfig:
    """Axis 3 — Feature Filtering.

    All ``exclude_*`` flags default to the conservative settings: remove MT
    and ribosomal genes and lowly expressed genes; keep everything else.
    """
    exclude_mt: bool = True
    exclude_ribo: bool = True
    exclude_low_expr: bool = True
    exclude_hb: bool = False          # haemoglobin genes
    exclude_tcr_ig: bool = False      # TCR/Ig VDJ clonotype genes
    exclude_sex_chr: bool = False     # XIST and Y-linked marker genes
    gini_min: Optional[float] = 0.02  # exclude genes with Gini < gini_min (housekeeping)


@dataclass
class SelectionConfig:
    """Axis 4 — Feature Selection.

    ``strategy`` controls the scoring function used to rank genes for the
    prompt.  ``combined`` shows two ranked lists: ``n_top`` by expression
    (primary) and ``n_top_secondary`` by z-score (secondary).

    Supported strategies:
        ``expr``         — raw expression count
        ``zscore``       — z-score vs population
        ``tfidf``        — TF-IDF (cell-specific rarity weighting)
        ``de``           — log2 fold-change vs background (or kNN neighbourhood)
        ``marker_panel`` — curated positive/negative marker panel
        ``combined``     — expression list + z-score list (dual prompt)
    """
    strategy: str = "zscore"   # expr | zscore | tfidf | de | marker_panel | combined
    n_top: int = 500            # genes in the primary list
    n_top_secondary: int = 50  # genes in the secondary list (combined strategy)
    modalities: list = field(default_factory=lambda: ["rna"])  # rna | adt
    marker_panel_path: Optional[str] = None   # path to MarkerPanel YAML


@dataclass
class InputConfig:
    """Axis 2 — Input Entity.

    ``mode`` selects how the expression vector for each cell is constructed:

    ``single_cell``
        Raw expression of the individual cell.

    ``knn_smoothed``
        Mean expression over the cell and its ``knn_k`` nearest neighbours.
        Neighbours are found in ``knn_use_rep`` space (PCA by default).

    ``pseudobulk``
        Mean expression of all cells sharing the same true label.
        Use as an upper-bound reference — it leaks label information.
    """
    mode: str = "single_cell"          # single_cell | knn_smoothed | pseudobulk
    knn_k: int = 20                    # neighbours used for smoothing
    knn_use_rep: Optional[str] = "X_pca"  # obsm key; None → compute PCA on the fly


@dataclass
class LLMConfig:
    """LLM backend selection and generation parameters."""
    backend: str = "gemini"            # gemini | claude | openai | deepseek | openrouter
    model: str = "gemini-2.0-flash"
    temperature: float = 0.0
    max_tokens: int = 4096
    api_key_env: Optional[str] = None  # env-var name that holds the API key
    # Number of samples processed concurrently. 1 keeps fully serial behaviour.
    concurrency: int = 1
    use_context_cache: bool = False
    context_cache_ttl_seconds: int = 3600


@dataclass
class Stage2Config:
    """Optional stage-2 refinement settings."""
    enabled: bool = False
    model: Optional[str] = None
    temperature: float = 0.0
    max_tokens: int = 4096
    mode: str = "strict"  # strict | combined
    n_program_genes: int = 50
    score_method: str = "tirosh"       # mean_z | tirosh | ucell
    score_min_genes: int = 3
    score_n_background: int = 50
    score_random_state: int = 0
    n_top_genes: int = 30
    n_top_proteins: int = 15
    program_query_max_output_tokens: int = 25600
    program_query_thinking_budget: Optional[int] = 0


@dataclass
class EvaluationConfig:
    """Sampling and evaluation parameters."""
    label_col: str = "celltype.l1"
    # Skip annotation and assign each sampled cell a random label from cell_type_list.
    random: bool = False
    # Label columns ordered from broadest to finest, e.g. ["celltype.l1", "celltype.l2"].
    hierarchy: Optional[list[str]] = None
    n_per_class: int = 5
    seed: int = 42
    # Matching strategies to compute: exact | keyword | hierarchy | llm_judge | llm_judge_binary
    strategies: list = field(default_factory=lambda: ["exact", "keyword"])
    # Backend for llm_judge / llm_judge_binary; None → reuse annotation backend
    judge_backend: Optional[str] = None
    # Number of samples evaluated concurrently. 1 keeps fully serial behaviour.
    concurrency: int = 1
    # Number of stratified bootstrap resamples for uncertainty estimates. 0 disables.
    n_bootstrap: int = 0
    bootstrap_seed: Optional[int] = 42


@dataclass
class OutputConfig:
    """Where to write results."""
    results_dir: str = "results"
    experiment_name: str = "experiment"
    save_results: bool = True


@dataclass
class InspectConfig:
    """Optional per-cell prompt/response tracing for debugging.

    When enabled, only cells whose global ``cell_idx`` appears in
    ``cell_indices`` are traced.
    """
    enabled: bool = False
    cell_indices: list[int] = field(default_factory=list)
    save_path: Optional[str] = None


# ---------------------------------------------------------------------------
# Root config
# ---------------------------------------------------------------------------

@dataclass
class ExperimentConfig:
    """Root configuration for one annotation experiment.

    Load from YAML::

        config = ExperimentConfig.from_yaml('configs/pbmc_l1_zscore_gemini.yaml')

    Minimal YAML example::

        dataset_path: Datasets/PBMC_CiteSeqRef/pbmc_citeseq_ref_2021.h5ad
        tissue: PBMC
        llm:
          backend: gemini
          model: gemini-2.0-flash
        evaluation:
          label_col: celltype.l1
          n_per_class: 5
    """

    dataset_path: str = ""
    tissue: Optional[str] = None
    global_metrics: GlobalMetricsConfig = field(default_factory=GlobalMetricsConfig)
    filter: FilterConfig = field(default_factory=FilterConfig)
    selection: SelectionConfig = field(default_factory=SelectionConfig)
    input: InputConfig = field(default_factory=InputConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    stage2: Stage2Config = field(default_factory=Stage2Config)
    evaluation: EvaluationConfig = field(default_factory=EvaluationConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    inspect: InspectConfig = field(default_factory=InspectConfig)

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    @classmethod
    def from_yaml(cls, path: str) -> "ExperimentConfig":
        """Load config from a YAML file.  Unknown keys are silently ignored."""
        with open(path, encoding="utf-8") as fh:
            d = yaml.safe_load(fh) or {}
        return cls(
            dataset_path=d.get("dataset_path", ""),
            tissue=d.get("tissue"),
            global_metrics=GlobalMetricsConfig(**_safe_kwargs(GlobalMetricsConfig, d.get("global_metrics", {}))),
            filter=FilterConfig(**_safe_kwargs(FilterConfig, d.get("filter", {}))),
            selection=SelectionConfig(**_safe_kwargs(SelectionConfig, d.get("selection", {}))),
            input=InputConfig(**_safe_kwargs(InputConfig, d.get("input", {}))),
            llm=LLMConfig(**_safe_kwargs(LLMConfig, d.get("llm", {}))),
            stage2=Stage2Config(**_safe_kwargs(Stage2Config, d.get("stage2", {}))),
            evaluation=EvaluationConfig(**_safe_kwargs(EvaluationConfig, d.get("evaluation", {}))),
            output=OutputConfig(**_safe_kwargs(OutputConfig, d.get("output", {}))),
            inspect=InspectConfig(**_safe_kwargs(InspectConfig, d.get("inspect", {}))),
        )

    def to_yaml(self, path: str) -> None:
        """Save config to a YAML file (for reproducibility snapshots)."""
        with open(path, "w", encoding="utf-8") as fh:
            yaml.dump(asdict(self), fh, default_flow_style=False, sort_keys=False)

    def save_full_snapshot(self, path: str) -> None:
        """Write the current config as a complete snapshot artifact.

        This is intended for result directories and experiment metadata files,
        where the stored YAML is a record of the exact run configuration and may
        safely replace any prior snapshot at ``path``.
        """
        self.to_yaml(path)

    def save_evaluation_snapshot(self, path: str) -> None:
        """Persist the current evaluation settings without overwriting other sections.

        If ``path`` already exists, preserve the existing YAML content and only
        replace the ``evaluation`` mapping. This avoids clobbering a source
        template config while still recording the evaluation state of the run.
        """
        existing: dict[str, Any] = {}
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as fh:
                loaded = yaml.safe_load(fh) or {}
            if isinstance(loaded, dict):
                existing = loaded

        merged = dict(existing)
        merged["evaluation"] = asdict(self.evaluation)
        for key, value in asdict(self).items():
            if key != "evaluation":
                merged.setdefault(key, value)

        with open(path, "w", encoding="utf-8") as fh:
            yaml.dump(merged, fh, default_flow_style=False, sort_keys=False)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def summary(self) -> str:
        """One-line human-readable summary for logging."""
        return (
            f"dataset={self.dataset_path!r} "
            f"input={self.input.mode}(k={self.input.knn_k}) "
            f"filter=(mt={self.filter.exclude_mt} ribo={self.filter.exclude_ribo} "
            f"lowexpr={self.filter.exclude_low_expr} gini_min={self.filter.gini_min}) "
            f"selection={self.selection.strategy}(n={self.selection.n_top}) "
            f"llm={self.llm.backend}/{self.llm.model}(concurrency={self.llm.concurrency}) "
            f"stage2={'on' if self.stage2.enabled else 'off'}({self.stage2.mode})({self.stage2.score_method}) "
            f"inspect={'on' if self.inspect.enabled else 'off'} "
            f"evaluation=(label_col={self.evaluation.label_col} random={self.evaluation.random})"
        )


def _safe_kwargs(cls, d: dict) -> dict:
    """Keep only keys that are valid field names for ``cls``."""
    import dataclasses
    valid = {f.name for f in dataclasses.fields(cls)}
    return {k: v for k, v in d.items() if k in valid}
