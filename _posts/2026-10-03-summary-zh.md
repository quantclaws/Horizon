---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> From 51 items, 10 important content pieces were selected

---

1. [AI 击败了顶尖人类斯特拉戈玩家。](#item-1) ⭐️ 8.0/10
2. [Redis 创始人 antirez 发布 ds4 以实现本地 LLM 推理](#item-2) ⭐️ 8.0/10
3. [RED-2400 v2 多场景 Solana/DeFi 市场微观结构数据语料库发布](#item-3) ⭐️ 8.0/10
4. [超越超竞争结果：深度强化学习在最优执行博弈中的串通行为](#item-4) ⭐️ 8.0/10
5. [混合机器学习-理论模型提升航运排放反事实预测](#item-5) ⭐️ 8.0/10
6. [提出评估低收入国家农民 AI 天气预报的标准](#item-6) ⭐️ 8.0/10
7. [基于证据的模块化 AI 代理声明验证框架。](#item-7) ⭐️ 8.0/10
8. [乐观的入流预测扭曲巴西水电系统的调度、价格和合同](#item-8) ⭐️ 8.0/10
9. [研究者提出 AI 行为科学的三部分框架](#item-9) ⭐️ 8.0/10
10. [更高的漏洞赏金奖励推动更多高价值漏洞报告](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 击败了顶尖人类斯特拉戈玩家。](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

研究人员开发了一种 AI，通过使用针对隐藏信息游戏的先进算法，超越了最佳人类斯特拉戈玩家，并在训练局数远少于之前工作的情况下达到超人类表现。 这一突破表明现代强化学习技术能够高效求解复杂的不完美信息游戏，为在涉及不确定性的实际场景（如谈判或网络安全）中构建更强的 AI 奠定基础。 新算法将 Neural Fictitious Self‑Play 与 Counterfactual Regret Minimization 的变体相结合，仅需约 2022 年 DeepNash 方法训练局数的 1/34，却在对抗顶尖人类玩家时获得了更高的胜率。

hackernews · PaulHoule · Oct 2, 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**背景**: 斯特拉戈是一种回合制的夺旗棋盘游戏，每位玩家都隐藏自己 40 枚棋子的等级，因此它是典型的不完美信息游戏。求解这类游戏通常依赖于迭代后悔最小化方法，如反事实后悔最小化（CFR），该方法在两人零和博弈中能够收敛到纳什均衡。神经虚构自我对弈（NFSP）则通过结合强化学习与监督学习来近似均衡，无需特定领域知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/mastering-stratego-the-classic-game-of-imperfect-information/">Mastering Stratego , the classic game of imperfect information</a></li>
<li><a href="https://arxiv.org/pdf/1811.00164">Deep Counterfactual Regret Minimization</a></li>
<li><a href="https://arxiv.org/abs/2104.10845">[2104.10845] Optimize Neural Fictitious Self-Play in Regret ... Fictitious Self-Play Reinforcement Learning with Expanding ... Neural Fictitious Self-Play in Imperfect Information Games ... LLM-Powered Neural Fictitious Self-Play (NFSP) Agent</a></li>

</ul>
</details>

**社区讨论**: 评论者回忆起童年玩斯特拉戈的乐趣，惊讶于此类游戏对 AI 构成挑战，并强调新方法的效率——仅需 DeepNash 训练局数的约 1/34——是关键。他们还回顾了之前的 DeepMind 尝试，分享了被标记棋子作弊的经历，并一致认为最新方法终于超过了先前的 AI 工作和顶尖人类玩家。

**标签**: `#AI`, `#Game Theory`, `#Reinforcement Learning`, `#Imperfect Information Games`, `#Stratego`

---

<a id="item-2"></a>
## [Redis 创始人 antirez 发布 ds4 以实现本地 LLM 推理](https://dwarfstar.sh/) ⭐️ 8.0/10

ds4 是由 Redis 创始人 antirez 开发的本地 LLM 启动器，能够在个人硬件上高效运行 DeepSeek V4 Flash、Qwen3.8 Flash Next 和 GLM 等模型。它提供社区构建的绑定和工具，支持文本和视觉模型，并附带 CLI 与原生代理。 ds4 使得大型语言模型能够在高内存机器上本地运行，从而免除云端 API 费用，降低开发者和研究者尝试前沿 LLM 的门槛。其可扩展性已经催生了社区分支和扩展，显示出生态系统的浓厚兴趣。 该引擎是一个针对 DeepSeek V4 Flash 进行优化的窄 C 实现，此外还支持 DeepSeek V4.1 Flash、GLM 5.x、Qwen3.8 Flash Next 以及视觉模型；它提供 CLI、守护进程模式、本地 API 和原生代理，可在 macOS（CUDA/ROCm）以及配备 128 GB+ 内存的 Linux 工作站上运行。

hackernews · fibo · Oct 2, 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49936575)

**背景**: 在本地运行大型语言模型需要大量内存和计算资源，通常需要模型量化和专用推理引擎才能适应消费级硬件。Redis 的创始人 antirez 将其专长转向构建 ds4，这是一种专为高内存机器设计的专用推理引擎。ds4 专注于一组狭窄的模型——主要是 DeepSeek V4 Flash 及其变体——以实现高效、低延迟的推理，而无需依赖云服务。该项目还鼓励社区贡献，例如语言绑定和辅助工具，以扩展其使用范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dwarfstar.sh/about/">About DwarfStar 4 ( ds 4 ): antirez Local Inference Engine</a></li>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local ...</a></li>
<li><a href="https://www.linkedin.com/posts/nayfack_github-antirezds4-deepseek-4-flash-and-activity-7459959128581533696-mm6Q">Antirez Releases ds 4 for Local DeepSeek V4 Flash Model | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 社区成员已经构建了分支和扩展，例如添加了 Vision 和 Qwen 支持的 Go 绑定分支（ds4go），以及针对 Intel Xe‑LP 笔记本的独立推理引擎。用户报告在高端硬件上运行 DeepSeek V4 Flash 和 Qwen 3.8 Flash Next 时性能强劲，尽管偶尔会出现上下文保留问题。还有人对工具调用能力表现出兴趣，并请求提供基准测试或演示。

**标签**: `#LLM`, `#local inference`, `#Redis`, `#ds4`, `#AI tools`

---

<a id="item-3"></a>
## [RED-2400 v2 多场景 Solana/DeFi 市场微观结构数据语料库发布](https://arxiv.org/abs/2610.00005) ⭐️ 8.0/10

作者发布了 RED-2400 家族 v2，包含五个公开基准数据集，覆盖 2026 年 5 月 8 日至 7 月 5 日的 Solana 和跨链 DeFi 活动，并提供固定种子可重复性脚本和 SHA‑256 清单。 该语料库提供了可重复使用、CC‑BY‑4.0 许可的 Solana 预言机滞后、Aave 利用率、 spot‑永续基差、CEX‑DEX 价差以及 Wormhole 跨链流量数据，降低了 Solana 和跨链微观结构研究的数据门槛。 五个数据集分别包含 164,002 条 Pyth 预言机观测、18,750 笔 Aave 清算及四链利用率序列、244,719 条 spot‑永续基差/资金费率观测、328,186 条 CEX‑DEX 价差观测（含实现冲击）以及 360,714 条 Wormhole 跨链消息，均采用 CC‑BY‑4.0 许可并附带可重复性脚本。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: 市场微观结构研究考察价格如何形成以及交易如何在交易所执行，依赖于高频交易和订单簿数据。在去中心化金融（DeFi）领域，此类研究主要局限于以太坊中心的数据集，因为缺乏 Solana 场馆、跨链流动以及链上预言机行为的公开逐条记录。RED‑2400 v2 语料库通过提供同步的、公开可观测的数据来填补这一空白，包括相对于集中交易所价格的 Pyth 预言机滞后、多链 Aave 利用率和清算、spot‑永续基差与资金费率耦合、Solana 上的 CEX‑DEX 价差以及 Wormhole 跨链消息流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chainscorelabs.com/guides/decentralized-finance-defi/oracle-integration/how-to-handle-oracle-price-latency">How to Handle Oracle Price Latency in DeFi | ChainScore Guides</a></li>
<li><a href="https://aave.com/help/aave-101/introduction-to-aave">Introduction To Aave V3 | Aave</a></li>
<li><a href="https://defillama.com/protocols/lending/solana">Solana DeFi Lending Protocols - TVL, Fees, & Revenue</a></li>

</ul>
</details>

**标签**: `#Solana`, `#DeFi`, `#market microstructure`, `#dataset`, `#blockchain`

---

<a id="item-4"></a>
## [超越超竞争结果：深度强化学习在最优执行博弈中的串通行为](https://arxiv.org/abs/2610.00619) ⭐️ 8.0/10

研究者表明，独立的 PPO 代理在 Almgren‑Chriss 清算博弈中学会惩罚偏离，使成本低于纳什基准，并提供了串通的行为证据。 此工作将强化学习、博弈论和市场微观结构联系起来，揭示了多智能体强化学习中出现的串通策略，为金融执行算法和 AI 安全提供了见解。 配备价格和动作历史的独立 PPO 代理学得了一种惩罚性响应，其惩罚幅度超过盈利偏离的收益，而惩罚者的平均收益保持不变；正式检验证实惩罚超过偏离收益，且交易行为的变化能够解释所施加的损失。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: Almgren‑Chriss 模型通过在有限时间范围内平衡临时市场冲击与价格风险来描述最优清算。近端策略优化（PPO）是一种广泛使用的强化学习算法，通过裁剪的 surrogate 目标更新策略，实现代理的稳定训练。在最优执行中，纳什基准指的是每个参与者遵循纳什均衡清算策略时的成本，作为评估合作或串通结果的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathematicsconsultants.com/2021/10/23/optimal-liquidation-algorithms-the-almgren-chriss-model/">Optimal Liquidation Algorithms - the Almgren - Chriss Model</a></li>
<li><a href="https://openai.com/index/openai-baselines-ppo/">Proximal Policy Optimization | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Volume-weighted_average_price">Volume-weighted average price - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#game theory`, `#optimal execution`, `#collusion`, `#financial markets`

---

<a id="item-5"></a>
## [混合机器学习-理论模型提升航运排放反事实预测](https://arxiv.org/abs/2610.01008) ⭐️ 8.0/10

作者开发了混合机器学习-理论模型，既保留了物理中的结构速度响应，又提高了对海运二氧化碳排放的外样本预测。他们通过减速的成本效益分析展示了政策相关性。 仅凭准确的总体预测不足以支持政策决策，因为反事实响应决定了诸如限速等干预措施的净收益。混合方法确保了可靠的反事实估计，这对环境法规和交通领域的机器学习应用至关重要。 混合模型在机器学习部分排除速度相关输入，以保留结构速度响应，同时外样本预测与报告的燃料总量相差仅几个百分点。纯机器学习或无限制回归会削弱速度响应，这可能导致成本效益分析中的净收益符号反转。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: 机器学习虽然能够很好地预测结果，但可能无法捕捉输入变化（如船速）对输出的影响，而这正是进行反事实政策分析所必需的。航运领域中，物理提供了速度与燃料消耗之间的明确速度响应关系，作为理论基准。论文将小时级的 AIS 轨迹数据与欧盟法规下的年度燃料报告相结合，比较了工程计算、结构回归、纯机器学习和混合模型，展示了混合模型如何在保持物理速度响应的同时提升预测准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2610.01008">Modeling Shipping Emissions: Machine Learning, Engineering ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0360544226012430">Review Review of speed optimisation for ship energy ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2590162121000320">A ship emission modeling system with scenario capabilities</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#maritime emissions`, `#counterfactual analysis`, `#hybrid models`, `#environmental policy`

---

<a id="item-6"></a>
## [提出评估低收入国家农民 AI 天气预报的标准](https://arxiv.org/abs/2610.00782) ⭐️ 8.0/10

本文提出一套原则和协议，用于评估与农业相关的 AI 天气预报，以防止低质量预报挤占对低收入国家农民有用的信息。它提出一个框架作为标准的起点，使预报提供者能够可信地传达预报质量。 可靠的预报评估能帮助低收入国家的数百万农民做出更好的农业决策，降低‘竞相下降’的风险。这将 AI 技术进步与服务不足的农村社区的实际需求联系起来。 该提案列出了具体的评估原则（如与作物决策相关、不确定性量化）和协议（如基准数据集、技能得分），并指出其依赖于局部数据以及需要利益相关者参与等局限。强调该框架目前仅为提案，尚未实施。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: AI 天气预报模型能够在有限计算资源下生成高质量预报，为缺乏可靠天气信息的农民提供潜在好处。然而，评估预报质量具有挑战性，可能导致低成本低质量预报的泛滥，误导用户。建立评估标准对于确保可信的 AI 驱动预报支持农业决策至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00782v1">Can we create a ‘race to the top’ for weather forecasts to ...</a></li>
<li><a href="https://climavision.com/agriculture/">Weather Data and Forecasting for Agriculture | Climavision</a></li>
<li><a href="https://deepmind.google/science/weathernext/">WeatherNext 3 is our most advanced global weather AI model.</a></li>

</ul>
</details>

**标签**: `#AI weather prediction`, `#agriculture`, `#forecast evaluation`, `#low-resource settings`, `#standards`

---

<a id="item-7"></a>
## [基于证据的模块化 AI 代理声明验证框架。](https://arxiv.org/abs/2610.01348) ⭐️ 8.0/10

本文提出了一种针对模块化代理的声明特定验证审计，通过记录每个声明的证据、四种裁决及其适用边界来评估声明，而不使用聚合任务得分。该方法结合了神谕政策、完美组件替换以及验证器得分测试，以定位性能变化的具体组件。 通过实现对改进或退步的细粒度归因，该框架帮助开发者定位导致性能变化的具体组件，从而提升 AI 安全性和强化学习研究。它将验证从黑箱评分转变为基于证据的透明审计。 每个结论都会记录其支持证据、四种可能的裁决（支持、不支持、未解决、未评估）以及其成立的边界。审计使用三种工具：神谕政策衡量可达到的改进、用完美组件替换以定位丢失的价值，以及检验验证器得分是否确实界定其声称限制的量。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: 模块化代理将决策分解为可独立更新的组件，如规划器、控制器、学习模型和验证器。传统评估依赖聚合任务得分，这会掩盖各组件的具体贡献。神谕政策通过明确的动作集衡量在给定策略下可达到的最大性能，以隔离环境影响。所提出的声明特定审计将每个声明与具体证据和有界裁决关联，从而实现组件级别的诊断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.01348v1">Verify Claims, Not Scores: Evidence - Based Verification of Modular ...</a></li>
<li><a href="https://ceur-ws.org/Vol-3962/paper20.pdf">Multi-LLM Agents Architecture for Claim Verification</a></li>
<li><a href="https://www.oracle.com/technical-resources/documentation/policy-automation.html">Oracle Policy Automation Documentation</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#verification`, `#modular systems`, `#reinforcement learning`, `#formal methods`

---

<a id="item-8"></a>
## [乐观的入流预测扭曲巴西水电系统的调度、价格和合同](https://arxiv.org/abs/2607.00504) ⭐️ 8.0/10

论文表明，巴西水热系统中持续的乐观入流预测偏差会降低水值并提前增加水电出力，从而扭曲调度、现货价格和合同意愿。 由于预测偏差会直接影响运营决策和市场结果，它导致效率低下、成本上升、可靠性风险以及水电生产者的激励扭曲，对其他以水电为主的市场也有启示。 在理论上，乐观偏差会弱化降低水值并增加首阶段水电出力；经验上，巴西数据显示水库水位降低、热力机组承诺延迟；在偏差预测下的 SDDP 实验得到更尖锐的价格峰值、更高的可靠性风险和更大的预期运营成本，增加价格‑数量风险并降低水电生产者的合同意愿。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: 在以水电为主的电力系统中，集中式水热规划模型利用入流预测来计算水值（即储水的机会成本），并据此安排发电和制定现货价格。巴西的审计成本框架依赖官方入流预测，通过池子结构协调大型多所有者水热机队。随机双动态规划（SDDP）常用于在不确定入流条件下求得最优政策，因而可用于检验预测偏差如何通过规划和市场结果传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optimism_bias">Optimism bias - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/336951960_Empirical_Modelling_of_the_Thermal_Generation_Cost_Function_for_the_Brazilian_Hydrothermal_Scheduling_Problem">(PDF) Empirical Modelling of the Thermal Generation Cost Function for...</a></li>

</ul>
</details>

**标签**: `#power systems`, `#hydroelectric generation`, `#forecast bias`, `#electricity markets`, `#energy economics`

---

<a id="item-9"></a>
## [研究者提出 AI 行为科学的三部分框架](https://arxiv.org/abs/2509.13323) ⭐️ 8.0/10

该论文提出了 AI 行为科学的三部分框架：利用社会科学工具模型 AI 行为、使用 AI 研究人类行为以及分析耦合的人机 AI 系统。 该框架为新兴的跨学科领域提供了研究议程，有助于提升 AI 透明度并评估其对社会和经济的影响。 框架包括三个子领域：(1)借鉴社会科学方法评估 AI 的偏差和启发式；(2)利用 AI 的计算能力模拟和预测人类行为；(3)建模人机交互动态及其对经济政治结果的影响。目前尚未给出具体实证结果。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: AI 行为科学是一个新兴的交叉学科领域，旨在利用社会科学的方法来理解和改善人工智能系统的行为。随着 AI 变得普遍且不透明，研究者需要工具来评估 AI 的偏差、启发式和倾向，就像研究人类行为一样。该领域还探讨 AI 如何增强行为研究以及耦合的人机系统如何影响经济和政治结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.2401336121">AI emerges as the frontier in behavioral science - PNAS</a></li>
<li><a href="https://www.nature.com/articles/s41599-026-07316-7">AI agent behavioral science | Humanities and Social Sciences ...</a></li>
<li><a href="https://ai4pb.stanford.edu/project-categories/ai-behavioral-science">AI and Behavioral Science | AI for Public Benefit Lab</a></li>

</ul>
</details>

**标签**: `#AI`, `#behavioral science`, `#human-AI interaction`, `#social science`, `#research agenda`

---

<a id="item-10"></a>
## [更高的漏洞赏金奖励推动更多高价值漏洞报告](https://arxiv.org/abs/2509.16655) ⭐️ 8.0/10

该研究分析了谷歌漏洞奖励计划在 2024 年 7 月奖励大幅上调后的情况，发现将最高影响等级的奖励提高最高 200%导致高价值漏洞报告增加，劳动供给弹性呈强正值，这种增长既来自老手研究者也吸引了新手研究者。 研究结果表明，通过调整漏洞赏金激励可以吸引更高质量的漏洞报告，为企业设计奖励机制提供实用参考，同时丰富了安全经济学的研究。 作者基于谷歌 VRP 的真实提交数据，测算了高价值漏洞的劳动供给弹性，并表明奖励提高既重新分配了老手研究者的关注，又吸引了新的顶级安全研究者参与。

rss · arXiv Quantitative Finance · Oct 2, 04:00

**背景**: 漏洞赏金计划邀请外部安全研究者发现并报告系统漏洞，以金钱奖励作为回报，奖励通常根据漏洞严重程度划分不同档次。谷歌漏洞奖励计划（VRP）是全球规模最大的项目之一，2024 年 7 月将最高影响等级漏洞的奖励上限从约 31,337 美元提高到约 101,010 美元，涨幅约 200%。劳动供给弹性衡量报酬变动对劳动供给数量（如提交的漏洞报告数）的响应程度，正弹性意味着奖励提高会带来更多研究者的参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515">Increasing Google & Alphabet VRP rewards up to $151,515</a></li>
<li><a href="https://api.emergentmind.com/topics/google-s-vulnerability-rewards-program-vrp">Google Vulnerability Rewards Program Overview</a></li>
<li><a href="https://fiveable.me/principles-econ/key-terms/labor-supply-elasticity">Labor Supply Elasticity | Principles of Economics | Fiveable</a></li>

</ul>
</details>

**标签**: `#bug bounty`, `#security economics`, `#incentive design`, `#empirical study`, `#vulnerability rewards program`

---