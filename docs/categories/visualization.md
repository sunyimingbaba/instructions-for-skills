# 科学可视化、文档与演示

生成或检查论文图表、流程图、海报、幻灯片和技术文档。

本页收录 **27** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$academic-plotting`](#skill-academic-plotting) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `academic-plotting` 的专项能力，主要用于生成或检查科研图表。 |
| [`$auto-review-loop-llm`](#skill-auto-review-loop-llm) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `auto-review-loop-llm` 的专项能力，主要用于生成或检查科研图表。 |
| [`$figure-spec`](#skill-figure-spec) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `figure-spec` 的专项能力，主要用于生成或检查科研图表。 |
| [`$generate-image`](#skill-generate-image) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `generate-image` 相关任务。 |
| [`$infographics`](#skill-infographics) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `infographics` 相关任务。 |
| [`$latex-posters`](#skill-latex-posters) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `latex-posters` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。 |
| [`$markdown-mermaid-writing`](#skill-markdown-mermaid-writing) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `markdown-mermaid-writing` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。 |
| [`$matplotlib`](#skill-matplotlib) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `matplotlib` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。 |
| [`$mermaid-diagram`](#skill-mermaid-diagram) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `mermaid-diagram` 的专项能力，主要用于生成或检查科研图表。 |
| [`$meta-apply`](#skill-meta-apply) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `meta-apply` 相关任务。 |
| [`$nature-figure`](#skill-nature-figure) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 围绕 `nature-figure` 的专项能力，主要用于起草和修改论文，并可生成或检查科研图表。 |
| [`$nature-image2ppt`](#skill-nature-image2ppt) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 围绕 `nature-image2ppt` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$paper-figure`](#skill-paper-figure) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `paper-figure` 的专项能力，主要用于生成或检查科研图表。 |
| [`$paper-illustration`](#skill-paper-illustration) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `paper-illustration` 的专项能力，主要用于生成或检查科研图表。 |
| [`$paper-poster`](#skill-paper-poster) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `paper-poster` 相关任务。 |
| [`$paper-poster-html`](#skill-paper-poster-html) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `paper-poster-html` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。 |
| [`$paper-slides`](#skill-paper-slides) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `paper-slides` 的专项能力，主要用于处理科研文档与结构化内容。 |
| [`$pixel-art`](#skill-pixel-art) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `pixel-art` 相关任务。 |
| [`$pptx-posters`](#skill-pptx-posters) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `pptx-posters` 相关任务。 |
| [`$research-implement-feature`](#skill-research-implement-feature) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `research-implement-feature` 相关任务。 |
| [`$scientific-figure-making`](#skill-scientific-figure-making) | [独立或暂未归入大型套件](../技能套件导航.md#suite-standalone) | 围绕 `scientific-figure-making` 的专项能力，主要用于生成或检查科研图表。 |
| [`$scientific-schematics`](#skill-scientific-schematics) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `scientific-schematics` 的专项能力，主要用于生成或检查科研图表。 |
| [`$scientific-slides`](#skill-scientific-slides) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `scientific-slides` 相关任务。 |
| [`$scientific-visualization`](#skill-scientific-visualization) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `scientific-visualization` 的专项能力，主要用于生成或检查科研图表。 |
| [`$seaborn`](#skill-seaborn) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `seaborn` 的专项能力，主要用于生成或检查科研图表。 |
| [`$slides-polish`](#skill-slides-polish) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `slides-polish` 相关任务。 |
| [`$visiomaster`](#skill-visiomaster) | [独立或暂未归入大型套件](../技能套件导航.md#suite-standalone) | 围绕 `visiomaster` 的专项能力，主要用于生成或检查科研图表。 |

## 详细说明

<a id="skill-academic-plotting"></a>
### `$academic-plotting`

- 全局目录：`~/.codex/skills/academic-plotting/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `academic-plotting` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $academic-plotting。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generates publication-quality figures for ML papers from research context. Given a paper section or description, extracts system components and relationships to generate architecture diagrams via Gemini. Given experiment results or data, auto-selects chart type and generates data-driven figures via matplotlib/seaborn. Use when creating any figure for a conference paper.

</details>

<a id="skill-auto-review-loop-llm"></a>
### `$auto-review-loop-llm`

- 全局目录：`~/.codex/skills/auto-review-loop-llm/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `auto-review-loop-llm` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $auto-review-loop-llm。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Autonomous research review loop using any OpenAI-compatible LLM API. Configure via llm-chat MCP server or environment variables. Trigger with "auto review loop llm" or "llm review".

</details>

<a id="skill-figure-spec"></a>
### `$figure-spec`

- 全局目录：`~/.codex/skills/figure-spec/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `figure-spec` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $figure-spec。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate deterministic publication-quality architecture, workflow, and pipeline diagrams from structured JSON (FigureSpec) into editable SVG. Use when user says "架构图", "workflow 图", "pipeline 图", "确定性矢量图", "figure spec", "draw architecture", or needs precise, editable, publication-ready vector diagrams. Preferred over AI illustration for formal architecture/workflow figures.

</details>

<a id="skill-generate-image"></a>
### `$generate-image`

- 全局目录：`~/.codex/skills/generate-image/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `generate-image` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $generate-image。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generates or edits images with AI models through the OpenRouter Image API (Gemini, Seedream, Recraft, GPT-Image, Riverflow). Use for photos, illustrations, artwork, concept art, visual assets, logos, and image editing or compositing from reference images. For flowcharts, circuits, pathways, and other technical diagrams, use the scientific-schematics skill instead.

</details>

<a id="skill-infographics"></a>
### `$infographics`

- 全局目录：`~/.codex/skills/infographics/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `infographics` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $infographics。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates and reviews infographics with Nano Banana 2 via OpenRouter. Use for statistical summaries, timelines, comparisons, processes, and visual explanations with supplied data or optional Sonar research. Supports ten layouts, eight style presets, reference images, and accessible palette starting points.

</details>

<a id="skill-latex-posters"></a>
### `$latex-posters`

- 全局目录：`~/.codex/skills/latex-posters/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `latex-posters` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $latex-posters。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates research posters in LaTeX using beamerposter, tikzposter, or baposter. Use for conference posters, academic presentations, multi-column scientific layouts, figure integration, typography, compilation, and PDF preflight.

</details>

<a id="skill-markdown-mermaid-writing"></a>
### `$markdown-mermaid-writing`

- 全局目录：`~/.codex/skills/markdown-mermaid-writing/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `markdown-mermaid-writing` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $markdown-mermaid-writing。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Writes scientific Markdown documentation and Mermaid diagrams for workflows, relationships, timelines, and schemas. Provides syntax references, document templates, accessibility guidance, and version-aware rendering checks. Use when a user requests Markdown, Mermaid, or a text-based structural diagram; quantitative scientific figures require suitable plotting tools.

</details>

上游线索：[https://github.com/SuperiorByteWorks-LLC/agent-project](https://github.com/SuperiorByteWorks-LLC/agent-project)

<a id="skill-matplotlib"></a>
### `$matplotlib`

- 全局目录：`~/.codex/skills/matplotlib/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `matplotlib` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $matplotlib。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates and customizes scientific plots with Matplotlib. Used for fine-grained control over plot elements, novel plot types, and scientific workflows. Export to PNG/PDF/SVG for publication. For quick statistical plots use seaborn; for interactive plots use plotly; for publication-ready multi-panel figures with journal styling, use scientific-visualization.

</details>

上游线索：[https://github.com/matplotlib/matplotlib](https://github.com/matplotlib/matplotlib)

<a id="skill-mermaid-diagram"></a>
### `$mermaid-diagram`

- 全局目录：`~/.codex/skills/mermaid-diagram/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `mermaid-diagram` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $mermaid-diagram。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate Mermaid diagrams from user requirements. Save .mmd and .md files to figures/ with syntax verification. Supports flowcharts, sequence diagrams, class diagrams, ER diagrams, Gantt charts, and many more diagram types.

</details>

<a id="skill-meta-apply"></a>
### `$meta-apply`

- 全局目录：`~/.codex/skills/meta-apply/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `meta-apply` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $meta-apply。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Privileged applier that LANDS meta-optimize / corpus-audit patches the user approved, with a fresh landing review and human approval. Base Codex review is same-family provisional. Use when the user says "meta apply", "/meta-apply", "land the staged patches", "应用优化", after a /meta-optimize run.

</details>

<a id="skill-nature-figure"></a>
### `$nature-figure`

- 全局目录：`~/.codex/skills/nature-figure/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：围绕 `nature-figure` 的专项能力，主要用于起草和修改论文，并可生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $nature-figure。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Create, revise, audit, and export manuscript scientific figures in Python or R. Use for 论文配图、科研绘图、多面板图 and submission-ready plots, or explicitly requested AI-generated graphical abstracts and mechanism schematics. Not for interactive dashboards, data cleaning, or statistics-only analysis.

</details>

<a id="skill-nature-image2ppt"></a>
### `$nature-image2ppt`

- 全局目录：`~/.codex/skills/nature-image2ppt/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：围绕 `nature-image2ppt` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $nature-image2ppt。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reconstruct slide images, screenshots, scanned PDFs, or image-only PPTX files as object-level editable PowerPoint. Use for 图片转可编辑PPT、截图还原PPT and diagram reconstruction; not authoring a new deck from research notes.

</details>

<a id="skill-paper-figure"></a>
### `$paper-figure`

- 全局目录：`~/.codex/skills/paper-figure/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `paper-figure` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-figure。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate publication-quality figures and tables from experiment results. Use when user says \"画图\", \"作图\", \"generate figures\", \"paper figures\", or needs plots for a paper.

</details>

上游线索：[https://github.com/jimliu/baoyu-skills](https://github.com/jimliu/baoyu-skills)

<a id="skill-paper-illustration"></a>
### `$paper-illustration`

- 全局目录：`~/.codex/skills/paper-illustration/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `paper-illustration` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-illustration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate publication-quality AI illustrations for academic papers using Gemini image generation. Creates architecture diagrams, method illustrations with Codex-supervised iterative refinement loop. Use when user says "生成图表", "画架构图", "AI绘图", "paper illustration", "generate diagram", or needs visual figures for papers.

</details>

<a id="skill-paper-poster"></a>
### `$paper-poster`

- 全局目录：`~/.codex/skills/paper-poster/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `paper-poster` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-poster。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

DEPRECATED — superseded by /paper-poster-html. Kept only as a redirect for muscle memory; do not use for new posters.

</details>

<a id="skill-paper-poster-html"></a>
### `$paper-poster-html`

- 全局目录：`~/.codex/skills/paper-poster-html/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `paper-poster-html` 的专项能力，主要用于生成或检查科研图表，并可处理科研文档与结构化内容。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-poster-html。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

DEFAULT poster pipeline — build an academic conference poster (ICML/NeurIPS/ICLR/CVPR/...) as a single HTML/CSS file with measurement-driven hard gates, real paper figures, a two-hue design-token system, and print-ready PDF via headless Chromium. Use when the user says "做海报", "poster", "conference poster", "paper poster", or asks to design/redo a research poster.

</details>

上游线索：[https://github.com/Chenruishuo/posterly](https://github.com/Chenruishuo/posterly)

<a id="skill-paper-slides"></a>
### `$paper-slides`

- 全局目录：`~/.codex/skills/paper-slides/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `paper-slides` 的专项能力，主要用于处理科研文档与结构化内容。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-slides。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate conference presentation slides (beamer LaTeX → PDF + editable PPTX) from a compiled paper, with speaker notes and full talk script. Use when user says "做PPT", "做幻灯片", "make slides", "conference talk", "presentation slides", "生成slides", "写演讲稿", or wants beamer slides for a conference talk.

</details>

<a id="skill-pixel-art"></a>
### `$pixel-art`

- 全局目录：`~/.codex/skills/pixel-art/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `pixel-art` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pixel-art。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate pixel art SVG illustrations for READMEs, docs, or slides. Use when user says "画像素图", "pixel art", "make an SVG illustration", "README hero image", or wants a cute visual.

</details>

<a id="skill-pptx-posters"></a>
### `$pptx-posters`

- 全局目录：`~/.codex/skills/pptx-posters/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `pptx-posters` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pptx-posters。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates and audits editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets. Used when the requested deliverable is a PowerPoint research/conference poster and exact physical, printer, accessibility, provenance, and package-security checks are required.

</details>

<a id="skill-research-implement-feature"></a>
### `$research-implement-feature`

- 全局目录：`~/.codex/skills/research-implement-feature/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `research-implement-feature` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $research-implement-feature。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Build a working artifact from a plain "implement X for me" request: a running end-to-end spine first, then one feature per rung, with every under-determined decision written to an assumption ledger BEFORE the code that depends on it and a sweep for the ones that slipped through undeclared (same-family provisional in the base Codex mirror). Use when user says "给我实现", "implement X", "帮我做一个能跑的", "先搭个原型再加功能", "build this feature", "prototype then extend", or hands over a capability description rather than an experiment plan.

</details>

<a id="skill-scientific-figure-making"></a>
### `$scientific-figure-making`

- 全局目录：`~/.codex/skills/scientific-figure-making/`
- 所属技能套件：[独立或暂未归入大型套件](../技能套件导航.md#suite-standalone)
- 推荐总入口：直接调用当前小 skill
- 中文理解：围绕 `scientific-figure-making` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $scientific-figure-making。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Covers publication-ready matplotlib figures for academic papers, slides, and reports—bars, trends, scatter, heatmaps, and multi-panel layouts—with this repository’s house style, print/vector export conventions, and parity with figures4papers demos. Use when the user is finalizing or creating such figures in matplotlib. Do not use for interactive dashboards or web viz (Plotly, Altair, Bokeh), exploratory-only plots without a publication target, dominant 3D or geographic mapping, or Illustrator/Figma-first infographic workflows.

</details>

<a id="skill-scientific-schematics"></a>
### `$scientific-schematics`

- 全局目录：`~/.codex/skills/scientific-schematics/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `scientific-schematics` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scientific-schematics。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generates scientific diagram drafts using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.7 Flash for quality review. Refines when the review requests improvement, with at most two generations. Specialized in neural network architectures, system diagrams, flowcharts, biological pathways, and complex scientific visualizations.

</details>

<a id="skill-scientific-slides"></a>
### `$scientific-slides`

- 全局目录：`~/.codex/skills/scientific-slides/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `scientific-slides` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scientific-slides。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds slide decks and presentations for research talks. Used for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.

</details>

<a id="skill-scientific-visualization"></a>
### `$scientific-visualization`

- 全局目录：`~/.codex/skills/scientific-visualization/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `scientific-visualization` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scientific-visualization。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates and audits truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or Plotly. Use it for figure design, multi-panel layouts, uncertainty and missing-data displays, color/contrast review, image metadata validation, and journal export planning.

</details>

<a id="skill-seaborn"></a>
### `$seaborn`

- 全局目录：`~/.codex/skills/seaborn/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `seaborn` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $seaborn。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates Seaborn statistical visualizations with pandas integration for distributions, relationships, categorical comparisons, regression displays, pair plots, and heatmaps. Supports function and objects interfaces with explicit aggregation, uncertainty, and missing-data handling. Best suited to static exploratory plots; plotly covers interactive figures and scientific-visualization covers publication styling.

</details>

<a id="skill-slides-polish"></a>
### `$slides-polish`

- 全局目录：`~/.codex/skills/slides-polish/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“科学可视化、文档与演示”的专项技能，用于处理 `slides-polish` 相关任务。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $slides-polish。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Per-page Codex review + targeted python-pptx / Beamer fixes for academic talk slides. Use AFTER /paper-slides (or any externally generated PPTX/Beamer) when the deck looks 'mostly OK' but the user wants a final pass that aligns visual weight with a reference, bumps PPTX fonts to projector-readable size, kills italic style leaks, fixes text-frame overflow, and catches per-slide layout drift. Trigger phrases: "polish slides", "slides 排版不对", "PPTX 字体太小", "和 Beamer 比一下", "per-page review", "和 codex 一页一页过".

</details>

<a id="skill-visiomaster"></a>
### `$visiomaster`

- 全局目录：`~/.codex/skills/Visiomaster/`
- 所属技能套件：[独立或暂未归入大型套件](../技能套件导航.md#suite-standalone)
- 推荐总入口：直接调用当前小 skill
- 中文理解：围绕 `visiomaster` 的专项能力，主要用于生成或检查科研图表。
- 适合何时使用：生成或检查论文图表、流程图、海报、幻灯片和技术文档。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $visiomaster。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Windows-first Visio diagram reconstruction workflow for flowcharts, architecture diagrams, and paper-style module figures. Reuses ppt-master style analysis and composition discipline on the front half, but outputs editable Visio .vsdx plus exported .svg and .png through a scene.json to Visio pipeline. Use when the user wants a diagram recreated as editable Visio shapes instead of a pasted screenshot or PPT-only result.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
