---
layout: default
title: "Horizon Summary: 2026-09-03 (EN)"
date: 2026-09-03
lang: en
---

> From 41 items, 15 important content pieces were selected

---

1. [Polars releases py-2.0.0-rc.1 with streaming SQL engine default and performance enhancements](#item-1) ⭐️ 9.0/10
2. [Scalable Algorithm for Inverting Multinomial Probit Choice Probabilities at Million‑Scale](#item-2) ⭐️ 9.0/10
3. [Meta Releases Muse Spark 1.3, a Cost‑Effective LLM with Strong Benchmark Gains](#item-3) ⭐️ 8.0/10
4. [Google DeepMind releases Gemini 3.8 Flash and Flash Cyber models.](#item-4) ⭐️ 8.0/10
5. [Google avoids forced breakup of its ad tech business](#item-5) ⭐️ 8.0/10
6. [Three Sites Generated Over 215k AI‑Created 'Best Software' Pages Cited by Perplexity](#item-6) ⭐️ 8.0/10
7. [Mistral AI's opt‑out setting for training data sparks privacy debate on Hacker News](#item-7) ⭐️ 8.0/10
8. [Paint.NET adds AI-generated Direct2D rewrite for WINE support.](#item-8) ⭐️ 8.0/10
9. [Pricing the DeFi Tail: Do Protocols or Depositors Price Operational Risk?](#item-9) ⭐️ 8.0/10
10. [AI as Capital, Labor, GPT, and Infrastructure: Economic Analysis.](#item-10) ⭐️ 8.0/10
11. [Agentic Empirical Asset Pricing Introduces LLM‑Driven Factor Discovery Framework](#item-11) ⭐️ 8.0/10
12. [Individualized algorithmic advice stabilizes Cournot competition, biased advice enables tacit collusion](#item-12) ⭐️ 8.0/10
13. [Explicit Solutions for Quadratic BSDEs with Jumps Driven by Affine Volterra Processes](#item-13) ⭐️ 8.0/10
14. [Direct Air Capture in Europe's 2050 Energy System: Integration, Storage and Cost Drivers](#item-14) ⭐️ 8.0/10
15. [Fuel-price shock reveals unequal urban mobility adaptation in China and US](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Polars releases py-2.0.0-rc.1 with streaming SQL engine default and performance enhancements](https://github.com/pola-rs/polars/releases/tag/py-2.0.0-rc.1) ⭐️ 9.0/10

Polars released py-2.0.0-rc.1, setting the default SQL engine to the streaming engine and introducing performance improvements such as reusing native metadata for Iceberg sinks, predicate pushdown for SQL EXISTS, and collecting primitive group-by aggregations into a single chunk. This major 2.0 release brings breaking changes and significant performance gains, enabling larger-than-RAM workloads and better integration with lakehouse formats like Iceberg, which impacts data engineers and analysts relying on Polars for fast analytics. Key changes include making the streaming engine the default for SQL, reusing native metadata for Iceberg sinks (#29062), pushing down SQL EXISTS predicates before subqueries (#29078), and collecting primitive group-by aggregations into a single chunk (#28825).

github · github-actions[bot] · Sep 2, 11:49

**Background**: Polars is a Rust‑based DataFrame library that provides both eager and lazy APIs, with a streaming engine capable of processing datasets larger than memory by executing operators in a pipelined fashion. Iceberg is an open table format for huge analytic datasets, and Polars supports reading and writing Iceberg tables, allowing metadata reuse for faster sinks. Predicate pushdown is a query optimization that applies filter conditions as early as possible, reducing the amount of data scanned.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pola.rs/user-guide/concepts/streaming/">Streaming - Polars user guide</a></li>
<li><a href="https://docs.pola.rs/api/python/stable/reference/api/polars.scan_iceberg.html">polars.scan_iceberg — Polars documentation</a></li>
<li><a href="https://pola.rs/posts/predicate-pushdown-query-optimizer/">Polars — The power of predicate pushdown</a></li>

</ul>
</details>

**Tags**: `#Polars`, `#Python`, `#DataFrame`, `#Release`, `#Performance`

---

<a id="item-2"></a>
## [Scalable Algorithm for Inverting Multinomial Probit Choice Probabilities at Million‑Scale](https://arxiv.org/abs/2609.01133) ⭐️ 9.0/10

The paper introduces a scalable inversion method for multinomial probit choice probabilities that works for up to one million alternatives, achieving high accuracy and linear runtime, far surpassing the traditional GHK simulator. This advance makes correlated discrete choice models feasible at modern data scales, enabling their use in large‑scale machine learning, economics, and marketing applications where logit models are insufficient. The method exploits factor, block, and hierarchical covariance structures within a grammar of distributions, yielding linear‑time computation versus the GHK simulator’s roughly n^2.8 cost, and it remains accurate even in extreme probability tails.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Multinomial probit models represent choice probabilities as Gaussian orthant integrals, which lack closed‑form solutions and are traditionally evaluated via simulation. The Geweke‑Hajivassiliou‑Keane (GHK) simulator is the standard importance‑sampling approach but its computational cost grows super‑linearly with the number of alternatives. Recent work shows that for covariance structures belonging to a certain grammar (factor, block, hierarchical), these integrals can be computed analytically or via fast deterministic methods, enabling scalable inversion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GHK_algorithm">GHK algorithm - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/254324145_Analytic_approximations_for_computing_probit_choice_probabilities">(PDF) Analytic approximations for computing probit choice ...</a></li>
<li><a href="https://hal.science/hal-01289126/document">Estimating orthant probabilities of high dimensional Gaussian vectors...</a></li>

</ul>
</details>

**Tags**: `#multinomial probit`, `#discrete choice modeling`, `#scalable inference`, `#GHk simulator`, `#choice probability inversion`

---

<a id="item-3"></a>
## [Meta Releases Muse Spark 1.3, a Cost‑Effective LLM with Strong Benchmark Gains](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta announced Muse Spark 1.3, the latest version of its Muse Spark LLM family, featuring enhanced reasoning for agentic tasks and improved real‑world usability. The model delivers strong benchmark improvements—e.g., +94 Elo on GDPval‑AA v2 and +12 points on Tau3‑Bench Banking—while remaining inexpensive, signaling a shift toward high‑performance, low‑cost LLMs that can broaden access for developers. Muse Spark 1.3 (xhigh) and (max) variants outperform Muse Spark 1.2 on the Artificial Analysis Intelligence Index, gaining up to +139 Elo in agentic evaluations and showing improved context tracking, conflict resolution, and proactive input‑asking behavior.

hackernews · bvaldivielso · Sep 2, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49541256)

**Background**: Meta's Muse Spark series is a family of large language models designed to balance performance and cost, targeting developers who need capable models without the expense of frontier systems. Earlier versions, such as Muse Spark 1.2, were noted for low pricing and decent performance on general tasks. Muse Spark 1.3 adds a 'max reasoning' mode aimed at challenging reasoning and agentic workloads, while retaining the ability to track context and handle ambiguous inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-spark-1-3">Introducing Muse Spark 1.3 | Meta AI Research</a></li>
<li><a href="https://developer.meta.com/ai/models/muse-spark/">Muse Spark 1.3 | Meta</a></li>
<li><a href="https://artificialanalysis.ai/articles/muse-spark-1-3">Muse Spark 1.3: Meta reaches the frontier | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the model's affordability, noting generation costs of just a few cents for tasks like creating an SVG of a pelican riding a bicycle, and praised its improved output quality over version 1.2. Several users appreciated the transparent pricing that makes the value of training data explicit, while others pointed out the strong benchmark scores (e.g., DeepSWE 75.4) and the resulting price pressure on competitors.

**Tags**: `#AI`, `#LLM`, `#Meta`, `#Muse Spark`, `#model release`

---

<a id="item-4"></a>
## [Google DeepMind releases Gemini 3.8 Flash and Flash Cyber models.](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

Google DeepMind unveiled Gemini 3.8 Flash and Gemini 3.8 Flash Cyber, fast multimodal AI models that benchmark competitively with larger models and excel at HTML/JavaScript generation. The models were announced one day ago via the Google Blog and DeepMind model card. The release matters because Gemini 3.8 Flash matches the intelligence score of Opus 5 medium while being a low‑cost flash model, offering strong performance for agentic workflows and software engineering. Additionally, the dedicated Gemini 3.8 Flash Cyber variant provides superior vulnerability discovery at lower cost, appealing to developers and security researchers. Gemini 3.8 Flash supports text, image, audio, and video inputs, features configurable effort levels to balance quality, cost, and latency, and retains the low price of the 3.7 Flash series. The Cyber variant achieves +7.5‑9.7% higher recall on internal penetration‑testing benchmarks while costing 2.3‑5.2× less than other frontier models.

hackernews · bratao · Sep 2, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49537553)

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind, succeeding LaMDA and PaLM 2 and announced on December 6 2023. The Flash line is designed for fast, low‑cost inference while still offering strong capabilities, with earlier versions such as Gemini 3.7 Flash already praised for coding and agentic tasks. Gemini 3.8 Flash builds on its predecessor by delivering performance advances in software engineering and agentic knowledge workflows, and introduces a specialized Cyber variant focused on autonomous vulnerability discovery and patch generation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3 . 8 Flash and 3 . 8 Flash Cyber</a></li>
<li><a href="https://www.datacamp.com/blog/gemini-3-8-flash-cyber">Gemini 3 . 8 Flash : Features, Benchmarks, and Pricing | DataCamp</a></li>

</ul>
</details>

**Discussion**: Community reactions highlighted excitement about the model’s speed, low cost, and strong HTML/JavaScript generation, with users noting improvements over Gemini 3.7 in real‑world knowledge, trip planning, photo ranking, and document parsing. Some observed a slight increase in cost for certain tasks compared to 3.7, while others praised its multimodal capabilities and the Cyber variant’s superior vulnerability discovery performance relative to other frontier models.

**Tags**: `#Gemini`, `#LLM`, `#Google DeepMind`, `#AI models`, `#Flash model`

---

<a id="item-5"></a>
## [Google avoids forced breakup of its ad tech business](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 8.0/10

Google defeated a U.S. government attempt to force a sale of its ad tech business, avoiding structural remedies after a court found it to be a monopoly in that market. The decision preserves Google's dominant position in digital advertising, signaling limits to antitrust enforcement and affecting competitors, advertisers, and publishers reliant on the ad tech ecosystem. The court found Google's ad tech business to be a monopoly but accepted behavioral remedies instead of a forced divestiture, noting the business generated about $30 billion in revenue last year, roughly 8 % of Alphabet’s total revenue.

hackernews · donohoe · Sep 2, 14:46 · [Discussion](https://news.ycombinator.com/item?id=49537131)

**Background**: Ad tech refers to the technology and services that facilitate the buying, selling, and delivery of online advertisements, including ad servers, exchanges, and data platforms. Google’s ad tech stack includes products like Google Ad Manager, AdSense, and AdMob, which together generate a significant portion of Alphabet’s advertising revenue. Antitrust authorities have long scrutinized whether such integrated platforms stifle competition by favoring their own services.

**Discussion**: Commenters debated the meaning of “ad tech,” noting that while Google’s ad tech revenue is a small fraction of profit, its overall ad revenue dominates Alphabet’s income. Some argued for stronger structural remedies, others suggested progressive taxation or easier unwinding of mergers to curb monopoly power.

**Tags**: `#antitrust`, `#Google`, `#ad tech`, `#monopoly`, `#legal`

---

<a id="item-6"></a>
## [Three Sites Generated Over 215k AI‑Created 'Best Software' Pages Cited by Perplexity](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

An investigation revealed that three websites created more than 215,128 AI‑generated pages listing ‘best software’ recommendations, which Perplexity’s AI cites as sources in its answers. This demonstrates how AI‑generated SEO spam can pollute the retrieval‑augmented generation pipelines of LLMs, leading to hallucinated recommendations and undermining trust in AI‑powered search. The pages were produced by three sites, totaling 215,128 entries, and are designed purely to influence AI vector databases rather than human readers; Perplexity’s citation system surfaces them as authoritative sources.

hackernews · jakobgreenfeld · Sep 2, 13:59 · [Discussion](https://news.ycombinator.com/item?id=49536375)

**Background**: Large language models can hallucinate, producing plausible but false information when their retrieval‑augmented generation relies on contaminated data. Perplexity cites sources through a retrieval‑ranking‑generation pipeline, pulling in web pages that score highly on relevance signals. AI‑generated SEO spam creates massive volumes of low‑quality content specifically to manipulate those relevance signals and pollute the vector databases used by LLMs. The investigation shows that such spam can be cited as factual, highlighting the need for better source filtering.

<details><summary>References</summary>
<ul>
<li><a href="https://cloro.dev/perplexity/sources/">Perplexity Citations API — Sources & Citation Pills in JSON</a></li>
<li><a href="https://www.iloveseo.net/spam-in-the-age-of-ai-search/">Spam in the age of AI Search - I Love SEO</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters observed that LLMs often favor their own generated text over human‑written content, and that AI‑generated SEO pages can be mistakenly trusted as factual. Some noted that manipulating the model’s chain‑of‑thought style can bias its recommendations, while others criticized Perplexity for prioritizing speed at the expense of result quality, leading to unreliable citations.

**Tags**: `#AI`, `#misinformation`, `#LLMs`, `#SEO spam`, `#Perplexity`

---

<a id="item-7"></a>
## [Mistral AI's opt‑out setting for training data sparks privacy debate on Hacker News](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) ⭐️ 8.0/10

A Hacker News thread discusses Mistral AI's opt‑in/out settings for using user input and output data in model training, noting that the Team tier was switched to opt‑in by default and users share their experiences and concerns. The discussion highlights growing user unease about how AI vendors handle data consent, which can affect trust and adoption of LLM services across the industry. According to Mistral's help center, input and output data are used for training by default unless users opt out via the Admin panel under Vibe > Privacy, and the Team tier was recently changed to opt‑in by default, while the free Experiment tier also defaults to opt‑in.

hackernews · teekert · Sep 2, 12:30 · [Discussion](https://news.ycombinator.com/item?id=49535284)

**Background**: Many large language models improve by training on user interactions, but privacy regulations and user expectations increasingly require clear opt‑out mechanisms. Mistral, as a European AI provider, offers configurable data usage settings to comply with GDPR‑like expectations, though the exact opt‑out process varies across its service tiers.

<details><summary>References</summary>
<ul>
<li><a href="https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training">Can I opt out of my input or output data being used for training? | Mistral Help Center</a></li>
<li><a href="https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models">Do you use my user data to train your Artificial Intelligence models? | Mistral Help Center</a></li>
<li><a href="https://meetily.ai/llm-privacy/mistral">Mistral La Plateforme Data Retention Policy 2026 - Does Mistral Train on Your Data? | Meetily</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some willingly share their codebase and logs to improve the model, while others express skepticism, noting that vendors often train on data regardless of consent and criticize default opt‑in policies as untrustworthy.

**Tags**: `#AI privacy`, `#data usage`, `#Mistral`, `#opt-out`, `#LLM training`

---

<a id="item-8"></a>
## [Paint.NET adds AI-generated Direct2D rewrite for WINE support.](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET now includes an AI-written, from-scratch clean-room reverse-engineered implementation of Direct2D, activated via the /wine flag to enable the software on WINE. The implementation consists of about 180,000 lines of code generated by Claude. This achievement demonstrates how large language models can assist in massive software engineering tasks, potentially lowering barriers for cross-platform compatibility. It also raises discussions about code quality, legal aspects of clean-room reverse engineering, and trust in AI-generated code. The Direct2D rewrite resides in PaintDotNet.Windows.Direct2D1.Managed.dll and was produced without extensive human review, described as 'vibe coded.' Rick Brewster noted needing to supervise Claude for resource management and correct COM reference counting.

rss · Simon Willison · Sep 2, 05:50

**Background**: Direct2D is a Microsoft 2D graphics API introduced with Windows Vista and later versions, used for high-performance rendering. WINE is a compatibility layer that allows Windows applications to run on Unix-like systems, but implementing Direct2D correctly has been a major obstacle. Clean-room reverse engineering involves recreating a specification from observed behavior without accessing the original source, aiming to avoid copyright infringement. In this case, the AI model Claude generated approximately 180,000 lines of Direct2D-compatible code, which Paint.NET now uses via the /wine flag.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/direct2d/direct2d-overview">About Direct2D - Win32 apps | Microsoft Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI-generated code`, `#Direct2D`, `#WINE`, `#Paint.NET`, `#reverse engineering`

---

<a id="item-9"></a>
## [Pricing the DeFi Tail: Do Protocols or Depositors Price Operational Risk?](https://arxiv.org/abs/2609.00911) ⭐️ 8.0/10

The paper quantifies operational risk tails across DeFi sectors using a new event dataset and a Basel loss‑distribution approach, finding that Bridge, Derivatives, and Other sectors exhibit heavy tails with tail index estimates past the infinite‑mean boundary, while the Lending sector would need an 18% TVL buffer at VaR99.9 but the ten largest Lending venues hold on average only about 5% of that buffer. These results show that many DeFi protocols are under‑capitalized relative to the tail risk they impose on depositors, meaning that retail users who cannot assess the hidden risk bear most of the loss, and that market discipline alone (a ~125 bps yield gap) does not sufficiently price the risk. The study models operational‑risk loss distributions per sector, estimates tail indices (ξ≈1.6 for Bridge, Derivatives, Other) beyond the ξ=1 infinite‑mean threshold, compares them to the Moscadelli banking band [0.85,1.39], calculates a VaR99.9 capital buffer of 18% of TVL for Lending, notes that the top venues hold only about 5% of that buffer, and observes a median yield premium of 125 basis points for venues without a buffer.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Operational risk in finance is often modeled using the Basel loss‑distribution approach (LDA), which combines frequency and severity distributions to estimate capital requirements under frameworks such as Basel II’s Advanced Measurement Approach. Heavy‑tailed loss distributions are characterized by a tail index ξ; when ξ exceeds 1 the distribution has an infinite mean, implying that extreme losses can dominate expected loss. The Moscadelli banking band provides an empirical range for the tail index of traditional banking operational loss ([0.85,1.39]), serving as a benchmark for comparing DeFi sectors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_measurement_approach">Advanced measurement approach - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heavy-tailed_distribution">Heavy - tailed distribution - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2609.00911">Pricing the DeFi Tail: Do Protocols or Depositors Price ...</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#operational risk`, `#risk management`, `#blockchain finance`, `#capital buffers`

---

<a id="item-10"></a>
## [AI as Capital, Labor, GPT, and Infrastructure: Economic Analysis.](https://arxiv.org/abs/2609.01263) ⭐️ 8.0/10

The arXiv essay (2609.01263v1) argues that AI functions simultaneously as capital, synthetic labor, a general‑purpose technology, and economic infrastructure, and examines its impact on productivity, employment, market structure, and welfare. By framing AI through multiple economic lenses, the essay provides a unified framework that helps researchers and policymakers anticipate AI’s broad effects and design policies to maximize benefits while mitigating harms. It details how AI drives productivity via automation, augmentation, optimization, prediction, and innovation, while reshaping labor through substitution, complementarity, and creative destruction, and analyzes effects on competition, market concentration, entrepreneurship, and welfare for consumers, producers, workers, government, and society.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Artificial intelligence can be viewed as a form of capital because it embodies accumulated knowledge that enhances future production, and as synthetic labor when AI systems autonomously perform cognitive or physical tasks that generate economic value. As a general‑purpose technology, AI resembles past innovations like the steam engine or electricity, capable of transforming entire economies by improving a wide range of processes. Furthermore, treating AI as economic infrastructure highlights its role in lowering transaction costs, diffusing capabilities across sectors, and enabling new digital services, much like broadband or telecommunications networks.

<details><summary>References</summary>
<ul>
<li><a href="https://khullani.medium.com/synthetic-labor-agents-and-the-workforce-of-the-future-bb02ab70528c">Synthetic Labor: Agents and the Workforce of the Future | by Khullani M. Abdullahi | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/General-purpose_technology">General-purpose technology - Wikipedia</a></li>
<li><a href="https://www.weforum.org/stories/geo-economics-and-politics/ai-infrastructure-critical-infrastructure/">It’s time to start treating AI infrastructure as critical infrastructure | World Economic Forum</a></li>

</ul>
</details>

**Tags**: `#AI economics`, `#productivity`, `#labor markets`, `#general-purpose technology`, `#public policy`

---

<a id="item-11"></a>
## [Agentic Empirical Asset Pricing Introduces LLM‑Driven Factor Discovery Framework](https://arxiv.org/abs/2609.00731) ⭐️ 8.0/10

The paper defines Agentic Empirical Asset Pricing (AEAP) as a paradigm where LLM agents autonomously conduct the full scientific‑discovery cycle in finance. It proposes a reference architecture, evaluation standards, and tests a prototype system called SEADS against five baselines on two US equity panels for autonomous factor discovery. AEAP shifts focus from backtesting only factor outputs to evaluating the discovery system itself, offering a rigorous framework for autonomous financial research. This could accelerate factor innovation and bridge AI advances with quantitative finance practices. SEADS was measured against five re‑implemented baselines; no single metric ranked the systems consistently, motivating multi‑axis evaluation. A rolling re‑execution assessed whether the discovery process, not just a static factor, is reliable, and the paper reports negative findings and limitations that highlight further evaluation pitfalls.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Large language model (LLM) agents can generate hypotheses, formalize them, and evaluate results, enabling autonomous scientific discovery. In asset pricing, researchers traditionally discover factors by backtesting trading strategies on historical data, but this often ignores how the factor was found. Out‑of‑sample testing guards against overfitting by evaluating strategies on unseen data, a practice the paper extends to the discovery system itself.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.00731">Agentic Empirical Asset Pricing: Methodological Foundations</a></li>
<li><a href="https://commonplace.workforcefutures.net/paper/arxiv:2609.00731">Agentic Empirical Asset Pricing: Methodological Foundations ...</a></li>
<li><a href="https://quant.stackexchange.com/questions/50806/backtest-overfitting-in-sample-vs-out-of-sample">backtesting - Backtest overfitting - in-sample vs out - of - sample ...</a></li>

</ul>
</details>

**Tags**: `#asset pricing`, `#LLM agents`, `#factor discovery`, `#empirical finance`, `#AI for finance`

---

<a id="item-12"></a>
## [Individualized algorithmic advice stabilizes Cournot competition, biased advice enables tacit collusion](https://arxiv.org/abs/2511.09454) ⭐️ 8.0/10

In an experiment with 129 participants playing a Cournot quantity game, individualized equilibrium-aligned advice led to stable convergence toward the Nash equilibrium, while strategically biased, downward advice caused sustained underproduction and supracompetitive profits, indicating tacit collusion. The findings show that algorithmic advice can act as a strategic signal that facilitates coordination without explicit communication, raising concerns about algorithmic collusion and highlighting the need for careful design and oversight of AI decision‑support tools in competitive markets. Participants receiving individualized advice converged faster and more consistently to the equilibrium quantity than those receiving collective advice, and the biased advice was specifically downward‑shifted, producing lower output and higher profits than the competitive benchmark.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Cournot competition is an oligopoly model in which firms choose output quantities simultaneously, leading to a Nash equilibrium where no firm can increase profit by unilaterally changing its output. Tacit collusion occurs when firms coordinate their output or pricing indirectly, without explicit communication, resulting in reduced output and prices above the competitive level. The study investigates how algorithmic advice influences these dynamics by acting as a strategic signal that can either stabilize the competitive equilibrium or sustain collusive outcomes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cournot_competition">Cournot competition - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tacit_collusion">Tacit collusion - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#algorithmic advice`, `#Cournot competition`, `#tacit collusion`, `#behavioral economics`, `#human-AI interaction`

---

<a id="item-13"></a>
## [Explicit Solutions for Quadratic BSDEs with Jumps Driven by Affine Volterra Processes](https://arxiv.org/abs/2604.01300) ⭐️ 8.0/10

The authors derive explicit solutions for a class of quadratic BSDEs with jumps driven by affine Volterra processes by reducing them to a system of generalized inhomogeneous integral Riccati-Volterra ODEs with Lévy jump compensators, and apply the result to solve the continuous-time Markowitz mean-variance portfolio selection problem in a jump-diffusion, non-Markovian setting. This work provides a tractable analytical framework for solving quadratic BSDEJs with jumps in non‑semimartingale markets, enabling closed‑form optimal strategies and efficient frontiers for mean‑variance portfolio problems where classical stochastic control fails. It bridges stochastic analysis, Volterra theory and mathematical finance, offering a new tool for modeling rough volatility and jump effects. The reduction leads to a system of generalized inhomogeneous integral Riccati-Volterra ODEs whose solution yields explicit expressions for the optimal feedback control and the mean‑variance efficient frontier; the optimal value function is expressed via the solution to an associated Riccati BSDEJ. Numerical experiments on a two‑dimensional fake stationary rough Heston model illustrate the impact of stabilized rough volatilities on the Markowitz allocation.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Quadratic backward stochastic differential equations (BSDEs) with jumps arise in stochastic control and finance when the generator grows quadratically in the control variable and the driving noise includes a Poisson random measure. Affine Volterra processes are solutions of stochastic convolution equations with affine coefficients; they are generally neither semimartingales nor Markov processes, allowing modeling of rough, memory‑dependent volatility. Integral Riccati‑Volterra ordinary differential equations appear in the linear‑quadratic control of such Volterra systems and can be solved (or studied) via fixed‑point methods, providing a tractable route to explicit BSDE solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1708.08796">[1708.08796] Affine Volterra processes - arXiv.org AFFINE VOLTERRA PROCESSES - JSTOR Affine Volterra processes - Project Euclid Affine Volterra processes with jumps - ScienceDirect Affine Volterra processes with jumps - arXiv.org (PDF) Affine Volterra processes - ResearchGate Affine Volterra processes - Institut Polytechnique de Paris</a></li>
<li><a href="https://arxiv.org/abs/1911.01903">[1911.01903] Integral operator Riccati equations arising in ... Integral Operator Riccati Equations Arising in Stochastic ... On the convergence of collocation methods for Volterra ... Integral operator Riccati equations arising in stochastic ... Integral Operator Riccati Equations Arising in Stochastic ... Integral operator Riccati equations arising in stochastic ... On the convergence of collocation methods for Volterra ...</a></li>
<li><a href="https://theses.hal.science/tel-02886647/document">Contributions to quadratic backward stochastic differential equations...</a></li>

</ul>
</details>

**Tags**: `#BSDE`, `#stochastic control`, `#Volterra processes`, `#mathematical finance`, `#jump-diffusion`

---

<a id="item-14"></a>
## [Direct Air Capture in Europe's 2050 Energy System: Integration, Storage and Cost Drivers](https://arxiv.org/abs/2604.05990) ⭐️ 8.0/10

The study models direct air carbon capture and storage (DACCS) integrated into a European capacity expansion model for a fully decarbonized electricity system in 2050, analyzing how CO₂ storage availability (North Sea only vs Europe‑wide) and system integration (stand‑alone vs fully integrated) affect total system costs. It quantifies that limiting CO₂ storage to North Sea sites raises capture costs by about 10 %, while treating DACCS as a stand‑alone technology increases costs by up to 30 %, highlighting the importance of storage geography and system integration for cost‑effective carbon removal in Europe’s net‑zero transition. The paper separates capture, transport, and storage, uses a capacity expansion model to compare three integration alternatives (isolated, fully integrated, retrospectively added), and finds cost sensitivities to storage location and integration level.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Direct Air Carbon Capture and Storage (DACCS) extracts CO₂ directly from ambient air and stores it durably, offering a pathway to mitigate hard‑to‑abate emissions. Capacity expansion models are optimization tools that determine the mix of generation, storage, and transmission investments needed to meet future demand under policy constraints, and have been applied to envision a fully decarbonized European electricity system by 2050. The study integrates DACCS into such a model to evaluate how storage availability and electricity system interaction influence total system costs in a net‑zero Europe.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct_air_capture">Direct air capture - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_energy_system_models">Open energy system models - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/373172609_Energy_System_2050_-_Towards_a_decarbonised_Europe">(PDF) Energy System 2050 - Towards a decarbonised Europe</a></li>

</ul>
</details>

**Tags**: `#Direct Air Capture`, `#DACCS`, `#Energy System Modeling`, `#Carbon Storage`, `#Europe 2050`

---

<a id="item-15"></a>
## [Fuel-price shock reveals unequal urban mobility adaptation in China and US](https://arxiv.org/abs/2608.12281) ⭐️ 8.0/10

The study applied a hierarchical panel regression discontinuity design to 1.7 trillion point-of-interest visits across 122,000 neighborhoods in China and the United States, using the 2026 US-Iran oil shock as a natural experiment. It found that mobility range declined in nearly three-quarters of neighborhoods, but responses varied systematically with pre-shock urban conditions. By exposing how fuel-price shocks act as urban stress tests, the paper highlights inequalities in mobility adaptation that can inform equitable transportation policies and planning. It shows that similar mobility outcomes can arise from different adaptive or constrained processes, guiding targeted interventions. The hierarchical panel regression discontinuity design leveraged a continuous running variable (distance to the shock threshold) to estimate causal effects. Exposure to energy-intensive travel explained the largest share of heterogeneity, while longer baseline travel intensified contraction and greater car dependence limited adjustment.

rss · arXiv Quantitative Finance · Sep 2, 04:00

**Background**: Regression discontinuity design (RDD) is a quasi-experimental method that estimates treatment effects by exploiting a cutoff in a running variable. Point-of-interest (POI) data capture visits to specific locations and are increasingly used to measure human mobility patterns. Fuel-price shocks, such as the 2026 US-Iran oil shock, provide exogenous variation in travel costs that can be used as natural experiments to study behavioral responses.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2309.01404v3">Hierarchical Regression Discontinuity Design: Pursuing ...</a></li>
<li><a href="https://datapartnership.org/red-sea-monitoring/notebooks/mobility/visits.html">Estimating Activity Through Point of Interest Visits Using Mobility ...</a></li>
<li><a href="https://frontiergroup.org/articles/is-more-energy-always-better-why-pursuit-of-energy-abundance-risks-missing-the-point/">Is more energy always better? Why pursuit of " energy abundance..."</a></li>

</ul>
</details>

**Tags**: `#urban mobility`, `#fuel price shock`, `#transportation inequality`, `#regression discontinuity`, `#point-of-interest data`

---