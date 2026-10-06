# 文献检索、证据与引用

用于找论文、核对出处、整理证据、管理引用和撰写综述。

本页收录 **33** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$alphaxiv`](#skill-alphaxiv) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `alphaxiv` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$arxiv`](#skill-arxiv) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `arxiv` 的专项能力，主要用于检索和筛选科研文献，并可处理科研文档与结构化内容。 |
| [`$bgpt-paper-search`](#skill-bgpt-paper-search) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `bgpt-paper-search` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$citation-audit`](#skill-citation-audit) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `citation-audit` 的专项能力，主要用于核对引用与来源。 |
| [`$citation-management`](#skill-citation-management) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `citation-management` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$comm-lit-review`](#skill-comm-lit-review) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `comm-lit-review` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$deepxiv`](#skill-deepxiv) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `deepxiv` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$folklore-variant-evidence`](#skill-folklore-variant-evidence) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `folklore-variant-evidence` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$gemini-search`](#skill-gemini-search) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `gemini-search` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$grant-proposal`](#skill-grant-proposal) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `grant-proposal` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$imaging-data-commons`](#skill-imaging-data-commons) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `imaging-data-commons` 的专项能力，主要用于核对引用与来源。 |
| [`$literature-review`](#skill-literature-review) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `literature-review` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$nature-academic-search`](#skill-nature-academic-search) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 围绕 `nature-academic-search` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$nature-citation`](#skill-nature-citation) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 围绕 `nature-citation` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$nature-data`](#skill-nature-data) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 围绕 `nature-data` 的专项能力，主要用于核对引用与来源。 |
| [`$nature-literature-pipeline`](#skill-nature-literature-pipeline) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 围绕 `nature-literature-pipeline` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$nature-ref-verifier`](#skill-nature-ref-verifier) | [Nature Research Skills](../技能套件导航.md#suite-nature) | 对学术文献逐条执行多源交叉验证，逐字段对比作者、标题、年份、卷期、页码， 标记卷年/DOI年冲突、作者顺序异常、页码偏差等问题，输出结构化验证报告。 |
| [`$networkx`](#skill-networkx) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `networkx` 的专项能力，主要用于核对引用与来源。 |
| [`$novelty-check`](#skill-novelty-check) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `novelty-check` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$openalex`](#skill-openalex) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `openalex` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$paper-lookup`](#skill-paper-lookup) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `paper-lookup` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$paper-talk`](#skill-paper-talk) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `paper-talk` 的专项能力，主要用于核对引用与来源。 |
| [`$paperclip`](#skill-paperclip) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `paperclip` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$peer-review`](#skill-peer-review) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `peer-review` 的专项能力，主要用于核对引用与来源。 |
| [`$prior-art-search`](#skill-prior-art-search) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `prior-art-search` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$pyzotero`](#skill-pyzotero) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pyzotero` 的专项能力，主要用于核对引用与来源，并可处理科研文档与结构化内容。 |
| [`$research-lit`](#skill-research-lit) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `research-lit` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$research-lookup`](#skill-research-lookup) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `research-lookup` 的专项能力，主要用于检索和筛选科研文献。 |
| [`$research-writing-skill`](#skill-research-writing-skill) | [Scientific Toolkit 科研计算套件](../技能套件导航.md#suite-scientific-toolkit) | 围绕 `research-writing-skill` 的专项能力，主要用于核对引用与来源。 |
| [`$scientific-toolkit-skill`](#skill-scientific-toolkit-skill) | [Scientific Toolkit 科研计算套件](../技能套件导航.md#suite-scientific-toolkit) | 围绕 `scientific-toolkit-skill` 的专项能力，主要用于核对引用与来源。 |
| [`$semantic-scholar`](#skill-semantic-scholar) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `semantic-scholar` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。 |
| [`$web-debug-search`](#skill-web-debug-search) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `web-debug-search` 的专项能力，主要用于核对引用与来源，并可处理科研文档与结构化内容。 |
| [`$wiki-enrich`](#skill-wiki-enrich) | [Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris) | 围绕 `wiki-enrich` 的专项能力，主要用于检索和筛选科研文献。 |

## 详细说明

<a id="skill-alphaxiv"></a>
### `$alphaxiv`

- 全局目录：`~/.codex/skills/alphaxiv/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `alphaxiv` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $alphaxiv。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Quick single-paper lookup via AlphaXiv LLM-optimized summaries with tiered source fallback. Use when user says "explain this paper", "summarize paper", pastes an arXiv/AlphaXiv URL, or provides a bare arXiv ID for quick understanding - not for broad literature search.

</details>

<a id="skill-arxiv"></a>
### `$arxiv`

- 全局目录：`~/.codex/skills/arxiv/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `arxiv` 的专项能力，主要用于检索和筛选科研文献，并可处理科研文档与结构化内容。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $arxiv。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search, download, and summarize academic papers from arXiv. Use when user says "search arxiv", "download paper", "fetch arxiv", "arxiv search", "get paper pdf", or wants to find and save papers from arXiv to the local paper library.

</details>

<a id="skill-bgpt-paper-search"></a>
### `$bgpt-paper-search`

- 全局目录：`~/.codex/skills/bgpt-paper-search/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `bgpt-paper-search` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $bgpt-paper-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Searches BGPT scientific papers by topic or DOI and retrieves claim-level evidence extracted from full text, including experiments, reported statistics, scope, limitations, and provenance. Use for literature reviews, evidence synthesis, and finding experimental details beyond abstracts.

</details>

上游线索：[https://github.com/punkpeye/mcp-remote](https://github.com/punkpeye/mcp-remote)

<a id="skill-citation-audit"></a>
### `$citation-audit`

- 全局目录：`~/.codex/skills/citation-audit/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `citation-audit` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $citation-audit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Zero-context verification that every bibliographic entry in the paper is real, correctly attributed, and used in a context the cited paper actually supports — catching hallucinated authors, wrong years, fabricated venues, version mismatches, and wrong-context citations. Use when user says "审查引用", "check citations", "citation audit", "verify references", "引用核对", or before submission to ensure bibliography integrity.

</details>

<a id="skill-citation-management"></a>
### `$citation-management`

- 全局目录：`~/.codex/skills/citation-management/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `citation-management` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $citation-management。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Comprehensive citation management for academic research. Search OpenAlex, PubMed, and Google Scholar for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. This skill should be used when you need to find papers, verify citation information, convert DOIs to BibTeX, or ensure reference accuracy in scientific writing.

</details>

<a id="skill-comm-lit-review"></a>
### `$comm-lit-review`

- 全局目录：`~/.codex/skills/comm-lit-review/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `comm-lit-review` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $comm-lit-review。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Communications-domain literature review with Claude-style knowledge-base-first retrieval. Use when the task is about communications, wireless, networking, satellite/NTN, Wi-Fi, cellular, transport protocols, congestion control, routing, scheduling, MAC/PHY, rate adaptation, channel estimation, beamforming, or communication-system research and the user wants papers, related work, a survey, or a landscape summary.

</details>

<a id="skill-deepxiv"></a>
### `$deepxiv`

- 全局目录：`~/.codex/skills/deepxiv/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `deepxiv` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $deepxiv。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search and progressively read open-access academic papers through DeepXiv. Use when the user wants layered paper access, section-level reading, trending papers, or DeepXiv-backed literature retrieval.

</details>

<a id="skill-folklore-variant-evidence"></a>
### `$folklore-variant-evidence`

- 全局目录：`~/.codex/skills/folklore-variant-evidence/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `folklore-variant-evidence` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $folklore-variant-evidence。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Retrieves ClinGen gene-disease validity assertions for a public gene or disease, and reviews source-linked public evidence and literature for one supported GRCh38 germline nuclear SNV or simple indel through Folklore Clinical Variant Interpretation MCP. Used when a scientific agent must branch deterministically on resolved, ambiguous, not-found, invalid, unsupported, or unavailable variant outcomes; chain a resolved public variant into related literature or publication details; or preserve evidence provenance without accepting patient, phenotype, family, segregation, or private case data.

</details>

上游线索：[https://github.com/helena-bioinformatics/folklore-mcp](https://github.com/helena-bioinformatics/folklore-mcp)

<a id="skill-gemini-search"></a>
### `$gemini-search`

- 全局目录：`~/.codex/skills/gemini-search/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `gemini-search` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $gemini-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search research papers via Gemini for broad literature discovery. Use when user says "gemini search", "gemini papers", "search with gemini", or wants AI-powered literature discovery beyond arXiv/Semantic Scholar indexes.

</details>

上游线索：[https://github.com/jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)

<a id="skill-grant-proposal"></a>
### `$grant-proposal`

- 全局目录：`~/.codex/skills/grant-proposal/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `grant-proposal` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $grant-proposal。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Draft a structured grant proposal from research ideas and literature. Supports KAKENHI (Japan), NSF (US), NSFC (China, including 面上/青年/优青/杰青/海外优青/重点), ERC (EU), DFG (Germany), SNSF (Switzerland), ARC (Australia), NWO (Netherlands), and generic formats. Use when user says "write grant", "grant proposal", "申請書", "write KAKENHI", "科研費", "基金申请", "写基金", "NSF proposal", or wants to turn research ideas into a funding application.

</details>

<a id="skill-imaging-data-commons"></a>
### `$imaging-data-commons`

- 全局目录：`~/.codex/skills/imaging-data-commons/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `imaging-data-commons` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $imaging-data-commons。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries and downloads public cancer imaging data from NCI Imaging Data Commons. Supports IDC collection discovery, DICOM access, radiology (CT, MR, PET) and pathology AI datasets, metadata SQL, visualization, licensing, and citations. Uses public metadata and download routes without authentication; optional BigQuery and Google Healthcare routes require Google credentials.

</details>

上游线索：[https://github.com/ImagingDataCommons/imaging-data-commons-skill](https://github.com/ImagingDataCommons/imaging-data-commons-skill)

<a id="skill-literature-review"></a>
### `$literature-review`

- 全局目录：`~/.codex/skills/literature-review/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `literature-review` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $literature-review。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Conducts systematic, scoping, and narrative literature reviews using PubMed, arXiv, bioRxiv, Semantic Scholar, and other appropriate sources. Use for research synthesis, reproducible literature searches, screening, citation checking, or preparing Markdown and PDF reviews. Tracks search coverage, records versus studies, and evidence limitations; supports meta-analysis planning but does not supply a meta-analysis engine.

</details>

<a id="skill-nature-academic-search"></a>
### `$nature-academic-search`

- 全局目录：`~/.codex/skills/nature-academic-search/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：围绕 `nature-academic-search` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $nature-academic-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search literature across sources, verify or manage citations, and build MeSH strategies or citation-impact audits. Use for 文献检索、引文核对、参考文献管理、严格他引 and evidence-backed citer profiles; not for translating a paper or drafting manuscript prose.

</details>

<a id="skill-nature-citation"></a>
### `$nature-citation`

- 全局目录：`~/.codex/skills/nature-citation/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：围绕 `nature-citation` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $nature-citation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Find and verify Nature/CNS-family literature supporting manuscript claims, with claim-to-source mapping and reference-manager export. Use for Nature系列引用、CNS支撑文献、分段补引用 when this journal scope is requested; use broader literature search for unrestricted sources.

</details>

<a id="skill-nature-data"></a>
### `$nature-data`

- 全局目录：`~/.codex/skills/nature-data/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：围绕 `nature-data` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $nature-data。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Draft or audit manuscript Data/Code Availability statements, dataset access routes, repository plans, and FAIR metadata. Use for 数据可用性声明、数据共享、数据仓库选择 and dataset citations; not general data cleaning or statistical analysis.

</details>

<a id="skill-nature-literature-pipeline"></a>
### `$nature-literature-pipeline`

- 全局目录：`~/.codex/skills/nature-literature-pipeline/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：围绕 `nature-literature-pipeline` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $nature-literature-pipeline。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Complete automated literature discovery pipeline: multi-source search → six-dimension scoring → fine reading → formatted delivery → archival. Combines a configurable engine with daily cron-driven application layer. Works with Feishu, Telegram, or any messaging platform.

</details>

<a id="skill-nature-ref-verifier"></a>
### `$nature-ref-verifier`

- 全局目录：`~/.codex/skills/nature-ref-verifier/`
- 所属技能套件：[Nature Research Skills](../技能套件导航.md#suite-nature)
- 推荐总入口：按任务直接调用对应的 $nature-* skill
- 中文理解：对学术文献逐条执行多源交叉验证，逐字段对比作者、标题、年份、卷期、页码， 标记卷年/DOI年冲突、作者顺序异常、页码偏差等问题，输出结构化验证报告。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $nature-ref-verifier。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

对学术文献逐条执行多源交叉验证，逐字段对比作者、标题、年份、卷期、页码， 标记卷年/DOI年冲突、作者顺序异常、页码偏差等问题，输出结构化验证报告。 可批量处理整篇论文/开题报告的参考文献列表，也可单条校验，支持与 Zotero 同步修正。

</details>

<a id="skill-networkx"></a>
### `$networkx`

- 全局目录：`~/.codex/skills/networkx/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `networkx` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $networkx。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Creates, analyzes, and visualizes complex networks and graphs in Python with NetworkX. Use when working with network/graph data structures, computing graph algorithms (shortest paths, centrality, clustering), detecting communities, generating synthetic networks (random, scale-free, small-world), reading/writing graph file formats, or drawing network topologies. Common applications include social, biological, transportation, and citation networks.

</details>

上游线索：[https://github.com/networkx/networkx](https://github.com/networkx/networkx)

<a id="skill-novelty-check"></a>
### `$novelty-check`

- 全局目录：`~/.codex/skills/novelty-check/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `novelty-check` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $novelty-check。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Verify research idea novelty against recent literature. Use when user says "查新", "novelty check", "有没有人做过", "check novelty", or wants to verify a research idea is novel before implementing.

</details>

<a id="skill-openalex"></a>
### `$openalex`

- 全局目录：`~/.codex/skills/openalex/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `openalex` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $openalex。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search academic papers via OpenAlex API for open citation data, institutional affiliations, and funding information. Use when user says "openalex search", "search openalex", "open citation graph", or wants comprehensive academic metadata beyond arXiv/Semantic Scholar.

</details>

<a id="skill-paper-lookup"></a>
### `$paper-lookup`

- 全局目录：`~/.codex/skills/paper-lookup/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `paper-lookup` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-lookup。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Searches 18 scholarly APIs for papers, preprints, citations, open-access full text, repository records, and journal OA status, and returns results with reproducible provenance. Covers PubMed, PMC, Europe PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall, OpenCitations, PubTator3, Zenodo, Figshare, ROR, BioStudies, and DOAJ. Use when searching for papers, citations, DOI/PMID/arXiv lookups, abstracts, full text, open-access PDFs, preprints, citation graphs, author publications, biomedical entity annotations, deposited records (Zenodo, Figshare, BioStudies), institution ROR IDs, or any scholarly literature query. Triggers on mentions of any supported database or requests like "find papers on X", "look up this DOI", "who cites this paper", or "get me the PDF".

</details>

<a id="skill-paper-talk"></a>
### `$paper-talk`

- 全局目录：`~/.codex/skills/paper-talk/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `paper-talk` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paper-talk。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

End-to-end conference talk pipeline: paper → slide outline → Beamer + PPTX → per-page polish → assurance checks (claim / citation / anonymity) → final export and report. Default-good for academic conference talks (NeurIPS / ICML / ICLR / VALSE / 投稿 talks). Trigger phrases: "做 talk", "做 PPT 全流程", "talk pipeline", "end-to-end slides", "做演讲", "conference talk full workflow". Use when the user wants the complete talk artifact, not just a slide deck.

</details>

<a id="skill-paperclip"></a>
### `$paperclip`

- 全局目录：`~/.codex/skills/paperclip/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `paperclip` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $paperclip。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Searches and reads biomedical papers, FDA/PMDA/EMA documents, clinical trials, and protein records with the GXL Paperclip CLI and Python SDK. Supports source-scoped search, full-text grep, metadata SQL, map/reduce extraction, figure analysis, optional repositories and claim verification, and line-pinned citations. Use when a task names GXL paperclip, asks to install or authenticate it, or requests literature retrieval and evidence extraction through Paperclip.

</details>

<a id="skill-peer-review"></a>
### `$peer-review`

- 全局目录：`~/.codex/skills/peer-review/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `peer-review` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $peer-review。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Prepares evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Supports authorized review of scientific manuscripts, protocols, preprints, or research proposals; reporting-guideline selection; claim–evidence checks; methods, statistics, reproducibility, ethics, figure/table, and citation critique; or revision-response planning.

</details>

<a id="skill-prior-art-search"></a>
### `$prior-art-search`

- 全局目录：`~/.codex/skills/prior-art-search/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `prior-art-search` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。 格式与证据整理不等于法律、合规、认证或专利意见。

可复制提示词：

```text
使用 $prior-art-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search patent databases and academic literature for prior art relevant to an invention. Use when user says "现有技术检索", "prior art search", "专利检索", "check patents", or wants to find relevant prior art.

</details>

<a id="skill-pyzotero"></a>
### `$pyzotero`

- 全局目录：`~/.codex/skills/pyzotero/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pyzotero` 的专项能力，主要用于核对引用与来源，并可处理科研文档与结构化内容。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $pyzotero。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Manages Zotero reference libraries using the pyzotero Python client: retrieves, creates, updates, and deletes items, collections, tags, and attachments via the Zotero Web API v3 or local API. Applies when working with Zotero libraries programmatically, managing bibliographic references, exporting citations, searching library contents, uploading PDF attachments, or building research automation workflows that integrate with Zotero.

</details>

<a id="skill-research-lit"></a>
### `$research-lit`

- 全局目录：`~/.codex/skills/research-lit/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `research-lit` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $research-lit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search and analyze research papers, find related work, summarize key ideas. Use when user says "find papers", "related work", "literature review", "what does this paper say", or needs to understand academic papers.

</details>

<a id="skill-research-lookup"></a>
### `$research-lookup`

- 全局目录：`~/.codex/skills/research-lookup/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `research-lookup` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $research-lookup。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Compiles current scholarly evidence for a scientific manuscript or research brief when the user explicitly asks to gather literature, references, background evidence, competing findings, or a manuscript research packet. Uses Parallel Search by default, Parallel Extract for source retrieval, Parallel Research for explicitly deep/exhaustive work, optional explicit Parallel Chat, and optional Perplexity only when requested or allowed as a failure fallback.

</details>

<a id="skill-research-writing-skill"></a>
### `$research-writing-skill`

- 全局目录：`~/.codex/skills/research-writing-skill/`
- 所属技能套件：[Scientific Toolkit 科研计算套件](../技能套件导航.md#suite-scientific-toolkit)
- 推荐总入口：`$scientific-toolkit-skill`
- 中文理解：围绕 `research-writing-skill` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $research-writing-skill。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Chinese-first research paper writing, revision, polishing, section drafting, rebuttal, peer-review response, thesis prose improvement, and manuscript argument planning. Use when the user asks to write or revise论文正文, abstracts, introductions, methods, results, discussion, conclusions, related work, responses to reviewers, LaTeX/Overleaf text, or academic prose. Preserve formulas, English paper titles, terms, citations, and measured results.

</details>

<a id="skill-scientific-toolkit-skill"></a>
### `$scientific-toolkit-skill`

- 全局目录：`~/.codex/skills/scientific-toolkit-skill/`
- 所属技能套件：[Scientific Toolkit 科研计算套件](../技能套件导航.md#suite-scientific-toolkit)
- 推荐总入口：`$scientific-toolkit-skill`
- 中文理解：围绕 `scientific-toolkit-skill` 的专项能力，主要用于核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $scientific-toolkit-skill。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Research computing toolkit for optoelectronic information science and engineering, MATLAB/Octave, Python scientific analysis, signal processing, image processing, statistics, simulation, optimization, publication figures, sensor/time-series data, citation lookup, and common scientific libraries. Use when the user asks for MATLAB code, scientific Python, data analysis, plots, simulations, formulas, statistics, machine learning, optical/physical/materials computation, or reproducible research workflows.

</details>

<a id="skill-semantic-scholar"></a>
### `$semantic-scholar`

- 全局目录：`~/.codex/skills/semantic-scholar/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `semantic-scholar` 的专项能力，主要用于检索和筛选科研文献，并可核对引用与来源。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $semantic-scholar。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search published venue papers (IEEE, ACM, Springer, etc.) via Semantic Scholar API. Complements /arxiv (preprints) with citation counts, venue metadata, and TLDR. Use when user says "search semantic scholar", "find IEEE papers", "find journal papers", "venue papers", "citation search", or wants published literature beyond arXiv preprints.

</details>

<a id="skill-web-debug-search"></a>
### `$web-debug-search`

- 全局目录：`~/.codex/skills/web-debug-search/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `web-debug-search` 的专项能力，主要用于核对引用与来源，并可处理科研文档与结构化内容。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $web-debug-search。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Search GitHub, Stack Exchange, Chinese technical communities, official documentation, and general developer web sources for software errors, compatibility problems, API usage questions, and real-world workarounds. Use for debugging and discovery only; results are not paper-citation evidence.

</details>

<a id="skill-wiki-enrich"></a>
### `$wiki-enrich`

- 全局目录：`~/.codex/skills/wiki-enrich/`
- 所属技能套件：[Auto Claude Code Research in Sleep（ARIS）](../技能套件导航.md#suite-aris)
- 推荐总入口：`$research-pipeline`
- 中文理解：围绕 `wiki-enrich` 的专项能力，主要用于检索和筛选科研文献。
- 适合何时使用：用于找论文、核对出处、整理证据、管理引用和撰写综述。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $wiki-enrich。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fill in the per-paper TODO sections of research-wiki/papers/<slug>.md pages that literature-ingest skills leave as bare scaffolds. Use when user says 'enrich wiki', 'fill paper TODOs', 'wiki body 補完', '把 paper 摘要寫進 wiki', 'research-wiki 自動填', or after a batch ingest that left papers/ as TODO scaffolds.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
