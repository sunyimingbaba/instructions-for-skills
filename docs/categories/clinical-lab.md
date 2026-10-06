# 医学、临床与实验室规范

支持临床研究、实验室方法验证、标准体系和医学数据工作流。

本页收录 **28** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$13c-metabolic-flux`](#skill-13c-metabolic-flux) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `13c-metabolic-flux` 相关任务。 |
| [`$adaptyv`](#skill-adaptyv) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `adaptyv` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$alphagenome`](#skill-alphagenome) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `alphagenome` 的专项能力，主要用于支持医学与临床研究分析。 |
| [`$analytical-method-validation`](#skill-analytical-method-validation) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `analytical-method-validation` 相关任务。 |
| [`$bids`](#skill-bids) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `bids` 的专项能力，主要用于处理科研或医学影像，并可支持医学与临床研究分析。 |
| [`$cellprofiler`](#skill-cellprofiler) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `cellprofiler` 的专项能力，主要用于处理科研或医学影像，并可组织可复现的科研流程。 |
| [`$cellxgene-census`](#skill-cellxgene-census) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `cellxgene-census` 相关任务。 |
| [`$clinical-decision-support`](#skill-clinical-decision-support) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `clinical-decision-support` 的专项能力，主要用于支持医学与临床研究分析。 |
| [`$clinical-reports`](#skill-clinical-reports) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `clinical-reports` 的专项能力，主要用于检查问题并给出修改建议，并可支持医学与临床研究分析。 |
| [`$experimental-design`](#skill-experimental-design) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `experimental-design` 相关任务。 |
| [`$fluidsim`](#skill-fluidsim) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `fluidsim` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$genomic-coordinates`](#skill-genomic-coordinates) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `genomic-coordinates` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$ginkgo-cloud-lab`](#skill-ginkgo-cloud-lab) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `ginkgo-cloud-lab` 相关任务。 |
| [`$glycoengineering`](#skill-glycoengineering) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `glycoengineering` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$iso-standards-readiness`](#skill-iso-standards-readiness) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `iso-standards-readiness` 的专项能力，主要用于检查问题并给出修改建议，并可支持医学与临床研究分析。 |
| [`$ncats-arax`](#skill-ncats-arax) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `ncats-arax` 的专项能力，主要用于支持医学与临床研究分析。 |
| [`$neurokit2`](#skill-neurokit2) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `neurokit2` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。 |
| [`$onekgpd`](#skill-onekgpd) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `onekgpd` 相关任务。 |
| [`$ontology-term-resolution`](#skill-ontology-term-resolution) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `ontology-term-resolution` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$pacsomatic`](#skill-pacsomatic) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pacsomatic` 的专项能力，主要用于处理科研或医学影像，并可支持医学与临床研究分析。 |
| [`$pkpd-modeling`](#skill-pkpd-modeling) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `pkpd-modeling` 相关任务。 |
| [`$primer-design`](#skill-primer-design) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `primer-design` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$pyhealth`](#skill-pyhealth) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pyhealth` 的专项能力，主要用于处理科研或医学影像，并可支持医学与临床研究分析。 |
| [`$qiime2-amplicon`](#skill-qiime2-amplicon) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `qiime2-amplicon` 相关任务。 |
| [`$relion`](#skill-relion) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `relion` 相关任务。 |
| [`$relsa-severity-assessment`](#skill-relsa-severity-assessment) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `relsa-severity-assessment` 的专项能力，主要用于支持医学与临床研究分析。 |
| [`$scientific-brainstorming`](#skill-scientific-brainstorming) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `scientific-brainstorming` 的专项能力，主要用于检查问题并给出修改建议，并可支持医学与临床研究分析。 |
| [`$treatment-plans`](#skill-treatment-plans) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `treatment-plans` 的专项能力，主要用于支持医学与临床研究分析。 |

## 详细说明

<a id="skill-13c-metabolic-flux"></a>
### `$13c-metabolic-flux`

- 全局目录：`~/.codex/skills/13c-metabolic-flux/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `13c-metabolic-flux` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $13c-metabolic-flux。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Estimates intracellular metabolic fluxes from steady-state carbon-13 isotope-tracing measurements using validated atom maps, mfapy isotope simulation, constrained multistart fitting, and flux-profile diagnostics. Use for 13C-MFA, carbon tracing, mass isotopomer distributions (MDVs/MIDs), positional isotopomers, parallel tracer experiments, and determining whether labeling data constrain a pathway flux. Distinguishes measured-label inference from COBRA flux balance analysis and flags experiments requiring nonstationary MFA.

</details>

上游线索：[https://github.com/fumiomatsuda/mfapy](https://github.com/fumiomatsuda/mfapy)

<a id="skill-adaptyv"></a>
### `$adaptyv`

- 全局目录：`~/.codex/skills/adaptyv/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `adaptyv` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $adaptyv。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Uses the Adaptyv Bio Foundry API and Python SDK to design protein characterization experiments, estimate costs, submit sequences, monitor laboratory progress, and retrieve results. Applies to Adaptyv Foundry, its target catalog, binding screening and affinity assays, thermostability, expression, fluorescence, epitope binning, and enzyme activity workflows, including code using adaptyv or FoundryClient.

</details>

上游线索：[https://github.com/adaptyvbio/adaptyv-sdk.git](https://github.com/adaptyvbio/adaptyv-sdk.git)

<a id="skill-alphagenome"></a>
### `$alphagenome`

- 全局目录：`~/.codex/skills/alphagenome/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `alphagenome` 的专项能力，主要用于支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $alphagenome。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Looks up precomputed AlphaGenome Atlas effects for any GRCh38 single-nucleotide variant (AVI score with Phred and 18 SHAP feature attributions, plus raw and quantile scores for RNA-seq, DNase, ATAC, ChIP-TF, ChIP-histone, CAGE, PRO-cap, splicing, polyadenylation and contact-map tracks), scores variants or scans windows on demand with the AlphaGenome model for human and mouse (variant scoring, in silico mutagenesis, REF-versus-ALT track prediction), and builds Atlas website deep links. Use when the user mentions AlphaGenome, AlphaGenome Atlas, AVI or AlphaGenome Variant Impact, DeepMind variant effect prediction, or wants to prioritise or mechanistically interpret non-coding, regulatory, splicing, enhancer, promoter, or chromatin-accessibility effects of SNVs from a VCF, credible set, or region. Research use only; not a clinical tool.

</details>

<a id="skill-analytical-method-validation"></a>
### `$analytical-method-validation`

- 全局目录：`~/.codex/skills/analytical-method-validation/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `analytical-method-validation` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $analytical-method-validation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Plans, executes, and documents validation, verification, and transfer of analytical procedures under the governing framework - ICH Q2(R2) and Q14, USP <1220>/<1225>/<1226>, ICH M10 bioanalytical, CLSI EP, or ISO/IEC 17025. Use for HPLC, LC-MS/MS, GC, CE, ICP-MS, dissolution, qNMR, qPCR, NIR, and ligand binding or cell-based assays whenever the question is whether a procedure is fit for its intended purpose. Triggers include "method validation", "analytical method validation", "AMV", "validation protocol", "acceptance criteria", "linearity", "reportable range", "accuracy and precision", "repeatability", "intermediate precision", "recovery", "LOD", "LOQ", "detection limit", "quantitation limit", "specificity", "robustness", "method transfer", "method comparison", "Deming", "Passing-Bablok", "Bland-Altman", "equivalence testing", "OOS investigation", "ICH Q2", "Q2(R2)", "Q14", "USP 1225", "ICH M10", "incurred sample reanalysis", "ISR", "CLSI EP", and any request to show that an assay works.

</details>

<a id="skill-bids"></a>
### `$bids`

- 全局目录：`~/.codex/skills/bids/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `bids` 的专项能力，主要用于处理科研或医学影像，并可支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $bids。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Organizes, queries, validates, and converts Brain Imaging Data Structure (BIDS) datasets. Supports organizing neuroscience and biomedical data (MRI, EEG, MEG, iEEG, PET, microscopy, NIRS, motion capture, EMG, MR spectroscopy, behavioral), querying BIDS layouts, validating compliance, converting DICOM to BIDS, writing metadata sidecars, or creating BIDS derivatives.

</details>

上游线索：[https://github.com/bids-standard/bids-schema](https://github.com/bids-standard/bids-schema)

<a id="skill-cellprofiler"></a>
### `$cellprofiler`

- 全局目录：`~/.codex/skills/cellprofiler/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `cellprofiler` 的专项能力，主要用于处理科研或医学影像，并可组织可复现的科研流程。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $cellprofiler。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Runs reproducible CellProfiler microscopy pipelines for nuclear segmentation, cell counts, and per-object fluorescence measurements. Supports image/channel manifests, headless batch execution, segmentation overlays, and measurement QC for 2D fluorescence assays.

</details>

<a id="skill-cellxgene-census"></a>
### `$cellxgene-census`

- 全局目录：`~/.codex/skills/cellxgene-census/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `cellxgene-census` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $cellxgene-census。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries the CZ CELLxGENE Census programmatically for versioned public single-cell and spatial transcriptomics data. Use when you need population-scale cell metadata, gene expression slices, Census summary counts, source H5AD URIs/downloads, embeddings, spatial Census data, or reference atlas comparisons across organisms, tissues, diseases, assays, and cell types. For analyzing your own local single-cell data use scanpy, anndata, or scvi-tools.

</details>

<a id="skill-clinical-decision-support"></a>
### `$clinical-decision-support`

- 全局目录：`~/.codex/skills/clinical-decision-support/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `clinical-decision-support` 的专项能力，主要用于支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $clinical-decision-support。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Prepares and validates research-only clinical decision-support evaluation, evidence-profile, cohort, survival, biomarker/model, privacy, and governance artifacts. Supports aggregate or synthetic research documentation and traceability, excluding patient care and live clinical operation.

</details>

<a id="skill-clinical-reports"></a>
### `$clinical-reports`

- 全局目录：`~/.codex/skills/clinical-reports/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `clinical-reports` 的专项能力，主要用于检查问题并给出修改建议，并可支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $clinical-reports。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates safety-bounded draft structures and runs local deterministic checks for clinical case, diagnostic, trial, safety, and aggregate research reports. Use only with synthetic, de-identified, or aggregate inputs and verified source-fact manifests; every output requires qualified review.

</details>

<a id="skill-experimental-design"></a>
### `$experimental-design`

- 全局目录：`~/.codex/skills/experimental-design/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `experimental-design` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $experimental-design。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Designs experiments and studies BEFORE data is collected — choosing a design, randomizing, blocking, and laying out treatment combinations so results are interpretable. Use whenever someone is planning a study, asks how to assign subjects/samples to groups, mentions randomization, blocking, stratification, controls, factorial or fractional-factorial designs, design of experiments (DOE), screening many factors, response-surface optimization, crossover or repeated-measures or split-plot designs, cluster/group randomization, Latin squares, plate layouts, batch/run-order effects, replication vs. pseudoreplication, or sequential/adaptive/group-sequential designs. Trigger even for informal phrasings like "how should I set up this experiment", "how do I avoid confounding", "what's the best way to test these 6 factors", or "assign these mice to conditions". For computing the sample size or power once the design is chosen, use statistical-power; for analyzing data already collected, use statistical-analysis.

</details>

上游线索：[https://github.com/relf/pyDOE3](https://github.com/relf/pyDOE3)

<a id="skill-fluidsim"></a>
### `$fluidsim`

- 全局目录：`~/.codex/skills/fluidsim/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `fluidsim` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $fluidsim。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Plans, configures, inspects, restarts, and analyzes bounded FluidSim computational-fluid-dynamics simulations with explicit numerical-validity and HPC safety checks. Use for FluidSim solver selection, parameter review, FFT/MPI setup, output diagnostics, or restart compatibility.

</details>

上游线索：[https://github.com/fluiddyn/fluidsim](https://github.com/fluiddyn/fluidsim)

<a id="skill-genomic-coordinates"></a>
### `$genomic-coordinates`

- 全局目录：`~/.codex/skills/genomic-coordinates/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `genomic-coordinates` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $genomic-coordinates。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Converts genomic intervals between coordinate conventions, normalises and compares variant representations, and detects assembly or contig-naming mismatches before they corrupt an analysis. Used whenever coordinates cross a format, tool, or assembly boundary - converting between BED, GFF/GTF, VCF, SAM/BAM, WIG, PSL, genePred, Picard interval_list, or region strings; reconciling 0-based half-open with 1-based inclusive; left-aligning or trimming indels; checking whether two variant records describe the same change; mapping genomic to transcript, CDS, or protein positions; auditing a BED/GTF/VCF for convention violations; or diagnosing GRCh37 vs hg19 vs GRCh38 vs T2T, chr-prefix, and liftover problems. Triggers include "off by one", "0-based", "1-based", "half-open", "coordinate system", "left-align", "normalize variant", "bcftools norm", "chr prefix", "wrong genome build", "liftover", "REF mismatch", and "HGVS".

</details>

<a id="skill-ginkgo-cloud-lab"></a>
### `$ginkgo-cloud-lab`

- 全局目录：`~/.codex/skills/ginkgo-cloud-lab/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `ginkgo-cloud-lab` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $ginkgo-cloud-lab。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Guides protocol selection, input preparation, pricing checks, and browser ordering on Ginkgo Bioworks Cloud Lab (cloud.ginkgo.bio). Applies to cell-free, E. coli, and Pichia protein expression; HiBiT, A280, and LabChip readouts; IVT mRNA/circRNA synthesis; thermal shift assays; Echo-MS methods; SPR target onboarding; plate-reader assay onboarding; and fluorescent pixel art.

</details>

<a id="skill-glycoengineering"></a>
### `$glycoengineering`

- 全局目录：`~/.codex/skills/glycoengineering/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `glycoengineering` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $glycoengineering。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes and engineers protein glycosylation by scanning canonical N-glycosylation sequons, describing S/T-rich regions, checking curated glycan evidence, and preparing NetNGlyc, NetOGlyc and GlycoSHIELD workflows. Use for glycoprotein engineering, antibody Fc glycosylation, glycan shielding, and site-specific glycoproteomics interpretation.

</details>

<a id="skill-iso-standards-readiness"></a>
### `$iso-standards-readiness`

- 全局目录：`~/.codex/skills/iso-standards-readiness/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `iso-standards-readiness` 的专项能力，主要用于检查问题并给出修改建议，并可支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $iso-standards-readiness。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Prepares and structurally reviews readiness evidence for ISO management-system and laboratory-competence standards - ISO 13485 medical device QMS, ISO 14971 device risk management, ISO/IEC 17025 testing and calibration laboratories, and ISO 15189 medical laboratories. Use when organizing declared scope, controlled documents, risk-management files, scope of accreditation, traceability, CAPA, external-provider controls, or bounded local evidence manifests, and when separating ISO certification from laboratory accreditation, FDA QMSR inspection, CLIA certification, MDSAP, and EU MDR/IVDR evidence boundaries. Not for legal applicability, compliance, certification, or accreditation decisions; contains no clause text.

</details>

<a id="skill-ncats-arax"></a>
### `$ncats-arax`

- 全局目录：`~/.codex/skills/ncats-arax/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `ncats-arax` 的专项能力，主要用于支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $ncats-arax。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries the NCATS Translator ARAX production API for bounded, typed, provenance-rich one-hop and endpoint-pinned two-hop biomedical knowledge-graph relationships. Use for Biolink-constrained RTX-KG2 lookup, explicit selected-provider ARAX federation, separate entity normalization, qualifier-aware graph traversal, and inspection of TRAPI edge bindings, publications, and knowledge-source provenance. Do not use for inference, ranking, open-ended pathfinding, clinical guidance, or sensitive queries.

</details>

上游线索：[https://github.com/RTXteam/RTX](https://github.com/RTXteam/RTX)

<a id="skill-neurokit2"></a>
### `$neurokit2`

- 全局目录：`~/.codex/skills/neurokit2/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `neurokit2` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $neurokit2。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and audits reproducible NeuroKit2 research workflows for physiological time-series preprocessing, event/interval analysis, multimodal alignment, variability, and complexity. Use when code imports neurokit2 or needs its current APIs, schemas, and method-aware validation—not for diagnosis or device validation.

</details>

上游线索：[https://github.com/neuropsychology/NeuroKit](https://github.com/neuropsychology/NeuroKit)

<a id="skill-onekgpd"></a>
### `$onekgpd`

- 全局目录：`~/.codex/skills/onekgpd/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `onekgpd` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $onekgpd。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants. Use when a question is about individuals or variants in the 1000 Genomes Project cohort: which individuals carry variants matching specific criteria in a gene or region, which individuals are homozygous-reference at a position, which variants exist in the dataset or carried by specified individuals in a gene or region, the relatedness between two specified individuals. Variants are returned with 1000 Genomes allele frequencies (AF), gnomAD v4.1 exome and genome AF, AlphaMissense score, and HGVSp annotations.

</details>

<a id="skill-ontology-term-resolution"></a>
### `$ontology-term-resolution`

- 全局目录：`~/.codex/skills/ontology-term-resolution/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `ontology-term-resolution` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $ontology-term-resolution。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Resolves free-text scientific labels to ontology term IDs and validates existing CURIEs against the EBI Ontology Lookup Service (OLS4). Also looks up prefixes in Bioregistry, resolves compact identifiers via Identifiers.org, maps lab shorthand with ZOOMA, and builds Ontobee term pages. Use whenever an ontology identifier must be produced or checked - annotating tissue, cell type, disease, phenotype, assay, chemical, organism, sex, or developmental stage fields; preparing metadata for GEO, ENA, BioSamples, CELLxGENE, HCA, or ISA-Tab submission; auditing a metadata table of term IDs; checking whether a term is obsolete and what replaced it; or deciding HPO vs HP. Triggers include "ontology term", "ontology ID", "CURIE", "controlled vocabulary", "UBERON", "CL:", "MONDO", "HPO", "EFO", "ChEBI", "NCBITaxon", "GO term", "PATO", "Zooma", "Bioregistry", "Identifiers.org", "Ontobee", "annotate this tissue/cell type/disease", and any request to emit or verify an identifier shaped like PREFIX:0001234.

</details>

<a id="skill-pacsomatic"></a>
### `$pacsomatic`

- 全局目录：`~/.codex/skills/pacsomatic/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pacsomatic` 的专项能力，主要用于处理科研或医学影像，并可支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $pacsomatic。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Prepares and launches nf-core/pacsomatic matched tumor-normal PacBio HiFi genomics workflows from unaligned BAM inputs. Supports samplesheet generation, pinned Nextflow launch artifacts, local checks, LSF/Slurm/PBS Pro/SGE launcher submission, and startup troubleshooting. Use for pacsomatic run preparation and execution, not general short-read somatic analysis or medical imaging PACS.

</details>

上游线索：[https://github.com/nf-core/pacsomatic](https://github.com/nf-core/pacsomatic)

<a id="skill-pkpd-modeling"></a>
### `$pkpd-modeling`

- 全局目录：`~/.codex/skills/pkpd-modeling/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `pkpd-modeling` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pkpd-modeling。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Pharmacokinetic and pharmacodynamic modelling and simulation - non-compartmental analysis, compartmental and population PK, PK/PD and exposure-response, TMDD, PBPK orientation, bioequivalence, allometric scaling and first-in-human dose, drug interaction prediction, and Bayesian therapeutic drug monitoring. Use when analysing concentration-time data, deriving exposure metrics, fitting PK or PD models, or evaluating dosing regimens. Triggers include "pharmacokinetics", "pharmacodynamics", "PK/PD", "NCA", "non-compartmental", "AUC", "Cmax", "lambda z", "half-life", "clearance", "volume of distribution", "compartmental model", "population PK", "popPK", "NONMEM", "nlmixr2", "Pharmpy", "Monolix", "exposure-response", "Emax", "EC50", "indirect response", "effect compartment", "TMDD", "PBPK", "bioequivalence", "RSABE", "ABEL", "allometric scaling", "first-in-human", "MABEL", "drug-drug interaction", "DDI", "ICH M12", "concentration-QTc", "therapeutic drug monitoring", "MIPD", and "dosing regimen".

</details>

<a id="skill-primer-design"></a>
### `$primer-design`

- 全局目录：`~/.codex/skills/primer-design/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `primer-design` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $primer-design。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Designs and audits PCR and RT-qPCR primers with Primer3, explicit thermodynamic conditions, reference-based off-target amplification searches, and traceable sequence coordinates. Use for designing primer pairs, checking existing primers, exon-junction or isoform-specific assays, variant masking, cloning tails, multiplex compatibility, and interpreting Primer-BLAST results. Includes bounded local in-silico PCR and BLAST screening; distinguishes computational candidates from experimentally validated assays.

</details>

<a id="skill-pyhealth"></a>
### `$pyhealth`

- 全局目录：`~/.codex/skills/pyhealth/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pyhealth` 的专项能力，主要用于处理科研或医学影像，并可支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $pyhealth。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and validates PyHealth clinical machine-learning pipelines for EHR, signals, imaging, and medical codes. Use for PyHealth dataset loading, MIMIC-III/IV, eICU or OMOP prediction tasks, patient-level evaluation, mortality/readmission/length-of-stay modeling, medication recommendation, sleep staging, Trainer checkpoints, and ICD/ATC/NDC/RxNorm mapping.

</details>

<a id="skill-qiime2-amplicon"></a>
### `$qiime2-amplicon`

- 全局目录：`~/.codex/skills/qiime2-amplicon/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `qiime2-amplicon` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $qiime2-amplicon。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Processes paired-end 16S amplicon reads into QIIME 2 ASVs and taxonomy with retained artifact provenance. Checks paired FASTQ manifests, primer orientation diagnostics, predicted post-trimming overlap, sample IDs, runtime versions and read retention, and guides selection of compatible taxonomic classifiers.

</details>

<a id="skill-relion"></a>
### `$relion`

- 全局目录：`~/.codex/skills/relion/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“医学、临床与实验室规范”的专项技能，用于处理 `relion` 相关任务。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $relion。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Validates and executes RELION single-particle cryo-EM refinement and half-map postprocessing. Supports STAR optics/acquisition checks, particle-stack consistency, gold-standard half sets, soft-mask validation, diagnostic Fourier shell correlation, and restart guidance.

</details>

<a id="skill-relsa-severity-assessment"></a>
### `$relsa-severity-assessment`

- 全局目录：`~/.codex/skills/relsa-severity-assessment/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `relsa-severity-assessment` 的专项能力，主要用于支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $relsa-severity-assessment。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports multivariate severity assessment and exploratory endpoint-time score forecasting for laboratory animal studies using the RELSA (RELative Severity Assessment) score and ARIMA-based foRcast forecasting. Use when combining welfare readouts — body weight or weight loss, body temperature, clinical or nesting scores, biomarkers, activity, heart rate, burrowing, wheel running — into one severity score per animal per day, when asking which animals are at risk of reaching a humane endpoint at a specified future observation time, when defining attention/danger zones or thresholds on a severity scale by kernel density estimation, or when reporting severity for a 3Rs, refinement, animal-welfare, or EU Directive 2010/63/EU severity-assessment context. Covers directionality ("turned" variables), baseline normalization, reference sets, RELSA weights, ARIMA prediction intervals, and RMSE/PICP/MPIW evaluation.

</details>

上游线索：[https://github.com/mytalbot/RELSA](https://github.com/mytalbot/RELSA)

<a id="skill-scientific-brainstorming"></a>
### `$scientific-brainstorming`

- 全局目录：`~/.codex/skills/scientific-brainstorming/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `scientific-brainstorming` 的专项能力，主要用于检查问题并给出修改建议，并可支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $scientific-brainstorming。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit assumptions, transparent evaluation, adversarial review, and decision logs. Use for early-stage research brainstorming or prioritizing candidate directions; hand off empirical validation, study design, ethics or regulatory review, and clinical questions to appropriate experts or skills.

</details>

<a id="skill-treatment-plans"></a>
### `$treatment-plans`

- 全局目录：`~/.codex/skills/treatment-plans/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `treatment-plans` 的专项能力，主要用于支持医学与临床研究分析。
- 适合何时使用：支持临床研究、实验室方法验证、标准体系和医学数据工作流。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $treatment-plans。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Formats and structurally validates local treatment-plan documentation after clinical decisions have already been supplied and verified by authorized licensed professionals. Use for source traceability, clinician-authored intervention records, goals and checkpoints, shared-decision records, reconciliation handoffs, and release gates—not for clinical decision-making.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
