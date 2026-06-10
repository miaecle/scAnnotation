from .data import load_dataset, sample_cells
from .adt import build_adt_adata, normalize_adt, compute_adt_stats, get_top_proteins
from .global_metrics import compute_global_metrics
from .filtering import annotate_genes, build_gene_mask, summarise_mask
from .selection import (
    score_by_expr,
    score_by_zscore,
    score_by_tfidf,
    score_by_de,
    compute_scores,
    select_genes,
    select_by_marker_panel,
    MarkerPanel,
)
from .smoothing import build_knn_index, get_knn_indices, compute_pseudobulk
from .config import (
    ExperimentConfig,
    FilterConfig,
    SelectionConfig,
    InputConfig,
    GlobalMetricsConfig,
    LLMConfig,
    EvaluationConfig,
    OutputConfig,
)
from .pipeline import run_experiment, build_backend, ensure_global_metrics
from .metrics import (
    accuracy,
    per_class_metrics,
    annotation_report,
    extract_cell_type,
    extract_rationale,
    parse_results,
    keyword_accuracy,
    llm_judge_accuracy,
    evaluate_all,
)
from .backends import ClaudeBackend, GeminiBackend

__all__ = [
    # data
    "load_dataset",
    "sample_cells",
    # adt
    "build_adt_adata",
    "normalize_adt",
    "compute_adt_stats",
    "get_top_proteins",
    # global metrics
    "compute_global_metrics",
    # filtering
    "annotate_genes",
    "build_gene_mask",
    "summarise_mask",
    # selection
    "score_by_expr",
    "score_by_zscore",
    "score_by_tfidf",
    "score_by_de",
    "compute_scores",
    "select_genes",
    "select_by_marker_panel",
    "MarkerPanel",
    # smoothing
    "build_knn_index",
    "get_knn_indices",
    "compute_pseudobulk",
    # config
    "ExperimentConfig",
    "FilterConfig",
    "SelectionConfig",
    "InputConfig",
    "GlobalMetricsConfig",
    "LLMConfig",
    "EvaluationConfig",
    "OutputConfig",
    # pipeline
    "run_experiment",
    "build_backend",
    "ensure_global_metrics",
    # metrics
    "accuracy",
    "per_class_metrics",
    "annotation_report",
    "extract_cell_type",
    "extract_rationale",
    "parse_results",
    "keyword_accuracy",
    "llm_judge_accuracy",
    "evaluate_all",
    # backends
    "ClaudeBackend",
    "GeminiBackend",
]
