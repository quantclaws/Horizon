---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> From 36 items, 8 important content pieces were selected

---

1. [Strata 使 125B Qwen 3.8 Flash Next 在 RTX 4090 上达到约 100 tokens/秒](#item-1) ⭐️ 8.0/10
2. [开发者为何更倾向框架而非原生平台 API](#item-2) ⭐️ 8.0/10
3. [可规范协议图组合用于杠杆事件市场，实现原子恢复](#item-3) ⭐️ 8.0/10
4. [期望效用遗憾规则同时实现最小最大和贝叶斯最优投资组合选择。](#item-4) ⭐️ 8.0/10
5. [MintEval 基准测试评估 LLM 生成交易策略代码的行为等价性](#item-5) ⭐️ 8.0/10
6. [自动做市商中流动性提供的最优费用设计](#item-6) ⭐️ 8.0/10
7. [无限期随机因子模型中的最优投资与消费](#item-7) ⭐️ 8.0/10
8. [重复嵌套期望估计的最优量子加速](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata 使 125B Qwen 3.8 Flash Next 在 RTX 4090 上达到约 100 tokens/秒](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

Strata 推理引擎使得 125B 参数的 Qwen 3.8 Flash Next 混合专家模型能够在单块消费级 RTX 4090 GPU 上达到约 100 tokens/秒的生成速度。 这表明大型混合专家模型可以在廉价消费硬件上本地运行，降低了开发者和研究者使用最先进 LLM 的门槛，无需依赖云服务。 该模型每 token 仅激活 125B 参数中的 6B，采用 4‑bit（或类似低比特）量化以适应显存，Strata 通过优化 KV‑cache 处理和 CUDA 调度实现了所述吞吐量。

hackernews · snehesht · Oct 4, 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: Qwen 3.8 Flash Next 是一种多模态混合专家语言模型，总参数量为 125B，每 token 仅激活 6B 参数，专为编码、工具使用和视觉任务的高效推理而设计。Strata 是一个开源推理引擎，提供 OpenAI/Anthropic 兼容的本地 API，支持 Windows 和 Linux，并通过优化内存使用和内核调度来适配低显存 GPU。NVIDIA RTX 4090 消费级 GPU 拥有 24 GB GDDR6X 显存，能够容纳量化后的模型及 KV‑cache，并以 tokens/秒 衡量输出速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/Niko1221/Strata">GitHub - Niko1221/ Strata : Qwen3.8-Flash-Next (125B MoE) on...</a></li>
<li><a href="https://www.youtube.com/watch?v=hJ_Iw2E7cnc">Strata GitHub Explained: How a 125B Qwen3.8-Flash-Next... - YouTube</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这是一项令人印象深刻的工程成就，推动了本地推理的发展，但也有人对低于 4‑bit 的量化持怀疑态度，担心质量下降。多位用户报告在类似硬件上获得了更高的 token 速率（例如 124 tokens/秒），并将 Strata 的视觉性能与 llama.cpp 进行比较，指出误差更高。还有人强调模型大小与速度之间的权衡，倾向于使用更小、更快的 Flash Next 变体进行实际的本地应用。

**标签**: `#LLM inference`, `#quantization`, `#consumer GPU`, `#Strata`, `#Qwen`

---

<a id="item-2"></a>
## [开发者为何更倾向框架而非原生平台 API](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/) ⭐️ 8.0/10

这篇博客文章探讨了许多开发者为何选择 React 等框架而非使用原生平台 API，指出了对 Web Components 的不满以及库带来的开发便利。 了解这些偏好有助于解释网络标准采用缓慢的原因，并为改进平台 API 以获得更广泛的开发者接受提供指引。 评论指出原生 API 使用繁琐、需要 Lit 等库才能使 Web Components 可用，以及浏览器对 <datalist> 等功能的实现较差。

hackernews · vinhnx · Oct 4, 04:10 · [社区讨论](https://news.ycombinator.com/item?id=49950554)

**背景**: Web Components 是一组标准化的浏览器 API，使开发者能够使用 Custom Elements 和 Shadow DOM 等技术创建可重用、封装的自定义元素。原生平台 API 指的是浏览器内置的功能，如 <datalist> 或表单验证，能够在不额外加载库的情况下提供底层功能。React 是一种流行的 JavaScript 库，提供基于组件的模型和声明式 UI，往往比直接使用原生 API 更易于构建复杂的用户界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_Components">Web Components - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_components">Web Components - Web APIs | MDN - MDN Web Docs</a></li>
<li><a href="https://kinsta.com/blog/web-components/">A Complete Introduction to Web Components in 2026 - Kinsta Web Components - Wikipedia Introduction - web components Web Components - Learn JavaScript | W3docs Introduction – Web Components Guide A Brief Introduction to Web Components - freeCodeCamp.org</a></li>

</ul>
</details>

**社区讨论**: 评论普遍认为原生 API 使用繁琐，而 React 等框架能减少样板代码；许多人认为 Web Components 是个好点子，但因 API 设计笨拙和浏览器支持不足而受阻，通常需要 Lit 等包装库才能实际使用。

**标签**: `#web development`, `#frontend`, `#Web Components`, `#React`, `#platform APIs`

---

<a id="item-3"></a>
## [可规范协议图组合用于杠杆事件市场，实现原子恢复](https://arxiv.org/abs/2610.02834) ⭐️ 8.0/10

论文提出了一种规范的协议图组合，为每个金融域提供单一存储权威，并实现原子转换、持久 saga 以及恰好一次恢复。 通过提供诸如原子组合和损失守恒等形式保证，该架构填补了 DeFi 协议设计中的关键安全空白，有望提升杠杆市场的可组合性和可靠性。 该方法为每个域定义唯一的存储权威，使用组合组件避免重新创建余额或状态，并通过十二项金融交互断言（FIA-001–FIA-012）进行验证，具备确定性部署清单和规范状态投影，以在检查点后实现恰好一次重建。

rss · arXiv Quantitative Finance · Oct 5, 04:00

**背景**: 杠杆事件市场协议由多个智能合约组成，负责风险批准、头寸、债务、结算、信贷池、清算和治理等功能，但常常缺乏单一的财务执行权威。规范协议图为每个金融域分配唯一的存储权威，并通过可组合的组件协调状态转移，避免重复存储余额、债务或凭证。持久 saga 将长期金融工作流建模为一系列带有补偿操作的本地事务，而恰好一次恢复则确保在链上确认的检查点后能够确定性地重建状态，而不重新执行金融操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://patterns.arcitura.com/blockchain-patterns">Blockchain Patterns, Mechanisms, Models, Metrics | Arcitura Patterns</a></li>
<li><a href="https://durable-workflow.com/docs/features/sagas/">Sagas | Durable Workflow</a></li>
<li><a href="https://exactly-once.github.io/posts/exactly-once-delivery/">Exactly-once message delivery · Exactly Once</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#DeFi`, `#protocol design`, `#formal methods`, `#smart contracts`

---

<a id="item-4"></a>
## [期望效用遗憾规则同时实现最小最大和贝叶斯最优投资组合选择。](https://arxiv.org/abs/2610.02290) ⭐️ 8.0/10

本文提出了期望效用遗憾（EUR）规则用于投资组合选择，表明单一的 EUR 规则能够在不需要贝叶斯准则所需的先验分布的情况下，同时达到最小最大和贝叶斯最优性能，包括其领先常数。 通过统一频率派最小最大和贝叶斯最优性，EUR 规则将均值‑方差和风险平价投资组合作为特例恢复出来，提供了一个理论基础坚实的框架，有望改进实际的资产配置策略。 在正则参数回报模型下，EUR 规则联合选择投资组合类并估计其权重，使渐近期望遗憾与最小最大和贝叶斯下界相匹配；当效用函数光滑、递增且凹陷，或资产的回报‑波动率比率可交换时，均值‑方差和风险平价投资组合作为特例出现。

rss · arXiv Quantitative Finance · Oct 5, 04:00

**背景**: 投资组合选择旨在跨资产分配财富以最大化终端财富的预期效用，这是金融和决策理论中的经典问题。最小最大准则旨在最小化最坏情况下的预期遗憾，而贝叶斯准则则在给定先验分布下最小化预期遗憾；同时实现两者具有挑战性。均值‑方差和风险平价投资组合是两种常用启发式方法，前者优化收益‑方差权衡，后者使各资产的风险贡献相等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Minimax_estimator">Minimax estimator - Wikipedia</a></li>
<li><a href="https://onwealth.net/glossary/regret-theory">Regret Theory | OnWealth</a></li>
<li><a href="https://arxiv.org/html/2610.02290v1">Expected Utility Regret Rule: Minimax and Bayes Optimal Portfolio ...</a></li>

</ul>
</details>

**标签**: `#portfolio optimization`, `#decision theory`, `#minimax`, `#Bayes`, `#expected utility`

---

<a id="item-5"></a>
## [MintEval 基准测试评估 LLM 生成交易策略代码的行为等价性](https://arxiv.org/abs/2610.03080) ⭐️ 8.0/10

论文提出 MintEval 基准，包含 800 项任务，通过在相同市场数据上按棒比较动作（忽略盈亏差异）来评估 LLM 生成的交易策略代码是否与所请求策略行为等价。 MintEval 揭示了一种静默失败模式：生成的代码能够运行却未执行预期的风险逻辑，填补了功能正确性基准与金融预测测试之间的空白，从而有助于提升基于 LLM 的交易策略部署安全性。 MintEval v0 采用可组合的构建块库生成参考策略，通过按棒比较动作计算 ActionMatch，结果显示低成本模型最高仅 0.544，而 Claude Opus 5.5 达到 0.889，但仍有 27.5 % 的任务出现静默失败。

rss · arXiv Quantitative Finance · Oct 5, 04:00

**背景**: 大型语言模型正越来越多地用于生成可执行的交易策略代码，而不仅仅是交易信号。现有基准测试要么检验代码的功能正确性，要么检验策略的预测表现，但未验证实现行为是否与交易者的自然语言描述一致。MintEval 通过关注行为等价性，在相同市场数据上执行参考程序和模型生成程序，并按棒比较它们的动作来弥补这一不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.03080">MintEval : Do LLMs Implement the Trading Strategy You Asked For?</a></li>
<li><a href="https://huggingface.co/datasets/dinobby/MINTEval">dinobby/ MINTEval · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#code generation`, `#trading strategies`, `#benchmark`, `#behavioral equivalence`

---

<a id="item-6"></a>
## [自动做市商中流动性提供的最优费用设计](https://arxiv.org/abs/2508.08152) ⭐️ 8.0/10

该论文通过大规模模拟和市场数据校准，研究了 AMM 费用对流动性提供者利润和总锁定价值的影响，并在不同波动率和交易量条件下得出利润最大化和 TVL 最大化的费用水平。 了解最优费用有助于 DeFi 协议降低流动性提供者因逆向选择造成的损失，吸引更多资本，提升整体市场效率。 研究表明，在正常市场条件下，利润最大化费用接近中心化交易所的交易成本且较为稳定；在高波动时期，较高费用可保护流动性提供者免受严重损失。在竞争性流动性提供者进入时，TVL 最大化费用略低于中心化交易所成本，且随着波动率上升，均衡流动性会急剧下降。

rss · arXiv Quantitative Finance · Oct 5, 04:00

**背景**: 自动做市商（AMM）是基于智能合约的资金池，通过确定性定价公式实现代币兑换，为去中心化交易所提供流动性。流动性提供者在 AMM 中会遭受损失 versus 再平衡（LVR），这是一种 MEV 形式，当套利者重新平衡头寸而 LPs 的持仓保持不变时产生。总锁定价值（TVL）衡量协议中锁定的资产总量，反映可用于交易的流动性规模。费用优化旨在平衡吸引交易量与获得足够收入以抵消 LVR 及其他成本之间的关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/learn/articles/loss-versus-rebalancing-in-de-fi/8609">Loss Versus Rebalancing ( LVR ) in DeFi Explained | Gate Learn</a></li>
<li><a href="https://xrpl.org/docs/concepts/tokens/decentralized-exchange/automated-market-makers">Automated Market Makers ( AMMs )</a></li>
<li><a href="https://www.opengradient.ai/blog/dynamic-amm-fee-research">Mitigating Risk and Loss in AMM Liquidity Pools: A Dynamic Fee ...</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#Automated Market Makers`, `#Liquidity Provision`, `#Fee Optimization`, `#Arbitrage`

---

<a id="item-7"></a>
## [无限期随机因子模型中的最优投资与消费](https://arxiv.org/abs/2509.09452) ⭐️ 8.0/10

该论文（arXiv:2509.09452v2）刻画了无限期随机因子模型中效用为幂函数的投资者的最优投资与消费，给出问题的良好定义性刻画，提供高效数值算法，并发展了 HJB 次解‑超解理论，对包括 Heston 模型在内的模型给出严格验证。 这些结果通过为无限期问题提供严格的存在性和计算方法，推进了随机控制理论，并能够为 Heston 等重要金融模型提供可靠的数值求解和验证，对学术研究和实际投资组合管理都有重要影响。 在有限状态空间情况下，作者给出了问题的完全良好定义性刻画和计算价值函数的高效算法；在无限或开区间状态空间、由伊藤扩散建模的情况下，他们发展了无边界值的二阶常微分方程的次解‑超解理论，得到显式界和验证论证，并表明连续时间的价值函数可通过细致离散化快速近似。

rss · arXiv Quantitative Finance · Oct 5, 04:00

**背景**: 在随机控制中，Hamilton‑Jacobi‑Bellman（HJB）方程描述了最优控制问题的价值函数，验证定理允许通过将候选解代入 HJB 偏微分方程来确认其为最优解。当无法直接求解时，次解‑超解法构造下解和上解，通过单调迭代得到半线性椭圆或抛物偏微分方程的解，而无需预先给定边界值。无限期随机因子模型将这些思想推广，使驱动因子遵循有限状态马尔可夫链或伊藤扩散，从而导致可能缺乏标准边界条件的 HJB 方程，需要论文中发展的理论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/93291628/Analytic_solutions_for_infinite_horizon_stochastic_optimal_control_problems_via_finite_horizon_approximation_A_practical_guide">(PDF) Analytic solutions for infinite horizon stochastic optimal...</a></li>
<li><a href="https://math.stackexchange.com/questions/1307325/method-of-sub-and-supersolutions">partial differential equations - Method of sub- and ...</a></li>
<li><a href="https://math.stackexchange.com/questions/4604971/role-of-verification-theorems-in-stochastic-optimal-control">probability theory - Role of verification theorems in ...</a></li>

</ul>
</details>

**标签**: `#stochastic control`, `#mathematical finance`, `#HJB equation`, `#optimal investment`, `#Heston model`

---

<a id="item-8"></a>
## [重复嵌套期望估计的最优量子加速](https://arxiv.org/abs/2602.08120) ⭐️ 8.0/10

作者提出了一种用于重复嵌套期望估计的量子算法，其在达到 ε‑误差时的成本为 Õ(ε⁻¹)（忽略对数因子），符合已知下界，因而相较于最佳经典方法实现了近乎二次的加速。 该结果将之前单层嵌套期望的量子加速推广到常数层数的多层嵌套，使其适用于最优停止、随机控制、多智能体系统等更广泛的问题，并展示了在蒙特卡罗类计算中实现量子优势的可行途径。 该算法通过构建经典随机多层蒙特卡罗（rMLMC）的去随机化版本来克服量化随机算法时通常出现的变时开销，并结合量子幅度估计实现 Õ(ε⁻¹) 的规模。

rss · arXiv Quantitative Finance · Oct 5, 04:00

**背景**: 重复嵌套期望是指计算包含自身期望的函数的期望，这类问题在随机控制、金融和概率编程中很常见。经典多层蒙特卡罗（MLMC）通过在不同精度层次上组合样本来降低方差，使得标准蒙特卡罗的 O(ε⁻²) 成本在某些条件下可改进为 O(ε⁻¹·log²ε)。量子幅度估计能够对期望进行估计，并在经典方法上实现二次提升；当算法经过去随机化处理时，可以将 MLMC 的成本降至 Õ(ε⁻¹)。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.08120">Optimal Quantum Speedups for Repeatedly Nested Expectation ...</a></li>
<li><a href="https://paperswithcode.co/paper/2602.08120">Optimal Quantum Speedups for Repeatedly Nested Expectation ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multilevel_Monte_Carlo_method">Multilevel Monte Carlo method - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#Monte Carlo`, `#nested expectations`, `#algorithm speedup`, `#derandomization`

---