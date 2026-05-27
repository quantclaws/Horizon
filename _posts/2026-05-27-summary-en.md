---
layout: default
title: "Horizon Summary: 2026-05-27 (EN)"
date: 2026-05-27
lang: en
---

> From 64 items, 23 important content pieces were selected

---

1. [Wikimedia lays off key developers, sparks editor strikes over anti‑labor influence](#item-1) ⭐️ 8.0/10
2. [: ](#item-2) ⭐️ 8.0/10
3. [: ](#item-3) ⭐️ 8.0/10
4. [: Microsoft Copilot Cowork Exfiltrates Files via Prompt Injection](#item-4) ⭐️ 8.0/10
5. [: ](#item-5) ⭐️ 8.0/10
6. [: Study Reveals Personal Productivity Bias in ED Patient Batching](#item-6) ⭐️ 8.0/10
7. [: Entropy-Regularized Certainty-Equivalent Bellman Operator for Risk-Sensitive Market Making](#item-7) ⭐️ 8.0/10
8. [: ](#item-8) ⭐️ 8.0/10
9. [: ](#item-9) ⭐️ 8.0/10
10. [:Agent-Facing Information Design in LLM Tool Registries](#item-10) ⭐️ 8.0/10
11. [: Survey Examines Nondeterminism in Financial AI Systems for Auditability](#item-11) ⭐️ 8.0/10
12. [: Study of 5.5M M365 Copilot Chat Sessions Reveals Dominant Work Uses](#item-12) ⭐️ 8.0/10
13. [: ](#item-13) ⭐️ 8.0/10
14. [Market Regime Council boosts multi-agent LLM crypto trading performance.](#item-14) ⭐️ 8.0/10
15. [:Incremental SVD Framework for Dynamic Matrices with Refresh Strategies](#item-15) ⭐️ 8.0/10
16. [: Generative AI exposure concentrates in Beijing core, causing high‑skill wage stagnation.](#item-16) ⭐️ 8.0/10
17. [StakeBench introduces a market‑grounded financial NLP benchmark.](#item-17) ⭐️ 8.0/10
18. [: Study Shows Inflation Reduction Act Tax Credits Boost Renewable Energy Investment.](#item-18) ⭐️ 8.0/10
19. [:Physics-Informed VAE-SDE Framework for Arbitrage-Free Yield Curve Modeling](#item-19) ⭐️ 8.0/10
20. [The Impact of Large Language Models on Open-source Innovation: Evidence from GitHub Copilot](#item-20) ⭐️ 8.0/10
21. [: EXOTIC introduces an exact optimistic tree‑based algorithm for min‑max optimization.](#item-21) ⭐️ 8.0/10
22. [: SURGE: Approximation and Training Free Particle Filter for Diffusion Surrogate](#item-22) ⭐️ 8.0/10
23. [:We model builder defection in Ethereum MEV auctions.](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Wikimedia lays off key developers, sparks editor strikes over anti‑labor influence](https://medium.com/@jakeorlowitz/wikipedia-is-doing-the-capitalist-thing-56a393232943) ⭐️ 8.0/10

The Wikimedia Foundation laid off Brooke, one of MediaWiki’s original developers, and disbanded its community tech team that maintained the Community Wishlist feature‑request process. In response, many English Wikipedia editors have begun a strike, protesting the loss of volunteer‑supported tooling. The layoffs signal growing influence of big‑tech‑style cost‑cutting and anti‑labor practices within a nonprofit that relies on volunteer labor, threatening the sustainability of Wikipedia’s open‑source ecosystem. It highlights tensions between fundraising‑driven foundations and the volunteer communities that produce the content. Brooke was a longtime MediaWiki contributor once considered a potential BDFL (benevolent dictator for life) of the project. The community tech team, which built and maintained custom tools for editors via the Community Wishlist, was eliminated, leaving editors to maintain their own ad‑hoc infrastructure.

hackernews · cdrnsf · May 26, 20:33 · [Discussion](https://news.ycombinator.com/item?id=48285592)

**Background**: Wikipedia is hosted by the Wikimedia Foundation, a nonprofit that funds its operations through donations. The site runs on MediaWiki, an open‑source wiki platform originally developed by volunteers. The Foundation also supports community‑driven initiatives like the Community Wishlist, which lets editors request and prioritize new features or tools. Recent fundraising has given the Foundation a multi‑year operating reserve, but operating costs remain high.

**Discussion**: Commenters expressed shock at the loss of a foundational MediaWiki developer and concern that losing the community tech team undermines editor productivity. Some argued the Foundation’s financial reserves are fragile, while others criticized its fundraising focus and wished for its collapse.

**Tags**: `#Wikipedia`, `#labor`, `#open-source`, `#Wikimedia`, `#tech layoffs`

---

<a id="item-2"></a>
## [: ](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/) ⭐️ 8.0/10

The piece argues that pairing outsourcing with locally-run AI models will soon be cheaper than using costly frontier lab APIs, prompting debate about pricing, developer skill, and outsourcing effectiveness.

hackernews · GodelNumbering · May 26, 12:08 · [Discussion](https://news.ycombinator.com/item?id=48278610)

**Tags**: `#AI economics`, `#LLM pricing`, `#outsourcing`, `#local AI`, `#frontier models`

---

<a id="item-3"></a>
## [: ](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 8.0/10

Daniel Stenberg describes the curl team facing unprecedented pressure from a surge in high-quality AI-assisted security vulnerability reports.

rss · Simon Willison · May 26, 23:48

**Tags**: `#curl`, `#security`, `#AI`, `#open-source`, `#vulnerability-disclosure`

---

<a id="item-4"></a>
## [: Microsoft Copilot Cowork Exfiltrates Files via Prompt Injection](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

Microsoft Copilot Cowork can be tricked via prompt injection to send emails containing external images that, when opened, trigger network requests to attacker-controlled servers, enabling data exfiltration. This demonstrates a concrete prompt‑injection flaw in a widely deployed AI agent product, showing how such vulnerabilities can be used to steal sensitive files and underscoring the ongoing security challenges in agentic systems. The attack works because Copilot Cowork can send emails to the user’s inbox without approval, and those emails can embed external images that trigger outbound HTTP requests when rendered; additionally, OneDrive’s pre‑authenticated download links can be leaked, allowing attackers to download files directly.

rss · Simon Willison · May 26, 15:36

**Background**: Prompt injection is a technique where malicious inputs cause LLMs to behave unintentionally, often bypassing safety guards. Agentic systems use LLMs to autonomously decide and execute actions, such as sending emails or accessing files, increasing the impact of such injections. OneDrive can generate pre‑authenticated download links that allow anyone with the link to access a file without further authentication, which can be abused if leaked.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://www.mongodb.com/resources/basics/artificial-intelligence/agentic-systems">7 Practical Design Patterns for Agentic Systems | MongoDB</a></li>
<li><a href="https://support.microsoft.com/en-us/office/external-or-guest-sharing-in-onedrive-sharepoint-and-lists-7aa070b8-d094-4921-9dd9-86392f2a79e7">External or guest sharing in OneDrive, SharePoint, and Lists - Microsoft Support</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#Microsoft Copilot`, `#data exfiltration`, `#agentic systems`

---

<a id="item-5"></a>
## [: ](https://arxiv.org/abs/2605.23905) ⭐️ 8.0/10

The paper models how widespread AI investment strategies accelerate signal decay, reducing alpha half-life from years to months via crowding, performative erosion, and Red Queen competition.

rss · arXiv Quantitative Finance · May 26, 04:00

**Tags**: `#AI finance`, `#algorithmic trading`, `#market efficiency`, `#alpha decay`, `#quantitative finance`

---

<a id="item-6"></a>
## [: Study Reveals Personal Productivity Bias in ED Patient Batching](https://arxiv.org/abs/2605.24208) ⭐️ 8.0/10

Using data from 1.4 million emergency department visits across five hospitals, researchers found that physicians frequently batch‑assign multiple patients at once, which lengthens patient stays even after controlling for acuity and congestion. This batching behavior persisted in experiments with healthcare workers and physicians, occurring even when it reduced their own payoffs, a tendency the authors label the personal productivity bias. The findings show that simply changing financial incentives is unlikely to eliminate batching, suggesting that redesigning electronic health record assignment interfaces may be a more effective lever to improve patient flow. This contributes to healthcare operations research by linking behavioral tendencies to queueing performance in emergency departments. In the empirical sample, 94% of 203 healthcare workers and 73% of 73 ED physicians chose to batch even when it lowered their personal earnings. The study also presents a continuous‑time queueing model that characterizes optimal self‑assignment under individual and group throughput incentives, and uses its predictions to interpret the experimental results.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Emergency departments often operate with a shared queue where triaged patients wait and physicians self‑assign cases from that pool. This setting creates a queueing system in which decisions about how many patients to take at once (batching) affect both physician workload and patient waiting times. Classical queueing theory predicts optimal assignment policies under various incentive structures, but real‑world behavior can deviate due to cognitive biases or habits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/emergency-department-queuing-theory-why-small-delays-trigger-mirani-4idoe">Emergency Department & Queuing Theory. Why Small Delays...</a></li>
<li><a href="https://www.academia.edu/47464791/Healthcare_queueing_models">(PDF) Healthcare queueing models</a></li>
<li><a href="https://arxiv.org/abs/2605.24208">[2605.24208] One at a Time? The Personal Productivity Bias in Emergency Department Patient Assignment</a></li>

</ul>
</details>

**Tags**: `#healthcare operations`, `#emergency department`, `#queueing theory`, `#behavioral economics`, `#productivity bias`

---

<a id="item-7"></a>
## [: Entropy-Regularized Certainty-Equivalent Bellman Operator for Risk-Sensitive Market Making](https://arxiv.org/abs/2605.24878) ⭐️ 8.0/10

The paper introduces an exact discrete entropy-regularized Bellman operator that applies log-sum-exp regularization to deterministic-action certainty-equivalent scores for finite‑inventory risk‑sensitive market making, and proves its uniform convergence to the continuous‑time risk‑sensitive value with rate O(h+λ(1+|log λ|)). By providing a provably convergent entropy‑regularized method for risk‑sensitive market making, the work bridges reinforcement learning and financial engineering, offering algorithmic traders a principled way to manage inventory risk while guaranteeing performance bounds. The operator uses log‑sum‑exp on deterministic‑action certainty‑equivalent scores rather than on a risk‑neutral reward, and under a quadratic growth condition on the Hamiltonian the induced Gibbs policies concentrate around the optimal quote set; a cheaper Hamiltonian‑Gibbs proxy attains the same order performance bound.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: In risk‑sensitive market making a dealer sets bid and ask quotes while facing Brownian midprice risk and receiving liquidity‑taking orders modeled as point processes with quote‑dependent intensities. The performance criterion is the certainty equivalent derived from exponential utility, which incorporates terminal and running inventory penalties. A Bellman operator updates the value function by aggregating one‑step returns; entropy regularization adds a log‑sum‑exp term to encourage exploration and improve stability. Applying this regularization to the certainty‑equivalent score (instead of a risk‑neutral reward) yields a novel operator that preserves the risk‑sensitive structure while enabling provable convergence.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.24878">[2605.24878] Entropy-Regularized Certainty-Equivalent Bellman ...</a></li>
<li><a href="https://www.emergentmind.com/topics/regularized-bellman-operators">Regularized Bellman Operators - emergentmind.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Exponential_utility">Exponential utility - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#market making`, `#risk-sensitive reinforcement learning`, `#entropy regularization`, `#Bellman operator`, `#financial mathematics`

---

<a id="item-8"></a>
## [: ](https://arxiv.org/abs/2605.25392) ⭐️ 8.0/10

The study models why onshore (CNY) and offshore (CNH) Renminbi forwards diverge despite linked spot prices, attributing the gap to transaction costs and segmented supply.

rss · arXiv Quantitative Finance · May 26, 04:00

**Tags**: `#Renminbi`, `#FX markets`, `#Onshore-offshore`, `#Forward pricing`, `#Financial markets`

---

<a id="item-9"></a>
## [: ](https://arxiv.org/abs/2605.25438) ⭐️ 8.0/10

The study finds that adopting Claude Code significantly increases developers' commit activity, repository contributions, language diversity, and acquisition of new programming languages over time.

rss · arXiv Quantitative Finance · May 26, 04:00

**Tags**: `#AI coding assistants`, `#software engineering`, `#empirical study`, `#developer productivity`, `#Claude Code`

---

<a id="item-10"></a>
## [:Agent-Facing Information Design in LLM Tool Registries](https://arxiv.org/abs/2605.23916) ⭐️ 8.0/10

The study analyzed over 17,700 trials across five LLMs and ten domains, finding that subjective superlatives in tool descriptions fully drive agent selection while false claims and system‑prompt warnings have negligible impact. It shows that LLM tool registries operate like unregulated advertising where marketing copy outweighs actual capability, suggesting that registry‑level interventions—such as separating selection‑facing and marketing‑facing descriptions and introducing an Agent Attention Quality Score—are needed to ensure trustworthy AI tool markets. Subjective superlatives alone accounted for 100% of the optimization effect (SBC = +0.35); fabricated claims added zero bias; system‑prompt warnings produced no measurable effect for four of five models; and registry‑layer description normalization achieved first‑best welfare independently of the underlying model.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: LLM tool registries are platforms where providers write free‑text descriptions that agents read to select tools, yet they lack viewability standards, quality scores, or outcome audits that would make the marketplace accountable. System prompts are instructions given to LLMs to guide their behavior, but warnings embedded in these prompts often fail to influence model choices, as shown by the study’s null effect for most models.

<details><summary>References</summary>
<ul>
<li><a href="https://toolregistry.readthedocs.io/">Home - ToolRegistry</a></li>
<li><a href="https://arxiv.org/html/2507.10593v1">ToolRegistry: A Protocol-Agnostic Tool Management Library for ...</a></li>
<li><a href="https://arxiv.org/abs/2412.13426">PromptKeeper: Safeguarding System Prompts for LLMs Safeguarding System Prompts for LLMs - OpenReview PromptKeeper : Safeguarding System Prompts for LLMs LLM Prompt Injection Prevention - OWASP Cheat Sheet Series PromptGuard a structured framework for injection resilient ... System Prompt Leakage Vulnerability in LLM | SecureFlag ... www-project-top-10-for-large-language-model-applications/2_0 ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#tool registries`, `#AI safety`, `#advertising`, `#prompt engineering`

---

<a id="item-11"></a>
## [: Survey Examines Nondeterminism in Financial AI Systems for Auditability](https://arxiv.org/abs/2605.23955) ⭐️ 8.0/10

The paper surveys sources of nondeterminism in tabular models, graph neural networks, and LLM‑based agentic workflows used in financial AI, quantifying their impact on reproducibility and auditability. It also proposes a layered evaluation framework linking modality‑specific metrics to audit readiness. Deterministic and auditable AI is essential for regulated finance, where regulators require reproducible models for credit risk, fraud detection, and anti‑money laundering. The survey highlights practical gaps and offers metrics that can help institutions meet compliance and reduce risk. Experiments on public financial datasets measured explanation rank instability (RBO), prediction flip rates in GNN fraud detection (D_cos), and tensor‑parallel‑induced output divergence in LLM entity extraction (TDI, PSD). The survey introduces a layered evaluation framework that combines logit‑level and semantic‑level determinism measures.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Determinism in AI refers to producing identical outputs given the same inputs, which is crucial for reproducibility and auditability. In financial AI, sources of nondeterminism include hardware‑level variability, stochastic sampling in graph neural networks, and batch‑dependent behavior in large language model agents. Understanding these sources helps regulated institutions ensure their models can be trusted and verified.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Graph_neural_network">Graph neural network - Wikipedia</a></li>
<li><a href="https://distill.pub/2021/gnn-intro/">A Gentle Introduction to Graph Neural Networks</a></li>
<li><a href="https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns">Agentic Workflows in 2026: The ultimate guide</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#Financial Systems`, `#Reproducibility`, `#Auditability`, `#Determinism`

---

<a id="item-12"></a>
## [: Study of 5.5M M365 Copilot Chat Sessions Reveals Dominant Work Uses](https://arxiv.org/abs/2605.23958) ⭐️ 8.0/10

The paper analyzed 5.5 million anonymized M365 Copilot Chat sessions, classifying user intent and mapping activities to O*NET work categories, finding writing, information retrieval, analysis, decision‑making and system evaluation as dominant uses. It provides large‑scale, privacy‑preserving empirical evidence of how AI assistants are embedded in everyday knowledge work, helping enterprises understand adoption patterns and guide future AI investments. The study combined a learned intent classifier with O*NET activity tags on a sample of ~5.5 M sessions, showing a shift from “chat as search” toward content‑creation and communication tasks and highlighting uneven adoption across occupations.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Microsoft 365 Copilot Chat is an AI‑powered conversational assistant integrated into Microsoft 365 apps, allowing users to access agents, upload files, generate images, and retrieve work‑related information through natural language. The O*NET system, maintained by the U.S. Department of Labor, categorizes occupations and work activities using a standardized database of over 1,000 occupation titles, enabling researchers to map AI usage to specific job functions. Together, these tools let the study link real‑world AI interactions to established labor‑market classifications.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/copilot/overview">Overview of Microsoft 365 Copilot Chat | Microsoft Learn</a></li>
<li><a href="https://www.dol.gov/agencies/eta/onet">O *NET | U.S. Department of Labor</a></li>

</ul>
</details>

**Tags**: `#AI in the Enterprise`, `#M365 Copilot`, `#Human‑AI Interaction`, `#Workplace Analytics`, `#Empirical Study`

---

<a id="item-13"></a>
## [: ](https://arxiv.org/abs/2605.23978) ⭐️ 8.0/10

Introduces algometrics to separate historical risk from deployment risk in forecasting models that influence the data they predict.

rss · arXiv Quantitative Finance · May 26, 04:00

**Tags**: `#algorithmic feedback`, `#time series forecasting`, `#deployment risk`, `#machine learning theory`, `#econometrics`

---

<a id="item-14"></a>
## [Market Regime Council boosts multi-agent LLM crypto trading performance.](https://arxiv.org/abs/2605.24490) ⭐️ 8.0/10

The paper introduces Market Regime Council (MRC), a cooperative multi-agent LLM system that assigns exact Shapley credits across all agent coalitions and applies regime‑adaptive multipliers to weight agents. Over 1,037 trading days on 13 crypto assets, MRC achieves a Sharpe ratio of 1.51 and a cumulative return of 440.1%. MRC solves the credit‑assignment and cold‑start problems that hinder multi‑agent LLM portfolio systems, offering a transparent, principled way to combine specialist models. Its strong risk‑adjusted returns demonstrate that LLM‑based multi‑agent approaches can compete with traditional quantitative strategies in crypto markets. MRC uses three specialist agents, recomputes exact Shapley values for single, pairwise and grand‑coalition outputs each period from exponentially weighted performance histories, stabilizes early periods with a Bayesian adaptive mixture, and applies regime‑dependent multipliers to adjust agent authority. Ablation studies show that performance gains stem from the Shapley‑weighted integration of coalition outputs rather than any individual component.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Multi‑agent LLM decision systems deploy several language‑model‑based specialists to propose portfolio actions, but lack a principled method to credit each agent’s contribution, especially when market regimes shift. Shapley values from cooperative game theory provide a fair, exact attribution of each agent’s marginal contribution across all possible coalitions. A Bayesian adaptive mixture smooths early‑period estimates by treating agent outputs as a mixture of expert distributions, reducing cold‑start dominance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.24490">[2605.24490] Market Regime Council for Dynamic Credit ...</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/market-regime-council-dynamic-credit-assignment-multi">Market Regime Council for Dynamic Credit Assignment in Multi ...</a></li>
<li><a href="https://peerj.com/articles/cs-3630.pdf">Adaptive LLM-based multi-agent systems to enhance ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#large language models`, `#portfolio optimization`, `#Shapley values`, `#cryptocurrency trading`

---

<a id="item-15"></a>
## [:Incremental SVD Framework for Dynamic Matrices with Refresh Strategies](https://arxiv.org/abs/2605.24514) ⭐️ 8.0/10

The paper presents a metric-driven incremental SVD framework that derives an explicit projection-based rank-1 update rule $U'\Sigma'(V')^\top = P_U(\widehat{A} + \delta e_i e_j^\top)P_V$ and systematically compares refresh policies (periodic, error-threshold, angle-threshold, adaptive-rank) on accuracy-latency trade-offs. It evaluates the method on synthetic streams and a multi-asset ETF factor model for covariance and portfolio-risk estimation. By enabling low-rank factorizations to be updated efficiently as matrices change entry-by-entry, the method makes high-frequency streaming data and real-time financial risk modeling tractable where full SVD would be prohibitive. It bridges theory and practice for dynamic matrix approximation in large-scale applications. The update rule keeps the rank fixed while discarding only the quantifiable out-of-subspace remainder, turning Brand's rank-suppression heuristic into an operational scheme. A unified engine handles row appends, column appends, and rank-1 entry updates, and refresh scheduling is treated as a first-class design axis. Experiments show that with a sensible rank and refresh cadence, incremental SVD matches full-SVD accuracy within a few percent at a fraction of the computational cost.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Incremental SVD seeks to maintain a low-rank approximation $A_t \approx U_t\Sigma_t V_t^\top$ as a matrix evolves, avoiding the O(n^3) cost of recomputing a full SVD at each step. The foundational Brand algorithm (2002) processes rank-1 updates but historically relied on heuristics that could suppress rank or lose orthogonality. Recent work treats refresh scheduling as a design choice to balance accuracy against latency, especially for streaming or financial data where matrices change one observation or entry at a time.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.24514">Incremental SVD for Large-Scale Dynamic Matrices: Accuracy ...</a></li>
<li><a href="https://github.com/bchaoss/incremental-SVD">GitHub - bchaoss/ incremental - SVD : An improved incremental ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Singular_value_decomposition">Singular value decomposition - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#incremental SVD`, `#matrix factorization`, `#streaming data`, `#financial risk models`, `#low-rank approximation`

---

<a id="item-16"></a>
## [: Generative AI exposure concentrates in Beijing core, causing high‑skill wage stagnation.](https://arxiv.org/abs/2605.25505) ⭐️ 8.0/10

Using five million Beijing job postings from 2018 to 2024, researchers built a neighborhood‑level GenAI Exposure Index from assessments by five large language models and found that exposure is highest in the city’s core districts. Since 2023, high‑exposure neighborhoods have seen wage stagnation despite continued inflows of high‑skilled workers, a phenomenon the authors call a high‑skill trap, driven by task de‑skilling and labor‑market crowding, supported by a difference‑in‑differences design around ChatGPT’s release. The findings challenge the traditional skill‑biased technological change view by showing that advanced AI can depress wages for high‑skill workers in concentrated urban areas. This highlights a new form of intra‑urban inequality that policymakers must address when designing inclusive AI governance for global technology hubs. The study covers 2018‑2024 job ads, aggregates task‑level exposure scores from five LLMs, and applies a DiD approach centered on the November 2022 ChatGPT release to estimate causal effects. Wage penalties are attributed to task de‑skilling and intensified labor‑market crowding in high‑exposure neighborhoods.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Generative AI refers to AI systems that can produce text, images, or other content, and recent advances in large language models have enabled automation of high‑cognitive tasks previously thought immune to machines. Skill‑biased technological change theory predicts that new technologies raise demand for skilled workers, but this study shows the opposite effect in localized high‑exposure areas. To measure exposure, the authors use O*NET task descriptions mapped to LLM capabilities, a method described in the AI Exposure Index methodology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aiexposure.org/analysis/genai-exposure-methodology">How We Score GenAI Exposure: O*NET Tasks Meet Large Language ...</a></li>
<li><a href="https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure">Generative AI and Jobs: A Refined Global Index of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#labor economics`, `#urban inequality`, `#skill premium`, `#Beijing`

---

<a id="item-17"></a>
## [StakeBench introduces a market‑grounded financial NLP benchmark.](https://arxiv.org/abs/2605.26074) ⭐️ 8.0/10

StakeBench links 560,876 comments from 2,261 resolved Polymarket and Manifold markets to verified positions, actions, and odds, using observable market behavior as supervision. By grounding language understanding in actual market commitments rather than human‑annotated sentiment, StakeBench offers a more objective measure of financial NLP performance and reveals model limitations in higher‑order reasoning. The benchmark defines four diagnostic tasks (detecting commitment, identifying revealed side, anticipating future action, projecting collective odds) and three commitment‑aware metrics; experiments on 15 LLMs show directed accuracy between 0.506 and 0.599 for side identification but structural failures on later tasks, with no correlation to model scale or finance‑domain tuning.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Financial NLP evaluation traditionally relies on labels created by external annotators, which capture perceived sentiment rather than the speaker’s actual market positions. Prediction markets such as Polymarket and Manifold record users’ trades, positions, and odds, providing observable evidence of commitment to a viewpoint. StakeBench leverages this market‑generated data to replace human annotation with supervision derived from real trading behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26074">[2605.26074] StakeBench: Evaluating Language Understanding ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polymarket">Polymarket - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Manifold_(prediction_market)">Manifold (prediction market)</a></li>

</ul>
</details>

**Tags**: `#NLP`, `#financial NLP`, `#benchmark`, `#prediction markets`, `#language understanding`

---

<a id="item-18"></a>
## [: Study Shows Inflation Reduction Act Tax Credits Boost Renewable Energy Investment.](https://arxiv.org/abs/2604.00582) ⭐️ 8.0/10

The study finds that renewable energy tax credits led to substantial increases in renewable capital and generation, with elasticities that diminish when accounting for inframarginal investment.

rss · arXiv Quantitative Finance · May 26, 04:00

**Tags**: `#energy policy`, `#renewable energy`, `#tax credits`, `#Inflation Reduction Act`, `#economic impact`

---

<a id="item-19"></a>
## [:Physics-Informed VAE-SDE Framework for Arbitrage-Free Yield Curve Modeling](https://arxiv.org/abs/2605.12764) ⭐️ 8.0/10

The paper introduces a two-stage physics-informed generative model combining a Student-t Conditional Variational Autoencoder with Dynamic Level Injection (CVAEsT+LS) and a continuous-time Neural Stochastic Differential Equation (SDE) constrained by a no-arbitrage partial differential equation (PDE) to model yield curve dynamics. By enforcing no-arbitrage conditions, the framework mitigates manifold collapse and arbitrage violations that plague standard generative models, delivering substantially lower out-of-sample forecasting errors (6.58 bps Mean Tenor RMSE) across major currencies and offering a scalable tool for quantitative finance. The first stage uses a heavy-tailed Student-t CVAE with dynamic level injection to separate macroeconomic shape dynamics from base rates, while the second stage evolves latents via a neural SDE penalized by the no-arbitrage PDE; experiments on USD, GBP, and JPY term structures show reduced parallel drift and zero-lower-bound violations compared to the classical Heath-Jarrow-Morton (HJM) model.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Yield curves depict the relationship between interest rates and time to maturity for debt securities, and arbitrage-free modeling requires that these curves satisfy certain partial differential equations to prevent risk‑free profit opportunities. Variational autoencoders are generative deep‑learning models that learn a probabilistic latent representation of data, while stochastic differential equations describe the continuous‑time evolution of financial variables under random shocks. Physics‑informed neural networks embed known physical laws (here, the no‑arbitrage PDE) into the training process to guide the model toward theoretically sound solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Variational_autoencoder">Variational autoencoder - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stochastic_differential_equation">Stochastic differential equation - Wikipedia</a></li>
<li><a href="https://ar5iv.labs.arxiv.org/html/2310.04173">[2310.04173] A physics - informed generative model for passive...</a></li>

</ul>
</details>

**Tags**: `#variational autoencoder`, `#yield curve modeling`, `#no-arbitrage`, `#stochastic differential equation`, `#financial machine learning`

---

<a id="item-20"></a>
## [The Impact of Large Language Models on Open-source Innovation: Evidence from GitHub Copilot](https://arxiv.org/abs/2409.08379) ⭐️ 8.0/10

Using a natural experiment around GitHub Copilot's October 2021 launch, the study finds that Copilot availability boosts open-source contributions by 28‑40 %, with a significantly larger increase in incremental contributions than in substantive contributions. The paper provides rare causal field evidence on how LLMs affect voluntary, self‑guided innovation, showing that AI assistance tilts open‑source collaboration toward exploiting existing code rather than exploring new functionality. The researchers employed three complementary identification strategies and two classification approaches to distinguish substantive from incremental contributions, and found the Copilot‑induced gap widens in highly active projects and after a model upgrade.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Large language models (LLMs) are AI systems that generate text or code based on patterns learned from vast datasets, and GitHub Copilot is an LLM‑powered code completion tool launched in October 2021. In open‑source software development, contributions can be classified as substantive, which require creative problem formulation to add new functionality, or incremental, which involve understanding and modifying existing code to maintain or improve it. The study exploits the fact that Copilot initially supported languages like Python but not R, creating an exogenous partition between otherwise comparable ecosystems to estimate its causal impact.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI pair programmer</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source`, `#GitHub Copilot`, `#software engineering`, `#empirical study`

---

<a id="item-21"></a>
## [: EXOTIC introduces an exact optimistic tree‑based algorithm for min‑max optimization.](https://arxiv.org/abs/2508.12479) ⭐️ 8.0/10

The paper introduces EXOTIC, an exact optimistic tree‑based algorithm that computes global minimax values for convex‑non‑concave and non‑convex‑concave min‑max problems by reformulating them as a max‑min task and combining an inner convex optimizer with an outer hierarchical tree search. Existing gradient‑based methods can converge only to approximate saddle points that may be arbitrarily far from the true optimum in non‑convex/non‑concave settings, whereas EXOTIC provides provable exact solutions, filling a critical gap in optimization theory and benefiting areas such as adversarial machine learning and multi‑player game theory. EXOTIC first applies a Sion‑type minimax theorem extension to convert the original problem into a non‑concave‑convex max‑min formulation, then uses an iterative convex solver for the inner minimization and an optimistic hierarchical tree search (inspired by StroquOOL) for the outer maximization, handling deterministic biased errors from finite‑time inner solutions and providing an upper bound on the optimality gap.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Min‑max optimization appears in game theory, adversarial machine learning, and robust control, where one seeks to minimize a loss while an adversary maximizes it. In the convex‑concave case, Sion’s minimax theorem guarantees that gradient‑based methods converge to a saddle point, but when convexity or concavity is missing, such methods may converge to points far from the global optimum. The paper extends Sion’s theorem to convex‑non‑concave and non‑convex‑concave settings, enabling exact algorithms like EXOTIC to compute the true minimax value.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.12479v2">EXOTIC: An Exact, Optimistic, Tree-Based Algorithm for Min ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Minimax_theorem">Minimax theorem - Wikipedia</a></li>
<li><a href="https://www.semanticscholar.org/paper/EXOTIC:-An-Exact,-Optimistic,-Tree-Based-Algorithm-Maheshwari-Pimpalkhare/dc009afbe05f0bf5120b3cfd2991b05644633034">EXOTIC: An Exact, Optimistic, Tree-Based Algorithm for Min ...</a></li>

</ul>
</details>

**Tags**: `#optimization`, `#min-max`, `#convex-non-concave`, `#algorithm`, `#game theory`

---

<a id="item-22"></a>
## [: SURGE: Approximation and Training Free Particle Filter for Diffusion Surrogate](https://arxiv.org/abs/2605.18745) ⭐️ 8.0/10

The paper introduces SURGE, a training‑free particle filter that treats a diffusion model as a world model and uses observation likelihood to guide the diffusion process, then applies Sequential Monte Carlo over the diffusion trajectory to reweight and resample particles for unbiased state estimation in data assimilation. By combining diffusion‑model priors with particle filtering, SURGE offers a training‑free, principled way to fuse noisy observations with learned dynamics, potentially improving data assimilation for complex dynamical systems and advancing ML‑based surrogate modeling. SURGE represents the posterior with a set of particles, guides the diffusion model using observation likelihood to steer samples toward observation‑consistent states, and then applies a Sequential Monte Carlo reweighting‑resampling step over the diffusion trajectory (viewed as a path measure) to correct the generation and ensure convergence to the true posterior.

rss · arXiv Quantitative Finance · May 26, 04:00

**Background**: Data assimilation (DA) seeks to estimate the evolving state of a dynamical system from noisy, sparse observations by combining a forecast model with measurement information. Diffusion models, particularly score‑based variants, have emerged as powerful generative priors that can learn complex stochastic dynamics from data. Particle filtering (Sequential Monte Carlo) approximates Bayesian posteriors by propagating a set of weighted samples (particles) through time and resampling based on likelihood. Recent work shows that diffusion models can serve as world models in DA, but guiding them with observations alone does not guarantee sampling from the true posterior, motivating the SURGE approach.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.18745v1">SURGE: Approximation-free Training Free Particle Filter for ...</a></li>
<li><a href="https://arxiv.org/abs/2506.02249">[2506.02249] Using Diffusion Models to do Data Assimilation</a></li>
<li><a href="https://arxiv.org/html/2402.07487">Score-based diffusion models via stochastic differential ...</a></li>

</ul>
</details>

**Tags**: `#data assimilation`, `#diffusion models`, `#particle filtering`, `#dynamical systems`, `#machine learning`

---

<a id="item-23"></a>
## [:We model builder defection in Ethereum MEV auctions.](https://arxiv.org/abs/2605.22667) ⭐️ 8.0/10

The paper models how block builders' probabilistic defection affects searcher bidding strategies and auction revenue in Ethereum MEV markets, combining theory with empirical measurement.

rss · arXiv Quantitative Finance · May 26, 04:00

**Tags**: `#MEV`, `#Ethereum`, `#auction theory`, `#blockchain`, `#game theory`

---