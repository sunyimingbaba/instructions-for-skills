# 统计、机器学习与时序分析

用于统计建模、预测、分类、聚类、因果或不确定性分析。

本页收录 **24** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$aeon`](#skill-aeon) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `aeon` 的专项能力，主要用于分析时间序列并进行预测，并可完成机器学习建模与评估。 |
| [`$cirq`](#skill-cirq) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `cirq` 的专项能力，主要用于规划、运行或复盘实验。 |
| [`$codex-autoresearch`](#skill-codex-autoresearch) | [Codex Autoresearch](../技能套件导航.md#suite-codex-autoresearch) | 围绕 `codex-autoresearch` 的专项能力，主要用于规划、运行或复盘实验。 |
| [`$exploratory-data-analysis`](#skill-exploratory-data-analysis) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `exploratory-data-analysis` 相关任务。 |
| [`$hypothesis-generation`](#skill-hypothesis-generation) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `hypothesis-generation` 相关任务。 |
| [`$market-research-reports`](#skill-market-research-reports) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `market-research-reports` 的专项能力，主要用于分析时间序列并进行预测。 |
| [`$optimize-for-gpu`](#skill-optimize-for-gpu) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `optimize-for-gpu` 相关任务。 |
| [`$pennylane`](#skill-pennylane) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pennylane` 相关任务。 |
| [`$pylabrobot`](#skill-pylabrobot) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pylabrobot` 相关任务。 |
| [`$pymc`](#skill-pymc) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pymc` 相关任务。 |
| [`$pymoo`](#skill-pymoo) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pymoo` 相关任务。 |
| [`$qiskit`](#skill-qiskit) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `qiskit` 相关任务。 |
| [`$scikit-learn`](#skill-scikit-learn) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `scikit-learn` 的专项能力，主要用于完成机器学习建模与评估。 |
| [`$scikit-survival`](#skill-scikit-survival) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `scikit-survival` 相关任务。 |
| [`$shap`](#skill-shap) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `shap` 的专项能力，主要用于生成或检查科研图表。 |
| [`$simpy`](#skill-simpy) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `simpy` 相关任务。 |
| [`$statistical-analysis`](#skill-statistical-analysis) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `statistical-analysis` 的专项能力，主要用于完成机器学习建模与评估，并可规划、运行或复盘实验。 |
| [`$statistical-power`](#skill-statistical-power) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `statistical-power` 的专项能力，主要用于完成机器学习建模与评估，并可规划、运行或复盘实验。 |
| [`$statsmodels`](#skill-statsmodels) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `statsmodels` 的专项能力，主要用于分析时间序列并进行预测。 |
| [`$timesfm-forecasting`](#skill-timesfm-forecasting) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `timesfm-forecasting` 的专项能力，主要用于分析时间序列并进行预测。 |
| [`$torch-geometric`](#skill-torch-geometric) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `torch-geometric` 的专项能力，主要用于完成机器学习建模与评估。 |
| [`$umap-learn`](#skill-umap-learn) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `umap-learn` 的专项能力，主要用于完成机器学习建模与评估。 |
| [`$usfiscaldata`](#skill-usfiscaldata) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `usfiscaldata` 相关任务。 |
| [`$what-if-oracle`](#skill-what-if-oracle) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `what-if-oracle` 的专项能力，主要用于分析时间序列并进行预测，并可规划、运行或复盘实验。 |

## 详细说明

<a id="skill-aeon"></a>
### `$aeon`

- 全局目录：`~/.codex/skills/aeon/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `aeon` 的专项能力，主要用于分析时间序列并进行预测，并可完成机器学习建模与评估。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $aeon。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection, segmentation, and similarity search. Use when working with temporal data, sequential patterns, or time-indexed observations requiring specialized algorithms beyond standard ML approaches. Particularly suited for univariate and multivariate time series analysis with scikit-learn compatible APIs.

</details>

上游线索：[https://github.com/aeon-toolkit/aeon](https://github.com/aeon-toolkit/aeon)

<a id="skill-cirq"></a>
### `$cirq`

- 全局目录：`~/.codex/skills/cirq/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `cirq` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $cirq。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Google quantum computing framework. Use when targeting Google Quantum AI hardware, designing noise-aware circuits, or running quantum characterization experiments. Best for Google hardware, noise modeling, and low-level circuit design. For IBM hardware use qiskit; for quantum ML with autodiff use pennylane; for physics simulations use qutip.

</details>

上游线索：[https://github.com/quantumlib/Cirq](https://github.com/quantumlib/Cirq)

<a id="skill-codex-autoresearch"></a>
### `$codex-autoresearch`

- 全局目录：`~/.codex/skills/codex-autoresearch/`
- 所属技能套件：[Codex Autoresearch](../技能套件导航.md#suite-codex-autoresearch)
- 推荐总入口：`$codex-autoresearch`
- 中文理解：围绕 `codex-autoresearch` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $codex-autoresearch。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Run repeated, measured Git experiments toward a numeric target; keep improvements and revert failures. Use for autonomous optimization or managing an autoresearch run, not one-shot edits.

</details>

<a id="skill-exploratory-data-analysis"></a>
### `$exploratory-data-analysis`

- 全局目录：`~/.codex/skills/exploratory-data-analysis/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `exploratory-data-analysis` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $exploratory-data-analysis。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs bounded, local exploratory analysis of explicitly supported scientific files. Supports redacted CSV/TSV/JSON profiles; optional NumPy, HDF5, FASTA/FASTQ, and basic image metadata inspection; missingness/leakage audits; outlier and transformation sensitivity; and rigorous EDA report scaffolds. Other domain formats are reference-only and unknown formats fail closed.

</details>

<a id="skill-hypothesis-generation"></a>
### `$hypothesis-generation`

- 全局目录：`~/.codex/skills/hypothesis-generation/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `hypothesis-generation` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hypothesis-generation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Formulates evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims, discriminating predictions, measurements, and preregistration-ready analysis plans. Used when turning observations or preliminary findings into transparent, testable research plans without treating hypotheses as facts.

</details>

<a id="skill-market-research-reports"></a>
### `$market-research-reports`

- 全局目录：`~/.codex/skills/market-research-reports/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `market-research-reports` 的专项能力，主要用于分析时间序列并进行预测。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $market-research-reports。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds evidence-traceable market research reports and assumption-driven market sizing or forecast scenarios. Use for market definition, industry and customer evidence, competitive landscapes, TAM/SAM/SOM reconciliation, forecast sensitivity, and auditable report scaffolds.

</details>

<a id="skill-optimize-for-gpu"></a>
### `$optimize-for-gpu`

- 全局目录：`~/.codex/skills/optimize-for-gpu/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `optimize-for-gpu` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $optimize-for-gpu。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

GPU-accelerates scientific Python on NVIDIA hardware and verifies that the result is correct and faster. Use for CUDA/GPU optimization; CPU-bound NumPy, SciPy, pandas, scikit-learn, NetworkX, scikit-image, vector-search, image-processing, graph, simulation, or file-I/O workloads; CuPy, cuDF, cuML, cuGraph, cuVS, cuCIM, KvikIO, Warp, Newton, Numba-CUDA, or RAFT questions; and profiling, memory-transfer, kernel, or multi-GPU bottlenecks. Also use when large data-parallel Python code is slow and GPU acceleration is a plausible option, even if the user does not name CUDA.

</details>

<a id="skill-pennylane"></a>
### `$pennylane`

- 全局目录：`~/.codex/skills/pennylane/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pennylane` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pennylane。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and differentiates PennyLane quantum circuits, hybrid PyTorch or JAX models, molecular VQE and QAOA workflows. Use for variational quantum algorithms, quantum machine learning, simulator validation, and moving validated circuits to provider plugins. For hardware-specific compilation use qiskit or cirq; for open-system dynamics use qutip.

</details>

上游线索：[https://github.com/PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)

<a id="skill-pylabrobot"></a>
### `$pylabrobot`

- 全局目录：`~/.codex/skills/pylabrobot/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pylabrobot` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pylabrobot。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Develops and reviews PyLabRobot lab-automation resources, liquid-handling plans, offline simulations, and supported-device integrations. Supports PyLabRobot protocols and API questions; keep physical execution behind an explicit operator safety gate.

</details>

上游线索：[https://github.com/PyLabRobot/pylabrobot](https://github.com/PyLabRobot/pylabrobot)

<a id="skill-pymc"></a>
### `$pymc`

- 全局目录：`~/.codex/skills/pymc/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pymc` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $pymc。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and checks Bayesian models with PyMC, including hierarchical models, NUTS MCMC, variational inference, mutable-data predictions, posterior predictive checks, diagnostics, and PSIS-LOO model comparison. Use for probabilistic modeling and uncertainty inference in PyMC.

</details>

<a id="skill-pymoo"></a>
### `$pymoo`

- 全局目录：`~/.codex/skills/pymoo/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `pymoo` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pymoo。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Solves and validates single-, multi-, and many-objective optimization with pymoo, including NSGA-II, NSGA-III, MOEA/D, constraints, Pareto approximations, reference directions, and ZDT/DTLZ benchmarks for engineering and research problems.

</details>

<a id="skill-qiskit"></a>
### `$qiskit`

- 全局目录：`~/.codex/skills/qiskit/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `qiskit` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $qiskit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds, simulates, transpiles, and executes quantum circuits with Qiskit and IBM Quantum Runtime. Use for Qiskit 2.x circuits and operators, V2 Sampler or Estimator primitives, target-aware transpilation, local or noisy simulation, IBM QPU execution, Runtime sessions or batches, error mitigation, and Qiskit ecosystem packages.

</details>

<a id="skill-scikit-learn"></a>
### `$scikit-learn`

- 全局目录：`~/.codex/skills/scikit-learn/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `scikit-learn` 的专项能力，主要用于完成机器学习建模与评估。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scikit-learn。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports machine learning in Python with scikit-learn. Applies when working with supervised learning (classification, regression), unsupervised learning (clustering, dimensionality reduction), model evaluation, hyperparameter tuning, preprocessing, or building ML pipelines. Provides comprehensive reference documentation for algorithms, preprocessing techniques, pipelines, and best practices.

</details>

<a id="skill-scikit-survival"></a>
### `$scikit-survival`

- 全局目录：`~/.codex/skills/scikit-survival/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `scikit-survival` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scikit-survival。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds, evaluates, and audits right-censored or competing-risk survival workflows with scikit-survival, including leakage-safe preprocessing, model selection, probability prediction, and censoring-aware metrics.

</details>

上游线索：[https://github.com/sebp/scikit-survival](https://github.com/sebp/scikit-survival)

<a id="skill-shap"></a>
### `$shap`

- 全局目录：`~/.codex/skills/shap/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `shap` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $shap。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Explain and audit machine-learning predictions with SHAP. Use for selecting SHAP explainers and maskers, computing and validating feature attributions, handling multi-output explanations, and producing local or global SHAP visualizations.

</details>

上游线索：[https://github.com/shap/shap](https://github.com/shap/shap)

<a id="skill-simpy"></a>
### `$simpy`

- 全局目录：`~/.codex/skills/simpy/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `simpy` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $simpy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds, inspects, tests, and analyzes bounded process-based discrete-event simulations with SimPy. Use for event scheduling, resource queues, interrupts, monitoring, independent replications, warm-up, and reproducible output analysis.

</details>

<a id="skill-statistical-analysis"></a>
### `$statistical-analysis`

- 全局目录：`~/.codex/skills/statistical-analysis/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `statistical-analysis` 的专项能力，主要用于完成机器学习建模与评估，并可规划、运行或复盘实验。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $statistical-analysis。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Guided statistical analysis for research data - test selection, assumption checking, effect sizes, power analysis, Bayesian alternatives, and APA-formatted reporting. Use whenever a user wants to compare groups, test a hypothesis, analyze experimental or survey data, check statistical assumptions, compute required sample sizes, or write up results - even if they never name a specific test. Covers t-tests, ANOVA, chi-square, correlation, regression, non-parametric and Bayesian methods. For low-level model APIs, see the statsmodels and pymc skills.

</details>

<a id="skill-statistical-power"></a>
### `$statistical-power`

- 全局目录：`~/.codex/skills/statistical-power/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `statistical-power` 的专项能力，主要用于完成机器学习建模与评估，并可规划、运行或复盘实验。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $statistical-power。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Calculates sample sizes and statistical power for study planning. Applies when someone asks "how many subjects/samples/replicates do I need", wants an a priori power analysis, a minimum detectable effect (MDE), a power curve, or needs to justify a sample size for a grant, IRB protocol, or pre-registration. Covers closed-form power for t-tests, ANOVA, proportions, correlations, chi-square, and regression, plus simulation-based (Monte Carlo) power for complex designs — logistic/Poisson regression, mixed models, cluster-randomized trials, survival, and interactions. Also handles requests that only mention an effect size, alpha, or "80% power" without saying "power analysis" explicitly. For laying out the study (randomization, blocking, factorial/DOE, crossover, sequential designs) use experimental-design; for analyzing data already collected and reporting it use statistical-analysis.

</details>

<a id="skill-statsmodels"></a>
### `$statsmodels`

- 全局目录：`~/.codex/skills/statsmodels/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `statsmodels` 的专项能力，主要用于分析时间序列并进行预测。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $statsmodels。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fits and diagnoses Python statistical models including OLS, GLM, discrete and mixed models, ARIMA and SARIMAX. Supports coefficient inference, marginal effects, model comparison and time series forecasting with explicit design and uncertainty checks. Used for econometrics and statistical modeling; for guided test selection with APA reporting, see statistical-analysis.

</details>

<a id="skill-timesfm-forecasting"></a>
### `$timesfm-forecasting`

- 全局目录：`~/.codex/skills/timesfm-forecasting/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `timesfm-forecasting` 的专项能力，主要用于分析时间序列并进行预测。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $timesfm-forecasting。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs zero-shot time-series forecasting with Google's TimesFM, including regular-grid CSV preparation, quantile forecasts, XReg covariates, and held-out evaluation. Uses the Apache-licensed TimesFM 2.5 checkpoint by default and documents the distinct TimesFM 3.0 multivariate API and weight-license requirements.

</details>

上游线索：[https://github.com/google-research/timesfm](https://github.com/google-research/timesfm)

<a id="skill-torch-geometric"></a>
### `$torch-geometric`

- 全局目录：`~/.codex/skills/torch-geometric/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `torch-geometric` 的专项能力，主要用于完成机器学习建模与评估。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $torch-geometric。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports PyTorch Geometric (PyG) graph neural networks — node/link/graph classification, message passing (GCN, GAT, GraphSAGE, GIN), heterogeneous graphs, neighbor sampling, and custom datasets. Use when working with torch_geometric, not for general NetworkX analytics or non-graph PyTorch models.

</details>

上游线索：[https://github.com/pyg-team/pytorch_geometric](https://github.com/pyg-team/pytorch_geometric)

<a id="skill-umap-learn"></a>
### `$umap-learn`

- 全局目录：`~/.codex/skills/umap-learn/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `umap-learn` 的专项能力，主要用于完成机器学习建模与评估。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $umap-learn。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Applies UMAP-learn to nonlinear dimensionality reduction, 2D/3D embeddings, clustering preprocessing, supervised or semi-supervised UMAP, DensMAP, AlignedUMAP, and Parametric UMAP workflows.

</details>

上游线索：[https://github.com/lmcinnes/umap](https://github.com/lmcinnes/umap)

<a id="skill-usfiscaldata"></a>
### `$usfiscaldata`

- 全局目录：`~/.codex/skills/usfiscaldata/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“统计、机器学习与时序分析”的专项技能，用于处理 `usfiscaldata` 相关任务。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $usfiscaldata。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries the U.S. Treasury Fiscal Data REST API for federal financial data. No API key required. Use for national debt (Debt to the Penny), Daily Treasury Statements, Monthly Treasury Statements, Treasury securities auctions, interest rates, foreign exchange rates, savings bonds, or U.S. government revenue and spending statistics.

</details>

<a id="skill-what-if-oracle"></a>
### `$what-if-oracle`

- 全局目录：`~/.codex/skills/what-if-oracle/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `what-if-oracle` 的专项能力，主要用于分析时间序列并进行预测，并可规划、运行或复盘实验。
- 适合何时使用：用于统计建模、预测、分类、聚类、因果或不确定性分析。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $what-if-oracle。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports structured what-if scenario analysis for research planning, experimental contingencies, and scientific project decisions. Explores favorable, reference, adverse, wild-card, contrarian, and second-order scenarios with explicit assumptions, evidence, and decision triggers. Use to stress-test a research plan under uncertainty; scenario narratives do not estimate causal effects or calibrated forecast probabilities.

</details>

上游线索：[https://github.com/ashrafkahoush-ux/claude-consciousness-skills](https://github.com/ashrafkahoush-ux/claude-consciousness-skills)

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
