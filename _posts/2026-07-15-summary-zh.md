---
layout: default
title: "Horizon Summary: 2026-07-15 (ZH)"
date: 2026-07-15
lang: zh
---

> From 69 items, 18 important content pieces were selected

---

1. [Bonsai 27B：首款可在手机上运行的 27B 参数模型](#item-1) ⭐️ 9.0/10
2. [The Tower Keeps Rising](#item-2) ⭐️ 8.0/10
3. [Cursor 零日漏洞允许通过恶意 git.exe 执行任意代码](#item-3) ⭐️ 8.0/10
4. [我们是否过度依赖 AI 进行思考？](#item-4) ⭐️ 8.0/10
5. [极值视角下的应力法则学习](#item-5) ⭐️ 8.0/10
6. [关于天真分散最优性的简单诊断准则](#item-6) ⭐️ 8.0/10
7. [显式构建无套利多期限风险中性边缘分布](#item-7) ⭐️ 8.0/10
8. [研究发现 Uniswap 协议费削减对流动性供给无显著短期影响](#item-8) ⭐️ 8.0/10
9. [学习预测不确定性集提升决策导向的 DRO。](#item-9) ⭐️ 8.0/10
10. [时序样本整合：提升生成模型尾部风险估计](#item-10) ⭐️ 8.0/10
11. [付费移动广告通过应用商店排名提升自然安装](#item-11) ⭐️ 8.0/10
12. [神经网络代理使灾害债券估值加速至毫秒级。](#item-12) ⭐️ 8.0/10
13. [LLM 构建的数据库揭示了弱银行和强银行中的银行挤兑。](#item-13) ⭐️ 8.0/10
14. [0DTE 期权的差分机器学习方法](#item-14) ⭐️ 8.0/10
15. [AI 生产率提升影响工资，最优政策可减少不平等。](#item-15) ⭐️ 8.0/10
16. [作者提出二元预测市场的结构波动模型。](#item-16) ⭐️ 8.0/10
17. [研究发现 LLMs 在经济因果推理中表现出意识形态偏见](#item-17) ⭐️ 8.0/10
18. [基准天花板：人类判断稀缺导致 AI 评估瓶颈](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bonsai 27B：首款可在手机上运行的 27B 参数模型](https://prismml.com/news/bonsai-27b) ⭐️ 9.0/10

PrismML 宣布了 Bonsai 27B，这是一个基于 Qwen3.6 的 270 亿参数多模态模型，通过激进的 1 位或三值量化将模型压缩到低于 4 GB，使其能够在智能手机上运行。 这一成就将前沿的语言和视觉能力带到移动设备上，推动了端侧 AI 的边界，可能改变开发者部署大模型的方式，并引起包括苹果在内的主要平台持有者的关注。 Bonsai 27B 将 Qwen3.6 的语言权重以端到端的 1 位（3.9 GB，保留 FP16 的 89.5%）或三值（5.9 GB，保留 FP16 的 94.6%）格式存储，视觉塔保持 4 位；传统的低于 4 位量化在 AIME、LiveCodeBench 和代理任务上据说会损失精度。

hackernews · xenova · Jul 14, 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48910545)

**背景**: 模型量化通过降低神经网络权重的数值精度来减少内存和计算需求，其中极端的 1 位或三值表示方式的压缩程度远超常见的 4 位方案。像 Qwen3.6-27B 这样的大型语言模型在全精度下通常占用数十 GB，超过了当前智能手机的统一内存预算。先前的研究表明，激进的量化可以保留一定的语言能力，但在复杂推理或代理基准测试上往往表现不佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-27b">PrismML — Announcing Bonsai 27B: The First 27B-Class Model to ...</a></li>
<li><a href="https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/">PrismML Releases Bonsai 27B: 1-bit and Ternary Builds of ...</a></li>
<li><a href="https://cryptobriefing.com/apple-evaluates-prismml-ai-compression-iphones/">Apple evaluates PrismML for AI model compression on iPhones</a></li>

</ul>
</details>

**社区讨论**: 评论者对模型的体积和潜力表示兴奋，SwellJoe 将其与 Gemma 4 12B QAT 进行有利比较，并质疑每一步量化带来的性能损失。其他人则希望了解量化过程的细节，提到苹果据称的兴趣，报告在 LM Studio 中运行 GGUF/MLX 版本遇到困难，并指出演示的烹饪示例存在事实错误。总体情绪是热情的，但对实际准确性和工具调用性能持怀疑态度。

**标签**: `#large language models`, `#model quantization`, `#edge AI`, `#mobile AI`, `#Hugging Face`

---

<a id="item-2"></a>
## [The Tower Keeps Rising](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) ⭐️ 8.0/10

The essay argues that reliance on AI agents and incremental prompting leads to ever‑growing software complexity, likening development to a tower that keeps rising without solid foundations.

hackernews · cdrnsf · Jul 14, 16:57 · [社区讨论](https://news.ycombinator.com/item?id=48909785)

**标签**: `#software-engineering`, `#AI-agents`, `#composability`, `#architecture`, `#Lisp-curse`

---

<a id="item-3"></a>
## [Cursor 零日漏洞允许通过恶意 git.exe 执行任意代码](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) ⭐️ 8.0/10

研究人员披露了 Cursor 中的零日漏洞，攻击者只需在用户代码文件夹中放置恶意的 git.exe，即可在打开仓库时任意执行可执行文件；该漏洞于 2025 年 12 月首次报告，但在六个月以上的时间里未获修复。 该漏洞影响广泛使用的 AI 编程编辑器，可实现静默代码执行，可能导致供应链攻击或勒索软件部署；同时凸显了在流行开发工具中忽视负责任披露的风险。 该利用利用了 Windows 默认在 PATH 之前搜索当前目录的行为，攻击者只需在项目文件夹放置恶意的 git.exe，Cursor 在调用 Git 时就会执行它，且无需用户额外交互。

hackernews · Synthetic7346 · Jul 14, 17:58 · [社区讨论](https://news.ycombinator.com/item?id=48910676)

**背景**: Cursor 是由 Anysphere 开发的 AI 驱动代码编辑器，集成了自然语言编程辅助和标准开发工作流，包括 Git 集成。在 Windows 上，当程序调用可执行文件时未提供完整路径，操作系统会先搜索当前工作目录，这一行为可能被用于可执行文件劫持攻击。负责任披露是指研究人员在公开漏洞之前私下通知供应商，以便供应商有时间修补。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>
<li><a href="https://github.com/InfoSecWarrior/Offensive-Linux-Privilege-Escalation/blob/main/Escalate-via-path-hijacking.md">Offensive-Linux-Privilege-Escalation/Escalate-via-path ...</a></li>
<li><a href="https://byteiota.com/cursor-ide-rce-unpatched-git-exe/">Cursor IDE RCE: Unpatched git.exe Flaw Goes Public | byteiota</a></li>

</ul>
</details>

**社区讨论**: 评论者们争论此漏洞是 Cursor 的 bug 还是 Windows PATH 的特性，有人指出利用需要在受害者代码文件夹中放置恶意的 git.exe，也有人批评供应商在负责任披露后长时间未作回应。部分用户提到 Windows 的安全提示可能会阻止未签名的可执行文件，但大家普遍认为 Cursor 长时间未回应令人担忧。

**标签**: `#security`, `#vulnerability`, `#Cursor`, `#zero-day`, `#responsible disclosure`

---

<a id="item-4"></a>
## [我们是否过度依赖 AI 进行思考？](https://www.artfish.ai/p/offloading-thinking-to-ai) ⭐️ 8.0/10

一个 Hacker News 帖子获得 383 个赞和 387 条评论，讨论过度依赖 AI 进行思考是否会导致认知退化，权衡 AI 辅助的好处与深度理解的必要性。 此次讨论凸显了人们对 AI 驱动的认知卸载可能削弱基础技能的担忧，影响着软件工程师、学习者和专业人士，他们需要在自动化与深度专业知识之间取得平衡。 评论者将 AI 使用比作计算器，警告初级开发者可能无法解释 AI 生成的代码，并认为过度依赖会导致懒惰并削 弱阅读手册或文档的习惯。

hackernews · yenniejun111 · Jul 14, 15:18 · [社区讨论](https://news.ycombinator.com/item?id=48908178)

**背景**: 认知卸载指的是使用外部工具（如计算器或 AI）来减轻心理工作负荷，这是认知科学研究的概念，用于管理有限的工作记忆。大型语言模型（LLM）是基于深度学习的神经网络，在海量文本数据上训练，能够生成、摘要和回答各种问题。人机交互研究探讨人们与 AI 系统的协作方式，关注用户体验、心理影响以及 AI 辅助工作流的设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://evidencebased.education/resource/cognitive-offloading-what-is-it-and-why-is-it-important-2/">Cognitive Offloading: What is it and why is it important?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human–AI_interaction">Human–AI interaction - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者观点分歧，有人认为 AI 像计算器一样能提升生产力，也有人警告过度依赖会导致认知退化、懒惰以及无法解释 AI 生成的工作。几位参与者主张保持深厚的技术知识，以便在 AI 时代保持有效性并更熟练地使用 AI。

**标签**: `#AI`, `#cognitive offloading`, `#software engineering`, `#LLM`, `#human-AI interaction`

---

<a id="item-5"></a>
## [极值视角下的应力法则学习](https://arxiv.org/abs/2607.10700) ⭐️ 8.0/10

论文提出了自相似生成估计（SS-GEN）方法，用于模拟多变量尾部事件并利用深度生成模型估计罕见事件概率。SS-GEN 利用渐近尾部结构将尾部分解为显式径向成分和非参数角向成分，使标准生成模型能够生成超出观测数据的极端样本。 通过将极值理论与深度生成模型相结合，SS-GEN 提供了理论保证和实际效用，可用于风险建模和机器学习，使得罕见事件概率的估计能够远超数据范围。这在金融、工程和环境科学等领域的罕见事件模拟和压力测试中推进了技术水平。 SS-GEN 将尾部分解为显式的径向成分和非参数的角向成分，将尾部学习简化为可由现成深度生成模型处理的紧致域问题。在轻微的非参数参数假设下，SS‑密度在尾处精确的，对正则变化分布具有消失的均匀相对误差，对韦伯尔型分布具有消失的均匀对数相对误差。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 极值理论（EVT）研究概率分布尾部的统计行为，为建模罕见极端事件提供工具。罕见事件模拟旨在估计发生在观测数据范围之外的结果的概率，这在数据稀缺时具有挑战性。深度生成模型如 GAN、VAE 和归一化流可以学习复杂的数据分布并生成合成样本。将 EVT 与这些模型相结合，研究人员可以利用理论尾部结构来指导生成逼真的极端情景。

**标签**: `#extreme value theory`, `#rare event simulation`, `#deep generative models`, `#multivariate tail analysis`, `#stress testing`

---

<a id="item-6"></a>
## [关于天真分散最优性的简单诊断准则](https://arxiv.org/abs/2607.11054) ⭐️ 8.0/10

该论文提出了一个简单的诊断准则（Golden Criterion）来判断天真分散何时最优，并设计了一种自适应两阶段策略，在天真权重和优化权重之间进行混合，在美股溢价预测中实现了样本外的预测准确度、效用和夏普比率的持续提升。 该工作解决了组合理论中长期存在的谜题，提供了可检验的条件和依据投资期限的组合构建指导，对金融机器学习和资产管理具有重要影响。 Golden Criterion 表明，当预测误差协方差矩阵具有 uniform eigenstructure ——即其特征值相等且特征向量张成整个空间——等权重是最小方差最优的；自适应策略通过测量与该条件的经验距离来混合天真权重和优化权重，在不同投资期限上提升了预测准确度、效用和夏普比率。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 天真分散（等权重）是一种简单的组合构建规则，尽管忽略了资产协方差，但在实践中往往表现良好。传统的均值-方差优化依赖于对预测误差协方差矩阵的准确估计，但该矩阵往往噪声较大且不够稳定。当预测误差协方差矩阵表现出 uniform eigenstructure ——即其特征值相等且特征向量张成整个空间——等权重成为最小方差的最优解。这一结果将组合理论、统计估计和特征分析联系起来，为判断天真分散何时最优提供了可检验的条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Portfolio_optimization">Portfolio optimization - Wikipedia</a></li>
<li><a href="https://medium.com/@bauermartin101/the-golden-middle-how-new-research-bridges-naïve-and-optimal-investing-7628148cb830">The Golden Middle: How New Research Bridges Naïve and Optimal Investing | by Martin Bauer | Oct, 2025 | Medium</a></li>
<li><a href="https://ieeexplore.ieee.org/document/317861">Eigenstructure techniques for 2-D angle estimation with ...</a></li>

</ul>
</details>

**标签**: `#portfolio optimization`, `#naive diversification`, `#financial machine learning`, `#Sharpe ratio`, `#covariance matrix`

---

<a id="item-7"></a>
## [显式构建无套利多期限风险中性边缘分布](https://arxiv.org/abs/2607.06204) ⭐️ 8.0/10

本文提出了一种显式方法，通过在观察到的行权价区间内逐区间分配概率质量以匹配输入期权价格，并在观察范围外使用封闭形式的幂律尾部来构建无套利多期限风险中性边缘分布。 它弥合了原始期权价格与下游量化金融工具（如马鞅最优传输、Bass 局部波动率校准、情景分析和尾部风险测量）之间的差距，提供了一种计算高效且无套利的边缘分布，可直接用于这些应用。 在观察到的行权价范围内，该构造精确再现输入期权价格；在范围外，封闭形式的幂律尾部满足价格和斜率边界条件并分配剩余概率质量，从而由构造保证无蝶形和日历套利，并得到具有封闭形式密度、累积分布函数、分位函数以及高效蒙特卡洛抽样的边缘分布。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 风险中性边缘分布是从期权价格推导出的概率分布，用于马鞅最优传输和 Bass 局部波动率校准等方法。蝶形套利指的是期权曲面凸性的违反，而日历套利则涉及到不同到期日之间单调性的违反。确保这些无套利条件对于边缘分布作为下游量化金融模型的有效输入至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://soner.princeton.edu/document/126">Martingale Optimal Transport H. Mete Soner ORFE, Princeton ————————————————————</a></li>
<li><a href="https://arxiv.org/abs/2311.14567">[2311.14567] Calibration of the Bass Local Volatility model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Butterfly_(options)">Butterfly (options) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#risk-neutral measure`, `#arbitrage-free`, `#option pricing`, `#martingale optimal transport`

---

<a id="item-8"></a>
## [研究发现 Uniswap 协议费削减对流动性供给无显著短期影响](https://arxiv.org/abs/2607.08525) ⭐️ 8.0/10

该论文采用预先指定的匹配重叠事件研究差分设计来估计 Uniswap 协议费削减对流动性供给的反应，发现对活跃流动性或局部深度没有显著短期影响。LP 的参与和组成同样没有反应。 提供费用变化对流动性影响的因果证据有助于 DeFi 协议设计者预测治理决策的影响，决定费用层级，并维持 AMM 的稳定性。结果表明短期流动性供给可能对协议费用调整不敏感，这为交易者面向的费用模型和风险评估提供了参考。 该研究在估计前将公开的 Uniswap v3 日志中的处理、事件时间、单位角色和结果重构为经过哈希校验的面板数据，将 LP 侧反应的核心估计量设为核 K_L，并对代币 1 交易量和原生费用收入进行平行趋势检验（未通过），因此仅作描述性报告。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 自动做市商（AMM）通过资金池实现去中心化交易；流动性提供者（LP）可赚取费用但也会遭受逆向选择损失。Uniswap v3 引入了集中流动性以及与交易者面向费用独立的协议费，该费用从 LP 收益中扣除。差分（DiD）是一种准实验方法，通过比较随时间变化过时间的处理组（接受干预）与对照组进行比较，常与事件研究结合以追踪动态效应。

**标签**: `#DeFi`, `#Automated Market Makers`, `#Causal Inference`, `#Liquidity Provision`, `#Uniswap`

---

<a id="item-9"></a>
## [学习预测不确定性集提升决策导向的 DRO。](https://arxiv.org/abs/2607.09820) ⭐️ 8.0/10

本文提出学习预测不确定性集（LPAS），其中深度上下文模型输出名义情景分布、状态依赖的 Wasserstein 半径以及可选的各向异性基准度量，以定义用于 DRO 决策层的上下文不确定性集。半径通过条件分位校准、大小正则化和下游决策损失进行训练，并在 2018‑2026 年的 20 只 S&P 500 成分股上进行了分布式鲁棒投资组合优化的评估。 通过将深度上下文建模与分布式鲁棒优化相结合，LPAS 提供了根据输入状态自适应调整的鲁棒性，而不是使用固定的全局半径。这减少了不必要的保守性，提高了制度适应性，并能够增强如金融投资组合管理等决策导向的应用。 该方法推导出决策层使用的有限对偶形式，采用分阶段训练算法，并可选地学习各向异性度量；训练结合了分位校准、半径大小正则化和实现的决策损失。实验表明年化收益率为 26.28%，夏普比率为 1.30，最终财富为 1.61，尾部损失低于固定半径 DRO 基线，同时平均 Wasserstein 半径更小。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 分布式鲁棒优化（DRO）通过在不确定性集内针对最坏情况分布进行优化来防止模型误设。传统的 Wasserstein DRO 将不确定性集中心放在历史样本上并使用固定半径，这可能过于保守。学习预测不确定性集用深度模型的输出替换固定中心和半径，该模型根据上下文特征进行条件化，使不确定性集能够随当前状态自适应。Wasserstein 距离衡量将一个概率分布转换为另一个分布的成本，而各向异性基准度量可以对不同方向赋予不同权重以捕捉特征特定的不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.09820v1">Learning Predictive Ambiguity Sets for Decision-Focused ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wasserstein_metric">Wasserstein metric - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/mathematics/wasserstein-distance">Wasserstein Distance - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**标签**: `#distributionally robust optimization`, `#machine learning`, `#decision-focused optimization`, `#ambiguity sets`, `#Wasserstein distance`

---

<a id="item-10"></a>
## [时序样本整合：提升生成模型尾部风险估计](https://arxiv.org/abs/2607.10810) ⭐️ 8.0/10

论文提出了时序样本整合（DSI），一种在测试时通过在训练检查点之间集成生成样本以稳定尾部风险估计的框架。在合成多变量过程和高频交易数据上的验证表明，DSI 在固定模拟预算下比单检查点基线显著降低尾部估计误差。 准确的尾部风险估计对金融和工程等风险敏感决策至关重要，因为罕见的不利事件往往决定结果。通过在有限模拟预算下提升生成模拟器的可靠性，DSI 能够改善下游的风险管理和期权定价。 DSI 构建一个检查点混合分布，通过平均各检查点的尾部波动来实现，并有有限预算偏差‑方差理论作为支持。实验表明，在不修改生成目标的情况下，DSI 超过了标准扩散模型和最先进的尾部感知基线。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 深度生成模型在数据稀缺时常被用作模拟器，但标准训练目标主要关注匹配分布的主体，导致低概率尾部容易受到噪声影响。在风险敏感场景中，准确估计这些尾部至关重要，因为决策依赖于罕见的极端事件。通过结合多个训练快照的信息的集成方法可以降低方差并提升尾部估计的稳定性。

**标签**: `#generative models`, `#tail risk estimation`, `#Diachronic Sample Integration`, `#high-frequency trading`, `#bias-variance theory`

---

<a id="item-11"></a>
## [付费移动广告通过应用商店排名提升自然安装](https://arxiv.org/abs/2504.16151) ⭐️ 8.0/10

基于一家美国大型移动游戏开发者的数据，研究发现全面关闭付费广告导致自然安装下降 20‑降低 20‑30%，表明付费广告通过提升应用商店排名对自然流量产生正向溢出。 这一发现与之前认为付费广告被过度归因的研究相悖，意味着移动应用安装广告知移动应用安装广告的实际效果高于仅看付费安装的指标，开发者可能系统性地投入不足。 事件研究显示关闭广告后自然安装下降 20‑30%；面板模型表明每花费 100 美元可带来 32 次付费安装和 2.2 次自然安装，而将应用商店排名纳入控制变量后，广告支出与自然安装的关系消失，说明溢出通过排名机制实现。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 移动应用安装广告允许用户直接从广告中下载应用，而应用商店的排名部分依据最近的下载速度和转化率。之前的搜索广告研究表明付费广告常常为本应自然发生的有机安装争夺功劳（过‑归因）。事件研究设计是一种常用的计量经济学工具，用于估算突发政策变化（如广告关闭）的动态影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/google-ads/answer/6357635?hl=en">About mobile app install ads - Google Help</a></li>
<li><a href="https://neilpatel.com/marketing-stats/halo-effect-paid-ads-lifting-organic-installs/">Paid Ads Boost Organic Installs on the App Store - Neil Patel</a></li>
<li><a href="https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.37.2.203">An Introductory Guide to Event Study Models</a></li>

</ul>
</details>

**标签**: `#mobile advertising`, `#app store optimization`, `#advertising spillovers`, `#empirical analysis`, `#ranking mechanism`

---

<a id="item-12"></a>
## [神经网络代理使灾害债券估值加速至毫秒级。](https://arxiv.org/abs/2509.25899) ⭐️ 8.0/10

研究者开发了一种神经网络代理，能够在毫秒级别内定价灾害债券，相比传统蒙特卡洛和偏微分方程方法，结构性估值速度提升了数个数量级。 该代理实现了灾害债券的实时定价、筛选和敏感性分析，有助于保险联动证券市场进行更快速的风险管理决策。 该代理基于复合泊松灾害债券模型的方差减少蒙特卡洛重要性抽样数据进行训练，在伽马和对数正态严重程度规范下实现亚分误差，能够在 0.03–0.04 秒内定价 1000 份合约，而传统蒙特卡洛需数十至数百秒，偏微分方程基准则需数小时。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 灾害债券是一种保险挂钩证券，将自然灾害的风险转移给投资者，其价值取决于触发事件的发生概率和严重程度。这些债券的结构性定价通常需要耗费大量计算的蒙特卡洛模拟或求解偏微积分方程，每份合约可能需要数秒到数小时。重要性抽样通过在对估计影响大的情景中更频繁地采样来降低蒙特卡洛估计的方差，从而为代理模型提供准确的训练标签；神经网络代理通过学习定价算子的近似，实现训练后的快速评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.corvidpartners.com/field-guide/insurance/catastrophe-bond">Catastrophe Bonds: Trigger Types, Modeling & Valuation ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Importance_sampling">Importance sampling - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0304405X25002302">Deep surrogates for finance: With an application to option ...</a></li>

</ul>
</details>

**标签**: `#catastrophe bonds`, `#neural network surrogate`, `#Monte Carlo importance sampling`, `#financial risk modeling`, `#surrogate modeling`

---

<a id="item-13"></a>
## [LLM 构建的数据库揭示了弱银行和强银行中的银行挤兑。](https://arxiv.org/abs/2601.20285) ⭐️ 8.0/10

研究者将大型语言模型应用于历史报纸，构建了包含 1863 年至 1934 年 3,984 起美国银行挤兑的数据库，发现挤兑在弱银行中更可能发生，但也会因系统性新闻而在强银行中发生，失败主要与基本面不佳相关。 该研究提供了大规模历史数据集，阐明了银行基本面而非仅仅恐慌如何推动挤兑及其经济后果，为金融稳定政策和危机预防提供见解。 强银行通过展示实力、银行间合作和暂停付款来幸免于难，而弱银行上的挤兑导致存款、贷款和当地制造业活动下降幅度显著更大。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 银行挤兑是指大量存款人同时提取资金，通常由对银行偿付能力的恐惧触发。历史上对这些事件的分析需要大量的人工档案工作，但大型语言模型现在可以自动从数字化报纸中提取挤兑事件。了解基本面与恐慌的作用有助于区分自我实现的危机和由实际经济弱点驱动的危机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dhlab.hypotheses.org/4938">Large-Scale Research with Historical Newspapers: A Turning ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S037842661400123X">Correlated bank runs, interbank markets and reserve ...</a></li>
<li><a href="https://www.fdic.gov/regulations/examinations/enforcement-actions/ch-06.pdf">Chapter 6 Removal, Prohibition, and Suspension Actions - FDIC</a></li>

</ul>
</details>

**标签**: `#banking`, `#financial crises`, `#natural language processing`, `#economic history`, `#bank runs`

---

<a id="item-14"></a>
## [0DTE 期权的差分机器学习方法](https://arxiv.org/abs/2603.07600) ⭐️ 8.0/10

本文提出一种差分机器学习方法，用于随机波动跳跃扩散模型下的零天到期（0DTE）期权定价。通过成熟门控方差修正、价格和希腊字母监督以及 PIDE 残差惩罚，并联合训练跳算子网络，采用三阶段训练流程。 该方法相较于单阶段基线提升了跳跃项近似精度，同时保持相当的定价误差，改善了希腊字母估计，产生稳定的一日 Delta 对冲，并在计算速度上优于傅里叶基准，对超短期期权交易和风险管理具有实际价值。 方法采用单一网络同时输出期权价格和希腊字母，引入独立的跳算子网络近似补偿跳跃算子，并采用三阶段训练流程；成熟门控方差修正将期权价格表示为 Black–Scholes 形式加上期限相关的方差项；PIDE 残差惩罚确保模型满足偏微积分方程。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 零天到期（0DTE）期权在交易日收盘时到期，需要能够捕捉快速价格变动和跳跃风险的模型。随机波动跳跃扩散模型将资产价格描述为既有连续波动波动又有不连续跳跃的过程，其定价由偏微积分方程（PIDE）支配。差分机器学习（DML）通过训练神经网络来逼近定价函数，同时引入价格敏感度（希腊字母）和 PIDE 残差惩罚以提高精度和对冲稳定性。成熟门控方差修正通过将方差随到期时间缩放，将 Black–Scholes 公式调整以适用于超短期限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.07600">[2603.07600] Differential Machine Learning for 0DTE Options ... Differential Machine Learning for 0DTE Options with ... 0DTE Volatility Gains Momentum in Income Strategies and ... Differential Machine Learning for 0DTE Options with ... Short-maturity options on realized variance in local ... Markovian stochastic volatility with stochastic correlation ...</a></li>
<li><a href="https://arxiv.org/html/2512.05301v1">Differential ML with a Difference - arXiv.org</a></li>
<li><a href="https://www.emergentmind.com/topics/partial-integro-differential-equation-pide">Partial Integro-Differential Equations (PIDE)</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#options pricing`, `#stochastic volatility`, `#jump diffusion`, `#0DTE`

---

<a id="item-15"></a>
## [AI 生产率提升影响工资，最优政策可减少不平等。](https://arxiv.org/abs/2607.01101) ⭐️ 8.0/10

本文建模了 AI 生产率提升如何影响不同劳动类型的工资，对比了竞争性与垄断性 AI 生产，并推导出缓解不平等的最优税收和监管政策。 它提供了一个严谨的理论框架，以理解 AI 对工资的分配影响，并指导政策制定者设计税收和监管措施以实现帕累托改进。 研究发现，对 AI 生产必不可少的劳动工资增长快于 GDP，被 AI 替代的劳动工资在绝对和相对意义上下降，仅用于最终商品生产的劳动工资与 GDP 同步增长；垄断的 AI 生产会减缓其部署并改变最优政策组合。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 人工智能被视为一种通用技术，能够提升各部门的生产率，但其对工人的影响取决于其任务是被 AI 互补还是被替代。当 AI 生产处于竞争状态时，技术会快速扩散；而垄断控制则可能限制部署并减缓收益的传播。经济学家研究税收、补贴和监管等工具，以重新分配 AI 产生的收入并缓解不平等的上升。

**标签**: `#AI economics`, `#inequality`, `#labor market`, `#technology policy`, `#productivity`

---

<a id="item-16"></a>
## [作者提出二元预测市场的结构波动模型。](https://arxiv.org/abs/2607.08199) ⭐️ 8.0/10

作者提出并估计了一种专门用于二元预测市场的波动模型，结合了 Wright-Fisher 截止分辨率组件和 Glosten-Milgrom 订单流组件，并在 Kalshi 合约的大面板上进行了测试。 这种结构化方法为预测市场提供了首个理论根基的波动预测，优于标准 ARCH/GARCH 基准，并揭示了信息到达和截止效应如何驱动波动率，对做市商、风险管理者和交易者具有重要价值。 该模型将 Wright-Fisher 过程（使二元不确定性随时间解决）与 Glosten-Milgrom 组件（通过价差和成交量捕捉知情交易导致的波动）相结合；实证表明结构变量优于普通 ARCH/GARCH，加入残差 GARCH 后预测效果最佳，波动率在接近 50-50 价格时最高，并在合约临近到期时上升。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 预测市场交易的合约价格代表未来二元结果的概率，价格在 0 和 1 之间，并在已知截止时间结算。传统的波动模型如 ARCH 和 GARCH 是为无界资产收益设计的，对这些有界概率不太适用。论文采用 Wright-Fisher 扩散过程来建模截止临近时不确定性如何解决，并使用 Glosten-Milgrom 顺序交易模型来捕捉通过价差和订单流产生的知情交易导致的波动。实证分析基于 Kalshi 平台的大规模合约面板，Kalshi 是一个在 2021 年推出的受监管的预测市场平台，提供多种事件合约。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.08199">[2607.08199] Volatility in Prediction Markets: A Structural ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kalshi">Kalshi - Wikipedia</a></li>
<li><a href="https://github.com/Cava11/Glosten_and_Milgorm_model">GitHub - Cava11/Glosten_and_Milgorm_model</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#volatility modeling`, `#econometrics`, `#market microstructure`, `#Kalshi`

---

<a id="item-17"></a>
## [研究发现 LLMs 在经济因果推理中表现出意识形态偏见](https://arxiv.org/abs/2604.21334) ⭐️ 8.0/10

研究人员在 EconCausal 基准中加入意识形态争议的案例，并评估了 20 种最先进的大型语言模型在预测经验验证的经济因果方向方面的能力。 研究结果表明，LLMs 在意识形态争议的经济问题上不仅准确性较低，而且系统性地倾向于干预导向的预期，这可能影响其政策分析的可靠性。 从顶尖经济期刊中得出的 10,490 个因果三元组中，研究人员识别出 1,056 个意识形态争议案例；在 20 种模型中有 18 种在真实因果方向符合干预导向预期时准确率更高，错误也倾向于该方向，即便经过一次上下文提示也未被消除。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: 大型语言模型被越来越多地用于经济预测和政策分析，正确推断因果效应的方向至关重要。EconCausal 基准收集了来自顶尖经济和金融期刊的、经验验证的因果方向的治疗‑结果对。通过加入意识形态争议的实例——即干预导向和市场导向视角预测出相反因果符号的情况——该基准可以检验 LLMs 的预测是否受政治意识形态的系统性偏倚影响。

**标签**: `#LLMs`, `#bias`, `#economic reasoning`, `#causal inference`, `#AI safety`

---

<a id="item-18"></a>
## [基准天花板：人类判断稀缺导致 AI 评估瓶颈](https://arxiv.org/abs/2607.01254) ⭐️ 8.0/10

该论文提出了基准天花板问题，表明随着 AI 模型在简单基准项上饱和，有意义的性能区分需要稀缺的专家判断来处理难项。它给出了基准信号贬值的形式模型，并利用 micro1 平台数据量化了高判断评估劳动的稀缺溢价。 理解基准天花板对 AI 安全和治理至关重要，因为它揭示了当前评估方法的局限性，并指导在更好基准和专家评估资源上的投资。这影响着依赖基准评估前沿模型的研究者、开发者和政策制定者。 形式模型表明有效信号集中在难尾基准项，这些项的替代成本随前沿能力凸增，且私人基准生产者在有效性上的投资低于社会最优。来自 micro1 超过一千名具备资质专业人士的数据显示，高判断低可编码评估劳动存在稀缺溢价。

rss · arXiv Quantitative Finance · Jul 14, 04:00

**背景**: AI 能力通常通过在众多测试项上聚合性能的基准来衡量。随着基础模型的提升，它们往往在大多数项上接近满分，只有最难的案例才能区分性能。设计这些难项需要顶尖专家，而这类专家供应有限且成本高，导致评估信号结构性稀缺。

**标签**: `#AI evaluation`, `#benchmarking`, `#foundation models`, `#human judgment`, `#AI safety`

---