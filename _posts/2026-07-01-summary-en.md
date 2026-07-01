---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 69 items, 21 important content pieces were selected

---

1. [Anthropic releases Claude Sonnet 5, a new agentic-focused AI model](#item-1) ⭐️ 8.0/10
2. [Anthropic launches Claude Science AI assistant for data science](#item-2) ⭐️ 8.0/10
3. [Hacker News discusses 1852 classic on crowd delusions and financial bubbles](#item-3) ⭐️ 8.0/10
4. [Formalizing the Fundamental Theorem of Asset Pricing in Lean 4](#item-4) ⭐️ 8.0/10
5. [Supply Chain-Augmented LLM Embeddings Predict Stock Returns](#item-5) ⭐️ 8.0/10
6. [Bayesian optimization finds optimal carbon taxes on low-dimensional equilibrium manifolds.](#item-6) ⭐️ 8.0/10
7. [Adaptive AI Delegation via Bayesian Governance-Aware POMDP](#item-7) ⭐️ 8.0/10
8. [Swiss cartel mimicked competition to hide bid‑rigging.](#item-8) ⭐️ 8.0/10
9. [A General Theory of Paths: Signatures, Jump Lifts, and Expected Signatures of Self-Exciting Processes](#item-9) ⭐️ 8.0/10
10. [LLM Compression of Financial Texts Can Distort Investment Decisions](#item-10) ⭐️ 8.0/10
11. [CLQT: Closed-Loop, Cost-Aware Benchmark for LLM Portfolio-Management Agents](#item-11) ⭐️ 8.0/10
12. [Permutation-Invariant Fine-Tuning Makes Metadata Retrieval Robust to Field Order](#item-12) ⭐️ 8.0/10
13. [AI Premium Identified via 380 Trillion Tokens of LLM Usage](#item-13) ⭐️ 8.0/10
14. [Deep Neural Networks Yield Linear Factor Models via Portfolio Tangent Kernel](#item-14) ⭐️ 8.0/10
15. [Equilibrium Transition from Loss-Leader Competition: How Advertising Restrictions Facilitate Price Coordination in Chilean Pharmaceutical Retail](#item-15) ⭐️ 8.0/10
16. [Formal Lean 4 Library for Mathematical Finance with Ito Integral and Risk-Neutral Measure](#item-16) ⭐️ 8.0/10
17. [Machine-Checked Ito Calculus for Brownian Motion in Lean 4](#item-17) ⭐️ 8.0/10
18. [China's domestic science now exceeds US contributions in patents.](#item-18) ⭐️ 8.0/10
19. [Study Links Corporate Landlord Concentration to Faster Rent Growth in Minority Neighborhoods](#item-19) ⭐️ 8.0/10
20. [Weighted universal approximation of differentiable maps on infinite-dimensional manifolds](#item-20) ⭐️ 8.0/10
21. [KineticSim boosts market simulator throughput to 54.7B events per second.](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic releases Claude Sonnet 5, a new agentic-focused AI model](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic unveiled Claude Sonnet 5, the first Sonnet-tier model with real-time cybersecurity safeguards and a focus on agentic behavior, making it the default model for Free and Pro plans and available across all tiers. The release signals Anthropic's push toward safer, more autonomous AI agents, offering developers a cheaper alternative for agentic tasks while highlighting ongoing cost‑performance trade‑offs with the higher‑end Opus models. Claude Sonnet 5 shows a lower rate of undesirable behaviors than Sonnet 4.6 but a markedly reduced ability to perform cybersecurity tasks compared with Opus models, and it is positioned as the first Sonnet model with real‑time cybersecurity safeguards.

hackernews · marinesebastian · Jun 30, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48736605)

**Background**: The Claude Sonnet series is Anthropic's mid‑tier line of large language models, sitting between the lightweight Haiku and the high‑performance Opus models. Agentic AI refers to systems that can autonomously plan, use tools such as browsers or terminals, and execute multi‑step tasks with minimal human intervention. Previous versions like Sonnet 4.6 and Opus 4.8 set benchmarks for reasoning and tool use, while Sonnet 5 introduces real‑time cybersecurity refusals to improve safety in agentic contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5">What's new in Claude Sonnet 5 - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Commenters debated the model's cost‑effectiveness, noting that Opus often delivers better performance per dollar and that Sonnet 5 only makes sense at low effort levels or when Opus credits are exhausted. Some praised its stronger agentic capabilities for tool use and autonomous planning, while others pointed out weaknesses in general knowledge, tool‑calling reliability, and the impact of cybersecurity refusals on utility.

**Tags**: `#Claude Sonnet 5`, `#Anthropic`, `#LLM`, `#AI agents`, `#model release`

---

<a id="item-2"></a>
## [Anthropic launches Claude Science AI assistant for data science](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic introduced Claude Science, an AI assistant tailored for data science that runs a local Model Context Protocol server and provides a web‑based UI connecting to institutional clusters, databases, and computational tools. By enabling LLMs to operate inside secure, on‑premises environments, Claude Science bridges the gap between advanced AI and existing high‑performance computing and data workflows, potentially accelerating research in fields such as pharma and biotech. Claude Science runs a local MCP server with a desktop extension, integrates with Jupyter‑style notebooks, databases, and HPC clusters, and produces auditable artifacts while allowing flexible compute access; early users noted its approach can be naive and limited in off‑target screening for certain biological designs.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: Claude is Anthropic’s next‑generation AI assistant designed to be safe, accurate, and secure for general productivity tasks. The Model Context Protocol (MCP) is an open standard that lets LLM applications connect to external data sources and tools, and its local server variant lets users run connectors on their own machines for privacy. Institutional clusters, such as those provided by Columbia University’s Shared Research Computing Facility or Stanford’s HPCC, are high‑performance computing resources shared across research groups to run large simulations and data analyses. Claude Science builds on these components to give scientists a private, controllable AI workbench that can tap into their organization’s HPC and data stores.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop">Getting Started with Local MCP Servers on Claude Desktop</a></li>
<li><a href="https://www.cuit.columbia.edu/shared-research-computing-facility">High Performance Computing — HPC | Columbia University ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised Claude Science’s local server architecture and its ability to connect to institutional HPC, databases, and tools, noting its immediate utility for data‑science workflows. Some users, after testing it in specialized domains like RNAi‑based pesticide design, found the AI’s suggestions useful but noted naive approaches and limited off‑target screening, indicating room for improvement. Overall, the discussion reflects strong interest in the product’s integrations while highlighting concerns about maturity and the need for more sophisticated scientific reasoning.

**Tags**: `#AI`, `#Data Science`, `#Anthropic`, `#Claude`, `#Scientific Computing`

---

<a id="item-3"></a>
## [Hacker News discusses 1852 classic on crowd delusions and financial bubbles](https://www.gutenberg.org/ebooks/24518) ⭐️ 8.0/10

A Hacker News post linking to the 1852 book 'Memoirs of Extraordinary Popular Delusions and the Madness of Crowds' sparked a discussion about its historical accounts of financial bubbles and crowd behavior. The discussion shows how the book’s insights into mass psychology remain relevant today, informing modern behavioral economics and interpretations of market manias such as AI‑stock speculation. Commenters highlighted the book’s vivid tales of Tulip mania, the South Sea Bubble and the Mississippi Company, while noting that some stories are embellished and mentioning related works like John Kenneth Galbraith’s 'A Short History of Financial Euphoria'.

hackernews · lstodd · Jun 30, 12:47 · [Discussion](https://news.ycombinator.com/item?id=48731989)

**Background**: Written by Scottish journalist Charles Mackay and first published in 1841, the book collects popular myths, scandals and schemes, focusing on how mass enthusiasm can drive speculative manias. It has become a classic reference in the study of crowd psychology and financial bubbles, influencing later works in economics, sociology and psychology.

**Discussion**: Commenters praised the book’s entertaining anecdotes, such as the fake investment stall during the South Sea Bubble, while some argued that Mackay exaggerates events like Tulip mania. Others referenced related reads, reflected on personal lessons about irrationality, and linked the discussion to current leveraged investments in AI stocks.

**Tags**: `#behavioral-economics`, `#crowd-psychology`, `#financial-bubbles`, `#history`, `#book-discussion`

---

<a id="item-4"></a>
## [Formalizing the Fundamental Theorem of Asset Pricing in Lean 4](https://arxiv.org/abs/2606.28990) ⭐️ 8.0/10

The paper formalizes the Fundamental Theorem of Asset Pricing in Lean 4 over Mathlib for three market settings: a finite‑state finite‑horizon market (Harrison‑Pliska), a one‑period scalar market (Follmer‑Schied), and a d‑asset one‑period market, constructing equivalent martingale measures without using Hahn‑Banach, L^0‑closedness, measurable selection or non‑redundancy assumptions. This is the first machine‑checked proof of the FTAP in any proof assistant, demonstrating how interactive theorem proving can provide rigorous foundations for core results in mathematical finance and enable further verified developments. The construction avoids Hahn‑Banach, L^0‑closedness, measurable selection and non‑redundancy hypotheses; in the d‑asset case the equivalent martingale measure is obtained as the minimizer of the convex potential 𝔼[log(1+e^{⟨θ,Y⟩})], whose coercivity characterizes arbitrage‑freeness and whose first‑order condition yields the martingale property. All theorems are sorry‑free and the development is reproducible from a pinned Lean 4 toolchain.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Lean 4 is a proof assistant and functional programming language based on the calculus of constructions with inductive types, and Mathlib is a large community‑maintained library of formalized mathematics built on Lean. The Fundamental Theorem of Asset Pricing states that a financial market admits no arbitrage opportunities iff there exists an equivalent martingale measure, i.e., a probability measure equivalent to the real‑world measure under which discounted asset prices are martingales. Equivalent martingale measures are central to risk‑neutral pricing and the theory of complete markets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://lean-lang.org/use-cases/mathlib/">Mathlib : A Foundation for Formal Mathematics Research... — Lean Lang</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_asset_pricing">Fundamental theorem of asset pricing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#Lean 4`, `#mathematical finance`, `#asset pricing`, `#theorem proving`

---

<a id="item-5"></a>
## [Supply Chain-Augmented LLM Embeddings Predict Stock Returns](https://arxiv.org/abs/2606.29290) ⭐️ 8.0/10

The paper introduces a framework that augments FinBERT embeddings of 10-K MD&A sections with supply chain knowledge graph propagation to create network-augmented return predictors for 255 S&P 500 firms (2011‑2025). By linking textual disclosures to inter‑firm network structure, the method offers a novel source of alpha that survives standard factor controls and out‑of‑sample tests, potentially improving asset pricing models. Using Fama‑MacBeth cross‑sectional regressions, the network‑augmented factor (net_pc_5) shows a Newey‑West t‑statistic of –2.64, and a long‑short portfolio based on it yields an annualized Sharpe ratio of 0.86 and a Fama‑French five‑factor alpha of 7.27% per year (t = 2.30).

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Large language models such as FinBERT convert textual disclosures into dense vector embeddings that capture semantic meaning. A supply chain knowledge graph represents inter‑firm relationships, allowing signals to propagate from one company to its suppliers or from its suppliers or customers. The Fama‑MacBeth procedure estimates risk premia in two steps, while Newey‑West standard errors correct for heteroskedasticity and autocorrelation in financial time series.

<details><summary>References</summary>
<ul>
<li><a href="https://terence-lim.github.io/docs/financial-data-science-notebooks/1.4_fama_macbeth.html">Fama - Macbeth Cross - sectional Regressions — Financial Data...</a></li>
<li><a href="https://deepwiki.com/fire-institute/fire/6.2-statistical-testing">Statistical Testing | fire-institute/fire | DeepWiki</a></li>
<li><a href="https://diagrams.so/d/supply-chain-kg-nl-query-system-architecture-jaNzQQ">Supply Chain Knowledge Graph NL Query — Azure LLM Architecture</a></li>

</ul>
</details>

**Tags**: `#LLM embeddings`, `#supply chain`, `#asset pricing`, `#finance`, `#network analysis`

---

<a id="item-6"></a>
## [Bayesian optimization finds optimal carbon taxes on low-dimensional equilibrium manifolds.](https://arxiv.org/abs/2606.29299) ⭐️ 8.0/10

The paper shows that when the equilibrium manifold can be parameterized by a low-dimensional set of Negishi weights, Bayesian optimization reliably approximates and certifies solutions. They apply this method to a heterogeneous-agent climate economy model to compute optimal carbon taxes. This work connects machine learning advances with macroeconomic policy analysis, providing a practical way to handle multiple equilibria in heterogeneous-agent models. It enables more robust climate‑policy design, such as carbon‑tax calculation, under realistic economic complexity. The approach relies on a Negishi‑weight parameterization of the equilibrium manifold, uses Bayesian optimization to find approximate solutions with high probability, and demonstrates the method on a calibrated dynamic economy with climate change where competitive equilibria are likely unique despite potential carbon externalities.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Negishi weights are a set of welfare weights used to parameterize the set of Pareto‑efficient allocations in general equilibrium models, allowing the equilibrium manifold to be expressed in low‑dimensional form. Bayesian optimization is a sequential model‑based strategy for optimizing black‑box functions, building a probabilistic surrogate (often a Gaussian process) to guide sampling and certify solutions with high probability. Heterogeneous‑agent macroeconomic models feature agents with differing characteristics (e.g., income, productivity), which can generate multiple equilibria due to complementarities or externalities such as climate change. The equilibrium manifold captures all possible equilibria as a function of underlying parameters, and when it is low‑dimensional, optimization over it becomes tractable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Takashi_Negishi">Takashi Negishi - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_optimization">Bayesian optimization - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0959652625017032">Optimizing the carbon taxation mechanism in heterogeneous ...</a></li>

</ul>
</details>

**Tags**: `#Bayesian optimization`, `#macroeconomics`, `#heterogeneous-agent models`, `#climate policy`, `#equilibrium manifold`

---

<a id="item-7"></a>
## [Adaptive AI Delegation via Bayesian Governance-Aware POMDP](https://arxiv.org/abs/2606.29406) ⭐️ 8.0/10

The paper introduces a Governance-Aware Partially Observable Markov Decision Process (POMDP) that uses Bayesian inference to estimate the informational state and sequentially optimizes the delegation of decision authority to AI under evolving uncertainty. This framework provides the first quantitative method for dynamically allocating AI authority in high‑consequence settings, offering a principled way to balance AI assistance with human oversight as evidence quality changes. The approach combines Bayesian belief updates with a sequential optimization routine, is validated through synthetic stress tests, LLM‑confidence robustness, forecast‑accuracy, governance‑appetite sensitivity, and fragile‑AI early‑warning experiments, and outperforms five baseline governance heuristics across heterogeneous AI‑quality regimes.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: A Partially Observable Markov Decision Process (POMDP) models decision making where the agent cannot directly observe the underlying state but maintains a belief distribution updated via Bayesian inference. In AI governance, delegating authority to large language models requires assessing the quality of their probabilistic recommendations as uncertainty evolves. The Governance‑Aware POMDP extends this by incorporating organizational objectives and uncertainty into the belief state, allowing sequential optimization of how much decision power to cede to AI.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.29406">Adaptive AI Delegation under Uncertainty: A Bayesian ...</a></li>
<li><a href="https://andrewtorgesen.com/notes/Autonomy/Estimation/Applied_Statistics_for_Stochastic_Processes/Bayesian_Inference.html">Bayesian Inference - Andrew's Notes</a></li>
<li><a href="https://www.aptlydone.com/blog/ai-delegation-of-authority-governance">How AI Is Transforming Delegation of Authority | Aptly Blog</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#POMDP`, `#Bayesian inference`, `#decision authority`, `#large language models`

---

<a id="item-8"></a>
## [Swiss cartel mimicked competition to hide bid‑rigging.](https://arxiv.org/abs/2606.30470) ⭐️ 8.0/10

The paper examines a road‑construction cartel in the Swiss canton of Ticino active from 1999 to 2005, showing that its members used a cost‑based allocation mechanism that imitated competitive bidding. Using double machine learning, the authors estimate that the cartel’s overcharges were at least 45%. The study reveals how sophisticated cartels can evade standard detection tools, offering a new empirical strategy for antitrust agencies to uncover hidden collusion and quantify its financial impact. Using documentary evidence of the 'convention' agreement, the authors show that observable cost proxies predict winning bids and rankings, and apply double machine learning to estimate average overcharges of at least 45%, potentially higher.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Cartels in procurement often coordinate bids to inflate prices, but detection relies on deviations from competitive patterns. Recent econometric advances, such as double machine learning, help isolate causal effects while controlling for high‑dimensional confounders, making it possible to assess collusion even when conspirators mimic competitive behavior. The Ticino case illustrates how a formal agreement can produce a cost‑based allocation that closely approximates the first‑best collusive outcome without side payments.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.30470">[2606.30470] Swimming in Dark Water: When Cartels Mimic Competition</a></li>
<li><a href="https://www.linkedin.com/pulse/what-double-machine-learning-dml-why-should-economists-eker-a4q1f">What Is Double Machine Learning (DML) and Why Should...</a></li>
<li><a href="https://trainings.doubleml.org/about.html">About – DoubleML Trainings</a></li>

</ul>
</details>

**Tags**: `#cartel detection`, `#econometrics`, `#machine learning`, `#industrial organization`, `#antitrust`

---

<a id="item-9"></a>
## [A General Theory of Paths: Signatures, Jump Lifts, and Expected Signatures of Self-Exciting Processes](https://arxiv.org/abs/2606.28869) ⭐️ 8.0/10

The paper introduces a path-first framework that treats the signature as a universal coordinate for deterministic, rough, jump, and random paths, proving a geometricity-defect theorem linking quadratic covariation to shuffle multiplicativity failures. It further establishes Hopf square results for pure-jump paths, finite-dimensional linear closures for affine and exponential Hawkes expected signatures, and an antisymmetric cross-area that detects excitation direction in two-channel Hawkes processes. By unifying signature theory, rough paths, jump processes, and expected signatures, the work provides a common algebraic language that bridges stochastic analysis and machine learning applications of path signatures. Its results enable explicit parameter identification for Hawkes processes and new tools for detecting directional excitation, impacting fields such as finance, neuroscience, and signal processing. The geometricity-defect theorem identifies quadratic covariation and coordinate covariance as the canonical failures of shuffle multiplicativity for expected signatures. For pure-jump finite-variation paths the forward Ito signature equals the iterated-sums signature, while affine/exponential Hawkes processes admit finite-dimensional linear closures after state-weight augmentation, allowing baseline, excitation, and decay parameters to be read off from level-two expected signatures; additionally, an antisymmetric second-level cross-area detects the direction of excitation in two-channel Hawkes processes to first order.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: In rough path theory, the signature of a path is a sequence of iterated integrals that uniquely encodes the path's shape and serves as a feature map for machine learning. Geometricity refers to the property that a lifted path lies in the free nilpotent group, and its defect measures deviations from shuffle multiplicativity caused by quadratic variation. A Hawkes process is a self-exciting point process where each event increases the future intensity, commonly modeled with an exponential or affine kernel. Expected signatures average the signature over random paths, enabling statistical inference and kernel methods for stochastic processes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rough_path">Rough path - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hawkes_process">Hawkes process - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2606.28869">A General Theory of Paths : Signatures , Jump Lifts, and Expected...</a></li>

</ul>
</details>

**Tags**: `#signature theory`, `#rough paths`, `#stochastic processes`, `#Hawkes processes`, `#algebraic topology`

---

<a id="item-10"></a>
## [LLM Compression of Financial Texts Can Distort Investment Decisions](https://arxiv.org/abs/2606.29251) ⭐️ 8.0/10

The study shows that LLM-based compression of financial filings and earnings-call transcripts can produce fluent, factually plausible summaries that nonetheless alter the investment decisions supported by the original material, identifying decontextualization and model dependency as key failure modes and proposing Agentic Context Compression to mitigate them. It reveals that evaluating LLM compression solely by fluency or factuality is insufficient for financial decision‑making, with implications for AI safety and the reliable deployment of LLMs in finance. The paper defines information fidelity as the preservation of the decision induced by the source, demonstrates fidelity loss across financial texts, and introduces Agentic Context Compression, which generates multiple candidate compressions and audits their disagreements against the original source.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Financial analysts often need to digest lengthy filings and transcripts, making context compression necessary. Large language models can summarize these texts, but compression may drop nuanced qualifiers or caveats, leading to decontextualization. Different LLMs may also produce varying summaries of the same source, creating model dependency. Preserving decision‑relevant context is therefore critical to avoid altering investment judgments.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.29251">[2606.29251] When Summaries Distort Decisions: Information ...</a></li>
<li><a href="https://letsdatascience.com/news/llm-compression-alters-financial-decision-fidelity-321b7306">LLM Compression Alters Financial Decision Fidelity</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#information fidelity`, `#financial analysis`, `#AI safety`, `#context compression`

---

<a id="item-11"></a>
## [CLQT: Closed-Loop, Cost-Aware Benchmark for LLM Portfolio-Management Agents](https://arxiv.org/abs/2606.29771) ⭐️ 8.0/10

The paper introduces CLQT, a closed-loop, cost-aware, strategy-consistent benchmark that evaluates LLM-based portfolio managers via a five-stage decision cycle and verifiable hash-chained decision trails. CLQT shifts evaluation from return‑centric leaderboards to diagnostic process analysis, revealing where agents succeed or fail and enabling more reliable development of LLM trading agents. CLQT features a hard TimeGate, institutional transaction and financing cost modeling, three‑tier memory, a Model‑Context‑Protocol tool layer, and mandate‑aware synthesis, producing a five‑axis capability scorecard (APM‑CS) from audited DecisionRound hash chains.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Recent work has shifted LLM agent evaluation from static financial Q&A to sequential trading simulations that mimic real‑time portfolio management. Most existing benchmarks rank agents solely by cumulative returns over a fixed window, which conflates skill with market path and can be inflated by look‑ahead leakage. CLQT addresses these limitations by enforcing a closed‑loop environment where agents must observe, decide, execute, and reflect within each time step, making performance diagnostics possible.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.29771">CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent ...</a></li>
<li><a href="https://letsdatascience.com/news/clqt-introduces-closed-loop-benchmark-for-llm-trading-agents-9f39d457">CLQT Introduces Closed-Loop Benchmark for LLM Trading Agents</a></li>
<li><a href="https://arxiv.deeppaper.ai/papers/2606.29771v1">CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#financial AI`, `#benchmarking`, `#trading simulation`, `#evaluation methodology`

---

<a id="item-12"></a>
## [Permutation-Invariant Fine-Tuning Makes Metadata Retrieval Robust to Field Order](https://arxiv.org/abs/2606.30473) ⭐️ 8.0/10

The paper introduces permutation-invariant fine-tuning (PI-FT), which trains text encoders on randomly ordered metadata fields with dropout, reducing the retrieval penalty from 7.4 to 0.2 nDCG@10 when field order changes. Field order is an arbitrary implementation detail that can severely degrade retrieval quality, especially for AI assistants that must reliably surface the correct public statistics across languages. PI-FT requires only about two lines of change in the data loader, incurs negligible in-distribution accuracy loss, and enables a 118M‑parameter CPU encoder to outperform zero‑shot baselines such as text‑embedding‑3‑large (0.707 vs. 0.556 nDCG@10).

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: In structured metadata retrieval, each record is serialized into a string by concatenating its fields, which forces a specific field order; standard fine‑tuning then learns to associate meaning with absolute token positions rather than field labels. Consequently, rebuilding the index with a different field order causes a large drop in ranking quality, measured by nDCG@10, because the encoder has become sensitive to the original order. The authors also introduce DevDataBench, a fully LLM‑generated benchmark of grounded, facet‑targeted queries in 15 languages for the development statistics catalog, enabling training and evaluation when real user logs are unavailable.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.30473">Field Order Should Not Matter: Permutation- Invariant Embedding...</a></li>
<li><a href="https://pulseaugur.com/cluster/117083-new-pi-ft-method-improves-structured-metadata-retrieval-by-ignoring-field-order">New PI - FT method improves metadata retrieval by ignoring field order...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discounted_cumulative_gain">Discounted cumulative gain - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#information retrieval`, `#metadata embedding`, `#permutation invariance`, `#fine-tuning`, `#NLP`

---

<a id="item-13"></a>
## [AI Premium Identified via 380 Trillion Tokens of LLM Usage](https://arxiv.org/abs/2606.30583) ⭐️ 8.0/10

The authors constructed an AI factor using 380 trillion tokens of LLM usage from the OpenRouter dataset and found that firms with higher AI beta earn excess returns, quantifying an AI premium of 64.1 basis points per week. This provides the first large‑scale empirical measure of how AI adoption translates into financial returns, offering a new factor for asset pricing and insight into AI’s economic impact across sectors. The premium is driven mainly by intensive, frontier‑oriented AI use—closed‑source models, paying and seasoned users, and long prompts—and is absent in emerging markets such as China, while showing a positive link to nonroutine interactive work and a negative link to analytical occupations.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: The study builds an AI factor from growth in token consumption, dollar spending, and user counts derived from the OpenRouter platform, which aggregates LLM usage across hundreds of models. OpenRouter’s dataset provides a granular, high‑frequency view of real‑world AI consumption, exemplified by its 100‑trillion‑token State of AI 2025 report. Factor investing techniques are then applied to estimate firm‑level AI betas from stock return comovement with this AI factor.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/data">Data - Authoritative AI Usage Data for Research | OpenRouter</a></li>
<li><a href="https://openrouter.ai/state-of-ai">State of AI 2025: 100T Token LLM Usage Study | OpenRouter</a></li>
<li><a href="https://arxiv.org/html/2601.10088v1">State of AI: An Empirical 100 Trillion Token Study with ...</a></li>

</ul>
</details>

**Tags**: `#AI economics`, `#factor investing`, `#token consumption`, `#stock returns`, `#machine learning impact`

---

<a id="item-14"></a>
## [Deep Neural Networks Yield Linear Factor Models via Portfolio Tangent Kernel](https://arxiv.org/abs/2402.06635) ⭐️ 8.0/10

The paper shows that a DNN-trained stochastic discount factor admits an additive decomposition into a linear factor representation governed by the Portfolio Tangent Kernel (PTK). Empirically, using U.S. equity data, the PTK representation delivers economically and statistically significant pricing gains while linking spectral complexity to ridge regularization. This bridges deep learning and asset pricing by providing an interpretable linear factor model derived from black‑box DNNs, offering a new tool for researchers and practitioners to understand and improve SDF estimation. It also connects model complexity to regularization, guiding better generalization in financial machine learning. The decomposition separates nonlinear characteristic discovery from the pricing rule, with the PTK summarizing learned features; in population the implied SDF converges to a ridge‑regularized true SDF where regularization strength depends on spectral complexity. Empirically, higher spectral complexity tightens finite‑sample pricing limits while the PTK representation yields significant economic and statistical gains.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: A stochastic discount factor (SDF) prices assets by conditioning payoffs on market states, and estimating it from data is a central challenge in asset pricing. Recent work uses deep neural networks to learn SDFs directly from returns and characteristics, often outperforming traditional linear factor models but lacking interpretability. The paper introduces an additive decomposition that isolates the network’s learned features into a linear factor model governed by the newly defined Portfolio Tangent Kernel, and relates the network’s spectral complexity to ridge‑type regularization.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2402.06635">[2402.06635] Large and Deep Factor Models - arXiv.org</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6225778">Large and Deep Factor Models by Bryan T. Kelly, Boris ... - SSRN</a></li>
<li><a href="https://arxiv.org/html/2402.06635">Large and Deep Factor Models</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#asset pricing`, `#stochastic discount factor`, `#factor models`, `#deep learning`

---

<a id="item-15"></a>
## [Equilibrium Transition from Loss-Leader Competition: How Advertising Restrictions Facilitate Price Coordination in Chilean Pharmaceutical Retail](https://arxiv.org/abs/2512.22917) ⭐️ 8.0/10

The study shows that Chile's ban on comparative-price advertising ended a loss-leader price war and enabled pharmacy chains to jointly raise prices by altering price sensitivity and beliefs. It reveals how advertising restrictions can shift market dynamics from destructive price wars to tacit coordination, offering important insights for industrial organization theory and antitrust policy. The paper builds a demand-grounded structural model with two mechanisms—store traffic and rival beliefs—and estimates it via simulated method of moments, reproducing the observed price war, failed attempts, and post-ban coordination; the resulting harm is mainly a transfer to supra‑competitive rents with small deadweight loss due to inelastic post‑ban demand.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Loss leader pricing involves selling a product below its cost to attract customers who then purchase higher-margin items. Comparative-price advertising highlights which retailer offers the lowest price, intensifying price competition and enabling loss-leader strategies. The simulated method of moments (SMM) is a structural estimation technique that matches simulated model moments to empirical moments when analytical solutions are infeasible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Loss_leader">Loss leader - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Method_of_simulated_moments">Method of simulated moments - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#industrial organization`, `#advertising regulation`, `#pharmaceutical pricing`, `#structural estimation`, `#tacit collusion`

---

<a id="item-16"></a>
## [Formal Lean 4 Library for Mathematical Finance with Ito Integral and Risk-Neutral Measure](https://arxiv.org/abs/2606.01356) ⭐️ 8.0/10

The authors released a Lean 4 library of mathematical finance that contains over 200 sorry‑free theorems across eleven sub‑areas, constructs the L² Itô integral as a bounded linear isometry, and derives the risk‑neutral pricing measure from first principles. This work provides a machine‑checked, axiom‑transparent foundation for quantitative finance, enabling trustworthy modeling and reusable verified components for derivatives pricing, risk management, and fixed‑income analysis. The library is built on Mathlib and the BrownianMotion package, classifies each theorem by its faithfulness to the underlying mathematics, and uses a build‑enforced gate to expose exactly which axioms each proof actually relies on.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Lean 4 is a functional programming language and proof assistant that supports interactive theorem proving; its mathematical library Mathlib provides a large collection of formalized mathematics. The Itô integral is a fundamental construction in stochastic calculus used to model integration with respect to Brownian motion, and the risk‑neutral measure is a probability measure under which discounted asset prices are martingales, central to derivative pricing. Formalizing these concepts in Lean 4 allows every step of a proof to be checked by the computer, eliminating hidden assumptions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.01356">A Formally Verified Library of Mathematical Finance in Lean 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Itô_calculus">Itô calculus - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Risk-neutral_measure">Risk-neutral measure - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#Lean 4`, `#mathematical finance`, `#stochastic calculus`, `#theorem proving`

---

<a id="item-17"></a>
## [Machine-Checked Ito Calculus for Brownian Motion in Lean 4](https://arxiv.org/abs/2606.15089) ⭐️ 8.0/10

The paper formalizes the Ito integral and Ito's formula for Brownian motion within Lean 4's Mathlib, constructing the integral as a Hilbert-space isometry via a predictable-rectangle π-system and deriving key properties from conditional-expectation projections. This work provides the first machine-checked construction of Ito calculus in any proof assistant, offering rigorous foundations for stochastic analysis and showcasing how formal methods can advance continuous-time probability theory. The construction proves Ito's formula for C^3 functions with bounded derivatives, obtains an almost-surely continuous modification of the integral process, and extends it to a pathwise continuous local martingale on ℝ≥0, all verified in Lean 4.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Ito calculus provides a framework for integrating with respect to Brownian motion, where the Ito integral satisfies an isometry property in L^2 space. The integral can be built as a Hilbert-space isometry from simple adapted processes, and its value at time t equals the conditional expectation of its terminal value given the filtration up to t. Lean 4 is a functional programming language and proof assistant whose Mathlib library contains formalized mathematics, including a BrownianMotion package. Formalizing these concepts in Lean 4 yields machine-checked proofs that guarantee correctness of the stochastic integral and Ito's formula.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Itô_calculus">Itô calculus - Wikipedia</a></li>
<li><a href="https://reservoir.lean-lang.org/@RemyDegenne/BrownianMotion">Construction of a Brownian Motion in Lean | Reservoir</a></li>
<li><a href="https://arxiv.org/html/2606.01356">A Formally Verified Library of Mathematical Finance in Lean 4</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#stochastic calculus`, `#Lean 4`, `#Ito integral`, `#Brownian motion`

---

<a id="item-18"></a>
## [China's domestic science now exceeds US contributions in patents.](https://arxiv.org/abs/2606.26470) ⭐️ 8.0/10

The study links Chinese invention patents to global scientific literature and finds that the share of China‑produced science behind those patents rose from 1% in 2000 to 26% in 2025, overtaking the US share in 2021. This shift shows China's growing technological self‑reliance, undermining the premise of US export controls that assume Chinese innovation depends on American science. The analysis covered the full corpus of Chinese invention patents, measuring domestic versus foreign science citations; China‑produced science share grew steadily while the US share declined, with the crossover occurring in 2021.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Invention patents grant exclusive rights to new technical solutions and are often linked to the scientific knowledge that underpins them. Researchers measure a country's dependence on foreign science by tracking the proportion of patent citations that point to domestic versus foreign publications. U.S. policy has sought to slow China's technological rise by limiting its access to American science, assuming that Chinese innovation relies heavily on U.S.-produced knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://www.uspto.gov/patents/search">Search for patents | USPTO</a></li>
<li><a href="https://patents.google.com/">Google Patents</a></li>
<li><a href="https://link.springer.com/article/10.1007/s11192-025-05363-6">Global ties in science: a scientometric approach to ...</a></li>

</ul>
</details>

**Tags**: `#innovation`, `#China`, `#technology policy`, `#patent analysis`, `#science dependence`

---

<a id="item-19"></a>
## [Study Links Corporate Landlord Concentration to Faster Rent Growth in Minority Neighborhoods](https://arxiv.org/abs/2606.27525) ⭐️ 8.0/10

The paper geocodes SEC EDGAR 10-K property filings to census tracts to measure corporate landlord concentration (CLC) and finds that doubling REIT concentration is associated with 2.8 percentage points higher rent growth from 2019 to 2023, with a significantly stronger effect in majority‑minority tracts. By providing the first tract‑level evidence that algorithmic landlord concentration correlates with disproportionately higher rent growth in communities of color, the study informs ongoing antitrust scrutiny and housing‑affordability policy. The analysis controls for a novel Algorithmic Housing Burden Index (AHBI) built from ACS rent burden and market tightness, uses Zillow’s Observed Rent Index (ZORI) as the rent outcome, and employs an XGBoost model that explains 44 % of out‑of‑sample variance, with SHAP values showing CLC’s effect positive in minority tracts and negative in white tracts.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Corporate landlord concentration (CLC) refers to the share of rental units owned by large, publicly traded real estate investment trusts (REITs), which is measured by geocoding property listings from SEC EDGAR 10‑K filings to census tracts. The study builds on the 2024 DOJ antitrust complaint that accused RealPage and several major REITs of using algorithmic tools to coordinate rent prices across hundreds of thousands of units. To isolate the effect of CLC, researchers created the Algorithmic Housing Burden Index (AHBI) from ACS data on pre‑existing rent burden and market tightness, and used the Zillow Observed Rent Index (ZORI) to track rent growth from 2019 to 2023.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sec.gov/search-filings">Search Filings - SEC.gov</a></li>
<li><a href="https://github.com/advayranade/algo-rent-pricing-research-ahbi">advayranade/algo-rent-pricing-research-ahbi - GitHub</a></li>
<li><a href="https://www.zillow.com/research/methodology-zori-repeat-rent-27092/">Methodology: Zillow Observed Rent Index ( ZORI ) - Zillow Research</a></li>

</ul>
</details>

**Tags**: `#housing economics`, `#algorithmic fairness`, `#racial disparity`, `#urban policy`, `#antitrust`

---

<a id="item-20"></a>
## [Weighted universal approximation of differentiable maps on infinite-dimensional manifolds](https://arxiv.org/abs/2606.09820) ⭐️ 8.0/10

The paper extends the universal approximation theorem for functional input neural networks to differentiable maps on infinite-dimensional weighted manifolds, proving a weighted Nachbin theorem that also guarantees approximation of the maps' derivatives. This yields approximation results for non‑anticipative functionals and shows that linear functions of the signature can approximate path space functionals together with their directional derivatives. By extending the universal approximation theorem to infinite‑dimensional settings and derivative approximation, the work provides a theoretical foundation for using neural networks to learn complex functionals arising in rough path theory, stochastic analysis, and functional data analysis. It bridges machine learning theory with advanced functional analysis, potentially impacting future algorithms for path‑dependent data. The approach uses a functional input neural network that maps an input from a possibly infinite‑dimensional weighted manifold to a real‑valued hidden layer, applies a scalar nonlinear activation, and reads out into a Banach space via linear functionals; the weighted Nachbin theorem guarantees density of such networks in the space of differentiable maps, including horizontal and vertical derivatives of non‑anticipative functionals. Linear combinations of the signature are shown to approximate these path space functionals.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: The universal approximation theorem states that feedforward neural networks can approximate any continuous function on compact sets; functional input neural networks (FNNs) extend this idea to inputs that are functions or paths, treating them as elements of infinite‑dimensional spaces. Nachbin’s theorem gives conditions under which an algebra of functions is dense in the space of continuous functions on a topological space, and a weighted version allows approximation on non‑compact, weighted manifolds. Path signatures provide a signature‑based feature map for streams, with horizontal and vertical derivatives capturing directional variations; approximating these objects enables learning of path‑dependent functionals.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.09820">Weighted universal approximation of differentiable maps on ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nachbin's_theorem">Nachbin 's theorem - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2301.05869">[2301.05869] Functional Neural Networks: Shift invariant ... FuncNN: Functional Neural Networks Functional Neural Networks: Shift Invariant Models for ... GitHub - b-thi/FNN: FuncNN R Package Website Fitting Functional Neural Networks — fnn.fit • FNN Feedforward Neural Network - GeeksforGeeks Images</a></li>

</ul>
</details>

**Tags**: `#universal approximation theorem`, `#neural networks`, `#infinite-dimensional manifolds`, `#functional analysis`, `#path signatures`

---

<a id="item-21"></a>
## [KineticSim boosts market simulator throughput to 54.7B events per second.](https://arxiv.org/abs/2606.21784) ⭐️ 8.0/10

KineticSim introduces a lightweight GPU execution engine that implements a persistent, state-carrying clearing pattern using shared-memory atomics to accelerate iterative multi-agent reductions in market simulators, achieving a peak throughput of over 54.7 billion agent-events per second. By drastically reducing per-step critical-path depth and eliminating step-dependent global-memory traffic, KineticSim enables real-time, large-scale market simulations for applications such as regulatory stress testing, reinforcement learning, and high-frequency trading, while consuming far less GPU memory than existing frameworks. The pattern reduces the per-step critical-path depth from Θ(L+A) to Θ(log L + ⌈A/L⌉) and makes global-memory traffic independent of the step count; on a fixed workload KineticSim delivers speedups of 3406× over NumPy, 27.8× over PyTorch GPU, 42.8× over JAX GPU, and 8.4× over a naive CUDA baseline while using roughly an order of magnitude less GPU memory than PyTorch, and produces bitwise-identical order books across 53 configurations.

rss · arXiv Quantitative Finance · Jun 30, 04:00

**Background**: Multi-agent market simulations model the interactions of many trading agents, but traditional CPU simulators process agents sequentially, creating a bottleneck, while vectorized GPU approaches suffer from kernel-launch overhead and repeated global-memory accesses. The persistent state-carrying clearing pattern caches mutable simulation state in thread-block shared memory across simulation steps, aggregates agent actions via shared-memory atomics, and resolves the clearing function cooperatively, thereby reducing critical-path depth and eliminating step-dependent global memory traffic. Shared-memory atomics provide low-latency updates within a thread block, as discussed in CUDA resources on shared memory atomic performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Bwv5J7dHYjU">From Scratch: Shared Memory Atomics and Dynamic... - YouTube</a></li>
<li><a href="https://stackoverflow.com/questions/51642503/which-is-faster-for-cuda-shared-mem-atomics-warp-locality-or-anti-locality">Which is faster for CUDA shared -mem atomics ... - Stack Overflow</a></li>
<li><a href="https://www.toolify.ai/gpts/unlock-the-power-of-cuda-shared-memory-atomics-and-dynamic-allocation-145200">Unlock the Power of CUDA: Shared Memory Atomics and Dynamic...</a></li>

</ul>
</details>

**Tags**: `#parallel computing`, `#agent-based modeling`, `#market simulation`, `#high-performance computing`, `#financial technology`

---