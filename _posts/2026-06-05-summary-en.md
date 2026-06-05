---
layout: default
title: "Horizon Summary: 2026-06-05 (EN)"
date: 2026-06-05
lang: en
---

> From 40 items, 14 important content pieces were selected

---

1. [VoidZero Is Joining Cloudflare](#item-1) ⭐️ 8.0/10
2. [: Huawei releases KVarN, a native vLLM backend for KV-cache quantization](#item-2) ⭐️ 8.0/10
3. [:Meta ships facial recognition in Ray-Ban smart glasses](#item-3) ⭐️ 8.0/10
4. [: ](#item-4) ⭐️ 8.0/10
5. [AI enthusiasts race against time while skeptics race against entropy.](#item-5) ⭐️ 8.0/10
6. [:Polymarket-v1 Database Released with Ground-Truth Aggressor Direction](#item-6) ⭐️ 8.0/10
7. [ReSGA: Retrieval-Enhanced Self-Grouping Autoencoder for VaR and ES](#item-7) ⭐️ 8.0/10
8. [:Preisach Hysteresis Model Applied to Gig Worker Transaction Acceptance](#item-8) ⭐️ 8.0/10
9. [: Fairness and Strategy-Proofness Impossible in Multi-Asset AMMs](#item-9) ⭐️ 8.0/10
10. [LLMs Show Human-Like Risk Aversion but Differ in Decision Mechanisms](#item-10) ⭐️ 8.0/10
11. [: Capacity, Technology Portfolios, and the Paradox of Concentration](#item-11) ⭐️ 8.0/10
12. [New Projection-Based Estimator Recovers Joint State Prices from Options](#item-12) ⭐️ 8.0/10
13. [: Fair Distribution of Digital Payments: Balancing Transaction Flows for Regulatory Compliance](#item-13) ⭐️ 8.0/10
14. [: FinTradeBench Introduces 1,400‑Question Financial Reasoning Benchmark for LLMs](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [VoidZero Is Joining Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/) ⭐️ 8.0/10

VoidZero, the company behind Vite, is joining Cloudflare to integrate its developer tooling with Cloudflare's platform.

hackernews · coloneltcb · Jun 4, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48398055)

**Tags**: `#Cloudflare`, `#Vite`, `#VoidZero`, `#frontend tooling`, `#acquisition`

---

<a id="item-2"></a>
## [: Huawei releases KVarN, a native vLLM backend for KV-cache quantization](https://github.com/huawei-csl/KVarN) ⭐️ 8.0/10

: Huawei's KVarN introduces a native vLLM backend that quantizes the key‑value cache to lower precision, enabling 3‑5× more KV‑cache capacity and up to ~1.3× higher throughput than FP16 while maintaining FP16‑level accuracy. : By reducing KV‑cache memory footprint, KVarN allows longer context windows and larger batch sizes on the same hardware, improving LLM serving efficiency and lowering costs. : KVarN is calibration‑free, requires only a single flag to enable, works as a drop‑in vLLM attention backend, and claims up to ~2.4× speedup over TurboQuant while delivering FP16‑level output quality.

hackernews · theanonymousone · Jun 4, 15:18 · [Discussion](https://news.ycombinator.com/item?id=48399974)

**Background**: : The key‑value (KV) cache stores intermediate keys and values during LLM autoregressive generation, and its size grows with sequence length, often becoming a memory bottleneck. vLLM is a high‑throughput LLM serving library that manages KV‑cache memory efficiently and supports pluggable attention backends. Quantizing the KV cache to lower‑precision formats such as FP8 or FP4 reduces its memory footprint, allowing more tokens to be cached and improving throughput, though aggressive quantization can affect accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/huawei-csl/KVarN">GitHub - huawei-csl/KVarN: KVarN is a native vLLM KV-cache quantization ...</a></li>
<li><a href="https://forums.developer.nvidia.com/t/kvarn-native-vllm-backend-for-kv-cache-quantization-by-huawei/372333">KVarN: Native vLLM backend for KV-cache quantization by Huawei</a></li>
<li><a href="https://docs.vllm.ai/en/stable/features/quantization/quantized_kvcache.html">Quantized KV Cache — vLLM</a></li>

</ul>
</details>

**Discussion**: : Commenters expressed surprise at the claimed performance gains, questioning whether KVarN truly outperforms existing quantization methods like TurboQuant while matching FP16 quality. Some asked why the work was released as a separate backend rather than a pull request to the main vLLM repository, indicating interest in upstream integration. One comment appeared off‑topic, but overall the discussion reflects strong curiosity and cautious optimism about the technology.

**Tags**: `#LLM inference`, `#KV-cache quantization`, `#vLLM`, `#Huawei`, `#performance optimization`

---

<a id="item-3"></a>
## [:Meta ships facial recognition in Ray-Ban smart glasses](https://www.buchodi.com/meta-glasses-facial-recognition/) ⭐️ 8.0/10

Meta has begun shipping facial recognition capabilities in its Ray-Ban Meta smart glasses, enabling real-time identification of people via the glasses' integrated cameras. The rollout reignites debates over privacy and surveillance while offering potential accessibility benefits for people with face blindness, influencing public perception of wearable tech and likely prompting regulatory scrutiny. The glasses feature two cameras, open-ear speakers, a microphone and a touchpad; facial recognition can be performed on-device or via cloud services such as Pimeyes, raising concerns about battery life, accuracy and the need for an internet connection for cloud-based matching.

hackernews · buchodi · Jun 4, 19:36 · [Discussion](https://news.ycombinator.com/item?id=48403588)

**Background**: Ray-Ban Meta smart glasses are a collaboration between Meta Platforms and EssilorLuxottica, equipped with dual cameras and audio components for capturing media and enabling voice commands. Facial recognition technology analyzes visual data to identify individuals, a capability previously restricted on devices like Google Glass due to privacy concerns. Meta’s internal research program, Project Aria, explores similar sensor-laden wearables for contextual AI and robotics, indicating a longer-term investment in wearable perception.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ray-Ban_Meta">Ray - Ban Meta - Wikipedia</a></li>
<li><a href="https://www.youtube.com/watch?v=XddWbkywhlk">Someone Put Facial Recognition Tech onto Meta 's Smart... - YouTube</a></li>
<li><a href="https://www.businessinsider.com/meta-ray-ban-smart-glasses-facial-recognition-distracted-2026-2">Meta Thinks We're Too Distracted to Care About Facial Recognition</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a desire for an offline, privacy‑preserving version to aid face‑blind users, while others warned of surveillance risks and suggested tactics such as flooding the system with fake data or creating detectors to warn nearby people of glasses users, referencing Foucault’s panopticon as a conceptual framework.

**Tags**: `#facial recognition`, `#smart glasses`, `#privacy`, `#Meta`, `#wearable technology`

---

<a id="item-4"></a>
## [: ](https://momentsingraphics.de/Siggraph2026.html) ⭐️ 8.0/10

Hacker News discussion on Gaussian Point Splatting explores its rendering potential, comparisons to mesh splatting, and community questions about practical benefits and tutorials.

hackernews · ibobev · Jun 4, 10:48 · [Discussion](https://news.ycombinator.com/item?id=48396792)

**Tags**: `#Gaussian Splatting`, `#Rendering`, `#Computer Graphics`, `#Point Clouds`, `#Real-time Rendering`

---

<a id="item-5"></a>
## [AI enthusiasts race against time while skeptics race against entropy.](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything) ⭐️ 8.0/10

The article argues that both AI enthusiasts and skeptics have valid points, noting that enthusiasts see real, discontinuous leaps in capabilities while skeptics warn that rapid code shipping erodes trust and institutional knowledge. It highlights the leadership and engineering challenge of bridging the gap between fast AI‑driven productivity and software reliability, showing that missing feedback loops can threaten both competitiveness and system stability. Charity Majors emphasizes that enthusiasts are not wrong about AI’s gains and skeptics are not wrong about the withdrawals from a trust account, and she identifies the missing natural feedback loop as the core problem to solve.

rss · Simon Willison · Jun 4, 23:55

**Background**: In modern software engineering, teams increasingly adopt AI tools to accelerate development, but rapid changes can outpace human review, leading to gaps in understanding and trust. Trust is built over time through shared context and reliable systems, and when it erodes, on‑call burdens and incoherent products can result. This tension creates a need for deliberate feedback mechanisms that align enthusiastic adoption with cautious oversight.

**Tags**: `#AI`, `#software engineering`, `#technology adoption`, `#skepticism`, `#enthusiasm`

---

<a id="item-6"></a>
## [:Polymarket-v1 Database Released with Ground-Truth Aggressor Direction](https://arxiv.org/abs/2606.04217) ⭐️ 8.0/10

The paper introduces the Polymarket-v1 Database, a complete on-chain trade archive of Polymarket's first-generation CTF Exchange on Polygon spanning November 21, 2022 to April 28, 2026, containing 1.20 billion trades across 1.30 million markets and $61 billion in nominal volume, with 100% ground-truth aggressor direction derived from blockchain settlement. Having verified trade direction enables accurate measurement of market microstructure metrics such as VPIN and OFI, improving transaction cost analysis and linking microstructure quality to forecasting performance in prediction markets. The dataset records 1.20 billion trades and $61B volume; its ground-truth aggressor direction shows that standard tick rule and bulk volume classification achieve only about 50% accuracy, masking a correctable price‑level gradient caused by trade direction autocorrelation and concentrated market‑making.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: Polymarket is a decentralized prediction market platform that uses the Conditional Token Framework (CTF) on the Polygon blockchain to create ERC‑1155 tokens representing market outcomes. The CTF Exchange facilitates atomic swaps between these conditional tokens and a base ERC‑20 currency, recording every trade on‑chain. Aggressor direction indicates whether a trade was initiated by the buyer (aggressor) or seller, and in this dataset it is derived directly from blockchain settlement, eliminating the need for heuristic inference. Traditional microstructure tools such as the tick rule and bulk volume classification infer trade direction from price changes and volume, but their accuracy can be low in markets where price trends persist due to autocorrelation or concentrated liquidity.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.polymarket.com/trading/ctf/overview">Conditional Token Framework - Polymarket Documentation</a></li>
<li><a href="https://github.com/polymarket/ctf-exchange">Polymarket/ctf-exchange - GitHub</a></li>
<li><a href="https://www.redalyc.org/journal/1230/123075331006/html/">Analysis of the Tick Rule and Bulk Volume Classification algorithms in the Brazilian stock market</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#blockchain data`, `#market microstructure`, `#dataset`, `#Polymarket`

---

<a id="item-7"></a>
## [ReSGA: Retrieval-Enhanced Self-Grouping Autoencoder for VaR and ES](https://arxiv.org/abs/2606.04576) ⭐️ 8.0/10

The paper introduces ReSGA, a large-parameter retrieval-enhanced self-grouping autoencoder designed to learn Value-at-Risk and Expected Shortfall from monthly US equity returns (1926–2023) using 153 firm characteristics. It outperforms twelve econometric and machine learning baselines in out-of-sample loss and statistical backtesting, and its forecasts yield economic gains via a size-enhanced left-side momentum strategy. By demonstrating that model improvements stem from data complexity rather than mere parameter count, ReSGA offers a principled way to scale tail risk models for big‑data financial applications. Its interpretability through group‑importance and transfer‑learning analyses also supports cross‑market generalization and practical risk‑management decisions. ReSGA employs millions of parameters, integrates a retrieval mechanism with a self‑grouping autoencoder, and is trained on 98 years of US equity data with 153 characteristics. Scaling analysis shows that gains in joint VaR‑ES forecasting are driven by data complexity, while group‑importance and transfer‑learning studies reveal the model’s interpretability and ability to generalize across markets.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: Value-at-Risk (VaR) measures the maximum loss over a target horizon at a given confidence level, while Expected Shortfall (ES) averages losses beyond the VaR threshold, together forming key tail‑risk metrics in finance. Autoencoders are neural networks that learn compact data representations by reconstructing inputs, and retrieval‑enhanced architectures augment them with external memory lookup to capture complex dependencies. Modeling tail risk with large‑parameter networks helps overcome misspecification risks inherent in traditional econometric approaches when faced with big‑dimensional, long‑term asset data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.04576">A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall</a></li>
<li><a href="https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_7_DeepLearning/Autoencoders.html">3. Autoencoders and anomaly detection — Reproducible Machine...</a></li>

</ul>
</details>

**Tags**: `#financial risk modeling`, `#Value-at-Risk`, `#Expected Shortfall`, `#deep learning`, `#autoencoder`

---

<a id="item-8"></a>
## [:Preisach Hysteresis Model Applied to Gig Worker Transaction Acceptance](https://arxiv.org/abs/2606.04916) ⭐️ 8.0/10

The paper models gig worker acceptance decisions using a Preisach hysteresis framework and a dual-output neural network to estimate acceptance and rejection utilities, achieving Jaccard = 0.827 and ROC AUC = 0.799 on 36,891 transactions. By revealing latent worker preferences, the approach enables platforms to lower wages while increasing fill rates, offering a novel interdisciplinary tool for labor economics and machine‑learning applications. The model uses a dual‑output neural network (shared layers 256→128 with a margin loss enforcing U₁≥U₀) to estimate acceptance and rejection utilities, computes the Preisach gap U₁−U₀, feeds it plus clip‑stabilised price‑to‑threshold encodings into an XGBoost classifier.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: The Preisach hysteresis model represents hysteretic behavior as an integral over binary threshold elements, originally used for magnetic materials but applicable to any system with history‑dependent output. In gig labor markets, each worker’s private acceptance wage creates a heterogeneous threshold, making the aggregate acceptance pattern naturally hysteretic. A dual‑output neural network learns two related outputs simultaneously, often with shared layers and a loss that enforces an order constraint between them.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Preisach_model_of_hysteresis">Preisach model of hysteresis - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/engineering/preisach-model">Preisach Model - an overview | ScienceDirect Topics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_network_(machine_learning)">Neural network (machine learning) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#gig economy`, `#hysteresis model`, `#Preisach`, `#worker utility`, `#machine learning`

---

<a id="item-9"></a>
## [: Fairness and Strategy-Proofness Impossible in Multi-Asset AMMs](https://arxiv.org/abs/2606.04959) ⭐️ 8.0/10

The paper shows that for automated market makers handling three or more assets, no aggregation rule can satisfy both fairness and strategy‑proofness except dictatorial rules, proving a structural impossibility. This result bridges DeFi, mechanism design and social choice theory, guiding designers of AMMs that fairness and incentive compatibility cannot be simultaneously achieved with many assets. The proof identifies the weighted Aitchison centroid (the weighted geometric mean of liquidity providers’ preferred pools) as the unique fair rule, while strategy‑proofness forces a median‑type rule; only a single‑provider dictator satisfies both, and the obstruction disappears for two‑asset pools.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: Automated market makers (AMMs) enable trustless trading by using a constant function to define prices, with liquidity providers supplying pools of assets. Fairness in this context follows Arrow’s condition, requiring the aggregation of providers’ preferred pools to be unbiased, while strategy‑proofness ensures no provider can benefit by misreporting its preferred pool. The paper studies the weighted‑product family of AMMs and shows that fairness forces a mean‑type aggregation (the weighted Aitchison centroid) whereas strategy‑proofness forces a median‑type aggregation, making them incompatible except under dictatorship.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.04959v1">Fairness and Strategy-Proofness in Automated Market Makers - arXiv</a></li>
<li><a href="https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.51">An Axiomatic Characterization of CFMMs and Equivalence to...</a></li>
<li><a href="https://www.researchgate.net/publication/228997817_ON_IRRELEVANCE_OF_ALTERNATIVES_AND_OPINION_POOLING">(PDF) on irrelevance of alternatives and opinion pooling</a></li>

</ul>
</details>

**Tags**: `#automated market makers`, `#fairness`, `#strategy-proofness`, `#mechanism design`, `#DeFi`

---

<a id="item-10"></a>
## [LLMs Show Human-Like Risk Aversion but Differ in Decision Mechanisms](https://arxiv.org/abs/2606.04978) ⭐️ 8.0/10

The study evaluated 28 large language models in the St. Petersburg game, finding that most produce finite bids resembling human risk aversion. However, controlled variants reveal substantial mechanism-level differences, with instruction tuning and human-cue prompting lowering bids but leaving underlying response patterns largely unchanged. These findings indicate that superficial behavioral alignment can mask misaligned decision mechanisms, which is critical for AI safety and high-stakes applications of LLMs. Evaluations must therefore look beyond outcome similarity to assess true mechanistic alignment. The paper tested 28 models including base and instruction-tuned variants, using a structured prompt suite covering the original game, controlled variants (truncation, repeated play, numeric endowment, occupational identity), and a human-perspective prompt. Most mechanism-level response patterns remained largely unchanged despite bid reductions from instruction tuning.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: The St. Petersburg game is a classic paradox where a coin is flipped until heads appears, paying 2^n dollars, yielding an infinite expected payoff, yet humans typically report a low, finite willingness to pay. In LLM research, outcome-level resemblance refers to models producing similar outputs to humans, while mechanism-level alignment concerns whether the internal decision processes match human reasoning. Distinguishing these helps assess whether AI behavior is genuinely aligned or merely superficial.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/St._Petersburg_paradox">St. Petersburg paradox - Wikipedia</a></li>
<li><a href="https://plato.stanford.edu/entries/paradox-stpetersburg/">The St. Petersburg Paradox (Stanford Encyclopedia of Philosophy)</a></li>

</ul>
</details>

**Tags**: `#LLM risk decision-making`, `#St. Petersburg game`, `#AI alignment`, `#mechanistic analysis`, `#instruction tuning`

---

<a id="item-11"></a>
## [: Capacity, Technology Portfolios, and the Paradox of Concentration](https://arxiv.org/abs/2407.03504) ⭐️ 8.0/10

The paper models firms competing via supply schedules with multiple technologies, each having constant marginal cost up to its capacity, and shows that capacity and technological efficiency are distinct sources of market power with opposite effects on prices. Using Colombia's wholesale electricity market, it finds a U‑shaped relationship between concentration and prices, where modest capacity transfers to the largest efficient firm lower prices but large transfers raise them. The results challenge the standard antitrust view that higher concentration always raises prices, showing that capacity limits and technology portfolios can produce non‑monotonic price effects. This has direct implications for antitrust policy tools such as capacity caps, divestitures, and merger review in electricity and other oligopolistic markets. The model assumes each technology has a constant marginal cost up to a capacity limit, derives a unique equilibrium in supply‑function competition, and proves that transferring high‑cost capacity to the most efficient firm can reduce prices by up to 30 % in low‑concentration markets. Large transfers reverse the effect, creating a U‑shaped price‑concentration curve, and the findings are validated with empirical data from Colombia’s hydropower‑rich electricity market where weather shocks shift capacity across firms.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: In supply‑function (or supply‑schedule) competition, firms choose how much to offer at each price, and equilibrium outcomes depend on both their cost structures and available capacity. Market concentration measures the share of output held by the largest firms, and traditional antitrust theory predicts a monotonic rise in prices as concentration increases. Colombia’s wholesale electricity market relies heavily on hydropower, whose output varies with weather, causing exogenous shifts in hydropower capacity across technology‑diversified firms and providing a natural experiment for studying concentration effects.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.03504">[2407.03504] Prices and Concentration: A U-shape? Theory and Evidence from Renewables</a></li>
<li><a href="https://ideas.repec.org/p/hal/wpaper/hal-04631762.html">Prices and Concentration: A U-Shape? Theory and Evidence from Renewables</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0140988318300550">Choosing roles under supply function competition - ScienceDirect.com</a></li>

</ul>
</details>

**Tags**: `#industrial organization`, `#electricity markets`, `#antitrust policy`, `#capacity constraints`, `#technology portfolio`

---

<a id="item-12"></a>
## [New Projection-Based Estimator Recovers Joint State Prices from Options](https://arxiv.org/abs/2601.14852) ⭐️ 8.0/10

We propose a projection-based estimator that approximates target payoffs over the entire state space using portfolios of observed options to extract joint risk-neutral distributions. The method improves upon Carr and Madan (2001) univariate estimates, provides an explicit finite-sample bound interpretable as a measure of market incompleteness, and, when applied to two unexpected Swiss National Bank announcements about the EUR/CHF floor, shows that dependence accounts for about two‑thirds of the change in joint crash risk. By enabling the estimation of joint risk-neutral probabilities and correlations even when markets are incomplete, the estimator offers a practical tool for assessing multi‑asset crash risk and quantifying market incompleteness. The finding that dependence drives most of the joint crash risk change during policy events highlights the importance of modeling co‑movements, which can inform risk management, derivative pricing, and central‑bank intervention strategies. The estimator forms a linear projection of the desired payoff onto the span of observed option payoffs (including cross‑rate options), yielding coefficients that can be computed via ordinary least squares. It delivers an explicit finite‑sample error bound that scales with the projection residual, interpretable as a measure of how far the market is from completeness, and in empirical tests it improves univariate risk‑neutral density estimates relative to the Carr–Madan Fourier method while attributing roughly 66% of the observed joint crash risk shift to changes in dependence rather than marginal volatility.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: In a complete, arbitrage‑free market there exists a unique risk‑neutral measure under which discounted asset prices are martingales, allowing state prices to be recovered from option prices via the Breeden–Litzenberger formula. When markets are incomplete, multiple risk‑neutral measures exist and the joint distribution of state prices cannot be identified uniquely, making the extraction of joint risk‑neutral probabilities a longstanding open problem since Ross (1976). The Carr–Madan (2001) approach provides a Fourier‑based method for estimating univariate risk‑neutral densities from option prices, but extending it to multivariate settings remains challenging, which motivates the projection‑based estimator proposed in this paper.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Risk-neutral_measure">Risk-neutral measure - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2601.14852">Recovering State Prices from Options</a></li>
<li><a href="https://gregorygundersen.com/blog/2023/01/26/carr-madan/">Carr – Madan Formula</a></li>

</ul>
</details>

**Tags**: `#options pricing`, `#risk-neutral distribution`, `#financial econometrics`, `#market incompleteness`, `#state price recovery`

---

<a id="item-13"></a>
## [: Fair Distribution of Digital Payments: Balancing Transaction Flows for Regulatory Compliance](https://arxiv.org/abs/2601.02369) ⭐️ 8.0/10

The authors formulate the redistribution of UPI transactions to satisfy NPCI's 30% per‑app cap as a Minimum Edge Activation Flow (MEAF) problem on a user‑app bipartite graph and prove that MEAF is NP‑complete. They also introduce a Decoupled Two‑Stage Allocation Strategy (DTAS) heuristic and show it finds near‑optimal solutions in seconds on large semi‑synthetic data. Addressing the duopoly of PhonePe and Google Pay, the work provides a concrete algorithmic tool for regulators and payment providers to enforce concentration limits while minimizing user disruption. Its theoretical depth (NP‑completeness proof) and practical heuristic advance the intersection of fintech regulation and network‑flow algorithms. MEAF is defined on a bipartite graph where activating an edge corresponds to a new app installation; the goal is to achieve a feasible flow respecting app capacities while minimizing activated edges. The paper proves MEAF NP‑complete via reduction from a known NP‑complete problem and evaluates DTAS against an ILP baseline, reporting solution quality within a few percent of optimal and runtimes under seconds.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: The Unified Payments Interface (UPI) is India’s real‑time payment system, where a few apps such as PhonePe and Google Pay dominate transaction volume. To curb this concentration, the National Payments Corporation of India (NPCI) mandated that no single UPI app may exceed 30% of total transaction volume. Enforcing this cap requires redistributing existing user‑app links, which can be modeled as a flow problem on a bipartite graph of users and apps, where adding a link corresponds to activating an edge. Minimum Edge Activation Flow seeks to minimize such activations while satisfying capacity constraints, a variant known to be computationally hard.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2601.02369">Fair Distribution of Digital Payments: Balancing Transaction Flows for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://indianexpress.com/article/business/economy/unified-payments-interface-30-cap-done-to-protect-ecosystem-but-may-end-up-being-an-own-goal-6982961/">Unified Payments Interface: 30% cap done to ‘protect ecosystem’ but may end up being an own goal | Business News - The Indian Express</a></li>

</ul>
</details>

**Tags**: `#digital payments`, `#algorithmic fairness`, `#network flow`, `#NP-completeness`, `#fintech regulation`

---

<a id="item-14"></a>
## [: FinTradeBench Introduces 1,400‑Question Financial Reasoning Benchmark for LLMs](https://arxiv.org/abs/2603.19225) ⭐️ 8.0/10

FinTradeBench is a new benchmark comprising 1,400 questions that combine company fundamentals and trading signals to evaluate LLMs' financial reasoning over NASDAQ‑100 companies across a ten‑year historical window. By integrating both fundamental and market‑trading signals, FinTradeBench fills a critical gap in existing LLM financial‑reasoning benchmarks, enabling more realistic assessment of models used for real‑world investment decisions. The benchmark is split into fundamentals‑focused, trading‑signal‑focused, and hybrid questions, and was built using a calibration‑then‑scaling pipeline that includes expert seed questions, multi‑model generation, self‑filtering, numerical auditing, and human‑LLM judge alignment; zero‑shot and retrieval‑augmented tests show retrieval helps fundamentals but not trading‑signal reasoning.

rss · arXiv Quantitative Finance · Jun 4, 04:00

**Background**: Large Language Models (LLMs) have been increasingly applied to financial tasks such as earnings prediction and investment analysis, but their ability to reason over heterogeneous financial data remains poorly measured. Traditional financial QA benchmarks mostly test static company fundamentals extracted from filings, neglecting dynamic trading signals derived from price movements and volume. The NASDAQ‑100 index comprises 100 of the largest non‑financial companies listed on NASDAQ, providing a rich, liquid universe for studying both fundamentals and market behavior. FinTradeBench addresses this gap by coupling fundamental data with technical trading signals across a ten‑year window, offering a more comprehensive evaluation of LLM‑driven financial reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.19225">FinTradeBench : A Financial Reasoning Benchmark for LLMs</a></li>
<li><a href="https://www.emergentmind.com/topics/fintradebench">FinTradeBench : Financial Reasoning Benchmark</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#financial reasoning`, `#benchmark`, `#NASDAQ-100`, `#finance AI`

---