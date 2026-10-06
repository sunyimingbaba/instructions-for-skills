# 实验室平台、ELN 与科研硬件

连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。

本页收录 **5** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 一句话理解 |
| --- | --- |
| [`$benchling-integration`](#skill-benchling-integration) | 围绕 `benchling-integration` 的专项能力，主要用于组织可复现的科研流程，并可管理实验记录、样品或实验室数据。 |
| [`$labarchive-integration`](#skill-labarchive-integration) | 围绕 `labarchive-integration` 的专项能力，主要用于组织可复现的科研流程，并可管理实验记录、样品或实验室数据。 |
| [`$omero-integration`](#skill-omero-integration) | 围绕 `omero-integration` 的专项能力，主要用于组织可复现的科研流程，并可管理实验记录、样品或实验室数据。 |
| [`$opentrons-integration`](#skill-opentrons-integration) | 围绕 `opentrons-integration` 的专项能力，主要用于组织可复现的科研流程，并可设计或自动化实验室操作。 |
| [`$protocolsio-integration`](#skill-protocolsio-integration) | 这是一个面向“实验室平台、ELN 与科研硬件”的专项技能，用于处理 `protocolsio-integration` 相关任务。 |

## 详细说明

<a id="skill-benchling-integration"></a>
### `$benchling-integration`

- 全局目录：`~/.codex/skills/benchling-integration/`
- 中文理解：围绕 `benchling-integration` 的专项能力，主要用于组织可复现的科研流程，并可管理实验记录、样品或实验室数据。
- 适合何时使用：连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $benchling-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明平台账户、对象标识、权限和预期操作；先做只读检查，提交/下单前列出影响。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Benchling Python SDK and REST API integration for registry entities, inventory, ELN entries, workflows, Benchling Apps, and Data Warehouse queries. Use when automating lab data with benchling-sdk or the v2 API.

</details>

<a id="skill-labarchive-integration"></a>
### `$labarchive-integration`

- 全局目录：`~/.codex/skills/labarchive-integration/`
- 中文理解：围绕 `labarchive-integration` 的专项能力，主要用于组织可复现的科研流程，并可管理实验记录、样品或实验室数据。
- 适合何时使用：连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $labarchive-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明平台账户、对象标识、权限和预期操作；先做只读检查，提交/下单前列出影响。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Integrates with the official LabArchives ELN REST-like API and Inventory API v1. Supports regional endpoint selection, signed-request construction, user authorization and UID flows, local LA container validation, and verified LabArchives integration workflows.

</details>

<a id="skill-omero-integration"></a>
### `$omero-integration`

- 全局目录：`~/.codex/skills/omero-integration/`
- 中文理解：围绕 `omero-integration` 的专项能力，主要用于组织可复现的科研流程，并可管理实验记录、样品或实验室数据。
- 适合何时使用：连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $omero-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明平台账户、对象标识、权限和预期操作；先做只读检查，提交/下单前列出影响。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Inspects and automates microscopy data workflows against OMERO.server with omero-py, BlitzGateway, OMERO CLI, tables, annotations, ROIs, rendering, and documented OMERO.web APIs. Use this skill for scoped OMERO inventory, metadata export, import/export planning, or reviewed write workflows.

</details>

<a id="skill-opentrons-integration"></a>
### `$opentrons-integration`

- 全局目录：`~/.codex/skills/opentrons-integration/`
- 中文理解：围绕 `opentrons-integration` 的专项能力，主要用于组织可复现的科研流程，并可设计或自动化实验室操作。
- 适合何时使用：连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $opentrons-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明平台账户、对象标识、权限和预期操作；先做只读检查，提交/下单前列出影响。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Authors, reviews, migrates, simulates, and troubleshoots official Opentrons Python Protocol API v2 protocols for Flex and OT-2 robots. Use for robot-specific liquid handling, deck and labware setup, pipettes, modules, runtime parameters, liquid classes, and Opentrons App analysis. Use pylabrobot instead when one workflow must support multiple robot vendors.

</details>

<a id="skill-protocolsio-integration"></a>
### `$protocolsio-integration`

- 全局目录：`~/.codex/skills/protocolsio-integration/`
- 中文理解：这是一个面向“实验室平台、ELN 与科研硬件”的专项技能，用于处理 `protocolsio-integration` 相关任务。
- 适合何时使用：连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $protocolsio-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明平台账户、对象标识、权限和预期操作；先做只读检查，提交/下单前列出影响。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reads, validates, and safely exports protocols.io data with current official REST/MCP contracts, or creates non-executing mutation plans. The bundled client makes bounded official-host GET requests only with explicit --execute. Use only for tasks explicitly targeting protocols.io or an exact protocols.io protocol version.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
