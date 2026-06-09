---
layout: default
title: "Horizon Summary: 2026-06-09 (ZH)"
date: 2026-06-09
lang: zh
---

> From 38 items, 8 important content pieces were selected

---

1. [xAI 的算力租赁策略使其更像数据中心 REIT 而非前沿实验室](#item-1) ⭐️ 8.0/10
2. [小米 MiMo-v2.5-Pro-UltraSpeed 宣称 1 万亿参数模型达每秒 1000 个 token](#item-2) ⭐️ 8.0/10
3. [苹果推出用于端侧 AI 模型的 Core AI 框架](#item-3) ⭐️ 8.0/10
4. [Signal 警告英国监控法威胁隐私与安全](#item-4) ⭐️ 8.0/10
5. [FrontierCode 基准测量 AI 代码可合并性](#item-5) ⭐️ 8.0/10
6. [OpenAI 向 SEC 提交保密草案 S-1。](#item-6) ⭐️ 8.0/10
7. [Perplexity 的 Computer AI 代理提升自主知识工作。](#item-7) ⭐️ 8.0/10
8. [权益证明的金融化：外在风险溢价下的渐进中心化](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [xAI 的算力租赁策略使其更像数据中心 REIT 而非前沿实验室](https://martinalderson.com/posts/xais-new-rental-business/) ⭐️ 8.0/10

文章认为，xAI 新的算力租赁策略——向 Cursor 等第三方提供 GPU 容量——使其从开发前沿 AI 模型转向像数据中心 REIT 那样运营。 这种重新定义凸显了 AI 公司越来越倾向于通过基础设施而非仅仅模型来变现的趋势，这将影响投资者、竞争对手以及更广泛的 AI 供应链。这也凸显了 xAI、SpaceX 以及谷歌等主要科技投资者之间的紧密关联。 xAI 计划向 Cursor 提供数万块 GPU 用于训练其编程模型，这些算力来源于使用临时发电机并引发污染担忧的 Colossus 数据中心。该策略与 SpaceX 的建设能力以及谷歌持有的 SpaceX 5‑6 % 股份相关联，后者可能从 SpaceX 估值提升中获益。

hackernews · martinald · Jun 8, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48446428)

**背景**: 数据中心 REIT 是一种房地产投资信托，它拥有并出租用于托管计算设备的物理基础设施——空间、电力和冷却——而不是直接出售计算能力。前沿 AI 实验室则专注于推动模型能力的边界，例如开发高级基础模型或多模态系统。xAI 由埃隆·马斯克创立，与 SpaceX 有紧密联系，并且一直在构建像 Colossus 这样的巨型 GPU 集群以支持其 AI 目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fool.com/investing/stock-market/market-sectors/real-estate-investing/reit/data-center-reit/">Best Data Center REITs for 2026 and How to Invest</a></li>
<li><a href="https://www.linkedin.com/pulse/frontier-ai-labs-what-building-why-transformation-leaders-kumar-gbuge">Frontier AI Labs: What They Are Building — and Why Transformation Leaders Should Care</a></li>
<li><a href="https://www.whatjobs.com/news/what-spacexs-cursor-deal-signals-about-xais-compute-strategy/">What SpaceX’s Cursor Deal Signals About xAI ’s Compute Strategy</a></li>

</ul>
</details>

**社区讨论**: 几位评论者指出，传统的数据中心 REIT 出租的是空间、电力和冷却，而不是计算能力，因此认为 REIT 类比不够准确。另一些评论者欢迎转向出租计算基础设施的做法，批评 Colossus 设施使用临时发电机并造成污染，对谷歌在 SpaceX 的股份及可能的估值虚高表示怀疑，并将 SpaceX 描述为马斯克其他业务的控股公司。

**标签**: `#AI infrastructure`, `#xAI`, `#datacenter REIT`, `#business model`, `#SpaceX`

---

<a id="item-2"></a>
## [小米 MiMo-v2.5-Pro-UltraSpeed 宣称 1 万亿参数模型达每秒 1000 个 token](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) ⭐️ 8.0/10

小米宣布了与 TileRT 共同开发的 MiMo-v2.5-Pro-UltraSpeed，这是一个能够在通用 GPU 上每秒生成 1000 个 token 的 1 万亿参数语言模型。该声明使该模型成为大语言模型速度的新前沿。 实现每秒 1000 个 token 的万亿参数模型有望实现近实时的 AI 应用，并改变成本‑性能预期，特别是在中国厂商提供具竞争力价格的背景下。这将加速全球在 AI 基础设施效率方面的竞争，并可能影响企业的采用模式。 该模型采用混合专家（MoE）架构并使用 FP4 量化，使其能够在普通硬件上运行，同时将 UltraSpeed 模式作为现有 MiMo V2.5 Pro 的高速交付选项。其定价宣称与 DeepSeek 相当，即使是超速 tier 也被认为价格惊人低廉。

hackernews · gainsurier · Jun 8, 15:27 · [社区讨论](https://news.ycombinator.com/item?id=48446639)

**背景**: 万亿参数语言模型代表当前的规模前沿，此时推理速度常常下降而显存需求急剧上升。每秒 token 数（TPS）是衡量模型每秒能生成多少 token 的标准指标，能够在不同硬件和模型之间提供可比的速度度量。小米的 MiMo 系列早期作为开放权重的 agentic 编码模型发布，如今通过 UltraSpeed 模式将 TPS 推高至每秒 1000 个 token 以上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gizmochina.com/2026/06/09/xiaomi-mimo-v2-5-pro-ultraspeed-mode-1000-tokens-per-second/">Xiaomi announces its fastest AI model yet with 1000 token/second...</a></li>
<li><a href="https://dataforcee.us/2026/06/08/xiaomi-mimo-and-tilert-push-1-trillion-parameter-model-past-1000-tokens-per-second-on-commodity-gpus/">Xiaomi MiMo and TileRT Push 1-Trillion-Parameter Model Past 1000...</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash">XiaomiMiMo/ MiMo - V 2 . 5 - Pro -FP4-DFlash · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者对近乎即时的 AI 助手表示兴奋，认为这可能减少多任务处理并提升专注度；但也有人质疑，如果工作时间不变，这种速度提升是否真的带来生产力增长。多位评论者强调了模型相较于 DeepSeek 的激进定价，并称赞其开放权重的 agentic 编码能力，同时也有人警告超快 AI 对工作模式的更广泛影响。

**标签**: `#AI/ML`, `#Large Language Models`, `#Model Performance`, `#AI Infrastructure`, `#China AI`

---

<a id="item-3"></a>
## [苹果推出用于端侧 AI 模型的 Core AI 框架](https://developer.apple.com/documentation/coreai/) ⭐️ 8.0/10

苹果宣布推出 Core AI，一个新框架，使开发者能够编写、优化并部署端侧 AI 模型，支持将 PyTorch 模型转换并在 CPU、GPU 以及 Apple Neural Engine 上运行。 Core AI 表明苹果希望统一端侧 AI 开发并可能取代 Core ML，使得大型语言模型和生成式 AI 能够在设备上本地运行，同时保护用户隐私。 该框架提供内存安全的 Swift API，通过 apple/coreai‑optimization 仓库支持 PyTorch 转换为 Core AI，并可在 CPU、GPU 以及 Apple Silicon 上的 16 核 Neural Engine 上运行模型。

hackernews · hmokiguess · Jun 8, 18:47 · [社区讨论](https://news.ycombinator.com/item?id=48449665)

**背景**: Core ML 一直是苹果用于在 iOS、macOS、watchOS 和 tvOS 应用中集成机器学习模型的主要框架，侧重于传统的预测任务。随着大型语言模型和生成式 AI 的兴起，开发者需要一种能够在设备上高效运行这些模型且不依赖云服务的框架。Apple Neural Engine 是嵌入 Apple Silicon 中的专用神经处理单元，能够加速 AI 工作负载的矩阵和卷积运算。Core AI 在这些技术基础上构建，提供统一的基于 Swift 的 API，面向 CPU、GPU 和 Neural Engine 来处理现代 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/core-ai/">Core AI - Apple Developer</a></li>
<li><a href="https://udit.co/blog/apple-core-ai-replaces-core-ml-wwdc-ios-27">Apple replacing Core ML with Core AI at WWDC 2026 changes e</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Neural_Engine">Apple Neural Engine</a></li>

</ul>
</details>

**社区讨论**: 评论者对即将到来的端侧基础模型更新表达热情，并分享了 WWDC 2026 中关于 Core AI 的 session 视频链接。有几位询问 Core AI 是否会完全取代 Core ML，而其他人则指出苹果正在研究低位量化（w4a8、w4a16），并可能对 sub‑100B 参数模型的部署产生影响。还有人猜测，向端侧 AI 的转变正在促使 AI 公司加速 IPO，因为它们的云端优势正在减弱。

**标签**: `#Apple`, `#Core AI`, `#Machine Learning`, `#On-device AI`, `#CoreML`

---

<a id="item-4"></a>
## [Signal 警告英国监控法威胁隐私与安全](https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf) ⭐️ 8.0/10

2026 年 6 月 8 日，Signal 发布 PDF 声明，警告英国最新监控立法（包括在线安全法和调查权力法案的修正案）将强制进行侵入式客户端扫描和对加密通信的监控，削弱用户隐私与安全。 该声明指出，这些措施可能破坏端到端加密，为全球监控树立危险先例，并影响数百万依赖 Signal、WhatsApp 等安全通讯应用的用户。 该立法提出在加密前对消息进行客户端扫描，要求使用经过认证的技术，可能实时运行基于 AI 的裸体检测，并包括远程认证以确保合规，扩展了 2024 年调查权力法案修正案的权限。

hackernews · g0xA52A2A · Jun 8, 19:42 · [社区讨论](https://news.ycombinator.com/item?id=48450646)

**背景**: 英国在线安全法案（Online Safety Act）授予 Ofcom 权力，要求科技公司安装‘认证技术’对加密消息进行批量扫描，即客户端扫描。2016 年通过的调查权力法案（Investigatory Powers Act）在 2024 年被修订，已经扩大了英国情报机构和警察的监控能力，最新修改进一步加强了这些权力。批评者认为这些措施会削弱加密、侵蚀信任，并可能导致大规模监控，影响不仅英国公民，还有全球用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.computerweekly.com/feature/The-UKs-Online-Safety-Act-explained-what-you-need-to-know">The UK’s Online Safety Act explained: what you need to know | Computer Weekly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Investigatory_Powers_Act_2016">Investigatory Powers Act 2016 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Encryption_ban_proposal_in_the_United_Kingdom">Encryption ban proposal in the United Kingdom - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对立法将设备变成监控工具的担忧，将其比作无处不在的‘斯塔西’，监控私人对话、就医访问和日常生活。一些人指出这与安全启动、DRM 和远程认证在技术上的相似之处，警告赋予企业对硬件的控制可能被政治滥用。其他人则呼吁 Signal 坚决反对他们认为不可避免的强制客户端扫描和数字身份验证趋势。

**标签**: `#privacy`, `#surveillance`, `#UK legislation`, `#Signal`, `#online safety`

---

<a id="item-5"></a>
## [FrontierCode 基准测量 AI 代码可合并性](https://cognition.ai/blog/frontier-code) ⭐️ 8.0/10

FrontierCode 推出了一种新基准，用超过 3000 条评价规则和维护者自行创建的任务来评估 AI 生成的代码是否能被专家开源维护者合并。 它将评估从单纯的正确性转向实际的可合并性，为 AI 代码生成质量提供更有力的信号，可能影响模型选择和部署决策。 该基准包含 20+ 位专家维护者创建的任务，超过 1000 小时的维护者工作，以及相比 SWE‑Bench Pro 误报率降低 81% 的验证流程。

hackernews · streamer45 · Jun 8, 20:45 · [社区讨论](https://news.ycombinator.com/item?id=48451723)

**背景**: 传统的代码生成基准（如 SWE‑Bench）主要检查模型输出是否能通过单元测试，但这并不能保证代码的可维护性或被项目维护者接受。FrontierCode 将“可合并性”定义为专家维护者接受并将 AI 生成的补丁合并到其代码库的可能性，使用源自真实维护者偏好的评价规则。通过引入数千条规则和大量人工策展，它旨在衡量 AI 生成代码的实际质量，而不仅仅是正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cognition.ai/blog/frontier-code">Introducing FrontierCode | Cognition</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/frontiercode-ai-coding-benchmark-goes-beyond-correctness">FrontierCode: AI Coding Benchmark Goes Beyond Correctness | StartupHub.ai</a></li>
<li><a href="https://digg.com/ai/ea1qevgh">FrontierCode benchmark launches to test code mergeability, finding over half of SWE-bench outputs are unmergeable · Digg</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该基准关注实际可合并性和低误报率，swyx 强调了背后规则制定的工作量，vessenes 指出其对计算部署的潜在影响。也有人如 singpolyma3 对衡量主观代码质量持怀疑态度，ilaksh 则询问数据是否可下载以及是否测试了 GLM 5.1 等模型。

**标签**: `#code-generation`, `#benchmark`, `#software-engineering`, `#AI-evaluation`, `#open-source`

---

<a id="item-6"></a>
## [OpenAI 向 SEC 提交保密草案 S-1。](https://openai.com/index/openai-submits-confidential-s-1/) ⭐️ 8.0/10

OpenAI 已向美国证券交易委员会（SEC）提交了一份保密草案 S-1 注册声明，表明其正在为可能的首次公开募股做准备。 此举表明 OpenAI 意图进入公开资本市场筹集资金，可能重塑人工智能行业的融资格局，并为早期投资者提供流动性。 该申请为保密文件，细节尚未公开；OpenAI 尚未确定 IPO 时间表，并表示保持私有化可能对某些计划更有利。

hackernews · hackerBanana · Jun 8, 21:22 · [社区讨论](https://news.ycombinator.com/item?id=48452317)

**背景**: 表格 S-1 是公司向美国证券交易委员会（SEC）提交的注册声明，用于披露财务状况、风险因素和募集资金用途以申请上市。根据 JOBS 法案，新兴增长公司可以保密提交草案 S-1，以便在公开披露前获得 SEC 的反馈。首次公开募股（IPO）使私营公司能够向公众投资者出售股票，从而筹集资金并提供流动性。OpenAI 的保密申请表明其正在寻求早期的 SEC 审查，同时保持细节不公开。

**社区讨论**: 评论者对 OpenAI 能否在当前收入平平且现金消耗大的情况下成功上市表示怀疑，警告任何公开发行可能估值大幅下降。有人指出竞争威胁，如苹果可能将 AI 模型商品化，并提到埃隆·马斯克对 OpenAI 盈利模式的不满。还有一些人猜测市场会因华尔街对 ticker 符号的炒作而被炒热。

**标签**: `#OpenAI`, `#IPO`, `#SEC filing`, `#AI industry`, `#finance`

---

<a id="item-7"></a>
## [Perplexity 的 Computer AI 代理提升自主知识工作。](https://arxiv.org/abs/2606.07489) ⭐️ 8.0/10

该研究使用 Perplexity 的 Search 和 Computer 产品的生产数据发现，Computer AI 代理每次用户会话能够自主工作 26 分钟，而 Search 产品仅为 33 秒。这一转变使每次查询的不满意度降低了 55%，并将用户的精力引向验证和扩展等更高阶任务。 这些发现表明，AI 代理能够显著提升自主性、效率和输出质量，同时将时间和成本降低多达 94%，从而重塑知识工作的执行方式。这对研究人员、企业和寻求利用 AI 处理复杂跨学科任务的工作者具有广泛影响。 Computer 通过编排 19 个 AI 模型实现任务的端到端分解与执行，使匹配任务的完成时间从 269 分钟缩短至 36 分钟——相比仅使用 Search 的人类，时间下降 87%，成本下降 94%。此外，Computer 的查询更常跨越职业边界、需要更高阶认知，并将相互依赖的子任务打包成复合查询，而在 Search 使用中这种情况极少出现。

rss · arXiv Quantitative Finance · Jun 8, 04:00

**背景**: AI 代理是一类超越对话式助手的系统，能够自主进行任务规划、分解和执行，而无需持续的用户提示。任务分解将复杂目标拆分为若干较小的子任务，使得专门模型能够各自处理，从而实现端到端自动化。Perplexity Search 提供快速的事实性回答，而其 Computer 产品则充当 AI 代理，通过协同多个模型来完成更深入、持续的知识工作。理解这些区别有助于阐明代理如何扩展自动化工作的范围和深度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/no-time/perplexity-computer-the-19-model-ai-agent-and-its-real-world-use-cases-0d707adac4aa">Perplexity Computer : The 19-Model AI Agent and Its... | Medium</a></li>
<li><a href="https://aiagentstore.ai/ai-agent/perplexity-computer">Perplexity Computer - AI Agent</a></li>
<li><a href="https://skyagency-group.com/en/ai-agents-handle-multi-step-tasks/">7 Powerful Steps on How Autonomous AI Agents Handle Multi-Step...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#knowledge work`, `#autonomy`, `#human-AI interaction`, `#empirical study`

---

<a id="item-8"></a>
## [权益证明的金融化：外在风险溢价下的渐进中心化](https://arxiv.org/abs/2604.26076) ⭐️ 8.0/10

该文提出了一种异质宏观经济模型，用于分析权益证明网络中外部传统金融风险溢价的长期中心化效应，表明投资者的财富将呈指数增长，导致内部质押收益被压至零，最终实现共识层的完全机构化捕获。 通过将传统金融收益与区块链共识挂钩，该研究揭示了一种可能削弱大规模权益证明协议去中心化和安全性的系统性风险，为协议设计提供了抵御外部经济压力的参考。 模型将行为者划分为投资者和消费者，采用准线性效用函数推导出唯一的宏观均衡——一个三次多项式；外部风险溢价使投资者财富呈指数增长，内部质押收益被压至零，消费者财富被上界限制，最终只能持有流动资产。

rss · arXiv Quantitative Finance · Jun 8, 04:00

**背景**: 权益证明（PoS）是一种区块链共识机制，验证者通过锁定加密货币作为质押来获得与其持有量成比例的奖励。外部风险溢价是指投资者相对于无风险基准资产要求的额外收益，例如传统金融中的股票风险溢价。在宏观经济建模中，准线性效用函数是指对某种商品（通常作为计价货币）的效用呈线性，而对另一种商品的效用则非线性，从而简化消费者选择分析。论文将这些概念结合起来，研究外部金融收益如何影响权益证明网络中的均衡质押行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/e/equityriskpremium.asp">investopedia.com/terms/e/equityriskpremium.asp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quasilinear_utility">Quasilinear utility - Wikipedia</a></li>
<li><a href="https://www.thoughtco.com/science-4132464">thoughtco.com/science-4132464</a></li>

</ul>
</details>

**标签**: `#Proof-of-Stake`, `#Blockchain Economics`, `#Centralization`, `#Financialization`, `#Macroeconomic Modeling`

---