# 全局科研 Skills 使用指南

更新日期：2026-10-06。本指南扫描了本机全局目录 `~/.codex/skills`，共收录 **428** 个科研及科研支撑 skills。

## 最简单的使用方法

在新建的 Codex 对话里写出 `$技能名`，再交代四件事：你要解决什么、材料在哪里、希望得到什么格式、哪些内容不能猜。

```text
使用 $paper-lookup。我的目标是核对这批论文的标题、年份、会议和 DOI。
材料在：<文件路径>。输出 Markdown 表格并附原始来源链接。
无法核实的字段标为“未核实”，不要根据标题猜测。
```

如果不知道技能名，先从下面的分类进入。一个任务通常只需一个主 skill；需要跨阶段工作时，再按“检索 → 分析 → 写作 → 审核”的顺序组合。

## 先找大套件还是直接找小 Skill

- 任务跨度很大，例如“从找选题一直做到论文”，先用大套件的总入口。
- 任务很具体，例如“核对 DOI”或“分析单细胞数据”，直接调用对应小 skill。
- 不清楚小 skill 属于哪里时，打开[技能套件与总入口导航](技能套件导航.md)。

| 主要技能套件 | 数量 | 推荐总入口 |
| --- | ---: | --- |
| [Scientific Agent Skills（K-Dense）](技能套件导航.md#suite-scientific-agent-skills) | 177 | 按任务直接调用对应小 skill |
| [Auto Claude Code Research in Sleep（ARIS）](技能套件导航.md#suite-aris) | 82 | `$research-pipeline` |
| [AI Research SKILLs（Orchestra Research）](技能套件导航.md#suite-orchestra) | 96 | `$autoresearch` |
| [ARS-Codex 学术研究套件](技能套件导航.md#suite-academic-research-suite) | 1 | `$academic-research-suite` |
| [Codex Autoresearch](技能套件导航.md#suite-codex-autoresearch) | 1 | `$codex-autoresearch` |
| [Nature Research Skills](技能套件导航.md#suite-nature) | 20 | 按任务直接调用对应的 $nature-* skill |
| [BZD 数学建模 Skills](技能套件导航.md#suite-bzd) | 16 | `$bzd-modeling-workflow` |
| [HWB 华为杯数学建模 Skills](技能套件导航.md#suite-hwb) | 16 | `$hwb-modeling-workflow` |
| [MathModel 数学建模工作流](技能套件导航.md#suite-mathmodel) | 8 | `$1start-mathmodel` |
| [Scientific Toolkit 科研计算套件](技能套件导航.md#suite-scientific-toolkit) | 3 | `$scientific-toolkit-skill` |
| [独立或暂未归入大型套件](技能套件导航.md#suite-standalone) | 8 | 直接调用当前小 skill |

## 分类导航

| 分类 | 数量 | 适合解决的问题 |
| --- | ---: | --- |
| [科研工作流与自治实验](categories/workflow.md) | 22 | 把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。 |
| [文献检索、证据与引用](categories/literature.md) | 33 | 用于找论文、核对出处、整理证据、管理引用和撰写综述。 |
| [论文写作、审稿与出版](categories/writing.md) | 36 | 帮助组织论文、改写段落、审稿、回复意见、制作投稿材料。 |
| [数学建模竞赛](categories/math-modeling.md) | 40 | 覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。 |
| [统计、机器学习与时序分析](categories/statistics-ml.md) | 24 | 用于统计建模、预测、分类、聚类、因果或不确定性分析。 |
| [科学可视化、文档与演示](categories/visualization.md) | 27 | 生成或检查论文图表、流程图、海报、幻灯片和技术文档。 |
| [生物信息、组学与遗传学](categories/bioinformatics.md) | 35 | 处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。 |
| [化学、药物、材料与分子模拟](categories/chemistry.md) | 19 | 用于化学信息学、药物发现、质谱、结构、材料和分子模拟。 |
| [医学、临床与实验室规范](categories/clinical-lab.md) | 28 | 支持临床研究、实验室方法验证、标准体系和医学数据工作流。 |
| [地学、空间、天文与环境](categories/geo-physical.md) | 4 | 处理地理空间、遥感、海洋、天文、物理和工程科学问题。 |
| [AI/LLM 模型训练、压缩与推理](categories/llm-training.md) | 60 | 覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。 |
| [智能体、RAG、安全与评测](categories/agents-rag.md) | 33 | 用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。 |
| [数据工程、计算与云平台](categories/data-compute.md) | 25 | 处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。 |
| [实验室平台、ELN 与科研硬件](categories/lab-platform.md) | 5 | 连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。 |
| [通用科研工具与质量保障](categories/general.md) | 37 | 无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。 |

## 选择技能的实用顺序

1. 先按任务类型选分类，不要仅凭软件名字选择。
2. 打开分类页，看“一句话理解”和原始说明，确认能力边界。
3. 复制提示词模板，替换目标、文件路径、数据和约束。
4. 涉及联网、API、云平台、实验提交、长时间训练或外部写入时，先让 Codex做只读检查和影响说明。
5. 对引用、实验数字、医学信息和合规结论，始终回到原始证据复核。

## 常见组合

| 研究阶段 | 常见组合 |
| --- | --- |
| 从选题到文献综述 | 文献检索类 → 研究创意/假设类 → 综述写作类 |
| 从数据到论文结果 | 学科数据处理类 → 统计/机器学习类 → 可视化类 → 论文写作类 |
| 从模型训练到报告 | LLM 训练类 → 实验监控/结果分析类 → 评测类 → 论文写作类 |
| 数学建模竞赛 | 工作流入口 → 赛题分析 → 编程求解 → 图表/流程图 → 写作 → 验收 |
| 投稿前检查 | 引用核对 → 统计审计 → 审稿/反方论证 → 格式检查 |

## 重要边界

- skill 是工作说明，不保证 Python 包、模型、数据库权限、API 密钥或 GPU 已准备好。
- 同名或相近 skills 可能来自不同项目。以本指南记录的全局目录和原始说明为准。
- `_references` 是共享知识库，通常由其他数学建模 skills 自动读取，不需要手动调用。
- 新安装或升级 skill 后，重新运行 `python3 scripts/build_skill_docs.py` 可刷新本仓库。

完整字母索引见：[技能总索引](技能总索引.md)。
