---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> From 29 items, 7 important content pieces were selected

---

1. [Optuna 5.0 发布默认采样器重大更新及新增受限优化 API](#item-1) ⭐️ 8.0/10
2. [展示 HN：Stuxnet 源代码已重建并在 GitHub 上共享用于研究。](#item-2) ⭐️ 8.0/10
3. [Keep Our Servers Running](#item-3) ⭐️ 8.0/10
4. [OpenAI 首席科学家呼吁快速发展 AI 用于防御。](#item-4) ⭐️ 8.0/10
5. [主要化方法揭示依赖不确定性下的分散与集中权衡](#item-5) ⭐️ 8.0/10
6. [代理间金融：区块链基础设施支持自主 AI 代理](#item-6) ⭐️ 8.0/10
7. [重新思考合成情景真实性：兼容性而非保真度驱动对冲表现](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Optuna 5.0 发布默认采样器重大更新及新增受限优化 API](https://github.com/optuna/optuna/releases/tag/v5.0.0) ⭐️ 8.0/10

Optuna v5.0 在 TPESampler 中默认启用多变量 TPE 和 constant liar 策略，改进了带宽计算，并将 TPESampler 设为多目标优化的默认采样器。它还通过 trial.set_constraint() 和 trial.constraints 引入了受限优化的核心 Trial API，废弃了采样器特定的 constraints_func，将 PedAnovaImportanceEvaluator 设为默认参数重要性评估器，并稳定了 GPSampler，提供基于蒙特卡洛的 q‑batch 获取函数。 这些改进提高了 Optuna 在机器学习和超参数调优任务中的效率和易用性，影响着依赖该库的成千上万的研究人员和从业者。通过将高级贝叶斯优化技术设为默认，Optuna v5.0 在无需手动调整的情况下提升了用户可期望的基线性能。 多变量 TPE、constant liar 以及基于 Watanabe 2023 的带宽计算现在在 TPESampler 中默认启用，用于单目标研究；TPESampler 也取代 NSGAIISampler 成为多目标优化的默认采样器。该版本通过 trial.set_constraint() 和 trial.constraints 引入了受限优化的核心 Trial API，废弃了采样器特定的 constraints_func，将 PedAnovaImportanceEvaluator 设为默认参数重要性评估器，并稳定了 GPSampler，提供 qLogEI、qLogCEI、qLogEHVI、qLogCEHVI 等 q‑batch 获取函数用于并行贝叶斯优化。

github · c-bata · Sep 7, 05:15

**背景**: Optuna 是一个开源的超参数优化框架，能够使用 TPE、CMA‑ES、随机搜索等各种采样器自动查找最佳模型配置。它提供了 Pythonic 的 API 来定义目标函数、管理试验以及可视化优化过程，广泛用于机器学习研究和生产环境。历史上，默认采样器一直是 TPESampler，该采样器基于 Tree‑structured Parzen Estimator（TPE）来建模超参数与目标值之间的关系。

**标签**: `#optuna`, `#hyperparameter-optimization`, `#machine-learning`, `#release`, `#sampler`

---

<a id="item-2"></a>
## [展示 HN：Stuxnet 源代码已重建并在 GitHub 上共享用于研究。](https://github.com/Sadpainy/Stuxnet) ⭐️ 8.0/10

Stuxnet 网络武器的重建源代码（约 15,000 行）已由用户 Sadpainy 上传至 GitHub，供研究和教育目的使用。 此次发布使安全研究者能够研究具有历史意义的网络武器，有助于深入理解高级恶意软件技术及其对工业控制系统的威胁。 该代码针对 Siemens Step7 软件，利用四个 Windows 零日漏洞，通过 U 盘、网络共享和 Windows 打印机后台处理服务传播，并包含改变离心机频率的逻辑。

hackernews · CMDDestory · Sep 7, 22:12 · [社区讨论](https://news.ycombinator.com/item?id=49603546)

**背景**: Stuxnet 是一种在 2010 年发现的复杂计算机蠕虫，专门通过操纵西门子 PLC 控制的离心机来攻击伊朗的核浓缩设施。它利用了四个此前未知的 Windows 零日漏洞以及一个西门子 Step7 软件的零日漏洞，通过 U 盘、网络共享和打印机后台处理服务实现自主传播。该蠕虫的攻击使离心机以破坏性速度旋转，导致伊朗铀浓缩计划遭到物理破坏，并标志着首次已知使用网络武器进行物理破坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stuxnet">Stuxnet - Wikipedia</a></li>
<li><a href="https://www.huntress.com/threat-library/malware/stuxnet-malware">Stuxnet Malware: Analysis, Detection, Removal | Huntress</a></li>
<li><a href="https://www.sciencedirect.com/topics/computer-science/stuxnet">Stuxnet - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**社区讨论**: 评论者感谢作者分享了约 15,000 行的 Stuxnet 源代码，并指出其教育价值，引用了如 Countdown to Zero Day 等作品。一些评论者质疑 U 盘传播途径的可行性以及硬件是否可能被预先感染，而其他人则建议增加文档以提高仓库的可导航性。

**标签**: `#cybersecurity`, `#malware`, `#Stuxnet`, `#reverse engineering`, `#historical`

---

<a id="item-3"></a>
## [Keep Our Servers Running](https://blog.archive.org/2026/09/01/keep-our-servers-running-your-recurring-donation-goes-3x-this-september/) ⭐️ 8.0/10

The Internet Archive seeks recurring donations with a 3x match in September, sparking community talk about volunteering, technical challenges, and donation matching mechanics.

hackernews · sonicrocketman · Sep 7, 03:29 · [社区讨论](https://news.ycombinator.com/item?id=49593563)

**标签**: `#internet-archive`, `#fundraising`, `#open-source`, `#digital-preservation`, `#community`

---

<a id="item-4"></a>
## [OpenAI 首席科学家呼吁快速发展 AI 用于防御。](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 8.0/10

Jakub Pachocki，OpenAI 首席科学家，指出我们必须快速训练更智能的 AI 来构建防御系统以应对其他 AI 的危险，但警告这一需求不应成为鲁莽推进的借口。 他的言论凸显了在 AI 安全与防御性 AI 能力之间寻求平衡的日益激烈的辩论，这将影响政策讨论和行业实践。 此言论出自 OpenAI 的博客文章《An Alien Mind》的'scalable defense'部分，Pachocki therein 强调需要强大且对齐的 AI 来保护基础设施并实时防御失控代理。

rss · Simon Willison · Sep 7, 22:26

**背景**: OpenAI 在首席科学家 Jakub Pachocki 的领导下，一直致力于 AI 对齐和安全的研究。防御性 AI 的概念是指部署先进的 AI 系统来检测、减轻或抵御其他 AI 构成的威胁，例如失控代理或恶意模型。Pachocki 的言论体现了 OpenAI 既追求强大 AI 以实现防御目标，又警告不要无序加速的双重策略。

**标签**: `#AI safety`, `#AI ethics`, `#OpenAI`, `#defensive AI`, `#AI policy`

---

<a id="item-5"></a>
## [主要化方法揭示依赖不确定性下的分散与集中权衡](https://arxiv.org/abs/2609.04496) ⭐️ 8.0/10

本文在依赖不确定性下，利用主要化序和双随机矩阵研究投资组合分散与集中的张力，证明准凸性是风险函数弱一致于主要化序的必要且充分条件。进一步得出 VaR、ES、RVaR 和标准差的最坏情况风险不等式，并求解对应的鲁棒投资组合选择问题。 该研究揭示了在依赖结构完全模糊时，鲁棒优化可能倾向于单一资产投资的“集中悖论”，为在风险管理中平衡分散与鲁棒性提供了理论基础。其成果可直接应用于如 FRTB 等监管框架，并为量化金融从业者提供新工具。 论文表明，准凸风险度量（如 VaR、ES、RVaR 和标准差）正是与主要化序兼容的那些度量，从而能够推导出最坏情况界和鲁棒解。此外，它提出了一种在参考依赖结构与最坏情况结构之间插值的加权鲁棒性形式，其结构类似于 FRTB 的 ES 混合。

rss · arXiv Quantitative Finance · Sep 7, 04:00

**背景**: 主要化序通过比较向量的分散程度来排序，双随机矩阵表示保持此顺序的变换，从而提供分散的正式度量。准凸函数的次级集是凸集，这一性质是许多金融风险度量的关键。依赖不确定性指的是对资产收益联合分布缺乏了解，这促使采用鲁棒优化来对抗最坏情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.04496">[2609.04496] Portfolio Diversification and Concentration under Dependence Uncertainty: A Majorization Approach</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doubly_stochastic_matrix">Doubly stochastic matrix - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quasiconvex_function">Quasiconvex function - Wikipedia</a></li>

</ul>
</details>

**标签**: `#portfolio optimization`, `#risk management`, `#robust optimization`, `#majorization order`, `#financial mathematics`

---

<a id="item-6"></a>
## [代理间金融：区块链基础设施支持自主 AI 代理](https://arxiv.org/abs/2607.00245) ⭐️ 8.0/10

该论文提出了代理间金融作为一种基于区块链的基础设施层，使自主 AI 代理能够发现交易对手、协商服务、执行支付并生成可审计的交易证据。 通过将 AI 自主性与可编程结算相结合，它提供了一个信任和支付层，有可能释放可扩展的多代理经济，并重塑去中心化金融和传统金融市场。 该框架依赖智能合约实现可编程结算、ERC-8004 代理注册表、来源钱包、确定性推理和 DeFi 意图挖掘，同时主张有界自主性以避免市场不透明和脆弱。

rss · arXiv Quantitative Finance · Sep 7, 04:00

**背景**: 自主 AI 代理如今能够执行诸如调用外部工具、与其他代理谈判以及发起区块链交易等经济行为，这就需要一种能够处理身份、授权、支付、验证、声誉和问责的基础设施。区块链通过智能合约提供可编程结算、近乎即时的确定性和低费用，而 ERC-8004 等标准则提供去中心化的代理注册表，来源钱包支持可验证计算。有界自主性的概念旨在扩大代理可以安全执行的经济行为范围，而不使市场变得更加不透明或不可问责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.00245">Agent - to - Agent Finance : Blockchain Payments and Trust...</a></li>
<li><a href="https://nevermined.ai/blog/ai-agents-pay-things">How Do AI Agents Pay for Things | Nevermined</a></li>
<li><a href="https://www.pingidentity.com/en/solution/agentic-ai-identity.html">Enable Agentic AI Securely and Confidently | Ping Identity</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#blockchain`, `#multi-agent systems`, `#financial infrastructure`, `#smart contracts`

---

<a id="item-7"></a>
## [重新思考合成情景真实性：兼容性而非保真度驱动对冲表现](https://arxiv.org/abs/2608.20842) ⭐️ 8.0/10

该论文提出了深度对冲中合成情景生成器的决策中心兼容性概念，表明对冲误差可分为学习误差和兼容性差距。实证表明，对冲性能取决于生成器与对冲者的对齐程度，而不仅仅取决于合成数据的真实感。 通过将焦点从统计真实感转移到任务驱动的兼容性，这项工作为设计直接改善对冲结果的合成数据提供了原则性方法，推动了金融机器学习的理论与实践。 作者理论上将对冲性能分解为学习误差和兼容性差距，表明真实感与兼容性可能背离。实验表明，对冲性能受生成器‑对冲者对齐和任务结构支配，而不仅仅取决于真实感。

rss · arXiv Quantitative Finance · Sep 7, 04:00

**背景**: 深度对冲利用深度强化学习从数据中推导最优对冲策略，尤其在真实市场历史稀缺时。从业者常使用合成价格路径生成器来模拟市场动态，并主要根据这些生成器再现真实市场统计特性的程度来评估它们。该工作指出，这些真实感指标并不一定保证对冲有效性，因而提出了以决策为中心的兼容性视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/1802.03042v1">DEEP HEDGING - arXiv.org</a></li>
<li><a href="http://deephedging.com/">Deep Hedging - Learning to Trade</a></li>
<li><a href="https://www.emergentmind.com/topics/deep-hedging-paradigm">Deep Hedging Paradigm</a></li>

</ul>
</details>

**标签**: `#deep hedging`, `#synthetic data`, `#compatibility`, `#financial machine learning`, `#reinforcement learning`

---