# Codex 科研技能使用说明

这个仓库记录我在 Codex 中使用的三套科研相关技能。先看下表选工具，再打开[完整中文使用指南](docs/三个科研技能使用指南.md)复制对应提示词。

| 技能 | 主要用途 | 在 Codex 中调用 |
| --- | --- | --- |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 文献查找、科研写作、统计、绘图、地理空间等专项任务；它是多个独立技能的合集 | 例如 `$paper-lookup`、`$literature-review`、`$scientific-writing` |
| [ARS-Codex](https://github.com/Imbad0202/academic-research-skills-codex) | 从研究问题、文献综述、论文写作到审稿和实验规划的分阶段工作流 | `$academic-research-suite` |
| [Codex Autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) | 针对可量化指标，反复修改代码、测量结果并保留改进 | `$codex-autoresearch` |

## 最快上手

在新建的 Codex 对话中，直接输入技能名和具体任务。例如：

```text
使用 $paper-lookup，查找 2024–2026 年遥感图文检索论文；核实发表会议、年份和 DOI，附原始链接。
```

```text
使用 $academic-research-suite，按 academic-paper 工作流帮助我写实验部分。
我会提供数据集、评价指标、对比表和消融结果。请用简体中文，缺失的数值先标出，不要补造。
```

```text
使用 $codex-autoresearch。先检查仓库和现有评估脚本，给我一份可量化的实验配置；
在确认目标、修改范围、测量命令和运行模式之前不要启动实验。
```

使用说明以[完整指南](docs/三个科研技能使用指南.md)为准。技能文件本身不等于所需 Python 包、模型、数据和 API 凭据都已安装。新装技能后，建议新开 Codex 对话并输入 `$` 检查是否能选到技能。

这份指南记录的是 2026-10-06 的本机安装状态；以后升级技能时，应以各项目的官方说明和本机实际版本为准。
