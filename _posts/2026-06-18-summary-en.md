---
layout: default
title: "Horizon Summary: 2026-06-18 (EN)"
date: 2026-06-18
lang: en
---

> From 46 items, 15 important content pieces were selected

---

1. [GLM-5.2 is probably the most powerful text-only open weights LLM](#item-1) ⭐️ 9.0/10
2. [Epic Games releases open-source Lore VCS for scalable game asset management](#item-2) ⭐️ 8.0/10
3. [US Science Faces Funding Crisis, Visa Hurdles, and Researcher Exodus](#item-3) ⭐️ 8.0/10
4. [Tesco Migrates 40k VMware Workloads Amid Broadcom Pricing Dispute](#item-4) ⭐️ 8.0/10
5. [Volkswagen blocks GrapheneOS users by requiring Play Protect‑certified Android app](#item-5) ⭐️ 8.0/10
6. [GLM-5.2 Becomes Leading Open Weights Model on Artificial Analysis Index](#item-6) ⭐️ 8.0/10
7. [PIVOT introduces a differentiable layer for Black-Scholes price and implied volatility.](#item-7) ⭐️ 8.0/10
8. [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](#item-8) ⭐️ 8.0/10
9. [Study Reveals Selection Bias in African and Latin American Prediction Markets](#item-9) ⭐️ 8.0/10
10. [Public transit gains and spatially uneven travel demand changes after NYC congestion pricing](#item-10) ⭐️ 8.0/10
11. [CARLOS: Deep RL Algorithm for Continuous-Time Optimal Stopping](#item-11) ⭐️ 8.0/10
12. [LLM Consumer Behavior Theory: Foundations of a Novel Research Field](#item-12) ⭐️ 8.0/10
13. [Wind generation now drives Texas day‑ahead electricity prices more than natural gas](#item-13) ⭐️ 8.0/10
14. [Non-Spanning Identification Protocol for Scheduled Event Risk in Option Pricing](#item-14) ⭐️ 8.0/10
15. [Trading Frictions in Dynamic Cap-and-Trade Markets](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM-5.2 is probably the most powerful text-only open weights LLM](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

On June 16, 2026, Z.ai released GLM-5.2, a 753‑billion‑parameter Mixture‑of‑Experts language model with text‑only input, a 1‑million‑token context window, and an MIT license, following an early release to coding plan subscribers on June 13. GLM-5.2 tops the Artificial Analysis Intelligence Index and ranks highly on coding benchmarks, demonstrating that a massive open‑weights MoE model can deliver state‑of‑the‑art performance while remaining freely usable under an MIT license, which may accelerate research and commercial adoption. The model has 753 billion total parameters but only 40 billion active parameters during inference, uses an IndexShare sparse‑attention mechanism for efficient long‑context processing, and supports a 1 million‑token context window. On benchmarks it consumes about 43 k output tokens per task, ranks #1 on the Intelligence Index v4.1 and #2 on the Code Arena WebDev leaderboard, and is offered via OpenRouter at roughly $1.40 per million input tokens and $4.40 per million output tokens.

rss · Simon Willison · Jun 17, 23:58

**Background**: Mixture‑of‑Experts (MoE) architectures allow a model to contain a vast number of total parameters while activating only a small, dynamically selected subset for each input, reducing compute cost. A 1 million‑token context window enables the model to process very long inputs such as entire codebases or lengthy documents in a single pass. Releasing model weights under an MIT license makes them freely usable, modifiable, and redistributable, encouraging widespread adoption in both academia and industry. Z.ai’s GLM series builds on earlier GLM‑5 and GLM‑5.1 models, scaling up size and context length while maintaining a text‑only focus.

<details><summary>References</summary>
<ul>
<li><a href="https://apidog.com/blog/glm-5-2-what-is/">What Is GLM - 5 . 2 ?</a></li>
<li><a href="https://medium.com/@divagr1925/breaking-the-scaling-wall-an-introduction-to-mixture-of-experts-in-llm-f8447a337a05">Breaking the Scaling Wall: An Introduction to Mixture of Experts in...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-weights`, `#Mixture-of-Experts`, `#AI research`, `#large language model`

---

<a id="item-2"></a>
## [Epic Games releases open-source Lore VCS for scalable game asset management](https://lore.org/) ⭐️ 8.0/10

Epic Games has announced Lore, an open-source version control system built for scalability and designed to handle large binary assets in game development, positioning it as a Perforce alternative. Lore addresses a long-standing need in game studios for a version control system that efficiently manages massive art, model, and audio files, potentially reducing reliance on proprietary Perforce licenses. Lore supports arbitrary content types, multi-axis scaling, multi-tenant safety, and a public versioned specification under a permissive open-source license, though the UEFN build currently uses a proprietary compression format not yet available in the open source release.

hackernews · regnerba · Jun 17, 14:30 · [Discussion](https://news.ycombinator.com/item?id=48571081)

**Background**: In game development, teams collaborate on large binary files such as textures, 3D models, and audio, which traditional text-oriented systems like Git handle poorly without extensions like Git LFS. Perforce (Helix Core) has been the industry standard for these workloads due to its support for large files, file locking, and fine-grained permissions, but it is proprietary and can be costly. Lore aims to provide an open-source alternative that combines Perforce’s scalability for binary assets with a permissive license and modern design.

<details><summary>References</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open-Source Version Control System</a></li>
<li><a href="https://www.perforce.com/blog/vcs/version-control-for-binary-files">Version Control for Binary Files: Manage Large ... | Perforce Software</a></li>

</ul>
</details>

**Discussion**: Commenters emphasized that Lore is not meant to compete with Git for general software development but to challenge Perforce in game development workflows. Several noted its potential to improve artist workflows through file locking and efficient handling of large binary assets, while others pointed out that Perforce remains entrenched due to familiarity and tooling. Some also remarked on Git’s UI verbosity and expressed hope that Lore could offer a simpler experience.

**Tags**: `#version-control`, `#game-development`, `#open-source`, `#scalability`, `#Perforce-alternative`

---

<a id="item-3"></a>
## [US Science Faces Funding Crisis, Visa Hurdles, and Researcher Exodus](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 8.0/10

The Scientific American article argues that the historic compact between US science and politics has broken down, resulting in severe funding shortages, stricter visa rules for foreign researchers, and a growing exodus of scientists leaving the country. This breakdown threatens America’s leadership in global research, risks a brain drain that could shift innovation elsewhere, and undermines the collaborative nature of science that depends on stable funding and open international exchange. Policymakers and institutions must address these issues to preserve the nation’s scientific capacity. Commenters describe concrete impacts: an optical‑trap specialist considering emigration after crying over funding stress, professors unable to hire foreign graduate students due to visa restrictions, and widespread anxiety that government decisions have become politicized, prompting some to contemplate leaving science altogether. These personal anecdotes illustrate systemic strain on the research ecosystem.

hackernews · presspot · Jun 17, 09:54 · [Discussion](https://news.ycombinator.com/item?id=48568058)

**Background**: The United States has long relied on a partnership between federal science agencies (such as the NIH and NSF) and private philanthropy to fund basic research, while also attracting global talent through visas like the H‑1B and J‑1. After World War II, this compact helped drive postwar innovation and economic growth. In recent years, increasing political polarization and debates over issues such as climate change and public health have strained that relationship, leading to budget uncertainties and stricter immigration scrutiny.

**Discussion**: Commenters express frustration and personal distress over funding cuts and visa hurdles, with many describing colleagues leaving or considering relocation abroad. Some note the politicization of scientific issues, while a few nostalgically propose recreating institutions like Bell Labs to revive research.

**Tags**: `#science policy`, `#research funding`, `#academia`, `#US science`, `#visa restrictions`

---

<a id="item-4"></a>
## [Tesco Migrates 40k VMware Workloads Amid Broadcom Pricing Dispute](https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/) ⭐️ 8.0/10

Tesco is migrating approximately 40,000 server workloads from VMware infrastructure to alternative virtualization platforms after Broadcom ended support and raised prices. This large-scale move underscores growing enterprise pushback against vendor lock‑in and costly licensing changes following Broadcom’s acquisition of VMware, signaling a shift toward more flexible, cost‑effective infrastructure. Tesco reported that Broadcom stopped supporting its VMware products in January 2026, forcing the retailer to pay for third‑party support and sue Broadcom in the UK High Court for alleged abusive conduct.

hackernews · Bender · Jun 17, 21:00 · [Discussion](https://news.ycombinator.com/item?id=48576838)

**Background**: VMware provides virtualization software that allows enterprises to run multiple workloads on shared servers, reducing hardware dependency. After Broadcom acquired VMware in 2023, it revised licensing and support policies, leading to steep price increases and reduced support for existing customers. Enterprises often respond by migrating workloads to alternative platforms or public cloud to avoid vendor lock‑in and control costs.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/">Tesco moving 40,000 server workloads off VMware ... - Ars Technica</a></li>
<li><a href="https://nsaneforums.com/news/software-news/300-percent-price-hikes-push-disgruntled-vmware-customers-toward-broadcom-rivals-r26310/">300 percent price hikes push disgruntled VMware ... - Nsane Forums</a></li>
<li><a href="https://slashdot.org/story/24/10/01/216232/att-claims-vmware-by-broadcom-offered-it-a-1050-price-increase">AT&T Claims VMware By Broadcom Offered It a 1,050% Price ...</a></li>

</ul>
</details>

**Discussion**: Commenters highlight Broadcom's aggressive pricing tactics, mention alternatives such as Proxmox, and note migration challenges with backup software compatibility, while many agree that similar experiences are widespread among VMware customers.

**Tags**: `#VMware`, `#Broadcom`, `#enterprise IT`, `#virtualization`, `#cloud migration`

---

<a id="item-5"></a>
## [Volkswagen blocks GrapheneOS users by requiring Play Protect‑certified Android app](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3) ⭐️ 8.0/10

Volkswagen updated its vehicle app to require Play Protect‑certified Android devices, effectively blocking users of the privacy‑focused GrapheneOS operating system. This move deprives privacy‑conscious Android users of access to vehicle functions such as remote climate control and charging, highlighting growing corporate control over device compatibility and raising concerns about user rights. The app now relies on Play Protect certification, which GrapheneOS devices fail because they do not pass SafetyNet attestation; consequently, community‑driven integrations and third‑party tools that used Volkswagen’s API are no longer functional.

hackernews · microtonal · Jun 17, 15:04 · [Discussion](https://news.ycombinator.com/item?id=48571526)

**Background**: GrapheneOS is a privacy‑focused, hardened fork of Android that omits Google Play services and often fails Google’s SafetyNet/Play Protect checks. Play Protect certification is Google’s program that verifies a device has passed Android compatibility testing and includes licensed Google apps; only certified devices can access certain APIs. SafetyNet attestation (now part of the Play Integrity API) checks device integrity to detect custom ROMs, rooting, or tampering, which causes non‑certified ROMs like GrapheneOS to be blocked.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/googleplay/answer/7165974?hl=en">Check & fix Play Protect certification status - Google Play Help</a></li>
<li><a href="https://www.android.com/certified/">Android – Certified</a></li>

</ul>
</details>

**Discussion**: Commenters expressed disappointment and criticism toward Volkswagen for limiting privacy‑oriented options, with some saying they would reconsider buying a VW vehicle. Others noted the official app is ad‑heavy and preferred using alternatives like Home Assistant for vehicle controls.

**Tags**: `#Volkswagen`, `#GrapheneOS`, `#Android`, `#privacy`, `#automotive API`

---

<a id="item-6"></a>
## [GLM-5.2 Becomes Leading Open Weights Model on Artificial Analysis Index](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) ⭐️ 8.0/10

GLM-5.2 has reached the top of the Artificial Analysis Intelligence Index as the leading open weights model, marking a new milestone for the GLM series. The model was released recently and demonstrates strong capabilities in long-horizon tasks and coding. Its top ranking shows that open-weight models can now rival proprietary systems in reasoning and coding, offering a cost-effective alternative for developers and researchers. This shift could accelerate adoption of open LLMs in real-world software engineering. GLM-5.2 supports a 1M-token context window, excels in long-horizon agentic workflows, and is available on Hugging Face under the zai-org/GLM-5.2 repository. Users have reported high reasoning token consumption and slower response times for coding tasks compared with some alternatives.

hackernews · himata4113 · Jun 17, 09:12 · [Discussion](https://news.ycombinator.com/item?id=48567759)

**Background**: The Artificial Analysis Intelligence Index is a composite benchmark that evaluates language models across reasoning, coding, knowledge, instruction following, scientific reasoning, and multi-step task completion. Open weights models are those whose parameters are publicly available, allowing anyone to use, fine-tune, or deploy them without relying on proprietary APIs. GLM-5.2 is part of Zhipu AI’s GLM series, which focuses on agentic software engineering and long-horizon tasks rather than pure chatbot behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM-5.2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters praised GLM-5.2’s strong performance and low cost, noting that some providers offer it at unlimited tokens for $50 per month, far cheaper than proprietary APIs. However, several users observed that the model spends excessive time and tokens on reasoning—e.g., over 15 minutes and 45k tokens for a small coding task—making it slower than alternatives like Codex 5.5 or Composer 2.5.

**Tags**: `#LLM`, `#open weights`, `#GLM-5.2`, `#Artificial Analysis`, `#AI benchmark`

---

<a id="item-7"></a>
## [PIVOT introduces a differentiable layer for Black-Scholes price and implied volatility.](https://arxiv.org/abs/2606.17065) ⭐️ 8.0/10

The paper introduces PIVOT, a differentiable translator that preserves the efficient LBR solver’s forward pass while computing gradients via implicit differentiation through the Black-Scholes price map, explicitly handling the low‑vega singularity. By providing a gradient‑compatible interface between price and implied volatility spaces, PIVOT enables machine‑learning models to directly optimize option‑pricing objectives, improving calibration accuracy and unlocking end‑to‑end differentiable pipelines in quantitative finance. PIVOT uses implicit differentiation on the smooth Black‑Scholes/Black‑76 price map, applies a gating contract that returns NaN for invalid domains, passes the exact 1/vega gradient for well‑conditioned rows, and attenuates low‑vega rows; a fused Triton kernel achieves 1.79 × 10⁹ implied‑volatility evaluations per second on an H100 with a max relative error of 9.3 × 10⁻¹⁴ versus the reference C solver.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: The Black‑Scholes model maps option prices to implied volatility, a transformation that is monotonic but lacks a closed‑form inverse, requiring numerical solvers such as Jäckel’s 'Let’s Be Rational' (LBR) algorithm. While LBR provides machine‑precision inversion efficiently, its forward pass contains branching logic that is not amenable to automatic differentiation, creating a bottleneck for gradient‑based learning. In the low‑vega regime the inverse map becomes singular, causing the gradient 1/vega to diverge, which must be handled explicitly to avoid numerical instability. PIVOT bridges this gap by keeping the LBR forward pass intact and supplying gradients via implicit differentiation, with a gating mechanism that treats singular regions appropriately.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.17065">PIVOT: Bridging Black - Scholes Implied-Volatility and Price Objectives...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Differentiation_rules">Differentiation rules - Wikipedia</a></li>
<li><a href="https://quant.stackexchange.com/questions/27603/understanding-vega-calculation-in-black-scholes-model">Understanding Vega calculation in black Scholes model - Quantitative...</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#option pricing`, `#differentiable programming`, `#Black-Scholes`, `#machine learning`

---

<a id="item-8"></a>
## [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](https://arxiv.org/abs/2606.17383) ⭐️ 8.0/10

The paper proposes a POMDP-based framework to independently validate belief states, forecasts, and policies of agentic AI systems, formalizing large language models as approximate Bayesian filtering operators. It demonstrates the approach with a portfolio‑management case study involving latent market regime inference and Black‑Litterman portfolio construction. This work fills a critical gap in model risk management for autonomous agents by providing a rigorous, component‑wise validation methodology that can improve AI safety, governance, and monitoring. Its impact extends to industries relying on autonomous decision‑making, such as finance, healthcare, and robotics. The framework decomposes autonomous decision making into information, beliefs, forecasts, actions, and utility, allowing each to be validated separately; LLMs are modeled as approximate Bayesian filtering operators. A taxonomy of risks covers state‑space, filtering, forecast, policy, utility‑specification, and parameter risks, validated via belief calibration diagnostics, coverage tests, ablation studies, and parameter‑sensitivity analysis.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: A partially observable Markov decision process (POMDP) extends a Markov decision process to model agents that cannot directly observe the underlying state, requiring them to maintain beliefs about hidden conditions. Agentic AI systems continuously acquire information, form beliefs about latent environmental states, generate forecasts, select actions, and adapt over time, which traditional predictive accuracy validation fails to assess. By treating large language models as approximate Bayesian filters, the paper provides a principled way to estimate hidden states from noisy observations. The proposed POMDP‑based validation framework thus enables rigorous evaluation of belief quality, forecast reliability, and policy robustness in autonomous AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process">Partially observable Markov decision process - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/partially-observable-markov-decision-process-pomdp-in-ai/">Partially Observable Markov Decision Process (POMDP) in AI - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#Agentic AI`, `#POMDP`, `#Model Validation`, `#Large Language Models`, `#Reinforcement Learning`

---

<a id="item-9"></a>
## [Study Reveals Selection Bias in African and Latin American Prediction Markets](https://arxiv.org/abs/2606.17503) ⭐️ 8.0/10

The paper introduces a coded measure of settlement legibility and applies it to an audited dataset of 6,047 Africa- and Latin America-topic contracts on Polymarket and Kalshi. It finds that market formation is selective, with African contracts overwhelmingly about football and Latin American contracts dominated by Venezuela-related civic events. The results show that prediction‑market inventories reflect what platforms can settle rather than what the public cares about, warning researchers and policymakers not to conflate market activity with public interest. This insight helps improve the design and interpretation of prediction markets in diverse regions. The settlement legibility metric achieved inter‑rater reliabilities of 0.92 and 0.96 on its primary dimensions and blind human benchmark scores of 0.97 and 0.92. Legibility ranks sports and elections highest and conflict lowest, and among listed contracts higher legibility is negatively correlated with trading value.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: Prediction markets allow participants to trade contracts that pay out based on the outcome of future events, aggregating beliefs into prices. Settlement legibility refers to how clearly an uncertainty can be described, sourced, and resolved by a third party, which determines whether a contract can be listed. Polymarket and Kalshi are two major platforms that host such contracts globally, often with low fees and minimal KYC requirements. Focusing on Africa and Latin America highlights regional differences in what kinds of uncertainties become tradable.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.17503">[2606.17503] What Prediction Markets Can See: Market Formation, Settlement Legibility, and the Geography of Tradable Uncertainty in Africa and Latin America</a></li>
<li><a href="https://polymarket.com/">Polymarket | The World's Largest Prediction Market</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-04-09/how-prediction-markets-are-blurring-the-line-between-trading-and-betting?trk=article-ssr-frontend-pulse_little-text-block">How Prediction Markets Are Blurring the Line Between... - Bloomberg</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#settlement legibility`, `#market formation`, `#Africa`, `#Latin America`

---

<a id="item-10"></a>
## [Public transit gains and spatially uneven travel demand changes after NYC congestion pricing](https://arxiv.org/abs/2606.17530) ⭐️ 8.0/10

The study finds that NYC's congestion pricing increased bus and subway ridership while modestly reducing overall travel demand, with effects varying across space and demographics. It provides empirical evidence on the effectiveness of congestion pricing, reveals spatial heterogeneity in impacts, and offers a valuable case for urban transportation planning and AI/ML‑based policy evaluation. Using time series foundation models to generate probabilistic counterfactual demand forecasts, the authors analyzed bus, subway, and aggregate trip data, finding significant post‑policy ridership gains, a modest overall demand reduction concentrated in the Congestion Relief Zone, transit gains extending beyond Manhattan’s core, and uneven socio‑demographic adaptation across neighborhoods.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: Congestion pricing charges vehicles for entering a designated cordon area to reduce traffic and encourage public transit use. Time series foundation models are large pretrained models that can forecast new series without retraining, enabling zero‑shot predictions. Probabilistic counterfactual forecasting generates a distribution of what demand would have been without the policy, allowing uncertainty‑aware causal inference. Together, these methods let researchers evaluate city‑wide interventions when proper control groups are unavailable.

<details><summary>References</summary>
<ul>
<li><a href="https://jscastanoc.github.io/blog/foundation-models-for-time-series/">Foundation Models for Time Series —A Case Study Using Brain...</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/10962247.2022.2100510">Full article: Cordon screen: A cordon - based congestion pricing ...</a></li>
<li><a href="https://scispace.com/pdf/causal-effect-estimation-with-global-probabilistic-1ozepqd9.pdf">Causal Effect Estimation with Global Probabilistic</a></li>

</ul>
</details>

**Tags**: `#congestion pricing`, `#urban mobility`, `#public transit`, `#time series forecasting`, `#policy evaluation`

---

<a id="item-11"></a>
## [CARLOS: Deep RL Algorithm for Continuous-Time Optimal Stopping](https://arxiv.org/abs/2606.17545) ⭐️ 8.0/10

The paper introduces CARLOS, an adaptive deep reinforcement learning algorithm that learns optimal stopping policies in continuous time by refining a joint space‑time decision boundary across progressively finer time grids. By removing the need for coarse discretization, CARLOS can achieve higher exercise prices than traditional Bermudan solvers and approach the American option upper bound, offering a more accurate and efficient tool for finance and operations research. CARLOS employs an aggregate deep neural network (ADNN) to represent the stopping boundary, starts from a coarse time grid and iteratively refines the grid while training the ADNN, and uses an adaptive sampling strategy that concentrates training samples near the learned boundary.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: Optimal stopping problems require deciding the best time to take an action to maximize expected reward, commonly encountered in pricing American‑style options. Traditional numerical methods discretize time, where a coarse grid can undervalue the option and a fine grid introduces backward‑recursion errors. Reinforcement learning offers a simulation‑based alternative that can learn policies directly from sampled paths without explicit discretization. The aggregate deep neural network in CARLOS jointly models the dependence of the stopping decision on both state and time, enabling learning at arbitrarily fine resolution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.17545">[2606.17545] Continuous-time Optimal Stopping through Deep ...</a></li>
<li><a href="https://www.columbia.edu/~xz2574/download/DSXZ2.pdf">Learning to Optimally Stop Diffusion Processes, with</a></li>

</ul>
</details>

**Tags**: `#optimal stopping`, `#reinforcement learning`, `#deep learning`, `#stochastic control`, `#finance`

---

<a id="item-12"></a>
## [LLM Consumer Behavior Theory: Foundations of a Novel Research Field](https://arxiv.org/abs/2606.18005) ⭐️ 8.0/10

The paper introduces LLM Consumer Behavior Theory, a new interdisciplinary framework that formalizes how large language model‑based agents reflect human preferences and how their individual decisions aggregate into market demand in agentic markets. By linking LLMs, agentic decision‑making, and classical/behavioral economics, the theory creates a unified lens for studying AI‑driven markets and highlights where traditional economic assumptions may break down, offering a fresh research agenda for both AI and economics. The work draws on NLP advances and economic models to describe preference representation, alignment challenges, and heterogeneity in LLM agents, while noting that assumptions such as rationality may fail; it does not provide empirical validation but outlines open questions in alignment, preference elicitation, and market dynamics.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: Large language models are increasingly used as autonomous agents that make purchasing decisions on behalf of users, shifting the traditional focus of consumer theory from human decision‑makers to AI‑driven agents. Consumer theory classically studies how individuals allocate limited resources to maximize utility based on preferences and constraints. Agentic markets replace direct human‑to‑human exchanges with buyer‑ and seller‑side software agents that interact autonomously, creating new market dynamics that require updated theoretical frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/agentic-markets">Agentic Markets : Autonomous Economic Platforms</a></li>
<li><a href="https://www.investopedia.com/terms/c/consumer-theory.asp">investopedia.com/terms/c/ consumer - theory .asp</a></li>
<li><a href="https://blog.synapticlabs.ai/eliciting-human-preferences-with-language-models">Eliciting Human Preferences with Language Models</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#consumer behavior`, `#agentic markets`, `#theoretical economics`, `#NLP`

---

<a id="item-13"></a>
## [Wind generation now drives Texas day‑ahead electricity prices more than natural gas](https://arxiv.org/abs/2604.14257) ⭐️ 8.0/10

Using causal discovery methods, researchers found that wind generation has become the dominant driver of Texas day‑ahead electricity prices, with an effect more than three times stronger than that of natural gas, though its price‑suppressing effect weakens during peak periods and shifts congestion costs. The findings challenge the long‑held view of Texas as a gas‑price‑driven market, highlighting the need for planners and investors to account for wind’s growing influence and its spatial‑temporal effects on price risks and infrastructure needs. The study analyzed wholesale electricity prices in ERCOT using causal discovery algorithms (e.g., GES, PC, LiNGAM) on time‑series data, revealing that wind’s causal impact exceeds three times that of natural gas while noting increased congestion costs in distant load centers due to wind growth.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: ERCOT operates the day‑ahead and real‑time electricity markets for most of Texas, where prices are set through auctions that reflect generation offers, load demand, and transmission constraints. Rapid growth of wind and solar, alongside rising electrification and data‑center loads, is altering the traditional price formation that once relied heavily on natural‑gas‑fired generators. Causal discovery techniques such as the Greedy Equivalence Search (GES) algorithm infer directional relationships from observational data, helping to distinguish true drivers from mere correlations. Transmission congestion occurs when power flows exceed line limits, causing redispatch and additional costs that are shifted to distant load centers.

<details><summary>References</summary>
<ul>
<li><a href="https://modoenergy.com/research/jp/ercot-energy-academy-power-markets-real-time-day-ahead-sced-ordc-qse-lse-ancillary-services-price-adders-system-lamdba-locational-marginal-prices">ERCOT : The Energy Academy - How do power markets in Texas work?</a></li>
<li><a href="https://www.pywhy.org/dowhy/v0.10/example_notebooks/dowhy_causal_discovery_example.html">Causal Discovery example — DoWhy documentation</a></li>
<li><a href="https://www.utilitydive.com/news/grid-congestion-costs-transmission-gets-grid-strategies-report/687309/">US grid congestion costs jumped 56% to $20.8B in 2022... | Utility Dive</a></li>

</ul>
</details>

**Tags**: `#electricity markets`, `#causal discovery`, `#renewable energy`, `#Texas power grid`, `#price formation`

---

<a id="item-14"></a>
## [Non-Spanning Identification Protocol for Scheduled Event Risk in Option Pricing](https://arxiv.org/abs/2606.12872) ⭐️ 8.0/10

The paper introduces a non-spanning identification protocol that models FOMC, CPI, and NFP announcements as deterministic-time jumps in risk-neutral option pricing, using non-spanning expiries to estimate the no-event volatility surface and event-spanning quotes to calibrate the scheduled jump, validated on SPX options from May 2022 to August 2025. By cleanly separating scheduled macro‑announcement jump risk from the continuous volatility surface, the protocol improves the accuracy of short‑dated option pricing and provides a clearer signal for risk management and model calibration in quantitative finance. Empirical results show Gaussian and two‑component mixture jumps reduce held‑out pricing errors most notably for straddles and strangles, while a contaminated‑surface stress test confirms that allowing event‑spanning quotes into the no‑event fit absorbs jump premia rather than identifying them; an amortized MDN benchmark indicates limited cross‑event transfer, with strongest identification for CPI and FOMC and weaker for NFP.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: In option pricing, scheduled macro‑announcements such as FOMC meetings, CPI releases, and NFP reports can cause abrupt jumps in asset prices at known times. Traders often infer this risk from the volatility surface, but a surface fitted using quotes that span the event can absorb the jump premium, making the jump component unidentified. The paper addresses this identification problem by proposing a protocol that uses non‑spanning expiries to isolate the underlying no‑event surface.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12872">Non-Spanning Identification of Scheduled Event Risk in Option Pricing</a></li>

</ul>
</details>

**Tags**: `#option pricing`, `#quantitative finance`, `#jump diffusion`, `#event risk`, `#volatility surface`

---

<a id="item-15"></a>
## [Trading Frictions in Dynamic Cap-and-Trade Markets](https://arxiv.org/abs/2606.03767) ⭐️ 8.0/10

The paper introduces a dynamic stochastic model of cap-and-trade markets that incorporates slow participation, limited intermediation, and heterogeneous information, derives closed-form expressions for equilibrium market access and the surrender‑month premium, and tests the model using 2.7 million EU ETS transactions from 2005‑2021. By integrating multiple frictions into a unified framework and providing both analytical and empirical validation, the study offers new insights into how market imperfections affect price formation and the effectiveness of emissions trading schemes, which is valuable for policymakers designing or refining carbon markets. The model yields closed‑form access choices, proves a unique equilibrium premium, shows that endogenous access dampens the price response to each friction in isolation while their interaction can be non‑additive and amplify price movements; empirically, about 40 % of operators do not trade each year, trading peaks in April with systematically high returns, and operator flow predicts future returns.

rss · arXiv Quantitative Finance · Jun 17, 04:00

**Background**: Cap‑and‑trade (or emissions trading) is a market‑based policy that sets a limit on total pollution and allows firms to buy and sell allowances, creating a price for emissions. The EU ETS is the world’s largest such system, covering power plants, factories and, since 2024, maritime transport, with compliance periods ending each April. Trading frictions such as slow participation (delayed market entry), limited intermediation (constraints on brokers or intermediaries), and heterogeneous information (different beliefs about future prices) can distort the allowance price and reduce the market’s ability to correct the externality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.03767">[2606.03767] Trading Frictions in Dynamic Cap - and - Trade Markets</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Union_Emissions_Trading_System">European Union Emissions Trading System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emissions_trading">Emissions trading - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#cap-and-trade`, `#environmental economics`, `#market frictions`, `#stochastic modeling`, `#EU ETS`

---