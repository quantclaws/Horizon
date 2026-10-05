---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 36 items, 8 important content pieces were selected

---

1. [Strata Enables 125B Qwen 3.8 Flash Next to Run at 100 Tokens/sec on RTX 4090](#item-1) ⭐️ 8.0/10
2. [Developers Prefer Frameworks Over Native Platform APIs, Citing Web Component Frustrations](#item-2) ⭐️ 8.0/10
3. [Canonical Protocol-Graph Composition for Leveraged Event Markets with Atomic Recovery](#item-3) ⭐️ 8.0/10
4. [Expected Utility Regret Rule Achieves Minimax and Bayes Optimal Portfolio Choice.](#item-4) ⭐️ 8.0/10
5. [MintEval Benchmark Tests LLM-Generated Trading Strategy Code for Behavioral Equivalence](#item-5) ⭐️ 8.0/10
6. [Optimal Fee Design for Liquidity Provision in Automated Market Makers](#item-6) ⭐️ 8.0/10
7. [Optimal Investment and Consumption in Infinite-Horizon Stochastic Factor Models](#item-7) ⭐️ 8.0/10
8. [Optimal Quantum Speedups for Repeatedly Nested Expectation Estimation](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata Enables 125B Qwen 3.8 Flash Next to Run at 100 Tokens/sec on RTX 4090](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

The Strata inference engine allows the 125‑parameter‑billion Qwen 3.8 Flash Next mixture‑of‑experts model to generate roughly 100 tokens per second on a single consumer RTX 4090 GPU. This demonstrates that large MoE models can be run locally on affordable hardware, lowering the barrier for developers and researchers to experiment with state‑of‑the‑art LLMs without relying on cloud services. The model activates only 6 B of its 125 B parameters per token, uses 4‑bit quantization (or similar low‑bit format) to fit in GPU memory, and Strata optimizes KV‑cache handling and CUDA scheduling to achieve the reported throughput.

hackernews · snehesht · Oct 4, 12:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

**Background**: Qwen 3.8 Flash Next is a multimodal mixture‑of‑experts language model with 125 B total parameters, of which only 6 B are active per token, designed for cost‑efficient inference in coding, tool use and vision tasks. Strata is an open‑source inference engine that provides an OpenAI/Anthropic‑compatible API on localhost, supports Windows and Linux, and is tuned for low‑VRAM GPUs by optimizing memory usage and kernel scheduling. The NVIDIA RTX 4090 consumer GPU offers 24 GB of GDDR6X memory, making it feasible to hold the quantized model and KV‑cache while measuring output speed in tokens per second.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/Niko1221/Strata">GitHub - Niko1221/ Strata : Qwen3.8-Flash-Next (125B MoE) on...</a></li>
<li><a href="https://www.youtube.com/watch?v=hJ_Iw2E7cnc">Strata GitHub Explained: How a 125B Qwen3.8-Flash-Next... - YouTube</a></li>

</ul>
</details>

**Discussion**: Commenters praised the achievement as an impressive engineering feat that pushes local inference forward, while some expressed skepticism about using quantization below 4‑bits due to possible quality loss. Several users reported obtaining even higher token rates (e.g., 124 tokens/sec) on similar hardware, and compared Strata’s vision performance unfavorably to llama.cpp, noting higher error rates. Others highlighted the trade‑off between model size and speed, preferring the smaller, faster Flash Next variant for practical local use.

**Tags**: `#LLM inference`, `#quantization`, `#consumer GPU`, `#Strata`, `#Qwen`

---

<a id="item-2"></a>
## [Developers Prefer Frameworks Over Native Platform APIs, Citing Web Component Frustrations](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/) ⭐️ 8.0/10

The blog post examines why many developers choose frameworks like React instead of using native platform APIs, pointing out frustrations with Web Components and the appeal of libraries that simplify development. Understanding these preferences helps explain the slow adoption of web standards and guides efforts to improve platform APIs for broader developer acceptance. Comments highlight issues such as the cumbersome nature of native APIs, the need for libraries like Lit to make Web Components usable, and the poor browser implementation of features like <datalist>.

hackernews · vinhnx · Oct 4, 04:10 · [Discussion](https://news.ycombinator.com/item?id=49950554)

**Background**: Web Components are a set of standardized browser APIs that enable developers to create reusable, encapsulated custom elements using technologies like Custom Elements and Shadow DOM. Native platform APIs refer to built‑in browser features such as <datalist> or form validation that provide low‑level functionality without extra libraries. React is a popular JavaScript library that offers a component‑based model and declarative UI, often making complex UI tasks easier than using raw platform APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_Components">Web Components - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_components">Web Components - Web APIs | MDN - MDN Web Docs</a></li>
<li><a href="https://kinsta.com/blog/web-components/">A Complete Introduction to Web Components in 2026 - Kinsta Web Components - Wikipedia Introduction - web components Web Components - Learn JavaScript | W3docs Introduction – Web Components Guide A Brief Introduction to Web Components - freeCodeCamp.org</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that native APIs feel cumbersome and that frameworks like React reduce boilerplate, while many view Web Components as a good idea hampered by awkward APIs and insufficient browser support, often requiring wrappers such as Lit to be practical.

**Tags**: `#web development`, `#frontend`, `#Web Components`, `#React`, `#platform APIs`

---

<a id="item-3"></a>
## [Canonical Protocol-Graph Composition for Leveraged Event Markets with Atomic Recovery](https://arxiv.org/abs/2610.02834) ⭐️ 8.0/10

The paper introduces a canonical protocol-graph composition that gives each financial domain a single storage authority and enables atomic transitions, durable sagas, and exactly-once recovery in leveraged event-market protocols. By providing formal guarantees such as atomic composition and loss conservation, the architecture addresses a critical safety gap in DeFi protocol design, potentially improving composability and reliability of leveraged markets. The approach defines unique storage authorities per domain, uses composition components to avoid recreating balances or state, and is validated via twelve Financial Interaction Assertions (FIA-001–FIA-012) with deterministic deployment manifests and canonical state projection for exactly-once reconstruction after a checkpoint.

rss · arXiv Quantitative Finance · Oct 5, 04:00

**Background**: Leveraged event-market protocols consist of multiple smart contracts handling risk approval, positions, debt, settlement, credit pools, liquidation, and governance, but often lack a single authoritative execution path. A canonical protocol graph assigns each financial domain a unique storage authority and coordinates state transitions through composable components, preventing duplicate storage of balances, debt, or evidence. Durable sagas model long-running financial workflows as sequences of local transactions with compensating actions, while exactly-once recovery ensures that state can be reconstructed deterministically after a chain-confirmed checkpoint without re-executing financial operations.

<details><summary>References</summary>
<ul>
<li><a href="https://patterns.arcitura.com/blockchain-patterns">Blockchain Patterns, Mechanisms, Models, Metrics | Arcitura Patterns</a></li>
<li><a href="https://durable-workflow.com/docs/features/sagas/">Sagas | Durable Workflow</a></li>
<li><a href="https://exactly-once.github.io/posts/exactly-once-delivery/">Exactly-once message delivery · Exactly Once</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#DeFi`, `#protocol design`, `#formal methods`, `#smart contracts`

---

<a id="item-4"></a>
## [Expected Utility Regret Rule Achieves Minimax and Bayes Optimal Portfolio Choice.](https://arxiv.org/abs/2610.02290) ⭐️ 8.0/10

The paper introduces the Expected Utility Regret (EUR) rule for portfolio choice, showing that a single EUR rule attains both minimax and Bayes optimal performance, including their leading constants, without requiring the prior distribution that defines the Bayes criterion. By unifying frequentist minimax and Bayesian optimality, the EUR rule recovers mean‑variance and risk‑parity portfolios as special cases, offering a theoretically grounded framework that could improve practical asset allocation strategies. Under a regular parametric return model, the EUR rule jointly selects a portfolio class and estimates its weights, achieving asymptotic expected regret that matches the minimax and Bayes lower bounds; mean‑variance and risk‑parity portfolios emerge as special cases when utility is smooth, increasing, concave or when asset return‑to‑volatility ratios are exchangeable.

rss · arXiv Quantitative Finance · Oct 5, 04:00

**Background**: Portfolio choice seeks to allocate wealth across assets to maximize the expected utility of terminal wealth, a classic problem in finance and decision theory. The minimax criterion aims to minimize the worst‑case expected regret, while the Bayes criterion minimizes expected regret under a prior distribution; achieving both simultaneously is challenging. Mean‑variance and risk‑parity portfolios are widely used heuristics that respectively optimize return‑variance trade‑offs and equalize risk contributions across assets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Minimax_estimator">Minimax estimator - Wikipedia</a></li>
<li><a href="https://onwealth.net/glossary/regret-theory">Regret Theory | OnWealth</a></li>
<li><a href="https://arxiv.org/html/2610.02290v1">Expected Utility Regret Rule: Minimax and Bayes Optimal Portfolio ...</a></li>

</ul>
</details>

**Tags**: `#portfolio optimization`, `#decision theory`, `#minimax`, `#Bayes`, `#expected utility`

---

<a id="item-5"></a>
## [MintEval Benchmark Tests LLM-Generated Trading Strategy Code for Behavioral Equivalence](https://arxiv.org/abs/2610.03080) ⭐️ 8.0/10

The paper introduces MintEval, a benchmark with 800 tasks that measures whether LLM‑generated trading strategy code behaves like the requested strategy by comparing bar‑by‑bar actions on identical market data, abstracting away profit differences. MintEval reveals a silent failure mode where generated code runs but does not execute the intended risk logic, filling a gap between functional correctness benchmarks and financial forecasting tests, and thus guides safer LLM‑based strategy deployment. MintEval v0 uses a library of composable building blocks to generate reference strategies, measures ActionMatch by comparing bar‑by‑bar actions, and reports that low‑cost models achieve at most 0.544 ActionMatch while Claude Opus 5.5 reaches 0.889 yet still fails silently on 27.5 % of tasks.

rss · arXiv Quantitative Finance · Oct 5, 04:00

**Background**: Large language models are increasingly used to generate executable trading strategy code rather than just signals. Existing benchmarks test either functional correctness of code or predictive performance of strategies, but none verify whether the implemented behavior matches the trader’s natural‑language specification. MintEval bridges this gap by focusing on behavioral equivalence, executing both reference and model‑generated programs on the same market data and comparing their actions bar by bar.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.03080">MintEval : Do LLMs Implement the Trading Strategy You Asked For?</a></li>
<li><a href="https://huggingface.co/datasets/dinobby/MINTEval">dinobby/ MINTEval · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#code generation`, `#trading strategies`, `#benchmark`, `#behavioral equivalence`

---

<a id="item-6"></a>
## [Optimal Fee Design for Liquidity Provision in Automated Market Makers](https://arxiv.org/abs/2508.08152) ⭐️ 8.0/10

The paper models how AMM fees influence liquidity provider profits and total value locked, using large‑scale simulations and market data calibration to derive profit‑maximizing and TVL‑maximizing fee levels under varying volatility and trading volume. Understanding the optimal fee helps DeFi protocols reduce liquidity provider losses from adverse selection and attract more capital, improving overall market efficiency. The study shows that, under normal conditions, the profit‑maximizing fee is close to the centralized exchange’s trading cost and stable, while high volatility calls for a higher fee to shield LPs; under competitive LP entry, the TVL‑maximizing fee sits slightly below the CEX cost and liquidity drops sharply as volatility rises.

rss · arXiv Quantitative Finance · Oct 5, 04:00

**Background**: Automated Market Makers (AMMs) are smart‑contract based pools that enable token swaps using a deterministic pricing formula, providing liquidity on decentralized exchanges. Liquidity providers in AMMs suffer Loss‑Versus‑Rebalancing (LVR), a form of MEV loss incurred when arbitrageurs rebalance their positions while LPs’ holdings remain static. Total Value Locked (TVL) measures the aggregate assets deposited in a protocol and reflects the amount of liquidity available for trading. Fee optimization seeks to balance attracting trading volume with earning enough revenue to offset LVR and other costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/learn/articles/loss-versus-rebalancing-in-de-fi/8609">Loss Versus Rebalancing ( LVR ) in DeFi Explained | Gate Learn</a></li>
<li><a href="https://xrpl.org/docs/concepts/tokens/decentralized-exchange/automated-market-makers">Automated Market Makers ( AMMs )</a></li>
<li><a href="https://www.opengradient.ai/blog/dynamic-amm-fee-research">Mitigating Risk and Loss in AMM Liquidity Pools: A Dynamic Fee ...</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#Automated Market Makers`, `#Liquidity Provision`, `#Fee Optimization`, `#Arbitrage`

---

<a id="item-7"></a>
## [Optimal Investment and Consumption in Infinite-Horizon Stochastic Factor Models](https://arxiv.org/abs/2509.09452) ⭐️ 8.0/10

The paper (arXiv:2509.09452v2) characterizes optimal investment and consumption for a power‑utility investor in an infinite‑horizon stochastic factor model, establishing well‑posedness, providing an efficient numerical algorithm, and developing HJB sub‑ and supersolution theory with verification for models such as the Heston model. These results advance stochastic control theory by giving rigorous existence and computation methods for infinite‑horizon problems, and they enable reliable numerical solution and verification for important finance models like Heston, impacting both academic research and practical portfolio management. For a finite state space the authors give a complete well‑posedness characterization and an efficient algorithm to compute the value function; for an infinite or open‑interval state space modeled by an Itô diffusion they develop sub‑ and supersolution theory for second‑order ODEs without boundary values, yielding explicit bounds and verification arguments, and they show that the continuous‑time value function can be approximated rapidly via a fine discretisation.

rss · arXiv Quantitative Finance · Oct 5, 04:00

**Background**: In stochastic control, the Hamilton‑Jacobi‑Bellman (HJB) equation characterizes the value function of optimal control problems, and verification theorems allow a candidate solution to be confirmed as optimal by substituting it into the HJB PDE. When direct solutions are unavailable, the sub‑ and supersolution method constructs lower and upper solutions whose monotone iteration yields a solution to semilinear elliptic or parabolic PDEs without prescribing boundary values. Infinite‑horizon stochastic factor models extend these ideas by letting the driving factor follow a finite‑state Markov chain or an Itô diffusion, leading to HJB equations that may lack standard boundary conditions and require the theory developed in the paper.

<details><summary>References</summary>
<ul>
<li><a href="https://www.academia.edu/93291628/Analytic_solutions_for_infinite_horizon_stochastic_optimal_control_problems_via_finite_horizon_approximation_A_practical_guide">(PDF) Analytic solutions for infinite horizon stochastic optimal...</a></li>
<li><a href="https://math.stackexchange.com/questions/1307325/method-of-sub-and-supersolutions">partial differential equations - Method of sub- and ...</a></li>
<li><a href="https://math.stackexchange.com/questions/4604971/role-of-verification-theorems-in-stochastic-optimal-control">probability theory - Role of verification theorems in ...</a></li>

</ul>
</details>

**Tags**: `#stochastic control`, `#mathematical finance`, `#HJB equation`, `#optimal investment`, `#Heston model`

---

<a id="item-8"></a>
## [Optimal Quantum Speedups for Repeatedly Nested Expectation Estimation](https://arxiv.org/abs/2602.08120) ⭐️ 8.0/10

The authors introduce a quantum algorithm for repeatedly nested expectation estimation that achieves ε‑error with cost Õ(ε⁻¹) (up to logarithmic factors), matching the known lower bound and thus providing an almost quadratic speedup over the best classical method. This result extends previous quantum speedups for a single nested expectation to arbitrarily many nestings with constant horizon, broadening applicability to problems such as optimal stopping, stochastic control, and multi‑agent systems, and demonstrates a practical path toward quantum advantage in Monte‑Carlo‑type computations. The algorithm builds on a derandomized version of the classical randomized multilevel Monte Carlo (rMLMC) method to resolve the variable‑time overhead that normally hinders quantization of randomized algorithms, and combines it with quantum amplitude estimation to achieve the Õ(ε⁻¹) scaling.

rss · arXiv Quantitative Finance · Oct 5, 04:00

**Background**: Repeatedly nested expectations involve computing expectations of functions that themselves contain expectations, arising in stochastic control, finance, and probabilistic programming. Classical multilevel Monte Carlo (MLMC) reduces variance by combining simulations across levels of accuracy, giving a cost of O(ε⁻²) for standard Monte Carlo and O(ε⁻¹·log²ε) for MLMC under certain conditions. Quantum amplitude estimation can estimate expectations with a quadratic improvement, turning the classical O(ε⁻¹) MLMC cost into Õ(ε⁻¹) when the algorithm is properly derandomized.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.08120">Optimal Quantum Speedups for Repeatedly Nested Expectation ...</a></li>
<li><a href="https://paperswithcode.co/paper/2602.08120">Optimal Quantum Speedups for Repeatedly Nested Expectation ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multilevel_Monte_Carlo_method">Multilevel Monte Carlo method - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#Monte Carlo`, `#nested expectations`, `#algorithm speedup`, `#derandomization`

---