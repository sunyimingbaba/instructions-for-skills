# 智能体、RAG、安全与评测

用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。

本页收录 **33** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$arbor`](#skill-arbor) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `arbor` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$auto-review-loop`](#skill-auto-review-loop) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `auto-review-loop` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$autogpt-agents`](#skill-autogpt) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `autogpt-agents` 的专项能力，主要用于构建或评估智能体工作流，并可组织可复现的科研流程。 |
| [`$chroma`](#skill-chroma) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `chroma` 的专项能力，主要用于构建检索增强与知识问答系统。 |
| [`$constitutional-ai`](#skill-constitutional-ai) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `constitutional-ai` 的专项能力，主要用于增加内容安全检查与防护。 |
| [`$crewai-multi-agent`](#skill-crewai) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `crewai-multi-agent` 的专项能力，主要用于构建或评估智能体工作流，并可组织可复现的科研流程。 |
| [`$datalad`](#skill-datalad) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `datalad` 的专项能力，主要用于构建检索增强与知识问答系统。 |
| [`$dspy`](#skill-dspy) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `dspy` 的专项能力，主要用于构建或评估智能体工作流，并可构建检索增强与知识问答系统。 |
| [`$evaluating-code-models`](#skill-bigcode-evaluation-harness) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 这是一个面向“智能体、RAG、安全与评测”的专项技能，用于处理 `evaluating-code-models` 相关任务。 |
| [`$evaluating-llms-harness`](#skill-lm-evaluation-harness) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 这是一个面向“智能体、RAG、安全与评测”的专项技能，用于处理 `evaluating-llms-harness` 相关任务。 |
| [`$evolving-ai-agents`](#skill-a-evolve) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `evolving-ai-agents` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$faiss`](#skill-faiss) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `faiss` 的专项能力，主要用于完成机器学习建模与评估，并可构建检索增强与知识问答系统。 |
| [`$guidance`](#skill-guidance) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `guidance` 的专项能力，主要用于组织可复现的科研流程。 |
| [`$instructor`](#skill-instructor) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `instructor` 的专项能力，主要用于增加内容安全检查与防护。 |
| [`$langchain`](#skill-langchain) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `langchain` 的专项能力，主要用于构建或评估智能体工作流，并可构建检索增强与知识问答系统。 |
| [`$langsmith-observability`](#skill-langsmith) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `langsmith-observability` 的专项能力，主要用于追踪、评测和监控 LLM 应用，并可组织可复现的科研流程。 |
| [`$llamaguard`](#skill-llamaguard) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `llamaguard` 的专项能力，主要用于增加内容安全检查与防护。 |
| [`$llamaindex`](#skill-llamaindex) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `llamaindex` 的专项能力，主要用于构建或评估智能体工作流，并可构建检索增强与知识问答系统。 |
| [`$nemo-evaluator-sdk`](#skill-nemo-evaluator) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `nemo-evaluator-sdk` 的专项能力，主要用于增加内容安全检查与防护。 |
| [`$nemo-guardrails`](#skill-nemo-guardrails) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `nemo-guardrails` 的专项能力，主要用于增加内容安全检查与防护。 |
| [`$outlines`](#skill-outlines) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 这是一个面向“智能体、RAG、安全与评测”的专项技能，用于处理 `outlines` 相关任务。 |
| [`$pathml`](#skill-pathml) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pathml` 的专项能力，主要用于构建检索增强与知识问答系统，并可组织可复现的科研流程。 |
| [`$phoenix-observability`](#skill-phoenix) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `phoenix-observability` 的专项能力，主要用于追踪、评测和监控 LLM 应用。 |
| [`$pi-agent`](#skill-pi-agent) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pi-agent` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$pinecone`](#skill-pinecone) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `pinecone` 的专项能力，主要用于构建检索增强与知识问答系统，并可构建向量检索与相似度搜索。 |
| [`$prompt-guard`](#skill-prompt-guard) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `prompt-guard` 的专项能力，主要用于构建检索增强与知识问答系统。 |
| [`$proof-checker`](#skill-proof-checker) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `proof-checker` 的专项能力，主要用于构建或评估智能体工作流，并可组织可复现的科研流程。 |
| [`$qdrant-vector-search`](#skill-qdrant) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `qdrant-vector-search` 的专项能力，主要用于构建检索增强与知识问答系统，并可构建向量检索与相似度搜索。 |
| [`$research-review`](#skill-research-review) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `research-review` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$result-to-claim`](#skill-result-to-claim) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `result-to-claim` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$sentence-transformers`](#skill-sentence-transformers) | [AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra) | 围绕 `sentence-transformers` 的专项能力，主要用于完成机器学习建模与评估，并可构建检索增强与知识问答系统。 |
| [`$stable-baselines3`](#skill-stable-baselines3) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `stable-baselines3` 的专项能力，主要用于构建或评估智能体工作流。 |
| [`$uncertainty-and-units`](#skill-uncertainty-and-units) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `uncertainty-and-units` 的专项能力，主要用于构建检索增强与知识问答系统。 |

## 详细说明

<a id="skill-arbor"></a>
### `$arbor`

- 全局目录：`~/.codex/skills/arbor/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `arbor` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $arbor。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Applies Arbor Hypothesis Tree Refinement to research artifacts with repeatable evaluators, including model training, agent harnesses, data synthesis and benchmark optimization. Uses persistent hypotheses, isolated experiments, evidence propagation and held-out candidate comparison for multi-experiment research runs. Includes a standard-library state manager and guidance for the RUC-NLPIR Arbor CLI.

</details>

<a id="skill-auto-review-loop"></a>
### `$auto-review-loop`

- 全局目录：`~/.codex/skills/auto-review-loop/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `auto-review-loop` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $auto-review-loop。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Autonomous multi-round research review loop. Repeatedly reviews using a secondary Codex agent, implements fixes, and re-reviews until positive assessment or max rounds reached. Use when user says "auto review loop", "review until it passes", or wants autonomous iterative improvement.

</details>

<a id="skill-autogpt"></a>
### `$autogpt-agents`

- 全局目录：`~/.codex/skills/autogpt/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `autogpt-agents` 的专项能力，主要用于构建或评估智能体工作流，并可组织可复现的科研流程。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $autogpt-agents。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Autonomous AI agent platform for building and deploying continuous agents. Use when creating visual workflow agents, deploying persistent autonomous agents, or building complex multi-step AI automation systems.

</details>

上游线索：[https://github.com/Significant-Gravitas/AutoGPT.git](https://github.com/Significant-Gravitas/AutoGPT.git)

<a id="skill-chroma"></a>
### `$chroma`

- 全局目录：`~/.codex/skills/chroma/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `chroma` 的专项能力，主要用于构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $chroma。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. Simple 4-function API. Scales from notebooks to production clusters. Use for semantic search, RAG applications, or document retrieval. Best for local development and open-source projects.

</details>

上游线索：[https://github.com/chroma-core/chroma](https://github.com/chroma-core/chroma)

<a id="skill-constitutional-ai"></a>
### `$constitutional-ai`

- 全局目录：`~/.codex/skills/constitutional-ai/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `constitutional-ai` 的专项能力，主要用于增加内容安全检查与防护。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $constitutional-ai。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Anthropic's method for training harmless AI through self-improvement. Two-phase approach - supervised learning with self-critique/revision, then RLAIF (RL from AI Feedback). Use for safety alignment, reducing harmful outputs without human labels. Powers Claude's safety system.

</details>

<a id="skill-crewai"></a>
### `$crewai-multi-agent`

- 全局目录：`~/.codex/skills/crewai/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `crewai-multi-agent` 的专项能力，主要用于构建或评估智能体工作流，并可组织可复现的科研流程。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $crewai-multi-agent。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Multi-agent orchestration framework for autonomous AI collaboration. Use when building teams of specialized agents working together on complex tasks, when you need role-based agent collaboration with memory, or for production workflows requiring sequential/hierarchical execution. Built without LangChain dependencies for lean, fast execution.

</details>

上游线索：[https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)

<a id="skill-datalad"></a>
### `$datalad`

- 全局目录：`~/.codex/skills/datalad/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `datalad` 的专项能力，主要用于构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $datalad。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Retrieves, versions, and publishes scientific datasets with DataLad and git-annex, and captures computational provenance with datalad run, rerun, and containers-run. Use when cloning or fetching data from OpenNeuro, DANDI, datasets.datalad.org, or any DataLad dataset; when a file in a dataset reads as a broken symlink or a small pointer instead of real data; when an analysis needs a machine-readable record of how each output was produced so it can be re-executed; or when publishing a dataset to siblings such as a GitHub repository plus a storage remote. Also use to decide between DataLad and plain Git for a data-carrying repository.

</details>

上游线索：[https://github.com/OpenNeuroDatasets/ds000001.git](https://github.com/OpenNeuroDatasets/ds000001.git)

<a id="skill-dspy"></a>
### `$dspy`

- 全局目录：`~/.codex/skills/dspy/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `dspy` 的专项能力，主要用于构建或评估智能体工作流，并可构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $dspy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Build complex AI systems with declarative programming, optimize prompts automatically, create modular RAG systems and agents with DSPy - Stanford NLP's framework for systematic LM programming

</details>

上游线索：[https://github.com/stanfordnlp/dspy.git](https://github.com/stanfordnlp/dspy.git)

<a id="skill-bigcode-evaluation-harness"></a>
### `$evaluating-code-models`

- 全局目录：`~/.codex/skills/bigcode-evaluation-harness/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：这是一个面向“智能体、RAG、安全与评测”的专项技能，用于处理 `evaluating-code-models` 相关任务。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $evaluating-code-models。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Evaluates code generation models across HumanEval, MBPP, MultiPL-E, and 15+ benchmarks with pass@k metrics. Use when benchmarking code models, comparing coding abilities, testing multi-language support, or measuring code generation quality. Industry standard from BigCode Project used by HuggingFace leaderboards.

</details>

上游线索：[https://github.com/bigcode-project/bigcode-evaluation-harness.git](https://github.com/bigcode-project/bigcode-evaluation-harness.git)

<a id="skill-lm-evaluation-harness"></a>
### `$evaluating-llms-harness`

- 全局目录：`~/.codex/skills/lm-evaluation-harness/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：这是一个面向“智能体、RAG、安全与评测”的专项技能，用于处理 `evaluating-llms-harness` 相关任务。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $evaluating-llms-harness。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag). Use when benchmarking model quality, comparing models, reporting academic results, or tracking training progress. Industry standard used by EleutherAI, HuggingFace, and major labs. Supports HuggingFace, vLLM, APIs.

</details>

上游线索：[https://github.com/EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

<a id="skill-a-evolve"></a>
### `$evolving-ai-agents`

- 全局目录：`~/.codex/skills/a-evolve/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `evolving-ai-agents` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $evolving-ai-agents。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms. Use when building self-improving agents, optimizing agent prompts and skills against benchmarks, or implementing automated agent evaluation loops.

</details>

<a id="skill-faiss"></a>
### `$faiss`

- 全局目录：`~/.codex/skills/faiss/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `faiss` 的专项能力，主要用于完成机器学习建模与评估，并可构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $faiss。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Facebook's library for efficient similarity search and clustering of dense vectors. Supports billions of vectors, GPU acceleration, and various index types (Flat, IVF, HNSW). Use for fast k-NN search, large-scale vector retrieval, or when you need pure similarity search without metadata. Best for high-performance applications.

</details>

上游线索：[https://github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss)

<a id="skill-guidance"></a>
### `$guidance`

- 全局目录：`~/.codex/skills/guidance/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `guidance` 的专项能力，主要用于组织可复现的科研流程。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $guidance。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research's constrained generation framework

</details>

上游线索：[https://github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance)

<a id="skill-instructor"></a>
### `$instructor`

- 全局目录：`~/.codex/skills/instructor/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `instructor` 的专项能力，主要用于增加内容安全检查与防护。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $instructor。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type safety, and stream partial results with Instructor - battle-tested structured output library

</details>

上游线索：[https://github.com/jxnl/instructor](https://github.com/jxnl/instructor)

<a id="skill-langchain"></a>
### `$langchain`

- 全局目录：`~/.codex/skills/langchain/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `langchain` 的专项能力，主要用于构建或评估智能体工作流，并可构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $langchain。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Framework for building LLM-powered applications with agents, chains, and RAG. Supports multiple providers (OpenAI, Anthropic, Google), 500+ integrations, ReAct agents, tool calling, memory management, and vector store retrieval. Use for building chatbots, question-answering systems, autonomous agents, or RAG applications. Best for rapid prototyping and production deployments.

</details>

上游线索：[https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

<a id="skill-langsmith"></a>
### `$langsmith-observability`

- 全局目录：`~/.codex/skills/langsmith/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `langsmith-observability` 的专项能力，主要用于追踪、评测和监控 LLM 应用，并可组织可复现的科研流程。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $langsmith-observability。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

LLM observability platform for tracing, evaluation, and monitoring. Use when debugging LLM applications, evaluating model outputs against datasets, monitoring production systems, or building systematic testing pipelines for AI applications.

</details>

上游线索：[https://github.com/langchain-ai/langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk)

<a id="skill-llamaguard"></a>
### `$llamaguard`

- 全局目录：`~/.codex/skills/llamaguard/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `llamaguard` 的专项能力，主要用于增加内容安全检查与防护。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $llamaguard。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Meta's 7-8B specialized moderation model for LLM input/output filtering. 6 safety categories - violence/hate, sexual content, weapons, substances, self-harm, criminal planning. 94-95% accuracy. Deploy with vLLM, HuggingFace, Sagemaker. Integrates with NeMo Guardrails.

</details>

<a id="skill-llamaindex"></a>
### `$llamaindex`

- 全局目录：`~/.codex/skills/llamaindex/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `llamaindex` 的专项能力，主要用于构建或评估智能体工作流，并可构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $llamaindex。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Data framework for building LLM applications with RAG. Specializes in document ingestion (300+ connectors), indexing, and querying. Features vector indices, query engines, agents, and multi-modal support. Use for document Q&A, chatbots, knowledge retrieval, or building RAG pipelines. Best for data-centric LLM applications.

</details>

上游线索：[https://github.com/run-llama/llama_index](https://github.com/run-llama/llama_index)

<a id="skill-nemo-evaluator"></a>
### `$nemo-evaluator-sdk`

- 全局目录：`~/.codex/skills/nemo-evaluator/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `nemo-evaluator-sdk` 的专项能力，主要用于增加内容安全检查与防护。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $nemo-evaluator-sdk。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Evaluates LLMs across 100+ benchmarks from 18+ harnesses (MMLU, HumanEval, GSM8K, safety, VLM) with multi-backend execution. Use when needing scalable evaluation on local Docker, Slurm HPC, or cloud platforms. NVIDIA's enterprise-grade platform with container-first architecture for reproducible benchmarking.

</details>

上游线索：[https://github.com/NVIDIA-NeMo/Evaluator](https://github.com/NVIDIA-NeMo/Evaluator)

<a id="skill-nemo-guardrails"></a>
### `$nemo-guardrails`

- 全局目录：`~/.codex/skills/nemo-guardrails/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `nemo-guardrails` 的专项能力，主要用于增加内容安全检查与防护。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $nemo-guardrails。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

NVIDIA's runtime safety framework for LLM applications. Features jailbreak detection, input/output validation, fact-checking, hallucination detection, PII filtering, toxicity detection. Uses Colang 2.0 DSL for programmable rails. Production-ready, runs on T4 GPU.

</details>

上游线索：[https://github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)

<a id="skill-outlines"></a>
### `$outlines`

- 全局目录：`~/.codex/skills/outlines/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：这是一个面向“智能体、RAG、安全与评测”的专项技能，用于处理 `outlines` 相关任务。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $outlines。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models (Transformers, vLLM), and maximize inference speed with Outlines - dottxt.ai's structured generation library

</details>

上游线索：[https://github.com/outlines-dev/outlines](https://github.com/outlines-dev/outlines)

<a id="skill-pathml"></a>
### `$pathml`

- 全局目录：`~/.codex/skills/pathml/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pathml` 的专项能力，主要用于构建检索增强与知识问答系统，并可组织可复现的科研流程。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pathml。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports local computational pathology research with PathML: slide loading and tiling, preprocessing and QC, h5path storage, multiplex quantification, spatial graphs, and bounded model inference. Use for whole-slide H&E, CODEX, Vectra, Mesmer, HoVer-Net, and HACTNet workflows.

</details>

上游线索：[https://github.com/Dana-Farber-AIOS/pathml](https://github.com/Dana-Farber-AIOS/pathml)

<a id="skill-phoenix"></a>
### `$phoenix-observability`

- 全局目录：`~/.codex/skills/phoenix/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `phoenix-observability` 的专项能力，主要用于追踪、评测和监控 LLM 应用。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $phoenix-observability。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Open-source AI observability platform for LLM tracing, evaluation, and monitoring. Use when debugging LLM applications with detailed traces, running evaluations on datasets, or monitoring production AI systems with real-time insights.

</details>

上游线索：[https://github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)

<a id="skill-pi-agent"></a>
### `$pi-agent`

- 全局目录：`~/.codex/skills/pi-agent/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pi-agent` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $pi-agent。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds with and operates Pi, the minimal terminal coding harness. Use for installing Pi, configuring providers/models/settings/environment variables, creating Pi skills/extensions/packages/themes/prompt templates, embedding Pi through the SDK, integrating over RPC or JSON event streams, parsing sessions, running local models through the llama.cpp router, developing custom Pi providers and TUI components, or using ecosystem packages such as pi-subagents (delegation/orchestration), pi-mcp-adapter (MCP servers), pi-interview (interactive forms), and pi-web-access (web search, fetching, video understanding).

</details>

上游线索：[https://github.com/earendil-works/pi](https://github.com/earendil-works/pi)

<a id="skill-pinecone"></a>
### `$pinecone`

- 全局目录：`~/.codex/skills/pinecone/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `pinecone` 的专项能力，主要用于构建检索增强与知识问答系统，并可构建向量检索与相似度搜索。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pinecone。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Managed vector database for production AI applications. Fully managed, auto-scaling, with hybrid search (dense + sparse), metadata filtering, and namespaces. Low latency (<100ms p95). Use for production RAG, recommendation systems, or semantic search at scale. Best for serverless, managed infrastructure.

</details>

<a id="skill-prompt-guard"></a>
### `$prompt-guard`

- 全局目录：`~/.codex/skills/prompt-guard/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `prompt-guard` 的专项能力，主要用于构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $prompt-guard。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Meta's 86M prompt injection and jailbreak detector. Filters malicious prompts and third-party data for LLM apps. 99%+ TPR, <1% FPR. Fast (<2ms GPU). Multilingual (8 languages). Deploy with HuggingFace or batch processing for RAG security.

</details>

上游线索：[https://github.com/meta-llama/llama-cookbook](https://github.com/meta-llama/llama-cookbook)

<a id="skill-proof-checker"></a>
### `$proof-checker`

- 全局目录：`~/.codex/skills/proof-checker/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `proof-checker` 的专项能力，主要用于构建或评估智能体工作流，并可组织可复现的科研流程。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $proof-checker。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Rigorous mathematical proof verification and fixing workflow. Reads a LaTeX proof, identifies gaps via fresh-agent Codex GPT-6-Astra ultra review, fixes each gap with full derivations, re-reviews, and generates an audit report. Base review is same-family provisional. Use when user says "检查证明", "verify proof", "proof check", "审证明", "check this proof", or wants rigorous mathematical verification of a theory paper.

</details>

<a id="skill-qdrant"></a>
### `$qdrant-vector-search`

- 全局目录：`~/.codex/skills/qdrant/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `qdrant-vector-search` 的专项能力，主要用于构建检索增强与知识问答系统，并可构建向量检索与相似度搜索。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $qdrant-vector-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast nearest neighbor search, hybrid search with filtering, or scalable vector storage with Rust-powered performance.

</details>

上游线索：[https://github.com/qdrant/qdrant](https://github.com/qdrant/qdrant)

<a id="skill-research-review"></a>
### `$research-review`

- 全局目录：`~/.codex/skills/research-review/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `research-review` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $research-review。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Get a deep critical review of research from GPT using a secondary Codex agent. Use when user says "review my research", "help me review", "get external review", or wants critical feedback on research ideas, papers, or experimental results.

</details>

<a id="skill-result-to-claim"></a>
### `$result-to-claim`

- 全局目录：`~/.codex/skills/result-to-claim/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `result-to-claim` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $result-to-claim。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Use when experiments complete to judge what claims the results support, what they don't, and what evidence is still missing. A secondary Codex agent evaluates results against intended claims and routes to next action (pivot, supplement, or confirm). Use after experiments finish — before writing the paper or running ablations.

</details>

<a id="skill-sentence-transformers"></a>
### `$sentence-transformers`

- 全局目录：`~/.codex/skills/sentence-transformers/`
- 所属技能套件：[AI Research SKILLs（Orchestra Research）](../技能套件导航.md#suite-orchestra)
- 推荐总入口：`$autoresearch`
- 中文理解：围绕 `sentence-transformers` 的专项能力，主要用于完成机器学习建模与评估，并可构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $sentence-transformers。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Framework for state-of-the-art sentence, text, and image embeddings. Provides 5000+ pre-trained models for semantic similarity, clustering, and retrieval. Supports multilingual, domain-specific, and multimodal models. Use for generating embeddings for RAG, semantic search, or similarity tasks. Best for production embedding generation.

</details>

上游线索：[https://github.com/UKPLab/sentence-transformers](https://github.com/UKPLab/sentence-transformers)

<a id="skill-stable-baselines3"></a>
### `$stable-baselines3`

- 全局目录：`~/.codex/skills/stable-baselines3/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `stable-baselines3` 的专项能力，主要用于构建或评估智能体工作流。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $stable-baselines3。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Trains and evaluates single-agent reinforcement learning with Stable Baselines3 (PPO, SAC, DQN, TD3, DDPG, A2C), Gymnasium custom environments, vectorized rollouts, callbacks, and checkpoint normalization. Applies to reproducible RL experiments, continuous control, discrete actions, and SB3-Contrib recurrent or masked policies.

</details>

上游线索：[https://github.com/Stable-Baselines-Team/stable-baselines3-contrib](https://github.com/Stable-Baselines-Team/stable-baselines3-contrib)

<a id="skill-uncertainty-and-units"></a>
### `$uncertainty-and-units`

- 全局目录：`~/.codex/skills/uncertainty-and-units/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `uncertainty-and-units` 的专项能力，主要用于构建检索增强与知识问答系统。
- 适合何时使用：用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $uncertainty-and-units。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Tracks physical units and propagates measurement uncertainty in scientific calculations using pint and uncertainties. Use for unit conversion and dimensional checking, GUM uncertainty budgets, Type A and Type B evaluation, coverage factors and expanded uncertainty, Monte Carlo propagation, significant-figure and plus-minus reporting, error propagation through curve fits, CODATA constants, auditing Python code for stripped units or broken uncertainty propagation, and order-of-magnitude plausibility checks using dimensionless groups (Reynolds, Peclet, Damkohler, Knudsen, Biot, Womersley), characteristic scales such as diffusion time or Debye length, and observed magnitude ranges. Trigger on "is this number physically reasonable", "sanity check these units", "what regime is this flow in", or a result that looks off by orders of magnitude.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
