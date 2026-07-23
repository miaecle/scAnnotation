# scAnnotation_codebase

scAnnotation_codebase is a configuration-driven single-cell annotation framework for transcriptomic data, with optional ADT support. It combines gene filtering, multiple feature construction strategies, several LLM backends, optional Stage-2 refinement, and a set of evaluation utilities for benchmarking cell type annotation workflows.

## What this project does

- Runs end-to-end annotation experiments from YAML configs.
- Supports three input construction modes: `single_cell`, `knn_smoothed`, and `pseudobulk`.
- Supports several gene scoring / prompt construction strategies: `expr`, `zscore`, `tfidf`, `de`, `marker_panel`, and `combined`.
- Works with multiple LLM providers: `gemini`, `claude`, `openai`, `deepseek`, and `openrouter`.
- Can optionally perform Stage-2 refinement by querying subtype programs and rescoring candidate labels.
- Evaluates predictions with `exact`, `keyword`, `llm_judge`, and `llm_judge_binary` matching strategies.
- Saves reproducible outputs, including a config snapshot, usage logs, and summary metrics.

## Repository Layout

```text
.
├── run_experiment.py        # CLI entry point for running one experiment from a YAML file
├── requirements.txt         # Python dependencies
├── .env.example             # Example API key template
├── configs/                 # Ready-to-run experiment configs
├── scripts/                 # Convenience shell scripts for common runs
├── sc_annotation/           # Core library code
├── results/                 # Default output directory for experiment artifacts
└── *.ipynb                  # Exploration and showcase notebooks
```

## Installation

Python 3.10+ is recommended.

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy the example environment file and fill in the API keys required by your chosen backend:

```bash
copy .env.example .env
```

Typical keys include:

- `GOOGLE_API_KEY`
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `DEEPSEEK_API_KEY`

The config field `llm.api_key_env` decides which variable is read for a run.

## Data and Configs

The pipeline expects an `.h5ad` dataset and a YAML config. At minimum, set:

- `dataset_path`: path to the AnnData file
- `evaluation.label_col`: the ground-truth label column used for sampling and scoring
- `tissue`: tissue context when required by the dataset or the prompt logic

The repo already includes example configs for PBMC and HLCA-style experiments under `configs/`.

Useful config groups:

- `global_metrics`: HVG and global gene statistics settings
- `filter`: gene exclusion switches such as MT, ribosomal, low-expression, HB, TCR/Ig, and sex chromosome genes
- `selection`: feature scoring strategy, number of genes, modality selection, and optional marker panel path
- `input`: how per-cell input is built before scoring
- `llm`: backend, model, temperature, token budget, concurrency, and cache options
- `stage2`: optional second-pass refinement settings
- `evaluation`: sampling, seed, evaluation strategies, and judge backend
- `output`: results directory, experiment name, and save flag
- `inspect`: optional tracing for selected cells

## Quick Start

Dry-run the config first to verify it parses without calling an LLM:

```bash
python run_experiment.py configs/pbmc_l2_knn.yaml --dry-run
```

Run the full experiment:

```bash
python run_experiment.py configs/pbmc_l2_knn.yaml
```

Common overrides:

```bash
python run_experiment.py configs/pbmc_l2_knn.yaml \
   --n-per-class 10 \
   --label-col celltype.l2 \
   --experiment-name my_exp \
   --results-dir results/my_exp
```

You can also use the ready-made scripts in `scripts/` for common PBMC and HLCA runs.

## Pipeline Summary

At a high level, a run does the following:

1. Loads the YAML config and applies CLI overrides.
2. Loads the dataset from `dataset_path`.
3. Annotates genes and computes global metrics if they are missing.
4. Builds the gene mask from the filtering rules.
5. Constructs the chosen input representation (`single_cell`, `knn_smoothed`, or `pseudobulk`).
6. Scores genes with the selected strategy and builds the prompt.
7. Calls the configured LLM backend.
8. Optionally runs Stage-2 refinement.
9. Evaluates the output with the configured metrics.
10. Writes results and a config snapshot to `output.results_dir`.

## Output Artifacts

Each run usually writes the following files into `output.results_dir`:

- `{name}_results.csv`: per-sample predictions and parsed outputs such as `pred_celltype` and `pred_rationale`
- `{name}_eval.csv`: overall evaluation summary
- `{name}_config.yaml`: the exact config snapshot used for the run
- `{name}_llm_usage.csv`: detailed LLM usage records
- `{name}_llm_usage_summary.csv`: aggregated usage statistics
- `{name}_confusion_matrix.png`: confusion matrix visualization
- `{name}_timing.csv`: timing information for the run
- `{name}_stage2_skipped.csv`: only when Stage-2 fails for some samples
- `{name}_inspect.jsonl`: only when inspect mode is enabled

## Examples Included

The repository includes several example configs for common experiments:

- `configs/hlca_celltype_knn.yaml`
- `configs/hlca_celltype_pseudobulk.yaml`
- `configs/hlca_celltype_single.yaml`
- `configs/pbmc_l2_expr.yaml`
- `configs/pbmc_l2_knn.yaml`
- `configs/pbmc_l2_pseudobulk.yaml`
- `configs/pbmc_l2_zscore.yaml`
- `configs/pbmc_l2_single.yaml`
- `configs/pbmc_l2_tfidf.yaml`

These are useful templates when creating a new experiment for a different dataset or backend.

## Common Troubleshooting

- If you see an API key error, check that `.env` exists and that `llm.api_key_env` matches the environment variable name.
- If an HLCA run complains about tissue handling, make sure `tissue` is set and that the value exists in `adata.obs["tissue"]`.
- If a run behaves unexpectedly, start with `--dry-run` and inspect the config summary printed by the CLI.

## Main Entry Points

- CLI: `run_experiment.py`
- Core pipeline: `sc_annotation/pipeline.py`
- Config schema: `sc_annotation/config.py`
- Gene scoring and selection: `sc_annotation/selection.py`
- Prompt builders: `sc_annotation/prompts.py`
- Evaluation logic: `sc_annotation/metrics.py`
- Stage-2 logic: `sc_annotation/stage2.py`

To add a new experiment, copy an existing YAML file from `configs/`, adjust the dataset, backend, and scoring strategy, then run it with `run_experiment.py`.
