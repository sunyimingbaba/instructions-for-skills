# 科研工作流与自治实验

把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。

本页收录 **22** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$ablation-planner`](#skill-ablation-planner) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `ablation-planner` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。 |
| [`$academic-research-suite`](#skill-academic-research-suite) | [ARS-Codex 学术研究套件](../技能套件导航.md#suite-academic-research-suite) | 围绕 `academic-research-suite` 的专项能力，主要用于检查问题并给出修改建议，并可规划、运行或复盘实验。 |
| [`$analyze-results`](#skill-analyze-results) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `analyze-results` 的专项能力，主要用于规划、运行或复盘实验。 |
| [`$ara-compiler`](#skill-compiler) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `ara-compiler` 的专项能力，主要用于构建或评估智能体工作流，并可规划、运行或复盘实验。 |
| [`$ara-research-manager`](#skill-research-manager) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `ara-research-manager` 的专项能力，主要用于检查问题并给出修改建议，并可规划、运行或复盘实验。 |
| [`$ara-rigor-reviewer`](#skill-rigor-reviewer) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `ara-rigor-reviewer` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。 |
| [`$autoresearch`](#skill-0-autoresearch-skill) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `autoresearch` 的专项能力，主要用于构建或评估智能体工作流，并可规划、运行或复盘实验。 |
| [`$autoskill`](#skill-autoskill) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `autoskill` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。 |
| [`$brainstorming-research-ideas`](#skill-brainstorming-research-ideas) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 这是一个面向“科研工作流与自治实验”的专项技能，用于处理 `brainstorming-research-ideas` 相关任务。 |
| [`$creative-thinking-for-research`](#skill-creative-thinking-for-research) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 这是一个面向“科研工作流与自治实验”的专项技能，用于处理 `creative-thinking-for-research` 相关任务。 |
| [`$experiment-audit`](#skill-experiment-audit) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `experiment-audit` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。 |
| [`$experiment-bridge`](#skill-experiment-bridge) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `experiment-bridge` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。 |
| [`$experiment-plan`](#skill-experiment-plan) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `experiment-plan` 的专项能力，主要用于规划、运行或复盘实验。 |
| [`$experiment-queue`](#skill-experiment-queue) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `experiment-queue` 的专项能力，主要用于规划、运行或复盘实验。 |
| [`$hypogenic`](#skill-hypogenic) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `hypogenic` 的专项能力，主要用于检查问题并给出修改建议，并可规划、运行或复盘实验。 |
| [`$idea-creator`](#skill-idea-creator) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 这是一个面向“科研工作流与自治实验”的专项技能，用于处理 `idea-creator` 相关任务。 |
| [`$idea-discovery`](#skill-idea-discovery) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `idea-discovery` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$idea-discovery-robot`](#skill-idea-discovery-robot) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `idea-discovery-robot` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。 |
| [`$monitor-experiment`](#skill-monitor-experiment) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `monitor-experiment` 的专项能力，主要用于规划、运行或复盘实验。 |
| [`$research-pipeline`](#skill-research-pipeline) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `research-pipeline` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。 |
| [`$research-refine-pipeline`](#skill-research-refine-pipeline) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `research-refine-pipeline` 的专项能力，主要用于组织可复现的科研流程，并可规划、运行或复盘实验。 |
| [`$run-experiment`](#skill-run-experiment) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `run-experiment` 的专项能力，主要用于规划、运行或复盘实验。 |

## 详细说明

<a id="skill-ablation-planner"></a>
### `$ablation-planner`

- 全局目录：`~/.codex/skills/ablation-planner/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `ablation-planner` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $ablation-planner。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Use when main results pass result-to-claim (`claim_supported = yes` or `partial`) and ablation studies are needed for paper submission. A secondary Codex agent designs ablations from a reviewer's perspective; the local executor reviews feasibility and implements.

</details>

<a id="skill-academic-research-suite"></a>
### `$academic-research-suite`

- 全局目录：`~/.codex/skills/academic-research-suite/`
- 所属技能套件：[ARS-Codex 学术研究套件](../技能套件导航.md#suite-academic-research-suite)
- 推荐总入口：`$academic-research-suite`
- 中文理解：围绕 `academic-research-suite` 的专项能力，主要用于检查问题并给出修改建议，并可规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $academic-research-suite。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

ARS-Codex research, writing, manuscript review, study screening, and experiments. Use for deep research, literature or systematic reviews, meta-analysis, research questions, drafts, revisions, roadmaps, abstracts, citations, integrity checks, peer review, research-to-paper. Screen records: sr-screener. Citation triggers: check citations, look over the refs, 檢查引用, 檢查參考文獻, 인용 확인, 인용 형식 검사. Korean: 논문 심사, 논문 수정, 초록 작성, 체계적 문헌고찰, 연구부터 논문까지. Español: revisión de literatura, revisar artículo, enmendar mi artículo, escribir resumen, investigación a artículo. Also use for ARS aliases: /ars-plan, /ars-outline, /ars-abstract, /ars-lit-review, /ars-citation-check, /ars-disclosure, /ars-format-convert, /ars-3w, /ars-revision-coach, /ars-revision, /ars-reviewer, /ars-mark-read, /ars-unmark-read, /ars-cache-invalidate, /ars-rebuttal-audit, /ars-full. Prompts, references, templates, and contracts live under ars/.

</details>

<a id="skill-analyze-results"></a>
### `$analyze-results`

- 全局目录：`~/.codex/skills/analyze-results/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `analyze-results` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $analyze-results。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyze ML experiment results, compute statistics, generate comparison tables and insights. Use when user says "analyze results", "compare", or needs to interpret experimental data.

</details>

<a id="skill-compiler"></a>
### `$ara-compiler`

- 全局目录：`~/.codex/skills/compiler/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `ara-compiler` 的专项能力，主要用于构建或评估智能体工作流，并可规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $ara-compiler。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Compiles any research input — PDF papers, GitHub repositories, experiment logs, code directories, or raw notes — into a complete Agent-Native Research Artifact (ARA) with cognitive layer (claims, concepts, heuristics), physical layer (configs, code stubs), exploration graph, and grounded evidence. Use when ingesting a paper or codebase into a structured, machine-executable knowledge package, building an ARA from scratch, or converting research outputs into a falsifiable, agent-traversable form.

</details>

<a id="skill-research-manager"></a>
### `$ara-research-manager`

- 全局目录：`~/.codex/skills/research-manager/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `ara-research-manager` 的专项能力，主要用于检查问题并给出修改建议，并可规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $ara-research-manager。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Records research provenance as a post-task epilogue, scanning conversation history at the end of a coding or research session to extract decisions, experiments, dead ends, claims, heuristics, and pivots, and writing them into the ara/ directory with user-vs-AI provenance tags. Use as a session epilogue — never during execution — to maintain a faithful, auditable trace of how a research project actually evolved.

</details>

<a id="skill-rigor-reviewer"></a>
### `$ara-rigor-reviewer`

- 全局目录：`~/.codex/skills/rigor-reviewer/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `ara-rigor-reviewer` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $ara-rigor-reviewer。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs ARA Seal Level 2 semantic epistemic review on Agent-Native Research Artifacts, scoring six dimensions (evidence relevance, falsifiability, scope calibration, argument coherence, exploration integrity, methodological rigor) and producing a constructive, severity-ranked report with a Strong Accept-to-Reject recommendation. Use after Level 1 structural validation passes, when an ARA needs an objective epistemic critique before publication or release.

</details>

<a id="skill-0-autoresearch-skill"></a>
### `$autoresearch`

- 全局目录：`~/.codex/skills/0-autoresearch-skill/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `autoresearch` 的专项能力，主要用于构建或评估智能体工作流，并可规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $autoresearch。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Orchestrates end-to-end autonomous AI research projects using a two-loop architecture. The inner loop runs rapid experiment iterations with clear optimization targets. The outer loop synthesizes results, identifies patterns, and steers research direction. Routes to domain-specific skills for execution, supports continuous agent operation via Claude Code /loop and OpenClaw heartbeat, and produces research presentations and papers. Use when starting a research project, running autonomous experiments, or managing a multi-hypothesis research effort.

</details>

<a id="skill-autoskill"></a>
### `$autoskill`

- 全局目录：`~/.codex/skills/autoskill/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `autoskill` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $autoskill。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes user-requested Screenpipe history windows to detect repeated research workflows, match existing scientific skills, and stage new skill drafts or composition recipes for review. Requires a reachable Screenpipe HTTP API, normally on localhost:3030. Detection and embedding inference run locally; the selected LLM receives redacted app/title cluster summaries and matched skill descriptions. Use only when the user explicitly asks to analyze their recent work and propose skills.

</details>

上游线索：[https://github.com/screenpipe/screenpipe](https://github.com/screenpipe/screenpipe)

<a id="skill-brainstorming-research-ideas"></a>
### `$brainstorming-research-ideas`

- 全局目录：`~/.codex/skills/brainstorming-research-ideas/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：这是一个面向“科研工作流与自治实验”的专项技能，用于处理 `brainstorming-research-ideas` 相关任务。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $brainstorming-research-ideas。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Guides researchers through structured ideation frameworks to discover high-impact research directions. Use when exploring new problem spaces, pivoting between projects, or seeking novel angles on existing work.

</details>

<a id="skill-creative-thinking-for-research"></a>
### `$creative-thinking-for-research`

- 全局目录：`~/.codex/skills/creative-thinking-for-research/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：这是一个面向“科研工作流与自治实验”的专项技能，用于处理 `creative-thinking-for-research` 相关任务。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $creative-thinking-for-research。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Applies cognitive science frameworks for creative thinking to CS and AI research ideation. Use when seeking genuinely novel research directions by leveraging combinatorial creativity, analogical reasoning, constraint manipulation, and other empirically grounded creative strategies.

</details>

<a id="skill-experiment-audit"></a>
### `$experiment-audit`

- 全局目录：`~/.codex/skills/experiment-audit/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `experiment-audit` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $experiment-audit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Audit experiment integrity before claiming results. Uses fresh-agent GPT-6-Astra review (same-family provisional in the base Codex mirror) to check for fake ground truth, score normalization fraud, phantom results, and insufficient scope. Use when user says "审计实验", "check experiment integrity", "audit results", "实验诚实度", or after experiments complete before writing claims.

</details>

<a id="skill-experiment-bridge"></a>
### `$experiment-bridge`

- 全局目录：`~/.codex/skills/experiment-bridge/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `experiment-bridge` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $experiment-bridge。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Workflow 1.5: Bridge between idea discovery and auto review. Reads EXPERIMENT_PLAN.md, implements experiment code, deploys to GPU, collects initial results. Use when user says "实现实验", "implement experiments", "bridge", "从计划到跑实验", "deploy the plan", or has an experiment plan ready to execute.

</details>

上游线索：[https://github.com/org/project](https://github.com/org/project)

<a id="skill-experiment-plan"></a>
### `$experiment-plan`

- 全局目录：`~/.codex/skills/experiment-plan/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `experiment-plan` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $experiment-plan。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Turn a refined research proposal or method idea into a detailed, claim-driven experiment roadmap. Use after `research-refine`, or when the user asks for a detailed experiment plan, ablation matrix, evaluation protocol, run order, compute budget, or paper-ready validation that supports the core problem, novelty, simplicity, and any LLM / VLM / Diffusion / RL-based contribution.

</details>

<a id="skill-experiment-queue"></a>
### `$experiment-queue`

- 全局目录：`~/.codex/skills/experiment-queue/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `experiment-queue` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $experiment-queue。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

SSH job queue for multi-seed/multi-config ML experiments with OOM-aware retry, stale-screen cleanup, and wave-transition race prevention. Use when user says "batch experiments", "队列实验", "run grid", "multi-seed sweep", "auto-chain experiments", or when /run-experiment is insufficient for 10+ jobs that need orchestration.

</details>

<a id="skill-hypogenic"></a>
### `$hypogenic`

- 全局目录：`~/.codex/skills/hypogenic/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `hypogenic` 的专项能力，主要用于检查问题并给出修改建议，并可规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $hypogenic。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Plans and audits use of ChicagoHAI HypoGeniC/HypoRefine for LLM-assisted hypothesis generation from labeled text datasets. Use for the `hypogenic` package, its task configs, hypothesis banks, or HypoBench datasets—not for manual hypothesis formulation or scientific validation.

</details>

上游线索：[https://github.com/ChicagoHAI/hypothesis-generation](https://github.com/ChicagoHAI/hypothesis-generation)

<a id="skill-idea-creator"></a>
### `$idea-creator`

- 全局目录：`~/.codex/skills/idea-creator/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：这是一个面向“科研工作流与自治实验”的专项技能，用于处理 `idea-creator` 相关任务。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $idea-creator。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generate and rank research ideas given a broad direction. Use when user says "找idea", "brainstorm ideas", "generate research ideas", "what can we work on", or wants to explore a research area for publishable directions.

</details>

<a id="skill-idea-discovery"></a>
### `$idea-discovery`

- 全局目录：`~/.codex/skills/idea-discovery/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `idea-discovery` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $idea-discovery。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Workflow 1: Full idea discovery pipeline to go from a broad research direction to validated, pilot-tested ideas. Use when user says "找idea全流程", "idea discovery pipeline", "从零开始找方向", or wants the complete idea exploration workflow.

</details>

<a id="skill-idea-discovery-robot"></a>
### `$idea-discovery-robot`

- 全局目录：`~/.codex/skills/idea-discovery-robot/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `idea-discovery-robot` 的专项能力，主要用于检查问题并给出修改建议，并可组织可复现的科研流程。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $idea-discovery-robot。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Workflow 1 adaptation for robotics and embodied AI. Orchestrates robotics-aware literature survey, idea generation, novelty check, and critical review to go from a broad robotics direction to benchmark-grounded, simulation-first ideas. Use when user says \"robotics idea discovery\", \"机器人找idea\", \"embodied AI idea\", \"机器人方向探索\", \"sim2real 选题\", or wants ideas for manipulation, locomotion, navigation, drones, humanoids, or general robot learning.

</details>

<a id="skill-monitor-experiment"></a>
### `$monitor-experiment`

- 全局目录：`~/.codex/skills/monitor-experiment/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `monitor-experiment` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $monitor-experiment。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Monitor running experiments, check progress, collect results. Use when user says "check results", "is it done", "monitor", or wants experiment output.

</details>

<a id="skill-research-pipeline"></a>
### `$research-pipeline`

- 全局目录：`~/.codex/skills/research-pipeline/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `research-pipeline` 的专项能力，主要用于检查问题并给出修改建议，并可构建或评估智能体工作流。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $research-pipeline。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Full end-to-end research pipeline: from a broad research direction through idea discovery, experiments, and review all the way to a polished paper PDF. Use when user says "全流程", "full pipeline", "从找idea到投稿", "end-to-end research", or wants the complete autonomous research lifecycle.

</details>

上游线索：[https://github.com/org/project](https://github.com/org/project)

<a id="skill-research-refine-pipeline"></a>
### `$research-refine-pipeline`

- 全局目录：`~/.codex/skills/research-refine-pipeline/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `research-refine-pipeline` 的专项能力，主要用于组织可复现的科研流程，并可规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $research-refine-pipeline。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Run an end-to-end workflow that chains `research-refine` and `experiment-plan`. Use when the user wants a one-shot pipeline from vague research direction to focused final proposal plus detailed experiment roadmap, or asks to "串起来", build a pipeline, do it end-to-end, or generate both the method and experiment plan together.

</details>

<a id="skill-run-experiment"></a>
### `$run-experiment`

- 全局目录：`~/.codex/skills/run-experiment/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `run-experiment` 的专项能力，主要用于规划、运行或复盘实验。
- 适合何时使用：把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $run-experiment。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Deploy and run ML experiments on local or remote GPU servers. Use when user says "run experiment", "deploy to server", "跑实验", or needs to launch training jobs.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
