#!/usr/bin/env python
"""CLI entry point for running annotation experiments from a YAML config file.

Usage::

    python run_experiment.py configs/pbmc_l1_zscore_gemini.yaml
    python run_experiment.py configs/pbmc_l1_knn_k20.yaml --n-per-class 10
    python run_experiment.py configs/pbmc_l1_baseline.yaml --dry-run

The script loads the dataset, runs the full pipeline defined by the config,
and writes results + a config snapshot to ``output.results_dir``.

Environment variables for API keys are read from the names given in each
config's ``llm.api_key_env`` field (e.g. ``GOOGLE_API_KEY``,
``ANTHROPIC_API_KEY``, ``DEEPSEEK_API_KEY``).
"""

from __future__ import annotations

import argparse
import sys
import os

import os, sys, warnings
warnings.filterwarnings('ignore')
from dotenv import load_dotenv
load_dotenv()

# Add project root to path so 'sc_annotation' is importable when running
# from the repo root without installing the package.
sys.path.insert(0, os.path.dirname(__file__))

from sc_annotation.config import ExperimentConfig
from sc_annotation.data import load_dataset
from sc_annotation.pipeline import run_experiment, build_backend


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Run an sc-annotation experiment from a YAML config file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("config", help="Path to the YAML experiment config file.")
    p.add_argument(
        "--n-per-class", type=int, default=None,
        help="Override evaluation.n_per_class in the config.",
    )
    p.add_argument(
        "--label-col", default=None,
        help="Override evaluation.label_col in the config.",
    )
    p.add_argument(
        "--experiment-name", default=None,
        help="Override output.experiment_name.",
    )
    p.add_argument(
        "--results-dir", default=None,
        help="Override output.results_dir.",
    )
    p.add_argument(
        "--dry-run", action="store_true",
        help="Parse config and show summary without calling the LLM.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # ------------------------------------------------------------------ #
    # Load config and apply CLI overrides
    # ------------------------------------------------------------------ #
    config = ExperimentConfig.from_yaml(args.config)

    if args.n_per_class is not None:
        config.evaluation.n_per_class = args.n_per_class
    if args.label_col is not None:
        config.evaluation.label_col = args.label_col
    if args.experiment_name is not None:
        config.output.experiment_name = args.experiment_name
    if args.results_dir is not None:
        config.output.results_dir = args.results_dir

    print(f"Config loaded from: {args.config}")
    print(config.summary())

    if args.dry_run:
        print("\n[dry-run] Skipping dataset load and LLM calls.")
        print("Config is valid. To run for real, omit --dry-run.")
        return

    # ------------------------------------------------------------------ #
    # Load dataset
    # ------------------------------------------------------------------ #
    if not config.dataset_path:
        print("ERROR: 'dataset_path' not set in config.", file=sys.stderr)
        sys.exit(1)

    print(f"\nLoading dataset: {config.dataset_path}")
    adata = load_dataset(config.dataset_path, config.tissue)
    print(f"  Loaded: {adata.shape[0]:,} cells x {adata.shape[1]:,} genes")

    # ------------------------------------------------------------------ #
    # Run
    # ------------------------------------------------------------------ #
    run_experiment(adata, config)


if __name__ == "__main__":
    main()
