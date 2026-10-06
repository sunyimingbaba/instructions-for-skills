# 数据工程、计算与云平台

处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。

本页收录 **25** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 一句话理解 |
| --- | --- |
| [`$dask`](#skill-dask) | 围绕 `dask` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$database-lookup`](#skill-database-lookup) | 围绕 `database-lookup` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$experiment-tracking-swanlab`](#skill-swanlab) | 围绕 `experiment-tracking-swanlab` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$hatch-pet`](#skill-hatch-pet) | 围绕 `hatch-pet` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$lambda-labs-gpu-cloud`](#skill-lambda-labs) | 围绕 `lambda-labs-gpu-cloud` 的专项能力，主要用于使用云端或 GPU 计算资源。 |
| [`$matlab`](#skill-matlab) | 围绕 `matlab` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$mlflow`](#skill-mlflow) | 这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `mlflow` 相关任务。 |
| [`$modal`](#skill-modal) | 围绕 `modal` 的专项能力，主要用于使用云端或 GPU 计算资源。 |
| [`$nature-shared`](#skill-nature-shared) | 围绕 `nature-shared` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$nemo-curator`](#skill-nemo-curator) | 围绕 `nemo-curator` 的专项能力，主要用于使用云端或 GPU 计算资源。 |
| [`$nextflow`](#skill-nextflow) | 围绕 `nextflow` 的专项能力，主要用于组织可复现的科研流程，并可使用云端或 GPU 计算资源。 |
| [`$overleaf-sync`](#skill-overleaf-sync) | 围绕 `overleaf-sync` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$parallel-web`](#skill-parallel-web) | 这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `parallel-web` 相关任务。 |
| [`$polars`](#skill-polars) | 围绕 `polars` 的专项能力，主要用于使用云端或 GPU 计算资源。 |
| [`$pytdc`](#skill-pytdc) | 围绕 `pytdc` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$qutip`](#skill-qutip) | 围绕 `qutip` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$qzcli`](#skill-qzcli) | Manage GPU compute jobs on the Qizhi (启智) platform using qzcli — a kubectl-style CLI tool. |
| [`$ray-data`](#skill-ray-data) | 围绕 `ray-data` 的专项能力，主要用于组织可复现的科研流程，并可使用云端或 GPU 计算资源。 |
| [`$resubmit-pipeline`](#skill-resubmit-pipeline) | 围绕 `resubmit-pipeline` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$serverless-modal`](#skill-serverless-modal) | 围绕 `serverless-modal` 的专项能力，主要用于使用云端或 GPU 计算资源。 |
| [`$skypilot-multi-cloud-orchestration`](#skill-skypilot) | 围绕 `skypilot-multi-cloud-orchestration` 的专项能力，主要用于使用云端或 GPU 计算资源。 |
| [`$tensorboard`](#skill-tensorboard) | 这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `tensorboard` 相关任务。 |
| [`$vaex`](#skill-vaex) | 这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `vaex` 相关任务。 |
| [`$weights-and-biases`](#skill-weights-and-biases) | 这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `weights-and-biases` 相关任务。 |
| [`$zarr-python`](#skill-zarr-python) | 这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `zarr-python` 相关任务。 |

## 详细说明

<a id="skill-dask"></a>
### `$dask`

- 全局目录：`~/.codex/skills/dask/`
- 中文理解：围绕 `dask` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $dask。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Scales pandas, NumPy, and custom Python research workflows beyond memory or across clusters with Dask. Covers DataFrames, Arrays, Bags, Futures, chunking, schedulers, and distributed diagnostics. Use for partitioned file processing, scientific array computation, or parallel tasks whose memory and dependency structure require Dask.

</details>

<a id="skill-database-lookup"></a>
### `$database-lookup`

- 全局目录：`~/.codex/skills/database-lookup/`
- 中文理解：围绕 `database-lookup` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $database-lookup。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries documented public database APIs with explicit endpoints, filters, pagination, and provenance. Used when a scientific, regulatory, financial, or other database-backed fact must be retrieved reproducibly from a named source rather than inferred from general knowledge.

</details>

<a id="skill-swanlab"></a>
### `$experiment-tracking-swanlab`

- 全局目录：`~/.codex/skills/swanlab/`
- 中文理解：围绕 `experiment-tracking-swanlab` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $experiment-tracking-swanlab。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for experiment tracking with SwanLab. Use when you need open-source run tracking, local or self-hosted dashboards, and lightweight media logging for ML workflows.

</details>

上游线索：[https://github.com/SwanHubX/SwanLab](https://github.com/SwanHubX/SwanLab)

<a id="skill-hatch-pet"></a>
### `$hatch-pet`

- 全局目录：`~/.codex/skills/hatch-pet/`
- 中文理解：围绕 `hatch-pet` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $hatch-pet。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from character art, generated images, company or prospect brand cues, or visual references. Use for any new Codex pet, custom mascot, non-pixel pet style, brand-inspired pet, existing-pet repair, or 8x11 spritesheet workflow requiring all 9 standard animation rows, 16 look directions, deterministic assembly, QA artifacts, and spriteVersionNumber 2 packaging.

</details>

<a id="skill-lambda-labs"></a>
### `$lambda-labs-gpu-cloud`

- 全局目录：`~/.codex/skills/lambda-labs/`
- 中文理解：围绕 `lambda-labs-gpu-cloud` 的专项能力，主要用于使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $lambda-labs-gpu-cloud。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reserved and on-demand GPU cloud instances for ML training and inference. Use when you need dedicated GPU instances with simple SSH access, persistent filesystems, or high-performance multi-node clusters for large-scale training.

</details>

上游线索：[https://github.com/user/project](https://github.com/user/project)

<a id="skill-matlab"></a>
### `$matlab`

- 全局目录：`~/.codex/skills/matlab/`
- 中文理解：围绕 `matlab` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $matlab。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds, reviews, migrates, and plans MATLAB or GNU Octave numerical workflows. Use for arrays, tabular/time data, tests, projects, graphics, MAT files, and explicit Python interoperability.

</details>

<a id="skill-mlflow"></a>
### `$mlflow`

- 全局目录：`~/.codex/skills/mlflow/`
- 中文理解：这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `mlflow` 相关任务。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $mlflow。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Track ML experiments, manage model registry with versioning, deploy models to production, and reproduce experiments with MLflow - framework-agnostic ML lifecycle platform

</details>

上游线索：[https://github.com/mlflow/mlflow](https://github.com/mlflow/mlflow)

<a id="skill-modal"></a>
### `$modal`

- 全局目录：`~/.codex/skills/modal/`
- 中文理解：围绕 `modal` 的专项能力，主要用于使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $modal。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Modal is a serverless cloud platform for running Python on demand, including on-demand GPUs. Use when deploying or serving AI/ML models, running GPU-accelerated workloads (training, fine-tuning, inference), serving web endpoints, scheduling batch jobs, or scaling Python code to cloud containers with the Modal SDK.

</details>

<a id="skill-nature-shared"></a>
### `$nature-shared`

- 全局目录：`~/.codex/skills/nature-shared/`
- 中文理解：围绕 `nature-shared` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $nature-shared。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Internal shared-reference support package for installed Nature Skills, including nature-writing, nature-polishing, nature-response, nature-reader, and nature-paper2ppt. Do not invoke it as a standalone user workflow. Load only the specific core or journal-format file requested by another Nature skill.

</details>

<a id="skill-nemo-curator"></a>
### `$nemo-curator`

- 全局目录：`~/.codex/skills/nemo-curator/`
- 中文理解：围绕 `nemo-curator` 的专项能力，主要用于使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $nemo-curator。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

GPU-accelerated data curation for LLM training. Supports text/image/video/audio. Features fuzzy deduplication (16× faster), quality filtering (30+ heuristics), semantic deduplication, PII redaction, NSFW detection. Scales across GPUs with RAPIDS. Use for preparing high-quality training datasets, cleaning web data, or deduplicating large corpora.

</details>

上游线索：[https://github.com/NVIDIA/NeMo-Curator](https://github.com/NVIDIA/NeMo-Curator)

<a id="skill-nextflow"></a>
### `$nextflow`

- 全局目录：`~/.codex/skills/nextflow/`
- 中文理解：围绕 `nextflow` 的专项能力，主要用于组织可复现的科研流程，并可使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $nextflow。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds, runs, and debugs Nextflow DSL2 pipelines and nf-core workflows. Use for Nextflow, nf-core, .nf files, nextflow.config, processes/channels/operators, samplesheets, nf-test, modules/subworkflows, container and executor configuration, HPC/SLURM or cloud deployment, and failed or resumed pipeline runs.

</details>

上游线索：[https://github.com/nextflow-io/nextflow](https://github.com/nextflow-io/nextflow)

<a id="skill-overleaf-sync"></a>
### `$overleaf-sync`

- 全局目录：`~/.codex/skills/overleaf-sync/`
- 中文理解：围绕 `overleaf-sync` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $overleaf-sync。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Two-way sync between a local paper directory and an Overleaf project, so ARIS audit/edit workflows stay on the local copy while collaborators edit in the Overleaf web UI. Use when user says "同步 overleaf", "overleaf sync", "推送到 overleaf", "connect overleaf", "Overleaf 桥接", "pull overleaf", "push overleaf", or wants to bridge their ARIS paper directory with an Overleaf project.

</details>

<a id="skill-parallel-web"></a>
### `$parallel-web`

- 全局目录：`~/.codex/skills/parallel-web/`
- 中文理解：这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `parallel-web` 相关任务。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $parallel-web。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Uses Parallel CLI for web search, URL extraction, deep research, structured data enrichment, entity discovery, and recurring web monitoring. Best for requests that explicitly need current web evidence, academic-source discovery, repeated entity lookups, exhaustive reports, or ongoing change tracking.

</details>

<a id="skill-polars"></a>
### `$polars`

- 全局目录：`~/.codex/skills/polars/`
- 中文理解：围绕 `polars` 的专项能力，主要用于使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $polars。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

High-performance DataFrame library for Python ETL, analytics, and pandas migration. It supports expression-based data manipulation with lazy query optimization, parallel execution, streaming out-of-core processing, Arrow interoperability, and optional GPU execution.

</details>

上游线索：[https://github.com/pola-rs/polars](https://github.com/pola-rs/polars)

<a id="skill-pytdc"></a>
### `$pytdc`

- 全局目录：`~/.codex/skills/pytdc/`
- 中文理解：围绕 `pytdc` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pytdc。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides Therapeutics Data Commons workflows through PyTDC for registry discovery, dataset access, task-aware splits, evaluator metrics, benchmark groups, and bounded molecular-oracle scoring. Use when working with TDC therapeutic ML datasets or benchmarks.

</details>

<a id="skill-qutip"></a>
### `$qutip`

- 全局目录：`~/.codex/skills/qutip/`
- 中文理解：围绕 `qutip` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $qutip。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Simulate and audit closed and open quantum-system models with QuTiP 5, including deterministic, trajectory, steady-state, spectral, and phase-space workflows. Use for local quantum-dynamics work where physical assumptions, dimensions, and numerical convergence must be explicit.

</details>

上游线索：[https://github.com/qutip/qutip](https://github.com/qutip/qutip)

<a id="skill-qzcli"></a>
### `$qzcli`

- 全局目录：`~/.codex/skills/qzcli/`
- 中文理解：Manage GPU compute jobs on the Qizhi (启智) platform using qzcli — a kubectl-style CLI tool.
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $qzcli。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Manage GPU compute jobs on the Qizhi (启智) platform using qzcli — a kubectl-style CLI tool. Use when user says "qzcli", "启智平台", "submit job", "stop job", "查计算组", "avail", "list jobs", "batch submit", or needs to manage distributed training jobs on a Qizhi instance.

</details>

上游线索：[https://github.com/tianyilt/qzcli_tool](https://github.com/tianyilt/qzcli_tool)

<a id="skill-ray-data"></a>
### `$ray-data`

- 全局目录：`~/.codex/skills/ray-data/`
- 中文理解：围绕 `ray-data` 的专项能力，主要用于组织可复现的科研流程，并可使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $ray-data。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Scalable data processing for ML workloads. Streaming execution across CPU/GPU, supports Parquet/CSV/JSON/images. Integrates with Ray Train, PyTorch, TensorFlow. Scales from single machine to 100s of nodes. Use for batch inference, data preprocessing, multi-modal data loading, or distributed ETL pipelines.

</details>

上游线索：[https://github.com/ray-project/ray](https://github.com/ray-project/ray)

<a id="skill-resubmit-pipeline"></a>
### `$resubmit-pipeline`

- 全局目录：`~/.codex/skills/resubmit-pipeline/`
- 中文理解：围绕 `resubmit-pipeline` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $resubmit-pipeline。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Workflow 5: orchestrate a text-only resubmit of a polished paper to a different venue under hard constraints (no new experiments, no bib edits, no framework changes, never overwrite prior submissions). Use when user says "resubmit pipeline", "重投流程", "port paper to <new venue>", "resubmit to <venue>", "tighten paper for resubmission", or has a rejected/withdrawn paper to move to a different top venue under tight time budget.

</details>

<a id="skill-serverless-modal"></a>
### `$serverless-modal`

- 全局目录：`~/.codex/skills/serverless-modal/`
- 中文理解：围绕 `serverless-modal` 的专项能力，主要用于使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $serverless-modal。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Run GPU workloads on Modal — training, fine-tuning, inference, batch processing. Zero-config serverless: no SSH, no Docker, auto scale-to-zero. Use when user says "modal run", "modal training", "modal inference", "deploy to modal", "need a GPU", "run on modal", "serverless GPU", or needs remote GPU compute.

</details>

<a id="skill-skypilot"></a>
### `$skypilot-multi-cloud-orchestration`

- 全局目录：`~/.codex/skills/skypilot/`
- 中文理解：围绕 `skypilot-multi-cloud-orchestration` 的专项能力，主要用于使用云端或 GPU 计算资源。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $skypilot-multi-cloud-orchestration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Multi-cloud orchestration for ML workloads with automatic cost optimization. Use when you need to run training or batch jobs across multiple clouds, leverage spot instances with auto-recovery, or optimize GPU costs across providers.

</details>

上游线索：[https://github.com/skypilot-org/skypilot](https://github.com/skypilot-org/skypilot)

<a id="skill-tensorboard"></a>
### `$tensorboard`

- 全局目录：`~/.codex/skills/tensorboard/`
- 中文理解：这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `tensorboard` 相关任务。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $tensorboard。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Visualize training metrics, debug models with histograms, compare experiments, visualize model graphs, and profile performance with TensorBoard - Google's ML visualization toolkit

</details>

上游线索：[https://github.com/tensorflow/tensorboard](https://github.com/tensorflow/tensorboard)

<a id="skill-vaex"></a>
### `$vaex`

- 全局目录：`~/.codex/skills/vaex/`
- 中文理解：这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `vaex` 相关任务。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $vaex。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Processes large tabular scientific datasets with Vaex expressions, filtered views, streamed statistics, binned visualizations, and file conversion. Use for larger-than-RAM HDF5, Arrow, CSV, or Parquet analysis, virtual feature engineering, or Vaex ML preprocessing; distinguishes these operations from estimators and conversions that materialize data.

</details>

<a id="skill-weights-and-biases"></a>
### `$weights-and-biases`

- 全局目录：`~/.codex/skills/weights-and-biases/`
- 中文理解：这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `weights-and-biases` 相关任务。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $weights-and-biases。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Track ML experiments with automatic logging, visualize training in real-time, optimize hyperparameters with sweeps, and manage model registry with W&B - collaborative MLOps platform

</details>

上游线索：[https://github.com/wandb/wandb](https://github.com/wandb/wandb)

<a id="skill-zarr-python"></a>
### `$zarr-python`

- 全局目录：`~/.codex/skills/zarr-python/`
- 中文理解：这是一个面向“数据工程、计算与云平台”的专项技能，用于处理 `zarr-python` 相关任务。
- 适合何时使用：处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $zarr-python。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Stores and queries chunked N-D scientific arrays with Zarr-Python 3, including codecs, sharding, S3/GCS storage, and NumPy/Dask/Xarray integration. Use for array layout, bounded I/O, format migration, or scientific metadata preservation.

</details>

上游线索：[https://github.com/zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python)

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
