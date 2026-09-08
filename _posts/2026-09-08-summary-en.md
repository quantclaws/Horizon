---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 29 items, 7 important content pieces were selected

---

1. [Optuna 5.0 releases major updates to its default sampler and adds new constrained optimization APIs](#item-1) ⭐️ 8.0/10
2. [Show HN: Stuxnet source code reconstructed and shared on GitHub for research.](#item-2) ⭐️ 8.0/10
3. [Keep Our Servers Running](#item-3) ⭐️ 8.0/10
4. [OpenAI Chief Scientist urges rapid AI development for defense.](#item-4) ⭐️ 8.0/10
5. [Majorization Approach Reveals Diversification-Concentration Trade-off Under Dependence Uncertainty](#item-5) ⭐️ 8.0/10
6. [Agent-to-Agent Finance: Blockchain Infrastructure for Autonomous AI Agents](#item-6) ⭐️ 8.0/10
7. [Rethinking Synthetic Scenario Realism: Compatibility, Not Fidelity, Drives Hedging Performance](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Optuna 5.0 releases major updates to its default sampler and adds new constrained optimization APIs](https://github.com/optuna/optuna/releases/tag/v5.0.0) ⭐️ 8.0/10

Optuna v5.0 enables multivariate TPE and the constant liar strategy by default in TPESampler, improves bandwidth computation, and makes TPESampler the default for multi‑objective optimization. It also introduces a core Trial API for constrained optimization via trial.set_constraint() and trial.constraints, deprecates sampler‑specific constraints_func, sets PedAnovaImportanceEvaluator as the default importance evaluator, and stabilizes GPSampler with Monte‑Carlo q‑batch acquisition functions. These changes improve the efficiency and ease of use of Optuna for a broad range of machine learning and hyperparameter tuning tasks, affecting thousands of researchers and practitioners who rely on the library. By making advanced Bayesian optimization techniques the default, Optuna v5.0 raises the baseline performance users can expect without manual configuration. Multivariate TPE, constant liar, and Watanabe‑2023 bandwidth computation are now enabled by default in TPESampler for single‑objective studies, and TPESampler replaces NSGAIISampler as the default sampler for multi‑objective optimization. The release adds a core Trial API for constrained optimization via trial.set_constraint() and trial.constraints, deprecates sampler‑specific constraints_func, makes PedAnovaImportanceEvaluator the default importance evaluator, and stabilizes GPSampler with q‑batch acquisition functions (qLogEI, qLogCEI, qLogEHVI, qLogCEHVI).

github · c-bata · Sep 7, 05:15

**Background**: Optuna is an open‑source hyperparameter optimization framework that automates the search for optimal model configurations using various samplers such as TPE, CMA‑ES, and random search. It provides a Pythonic API for defining objective functions, managing trials, and visualizing optimization progress, and is widely used in machine learning research and production. The default sampler has historically been TPESampler, which implements the Tree‑structured Parzen Estimator approach to model the relationship between hyperparameters and objective values.

**Tags**: `#optuna`, `#hyperparameter-optimization`, `#machine-learning`, `#release`, `#sampler`

---

<a id="item-2"></a>
## [Show HN: Stuxnet source code reconstructed and shared on GitHub for research.](https://github.com/Sadpainy/Stuxnet) ⭐️ 8.0/10

A reconstructed source code of the Stuxnet cyber-weapon, comprising roughly 15,000 lines, has been uploaded to GitHub by user Sadpainy for research and educational use. The release enables security researchers to study a historically significant cyber‑weapon, improving understanding of advanced malware techniques and industrial control system threats. The code targets Siemens Step7 software, exploits four Windows zero‑day vulnerabilities, spreads via USB drives, network shares and the Windows printer spooler, and includes logic to alter centrifuge frequencies.

hackernews · CMDDestory · Sep 7, 22:12 · [Discussion](https://news.ycombinator.com/item?id=49603546)

**Background**: Stuxnet is a sophisticated computer worm discovered in 2010 that specifically targeted Iran’s nuclear enrichment facilities by manipulating Siemens PLC‑controlled centrifuges. It employed four previously unknown Windows zero‑day exploits and a zero‑day in Siemens Step7 software to propagate autonomously via USB drives, network shares and the printer spooler service. The worm’s attack caused the centrifuges to spin at destructive speeds, physically damaging Iran’s uranium enrichment program and marking the first known use of a cyber‑weapon for physical sabotage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stuxnet">Stuxnet - Wikipedia</a></li>
<li><a href="https://www.huntress.com/threat-library/malware/stuxnet-malware">Stuxnet Malware: Analysis, Detection, Removal | Huntress</a></li>
<li><a href="https://www.sciencedirect.com/topics/computer-science/stuxnet">Stuxnet - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**Discussion**: Commenters thanked the author for sharing the roughly 15,000‑line Stuxnet source code and highlighted its educational value, citing works like Countdown to Zero Day. Some questioned the feasibility of the USB‑drive propagation mechanism and whether the hardware might have been pre‑infected, while others suggested that additional documentation would make the repository easier to navigate.

**Tags**: `#cybersecurity`, `#malware`, `#Stuxnet`, `#reverse engineering`, `#historical`

---

<a id="item-3"></a>
## [Keep Our Servers Running](https://blog.archive.org/2026/09/01/keep-our-servers-running-your-recurring-donation-goes-3x-this-september/) ⭐️ 8.0/10

The Internet Archive seeks recurring donations with a 3x match in September, sparking community talk about volunteering, technical challenges, and donation matching mechanics.

hackernews · sonicrocketman · Sep 7, 03:29 · [Discussion](https://news.ycombinator.com/item?id=49593563)

**Tags**: `#internet-archive`, `#fundraising`, `#open-source`, `#digital-preservation`, `#community`

---

<a id="item-4"></a>
## [OpenAI Chief Scientist urges rapid AI development for defense.](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 8.0/10

Jakub Pachocki, OpenAI's Chief Scientist, stated that we must quickly train much smarter AI to build defensive systems against other AI dangers, but warned that this need should not excuse reckless advancement. His remarks highlight the growing debate over balancing AI safety with the need for defensive AI capabilities, influencing both policy discussions and industry practices. The quote comes from OpenAI's blog post 'An Alien Mind' under the 'scalable defense' section, where Pachocki emphasizes the need for powerful, aligned AI to secure infrastructure and protect against rogue agents in real time.

rss · Simon Willison · Sep 7, 22:26

**Background**: OpenAI, led by Chief Scientist Jakub Pachocki, has been at the forefront of research on AI alignment and safety. The idea of defensive AI involves deploying advanced AI systems to detect, mitigate, or counter threats posed by other AI, such as rogue agents or malicious models. Pachocki's statement reflects OpenAI's strategy to pursue powerful AI for protective purposes while cautioning against unchecked acceleration.

**Tags**: `#AI safety`, `#AI ethics`, `#OpenAI`, `#defensive AI`, `#AI policy`

---

<a id="item-5"></a>
## [Majorization Approach Reveals Diversification-Concentration Trade-off Under Dependence Uncertainty](https://arxiv.org/abs/2609.04496) ⭐️ 8.0/10

The paper investigates the tension between portfolio diversification and concentration under dependence uncertainty using majorization order and doubly stochastic matrices, proving that quasi-convexity is necessary and sufficient for a risk functional to be weakly consistent with majorization order. It derives worst-case risk measure inequalities and solves robust portfolio selection problems for VaR, ES, RVaR, and standard deviation. By revealing a 'concentration paradox' where robust optimization may favor single-asset investment under full dependence ambiguity, the work provides a theoretical foundation for balancing diversification against robustness in risk management. Its results are directly applicable to regulatory frameworks such as the FRTB and offer new tools for quantitative finance practitioners. The paper shows that quasi-convex risk measures (including VaR, ES, RVaR, and SD) are precisely those compatible with majorization order, enabling derivation of worst-case bounds and robust solutions. It also proposes a weighted robustness formulation that interpolates between a reference dependence structure and the worst-case structure, structurally akin to the FRTB ES blend.

rss · arXiv Quantitative Finance · Sep 7, 04:00

**Background**: Majorization order compares vectors by their spread, and doubly stochastic matrices represent transformations that preserve this order, allowing a formal measure of diversification. Quasi-convex functions have sublevel sets that are convex, a property key to many risk measures used in finance. Dependence uncertainty refers to lack of knowledge about the joint distribution of asset returns, prompting robust optimization approaches that hedge against worst-case scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.04496">[2609.04496] Portfolio Diversification and Concentration under Dependence Uncertainty: A Majorization Approach</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doubly_stochastic_matrix">Doubly stochastic matrix - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quasiconvex_function">Quasiconvex function - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#portfolio optimization`, `#risk management`, `#robust optimization`, `#majorization order`, `#financial mathematics`

---

<a id="item-6"></a>
## [Agent-to-Agent Finance: Blockchain Infrastructure for Autonomous AI Agents](https://arxiv.org/abs/2607.00245) ⭐️ 8.0/10

The paper introduces agent-to-agent finance as a blockchain-based infrastructure layer that enables autonomous AI agents to discover counterparties, negotiate services, execute payments, and generate auditable transaction evidence. By linking AI autonomy with programmable settlement, it provides a trust and payment layer that could unlock scalable multi-agent economies and reshape decentralized finance and traditional financial markets. The framework relies on smart contracts for programmable settlement, ERC-8004 agent registries, provenance-based wallets, deterministic inference, and DeFi intent mining, while advocating bounded autonomy to prevent market opacity and fragility.

rss · arXiv Quantitative Finance · Sep 7, 04:00

**Background**: Autonomous AI agents can now perform economic actions such as calling external tools, negotiating with other agents, and initiating blockchain transactions, creating a need for infrastructure that handles identity, authorization, payment, verification, reputation, and accountability. Blockchain offers programmable settlement via smart contracts, near-instant finality, and low fees, while standards like ERC-8004 provide decentralized agent registries and provenance wallets enable verifiable computation. The concept of bounded autonomy seeks to expand the set of safe economic actions agents can take without making markets more opaque or unaccountable.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.00245">Agent - to - Agent Finance : Blockchain Payments and Trust...</a></li>
<li><a href="https://nevermined.ai/blog/ai-agents-pay-things">How Do AI Agents Pay for Things | Nevermined</a></li>
<li><a href="https://www.pingidentity.com/en/solution/agentic-ai-identity.html">Enable Agentic AI Securely and Confidently | Ping Identity</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#blockchain`, `#multi-agent systems`, `#financial infrastructure`, `#smart contracts`

---

<a id="item-7"></a>
## [Rethinking Synthetic Scenario Realism: Compatibility, Not Fidelity, Drives Hedging Performance](https://arxiv.org/abs/2608.20842) ⭐️ 8.0/10

The paper introduces a decision‑centric notion of compatibility for synthetic scenario generators in deep hedging, showing that hedging error splits into learning error and a compatibility gap. Empirically, hedging performance depends on the alignment between the generator and the hedger, not merely on the realism of the synthetic data. By shifting focus from statistical realism to task‑driven compatibility, the work provides a principled way to design synthetic data that directly improves hedging outcomes, advancing both theory and practice in financial machine learning. The authors theoretically decompose hedging performance into learning error and a compatibility gap, demonstrating that realism and compatibility can diverge. Experiments show that hedging performance is governed by generator‑hedger alignment and task structure rather than realism alone.

rss · arXiv Quantitative Finance · Sep 7, 04:00

**Background**: Deep hedging uses deep reinforcement learning to derive optimal hedging strategies from data, especially when real market histories are scarce. Practitioners often train on synthetic price‑path generators that simulate market dynamics, evaluating these generators primarily by how well they reproduce statistical properties of real markets. This work argues that such realism metrics do not guarantee hedging effectiveness, motivating a decision‑centric compatibility perspective.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/1802.03042v1">DEEP HEDGING - arXiv.org</a></li>
<li><a href="http://deephedging.com/">Deep Hedging - Learning to Trade</a></li>
<li><a href="https://www.emergentmind.com/topics/deep-hedging-paradigm">Deep Hedging Paradigm</a></li>

</ul>
</details>

**Tags**: `#deep hedging`, `#synthetic data`, `#compatibility`, `#financial machine learning`, `#reinforcement learning`

---