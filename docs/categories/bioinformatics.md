# 生物信息、组学与遗传学

处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。

本页收录 **35** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 一句话理解 |
| --- | --- |
| [`$anndata`](#skill-anndata) | 围绕 `anndata` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$arboreto`](#skill-arboreto) | 围绕 `arboreto` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$biopython`](#skill-biopython) | 围绕 `biopython` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。 |
| [`$bioservices`](#skill-bioservices) | 围绕 `bioservices` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$bulk-rnaseq`](#skill-bulk-rnaseq) | 围绕 `bulk-rnaseq` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$cobrapy`](#skill-cobrapy) | 围绕 `cobrapy` 的专项能力，主要用于进行代谢网络与通量分析。 |
| [`$deepspot-m`](#skill-deepspot-m) | 围绕 `deepspot-m` 的专项能力，主要用于处理生物信息与组学数据，并可处理科研或医学影像。 |
| [`$deeptools`](#skill-deeptools) | 围绕 `deeptools` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$depmap`](#skill-depmap) | 这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `depmap` 相关任务。 |
| [`$dnanexus-integration`](#skill-dnanexus-integration) | 围绕 `dnanexus-integration` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$esm`](#skill-esm) | 围绕 `esm` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$etetoolkit`](#skill-etetoolkit) | 围绕 `etetoolkit` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。 |
| [`$geniml`](#skill-geniml) | 围绕 `geniml` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$genomic-intelligence`](#skill-genomic-intelligence) | 围绕 `genomic-intelligence` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$gget`](#skill-gget) | 围绕 `gget` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$gtars`](#skill-gtars) | 围绕 `gtars` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$hugging-science`](#skill-hugging-science) | 围绕 `hugging-science` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$lamindb`](#skill-lamindb) | 这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `lamindb` 相关任务。 |
| [`$latchbio-integration`](#skill-latchbio-integration) | 这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `latchbio-integration` 相关任务。 |
| [`$mageck`](#skill-mageck) | 这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `mageck` 相关任务。 |
| [`$pathogen-variant-surveillance`](#skill-pathogen-variant-surveillance) | 围绕 `pathogen-variant-surveillance` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。 |
| [`$pathway-enrichment`](#skill-pathway-enrichment) | 围绕 `pathway-enrichment` 的专项能力，主要用于处理质谱、蛋白组或代谢组数据。 |
| [`$phylogenetics`](#skill-phylogenetics) | 围绕 `phylogenetics` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。 |
| [`$polars-bio`](#skill-polars-bio) | 围绕 `polars-bio` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。 |
| [`$primekg`](#skill-primekg) | 这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `primekg` 相关任务。 |
| [`$pydeseq2`](#skill-pydeseq2) | 围绕 `pydeseq2` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$pysam`](#skill-pysam) | 围绕 `pysam` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。 |
| [`$scanpy`](#skill-scanpy) | 围绕 `scanpy` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$scikit-bio`](#skill-scikit-bio) | 围绕 `scikit-bio` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。 |
| [`$scvelo`](#skill-scvelo) | 围绕 `scvelo` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$scvi-tools`](#skill-scvi-tools) | 围绕 `scvi-tools` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$tamarind`](#skill-tamarind) | 围绕 `tamarind` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$tiledbvcf`](#skill-tiledbvcf) | 围绕 `tiledbvcf` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。 |
| [`$torchdrug`](#skill-torchdrug) | 围绕 `torchdrug` 的专项能力，主要用于处理生物信息与组学数据。 |
| [`$waypoint-bio`](#skill-waypoint-bio) | 这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `waypoint-bio` 相关任务。 |

## 详细说明

<a id="skill-anndata"></a>
### `$anndata`

- 全局目录：`~/.codex/skills/anndata/`
- 中文理解：围绕 `anndata` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $anndata。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Handles annotated matrices in single-cell analysis, .h5ad and Zarr files, and integration with the scverse ecosystem. This is the data format skill—for analysis workflows use scanpy; for probabilistic models use scvi-tools; for population-scale queries use cellxgene-census.

</details>

上游线索：[https://github.com/scverse/anndata](https://github.com/scverse/anndata)

<a id="skill-arboreto"></a>
### `$arboreto`

- 全局目录：`~/.codex/skills/arboreto/`
- 中文理解：围绕 `arboreto` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $arboreto。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Infers candidate gene regulatory networks from bulk or single-cell expression data using AertsLab Arboreto GRNBoost2 and GENIE3. Use for transcription factor-target association ranking, compatible Dask execution, sparse expression inputs, and network stability checks.

</details>

上游线索：[https://github.com/aertslab/arboreto](https://github.com/aertslab/arboreto)

<a id="skill-biopython"></a>
### `$biopython`

- 全局目录：`~/.codex/skills/biopython/`
- 中文理解：围绕 `biopython` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $biopython。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides Biopython workflows for sequence manipulation, file parsing (FASTA/GenBank/PDB), phylogenetics, and programmatic NCBI/PubMed access (Bio.Entrez). Supports batch processing, custom molecular-biology pipelines, BLAST automation, structure analysis, and motif analysis.

</details>

上游线索：[https://github.com/biopython/biopython](https://github.com/biopython/biopython)

<a id="skill-bioservices"></a>
### `$bioservices`

- 全局目录：`~/.codex/skills/bioservices/`
- 中文理解：围绕 `bioservices` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bioservices。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides a Python interface to bioinformatics services including UniProt, KEGG, ChEMBL, Reactome, QuickGO, and UniChem. Used for cross-database protein annotation, pathway retrieval, chemical identifier mapping, and integrated biological data workflows with BioServices.

</details>

<a id="skill-bulk-rnaseq"></a>
### `$bulk-rnaseq`

- 全局目录：`~/.codex/skills/bulk-rnaseq/`
- 中文理解：围绕 `bulk-rnaseq` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $bulk-rnaseq。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Prepares bulk RNA-seq FASTQ, Salmon, STAR or featureCounts output for gene-level differential expression. Covers nf-core/rnaseq and standalone quantification, biological replication, strandedness, reference provenance, validated count assembly and a PyDESeq2 handoff. Use for FASTQ-to-counts analysis, nf-core/rnaseq configuration, STAR/Salmon quantification, or building a counts matrix for DESeq2. For single-cell data use scanpy; for statistical fitting alone use pydeseq2.

</details>

上游线索：[https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)

<a id="skill-cobrapy"></a>
### `$cobrapy`

- 全局目录：`~/.codex/skills/cobrapy/`
- 中文理解：围绕 `cobrapy` 的专项能力，主要用于进行代谢网络与通量分析。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $cobrapy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs constraint-based metabolic modeling with COBRApy, including FBA, pFBA, FVA, gene knockouts, flux sampling, growth media, production envelopes, gap filling, and SBML model validation for systems biology and metabolic engineering.

</details>

上游线索：[https://github.com/opencobra/cobrapy](https://github.com/opencobra/cobrapy)

<a id="skill-deepspot-m"></a>
### `$deepspot-m`

- 全局目录：`~/.codex/skills/deepspot-m/`
- 中文理解：围绕 `deepspot-m` 的专项能力，主要用于处理生物信息与组学数据，并可处理科研或医学影像。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $deepspot-m。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Generates transcriptome-wide virtual spatial transcriptomics from H&E histology with DeepSpot-M. Used for predicted log1p-CPM expression from 224x224 tiles at about 20x, querying the released protein-coding gene panel by symbol, and whole-slide prediction after resolution-aware tiling with histolab.

</details>

上游线索：[https://github.com/ratschlab/DeepSpotM](https://github.com/ratschlab/DeepSpotM)

<a id="skill-deeptools"></a>
### `$deeptools`

- 全局目录：`~/.codex/skills/deeptools/`
- 中文理解：围绕 `deeptools` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $deeptools。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

NGS analysis toolkit. BAM to bigWig conversion, QC (correlation, PCA, fingerprints), heatmaps/profiles (TSS, peaks), for ChIP-seq, RNA-seq, ATAC-seq visualization.

</details>

<a id="skill-depmap"></a>
### `$depmap`

- 全局目录：`~/.codex/skills/depmap/`
- 中文理解：这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `depmap` 相关任务。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $depmap。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Retrieves and analyzes Cancer Dependency Map (DepMap) release data, including CRISPR Chronos gene effects, cancer model annotations, omics biomarkers, and PRISM drug sensitivity. Supports cancer-selective dependency, co-essentiality, and candidate synthetic-lethality analyses with release-aware identifiers and statistical checks.

</details>

上游线索：[https://github.com/broadinstitute/depmap-portal](https://github.com/broadinstitute/depmap-portal)

<a id="skill-dnanexus-integration"></a>
### `$dnanexus-integration`

- 全局目录：`~/.codex/skills/dnanexus-integration/`
- 中文理解：围绕 `dnanexus-integration` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $dnanexus-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and operates reproducible genomics workloads on DNAnexus with the dx CLI, dxpy, apps/applets, native workflows, dxCompiler, and Nextflow. Supports DNAnexus data transfers, dxapp.json development, execution monitoring, workflow import, and project automation.

</details>

<a id="skill-esm"></a>
### `$esm`

- 全局目录：`~/.codex/skills/esm/`
- 中文理解：围绕 `esm` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $esm。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Uses the Biohub esm Python SDK for ESM3 protein generation, ESMC embeddings, and ESMFold2 all-atom folding. Applies to local model inference and Biohub hosted clients, including former Forge workflows; distinguishes the separate legacy fair-esm distribution.

</details>

<a id="skill-etetoolkit"></a>
### `$etetoolkit`

- 全局目录：`~/.codex/skills/etetoolkit/`
- 中文理解：围绕 `etetoolkit` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $etetoolkit。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes, manipulates, compares, annotates, and visualizes phylogenetic or other hierarchical trees with ETE 4. Supports Newick/Nexus tree I/O, topology edits and pattern matching, Robinson-Foulds comparisons, gene-tree evolutionary events and reconciliation, NCBI/GTDB taxonomy, SmartView exploration, and publication rendering. Applies to existing trees after alignment and phylogenetic inference, rather than inferring trees from raw sequences.

</details>

上游线索：[https://github.com/etetoolkit/ete](https://github.com/etetoolkit/ete)

<a id="skill-geniml"></a>
### `$geniml`

- 全局目录：`~/.codex/skills/geniml/`
- 中文理解：围绕 `geniml` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $geniml。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports audited local Geniml genomic-interval workflows: validate BED and universe contracts, plan Region2Vec or scEmbed runs, inspect model/tokenizer compatibility, and assess consensus universes.

</details>

上游线索：[https://github.com/databio/geniml](https://github.com/databio/geniml)

<a id="skill-genomic-intelligence"></a>
### `$genomic-intelligence`

- 全局目录：`~/.codex/skills/genomic-intelligence/`
- 中文理解：围绕 `genomic-intelligence` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $genomic-intelligence。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Predicts regulatory features, gene structure, and expression directly from DNA sequence using Genomic Intelligence's hosted transformer DNA language models — no local GPU or model weights. Six tasks over a REST API and a hosted MCP server (keyless public demo): promoter regions, splice donor/acceptor sites, enhancer activity, chromatin state, sequence-to-expression (log TPM), and de-novo gene annotation, plus a composite find-genes-then-predict-expression workflow. Use when the user has a gene symbol, a genomic region, or a DNA/FASTA sequence and wants any of these predictions, mentions Genomic Intelligence, genomicintelligence.ai, api.genomicintelligence.ai, or mcp.genomicintelligence.ai.

</details>

<a id="skill-gget"></a>
### `$gget`

- 全局目录：`~/.codex/skills/gget/`
- 中文理解：围绕 `gget` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $gget。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries 20+ bioinformatics resources through CLI/Python. Supports quick lookups of gene info, BLAST/BLAT, viral sequence downloads, PDB/mmCIF structures, G2P residue annotations, enrichment analysis, OpenTargets, COSMIC, CELLxGENE, and 8cube mouse specificity/expression data. Best for interactive exploration and simple queries. For batch processing or advanced BLAST use biopython; for multi-database Python workflows use bioservices.

</details>

上游线索：[https://github.com/scverse/gget](https://github.com/scverse/gget)

<a id="skill-gtars"></a>
### `$gtars`

- 全局目录：`~/.codex/skills/gtars/`
- 中文理解：围绕 `gtars` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $gtars。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports Gtars for local genomic interval models and set algebra, overlaps and counts, consensus and coverage, tokenization, fragment processing, and refget/BEDbase planning across Python, Rust, and the CLI.

</details>

上游线索：[https://github.com/databio/gtars](https://github.com/databio/gtars)

<a id="skill-hugging-science"></a>
### `$hugging-science`

- 全局目录：`~/.codex/skills/hugging-science/`
- 中文理解：围绕 `hugging-science` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $hugging-science。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Discovers and evaluates scientific datasets, models, methodology posts, and Spaces through the Hugging Science catalog. Used when selecting scientific ML resources in biology, chemistry, genomics, materials, climate, physics, astronomy, medicine, mathematics, protein design, single-cell analysis, or PDE modeling, and when checking their actual datasets, Transformers, native-runtime, Inference Providers, or Gradio interfaces.

</details>

<a id="skill-lamindb"></a>
### `$lamindb`

- 全局目录：`~/.codex/skills/lamindb/`
- 中文理解：这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `lamindb` 相关任务。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $lamindb。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Manages biological datasets and models with LaminDB, including artifact registration, lineage tracking, schema validation, Bionty ontology annotation, query/search, collections, branches, storage, and workflow integrations. Use for reproducible biological data curation or a LaminDB lakehouse.

</details>

<a id="skill-latchbio-integration"></a>
### `$latchbio-integration`

- 全局目录：`~/.codex/skills/latchbio-integration/`
- 中文理解：这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `latchbio-integration` 相关任务。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $latchbio-integration。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds, registers, debugs, and operates bioinformatics workflows on Latch using the Python SDK, CLI, Latch Data and Registry, Nextflow, Snakemake, programmatic execution, and Latch MCP. Use when authoring or deploying Latch workflows, configuring resources or interfaces, moving data, integrating Registry, or launching and monitoring runs.

</details>

上游线索：[https://github.com/latchbio/latch](https://github.com/latchbio/latch)

<a id="skill-mageck"></a>
### `$mageck`

- 全局目录：`~/.codex/skills/mageck/`
- 中文理解：这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `mageck` 相关任务。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $mageck。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Analyzes pooled CRISPR screen FASTQ reads and guide-count matrices with MAGeCK, validates guide libraries and contrasts, measures replicate and library QC, and produces gene hit rankings with effect sizes and FDR. Use for new knockout, CRISPRi, or CRISPRa screen analysis, enrichment or depletion contrasts, and MAGeCK count/test workflows; existing public dependency-score lookup belongs to DepMap.

</details>

上游线索：[https://github.com/davidliwei/mageck2](https://github.com/davidliwei/mageck2)

<a id="skill-pathogen-variant-surveillance"></a>
### `$pathogen-variant-surveillance`

- 全局目录：`~/.codex/skills/pathogen-variant-surveillance/`
- 中文理解：围绕 `pathogen-variant-surveillance` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $pathogen-variant-surveillance。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries public GenSpectrum LAPIS data for pathogen genomic surveillance, current lineage nomenclature, weekly sequence proportions, reporting delays, and descriptive mutation frequencies. Use for variant surveillance, Pango lineage validation, dominant submitted lineages, Nextclade assignment provenance, SARS-CoV-2, influenza/H5N1 clades, RSV, mpox, measles, dengue, or LAPIS queries. Distinguishes sequence prevalence from infection prevalence, clades from genotypes, missing calls from reference matches, and sampling changes from biological growth advantage.

</details>

<a id="skill-pathway-enrichment"></a>
### `$pathway-enrichment`

- 全局目录：`~/.codex/skills/pathway-enrichment/`
- 中文理解：围绕 `pathway-enrichment` 的专项能力，主要用于处理质谱、蛋白组或代谢组数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pathway-enrichment。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs pathway and gene-set enrichment analysis on gene lists or ranked gene data and interprets the results. Used when the user has a set of genes (differentially expressed genes from PyDESeq2/Scanpy, CRISPR-screen hits, cluster marker genes, proteomics hits) and wants to know which biological pathways, GO terms, or gene sets are over-represented or enriched. Covers over-representation analysis (ORA / Enrichr / Fisher / hypergeometric), ranked Gene Set Enrichment Analysis (GSEA / preranked), single-sample scoring (ssGSEA/GSVA), and functional profiling via gseapy, g:Profiler, Enrichr libraries, MSigDB, GO, KEGG, Reactome, and WikiPathways — plus gene-ID mapping, choosing the right background universe, multiple-testing correction, redundancy reduction, dotplots/enrichment maps, and publication-ready tables. Use this for "pathway analysis", "enrichment analysis", "GO enrichment", "KEGG/Reactome pathways", "GSEA", "over-representation", "functional annotation", or "what pathways are my genes in".

</details>

上游线索：[https://github.com/zqfang/GSEApy](https://github.com/zqfang/GSEApy)

<a id="skill-phylogenetics"></a>
### `$phylogenetics`

- 全局目录：`~/.codex/skills/phylogenetics/`
- 中文理解：围绕 `phylogenetics` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $phylogenetics。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and analyzes phylogenetic trees using MAFFT multiple sequence alignment, IQ-TREE maximum likelihood with ModelFinder and branch support, and FastTree approximate inference. Uses ETE3 for tree summaries and visualization. Applies to homologous nucleotide or protein sequences, microbial gene trees, protein families, and cautiously interpreted dated phylogenies.

</details>

上游线索：[https://github.com/iqtree/iqtree3](https://github.com/iqtree/iqtree3)

<a id="skill-polars-bio"></a>
### `$polars-bio`

- 全局目录：`~/.codex/skills/polars-bio/`
- 中文理解：围绕 `polars-bio` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $polars-bio。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs genomic interval overlap, nearest, merge, coverage, complement and subtraction on Polars DataFrames, and reads or writes BED, VCF, BCF, BAM, CRAM, GFF, GTF, FASTA and FASTQ data. Use for coordinate-aware genomic joins, read-depth analysis, lazy bioinformatics I/O, SQL queries or migration from bioframe.

</details>

上游线索：[https://github.com/biodatageeks/polars-bio](https://github.com/biodatageeks/polars-bio)

<a id="skill-primekg"></a>
### `$primekg`

- 全局目录：`~/.codex/skills/primekg/`
- 中文理解：这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `primekg` 相关任务。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $primekg。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Queries a pinned Precision Medicine Knowledge Graph (PrimeKG) CSV for typed gene, drug, disease, and phenotype nodes, direct associations, disease context, and one- or two-hop paths. Use for PrimeKG reproducibility, biological association lookup, and hypothesis generation with relation and data provenance preserved.

</details>

上游线索：[https://github.com/mims-harvard/PrimeKG](https://github.com/mims-harvard/PrimeKG)

<a id="skill-pydeseq2"></a>
### `$pydeseq2`

- 全局目录：`~/.codex/skills/pydeseq2/`
- 中文理解：围绕 `pydeseq2` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pydeseq2。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs bulk RNA-seq differential expression analysis with PyDESeq2, including count validation, formula designs, explicit contrasts, Wald tests, FDR correction, coefficient-matched LFC shrinkage, and result visualization. Use for PyDESeq2 or Python DESeq2 workflows with biological replicates.

</details>

上游线索：[https://github.com/scverse/PyDESeq2](https://github.com/scverse/PyDESeq2)

<a id="skill-pysam"></a>
### `$pysam`

- 全局目录：`~/.codex/skills/pysam/`
- 中文理解：围绕 `pysam` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $pysam。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides Python/HTSlib workflows for genomic files. Used when reading, querying, filtering, or writing SAM/BAM/CRAM, VCF/BCF, FASTA/FASTQ, or tabix data with pysam, including pileup, coverage, indexing, and CRAM references.

</details>

<a id="skill-scanpy"></a>
### `$scanpy`

- 全局目录：`~/.codex/skills/scanpy/`
- 中文理解：围绕 `scanpy` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scanpy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs Scanpy single-cell RNA-seq QC, normalization, HVG selection, PCA/UMAP/t-SNE, clustering, exploratory marker ranking, pseudobulk preparation, visualization, and Seurat or SingleCellExperiment RDS conversion to h5ad. Applies to established exploratory scRNA-seq workflows with explicit count and expression provenance; complementary skills cover scvi-tools models and AnnData format details.

</details>

<a id="skill-scikit-bio"></a>
### `$scikit-bio`

- 全局目录：`~/.codex/skills/scikit-bio/`
- 中文理解：围绕 `scikit-bio` 的专项能力，主要用于处理生物信息与组学数据，并可开展系统发育或分类学分析。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scikit-bio。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Biological data toolkit. Sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ordination (PCoA), PERMANOVA, FASTA/Newick I/O, for microbiome analysis.

</details>

上游线索：[https://github.com/scikit-bio/scikit-bio](https://github.com/scikit-bio/scikit-bio)

<a id="skill-scvelo"></a>
### `$scvelo`

- 全局目录：`~/.codex/skills/scvelo/`
- 中文理解：围绕 `scvelo` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。

可复制提示词：

```text
使用 $scvelo。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Performs RNA velocity analysis with scVelo from spliced and unspliced single-cell RNA counts. Fits deterministic or dynamical models, examines gene phase portraits, builds velocity graphs, estimates relative latent time, and ranks velocity-associated genes. Use for directional trajectory hypotheses and kinetic-model diagnostics alongside Scanpy; velocity alone does not establish cell fate or causal drivers.

</details>

上游线索：[https://github.com/theislab/scvelo](https://github.com/theislab/scvelo)

<a id="skill-scvi-tools"></a>
### `$scvi-tools`

- 全局目录：`~/.codex/skills/scvi-tools/`
- 中文理解：围绕 `scvi-tools` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $scvi-tools。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fits probabilistic models for single-cell omics, including scVI batch integration, scANVI annotation, totalVI CITE-seq, MultiVI RNA/ATAC integration, and posterior differential expression. Use for generative modeling, reference mapping, multimodal analysis, or model-based uncertainty; use scanpy for standard preprocessing and exploratory analysis.

</details>

上游线索：[https://github.com/scverse/scvi-tools](https://github.com/scverse/scvi-tools)

<a id="skill-tamarind"></a>
### `$tamarind`

- 全局目录：`~/.codex/skills/tamarind/`
- 中文理解：围绕 `tamarind` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $tamarind。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides access to a collection of open-source molecular design and structural biology tools on the Tamarind Bio platform, via its REST API or MCP server — no local GPUs required. Tamarind bundles popular open-source models for structure prediction (AlphaFold, Boltz, Chai, ESMFold), protein, binder, and de novo design (RFdiffusion, ProteinMPNN, BoltzGen), antibody and nanobody design and developability, protein-ligand docking (DiffDock, Autodock Vina), binding-affinity prediction, MSA generation, and molecular dynamics. Use when the user mentions Tamarind or tamarind.bio, wants to run any of these open-source tools in the cloud, references app.tamarind.bio/api or the x-api-key header, or needs to submit batches of sequences for structural or biophysical characterization.

</details>

<a id="skill-tiledbvcf"></a>
### `$tiledbvcf`

- 全局目录：`~/.codex/skills/tiledbvcf/`
- 中文理解：围绕 `tiledbvcf` 的专项能力，主要用于处理生物信息与组学数据，并可分析遗传变异及其影响。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $tiledbvcf。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Stores and retrieves genomic variant calls with TileDB-VCF. Use for indexed single-sample VCF/BCF ingestion, incremental cohorts, region and sample queries, streaming results, allele statistics, QC, and VCF/BCF export locally or through TileDB Cloud.

</details>

上游线索：[https://github.com/TileDB-Inc/TileDB-VCF](https://github.com/TileDB-Inc/TileDB-VCF)

<a id="skill-torchdrug"></a>
### `$torchdrug`

- 全局目录：`~/.codex/skills/torchdrug/`
- 中文理解：围绕 `torchdrug` 的专项能力，主要用于处理生物信息与组学数据。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $torchdrug。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Builds and troubleshoots TorchDrug 0.2.1 workflows for molecular graphs, property prediction, self-supervised pretraining, molecule generation, retrosynthesis, protein representation learning, and knowledge graph reasoning. Use when code imports torchdrug or needs its datasets, models, tasks, or Engine.

</details>

上游线索：[https://github.com/DeepGraphLearning/torchdrug](https://github.com/DeepGraphLearning/torchdrug)

<a id="skill-waypoint-bio"></a>
### `$waypoint-bio`

- 全局目录：`~/.codex/skills/waypoint-bio/`
- 中文理解：这是一个面向“生物信息、组学与遗传学”的专项技能，用于处理 `waypoint-bio` 相关任务。
- 适合何时使用：处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $waypoint-bio。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Supports work with Outpost Bio's open microbiome foundation models - the Waypoint checkpoints (Waypoint-6m, Waypoint-45m, Waypoint-170m), the Atlas pretraining corpus, the Compass eight-task benchmark, or the `waypoint` CLI from the `waypoint-bio` package. Covers embedding microbiome samples, fine-tuning on taxonomic abundance data, benchmarking a checkpoint on Compass, pretraining a GPT-2 model on taxonomic abundance profiles, and converting MetaPhlAn, Kraken2, QIIME 2, or MGnify abundance tables into waypoint format.

</details>

上游线索：[https://github.com/Outpost-Bio/waypoint](https://github.com/Outpost-Bio/waypoint)

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
