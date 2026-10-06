# 化学、药物、材料与分子模拟

用于化学信息学、药物发现、质谱、结构、材料和分子模拟。

本页收录 **19** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 所属技能套件 | 一句话理解 |
| --- | --- | --- |
| [`$cantera`](#skill-cantera) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `cantera` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$datamol`](#skill-datamol) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `datamol` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$deepchem`](#skill-deepchem) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `deepchem` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$diffdock`](#skill-diffdock) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `diffdock` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$geomaster`](#skill-geomaster) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `geomaster` 相关任务。 |
| [`$marine-carbonate-chemistry`](#skill-marine-carbonate-chemistry) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `marine-carbonate-chemistry` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$matchms`](#skill-matchms) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `matchms` 的专项能力，主要用于处理质谱、蛋白组或代谢组数据。 |
| [`$medchem`](#skill-medchem) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `medchem` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$molecular-dynamics`](#skill-molecular-dynamics) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `molecular-dynamics` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$molfeat`](#skill-molfeat) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `molfeat` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$nmrglue`](#skill-nmrglue) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `nmrglue` 相关任务。 |
| [`$office-academic-skill`](#skill-office-academic-skill) | [Scientific Toolkit 科研计算套件](../技能套件导航.md#suite-scientific-toolkit) | 围绕 `office-academic-skill` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$pybamm`](#skill-pybamm) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pybamm` 的专项能力，主要用于处理化学、药物或材料问题，并可规划、运行或复盘实验。 |
| [`$pycalphad`](#skill-pycalphad) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `pycalphad` 相关任务。 |
| [`$pymatgen`](#skill-pymatgen) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pymatgen` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$pyopenms`](#skill-pyopenms) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `pyopenms` 的专项能力，主要用于处理质谱、蛋白组或代谢组数据，并可处理化学、药物或材料问题。 |
| [`$rdkit`](#skill-rdkit) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `rdkit` 相关任务。 |
| [`$rowan`](#skill-rowan) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `rowan` 的专项能力，主要用于处理化学、药物或材料问题。 |
| [`$tellurium`](#skill-tellurium) | [Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills) | 围绕 `tellurium` 的专项能力，主要用于进行代谢网络与通量分析，并可处理化学、药物或材料问题。 |

## 详细说明

<a id="skill-cantera"></a>
### `$cantera`

- 全局目录：`~/.codex/skills/cantera/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `cantera` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $cantera。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Runs Cantera homogeneous chemical reactors and evaluates ignition delay with mechanism provenance, conservation checks, and numerical refinement. Use for combustion kinetics, closed adiabatic ideal-gas constant-volume or constant-pressure ignition, temperature histories, or mechanism-specific ignition-delay comparisons.

</details>

<a id="skill-datamol"></a>
### `$datamol`

- 全局目录：`~/.codex/skills/datamol/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `datamol` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $datamol。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Pythonic wrapper around RDKit with simplified interface and sensible defaults. Preferred for standard drug discovery including SMILES parsing, standardization, descriptors, fingerprints, clustering, 3D conformers, parallel processing. Returns native rdkit.Chem.Mol objects. For advanced control or custom parameters, use rdkit directly.

</details>

上游线索：[https://github.com/datamol-io/datamol](https://github.com/datamol-io/datamol)

<a id="skill-deepchem"></a>
### `$deepchem`

- 全局目录：`~/.codex/skills/deepchem/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `deepchem` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $deepchem。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds molecular property prediction and MoleculeNet workflows with DeepChem, including SMILES featurization, scaffold or grouped holdouts, masked labels, graph models and explicit pretrained encoder transfer. Used for ADMET, toxicity, solubility and chemistry ML when DeepChem data/model contracts and scientific validation are needed.

</details>

<a id="skill-diffdock"></a>
### `$diffdock`

- 全局目录：`~/.codex/skills/diffdock/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `diffdock` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $diffdock。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Predicts protein-small-molecule binding poses with DiffDock and DiffDock-L from PDB or sequence plus SMILES/SDF/MOL2. Covers batch docking, pose triage, confidence interpretation, and validation. Use for molecular docking and virtual-screening pose generation, not binding-affinity prediction.

</details>

上游线索：[https://github.com/gcorso/DiffDock](https://github.com/gcorso/DiffDock)

<a id="skill-geomaster"></a>
### `$geomaster`

- 全局目录：`~/.codex/skills/geomaster/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `geomaster` 相关任务。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $geomaster。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports geospatial research workflows for remote sensing, vector and raster GIS, spatial statistics, terrain and network analysis, and machine learning for Earth observation. Use when processing satellite imagery, aligning coordinate systems and raster grids, accessing STAC catalogs, analyzing geospatial time series, or implementing scientific GIS workflows in Python, R, Julia, JavaScript, C++, Java, Go, or Rust.

</details>

<a id="skill-marine-carbonate-chemistry"></a>
### `$marine-carbonate-chemistry`

- 全局目录：`~/.codex/skills/marine-carbonate-chemistry/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `marine-carbonate-chemistry` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $marine-carbonate-chemistry。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Solves seawater carbonate chemistry with PyCO2SYS for chemical oceanography, ocean acidification, and marine carbon-cycle research. Use for paired total alkalinity, dissolved inorganic carbon, pH, or seawater pCO2/fCO2 measurements; carbonate speciation; aragonite and calcite saturation; Revelle factors; lab-to-in-situ temperature and pressure corrections; and measurement uncertainty propagation. Applies to carbonate-system calculations, not general aqueous speciation or air-sea gas-flux estimation.

</details>

上游线索：[https://github.com/mvdh7/PyCO2SYS](https://github.com/mvdh7/PyCO2SYS)

<a id="skill-matchms"></a>
### `$matchms`

- 全局目录：`~/.codex/skills/matchms/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `matchms` 的专项能力，主要用于处理质谱、蛋白组或代谢组数据。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $matchms。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Processes, cleans, compares, and searches tandem mass spectra with matchms. Use for MS/MS file I/O, metadata harmonization, peak filtering, spectral similarity, library matching, score matrices, and molecular-similarity networks. Use pyopenms instead for LC-MS feature detection or proteomics pipelines.

</details>

<a id="skill-medchem"></a>
### `$medchem`

- 全局目录：`~/.codex/skills/medchem/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `medchem` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $medchem。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Applies medicinal chemistry filters for compound triage, using drug-likeness rules (Lipinski, Veber, CNS), structural alert catalogs (PAINS, NIBR, ChEMBL), complexity metrics, and the medchem query language for library filtering.

</details>

上游线索：[https://github.com/datamol-io/medchem](https://github.com/datamol-io/medchem)

<a id="skill-molecular-dynamics"></a>
### `$molecular-dynamics`

- 全局目录：`~/.codex/skills/molecular-dynamics/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `molecular-dynamics` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $molecular-dynamics。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Runs and analyzes molecular dynamics simulations with OpenMM and MDAnalysis. Sets up protein/small molecule systems, defines force fields, runs energy minimization and production MD, and analyzes trajectories (RMSD, RMSF, contact maps, free energy surfaces). For structural biology, drug binding, and biophysics.

</details>

<a id="skill-molfeat"></a>
### `$molfeat`

- 全局目录：`~/.codex/skills/molfeat/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `molfeat` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $molfeat。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Featurizes small molecules with Molfeat for QSAR/QSPR, chemical similarity, virtual screening, and molecular ML. Covers ECFP/MACCS fingerprints, RDKit descriptors, pharmacophores, pretrained embeddings, configuration persistence, and molecule-to-label alignment.

</details>

上游线索：[https://github.com/datamol-io/molfeat](https://github.com/datamol-io/molfeat)

<a id="skill-nmrglue"></a>
### `$nmrglue`

- 全局目录：`~/.codex/skills/nmrglue/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `nmrglue` 相关任务。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $nmrglue。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Processes calibrated one-dimensional complex NMR free-induction decays with nmrglue into phased spectra, peak candidates, and signed integration regions. Use for raw 1D NMR processing, ppm-axis verification, apodization, Fourier transformation, manual phasing, baseline correction, or reproducible spectral integration.

</details>

上游线索：[https://github.com/jjhelmus/nmrglue](https://github.com/jjhelmus/nmrglue)

<a id="skill-office-academic-skill"></a>
### `$office-academic-skill`

- 全局目录：`~/.codex/skills/office-academic-skill/`
- 所属技能套件：[Scientific Toolkit 科研计算套件](../技能套件导航.md#suite-scientific-toolkit)
- 推荐总入口：`$scientific-toolkit-skill`
- 中文理解：围绕 `office-academic-skill` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $office-academic-skill。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Chinese-first academic Word and PowerPoint workflow for paper reading reports, thesis or group-meeting PPTs, editable DOCX/PPTX generation, Office file inspection, template matching, speaker notes, and layout quality checks. Use when the user asks to read papers into Word reports, create or polish PPT/PPTX, convert paper/thesis materials into slides, edit DOCX/PPTX, inspect Office files, or produce Chinese academic presentation/report deliverables. Preserve English paper titles, formulas, variable names, software commands, and references.

</details>

<a id="skill-pybamm"></a>
### `$pybamm`

- 全局目录：`~/.codex/skills/pybamm/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pybamm` 的专项能力，主要用于处理化学、药物或材料问题，并可规划、运行或复盘实验。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pybamm。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Simulates lithium-ion battery charge, discharge and rest experiments with PyBaMM, records parameter-set provenance, checks mesh and solver sensitivity, and compares predicted voltage curves with measured cycling data. Use for SPM or DFN electrochemical battery modeling, C-rate protocols, voltage cutoffs, parameter studies and numerical validation of battery simulations.

</details>

上游线索：[https://github.com/pybamm-team/PyBaMM](https://github.com/pybamm-team/PyBaMM)

<a id="skill-pycalphad"></a>
### `$pycalphad`

- 全局目录：`~/.codex/skills/pycalphad/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `pycalphad` 相关任务。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pycalphad。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Computes finite-temperature CALPHAD equilibria, phase fractions, and phase compositions from thermodynamic TDB databases using pycalphad. Use for alloy phase stability, equilibrium temperature sweeps, tie lines, lever-rule checks, or reproducible phase-fraction calculations with explicit components and mole-fraction conditions.

</details>

上游线索：[https://github.com/pycalphad/pycalphad](https://github.com/pycalphad/pycalphad)

<a id="skill-pymatgen"></a>
### `$pymatgen`

- 全局目录：`~/.codex/skills/pymatgen/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pymatgen` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pymatgen。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes, validates, converts, and transforms materials structures and computed materials data with pymatgen. Use for local phase diagrams, symmetry sensitivity, electronic-structure I/O, and bounded Materials Project queries.

</details>

上游线索：[https://github.com/computron/pymatgen_tutorials](https://github.com/computron/pymatgen_tutorials)

<a id="skill-pyopenms"></a>
### `$pyopenms`

- 全局目录：`~/.codex/skills/pyopenms/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `pyopenms` 的专项能力，主要用于处理质谱、蛋白组或代谢组数据，并可处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pyopenms。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Processes mass spectrometry data with pyOpenMS. Supports proteomics and metabolomics workflows—feature detection, peptide/protein identification, label-free quantification, adduct/accurate-mass annotation, and complex LC-MS/MS pipelines. Supports extensive file formats and algorithms. For simple spectral comparison and small-molecule library matching use matchms.

</details>

上游线索：[https://github.com/OpenMS/OpenMS](https://github.com/OpenMS/OpenMS)

<a id="skill-rdkit"></a>
### `$rdkit`

- 全局目录：`~/.codex/skills/rdkit/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：这是一个面向“化学、药物、材料与分子模拟”的专项技能，用于处理 `rdkit` 相关任务。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $rdkit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Cheminformatics toolkit for fine-grained molecular control. SMILES/SDF parsing, descriptors (MW, LogP, TPSA), fingerprints, substructure search, 2D/3D generation, similarity, reactions. For standard workflows with simpler interface, use datamol (wrapper around RDKit). Use rdkit for advanced control, custom sanitization, specialized algorithms.

</details>

<a id="skill-rowan"></a>
### `$rowan`

- 全局目录：`~/.codex/skills/rowan/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `rowan` 的专项能力，主要用于处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $rowan。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Rowan is a cloud-native molecular modeling and medicinal-chemistry workflow platform with a Python API. Use for pKa and macropKa prediction, conformer and tautomer ensembles, docking and analogue docking, protein-ligand cofolding, MSA generation, molecular dynamics, permeability, descriptor workflows, and related small-molecule or protein modeling tasks. Ideal for programmatic batch screening, multi-step chemistry pipelines, and workflows that would otherwise require maintaining local HPC/GPU infrastructure.

</details>

<a id="skill-tellurium"></a>
### `$tellurium`

- 全局目录：`~/.codex/skills/tellurium/`
- 所属技能套件：[Scientific Agent Skills（K-Dense）](../技能套件导航.md#suite-scientific-agent-skills)
- 推荐总入口：按任务直接调用对应小 skill
- 中文理解：围绕 `tellurium` 的专项能力，主要用于进行代谢网络与通量分析，并可处理化学、药物或材料问题。
- 适合何时使用：用于化学信息学、药物发现、质谱、结构、材料和分子模拟。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $tellurium。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Simulates biochemical kinetic models from SBML or Antimony with Tellurium and libRoadRunner, checks model units, compares deterministic parameter perturbations, and exports and replays SBML plus SED-ML COMBINE archives. Use for reaction-network time courses, kinetic parameters, concentration dynamics and reproducible simulation experiments; steady-state constraint-based metabolic flux analysis belongs to cobrapy.

</details>

上游线索：[https://github.com/sys-bio/roadrunner](https://github.com/sys-bio/roadrunner)

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
