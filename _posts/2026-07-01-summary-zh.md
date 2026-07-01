---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> From 69 items, 21 important content pieces were selected

---

1. [Anthropic 发布 Claude Sonnet 5，专注于具代理行为的 AI 模型](#item-1) ⭐️ 8.0/10
2. [Anthropic 发布 Claude Science 数据科学 AI 助手](#item-2) ⭐️ 8.0/10
3. [黑客新闻讨论 1852 年经典著作《众愚奇谈》与金融泡沫](#item-3) ⭐️ 8.0/10
4. [在 Lean 4 中形式化资产定价基本定理](#item-4) ⭐️ 8.0/10
5. [供应链增强型 LLM 嵌入预测股票收益](#item-5) ⭐️ 8.0/10
6. [贝叶斯优化在低维均衡流形上求得最优碳税。](#item-6) ⭐️ 8.0/10
7. [基于贝叶斯的治理感知 POMDP 的自适应 AI 授权](#item-7) ⭐️ 8.0/10
8. [瑞士卡特尔模拟竞争以掩盖串标。](#item-8) ⭐️ 8.0/10
9. [路径的一般理论：签名、跳跃提升和自激过程的期望签名](#item-9) ⭐️ 8.0/10
10. [LLM 压缩金融文本可能扭曲投资决策](#item-10) ⭐️ 8.0/10
11. [CLQT：闭环、成本感知的 LLM 投资组合管理代理基准](#item-11) ⭐️ 8.0/10
12. [置换不变微调使元数据检索对字段顺序鲁棒](#item-12) ⭐️ 8.0/10
13. [通过 380 万亿 Tokens 的 LLM 使用识别 AI 溢价](#item-13) ⭐️ 8.0/10
14. [深度神经网络通过投资组合切线核得到线性因子模型](#item-14) ⭐️ 8.0/10
15. [广告禁令结束智利药店亏损价格战并实现价格协同](#item-15) ⭐️ 8.0/10
16. [Lean 4 形式化数学金融库，包含伊托积分和风险中性度量](#item-16) ⭐️ 8.0/10
17. [Lean 4 中的布朗运动伊托微积分机器检验](#item-17) ⭐️ 8.0/10
18. [中国国内科学现在超越美国在专利中的贡献。](#item-18) ⭐️ 8.0/10
19. [研究将企业房东集中度与少数族裔社区租金增长加快联系起来](#item-19) ⭐️ 8.0/10
20. [无限维流形上可微映射的加权通用逼近](#item-20) ⭐️ 8.0/10
21. [KineticSim 将市场模拟吞吐量提升至每秒 547 亿事件。](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Sonnet 5，专注于具代理行为的 AI 模型](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Sonnet 5，这是首个具备实时网络安全防护的 Sonnet 级模型，专注于具代理行为，并成为免费和专业计划的默认模型，向所有用户开放。 此次发布表明 Anthropic 正在推动更安全、更自主的 AI 代理，为开发者提供了一种在具代理任务上更具成本效益的选择，同时凸显了与更高端 Opus 模型之间的成本‑性能权衡。 Claude Sonnet 5 的不良行为发生率低于 Sonnet 4.6，但相比 Opus 模型其执行网络安全任务的能力显著降低，且它是首个具备实时网络安全防护的 Sonnet 模型。

hackernews · marinesebastian · Jun 30, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48736605)

**背景**: Claude Sonnet 系列是 Anthropic 介于轻量级 Haiku 和高性能 Opus 之间的中等规模大语言模型系列。具代理行为的 AI 指能够自主规划、使用诸如浏览器或终端之类的外部工具并执行多步骤任务，且只需少量人工干预的系统。之前的 Sonnet 4.6 和 Opus 4.8 在推理和工具使用方面设定了基准，而 Sonnet 5 加入了实时网络安全拒答机制，以提升具代理场景下的安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5">What's new in Claude Sonnet 5 - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者就该模型的成本效益展开讨论，指出 Opus 在每美元性能上往往更优，Sonnet 5 仅在低努力级别或 Opus 额度用尽时才有意义。一些用户称赞其在具代理任务中的工具使用和自主规划能力更强，而另一些则指出其在通用知识、工具调用可靠性方面的不足，以及网络安全拒答对实用性的影响。

**标签**: `#Claude Sonnet 5`, `#Anthropic`, `#LLM`, `#AI agents`, `#model release`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Science 数据科学 AI 助手](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 推出了 Claude Science，一个专为数据科学设计的 AI 助手，它运行本地 Model Context Protocol 服务器并提供网页 UI，可连接机构集群、数据库和计算工具。 通过允许大语言模型在安全的本地环境中运行，Claude Science 在先进 AI 与现有高性能计算和数据工作流之间架起桥梁，有望加速制药、生物技术等领域的研究。 Claude Science 运行本地 MCP 服务器并提供桌面扩展，集成 Jupyter 风格的笔记本、数据库和 HPC 集群，生成可审计的成果并支持灵活的计算访问；早期用户指出其方法可能较为 naive，且在某些生物设计中的脱靶筛选有限。

hackernews · lebovic · Jun 30, 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: Claude 是 Anthropic 推出的下一代 AI 助手，旨在提供安全、准确且可靠的通用生产力支持。 Model Context Protocol（MCP）是一种开放协议，使 LLM 应用能够连接外部数据源和工具；其本地服务器版本允许用户在自己的机器上运行连接器以实现隐私保护。 机构集群，如哥伦比亚大学共享研究计算设施或斯坦福 HPCC 提供的高性能计算资源，是在各研究小组之间共享的，用于运行大规模模拟和数据分析。 Claude Science 在这些基础之上构建了一个私密且可控的 AI 工作台，使科学家能够调用所在机构的 HPC 和数据存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop">Getting Started with Local MCP Servers on Claude Desktop</a></li>
<li><a href="https://www.cuit.columbia.edu/shared-research-computing-facility">High Performance Computing — HPC | Columbia University ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Claude Science 的本地服务器架构及其连接机构 HPC、数据库和工具的能力，指出它在数据科学工作流中具有即时实用性。 有用户在 RNAi 农药设计等专业领域进行测试后认为 AI 的建议有用，但指出其方法较为 naive 且脱靶筛选有限，表明仍有提升空间。 总体来看，讨论显示出对该产品集成能力的浓厚兴趣，同时也凸显了对其成熟度和科学推理深度的担忧。

**标签**: `#AI`, `#Data Science`, `#Anthropic`, `#Claude`, `#Scientific Computing`

---

<a id="item-3"></a>
## [黑客新闻讨论 1852 年经典著作《众愚奇谈》与金融泡沫](https://www.gutenberg.org/ebooks/24518) ⭐️ 8.0/10

一则黑客新闻帖子链接到 1852 年的《众愚奇谈》，引发了关于该书对金融泡沫和群众行为历史叙述的讨论。 此次讨论表明，该书对群众心理的洞见至今仍具现实意义，为当代行为经济学和对诸如 AI 股票投机等市场狂热的解读提供参考。 评论者指出书中生动描述了郁金香狂热、南海泡沫和密西西比公司事件，同时指出部分故事被夸大，并提及约翰·肯尼斯·加尔布雷斯的《金融狂热简史》等相关著作。

hackernews · lstodd · Jun 30, 12:47 · [社区讨论](https://news.ycombinator.com/item?id=48731989)

**背景**: 该书由苏格兰记者查尔斯·麦凯撰写，首次出版于 1841 年，收录了众多流行的神话、丑闻和骗局，重点探讨群众热情如何推动投机狂热。此后，它成为研究群众心理和金融泡沫的经典参考，对后来的经济学、社会学和心理学著作产生了影响。

**社区讨论**: 评论者称赞书中趣闻轶事，如南海泡沫期间的虚假投资摊位，但也有人认为麦凯夸大了郁金香狂热等事件。还有人提到了相关读物，分享了个人对非理性的体悟，并将讨论与当前杠杆投资 AI 股票联系起来。

**标签**: `#behavioral-economics`, `#crowd-psychology`, `#financial-bubbles`, `#history`, `#book-discussion`

---

<a id="item-4"></a>
## [在 Lean 4 中形式化资产定价基本定理](https://arxiv.org/abs/2606.28990) ⭐️ 8.0/10

该论文在 Lean 4 的 Mathlib 库中形式化了资产定价基本定理，覆盖三种市场设置：有限状态有限期市场（Harrison‑Pliska）、一期标量市场（Follmer‑Schied）以及 d 资产一期市场，并在不使用 Hahn‑Banach、L^0‑封闭性、可测选择或非冗余假设的情况下显式构造了等价鞅测度。 这是首次在任何证明助手中机器检查资产定价基本定理的证明，表明交互式定理证明可以为金融数学的核心结果提供严格基础，并促进进一步的验证工作。 构造过程避免了 Hahn‑Banach、L^0‑封闭性、可测选择和非冗余假设；在 d 资产情况下，等价鞅测度是凸泛函 𝔼[log(1+e^{⟨θ,Y⟩})] 的最小化点，其强 coercivity 刻画了无套利条件，一阶条件给出鞅性质。所有定理均无 sorry，且整个开发可在固定的 Lean 4 工具链上复现。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: Lean 4 是一种基于归纳类型的构造演算的证明助手兼函数式编程语言，而 Mathlib 是一个由社区维护的、建立在 Lean 上的大型形式化数学库。资产定价基本定理指出，一个金融市场无套利当且仅当存在一个等价鞅测度，即一个与实际概率测度等价、使得折后资产价格成为鞅的概率测度。等价鞅测度是风险中性定价和完整市场理论的核心概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://lean-lang.org/use-cases/mathlib/">Mathlib : A Foundation for Formal Mathematics Research... — Lean Lang</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_asset_pricing">Fundamental theorem of asset pricing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#Lean 4`, `#mathematical finance`, `#asset pricing`, `#theorem proving`

---

<a id="item-5"></a>
## [供应链增强型 LLM 嵌入预测股票收益](https://arxiv.org/abs/2606.29290) ⭐️ 8.0/10

本文提出了一种框架，将 FinBERT 对 10-K MD&A 章节的嵌入与供应链知识图谱传播相结合，构建网络增强的收益预测因子，覆盖 2011‑2025 年的 255 只 S&P 500 成分股。 通过将文本披露与企业间网络结构相连接，该方法提供了一种新颖的阿尔法来源，能够在控制标准因子和样本外检验后仍然存在，有望改进资产定价模型。 通过 Fama‑MacBeth 横截面回归，网络增强因子（net_pc_5）的 Newey‑West t 统计量为‑2.64，基于该因子的多空组合年化夏普比率为 0.86，Fama‑French 五因子年化阿尔法为 7.27%（t=2.30）。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 像 FinBERT 这样的大型语言模型能够将文本披露转换为捕捉语义信息的密集向量嵌入。供应链知识图谱描述了公司之间的关系，使得信息可以在供应链网络中传播。Fama‑MacBeth 两步法用于估计风险溢价，而 Newey‑West 标准误则用于修正金融时间序列中的异方差和自相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terence-lim.github.io/docs/financial-data-science-notebooks/1.4_fama_macbeth.html">Fama - Macbeth Cross - sectional Regressions — Financial Data...</a></li>
<li><a href="https://deepwiki.com/fire-institute/fire/6.2-statistical-testing">Statistical Testing | fire-institute/fire | DeepWiki</a></li>
<li><a href="https://diagrams.so/d/supply-chain-kg-nl-query-system-architecture-jaNzQQ">Supply Chain Knowledge Graph NL Query — Azure LLM Architecture</a></li>

</ul>
</details>

**标签**: `#LLM embeddings`, `#supply chain`, `#asset pricing`, `#finance`, `#network analysis`

---

<a id="item-6"></a>
## [贝叶斯优化在低维均衡流形上求得最优碳税。](https://arxiv.org/abs/2606.29299) ⭐️ 8.0/10

文章表明，当均衡流形可用低维 Negishi 权重参数化时，贝叶斯优化能够可靠地近似并认证解。他们将此方法应用此方法于异用于异构代理人气候经济模型以计算最优碳税。 这项工作将机器学习进步与宏观经济政策分析联系起来，为处理异构代理人模型中的多重均衡提供了实际方法。它使得在现实经济复杂性下设计更稳健的气候政策（如碳税）成为可能。 该方法依赖于均衡流形的 Negishi 权重参数化，利用贝叶斯优化以高概率找到近似解，并在一个包含气候变化的动态经济模型上进行演示，尽管存在碳外部性，竞争均衡很可能是唯一的。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: Negishi 权重是一组福利权重，用于参数化一般均衡模型中的帕累托有效分配集合，从而使均衡流形能够以低维形式表示。贝叶斯优化是一种基于模型的序列策略，用于优化黑箱函数，通过构建概率代理（通常是高斯过程）来引导采样并以高概率认证解。异构代理人宏观经济模型包含具有不同特征（如收入、生产率）的代理人，由于互补性或气候变化等外部性，可能产生多重均衡。均衡流形捕捉了作为基本参数函数的所有可能均衡，当其为低维时，对其进行优化变得可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Takashi_Negishi">Takashi Negishi - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_optimization">Bayesian optimization - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0959652625017032">Optimizing the carbon taxation mechanism in heterogeneous ...</a></li>

</ul>
</details>

**标签**: `#Bayesian optimization`, `#macroeconomics`, `#heterogeneous-agent models`, `#climate policy`, `#equilibrium manifold`

---

<a id="item-7"></a>
## [基于贝叶斯的治理感知 POMDP 的自适应 AI 授权](https://arxiv.org/abs/2606.29406) ⭐️ 8.0/10

本文提出了一种治理感知的部分可观测马尔可夫决策过程（POMDP），利用贝叶斯推断估计信息状态，并通过序列优化在不断变化的不确定性下动态分配 AI 的决策权限。 该框架提供了首种用于高风险环境中动态分配 AI 权限的定量方法，能够在证据质量变化时以原则性的方式平衡 AI 辅助与人工监督。 该方法将贝叶斯信念更新与序列优化相结合，通过合成压力测试、LLM 置信度鲁棒性、预测准确性、治理偏好敏感性以及脆弱 AI 早期警告实验进行验证，在不同 AI 质量 regimes 下优于五种基准治理启发式方法。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 部分可观测马尔可夫决策过程（POMDP）用于建模智能体无法直接观察底层状态但可通过贝叶斯推断更新信念分布的决策情景。在 AI 治理中，向大型语言模型授予决策权需要评估其概率建议的质量，因为不确定性会随时间变化。治理感知的 POMDP 在此基础上将组织目标和不确定性纳入信念状态，从而实现对向 AI 让渡多少决策权的序列优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.29406">Adaptive AI Delegation under Uncertainty: A Bayesian ...</a></li>
<li><a href="https://andrewtorgesen.com/notes/Autonomy/Estimation/Applied_Statistics_for_Stochastic_Processes/Bayesian_Inference.html">Bayesian Inference - Andrew's Notes</a></li>
<li><a href="https://www.aptlydone.com/blog/ai-delegation-of-authority-governance">How AI Is Transforming Delegation of Authority | Aptly Blog</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#POMDP`, `#Bayesian inference`, `#decision authority`, `#large language models`

---

<a id="item-8"></a>
## [瑞士卡特尔模拟竞争以掩盖串标。](https://arxiv.org/abs/2606.30470) ⭐️ 8.0/10

本文考察了瑞士提契诺州道路建设卡特尔（1999‑2005），发现其成员采用基于成本的分配机制，模拟竞争性投标。通过双重机器学习，作者估计该卡特尔的超收费至少达 45%。 该研究揭示了复杂卡特尔如何规避常规检测工具，为反垄断机构提供了一种新的实证策略，以发现隐蔽串标并量化其财务影响。 通过对“公约”文件的分析，作者表明可观察的成本代理变量能够预测中标投标及其排名，并采用双重机器学习估算平均超收费至少为 45%，甚至可能更高。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 在采购领域，卡特尔常通过协调投标来抬高价格，而检测则依赖于与竞争行为的偏差。最近的计量经济学进展，如双重机器学习，能够在控制高维混杂变量的同时分离因果效应，因而即使卡特尔模拟竞争行为也能评估其串标影响。提契诺案例表明，正式协议可以产生一种基于成本的分配机制，在不进行副付款的情况下紧密逼近第一最优串标结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.30470">[2606.30470] Swimming in Dark Water: When Cartels Mimic Competition</a></li>
<li><a href="https://www.linkedin.com/pulse/what-double-machine-learning-dml-why-should-economists-eker-a4q1f">What Is Double Machine Learning (DML) and Why Should...</a></li>
<li><a href="https://trainings.doubleml.org/about.html">About – DoubleML Trainings</a></li>

</ul>
</details>

**标签**: `#cartel detection`, `#econometrics`, `#machine learning`, `#industrial organization`, `#antitrust`

---

<a id="item-9"></a>
## [路径的一般理论：签名、跳跃提升和自激过程的期望签名](https://arxiv.org/abs/2606.28869) ⭐️ 8.0/10

本文提出了一种以签名为普遍坐标的路径优先框架，适用于确定的、粗糙的、跳跃的和随机路径，并证明了几何性缺陷定理将二次协方差与 shuffle 乘法性的失败联系起来。此外，它还为纯跳跃路径建立了霍夫平方结果，为仿指和指数 Hawkes 过程的期望签名提供了有限维线性闭包，并提出了一种反对称的交叉面积，能够一阶检测双通道 Hawkes 过程的激发方向。 通过统一签名理论、粗糙路径、跳跃过程和期望签名，这项工作提供了一种共同的代数语言，连接随机分析与路径签名在机器学习中的应用。其成果使得 Hawkes 过程的参数能够被显式识别，并提供了检测方向性激发的新工具，对金融、神经科学和信号处理等领域产生影响。 几何性缺陷定理指出，二次协方差和坐标协方差是期望签名中 shuffle 乘法性失败的规范原因。对于有限变分的纯跳跃路径，前向 Ito 签名等于迭代求和签名；仿指和指数 Hawkes 过程在状态权重增广后接受有限维线性闭包，使得基线、激发和衰减参数可以从二阶期望签名中直接读取；此外，反对称的二阶交叉面积能够一阶检测双通道 Hawkes 过程的激发方向。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 在粗糙路径理论中，路径的签名是一系列迭代积分，能够唯一编码路径的形状，并作为机器学习的特征映射。几何性指的是提升后的路径位于自由 nilpotent 群的性质，其缺陷衡量由二次变化导致的 shuffle 乘法性偏差。Hawkes 过程是一种自激点过程，其中每个事件都会增加未来的强度，通常用指数或仿射核建模。期望签名对随机路径的签名进行平均，使得随机过程的统计推断和核方法成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rough_path">Rough path - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hawkes_process">Hawkes process - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2606.28869">A General Theory of Paths : Signatures , Jump Lifts, and Expected...</a></li>

</ul>
</details>

**标签**: `#signature theory`, `#rough paths`, `#stochastic processes`, `#Hawkes processes`, `#algebraic topology`

---

<a id="item-10"></a>
## [LLM 压缩金融文本可能扭曲投资决策](https://arxiv.org/abs/2606.29251) ⭐️ 8.0/10

该研究表明，基于 LLM 的金融文件和电话会议记录压缩可以产生流畅且事实合理的摘要，但这些摘要仍可能改变原始材料所支持的投资决策，指出去上下文化和模型依赖是两种关键失效模式，并提出了 Agentic Context Compression 来缓解这些问题。 这表明仅凭流畅性或事实性来评估 LLM 压缩在金融决策中的作用是不够的，对 AI 安全以及 LLM 在金融领域的可靠部署具有重要意义。 论文将信息忠诚度定义为保持源材料所引发的决策，在金融文本上展示了忠诚度的损失，并提出了 Agentic Context Compression，即生成多个候选压缩并根据原始来源审计它们之间的分歧。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 金融分析师常需阅读冗长的文件和电话会议记录，因此需要上下文压缩。大型语言模型可以对这些文本进行摘要，但压缩过程可能会丢失细微的限定词或警示，导致去上下文化。不同的 LLM 也可能对同一来源产生不同的摘要，造成模型依赖。因此，保留与决策相关的上下文对于避免改变投资判断至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.29251">[2606.29251] When Summaries Distort Decisions: Information ...</a></li>
<li><a href="https://letsdatascience.com/news/llm-compression-alters-financial-decision-fidelity-321b7306">LLM Compression Alters Financial Decision Fidelity</a></li>

</ul>
</details>

**标签**: `#LLM`, `#information fidelity`, `#financial analysis`, `#AI safety`, `#context compression`

---

<a id="item-11"></a>
## [CLQT：闭环、成本感知的 LLM 投资组合管理代理基准](https://arxiv.org/abs/2606.29771) ⭐️ 8.0/10

论文提出了 CLQT，一个闭环、成本感知、策略一致的基准，通过五阶段决策循环和可验证的哈希链决策轨迹来评估基于 LLM 的投资组合管理代理。 CLQT 将评估从以回报为中心的排行榜转向诊断性过程分析，揭示代理成功或失败的位置，从而促进更可靠的 LLM 交易代理开发。 CLQT 包含硬 TimeGate、机构交易与融资成本建模、三层记忆、Model‑Context‑Protocol 工具层和任务感知的综合，通过可审计的 DecisionRound 哈希链生成五轴能力评分卡（APM‑CS）。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 最近的工作将 LLM 代理的评估从静态金融问答转移到模拟实时投资组合管理的顺序交易仿真。大多数现有基准仅根据固定窗口内的累积收益对代理进行排名，这将技能与市场路径混淆，并且可能受到前视泄漏的影响。CLQT 通过强制在每个时间步内实施闭环环境——代理必须观察、决策、执行和反思——来克服这些局限，从而实现性能诊断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.29771">CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent ...</a></li>
<li><a href="https://letsdatascience.com/news/clqt-introduces-closed-loop-benchmark-for-llm-trading-agents-9f39d457">CLQT Introduces Closed-Loop Benchmark for LLM Trading Agents</a></li>
<li><a href="https://arxiv.deeppaper.ai/papers/2606.29771v1">CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#financial AI`, `#benchmarking`, `#trading simulation`, `#evaluation methodology`

---

<a id="item-12"></a>
## [置换不变微调使元数据检索对字段顺序鲁棒](https://arxiv.org/abs/2606.30473) ⭐️ 8.0/10

本文提出置换不变微调（PI-FT），通过在随机字段顺序并加入 dropout 的情况下微调文本编码器，使得字段顺序变化时的检索损失从 7.4 降至 0.2 nDCG@10。 字段顺序是一个任意的实现细节，但在 AI 助手需要跨语言可靠地检索公共统计数据时，它会严重降低检索质量。 PI-FT 仅需在数据加载器中改动约两行代码，在分内精度几乎无损，并使 118M 参数的 CPU 编码器在零样本基线上取得更高表现（0.707 对 0.556 nDCG@10），包括 text‑embedding‑3‑large。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 在结构化元数据检索中，每条记录通过将其字段拼接成字符串进行序列化，这迫使了一个特定的字段顺序；常规微调会使模型学习将意义与绝对位置而不是字段标签关联。因此，在使用不同字段顺序重建索引时，检索质量会显著下降，这通过 nDCG@10 来衡量，因为编码器已经对原始顺序产生了敏感性。此外，论文提出了 DevDataBench，一个完全由 LLM 生成的、覆盖 15 种语言的基于事实的面向查询的基准，用于发展统计目录，以便在缺乏真实用户日志时进行训练和评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.30473">Field Order Should Not Matter: Permutation- Invariant Embedding...</a></li>
<li><a href="https://pulseaugur.com/cluster/117083-new-pi-ft-method-improves-structured-metadata-retrieval-by-ignoring-field-order">New PI - FT method improves metadata retrieval by ignoring field order...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discounted_cumulative_gain">Discounted cumulative gain - Wikipedia</a></li>

</ul>
</details>

**标签**: `#information retrieval`, `#metadata embedding`, `#permutation invariance`, `#fine-tuning`, `#NLP`

---

<a id="item-13"></a>
## [通过 380 万亿 Tokens 的 LLM 使用识别 AI 溢价](https://arxiv.org/abs/2606.30583) ⭐️ 8.0/10

作者使用 OpenRouter 数据集中的 380 万亿 LLM token 构建了 AI 因子，发现 AI beta 较高的公司获得超额收益，量化出每周 64.1 个基点的 AI 溢价。 这提供了首个大规模经验证据，衡量 AI 采用如何转化为金融回报，为资产定价提供新因子，并揭示 AI 在各行业的经济影响。 该溢价主要由密集型、前沿导向的 AI 使用驱动——闭源模型、付费及资深用户以及长提示——在新兴市场如中国中不存在，而与非例行互动工作呈正相关、与分析性职业呈负相关。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 该研究基于 OpenRouter 平台上的 token 消费、美元支出和用户数量增长构建 AI 因子。OpenRouter 的数据集提供了对真实世界 AI 消费的细粒度、高频视图，如其 2025 年 State of AI 报告中所展示的 100 万亿 token。随后采用因子投资方法，通过股票收益与 AI 因子的共动来估算公司层面的 AI beta。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/data">Data - Authoritative AI Usage Data for Research | OpenRouter</a></li>
<li><a href="https://openrouter.ai/state-of-ai">State of AI 2025: 100T Token LLM Usage Study | OpenRouter</a></li>
<li><a href="https://arxiv.org/html/2601.10088v1">State of AI: An Empirical 100 Trillion Token Study with ...</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#factor investing`, `#token consumption`, `#stock returns`, `#machine learning impact`

---

<a id="item-14"></a>
## [深度神经网络通过投资组合切线核得到线性因子模型](https://arxiv.org/abs/2402.06635) ⭐️ 8.0/10

本文表明，深度神经网络训练的随机贴现因子可进行加性分解，得到由投资组合切线核（PTK）支配的线性因子表示。在美国股票数据上的实证检验表明，该表示在定价表现上具有显著提升，并将谱复杂度与岭正则化联系起来。 这项工作通过从黑箱深度神经网络中导出可解释的线性因子模型，连接了深度学习与资产定价，为研究者和从业者提供了理解和改进随机贴现因子估计的新工具。同时，它将模型复杂度与正则化联系起来，为金融机器学习中的更好泛化提供指导。 该分解将非线性特征发现与定价规则分离，投资组合切线核汇总了网络学习到的特征；在总体层面，隐含的随机贴现因子收敛于由谱复杂度决定强度的岭正则化真实随机贴现因子。实证表明，更高的谱复杂度会收紧有限样本的定价上限，而 PTK 表示带来了显著的经济和统计性提升。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 随机贴现因子（SDF）通过对市场状态下的收益进行加权来定价资产，其从数据中估计是资产定价的核心挑战。近年来，研究者利用深度神经网络直接从收益和特征中学习 SDF，常优于传统线性因子模型但缺乏可解释性。本文提出一种加性分解，将网络学习到的特征隔离出来，由新定义的投资组合切线核（PTK）支配的线性因子模型表示，并将网络的谱复杂度与岭型正则化联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2402.06635">[2402.06635] Large and Deep Factor Models - arXiv.org</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6225778">Large and Deep Factor Models by Bryan T. Kelly, Boris ... - SSRN</a></li>
<li><a href="https://arxiv.org/html/2402.06635">Large and Deep Factor Models</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#asset pricing`, `#stochastic discount factor`, `#factor models`, `#deep learning`

---

<a id="item-15"></a>
## [广告禁令结束智利药店亏损价格战并实现价格协同](https://arxiv.org/abs/2512.22917) ⭐️ 8.0/10

研究表明，智利对比价广告的禁令结束了亏损定价战，使得药店联合提高价格，通过改变价格敏感度和信念实现。 该研究揭示广告限制如何将市场从价格战转向默契协同，为工业组织理论和反垄断政策提供重要启示。 文章构建了基于需求的结构模型，包含店铺流量和竞争对手信念两部分机制，并采用模拟矩估计法（SMM）对参数进行估计，成功再现了价格战、失败尝试及禁令后的协同涨价；结果显示伤害主要是转移至垄断利润，死 weight 损失较小，因为事后需求缺乏弹性。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 损失领袖定价指的是以低于成本的价格销售产品，以吸引顾客随后购买更高利润的商品。比较价广告会突出哪家零售商提供最低价格，从而加剧价格竞争并促进损失领袖策略。模拟矩估计法（SMM）是一种结构估计技术，通过匹配模拟生成的矩与实证矩来估计参数，适用于无法直接解析的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Loss_leader">Loss leader - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Method_of_simulated_moments">Method of simulated moments - Wikipedia</a></li>

</ul>
</details>

**标签**: `#industrial organization`, `#advertising regulation`, `#pharmaceutical pricing`, `#structural estimation`, `#tacit collusion`

---

<a id="item-16"></a>
## [Lean 4 形式化数学金融库，包含伊托积分和风险中性度量](https://arxiv.org/abs/2606.01356) ⭐️ 8.0/10

作者发布了一个基于 Lean 4 的数学金融库，包含超过 200 个无 sorry 的定理，覆盖十一个子领域，构造了 L² 伊托积分作为有界线性等距，并从首原则导出了风险中性定价度量。 该工作提供了经过机器检查且 axiomatic 透明的量化金融基础，使得建模更可信，并为衍生品定价、风险管理和固定收益分析提供可重用的验证组件。 该库构建在 Mathlib 和 BrownianMotion 包之上，按定理与底层数学的忠实程度进行分类，并通过构建时强制的门户暴露每个证明实际依赖的确切 axiomatic 集合。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: Lean 4 是一种函数式编程语言和证明助手，支持交互式定理证明；其数学库 Mathlib 提供了大量已形式化的数学。伊托积分是随机微积分中的基本构造，用于对布朗运动进行积分，而风险中性度量是一种使得折算后资产价格成为鞅的概率度量，是衍生品定价的核心。在 Lean 4 中形式化这些概念可以让计算机检查证明的每一步，消除隐含假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.01356">A Formally Verified Library of Mathematical Finance in Lean 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Itô_calculus">Itô calculus - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Risk-neutral_measure">Risk-neutral measure - Wikipedia</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#Lean 4`, `#mathematical finance`, `#stochastic calculus`, `#theorem proving`

---

<a id="item-17"></a>
## [Lean 4 中的布朗运动伊托微积分机器检验](https://arxiv.org/abs/2606.15089) ⭐️ 8.0/10

该论文在 Lean 4 的 Mathlib 中正式化了布朗运动的伊托积分和伊托公式，通过可预测矩形 π-系统构建希尔伯特空间等距的积分，并从条件期望投影导出关键性质。 这项工作提供了任何证明助手中首次机器检验的伊托微积分构建，为随机分析提供了严格的基础，并展示了形式化方法如何推进连续时间概率论。 该构建证明了对有界导数的 C^3 函数的伊托公式，获得积分过程的几乎处处连续的修正，并将其扩展为 ℝ≥0 上的路径 wise 连续局部鞅，全部在 Lean 4 中得到验证。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: Ito 积分提供了相对于布朗运动进行积分的框架，其中伊托积分在 L^2 空间满足等距性质。可以通过简单自适应过程构建希尔伯特空间等距的伊托积分，且其在时间 t 的值等于其终端值在 t 之前的过滤算子下的条件期望。Lean 4 是一种函数式编程语言和证明助手，其 Mathlib 库包含形式化的数学，包括 BrownianMotion 包。在 Lean 4 中形式化这些概念可以得到机器检验的证明，从而保证随机积分和伊托公式的正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Itô_calculus">Itô calculus - Wikipedia</a></li>
<li><a href="https://reservoir.lean-lang.org/@RemyDegenne/BrownianMotion">Construction of a Brownian Motion in Lean | Reservoir</a></li>
<li><a href="https://arxiv.org/html/2606.01356">A Formally Verified Library of Mathematical Finance in Lean 4</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#stochastic calculus`, `#Lean 4`, `#Ito integral`, `#Brownian motion`

---

<a id="item-18"></a>
## [中国国内科学现在超越美国在专利中的贡献。](https://arxiv.org/abs/2606.26470) ⭐️ 8.0/10

该研究将中国发明专利与全球科学文献关联，发现中国本土科学在这些专利中的占比从 2000 年的 1%上升至 2025 年的 26%，并在 2021 年超过了美国的份额。 这一变化表明中国的技术自给自足能力在增强，削弱了美国出口管制假设——即中国创新依赖美国科学——的基础。 该分析涵盖了全部中国发明专利，测量国内外科学引用；中国本土科学份额稳步增长，而美国份额下降，交叉点出现在 2021 年。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 发明专利赋予新技术解决方案的专属权利，并且通常与支撑它们的科学知识相关联。研究者通过追踪专利引用中指向国内外文献的比例来衡量一个国家对外国科学的依赖程度。美国曾试图通过限制中国获取美国科学来减缓中国的技术崛起，基于中国创新严重依赖美国知识的假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.uspto.gov/patents/search">Search for patents | USPTO</a></li>
<li><a href="https://patents.google.com/">Google Patents</a></li>
<li><a href="https://link.springer.com/article/10.1007/s11192-025-05363-6">Global ties in science: a scientometric approach to ...</a></li>

</ul>
</details>

**标签**: `#innovation`, `#China`, `#technology policy`, `#patent analysis`, `#science dependence`

---

<a id="item-19"></a>
## [研究将企业房东集中度与少数族裔社区租金增长加快联系起来](https://arxiv.org/abs/2606.27525) ⭐️ 8.0/10

本文通过将 SEC EDGAR 10-K 房产申报地理编码到人口普查 tracts，测 tracts，测量企业房东集中度（CLC），发现将 REIT 集中度翻倍与 2019‑2023 年租金增长提高 2.8 个百分点相关，且在多数少数族裔 tracts 中影响更显著。 通过提供首个人口普查 tracts 级别的证据，表明算法房东集中度与有色人种社区租金增长不成比例地加快相关，该研究为正在进行的反垄断审查和住房可负担性政策提供了信息。 分析控制了由 ACS 租金负担和市场紧张度构建的新颖算法住房负担指数（AHBI），使用 Zillow 观察租金指数（ZORI）作为租金结果，并采用解释外样本方差 44%的 XGBoost 模型，SHAP 值显示 CLC 在少数族裔 tracts 中的影响为正，在白人 tracts 中的影响为负。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 企业房东集中度（CLC）指的是大型公开交易房地产投资信托（REITs）拥有的租赁单位份额，通过将 SEC EDGAR 10‑K 房产申报地理编码到人口普查 tracts 来测量。该研究建立在 2024 年美国司法部反垄断诉讼之上，该诉讼指控 RealPage 及几家主要 REITs 使用算法工具在数十万套住房单元之间协调租金。为了隔离 CLC 的影响，研究人员利用 ACS 数据构建了算法住房负担指数（AHBI），并采用 Zillow 观察租金指数（ZORI）来追踪 2019‑2023 年的租金增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sec.gov/search-filings">Search Filings - SEC.gov</a></li>
<li><a href="https://github.com/advayranade/algo-rent-pricing-research-ahbi">advayranade/algo-rent-pricing-research-ahbi - GitHub</a></li>
<li><a href="https://www.zillow.com/research/methodology-zori-repeat-rent-27092/">Methodology: Zillow Observed Rent Index ( ZORI ) - Zillow Research</a></li>

</ul>
</details>

**标签**: `#housing economics`, `#algorithmic fairness`, `#racial disparity`, `#urban policy`, `#antitrust`

---

<a id="item-20"></a>
## [无限维流形上可微映射的加权通用逼近](https://arxiv.org/abs/2606.09820) ⭐️ 8.0/10

该论文将功能输入神经网络的通用逼近定理扩展到无限维加权流形上的可微映射，通过证明加权 Nachbin 定理，也保证了对映射导数的逼近。这导致了对非预期函数泛函的逼近结果，并表明签名的线性函数能够逼近路径空间泛函及其方向导数。 通过将通用逼近定理扩展到无限维环境并包含导数逼近，这项工作为使用神经网络学习粗糙路径理论、随机分析和功能数据分析中出现的复杂泛函提供了理论基础。它将机器学习理论与高级函数分析联系起来，可能对未来处理路径依赖数据的算法产生影响。 该方法使用功能输入神经网络，将来自可能无限维加权流形的输入映射到实值隐藏层，应用标量非线性激活函数，然后通过线性泛函读出到 Banach 空间；加权 Nachbin 定理保证了此类网络在可微映射空间中的稠密性，包括非预期函数泛函的水平和垂直导数。签名的线性组合被证明能够逼近这些路径空间泛函。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 通用逼近定理表明前馈神经网络可以在紧集上逼近任何连续函数；功能输入神经网络（FNNs）将这一思想扩展到输入为函数或路径的情况，将其视为无限维空间的元素。Nachbin 定理给出了代数在拓扑空间上连续函数空间中稠密的条件，而加权版本则允许在非紧致、加权流形上进行逼近。路径签名提供了一种基于签名的特征映射用于数据流，其水平和垂直导数捕捉方向变化；逼近这些对象使得能够学习路径依赖泛函。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.09820">Weighted universal approximation of differentiable maps on ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nachbin's_theorem">Nachbin 's theorem - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2301.05869">[2301.05869] Functional Neural Networks: Shift invariant ... FuncNN: Functional Neural Networks Functional Neural Networks: Shift Invariant Models for ... GitHub - b-thi/FNN: FuncNN R Package Website Fitting Functional Neural Networks — fnn.fit • FNN Feedforward Neural Network - GeeksforGeeks Images</a></li>

</ul>
</details>

**标签**: `#universal approximation theorem`, `#neural networks`, `#infinite-dimensional manifolds`, `#functional analysis`, `#path signatures`

---

<a id="item-21"></a>
## [KineticSim 将市场模拟吞吐量提升至每秒 547 亿事件。](https://arxiv.org/abs/2606.21784) ⭐️ 8.0/10

KineticSim 提出了一种轻量级 GPU 执行引擎，通过在共享内存中使用原子操作的持续状态携带清除模式，加速迭代多智能体规约，峰值吞吐量超过每秒 547 亿智能体事件。 通过大幅降低每步临界路径深度并消除与步数相关的全局内存流量，KineticSim 使得实时、大规模的市场模拟成为可能，适用于监管压力测试、强化学习和高频交易等场景，且 GPU 内存消耗远低于现有框架。 该模式将每步临界路径深度从Θ(L+A)降低至Θ(log L + ⌈A/L⌉)，并使全局内存流量与步数无关；在固定工作负载下，KineticSim 相比 NumPy 提速 3406 倍，相比 PyTorch GPU 提速 27.8 倍，相比 JAX GPU 提速 42.8 倍，相比 naïve CUDA 基线提速 8.4 倍，且 GPU 内存消耗仅为 PyTorch 的约十分之一，在 53 种配置下产生逐位相同的订单簿。

rss · arXiv Quantitative Finance · Jun 30, 04:00

**背景**: 多智能体市场模拟用于建模众多交易智能体的交互，传统 CPU 模拟器按顺序处理智能体，导致瓶颈；而向量化 GPU 方法则受内核启动开销和重复全局内存访问的限制。持续状态携带清除模式在线程块共享内存中跨步骤缓存可变仿真状态，通过共享内存原子操作聚合智能体动作，并合作解决清除函数，从而降低临界路径深度并消除与步数相关的全局内存流量。共享内存原子操作提供了线程块内低延迟的更新，正如 CUDA 相关资料中所述的共享内存原子性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Bwv5J7dHYjU">From Scratch: Shared Memory Atomics and Dynamic... - YouTube</a></li>
<li><a href="https://stackoverflow.com/questions/51642503/which-is-faster-for-cuda-shared-mem-atomics-warp-locality-or-anti-locality">Which is faster for CUDA shared -mem atomics ... - Stack Overflow</a></li>
<li><a href="https://www.toolify.ai/gpts/unlock-the-power-of-cuda-shared-memory-atomics-and-dynamic-allocation-145200">Unlock the Power of CUDA: Shared Memory Atomics and Dynamic...</a></li>

</ul>
</details>

**标签**: `#parallel computing`, `#agent-based modeling`, `#market simulation`, `#high-performance computing`, `#financial technology`

---