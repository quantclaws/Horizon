---
layout: default
title: "Horizon Summary: 2026-07-15 (EN)"
date: 2026-07-15
lang: en
---

> From 69 items, 18 important content pieces were selected

---

1. [Bonsai 27B: First 27B-parameter model runs on a smartphone](#item-1) ⭐️ 9.0/10
2. [Essay warns AI agents cause ever‑growing software complexity](#item-2) ⭐️ 8.0/10
3. [Cursor Zero‑Day Allows Arbitrary Code Execution via Malicious git.exe](#item-3) ⭐️ 8.0/10
4. [Are we offloading too much of our thinking to AI?](#item-4) ⭐️ 8.0/10
5. [An Extreme Value Perspective on Learning Stress Laws](#item-5) ⭐️ 8.0/10
6. [Simple Diagnostic Criterion for Naive Diversification Optimality](#item-6) ⭐️ 8.0/10
7. [Explicit Construction of Arbitrage-Free Multi-Maturity Risk-Neutral Marginals](#item-7) ⭐️ 8.0/10
8. [Study Finds No Short-Run Liquidity Response to Uniswap Protocol-Fee Cuts](#item-8) ⭐️ 8.0/10
9. [Learned Predictive Ambiguity Sets Enhance Decision-Focused DRO.](#item-9) ⭐️ 8.0/10
10. [Diachronic Sample Integration Improves Tail-Risk Estimation for Generative Models](#item-10) ⭐️ 8.0/10
11. [Paid Mobile Ads Boost Organic Installs via App Store Rankings](#item-11) ⭐️ 8.0/10
12. [Neural-Network Surrogate Speeds Catastrophe Bond Valuation to Milliseconds.](#item-12) ⭐️ 8.0/10
13. [LLM-built database reveals bank runs in weak and strong banks.](#item-13) ⭐️ 8.0/10
14. [Differential ML for 0DTE Options with Stochastic Volatility and Jumps](#item-14) ⭐️ 8.0/10
15. [AI productivity gains affect wages and optimal policies reduce inequality.](#item-15) ⭐️ 8.0/10
16. [Authors introduce a structural volatility model for binary prediction markets.](#item-16) ⭐️ 8.0/10
17. [Study Finds LLMs Show Ideological Bias in Economic Causal Reasoning](#item-17) ⭐️ 8.0/10
18. [The Benchmark Ceiling: Human Judgment Limits AI Evaluation as Models Improve](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bonsai 27B: First 27B-parameter model runs on a smartphone](https://prismml.com/news/bonsai-27b) ⭐️ 9.0/10

PrismML announced Bonsai 27B, a 27-billion-parameter multimodal model based on Qwen3.6 that uses aggressive 1-bit or ternary quantization to shrink the model to under 4 GB, enabling it to run on a smartphone. This achievement pushes the frontier of on-device AI by bringing near-frontier language and vision capabilities to mobile devices, potentially reshaping how developers deploy large models and prompting interest from major platform holders such as Apple. Bonsai 27B keeps the language weights of Qwen3.6 in end-to-end 1-bit (3.9 GB, 89.5% FP16 retention) or ternary (5.9 GB, 94.6% FP16 retention) formats, while its vision tower remains at 4-bit; conventional sub-4-bit quantizations reportedly lose accuracy on AIME, LiveCodeBench and agentic tasks.

hackernews · xenova · Jul 14, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48910545)

**Background**: Model quantization reduces the numerical precision of neural-network weights to cut memory and compute requirements, with extreme methods such as 1-bit or ternary representation pushing compression far beyond typical 4-bit schemes. Large language models like Qwen3.6-27B normally occupy tens of gigabytes in full precision, exceeding the unified memory budget of current smartphones. Prior work showed that aggressive quantization can preserve useful language ability, but often struggles on complex reasoning or agentic benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-27b">PrismML — Announcing Bonsai 27B: The First 27B-Class Model to ...</a></li>
<li><a href="https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/">PrismML Releases Bonsai 27B: 1-bit and Ternary Builds of ...</a></li>
<li><a href="https://cryptobriefing.com/apple-evaluates-prismml-ai-compression-iphones/">Apple evaluates PrismML for AI model compression on iPhones</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the model's size and potential, with SwellJoe comparing it favorably to Gemma 4 12B QAT and questioning performance loss per quantization step. Others sought clarification on the quantization process, noted Apple's reported interest, reported difficulties running the GGUF/MLX versions in LM Studio, and pointed out factual errors in the demo's cooking example. Overall sentiment is enthusiastic but tempered by skepticism about real-world accuracy and tool-calling performance.

**Tags**: `#large language models`, `#model quantization`, `#edge AI`, `#mobile AI`, `#Hugging Face`

---

<a id="item-2"></a>
## [Essay warns AI agents cause ever‑growing software complexity](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) ⭐️ 8.0/10

The essay argues that reliance on AI agents and incremental prompting leads to ever‑growing software complexity, likening development to a tower that keeps rising without solid foundations.

hackernews · cdrnsf · Jul 14, 16:57 · [Discussion](https://news.ycombinator.com/item?id=48909785)

**Tags**: `#software-engineering`, `#AI-agents`, `#composability`, `#architecture`, `#Lisp-curse`

---

<a id="item-3"></a>
## [Cursor Zero‑Day Allows Arbitrary Code Execution via Malicious git.exe](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) ⭐️ 8.0/10

Researchers disclosed a zero‑day vulnerability in Cursor where placing a malicious git.exe in a user's code folder lets attackers run arbitrary executables when the editor invokes Git; the issue was reported to Cursor in December 2025 and remained unpatched for over six months despite multiple reports. The vulnerability affects a widely used AI‑powered code editor, enabling silent code execution that could lead to supply‑chain attacks or ransomware deployment; it also highlights the risks of ignored responsible disclosure in popular developer tools. The exploit relies on Windows’ default behavior of searching the current directory before the PATH variable, allowing a malicious git.exe placed in the project folder to be executed when Cursor invokes Git; no user interaction is required beyond opening a repository.

hackernews · Synthetic7346 · Jul 14, 17:58 · [Discussion](https://news.ycombinator.com/item?id=48910676)

**Background**: Cursor is an AI‑driven code editor developed by Anysphere that integrates natural‑language coding assistance with standard development workflows, including Git integration. On Windows, when a program calls an executable without a full path, the operating system searches the current working directory first, a behavior that can be abused via DLL or executable hijacking. Responsible disclosure is a security practice where researchers privately notify vendors before public release, giving them time to patch.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>
<li><a href="https://github.com/InfoSecWarrior/Offensive-Linux-Privilege-Escalation/blob/main/Escalate-via-path-hijacking.md">Offensive-Linux-Privilege-Escalation/Escalate-via-path ...</a></li>
<li><a href="https://byteiota.com/cursor-ide-rce-unpatched-git-exe/">Cursor IDE RCE: Unpatched git.exe Flaw Goes Public | byteiota</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the flaw is a Cursor bug or a Windows PATH quirk, with some noting that exploitation requires placing a malicious git.exe in the victim’s code folder, while others criticized the vendor’s months‑long silence after responsible disclosure. Several users pointed out that Windows security prompts might block unsigned executables, but agreed that the lack of response from Cursor is concerning.

**Tags**: `#security`, `#vulnerability`, `#Cursor`, `#zero-day`, `#responsible disclosure`

---

<a id="item-4"></a>
## [Are we offloading too much of our thinking to AI?](https://www.artfish.ai/p/offloading-thinking-to-ai) ⭐️ 8.0/10

A Hacker News thread garnered 383 points and 387 comments debating whether excessive reliance on AI for thinking risks cognitive atrophy, weighing AI assistance benefits against the need or deep understanding. The discussion highlights growing concerns that AI‑driven cognitive offloading may erode foundational skills, affecting software engineers, learners, and professionals who must balance automation with deep expertise. Commenters compared AI use to calculators, warned that junior developers could not explain AI‑generated code, and argued that over‑reliance fosters laziness and undermines manual reading or documentation.

hackernews · yenniejun111 · Jul 14, 15:18 · [Discussion](https://news.ycombinator.com/item?id=48908178)

**Background**: Cognitive offloading refers to the practice of using external tools—such as calculators or AI—to reduce mental workload, a concept studied in cognitive science to manage limited working memory. Large language models (LLMs) are deep‑learning neural networks trained on vast text corpora, enabling them to generate, summarize, and answer questions across many domains. Human‑AI interaction examines how people collaborate with AI systems, focusing on user experience, psychological effects, and the design of AI‑assisted workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://evidencebased.education/resource/cognitive-offloading-what-is-it-and-why-is-it-important-2/">Cognitive Offloading: What is it and why is it important?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human–AI_interaction">Human–AI interaction - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a split view, with some defending AI as a productivity booster akin to calculators, while others warned that excessive reliance leads to cognitive atrophy, laziness, and an inability to explain AI‑generated work. Several participants advocated for maintaining deep technical knowledge to stay effective and to use AI more skillfully.

**Tags**: `#AI`, `#cognitive offloading`, `#software engineering`, `#LLM`, `#human-AI interaction`

---

<a id="item-5"></a>
## [An Extreme Value Perspective on Learning Stress Laws](https://arxiv.org/abs/2607.10700) ⭐️ 8.0/10

The paper introduces Self-Similar Generative Estimation (SS-GEN), a method that simulates multivariate tail events and estimates rare-event probabilities using deep generative models. SS-GEN leverages asymptotic tail structure to split the tail into an explicit radial component and a nonparametric angular component, enabling standard generative models to produce extreme samples beyond observed data. By combining extreme value theory with deep generative models, SS-GEN provides theoretical guarantees and practical utility for risk modeling and machine learning, allowing accurate probability estimation far beyond the data range. This advances the state‑of‑the‑art in rare‑event simulation and stress testing across finance, engineering, and environmental sciences. SS-GEN decomposes the tail distribution into a radial component (explicit) and an angular component (nonparametric), reducing tail learning to a compact‑domain problem solvable by off‑the‑shelf deep generative models. Under mild nonparametric tail assumptions, the SS‑GEN density is asymptotically exact in the tail, with vanishing uniform relative error for regularly varying distributions and vanishing uniform log‑relative error for Weibull‑type distributions.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Extreme value theory (EVT) studies the statistical behavior of the tails of probability distributions, providing tools to model rare, extreme events. Rare‑event simulation aims to estimate probabilities of outcomes that occur far outside the range of observed data, which is challenging due to data scarcity. Deep generative models such as GANs, VAEs, and normalizing flows can learn complex data distributions and generate synthetic samples. By integrating EVT with these models, researchers can leverage theoretical tail structure to guide the generation of realistic extreme scenarios.

**Tags**: `#extreme value theory`, `#rare event simulation`, `#deep generative models`, `#multivariate tail analysis`, `#stress testing`

---

<a id="item-6"></a>
## [Simple Diagnostic Criterion for Naive Diversification Optimality](https://arxiv.org/abs/2607.11054) ⭐️ 8.0/10

The paper introduces a simple, testable condition called the Golden Criterion that determines when naive (equal‑weight) diversification is minimum‑variance optimal, and proposes an adaptive two‑stage strategy that blends naive and optimized weights based on the empirical distance from this condition. Applied to U.S. equity premium forecasting, the method yields consistent out‑of‑sample improvements in forecast accuracy, utility, and Sharpe ratios. By resolving a long‑standing puzzle in portfolio theory, the work offers a practical, horizon‑dependent rule for when to trust naive diversification versus sophisticated optimization, with clear implications for financial machine learning and asset management. The Golden Criterion states that equal weighting is minimum‑variance optimal when the forecast‑error covariance matrix has a uniform eigenstructure; the adaptive strategy measures the empirical distance from this condition to dynamically blend naive and optimized weights, delivering improved forecast accuracy, utility, and Sharpe ratios across investment horizons.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Naive diversification (equal weighting (equal‑equal weighting‑is a simple portfolio construction rule that often performs well despite ignoring asset covariances. Traditional mean‑variance optimization relies on accurate estimates of the forecast‑error covariance matrix, which can be noisy and unstable. The paper shows that when this matrix exhibits a uniform eigenstructure—meaning its eigenvalues are equal and its eigenvectors span the space—equal weighting becomes the minimum‑variance solution. This insight links portfolio theory, statistical estimation, and eigenanalysis, providing a testable condition for when the naive approach is optimal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Portfolio_optimization">Portfolio optimization - Wikipedia</a></li>
<li><a href="https://medium.com/@bauermartin101/the-golden-middle-how-new-research-bridges-naïve-and-optimal-investing-7628148cb830">The Golden Middle: How New Research Bridges Naïve and Optimal Investing | by Martin Bauer | Oct, 2025 | Medium</a></li>
<li><a href="https://ieeexplore.ieee.org/document/317861">Eigenstructure techniques for 2-D angle estimation with ...</a></li>

</ul>
</details>

**Tags**: `#portfolio optimization`, `#naive diversification`, `#financial machine learning`, `#Sharpe ratio`, `#covariance matrix`

---

<a id="item-7"></a>
## [Explicit Construction of Arbitrage-Free Multi-Maturity Risk-Neutral Marginals](https://arxiv.org/abs/2607.06204) ⭐️ 8.0/10

The paper proposes an explicit method to derive arbitrage-free risk-neutral marginals from discrete option prices by assigning probability mass interval by interval to match observed strikes and appending closed-form power-law tails outside the observed range. It closes the gap between raw option prices and downstream quantitative finance tools such as martingale optimal transport, Bass local‑volatility calibration, scenario analysis and tail‑risk measurement, providing a computationally efficient, arbitrage‑free marginal that can be directly used in those applications. On the observed strike range the construction reproduces input option prices exactly; outside this range power‑law tails satisfy price and slope boundary conditions while allocating the remaining probability mass, guaranteeing butterfly‑ and calendar‑arbitrage‑freeness by design and yielding marginals with closed‑form density, CDF, quantile functions and efficient Monte Carlo sampling.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Risk‑neutral marginals are probability distributions derived from option prices that are used in methods such as martingale optimal transport and Bass local‑volatility calibration. Butterfly arbitrage refers to violations of convexity in the option surface, while calendar arbitrage concerns violations of monotonicity across maturities. Ensuring these arbitrage‑free conditions is essential for the marginals to be valid inputs for downstream quantitative finance models.

<details><summary>References</summary>
<ul>
<li><a href="https://soner.princeton.edu/document/126">Martingale Optimal Transport H. Mete Soner ORFE, Princeton ————————————————————</a></li>
<li><a href="https://arxiv.org/abs/2311.14567">[2311.14567] Calibration of the Bass Local Volatility model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Butterfly_(options)">Butterfly (options) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#risk-neutral measure`, `#arbitrage-free`, `#option pricing`, `#martingale optimal transport`

---

<a id="item-8"></a>
## [Study Finds No Short-Run Liquidity Response to Uniswap Protocol-Fee Cuts](https://arxiv.org/abs/2607.08525) ⭐️ 8.0/10

The paper uses a pre‑specified matched‑overlap event‑study difference‑in‑differences design to estimate the liquidity‑supply response to Uniswap protocol‑fee cuts, finding no significant short‑run effect on active liquidity or local depth. LP participation and composition likewise show no response. Providing causal evidence on how fee changes affect liquidity helps DeFi protocol designers anticipate the impact of governance decisions on fee tiers, and the stability of AMMs. It shows that short‑run liquidity supply may be insensitive to protocol‑fee adjustments, informing trader‑facing fee models and risk assessments. The study reconstructs treatment, event time, unit roles, and outcomes from public Uniswap v3 logs into a hash‑checked panel before estimation, uses the kernel K_L as the estimand for LP‑side response, and subjects token‑1 volume and native fee income to a parallel‑trends gate, which they fail, so those are reported only descriptively.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Automated market makers (AMMs) enable decentralized trading by pooling assets; liquidity providers (LPs) earn fees but also suffer losses from adverse selection. Uniswap v3 introduced concentrated liquidity and a separate protocol fee that is taken from LP earnings without changing trader‑facing fees. Difference‑in‑differences (DiD) is a quasi‑experimental method that compares changes over time between a treatment group exposed to an intervention and a control group, often combined with event‑study designs to trace dynamic effects.

**Tags**: `#DeFi`, `#Automated Market Makers`, `#Causal Inference`, `#Liquidity Provision`, `#Uniswap`

---

<a id="item-9"></a>
## [Learned Predictive Ambiguity Sets Enhance Decision-Focused DRO.](https://arxiv.org/abs/2607.09820) ⭐️ 8.0/10

The paper introduces learned predictive ambiguity sets (LPAS), where a deep contextual model outputs a nominal scenario distribution, a state‑dependent Wasserstein radius, and optionally an anisotropic ground metric to define a contextual ambiguity set for a DRO decision layer. The radius is trained using conditional quantile calibration, size regularization, and downstream decision loss, and the method is evaluated on distributionally robust portfolio optimization with 20 S&P 500 constituents from 2018‑2026. By integrating deep contextual modeling with distributionally robust optimization, LPAS provides adaptive robustness that adjusts to the input state rather than using a fixed global radius. This reduces unnecessary conservatism, improves regime adaptivity, and can enhance decision‑focused applications such as financial portfolio management. The method derives the finite dual form used by the decision layer, employs a staged training algorithm, and optionally learns an anisotropic metric; training combines quantile calibration, radius‑size regularization, and realized decision loss. Experiments show 26.28% annualized return, Sharpe ratio 1.30, final wealth 1.61, lower tail loss than a fixed‑radius DRO baseline, while using a smaller average Wasserstein radius.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Distributionally robust optimization (DRO) protects against model misspecification by optimizing against the worst‑case distribution within an ambiguity set. Traditional Wasserstein DRO centers the ambiguity set on historical samples and uses a fixed radius, which can be overly conservative. Learned predictive ambiguity sets replace the fixed center and radius with outputs of a deep model that conditions on contextual features, allowing the ambiguity set to adapt to the current state. The Wasserstein distance measures the cost of transforming one probability distribution into another, and an anisotropic ground metric can weight directions differently to capture feature‑specific uncertainty.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.09820v1">Learning Predictive Ambiguity Sets for Decision-Focused ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wasserstein_metric">Wasserstein metric - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/mathematics/wasserstein-distance">Wasserstein Distance - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**Tags**: `#distributionally robust optimization`, `#machine learning`, `#decision-focused optimization`, `#ambiguity sets`, `#Wasserstein distance`

---

<a id="item-10"></a>
## [Diachronic Sample Integration Improves Tail-Risk Estimation for Generative Models](https://arxiv.org/abs/2607.10810) ⭐️ 8.0/10

The paper introduces Diachronic Sample Integration (DSI), a test-time inference framework that ensembles generated samples across training checkpoints to stabilize tail-risk estimation. It is validated on synthetic multivariate processes and high-frequency trading data, showing reduced error versus single-checkpoint baselines. Accurate tail-risk estimation is crucial for risk-sensitive decisions in finance and engineering, where rare adverse events dominate outcomes. By improving the reliability of generative simulators under limited simulation budgets, DSI can enhance downstream risk management and option pricing. DSI forms a checkpoint-mixture distribution that averages checkpoint-specific tail fluctuations, supported by a finite-budget bias‑variance theory. Empirically it outperforms standard diffusion models and state‑of‑the‑art tail‑aware baselines without altering the generative objective.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Deep generative models are often used as simulators when real data are scarce, but standard training objectives focus on matching the bulk of the distribution, leaving low‑probability tails vulnerable to noise. In risk‑sensitive applications, accurate estimation of these tails is essential because decisions depend on rare extreme events. Ensemble methods that combine information from multiple training snapshots can reduce variance and improve stability of tail estimates.

**Tags**: `#generative models`, `#tail risk estimation`, `#Diachronic Sample Integration`, `#high-frequency trading`, `#bias-variance theory`

---

<a id="item-11"></a>
## [Paid Mobile Ads Boost Organic Installs via App Store Rankings](https://arxiv.org/abs/2504.16151) ⭐️ 8.0/10

Using data from a large US-based mobile game developer, the study finds that a global advertising shutoff reduced organic installs by 20‑30%, showing that paid ads generate positive spillovers to organic traffic through improved app store rankings. The result contradicts earlier work that found over‑attribution of paid ads, implying that mobile install advertising is more effective than paid‑install metrics alone suggest and that developers may be under‑investing in marketing. Event‑study analysis shows a 20‑30% drop in organic installs after the shutoff; panel regressions estimate that each $100 of ad spend yields 32 paid installs and 2.2 organic installs, and the ad‑spend‑organic link disappears once store rankings are controlled for, indicating a ranking‑mediated spillover.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Mobile app install ads let users download an app directly from an advertisement, and app stores rank apps partly by recent download velocity and conversion rates. Prior research in search advertising showed that paid ads often take credit for organic installs that would have happened anyway (over‑attribution). Event study designs are a common econometric tool for estimating the dynamic impact of a sudden policy change, such as an advertising shutoff.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/google-ads/answer/6357635?hl=en">About mobile app install ads - Google Help</a></li>
<li><a href="https://neilpatel.com/marketing-stats/halo-effect-paid-ads-lifting-organic-installs/">Paid Ads Boost Organic Installs on the App Store - Neil Patel</a></li>
<li><a href="https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.37.2.203">An Introductory Guide to Event Study Models</a></li>

</ul>
</details>

**Tags**: `#mobile advertising`, `#app store optimization`, `#advertising spillovers`, `#empirical analysis`, `#ranking mechanism`

---

<a id="item-12"></a>
## [Neural-Network Surrogate Speeds Catastrophe Bond Valuation to Milliseconds.](https://arxiv.org/abs/2509.25899) ⭐️ 8.0/10

Researchers developed a neural-network surrogate that prices catastrophe bonds in milliseconds, dramatically accelerating structural valuation compared to traditional Monte Carlo and PDE methods. The surrogate enables real-time pricing, screening, and sensitivity analysis for catastrophe bonds, supporting faster risk management decisions in insurance-linked securities markets. Trained on variance-reduced Monte Carlo importance‑sampling data from a compound‑Poisson catastrophe bond model, the surrogate achieves sub‑cent accuracy across Gamma and Lognormal severity specifications and prices 1000 contracts in 0.03–0.04 seconds, versus tens to hundreds of seconds for Monte Carlo and many hours for a partial integro‑differential equation benchmark.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Catastrophe bonds are insurance-linked securities that transfer the risk of natural disasters to investors, with their value depending on the probability and severity of triggering events. Structural pricing of these bonds typically requires computationally intensive Monte Carlo simulation or solving partial integro‑differential equations, which can take seconds to hours per contract. Importance sampling reduces variance in Monte Carlo estimators by sampling more frequently from influential scenarios, providing accurate training labels for surrogate models, while neural‑network surrogates learn to approximate the pricing operator for rapid evaluation after training.

<details><summary>References</summary>
<ul>
<li><a href="https://www.corvidpartners.com/field-guide/insurance/catastrophe-bond">Catastrophe Bonds: Trigger Types, Modeling & Valuation ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Importance_sampling">Importance sampling - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0304405X25002302">Deep surrogates for finance: With an application to option ...</a></li>

</ul>
</details>

**Tags**: `#catastrophe bonds`, `#neural network surrogate`, `#Monte Carlo importance sampling`, `#financial risk modeling`, `#surrogate modeling`

---

<a id="item-13"></a>
## [LLM-built database reveals bank runs in weak and strong banks.](https://arxiv.org/abs/2601.20285) ⭐️ 8.0/10

Researchers applied large language models to historical newspapers to create a database of 3,984 U.S. bank runs from 1863 to 1934, showing that runs are more likely in weak banks but also occur in strong banks due to systemic news, with failures mainly linked to poor fundamentals. The work provides a large-scale historical dataset that clarifies how bank fundamentals, not just panic, drive runs and their economic consequences, offering insights for financial stability policy and crisis prevention. Strong banks survive runs through signaling strength, interbank cooperation, and temporary suspension, while runs on weak banks lead to substantially larger declines in deposits, lending, and local manufacturing activity.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Bank runs occur when many depositors withdraw funds simultaneously, often triggered by fears of insolvency. Historical analysis of such events has been constrained by the need for extensive manual archival work, but large language models can now automate the extraction of run events from digitized newspapers. Understanding the role of fundamentals versus panic helps distinguish between self‑fulfilling crises and those driven by real economic weaknesses.

<details><summary>References</summary>
<ul>
<li><a href="https://dhlab.hypotheses.org/4938">Large-Scale Research with Historical Newspapers: A Turning ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S037842661400123X">Correlated bank runs, interbank markets and reserve ...</a></li>
<li><a href="https://www.fdic.gov/regulations/examinations/enforcement-actions/ch-06.pdf">Chapter 6 Removal, Prohibition, and Suspension Actions - FDIC</a></li>

</ul>
</details>

**Tags**: `#banking`, `#financial crises`, `#natural language processing`, `#economic history`, `#bank runs`

---

<a id="item-14"></a>
## [Differential ML for 0DTE Options with Stochastic Volatility and Jumps](https://arxiv.org/abs/2603.07600) ⭐️ 8.0/10

The paper introduces a differential machine learning method for pricing zero-days-to-expiry (0DTE) options under a stochastic-volatility jump-diffusion model. It uses a maturity-gated variance correction, price and Greek supervision, a PIDE-residual penalty, and a jointly trained jump-operator network in a three-stage procedure. The approach improves jump-term approximation while keeping pricing errors comparable, reduces Greek errors, yields stable one-day delta hedges, and provides significant speedups over Fourier-based benchmarks. This enhances practical pricing and risk management for ultra-short-maturity options. A single network outputs both option prices and Greeks; a separate jump-operator network approximates the compensated jump operator and is trained jointly. The method incorporates a maturity-gated variance correction to express prices in Black–Scholes form and adds a PIDE-residual penalty to enforce model consistency.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Zero-days-to-expiry (0DTE) options expire at the close of the trading day, requiring models that capture rapid price dynamics and jump risks. Stochastic-volatility jump-diffusion models describe asset prices with both continuous volatility fluctuations and discontinuous jumps, governed by a partial integro-differential equation (PIDE). Differential machine learning (DML) trains neural networks to approximate pricing functions while incorporating price sensitivities (Greeks) and PIDE residuals to improve accuracy and hedging stability. The maturity-gated variance correction adapts the Black–Scholes formula for ultra-short maturities by scaling variance with time-to-expiry.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.07600">[2603.07600] Differential Machine Learning for 0DTE Options ... Differential Machine Learning for 0DTE Options with ... 0DTE Volatility Gains Momentum in Income Strategies and ... Differential Machine Learning for 0DTE Options with ... Short-maturity options on realized variance in local ... Markovian stochastic volatility with stochastic correlation ...</a></li>
<li><a href="https://arxiv.org/html/2512.05301v1">Differential ML with a Difference - arXiv.org</a></li>
<li><a href="https://www.emergentmind.com/topics/partial-integro-differential-equation-pide">Partial Integro-Differential Equations (PIDE)</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#options pricing`, `#stochastic volatility`, `#jump diffusion`, `#0DTE`

---

<a id="item-15"></a>
## [AI productivity gains affect wages and optimal policies reduce inequality.](https://arxiv.org/abs/2607.01101) ⭐️ 8.0/10

The paper models how increases in AI productivity affect wages across different labor types, contrasts competitive versus monopolistic AI production, and derives optimal tax and regulatory policies to mitigate inequality. It offers a rigorous theoretical framework for understanding AI's distributional effects on wages and guides policymakers in designing taxes and regulations that can achieve Pareto‑improvements. The study finds that wages for labor essential to AI production rise faster than GDP, wages for labor substitutable by AI fall in absolute and relative terms, and wages for labor used only in final‑goods production track GDP; monopoly AI production slows deployment and alters the optimal policy mix.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Artificial intelligence is increasingly viewed as a general‑purpose technology that can raise productivity across sectors, but its impact on workers depends on whether their tasks are complemented or replaced by AI. When AI production is competitive, the technology spreads quickly, whereas monopolistic control can restrict deployment and slow the diffusion of gains. Economists study taxes, subsidies, and regulation as tools to redistribute AI‑generated income and mitigate rising inequality.

**Tags**: `#AI economics`, `#inequality`, `#labor market`, `#technology policy`, `#productivity`

---

<a id="item-16"></a>
## [Authors introduce a structural volatility model for binary prediction markets.](https://arxiv.org/abs/2607.08199) ⭐️ 8.0/10

The authors develop and estimate a volatility model tailored to binary prediction markets, combining a Wright-Fisher deadline-resolution component and a Glosten-Milgrom order-flow component, and test it on a large panel of Kalshi contract data. This structural approach provides the first theoretically grounded volatility forecast for prediction markets, outperforming standard ARCH/GARCH benchmarks and offering insights into how information arrival and deadline effects drive volatility, which is valuable for market makers, risk managers, and traders. The model combines a Wright-Fisher process that forces binary uncertainty to resolve over time with a Glosten-Milgrom component that captures volatility from informed trading via spreads and volume; empirical results show structural variables dominate plain ARCH/GARCH, and adding residual GARCH yields the best forecasts, with volatility peaking near 50-50 prices and rising as contracts approach expiration.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Prediction markets trade contracts whose prices represent the probability of future binary outcomes, with prices bounded between 0 and 1 and settling at known deadlines. Traditional volatility models like ARCH and GARCH are designed for unbounded asset returns, making them less suitable for these bounded probabilities. The paper adapts a Wright-Fisher diffusion to model how uncertainty resolves as the deadline approaches, and a Glosten-Milgrom sequential trade model to capture volatility generated by informed trading through spreads and order flow. Empirical analysis uses a large panel of contracts from Kalshi, a regulated prediction‑market platform launched in 2021 that hosts a wide range of event contracts.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.08199">[2607.08199] Volatility in Prediction Markets: A Structural ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kalshi">Kalshi - Wikipedia</a></li>
<li><a href="https://github.com/Cava11/Glosten_and_Milgorm_model">GitHub - Cava11/Glosten_and_Milgorm_model</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#volatility modeling`, `#econometrics`, `#market microstructure`, `#Kalshi`

---

<a id="item-17"></a>
## [Study Finds LLMs Show Ideological Bias in Economic Causal Reasoning](https://arxiv.org/abs/2604.21334) ⭐️ 8.0/10

Researchers extended the EconCausal benchmark with ideology‑contested cases and evaluated 20 state‑of‑the‑art large language models on their ability to predict empirically verified economic causal directions. The findings reveal that LLMs are not only less accurate on ideologically contested economic questions but also systematically biased toward intervention‑oriented expectations, which could affect their reliability in policy analysis. From 10,490 causal triplets derived from top‑tier economics journals, 1,056 were identified as ideology‑contested; across 18 of 20 models, accuracy was higher when the true causal sign matched intervention‑oriented expectations, and errors leaned disproportionately toward that direction even after one‑shot prompting.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: Large language models are increasingly employed to assist in economic forecasting and policy analysis, where correctly inferring the direction of causal effects is crucial. The EconCausal benchmark provides a collection of treatment‑outcome pairs with empirically verified causal directions drawn from peer‑reviewed economics and finance literature. By adding ideology‑contested instances—cases where intervention‑oriented and market‑oriented viewpoints predict opposite causal signs—the benchmark can test whether LLMs’ predictions are systematically skewed by political ideology.

**Tags**: `#LLMs`, `#bias`, `#economic reasoning`, `#causal inference`, `#AI safety`

---

<a id="item-18"></a>
## [The Benchmark Ceiling: Human Judgment Limits AI Evaluation as Models Improve](https://arxiv.org/abs/2607.01254) ⭐️ 8.0/10

The paper introduces the benchmark ceiling problem, showing that as AI models saturate easy benchmark items, meaningful performance differences depend on scarce expert judgment for hard items. It presents a formal model of benchmark signal depreciation and uses micro1 platform data to quantify the scarcity premium for high‑judgment evaluation labor. Understanding the benchmark ceiling is crucial for AI safety and governance because it reveals limits of current evaluation methods and guides investment in better benchmarks and expert evaluation resources. It affects researchers, developers, and policymakers who rely on benchmarks to assess frontier models. The formal model shows that valid signal concentrates in hard‑tail benchmark items, that the replacement cost of such items rises convexly with frontier capability, and that private benchmark producers underinvest in validity relative to the social optimum. Empirical data from micro1 over one thousand credentialed professionals reveal a scarcity premium for high‑judgment, low‑codifiability evaluation labor.

rss · arXiv Quantitative Finance · Jul 14, 04:00

**Background**: AI capability is commonly measured using benchmarks that aggregate performance across many test items. As foundation models improve, they often achieve near‑perfect scores on the majority of items, leaving only the hardest cases to discriminate performance. Designing those hard items requires elite expertise, which is limited in supply and expensive to produce, creating a structural scarcity in evaluation signal.

**Tags**: `#AI evaluation`, `#benchmarking`, `#foundation models`, `#human judgment`, `#AI safety`

---