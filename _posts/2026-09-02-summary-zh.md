---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> From 58 items, 16 important content pieces were selected

---

1. [坚持使用 Firefox 以保护浏览器引擎多样性](#item-1) ⭐️ 8.0/10
2. [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1 更新](#item-2) ⭐️ 8.0/10
3. [Slotstream 通过专家卸载在 48GB Mac 上运行 125B Qwen3.8‑Flash‑Next](#item-3) ⭐️ 8.0/10
4. [Play Store 屏蔽 AuroraStore，影响 GrapheneOS 用户](#item-4) ⭐️ 8.0/10
5. [Atlas：空间智能的世界模型](#item-5) ⭐️ 8.0/10
6. [随机跟踪问题的尖锐收敛率及其在最优执行中的应用。](#item-6) ⭐️ 8.0/10
7. [智能的代价：AI 服务的质量调整价格指数](#item-7) ⭐️ 8.0/10
8. [跳扩散模型表明 LVR 在区块时间趋零时仍有非零下界。](#item-8) ⭐️ 8.0/10
9. [基于 LLM 的多智能体模型模拟家庭在关税威胁下的预期](#item-9) ⭐️ 8.0/10
10. [电池储能在英国平衡机制价格形成中的日益增长作用](#item-10) ⭐️ 8.0/10
11. [风险调整伤害评分和 FinRedTeamBench 提升金融服务 LLM 安全](#item-11) ⭐️ 8.0/10
12. [AI 辅助劳动市场中的绩效操纵：理论与实证](#item-12) ⭐️ 8.0/10
13. [数据驱动的随机最优控制用于 intraday 电力交易](#item-13) ⭐️ 8.0/10
14. [同行评审与 AI 筛选对期刊印章价值的建模](#item-14) ⭐️ 8.0/10
15. [PortBench：一种相关性感知的全流程 LLM 驱动投资组合管理基准](#item-15) ⭐️ 8.0/10
16. [Fund2Persona 框架从基金披露构建财务顾问角色](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [坚持使用 Firefox 以保护浏览器引擎多样性](https://www.newsonaut.com/articles/hang-on-to-your-firefox) ⭐️ 8.0/10

文章呼吁用户继续使用 Firefox，以维持浏览器引擎多样性并抵御 Chrome 和 WebKit 内核浏览器的主导地位。 浏览器引擎多样性对创新、隐私以及防止单一供应商主导网络标准至关重要，这会影响开发者和普通用户。 Firefox 是少数仍在使用 Mozilla Gecko 引擎的主要桌面浏览器，而大多数竞争对手依赖 Blink（Chrome）或 WebKit（Safari）；文章还提到了对 Mozilla 广告技术收购和数据收集做法的批评。

hackernews · speckx · Sep 1, 20:30 · [社区讨论](https://news.ycombinator.com/item?id=49527748)

**背景**: 浏览器引擎（如 Blink、Gecko 和 WebKit）负责渲染网页并实现网络标准；引擎多样性通过允许不同的特性和性能实现方式来促进创新。Firefox 使用的 Gecko 引擎由 Mozilla 开发，是唯一主要的不基于 Chromium 或 WebKit 的独立引擎，为 Chrome 和 Safari 的主导地位提供了制衡。保持多种引擎有助于防止单一供应商控制网络标准，并在隐私和广告拦截等方面鼓励竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://css-tricks.com/browser-engine-diversity/">Browser Engine Diversity | CSS-Tricks</a></li>
<li><a href="https://blog.mozilla.org/netpolicy/2026/03/23/competition-innovation-and-the-future-of-the-web/">Competition, Innovation, and the Future of the Web - Why Independent Browser Engines Matter - Open Policy & Advocacy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Comparison_of_browser_engines">Comparison of browser engines - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Firefox 是最后提供引擎多样性且具备强劲广告拦截能力的主要浏览器，认为它对保持网络竞争至关重要。同时，许多人批评 Mozilla 的最近举措——如收购广告技术公司和收集用户数据——认为这些行为会驱走用户。还有人指出，尽管对 Mozilla 有诸多分歧，但在引擎多样性问题上支持 Firefox 仍然有价值，并建议围绕共同目标建立联盟。

**标签**: `#Firefox`, `#browser diversity`, `#web privacy`, `#ad blocking`, `#open web`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1 更新](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 8.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1，提供了改进的写作风格、可调节的推理努力级别（低、中、高、x 高），并将缓存读取价格从每百万 token 1 美元降至 0.25 美元。 此更新回应了用户对 Claude 风格刻板的反馈，为开发者提供了对模型推理成本的细粒度控制，并降低了运营费用，使其在生产工作负载中更具竞争力。 模型的系统卡可在 https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf 查看，价格削减使 Fable 5.1 的缓存读取成本降至 Opus 的一半。可调节的推理努力级别让用户可以在延迟和更深入推理之间进行权衡。

hackernews · denysvitali · Sep 1, 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**背景**: Anthropic 的 Claude 系列包括 Opus、Sonnet 和早期的 Fable 系列等模型，这些模型通过 API 按 token 计费提供服务。缓存读取价格指的是检索之前计算的模型状态的成本，这会影响对延迟敏感的应用。推理努力级别允许用户指定模型在回答前应投入多少计算工作进行思考，这会影响回答的质量和响应时间。

**社区讨论**: Anthropic 员工 Felix 称赞 Fable 5.1 风格更自然、更好地遵循风格指令。SimonW 演示了新的推理努力级别（低、中、高、x 高），并展示了能够捕获推理轨迹的工具，指出 xhigh 设置大约需要 14 分钟。GodelNumbering 强调了缓存读取价格的降低，但质疑基准改善；exabrial 则开玩笑说此更新就像是一次削弱，同时作为 Mythos 的营销噱头。

**标签**: `#Claude`, `#LLM`, `#Anthropic`, `#AI models`, `#price reduction`

---

<a id="item-3"></a>
## [Slotstream 通过专家卸载在 48GB Mac 上运行 125B Qwen3.8‑Flash‑Next](https://github.com/carloslfu/slotstream) ⭐️ 8.0/10

Slotstream 通过将不活跃的专家卸载到 SSD 并按需流式传输，使低内存 Mac 能够运行 125B 参数的 Qwen3.8‑Flash‑Next 模型，达到约 12 token/秒。 这表明巨大的混合专家模型可以在消费级硬件上进行推理，降低了缺乏 GPU 服务器的开发者的门槛。 该工具基于 Apple 的 MLX 框架和 Swift 构建，提供自动模式以平衡内存和速度，以 4‑bit 量化运行模型，并可通过类似 pip 的命令安装。

hackernews · carloslfu · Sep 1, 16:42 · [社区讨论](https://news.ycombinator.com/item?id=49524447)

**背景**: Qwen3.8‑Flash‑Next 是一个具有 1250 亿参数的混合专家（MoE）语言模型，每个 token 只激活一部分专家。专家卸载将不活跃的专家存储在较慢的存储设备（如 SSD）中，并在需要时将其流式传输到内存，从而大幅降低 RAM 需求。MLX 是苹果公司的开源机器学习框架，能够在 Mac 上利用统一内存进行类似 GPU 的高效计算，而 4‑bit 量化则进一步减小了模型的内存占用。

**社区讨论**: 评论者称赞了这一成就，但指出 README 内容杂乱，需要为新手提供更清晰的介绍。拥有类似 Mac 硬件的用户询问如何将上下文窗口扩展到当前的 71,680 个标记之外，而其他人则对在 16 GB 机器上实现高 token 速率而不触发热限制表示怀疑。还有人讨论了在 GPU 上添加 DDR5 的硬件想法，并希望未来配备更大统一内存的 Mac 能从 Slotstream 等技术中受益。

**标签**: `#LLM inference`, `#model offloading`, `#Mac MLX`, `#SSD streaming`, `#open-source tool`

---

<a id="item-4"></a>
## [Play Store 屏蔽 AuroraStore，影响 GrapheneOS 用户](https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566) ⭐️ 8.0/10

Google Play 商店已封锁 AuroraStore 客户端，导致无 Google 账户的用户无法更新应用，如 AuroraOSS GitLab 工作项所示。 此举影响依赖 AuroraStore 以避免 Google 追踪的隐私敏感用户，在 GrapheneOS 社区引发了关于安全与易用性权衡的讨论。 AuroraStore 是一个开源的 Google Play Store 前端，可实现匿名下载应用；GrapheneOS 官方建议使用沙盒化 Play Store 以获得更好的安全性；但一些用户更偏好 Aurora，因其无广告和黑暗模式。

hackernews · erikvanoosten · Sep 1, 15:55 · [社区讨论](https://news.ycombinator.com/item?id=49523754)

**背景**: AuroraStore 提供了一种无需登录 Google 账户即可浏览和安装 Google Play 应用的方法，作为官方客户端的隐私友好替代方案。GrapheneOS 是一个以安全和隐私为核心的开源 Android 基础操作系统，官方支持 Google Pixel 设备，基于 AOSP 构建。该系统鼓励用户通过 Play Integrity API 使用沙盒化 Play Store，以降低攻击面同时保持应用兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://frr.wikipedia.org/wiki/Aurora_Store">Aurora Store – Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 GrapheneOS 实际上建议不要使用 AuroraStore，而倾向于使用沙盒化 Play Store；也有用户欣赏 Aurora 无毒性界面和 absence of dark patterns；一些人不确定该封锁是故意还是错误；还有几位用户表示因 Aurora 无法更新应用或依赖它为没有 Google 账户的亲戚更新软件。

**标签**: `#Android`, `#GrapheneOS`, `#AuroraStore`, `#Privacy`, `#Google Play Store`

---

<a id="item-5"></a>
## [Atlas：空间智能的世界模型](https://www.worldlabs.ai/blog/atlas) ⭐️ 8.0/10

World Labs 发布了 Atlas，一个全模态世界模型，能够从稀疏图像中学习空间理解，实现高保真 3D 场景重建并生成最长一分钟的可控制 1440p 视频。 通过提供紧凑且具预测能力的 3D 环境表示，Atlas 能够加速机器人仿真、游戏关卡原型设计以及自主感知，连接原始感知与可操作的空间智能。 Atlas 是一种多模态自回归扩散 Transformer，在 DTU、ETH3D 和 ScanNet 等稀疏视图 3D 重建基准上优于开源专家，但社区指出其在相机移动时的时间一致性可能有所不足。

hackernews · johnsutor · Sep 1, 17:36 · [社区讨论](https://news.ycombinator.com/item?id=49525160)

**背景**: 在人工智能中，世界模型是一种机器学习系统，它构建环境的内部表示并预测该环境随动作变化的方式。空间智能指的是理解和推理物理空间的能力，世界模型通过保持一致且随时间连续的世界地图来实现这一目标。稀疏视图 3D 重建具有挑战性，因为重叠图像很少，导致传统的结构从运动和多视图立体方法失效，因而需要基于学习的方法如 Atlas。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.worldlabs.ai/blog/atlas">Atlas: A World Model for Spatial Intelligence | World Labs</a></li>
<li><a href="https://arxiv.org/html/2507.16406v1">Sparse-View 3D Reconstruction: Recent Advances and Open ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Atlas 在快速游戏原型和房屋级重建方面的潜力，但也有人质疑“世界模型”的确切含义，并指出相机移动时时间一致性可能不足。还有人强调从模型潜在空间提取语义信息的价值，而一位共同创始人则邀请大家提出更多问题。

**标签**: `#world model`, `#spatial intelligence`, `#3D reconstruction`, `#robotics`, `#AI`

---

<a id="item-6"></a>
## [随机跟踪问题的尖锐收敛率及其在最优执行中的应用。](https://arxiv.org/abs/2608.29468) ⭐️ 8.0/10

作者利用目标过程的 Besov 型模量，推导出二次随机跟踪问题的显式非渐近上界，并将其应用于具有随机终端库存的广义 Obizhaeva–Wang 执行模型。 这些结果首次给出随机跟踪的尖锐收敛率，提供了可实施的近似最优策略，能够改进实际执行成本并推进量化金融和随机控制的理论。 对于半鞅目标，这些界退化为平方根阶 O(√ε)；正则化后的最优执行成本以此速率收敛，并且可以构造出一个近似最优策略（尽管没有闭形式）以达到同样的逼近速率。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 随机跟踪问题涉及通过控制使过程随机目标对齐，在金融中常表现为交易的最优执行。Obizhaeva–Wang 模型描述了交易导致的价格冲击，引入二次交易速率惩罚参数ε可以对问题进行正则化，以避免不切实际的交易尖峰。Besov 型模量衡量目标过程的粗糙程度，决定了跟踪误差的收敛速度。

**标签**: `#stochastic control`, `#optimal execution`, `#convergence rates`, `#Besov modulus`, `#quantitative finance`

---

<a id="item-7"></a>
## [智能的代价：AI 服务的质量调整价格指数](https://arxiv.org/abs/2608.29843) ⭐️ 8.0/10

该论文利用来自 3,208 个模型和 86 家提供商的 21,024 条公开价格观测，并将其与 4,605 个基准分数通过潜在质量指数关联，构建了 AI 推理的质量调整价格指数。研究表明，传统匹配模型方法仅测得年下降 0.10 个对数点，而质量调整指数年下降 0.73 个对数点，意味着 87%的价格下降被质量提升掩盖。 该研究揭示了观察到的价格下降大部分被质量提升掩盖，从而改变了经济学家和政策制定者衡量 AI 市场竞争、集中度和生产力的方式。它提供了一种更准确的工具，以判断 AI 服务是否真的在变便宜，还是仅仅在性能上提升。 该指数采用统计机构用于软件的匹配模型方法，从基准响应模式构建潜在质量指数，并通过预注册的有效性审计排除受污染的基准。所有数据、代码和结果均可从公开来源零成本复现。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 质量调整价格指数（或称享乐指数）会在计算价格变化时考虑产品质量的变化，从而将纯粹的价格运动与性能提升分离开来。在 AI 推理领域，质量无法仅靠简单规格捕捉，而需要通过衡量模型能力的基准分数来推断。匹配模型方法通过比较同一模型在不同时间的表现，是统计局等机构用于软件和其他技术产品的标准做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.29843">The Price of Intelligence:A Quality-Adjusted Price Index for AI Services</a></li>
<li><a href="https://cemmap.ac.uk/wp-content/uploads/2021/02/CWP0421-Hedonic-prices-and-quality-adjusted-price-indices-powered-by-AI-1.pdf">Hedonic prices and quality</a></li>
<li><a href="https://benchlm.ai/">LLM Leaderboard & AI Model Benchmarks — September 2026</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#price index`, `#hedonic pricing`, `#AI inference`, `#measurement`

---

<a id="item-8"></a>
## [跳扩散模型表明 LVR 在区块时间趋零时仍有非零下界。](https://arxiv.org/abs/2608.30321) ⭐️ 8.0/10

该论文采用跳扩散价格过程建模 AMM 流动性提供者成本，发现 LVR 率分为随时间减小而消失的扩散项和与区块时间无关的跳跃项，从而使 LVR 具有不随区块时间趋零而消失的下界，且该下界随 √Δt 缩放。因此，即使区块时间趋于零，LVR 也不为零。 该结果表明，仅仅缩短区块时间无法消除流动性提供者的主要逆向选择成本，因而区块时间的设计应更多关注波动率、费率和共识成本，而不仅仅是区块时长。它为 LP 侧对区块时间福利的贡献提供了定量上限，有助于在以太坊、Solana 等 DeFi 协议中选择最优区块时间。 LVR 率表示为 F(γ/(σ√Δt)) + λV·G(γ;m,δ²) 加上一个有界余项；对于对称跳跃律，跳跃通道 λV·G 是精确下界，因此 LVR ≥ λV·G > 0 且随 √Δt 衰减。在以太坊 12 秒槽位时，LVR 率为 471 bp/yr，下界为 125 bp/yr；在 Solana 400 ms 槽位时，跳跃通道已占主导。将 LVR 与每区块共识成本相减，得到 LP 侧最优区块时间约为 8 秒，与池规模和跳跃参数 (λ,m,δ) 无关。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 自动做市商（AMM）如 Uniswap 允许用户对池子中的资产进行交易，流动性提供者（LP）可赚取交易费用，但会因套利者在 AMM 与外部市场之间的价差而遭受损失‑再平衡成本（LVR）。在几何布朗运动价格模型下，盈利套利区块的概率会随区块时间 Δt 减小，因而 LVR 在 Δt→ 0 时趋于零，这促使人们追求更短的区块时间。跳扩散模型在此基础上加入泊松驱动的跳跃项，以表示价格的突然大幅变动，这些变动不会被更短的区块时间所平滑。

**标签**: `#AMM`, `#LVR`, `#blockchain`, `#DeFi`, `#jump-diffusion`

---

<a id="item-9"></a>
## [基于 LLM 的多智能体模型模拟家庭在关税威胁下的预期](https://arxiv.org/abs/2608.30522) ⭐️ 8.0/10

研究人员构建了一个多智能体系统，将密歇根消费者调查中的 300 个家庭转换为持续的大语言模型代理，并在数个模拟月份中让其接触社交媒体信息。校准后的代理复制了“解放日”关税公告后人类调查数据的分布和人口统计模式，实验表明关税威胁和央行解释共同影响通胀和失业预期及其离散程度。 该框架提供了一种受控的人工智能驱动方法，用于研究政策沟通如何影响家庭信念，连接了计算社会科学与经济学。它为政策制定者和研究人员提供了一个测试平台，可在实际政策实施前评估关税威胁和央行信息的影响。 代理接触了不同的信息属性——即时性、率显著性、语义进展、复杂性、叙事和发送者身份——这些因素共同作用于预期及其离散程度；开放式回答将这些效应与注意力、歧义、可信度和因果叙事联系起来。第二个实验发现，央行解释可以协调信念，但其对平均预期的影响取决于解释的具体内容。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 密歇根消费者调查定期测量家庭对通胀和失业的预期，这些是宏观经济预测的重要指标。诸如“解放日”宣布的关税威胁等，即使在政策实施前也可能改变这些预期，但其措辞变化快速，使得传统调查难以捕捉。多智能体系统模拟相互作用的实体，而大型语言模型使代理能够生成类似人类的文本响应，从而让研究者能够在受控、可重复的环境中建模信息如何传播并影响信念。

**标签**: `#multi-agent systems`, `#large language models`, `#economic expectations`, `#policy communication`, `#computational social science`

---

<a id="item-10"></a>
## [电池储能在英国平衡机制价格形成中的日益增长作用](https://arxiv.org/abs/2608.29818) ⭐️ 8.0/10

该研究通过重构 2023 年至 2025 年英国平衡机制 50,684 个半小时结算期的买卖报价堆栈，将边际价格形成归因于单个平衡机制单位。电池储能在买方活跃边际中的份额从 0.8%上升至 36.2%，在卖方活跃边际中的份额从 3.2%上升至 26.9%，取代了燃气联合循环机组和抽水蓄能。 研究结果表明，在可再生能源主导的系统中，灵活的电池储能正越来越多地决定实时价格，这对市场设计、脱碳政策和储能资产估值具有直接影响。政策制定者和市场运营者可以利用这一证据来预测储能在电网脱碳过程中将如何影响平衡成本和价格信号。 该分析基于 50,684 个半小时期，发现容量归一化的边际捕获在买卖两侧均有上升，并估计每额外 100 MW 的平衡机制活跃容量将使季度买方和卖方边际份额分别提升 0.55 和 0.48 个百分点。到 2025 年，电池动作相比体积匹配的非电池替代方案更有利约 9–10 英镑/兆瓦时，但在价格最高的 5%短系统期中，电池的代表性不足 12.9 个百分点。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 英国平衡机制（BM）是国家能源系统运营商用来在近实时平衡电力供需的主要工具，通过接受发电机和储能资产的买卖报价来实现。不平衡价格（即现金结算价格）是根据被接受的 BM 买卖报价得出的，反映了每半小时结算系统失衡的成本。在可再生能源比例较高的系统中，当灵活技术（如电池）成为平衡电网所需的最贵或最廉价单元时，它们可能成为边际价格制定者。本研究提供了从 2023 年至 2025 年电池储能在 BM 中的边际份额变化的单位水平证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.neso.energy/what-we-do/systems-operations/what-balancing-mechanism">What is the Balancing Mechanism? | National Energy System Operator</a></li>
<li><a href="https://www.elexon.co.uk/bsc/settlement/imbalance-pricing/">Imbalance Pricing - Elexon BSC</a></li>
<li><a href="https://arxiv.org/abs/2608.29818">[2608.29818] Decarbonising price formation: unit-level evidence on battery storage and the imbalance price in the GB Balancing Mechanism</a></li>

</ul>
</details>

**标签**: `#energy markets`, `#battery storage`, `#GB Balancing Mechanism`, `#renewables integration`, `#electricity price formation`

---

<a id="item-11"></a>
## [风险调整伤害评分和 FinRedTeamBench 提升金融服务 LLM 安全](https://arxiv.org/abs/2603.10807) ⭐️ 8.0/10

论文提出 RAHS，一种风险调整的伤害评分，能够同时考虑披露严重性、免责声明缓解以及评 judge 间一致性；并提出 FinRedTeamBench，一个包含 989 个提示的基准，覆盖银行、金融服务和保险（BFSI）七大风险领域及 34 个子类别，并映射到监管框架。 通过提供细致入微的风险敏感指标和领域特定的红队基准，该工作使 LLM 在受监管金融场景下的安全测试更具真实性，帮助机构满足合规要求并降低因合法合规表述引发的潜在危害。 RAHS 结合披露严重性、免责声明存在以及三种异构 LLM 判断者间的一致性；FinRedTeamBench 包含多轮红队提示，并在人类专家验证后显示出在超参数扫描下排名稳定，且比单轮测试揭示出更高严重性的披露。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 大型语言模型的安全评估常依赖二元攻击成功率（ASR），将所有越狱视为等同，而未考虑所披露信息危害程度的差异。在银行、金融服务和保险（BFSI）等受监管行业中，有害输出可能通过看似合法或专业的请求被引发，而通用基准往往无法捕捉此类情景。风险调整伤害评分通过根据披露的运营严重性、免责声明的存在以及多个 LLM 判断者的一致性来对 ASR 进行加权，从而细化危害评估。FinRedTeamBench 则提供了一组与 BFSI 监管类别对齐的精心挑选的提示，以捕捉这些细微的失效模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.10807">Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in...</a></li>
<li><a href="https://www.researchgate.net/publication/401833402_Risk-Adjusted_Harm_Scoring_for_Automated_Red_Teaming_for_LLMs_in_Financial_Services">(PDF) Risk - Adjusted Harm Scoring for Automated Red Teaming for...</a></li>
<li><a href="https://www.themoonlight.io/en/review/risk-adjusted-harm-scoring-for-automated-red-teaming-for-llms-in-financial-services">[Literature Review] Risk - Adjusted Harm Scoring for Automated Red...</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#red teaming`, `#financial services`, `#risk assessment`, `#benchmark`

---

<a id="item-12"></a>
## [AI 辅助劳动市场中的绩效操纵：理论与实证](https://arxiv.org/abs/2604.22230) ⭐️ 8.0/10

该论文提出了一种博弈论模型，其中代理人在 AI 增强下分配创造性和机械性任务的努力，表明当 AI 充分挤占创造性努力时，基于绩效的筛选会退化为不信息的汇聚均衡。 这些发现阐明了在何种情况下 AI 增强的劳动市场仍能依赖可观察的绩效进行招聘或晋升，以及何时此类筛选会产生误导，为政策制定者和企业设计奖励结构和评估标准提供了参考。 该模型证明存在对称单调纯策略均衡，低类型代理人系统性地过度投资于机械性努力而高类型则不然，且更偏斜的奖励结构能减少此操纵；实证验证基于语言模型的努力测量方法，在近 1500 份 Kaggle 竞赛脚本上得到支持。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 绩效操纵指工人专注于易于测量的常规任务来人为提升可观察的产出，而不贡献真正的创新。在 AI 辅助的环境中，AI 增强了基于规则的机械性任务，使其成本降低，可能会挤占稀缺且与私人专业知识互补的创造性努力——这就是雇主真正所看重的。论文采用博弈论框架分析努力分配，表明当 AI 能力足够大时，均衡会转向汇聚状态，此时绩效得分不再揭示工人的类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.22230">Performance Manipulation: Labor Market Implications in AI-assisted Era</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pooling_equilibrium">Pooling equilibrium - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2604.22230">On Benchmark Hacking in ML Contests: Modeling , Insights and Design</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#labor market`, `#game theory`, `#performance manipulation`, `#screening mechanisms`

---

<a id="item-13"></a>
## [数据驱动的随机最优控制用于 intraday 电力交易](https://arxiv.org/abs/2604.27700) ⭐️ 8.0/10

作者提出了一种连续时间的随机最优控制框架用于 intraday 电力交易，其中可再生能源生成遵循 Jacobi 扩散，价格遵循非对称跳跃扩散以捕捉重尾行为。该模型通过状态增广纳入了闸门关闭和基于能量的失结算，并采用单调 IMEX 有限差分方案求解；基于德国市场数据的数值实验表明，该策略优于 TWAP 基准并接近完美预见基准。 该框架为可再生能源生产者提供了一种数据驱动的工具，以管理价格波动和失衡风险，有望提高利润并促进可再生能源在电力市场中的更高渗透。通过将先进的随机建模与真实市场机制相结合，它在理论控制理论与实际 intraday 交易操作之间架起了一座桥梁。 生产过程采用有限的 Jacobi 扩散，而价格动态使用具有季节依赖跳跃强度的非对称跳跃扩散；通过状态增广来处理路径依赖的失衡成本以保持马尔可夫性质，由此得到由两个线尔莫哥洛夫后向方程和一个非线性 Hamilton‑Jacobi‑Bellman 偏微积分方程组成的三阶段动态规划解。通过采用操作符分割、半隐式线性化以及跳跃算子的微分形式的单调 IMEX 有限差分方案实现高效求解。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: intraday 电力市场允许参与者在接近实时交付时交易电力，有助于纠正日前市场的预测误差并减少失衡罚款。可再生能源发电依赖天气，导致输出波动和价格尖峰，这就需要复杂的交易策略来对冲不确定性。随机最优控制将交易建模为连续时间的决策问题，其中状态随随机微分方程演变，目标是最大化期望利润。Jacobi 扩散是有界过程，常用于建模保持在固定范围内的变量，而非对称跳跃扩散则捕捉了电力价格中观察到的重尾和尖峰倾向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s00477-024-02849-2">Stochastic modeling with time-inhomogeneous Jacobi diffusions ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0378437113002434">A jump diffusion model for spot electricity prices and market price of risk - ScienceDirect</a></li>
<li><a href="https://www.emissions-euets.com/internal-electricity-market-glossary/1486-intraday-electricity-market">Intraday electricity market - Emissions-EUETS.com</a></li>

</ul>
</details>

**标签**: `#stochastic optimal control`, `#electricity trading`, `#renewable energy`, `#intraday markets`, `#jump-diffusion`

---

<a id="item-14"></a>
## [同行评审与 AI 筛选对期刊印章价值的建模](https://arxiv.org/abs/2607.13844) ⭐️ 8.0/10

该论文（arXiv:2607.13844v3）提出一个形式模型，比较直接拒绝未审稿件与使用快速但准确度较低的 AI 筛选，以保持期刊印章的价值。模型表明最佳选择取决于高质量工作的普遍程度，并给出了精确的切换点。 了解同行评审与 AI 筛选如何影响期刊印章的感知价值，有助于编辑、出版商和研究者在 AI 工具日益普及的学术环境中设计更佳的评价体系。这些见解还能为作者和机构的基于声誉的激励提供参考。 模型根据高质量稿件的比例得出一个切换阈值；低于该阈值时拒绝未审稿件能提升印章价值，高于则 AI 筛选更佳。当作者自行运行筛选工具时，印章价值由通过筛选的成本决定而非其检测能力，而专家评审则防止此类博弈。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 同行评审是专家对稿件进行评估的传统过程，以期刊的印章批准作为质量的信号向读者表明。当稿件数量超过审稿人能力时，编辑可以选择直接拒绝未阅读的稿件，或使用速度更快但准确度较低的 AI 筛选工具。期刊印章的价值取决于读者对盖章作品与未盖章作品质量的感知差异，这会影响作者的声誉和机构地位。学术出版中的声誉体系通过影响因子、奖项和社区排名等指标来衡量和强化这些信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thesify.ai/blog/ai-tools-academic-peer-review">AI Tools for Academic Peer Review: What They Actually Check ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rankings_of_academic_publishers">Rankings of academic publishers - Wikipedia</a></li>

</ul>
</details>

**标签**: `#peer review`, `#academic publishing`, `#AI screening`, `#reputation systems`, `#scholarly communication`

---

<a id="item-15"></a>
## [PortBench：一种相关性感知的全流程 LLM 驱动投资组合管理基准](https://arxiv.org/abs/2605.27887) ⭐️ 8.0/10

该论文提出了 PortBench，一个涵盖 2015‑2025 年六类异质资产的基准，包含 6,269 道静态问答题和五阶段动态分配流程，并提出两种新指标：双层相关性得分和 CEPS，用于衡量推理错误的级联效应。 PortBench 通过引入跨资产相关性并评估完整决策流程，填补了 LLM 驱动投资组合评估的关键空白，实现更真实的压力测试，为研究者和从业者提供更好的模型设计指导。 该基准涵盖六类资产，静态问答集包含 6,269 题（七种模板），动态五阶段流程，双层相关性得分用于评估跨类对冲和类内集中度，CEPS 用于量化推理错误在各阶段的累积；评估在三种压力窗口、三种风险配置下进行，并采用实时测试以降低预训练污染，结果显示仅有 32.5%的 120 次 LLM 评估在四个市场期间的夏普比率优于等权重基准。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 大型语言模型在许多金融任务中表现出色，但投资组合管理缺乏全面的基准。现有测试常仅关注股票，忽视不同资产类别之间的相关性，并且只评估孤立的环节而非从分析到分配的完整流程。这限制了我们衡量 LLM 在真实市场条件下构建多样化、风险调整后投资组合能力的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://portbench.github.io/">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>
<li><a href="https://arxiv.org/html/2605.27887">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>
<li><a href="https://www.emergentmind.com/topics/portbench">PortBench : LLM -Driven Portfolio Benchmark</a></li>

</ul>
</details>

**标签**: `#LLM`, `#portfolio management`, `#benchmark`, `#finance`, `#AI`

---

<a id="item-16"></a>
## [Fund2Persona 框架从基金披露构建财务顾问角色](https://arxiv.org/abs/2606.29793) ⭐️ 8.0/10

论文提出 Fund2Persona 框架，该框架从真实基金披露数据构建财务顾问角色，并通过演员–评分者–修补者循环进行迭代优化，展示出在投资组合变化预测和提供更具体建议方面优于通用 LLM 顾问。 通过将 LLM‑based 顾问与实际基金经理专业知识相结合，Fund2Persona 填补了个性化金融 AI 的关键空白，有望提升自动化顾问服务的质量和可扩展性。 该框架融合持仓变动、市场背景和经理注释，通过活跃‑delta 准确率和注释一致性验证角色，并在市场情景生成及多轮投资者‑顾问对话中进行评估。

rss · arXiv Quantitative Finance · Sep 1, 04:00

**背景**: 大型语言模型在使用简单角色提示时往往会给出泛泛的财务建议，缺乏真实世界专业知识的深度。基金披露数据——如持仓、交易活动和经理叙事——蕴含了基金经理特定的投资推理。演员‑评分者‑修补者循环是一种迭代方案：演员生成建议，评分者根据源数据评分其忠实度，修补者据此更新角色以减少误差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.29793">[2606.29793] Fund2Persona: A Framework for Building and ...</a></li>
<li><a href="https://arxiv.org/html/2606.29793v3">Fund2Persona: A Framework for Building and Refining Financial ...</a></li>

</ul>
</details>

**标签**: `#AI in Finance`, `#LLM Personas`, `#Fund Disclosure`, `#Personalized Advisory`, `#Actor-Scorer-Patcher`

---