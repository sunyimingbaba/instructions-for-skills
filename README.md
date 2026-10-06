# 全局科研 Skills 中文使用说明

这里整理了当前 Codex 全局安装目录中的 **428 个科研及科研支撑 skills**，并把每个 skill 的用途、调用方法、注意事项和提示词模板写成中文。

## 从这里开始

- [按研究任务选择 Skill](docs/全局科研Skills使用指南.md)
- [查看全部 Skills 字母索引](docs/技能总索引.md)
- [查看生成规则与维护方法](docs/维护与更新.md)

最快的调用方式：

```text
使用 $技能名。我的目标是：<具体任务>。
材料在：<文件或目录路径>。
请输出：<格式>；不要编造数据、引用或运行结果。
```

## 常见任务入口

| 我想做什么 | 可以先看这些 Skills |
| --- | --- |
| 查论文与核对 DOI | `paper-lookup / literature-review / arxiv / nature-academic-search` |
| 写论文与审稿 | `scientific-writing / nature-writing / ml-paper-writing / peer-review` |
| 做统计与画图 | `statistical-analysis / scientific-visualization / matplotlib / seaborn` |
| 做生物信息分析 | `scanpy / biopython / bulk-rnaseq / pathway-enrichment` |
| 训练与评测 LLM | `transformers / axolotl / deepspeed / vllm / lm-evaluation-harness` |
| 参加数学建模竞赛 | `1start-mathmodel / bzd-modeling-workflow / hwb-modeling-workflow` |

## 分类

| 分类 | Skills 数量 |
| --- | ---: |
| [科研工作流与自治实验](docs/categories/workflow.md) | 22 |
| [文献检索、证据与引用](docs/categories/literature.md) | 33 |
| [论文写作、审稿与出版](docs/categories/writing.md) | 36 |
| [数学建模竞赛](docs/categories/math-modeling.md) | 40 |
| [统计、机器学习与时序分析](docs/categories/statistics-ml.md) | 24 |
| [科学可视化、文档与演示](docs/categories/visualization.md) | 27 |
| [生物信息、组学与遗传学](docs/categories/bioinformatics.md) | 35 |
| [化学、药物、材料与分子模拟](docs/categories/chemistry.md) | 19 |
| [医学、临床与实验室规范](docs/categories/clinical-lab.md) | 28 |
| [地学、空间、天文与环境](docs/categories/geo-physical.md) | 4 |
| [AI/LLM 模型训练、压缩与推理](docs/categories/llm-training.md) | 60 |
| [智能体、RAG、安全与评测](docs/categories/agents-rag.md) | 33 |
| [数据工程、计算与云平台](docs/categories/data-compute.md) | 25 |
| [实验室平台、ELN 与科研硬件](docs/categories/lab-platform.md) | 5 |
| [通用科研工具与质量保障](docs/categories/general.md) | 37 |

## 范围说明

本仓库以 `~/.codex/skills/*/SKILL.md` 为扫描范围，排除 Codex 的 `.system` 内置目录；其余直接安装在全局目录中的 skills 全部收录。某些技能更偏工具、基础设施或质量保障，也一并保留，因为它们常是科研流程的一部分。

当前快照日期：**2026-10-06**。技能升级后，可运行仓库内的生成脚本刷新文档。
