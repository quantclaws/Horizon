---
layout: default
title: "Horizon Summary: 2026-06-26 (ZH)"
date: 2026-06-26
lang: zh
---

> From 35 items, 10 important content pieces were selected

---

1. [首次使用 AI 解卷和墨迹检测读取完整赫库兰尼姆卷轴](#item-1) ⭐️ 9.0/10
2. [苹果跳过 M6 芯片，推出 AI 优化的 M7 系列用于 Mac](#item-2) ⭐️ 8.0/10
3. [互联网的“请出示文件”时代将摧毁您的隐私](#item-3) ⭐️ 8.0/10
4. [Zig 引入端无关位转换语义及 LLVM 后端改进](#item-4) ⭐️ 8.0/10
5. [德国法院裁定谷歌对 AI 概览错误承担责任](#item-5) ⭐️ 8.0/10
6. [层次图学习优化期货日历价差](#item-6) ⭐️ 8.0/10
7. [多流时序融合用于金融欺诈检测](#item-7) ⭐️ 8.0/10
8. [限价单簿预测中的幂律缩放与 FastBiNLOB 架构](#item-8) ⭐️ 8.0/10
9. [点工平台推荐曝光与收藏列表实地实验](#item-9) ⭐️ 8.0/10
10. [未被采纳的令牌：采样、状态与 AI 代理的随机性](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [首次使用 AI 解卷和墨迹检测读取完整赫库兰尼姆卷轴](https://scrollprize.org/firstscroll) ⭐️ 9.0/10

研究人员首次使用基于 AI 的分割、虚拟解卷和墨迹检测技术，成功读取了一整卷赫库兰尼姆纸莎草卷，揭示了此前无法触及的古代文本。 这一突破展示了人工智能在考古遗产保护中的巨大潜力，使得其他被碳化的古卷也有望被解读，可能重新发现失传的古希腊和拉丁作品。 研究团队先利用 X 射线断层扫描获取卷轴的三维影像，再用 AI 算法将内部层分割并虚拟展平，最后应用在碳墨碎片上训练的机器学习模型检测墨迹，从而重建出可阅读的文字。

hackernews · verditelabs · Jun 25, 15:48 · [社区讨论](https://news.ycombinator.com/item?id=48675179)

**背景**: 赫库兰尼姆是公元 79 年维苏威火山爆发时被火山灰掩埋的古罗马城镇，其图书馆中的纸莎草卷在高温下碳化，外观呈黑色且极其脆弱，传统展开方式会导致毁坏。自 2000 年代起，研究者使用 X 射线相位对比断层扫描获取内部结构的三维数据，随后通过虚拟解卷算法将这些数据转换为可检查的平面图像。近期，深度学习模型被用于识别碳墨在扫描体素中的特征，使得在不接触卷轴的情况下恢复隐藏文字成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/inside-the-ai-competition-that-decoded-an-ancient-scroll-and-changed/">Inside the AI Competition That Decoded an Ancient Herculaneum Scroll | Scientific American</a></li>
<li><a href="https://www.nationalgeographic.com/history/article/herculaneum-scrolls-mount-vesuvius-ai">Inside the stunning recovery of the lost Herculaneum Scrolls | National Geographic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Virtual_unfolding">Virtual unfolding - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者惊叹于古代作者设想他们的作品能够流传千年的想法，指出赫库兰尼姆遗址仅有约 20%被发掘，因而仍有大量卷轴可能等待发现，并认为此项目是技术用于文化福祉而非广告的积极典范。此外，前项目负责人透露，另一卷轴 recientemente 解开了 140 列新文本。

**标签**: `#archaeology`, `#AI`, `#cultural heritage`, `#Vesuvius challenge`, `#text recovery`

---

<a id="item-2"></a>
## [苹果跳过 M6 芯片，推出 AI 优化的 M7 系列用于 Mac](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true) ⭐️ 8.0/10

苹果宣布将跳过高端 M6 Pro 和 Max 版本，而是加速推出以 AI 为重点的 M7 系列（Pro、Max、Ultra），旨在提升 Mac 本地大语言模型推理能力。 这一转变表明苹果致力于将 AI 工作负载直接集成到其芯片中，可能为 Mac 用户提供更强的本地 LLM 性能并减少对云端 API 的依赖。 基础 M7 版本目标内存带宽约为 240 GB/s，未来版本可能达到 1,200–1,500 GB/s 并提供最高 512 GB 统一内存，且可能采用英特尔 18A 制程。

hackernews · scrlk · Jun 25, 17:38 · [社区讨论](https://news.ycombinator.com/item?id=48676795)

**背景**: 苹果的 M 系列芯片将 CPU、GPU 和神经引擎集成在一起，并采用统一内存架构，使处理器和图形核心能够共享同一池高带宽内存，从而消除了离散 GPU 显存限制导致的大型模型推理瓶颈。自 2020 年 M1 发布以来，每一代都提升了内存带宽和 AI 加速能力，使开发者能够在 MacBook 和 Mac Studio 上本地运行大型语言模型。即将推出的 M7 系列旨在进一步提升内存带宽和 AI 计算能力，以支持更苛刻的本地 LLM 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macworld.com/article/3177046/report-apple-to-skip-m6-pro-max-chips-fast-track-m7-for-local-ai.html">Report: Apple to skip M6 Pro/Max chips, fast-track M7 for local AI</a></li>
<li><a href="https://www.sitepoint.com/local-llms-apple-silicon-mac-2026/">Local LLMs Apple Silicon Mac 2026 | M1 M2 M3 Guide</a></li>
<li><a href="https://www.cultofmac.com/news/apple-will-skip-m6-pro-and-max-chips">Apple will skip M6 Pro and Max chips, fast-track M7 — here's why</a></li>

</ul>
</details>

**社区讨论**: 几位评论者称赞苹果专注于 AI 优化芯片以支持本地 LLM 推理的战略契合，指出计划的 240 GB/s 带宽以及可能的更高带宽版本。其他人则担心如果 AI 需求放缓的应对方案，并讨论了采用英特尔 18A 制程节点生产早期 M7 所带来的风险。

**标签**: `#Apple`, `#M7 chip`, `#AI hardware`, `#Mac processors`, `#semiconductor roadmap`

---

<a id="item-3"></a>
## [互联网的“请出示文件”时代将摧毁您的隐私](https://expression.fire.org/p/the-papers-please-era-of-the-internet) ⭐️ 8.0/10

文章警告称，日益增加的在线身份检查（常以年龄验证的名义出现）正在侵蚀用户隐私，并探讨了诸如匿名凭证和零知识证明等技术缓解措施。 随着政府推动强制年龄验证和身份验证，缺乏隐私保护机制可能导致大规模监控和数据滥用，影响所有互联网用户。 匿名凭证允许用户在不透露身份的情况下证明属性（例如超过一定年龄），使用诸如微软的 U‑Prove 或 IBM 的 Idemix 等方案；零知识证明则能够在不泄露出生日期或其他个人数据的情况下进行年龄验证。

hackernews · bilsbie · Jun 25, 21:44 · [社区讨论](https://news.ycombinator.com/item?id=48679608)

**背景**: 许多国家的最新立法要求在线平台在允许访问特定内容前验证用户年龄，导致出现类似‘请出示文件’的身份检查。匿名凭证最早由 Chaum 提出，随后由 Brands 和 Camenisch‑Lysyanskaya 改进，能够在隐藏持有者身份的情况下证明某些声明。零知识证明则通过不泄露任何底层数据来验证声明的真实性，因而成为隐私保护的年龄验证的有吸引力的方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/computer-science/anonymous-credential">Anonymous Credential - an overview | ScienceDirect Topics</a></li>
<li><a href="https://www.newamerica.org/insights/exploring-privacy-preserving-age-verification/">Age Verification to Protect Youth Online: Using Zero Knowledge Proofs</a></li>
<li><a href="https://brave.com/blog/zkp-age-verification-limits/">The limits of zero-knowledge for age-verification - Brave</a></li>

</ul>
</details>

**社区讨论**: 评论者指出匿名凭证提供了一种技术性解决方案（j2kun），讨论了隐私损失的感知成本收益（tqi），表示打算退出数字世界（HoldOnAMinute），质疑儿童是否需要持续在线（mossTechnician），并预测英国将出现结合年龄门槛与国家身份护照的政策（AJRF）。

**标签**: `#privacy`, `#identity verification`, `#internet policy`, `#anonymous credentials`, `#age verification`

---

<a id="item-4"></a>
## [Zig 引入端无关位转换语义及 LLVM 后端改进](https://ziglang.org/devlog/2026/#2026-06-25) ⭐️ 8.0/10

Zig 将 @bitCast 操作更新为端无关语义，使其结果不再依赖目标的字节序，并对 LLVM 后端进行了改进以更好地支持这些语义。 它还改善了打包结构和任意宽度整数的操作，使 Zig 在低级编程中更具吸引力。 该语义在语言提案 #19755 中被正式化，并且已经在自托管的 x86_64 后端实现。

hackernews · kouosi · Jun 25, 14:19 · [社区讨论](https://news.ycombinator.com/item?id=48673825)

**背景**: LLVM 是 Zig 用于代码生成的编译器基础设施，对其后端的改进会影响位转换和打包结构如何被降级为机器指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ziglang.org/devlog/2026/?from_theconsensus=1">Devlog ⚡ Zig Programming Language - ziglang.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Endianness">Endianness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLVM">LLVM - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 许多用户强调该变化如何简化打包结构的操作，而少数用户则质疑任意宽度整数是否值得额外的复杂度，相比手动打包。

**标签**: `#Zig`, `#programming languages`, `#bitcast`, `#LLVM`, `#systems programming`

---

<a id="item-5"></a>
## [德国法院裁定谷歌对 AI 概览错误承担责任](https://simonwillison.net/2026/Jun/25/ai-and-liability/#atom-everything) ⭐️ 8.0/10

德国法院裁定谷歌对其 AI 生成的搜索概览中的错误信息承担责任，将 AI 输出视为谷歌自身的陈述。布鲁斯·施奈尔评论称，AI 代理应被视为其部署者的延伸。 此裁定可能成为先例，使科技公司直接对 AI 生成内容承担责任，影响企业部署生成式 AI 和风险管理的方式。它挑战了 AI 可以为企业错误提供免责的观念。 该裁决具体涉及谷歌的 AI Overviews 功能，该功能在搜索结果中提供摘要答案，并将谷歌对不准确信息的责任视为其自身陈述。施奈尔认为，让公司依赖 AI 错误来逃避责任会产生不良激励并阻碍雇佣人类专家。

rss · Simon Willison · Jun 25, 22:28

**背景**: AI Overviews 是谷歌在搜索结果顶部显示的生成式 AI 生成摘要，用于直接回答用户查询。关于 AI 生成内容的法律责任是一个新兴问题，法院开始考虑 AI 输出是否应归因于其部署者。此德国案例是首批将 AI 输出视为公司自身言论的裁决之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dublinpost.ie/policy/german-court-rules-on-google-ai-overviews-liability">German court rules on Google AI Overviews liability</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/">Nobody needs AI to search the Internet, court says in ruling against...</a></li>
<li><a href="https://www.techsterhub.com/news/google-expands-ai-generated-overviews-for-search-engine-results/">Google Expands AI - Generated Overviews For Search Engine Results</a></li>

</ul>
</details>

**标签**: `#AI liability`, `#legal policy`, `#AI ethics`, `#Google`, `#German ruling`

---

<a id="item-6"></a>
## [层次图学习优化期货日历价差](https://arxiv.org/abs/2606.25811) ⭐️ 8.0/10

该论文提出了一种层次图学习框架，以层次方式建模商品期货并将其应用于日历价差策略，在 CME 数据上展示了改进的预测和交易表现。 通过填补日历价差策略缺乏基于学习的方法以及忽视到期依赖关系的两个空白，该工作在机器学习金融领域具有重要意义，并可能激发新的量化交易方法。 该方法构建两层图（基础资产和单个合约），包含同层和跨层边，利用层次图神经网络学习表示，将预测转换为日历价差头寸，并在 CME 交易的商品期货上实证优于基准模型。

rss · arXiv Quantitative Finance · Jun 25, 04:00

**背景**: 商品期货通常按照基础资产和合约到期日进行组织，因而可以采用层次表示：基础资产位于上层，单个期货合约位于下层。日历价差策略涉及同时买入和卖出同一基础资产但到期日不同的期货合约，以利用期限结构的变化获利。层次图学习将图神经网络扩展到多尺度图上，使模型能够同时捕捉资产内部相关性和到期依赖关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Calendar_spread">Calendar spread - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2606.25811">[2606.25811] Hierarchical Graph Learning for Calendar Spread ...</a></li>
<li><a href="https://johnnylu305.github.io/data/Hierarchical_Graph_Learning_20250327.pdf">Hierarchical Graph Learning for Spectral Clustering</a></li>

</ul>
</details>

**标签**: `#hierarchical graph learning`, `#calendar spread`, `#commodity futures`, `#machine learning`, `#quantitative finance`

---

<a id="item-7"></a>
## [多流时序融合用于金融欺诈检测](https://arxiv.org/abs/2606.25007) ⭐️ 8.0/10

本文提出多流欺诈 Transformer（MSFT），分别用独立的 Transformer 编码器对交易、登录会话、风险信号等异构事件流进行编码，并通过可配置机制融合它们的表示。在包含 1000 万用户、欺诈率 1.5%的大规模数据集上，MSFT 达到 0.99 AUROC，显著优于在聚合特征上的梯度提升树（0.74 AUROC）。 该研究表明，基于多流序列建模的方法能够超越传统的树模型，为数字银行业提供更精准且可部署的欺诈检测方案。消融研究进一步指出了最有效的融合策略和位置编码方式，为从业者架构选择提供指导。 作者比较了五种融合策略——拼接、门控融合、时间感知位置编码、跨流注意力及其全组合——发现时间感知位置编码的 AUROC 最高（0.9961），而门控融合的精度最好（0.989）。消融表明，参数匹配的单流 Transformer 仅达 0.82 AUROC，证实了多流编码的必要性；风险事件流提供最强的单独信号。在专有生产数据上的验证表明，相较于 XGBoost 基线，MSFT 实现了超过 22%的相对 AUROC 提升。

rss · arXiv Quantitative Finance · Jun 25, 04:00

**背景**: 金融欺诈检测通常需要分析多种异构事件流——如交易、登录会话和风险信号——这些流单独看似正常，但共同揭示欺诈模式。传统方法将这些流聚合为手工特征，然后使用梯度提升树，这可能忽略细微的时间依赖性。Transformer 模型擅长捕捉长程序列，而多流架构允许每种模态独立编码后再融合，既保留模态特定信息，又实现跨流交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.25007">Multi - Stream Temporal Fusion for Financial Fraud Detection</a></li>
<li><a href="https://arxiv.org/pdf/2206.06488">Multimodal Learning with Transformers</a></li>
<li><a href="https://arxiv.org/html/2509.14640">DyWPE: Signal- Aware Dynamic Wavelet Positional Encoding for ...</a></li>

</ul>
</details>

**标签**: `#financial fraud detection`, `#transformer`, `#multi-stream learning`, `#time series`, `#machine learning`

---

<a id="item-8"></a>
## [限价单簿预测中的幂律缩放与 FastBiNLOB 架构](https://arxiv.org/abs/2606.25986) ⭐️ 8.0/10

论文表明，限价单簿预测的预测损失与计算量之间遵循幂律关系，R^2=0.941。它提出了 FastBiNLOB，一种低延迟的密集轴可分离 LOB 混合器，在更低延迟下实现了比之前 SOTA 更高的宏 F1 分数。 这项工作将机器学习缩放理论与高频交易联系起来，为 LOB 预测中的计算与延迟权衡提供了原则性方法。它对高效交易系统的设计以及更广泛的 ML 系统社区（关注推理‑计算前沿）都有影响。 实验使用 FI‑2010 数据集，评估了从决策树到 MLPLOB 及其他神经 LOB 架构的各种模型；对低、中计算非 MLPLOB 点的幂律拟合外推到高计算 MLPLOB 前沿，得到 R^2=0.941。FastBiNLOB 采用密集轴可分离的时间和特征混合，在显著更低的延迟下超过了已发布的 y10 和 y100 宏 F1 目标。

rss · arXiv Quantitative Finance · Jun 25, 04:00

**背景**: 限价单簿（LOB）预测旨在从买卖订单序列预测短期价格走势，这对高频交易至关重要。机器学习中的缩放律描述了模型性能如何随计算或数据量的增加而可预测地提升，通常遵循幂律。MLPLOB 是一种用于 LOB 预测的简单多层感知器基线，常被用作基准中的参考架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.25986">The Inference-Compute Frontier and a Latency-Efficient Architecture ...</a></li>
<li><a href="https://openreview.net/forum?id=CYT5zrOfK5">LOBBen-TM: A Benchmark Study of Limit Order Book Prediction ...</a></li>
<li><a href="https://www.researchgate.net/publication/389315687_TLOB_A_Novel_Transformer_Model_with_Dual_Attention_for_Stock_Price_Trend_Prediction_with_Limit_Order_Book_Data">(PDF) TLOB: A Novel Transformer Model with Dual Attention for Stock...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#limit order book`, `#scaling laws`, `#financial trading`, `#neural architecture`

---

<a id="item-9"></a>
## [点工平台推荐曝光与收藏列表实地实验](https://arxiv.org/abs/2606.17397) ⭐️ 8.0/10

该研究提出阈值资格控制（TEC）推荐器，根据发布活动和未填容量重新分配模板曝光，使模拟中的求职成功率从 57.6%提升至 70.0%，并在真实的县级随机实地实验中得到验证。 该方法解决了稀缺短暂机会市场中的推荐偏见问题，提升了双边劳动平台的匹配效率，并提供了可大规模并行的曝光控制方案。 TEC 完全可并行，适用于大规模数字平台；县级随机场试显示活跃模板的曝光增加、低曝光模板比例下降，以及印象级收藏和后续匹配的改善。

rss · arXiv Quantitative Finance · Jun 25, 04:00

**背景**: 点工平台是一种将临时工人与短期工作岗位匹配的在线市场，工人会收藏职位模板并在企业发布对应班次时收到通知。传统推荐系统倾向于将曝光集中在热门模板上，导致需求未得到满足的岗位被忽视。在双边市场中，平台需要同时考虑工人和企业两方的匹配效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.17397">Designing Recommendation Exposure and Favorite Lists : A Field...</a></li>
<li><a href="https://www.mdc.e.u-tokyo.ac.jp/news/9401/">[UTMD-136] Designing Recommendation Exposure and Favorite Lists...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Two-sided_market">Two - sided market - Wikipedia</a></li>

</ul>
</details>

**标签**: `#recommender systems`, `#field experiment`, `#two-sided markets`, `#labor platforms`, `#exposure control`

---

<a id="item-10"></a>
## [未被采纳的令牌：采样、状态与 AI 代理的随机性](https://arxiv.org/abs/2606.08998) ⭐️ 8.0/10

arXiv 预印本 2606.08998v2 分析了令牌采样和外在因素如何导致 AI 代理行为的可变性，提出了一种框架来区分内在和外在的随机性来源并减轻其影响。 了解这些随机性来源对于提高部署 AI 代理的可靠性、可重复性和安全性至关重要，有助于指导更好的系统设计和评估实践。 论文指出内在变异来源于令牌生成——模型的概率分布通过伪随机数生成器进行采样——并展示单个令牌的变化如何改变工具调用、代码编辑或代理状态；外在来源包括环境变化、实时数据、服务基础设施、批次效应和数值精度。

rss · arXiv Quantitative Finance · Jun 25, 04:00

**背景**: 代理 AI 系统通常以一个基础模型为核心，嵌入一个负责规划、调用工具、观察结果并更新状态的编排循环中。令牌采样引入内在随机性，因为模型将对数转换为概率，并使用伪随机数生成器选择下一个令牌，微小的变化可能被放大导致行为分歧。外在因素如环境变化、实时数据流、服务基础设施差异、批次效应和数值细节也会导致不同运行之间的可变性。通过区分这些层次，论文阐明了在何种条件下观察到的随机性可以被复现，以及确定性执行在实际部署中仍可能产生不同结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://charanhu.medium.com/how-large-language-models-like-gpt-generate-text-a-deep-dive-into-stochastic-decoding-3d7219dfe0a3">How Large Language Models Like GPT Generate Text... | Medium</a></li>
<li><a href="https://github.com/crewAIInc/crewAI">GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing...</a></li>
<li><a href="https://www.engineering.fyi/article/stanford-s-marin-foundation-model-the-first-fully-open-model-developed-using-jax">Stanford’s Marin foundation model : The first fully... | Engineering.fyi</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#token sampling`, `#stochasticity`, `#foundation models`, `#reproducibility`

---