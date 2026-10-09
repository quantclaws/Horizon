---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> From 43 items, 9 important content pieces were selected

---

1. [Bevy 0.20 发布，带来渲染优化和新功能。](#item-1) ⭐️ 8.0/10
2. [OpenAI 撤回三项 AI 生成的数学成果](#item-2) ⭐️ 8.0/10
3. [深度学习与统计模型在二手电子产品价格预测中的基准测试](#item-3) ⭐️ 8.0/10
4. [研究发现异构 LLM 在模拟伯特兰市场中表现出不同程度的串通](#item-4) ⭐️ 8.0/10
5. [深度强化学习结合 RNN 用于部分可观测的最优交易](#item-5) ⭐️ 8.0/10
6. [中国加入 WTO 促进创新的动态机制](#item-6) ⭐️ 8.0/10
7. [显而易见的扩散：市场影响的不显眼定律](#item-7) ⭐️ 8.0/10
8. [草根 CBDC 实现信贷并防止外流。](#item-8) ⭐️ 8.0/10
9. [AlphaPADI 提出池感知层次离散扩散方法用于符号 alpha 发现](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bevy 0.20 发布，带来渲染优化和新功能。](https://bevy.org/news/bevy-0-20/) ⭐️ 8.0/10

Bevy 0.20 引入了随实体变化数量线性扩展的 O(changed entities) CPU 渲染器，并加入了多项新功能和改进。 此版本通过提升大场景性能展示了 Bevy 的快速迭代，吸引了游戏开发者和模拟构建者。 该 O(changed entities) 渲染器由 pcwalton 贡献，社区反馈指出 BSN 语法过于复杂以及频繁的破坏性更改是需要改进的地方。

hackernews · Philpax · Oct 8, 22:57 · [社区讨论](https://news.ycombinator.com/item?id=50013610)

**背景**: Bevy 是一个使用 Rust 编写的免费开源游戏引擎，采用实体组件系统（ECS）架构来实现数据导向、可并行的游戏逻辑。它通过 wgpu 图形 API 提供跨平台渲染，支持 Vulkan、Metal、DirectX 12 和 OpenGL。Bevy 大约每三个月发布一次新版本，带来新功能和破坏性更改，并提供迁移指南。其模块化设计使开发者可以仅按需引入所需组件，适用于游戏和仿真等场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bevy.org/">Bevy Engine</a></li>
<li><a href="https://github.com/bevyengine/bevy">GitHub - bevyengine/bevy: A refreshingly simple data-driven ... Learn Bevy - Bevy Engine Bevy Engine by bevy - Itch.io Rust Game Development with Bevy Engine: Complete 2026 Guide Bevy Game Engine Guide - gamineai.com Rust for Game Development: Getting Started with Bevy in 2026</a></li>
<li><a href="https://docs.rs/bevy_ecs/latest/bevy_ecs/">bevy_ecs - Rust - Docs.rs</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞了渲染优化，并表达了在城市建造者、即时战略游戏等项目中使用 Bevy 的热情。多位评论者批评 BSN 语法过于复杂，并指出频繁的破坏性更改可能成为商业采用的障碍。总体而言，讨论显示出浓厚兴趣以及对引擎未来方向的建设性反馈。

**标签**: `#bevy`, `#rust`, `#game-engine`, `#release`, `#graphics`

---

<a id="item-2"></a>
## [OpenAI 撤回三项 AI 生成的数学成果](https://twitter.com/danintheory/status/2108065033070789090) ⭐️ 8.0/10

OpenAI 从其公开的数学仓库中撤回了三项 AI 生成的数学成果，因为人们对其正确性和验证提出了担忧。 此次撤回凸显了确保 AI 生成数学可靠性的持续挑战，并凸显了 Lean 等形式验证工具在验证此类结果中的日益重要作用。 被撤回的论文是 OpenAI 在 2026 年 10 月 6 日发布的 372 篇 AI 生成数学手稿的一部分；其中一些拥有 Lean 证书，而另一些仅用自然语言表达，撤回是在数学家审阅仓库后发现错误之后进行的。

hackernews · sashank_1509 · Oct 8, 07:05 · [社区讨论](https://news.ycombinator.com/item?id=50002650)

**背景**: OpenAI 一直在发布大量 AI 生成的数学手稿，以探索语言模型是否能够产出新颖的定理。Lean 是一种证明助手和函数式编程语言，使数学家能够编写可由机器检查的证明，从而提供高度的确定性。使用 Lean 等工具进行形式验证对于验证复杂的 AI 生成结果变得越来越重要，因为传统的同行评审可能会忽略冗长论证中的细微错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/blog/openai-math-breakthroughs-what-the-latest-results-mean">OpenAI’s AI Math Breakthroughs: What the Latest Results Mean</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_mathematical_discoveries_by_artificial_intelligence">List of mathematical discoveries by artificial intelligence</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑被撤回的证明是否缺乏 Lean 验证，指出其中混有经过验证和未验证的作品。一些人表示怀疑，即使经过 Lean 检查的 AI 生成证明也可能隐藏错误，只有在经过广泛审查后才会暴露。还有人将此情况比作软件工程实践，建议所有结果都应完全形式化以避免错误。

**标签**: `#AI`, `#mathematics`, `#formal verification`, `#Lean`, `#retractions`

---

<a id="item-3"></a>
## [深度学习与统计模型在二手电子产品价格预测中的基准测试](https://arxiv.org/abs/2610.10727) ⭐️ 8.0/10

该论文对包括 ARIMA、LSTM、N-BEATS、TFT、PatchTST、Informer、TCN、ETS、Theta 等在内的十一种预测模型进行了基准测试，使用波兰在线市场的日度价格挂牌数据（2022 年 1 月至 2025 年 3 月），预测 horizon 从 1 天到 365 天。 它为一个小众但经济重要的领域提供了首个系统的多 horizon 统计与深度学习方法比较，表明 N-BEATS 能够将长 horizon 预测误差相较于最佳统计基线降低超过 40%。 N-BEATS 在 30 天以后的预测中 MAPE 最低，365 天达到 8.51%，而最佳统计基线为 14.94%，降幅达 43%；在短 horizon（1‑7 天）所有模型收敛于约 0.72% MAPE，且单个在 365 天上训练的 N-BEATS 模型能够泛化到所有更短 horizon，同时 N-BEATS 与 N-HiTS 展现出更好的超参数稳定性。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 时间序列预测基于历史观测预测未来值，统计方法如 ARIMA、ETS 和 Theta 依赖对趋势和季节性的显式假设，而深度学习模型如 LSTM、TCN、N‑BEATS、N‑HiTS、TFT、PatchTST 和 Informer 则直接从数据中学习复杂模式。由于高波动性、稀疏的挂牌历史和非正态价格动态，二手电子产品的转售价格预测尤具挑战性，这与金融市场中较为稳定的模式不同。本文通过提供大规模真实世界基准，跨多个 horizon 和评估协议评估统计与深度学习两类模型，填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://towardsdatascience.com/n-beats-time-series-forecasting-with-neural-basis-expansion-af09ea39f538/">N-BEATS : Time-Series Forecasting with Neural Basis Expansion</a></li>
<li><a href="https://arxiv.org/abs/1912.09363">[1912.09363] Temporal Fusion Transformers for Interpretable...</a></li>
<li><a href="https://huggingface.co/docs/transformers/main/en/model_doc/patchtst">PatchTST - Hugging Face</a></li>

</ul>
</details>

**标签**: `#time-series forecasting`, `#deep learning`, `#statistical models`, `#price prediction`, `#second-hand electronics`

---

<a id="item-4"></a>
## [研究发现异构 LLM 在模拟伯特兰市场中表现出不同程度的串通](https://arxiv.org/abs/2610.11256) ⭐️ 8.0/10

作者使用 Claude、Gemini、DeepSeek 和 GPT 的最便宜版本，在四企业 logit 伯特兰市场中进行了模拟，测试了 11 种模型组合，每种组合进行 20 次运行，每次运行 200 个周期。结果显示，Claude 和 Gemini 主导的市场获得了 72%–79%的垄断利润，DeepSeek 市场约为 24%，而 GPT 市场几乎没有串通，价格甚至漂移到垄断水平之上。 结果表明，异构 AI 代理在没有显式通信的情况下也可能产生算法串通，这凸显了 AI 驱动市场的新安全风险。这对反垄断政策、AI 治理以及未来基于语言模型的交易系统设计具有重要影响。 混合不同模型本身并不会降低串通程度；市场的稳定性取决于最不稳定的参与者，两家 GPT 公司就足以阻止收敛。在混合市场中，垄断利润按照 DeepSeek > Claude > Gemini > GPT 的顺序分配，这与各模型的初始价格锚点呈反向关系，符合价格领导模型的预测。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 在 logit 伯特兰市场中，企业为差异化产品定价，消费者根据效用以概率方式选择购买，从而得到光滑的最佳响应函数。算法串通是指定价算法在没有显式通信的情况下，自发趋向于高于竞争水平的价格，类似于卡特尔的结果。垄断租利指的是企业在能够独占供应时，相对于竞争状态所获得的额外利润；本实验中通过市场实际获得的垄断利润比例来衡量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2406.02437">Algorithmic Collusion in Dynamic Pricing with Deep Reinforcement...</a></li>
<li><a href="https://arxiv.org/pdf/2404.00806">Algorithmic Collusion by Large Language Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bertrand_competition">Bertrand competition - Wikipedia</a></li>

</ul>
</details>

**标签**: `#algorithmic collusion`, `#language models`, `#market economics`, `#AI safety`, `#multi-agent systems`

---

<a id="item-5"></a>
## [深度强化学习结合 RNN 用于部分可观测的最优交易](https://arxiv.org/abs/2511.00190) ⭐️ 8.0/10

该论文（arXiv:2511.00190v2，2025 年 11 月发布）提出了三种结合循环神经网络的强化学习方法，用于在仅能观测到部分市场信息的情况下推断潜在市场状态并得出最优交易策略。 通过将交易信号建模为具有 regime‑switching 参数的 Ornstein‑Uhlenbeck 过程，并将问题视为部分可观测马尔可夫决策过程，该工作为提升算法交易系统的表现和可解释性提供了一种 principled 方法。 作者将一步 GRU 方法与两种两步方法进行比较：一种将后验 regime 概率估计输入 RL 代理，另一种则输入下一信号值的预测；仿真表明后验概率方法获得更高的累积奖励且策略更具可解释性。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 部分可观测马尔可夫决策过程（POMDP）用于建模代理无法直接观测系统状态，而必须通过观测推断状态的决策问题。本文中的交易信号遵循均值回复的 Ornstein‑Uhlenbeck 过程，其参数会在不同 regime 之间切换，从而产生交易者需要估计的潜在动态。循环神经网络（RNN），尤其是门控循环单元（GRU），被用来处理观测历史并生成关于潜在 regime 或未来信号值的信念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.opentrain.ai/glossary/partially-observable-markov-decision-process-pomdp/">Partially Observable Markov Decision Process ( POMDP ) Definition</a></li>
<li><a href="https://www.emergentmind.com/topics/ornstein-uhlenbeck-process">Ornstein - Uhlenbeck Process : Theory & Extensions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recurrent_neural_network">Recurrent neural network - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#financial trading`, `#partially observable Markov decision process`, `#recurrent neural networks`, `#algorithmic trading`

---

<a id="item-6"></a>
## [中国加入 WTO 促进创新的动态机制](https://arxiv.org/abs/2603.23825) ⭐️ 8.0/10

研究发现，中国加入 WTO 使空调制造业的冰山贸易成本下降约 13.5%，显著提高出口和产品创新的概率，主要通过动态机制——即出口和创新使企业预期进入更高生产率状态并降低未来进入成本——来实现。 该研究表明，创新响应的大部分来源于前瞻性的动态激励而非静态成本降低，凸显了贸易政策如何通过激励企业的前瞻决策促进长期增长和创新。 静态效应仅占总影响的 9.2%；关闭状态转移通道后仍保留 62.4%的效应，关闭进入成本节约后保留 28.5%，说明动态机制是创新响应的主要驱动力。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 贸易自由化通过降低冰山贸易成本（即所有国际贸易摩擦的乘法因子τ≥1）来减少贸易壁垒。中国在 2001 年加入世界贸易组织提供了一个天然实验，以研究此类成本下降对企业行为的影响。在异质企业模型中，企业会进行前瞻性决策，权衡当前利润与未来更高生产率状态的预期以及进入成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iceberg_Transport_Cost_Model">Iceberg transport cost model - Wikipedia</a></li>
<li><a href="https://ideas.repec.org/p/aah/aarhec/2012-03.html">A Dynamic Model of Trade with Heterogeneous Firms</a></li>

</ul>
</details>

**标签**: `#trade liberalization`, `#product innovation`, `#dynamic firm model`, `#China WTO accession`, `#iceberg trade costs`

---

<a id="item-7"></a>
## [显而易见的扩散：市场影响的不显眼定律](https://arxiv.org/abs/2606.07059) ⭐️ 8.0/10

该论文表明，对实现收益和反事实收益同时施加扩散性条件将得到一个结构身份，该身份限制了市场影响动态，在信息中性 regime 下产生平方根定律，而在强信息耦合下则转向线性影响。 该结果将微观收益的扩散性与宏观影响的尺度联系起来，为观测到的平方根定律及其向线性影响的过渡提供了理论基础，对量化金融中的最优执行策略和无套利约束具有直接意义。 在信息中性 regime 下，累积影响本身变得扩散，保持一个未确定的全通自由度，这阻止其简化为纯惊喜模型，并允许瞬态影响动态和严格正的影响成本。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 市场影响是指执行交易导致的价格变化，经验上其典型幅度随交易规模的平方根在各种资产和时间尺度上呈现规律。扩散过程描述的是增量独立且服从正态分布的变量，类似布朗运动，常用于建模随机价格变动。信息中性 regime 指的是交易者的订单流与底层价格运动无关，此时实现收益和反事实收益表现出扩散性。在此条件下，对这两类收益同时施加扩散性约束会限制影响动态，在信息中性情况下导致平方根定律，而在信息耦合增强时则过渡到线性影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ceedtrading.com/glossary/market-impact-square-root-law/">Market impact square root law - CEED.trading</a></li>
<li><a href="https://www.mccormick.northwestern.edu/applied-math/areas/diffusive-processes.html">Diffusive Processes | Research Areas | Engineering Sciences...</a></li>
<li><a href="https://arxiv.org/html/2606.07059v2">Diffusive in plain sight: An inconspicuous law of market impact</a></li>

</ul>
</details>

**标签**: `#market impact`, `#quantitative finance`, `#diffusive processes`, `#optimal execution`, `#no-arbitrage`

---

<a id="item-8"></a>
## [草根 CBDC 实现信贷并防止外流。](https://arxiv.org/abs/2609.27727) ⭐️ 8.0/10

该论文提出了一种基于草根货币的 CBDC 架构，包括由中央银行发行的主权草根币、任何人可发行的非主权草根币以及增加期限和利息的草根债券。
该设计在不触发存款外流的情况下实现了信贷创造和货币政策操作，并在小规模实施中得到验证。 通过解决传统 CBDC 设计中的存款外流风险和缺乏信贷创造功能，该架构有望提升货币政策的有效性，并扩大非银行对手方获得中央银行流动性操作的途径。
这对金融稳定、金融科技创新以及数字货币的未来演化具有重要影响。 主权草根币是由中央银行发行的等值于一单位法定货币的数字债权；非主权草根币可由任何自然人或法人发行，按面值兑换，其无套利价格等于一单位法定货币。
草根债券提供期限和利息，使中央银行能够放款、吸收流动性、设定利率并买卖证券，而无需将银行存款转换为新发行的中央银行货币；该系统已在小规模上进行测试。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 中央银行数字货币（CBDC）是法定货币的数字形式，是对中央银行的直接要求，但现有设计常因公众将银行存款转换为 CBDC 而导致存款外流。
草根货币允许任何个人或实体发行面值为一单位法定货币的数字代币，这些代币可在 CBDC 框架内用于创造信贷。
通过将主权（中央银行发行）和非主权（公众发行）草根币分离并引入草根债券，所提出的架构旨在保持货币的信贷创造功能，同时缓解快速存款外流的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.27727">[2609.27727] Sovereign Grassroots Currencies : A CBDC ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2609.27727">Sovereign Grassroots Currencies : A CBDC Architecture for Credit...</a></li>
<li><a href="https://www.atlanticcouncil.org/cbdctracker/">Central Bank Digital Currency Tracker - Atlantic Council</a></li>

</ul>
</details>

**标签**: `#CBDC`, `#grassroots currency`, `#monetary policy`, `#digital currency`, `#financial architecture`

---

<a id="item-9"></a>
## [AlphaPADI 提出池感知层次离散扩散方法用于符号 alpha 发现](https://arxiv.org/abs/2610.04959) ⭐️ 8.0/10

AlphaPADI 提出了一种池感知层次离散扩散框架，通过将整个 alpha 池作为生成、评估和学习的统一单元，来生成互补的符号 alpha 公式以预测资产收益。 通过克服先前强化学习和生成流网络方法的局限性（如缺乏池上下文和统一的结构修订机制），AlphaPADI 实现了更好的预测和投资组合表现，推动了量化金融中的自动化 alpha 发现。 该框架包括语法约束的缓冲区初始化以构建语法有效的 alpha 池候选、池感知层次离散扩散在当前池上下文下多尺度结构重建池、以及基于奖励的池精炼，用于评估联合预测表现和内部多样性，更新精英缓冲区，并通过重建和偏好学习训练逆模型。

rss · arXiv Quantitative Finance · Oct 9, 04:00

**背景**: 符号 alpha 发现旨在寻找能够预测截面资产收益的符号表达式；实际应用中，多个公式会被组合成一个 alpha 池，每个公式的价值来源于其对联合预测表现的互补贡献。层次离散扩散模型在离散状态空间上应用多级去噪，以结构化方式生成数据，能够在不同抽象层次上进行生成。之前基于强化学习或生成流网络的方法通常是单独生成公式，缺乏显式的池上下文以及在不同尺度上保持和修订公式结构的统一机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2610.04959">AlphaPADI: Formulaic Alpha Discovery via Pool - Aware Hierarchical ...</a></li>
<li><a href="https://www.emergentmind.com/topics/hierarchical-discrete-diffusion-model">Hierarchical Discrete Diffusion Model</a></li>
<li><a href="https://grokipedia.com/page/Generative_flow_network">Generative flow network</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#quantitative finance`, `#symbolic regression`, `#diffusion models`, `#alpha discovery`

---