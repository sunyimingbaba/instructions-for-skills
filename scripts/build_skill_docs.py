#!/usr/bin/env python3
"""Build a readable Chinese catalog from globally installed Codex skills."""

from __future__ import annotations

import json
import os
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = Path(
    os.environ.get("GLOBAL_SKILLS_ROOT", "/Users/botlv/.codex/skills")
).expanduser()
SKILLS_DISPLAY = "~/.codex/skills"
DOCS_ROOT = REPO_ROOT / "docs"
CATEGORY_ROOT = DOCS_ROOT / "categories"
DATA_ROOT = REPO_ROOT / "data"


@dataclass(frozen=True)
class Category:
    slug: str
    title: str
    explanation: str
    prompt: str


@dataclass(frozen=True)
class Suite:
    slug: str
    title: str
    entry: str
    explanation: str
    url: str | None = None


CATEGORIES = [
    Category("workflow", "科研工作流与自治实验", "把研究目标拆成可追踪步骤，管理假设、实验、结果与迭代。", "说明研究目标、已有材料、可修改范围、评价指标和停止条件；先给计划，再执行。"),
    Category("literature", "文献检索、证据与引用", "用于找论文、核对出处、整理证据、管理引用和撰写综述。", "说明主题、时间范围、数据库偏好和纳排标准；要求逐条给来源，未核实内容明确标记。"),
    Category("writing", "论文写作、审稿与出版", "帮助组织论文、改写段落、审稿、回复意见、制作投稿材料。", "提供论文或材料路径、目标期刊/会议、需要处理的章节和禁止编造的内容；先列问题再修改。"),
    Category("math-modeling", "数学建模竞赛", "覆盖读题、建模、求解、绘图、写作、格式检查和最终验收。", "提供完整题面、附件和当前进度；说明比赛、截止时间、输出格式，并要求所有数值可追溯。"),
    Category("statistics-ml", "统计、机器学习与时序分析", "用于统计建模、预测、分类、聚类、因果或不确定性分析。", "提供数据路径、变量含义、研究问题和评价指标；要求先做数据检查，再给方法、代码和诊断。"),
    Category("visualization", "科学可视化、文档与演示", "生成或检查论文图表、流程图、海报、幻灯片和技术文档。", "提供数据/草图、目标尺寸、受众和输出格式；要求说明视觉编码并导出可编辑源文件。"),
    Category("bioinformatics", "生物信息、组学与遗传学", "处理序列、单细胞、转录组、基因组、系统生物学和公共生物数据库。", "说明物种、参考版本、数据格式、实验设计和生物学问题；保留样本与基因标识的映射。"),
    Category("chemistry", "化学、药物、材料与分子模拟", "用于化学信息学、药物发现、质谱、结构、材料和分子模拟。", "提供分子/材料标识、输入格式、计算目标和约束；要求报告单位、参数、版本和适用边界。"),
    Category("clinical-lab", "医学、临床与实验室规范", "支持临床研究、实验室方法验证、标准体系和医学数据工作流。", "说明使用场景、证据等级、适用标准和数据边界；输出须区分科研建议与临床/法规结论。"),
    Category("geo-physical", "地学、空间、天文与环境", "处理地理空间、遥感、海洋、天文、物理和工程科学问题。", "提供坐标系/单位、空间或时间范围、数据来源和目标；要求先核对元数据与物理量纲。"),
    Category("llm-training", "AI/LLM 模型训练、压缩与推理", "覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。", "提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。"),
    Category("agents-rag", "智能体、RAG、安全与评测", "用于构建智能体、检索增强系统、评测框架、安全护栏和可观测性。", "说明模型、工具、知识库、评测集和失败标准；要求给最小可运行方案及可复现评测。"),
    Category("data-compute", "数据工程、计算与云平台", "处理数据格式、并行计算、工作流编排、GPU 云和科研计算基础设施。", "提供数据量、运行环境、预算和目标命令；要求先检查依赖、权限和可恢复性。"),
    Category("lab-platform", "实验室平台、ELN 与科研硬件", "连接云实验室、电子实验记录、仪器、实验硬件和科研数据平台。", "说明平台账户、对象标识、权限和预期操作；先做只读检查，提交/下单前列出影响。"),
    Category("general", "通用科研工具与质量保障", "无法归入单一学科、但可支撑科研质量、文件处理、复现或效率的工具。", "说明当前材料、想得到的结果和输出格式；要求列出假设、缺失信息和验证方法。"),
]
CATEGORY_BY_SLUG = {item.slug: item for item in CATEGORIES}


SUITES = [
    Suite("scientific-agent-skills", "Scientific Agent Skills（K-Dense）", "按任务直接调用对应小 skill", "覆盖文献、科研计算、统计、生物信息、实验室规范等大量独立专项能力。", "https://github.com/K-Dense-AI/scientific-agent-skills"),
    Suite("aris", "Auto Claude Code Research in Sleep（ARIS）", "$research-pipeline", "覆盖选题、文献、实验、写作、审稿和论文改进的端到端研究工作流。", "https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep"),
    Suite("orchestra", "AI Research SKILLs（Orchestra Research）", "$autoresearch", "面向 AI 研究的模型架构、训练、后训练、推理、智能体和论文写作技能集合。", "https://github.com/Orchestra-Research/AI-Research-SKILLs"),
    Suite("academic-research-suite", "ARS-Codex 学术研究套件", "$academic-research-suite", "统一入口，内部路由文献综述、论文写作、审稿、筛选和实验工作流。", "https://github.com/Imbad0202/academic-research-skills-codex"),
    Suite("codex-autoresearch", "Codex Autoresearch", "$codex-autoresearch", "针对可量化指标反复修改、测量、保留改进并回退失败实验。", "https://github.com/leo-lilinxiao/codex-autoresearch"),
    Suite("nature", "Nature Research Skills", "按任务直接调用对应的 $nature-* skill", "覆盖学术检索、写作、审稿、统计、图表、回应审稿人和科研资料处理。"),
    Suite("bzd", "BZD 数学建模 Skills", "$bzd-modeling-workflow", "数学建模竞赛的读题、建模、写作、格式、引用、AIGC 和评审工作流。"),
    Suite("hwb", "HWB 华为杯数学建模 Skills", "$hwb-modeling-workflow", "针对华为杯研究生数学建模竞赛的完整流程和专项检查。"),
    Suite("mathmodel", "MathModel 数学建模工作流", "$1start-mathmodel", "从赛题分析、编程求解、图表到论文撰写和最终验收的阶段式工作流。"),
    Suite("scientific-toolkit", "Scientific Toolkit 科研计算套件", "$scientific-toolkit-skill", "面向 MATLAB、Python 科研计算、信号图像、统计、仿真和可复现分析。"),
    Suite("standalone", "独立或暂未归入大型套件", "直接调用当前小 skill", "这些 skill 可以独立使用，或其本地文件中没有足够信息可靠判断上级套件。"),
]
SUITE_BY_SLUG = {item.slug: item for item in SUITES}


ARIS_SKILLS = set("""
ablation-planner alphaxiv analyze-results arxiv auto-paper-improvement-loop
auto-review-loop auto-review-loop-llm auto-review-loop-minimax citation-audit
claims-drafting comm-lit-review deepxiv dse-loop embodiment-description experiment-audit
experiment-bridge experiment-plan experiment-queue feishu-notify figure-description
figure-spec formula-derivation gemini-search grant-proposal idea-creator idea-discovery
idea-discovery-robot integrity-forensics interview-cheatsheet invention-structuring
jurisdiction-format kill-argument mermaid-diagram meta-apply meta-optimize
monitor-experiment novelty-check openalex overleaf-sync paper-claim-audit paper-compile
paper-figure paper-illustration paper-illustration-image2 paper-plan paper-poster
paper-poster-html paper-slides paper-talk paper-write paper-writing patent-novelty-check
patent-pipeline patent-review pixel-art prior-art-search proof-checker proof-orchestrator
proof-writer qzcli rebuttal render-html research-implement-feature research-lit
research-pipeline research-refine research-refine-pipeline research-review research-wiki
resubmit-pipeline result-to-claim run-experiment semantic-scholar serverless-modal
slides-polish specification-writing system-profile training-check vast-gpu
web-debug-search wiki-enrich writing-systems-papers
""".split())


EXACT_CATEGORY = {
    "_references": "math-modeling",
    "1start-mathmodel": "math-modeling",
    "2analysis-modeling": "math-modeling",
    "3coding-visual": "math-modeling",
    "4drawio": "math-modeling",
    "5writing": "math-modeling",
    "6verity": "math-modeling",
    "Visiomaster": "visualization",
    "academic-research-suite": "workflow",
    "autoskill": "workflow",
    "humanizer": "writing",
    "doctor": "general",
    "find-skills": "general",
    "get-available-resources": "general",
    "markitdown": "general",
    "liteparse": "general",
}


def add_exact(slug: str, names: str) -> None:
    for item in names.split():
        EXACT_CATEGORY[item] = slug


# Explicit mappings for suites whose product names are too ambiguous for keyword
# classification (for example Mamba, Whisper, Modal, and Phoenix).
add_exact("llm-training", """
litgpt mamba nanogpt rwkv torchtitan huggingface-tokenizers sentencepiece axolotl
llama-factory peft unsloth nnsight pyvene saelens transformer-lens grpo-rl-training
miles openrlhf simpo slime torchforge trl-fine-tuning verl accelerate deepspeed
megatron-core pytorch-fsdp2 pytorch-lightning ray-train awq bitsandbytes
flash-attention gguf gptq hqq ml-training-recipes llama-cpp sglang tensorrt-llm
vllm audiocraft blip-2 clip cosmos-policy llava openpi openvla-oft
segment-anything stable-diffusion whisper knowledge-distillation long-context
model-merging model-pruning moe-training speculative-decoding transformers
""")
add_exact("agents-rag", """
constitutional-ai llamaguard nemo-guardrails prompt-guard bigcode-evaluation-harness
lm-evaluation-harness nemo-evaluator a-evolve autogpt crewai langchain llamaindex
chroma faiss pinecone qdrant sentence-transformers dspy guidance instructor outlines
langsmith phoenix
""")
add_exact("data-compute", """
nemo-curator ray-data lambda-labs modal skypilot mlflow swanlab tensorboard
weights-and-biases
""")
add_exact("writing", """
academic-plotting ml-paper-writing presenting-conference-talks systems-paper-writing
""")
add_exact("workflow", """
0-autoresearch-skill brainstorming-research-ideas creative-thinking-for-research
compiler research-manager rigor-reviewer ablation-planner analyze-results
experiment-audit experiment-bridge experiment-plan experiment-queue idea-creator
idea-discovery idea-discovery-robot monitor-experiment research-pipeline
research-refine-pipeline run-experiment
""")
add_exact("visualization", """
academic-plotting generate-image infographics markdown-mermaid-writing matplotlib
mermaid-diagram nature-figure scientific-figure-making scientific-schematics
scientific-slides scientific-visualization seaborn latex-posters pptx-posters
""")
add_exact("statistics-ml", """
exploratory-data-analysis statistical-analysis statistical-power statsmodels
scikit-learn scikit-survival aeon timesfm-forecasting umap-learn shap pymc pymoo
""")
add_exact("chemistry", """
molecular-dynamics diffdock rowan rdkit medchem molfeat matchms pyopenms nmrglue
pymatgen pycalphad cantera
""")
add_exact("bioinformatics", """
depmap primekg waypoint-bio scanpy scvi-tools scvelo pathway-enrichment
phylogenetics biopython bioservices cobrapy
""")
add_exact("data-compute", "qzcli serverless-modal dask polars vaex zarr-python")


CLASSIFIERS = [
    ("math-modeling", ("mathmodel", "mathematical-modeling", "modeling competition", "cumcm", "cpgmcm", "建模竞赛", "赛题", "bzd-", "hwb-")),
    ("literature", ("literature", "citation", "bibliograph", "paper search", "pubmed", "arxiv", "semantic scholar", "openalex", "doi", "evidence synthesis", "reference management")),
    ("writing", ("paper writing", "manuscript", "peer review", "reviewer", "rebuttal", "abstract", "camera-ready", "grant proposal", "patent", "academic writing", "response letter", "论文", "审稿")),
    ("clinical-lab", ("clinical", "medical", "patient", "treatment", "diagnos", "iso ", "ich ", "usp ", "assay", "method validation", "laboratory-competence", "healthcare")),
    ("bioinformatics", ("genom", "transcript", "rna-seq", "single-cell", "protein", "sequence", "biological", "bioinformatics", "crispr", "phylogen", "gene ", "variant", "cellxgene", "scanpy", "anndata", "pydeseq", "biopython", "pathway", "ontology")),
    ("chemistry", ("molecule", "chemical", "chemistry", "drug", "compound", "mass spect", "nmr", "molecular dynamics", "materials", "crystal", "reaction", "rdkit", "cheminformat", "pymatgen", "catal", "thermodynamic")),
    ("geo-physical", ("geospatial", "geographic", "astronom", "astrophys", "ocean", "marine", "climate", "remote sensing", "fluid", "particle image velocimetry", "carbonate chemistry", "geopandas")),
    ("llm-training", ("fine-tun", "llm training", "language model", "distributed training", "quantization", "inference serving", "model pruning", "model merging", "knowledge distillation", "transformer", "lora", "rl training", "gpu memory", "megatron", "deepspeed", "vllm")),
    ("agents-rag", ("agent", "rag", "vector database", "guardrail", "observability", "evaluation harness", "prompt engineering", "llm application", "tool calling", "retrieval-augmented")),
    ("statistics-ml", ("statistics", "statistical", "machine learning", "classification", "regression", "clustering", "forecast", "time series", "survival", "bayesian", "causal", "uncertainty", "optimization", "simulation")),
    ("visualization", ("plot", "visualization", "figure", "diagram", "poster", "slides", "presentation", "mermaid", "drawio", "visio", "infographic")),
    ("lab-platform", ("eln", "benchling", "labarchives", "cloud lab", "laboratory hardware", "opentrons", "instrument", "foundry", "protocols.io", "omero", "dnanexus", "latch", "lamindb")),
    ("data-compute", ("dataframe", "data engineering", "parallel", "distributed computing", "workflow", "cloud platform", "gpu cloud", "file format", "zarr", "dask", "polars", "nextflow", "modal", "database", "storage")),
    ("workflow", ("research workflow", "research project", "experiment loop", "hypothesis", "research ide", "autonomous research", "experiment plan", "monitor experiment", "research pipeline")),
]


CAPABILITIES = [
    (("literature", "paper search", "arxiv", "pubmed"), "检索和筛选科研文献"),
    (("citation", "doi", "bibliograph", "reference management"), "核对引用与来源"),
    (("paper writing", "manuscript", "academic writing"), "起草和修改论文"),
    (("review", "reviewer", "audit"), "检查问题并给出修改建议"),
    (("plot", "figure", "visualization"), "生成或检查科研图表"),
    (("single-cell", "rna-seq", "genom", "protein", "sequence"), "处理生物信息与组学数据"),
    (("metabolic", "flux balance", "cobra"), "进行代谢网络与通量分析"),
    (("variant", "vcf", "mutation"), "分析遗传变异及其影响"),
    (("mass spect", "proteomic", "metabolomic"), "处理质谱、蛋白组或代谢组数据"),
    (("microscopy", "histology", "pathology", "imaging"), "处理科研或医学影像"),
    (("phylogen", "taxonomy"), "开展系统发育或分类学分析"),
    (("spatial", "geospatial", "coordinate system"), "处理空间数据与坐标关系"),
    (("astronom", "fits", "cosmology"), "处理天文与天体物理数据"),
    (("fluid", "piv", "cfd"), "开展流体或工程仿真分析"),
    (("clinical", "patient", "medical"), "支持医学与临床研究分析"),
    (("molecule", "chemical", "drug", "materials"), "处理化学、药物或材料问题"),
    (("time series", "forecast"), "分析时间序列并进行预测"),
    (("classification", "regression", "clustering"), "完成机器学习建模与评估"),
    (("fine-tun", "lora"), "配置和执行模型微调"),
    (("reinforcement learning", "rl training", "post-training", "grpo", "dpo"), "进行模型后训练或强化学习"),
    (("tokeniz", "sentencepiece"), "训练或使用文本分词器"),
    (("model architecture", "architecture from scratch", "state-space model"), "理解或实现模型架构"),
    (("interpretability", "activation", "sparse autoencoder"), "分析模型内部机制与可解释性"),
    (("inference", "serving", "deploy"), "部署模型并优化推理"),
    (("quantization", "pruning", "distillation", "compression"), "压缩模型并优化推理资源"),
    (("distributed", "multi-gpu", "parallelism"), "配置分布式或多 GPU 训练"),
    (("agent", "autonomous"), "构建或评估智能体工作流"),
    (("rag", "retrieval"), "构建检索增强与知识问答系统"),
    (("vector database", "vector store", "similarity search"), "构建向量检索与相似度搜索"),
    (("observability", "tracing", "monitoring"), "追踪、评测和监控 LLM 应用"),
    (("guardrail", "moderation", "safety"), "增加内容安全检查与防护"),
    (("audio generation", "musicgen", "audiogen"), "生成音乐、语音或音效"),
    (("image generation", "stable diffusion"), "生成或编辑图像"),
    (("vision-language", "image caption", "visual question"), "处理图像与文本的多模态任务"),
    (("workflow", "pipeline"), "组织可复现的科研流程"),
    (("experiment", "hypothesis"), "规划、运行或复盘实验"),
    (("cloud", "gpu"), "使用云端或 GPU 计算资源"),
    (("document", "pdf", "markdown"), "处理科研文档与结构化内容"),
    (("eln", "laboratory information", "inventory"), "管理实验记录、样品或实验室数据"),
    (("robot", "liquid handler", "automation"), "设计或自动化实验室操作"),
]


CATEGORY_ALLOWED_PHRASES = {
    "workflow": {"构建或评估智能体工作流", "组织可复现的科研流程", "规划、运行或复盘实验", "检查问题并给出修改建议"},
    "literature": {"检索和筛选科研文献", "核对引用与来源", "处理科研文档与结构化内容"},
    "writing": {"起草和修改论文", "核对引用与来源", "检查问题并给出修改建议", "生成或检查科研图表", "处理科研文档与结构化内容"},
    "math-modeling": {"组织可复现的科研流程", "规划、运行或复盘实验", "生成或检查科研图表", "完成机器学习建模与评估", "检查问题并给出修改建议"},
    "statistics-ml": {"完成机器学习建模与评估", "分析时间序列并进行预测", "规划、运行或复盘实验", "生成或检查科研图表"},
    "visualization": {"生成或检查科研图表", "处理科研文档与结构化内容", "起草和修改论文"},
    "bioinformatics": {"处理生物信息与组学数据", "进行代谢网络与通量分析", "分析遗传变异及其影响", "处理质谱、蛋白组或代谢组数据", "处理科研或医学影像", "开展系统发育或分类学分析"},
    "chemistry": {"处理化学、药物或材料问题", "进行代谢网络与通量分析", "处理质谱、蛋白组或代谢组数据", "规划、运行或复盘实验"},
    "clinical-lab": {"支持医学与临床研究分析", "处理科研或医学影像", "检查问题并给出修改建议", "组织可复现的科研流程"},
    "geo-physical": {"处理空间数据与坐标关系", "处理天文与天体物理数据", "开展流体或工程仿真分析", "分析时间序列并进行预测"},
    "llm-training": {"配置和执行模型微调", "进行模型后训练或强化学习", "训练或使用文本分词器", "理解或实现模型架构", "分析模型内部机制与可解释性", "部署模型并优化推理", "压缩模型并优化推理资源", "配置分布式或多 GPU 训练", "使用云端或 GPU 计算资源", "完成机器学习建模与评估", "生成音乐、语音或音效", "生成或编辑图像", "处理图像与文本的多模态任务"},
    "agents-rag": {"构建或评估智能体工作流", "构建检索增强与知识问答系统", "构建向量检索与相似度搜索", "追踪、评测和监控 LLM 应用", "增加内容安全检查与防护", "完成机器学习建模与评估", "组织可复现的科研流程"},
    "data-compute": {"使用云端或 GPU 计算资源", "组织可复现的科研流程", "处理科研文档与结构化内容"},
    "lab-platform": {"组织可复现的科研流程", "使用云端或 GPU 计算资源", "规划、运行或复盘实验", "管理实验记录、样品或实验室数据", "设计或自动化实验室操作"},
    "general": {"处理科研文档与结构化内容", "检查问题并给出修改建议", "组织可复现的科研流程", "生成或检查科研图表"},
}


@dataclass
class Skill:
    directory: str
    name: str
    description: str
    category: str
    suite: str
    source_file: str
    upstream: str | None


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        data = yaml.safe_load(parts[1]) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        # A few third-party skills contain an unquoted colon in description.
        # Recover the two fields this catalog needs instead of rejecting the skill.
        recovered: dict[str, str] = {}
        lines = parts[1].splitlines()
        for index, line in enumerate(lines):
            match = re.match(r"^(name|description):\s*(.*)$", line)
            if not match:
                continue
            key, value = match.groups()
            if value in {">", "|"}:
                continuation: list[str] = []
                for following in lines[index + 1 :]:
                    if following.startswith((" ", "\t")):
                        continuation.append(following.strip())
                    else:
                        break
                value = " ".join(continuation)
            recovered[key] = value.strip().strip('"').strip("'")
        return recovered


def compact(value: object) -> str:
    text = str(value or "").strip()
    return re.sub(r"\s+", " ", text)


def category_for(directory: str, name: str, description: str) -> str:
    if directory in EXACT_CATEGORY:
        return EXACT_CATEGORY[directory]
    haystack = f"{directory} {name} {description}".lower()
    for slug, terms in CLASSIFIERS:
        if any(term in haystack for term in terms):
            return slug
    return "general"


def suite_for(directory: str, meta: dict) -> str:
    metadata = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
    author = compact(meta.get("author") or metadata.get("author"))
    skill_author = compact(meta.get("skill-author") or metadata.get("skill-author"))

    if directory == "academic-research-suite":
        return "academic-research-suite"
    if directory == "codex-autoresearch":
        return "codex-autoresearch"
    if directory.startswith("bzd-"):
        return "bzd"
    if directory.startswith("hwb-"):
        return "hwb"
    if directory.startswith("nature-") or directory == "nature-proposal-writer":
        return "nature"
    if directory in {"1start-mathmodel", "2analysis-modeling", "3coding-visual", "4drawio", "5writing", "6verity", "_references", "mathmodel-figure-templates"}:
        return "mathmodel"
    if directory in {"scientific-toolkit-skill", "research-writing-skill", "office-academic-skill"}:
        return "scientific-toolkit"
    if author == "Orchestra Research" or directory in {"ml-training-recipes", "a-evolve"}:
        return "orchestra"
    if skill_author:
        return "scientific-agent-skills"
    if directory in ARIS_SKILLS:
        return "aris"
    return "standalone"


def first_github_url(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", text)
    return match.group(0).rstrip(".)]") if match else None


def load_skills() -> list[Skill]:
    skills: list[Skill] = []
    for path in sorted(SKILLS_ROOT.glob("*/SKILL.md"), key=lambda item: item.parent.name.lower()):
        directory = path.parent.name
        if directory == ".system":
            continue
        meta = frontmatter(path)
        name = compact(meta.get("name")) or directory
        description = compact(meta.get("description"))
        if not description:
            description = "该技能未在 frontmatter 中提供简介，请在调用前阅读它的 SKILL.md。"
        category = category_for(directory, name, description)
        suite = suite_for(directory, meta)
        skills.append(
            Skill(
                directory=directory,
                name=name,
                description=description,
                category=category,
                suite=suite,
                source_file=str(path),
                upstream=first_github_url(path),
            )
        )
    return skills


def has_chinese(text: str) -> bool:
    return len(re.findall(r"[\u4e00-\u9fff]", text)) >= 8


def trim_sentence(text: str, limit: int = 180) -> str:
    text = compact(text).strip('"')
    pieces = re.split(r"(?<=[。！？.!?])\s+", text)
    first = pieces[0] if pieces else text
    if len(first) <= limit:
        return first
    return first[: limit - 1].rstrip() + "…"


def chinese_summary(skill: Skill) -> str:
    first_sentence = trim_sentence(skill.description)
    if has_chinese(first_sentence):
        return first_sentence
    lowered = skill.description.lower()
    matched: list[str] = []
    allowed = CATEGORY_ALLOWED_PHRASES[skill.category]
    for terms, phrase in CAPABILITIES:
        if phrase in allowed and any(term in lowered for term in terms) and phrase not in matched:
            matched.append(phrase)
        if len(matched) == 2:
            break
    category = CATEGORY_BY_SLUG[skill.category]
    if matched:
        joined = "，并可".join(matched)
        return f"围绕 `{skill.name}` 的专项能力，主要用于{joined}。"
    return f"这是一个面向“{category.title}”的专项技能，用于处理 `{skill.name}` 相关任务。"


def caution_for(skill: Skill) -> str:
    text = skill.description.lower()
    cautions: list[str] = []
    if skill.category == "clinical-lab" or any(word in text for word in ("clinical decision", "patient", "diagnos")):
        cautions.append("医学输出仅用于科研和信息整理，不能替代临床判断。")
    if any(word in text for word in ("api", "sdk", "cloud", "submit", "deploy")):
        cautions.append("可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。")
    if any(word in text for word in ("gpu", "training", "fine-tun", "simulation")):
        cautions.append("先核对硬件、依赖版本、运行时间和预算，再启动长任务。")
    if any(word in text for word in ("citation", "literature", "paper", "evidence")):
        cautions.append("论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。")
    if any(word in text for word in ("patent", "legal", "iso ", "regulatory compliance")):
        cautions.append("格式与证据整理不等于法律、合规、认证或专利意见。")
    if not cautions:
        cautions.append("技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。")
    return " ".join(cautions[:2])


def prompt_for(skill: Skill) -> str:
    category = CATEGORY_BY_SLUG[skill.category]
    if skill.directory == "_references":
        return "这个目录是其他数学建模 skills 使用的共享知识库，通常无需单独调用。"
    return (
        f"使用 ${skill.name}。我的目标是：<具体任务>。\n"
        f"已有材料：<文件路径、数据、论文或代码>。\n"
        f"要求：{category.prompt}\n"
        "如信息不足，请先列出缺口；不要编造数据、引用或运行结果。"
    )


def anchor(skill: Skill) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "-", skill.directory).strip("-").lower()
    return f"skill-{safe or 'unnamed'}"


def md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def suite_anchor(slug: str) -> str:
    return f"suite-{slug}"


def render_category(category: Category, skills: list[Skill]) -> str:
    lines = [
        f"# {category.title}",
        "",
        category.explanation,
        "",
        f"本页收录 **{len(skills)}** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。",
        "",
        "## 本页索引",
        "",
        "| Skill | 所属技能套件 | 一句话理解 |",
        "| --- | --- | --- |",
    ]
    for skill in skills:
        suite = SUITE_BY_SLUG[skill.suite]
        lines.append(f"| [`${md_cell(skill.name)}`](#{anchor(skill)}) | [{suite.title}](../技能套件导航.md#{suite_anchor(skill.suite)}) | {md_cell(chinese_summary(skill))} |")
    lines.extend(["", "## 详细说明", ""])
    for skill in skills:
        suite = SUITE_BY_SLUG[skill.suite]
        lines.extend(
            [
                f'<a id="{anchor(skill)}"></a>',
                f"### `${skill.name}`",
                "",
                f"- 全局目录：`~/.codex/skills/{skill.directory}/`",
                f"- 所属技能套件：[{suite.title}](../技能套件导航.md#{suite_anchor(skill.suite)})",
                f"- 推荐总入口：`{suite.entry}`" if suite.entry.startswith("$") else f"- 推荐总入口：{suite.entry}",
                f"- 中文理解：{chinese_summary(skill)}",
                f"- 适合何时使用：{category.explanation}",
                f"- 使用前注意：{caution_for(skill)}",
                "",
                "可复制提示词：",
                "",
                "```text",
                prompt_for(skill),
                "```",
                "",
                "<details>",
                "<summary>查看技能原始说明（用于核对精确能力边界）</summary>",
                "",
                skill.description,
                "",
                "</details>",
                "",
            ]
        )
        if skill.upstream:
            lines.extend([f"上游线索：[{skill.upstream}]({skill.upstream})", ""])
    lines.extend(["---", "", "[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)", ""])
    return "\n".join(lines)


def render_index(skills: list[Skill]) -> str:
    counts = Counter(skill.category for skill in skills)
    lines = [
        "# 全局 Skills 总索引",
        "",
        f"本索引来自 `{SKILLS_DISPLAY}/*/SKILL.md` 的实际扫描，共 **{len(skills)}** 个 skills。",
        "",
        "| Skill | 所属技能套件 | 推荐总入口 | 分类 | 全局目录 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for skill in sorted(skills, key=lambda item: (item.name.lower(), item.directory.lower())):
        category = CATEGORY_BY_SLUG[skill.category]
        suite = SUITE_BY_SLUG[skill.suite]
        link = f"categories/{category.slug}.md#{anchor(skill)}"
        directory_note = skill.directory if skill.directory == skill.name else f"{skill.directory}（调用名：{skill.name}）"
        entry = f"`{suite.entry}`" if suite.entry.startswith("$") else suite.entry
        lines.append(f"| [`${md_cell(skill.name)}`]({link}) | [{suite.title}](技能套件导航.md#{suite_anchor(skill.suite)}) | {entry} | [{category.title}](categories/{category.slug}.md) | `{md_cell(directory_note)}` |")
    lines.extend(["", "## 分类统计", "", "| 分类 | 数量 |", "| --- | ---: |"])
    for category in CATEGORIES:
        lines.append(f"| [{category.title}](categories/{category.slug}.md) | {counts[category.slug]} |")
    return "\n".join(lines) + "\n"


def render_suites(skills: list[Skill]) -> str:
    counts = Counter(skill.suite for skill in skills)
    lines = [
        "# 技能套件与总入口导航",
        "",
        "这里回答“这个小 skill 属于哪个大套件、应该从哪个总入口开始”。总入口不是必须使用；任务很明确时，直接调用小 skill 通常更快。",
        "",
        "| 技能套件 | 小 Skills 数量 | 推荐总入口 | 什么时候从总入口开始 |",
        "| --- | ---: | --- | --- |",
    ]
    for suite in SUITES:
        entry = f"`{suite.entry}`" if suite.entry.startswith("$") else suite.entry
        lines.append(f"| [{suite.title}](#{suite_anchor(suite.slug)}) | {counts[suite.slug]} | {entry} | {suite.explanation} |")

    for suite in SUITES:
        members = sorted((skill for skill in skills if skill.suite == suite.slug), key=lambda item: item.name.lower())
        lines.extend(["", f'<a id="{suite_anchor(suite.slug)}"></a>', f"## {suite.title}", ""])
        if suite.url:
            lines.append(f"项目地址：[{suite.url}]({suite.url})")
            lines.append("")
        entry = f"`{suite.entry}`" if suite.entry.startswith("$") else suite.entry
        lines.extend([f"- 推荐总入口：{entry}", f"- 套件定位：{suite.explanation}", f"- 当前收录：{len(members)} 个小 skills", "", "| 小 Skill | 分类 | 中文理解 |", "| --- | --- | --- |"])
        for skill in members:
            category = CATEGORY_BY_SLUG[skill.category]
            link = f"categories/{category.slug}.md#{anchor(skill)}"
            lines.append(f"| [`${md_cell(skill.name)}`]({link}) | [{category.title}](categories/{category.slug}.md) | {md_cell(chinese_summary(skill))} |")
    lines.extend(["", "---", "", "[返回完整使用指南](全局科研Skills使用指南.md) · [返回全部技能索引](技能总索引.md)", ""])
    return "\n".join(lines)


def render_guide(skills: list[Skill]) -> str:
    counts = Counter(skill.category for skill in skills)
    suite_counts = Counter(skill.suite for skill in skills)
    lines = [
        "# 全局科研 Skills 使用指南",
        "",
        f"更新日期：{date.today().isoformat()}。本指南扫描了本机全局目录 `{SKILLS_DISPLAY}`，共收录 **{len(skills)}** 个科研及科研支撑 skills。",
        "",
        "## 最简单的使用方法",
        "",
        "在新建的 Codex 对话里写出 `$技能名`，再交代四件事：你要解决什么、材料在哪里、希望得到什么格式、哪些内容不能猜。",
        "",
        "```text",
        "使用 $paper-lookup。我的目标是核对这批论文的标题、年份、会议和 DOI。",
        "材料在：<文件路径>。输出 Markdown 表格并附原始来源链接。",
        "无法核实的字段标为“未核实”，不要根据标题猜测。",
        "```",
        "",
        "如果不知道技能名，先从下面的分类进入。一个任务通常只需一个主 skill；需要跨阶段工作时，再按“检索 → 分析 → 写作 → 审核”的顺序组合。",
        "",
        "## 先找大套件还是直接找小 Skill",
        "",
        "- 任务跨度很大，例如“从找选题一直做到论文”，先用大套件的总入口。",
        "- 任务很具体，例如“核对 DOI”或“分析单细胞数据”，直接调用对应小 skill。",
        "- 不清楚小 skill 属于哪里时，打开[技能套件与总入口导航](技能套件导航.md)。",
        "",
        "| 主要技能套件 | 数量 | 推荐总入口 |",
        "| --- | ---: | --- |",
    ]
    for suite in SUITES:
        entry = f"`{suite.entry}`" if suite.entry.startswith("$") else suite.entry
        lines.append(f"| [{suite.title}](技能套件导航.md#{suite_anchor(suite.slug)}) | {suite_counts[suite.slug]} | {entry} |")
    lines.extend([
        "",
        "## 分类导航",
        "",
        "| 分类 | 数量 | 适合解决的问题 |",
        "| --- | ---: | --- |",
    ])
    for category in CATEGORIES:
        lines.append(f"| [{category.title}](categories/{category.slug}.md) | {counts[category.slug]} | {category.explanation} |")
    lines.extend(
        [
            "",
            "## 选择技能的实用顺序",
            "",
            "1. 先按任务类型选分类，不要仅凭软件名字选择。",
            "2. 打开分类页，看“一句话理解”和原始说明，确认能力边界。",
            "3. 复制提示词模板，替换目标、文件路径、数据和约束。",
            "4. 涉及联网、API、云平台、实验提交、长时间训练或外部写入时，先让 Codex做只读检查和影响说明。",
            "5. 对引用、实验数字、医学信息和合规结论，始终回到原始证据复核。",
            "",
            "## 常见组合",
            "",
            "| 研究阶段 | 常见组合 |",
            "| --- | --- |",
            "| 从选题到文献综述 | 文献检索类 → 研究创意/假设类 → 综述写作类 |",
            "| 从数据到论文结果 | 学科数据处理类 → 统计/机器学习类 → 可视化类 → 论文写作类 |",
            "| 从模型训练到报告 | LLM 训练类 → 实验监控/结果分析类 → 评测类 → 论文写作类 |",
            "| 数学建模竞赛 | 工作流入口 → 赛题分析 → 编程求解 → 图表/流程图 → 写作 → 验收 |",
            "| 投稿前检查 | 引用核对 → 统计审计 → 审稿/反方论证 → 格式检查 |",
            "",
            "## 重要边界",
            "",
            "- skill 是工作说明，不保证 Python 包、模型、数据库权限、API 密钥或 GPU 已准备好。",
            "- 同名或相近 skills 可能来自不同项目。以本指南记录的全局目录和原始说明为准。",
            "- `_references` 是共享知识库，通常由其他数学建模 skills 自动读取，不需要手动调用。",
            "- 新安装或升级 skill 后，重新运行 `python3 scripts/build_skill_docs.py` 可刷新本仓库。",
            "",
            "完整字母索引见：[技能总索引](技能总索引.md)。",
            "",
        ]
    )
    return "\n".join(lines)


def render_readme(skills: list[Skill]) -> str:
    counts = Counter(skill.category for skill in skills)
    suite_counts = Counter(skill.suite for skill in skills)
    popular = [
        ("查论文与核对 DOI", "paper-lookup / literature-review / arxiv / nature-academic-search"),
        ("写论文与审稿", "scientific-writing / nature-writing / ml-paper-writing / peer-review"),
        ("做统计与画图", "statistical-analysis / scientific-visualization / matplotlib / seaborn"),
        ("做生物信息分析", "scanpy / biopython / bulk-rnaseq / pathway-enrichment"),
        ("训练与评测 LLM", "transformers / axolotl / deepspeed / vllm / lm-evaluation-harness"),
        ("参加数学建模竞赛", "1start-mathmodel / bzd-modeling-workflow / hwb-modeling-workflow"),
    ]
    lines = [
        "# 全局科研 Skills 中文使用说明",
        "",
        f"这里整理了当前 Codex 全局安装目录中的 **{len(skills)} 个科研及科研支撑 skills**，并把每个 skill 的用途、调用方法、注意事项和提示词模板写成中文。",
        "",
        "## 从这里开始",
        "",
        "- [按研究任务选择 Skill](docs/全局科研Skills使用指南.md)",
        "- [按所属技能套件和总入口查找](docs/技能套件导航.md)",
        "- [查看全部 Skills 字母索引](docs/技能总索引.md)",
        "- [查看生成规则与维护方法](docs/维护与更新.md)",
        "",
        "最快的调用方式：",
        "",
        "```text",
        "使用 $技能名。我的目标是：<具体任务>。",
        "材料在：<文件或目录路径>。",
        "请输出：<格式>；不要编造数据、引用或运行结果。",
        "```",
        "",
        "## 常见任务入口",
        "",
        "| 我想做什么 | 可以先看这些 Skills |",
        "| --- | --- |",
    ]
    for task, names in popular:
        lines.append(f"| {task} | `{names}` |")
    lines.extend(["", "## 主要技能套件与总入口", "", "| 技能套件 | 小 Skills 数量 | 推荐总入口 |", "| --- | ---: | --- |"])
    for suite in SUITES:
        entry = f"`{suite.entry}`" if suite.entry.startswith("$") else suite.entry
        lines.append(f"| [{suite.title}](docs/技能套件导航.md#{suite_anchor(suite.slug)}) | {suite_counts[suite.slug]} | {entry} |")
    lines.extend(["", "## 分类", "", "| 分类 | Skills 数量 |", "| --- | ---: |"])
    for category in CATEGORIES:
        lines.append(f"| [{category.title}](docs/categories/{category.slug}.md) | {counts[category.slug]} |")
    lines.extend(
        [
            "",
            "## 范围说明",
            "",
            f"本仓库以 `{SKILLS_DISPLAY}/*/SKILL.md` 为扫描范围，排除 Codex 的 `.system` 内置目录；其余直接安装在全局目录中的 skills 全部收录。某些技能更偏工具、基础设施或质量保障，也一并保留，因为它们常是科研流程的一部分。",
            "",
            f"当前快照日期：**{date.today().isoformat()}**。技能升级后，可运行仓库内的生成脚本刷新文档。",
            "",
        ]
    )
    return "\n".join(lines)


def render_maintenance(skills: list[Skill]) -> str:
    return f"""# 维护与更新

本文档由 `scripts/build_skill_docs.py` 从全局 skill 目录生成。

## 当前规则

- 默认扫描路径：`{SKILLS_DISPLAY}/*/SKILL.md`
- 收录数量：{len(skills)}
- 排除项：`.system` 内置目录
- 分类依据：目录名、frontmatter 中的 `name` 与 `description`
- 套件归属：优先读取作者/套件元数据，再使用明确的目录前缀和已知安装清单；无法可靠判断时标为“独立或暂未归入大型套件”
- 原始说明：完整保留在每个 skill 的折叠区域，便于核对自动中文解释

## 刷新方法

```bash
python3 scripts/build_skill_docs.py
```

如需扫描另一台机器的全局目录：

```bash
GLOBAL_SKILLS_ROOT=/path/to/skills python3 scripts/build_skill_docs.py
```

生成后检查：

```bash
git diff --check
git status --short
```

自动分类只负责导航，不改变 skill 本身。遇到跨学科技能时，应以分类页中的“技能原始说明”和实际 `SKILL.md` 为准。
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    skills = load_skills()
    if not skills:
        raise SystemExit(f"No skills found under {SKILLS_ROOT}")

    CATEGORY_ROOT.mkdir(parents=True, exist_ok=True)
    DATA_ROOT.mkdir(parents=True, exist_ok=True)

    grouped = {category.slug: [] for category in CATEGORIES}
    for skill in skills:
        grouped[skill.category].append(skill)

    write(REPO_ROOT / "README.md", render_readme(skills))
    write(DOCS_ROOT / "全局科研Skills使用指南.md", render_guide(skills))
    write(DOCS_ROOT / "技能总索引.md", render_index(skills))
    write(DOCS_ROOT / "技能套件导航.md", render_suites(skills))
    write(DOCS_ROOT / "维护与更新.md", render_maintenance(skills))

    for category in CATEGORIES:
        category_skills = sorted(grouped[category.slug], key=lambda item: item.name.lower())
        write(CATEGORY_ROOT / f"{category.slug}.md", render_category(category, category_skills))

    payload = [
        {
            "directory": skill.directory,
            "name": skill.name,
            "description": skill.description,
            "category": skill.category,
            "suite": skill.suite,
            "suite_title": SUITE_BY_SLUG[skill.suite].title,
            "recommended_entry": SUITE_BY_SLUG[skill.suite].entry,
            "upstream": skill.upstream,
        }
        for skill in skills
    ]
    write(DATA_ROOT / "global-skills.json", json.dumps(payload, ensure_ascii=False, indent=2))

    write(
        DOCS_ROOT / "三个科研技能使用指南.md",
        """# 原三套科研技能指南已扩展

本仓库现已从“三套技能”扩展为全部全局科研及科研支撑 skills 的中文指南。

- [进入新的完整使用指南](全局科研Skills使用指南.md)
- [按所属技能套件和总入口查找](技能套件导航.md)
- [查看全部 Skills 字母索引](技能总索引.md)

保留本页面是为了让旧链接仍然可用。
""",
    )

    print(f"Generated documentation for {len(skills)} skills in {len(CATEGORIES)} categories.")


if __name__ == "__main__":
    main()
