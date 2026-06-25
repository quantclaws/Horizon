---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> From 35 items, 8 important content pieces were selected

---

1. [Polars 1.42.0 版本发布，新增离核溢出、严格模式及 SQL 隐式 JOIN 支持](#item-1) ⭐️ 8.0/10
2. [OpenAI 首次发布其定制 AI 推理芯片。](#item-2) ⭐️ 8.0/10
3. [Anthropic 指控阿里巴巴非法提取 Claude AI 模型能力](#item-3) ⭐️ 8.0/10
4. [高通计划以 40 亿美元收购 AI 初创公司 Modular](#item-4) ⭐️ 8.0/10
5. [NVIDIA 45°C 液冷架构将数据中心用水降至近零](#item-5) ⭐️ 8.0/10
6. [Nub：受 Bun 启发的 Node.js 一体化工具包，使用 --require 钩子](#item-6) ⭐️ 8.0/10
7. [AI 代币经济学：基础模型中的代币、计算与定价](#item-7) ⭐️ 8.0/10
8. [TIP-Search：面向不确定负载的市场预测时间可预测推理调度](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Polars 1.42.0 版本发布，新增离核溢出、严格模式及 SQL 隐式 JOIN 支持](https://github.com/pola-rs/polars/releases/tag/py-1.42.0) ⭐️ 8.0/10

Polars 1.42.0 引入了性能改进，如基于字节的云 I/O 并发控制和消除空块复制，添加了实验性的离核溢出和严格模式，并支持 SQL 的隐式 JOIN 语法，同时废弃了字符串到时间类型的转换。 这些更新使 Polars 能够更好地处理大于内存的工作负载和云原生环境，同时提供更严格、更可预测的 API 以及更易用的 SQL 风格查询，对依赖快速 DataFrame 操作的数据工程师和分析师尤为有益。 此版本包含 PR #27998 的离核溢出实现，PR #28023 的实验性严格模式，PR #27890 的 SQL 隐式 JOIN 支持，以及性能改进 PR #27924（基于字节的云 I/O 并发控制），PR #28013（阶段变化时不刷新多路复用器），和 PR #27953（避免空块复制）。

github · github-actions[bot] · Jun 24, 05:20

**背景**: Polars 是一种基于 Apache Arrow 的高性能 Rust 编写的 DataFrame 库，提供 Python 绑定，以快速单节点分析著称。离核溢出通过将中间数据溢出到磁盘来处理大于内存的数据集。严格模式通过更严格的类型检查和错误处理尽早捕获错误，而 SQL 隐式 JOIN 则允许在 FROM 子句中使用逗号分隔的表格编写查询，无需显式的 JOIN 关键字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pola-rs/polars">GitHub - pola-rs/polars: Extremely fast Query Engine for DataFrames...</a></li>
<li><a href="https://pola.rs/">Polars — DataFrames for the new era</a></li>
<li><a href="https://docs.pola.rs/api/python/dev/reference/sql/clauses.html">Query Clauses — Polars documentation</a></li>

</ul>
</details>

**标签**: `#polars`, `#dataframe`, `#python`, `#performance`, `#release`

---

<a id="item-2"></a>
## [OpenAI 首次发布其定制 AI 推理芯片。](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 8.0/10

OpenAI 宣布其首款定制 AI 推理芯片 Jalapeno，与 Broadcom 共同设计并由 TSMC 制造，旨在提升大语言模型推理效率。 该芯片表明 OpenAI 正在向 AI 硬件垂直整合迈进，减少对 Nvidia GPU 的依赖，并有望降低其服务的推理成本。 Jalapeno 从设计到量产仅用九个月，利用 OpenAI 自身的模型加速设计流程，并采用 TSMC 的先进制造工艺。

hackernews · jamdesk · Jun 24, 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专门用于高效运行已训练模型的处理器，相比通用 GPU 能提供更高的性能和能效。Broadcom 提供 ASIC 设计和封装专业知识，而 TSMC 是全球领先的半导体代工厂，使用先进制程生产芯片。OpenAI 的合作符合主要 AI 公司开发定制硅以提升可扩展性和降低成本的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.933thedrive.com/2026/06/24/openai-unveils-custom-chip-it-designed-with-broadcom-to-boost-its-ai-infrastructure/">OpenAI unveils custom chip it designed with Broadcom to boost its AI infrastructure | 93.3 The Drive</a></li>
<li><a href="https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/">TSMC AI Fabricating Dominance: Chip Manufacturing Leadership in AI Era - Klover.ai</a></li>

</ul>
</details>

**社区讨论**: 评论者对九个月的开发周期表示怀疑，认为可能被夸大的营销说法。其他人强调了芯片由 TSMC 制造，并讨论了诸如将权重存储在 ROM 中或将模型烧录到硅片等创新架构，提到了 Taalas 等初创公司。还有人指出，谷歌长期的 TPU 系列让 OpenAI 的进入看起来不那么新颖，但仍具重要意义。

**标签**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#Broadcom`, `#TSMC`

---

<a id="item-3"></a>
## [Anthropic 指控阿里巴巴非法提取 Claude AI 模型能力](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 8.0/10

Anthropic 称，2026 年 6 月 24 日，阿里巴巴通过模型蒸馏和未经授权的访问方案非法提取了其 Claude AI 模型的能力，据路透社看到的信函所述。 此指控凸显了 AI 行业在知识产权方面日益加剧的紧张局势，特别是关于模型蒸馏这一能够以低成本复制先进模型的做法。这可能影响 AI 公司如何保护其模型，并影响未来的许可和法律框架。 Anthropic 将此行为描述为对其模型已知的最大规模蒸馏攻击，涉及对抗性蒸馏——即用更小的模型在 Claude 的输出上进行训练以以较低成本模拟其能力。据称该方案还包括以低于官方 API 价格 70%-90%的价格转售 Claude 令牌，并将用户日志用作训练数据。

hackernews · htrp · Jun 24, 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48664814)

**背景**: 模型蒸馏是一种机器学习技术，其中较小的“学生”模型通过学习较大的“教师”模型的输出来复制其行为。虽然蒸馏可以降低计算成本，但未经教师模型所有者许可进行蒸馏可能构成对专有能力的未授权提取。Anthropic 的 Claude 系列是大型语言模型，通过 API 提供访问，其输出被视为有价值的知识产权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API | OpenAI</a></li>
<li><a href="https://cybersecuritynews.com/anthropic-accuses-alibaba/">Anthropic Accuses Alibaba of 'Illicitly' Accessing Its Claude AI Models in Largest Known Distillation Attack</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Anthropic 抱怨数据被使用具有讽刺意味，因为其自身模型也是在大量公开文本上训练的，有人将此比作历史上的 GUI 复制纠纷。其他人解释了蒸馏的两种主要类型——黑箱和有针对性的——并指出，以大幅折扣转售 Claude 令牌和收集用户日志使得低成本运营成为可能。

**标签**: `#AI`, `#model distillation`, `#intellectual property`, `#Alibaba`, `#Anthropic`

---

<a id="item-4"></a>
## [高通计划以 40 亿美元收购 AI 初创公司 Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

高通宣布于 2026 年 6 月 24 日将收购以 Mojo 编程语言和 MAX 编译器栈著称的 AI 初创公司 Modular，以增强其 AI 推理产品线。 此举表明高通希望通过将 Modular 的软件栈与其 ARM 芯片结合来挑战英伟达 CUDA 的主导地位，为开发者提供高性能 AI 推理的替代方案。 Modular 的 Mojo 语言基于 MLIR 编译框架，可面向 CPU、GPU、ASIC 等加速器；MAX 栈提供 CUDA 的替代推理引擎；交易价值约 40 亿美元，尚需监管批准。

hackernews · timmyd · Jun 24, 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: AI 推理是指运行已训练的机器学习模型进行预测，传统上依赖英伟达的 CUDA 平台在 GPU 上加速。Modular 的 Mojo 语言旨在通过利用 MLIR 这一灵活的编译基础设施，将 Python 般的易用性与系统级性能结合，以支持多种硬件。MAX 编译器栈建立在 Mojo 之上，提供一套端到端的工具链，用于在各种加速器上编译 AI 内核，因而有望成为 CUDA 生态的竞争对手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://krun.pro/mojo-ecosystem/">Mojo Ecosystem 2026: Infrastructure, Libraries, and the MAX ... - KruN</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**社区讨论**: 评论者对收购速度感到惊讶，对 Mojo 语言持有复杂情感，对高通在 ARM/RISC‑V 方面的野心持乐观态度，同时也怀疑硬件公司是否能够成功构建具有竞争力的 AI 软件栈。

**标签**: `#Qualcomm`, `#Modular`, `#AI acquisition`, `#Mojo language`, `#AI inference`

---

<a id="item-5"></a>
## [NVIDIA 45°C 液冷架构将数据中心用水降至近零](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 推出了一种适用于 AI 工厂的 45°C 液冷架构，免除冷却塔和冷水机组，使现场用水接近零，同时将捕获的废热用于区域供暖。 通过大幅降低用水量并将热量再利用，该设计缓解了数据中心的可持续性压力，并通过区域供暖提供潜在的收入或社区效益，使 AI 基础设施的发展与气候目标保持一致。 冷却剂温度可达 45°C（113°F），实现直接对芯片液冷而无需冷水机；通过热交换器将回收的热量输送至区域供暖网络，为附近建筑提供可用热能。

hackernews · nitin_flanker · Jun 24, 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 传统数据中心依赖冷水机和冷却塔消耗大量水来散发来自空冷或液冷系统的热量。液冷将冷却剂直接输送到芯片，提高热效率并允许使用更高温度的冷却剂。区域供暖系统将集中热源的废热输送到住宅或商业建筑用于供暖。通过将冷却剂温度提升至 45°C，NVIDIA 的设计避免了耗水的热排放，并使热量适合在此类网络中重复使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/">Hotter Than a Hot Tub: The 45 ° C Breakthrough to Cool ... | NVIDIA Blog</a></li>
<li><a href="https://schemaninja.com/nvidia-says-its-hotter-than-a-hot-tub/">Nvidia Says Its "Hotter Than a Hot Tub" Cooling Can Cut AI Data...</a></li>
<li><a href="https://www.linkedin.com/pulse/how-innovation-sustainability-shaping-tomorrows-world-tiago-n7lgf">Repurposing Data Center Waste Heat : A Sustainable Solution for...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了与区域供暖系统合作的潜力，指出 45°C 的废热能为社区带来可观的效益。也有人质疑这一做法是否真正新颖，引用已有的液冷设施并要求解释何谓“有利气候”。此外，还有人分享了个人使用温热 GPU 冷却剂的经验，并提及 NASA 阿姆斯模块化超算设施等先前案例。

**标签**: `#liquid cooling`, `#data center`, `#AI infrastructure`, `#energy efficiency`, `#district heating`

---

<a id="item-6"></a>
## [Nub：受 Bun 启发的 Node.js 一体化工具包，使用 --require 钩子](https://github.com/nubjs/nub) ⭐️ 8.0/10

Nub 是一个受 Bun 启发的 Node.js 一体化工具包，它通过 --require 预加载钩子加载基于 oxc 的 Node-API 转译器，注册模块解析钩子，并在 Node 原生引擎上运行时注入 Worker、Temporal 等 API 的 polyfill。 它将 Bun 般的开发者体验——快速启动、集成转译和 polyfill——带到 Node.js，而无需离开 Node 运行时，为 Node 开发者提供了一种在熟悉的生态系统中享受现代工具链的方式。 Nub 将 oxc 转译器打包为 Node-API 插件，利用 Node 的 --require 钩子进行预加载并通过 module.registerHooks 进行模块解析，按需注入 polyfill；所有代码最终在原生 Node 引擎和标准库上运行。

hackernews · colinmcd · Jun 24, 14:14 · [社区讨论](https://news.ycombinator.com/item?id=48660267)

**背景**: Node.js 提供 --require 标志，可在应用启动前加载模块，以实现运行时的转译或 polyfill 注入。module.registerHooks API 允许自定义模块的解析和加载方式，以支持 ESM 与 CJS 的互操作性。Oxc 是一种用 Rust 编写的高性能 JavaScript 工具链，提供可编译为 Node-API 插件的转译器，以达到接近原生的速度。Node-API 插件是 ABI 稳定的原生模块，可在不同 Node 版本之间免重新编译使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://glebbahmutov.com/blog/hooking-into-node-loader-for-fun-and-profit/">Hooking into Node loader for fun and profit | Better world by better...</a></li>
<li><a href="https://stackoverflow.com/questions/24602136/import-hooks-in-node-js">javascript - Import hooks in Node . js - Stack Overflow</a></li>
<li><a href="https://git-stars.org/repositories/topic/transpiler">Top transpiler Repositories - GitHub Projects for transpiler ... | Git Stars</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞此思路为将 Bun 的开发者体验引入 Node.js 的合理方式，质疑为何不直接使用 Bun，好奇为何选择 --require 而非 --import 及其对 ESM 的影响，指出 Node 已能原生运行 TypeScript，并分享了将整个 monorepo 迁移至 Nub 后零问题且速度极快的经验。

**标签**: `#Node.js`, `#developer tooling`, `#transpilation`, `#Bun alternative`, `#JavaScript`

---

<a id="item-7"></a>
## [AI 代币经济学：基础模型中的代币、计算与定价](https://arxiv.org/abs/2606.24616) ⭐️ 8.0/10

该论文（arXiv:2606.24616v1）提出了 AI 代币经济学框架，研究代币的生成、消耗、定价、分配与优化，将代币层面的技术成本与工作流生产率和经济价值联系起来。 通过区分代币支出与经济价值，该框架为定价 AI 服务提供了新视角，指导资源分配和市场设计决策，影响研究者、企业和政策制定者。 该框架表明代币支出与经济价值不同；价值取决于边际生产率、工作流位置、隐藏推理活动、风险及下游传播效应。同时，它列出了诸如隐藏代币测量、经验校准、代币生产率、动态分配和基于代币的市场等开放研究方向。

rss · arXiv Quantitative Finance · Jun 24, 04:00

**背景**: 在现代基础模型服务中，代币作为实用的记账单位，度量信息处理、计算、内存使用和能源消耗。代币经济学研究代币的生成、消耗、定价、分配与优化，将技术成本与经济价值和市场动态联系起来。理解代币层面的经济学有助于服务提供者制定定价策略，以及用户评估 AI 生成输出的真实成本与价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.24616">[2606.24616] AI Tokenomics: The Economics of Tokens ...</a></li>
<li><a href="https://pub.towardsai.net/thinking-tokens-are-not-free-most-pipelines-treat-them-like-they-are-846708fdcef1">Thinking Tokens Are Not Free. Most Pipelines Treat... | Towards AI</a></li>
<li><a href="https://www.linkedin.com/posts/artemnovichkov_tracking-token-usage-in-foundation-models-activity-7429490715279134720-56Jj">Measuring Token Usage in iOS 26.4 Foundation Models | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#tokenomics`, `#foundation models`, `#resource allocation`, `#market design`

---

<a id="item-8"></a>
## [TIP-Search：面向不确定负载的市场预测时间可预测推理调度](https://arxiv.org/abs/2506.08026) ⭐️ 8.0/10

TIP-Search 提出了一种时间可预测的推理调度框架，通过筛选符合 conformal 延迟分位数可行的模型并使用受限约束在线专家在有限工作器上调度预测，在优化的可部署池中达到 0.994 的原始准确率和 0.991 的及时准确率。在 TLOB FI-2010 基准（h=10）上，TIP-Search++ 将及时准确率从 0.156 提升至 0.239，截止满意度从 0.391 提升至 0.962。 该工作通过在不确定工作负载下提供能够保证预测在决策截止时间前到达的调度方法，推进了实时机器学习系统的发展，直接提升了市场预测服务的可用性。其在及时准确率和截止满意度上的经验改进展示了在波动环境中实现可靠金融预测的实际途径。 TIP-Search 首先使用符合一致预测延迟分位数可行性检查过滤预测器，然后通过受限约束在线专家在有限工作器池中调度任务，以平衡准确率、队列压力和截止风险。诸如 OCO-ACPO 和 SA-OCO-ACPO 等变体在基线如 RAMSIS 和 SneakPeek 上实现了统计显著的提升（例如及时准确率 +0.00285，p=0.0118；截止满意度 +0.0146，p=1.5×10⁻⁵）。

rss · arXiv Quantitative Finance · Jun 24, 04:00

**背景**: 实时市场预测服务必须在固定的决策截止时间之前产生正确的预测；若预测在截止时间之后才到达，则毫无用处，因此及时性与准确性同等重要。一致预测提供了无需分布假设的不确定性量化，使得可以构建延迟分位数可行的模型，以保证满足用户指定时间约束的概率。在线专家学习（如受限约束在线专家）能够动态地在多个模型之间进行选择，以在资源限制下平衡准确率。在工作负载不确定（请求到达率不可预测变化）的情况下，时间可预测的推理调度旨在同时优化预测质量和截止满意度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ideas.repec.org/p/arx/papers/2506.08026.html">TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load - IDEAS/RePEc</a></li>
<li><a href="https://www.semanticscholar.org/paper/78470575239e46b5a8a19ca11b425874c3083866">[PDF] TIP-Search: Time-Predictable Inference Scheduling for Market ...</a></li>
<li><a href="https://arxiv.org/html/2506.08026v2">TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load - arXiv</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#real-time systems`, `#inference scheduling`, `#financial forecasting`, `#conformal prediction`

---