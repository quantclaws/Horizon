---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> From 45 items, 11 important content pieces were selected

---

1. [F-Droid 2.0 发布：全新 UI 与移除特权扩展](#item-1) ⭐️ 8.0/10
2. [Whiteboard：面向人机协作的开源软件设计 IDE](#item-2) ⭐️ 8.0/10
3. [谷歌宣布 Suncatcher 项目将在太空部署机器学习基础设施。](#item-3) ⭐️ 8.0/10
4. [苹果在英国撤回高级数据保护，导致双层加密](#item-4) ⭐️ 8.0/10
5. [加州瞄准富裕居民，应对财富和人才外流](#item-5) ⭐️ 8.0/10
6. [实验研究表明基于规则的定价算法设计提高市场价格](#item-6) ⭐️ 8.0/10
7. [主权草根货币：一种用于信贷和货币政策的 CBDC 架构](#item-7) ⭐️ 8.0/10
8. [冻结统计裁判提升 LLM 驱动的投资因子发现](#item-8) ⭐️ 8.0/10
9. [局部弱极限证明网络均衡风险收敛。](#item-9) ⭐️ 8.0/10
10. [中心化交易所下的权益证明经济——均场模型](#item-10) ⭐️ 8.0/10
11. [漏积分器重构：抑制递归差分时间序列预测中的误差累积](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [F-Droid 2.0 发布：全新 UI 与移除特权扩展](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

F-Droid 发布 2.0 版本，进行了重大改版，包括重新设计的用户界面以及逐步淘汰之前需要 root 权限才能实现自动安装的特权扩展。 此次更新通过用 Android 标准会话安装器取代特权扩展，提升了易用性和安全性，使非 root 设备也能更方便地使用 F-Droid，并符合主流 Android 实践。 F-Droid 2.0 不再支持 Android 6，采用符合 Material Design 指南的新界面，并使用 Android 6.0 引入的会话安装器实现后台更新，无需用户点击。

hackernews · daveoc64 · Sep 24, 15:26 · [社区讨论](https://news.ycombinator.com/item?id=49831968)

**背景**: F-Droid 是一个面向 Android 的开源应用商店，专注于分发自由和开源软件。特权扩展曾让 F-Droid 能够在不启用‘未知来源’或用户确认的情况下自行安装、更新和删除应用，但需要 root 权限或特殊配置。F-Droid 2.0 用 Android 标准的会话安装器取代了该扩展，使其在非 root 设备上也能工作，并与 Google Play 的更新方式保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://f-droid.org/packages/org.fdroid.fdroid.privileged/">F - Droid Privileged Extension | F - Droid - Free and Open Source...</a></li>
<li><a href="https://daily.dev/posts/f-droid-2-0-what-changed-in-the-biggest-overhaul-in-a-decade-jega3om7h">F-Droid 2.0: what changed in the biggest overhaul in a decade</a></li>
<li><a href="https://github.com/f-droid/privileged-extension">F-Droid Privileged Extension - GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎 UI 重新设计和特权扩展的移除，认为相比以前笨拙的界面有所改善。然而，也有用户批评新设计缺乏视觉分离、点击元素不明显以及文字对齐不佳。部分人提到他们使用 Droid-ify 或 NeoStore 等替代品，并担心未来谷歌可能施加的限制。

**标签**: `#F-Droid`, `#Android`, `#open source`, `#app store`, `#UI redesign`

---

<a id="item-2"></a>
## [Whiteboard：面向人机协作的开源软件设计 IDE](https://github.com/devdotfast/whiteboard) ⭐️ 8.0/10

Whiteboard 是一款由 YC W26 支持的开源桌面应用，通过 agent SDK 让人类和 AI 代理在共享画布上协同设计软件架构。 它解决了 AI 代理编码导致的认知债务，提供了一个具体的工作空间用于架构审查和迭代设计。 Whiteboard 基于 CodeOSS 构建，提供可点击跳转到源代码的图表、基于 Rust 的语义 AST 感知差异查看器（支持 WASM 插件）以及将代理轨迹与设计决策关联的决策日志。

hackernews · sidharthkmenon · Sep 24, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=49833867)

**背景**: CodeOSS 是 Visual Studio Code 的开源核心，提供了熟悉的编辑器基础，具备 LSP 和快捷键。Whiteboard 利用这一基础为代理提供 SDK，在应用内画布上绘图，使其能够以可视化方式表达设计意图。通过与 Claude Code 等工具集成并提供语义差异查看器，它在高层架构讨论与底层代码变更之间架起了桥梁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Visual_Studio_Code">Visual Studio Code - Wikipedia</a></li>
<li><a href="https://www.morphllm.com/ai-agent-framework">AI Agent Frameworks (2026 Update): 8 SDKs Compared + the Claude Agent SDK Primitive Reference</a></li>
<li><a href="https://code.claude.com/docs/en/vs-code">Use Claude Code in VS Code - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这一概念是人机协作的有前景方向，同时指出 macOS 提示应更显著且质疑缺少文件编辑功能。有人担心图表准确性和大语言模型幻觉，但许多人强调语义差异查看器在审查代码变更方面的实用价值。

**标签**: `#software-design`, `#AI-agent`, `#open-source`, `#IDE`, `#collaborative-development`

---

<a id="item-3"></a>
## [谷歌宣布 Suncatcher 项目将在太空部署机器学习基础设施。](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) ⭐️ 8.0/10

谷歌揭晓 Suncatcher 项目，这是一项研究计划，旨在将包括张量处理单元在内的机器学习硬件部署在太阳能卫星上，以进行轨道人工智能处理，并宣布轨道数据中心测试发射定于 2026 年 10 月 1 日。 基于太空的机器学习可以利用持续的太阳能和真空的低温环境进行高效的人工智能计算，从而可能降低地面数据中心的能源足迹。然而，克服散热、辐射硬化以及高昂的发射成本仍然困难重重，这引发了对其可行性以及潜在军事用途的讨论。 Suncatcher 计划使用谷歌的 TPU 人工智能芯片，安装在配备太阳能阵列的卫星上，需要采用辐射硬化封装和主动热控系统来管理真空中的热量。首次轨道测试将搭载四个 TPU，每次运行仅 15 分钟；与此同时，像 Starcloud 这样的初创公司已经发射了概念验证单元，以验证类似硬件和经济性。

hackernews · xnx · Sep 24, 13:53 · [社区讨论](https://news.ycombinator.com/item?id=49830606)

**背景**: 如今的机器学习基础设施依赖于耗电大的 GPU 和 TPU，这些芯片安装在耗能显著且产生热量的地面数据中心内。将类似硬件放置在轨道上可以获得近乎持续的太阳能以及有利于散热的冷环境，但同时带来了真空中的热管理、辐射导致的位翻转以及对高带宽上下行链路的需求等挑战。谷歌的研究正在探索太阳能供电的卫星网络、基于 TPU 的人工智能节点以及辐射硬化芯片等技术，以克服这些障碍，从而实现可扩展的空间人工智能架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/">Learn about Google’s Project Suncatcher to put ML ...</a></li>
<li><a href="https://arstechnica.com/google/2026/09/googles-first-suncatcher-orbital-data-center-test-launches-october-1/">Google's first Suncatcher orbital data center test launches ...</a></li>
<li><a href="https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/">Exploring a space-based, scalable AI infrastructure system design</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为，空间数据中心在物理和经济方面不如地面设施有优势，指出散热更差以及发射成本更高。一些评论者提到与 Starcloud 等现有项目的类似之处，指出该初创公司已经飞行了概念验证单元，并指摘 Alphabet 在 SpaceX 中的大额持股可能成为推动力。还有人质疑散热解决方案、潜在的双重用途军事应用，并将其与如 Glomar Explorer 这样的秘密项目进行类比，既表达兴趣也保持谨慎。

**标签**: `#space computing`, `#machine learning`, `#data centers`, `#AI infrastructure`, `#Google`

---

<a id="item-4"></a>
## [苹果在英国撤回高级数据保护，导致双层加密](https://macanorak.com/two-tier-encryption-in-the-uk/) ⭐️ 8.0/10

苹果因英国法律压力撤回了面向英国用户的高级数据保护（ADP）功能，导致部分 iCloud 数据从端到端加密恢复为标准数据保护，而其他数据仍保持端到端加密。 这一举措在英国形成双层加密体系，引发对用户隐私的担忧，为政府访问云数据设定先例，并影响全球关于企业抵御监管法律的讨论。 ADP 原本将端到端加密的 iCloud 类别从默认的 14 项扩展到 23 项；未启用 ADP 时，额外的九类（如备份、照片、笔记、iCloud 云盘等）恢复为标准数据保护，苹果持有解密密钥，而原始的 14 类（如钥匙串、健康等）仍保持端到端加密。

hackernews · ReturnoftheHack · Sep 24, 10:39 · [社区讨论](https://news.ycombinator.com/item?id=49828731)

**背景**: 高级数据保护是 iCloud 的一项可选功能，它将加密密钥仅存储在用户的受信任设备上，从而为备份、照片、笔记等数据提供端到端加密。未启用高级数据保护时，iCloud 使用标准数据保护模式，苹果保留加密密钥，可在合法请求下访问用户数据。英国的《调查权力法案》等法律允许当局强制公司交出数据，这正是导致苹果为英国用户撤回高级数据保护的法律压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/legal/privacy/data/en/advanced-data-protection/">Legal - Advanced Data Protection Analytics & Privacy- Apple</a></li>
<li><a href="https://www.idownloadblog.com/2025/02/26/how-to-turn-on-advanced-data-protection-for-icloud/">Why and how to enable Advanced Data Protection for iCloud</a></li>
<li><a href="https://www.macworld.com/article/1439693/how-to-enable-manage-advanced-data-protection-icloud-data.html">How to enable and manage Apple 's Advanced Data Protection for...</a></li>

</ul>
</details>

**社区讨论**: 评论者对苹果屈服于法律压力表示失望，将其与之前对抗 FBI 的立场形成对比，并警告一次让步可能导致进一步的要求。有人指出，虽然基础的 14 类仍保持端到端加密，但失去 ADP 扩大了政府可访问的数据范围。少数评论者建议苹果退出英国市场或停止向政府销售产品，以作更强烈的回应。

**标签**: `#encryption`, `#privacy`, `#Apple`, `#UK law`, `#data protection`

---

<a id="item-5"></a>
## [加州瞄准富裕居民，应对财富和人才外流](https://blog.landeconomics.org/p/california-is-chasing-wealth-that) ⭐️ 8.0/10

加州政策制定者正在考虑或实施对高净值个人的财富税，引发人们担忧富裕居民可能搬迁到税负较低的州，带走他们的资产和人才。 这场辩论凸显税收政策如何影响富裕人群和技术工人选择居住地，进而影响州税收收入、经济增长以及科技等行业的竞争力。 提案包括对超过一定门槛的净资产征收财富税，以及仅对未改良土地价值征收土地价值税，旨在捕获难以流动的财富，同时减少通过搬迁轻易逃税的可能。

hackernews · idbnstra · Sep 24, 20:34 · [社区讨论](https://news.ycombinator.com/item?id=49836419)

**背景**: 财富税是对个人净资产超过一定门槛的征税；土地价值税仅对土地本身的价值征税，不包括建筑物和其他改良。经济学家认为土地价值税效率高且难以逃避，因为土地不能移动。在加州，高收入者和科技人才倾向于迁移到税负较低的州，这引发了对这些税收措施有效性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wealth_tax">Wealth tax - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Land_value_tax">Land value tax - Wikipedia</a></li>
<li><a href="https://cepr.org/voxeu/columns/global-talent-mobility-and-human-capital-agglomeration">Global talent mobility and human capital agglomeration - CEPR</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论土地价值税的优点，指出它不能通过离开来规避，并质疑是否能转嫁给租户。其他人警告说财富税无效，因为超级富豪可以简单搬迁或通过诉讼抗争，还有人指出在实际操作中评估土地与改良价值存在问题。

**标签**: `#wealth tax`, `#land value tax`, `#California policy`, `#talent migration`, `#economics`

---

<a id="item-6"></a>
## [实验研究表明基于规则的定价算法设计提高市场价格](https://arxiv.org/abs/2609.26861) ⭐️ 8.0/10

在一个受控市场实验中，参与者使用仪表盘构建定价算法，在多个时期内进行顺序伯 trand 博弈竞争，实验变动包括价格战争警告、预配置策略以及来自大型语言模型的建议。大多数处理导致市场价格上升，原因是起始价格提高以及算法设计更具合作性。 研究结果揭示了广泛使用的基于规则的定价工具的设计特征如何影响市场结果，为竞争政策和平台监管者提供了直接指导，以遏制算法定价的反竞争效应。这凸显了在反垄断分析中需要考虑算法设计而不仅仅是结果的必要性。 实验采用顺序伯 trand 博弈，参与者通过基于规则的算法设定价格；处理包括警告、预配置策略以及来自大型语言模型的建议。市场价格上升主要源于更高的初始价格设定以及算法策略向更合作方向的转变。

rss · arXiv Quantitative Finance · Sep 24, 04:00

**背景**: 基于规则的定价工具在数字商务中很常见，使卖家能够使用简单的如果‑那么规则自动调整价格。顺序伯 trand 博弈模拟了企业按顺序选择价格的价格竞争，可能导致与同时定价不同的结果。大型语言模型可以生成战略建议，影响参与者如何设计他们的定价规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bertrand_competition">Bertrand competition - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2609.26861">Rule - Based Pricing Algorithms and Market Outcomes: An...</a></li>
<li><a href="https://sloanreview.mit.edu/article/how-to-use-generative-ai-for-pricing/">How to Use Generative AI for Pricing | MIT Sloan Management Review</a></li>

</ul>
</details>

**标签**: `#algorithmic pricing`, `#market experiments`, `#competition policy`, `#LLM advice`, `#Bertrand competition`

---

<a id="item-7"></a>
## [主权草根货币：一种用于信贷和货币政策的 CBDC 架构](https://arxiv.org/abs/2609.27727) ⭐️ 8.0/10

该论文提出了一种基于草根货币和债券的 CBDC 架构，能够实现信贷创造、降低存款外逃风险，并直接融入货币政策操作。 通过解决现有 CBDC 设计的两个关键限制——存款外逃和被排除在信贷创造之外——该方法可能塑造未来的中央银行数字货币框架和货币政策工具。 该架构包括主权草根币（直接 CBDC）、非主权草根币（由任何实体发行的信贷）以及草根债券（主权和非主权）以提供利息；中央银行可以在这些工具上放款、吸收流动性、设定利率并交易证券，而无需将银行存款转换为新发行的中央银行货币。

rss · arXiv Quantitative Finance · Sep 24, 04:00

**背景**: 中央银行数字货币（CBDC）是中央银行发行的法定货币数字形式，由公众持有。现有的 CBDC 设计可能加剧存款外逃，因为用户会将银行存款转移到 CBDC，并且这些设计通常不参与信贷创造，限制了其在货币政策中的应用。草根货币是由受信任的社区成员发行的可按面值兑换的数字代币，能够在无外部资本的情况下实现地方信贷创造。草根债券在此基础上增加了到期和利息，使这些工具能够像标准银行工具一样运作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2202.05619v17">Grassroots Currencies: Foundations for Grassroots Digital ...</a></li>
<li><a href="https://arxiv.org/html/2609.27727v1">Sovereign Grassroots Currencies: A CBDC Architecture for ...</a></li>
<li><a href="https://arxiv.org/html/2603.13671v3">Grassroots Bonds as a Foundation for Market Liquidity - arXiv</a></li>

</ul>
</details>

**标签**: `#CBDC`, `#digital currency`, `#monetary policy`, `#grassroots currency`, `#central banking`

---

<a id="item-8"></a>
## [冻结统计裁判提升 LLM 驱动的投资因子发现](https://arxiv.org/abs/2609.27051) ⭐️ 8.0/10

本文提出了一种使用随时有效博彩策略的冻结统计裁判，用于验证 LLM 代理提出的投资因子，结果显示其误判远少于漏洞裁判。 通过提供强伪发现控制，该方法能够减轻自动化量化研究中的过拟合，并有望提高 LLM 生成因子模型的可靠性。 该裁判仅根据提交后揭示的市场结果通过博彩进行评分，从而在任意停止时间保证伪发现控制；在脚本提出者下，其承认的低阈值因子比漏洞裁判少 5‑11 倍，而 LLM 提出者与带宽匹配且能自行编写诊断探针。

rss · arXiv Quantitative Finance · Sep 24, 04:00

**背景**: 随时有效博彩策略是一种序列检验方法，能够在任意停止时间保持类型 I 错误控制，从而允许在未预先指定样本量的情况下连续监测假设。伪发现率（FDR）控制（例如 Benjamini‑Hochberg 过程）限制了多重假设检验中被宣布发现的假阳性的期望比例。在量化金融中，语言模型代理能够自主提出、回测并选择投资因子，但若缺乏严格的统计保障，容易过拟合。本文通过将一个冻结的、随时有效的裁判置于代理影响之外，来判断因子提案，从而结合了上述思想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.06521v1">Time-sensitive anytime-valid testing</a></li>
<li><a href="https://en.wikipedia.org/wiki/False_discovery_rate">False discovery rate - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2609.27051">Propose, Don’t Judge: An Anytime-Valid Referee for LLM Agents That...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#quantitative finance`, `#anytime-valid inference`, `#factor mining`, `#false discovery control`

---

<a id="item-9"></a>
## [局部弱极限证明网络均衡风险收敛。](https://arxiv.org/abs/2609.27107) ⭐️ 8.0/10

作者证明了在大型稀疏经济网络中，均衡分布和风险度量的局部弱极限定理，在均匀收缩响应以及下上根迭代 coalesce 的有界单调非膨胀响应两种情况下实现经验均衡分布的概率收敛，并通过生产和支付清算系统的数值实验进行说明。 这为分析大型经济网络中的系统性风险提供了严格的理论基础，使得均衡结果和法律不变风险度量（如 CVaR）的可扩展近似成为可能，这对监管机构和金融机构至关重要。 证明依赖于标记的局部弱收敛，在均匀收缩响应以及下上根迭代 coalesce 的有界单调非膨胀响应两种情况下实现经验均衡分布的概率收敛；在有界域和连续性假设下，该结果推广到法律不变风险度量，并给出递归深度的误差界。

rss · arXiv Quantitative Finance · Sep 24, 04:00

**背景**: 局部弱收敛是随机有根图序列的一种收敛概念，即随着图的大小增长，随机选取节点的邻域分布趋于稳定。在稀疏经济网络中，这使得全局均衡分布可以通过局部计算在一个限制的有根网络上近似。均衡指的是代理人的决策（如生产、支付）在双边暴露和冲击下相互一致的状态，而风险度量（如条件价值-at-risk）评估尾部风险，并且在仅依赖结果分布时是法律不变的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convergence_of_measures">Convergence of measures - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2609.27107">Local Weak Limits for Equilibrium and Risk in Economic Networks</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6759138">Local Approximation of Systemic Risk in Large Sparse Economic ...</a></li>

</ul>
</details>

**标签**: `#economic networks`, `#local weak convergence`, `#equilibrium analysis`, `#risk measures`, `#systemic risk`

---

<a id="item-10"></a>
## [中心化交易所下的权益证明经济——均场模型](https://arxiv.org/abs/2606.09003) ⭐️ 8.0/10

本文提出一种连续时间的均场模型，其中参与者既是权益证明验证者也是中心化交易所的交易者，结果表明交易所交易能够提升质押参与度并促进代币持有的去中心化。 通过挑战中心化交易所削弱区块链去中心化的常见观点，该工作为设计能够实际增强网络安全的代币经济学和交易所整合提供了新视角。 该模型在温和假设下建立了局部良好定义性，推导出半显式均衡交易策略，并考察了交易成本和代币供给机制对均衡质押比例和集中度分布的影响。

rss · arXiv Quantitative Finance · Sep 24, 04:00

**背景**: 权益证明（PoS）是一种共识机制，验证者通过锁定代币来保护区块链并按其质押比例获得奖励。中心化交易所（CEX）主导着加密货币交易量，并能通过订单流和流动性提供影响代币价格。均场博弈用于建模大量相互作用的代理人，能够分析个体交易策略如何汇总影响系统层面的结果，如质押分布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.09003v2">Proof of Stake economy under centralized exchanges - arXiv</a></li>
<li><a href="https://www.investopedia.com/terms/p/proof-stake-pos.asp">Understanding Proof-of-Stake: How PoS Transforms Cryptocurrency</a></li>
<li><a href="https://ideas.repec.org/a/spr/digfin/v6y2024i3d10.1007_s42521-024-00113-4.html">A mean field game model of staking system - IDEAS/RePEc</a></li>

</ul>
</details>

**标签**: `#Proof of Stake`, `#Centralized Exchanges`, `#Mean Field Game`, `#Blockchain Economics`, `#Cryptocurrency`

---

<a id="item-11"></a>
## [漏积分器重构：抑制递归差分时间序列预测中的误差累积](https://arxiv.org/abs/2609.23378) ⭐️ 8.0/10

论文提出了漏积分器重构，这是一种免训练的方法，用一阶 IIR 滤波器 H(z)=1/(1−γz⁻¹)（γ<1）替换递归差分预测中的纯累积和，以将积分器的极点移入单位圆内。仅需固定 γ=0.9 并进行两行代码的后处理修改，即可在不重新训练的情况下提升滚动预测的稳定性。 递归差分预测中的误差累积会导致长期预测发散，限制其实际应用；漏积分器修正能够限制这种误差并在不同架构和数据集上带来持续的改进。由于该方法无需重新训练且可直接作用于任何现有的一步或基础模型预测器，它为实际时间序列预测提供了简便且有效的提升手段。 实验表明，在 γ=0.9 时，归一化 MAE 从不稳定的 1.6‑3.8 降至 0.87‑0.97，且相对改善随预测 horizon 增长，从约 3%（H=24）提升至 51%（H=336），在使用最优极点时甚至可达 78%。这些改善在七种不同的神经网络架构和二十个多样化数据集上均得到验证，表明该方法具有良好的鲁棒性。

rss · arXiv Quantitative Finance · Sep 24, 04:00

**背景**: 递归差分预测通过先模型预测一步变化，然后对这些变化进行累积求和来重构完整序列，这一过程等价于一个在单位圆上具有极点的离散积分器。由于学习到的增量模型存在偏差，其误差在累积过程中会无界增长，导致长时滚动预测发散。漏积分器用一阶低通滤波器 H(z)=1/(1−γz⁻¹)（γ<1）替换纯积分器，将极点移入单位圆内，从而对误差进行衰减，抑制累积。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.23378v2">[2609.23378v2] Leaky-integrator reconstruction: taming error accumulation in recursive differenced time-series forecasting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leaky_integrator">Leaky integrator - Wikipedia</a></li>

</ul>
</details>

**标签**: `#time-series forecasting`, `#recursive differencing`, `#leaky integrator`, `#error accumulation`, `#machine learning`

---