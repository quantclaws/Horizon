---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 81 items, 23 important content pieces were selected

---

1. [Kokoro: CPU-Friendly, High-Quality Open-Source TTS Model Released](#item-1) ⭐️ 8.0/10
2. [EU Chat Control 1.0 and 2.0 proposals explained](#item-2) ⭐️ 8.0/10
3. [EU Mandates Driver Monitoring Cameras in All New Cars Starting 2026](#item-3) ⭐️ 8.0/10
4. [Introducing PgDog: New Postgres Connection Pooler with Prepared Statements.](#item-4) ⭐️ 8.0/10
5. [Microsoft lays off id Software's idTech engine team, shifts to Unreal Engine 5](#item-5) ⭐️ 8.0/10
6. [sqlite-utils 4.0 adds schema migrations, nested transactions, compound foreign keys](#item-6) ⭐️ 8.0/10
7. [Detection of 1,012 Coordinated Wallet Cohorts on Pump.fun](#item-7) ⭐️ 8.0/10
8. [DSGE as a Structured World Model: Benchmarking Counterfactual Generalization in Economic Worlds](#item-8) ⭐️ 8.0/10
9. [Exact Conditional Simulation of Point Processes for Pathwise Market Impact Estimation](#item-9) ⭐️ 8.0/10
10. [Spectral variance ratio yields five-factor model for U.S. equity returns](#item-10) ⭐️ 8.0/10
11. [GAICF Proposed to Align Generative AI Governance with SR 26-2 for Banks](#item-11) ⭐️ 8.0/10
12. [Deep Learning for Dynamic Programming with Recursive Utility](#item-12) ⭐️ 8.0/10
13. [Study Shows Upper Censorship Boosts Profits in Q-Learning Pricing Algorithms](#item-13) ⭐️ 8.0/10
14. [WorldTensor: Harmonized Global Dataset for Earth System Foundation Models](#item-14) ⭐️ 8.0/10
15. [Formalizing Look-Ahead Freedom as Temporal Non-Interference for Verifiable Trading Pipelines](#item-15) ⭐️ 8.0/10
16. [Final odds alone are insufficient for inferring beliefs in horse racing.](#item-16) ⭐️ 8.0/10
17. [Endogenous Grid Method Extended to Epstein-Zin Preferences via Power Transformation](#item-17) ⭐️ 8.0/10
18. [Cities Cluster into 17 Growth Regimes Propagating Economic Shocks](#item-18) ⭐️ 8.0/10
19. [Physics-informed VAE-Neural SDE Model for Arbitrage-free Yield Curve Forecasting](#item-19) ⭐️ 8.0/10
20. [Probabilistic proof of continuous differentiability for optimal stopping boundaries.](#item-20) ⭐️ 8.0/10
21. [Adaptive Partitioning RL for Unbounded Diffusion Processes with Regret Bounds](#item-21) ⭐️ 8.0/10
22. [Universal approximation via Brownian motion signatures for stochastic processes.](#item-22) ⭐️ 8.0/10
23. [AI Premium](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kokoro: CPU-Friendly, High-Quality Open-Source TTS Model Released](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

The article introduces Kokoro, an open-source text-to-speech model with 82 million parameters that runs efficiently on CPUs and Apple Silicon, delivering high-quality speech synthesis without requiring an NVIDIA GPU. Kokoro lowers the barrier to high-quality TTS by removing GPU dependence, making advanced voice synthesis accessible to developers and users with modest hardware, and its IPA support improves pronunciation accuracy for linguistic applications. The model supports manual IPA pronunciation guides, offers multiple voices via fine-tuning, and is available as a CLI tool and through the mlx-audio library for Apple Silicon; however, users note occasional mispronunciation of homographs and weaker performance on very short utterances.

hackernews · speckx · Jul 7, 18:24 · [Discussion](https://news.ycombinator.com/item?id=48821576)

**Background**: Most high-quality neural text-to-speech models rely on NVIDIA GPUs for real-time inference, limiting their use on low-end or CPU-only systems. Kokoro is an open-source TTS model with 82 million parameters designed to run efficiently on CPUs and Apple Silicon, leveraging the mlx-audio framework. It provides natural-sounding speech while avoiding the hardware barrier posed by GPU-dependent alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kokoro_TTS">Kokoro TTS</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>

</ul>
</details>

**Discussion**: Commenters praise Kokoro for enabling high-quality TTS on modest hardware, highlighting its IPA support and ease of integration into accessibility tools, article readers, and browser extensions. Some note shortcomings such as occasional mispronunciation of homographs and less natural output when synthesizing very short words or phrases. Overall, the community expresses strong interest and sees practical value in Kokoro’s CPU‑friendly approach.

**Tags**: `#TTS`, `#Kokoro`, `#CPU-friendly`, `#accessibility`, `#open-source`

---

<a id="item-2"></a>
## [EU Chat Control 1.0 and 2.0 proposals explained](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

The article provides an overview of the EU's Chat Control 1.0 (a temporary derogation allowing voluntary scanning of private messages) and Chat Control 2.0 (a proposal for mandatory scanning of encrypted communications), detailing their scope and sparking community debate about surveillance and encryption. The proposals threaten end-to-end encryption by requiring client‑side scanning or backdoor access, raising alarms among privacy advocates, engineers, and the broader digital rights community about potential mass surveillance and erosion of privacy protections. Chat Control 1.0, adopted in 2021, created a temporary exemption from the ePrivacy Directive that permitted providers to voluntarily scan messages for known CSAM using AI and hash matching; Chat Control 2.0 would make such scanning mandatory and apply to encrypted messages, likely via client‑side scanning or MITM decryption, affecting all users regardless of suspicion.

hackernews · gasull · Jul 7, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48818311)

**Background**: The ePrivacy Directive protects the confidentiality of electronic communications in the EU, but in 2021 the Council introduced a temporary derogation (Chat Control 1.0) to allow voluntary scanning for child sexual abuse material. Chat Control 2.0 builds on this by proposing a permanent framework that would require scanning of encrypted chats, raising concerns about client‑side scanning technologies that analyze content before encryption. These proposals intersect with ongoing debates about balancing child protection with encryption and privacy rights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html">Chat Control 1.0: EU Council forces messenger scans via fast-track | heise online</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>

</ul>
</details>

**Discussion**: Commenters expressed broad concern that the proposals constitute overreach, arguing that a sweeping surveillance measure is unjustified given the small proportion of offenders. Several noted technical worries, such as the impact on encrypted messaging and the possibility of client‑side scanning undermining privacy, while others pointed out that voluntary scanning continues despite the expiration of Chat Control 1.0.

**Tags**: `#privacy`, `#encryption`, `#EU policy`, `#chat control`, `#surveillance`

---

<a id="item-3"></a>
## [EU Mandates Driver Monitoring Cameras in All New Cars Starting 2026](https://allaboutcookies.org/eu-mandatory-distracted-driver-system) ⭐️ 8.0/10

The European Union will require every new car sold in its member states to include a driver monitoring camera system that detects distracted driving, effective from July 2026. This regulation marks a major shift in automotive safety policy, affecting millions of new vehicles and prompting manufacturers to integrate advanced sensing technology while raising privacy and user‑experience concerns. The mandate stems from the EU General Safety Regulation (GSR) and requires Driver Drowsiness and Attention Warning (DDAW) systems that use infrared cameras to track gaze, head position, and eye closure, applying to vehicle categories M and N.

hackernews · nickslaughter02 · Jul 7, 20:50 · [Discussion](https://news.ycombinator.com/item?id=48823557)

**Background**: Driver monitoring systems (DMS) use cameras and infrared sensors to detect signs of distraction or drowsiness by tracking the driver's face, eyes, and head position. The EU's General Safety Regulation, first established in 2019, already required vehicles to include DDAW systems, and the upcoming amendment makes such cameras mandatory for all newly registered cars, vans, trucks, and buses from July 2026. These systems can cooperate with pre‑collision safety features and are intended to reduce accidents caused by inattention.

<details><summary>References</summary>
<ul>
<li><a href="https://smarteye.se/blog/the-general-safety-regulations-gsr-and-driver-monitoring-systems-dms/">How Driver Monitoring Systems (DMS) Are Being Made Mandatory in 18 Million European Cars - Smart Eye</a></li>
<li><a href="https://www.idtechex.com/en/research-article/regulations-drivers-for-mandating-driver-monitoring-systems/30322">Regulations - Drivers for Mandating Driver Monitoring Systems | IDTechEx Research Article</a></li>
<li><a href="https://medium.com/@shahadilh18/your-car-will-soon-watch-your-eyes-b8e78dcfb114">Your Car Will Soon Watch Your Eyes. Here Is the Real Story Behind the EU’s Driver Monitoring Mandate | by Shahadilh | Medium</a></li>

</ul>
</details>

**Discussion**: Many commenters criticize the new systems for annoying false alerts, overly aggressive lane‑keeping beeps, and poor user experience, especially when integrated with Android Auto. Others note that the technology can be accurate, detecting subtle distractions like talking to passengers or adjusting controls, and believe it could save lives. Privacy worries and concerns about data misuse are also raised, with some users expressing reluctance to buy newer vehicles because of these intrusive features.

**Tags**: `#EU regulation`, `#automotive safety`, `#driver monitoring`, `#privacy`, `#vehicle technology`

---

<a id="item-4"></a>
## [Introducing PgDog: New Postgres Connection Pooler with Prepared Statements.](https://pgdog.dev/blog/why-yet-another-connection-pooler) ⭐️ 8.0/10

The author introduces PgDog, a new Postgres connection pooler that supports prepared statements, uses the AGPL license, and addresses connection state leakage and other shortcomings of existing poolers. PgDog fills a gap by enabling prepared statement support in connection pooling, which improves query performance and scalability, while its AGPL licensing ensures openness for network‑service software, appealing to developers wary of restrictive licenses. It also offers load balancing and sharding, facilitating horizontal scaling of Postgres without application changes. PgDog operates at OSI Layer 7, understands the Postgres protocol, can proxy multiple replicas and primary nodes, distributes transactions evenly, and explicitly avoids connection state leakage by resetting session state between clients. It is released under AGPL‑3.0 and includes features like prepared statement handling and optional query caching.

hackernews · levkk · Jul 7, 15:36 · [Discussion](https://news.ycombinator.com/item?id=48819308)

**Background**: Connection poolers reuse database connections to reduce overhead, but they can leak session state (e.g., prepared statements, temporary tables) from one client to another, causing bugs. Prepared statements allow the database to parse and plan a query once and reuse the plan, improving performance. The AGPL license is a strong copyleft license designed for software that is accessed over a network, ensuring that modifications made to network‑service software must also be released under the same license.

<details><summary>References</summary>
<ul>
<li><a href="https://pgdog.dev/blog/why-yet-another-connection-pooler">Why we built yet another Postgres connection pooler - PgDog</a></li>
<li><a href="https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License">GNU Affero General Public License - Wikipedia</a></li>
<li><a href="https://www.postgresql.org/docs/current/sql-prepare.html">PostgreSQL: Documentation: 18: PREPARE</a></li>

</ul>
</details>

**Discussion**: Commenters praised PgDog’s prepared‑statement support and AGPL licensing, raised concerns about connection state leakage in typical Postgres setups, and asked about future features such as query caching and schema‑sharding for multi‑tenant frameworks like Django‑tenant.

**Tags**: `#PostgreSQL`, `#connection pooling`, `#PgDog`, `#database infrastructure`, `#open source`

---

<a id="item-5"></a>
## [Microsoft lays off id Software's idTech engine team, shifts to Unreal Engine 5](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

Microsoft has laid off the entire idTech engine team at id Software, confirming a strategic move to adopt Epic's Unreal Engine 5 for future id Software titles. The layoffs were reported by GameFromScratch and have ignited debate over the implications for internal engine development. The decision signals a major shift away from proprietary in-house engines toward licensing third‑party technology, potentially reducing development costs but also risking loss of the unique technical identity that defined id Software’s flagship franchises. It reflects broader industry trends where even legacy studios adopt UE5 to stay competitive. The layoffs affected the entire idTech team, which had maintained the engine since id Tech 5 and contributed to id Tech 6 and id Tech 7 used in recent Doom titles. No official statement from Microsoft or id Software has been released, and the article notes a lack of concrete evidence confirming which specific employees were let go.

hackernews · bauc · Jul 7, 15:33 · [Discussion](https://news.ycombinator.com/item?id=48819244)

**Background**: id Software developed the idTech series of proprietary game engines, beginning with id Tech 1 used in the original Doom and progressing through id Tech 5 (first seen in Rage) and id Tech 7, which powered Doom Eternal. These engines are known for their cutting‑edge graphics and tight integration with id’s game design. In recent years, many studios have moved to licensing engines like Unreal Engine 5 to reduce internal maintenance overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_tech_5_engine">Id tech 5 engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech_5">id Tech 5 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that losing the idTech team erodes id Software’s technical uniqueness and could lead to a homogenized output reliant on UE5, while some criticized Microsoft’s move as a monopolistic blunder that benefits Epic. Others questioned the evidence of the layoffs, noting the article’s reliance on speculation rather than confirmed reports.

**Tags**: `#Microsoft`, `#id Software`, `#game engine`, `#layoffs`, `#Unreal Engine 5`

---

<a id="item-6"></a>
## [sqlite-utils 4.0 adds schema migrations, nested transactions, compound foreign keys](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

Simon Willison released sqlite-utils 4.0 on July 7, 2026, introducing database schema migrations, nested transactions via the new db.atomic() method, and support for compound foreign keys. These features simplify schema evolution, transaction handling, and complex relational modeling for SQLite developers, enhancing the Datasette ecosystem and reducing reliance on external tools. Migrations are defined in Python files using the Migrations class and the table.transform() method, which recreates tables to work around SQLite's limited ALTER TABLE; nested transactions use savepoints exposed through db.atomic(); compound foreign keys allow multi‑column foreign key constraints.

rss · Simon Willison · Jul 7, 19:32

**Background**: sqlite-utils is a popular Python CLI utility and library for manipulating SQLite databases, often used alongside Datasette to explore and publish data. Schema migrations track changes via Python scripts and apply pending changes, using table.transform() to implement alterations that SQLite's ALTER TABLE cannot perform directly. Nested transactions rely on SQLite's savepoint mechanism, allowing atomic blocks to be safely nested within larger transactions through the db.atomic() API. Compound foreign keys enable foreign key constraints that reference multiple columns, supporting more intricate relational designs.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/">sqlite-utils 4.0rc1 adds migrations and nested transactions</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#database-migrations`, `#python`, `#datasette`, `#release`

---

<a id="item-7"></a>
## [Detection of 1,012 Coordinated Wallet Cohorts on Pump.fun](https://arxiv.org/abs/2607.02795) ⭐️ 8.0/10

Researchers analyzed 1.58 million buyer observations from 166,098 Solana pump.fun token launches between June 12 and June 26, 2026 using a two‑stage detection pipeline, uncovering 1,012 persistent wallet cohorts (each 2‑12 wallets) that repeatedly appear as early buyers. These cohorts are associated with a +132.3% increase in first‑30‑minute buyer count and a +136.5% rise in SOL inflow compared to launches without cohort activity. The findings reveal that coordinated buyer groups can dramatically inflate early‑launch metrics, exposing a manipulation vulnerability in Solana’s meme‑token market. Regulators, developers, and analysts can adopt the presented detection pipeline to monitor such behavior and improve causal inference techniques for on‑chain activity. The detection pipeline first extracts intra‑launch first‑buyer windows, then builds a co‑occurrence graph across launches and applies union‑find to surface persistent cohorts of 2‑12 wallets. While cohort‑touched launches show a +132.3% buyer‑flow lift, an activity‑matched placebo yields a larger +216.3% lift, indicating selection bias; the authors release the full cohort catalogue, code, and robustness artefacts as RED‑COHORT‑2026‑v1 under CC‑BY‑4.0.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Pump.fun uses a bonding‑curve mechanism where token price is a deterministic function of the circulating supply, enabling instant tradability without an order book. The union‑find data structure efficiently groups elements that appear together repeatedly, making it suitable for discovering wallet sets that co‑occur as early buyers across many token launches. First‑buyer‑window extraction isolates the wallets that purchase a token within the initial moments of its launch, providing the signal needed to detect coordinated sniping behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://pump.fun/docs/bonding-curve">The Pump.fun bonding curve | Pump</a></li>
<li><a href="https://github.com/laurentpetit/union-find">GitHub - laurentpetit/union-find: Persistent Union-Find ...</a></li>
<li><a href="https://docs.mobula.io/guides/how-to-track-token-first-buyers">How to Track Token First Buyers Across Solana, Ethereum, BNB ...</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#DeFi`, `#market manipulation`, `#Solana`, `#wallet clustering`

---

<a id="item-8"></a>
## [DSGE as a Structured World Model: Benchmarking Counterfactual Generalization in Economic Worlds](https://arxiv.org/abs/2607.03144) ⭐️ 8.0/10

The paper argues that Dynamic Stochastic General Equilibrium (DSGE) models constitute structured world models and introduces DSGE‑Gym, a benchmark of eight DSGE environments with off‑path counterfactual test sets, scaling to the ECB’s 230‑variable New Area‑Wide Model. It shows that learned world models (e.g., Dreamer, IRIS, Genie, JEPA) match dynamics on‑path but collapse off‑path, with tail RMSE up to ~40× the on‑path level, while training on DSGE‑generated data halves tail error and cuts policy‑regime error by 10‑280. Linking DSGE economics with machine‑learning world models provides a principled way to measure and improve counterfactual generalization, a critical weakness of current RL agents. The benchmark offers economists and AI researchers a shared testbed to evaluate how structural knowledge can synthesize missing data distributions for robust policy analysis and decision‑making. DSGE‑Gym comprises eight DSGE environments, from simple textbook models to the ECB’s 230‑variable New Area‑Wide Model, each equipped with off‑path counterfactual test sets generated by rare policies that cannot be observed in any single history. Standard world‑model architectures match on‑path dynamics but exhibit a 5σ tail RMSE up to ~40× the on‑path level; training on DSGE‑generated data cuts tail error by about half and reduces policy‑regime error by 10‑280 when the counterfactual rule shifts ergodic support, with all code released for reproducibility.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Dynamic Stochastic General Equilibrium (DSGE) models are macroeconomic frameworks that describe the economy as the stochastic evolution of intertemporally optimizing agents in markets that clear, providing a causal, structurally constrained representation of economic dynamics. Machine‑learning world models such as Dreamer, IRIS, Genie, and JEPA learn an internal belief state of an environment from observed trajectories and predict how it changes in response to actions, but their transition functions are only reliable where data have been seen. Counterfactual generalization refers to the ability of a model to make accurate predictions about states that were never encountered during training, which is essential for robust decision‑making under distribution shifts or novel policies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_stochastic_general_equilibrium">Dynamic stochastic general equilibrium - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/decision-transformer-with-counterfactuals">Decision Transformer with Counterfactuals - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#DSGE`, `#world models`, `#counterfactual generalization`, `#reinforcement learning`, `#economics`

---

<a id="item-9"></a>
## [Exact Conditional Simulation of Point Processes for Pathwise Market Impact Estimation](https://arxiv.org/abs/2607.03239) ⭐️ 8.0/10

The paper introduces an exact conditional simulation algorithm for point processes under perturbed intensities, using a thinning representation to reconstruct counterfactual price paths on a common randomness source. This enables rigorous, pathwise estimation of market impact for various execution strategies, addressing a key unobservable counterfactual problem in quantitative finance. The method characterizes the conditional law of the latent Poisson random measure in the thinning representation, yielding an event‑driven exact simulator that works for aggressive, passive, and mixed trading strategies.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Point processes model the timing of discrete events, such as trades or price jumps, and are often described by an intensity that depends on past events. In the thinning representation, a point process is generated by thinning a homogeneous Poisson process with a time‑varying acceptance probability, introducing a latent Poisson random measure. Market impact is defined as the difference between the observed price trajectory under a given execution strategy and the unobservable counterfactual trajectory that would have occurred without the strategy, necessitating simulation of alternative paths under the same market randomness.

**Tags**: `#point processes`, `#market impact`, `#stochastic simulation`, `#quantitative finance`, `#thinning representation`

---

<a id="item-10"></a>
## [Spectral variance ratio yields five-factor model for U.S. equity returns](https://arxiv.org/abs/2607.03858) ⭐️ 8.0/10

The authors introduce a multivariate generalization of the Lo‑MacKinlay (1988) variance ratio that splits long‑horizon equity‑return dynamics into separate return‑channel and volatility‑channel memory components, producing a parsimonious five‑factor model. This framework simultaneously fits multiple U.S. and European equity panels, recovers seven stylized facts of long‑horizon dynamics, and reveals a regime shift in U.S. volatility memory, offering a new tool for quantitative finance and factor‑based investing. The model captures persistent, antipersistent, and multi‑scale memory in returns and volatility; a rolling‑window bootstrap locates a volatility‑memory regime transition in the late 1980s with the slowest component lengthening from ~2 to ~4 years; cross‑channel beta‑inversion tests reject a shared loading, showing distinct drivers for return‑ and volatility‑channel memory.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: The Lo‑MacKinlay variance ratio test, introduced in 1988, is a widely used parametric test for the random walk hypothesis that compares variance estimators at different horizons. Spectral generalization extends this idea by analyzing the eigenstructure of the covariance matrix across frequencies, allowing decomposition of return dynamics into memory components. Long‑memory processes in financial time series refer to slow decay of autocorrelations, which can be present in both returns and volatility. Factor models such as the Fama‑French framework capture cross‑sectional return patterns via a small set of risk factors.

<details><summary>References</summary>
<ul>
<li><a href="https://metricgate.com/docs/lo-mackinlay-variance-ratio/">Lo-MacKinlay Variance Ratio Test Calculator | MetricGate</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spectral_density">Spectral density - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S154461232502197X">Long memory of stock market return volatility and its impact ...</a></li>

</ul>
</details>

**Tags**: `#financial econometrics`, `#factor models`, `#variance ratio`, `#spectral analysis`, `#equity returns`

---

<a id="item-11"></a>
## [GAICF Proposed to Align Generative AI Governance with SR 26-2 for Banks](https://arxiv.org/abs/2607.04103) ⭐️ 8.0/10

The paper introduces the Generative AI Control Framework (GAICF), a governance framework designed to be compatible with the updated SR 26-2 model risk management guidance for U.S. financial institutions. GAICF fills a critical gap by extending SR 26-2’s risk‑based principles to generative AI uses that sit outside traditional model boundaries yet influence regulated decisions, helping banks meet supervisory expectations. GAICF translates core model risk management concepts—such as governance, validation, and monitoring—into a layered control structure for generative AI workflows that operate outside the formal model boundary but remain embedded in banking processes.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: SR 26-2, issued in April 2026, supersedes SR 11-7 as the U.S. Federal Reserve’s supervisory guidance on model risk management, shifting from prescriptive checklists to a principles‑based, risk‑focused approach that widens the model definition and adds explicit AI/ML considerations. While SR 26-2 modernizes MRM, it does not explicitly address generative and agentic AI, leaving a gap for financial institutions that use these technologies in areas such as monitoring interpretation, policy analysis, or adverse‑action language drafting. This omission creates a need for a complementary framework that aligns generative AI governance with SR 26-2’s risk‑based expectations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf">FRB: Supervisory Letter SR 26-2 on Revised Guidance on Model ...</a></li>
<li><a href="https://tanukamandal.com/sr-11-7-vs-sr-26-2-guide-to-model-risk-evolution/">SR 11-7 vs SR 26-2 Detail Guide to Evolution of Model Risk</a></li>
<li><a href="https://coalitiongreenwichuat.crisil.com/content/dam/crisil-integral-iq/what-we-think/all-our-thinking/reports/2026/04/navigating-the-mrm-framework-shift--from-sr-11-7-to-sr-26-2/navigating-the-mrm-framework-shift-from-sr-11-7-to-sr-26-2.pdf">Navigating the MRM framework shift From SR 11-7 to SR 26-2</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#model risk management`, `#financial regulation`, `#SR 26-2`, `#AI governance`

---

<a id="item-12"></a>
## [Deep Learning for Dynamic Programming with Recursive Utility](https://arxiv.org/abs/2607.04278) ⭐️ 8.0/10

The paper introduces the Certainty Equivalent Learning (CEL) algorithm, a deep learning method that directly learns certainty-equivalent values to solve high-dimensional discrete-time dynamic programming problems with recursive utility. CEL is the first deep learning approach for recursive utility dynamic programming, enabling mesh-free, simulation-based solutions in high dimensions without requiring Euler equations or differentiability, thus opening new avenues for complex economic and financial modeling. The CEL algorithm uses neural networks to jointly approximate value functions, policy functions, and certainty-equivalent functions; it is tested on discounted linear exponential quadratic Gaussian control, small-noise robust control, Epstein-Zin DSGE, and multivariate strategic asset allocation problems, achieving Bellman errors between 1.0e-4 and 1.0e-3.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Recursive utility, exemplified by Epstein-Zin preferences, represents utility as a function of current consumption and future utility, lacking an explicit closed form and making the Bellman equation's certainty equivalent hard to evaluate. Traditional dynamic programming relies on grid-based value function iteration or Euler equations, which become infeasible in high dimensions. The certainty equivalent is the risk-adjusted sure amount that yields the same expected utility as a risky prospect, and learning it directly avoids the need for analytical integration or differentiation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_economics">Recursive economics - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#dynamic programming`, `#recursive utility`, `#reinforcement learning`, `#numerical methods`

---

<a id="item-13"></a>
## [Study Shows Upper Censorship Boosts Profits in Q-Learning Pricing Algorithms](https://arxiv.org/abs/2607.04345) ⭐️ 8.0/10

The paper examines three disclosure rules—no disclosure, full disclosure, and upper censorship—for firms that delegate pricing to Q-learning algorithms under stochastic demand. It finds that upper censorship yields higher profits than full disclosure, but a profit reversal occurs where high discount factors favor no disclosure while low discount factors favor full disclosure. The findings challenge classical collusion theory and suggest that restricting information sharing may backfire when AI pricing agents are sufficiently patient, offering direct insights for regulators designing policies to curb algorithmic collusion. This work bridges theory and simulation, highlighting the need to reassess information‑design approaches in AI‑mediated markets. Upper censorship truthfully reveals low‑demand states while pooling high‑demand ones, and the study shows that Q‑learning agents’ profits depend systematically on the discount factor: high γ makes no disclosure more profitable, low γ makes full disclosure more profitable, a pattern opposite to traditional collusion predictions.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Q‑learning is a model‑free reinforcement learning algorithm that updates action values using a Bellman equation and a discount factor to balance immediate and future rewards. In algorithmic pricing, firms delegate price setting to such Q‑learning agents, which learn optimal prices from stochastic demand signals. Information design studies how a third‑party intermediary’s disclosure rules—such as no disclosure, full disclosure, or upper censorship—affect agents’ learning outcomes and market performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Q-learning">Q-learning - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2607.04345v1">Strategic Information Disclosure in Algorithmic Pricing</a></li>
<li><a href="https://economics.mit.edu/sites/default/files/inline-files/Platform+Price+Recommendations_2.pdf">Algorithm Design Meets Information Design: Price ...</a></li>

</ul>
</details>

**Tags**: `#algorithmic pricing`, `#information design`, `#Q-learning`, `#AI regulation`, `#algorithmic collusion`

---

<a id="item-14"></a>
## [WorldTensor: Harmonized Global Dataset for Earth System Foundation Models](https://arxiv.org/abs/2607.03298) ⭐️ 8.0/10

The paper introduces WorldTensor, a harmonized global dataset that aligns hundreds of environmental and socioeconomic variables to a 0.25° spatial grid and annual temporal framework for training Earth system foundation models. By providing a unified, multimodal training resource that bridges physical climate data with human systems, WorldTensor enables more comprehensive Earth system foundation models, addressing a key data limitation in climate AI research. WorldTensor integrates reanalysis products, remote sensing, emissions inventories, land use reconstructions, hydrological observations, infrastructure and hazard datasets, and socioeconomic indicators, all regridded to a common 0.25° grid and distributed as NetCDF files with CF metadata conventions.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Earth system foundation models are large AI models trained on diverse physical climate and weather data to learn statistical relationships across variables for downstream forecasting and analysis tasks. A 0.25° spatial grid corresponds to roughly 27.75 km resolution, providing a fine‑scale regular latitude‑longitude grid commonly used in global reanalysis datasets such as ERA5. Reanalysis products combine historical observations with model simulations to produce globally consistent gridded fields of atmospheric, oceanic, and land variables, serving as a foundational data source for climate research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-09005-y">A foundation model for the Earth system - Nature</a></li>
<li><a href="https://confluence.ecmwf.int/spaces/CKB/pages/65237704/ERA5+What+is+the+spatial+reference">ERA5: What is the spatial reference - Copernicus Knowledge ...</a></li>
<li><a href="https://climatedataguide.ucar.edu/climate-data/atmospheric-reanalysis-overview-comparison-tables">Atmospheric Reanalysis: Overview & Comparison Tables</a></li>

</ul>
</details>

**Tags**: `#Earth system science`, `#foundation models`, `#climate data`, `#multimodal datasets`, `#geospatial AI`

---

<a id="item-15"></a>
## [Formalizing Look-Ahead Freedom as Temporal Non-Interference for Verifiable Trading Pipelines](https://arxiv.org/abs/2607.04958) ⭐️ 8.0/10

The paper formalizes look-ahead bias as temporal non-interference, showing it is undecidable in general (Π₁⁰-hard) and provides a decidable fragment with a type-and-effect system for backtesting and agentic trading pipelines. By bridging formal methods and quantitative finance, the work offers a verifiable correctness property that can detect look-ahead leaks missed by existing differential and tiling detectors, improving reliability of backtests and deployed trading algorithms. The decidable fragment covers windowing, resampling, joins, point-in-time/vintage reads, and agentic retrieval; the resulting checker runs in linear time, is sound, and catches every planted leak that differential and tiling detectors miss.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Look-ahead bias occurs when a model uses future information that was not available at the decision epoch, leading to overly optimistic backtest results. Treating this bias as an information-flow property, temporal non-interference ensures that later data does not influence earlier decisions. The paper models data availability via a time-indexed information lattice and separates a datum's availability from its reference time using a pipeline calculus.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.04958v1">Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable ...</a></li>
<li><a href="https://matproof.com/regulatory-updates/arxiv-look-ahead-freedom-as-temporal-non-interference-a-verifiable-correctness-p-6856">arXiv: Look-Ahead-Freedom as Temporal Non-Interference: A ...</a></li>

</ul>
</details>

**Tags**: `#look-ahead bias`, `#temporal non-interference`, `#backtesting`, `#formal verification`, `#agentic trading`

---

<a id="item-16"></a>
## [Final odds alone are insufficient for inferring beliefs in horse racing.](https://arxiv.org/abs/2509.14645) ⭐️ 8.0/10

Using interim odds from horse racing, the study shows that realized returns depend not only on final odds but also on the path through which they are reached, with horses experiencing odds declines in the last five minutes earning higher returns than those with similar final odds. This finding challenges the common practice of inferring risk preferences or beliefs from final market prices alone, highlighting that path dependence in parimutuel markets can distort such inferences. The authors extend the Ottaviani–Sørensen information‑based model to two periods, showing that late informed wagers cause final‑stage odds declines and generate path‑dependent returns, so that final odds–return patterns cannot distinguish information aggregation from probability distortions.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: In parimutuel betting, all wagers are pooled, and payoff odds are determined after the pool is closed, so bettors cannot condition their wagers on final odds. The Ottaviani–Sørensen model explains how private information leads to favorite‑longshot bias through informed traders updating odds as they place bets. Close to race time, odds often shift due to late informed trading, creating path dependence where the trajectory of odds matters for returns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Parimutuel_betting">Parimutuel betting - Wikipedia</a></li>
<li><a href="https://igier.unibocconi.eu/sites/default/files/media/attach/131205.pdf">Noise, Information and the Favorite-Longshot Bias∗</a></li>
<li><a href="https://caanberry.com/what-causes-betting-odds-to-change/">What Causes Betting Odds to Change? - Caan Berry Why Do Horse Betting Odds Change? - TheHorseBet.com A Deep Dive Podcast into Betting Odds, Market Efficiency ... Understanding the Key Factors That Influence Betting Odds in ... Horse Racing Winning Odds Statistics: 2026 Market Report</a></li>

</ul>
</details>

**Tags**: `#market microstructure`, `#information aggregation`, `#parimutuel betting`, `#behavioral finance`, `#economics`

---

<a id="item-17"></a>
## [Endogenous Grid Method Extended to Epstein-Zin Preferences via Power Transformation](https://arxiv.org/abs/2601.04438) ⭐️ 8.0/10

The paper shows that applying a power transformation to the value function enables the endogenous grid method (EGM) to be used with Epstein-Zin preferences, eliminating the need for root-finding. The resulting algorithm achieves speed gains of one to two orders of magnitude over value function iteration and improves accuracy by more than one order of magnitude. This methodological advance allows economists to solve dynamic programming problems with Epstein-Zin preferences much faster and more accurately, facilitating larger-scale macro-finance models. By sidestepping the speed-accuracy tradeoff of traditional value function iteration and time iteration, it expands the feasible computational frontier for recursive utility models. The power transformation converts the Epstein-Zin Euler equation into a form invertible by EGM, yielding a root‑free algorithm that is two to three orders of magnitude faster than VFI at equal accuracy. Numerical experiments confirm speedups of 10‑1000× and accuracy improvements exceeding 10× over standard value function iteration.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: The endogenous grid method (EGM) is a numerical technique for solving dynamic programming problems by inverting the Euler equation to avoid root‑finding, originally devised by Chris Carroll. Epstein‑Zin preferences are a recursive utility specification that separates risk aversion from the elasticity of intertemporal substitution, widely used in macro‑finance and asset pricing. Because the value function appears inside the Euler equation for Epstein‑Zin preferences, standard EGM cannot be directly applied.

<details><summary>References</summary>
<ul>
<li><a href="https://julia.quantecon.org/dynamic_programming/egm_policy_iter.html">37. Optimal Growth III: The Endogenous Grid Method ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epstein-Zin_preferences">Epstein-Zin preferences</a></li>

</ul>
</details>

**Tags**: `#endogenous grid method`, `#Epstein-Zin preferences`, `#dynamic programming`, `#computational economics`, `#algorithmic improvement`

---

<a id="item-18"></a>
## [Cities Cluster into 17 Growth Regimes Propagating Economic Shocks](https://arxiv.org/abs/2603.16007) ⭐️ 8.0/10

Researchers built GDP trajectories for 8,808 functional urban areas across 165 countries from 1993 to 2019 using satellite-derived nighttime light data and identified 17 distinct, persistent growth regimes by clustering full temporal trajectories. The findings show that economic convergence occurs within these regimes rather than globally, revealing that shock transmission follows structural similarity rather than geography, which reshapes how we understand urban inequality and policy effectiveness. Regime membership accounts for 16% of within-country growth variance beyond country fixed effects; advanced economies tend to export shocks while emerging economies absorb or amplify them, and spatial inequality declines with industrialization maturity as growth diffuses from leading cities.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Functional urban areas (FUAs) capture the economic extent of cities based on commuting zones, not just administrative borders. Nighttime light satellite imagery serves as a proxy for economic activity, enabling GDP estimation where official data are scarce. Clustering full temporal trajectories groups cities by similar long-term growth patterns, volatility, and shock responses.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Functional_Urban_Area">Functional urban area - Wikipedia</a></li>
<li><a href="https://www.earthdata.nasa.gov/topics/human-dimensions/nighttime-lights">Nighttime Lights - NASA Earthdata</a></li>
<li><a href="https://arxiv.org/abs/2603.16007">[2603.16007] Cities cluster into growth regimes that ...</a></li>

</ul>
</details>

**Tags**: `#urban economics`, `#economic growth`, `#nighttime lights`, `#clustering analysis`, `#regional development`

---

<a id="item-19"></a>
## [Physics-informed VAE-Neural SDE Model for Arbitrage-free Yield Curve Forecasting](https://arxiv.org/abs/2605.12764) ⭐️ 8.0/10

The paper introduces a two-stage framework: first, a Student-t Conditional Variational Autoencoder with Dynamic Level Injection (CVAEsT+LS) learns a heavy-tailed term structure manifold; second, the latent dynamics are modeled by a Neural Stochastic Differential Equation (SDE) strictly penalized by a no-arbitrage Partial Differential Equation (PDE). Applied to USD, GBP, and JPY yield curves, the model achieves a 6.58 basis point Mean Tenor RMSE and eliminates parallel drift and zero‑lower‑bound violations seen in classical HJM models. By embedding the no‑arbitrage PDE constraint into a deep generative model, the approach reconciles the flexibility of neural networks with the rigorous theoretical requirements of fixed‑income modeling, thereby reducing arbitrage opportunities and improving forecast reliability for investors, regulators, and risk managers. The method also enables unsupervised macroeconomic regime detection and continuous‑time scenario generation, offering a scalable tool for term structure analysis across diverse economic environments. The model employs a Student‑t CVAE with Dynamic Level Injection to decouple macro‑economic shape dynamics from absolute base rates, capturing heavy‑tailed variations in yield curves. Latent evolution follows a Neural SDE whose loss includes a penalty term derived from the HJM no‑arbitrage PDE; empirical tests show a 6.58 bps Mean Tenor RMSE across USD, GBP, JPY curves and successful phase‑space vector field analysis for regime detection.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Yield curves represent the relationship between interest rates and time to maturity for debt securities, and their accurate modeling is essential for pricing, risk management, and monetary policy. The no‑arbitrage condition, formalized in the Heath‑Jarrow‑Morton (HJM) framework, imposes a partial differential equation that any admissible term‑structure model must satisfy to prevent risk‑free profit opportunities. Variational autoencoders (VAEs) are generative deep‑learning models that learn a low‑dimensional latent representation of data, while neural stochastic differential equations (SDEs) use neural networks to parameterize the drift and diffusion of continuous‑time dynamics. Physics‑informed generative models combine the flexibility of deep learning with physical laws expressed as differential equations, ensuring that generated samples respect known theoretical constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12764">[2605.12764] Yield Curves Dynamics Using Variational ... Yield Curve Dynamics Using Variational Autoencoders Under No ... Yield Curves Dynamics Using Variational ... - EconPapers Physics-guided deep learning for crop yield estimation A physics-informed GAN framework based on model-free data ... Yashsethi24/Forecast_Treasury_Curve - GitHub Exploring Physics-Informed Neural Networks for Crop Yield ...</a></li>
<li><a href="https://sungchullee.github.io/financial_math_book_writing/ch24/deep_learning/neural_sde_models/">Neural Stochastic Differential Equation Models - Quant ...</a></li>
<li><a href="https://mlanthology.org/iclr/2024/kim2024iclr-3variational/">$t^3$-Variational Autoencoder: Learning Heavy-Tailed Data ...</a></li>

</ul>
</details>

**Tags**: `#variational autoencoder`, `#yield curve modeling`, `#no-arbitrage`, `#neural SDE`, `#finance`

---

<a id="item-20"></a>
## [Probabilistic proof of continuous differentiability for optimal stopping boundaries.](https://arxiv.org/abs/2405.16636) ⭐️ 8.0/10

The authors provide the first probabilistic proof of continuous differentiability of time-dependent optimal stopping boundaries for one-dimensional, time-inhomogeneous diffusions with non‑smooth gain and discount, and they link the value function to the solution of Stefan’s problem. This result extends previous regularity results to much more general settings, impacting stochastic control, financial mathematics, and the theory of free‑boundary PDEs. The proof relies on local arguments that accommodate time‑and‑state‑dependent discount rates, finite or infinite horizons, and gain functions lacking smoothness, and as a byproduct establishes a probabilistic connection between the optimal stopping value function and the Stefan problem.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Optimal stopping problems involve deciding when to halt a stochastic process to maximize expected reward or minimize cost, and they are closely related to free‑boundary problems in PDE theory. A one‑dimensional time‑inhomogeneous diffusion is a stochastic process whose drift and volatility may vary with time, providing a flexible model for many applications. The Stefan problem describes the evolution of a phase‑change interface (e.g., ice‑water) and is a classic free‑boundary problem whose solution can be linked to the value function of certain optimal stopping tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2405.16636">[2405.16636] A probabilistic approach to continuous ... 14 Optimal stopping – Stochastic Control and Decision Theory OPTIMAL STOPPING PROBLEMS FOR TIME-HOMOGENEOUS ... - Springer [2110.03831v1] The Stefan problem and free targets of optimal ... Threshold Stopping Rules for Diffusion Processes and Stefan’s ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Optimal_stopping">Optimal stopping - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0168202408702947">Chapter VII Problems of Optimal Stopping - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#optimal stopping`, `#stochastic processes`, `#free boundary problems`, `#probability theory`, `#PDE`

---

<a id="item-21"></a>
## [Adaptive Partitioning RL for Unbounded Diffusion Processes with Regret Bounds](https://arxiv.org/abs/2512.14991) ⭐️ 8.0/10

The paper introduces a model-based reinforcement learning algorithm that adaptively partitions the joint state‑action space of controlled diffusion processes, maintaining estimators of drift, volatility and reward in each cell and refining the partition when estimation bias exceeds statistical confidence. It derives regret bounds that scale with horizon, state dimension, reward growth order and a newly defined zooming dimension, and validates the method on high‑dimensional finance tasks such as multi‑asset mean‑variance portfolio selection. By providing the first regret‑bound analysis for model‑based RL in unbounded continuous‑state diffusion settings, the work bridges theory and practice for problems arising in finance, economics and operations research. The bounds recover prior results for bounded domains as a special case, thereby extending guarantees to a broader class of stochastic control problems. The algorithm keeps separate drift, volatility and reward estimators per partition and triggers refinement when the bias exceeds a confidence threshold, balancing exploration and approximation. Regret bounds are expressed as O(√(H·d·ρ·ζ)) where H is horizon, d state dimension, ρ reward growth order and ζ the zooming dimension, reducing to known bounds when the state space is bounded. Numerical experiments include a 10‑asset mean‑variance portfolio selection problem demonstrating scalability.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Controlled diffusion processes describe the evolution of continuous‑state systems driven by stochastic differential equations, commonly used to model asset prices in finance. Reinforcement learning in such settings is challenging because the state space is infinite and high‑dimensional, making traditional tabular or function‑approximation methods inefficient. Model‑based RL approaches learn estimates of the system dynamics (drift and volatility) and reward function to plan or act adaptively. Adaptive partitioning refines the state‑action discretization only where needed, based on statistical confidence of the estimates, thereby mitigating the curse of dimensionality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.14991">[2512.14991] Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes</a></li>
<li><a href="https://arxiv.org/html/2512.14991v1">Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes</a></li>
<li><a href="https://thequant.space/flowcharts/adaptive-partitioning-and-learning-for-stochastic-control-of/">Adaptive Partitioning and Learning for Stochastic Control of ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#stochastic control`, `#diffusion processes`, `#adaptive partitioning`, `#regret bounds`

---

<a id="item-22"></a>
## [Universal approximation via Brownian motion signatures for stochastic processes.](https://arxiv.org/abs/2512.16396) ⭐️ 8.0/10

The authors prove that linear functionals acting on the signatures of time‑extended Brownian motion are dense in L^p for any p‑integrable adapted stochastic process, establishing an L^p universal approximation theorem for rough path spaces. This result appears in arXiv:2512.16396v2. This extends universal approximation theory to stochastic analysis, showing that signature‑based methods can model and learn from general stochastic differential equations and fractional Brownian motion. It bridges rough path theory with machine learning, impacting fields such as quantitative finance and path‑dependent modeling. The proof constructs weighted rough path spaces and demonstrates that linear signature functionals approximate any adapted process in L^p norm, including solutions to SDEs driven by Brownian filtration. The theorem further applies to Gaussian processes, notably fractional Brownian motion, by verifying the required regularity conditions.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Background**: Rough path theory provides a framework for defining differential equations driven by irregular signals such as fractional Brownian motion, where the signature of a path encodes its iterated integrals as elements of a tensor algebra. The expected signature plays a role analogous to the characteristic function of a random variable, capturing essential statistical information of the path. Universal approximation results for signatures show that linear functionals on these signatures can densely approximate continuous functionals on rough path spaces, a property now extended to L^p settings for Gaussian processes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rough_path">Rough path - Wikipedia</a></li>
<li><a href="https://projecteuclid.org/journals/annals-of-probability/volume-43/issue-5/Expected-signature-of-Brownian-motion-up-to-the-first-exit/10.1214/14-AOP949.pdf">Expected signature of Brownian motion up to the first exit ...</a></li>
<li><a href="https://arxiv.org/abs/2603.03058">[2603.03058] Universal approximation by signatures for ... Universal approximation by signatures for infinite ... Full article: Universal Approximation on Non-geometric Rough ... Notes on Signature and Rough Path Asma Khedher: Universal approximation by signatures for ... - KTH Universal Approximation on Non-geometric Rough Paths and ...</a></li>

</ul>
</details>

**Tags**: `#rough paths`, `#signature methods`, `#universal approximation`, `#stochastic analysis`, `#fractional Brownian motion`

---

<a id="item-23"></a>
## [AI Premium](https://arxiv.org/abs/2606.30583) ⭐️ 8.0/10

The authors construct an AI factor from massive LLM token consumption data and show that firms with higher AI beta earn excess returns, revealing a substantial and heterogeneous AI premium.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**Tags**: `#AI economics`, `#factor investing`, `#machine learning`, `#finance`, `#token consumption`

---