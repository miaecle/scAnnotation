import os
import tempfile

import anndata as ad
import numpy as np
import pandas as pd

from sc_annotation.config import ExperimentConfig
from sc_annotation.pipeline import _resolve_result_paths
from sc_annotation.pipeline import run_experiment
from sc_annotation.visualization import _hierarchy_leaf_order


def test_legacy_result_paths_are_resolved_from_root_layout():
    with tempfile.TemporaryDirectory() as d:
        name = "legacy_run"
        for fn in [
            f"{name}_results.csv",
            f"{name}_eval.csv",
            f"{name}_config.yaml",
            f"{name}_confusion_matrix.png",
            f"{name}_llm_usage.csv",
            f"{name}_timing.csv",
        ]:
            with open(os.path.join(d, fn), "w", encoding="utf-8") as fh:
                fh.write("x")

        paths = _resolve_result_paths(d, name)

        assert os.path.basename(paths["results_path"]) == f"{name}_results.csv"
        assert os.path.basename(paths["eval_path"]) == f"{name}_eval.csv"
        assert os.path.basename(paths["config_path"]) == f"{name}_config.yaml"
        assert os.path.basename(paths["cm_path"]) == f"{name}_confusion_matrix.png"
        assert os.path.basename(paths["usage_path"]) == f"{name}_llm_usage.csv"
        assert os.path.basename(paths["timing_path"]) == f"{name}_timing.csv"

        assert os.path.isdir(os.path.join(d, "tables"))
        assert os.path.isdir(os.path.join(d, "meta"))
        assert os.path.isdir(os.path.join(d, "plots"))
        assert os.path.isdir(os.path.join(d, "logs"))


def test_random_evaluation_skips_annotation_and_assigns_known_labels(monkeypatch, tmp_path):
    adata = ad.AnnData(X=np.ones((4, 2)))
    adata.obs_names = ["cell-1", "cell-2", "cell-3", "cell-4"]
    adata.obs["cell_type"] = pd.Categorical(["B cell", "B cell", "T cell", "T cell"])
    config = ExperimentConfig()
    config.evaluation.random = True
    config.evaluation.label_col = "cell_type"
    config.evaluation.n_per_class = 2
    config.evaluation.seed = 7
    config.evaluation.strategies = ["exact"]
    config.output.results_dir = str(tmp_path)
    config.output.save_results = False

    def fail_if_called(*args, **kwargs):
        raise AssertionError("random evaluation must not initialize annotation dependencies")

    monkeypatch.setattr("sc_annotation.pipeline.build_backend", fail_if_called)
    monkeypatch.setattr("sc_annotation.pipeline.ensure_global_metrics", fail_if_called)

    results_df = run_experiment(adata, config)

    assert len(results_df) == 4
    assert set(results_df["pred_label"]).issubset({"B cell", "T cell"})
    assert results_df["pred_label"].tolist() == ["T cell", "T cell", "T cell", "T cell"]


def test_hierarchy_leaf_order_groups_related_cell_types():
    hierarchy_tree = {
        "children": {
            "immune": {
                "label": "Immune",
                "children": {
                    "b_cell": {"label": "B cell", "children": {}},
                    "t_cell": {"label": "T cell", "children": {}},
                },
            },
            "stromal": {
                "label": "Stromal",
                "children": {
                    "fibroblast": {"label": "Fibroblast", "children": {}},
                },
            },
        },
    }

    assert _hierarchy_leaf_order(hierarchy_tree) == ["B cell", "T cell", "Fibroblast"]
