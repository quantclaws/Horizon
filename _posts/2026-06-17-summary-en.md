---
layout: default
title: "Horizon Summary: 2026-06-17 (EN)"
date: 2026-06-17
lang: en
---

> From 58 items, 19 important content pieces were selected

---

1. [GrapheneOS Ported to Android 17, Official Release Imminent.](#item-1) ⭐️ 8.0/10
2. [Running Local LLMs Becomes Practical in 2026](#item-2) ⭐️ 8.0/10
3. [Wolfram Language and Mathematica Version 15 launched with AI assistant and symbolic music.](#item-3) ⭐️ 8.0/10
4. [Interactive guide explains mechanical watch mechanics with visualizations](#item-4) ⭐️ 8.0/10
5. [Qwen Releases Foundation Model Suite for Physical World Robotics](#item-5) ⭐️ 8.0/10
6. [Is Meta destroying its engineering organization?](#item-6) ⭐️ 8.0/10
7. [Apple to Limit Hide My Email Alias Creation, Reducing Its Privacy Utility](#item-7) ⭐️ 8.0/10
8. [Machine-Checked Lean 4 Formalization of Ito Calculus for Brownian Motion](#item-8) ⭐️ 8.0/10
9. [Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters](#item-9) ⭐️ 8.0/10
10. [Fast, Error-Bounded Option Pricing via Pretrained Neural Surrogates for GJR-GARCH](#item-10) ⭐️ 8.0/10
11. [Visible TWAP orders on Hyperliquid reduce execution costs vs hidden metaorders](#item-11) ⭐️ 8.0/10
12. [Chaining Tasks, Redefining Work: A Theory of AI Automation](#item-12) ⭐️ 8.0/10
13. [Probabilistic identification of technology tipping points in decarbonized German and British power systems](#item-13) ⭐️ 8.0/10
14. [PHINN: Persistent Homology Inspired Neural Network for Rare-Event Time Series Generation](#item-14) ⭐️ 8.0/10
15. [Gaming-Resistant Insurance Contracts for Autonomous AI Agents via Strategy-Proof Toll Mechanism](#item-15) ⭐️ 8.0/10
16. [Smiles in profiles improve efficiency and reduce disparities.](#item-16) ⭐️ 8.0/10
17. [Optimal Quoting Framework Addresses Adverse Selection and Price Reading](#item-17) ⭐️ 8.0/10
18. [This paper presents mixture-preserving, arbitrage-free interpolation for volatility-surface models.](#item-18) ⭐️ 8.0/10
19. [Shachi: Modular Framework for LLM-Based Agent-Based Modeling of Emergent Behavior](#item-19) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GrapheneOS Ported to Android 17, Official Release Imminent.](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) ⭐️ 8.0/10

GrapheneOS has been successfully ported to Android 17, with the development team announcing that official releases are forthcoming. This update ensures that privacy‑focused users continue to receive security hardening on the latest Android version, extending the lifespan of GrapheneOS on newer Pixel devices. The port is based on Android 17 (API level 35) and includes the usual GrapheneOS hardening patches; official builds are expected for supported Pixel models soon.

hackernews · Cider9986 · Jun 16, 20:34 · [Discussion](https://news.ycombinator.com/item?id=48561654)

**Background**: GrapheneOS is an open-source, privacy-focused operating system that hardens Android by removing Google services and adding exploit mitigations, primarily targeting Pixel smartphones. Android 17 represents the newest major version of the Android platform, introducing new APIs and system changes; its version history is documented in the Android version history Wikipedia page. This port brings GrapheneOS’s security enhancements to that latest baseline.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Android_version_history">Android version history - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong satisfaction with GrapheneOS's privacy benefits, noting they would not return to stock Android. Several pointed out missing conveniences such as swipe-to-move cursor and limited reaction emoji handling, as well as compatibility issues with certain banking and fitness apps like Strava. Others highlighted the limited availability of Pixel devices worldwide and expressed interest in seeing GrapheneOS on more hardware, with one longtime iPhone user considering a switch.

**Tags**: `#GrapheneOS`, `#Android`, `#privacy`, `#mobile security`, `#open source`

---

<a id="item-2"></a>
## [Running Local LLMs Becomes Practical in 2026](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) ⭐️ 8.0/10

On June 15, 2026, Vicki Boykis published a blog post arguing that running large language models locally has become practical, covering model types, quantization, hardware needs, and the impact on commercial API providers. This shift lowers the barrier for developers and small teams to experiment with state‑of‑the‑art AI without costly cloud subscriptions, potentially pressuring hosted model providers to adjust pricing and expand accessibility. The post notes that dense models like Qwen 27B and Gemma 31B are knowledgeable but slow, while Mixture‑of‑Experts models such as Gemma 26B and Qwen 35B run faster yet make more mistakes; 4‑bit quantization reduces memory but weakens tool‑calling ability, and modern GPUs like the RTX 5090 or Apple M4 Ultra provide sufficient VRAM for local inference.

hackernews · jfb · Jun 16, 14:36 · [Discussion](https://news.ycombinator.com/item?id=48555993)

**Background**: Large language models require substantial memory and compute, making local deployment historically difficult. Quantization techniques reduce the numerical precision of weights, shrinking model size and inference cost while preserving reasonable performance. Recent consumer GPUs such as NVIDIA’s RTX 5090 and Apple’s M4 Ultra now deliver enough VRAM to run quantized LLMs on a desk‑side machine, as highlighted in hardware comparisons and compression surveys.

<details><summary>References</summary>
<ul>
<li><a href="https://michielh.medium.com/llm-quantization-techniques-balancing-performance-and-efficiency-bc348eed3816">LLM Quantization Techniques : Balancing Performance and... | Medium</a></li>
<li><a href="https://www.fazb.com.sa/fast-local-llm-inference-hardware-choices-tuning/">Fast Local LLM Inference , Hardware ... - Faz Business | فاز الأعمال</a></li>
<li><a href="https://www.projectpro.io/article/llm-compression/1179">LLM Compression Techniques to Build Faster and Cheaper LLMs</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed feelings: some lament that dense local models remain slow and that quantization harms tool use, while others prefer local models over hosted alternatives due to cost and dissatisfaction with models like Claude Sonnet 4.6; several noted the economic pressure on providers and asked for concrete code examples to evaluate usability.

**Tags**: `#LLM`, `#local models`, `#AI`, `#machine learning`, `#Hacker News`

---

<a id="item-3"></a>
## [Wolfram Language and Mathematica Version 15 launched with AI assistant and symbolic music.](https://writings.stephenwolfram.com/2026/06/launching-version-15-of-wolfram-language-mathematica-built-in-useful-ai-lots-of-new-core-functionality/) ⭐️ 8.0/10

Wolfram released Version 15 of the Wolfram Language and Mathematica, adding a built‑in AI assistant that appears as a chatbar in notebooks and new symbolic music features that enable direct MIDI‑style note synthesis. The release tightens the integration of AI assistance into technical workflows, boosting productivity for scientists and engineers, while the symbolic music tools expand the platform’s creative applications and signal Wolfram’s effort to stay relevant amid growing open‑source alternatives. The AI assistant requires Wolfram Language Version 14.1 or higher and a paclet installation before Version 15; the chatbar appears at the bottom of each notebook unless disabled. Symbolic music leverages the language’s native MIDI‑style note‑based sound synthesis, allowing users to generate music directly from symbolic expressions.

hackernews · alok-g · Jun 16, 23:15 · [Discussion](https://news.ycombinator.com/item?id=48563609)

**Background**: Wolfram Language and its flagship product Mathematica have long been used for symbolic computation, data analysis, and technical prototyping in academia and industry. Earlier work such as WolframTones demonstrated the platform’s capacity for algorithmic music generation, and the Sound and Sonification documentation shows its support for arbitrary waveform and MIDI‑style synthesis. Version 15 builds on this foundation by embedding a conversational AI assistant and formalizing symbolic music capabilities within the core language.

<details><summary>References</summary>
<ul>
<li><a href="https://writings.stephenwolfram.com/2011/06/music-mathematica-and-the-computational-universe/">Music, Mathematica, and the Computational Universe—Stephen Wolfram Writings</a></li>
<li><a href="https://reference.wolfram.com/language/guide/SoundAndSonification.html">Sound and Sonification - Wolfram Language Documentation</a></li>
<li><a href="https://www.wolfram.com/ai-assistant/">Wolfram AI Assistant</a></li>

</ul>
</details>

**Discussion**: Commenters praised Mathematica’s ease of use for creating fractals and animations but criticized its high cost and closed‑source nature, noting that the AI assistant feels inferior to alternatives like Claude. Some expressed interest in the symbolic music features, questioned real‑world industrial adoption, and pointed to free open‑source options such as Hissab.

**Tags**: `#Wolfram Language`, `#Mathematica`, `#Version 15`, `#AI assistant`, `#symbolic music`

---

<a id="item-4"></a>
## [Interactive guide explains mechanical watch mechanics with visualizations](https://ciechanow.ski/mechanical-watch/) ⭐️ 8.0/10

In 2022, Ciechanowski released an interactive article that walks readers through the inner workings of a mechanical watch using step‑by‑step explanations and visualizations. It serves as an exceptional educational resource for horology enthusiasts and learners, demonstrating how interactive web content can teach complex mechanical concepts effectively. The site uses plain HTML, CSS, and JavaScript without frameworks, ensuring compatibility with older devices like iPhone 7, and includes hand‑drawn illustrations and interactive diagrams of the gear train, escapement, and mainspring.

hackernews · razin · Jun 16, 11:26 · [Discussion](https://news.ycombinator.com/item?id=48553550)

**Background**: Horology is the study of timekeeping devices, particularly mechanical clocks and watches. A mechanical watch stores energy in a coiled mainspring, which releases power through a gear train to drive the hands. The escapement regulates this release, allowing the gear train to advance in discrete ticks and producing the characteristic ticking sound.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Horology">Horology</a></li>
<li><a href="https://www.firgelliauto.com/blogs/mechanisms/escapement">Escapement Mechanism : How It Works, Diagram & Examples</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article's clarity, inspirational value, and educational quality, with some saying it motivated them to build physical exploded‑view models. They also highlighted the simplicity of the vanilla HTML/CSS/JS code, noting that it works well on older devices and appreciates the author's restraint in self‑promotion.

**Tags**: `#mechanical watch`, `#interactive visualization`, `#education`, `#horology`, `#web development`

---

<a id="item-5"></a>
## [Qwen Releases Foundation Model Suite for Physical World Robotics](https://qwen.ai/blog?id=qwen-robotsuite) ⭐️ 8.0/10

Qwen has introduced the Qwen-Robot Suite, a collection of three foundation models—Qwen-RobotNav, Qwen-RobotManip, and Qwen-RobotWorld—that integrate perception, planning, and control for robotic systems. The suite aims to close the perception‑action gap in embodied AI, potentially accelerating the deployment of intelligent robots in manufacturing, logistics and other physical‑world applications. Qwen-RobotNav handles vision‑language navigation, Qwen-RobotManip provides generalist vision‑language‑action capabilities, and Qwen-RobotWorld serves as a video world model for prediction and simulation.

hackernews · ilreb · Jun 16, 13:15 · [Discussion](https://news.ycombinator.com/item?id=48554814)

**Background**: Foundation models are large‑scale AI models trained on broad data that can be adapted to many downstream tasks. Physical world intelligence refers to AI systems that can perceive, reason about, and act in real‑world environments, a core challenge in robotics. The perception‑planning‑control paradigm decomposes robotic behavior into sensing the environment, formulating a plan, and executing actions. Qwen-Robot Suite integrates these stages into a unified set of models to enable end‑to‑end robotic intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48554814">Qwen-Robot Suite: A Foundation Model Suite for Physical World Intelligence | Hacker News</a></li>
<li><a href="https://letsdatascience.com/news/alibaba-unveils-qwen-robot-suite-for-embodied-ai-d7c90c5a">Alibaba Unveils Qwen Robot Suite for Embodied AI | Let's Data Science</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong enthusiasm, noting the suite’s potential to tap into a much larger market for robots than for software services. Some speculated about rapid mass production, envisioning millions of units per year, while others asked for technical assessments and comparisons with existing alternatives.

**Tags**: `#robotics`, `#foundation models`, `#Qwen`, `#AI`, `#physical world intelligence`

---

<a id="item-6"></a>
## [Is Meta destroying its engineering organization?](https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering) ⭐️ 8.0/10

A Hacker News discussion examines claims that Meta's engineering organization is deteriorating due to AI obsession, overhiring, and cultural issues, featuring firsthand accounts from former employees. The conversation highlights a broader trend of AI-driven shifts affecting engineering culture, workplace toxicity, and talent retention, which could signal industry-wide changes in how tech companies prioritize AI initiatives. Commenters note that well‑run teams often come from acquisitions (WhatsApp, Reality Labs, Instagram), describe overhiring and shifting requirements, mention that 30‑50% of infrastructure engineers were drafted into the ADO org, cite the departure of longtime CISO Guy Rosen, and accuse Scale AI’s founder of poaching top Meta engineers for data‑labeling work.

hackernews · throwarayes · Jun 16, 16:42 · [Discussion](https://news.ycombinator.com/item?id=48558045)

**Background**: Meta has been investing heavily in artificial intelligence, creating new organizations such as the ADO (AI Data Operations) group to support its AI ambitions. This rapid reallocation of talent has led to internal reorganizations, shifting priorities, and reports of increased pressure on engineers. The company’s size and history of acquiring successful products have created a contrast between integrated acquired teams and homegrown orgs that some employees perceive as less well managed.

**Discussion**: The discussion shows a mix of criticism and personal anecdotes, with many expressing concern over AI obsession and perceived toxicity, while some argue the issues reflect wider industry trends rather than being unique to Meta. A few commenters defend the company, noting that problems may stem from overhiring and rapid change rather than intentional malice.

**Tags**: `#Meta`, `#engineering culture`, `#AI impact`, `#workplace toxicity`, `#Hacker News`

---

<a id="item-7"></a>
## [Apple to Limit Hide My Email Alias Creation, Reducing Its Privacy Utility](https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/) ⭐️ 8.0/10

Apple is preparing to impose stricter limits on Hide My Email alias generation, including a rate limit of at least 30 aliases per hour and a maximum total number of addresses, after which users must delete old aliases to create new ones. The change undermines a core privacy tool for iCloud+ subscribers, forcing privacy‑conscious users to seek alternative alias services or adopt more cumbersome work‑arounds, and highlights the trade‑off between convenience and stricter controls in Apple’s ecosystem. Reports indicate users hit an address limit around 1,047 aliases, receiving an "Email Address Limit Reached" error; the new policy also requires services to pre‑register sending addresses, which can break notifications from payment processors or shipping companies.

hackernews · SXX · Jun 16, 18:37 · [Discussion](https://news.ycombinator.com/item?id=48559935)

**Background**: Hide My Email is an iCloud+ feature that creates unique, random email addresses forwarding to a user’s real inbox, allowing sign‑ups without revealing the true address; unlike simple plus addressing, these aliases cannot be stripped by tracking networks. Email aliasing in general hides the real address and can be disabled or revoked as needed.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/guide/icloud/set-up-hide-my-email-mm9d9012c9e8/icloud">Set up and use Hide My Email in iCloud+ on all your devices - Apple Support</a></li>
<li><a href="https://www.privacyguides.org/en/email-aliasing/">Email Aliasing - Privacy Guides</a></li>
<li><a href="https://apple.stackexchange.com/questions/441028/limit-number-for-hide-my-email">icloud - Limit number for " Hide my Email "? - Ask Different</a></li>

</ul>
</details>

**Discussion**: Commenters criticize the added hassle of pre‑generating aliases, suggest using custom domains with catch‑all forwarding, and recommend services like SimpleLogin or Fastmail for better flexibility; they also note that services must pre‑register sending addresses, causing missed notifications such as shipping updates or invoices.

**Tags**: `#privacy`, `#Apple`, `#Hide My Email`, `#email aliasing`, `#security`

---

<a id="item-8"></a>
## [Machine-Checked Lean 4 Formalization of Ito Calculus for Brownian Motion](https://arxiv.org/abs/2606.15089) ⭐️ 8.0/10

The paper presents a Lean 4 formalization of the L^2 Ito calculus for Brownian motion on [0,T], constructing the Ito integral as a Hilbert space isometry and proving Ito's formula for C^3 functions with bounded derivatives. This work delivers the first machine‑checked proof of Ito's formula and the first construction of the Ito integral as a martingale‑valued process in any proof assistant, advancing verified stochastic analysis and formal methods. Formalized in Lean 4 atop Mathlib and the BrownianMotion package, the development spans roughly 7,200 lines across 22 sorry‑free modules, building the integral from a predictable‑rectangle π‑system via density of simple adapted processes and deriving the Ito formula through a discrete‑to‑continuous argument with explicit L^2 remainder bounds.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Lean 4 is a functional programming language and proof assistant whose community‑maintained library Mathlib aims to formalize research‑level mathematics. Brownian motion (the Wiener process) is a continuous‑time stochastic process central to stochastic calculus, and its Ito integral is defined as an isometry from a Hilbert space of simple predictable processes into L^2. Formalizing these concepts requires constructing the integral as a martingale‑valued process and proving Ito's formula, which relates the differential of a function of the process to its quadratic variation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://reservoir.lean-lang.org/@RemyDegenne/BrownianMotion">BrownianMotion | Reservoir</a></li>
<li><a href="https://getacademy.blog/ito-isometry-theorem-guide">Ito Isometry Theorem: The Ultimate Guide... - GetAcademy.blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hilbert_space">Hilbert space - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#stochastic calculus`, `#Lean 4`, `#Ito integral`, `#Mathlib`

---

<a id="item-9"></a>
## [Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters](https://arxiv.org/abs/2606.15473) ⭐️ 8.0/10

The paper introduces a Bayesian filtering framework that treats a large language model as an uncertain semantic observation model within a partially observed Markov decision process to quantify uncertainty and risk in agentic AI systems. By providing a rigorous mathematical foundation for validating agentic AI in regulated environments, the work bridges AI safety, model risk management, and quantitative risk measurement, potentially influencing financial and high‑stakes AI deployment. The framework separates uncertainty quantification (posterior entropy, belief drift, calibration error) from risk measurement (loss distribution under beliefs), uses the LLM to map evidence to a probability vector over latent regimes, and demonstrates the approach on adjusted daily equity returns from Massive.com to produce regime probabilities and VaR/CVaR‑style risk measures.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: A partially observable Markov decision process (POMDP) models decision making where the underlying state is hidden and must be inferred from observations. Bayesian filtering recursively updates beliefs about hidden states using a sensor model and temporal dynamics, providing coherent posterior distributions. In this work, a large language model serves as an uncertain observation model that converts high‑dimensional evidence into a probability distribution over latent regimes, while the filter enforces temporal consistency. The framework also connects to tail‑risk functionals such as VaR and CVaR, which quantify the expected loss beyond a given probability threshold, and to concepts of agentic AI that autonomously act based on inferred beliefs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process">Partially observable Markov decision process - Wikipedia</a></li>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tail_value_at_risk">Tail value at risk - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#agentic AI`, `#Bayesian filtering`, `#LLM`, `#risk quantification`

---

<a id="item-10"></a>
## [Fast, Error-Bounded Option Pricing via Pretrained Neural Surrogates for GJR-GARCH](https://arxiv.org/abs/2606.15502) ⭐️ 8.0/10

The paper introduces a Mixture Density Network surrogate that maps model parameters and option maturity to the terminal return density as a Gaussian mixture, enabling closed-form, arbitrage-free option prices, implied volatilities and Greeks with verifiable error bounds. By providing both speed (microsecond pricing) and rigorous error guarantees, the method makes simulation‑heavy models like GJR‑GARCH practical for real‑time risk management and trading, bridging the gap between machine learning and quantitative finance. The surrogate uses a CDF‑matching loss aligned to pricing error, and its accuracy is bounded by a distribution‑free Monte Carlo noise floor √(1/(6N)); on GJR‑GARCH it achieves an out‑of‑sample CDF error of 1.4×10⁻⁴, within 10% of the noise floor, while pricing each option in a few microseconds on a CPU core or under a microsecond on a GPU.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Many financial models, such as GJR‑GARCH, lack closed‑form option prices and therefore rely on slow, noisy Monte Carlo simulation for pricing. Neural surrogates can restore speed but traditionally offer no error guarantees. The GJR‑GARCH model extends standard GARCH by adding an indicator term that captures the leverage effect, where negative returns increase volatility more than positive ones of equal magnitude.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity">Autoregressive conditional heteroskedasticity - Wikipedia</a></li>
<li><a href="https://vlab.stern.nyu.edu/docs/volatility/GJR-GARCH">V-Lab: GJR-GARCH Volatility Documentation</a></li>
<li><a href="https://arxiv.org/html/2606.15502">Fast, Reliable, and Error-Bounded Option Pricing with Pretrained...</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#option pricing`, `#neural networks`, `#GJR-GARCH`, `#surrogate modeling`

---

<a id="item-11"></a>
## [Visible TWAP orders on Hyperliquid reduce execution costs vs hidden metaorders](https://arxiv.org/abs/2606.15715) ⭐️ 8.0/10

The study analyzed 4.3 million hidden metaorders and 465,000 visible TWAP executions on Hyperliquid, finding that visible TWAPs incur lower execution costs and smaller permanent price impact than comparable hidden metaorders. It provides empirical evidence that preannouncing trades on-chain can mitigate adverse selection, offering guidance for algorithmic traders and DeFi platforms considering transparent order types. Hidden metaorders followed front-loaded, U-shaped schedules consistent with transient-impact optimal execution, whereas TWAPs traded nearly uniformly; visible TWAPs increased displayed depth and tilted the book toward the absorbing side.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Sunshine trading theory (Admati & Pfleiderer, 1991) predicts that publicly disclosing trading intentions reduces adverse selection and attracts liquidity, lowering execution costs. Hyperliquid operates a fully on-chain limit order book for cryptocurrency perpetual futures, where its native TWAP orders are visible from inception and remain active, providing a natural setting for sunshine trading. Transient-impact optimal execution models describe how large orders should be sliced to minimize temporary market impact, often resulting in front-loaded, U-shaped trading patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bankofcanada.ca/wp-content/uploads/2012/11/Session-3-Kumar-Venkataraman.pdf">Predatory or Sunshine Trading ? Evidence from Crude Oil ETF Rolls...</a></li>
<li><a href="https://medium.com/@gwrx2005/hyperliquid-on-chain-order-book-6df27cbce416">Hyperliquid On - Chain Order Book . Hyperliquid ... | Medium</a></li>
<li><a href="https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/cfm-imperial-institute-of-quantitative-finance/events/Lillo-Imperial-Lecture1.pdf">Market impact models and optimal execution algorithms</a></li>

</ul>
</details>

**Tags**: `#market microstructure`, `#cryptocurrency`, `#algorithmic trading`, `#sunshine trading`, `#Hyperliquid`

---

<a id="item-12"></a>
## [Chaining Tasks, Redefining Work: A Theory of AI Automation](https://arxiv.org/abs/2606.15960) ⭐️ 8.0/10

The authors introduce a theoretical model where production steps are organized into manual, AI‑augmented, or fully automated contiguous chains, showing how firms optimally allocate humans and AI to steps and derive non‑linear productivity gains from AI quality improvements. The framework reveals how AI can reshape job design beyond simple task automation, highlighting that comparative advantage reasoning may break down when AI steps are chained together. This has implications for productivity forecasting, workforce planning, and policy aimed at managing AI‑driven labor market changes. The model admits a constant‑elasticity‑of‑substitution (CES) representation at the macro level and predicts that AI‑executed steps tend to appear in contiguous chains, that greater dispersion of AI‑exposed steps reduces AI usage at the job level, and that a step’s likelihood of being AI‑executed rises with adjacency to other AI‑executed steps.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: In production theory, a task is often viewed as a sequence of steps that can be performed by labor, capital, or a combination of both. Traditional comparative advantage suggests assigning each step to the factor (human or AI) that can perform it more efficiently, assuming steps are independent. However, when AI can execute multiple consecutive steps, coordination costs fall and synergies emerge, causing the optimal allocation to deviate from simple comparative advantage. The paper formalizes this idea by modeling contiguous AI‑executed chains and shows how such chaining yields non‑linear productivity gains that can be captured by a CES aggregate production function.

<details><summary>References</summary>
<ul>
<li><a href="https://www.libertify.com/interactive-library/nber-ai-task-chaining-job-automation-theory/">AI Task Chaining and Job Automation: NBER Theory of How AI ...</a></li>
<li><a href="https://www.linkedin.com/posts/jaiganesh_how-ai-is-reshaping-workflows-and-redefining-activity-7453707992266391552-mQoc">AI Task Chaining Transforms Workflows and Job Design | LinkedIn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Macroeconomic_model">Macroeconomic model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI automation`, `#labor economics`, `#task chaining`, `#productivity theory`, `#human-AI collaboration`

---

<a id="item-13"></a>
## [Probabilistic identification of technology tipping points in decarbonized German and British power systems](https://arxiv.org/abs/2606.16469) ⭐️ 8.0/10

The study couples a sector-linked national optimization model with Monte Carlo sampling (10,000 runs) for Germany and Great Britain to quantify uncertainty and identify cost thresholds at which wind, solar, CCS, and negative‑emissions technologies become competitive. By providing probability distributions of technology pathways, the work helps policymakers design robust net‑zero strategies that account for uncertainty in technology costs and performance, highlighting where cross‑country differences matter. Tipping point cost thresholds: Britain invests in nuclear if 2035 costs fall below €4700/kW; otherwise favors offshore wind. Germany’s dispatchable low‑carbon options hinge on gas CCS (<€2100/kW), biomass CCS (<€4200/kW), or hydrogen electrolysis (<€560/kW). Wind versus solar roles remain highly ambiguous.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Sector‑linked national optimization models integrate energy supply, demand, and policy across sectors to compute least‑cost pathways. Monte Carlo simulation propagates uncertainties in technology costs, fuel prices, demand, and weather through thousands of model runs to generate probability distributions. Technology tipping points refer to the cost or performance levels at which a technology’s competitiveness shifts sharply, influencing investment decisions in decarbonizing power systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/385131637_A_regional_energy_system_transition_modeling_tool_for_decision_support_-_A_case_study_of_the_Groningen_province_in_the_Northern_Netherlands">(PDF) A regional energy system transition modeling tool for decision...</a></li>
<li><a href="https://www.weforum.org/stories/2015/09/have-we-reached-a-tipping-point-for-technology/">Have we reached a tipping point for technology ? | World Economic...</a></li>
<li><a href="https://www.researchgate.net/publication/386749180_Negative_emissions_technologies_in_energy_system_models_and_mitigation_scenarios_-a_systematic_review">(PDF) Negative emissions technologies in energy system models...</a></li>

</ul>
</details>

**Tags**: `#energy systems`, `#decarbonization`, `#Monte Carlo simulation`, `#technology tipping points`, `#power systems`

---

<a id="item-14"></a>
## [PHINN: Persistent Homology Inspired Neural Network for Rare-Event Time Series Generation](https://arxiv.org/abs/2606.15452) ⭐️ 8.0/10

We introduce PHINN, a flow‑matching framework that conditions on dynamic Betti curves and optimizes a persistence landscape loss to generate rare‑event time series with high topological fidelity. The method also offers a natural‑language interface for setting Betti targets, supports cross‑domain meta‑learning, few‑shot generation, and provides certified adversarial robustness. PHINN tackles the core challenge of modeling rare events where data are scarce, improving topological fidelity over statistical and diffusion baselines by 41‑63% in beta‑RMSE and boosting transition accuracy up to 84%. Its certified robustness and cross‑domain applicability make it valuable for finance, epidemiology, and other fields requiring reliable extreme‑event simulation. On financial, epidemiological and multi‑modal benchmarks, PHINN matches jump‑diffusion models in tail coverage while exceeding them in shape fidelity, and all results are reported with 95% confidence intervals. The framework scales to multivariate data, accepts natural‑language Betti targets, enables few‑shot and cross‑domain meta‑learning, and provides provable adversarial robustness guarantees.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Persistent homology measures topological features of data across scales, summarizing them with Betti numbers that count components, loops, and voids. Betti curves track these numbers over a filtration parameter, offering a stable signature that shifts markedly during rare events. Persistence landscapes turn persistence diagrams into functions suitable for loss‑based learning, while flow matching provides a simulation‑free way to train generative models by learning a velocity field that transports noise to data.

<details><summary>References</summary>
<ul>
<li><a href="https://giotto-ai.github.io/gtda-docs/latest/modules/generated/diagrams/representations/gtda.diagrams.BettiCurve.html">BettiCurve — giotto-tda 0.5.1 documentation</a></li>
<li><a href="https://jmlr.org/papers/volume16/bubenik15a/bubenik15a.pdf">Statistical Topological Data Analysis using Persistence</a></li>
<li><a href="https://arxiv.org/abs/2210.02747">[2210.02747] Flow Matching for Generative Modeling</a></li>

</ul>
</details>

**Tags**: `#time-series generation`, `#persistent homology`, `#rare events`, `#flow matching`, `#topological data analysis`

---

<a id="item-15"></a>
## [Gaming-Resistant Insurance Contracts for Autonomous AI Agents via Strategy-Proof Toll Mechanism](https://arxiv.org/abs/2606.16326) ⭐️ 8.0/10

The paper defines a five-attack space for insurance contracts of autonomous AI agents and introduces new contract clauses—common-control aggregation, interface failure handling, and a model-identity menu—to make the actuarial runtime strategy-proof against gaming. It also shows how these clauses compose with a prior runtime to achieve joint incentive compatibility and a two-parameter premium family satisfying individual rationality and weak budget balance. By providing a formal, gaming-resistant insurance framework, the work advances AI safety and mechanism design, enabling reliable deployment of autonomous agents in settings where side effects must be financially internalized. The approach could influence regulatory standards and insurance products for AI systems. The five-attack space includes post-toll safe-default selection, within-boundary action splitting, cross-boundary re-routing, interface failures, and misreporting of model identity; corresponding clauses close the first two attacks and introduce common-control aggregation, interface compliance penalties, and a componentwise-minimum penalty schedule for truthful reporting. A two-parameter premium family ensures individual rationality and weak budget balance at the truthful equilibrium.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: The paper builds on a prior actuarial runtime that assigns a time-consistent counterfactual risk toll to each side-effect-bearing action of an autonomous agent against a contractually safe default, gating execution by a reserve budget. That runtime treats the operator as passive; this work extends it to a strategic operator by characterizing attack surfaces and designing contract clauses to prevent gaming. The concept of common-control aggregation comes from mechanism design literature where coordinated control prevents benefit shifting across boundaries.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.26508">Foundations of a Time -Consistent Counterfactual Actuarial Runtime ...</a></li>
<li><a href="https://arxiv.org/abs/2606.16326">[2606.16326] Gaming-Resistant Insurance Contracts for Autonomous...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#mechanism design`, `#autonomous agents`, `#insurance contracts`, `#game theory`

---

<a id="item-16"></a>
## [Smiles in profiles improve efficiency and reduce disparities.](https://arxiv.org/abs/2209.01235) ⭐️ 8.0/10

Researchers used causal inference and computer vision to show that encouraging smile-related profile changes can improve transaction efficiency while reducing demographic-based disparities in peer-to-peer lending platforms. The study offers a practical way for online platforms to balance efficiency and fairness by targeting easily changeable profile features, informing policy design for more inclusive marketplaces. The approach distinguishes between immutable "type" features (e.g., gender, age) and mutable "style" features (e.g., smiling), uses causal inference on observational data and generative-model-based survey experiments to estimate effects, and finds that style differences often worsen type-based disparities.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Online peer-to-peer lending platforms rely on profile pictures to signal trustworthiness, but demographic cues can lead to biased lending decisions. Causal inference methods estimate cause-effect relationships from non-experimental data, while computer vision algorithms can automatically detect facial attributes such as smiles. Understanding the trade-off between market efficiency and disparity reduction is central to platform fairness research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marvik.ai/blog/introduction-to-causal-inference-understanding-cause-and-effect-relationships">Introduction to Causal Inference : Understanding Cause and... — Marvik</a></li>
<li><a href="https://reubensinha7.medium.com/smile-detection-a-hello-world-for-computer-vision-1b70dc65b9dc">Smile Detection — A “Hello World” for Computer Vision | Medium</a></li>
<li><a href="https://facerate.ai/">FaceRate.ai: Face Attractiveness Test & Detailed Face Analysis Tool</a></li>

</ul>
</details>

**Tags**: `#online marketplaces`, `#fairness`, `#causal inference`, `#computer vision`, `#peer-to-peer lending`

---

<a id="item-17"></a>
## [Optimal Quoting Framework Addresses Adverse Selection and Price Reading](https://arxiv.org/abs/2508.20225) ⭐️ 8.0/10

The authors of arXiv:2508.20225v5 propose a tractable optimal quoting framework that incorporates adverse selection from informed traders and the risk of price reading through the market maker's own quotes. By bridging the gap between practitioner concerns and academic models, the framework offers actionable insights for algorithmic trading and quantitative finance, addressing two long‑standing risks in market making. The model extends the Ho and Stoll (1981) and Avellaneda‑Stoikov (2008) foundations, allowing market makers to adjust bid‑ask spreads while accounting for informed flow and the inadvertent revelation of inventory via their quotes.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Market makers continuously quote bid and ask prices to provide liquidity, a practice formalized in early models such as Ho and Stoll (1981) that derive the optimal spread from a dealer’s expected utility maximization. Later, Avellaneda and Stoikov (2008) adapted this framework to high‑frequency settings using exponential utility and Poisson trade arrivals, focusing on inventory risk. In practice, market makers also face adverse selection from informed traders and the risk that their own quotes reveal inventory direction—a phenomenon known as price reading. Despite being well known to practitioners, these risks have received limited attention in the quantitative finance literature beyond stylized toy models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.09454">Axiomatic Market Making</a></li>
<li><a href="https://uditsamani.com/avellaneda-stoikov/">Optimal Market Making ( Avellaneda - Stoikov ) | Udit Samani</a></li>
<li><a href="https://en.wikipedia.org/wiki/Price_action_trading">Price action trading - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#market making`, `#adverse selection`, `#algorithmic trading`, `#quantitative finance`, `#price reading`

---

<a id="item-18"></a>
## [This paper presents mixture-preserving, arbitrage-free interpolation for volatility-surface models.](https://arxiv.org/abs/2606.12717) ⭐️ 8.0/10

The paper proposes a mixture-preserving, arbitrage-free interpolation for volatility surfaces that uses a fixed 2N-component mixture framework, freezing the components of the two expiry pillars while adjusting their weights. By guaranteeing a non‑negative Dupire local volatility, the interpolation yields a unique continuous local‑volatility diffusion, providing a theoretically sound and practically usable tool for pricing and hedging derivatives across expiries. The construction keeps the two pillar mixtures’ components fixed in a 2N‑component family and only transports their weights, ensuring the peacock (convex‑order) property and thus a non‑negative local volatility.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Volatility surfaces plot implied volatility against strike price and time to maturity, and arbitrage‑free interpolation ensures that the implied densities across expiries are ordered in convex order, which is equivalent to a non‑negative Dupire local volatility. Mixture models represent risk‑neutral densities as weighted sums of a kernel (e.g., Gaussian or lognormal); preserving the mixture structure during interpolation keeps the model tractable. The Brigo–Mercurio mixture term‑structure model uses such mixtures to describe forward rates, while the SANOS model provides a fully flexible, free‑per‑strike‑width representation; the new method bridges these approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12717v2">Mixture-Preserving, Arbitrage- Free Interpolation for Volatility - Surface ...</a></li>
<li><a href="https://quant.stackexchange.com/questions/83652/arbitrage-free-interpolation/83662">volatility - Arbitrage - free interpolation - Quantitative Finance Stack...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Damiano_Brigo">Damiano Brigo - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#volatility surface`, `#arbitrage-free interpolation`, `#mixture models`, `#quantitative finance`, `#local volatility`

---

<a id="item-19"></a>
## [Shachi: Modular Framework for LLM-Based Agent-Based Modeling of Emergent Behavior](https://arxiv.org/abs/2509.21862) ⭐️ 8.0/10

The paper introduces Shachi, a modular framework that decomposes LLM agent cognition into Configuration, Memory, and Tools components, enabling controlled perturbation studies of emergent collective behavior. Shachi addresses the lack of principled simulation tools for studying how micro-level cognitive traits influence macro-level dynamics, offering a rigorous, open-source platform for artificial life and multi-agent LLM research. The framework isolates Configuration (intrinsic identity), Memory (contextual continuity), and Tools (extended capabilities), all orchestrated by an LLM reasoning engine, and validates memory transfer across environments and cross‑environment interference in a 10‑task benchmark and a U.S. tariff shock case study.

rss · arXiv Quantitative Finance · Jun 16, 04:00

**Background**: Agent‑based modeling (ABM) simulates systems of interacting autonomous agents to study emergent collective behaviors that arise from local interactions. When agents are powered by large language models (LLMs), their cognition becomes rich but also opaque, making it difficult to systematically vary individual traits and observe resulting population‑level patterns. Shachi provides a principled, modular decomposition of LLM agent cognition into controllable components, enabling researchers to run perturbation experiments that trace how changes in memory, identity, or tool use propagate to macro‑level dynamics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2509.21862">Reimagining Agent - based Modeling with Large Language Model ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_life">Artificial life - Wikipedia</a></li>
<li><a href="https://www.ruh.ai/blogs/agentic-reasoning-fixing-llm-limitations">How Agentic Reasoning Is Fixing the Fundamental... - Ruh AI Blog</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#agent-based modeling`, `#emergent behavior`, `#artificial life`, `#framework`

---