# 通用科研工具与质量保障

无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。

本页收录 **37** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$auto-review-loop-minimax`](#skill-auto-review-loop-minimax) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `auto-review-loop-minimax` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$consciousness-council`](#skill-consciousness-council) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `consciousness-council` 相关任务。 |
| [`$doctor`](#skill-doctor) | [独立或暂未归入大型套件](../技能套件导航.md#suite-standalone) | 环境检查与安装向导。检查数学建模工作流所需的全部依赖是否已安装，对缺失项提供安装命令，并在用户确认后执行安装。手动触发。 |
| [`$docx-editor-cn`](#skill-docx-editor-cn) | [独立或暂未归入大型套件](../技能套件导航.md#suite-standalone) | 围绕 `docx-editor-cn` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$exa-search`](#skill-exa-search) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `exa-search` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$feishu-notify`](#skill-feishu-notify) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `feishu-notify` 相关任务。 |
| [`$fictiv`](#skill-fictiv) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `fictiv` 相关任务。 |
| [`$find-skills`](#skill-find-skills) | [独立或暂未归入大型套件](../技能套件导航.md#suite-standalone) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `find-skills` 相关任务。 |
| [`$flowio`](#skill-flowio) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `flowio` 相关任务。 |
| [`$flowkit`](#skill-flowkit) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `flowkit` 相关任务。 |
| [`$formula-derivation`](#skill-formula-derivation) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `formula-derivation` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$get-available-resources`](#skill-get-available-resources) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `get-available-resources` 相关任务。 |
| [`$histolab`](#skill-histolab) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `histolab` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$integrity-forensics`](#skill-integrity-forensics) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `integrity-forensics` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$interview-cheatsheet`](#skill-interview-cheatsheet) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `interview-cheatsheet` 相关任务。 |
| [`$liteparse`](#skill-liteparse) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `liteparse` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$markitdown`](#skill-markitdown) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `markitdown` 的专项能力，主要用于组织可复现的科研流程，并可处理科研文档与结构化内容。 |
| [`$nature-downloader`](#skill-nature-downloader) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `nature-downloader` 相关任务。 |
| [`$nature-experiment-log`](#skill-nature-experiment-log) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 标准化实验日志记录——直接上传或读取本地图片、语音和文字，产出带 YAML frontmatter 的 Markdown；可选集成飞书 CLI 与 Obsidian。 |
| [`$neuropixels-analysis`](#skill-neuropixels-analysis) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `neuropixels-analysis` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$nwb-conversion`](#skill-nwb-conversion) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `nwb-conversion` 相关任务。 |
| [`$open-notebook`](#skill-open-notebook) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `open-notebook` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$paper-illustration-image2`](#skill-paper-illustration-image2) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `paper-illustration-image2` 相关任务。 |
| [`$paperzilla`](#skill-paperzilla) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `paperzilla` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$proof-orchestrator`](#skill-proof-orchestrator) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `proof-orchestrator` 相关任务。 |
| [`$proof-writer`](#skill-proof-writer) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `proof-writer` 相关任务。 |
| [`$pydicom`](#skill-pydicom) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pydicom` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$render-html`](#skill-render-html) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `render-html` 的专项能力，主要用于检查问题并给出修改建议，并可处理科研文档与结构化内容。 |
| [`$research-grants`](#skill-research-grants) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `research-grants` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$research-refine`](#skill-research-refine) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `research-refine` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$research-wiki`](#skill-research-wiki) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `research-wiki` 相关任务。 |
| [`$scholar-evaluation`](#skill-scholar-evaluation) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `scholar-evaluation` 的专项能力，主要用于检查问题并给出修改建议。 |
| [`$sympy`](#skill-sympy) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `sympy` 相关任务。 |
| [`$system-profile`](#skill-system-profile) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `system-profile` 相关任务。 |
| [`$training-check`](#skill-training-check) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `training-check` 相关任务。 |
| [`$typst-author`](#skill-typst-author) | [独立或暂未归入大型套件](../技能套件导航.md#suite-standalone) | 围绕 `typst-author` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$vast-gpu`](#skill-vast-gpu) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `vast-gpu` 相关任务。 |

## 详细说明

<a id="skill-auto-review-loop-minimax"></a>
### `$auto-review-loop-minimax`

- 全局目录：`~/.codex/skills/auto-review-loop-minimax/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `auto-review-loop-minimax` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $auto-review-loop-minimax。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Autonomous multi-round research review loop using MiniMax API. Use when you want to use MiniMax instead of Codex MCP for external review. Trigger with "auto review loop minimax" or "minimax review".

</details>

上游线索：[https://github.com/openai/codex](https://github.com/openai/codex)

<a id="skill-consciousness-council"></a>
### `$consciousness-council`

- 全局目录：`~/.codex/skills/consciousness-council/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `consciousness-council` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $consciousness-council。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Structures a multi-perspective council exercise for decisions, research trade-offs, and creative challenges. Simulates thinking archetypes, separates evidence from assumptions and values, and synthesizes a conditional recommendation. Use when the user requests a council, panel, devil's advocate analysis, "mind council", or deliberate comparison of perspectives on a difficult choice.

</details>

<a id="skill-doctor"></a>
### `$doctor`

- 全局目录：`~/.codex/skills/doctor/`
- 所属技能套件：[独立或暂未归入大型套件](../技能套件导航.md#suite-standalone)
- 推荐总入口：直接调用当前小 skill
- 中文理解：环境检查与安装向导。检查数学建模工作流所需的全部依赖是否已安装，对缺失项提供安装命令，并在用户确认后执行安装。手动触发。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $doctor。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

环境检查与安装向导。检查数学建模工作流所需的全部依赖是否已安装，对缺失项提供安装命令，并在用户确认后执行安装。手动触发。

</details>

上游线索：[https://github.com/jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)

<a id="skill-docx-editor-cn"></a>
### `$docx-editor-cn`

- 全局目录：`~/.codex/skills/docx-editor-cn/`
- 所属技能套件：[独立或暂未归入大型套件](../技能套件导航.md#suite-standalone)
- 推荐总入口：直接调用当前小 skill
- 中文理解：围绕 `docx-editor-cn` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $docx-editor-cn。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of "Word doc", "word document", ".docx", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a "report", "memo", "letter", "template", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

</details>

<a id="skill-exa-search"></a>
### `$exa-search`

- 全局目录：`~/.codex/skills/exa-search/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `exa-search` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $exa-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Searches scientific and technical web content with Exa and extracts page or PDF text from URLs in batches. Supports scholarly discovery with the publication category and academic domain filters. Applies to requests to search the web, look up current research, fetch a page, or extract an article using Exa.

</details>

上游线索：[https://github.com/exa-labs/exa-py](https://github.com/exa-labs/exa-py)

<a id="skill-feishu-notify"></a>
### `$feishu-notify`

- 全局目录：`~/.codex/skills/feishu-notify/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `feishu-notify` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $feishu-notify。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Send notifications to Feishu/Lark. Internal utility used by other skills, or manually via /feishu-notify. Use when user says "发飞书", "notify feishu", or other skills need to send status updates.

</details>

上游线索：[https://github.com/joewongjc/feishu-claude-code](https://github.com/joewongjc/feishu-claude-code)

<a id="skill-fictiv"></a>
### `$fictiv`

- 全局目录：`~/.codex/skills/fictiv/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `fictiv` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $fictiv。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Operates Fictiv (app.fictiv.com), the on-demand manufacturing platform, end to end in the user's browser. Covers uploading CAD parts, configuring process, material, finish, threads, tolerances and inspections, getting instant or manual quotes, reading and fixing DFM feedback, choosing lead time and region, checking out and paying (card or PO), tracking orders, reordering, and troubleshooting. Applies when the user mentions Fictiv, wants a part CNC machined, 3D printed, sheet-metal fabricated, urethane cast, injection or compression molded, or die cast through an online service, asks to "get a quote" or "order parts" for a STEP/SLDPRT/STL file, wants to check a Fictiv quote or order status, or has a problem with a Fictiv upload, DFM warning, price or checkout. Also applies when the user wants custom parts manufactured and has a Fictiv account, even if Fictiv is not named.

</details>

<a id="skill-find-skills"></a>
### `$find-skills`

- 全局目录：`~/.codex/skills/find-skills/`
- 所属技能套件：[独立或暂未归入大型套件](../技能套件导航.md#suite-standalone)
- 推荐总入口：直接调用当前小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `find-skills` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $find-skills。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.

</details>

<a id="skill-flowio"></a>
### `$flowio`

- 全局目录：`~/.codex/skills/flowio/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `flowio` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $flowio。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reads, inspects, and writes Flow Cytometry Standard (FCS) 2.0, 3.0, and 3.1 files with FlowIO. Use for low-level FCS metadata and channel inspection, NumPy event extraction, multi-dataset files, table export, and FCS 3.1 creation; use FlowKit for compensation, cytometry transforms, gating, or FlowJo workspaces.

</details>

<a id="skill-flowkit"></a>
### `$flowkit`

- 全局目录：`~/.codex/skills/flowkit/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `flowkit` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $flowkit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes flow cytometry data with FlowKit, including spillover compensation, logicle and biexponential transforms, hierarchical gating, GatingML strategies, and supported FlowJo 10 workspaces. Use for reproducible gate counts, population percentages, gated fluorescence summaries, or reproducing a FlowJo analysis in Python. For FCS metadata inspection or file-format repair alone, use FlowIO.

</details>

上游线索：[https://github.com/whitews/FlowKit](https://github.com/whitews/FlowKit)

<a id="skill-formula-derivation"></a>
### `$formula-derivation`

- 全局目录：`~/.codex/skills/formula-derivation/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `formula-derivation` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $formula-derivation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Structures and derives research formulas when the user wants to 推导公式, build a theory line, organize assumptions, turn scattered equations into a coherent derivation, or rewrite theory notes into a paper-ready formula document. Use when the derivation target is not yet fully fixed, the main object still needs to be chosen, or the user needs a coherent derivation package rather than a finished theorem proof.

</details>

<a id="skill-get-available-resources"></a>
### `$get-available-resources`

- 全局目录：`~/.codex/skills/get-available-resources/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `get-available-resources` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $get-available-resources。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Detects host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before a clearly resource-sensitive local workload. Produces a redacted JSON snapshot and conservative planning helpers without stress tests or assuming visible host hardware is usable.

</details>

<a id="skill-histolab"></a>
### `$histolab`

- 全局目录：`~/.codex/skills/histolab/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `histolab` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $histolab。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Extracts and preprocesses whole-slide histology image tiles with Histolab. Use for WSI inspection, tissue masks, random/grid/score-based tile extraction, H&E stain normalization, and tile dataset preparation. For multiplexed imaging or deep learning inference pipelines, use pathml.

</details>

上游线索：[https://github.com/histolab/histolab](https://github.com/histolab/histolab)

<a id="skill-integrity-forensics"></a>
### `$integrity-forensics`

- 全局目录：`~/.codex/skills/integrity-forensics/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `integrity-forensics` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $integrity-forensics。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Run the Anti-Autoresearch integrity-forensics DETERMINISTIC slice (numeric core + rules-only reporter) against a paper via a SHA-pinned thin launcher, then convert the verdict into a typed policy gate (BLOCK/WARN/NO_NEW_BLOCKER) and an append-only obligations ledger. Codex-native limitation: upstream ships no Codex-native auditor pack, so the full nine-dimension semantic sweep requires a Claude Code session — this pack runs the honestly-scoped deterministic-only mode (it can flag, it can never say CLEAN). Use when user says "integrity forensics", "forensic audit this paper", "投稿前自查诚信".

</details>

上游线索：[https://github.com/wanshuiyin/Anti-Autoresearch.git](https://github.com/wanshuiyin/Anti-Autoresearch.git)

<a id="skill-interview-cheatsheet"></a>
### `$interview-cheatsheet`

- 全局目录：`~/.codex/skills/interview-cheatsheet/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `interview-cheatsheet` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $interview-cheatsheet。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate a long-form Chinese interview-prep cheat sheet on a specific ML/LLM topic — formulas with derivations, from-scratch PyTorch code, comparison tables, and 25 高频面试题 (L1 必会 / L2 进阶 / L3 顶级 lab). Use when the user says '写面试 cheat sheet', '写一份 X 教程', '帮我准备 Y 面试题', '出一份 X 速查', or wants a 600-1000 line Chinese tutorial on a specific ML topic.

</details>

<a id="skill-liteparse"></a>
### `$liteparse`

- 全局目录：`~/.codex/skills/liteparse/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `liteparse` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $liteparse。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Local document and PDF parsing that returns spatial text with bounding boxes. Use for extracting text from PDFs, DOCX, Office files, and images; running OCR on scans; producing layout-preserved JSON for RAG; batch-ingesting folders of papers; or rendering pages to PNG for multimodal agents. Distinguishing capabilities are spatial text boxes, Markdown, page raster output, and local parsing with optional custom HTTP OCR.

</details>

上游线索：[https://github.com/run-llama/liteparse](https://github.com/run-llama/liteparse)

<a id="skill-markitdown"></a>
### `$markitdown`

- 全局目录：`~/.codex/skills/markitdown/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `markitdown` 的专项能力，主要用于组织可复现的科研流程，并可处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $markitdown。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Converts heterogeneous documents and selected URIs to Markdown with Microsoft MarkItDown for text analysis, search, and LLM/RAG ingestion. Covers safe local conversion, streams, Office/PDF/data formats, batch workflows, plugins, vision OCR, Azure extraction, and the official MCP server.

</details>

上游线索：[https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)

<a id="skill-nature-downloader"></a>
### `$nature-downloader`

- 全局目录：`~/.codex/skills/nature-downloader/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `nature-downloader` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $nature-downloader。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Use when a user needs lawful academic full text, CNKI institutional access, English OA retrieval, publisher API access, institutional browser fallback, or supporting information downloads.

</details>

<a id="skill-nature-experiment-log"></a>
### `$nature-experiment-log`

- 全局目录：`~/.codex/skills/nature-experiment-log/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：标准化实验日志记录——直接上传或读取本地图片、语音和文字，产出带 YAML frontmatter 的 Markdown；可选集成飞书 CLI 与 Obsidian。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $nature-experiment-log。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

标准化实验日志记录——直接上传或读取本地图片、语音和文字，产出带 YAML frontmatter 的 Markdown；可选集成飞书 CLI 与 Obsidian。

</details>

上游线索：[https://github.com/blacksmithgu/obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview)

<a id="skill-neuropixels-analysis"></a>
### `$neuropixels-analysis`

- 全局目录：`~/.codex/skills/neuropixels-analysis/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `neuropixels-analysis` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $neuropixels-analysis。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes Neuropixels extracellular recordings end-to-end with SpikeInterface. Covers loading SpikeGLX/Open Ephys/NWB data, preprocessing, drift/motion correction, Kilosort4 (and CPU) spike sorting, quality metrics, and unit curation (threshold-based, model-based UnitRefine, and AI-assisted visual review). Use when working with Neuropixels 1.0/2.0 recordings, spike sorting, or extracellular electrophysiology analysis.

</details>

上游线索：[https://github.com/MouseLand/Kilosort](https://github.com/MouseLand/Kilosort)

<a id="skill-nwb-conversion"></a>
### `$nwb-conversion`

- 全局目录：`~/.codex/skills/nwb-conversion/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `nwb-conversion` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $nwb-conversion。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Converts neuroscience acquisition data to Neurodata Without Borders files with NeuroConv and PyNWB, preserves metadata and timebases, checks evidence-based clock alignment, and produces schema validation, NWB Inspector findings and round-trip checks. Use for NWB conversion and synchronization of planar single-channel two-photon TIFF imaging plus timestamped behavioral position CSV; this skill does not perform spike sorting or claim tested support for arbitrary acquisition formats.

</details>

上游线索：[https://github.com/NeurodataWithoutBorders/pynwb](https://github.com/NeurodataWithoutBorders/pynwb)

<a id="skill-open-notebook"></a>
### `$open-notebook`

- 全局目录：`~/.codex/skills/open-notebook/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `open-notebook` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $open-notebook。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Organizes research with the self-hosted Open Notebook alternative to NotebookLM. Supports source ingestion (PDFs, web pages, audio, video, and Office documents), cited document chat, text and vector search, notes, custom transformations, and multi-speaker podcasts. Use when automating Open Notebook through its REST API or configuring its local or cloud AI providers, including OpenAI, Anthropic, Google, Ollama, Groq, and Mistral.

</details>

上游线索：[https://github.com/lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)

<a id="skill-paper-illustration-image2"></a>
### `$paper-illustration-image2`

- 全局目录：`~/.codex/skills/paper-illustration-image2/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `paper-illustration-image2` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-illustration-image2。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate publication-quality academic illustrations through a local Codex app-server bridge that uses Codex native image generation. This is a separate experimental alternative to `paper-illustration`, intended for Claude Code users who want a GPT-image-style renderer without modifying the original skill.

</details>

<a id="skill-paperzilla"></a>
### `$paperzilla`

- 全局目录：`~/.codex/skills/paperzilla/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `paperzilla` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paperzilla。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reads projects, searches project feeds, and retrieves recommendations and canonical papers in Paperzilla through the pz CLI. Supports recent recommendations, paper details, markdown-based summaries, recommendation feedback, JSON export, and Atom feed URLs.

</details>

上游线索：[https://github.com/paperzilla-ai/scoop-bucket](https://github.com/paperzilla-ai/scoop-bucket)

<a id="skill-proof-orchestrator"></a>
### `$proof-orchestrator`

- 全局目录：`~/.codex/skills/proof-orchestrator/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `proof-orchestrator` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $proof-orchestrator。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Manage a stateful, run-directory-based proof project with Codex: continuation across runs, run-local source bookkeeping, manual GPT Pro handoff packages when a local attempt stalls, and an optional DeepSeek second opinion as additional evidence only. Use when the user asks for proof-run orchestration, a GPT Pro handoff, or cross-run proof continuation — use /proof-writer for ordinary proof drafting and /proof-checker for rigorous verification or submission acceptance.

</details>

<a id="skill-proof-writer"></a>
### `$proof-writer`

- 全局目录：`~/.codex/skills/proof-writer/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `proof-writer` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $proof-writer。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Writes rigorous mathematical proofs for ML/AI theory. Use when asked to prove a theorem, lemma, proposition, or corollary, fill in missing proof steps, formalize a proof sketch, 补全证明, 写证明, 证明某个命题, or determine whether a claimed proof can actually be completed under the stated assumptions.

</details>

<a id="skill-pydicom"></a>
### `$pydicom`

- 全局目录：`~/.codex/skills/pydicom/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pydicom` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pydicom。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reads, inspects, writes, transforms, and preflights local DICOM datasets and pixel data. Applies to DICOM metadata, transfer syntaxes, compression plugins, frames, private elements, JSON, and bounded de-identification review.

</details>

上游线索：[https://github.com/pydicom/pydicom](https://github.com/pydicom/pydicom)

<a id="skill-render-html"></a>
### `$render-html`

- 全局目录：`~/.codex/skills/render-html/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `render-html` 的专项能力，主要用于检查问题并给出修改建议，并可处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $render-html。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Render an ARIS Markdown / JSON artifact (IDEA_REPORT, AUTO_REVIEW, KILL_ARGUMENT, PAPER_PLAN, research-wiki state, etc.) into a single-file HTML view designed for human reading. Use when the user says "渲染 HTML", "出一份 HTML 报告", "render html", "make this readable", "export to html", or wants a polished web-rendered view of a Markdown artifact.

</details>

上游线索：[https://github.com/nexu-io/html-anything](https://github.com/nexu-io/html-anything)

<a id="skill-research-grants"></a>
### `$research-grants`

- 全局目录：`~/.codex/skills/research-grants/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `research-grants` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $research-grants。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports research proposal preparation and review for NSF, NIH, DOE, DARPA, and Taiwan NSTC, including opportunity-specific requirements, aims, review criteria, budgets, broader impacts, forms, and resubmissions. Use for investigator-authored grant development, compliance matrices, and proposal critiques.

</details>

<a id="skill-research-refine"></a>
### `$research-refine`

- 全局目录：`~/.codex/skills/research-refine/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `research-refine` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $research-refine。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Turn a vague research direction into a problem-anchored, elegant, frontier-aware, implementation-oriented method plan via iterative GPT-6-Astra review. Use when the user says "refine my approach", "帮我细化方案", "decompose this problem", "打磨idea", "refine research plan", "细化研究方案", or wants a concrete research method that stays simple, focused, and top-venue ready instead of a vague or overbuilt idea.

</details>

<a id="skill-research-wiki"></a>
### `$research-wiki`

- 全局目录：`~/.codex/skills/research-wiki/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `research-wiki` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $research-wiki。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Persistent research knowledge base that accumulates papers, ideas, experiments, claims, and their relationships across the entire research lifecycle. Inspired by Karpathy's LLM Wiki pattern. Use when user says "知识库", "research wiki", "add paper", "wiki query", "查知识库", or wants to build/query a persistent field map.

</details>

<a id="skill-scholar-evaluation"></a>
### `$scholar-evaluation`

- 全局目录：`~/.codex/skills/scholar-evaluation/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `scholar-evaluation` 的专项能力，主要用于检查问题并给出修改建议。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $scholar-evaluation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with optional local quality controls. Never use for ranking people or consequential decisions.

</details>

<a id="skill-sympy"></a>
### `$sympy`

- 全局目录：`~/.codex/skills/sympy/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `sympy` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $sympy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs exact symbolic mathematics with SymPy for algebra, calculus, equation solving, symbolic linear algebra, physics, and lambdify or LaTeX code generation. Use when a task needs symbolic results, explicit assumptions, or exact arithmetic; use NumPy or SciPy for purely numerical workloads.

</details>

上游线索：[https://github.com/sympy/sympy](https://github.com/sympy/sympy)

<a id="skill-system-profile"></a>
### `$system-profile`

- 全局目录：`~/.codex/skills/system-profile/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `system-profile` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $system-profile。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Profile a target (script, process, GPU, memory, interconnect) for performance analysis. Use when user says "profile", "benchmark", "bottleneck", or wants performance analysis.

</details>

<a id="skill-training-check"></a>
### `$training-check`

- 全局目录：`~/.codex/skills/training-check/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `training-check` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $training-check。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Interactively monitor training metrics from the current Codex session, periodically checking WandB or fallback logs for NaN, divergence, plateaus, and broken runs.

</details>

<a id="skill-typst-author"></a>
### `$typst-author`

- 全局目录：`~/.codex/skills/typst-author/`
- 所属技能套件：[独立或暂未归入大型套件](../技能套件导航.md#suite-standalone)
- 推荐总入口：直接调用当前小 skill
- 中文理解：围绕 `typst-author` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $typst-author。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate idiomatic Typst (.typ) code, edit and troubleshoot Typst documents and projects, and answer Typst syntax/reference questions. Use when working with .typ files or when the user explicitly asks for Typst document creation, editing, debugging, compilation, formatting, template work, or package usage.

</details>

<a id="skill-vast-gpu"></a>
### `$vast-gpu`

- 全局目录：`~/.codex/skills/vast-gpu/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“通用科研工具与质量保障”的专项技能，用于处理 `vast-gpu` 相关任务。
- 适合何时使用：无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $vast-gpu。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Rent, manage, and destroy GPU instances on vast.ai. Use when user says "rent gpu", "vast.ai", "rent a server", "cloud gpu", or needs on-demand GPU without owning hardware.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
