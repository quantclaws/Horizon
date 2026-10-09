---
layout: default
title: "Horizon Summary: 2026-10-09 (EN)"
date: 2026-10-09
lang: en
---

> From 43 items, 9 important content pieces were selected

---

1. [Bevy 0.20 released with rendering optimizations and new features.](#item-1) ⭐️ 8.0/10
2. [OpenAI retracts three AI-generated mathematical proofs](#item-2) ⭐️ 8.0/10
3. [Benchmarking Deep Learning vs Statistical Models for Used Electronics Price Forecasting](#item-3) ⭐️ 8.0/10
4. [Study finds heterogeneous LLMs show varying collusion in simulated Bertrand markets](#item-4) ⭐️ 8.0/10
5. [Deep RL with RNNs for optimal trading under partial information](#item-5) ⭐️ 8.0/10
6. [Trade Liberalization Boosts Innovation via Dynamic Firm Responses in China](#item-6) ⭐️ 8.0/10
7. [Diffusive in plain sight: An inconspicuous law of market impact](#item-7) ⭐️ 8.0/10
8. [New CBDC architecture enables credit creation and prevents deposit flight using grassroots coins.](#item-8) ⭐️ 8.0/10
9. [AlphaPADI Introduces Pool-Aware Hierarchical Discrete Diffusion for Symbolic Alpha Discovery](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bevy 0.20 released with rendering optimizations and new features.](https://bevy.org/news/bevy-0-20/) ⭐️ 8.0/10

Bevy 0.20 introduces a renderer that scales O(number of changed entities) on the CPU, along with various new features and improvements. This release improves performance for large scenes and showcases Bevy's rapid evolution, attracting both game developers and simulation builders. The O(number of changed entities) renderer was contributed by pcwalton, while community feedback noted concerns about BSN syntax complexity and the engine's frequent breaking changes.

hackernews · Philpax · Oct 8, 22:57 · [Discussion](https://news.ycombinator.com/item?id=50013610)

**Background**: Bevy is a free, open-source game engine written in Rust that employs an Entity Component System (ECS) architecture for data‑oriented, parallel game logic. It uses the wgpu graphics API to provide cross‑platform rendering on Vulkan, Metal, DirectX 12 and OpenGL. The engine follows a rapid release cycle, delivering new features and breaking changes roughly every three months, with migration guides provided. Its modular design lets developers include only the components they need, making it suitable for both games and simulations.

<details><summary>References</summary>
<ul>
<li><a href="https://bevy.org/">Bevy Engine</a></li>
<li><a href="https://github.com/bevyengine/bevy">GitHub - bevyengine/bevy: A refreshingly simple data-driven ... Learn Bevy - Bevy Engine Bevy Engine by bevy - Itch.io Rust Game Development with Bevy Engine: Complete 2026 Guide Bevy Game Engine Guide - gamineai.com Rust for Game Development: Getting Started with Bevy in 2026</a></li>
<li><a href="https://docs.rs/bevy_ecs/latest/bevy_ecs/">bevy_ecs - Rust - Docs.rs</a></li>

</ul>
</details>

**Discussion**: Community members praised the rendering optimizations and expressed enthusiasm for using Bevy in projects ranging from city builders to real‑time strategy games. Several commenters criticized the BSN syntax as overly complex and noted the engine’s frequent breaking changes as a barrier to commercial adoption. Overall, the discussion reflects strong interest and constructive feedback on the engine’s direction.

**Tags**: `#bevy`, `#rust`, `#game-engine`, `#release`, `#graphics`

---

<a id="item-2"></a>
## [OpenAI retracts three AI-generated mathematical proofs](https://twitter.com/danintheory/status/2108065033070789090) ⭐️ 8.0/10

OpenAI withdrew three AI-generated mathematical results from its public math repository after concerns were raised about their correctness and lack of verification. The retraction underscores the ongoing challenges of ensuring reliability in AI‑generated mathematics and highlights the growing role of formal verification tools like Lean in validating such results. The withdrawn papers were part of OpenAI’s set of 372 AI‑generated math manuscripts released on October 6, 2026; some had Lean certificates while others were only in natural language, and the withdrawal followed errors spotted by mathematicians reviewing the repository.

hackernews · sashank_1509 · Oct 8, 07:05 · [Discussion](https://news.ycombinator.com/item?id=50002650)

**Background**: OpenAI has been publishing large collections of AI‑generated mathematical manuscripts, aiming to explore whether language models can produce novel theorems. Lean is a proof assistant and functional programming language that allows mathematicians to write machine‑checkable proofs, providing a high level of confidence in correctness. Formal verification using tools like Lean has become increasingly important for validating complex AI‑produced results, as traditional peer review can miss subtle errors in lengthy arguments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/blog/openai-math-breakthroughs-what-the-latest-results-mean">OpenAI’s AI Math Breakthroughs: What the Latest Results Mean</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_mathematical_discoveries_by_artificial_intelligence">List of mathematical discoveries by artificial intelligence</a></li>

</ul>
</details>

**Discussion**: Commenters questioned whether the withdrawn proofs lacked Lean verification, noting a mix of verified and unverified works. Several expressed skepticism that AI‑generated proofs, even those checked in Lean, could contain hidden errors that only emerge after extensive scrutiny. Others likened the situation to software engineering practices, suggesting that all results should be fully formalized to avoid mistakes.

**Tags**: `#AI`, `#mathematics`, `#formal verification`, `#Lean`, `#retractions`

---

<a id="item-3"></a>
## [Benchmarking Deep Learning vs Statistical Models for Used Electronics Price Forecasting](https://arxiv.org/abs/2610.10727) ⭐️ 8.0/10

The paper benchmarks eleven forecasting models—including ARIMA, LSTM, N-BEATS, TFT, PatchTST, Informer, TCN, ETS, Theta, and others—on a daily price listing dataset from Polish online marketplaces (Jan 2022–Mar 2025) for horizons of 1 to 365 days. It provides the first systematic multi-horizon comparison of statistical and deep learning methods for a niche but economically important domain, showing that N-BEATS can cut long‑horizon forecast error by over 40% versus the best statistical baseline. N-BEATS achieved the lowest MAPE beyond 30 days, reaching 8.51% at 365 days versus 14.94% for the best statistical baseline—a 43% reduction; at short horizons (1‑7 days) all models converged near 0.72% MAPE, and a single N-BEATS model trained at 365 days generalized to all shorter horizons, while N-BEATS and N-HiTS showed superior hyperparameter stability.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: Time‑series forecasting predicts future values based on historical observations, with statistical approaches such as ARIMA, ETS, and Theta relying on explicit assumptions about trends and seasonality, while deep learning models like LSTM, TCN, N‑BEATS, N‑HiTS, TFT, PatchTST, and Informer learn complex patterns directly from data. Forecasting resale prices of used electronics is especially challenging due to high volatility, sparse listing histories, and non‑normal price dynamics, which differ from the more stable patterns seen in financial markets. The paper fills a gap by providing a large‑scale, real‑world benchmark that evaluates both families of models across multiple horizons and evaluation protocols.

<details><summary>References</summary>
<ul>
<li><a href="https://towardsdatascience.com/n-beats-time-series-forecasting-with-neural-basis-expansion-af09ea39f538/">N-BEATS : Time-Series Forecasting with Neural Basis Expansion</a></li>
<li><a href="https://arxiv.org/abs/1912.09363">[1912.09363] Temporal Fusion Transformers for Interpretable...</a></li>
<li><a href="https://huggingface.co/docs/transformers/main/en/model_doc/patchtst">PatchTST - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#time-series forecasting`, `#deep learning`, `#statistical models`, `#price prediction`, `#second-hand electronics`

---

<a id="item-4"></a>
## [Study finds heterogeneous LLMs show varying collusion in simulated Bertrand markets](https://arxiv.org/abs/2610.11256) ⭐️ 8.0/10

The authors simulated a four‑firm logit Bertrand market using the cheapest tiers of Claude, Gemini, DeepSeek and GPT, testing 11 model compositions over 20 runs of 200 periods each. They found that Claude‑ and Gemini‑based markets capture 72–79 % of monopoly rent, DeepSeek markets about 24 %, while GPT‑based markets show no collusion, with prices drifting above the monopoly level. The results show that algorithmic collusion can emerge among heterogeneous AI agents without explicit communication, highlighting a new safety concern for AI‑driven markets. This has implications for antitrust policy, AI governance, and the design of future language‑model‑based trading systems. Mixing different models did not by itself reduce collusion; market stability depended on the least stable participant, with two GPT firms sufficient to prevent convergence. In mixed markets the monopoly rent was shared in the transitive order DeepSeek > Claude > Gemini > GPT, inversely related to each model’s initial price anchor, consistent with a price‑leadership model.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: In a logit Bertrand market, firms set prices for differentiated products and consumers choose probabilistically based on utility, leading to a smooth best‑response function. Algorithmic collusion occurs when pricing algorithms, without explicit communication, converge to supra‑competitive prices that mimic cartel outcomes. Monopoly rent refers to the extra profit a firm earns above competitive levels when it can act as a sole supplier, which in this experiment is measured as the share of the possible monopoly profit achieved by the market.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2406.02437">Algorithmic Collusion in Dynamic Pricing with Deep Reinforcement...</a></li>
<li><a href="https://arxiv.org/pdf/2404.00806">Algorithmic Collusion by Large Language Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bertrand_competition">Bertrand competition - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#algorithmic collusion`, `#language models`, `#market economics`, `#AI safety`, `#multi-agent systems`

---

<a id="item-5"></a>
## [Deep RL with RNNs for optimal trading under partial information](https://arxiv.org/abs/2511.00190) ⭐️ 8.0/10

The paper, arXiv:2511.00190v2 released in November 2025, introduces three reinforcement‑learning frameworks augmented with recurrent neural networks to infer latent market states and derive optimal trading strategies when only partial market information is observable. By explicitly modeling the trading signal as an Ornstein‑Uhlenbeck process with regime‑switching parameters and treating the problem as a partially observable Markov decision process, the work offers a principled way to improve both performance and interpretability of algorithmic trading systems. The authors compare a one‑step GRU‑based method with two‑step approaches that either feed posterior regime‑probability estimates or forecast the next signal value into the RL agent; simulations show the posterior‑probability version yields higher cumulative rewards and more interpretable policies.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: A partially observable Markov decision process (POMDP) models decision‑making when the agent cannot directly observe the underlying state and must infer it from noisy observations. In this work the trading signal follows an Ornstein‑Uhlenbeck process whose mean‑reverting parameters switch regimes, creating a latent dynamics that the trader must estimate. Recurrent neural networks (RNNs), especially gated recurrent units (GRUs), are used to process the history of observations and produce beliefs about the latent regime or future signal values.

<details><summary>References</summary>
<ul>
<li><a href="https://www.opentrain.ai/glossary/partially-observable-markov-decision-process-pomdp/">Partially Observable Markov Decision Process ( POMDP ) Definition</a></li>
<li><a href="https://www.emergentmind.com/topics/ornstein-uhlenbeck-process">Ornstein - Uhlenbeck Process : Theory & Extensions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recurrent_neural_network">Recurrent neural network - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#financial trading`, `#partially observable Markov decision process`, `#recurrent neural networks`, `#algorithmic trading`

---

<a id="item-6"></a>
## [Trade Liberalization Boosts Innovation via Dynamic Firm Responses in China](https://arxiv.org/abs/2603.23825) ⭐️ 8.0/10

The study finds that China's WTO accession reduced iceberg trade costs by about 13.5% in air‑conditioner manufacturing, raising export and product‑innovation probabilities mainly through dynamic mechanisms that improve expected productivity and lower future entry costs. By showing that most of the innovation response comes from forward‑looking, dynamic incentives rather than static cost reductions, the paper highlights how trade policy can spur long‑term firm growth and innovation. Static effects account for only 9.2% of the total impact; removing the state‑transition channel retains 62.4% of the effect, while eliminating entry‑cost savings retains 28.5%, indicating that dynamic mechanisms drive the majority of the innovation response.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: Trade liberalization lowers barriers to international trade, often modeled as a reduction in iceberg trade costs, which represent all frictions as a multiplicative factor τ≥1. China's accession to the World Trade Organization in 2001 provided a natural experiment for studying how such cost reductions affect firm behavior. In heterogeneous‑firm models, firms make forward‑looking decisions about exporting and product innovation, weighing current profits against expected future productivity states and entry costs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iceberg_Transport_Cost_Model">Iceberg transport cost model - Wikipedia</a></li>
<li><a href="https://ideas.repec.org/p/aah/aarhec/2012-03.html">A Dynamic Model of Trade with Heterogeneous Firms</a></li>

</ul>
</details>

**Tags**: `#trade liberalization`, `#product innovation`, `#dynamic firm model`, `#China WTO accession`, `#iceberg trade costs`

---

<a id="item-7"></a>
## [Diffusive in plain sight: An inconspicuous law of market impact](https://arxiv.org/abs/2606.07059) ⭐️ 8.0/10

The paper shows that imposing diffusivity on both realized and counterfactual returns yields a structural identity that constrains market impact dynamics, producing the square‑root law in the information‑neutral regime and a crossover to linear impact under strong informational coupling. This result links microscopic return diffusivity to macroscopic impact scaling, offering a theoretical basis for the empirically observed square‑root law and its transition to linear impact, with direct implications for optimal execution strategies and no‑arbitrage constraints in quantitative finance. In the information‑neutral regime cumulative impact itself becomes diffusive, retaining an undetermined all‑pass degree of freedom that prevents reduction to a pure surprise model and allows transient impact dynamics and strictly positive impact costs.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: Market impact refers to the price change caused by executing a trade, and empirically its typical magnitude scales with the square root of trade size across many assets and time periods. Diffusive processes describe variables whose increments are independent and normally distributed, akin to Brownian motion, and are used to model random price movements. The information‑neutral regime occurs when a trader's order flow is uncorrelated with underlying price movements, so that realized and counterfactual returns exhibit diffusivity. Under these conditions, imposing diffusivity on both return components constrains impact dynamics, leading to the square‑root law and a crossover to linear impact when informational coupling strengthens.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ceedtrading.com/glossary/market-impact-square-root-law/">Market impact square root law - CEED.trading</a></li>
<li><a href="https://www.mccormick.northwestern.edu/applied-math/areas/diffusive-processes.html">Diffusive Processes | Research Areas | Engineering Sciences...</a></li>
<li><a href="https://arxiv.org/html/2606.07059v2">Diffusive in plain sight: An inconspicuous law of market impact</a></li>

</ul>
</details>

**Tags**: `#market impact`, `#quantitative finance`, `#diffusive processes`, `#optimal execution`, `#no-arbitrage`

---

<a id="item-8"></a>
## [New CBDC architecture enables credit creation and prevents deposit flight using grassroots coins.](https://arxiv.org/abs/2609.27727) ⭐️ 8.0/10

The paper introduces a CBDC architecture based on grassroots currencies, comprising sovereign grassroots coins issued by the central bank, non‑sovereign grassroots coins issuable by any person, and grassroots bonds that add maturity and interest. This design enables credit creation and monetary‑policy operations without triggering deposit flight, as demonstrated in a small‑scale implementation. By solving the deposit‑flight risk and the lack of credit‑creation function in traditional CBDC designs, the architecture could improve the effectiveness of monetary policy and broaden access to central‑bank liquidity operations for non‑bank counterparties. This has implications for financial stability, fintech innovation, and the future evolution of digital money. Sovereign grassroots coins are digital debts of one fiat unit issued by the central bank; non‑sovereign grassroots coins can be issued by any natural or legal entity, are redeemable at par, and their arbitrage‑free price equals one fiat unit. Grassroots bonds provide maturity and interest, allowing the central bank to lend, absorb liquidity, set rates, and trade securities without converting bank deposits into new central‑bank money; the system has been tested on a small scale.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: A central bank digital currency (CBDC) is a digital form of fiat money that is a direct claim on the central bank, but existing designs often face deposit flight when the public converts bank deposits into CBDC. Grassroots currencies allow any individual or entity to issue their own digital tokens denominated in a fiat unit, which can be used to create credit within a CBDC framework. By separating sovereign (central‑bank issued) and non‑sovereign (publicly issued) grassroots coins and adding grassroots bonds, the proposed architecture aims to preserve the credit‑creation function of money while mitigating the risk of rapid deposit outflows.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.27727">[2609.27727] Sovereign Grassroots Currencies : A CBDC ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2609.27727">Sovereign Grassroots Currencies : A CBDC Architecture for Credit...</a></li>
<li><a href="https://www.atlanticcouncil.org/cbdctracker/">Central Bank Digital Currency Tracker - Atlantic Council</a></li>

</ul>
</details>

**Tags**: `#CBDC`, `#grassroots currency`, `#monetary policy`, `#digital currency`, `#financial architecture`

---

<a id="item-9"></a>
## [AlphaPADI Introduces Pool-Aware Hierarchical Discrete Diffusion for Symbolic Alpha Discovery](https://arxiv.org/abs/2610.04959) ⭐️ 8.0/10

AlphaPADI introduces a pool-aware hierarchical discrete diffusion framework that generates complementary symbolic alpha formulas for predicting asset returns by treating the entire alpha pool as the unit of generation, evaluation, and learning. By overcoming the limitations of prior reinforcement learning and generative flow network methods—such as lack of pool context and unified structural revision—AlphaPADI achieves superior predictive and portfolio performance, advancing automated alpha discovery in quantitative finance. The framework comprises grammar‑constrained buffer initialization to build syntactically valid pool candidates, pool‑aware hierarchical diffusion that reconstructs pools at multiple structural scales under current pool context, and reward‑guided pool refinement that evaluates joint predictive performance and inner diversity, updates an elite buffer, and trains the reverse model via reconstruction and preference learning.

rss · arXiv Quantitative Finance · Oct 9, 04:00

**Background**: Formulaic alpha discovery seeks symbolic expressions that predict cross‑sectional asset returns, and in practice multiple formulas are combined into an alpha pool where each formula’s value derives from its complementary contribution to joint predictive performance. Hierarchical discrete diffusion models apply multi‑level denoising on discrete state spaces to generate structured data, enabling generation at different abstraction levels. Prior approaches using reinforcement learning or generative flow networks generate formulas individually, lacking explicit pool‑aware context and a unified mechanism for preserving and revising formula structures across scales.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2610.04959">AlphaPADI: Formulaic Alpha Discovery via Pool - Aware Hierarchical ...</a></li>
<li><a href="https://www.emergentmind.com/topics/hierarchical-discrete-diffusion-model">Hierarchical Discrete Diffusion Model</a></li>
<li><a href="https://grokipedia.com/page/Generative_flow_network">Generative flow network</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#quantitative finance`, `#symbolic regression`, `#diffusion models`, `#alpha discovery`

---