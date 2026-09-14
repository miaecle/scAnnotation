# scAnnotation

`scAnnotation` 是一个由 YAML 配置驱动的单细胞转录组细胞类型注释框架。它把基因过滤、特征选择、表达输入构造、LLM 注释、可选的二阶段精修和评估整合到同一条可复现实验流水线中，并支持 RNA 与可选的 ADT 蛋白数据。

项目适合用于：

- 比较不同基因选择策略、输入构造方式和 LLM 模型的注释效果；
- 对 PBMC、HLCA 等带有细胞类型标签的 AnnData 数据进行抽样注释；
- 记录每次实验的配置、预测、评估指标、LLM token 使用量和运行时间；
- 调试指定细胞的 prompt、模型响应和 Stage-2 处理过程。

## 核心能力

- **三种输入模式**：`single_cell`、`knn_smoothed`、`pseudobulk`。
- **六种基因选择策略**：`expr`、`zscore`、`tfidf`、`de`、`marker_panel`、`combined`。
- **多种 LLM 后端**：`gemini`、`claude`、`openai`、`deepseek`、`openrouter`。
- **RNA/ADT 支持**：数据包含 `obsm["protein_counts"]` 和 `uns["ADT_names"]` 时可将 ADT 纳入 prompt。
- **Stage-2 refinement**：根据第一阶段标签查询细胞亚型/易混淆类型的基因程序，再进行程序打分和候选标签精修。
- **多种评估方式**：`exact`、`keyword`、`hierarchy`、`llm_judge`、`llm_judge_binary`。
- **可复现记录**：固定随机种子、保存最终配置快照、预测表、评估报告、混淆矩阵、LLM usage 和 timing。

## 目录结构

```text
.
├── run_experiment.py        # 主 CLI：从 YAML 启动一次实验
├── requirements.txt         # Python 依赖
├── configs/                 # PBMC、HLCA 及其他实验模板
├── scripts/                 # 常用实验的 shell 启动脚本
├── sc_annotation/           # 核心 Python 包
│   ├── backends/             # Gemini、Claude、OpenAI 兼容后端
│   ├── config.py             # dataclass 配置定义和 YAML 序列化
│   ├── data.py               # h5ad 加载、抽样和 inspect
│   ├── filtering.py          # 基因注释与过滤
│   ├── selection.py          # 基因打分和选择
│   ├── pipeline.py           # 端到端实验流程
│   ├── metrics.py            # 预测解析和评估
│   └── stage2.py             # 二阶段程序查询与打分
├── figure/                  # PBMC/HLCA 绘图和汇总脚本
├── results/                 # 实验输出目录
├── tests/                   # 测试
└── *.ipynb                  # 数据检查和实验展示 notebook
```

## 安装

建议使用 Python 3.10 或更高版本。Windows PowerShell 下：

```powershell
git clone <repository-url>
cd scAnnotation
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Linux/macOS 下：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

依赖主要包括 `scanpy`、`anndata`、`scikit-learn`、`pandas`、`scipy`、`matplotlib`、`PyYAML`、`python-dotenv` 以及各 LLM provider 的 SDK。

## API Key 配置

`run_experiment.py` 启动时会自动调用 `python-dotenv` 加载项目根目录下的 `.env`。当前仓库没有提交 `.env.example`，请手动创建 `.env`，只填写实际使用的 provider：

```dotenv
GOOGLE_API_KEY=your_google_key
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key
DEEPSEEK_API_KEY=your_deepseek_key
OPENROUTER_API_KEY=your_openrouter_key
```

然后在 YAML 的 `llm.api_key_env` 中指定变量名，例如：

```yaml
llm:
   backend: deepseek
   model: deepseek-chat
   api_key_env: DEEPSEEK_API_KEY
```

不要把 `.env` 或真实 API key 提交到版本库。`api_key_env` 为空时，后端 SDK 可能尝试使用其默认环境变量；为了避免歧义，建议在每个实验配置中显式设置。

## 数据要求

主输入是 `.h5ad` 文件，程序通过 `anndata.read_h5ad` 加载。一个可运行的配置至少需要：

- `dataset_path`：`.h5ad` 文件路径；
- `evaluation.label_col`：`adata.obs` 中的真实细胞类型列；
- 对 HLCA 数据设置 `tissue`，并确保其值存在于 `adata.obs["tissue"]`。

表达矩阵放在 `adata.X`。如果使用 ADT，需要同时提供：

- `adata.obsm["protein_counts"]`：每个细胞的蛋白计数；
- `adata.uns["ADT_names"]`：与蛋白计数列对应的蛋白名称。

HLCA 文件名为 `hlca_core.h5ad` 时，加载器会按 `tissue` 过滤细胞。例如：

```yaml
dataset_path: Datasets/HLCA/hlca_core.h5ad

evaluation:
   label_col: cell_type
```

PBMC 等其他数据不会执行 HLCA 专用的组织过滤。若标签不在 h5ad 中，当前 `run_experiment.py` 没有 labels CSV 的 CLI 参数，需要先把标签合并到 `adata.obs` 或在代码中调用 `load_dataset(..., labels_path=...)`。

## 快速开始

### 1. 先做 dry-run

`--dry-run` 只读取并解析 YAML、打印配置摘要，不加载数据，也不会调用 LLM：

```powershell
python run_experiment.py configs/pbmc_l2_knn.yaml --dry-run
```

### 2. 运行一次完整实验

```powershell
python run_experiment.py configs/pbmc_l2_knn.yaml
```

完整运行会加载数据、计算缺失的基因指标、抽样细胞、构造 prompt、调用 LLM，并把结果写入配置中的 `output.results_dir`。

### 3. 使用命令行覆盖少量参数

```powershell
python run_experiment.py configs/pbmc_l2_knn.yaml `
   --n-per-class 10 `
   --label-col celltype.l2 `
   --experiment-name pbmc_debug `
   --results-dir results/pbmc_debug
```

支持的 CLI 参数只有以下几项：

| 参数 | 覆盖的配置 | 说明 |
| --- | --- | --- |
| `--n-per-class N` | `evaluation.n_per_class` | 每个类别抽样数量 |
| `--label-col COLUMN` | `evaluation.label_col` | 真实标签列 |
| `--experiment-name NAME` | `output.experiment_name` | 输出文件名前缀 |
| `--results-dir PATH` | `output.results_dir` | 输出目录 |
| `--dry-run` | 无 | 只校验配置，不运行实验 |

## 配置说明

配置文件由 `sc_annotation.config.ExperimentConfig` 解析。未知 YAML 字段会被忽略；建议从 `configs/` 复制模板再修改。

### 最小配置

```yaml
dataset_path: Datasets/PBMC_CiteSeqRef/pbmc_citeseq_ref_2021.h5ad
tissue: PBMC

llm:
   backend: deepseek
   model: deepseek-chat
   api_key_env: DEEPSEEK_API_KEY

evaluation:
   label_col: celltype.l2
   n_per_class: 5

output:
   results_dir: results/my_experiment
   experiment_name: my_experiment
```

### `global_metrics`

控制全局基因统计量。若 `adata.var` 中已经存在所需列，流水线会复用它们；否则自动计算。

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| `n_top_hvg` | `2000` | 用于 HVG 统计的基因数 |
| `min_cells_pct` | `0.01` | 基因至少在多少比例细胞中表达 |
| `compute_gini` | `true` | 是否计算 Gini 指标 |
| `gini_scope` | `hvg` | Gini 范围：`hvg`、`expressed` 或 `all` |

### `filter`

决定哪些基因可以进入后续打分和 prompt：

| 字段 | 默认值 | 过滤内容 |
| --- | --- | --- |
| `exclude_mt` | `true` | 线粒体基因 |
| `exclude_ribo` | `true` | 核糖体基因 |
| `exclude_low_expr` | `true` | 低表达基因 |
| `exclude_hb` | `false` | 血红蛋白基因 |
| `exclude_tcr_ig` | `false` | TCR/Ig VDJ 基因 |
| `exclude_sex_chr` | `false` | 性染色体相关基因，如 XIST/Y-linked genes |
| `gini_min` | `0.02` | 排除 Gini 低于该值的 housekeeping 基因；设为 `null` 禁用 |

### `selection`

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| `strategy` | `zscore` | `expr`、`zscore`、`tfidf`、`de`、`marker_panel` 或 `combined` |
| `n_top` | `500` | 主基因列表长度 |
| `n_top_secondary` | `50` | 仅 `combined` 使用的第二列表长度 |
| `modalities` | `[rna]` | 可选 `rna`、`adt`，需要数据中有对应模态 |
| `marker_panel_path` | `null` | `marker_panel` 策略使用的 marker YAML |

策略含义：

- `expr`：按表达量排序；
- `zscore`：相对总体表达分布的 z-score；
- `tfidf`：提高细胞特异基因权重；
- `de`：相对背景或 kNN 邻域的差异表达；
- `marker_panel`：结合 marker panel 中的正/负 marker；
- `combined`：同时提供 expression 和 z-score 两组列表。

### `input`

| 模式 | 行为 | 注意事项 |
| --- | --- | --- |
| `single_cell` | 只使用当前细胞 | 最接近原始单细胞，但噪声较大 |
| `knn_smoothed` | 使用当前细胞及其 k 个近邻的均值 | `knn_use_rep` 默认为 `X_pca`；不存在时会计算 PCA |
| `pseudobulk` | 使用与当前细胞真实标签相同的所有细胞均值 | 会泄漏真实标签，只适合作为上界/对照 |

相关字段：

```yaml
input:
   mode: knn_smoothed
   knn_k: 10
   knn_use_rep: X_pca
```

### `llm`

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| `backend` | `gemini` | `gemini`、`claude`、`openai`、`deepseek`、`openrouter` |
| `model` | `gemini-2.0-flash` | provider 对应的模型 ID |
| `temperature` | `0.0` | 生成温度；注释实验通常建议保持 0 |
| `max_tokens` | `4096` | 单次响应 token 上限 |
| `api_key_env` | `null` | API key 的环境变量名 |
| `concurrency` | `1` | 并发处理的样本数，需结合 provider 限流设置 |
| `use_context_cache` | `false` | Gemini 等支持的上下文缓存开关 |
| `context_cache_ttl_seconds` | `3600` | 上下文缓存有效期，必须大于 0 |

DeepSeek 和 OpenRouter 通过 OpenAI 兼容接口访问；Stage-2 的 JSON 程序查询支持 `gemini`、`openai`、`deepseek` 和 `openrouter`，不支持 `claude`。

### `stage2`

```yaml
stage2:
   enabled: true
   model: deepseek-chat
   mode: strict
   score_method: tirosh
   n_program_genes: 50
   score_min_genes: 3
   score_n_background: 50
   n_top_genes: 30
   n_top_proteins: 15
```

主要字段：

- `enabled`：是否启用第二阶段；
- `mode`：`strict` 或 `combined`；
- `score_method`：`mean_z`、`tirosh` 或 `ucell`；
- `n_program_genes`：每个程序请求的候选基因数；
- `score_min_genes`、`score_n_background`、`score_random_state`：程序评分参数；
- `n_top_genes`、`n_top_proteins`：Stage-2 prompt 中使用的 RNA/ADT 特征数；
- `program_query_max_output_tokens`、`program_query_thinking_budget`：程序 JSON 查询的输出和 thinking 设置。

Stage-2 可能因某个细胞的程序查询或评分失败而跳过该细胞；这类记录会写入 `stage2/` 下的 skipped 文件，主实验仍会保留可用结果。

### `evaluation`

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| `label_col` | `celltype.l1` | `adata.obs` 中的真实标签列 |
| `random` | `false` | 不调用 LLM，改为随机分配标签，用作基线 |
| `hierarchy` | `null` | 从粗到细的标签列列表，例如 `[celltype.l1, celltype.l2]` |
| `n_per_class` | `5` | 每类抽样数量 |
| `seed` | `42` | 抽样随机种子 |
| `strategies` | `[exact, keyword]` | 要计算的匹配方式 |
| `judge_backend` | `null` | `llm_judge*` 使用的后端；为空时复用注释后端 |
| `concurrency` | `1` | 评估阶段并发数 |
| `n_bootstrap` | `0` | 分层 bootstrap 次数；0 表示关闭 |
| `bootstrap_seed` | `42` | bootstrap 随机种子 |

### `output` 与 `inspect`

```yaml
output:
   results_dir: results/my_experiment
   experiment_name: my_experiment
   save_results: true

inspect:
   enabled: true
   cell_indices: [13748, 48]
   save_path: results/my_experiment/inspect.jsonl
```

`inspect.cell_indices` 使用加载后 AnnData 中的全局整数位置，不是 barcode。启用 inspect 时必须提供至少一个合法索引；若未设置 `save_path`，默认写到结果目录下的 `{experiment_name}_inspect.jsonl`。

## 流水线顺序

一次实验大致按以下顺序执行：

1. 读取 YAML 并应用 CLI 覆盖参数；
2. 加载 `.h5ad`，必要时筛选 HLCA tissue；
3. 检查并补充 `adata.var` 中的基因类别和全局指标；
4. 根据 `filter` 构建基因 mask；
5. 根据 `input.mode` 构造单细胞、kNN 平滑或 pseudobulk 表达；
6. 根据 `selection.strategy` 计算排名并生成 prompt；
7. 调用 LLM，解析第一行细胞类型和后续 rationale；
8. 如果启用 Stage-2，查询基因程序并重新评分候选类型；
9. 根据 `evaluation.strategies` 计算准确率、层级匹配或 LLM judge 指标；
10. 保存表格、报告、配置快照和运行日志。

## 输出文件

当前版本通常会在 `output.results_dir` 下创建以下子目录：

```text
results/my_experiment/
├── tables/
│   ├── my_experiment_results.csv
│   ├── my_experiment_eval.csv
│   └── my_experiment_eval_report.txt
├── logs/
│   ├── my_experiment_llm_usage.csv
│   ├── my_experiment_llm_usage_failures.csv
│   ├── my_experiment_llm_usage_summary.csv
│   ├── my_experiment_llm_usage_program_method_rows.csv
│   └── my_experiment_llm_usage_program_method_summary.csv
├── stage2/
│   ├── my_experiment_stage2_program_cache.json
│   └── my_experiment_stage2_skipped.csv
├── meta/
│   ├── my_experiment_config.yaml
│   └── my_experiment_timing.csv
└── my_experiment_inspect.jsonl
```

不同模式或旧结果目录可能直接把文件写在根目录，读取结果时应以实际运行日志和配置快照为准。重要文件说明：

- `*_results.csv`：每个抽样细胞的真实标签、原始 LLM 响应、解析后的 `pred_celltype` 和 `pred_rationale`；
- `*_eval.csv`：评估指标汇总；
- `*_eval_report.txt`：更适合人工阅读的评估报告；
- `*_config.yaml`：本次运行最终使用的完整配置快照；
- `*_llm_usage.csv`：按请求记录 provider、模型和 token 使用情况；
- `*_llm_usage_summary.csv`：聚合后的 usage 统计；
- `*_timing.csv`：阶段耗时；
- `*_stage2_skipped.csv`：Stage-2 失败或跳过的细胞及错误信息；
- `*_inspect.jsonl` 和对应 Markdown：指定细胞的 prompt、响应和调试信息。

## 已有配置和启动脚本

配置模板位于 `configs/`，包括：

- PBMC：`pbmc_l2_expr.yaml`、`pbmc_l2_knn.yaml`、`pbmc_l2_pseudobulk.yaml`、`pbmc_l2_random.yaml`、`pbmc_l2_single.yaml`、`pbmc_l2_tfidf.yaml`、`pbmc_l2_zscore.yaml`；
- HLCA：`hlca_celltype_knn.yaml`、`hlca_celltype_pseudobulk.yaml`、`hlca_celltype_random.yaml`、`hlca_celltype_single.yaml`；
- 结果修复：`pbmc_result_fixer.yaml`、`hlca_result_fixer.yaml`；
- marker panel：`configs/markers/pbmc_broad_lineage.yaml`。

对应的 shell 脚本在 `scripts/` 中，例如：

```bash
bash scripts/pbmc_l2_knn.sh
bash scripts/hlca_celltype_pseudobulk.sh
```

这些脚本通常包含数据路径和运行参数，执行前请检查其中的路径、API key 配置和输出目录。Windows 下若没有 Bash，可直接使用同名 YAML 调用 `python run_experiment.py`。

## 新建实验

推荐流程：

1. 复制一个最接近目标数据和实验目的的 YAML；
2. 修改 `dataset_path`、`tissue`、`evaluation.label_col`；
3. 选择 `input.mode`、`selection.strategy` 和 LLM backend；
4. 先执行 `--dry-run` 检查 YAML；
5. 用较小的 `n_per_class` 做试运行；
6. 核对 `*_results.csv`、`*_eval.csv`、usage 和 timing；
7. 最后再提高抽样数量或并发数，并保留最终配置快照。

## 故障排查

### 配置无法解析

先运行：

```bash
python run_experiment.py configs/pbmc_l2_knn.yaml --dry-run
```

检查 YAML 缩进、字段拼写和 `configs/` 中同类模板。`dataset_path` 缺失时 dry-run 可以通过，但正式运行会报错。

### API key 或 provider 错误

- 确认 `.env` 位于项目根目录，或变量已存在于当前 shell；
- 确认 `llm.api_key_env` 与变量名完全一致；
- 确认 `llm.backend` 是 `gemini`、`claude`、`openai`、`deepseek` 或 `openrouter`；
- 检查模型 ID 是否被所选 provider 支持；
- 降低 `concurrency`，避免触发 provider 限流。

### HLCA 找不到组织

HLCA 必须设置 `tissue`，并且字符串要和 `adata.obs["tissue"]` 中的值完全一致，例如 `respiratory airway`、`lung parenchyma` 或 `nose`。

### kNN 或 ADT 报错

- `knn_smoothed` 默认查找 `adata.obsm["X_pca"]`；缺失时应允许代码计算 PCA，或将 `knn_use_rep` 改为数据中已有的 representation；
- 使用 `modalities: [rna, adt]` 前确认 `protein_counts` 和 `ADT_names` 都存在；
- `knn_k` 不应大于可用细胞数。

### Stage-2 失败

先关闭 `stage2.enabled` 验证第一阶段是否正常。若只有少数细胞失败，查看 `stage2/*_stage2_skipped.csv`；若后端为 Claude，需要改用支持 Stage-2 JSON 查询的 `gemini`、`openai`、`deepseek` 或 `openrouter`。

## 主要代码入口

- CLI：`run_experiment.py`
- 配置模型：`sc_annotation/config.py`
- 主流水线：`sc_annotation/pipeline.py`
- 数据加载与抽样：`sc_annotation/data.py`
- 基因过滤：`sc_annotation/filtering.py`
- 特征选择：`sc_annotation/selection.py`
- prompt：`sc_annotation/prompts.py`
- 评估：`sc_annotation/metrics.py`
- Stage-2：`sc_annotation/stage2.py`
- LLM 后端：`sc_annotation/backends/`

项目没有安装为独立 Python package，CLI 会把仓库根目录加入 import path。因此运行命令时应在仓库根目录执行，或者使用配置文件和脚本中的正确相对路径。
