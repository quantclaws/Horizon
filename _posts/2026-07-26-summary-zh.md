---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> From 10 items, 6 important content pieces were selected

---

1. [vLLM v0.26.0 发布，支持 Inkling 模型并带来性能增强](#item-1) ⭐️ 8.0/10
2. [通用汽车支持钠离子电池用于美国电网储存](#item-2) ⭐️ 8.0/10
3. [Claude 5 生成模型的上下文工程新规则](#item-3) ⭐️ 8.0/10
4. [开放权重 AI 正迎来其 Kubernetes 时刻](#item-4) ⭐️ 8.0/10
5. [谷歌可能很快限制 Android 上的设备端 ADB 访问](#item-5) ⭐️ 8.0/10
6. [Ruff v0.16.0 将默认规则扩展至 413 项，导致 CI 流程中断](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布，支持 Inkling 模型并带来性能增强](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 新增了 Inkling 模型族的完整支持、DeepSeek‑V4 性能优化、用于生成模型的 fp32 lm_head，以及包括每 KV 缓存组可选注意力后端和 Rust 前端多模态视频/音频在内的多项后端改进。 此次发布显著推进了广泛使用的 LLM 推理库，使其能够高效服务于新的 1T 参数多模态模型，并在 NVIDIA、AMD 和 XPU 硬件上实现可测量的加速，对科研人员和生产用户均有利。 Inkling 支持包含 Hopper FA4 相对注意力、分段 CUDA 图、MTP=1 猜测解码、LoRA 以及标准 ModelOpt NVFP4 量化；fp32 lm_head 通过 head_dtype 选项暴露并扩展到 LoRA 路径；注意力后端现在可以按 KV 缓存组选择，Rust 前端新增了多模态视频/音频处理以及原生 vllm‑bench 工具。

github · khluu · Jul 25, 10:38

**背景**: vLLM 是一种高吞吐、内存高效的 LLM 服务库，采用 PagedAttention、CUDA 图和量化等技术降低延迟。ModelOpt 的 NVFP4 格式在 Blackwell GPU 上提供 4 位浮点量化，在保持动态范围的同时降低内存带宽。Hopper 的 FA4 相对注意力内核通过异步执行和 warp 专业化加速 H100/H200 GPU 上的注意力层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance</a></li>
<li><a href="https://build.nvidia.com/spark/nvfp4-quantization">NVFP4 Quantization | DGX Spark</a></li>
<li><a href="https://github.com/vllm-project/vllm/blob/main/vllm/models/inkling/nvidia/ops/fa4_rel_attention.py">vllm/vllm/models/inkling/nvidia/ops/fa4_rel_attention.py at ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release notes`, `#performance optimization`, `#model support`

---

<a id="item-2"></a>
## [通用汽车支持钠离子电池用于美国电网储存](https://spectrum.ieee.org/sodium-ion-battery-peak-energy) ⭐️ 8.0/10

通用汽车正在支持钠离子电池开发商 Peak Energy，将该技术用于美国大规模电网储存，并称其循环效率可达 96 % 且成本前景良好。 通用汽车的背书可能会加速钠离子电池在固定储存中的应用，减少对锂的依赖，降低电网规模储存成本，并推动国内供应链的发展。 钠离子电池的工作原理类似于锂离子电池，但使用 Na+ 作为载流子，循环效率约为 96 %，材料成本较低，极端温度下表现更好，但能量密度仍低于锂离子电池且大规模产能有限。

hackernews · rbanffy · Jul 25, 21:48 · [社区讨论](https://news.ycombinator.com/item?id=49051947)

**背景**: 钠离子电池是一种可充电电池，通过在电极之间移动钠离子来存储和释放能量，其工作原理与锂离子电池类似，只是使用钠作为嵌入离子。目前钠离子电池占全球电池市场不到 1 %，但分析师预测其市场份额在未来十年内可能达到 15.5 %。电网规模储能系统会在可再生能源发电过剩时储存电力，并在需要时释放以平衡电网的供需。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sodium-ion_battery">Sodium-ion battery - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grid_energy_storage">Grid energy storage - Wikipedia</a></li>
<li><a href="https://cen.acs.org/energy/energy-storage-/Sodium-ion-batteries-Should-believe/103/web/2025/11">Sodium-ion batteries: Should we believe the hype?</a></li>

</ul>
</details>

**社区讨论**: 有评论者怀疑通用汽车的举动只是把中国制造的硬件贴上‘美国制造’的标签；也有人认为如果钠离子电池成本与目前用于电网储存的 LFP 电池相当，则具备成本优势。此外，与会者指出其高达 96 % 的循环效率、消费者对家用钠离子电池的兴趣，以及回忆起一家需要 500 万美元桥梁贷款的美国钠离子电池初创公司最终被卖为废铁的案例。

**标签**: `#sodium-ion batteries`, `#grid storage`, `#GM`, `#energy storage`, `#battery technology`

---

<a id="item-3"></a>
## [Claude 5 生成模型的上下文工程新规则](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 8.0/10

Anthropic 发布了专为 Claude 5 代模型设计的新提示和上下文窗口工程指南，透露他们在 Claude Opus 5 和 Claude Fable 5 等模型上删除了超过 80% 的 Claude Code 系统提示，且编码性能没有可测量的下降。 这些新规则预示着向更精简系统提示的转变，可能降低 token 开销并影响开发者对高级 LLM 的提示设计，同时也引发了对供应商特定工具依赖和潜在供应商锁定的讨论。 该指南指出 Claude Opus 5 和 Claude Fable 5 在仅保留原始 Claude Code 系统提示的 20% 以下时仍能有效工作，但社区成员警告过度依赖 Claude 的自动记忆可能导致不合理的跳跃，且由于频繁重试 token 使用量可能上升。

hackernews · mellosouls · Jul 25, 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**背景**: 上下文工程涉及在大型语言模型推理过程中策划和维护最优的 token 集合，超越简单的提示设计，还包括外部信息。上下文窗口是指大型语言模型一次能处理的最大 token 长度输入，决定了模型在生成响应时能“看到”多少信息。Claude 5 代模型（如 Claude Opus 5 和 Claude Fable 5）是 Anthropic 最新系列，相较于早期版本（如 Claude Opus 4.8）性能有所提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models">The new rules of context engineering for Claude 5 generation models | Claude by Anthropic</a></li>
<li><a href="https://blog.bytebytego.com/p/a-guide-to-context-engineering-for">A Guide to Context Engineering for LLMs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Context_window">Context window - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者反应不一：有人主张使用专门的、关键词极少的语言来精确编码需求，而另一些人则批评对 Claude 自动记忆的过度依赖不透明且易出错。还有人指出 token 消耗增加、意外删除，并认为新指南是在向供应商特定工具靠拢，可能加剧锁定。

**标签**: `#LLM`, `#prompt engineering`, `#Claude`, `#AI`, `#context window`

---

<a id="item-4"></a>
## [开放权重 AI 正迎来其 Kubernetes 时刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

文章于 2026 年 7 月 25 日指出，开放权重 AI 正成为类似 Kubernetes 的共享基础设施，促进协作和成本透明。 此类比表明开放权重模型有望降低供应商锁定、普及前沿 AI 访问，并推动透明定价及类似开源软件的协同开发。 开放权重仅指模型权重公开，而非训练数据或代码；可通过 Ollama、LM Studio 等工具在本地运行；但权重本身无法标示模型国籍，要想达到类似 Kubernetes 的地位，还需公开训练数据并获得广泛产业协作。

hackernews · tknaup · Jul 25, 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 指的是模型的学习参数（权重）公开，使他人能够在不获得原始训练数据或代码的情况下运行和微调模型，正如行业解释所述。AI 中的 tokenomics 研究基础模型中 token 使用、计算和定价的经济学，旨在为波动的 API 成本带来理性。AI 模型治理涵盖模型开发、部署和风险管理的政策与实践，以确保可信度和合规性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://arxiv.org/abs/2606.24616">[2606.24616] AI Tokenomics: The Economics of Tokens ...</a></li>
<li><a href="https://www.informatica.com/resources/articles/ai-governance-explained.html">AI Governance : Best Practices and Importance | Informatica</a></li>

</ul>
</details>

**社区讨论**: 评论者认为按国籍禁用模型在技术上不可行，因为权重只是数字；他们指出 AI token 定价持续波动，视开放权重为提供成本基准的可能途径；并强调要实现类似 Kubernetes 的协作，需要公开训练数据和广泛产业贡献，同时指出现有来自 OpenAI 等实验室的开放模型虽有价值但更新频率低。

**标签**: `#open-weight AI`, `#Kubernetes analogy`, `#AI policy`, `#model governance`, `#tokenomics`

---

<a id="item-5"></a>
## [谷歌可能很快限制 Android 上的设备端 ADB 访问](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

谷歌正在考虑限制设备端 ADB 连接，以防止应用在手机上本地运行 ADB 客户端与 ADB 守护进程通信。 此限制将影响依赖设备端 ADB 实现无 root 功能的流行开发者工具（如 Shizuku 和 libadb），可能导致众多高级用户和隐私应用失效。 设备端 ADB 通过在手机上运行 ADB 客户端并连接到本地回环地址（127.0.0.1）实现；封锁它将阻止使用此回环方式的工具，但 USB ADB 仍可用。

hackernews · shscs911 · Jul 25, 06:57 · [社区讨论](https://news.ycombinator.com/item?id=49045159)

**背景**: Android 调试桥（ADB）是一种命令行工具，开发者用它通过 USB 或无线方式与 Android 设备进行调试和应用安装。除了在主机电脑上运行 ADB 客户端外，开发者还可以在设备本身运行 ADB 客户端，通过本地回环接口（127.0.0.1）连接到设备上的 ADB 守护进程，这种方式称为设备端 ADB。该机制使得 Shizuku 等无 root 工具能够为应用授予特权权限，从而孕育出一个庞大的高级用户和隐私应用生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/">Android May Soon Restrict On-Device ADB, Affecting Shizuku, libadb and Developers | Kitsumed Blog</a></li>
<li><a href="https://mangodeveloper.com/articles/android-may-soon-restrict-on-device-adb-stirring-developer-concern">Android May Soon Restrict On - Device ADB , Stirring Developer Concern</a></li>
<li><a href="https://provenbrief.com/story/google-s-plan-to-restrict-on-device-adb-could-kill-shizuku-and-an-entire-ecosyst">Google May Restrict Android ADB , Killing Shizuku Ecosystem</a></li>

</ul>
</details>

**社区讨论**: 评论者承认安全考虑，但指出攻击面很小，因为需要先打开开发者选项并启用远程 ADB，因此对大多数用户而言收益有限。许多人担心限制设备端 ADB 会破坏如 Shizuku 这样的关键开发者工具，影响高级用户的工作流程，并期待可能出现的绕过方案。还有人认为这符合谷歌逐步收紧 Android 开放性的更大趋势，甚至与 iOS 相比较。

**标签**: `#Android`, `#ADB`, `#security`, `#developer tools`, `#Hacker News`

---

<a id="item-6"></a>
## [Ruff v0.16.0 将默认规则扩展至 413 项，导致 CI 流程中断](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral 于 2026 年 7 月 23 日发布 Ruff v0.16.0，将默认 linting 规则从 59 条增加到 413 条。此变更导致许多现有 CI 流程因新启用的检查而失败。 此次扩展会暴露以前隐藏的语法和运行时错误，提升代码质量，但需要用户更新配置或锁定版本。这影响了广泛依赖 Ruff 进行 CI/CD linting 的 Python 开发者社区。 Ruff 现在默认启用 413 条规则，之前为 59 条；自 v0.1.0 以来，规则总数已从 708 增至 968。该版本还引入了 JSON 输出的小幅破坏性更改，某些字段可能为 null 而非空字符串。

rss · Simon Willison · Jul 25, 22:44

**背景**: Ruff 是一种用 Rust 编写的 Python 检查工具，提供快速的 linting 和自动修复功能，常被用作 Flake8、pylint、Black 等工具的替代品。它内置了数百条规则，涵盖代码风格、错误和安全问题，可通过 pyproject.toml 或命令行标志进行配置。在 CI 流程中，Ruff 常被用于在合并前强制执行代码质量。v0.16.0 版本是自 v0.1.0 以来首次对其默认规则集进行的重大更改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://astral.sh/blog/ruff-v0.16.0">Ruff v0.16.0 - Astral</a></li>
<li><a href="https://github.com/astral-sh/ruff/releases/tag/0.16.0">Release 0.16.0 · astral-sh/ruff</a></li>
<li><a href="https://docs.astral.sh/ruff/rules/">Rules | Ruff</a></li>

</ul>
</details>

**标签**: `#Python`, `#Linting`, `#Ruff`, `#Developer Tools`, `#CI/CD`

---