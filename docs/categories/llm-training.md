# AI/LLM 模型训练、压缩与推理

覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。

本页收录 **60** 个全局 skill。调用时优先写 `$技能名`；目录名与技能名不同的情况已单独标出。

## 本页索引

| Skill | 一句话理解 |
| --- | --- |
| [`$audiocraft-audio-generation`](#skill-audiocraft) | 围绕 `audiocraft-audio-generation` 的专项能力，主要用于生成音乐、语音或音效。 |
| [`$awq-quantization`](#skill-awq) | 围绕 `awq-quantization` 的专项能力，主要用于分析模型内部机制与可解释性，并可部署模型并优化推理。 |
| [`$axolotl`](#skill-axolotl) | 围绕 `axolotl` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。 |
| [`$blip-2-vision-language`](#skill-blip-2) | 围绕 `blip-2-vision-language` 的专项能力，主要用于处理图像与文本的多模态任务。 |
| [`$clip`](#skill-clip) | 围绕 `clip` 的专项能力，主要用于完成机器学习建模与评估，并可配置和执行模型微调。 |
| [`$deepspeed`](#skill-deepspeed) | 围绕 `deepspeed` 的专项能力，主要用于配置分布式或多 GPU 训练。 |
| [`$dhdna-profiler`](#skill-dhdna-profiler) | 围绕 `dhdna-profiler` 的专项能力，主要用于配置和执行模型微调。 |
| [`$distributed-llm-pretraining-torchtitan`](#skill-torchtitan) | 围绕 `distributed-llm-pretraining-torchtitan` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。 |
| [`$dse-loop`](#skill-dse-loop) | 围绕 `dse-loop` 的专项能力，主要用于配置和执行模型微调。 |
| [`$evaluating-cosmos-policy`](#skill-cosmos-policy) | 围绕 `evaluating-cosmos-policy` 的专项能力，主要用于部署模型并优化推理，并可使用云端或 GPU 计算资源。 |
| [`$fine-tuning-openvla-oft`](#skill-openvla-oft) | 围绕 `fine-tuning-openvla-oft` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。 |
| [`$fine-tuning-serving-openpi`](#skill-openpi) | 围绕 `fine-tuning-serving-openpi` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。 |
| [`$fine-tuning-with-trl`](#skill-trl-fine-tuning) | 围绕 `fine-tuning-with-trl` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。 |
| [`$gguf-quantization`](#skill-gguf) | 围绕 `gguf-quantization` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。 |
| [`$gptq`](#skill-gptq) | 围绕 `gptq` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。 |
| [`$grpo-rl-training`](#skill-grpo-rl-training) | 围绕 `grpo-rl-training` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。 |
| [`$hqq-quantization`](#skill-hqq) | 围绕 `hqq-quantization` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。 |
| [`$huggingface-accelerate`](#skill-accelerate) | 围绕 `huggingface-accelerate` 的专项能力，主要用于配置分布式或多 GPU 训练。 |
| [`$huggingface-tokenizers`](#skill-huggingface-tokenizers) | 围绕 `huggingface-tokenizers` 的专项能力，主要用于训练或使用文本分词器。 |
| [`$implementing-llms-litgpt`](#skill-litgpt) | 围绕 `implementing-llms-litgpt` 的专项能力，主要用于配置和执行模型微调。 |
| [`$knowledge-distillation`](#skill-knowledge-distillation) | 围绕 `knowledge-distillation` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。 |
| [`$llama-cpp`](#skill-llama-cpp) | 围绕 `llama-cpp` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。 |
| [`$llama-factory`](#skill-llama-factory) | 围绕 `llama-factory` 的专项能力，主要用于配置和执行模型微调。 |
| [`$llava`](#skill-llava) | 围绕 `llava` 的专项能力，主要用于处理图像与文本的多模态任务。 |
| [`$long-context`](#skill-long-context) | 这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `long-context` 相关任务。 |
| [`$mamba-architecture`](#skill-mamba) | 围绕 `mamba-architecture` 的专项能力，主要用于理解或实现模型架构，并可部署模型并优化推理。 |
| [`$miles-rl-training`](#skill-miles) | 围绕 `miles-rl-training` 的专项能力，主要用于进行模型后训练或强化学习，并可部署模型并优化推理。 |
| [`$ml-training-recipes`](#skill-ml-training-recipes) | 围绕 `ml-training-recipes` 的专项能力，主要用于配置和执行模型微调，并可使用云端或 GPU 计算资源。 |
| [`$model-merging`](#skill-model-merging) | 围绕 `model-merging` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。 |
| [`$model-pruning`](#skill-model-pruning) | 围绕 `model-pruning` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。 |
| [`$moe-training`](#skill-moe-training) | 围绕 `moe-training` 的专项能力，主要用于部署模型并优化推理，并可配置分布式或多 GPU 训练。 |
| [`$nanogpt`](#skill-nanogpt) | 围绕 `nanogpt` 的专项能力，主要用于理解或实现模型架构，并可配置分布式或多 GPU 训练。 |
| [`$nnsight-remote-interpretability`](#skill-nnsight) | 围绕 `nnsight-remote-interpretability` 的专项能力，主要用于分析模型内部机制与可解释性，并可使用云端或 GPU 计算资源。 |
| [`$openrlhf-training`](#skill-openrlhf) | 围绕 `openrlhf-training` 的专项能力，主要用于进行模型后训练或强化学习，并可配置分布式或多 GPU 训练。 |
| [`$optimizing-attention-flash`](#skill-flash-attention) | 围绕 `optimizing-attention-flash` 的专项能力，主要用于部署模型并优化推理，并可使用云端或 GPU 计算资源。 |
| [`$peft-fine-tuning`](#skill-peft) | 围绕 `peft-fine-tuning` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。 |
| [`$pufferlib`](#skill-pufferlib) | 围绕 `pufferlib` 的专项能力，主要用于进行模型后训练或强化学习。 |
| [`$pytorch-fsdp2`](#skill-pytorch-fsdp2) | 围绕 `pytorch-fsdp2` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。 |
| [`$pytorch-lightning`](#skill-pytorch-lightning) | 围绕 `pytorch-lightning` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。 |
| [`$pyvene-interventions`](#skill-pyvene) | 围绕 `pyvene-interventions` 的专项能力，主要用于分析模型内部机制与可解释性。 |
| [`$quantizing-models-bitsandbytes`](#skill-bitsandbytes) | 围绕 `quantizing-models-bitsandbytes` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。 |
| [`$ray-train`](#skill-ray-train) | 围绕 `ray-train` 的专项能力，主要用于配置分布式或多 GPU 训练。 |
| [`$rwkv-architecture`](#skill-rwkv) | 围绕 `rwkv-architecture` 的专项能力，主要用于部署模型并优化推理。 |
| [`$segment-anything-model`](#skill-segment-anything) | 这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `segment-anything-model` 相关任务。 |
| [`$sentencepiece`](#skill-sentencepiece) | 围绕 `sentencepiece` 的专项能力，主要用于训练或使用文本分词器。 |
| [`$serving-llms-vllm`](#skill-vllm) | 围绕 `serving-llms-vllm` 的专项能力，主要用于进行模型后训练或强化学习，并可部署模型并优化推理。 |
| [`$sglang`](#skill-sglang) | 围绕 `sglang` 的专项能力，主要用于部署模型并优化推理，并可使用云端或 GPU 计算资源。 |
| [`$simpo-training`](#skill-simpo) | 围绕 `simpo-training` 的专项能力，主要用于进行模型后训练或强化学习。 |
| [`$slime-rl-training`](#skill-slime) | 围绕 `slime-rl-training` 的专项能力，主要用于进行模型后训练或强化学习。 |
| [`$sparse-autoencoder-training`](#skill-saelens) | 围绕 `sparse-autoencoder-training` 的专项能力，主要用于分析模型内部机制与可解释性。 |
| [`$speculative-decoding`](#skill-speculative-decoding) | 围绕 `speculative-decoding` 的专项能力，主要用于部署模型并优化推理。 |
| [`$stable-diffusion-image-generation`](#skill-stable-diffusion) | 围绕 `stable-diffusion-image-generation` 的专项能力，主要用于生成或编辑图像。 |
| [`$tensorrt-llm`](#skill-tensorrt-llm) | 围绕 `tensorrt-llm` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。 |
| [`$torchforge-rl-training`](#skill-torchforge) | 这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `torchforge-rl-training` 相关任务。 |
| [`$training-llms-megatron`](#skill-megatron-core) | 围绕 `training-llms-megatron` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。 |
| [`$transformer-lens-interpretability`](#skill-transformer-lens) | 围绕 `transformer-lens-interpretability` 的专项能力，主要用于分析模型内部机制与可解释性。 |
| [`$transformers`](#skill-transformers) | 围绕 `transformers` 的专项能力，主要用于配置和执行模型微调，并可训练或使用文本分词器。 |
| [`$unsloth`](#skill-unsloth) | 围绕 `unsloth` 的专项能力，主要用于配置和执行模型微调。 |
| [`$verl-rl-training`](#skill-verl) | 围绕 `verl-rl-training` 的专项能力，主要用于进行模型后训练或强化学习。 |
| [`$whisper`](#skill-whisper) | 这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `whisper` 相关任务。 |

## 详细说明

<a id="skill-audiocraft"></a>
### `$audiocraft-audio-generation`

- 全局目录：`~/.codex/skills/audiocraft/`
- 中文理解：围绕 `audiocraft-audio-generation` 的专项能力，主要用于生成音乐、语音或音效。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $audiocraft-audio-generation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen). Use when you need to generate music from text descriptions, create sound effects, or perform melody-conditioned music generation.

</details>

上游线索：[https://github.com/facebookresearch/audiocraft.git](https://github.com/facebookresearch/audiocraft.git)

<a id="skill-awq"></a>
### `$awq-quantization`

- 全局目录：`~/.codex/skills/awq/`
- 中文理解：围绕 `awq-quantization` 的专项能力，主要用于分析模型内部机制与可解释性，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $awq-quantization。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. Use when deploying large models (7B-70B) on limited GPU memory, when you need faster inference than GPTQ with better accuracy preservation, or for instruction-tuned and multimodal models. MLSys 2024 Best Paper Award winner.

</details>

上游线索：[https://github.com/vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor)

<a id="skill-axolotl"></a>
### `$axolotl`

- 全局目录：`~/.codex/skills/axolotl/`
- 中文理解：围绕 `axolotl` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $axolotl。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support

</details>

上游线索：[https://github.com/axolotl-ai-cloud/diff-transformer](https://github.com/axolotl-ai-cloud/diff-transformer)

<a id="skill-blip-2"></a>
### `$blip-2-vision-language`

- 全局目录：`~/.codex/skills/blip-2/`
- 中文理解：围绕 `blip-2-vision-language` 的专项能力，主要用于处理图像与文本的多模态任务。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $blip-2-vision-language。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Vision-language pre-training framework bridging frozen image encoders and LLMs. Use when you need image captioning, visual question answering, image-text retrieval, or multimodal chat with state-of-the-art zero-shot performance.

</details>

上游线索：[https://github.com/salesforce/LAVIS](https://github.com/salesforce/LAVIS)

<a id="skill-clip"></a>
### `$clip`

- 全局目录：`~/.codex/skills/clip/`
- 中文理解：围绕 `clip` 的专项能力，主要用于完成机器学习建模与评估，并可配置和执行模型微调。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $clip。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks without fine-tuning. Best for general-purpose image understanding.

</details>

上游线索：[https://github.com/openai/CLIP.git](https://github.com/openai/CLIP.git)

<a id="skill-deepspeed"></a>
### `$deepspeed`

- 全局目录：`~/.codex/skills/deepspeed/`
- 中文理解：围绕 `deepspeed` 的专项能力，主要用于配置分布式或多 GPU 训练。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $deepspeed。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Expert guidance for distributed training with DeepSpeed - ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8, 1-bit Adam, sparse attention

</details>

<a id="skill-dhdna-profiler"></a>
### `$dhdna-profiler`

- 全局目录：`~/.codex/skills/dhdna-profiler/`
- 中文理解：围绕 `dhdna-profiler` 的专项能力，主要用于配置和执行模型微调。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：论文、引用和结论必须回到原始来源核验，不要把摘要或模型回答当作最终证据。

可复制提示词：

```text
使用 $dhdna-profiler。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Applies the DHDNA framework as an exploratory rubric for reasoning and writing patterns in supplied text. Used for explicit requests for DHDNA, cognitive-style reflection, a thinking-pattern profile, or comparisons of textual reasoning. Scores describe evidence in the sample, not validated psychological traits or personal identity.

</details>

<a id="skill-torchtitan"></a>
### `$distributed-llm-pretraining-torchtitan`

- 全局目录：`~/.codex/skills/torchtitan/`
- 中文理解：围绕 `distributed-llm-pretraining-torchtitan` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $distributed-llm-pretraining-torchtitan。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP). Use when pretraining Llama 3.1, DeepSeek V3, or custom models at scale from 8 to 512+ GPUs with Float8, torch.compile, and distributed checkpointing.

</details>

上游线索：[https://github.com/pytorch/torchtitan](https://github.com/pytorch/torchtitan)

<a id="skill-dse-loop"></a>
### `$dse-loop`

- 全局目录：`~/.codex/skills/dse-loop/`
- 中文理解：围绕 `dse-loop` 的专项能力，主要用于配置和执行模型微调。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $dse-loop。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Autonomous design space exploration loop for computer architecture and EDA. Runs a program, analyzes results, tunes parameters, and iterates until objective is met or timeout. Use when user says \"DSE\", \"design space exploration\", \"sweep parameters\", \"optimize\", \"find best config\", or wants iterative parameter tuning.

</details>

<a id="skill-cosmos-policy"></a>
### `$evaluating-cosmos-policy`

- 全局目录：`~/.codex/skills/cosmos-policy/`
- 中文理解：围绕 `evaluating-cosmos-policy` 的专项能力，主要用于部署模型并优化推理，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $evaluating-cosmos-policy。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Evaluates NVIDIA Cosmos Policy on LIBERO and RoboCasa simulation environments. Use when setting up cosmos-policy for robot manipulation evaluation, running headless GPU evaluations with EGL rendering, or profiling inference latency on cluster or local GPU machines.

</details>

上游线索：[https://github.com/moojink/robocasa-cosmos-policy.git](https://github.com/moojink/robocasa-cosmos-policy.git)

<a id="skill-openvla-oft"></a>
### `$fine-tuning-openvla-oft`

- 全局目录：`~/.codex/skills/openvla-oft/`
- 中文理解：围绕 `fine-tuning-openvla-oft` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $fine-tuning-openvla-oft。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA adaptation, and FiLM conditioning on LIBERO simulation and ALOHA real-world setups. Use when reproducing OpenVLA-OFT paper results, training custom VLA action heads (L1 or diffusion), deploying server-client inference for ALOHA, or debugging normalization, LoRA merge, and cross-GPU issues.

</details>

上游线索：[https://github.com/moojink/openvla-oft.git](https://github.com/moojink/openvla-oft.git)

<a id="skill-openpi"></a>
### `$fine-tuning-serving-openpi`

- 全局目录：`~/.codex/skills/openpi/`
- 中文理解：围绕 `fine-tuning-serving-openpi` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $fine-tuning-serving-openpi。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fine-tune and serve Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) using JAX or PyTorch backends for robot policy inference across ALOHA, DROID, and LIBERO environments. Use when adapting pi0 models to custom datasets, converting JAX checkpoints to PyTorch, running policy inference servers, or debugging norm stats and GPU memory issues.

</details>

上游线索：[https://github.com/Physical-Intelligence/openpi.git](https://github.com/Physical-Intelligence/openpi.git)

<a id="skill-trl-fine-tuning"></a>
### `$fine-tuning-with-trl`

- 全局目录：`~/.codex/skills/trl-fine-tuning/`
- 中文理解：围绕 `fine-tuning-with-trl` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $fine-tuning-with-trl。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward model training. Use when need RLHF, align model with preferences, or train from human feedback. Works with HuggingFace Transformers.

</details>

上游线索：[https://github.com/huggingface/trl](https://github.com/huggingface/trl)

<a id="skill-gguf"></a>
### `$gguf-quantization`

- 全局目录：`~/.codex/skills/gguf/`
- 中文理解：围绕 `gguf-quantization` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $gguf-quantization。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2-8 bit without GPU requirements.

</details>

上游线索：[https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

<a id="skill-gptq"></a>
### `$gptq`

- 全局目录：`~/.codex/skills/gptq/`
- 中文理解：围绕 `gptq` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $gptq。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Post-training 4-bit quantization for LLMs with minimal accuracy loss. Use for deploying large models (70B, 405B) on consumer GPUs, when you need 4× memory reduction with <2% perplexity degradation, or for faster inference (3-4× speedup) vs FP16. Integrates with transformers and PEFT for QLoRA fine-tuning.

</details>

上游线索：[https://github.com/AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ)

<a id="skill-grpo-rl-training"></a>
### `$grpo-rl-training`

- 全局目录：`~/.codex/skills/grpo-rl-training/`
- 中文理解：围绕 `grpo-rl-training` 的专项能力，主要用于配置和执行模型微调，并可进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $grpo-rl-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training

</details>

上游线索：[https://github.com/huggingface/open-r1](https://github.com/huggingface/open-r1)

<a id="skill-hqq"></a>
### `$hqq-quantization`

- 全局目录：`~/.codex/skills/hqq/`
- 中文理解：围绕 `hqq-quantization` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $hqq-quantization。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Half-Quadratic Quantization for LLMs without calibration data. Use when quantizing models to 4/3/2-bit precision without needing calibration datasets, for fast quantization workflows, or when deploying with vLLM or HuggingFace Transformers.

</details>

上游线索：[https://github.com/mobiusml/hqq](https://github.com/mobiusml/hqq)

<a id="skill-accelerate"></a>
### `$huggingface-accelerate`

- 全局目录：`~/.codex/skills/accelerate/`
- 中文理解：围绕 `huggingface-accelerate` 的专项能力，主要用于配置分布式或多 GPU 训练。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $huggingface-accelerate。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Simplest distributed training API. 4 lines to add distributed support to any PyTorch script. Unified API for DeepSpeed/FSDP/Megatron/DDP. Automatic device placement, mixed precision (FP16/BF16/FP8). Interactive config, single launch command. HuggingFace ecosystem standard.

</details>

上游线索：[https://github.com/huggingface/accelerate](https://github.com/huggingface/accelerate)

<a id="skill-huggingface-tokenizers"></a>
### `$huggingface-tokenizers`

- 全局目录：`~/.codex/skills/huggingface-tokenizers/`
- 中文理解：围绕 `huggingface-tokenizers` 的专项能力，主要用于训练或使用文本分词器。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $huggingface-tokenizers。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fast tokenizers optimized for research and production. Rust-based implementation tokenizes 1GB in <20 seconds. Supports BPE, WordPiece, and Unigram algorithms. Train custom vocabularies, track alignments, handle padding/truncation. Integrates seamlessly with transformers. Use when you need high-performance tokenization or custom tokenizer training.

</details>

上游线索：[https://github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers)

<a id="skill-litgpt"></a>
### `$implementing-llms-litgpt`

- 全局目录：`~/.codex/skills/litgpt/`
- 中文理解：围绕 `implementing-llms-litgpt` 的专项能力，主要用于配置和执行模型微调。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $implementing-llms-litgpt。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Implements and trains LLMs using Lightning AI's LitGPT with 20+ pretrained architectures (Llama, Gemma, Phi, Qwen, Mistral). Use when need clean model implementations, educational understanding of architectures, or production fine-tuning with LoRA/QLoRA. Single-file implementations, no abstraction layers.

</details>

上游线索：[https://github.com/Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt)

<a id="skill-knowledge-distillation"></a>
### `$knowledge-distillation`

- 全局目录：`~/.codex/skills/knowledge-distillation/`
- 中文理解：围绕 `knowledge-distillation` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $knowledge-distillation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Compress large language models using knowledge distillation from teacher to student models. Use when deploying smaller models with retained performance, transferring GPT-4 capabilities to open-source models, or reducing inference costs. Covers temperature scaling, soft targets, reverse KLD, logit distillation, and MiniLLM training strategies.

</details>

上游线索：[https://github.com/microsoft/LMOps](https://github.com/microsoft/LMOps)

<a id="skill-llama-cpp"></a>
### `$llama-cpp`

- 全局目录：`~/.codex/skills/llama-cpp/`
- 中文理解：围绕 `llama-cpp` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $llama-cpp。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Runs LLM inference on CPU, Apple Silicon, and consumer GPUs without NVIDIA hardware. Use for edge deployment, M1/M2/M3 Macs, AMD/Intel GPUs, or when CUDA is unavailable. Supports GGUF quantization (1.5-8 bit) for reduced memory and 4-10× speedup vs PyTorch on CPU.

</details>

上游线索：[https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

<a id="skill-llama-factory"></a>
### `$llama-factory`

- 全局目录：`~/.codex/skills/llama-factory/`
- 中文理解：围绕 `llama-factory` 的专项能力，主要用于配置和执行模型微调。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $llama-factory。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Expert guidance for fine-tuning LLMs with LLaMA-Factory - WebUI no-code, 100+ models, 2/3/4/5/6/8-bit QLoRA, multimodal support

</details>

<a id="skill-llava"></a>
### `$llava`

- 全局目录：`~/.codex/skills/llava/`
- 中文理解：围绕 `llava` 的专项能力，主要用于处理图像与文本的多模态任务。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $llava。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Large Language and Vision Assistant. Enables visual instruction tuning and image-based conversations. Combines CLIP vision encoder with Vicuna/LLaMA language models. Supports multi-turn image chat, visual question answering, and instruction following. Use for vision-language chatbots or image understanding tasks. Best for conversational image analysis.

</details>

上游线索：[https://github.com/haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA)

<a id="skill-long-context"></a>
### `$long-context`

- 全局目录：`~/.codex/skills/long-context/`
- 中文理解：这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `long-context` 相关任务。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $long-context。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Extend context windows of transformer models using RoPE, YaRN, ALiBi, and position interpolation techniques. Use when processing long documents (32k-128k+ tokens), extending pre-trained models beyond original context limits, or implementing efficient positional encodings. Covers rotary embeddings, attention biases, interpolation methods, and extrapolation strategies for LLMs.

</details>

上游线索：[https://github.com/jquesnelle/yarn](https://github.com/jquesnelle/yarn)

<a id="skill-mamba"></a>
### `$mamba-architecture`

- 全局目录：`~/.codex/skills/mamba/`
- 中文理解：围绕 `mamba-architecture` 的专项能力，主要用于理解或实现模型架构，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $mamba-architecture。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

State-space model with O(n) complexity vs Transformers' O(n²). 5× faster inference, million-token sequences, no KV cache. Selective SSM with hardware-aware design. Mamba-1 (d_state=16) and Mamba-2 (d_state=128, multi-head). Models 130M-2.8B on HuggingFace.

</details>

上游线索：[https://github.com/state-spaces/mamba](https://github.com/state-spaces/mamba)

<a id="skill-miles"></a>
### `$miles-rl-training`

- 全局目录：`~/.codex/skills/miles/`
- 中文理解：围绕 `miles-rl-training` 的专项能力，主要用于进行模型后训练或强化学习，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $miles-rl-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime. Use when training large MoE models with FP8/INT4, needing train-inference alignment, or requiring speculative RL for maximum throughput.

</details>

上游线索：[https://github.com/radixark/miles.git](https://github.com/radixark/miles.git)

<a id="skill-ml-training-recipes"></a>
### `$ml-training-recipes`

- 全局目录：`~/.codex/skills/ml-training-recipes/`
- 中文理解：围绕 `ml-training-recipes` 的专项能力，主要用于配置和执行模型微调，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：医学输出仅用于科研和信息整理，不能替代临床判断。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $ml-training-recipes。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Battle-tested PyTorch training recipes for all domains — LLMs, vision, diffusion, medical imaging, protein/drug discovery, spatial omics, genomics. Covers training loops, optimizer selection (AdamW, Muon), LR scheduling, mixed precision, debugging, and systematic experimentation. Use when training or fine-tuning neural networks, debugging loss spikes or OOM, choosing architectures, or optimizing GPU throughput.

</details>

<a id="skill-model-merging"></a>
### `$model-merging`

- 全局目录：`~/.codex/skills/model-merging/`
- 中文理解：围绕 `model-merging` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $model-merging。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Merge multiple fine-tuned models using mergekit to combine capabilities without retraining. Use when creating specialized models by blending domain-specific expertise (math + coding + chat), improving performance beyond single models, or experimenting rapidly with model variants. Covers SLERP, TIES-Merging, DARE, Task Arithmetic, linear merging, and production deployment strategies.

</details>

上游线索：[https://github.com/arcee-ai/mergekit.git](https://github.com/arcee-ai/mergekit.git)

<a id="skill-model-pruning"></a>
### `$model-pruning`

- 全局目录：`~/.codex/skills/model-pruning/`
- 中文理解：围绕 `model-pruning` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $model-pruning。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Reduce LLM size and accelerate inference using pruning techniques like Wanda and SparseGPT. Use when compressing models without retraining, achieving 50% sparsity with minimal accuracy loss, or enabling faster inference on hardware accelerators. Covers unstructured pruning, structured pruning, N:M sparsity, magnitude pruning, and one-shot methods.

</details>

上游线索：[https://github.com/locuslab/wanda](https://github.com/locuslab/wanda)

<a id="skill-moe-training"></a>
### `$moe-training`

- 全局目录：`~/.codex/skills/moe-training/`
- 中文理解：围绕 `moe-training` 的专项能力，主要用于部署模型并优化推理，并可配置分布式或多 GPU 训练。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $moe-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Train Mixture of Experts (MoE) models using DeepSpeed or HuggingFace. Use when training large-scale models with limited compute (5× cost reduction vs dense models), implementing sparse architectures like Mixtral 8x7B or DeepSeek-V3, or scaling model capacity without proportional compute increase. Covers MoE architectures, routing mechanisms, load balancing, expert parallelism, and inference optimization.

</details>

上游线索：[https://github.com/microsoft/Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed)

<a id="skill-nanogpt"></a>
### `$nanogpt`

- 全局目录：`~/.codex/skills/nanogpt/`
- 中文理解：围绕 `nanogpt` 的专项能力，主要用于理解或实现模型架构，并可配置分布式或多 GPU 训练。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $nanogpt。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Educational GPT implementation in ~300 lines. Reproduces GPT-2 (124M) on OpenWebText. Clean, hackable code for learning transformers. By Andrej Karpathy. Perfect for understanding GPT architecture from scratch. Train on Shakespeare (CPU) or OpenWebText (multi-GPU).

</details>

上游线索：[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

<a id="skill-nnsight"></a>
### `$nnsight-remote-interpretability`

- 全局目录：`~/.codex/skills/nnsight/`
- 中文理解：围绕 `nnsight-remote-interpretability` 的专项能力，主要用于分析模型内部机制与可解释性，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $nnsight-remote-interpretability。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for interpreting and manipulating neural network internals using nnsight with optional NDIF remote execution. Use when needing to run interpretability experiments on massive models (70B+) without local GPU resources, or when working with any PyTorch architecture.

</details>

上游线索：[https://github.com/ndif-team/nnsight](https://github.com/ndif-team/nnsight)

<a id="skill-openrlhf"></a>
### `$openrlhf-training`

- 全局目录：`~/.codex/skills/openrlhf/`
- 中文理解：围绕 `openrlhf-training` 的专项能力，主要用于进行模型后训练或强化学习，并可配置分布式或多 GPU 训练。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $openrlhf-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

High-performance RLHF framework with Ray+vLLM acceleration. Use for PPO, GRPO, RLOO, DPO training of large models (7B-70B+). Built on Ray, vLLM, ZeRO-3. 2× faster than DeepSpeedChat with distributed architecture and GPU resource sharing.

</details>

上游线索：[https://github.com/OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

<a id="skill-flash-attention"></a>
### `$optimizing-attention-flash`

- 全局目录：`~/.codex/skills/flash-attention/`
- 中文理解：围绕 `optimizing-attention-flash` 的专项能力，主要用于部署模型并优化推理，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $optimizing-attention-flash。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Optimizes transformer attention with Flash Attention for 2-4x speedup and 10-20x memory reduction. Use when training/running transformers with long sequences (>512 tokens), encountering GPU memory issues with attention, or need faster inference. Supports PyTorch native SDPA, flash-attn library, H100 FP8, and sliding window attention.

</details>

上游线索：[https://github.com/Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)

<a id="skill-peft"></a>
### `$peft-fine-tuning`

- 全局目录：`~/.codex/skills/peft/`
- 中文理解：围绕 `peft-fine-tuning` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $peft-fine-tuning。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter serving. HuggingFace's official library integrated with transformers ecosystem.

</details>

上游线索：[https://github.com/huggingface/peft](https://github.com/huggingface/peft)

<a id="skill-pufferlib"></a>
### `$pufferlib`

- 全局目录：`~/.codex/skills/pufferlib/`
- 中文理解：围绕 `pufferlib` 的专项能力，主要用于进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pufferlib。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, PuffeRL training, evaluation, and safe checkpoint review. Covers the native 5.0 build and environment API, published 3.0.0 Gymnasium/PettingZoo adaptation, and a pinned historical 4.0 profile.

</details>

上游线索：[https://github.com/PufferAI/PufferLib.git](https://github.com/PufferAI/PufferLib.git)

<a id="skill-pytorch-fsdp2"></a>
### `$pytorch-fsdp2`

- 全局目录：`~/.codex/skills/pytorch-fsdp2/`
- 中文理解：围绕 `pytorch-fsdp2` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pytorch-fsdp2。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Adds PyTorch FSDP2 (fully_shard) to training scripts with correct init, sharding, mixed precision/offload config, and distributed checkpointing. Use when models exceed single-GPU memory or when you need DTensor-based sharding with DeviceMesh.

</details>

<a id="skill-pytorch-lightning"></a>
### `$pytorch-lightning`

- 全局目录：`~/.codex/skills/pytorch-lightning/`
- 中文理解：围绕 `pytorch-lightning` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pytorch-lightning。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Deep learning framework (PyTorch Lightning / lightning package). Organize PyTorch code into LightningModules, configure Trainers for multi-GPU/TPU, implement data pipelines, callbacks, logging (W&B, TensorBoard, MLflow), distributed training (DDP, FSDP, DeepSpeed), for scalable neural network training.

</details>

上游线索：[https://github.com/Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)

<a id="skill-pyvene"></a>
### `$pyvene-interventions`

- 全局目录：`~/.codex/skills/pyvene/`
- 中文理解：围绕 `pyvene-interventions` 的专项能力，主要用于分析模型内部机制与可解释性。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $pyvene-interventions。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for performing causal interventions on PyTorch models using pyvene's declarative intervention framework. Use when conducting causal tracing, activation patching, interchange intervention training, or testing causal hypotheses about model behavior.

</details>

上游线索：[https://github.com/stanfordnlp/pyvene](https://github.com/stanfordnlp/pyvene)

<a id="skill-bitsandbytes"></a>
### `$quantizing-models-bitsandbytes`

- 全局目录：`~/.codex/skills/bitsandbytes/`
- 中文理解：围绕 `quantizing-models-bitsandbytes` 的专项能力，主要用于配置和执行模型微调，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $quantizing-models-bitsandbytes。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Quantizes LLMs to 8-bit or 4-bit for 50-75% memory reduction with minimal accuracy loss. Use when GPU memory is limited, need to fit larger models, or want faster inference. Supports INT8, NF4, FP4 formats, QLoRA training, and 8-bit optimizers. Works with HuggingFace Transformers.

</details>

上游线索：[https://github.com/bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes)

<a id="skill-ray-train"></a>
### `$ray-train`

- 全局目录：`~/.codex/skills/ray-train/`
- 中文理解：围绕 `ray-train` 的专项能力，主要用于配置分布式或多 GPU 训练。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $ray-train。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Distributed training orchestration across clusters. Scales PyTorch/TensorFlow/HuggingFace from laptop to 1000s of nodes. Built-in hyperparameter tuning with Ray Tune, fault tolerance, elastic scaling. Use when training massive models across multiple machines or running distributed hyperparameter sweeps.

</details>

上游线索：[https://github.com/ray-project/ray](https://github.com/ray-project/ray)

<a id="skill-rwkv"></a>
### `$rwkv-architecture`

- 全局目录：`~/.codex/skills/rwkv/`
- 中文理解：围绕 `rwkv-architecture` 的专项能力，主要用于部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $rwkv-architecture。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

RNN+Transformer hybrid with O(n) inference. Linear time, infinite context, no KV cache. Train like GPT (parallel), infer like RNN (sequential). Linux Foundation AI project. Production at Windows, Office, NeMo. RWKV-7 (March 2025). Models up to 14B parameters.

</details>

上游线索：[https://github.com/BlinkDL/RWKV-LM](https://github.com/BlinkDL/RWKV-LM)

<a id="skill-segment-anything"></a>
### `$segment-anything-model`

- 全局目录：`~/.codex/skills/segment-anything/`
- 中文理解：这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `segment-anything-model` 相关任务。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $segment-anything-model。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Foundation model for image segmentation with zero-shot transfer. Use when you need to segment any object in images using points, boxes, or masks as prompts, or automatically generate all object masks in an image.

</details>

上游线索：[https://github.com/facebookresearch/segment-anything.git](https://github.com/facebookresearch/segment-anything.git)

<a id="skill-sentencepiece"></a>
### `$sentencepiece`

- 全局目录：`~/.codex/skills/sentencepiece/`
- 中文理解：围绕 `sentencepiece` 的专项能力，主要用于训练或使用文本分词器。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $sentencepiece。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Language-independent tokenizer treating text as raw Unicode. Supports BPE and Unigram algorithms. Fast (50k sentences/sec), lightweight (6MB memory), deterministic vocabulary. Used by T5, ALBERT, XLNet, mBART. Train on raw text without pre-tokenization. Use when you need multilingual support, CJK languages, or reproducible tokenization.

</details>

上游线索：[https://github.com/google/sentencepiece.git](https://github.com/google/sentencepiece.git)

<a id="skill-vllm"></a>
### `$serving-llms-vllm`

- 全局目录：`~/.codex/skills/vllm/`
- 中文理解：围绕 `serving-llms-vllm` 的专项能力，主要用于进行模型后训练或强化学习，并可部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $serving-llms-vllm。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching. Use when deploying production LLM APIs, optimizing inference latency/throughput, or serving models with limited GPU memory. Supports OpenAI-compatible endpoints, quantization (GPTQ/AWQ/FP8), and tensor parallelism.

</details>

上游线索：[https://github.com/vllm-project/vllm](https://github.com/vllm-project/vllm)

<a id="skill-sglang"></a>
### `$sglang`

- 全局目录：`~/.codex/skills/sglang/`
- 中文理解：围绕 `sglang` 的专项能力，主要用于部署模型并优化推理，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $sglang。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Fast structured generation and serving for LLMs with RadixAttention prefix caching. Use for JSON/regex outputs, constrained decoding, agentic workflows with tool calls, or when you need 5× faster inference than vLLM with prefix sharing. Powers 300,000+ GPUs at xAI, AMD, NVIDIA, and LinkedIn.

</details>

上游线索：[https://github.com/sgl-project/sglang.git](https://github.com/sgl-project/sglang.git)

<a id="skill-simpo"></a>
### `$simpo-training`

- 全局目录：`~/.codex/skills/simpo/`
- 中文理解：围绕 `simpo-training` 的专项能力，主要用于进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $simpo-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Simple Preference Optimization for LLM alignment. Reference-free alternative to DPO with better performance (+6.4 points on AlpacaEval 2.0). No reference model needed, more efficient than DPO. Use for preference alignment when want simpler, faster training than DPO/PPO.

</details>

上游线索：[https://github.com/huggingface/alignment-handbook.git](https://github.com/huggingface/alignment-handbook.git)

<a id="skill-slime"></a>
### `$slime-rl-training`

- 全局目录：`~/.codex/skills/slime/`
- 中文理解：围绕 `slime-rl-training` 的专项能力，主要用于进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $slime-rl-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. Use when training GLM models, implementing custom data generation workflows, or needing tight Megatron-LM integration for RL scaling.

</details>

上游线索：[https://github.com/THUDM/slime.git](https://github.com/THUDM/slime.git)

<a id="skill-saelens"></a>
### `$sparse-autoencoder-training`

- 全局目录：`~/.codex/skills/saelens/`
- 中文理解：围绕 `sparse-autoencoder-training` 的专项能力，主要用于分析模型内部机制与可解释性。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $sparse-autoencoder-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations into interpretable features. Use when discovering interpretable features, analyzing superposition, or studying monosemantic representations in language models.

</details>

上游线索：[https://github.com/jbloomAus/SAELens](https://github.com/jbloomAus/SAELens)

<a id="skill-speculative-decoding"></a>
### `$speculative-decoding`

- 全局目录：`~/.codex/skills/speculative-decoding/`
- 中文理解：围绕 `speculative-decoding` 的专项能力，主要用于部署模型并优化推理。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。

可复制提示词：

```text
使用 $speculative-decoding。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Accelerate LLM inference using speculative decoding, Medusa multiple heads, and lookahead decoding techniques. Use when optimizing inference speed (1.5-3.6× speedup), reducing latency for real-time applications, or deploying models with limited compute. Covers draft models, tree-based attention, Jacobi iteration, parallel token generation, and production deployment strategies.

</details>

上游线索：[https://github.com/FasterDecoding/Medusa](https://github.com/FasterDecoding/Medusa)

<a id="skill-stable-diffusion"></a>
### `$stable-diffusion-image-generation`

- 全局目录：`~/.codex/skills/stable-diffusion/`
- 中文理解：围绕 `stable-diffusion-image-generation` 的专项能力，主要用于生成或编辑图像。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $stable-diffusion-image-generation。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines.

</details>

上游线索：[https://github.com/huggingface/diffusers](https://github.com/huggingface/diffusers)

<a id="skill-tensorrt-llm"></a>
### `$tensorrt-llm`

- 全局目录：`~/.codex/skills/tensorrt-llm/`
- 中文理解：围绕 `tensorrt-llm` 的专项能力，主要用于部署模型并优化推理，并可压缩模型并优化推理资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：可能需要账号、API 凭据、联网权限或付费资源；执行外部写入前先确认。 先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $tensorrt-llm。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency. Use for production deployment on NVIDIA GPUs (A100/H100), when you need 10-100x faster inference than PyTorch, or for serving models with quantization (FP8/INT4), in-flight batching, and multi-GPU scaling.

</details>

上游线索：[https://github.com/NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

<a id="skill-torchforge"></a>
### `$torchforge-rl-training`

- 全局目录：`~/.codex/skills/torchforge/`
- 中文理解：这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `torchforge-rl-training` 相关任务。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $torchforge-rl-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for PyTorch-native agentic RL using torchforge, Meta's library separating infra from algorithms. Use when you want clean RL abstractions, easy algorithm experimentation, or scalable training with Monarch and TorchTitan.

</details>

上游线索：[https://github.com/meta-pytorch/torchforge](https://github.com/meta-pytorch/torchforge)

<a id="skill-megatron-core"></a>
### `$training-llms-megatron`

- 全局目录：`~/.codex/skills/megatron-core/`
- 中文理解：围绕 `training-llms-megatron` 的专项能力，主要用于配置分布式或多 GPU 训练，并可使用云端或 GPU 计算资源。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $training-llms-megatron。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Trains large language models (2B-462B parameters) using NVIDIA Megatron-Core with advanced parallelism strategies. Use when training models >1B parameters, need maximum GPU efficiency (47% MFU on H100), or require tensor/pipeline/sequence/context/expert parallelism. Production-ready framework used for Nemotron, LLaMA, DeepSeek.

</details>

上游线索：[https://github.com/NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)

<a id="skill-transformer-lens"></a>
### `$transformer-lens-interpretability`

- 全局目录：`~/.codex/skills/transformer-lens/`
- 中文理解：围绕 `transformer-lens-interpretability` 的专项能力，主要用于分析模型内部机制与可解释性。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $transformer-lens-interpretability。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for mechanistic interpretability research using TransformerLens to inspect and manipulate transformer internals via HookPoints and activation caching. Use when reverse-engineering model algorithms, studying attention patterns, or performing activation patching experiments.

</details>

上游线索：[https://github.com/TransformerLensOrg/TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)

<a id="skill-transformers"></a>
### `$transformers`

- 全局目录：`~/.codex/skills/transformers/`
- 中文理解：围绕 `transformers` 的专项能力，主要用于配置和执行模型微调，并可训练或使用文本分词器。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $transformers。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Hugging Face Transformers for loading Hub models, running pipeline inference, text generation, and Trainer fine-tuning on NLP, vision, audio, and multimodal tasks. Applies when working with AutoModel, pipelines, tokenizers, generation configs, or TrainingArguments within Transformers.

</details>

上游线索：[https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)

<a id="skill-unsloth"></a>
### `$unsloth`

- 全局目录：`~/.codex/skills/unsloth/`
- 中文理解：围绕 `unsloth` 的专项能力，主要用于配置和执行模型微调。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $unsloth。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization

</details>

<a id="skill-verl"></a>
### `$verl-rl-training`

- 全局目录：`~/.codex/skills/verl/`
- 中文理解：围绕 `verl-rl-training` 的专项能力，主要用于进行模型后训练或强化学习。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：先核对硬件、依赖版本、运行时间和预算，再启动长任务。

可复制提示词：

```text
使用 $verl-rl-training。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL). Use when implementing RLHF, GRPO, PPO, or other RL algorithms for LLM post-training at scale with flexible infrastructure backends.

</details>

上游线索：[https://github.com/volcengine/verl.git](https://github.com/volcengine/verl.git)

<a id="skill-whisper"></a>
### `$whisper`

- 全局目录：`~/.codex/skills/whisper/`
- 中文理解：这是一个面向“AI/LLM 模型训练、压缩与推理”的专项技能，用于处理 `whisper` 相关任务。
- 适合何时使用：覆盖模型架构、微调、分布式训练、强化学习、量化、推理和部署。
- 使用前注意：技能说明不代表依赖、模型、数据或凭据已经安装；首次使用先让 Codex 检查环境。

可复制提示词：

```text
使用 $whisper。我的目标是：<具体任务>。
已有材料：<文件路径、数据、论文或代码>。
要求：提供模型、硬件、数据规模、训练目标和显存预算；先给兼容性与资源检查，再给配置。
如信息不足，请先列出缺口；不要编造数据、引用或运行结果。
```

<details>
<summary>查看技能原始说明（用于核对精确能力边界）</summary>

OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast transcription, or multilingual audio processing. Best for robust, multilingual ASR.

</details>

上游线索：[https://github.com/openai/whisper](https://github.com/openai/whisper)

---

[返回总览](../全局科研Skills使用指南.md) · [返回总索引](../技能总索引.md)
