# 地学、空间、天文与环境

处理地理空间、遥感、海洋、天文、物理和工程科学问题。

本页收录 **4** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 一句话理解 |
| --- | --- |
| [`$astropy`](#skill-astropy) | 围绕 `astropy` 的专项能力，主要用于处理天文与天体物理数据。 |
| [`$geopandas`](#skill-geopandas) | 围绕 `geopandas` 的专项能力，主要用于处理空间数据与坐标关系。 |
| [`$lab-hardware-cad`](#skill-lab-hardware-cad) | 围绕 `lab-hardware-cad` 的专项能力，主要用于开展流体或工程仿真分析。 |
| [`$openpiv`](#skill-openpiv) | 围绕 `openpiv` 的专项能力，主要用于开展流体或工程仿真分析。 |

## 详细说明

<a id="skill-astropy"></a>
### `$astropy`

- 全局目录：`~/.codex/skills/astropy/`
- 中文理解：围绕 `astropy` 的专项能力，主要用于处理天文与天体物理数据。
- 适合何时使用：处理地理空间、遥感、海洋、天文、物理和工程科学问题。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $astropy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供坐标系/单位、空间或时间范围、数据来源和目标；要求先核对元数据与物理量纲。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Core Python library for astronomy and astrophysics workflows that need Astropy APIs, including units/quantities, coordinates, FITS I/O, tables, time systems, WCS, and cosmology. Use when implementing or debugging astronomical data analysis code with Astropy.

</details>

上游线索：[https://github.com/astropy/astropy](https://github.com/astropy/astropy)

<a id="skill-geopandas"></a>
### `$geopandas`

- 全局目录：`~/.codex/skills/geopandas/`
- 中文理解：围绕 `geopandas` 的专项能力，主要用于处理空间数据与坐标关系。
- 适合何时使用：处理地理空间、遥感、海洋、天文、物理和工程科学问题。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $geopandas。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供坐标系/单位、空间或时间范围、数据来源和目标；要求先核对元数据与物理量纲。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Guidance and local audit tools for Python workflows that directly use GeoPandas GeoSeries, GeoDataFrame, spatial operations, or vector-data I/O.

</details>

上游线索：[https://github.com/geopandas/geopandas](https://github.com/geopandas/geopandas)

<a id="skill-lab-hardware-cad"></a>
### `$lab-hardware-cad`

- 全局目录：`~/.codex/skills/lab-hardware-cad/`
- 中文理解：围绕 `lab-hardware-cad` 的专项能力，主要用于开展流体或工程仿真分析。
- 适合何时使用：处理地理空间、遥感、海洋、天文、物理和工程科学问题。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $lab-hardware-cad。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供坐标系/单位、空间或时间范围、数据来源和目标；要求先核对元数据与物理量纲。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Designs custom laboratory hardware as parametric build123d models and exports fabrication artifacts as STEP, STL, and DXF files - microfluidic chips and molds, optomechanical mounts and breadboard adapters, cuvette and microplate holders, tube racks, animal-behavior rigs, and 3D-printed instrument fixtures. Use when a research task needs a physical part that must mate with standardized labware, an optical table, a cage system, or a printer, CNC, or laser process.

</details>

<a id="skill-openpiv"></a>
### `$openpiv`

- 全局目录：`~/.codex/skills/openpiv/`
- 中文理解：围绕 `openpiv` 的专项能力，主要用于开展流体或工程仿真分析。
- 适合何时使用：处理地理空间、遥感、海洋、天文、物理和工程科学问题。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $openpiv。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供坐标系/单位、空间或时间范围、数据来源和目标；要求先核对元数据与物理量纲。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs Particle Image Velocimetry (PIV) analysis with OpenPIV. Use when extracting velocity fields from PIV image pairs, analyzing fluid dynamics or flow visualization experiments, cross-correlating interrogation windows, validating and replacing spurious PIV vectors, or computing vorticity, strain rate, and turbulence statistics from measured velocity fields.

</details>

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
