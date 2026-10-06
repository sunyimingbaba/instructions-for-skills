# 数学建模竞赛

覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。

本页收录 **40** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$1start-mathmodel`](#skill-1start-mathmodel) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 数学建模竞赛工作流入口。用于启动完整建模流程：询问用户偏好，生成 plan.md 和 todo.md，并按阶段调用赛题分析、建模、代码与图表、流程图、论文撰写、验证验收等 skills。 |
| [`$2analysis-modeling`](#skill-2analysis-modeling) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 数学建模赛题分析与建模设计合并阶段。用于读取题面和附件，完成子问题拆解、数据理解、假设预检、变量定义、模型公式、目标函数、约束条件、求解策略和可交给代码实现的建模报告。 |
| [`$3coding-visual`](#skill-3coding-visual) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 数学建模编程实现与数据图表生成阶段。根据 ANALYSIS_MODELING_REPORT.md 编写可复现代码、运行求解、验证约束、输出 RESULTS_REPORT.md 并生成论文可用的数据驱动图表 PDF。 |
| [`$4drawio`](#skill-4drawio) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 数学建模非数据型图示绘制阶段。根据 ANALYSIS_MODELING_REPORT.md、RESULTS_REPORT.md 和已有 figures/ 生成技术路线图、子问题求解流程图、模型结构图、数据处理流程图等 DrawIO 图，并导出论文可引用 PDF。 |
| [`$5writing`](#skill-5writing) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 数学建模竞赛论文撰写阶段，支持 Typst 和 LaTeX 双引擎。根据 ANALYSIS_MODELING_REPORT.md、RESULTS_REPORT.md 和 figures/*.pdf 选择比赛模板、排版引擎、组织章节，并在论文正文中按章节直接插入图表。 |
| [`$6verity`](#skill-6verity) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 数学建模竞赛最终验证和验收阶段，支持 Typst 和 LaTeX 双引擎。用于论文写完后检查章节数量、标题顺序、图表引用、数值一致性、占位符、内部文件泄露、参考文献、代码可复现性、编译和提交就绪状态。 |
| [`$_references`](#skill-_references) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 共享规范知识库。包含数学建模竞赛的写作规范、题型防错速查、图表规范等参考内容。其他 skills 在执行过程中按需读取，无需单独触发。 |
| [`$bzd-abstract-checker`](#skill-bzd-abstract-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-abstract-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-ai-usage-disclosure`](#skill-bzd-ai-usage-disclosure) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-ai-usage-disclosure` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-cumcm-school-awards`](#skill-bzd-cumcm-school-awards) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `bzd-cumcm-school-awards` 相关任务。 |
| [`$bzd-model-assumption-checker`](#skill-bzd-model-assumption-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-model-assumption-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-model-dictionary`](#skill-bzd-model-dictionary) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-model-dictionary` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-model-solution-checker`](#skill-bzd-model-solution-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-model-solution-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-modeling-ideas`](#skill-bzd-modeling-ideas) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `bzd-modeling-ideas` 相关任务。 |
| [`$bzd-modeling-workflow`](#skill-bzd-modeling-workflow) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-modeling-workflow` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。 |
| [`$bzd-paper-aigc-auditor`](#skill-bzd-paper-aigc-auditor) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 对数学建模竞赛论文进行两层AI痕迹审计——第一层9维检测(语言层面60%：连接词/排比/拔高词/被动句/段落规律/文本复杂度；事实层面40%：引文验证/数值一致性/术语一致性)，第二层模型合理性深度审查。严格判分+一票否决+问题标红。输出分层HTML报告。 |
| [`$bzd-paper-format-checker`](#skill-bzd-paper-format-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-paper-format-checker` 的专项能力，主要用于检查问题并给出修改建议，并可生成或检查科研图表。 |
| [`$bzd-problem-analysis-checker`](#skill-bzd-problem-analysis-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-problem-analysis-checker` 的专项能力，主要用于检查问题并给出修改建议，并可完成机器学习建模与评估。 |
| [`$bzd-problem-restatement`](#skill-bzd-problem-restatement) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-problem-restatement` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-problem-translator`](#skill-bzd-problem-translator) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-problem-translator` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-reference-appendix-checker`](#skill-bzd-reference-appendix-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-reference-appendix-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-review-paper`](#skill-bzd-review-paper) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-review-paper` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$bzd-symbol-notation-checker`](#skill-bzd-symbol-notation-checker) | [BZD 数学建模 Skills](../技能套件导航.md#suite-bzd) | 围绕 `bzd-symbol-notation-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-abstract-checker`](#skill-hwb-abstract-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-abstract-checker` 相关任务。 |
| [`$hwb-ai-usage-disclosure`](#skill-hwb-ai-usage-disclosure) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-ai-usage-disclosure` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-cpgmcm-award-standing`](#skill-hwb-cpgmcm-award-standing) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-cpgmcm-award-standing` 相关任务。 |
| [`$hwb-model-assumption-checker`](#skill-hwb-model-assumption-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-model-assumption-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-model-dictionary`](#skill-hwb-model-dictionary) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-model-dictionary` 相关任务。 |
| [`$hwb-model-solution-checker`](#skill-hwb-model-solution-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-model-solution-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-modeling-ideas`](#skill-hwb-modeling-ideas) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-modeling-ideas` 相关任务。 |
| [`$hwb-modeling-workflow`](#skill-hwb-modeling-workflow) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-modeling-workflow` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。 |
| [`$hwb-paper-aigc-auditor`](#skill-hwb-paper-aigc-auditor) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-paper-aigc-auditor` 的专项能力，主要用于检查问题并给出修改建议，并可完成机器学习建模与评估。 |
| [`$hwb-paper-format-checker`](#skill-hwb-paper-format-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-paper-format-checker` 的专项能力，主要用于检查问题并给出修改建议，并可生成或检查科研图表。 |
| [`$hwb-problem-analysis-checker`](#skill-hwb-problem-analysis-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-problem-analysis-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-problem-restatement`](#skill-hwb-problem-restatement) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-problem-restatement` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-problem-translator`](#skill-hwb-problem-translator) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-problem-translator` 相关任务。 |
| [`$hwb-reference-appendix-checker`](#skill-hwb-reference-appendix-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-reference-appendix-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-review-paper`](#skill-hwb-review-paper) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-review-paper` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$hwb-symbol-notation-checker`](#skill-hwb-symbol-notation-checker) | [HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb) | 围绕 `hwb-symbol-notation-checker` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$mathmodel-figure-templates`](#skill-mathmodel-figure-templates) | [MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel) | 围绕 `mathmodel-figure-templates` 的专项能力，主要用于生成或检查科研图表。 |

## 详细说明

<a id="skill-1start-mathmodel"></a>
### `$1start-mathmodel`

- 全局目录：`~/.codex/skills/1start-mathmodel/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：数学建模竞赛工作流入口。用于启动完整建模流程：询问用户偏好，生成 plan.md 和 todo.md，并按阶段调用赛题分析、建模、代码与图表、流程图、论文撰写、验证验收等 skills。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $1start-mathmodel。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

数学建模竞赛工作流入口。用于启动完整建模流程：询问用户偏好，生成 plan.md 和 todo.md，并按阶段调用赛题分析、建模、代码与图表、流程图、论文撰写、验证验收等 skills。

</details>

<a id="skill-2analysis-modeling"></a>
### `$2analysis-modeling`

- 全局目录：`~/.codex/skills/2analysis-modeling/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：数学建模赛题分析与建模设计合并阶段。用于读取题面和附件，完成子问题拆解、数据理解、假设预检、变量定义、模型公式、目标函数、约束条件、求解策略和可交给代码实现的建模报告。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $2analysis-modeling。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

数学建模赛题分析与建模设计合并阶段。用于读取题面和附件，完成子问题拆解、数据理解、假设预检、变量定义、模型公式、目标函数、约束条件、求解策略和可交给代码实现的建模报告。

</details>

<a id="skill-3coding-visual"></a>
### `$3coding-visual`

- 全局目录：`~/.codex/skills/3coding-visual/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：数学建模编程实现与数据图表生成阶段。根据 ANALYSIS_MODELING_REPORT.md 编写可复现代码、运行求解、验证约束、输出 RESULTS_REPORT.md 并生成论文可用的数据驱动图表 PDF。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $3coding-visual。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

数学建模编程实现与数据图表生成阶段。根据 ANALYSIS_MODELING_REPORT.md 编写可复现代码、运行求解、验证约束、输出 RESULTS_REPORT.md 并生成论文可用的数据驱动图表 PDF。

</details>

<a id="skill-4drawio"></a>
### `$4drawio`

- 全局目录：`~/.codex/skills/4drawio/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：数学建模非数据型图示绘制阶段。根据 ANALYSIS_MODELING_REPORT.md、RESULTS_REPORT.md 和已有 figures/ 生成技术路线图、子问题求解流程图、模型结构图、数据处理流程图等 DrawIO 图，并导出论文可引用 PDF。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $4drawio。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

数学建模非数据型图示绘制阶段。根据 ANALYSIS_MODELING_REPORT.md、RESULTS_REPORT.md 和已有 figures/ 生成技术路线图、子问题求解流程图、模型结构图、数据处理流程图等 DrawIO 图，并导出论文可引用 PDF。

</details>

<a id="skill-5writing"></a>
### `$5writing`

- 全局目录：`~/.codex/skills/5writing/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：数学建模竞赛论文撰写阶段，支持 Typst 和 LaTeX 双引擎。根据 ANALYSIS_MODELING_REPORT.md、RESULTS_REPORT.md 和 figures/*.pdf 选择比赛模板、排版引擎、组织章节，并在论文正文中按章节直接插入图表。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $5writing。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

数学建模竞赛论文撰写阶段，支持 Typst 和 LaTeX 双引擎。根据 ANALYSIS_MODELING_REPORT.md、RESULTS_REPORT.md 和 figures/*.pdf 选择比赛模板、排版引擎、组织章节，并在论文正文中按章节直接插入图表。

</details>

<a id="skill-6verity"></a>
### `$6verity`

- 全局目录：`~/.codex/skills/6verity/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：数学建模竞赛最终验证和验收阶段，支持 Typst 和 LaTeX 双引擎。用于论文写完后检查章节数量、标题顺序、图表引用、数值一致性、占位符、内部文件泄露、参考文献、代码可复现性、编译和提交就绪状态。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $6verity。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

数学建模竞赛最终验证和验收阶段，支持 Typst 和 LaTeX 双引擎。用于论文写完后检查章节数量、标题顺序、图表引用、数值一致性、占位符、内部文件泄露、参考文献、代码可复现性、编译和提交就绪状态。

</details>

<a id="skill-_references"></a>
### `$_references`

- 全局目录：`~/.codex/skills/_references/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：共享规范知识库。包含数学建模竞赛的写作规范、题型防错速查、图表规范等参考内容。其他 skills 在执行过程中按需读取，无需单独触发。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
这个目录是其他数学建模 skills 使用的共享知识库，通常无需单独调用。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

共享规范知识库。包含数学建模竞赛的写作规范、题型防错速查、图表规范等参考内容。其他 skills 在执行过程中按需读取，无需单独触发。

</details>

<a id="skill-bzd-abstract-checker"></a>
### `$bzd-abstract-checker`

- 全局目录：`~/.codex/skills/bzd-abstract-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-abstract-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-abstract-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review a user-provided Chinese mathematical-modeling abstract without requiring the problem statement or full paper, identify concrete writing defects, and prioritize revisions. Use when the user asks to check, diagnose, or improve a modeling-paper abstract; do not claim coverage or factual consistency that cannot be verified without the problem or paper.

</details>

<a id="skill-bzd-ai-usage-disclosure"></a>
### `$bzd-ai-usage-disclosure`

- 全局目录：`~/.codex/skills/bzd-ai-usage-disclosure/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-ai-usage-disclosure` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-ai-usage-disclosure。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate or review mathematical-modeling competition AI tool usage statements and the anonymous AI工具使用详情.pdf. Use when users provide real AI usage records, or when checking a paper, statement, details PDF, code, and AI records for completeness, anonymity, and consistency.

</details>

<a id="skill-bzd-cumcm-school-awards"></a>
### `$bzd-cumcm-school-awards`

- 全局目录：`~/.codex/skills/bzd-cumcm-school-awards/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `bzd-cumcm-school-awards` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bzd-cumcm-school-awards。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Query 2021-2025 CUMCM school awards and 2026 forecasts, or assess a student's preparation distance from provincial and national awards using school history and prior modeling experience.

</details>

<a id="skill-bzd-model-assumption-checker"></a>
### `$bzd-model-assumption-checker`

- 全局目录：`~/.codex/skills/bzd-model-assumption-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-model-assumption-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-model-assumption-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review a mathematical-modeling paper's model-assumption section against the complete problem statement. Diagnose whether each assumption is necessary, evidence-based, compatible with the task, appropriately simplified, and usable by the later model. Use for assumption review, not automatic full-paper review or unsupported assumption generation.

</details>

<a id="skill-bzd-model-dictionary"></a>
### `$bzd-model-dictionary`

- 全局目录：`~/.codex/skills/bzd-model-dictionary/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-model-dictionary` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bzd-model-dictionary。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Query the bundled BZD mathematical-modeling dictionary for a user-selected model, explain its assumptions, inputs, outputs, limitations and validation, then judge whether it fits the current competition problem and data. Use when a user asks whether a proposed model is appropriate, requests model feasibility review, or wants dictionary-based alternatives for a modeling task.

</details>

<a id="skill-bzd-model-solution-checker"></a>
### `$bzd-model-solution-checker`

- 全局目录：`~/.codex/skills/bzd-model-solution-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-model-solution-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-model-solution-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review the model establishment, numerical solution, result analysis, model validation, and sensitivity or robustness sections of a mathematical-modeling paper against the complete problem. Use for core-model-section diagnosis, not automatic full-paper scoring or unsupported recomputation.

</details>

<a id="skill-bzd-modeling-ideas"></a>
### `$bzd-modeling-ideas`

- 全局目录：`~/.codex/skills/bzd-modeling-ideas/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `bzd-modeling-ideas` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-modeling-ideas。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate a coherent, whole-paper mathematical modeling solution framework from a complete contest problem. Use after the user supplies a CUMCM or other modeling problem and asks for modeling ideas, an overall solution plan, question-by-question analysis, candidate-model comparison, model-selection reasons, innovations, validation, or cross-question linkage. For every question, explain the task and mathematical essence, compare multiple feasible models in tables, recommend a route with explicit reasons, and keep all questions connected through shared data, variables, parameters, constraints, and validation.

</details>

<a id="skill-bzd-modeling-workflow"></a>
### `$bzd-modeling-workflow`

- 全局目录：`~/.codex/skills/bzd-modeling-workflow/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-modeling-workflow` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-modeling-workflow。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Orchestrate the BZD mathematical-modeling Skills across problem reading, idea generation, model selection, paper drafting, section checks, final format/AIGC audits and judge-style scoring. Use when a user wants one entry point, an end-to-end competition workflow, the next appropriate Skill, or coordinated processing of a problem and paper.

</details>

<a id="skill-bzd-paper-aigc-auditor"></a>
### `$bzd-paper-aigc-auditor`

- 全局目录：`~/.codex/skills/bzd-paper-aigc-auditor/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：对数学建模竞赛论文进行两层AI痕迹审计——第一层9维检测(语言层面60%：连接词/排比/拔高词/被动句/段落规律/文本复杂度；事实层面40%：引文验证/数值一致性/术语一致性)，第二层模型合理性深度审查。严格判分+一票否决+问题标红。输出分层HTML报告。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bzd-paper-aigc-auditor。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

对数学建模竞赛论文进行两层AI痕迹审计——第一层9维检测(语言层面60%：连接词/排比/拔高词/被动句/段落规律/文本复杂度；事实层面40%：引文验证/数值一致性/术语一致性)，第二层模型合理性深度审查。严格判分+一票否决+问题标红。输出分层HTML报告。

</details>

<a id="skill-bzd-paper-format-checker"></a>
### `$bzd-paper-format-checker`

- 全局目录：`~/.codex/skills/bzd-paper-format-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-paper-format-checker` 的专项能力，主要用于检查问题并给出修改建议，并可生成或检查科研图表。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-paper-format-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review a complete mathematical-modeling competition paper with an atomic checklist covering abstract readability, page structure, typography, headings, pagination, figures, tables, equations, anonymity, metadata, visual balance, and page allocation. Return the review in chat or Markdown by default, and provide the bundled single-sheet checklist when the user requests a reusable form. Use when the user provides a PDF or Word paper and asks for a full-paper format and writing-compliance audit; do not replace technical model correctness review.

</details>

<a id="skill-bzd-problem-analysis-checker"></a>
### `$bzd-problem-analysis-checker`

- 全局目录：`~/.codex/skills/bzd-problem-analysis-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-problem-analysis-checker` 的专项能力，主要用于检查问题并给出修改建议，并可完成机器学习建模与评估。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $bzd-problem-analysis-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review a Chinese mathematical-modeling problem-analysis section against the original problem, checking task classification, data reasoning, cross-problem linkage, model-choice rationale, validation planning, chapter boundaries, and the overall solution framework. Use for diagnosis, not automatic full rewriting.

</details>

<a id="skill-bzd-problem-restatement"></a>
### `$bzd-problem-restatement`

- 全局目录：`~/.codex/skills/bzd-problem-restatement/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-problem-restatement` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bzd-problem-restatement。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate a compliant Chinese mathematical-modeling problem-restatement chapter from a complete problem statement, or review a user's restatement against the original problem. Covers research background, problem review, and research overview; does not perform the separate problem-analysis chapter.

</details>

<a id="skill-bzd-problem-translator"></a>
### `$bzd-problem-translator`

- 全局目录：`~/.codex/skills/bzd-problem-translator/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-problem-translator` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bzd-problem-translator。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Translate a complete mathematical modeling contest problem sentence by sentence into precise modeling language, preserve every substantive condition and definition, expose hidden constraints, draw a mandatory Mermaid cross-question flowchart, audit omissions, and deliver one easy-to-open Markdown report. For Huawei Cup (CPGMCM) graduate-contest problems, additionally prepend a plain-language layer that rewrites the background and questions as a primary-school word problem with a mandatory term-mapping table. Optionally render the finished report as one standalone HTML page on request. Use whenever a user supplies a CUMCM, CPGMCM, or other modeling problem and asks to interpret, translate, unpack, read closely, identify requirements, or avoid missing details before modeling.

</details>

<a id="skill-bzd-reference-appendix-checker"></a>
### `$bzd-reference-appendix-checker`

- 全局目录：`~/.codex/skills/bzd-reference-appendix-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-reference-appendix-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-reference-appendix-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Check a mathematical-modeling paper's in-text citations, bibliography, appendix length and content, code, supporting files, reproducibility, consistency, and anonymity. Use when the user provides a paper or related materials and wants one consolidated P0-P3 audit; do not generate or invent missing sources or programs.

</details>

<a id="skill-bzd-review-paper"></a>
### `$bzd-review-paper`

- 全局目录：`~/.codex/skills/bzd-review-paper/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-review-paper` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-review-paper。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review mathematical modeling competition papers from a complete problem and paper, with an optional strict bzd-paper-format-checker audit, itemized problem-specific scoring, a bottom-up low-score safeguard, and CUMCM award calibration by problem type, division, region, school and advisor. Generate a Chinese HTML judge report.

</details>

<a id="skill-bzd-symbol-notation-checker"></a>
### `$bzd-symbol-notation-checker`

- 全局目录：`~/.codex/skills/bzd-symbol-notation-checker/`
- 所属技能套件：[BZD 数学建模 Skills](../技能套件导航.md#suite-bzd)
- 推荐总入口：`$bzd-modeling-workflow`
- 中文理解：围绕 `bzd-symbol-notation-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bzd-symbol-notation-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review the symbol-notation section of a mathematical-modeling paper against the full paper. Check table coverage, symbol meanings, units, overloading, case and subscript consistency, first-use definitions, formula usage, and visible table formatting. Use for symbol-table diagnosis, not general paper review.

</details>

<a id="skill-hwb-abstract-checker"></a>
### `$hwb-abstract-checker`

- 全局目录：`~/.codex/skills/hwb-abstract-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-abstract-checker` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-abstract-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Check the title, abstract and keywords of a HUAWEI Cup paper for independence, information density, the five required abstract elements and two-page limit compliance. Use when a graduate team has drafted the abstract page and needs a strict, contest-specific diagnosis before submission.

</details>

<a id="skill-hwb-ai-usage-disclosure"></a>
### `$hwb-ai-usage-disclosure`

- 全局目录：`~/.codex/skills/hwb-ai-usage-disclosure/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-ai-usage-disclosure` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-ai-usage-disclosure。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate or review an AI-tool usage statement and detailed usage disclosure for a HUAWEI Cup paper, matching the contest's explicit policy that AI products may be used only as auxiliary tools with sources cited. Use when a team used AI assistance and must disclose it truthfully, or wants an existing disclosure checked for completeness and consistency.

</details>

<a id="skill-hwb-cpgmcm-award-standing"></a>
### `$hwb-cpgmcm-award-standing`

- 全局目录：`~/.codex/skills/hwb-cpgmcm-award-standing/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-cpgmcm-award-standing` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-cpgmcm-award-standing。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Query a graduate training unit's Huawei Cup (CPGMCM) award profile, estimate the award band from the contest's total team count and a team's rank or paper score, and assess a student's preparation distance from first/second/third prizes using the unit's self-filled history and the student's own modeling and simulation experience. Use when a user asks about a training unit's Huawei Cup record, next-year award probability, Huawei Special Award hit rate, problem selection, preparation advice, or the rank needed for a given award level.

</details>

<a id="skill-hwb-model-assumption-checker"></a>
### `$hwb-model-assumption-checker`

- 全局目录：`~/.codex/skills/hwb-model-assumption-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-model-assumption-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-model-assumption-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Diagnose whether each modeling assumption in a HUAWEI Cup paper is necessary, realistic, consistent with the data, and actually used later in the paper. Use when the model-assumption chapter is drafted and needs a strict review before it can support the model chapters.

</details>

<a id="skill-hwb-model-dictionary"></a>
### `$hwb-model-dictionary`

- 全局目录：`~/.codex/skills/hwb-model-dictionary/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-model-dictionary` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $hwb-model-dictionary。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Judge whether a candidate model actually fits a HUAWEI Cup problem, its data and its intended use, returning a model archive with requirements, assumptions, strengths, limitations, failure conditions, validation routes and alternative models. Use when a team is choosing models and needs a data-driven fit decision instead of a generic model list.

</details>

<a id="skill-hwb-model-solution-checker"></a>
### `$hwb-model-solution-checker`

- 全局目录：`~/.codex/skills/hwb-model-solution-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-model-solution-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-model-solution-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Diagnose the model-establishment, solution, results, validation and sensitivity-analysis parts of a HUAWEI Cup paper, including reproducibility and red-line risks. Use when the core chapters are drafted and need a strict review before the final submission gate.

</details>

<a id="skill-hwb-modeling-ideas"></a>
### `$hwb-modeling-ideas`

- 全局目录：`~/.codex/skills/hwb-modeling-ideas/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-modeling-ideas` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-modeling-ideas。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate a whole-paper modeling backbone for a HUAWEI Cup post-graduate contest problem, comparing candidate models per question with selection reasons, innovation points and validation routes. Use when a team has read the A~F problem and needs a coherent modeling main line instead of per-question ad-hoc models.

</details>

<a id="skill-hwb-modeling-workflow"></a>
### `$hwb-modeling-workflow`

- 全局目录：`~/.codex/skills/hwb-modeling-workflow/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-modeling-workflow` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-modeling-workflow。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Orchestrate the HWB (HUAWEI Cup China Post-Graduate Mathematical Contest in Modeling) Skills across problem reading, idea generation, model selection, paper drafting, section checks, final format/AIGC audits and judge-style scoring. Use when a graduate team wants one entry point, an end-to-end four-day contest workflow, the next appropriate Skill, or coordinated processing of a problem and paper.

</details>

<a id="skill-hwb-paper-aigc-auditor"></a>
### `$hwb-paper-aigc-auditor`

- 全局目录：`~/.codex/skills/hwb-paper-aigc-auditor/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-paper-aigc-auditor` 的专项能力，主要用于检查问题并给出修改建议，并可完成机器学习建模与评估。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-paper-aigc-auditor。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Audit a HUAWEI Cup paper for AI-generation traces, template-like modeling, model stacking and fake improvement, producing a risk band, per-section evidence, model-authenticity classification and humanisation suggestions. Use at the final stage to locate sections that read as machine-generated so the team can rewrite them in its own voice and disclose AI use truthfully.

</details>

<a id="skill-hwb-paper-format-checker"></a>
### `$hwb-paper-format-checker`

- 全局目录：`~/.codex/skills/hwb-paper-format-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-paper-format-checker` 的专项能力，主要用于检查问题并给出修改建议，并可生成或检查科研图表。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-paper-format-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Run a strict whole-paper format, structure, anonymity and file-hygiene audit for a HUAWEI Cup paper: official template compliance, cover page, abstract page limit, page allocation, headings, figures, tables, equations, anonymity of all pages except the cover, and file hygiene. Use when a near-final PDF exists and a fast, exhaustive presentation check is needed.

</details>

<a id="skill-hwb-problem-analysis-checker"></a>
### `$hwb-problem-analysis-checker`

- 全局目录：`~/.codex/skills/hwb-problem-analysis-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-problem-analysis-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-problem-analysis-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Diagnose the problem-analysis chapter of a HUAWEI Cup paper: task mapping to each question, data reasoning, justification of model choice and cross-question linkage. Use when the analysis chapter is drafted and must justify the modeling route before reviewers read the model chapters.

</details>

<a id="skill-hwb-problem-restatement"></a>
### `$hwb-problem-restatement`

- 全局目录：`~/.codex/skills/hwb-problem-restatement/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-problem-restatement` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $hwb-problem-restatement。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate a compliant Chinese problem-restatement chapter from a complete HUAWEI Cup problem statement, or review a user's restatement against the original problem. Covers research background, problem review and research overview; does not perform the separate problem-analysis chapter.

</details>

<a id="skill-hwb-problem-translator"></a>
### `$hwb-problem-translator`

- 全局目录：`~/.codex/skills/hwb-problem-translator/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：这是一个面向“数学建模竞赛”的专项技能，用于处理 `hwb-problem-translator` 相关任务。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $hwb-problem-translator。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Translate a complete HUAWEI Cup (China Post-Graduate Mathematical Contest in Modeling) problem into a sentence-level interpretation report, identifying definitions, constraints, data semantics, deliverable requirements and cross-question dependencies. Use when a graduate team has just received the A~F problem and needs an exhaustive reading before modeling.

</details>

<a id="skill-hwb-reference-appendix-checker"></a>
### `$hwb-reference-appendix-checker`

- 全局目录：`~/.codex/skills/hwb-reference-appendix-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-reference-appendix-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-reference-appendix-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Audit in-text citations, the reference list, appendices, code and supporting materials of a HUAWEI Cup paper, including reference consistency, appendix completeness, reproducibility and the 50MB attachment rule. Use before the final submission gate when references and appendices are finalised.

</details>

<a id="skill-hwb-review-paper"></a>
### `$hwb-review-paper`

- 全局目录：`~/.codex/skills/hwb-review-paper/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-review-paper` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-review-paper。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Review mathematical modeling competition papers from a complete problem and paper, with an optional strict hwb-paper-format-checker audit, itemized problem-specific scoring, a bottom-up low-score safeguard, and CPGMCM (Huawei Cup graduate contest) award calibration by problem type, participating unit and Huawei-problem choice. Generate a Chinese HTML judge report.

</details>

<a id="skill-hwb-symbol-notation-checker"></a>
### `$hwb-symbol-notation-checker`

- 全局目录：`~/.codex/skills/hwb-symbol-notation-checker/`
- 所属技能套件：[HWB 华为杯数学建模 Skills](../技能套件导航.md#suite-hwb)
- 推荐总入口：`$hwb-modeling-workflow`
- 中文理解：围绕 `hwb-symbol-notation-checker` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $hwb-symbol-notation-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Audit the symbol table of a HUAWEI Cup paper for missing definitions, conflicts, missing units, subscript/superscript consistency and first-use definitions across the whole text. Use when the symbol chapter is drafted or when reviewers flag inconsistent notation.

</details>

<a id="skill-mathmodel-figure-templates"></a>
### `$mathmodel-figure-templates`

- 全局目录：`~/.codex/skills/mathmodel-figure-templates/`
- 所属技能套件：[MathModel 数学建模工作流](../技能套件导航.md#suite-mathmodel)
- 推荐总入口：`$1start-mathmodel`
- 中文理解：围绕 `mathmodel-figure-templates` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $mathmodel-figure-templates。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Use this skill in the MathModel LaTeX sandbox when the user asks to reproduce built-in scientific visualization templates, especially prompts from the Improve tab mentioning $mathmodel-figure-templates, 科研绘图模板, SHAP蜂群柱状图, 配对云雨图, 交叉验证ROC, 泰勒图, 相关矩阵组合图, 预测真实值边缘分布图, TPE调参3D曲面, 下三角相关矩阵半边小提琴图, 分组环形热图, 城市公园降温组合图, or Nature和弦图. It provides ready-to-run Python scripts bundled inside the skill.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
