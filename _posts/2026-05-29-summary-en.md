---
layout: default
title: "Horizon Summary: 2026-05-29 (EN)"
date: 2026-05-29
lang: en
---

> From 36 items, 7 important content pieces were selected

---

1. [Blue Origin's New Glenn rocket explodes during static fire test](#item-1) ⭐️ 8.0/10
2. [GitHub bans security researcher who posted zero-day Windows exploits](#item-2) ⭐️ 8.0/10
3. [: Building durable workflows on Postgres](#item-3) ⭐️ 8.0/10
4. [: ](#item-4) ⭐️ 8.0/10
5. [:From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets](#item-5) ⭐️ 8.0/10
6. [: Well-posedness of Infinite-Dimensional LQ MFG with Common Noise.](#item-6) ⭐️ 8.0/10
7. [: From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Blue Origin's New Glenn rocket explodes during static fire test](https://twitter.com/nasaspaceflight/status/2060164928472854821) ⭐️ 8.0/10

Blue Origin's New Glenn rocket suffered a catastrophic failure during a static fire test at its Florida launch site, causing significant infrastructure damage and delaying the vehicle's development timeline. The explosion is a major setback for Blue Origin's launch ambitions, affecting NASA's Artemis moon lander plans and highlighting risks associated with large methane-fueled rockets. The static fire test involved a fully fueled booster estimated to hold about 1,000 tons of liquid methane, releasing energy comparable to roughly 13 kilotons of TNT in heat output.

hackernews · enraged_camel · May 29, 01:16 · [Discussion](https://news.ycombinator.com/item?id=48317774)

**Background**: New Glenn is a two-stage partially reusable launch vehicle developed by Blue Origin, announced in 2016 and featuring a seven-meter diameter. A static fire test fires the rocket engines while the vehicle remains restrained to verify propulsion and ground‑support readiness before flight. This test is standard practice to check that the launch system can safely reach orbit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/New_Glenn">New Glenn - Wikipedia</a></li>
<li><a href="https://www.blueorigin.com/new-glenn">New Glenn | Blue Origin</a></li>
<li><a href="https://en.wikipedia.org/wiki/Static_fire_test">Static fire test</a></li>

</ul>
</details>

**Discussion**: Commenters lamented the infrastructure damage and predicted over a year of repairs, while some noted the test’s methane energy equivalent to about 13 kilotons of TNT. Others argued the incident changes little for U.S. spaceflight given SpaceX’s dominance, but hoped Blue Origin would learn lessons for future ambitions.

**Tags**: `#Blue Origin`, `#New Glenn`, `#rocket explosion`, `#static fire test`, `#space launch`

---

<a id="item-2"></a>
## [GitHub bans security researcher who posted zero-day Windows exploits](https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation) ⭐️ 8.0/10

GitHub banned a security researcher after they published proof‑of‑concept code for previously undisclosed zero‑day vulnerabilities in Windows, prompting debate over responsible disclosure and platform moderation. The incident underscores the clash between platform policies that prohibit exploit publication and the security community’s reliance on responsible disclosure to improve software safety, potentially affecting bug bounty incentives and researcher‑vendor relations. The researcher’s posts included exploit PoCs for Windows zero‑days; GitHub’s ban followed Microsoft’s alleged pressure, and commenters speculate about personal motives and lack of compensation.

hackernews · possibilistic · May 28, 21:45 · [Discussion](https://news.ycombinator.com/item?id=48315968)

**Background**: A zero‑day exploit is a previously unknown vulnerability that attackers can use before a patch is available, often shared as proof‑of‑concept code to demonstrate risk. Responsible disclosure (also called coordinated vulnerability disclosure) encourages researchers to report such flaws to vendors privately before public release, allowing fixes to be developed. Bug bounty programs reward researchers for responsibly reporting vulnerabilities, providing financial incentives that align with coordinated disclosure. Platforms like GitHub host code repositories and must balance openness with policies that prohibit publishing harmful exploit code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cyderes.com/howler-cell/windows-zero-day-bluehammer">BlueHammer: Inside the Windows Zero-Day</a></li>
<li><a href="https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-program">Coordinated Vulnerability Disclosure Program - CISA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bug_bounty_program">Bug bounty program - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed confusion about the ban, speculated that Microsoft might regret the move, questioned whether any public statement was made, suggested the researcher could have a personal vendetta, and debated whether platforms now bear editorial responsibility for hosted exploit code.

**Tags**: `#cybersecurity`, `#zero-day exploits`, `#GitHub`, `#responsible disclosure`, `#bug bounty`

---

<a id="item-3"></a>
## [: Building durable workflows on Postgres](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

The blog post explores using PostgreSQL as the core storage and coordination layer for durable workflow engines, comparing implementations such as absurd, Restate.dev, Cloudflare workflows, Temporal, and DBOS. It demonstrates that a traditional relational database can provide reliable, transaction‑backed execution for complex workflows, reducing reliance on external orchestrators and lowering operational overhead. The discussion highlights specific systems—Armin Ronacher’s absurd, Restate.dev for self‑hosted payment integrations, Cloudflare workflows for cheap report generation, DBOS for atomic messaging tied to Postgres transactions, and Temporal with noted payload size limits.

hackernews · KraftyOne · May 28, 18:41 · [Discussion](https://news.ycombinator.com/item?id=48313530)

**Background**: Durable workflow engines persist execution state so that workflows can survive crashes and be resumed exactly where they left off. PostgreSQL provides strong ACID transactions, logical replication, and change‑data‑capture capabilities that make it well suited to store workflow state and coordinate steps. Projects like pg‑workflows and DBOS leverage these features to build lightweight orchestrators directly on top of Postgres, avoiding external queues or dedicated state stores.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dbos.dev/blog/why-postgres-durable-execution">Why Postgres is a Good Choice for Durable Workflow Execution | DBOS</a></li>
<li><a href="https://sokratisvidros.github.io/pg-workflows/">pg-workflows | The simplest Postgres workflow engine for TypeScript ...</a></li>
<li><a href="https://supabase.com/blog/durable-workflows-in-postgres-dbos">Running Durable Workflows in Postgres using DBOS</a></li>

</ul>
</details>

**Discussion**: Commenters pointed out Armin Ronacher’s absurd as a Postgres‑based workflow example, discussed patterns inspired by Spanner’s change streams, shared personal usage notes comparing Restate.dev, Cloudflare workflows and DBOS for different reliability and cost needs, and raised questions about DBOS versus Temporal, especially regarding payload limits and operational experience.

**Tags**: `#PostgreSQL`, `#durable workflows`, `#workflow engines`, `#distributed systems`, `#DBOS`

---

<a id="item-4"></a>
## [: ](https://arxiv.org/abs/2605.27887) ⭐️ 8.0/10

PortBench proposes a correlation-aware, full-pipeline benchmark for evaluating LLMs in portfolio management, combining static QA and dynamic allocation tasks.

rss · arXiv Quantitative Finance · May 28, 04:00

**Tags**: `#LLM`, `#portfolio management`, `#benchmark`, `#finance`, `#AI`

---

<a id="item-5"></a>
## [:From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets](https://arxiv.org/abs/2605.28359) ⭐️ 8.0/10

The paper introduces KTD‑Fin, a memory‑controlled benchmark that masks historical identifiers and calendar data to prevent LLM memorization and uses a Barra‑style attribution framework to isolate stock‑selection alpha from market beta. By separating genuine investment skill from passive market exposure, KTD‑Fin provides a cleaner signal for evaluating LLM trading agents, guiding researchers toward more skill‑focused model development. KTD‑Fin applies a data‑side masking protocol that anonymizes tickers, dates and prices across prompts and tools, then decomposes returns into market, style and stock‑selection components using a Barra‑style model; tests on ten frontier LLMs trading the CSI300 (2024‑2026) show most returns are explained by market and style factors, with limited persistent alpha.

rss · arXiv Quantitative Finance · May 28, 04:00

**Background**: Large language model agents are increasingly tested in end‑to‑end trading simulations where they make buy/sell decisions based on historical market data and their portfolio returns are used as a performance metric. However, such backtests can suffer from memorization bias when the model has seen the same tickers, dates or news during pretraining, and raw returns conflate skill with market beta or style exposure. The Barra‑style attribution framework separates returns into market, style and stock‑selection (alpha) components to isolate true investment skill.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.28359">From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alpha_(finance)">Alpha (finance) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#trading benchmark`, `#financial AI`, `#evaluation methodology`, `#KTD-Fin`

---

<a id="item-6"></a>
## [: Well-posedness of Infinite-Dimensional LQ MFG with Common Noise.](https://arxiv.org/abs/2601.13493) ⭐️ 8.0/10

The work establishes well-posedness and epsilon-Nash properties for linear-quadratic mean field games in Hilbert spaces influenced by infinite-dimensional common noise across all time horizons.

rss · arXiv Quantitative Finance · May 28, 04:00

**Tags**: `#mean field games`, `#stochastic control`, `#infinite-dimensional systems`, `#linear-quadratic`, `#common noise`

---

<a id="item-7"></a>
## [: From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems](https://arxiv.org/abs/2605.23955) ⭐️ 8.0/10

The paper surveys sources of nondeterminism in tabular models, graph neural networks, and LLM‑based agentic workflows used in financial AI, quantifying explanation rank instability, prediction flip rates, and tensor‑parallel output divergence on public financial datasets. It proposes a layered evaluation framework linking modality‑specific metrics to audit readiness. Reproducibility and auditability are critical for regulated financial applications such as credit risk, fraud detection, and anti‑money laundering; this survey provides actionable insights for meeting compliance requirements. It helps researchers and practitioners identify and mitigate sources of nondeterminism across dominant AI modalities. The study examines three modalities: tabular models (post‑hoc explanation variance), graph networks (stochastic sampling and temporal asynchrony), and LLM‑based agentic workflows (batch‑dependent divergence and trajectory drift). Experiments measure explanation rank instability (RBO), prediction flip rates (D_cos), and tensor‑parallel‑induced output divergence (TDI, PSD), linking these metrics to a layered audit‑readiness framework.

rss · arXiv Quantitative Finance · May 28, 04:00

**Background**: Determinism in machine learning refers to producing identical outputs given the same inputs and model state, which is essential for auditability in regulated finance. Sources of nondeterminism include hardware‑level variations, stochastic algorithms such as random sampling in GNNs, and batch‑level effects in LLM serving (e.g., KV cache reuse). Tabular models often rely on post‑hoc explanation methods whose rankings can shift, while GNNs suffer from sampling randomness and temporal misalignment, and LLM workflows exhibit divergence when processing similar batches in parallel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post_hoc_analysis">Post hoc analysis - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2508.00267">Neighbor-Sampling Based Momentum Stochastic Methods for Training Graph ...</a></li>
<li><a href="https://arxiv.org/html/2509.02121v2">Batch Query Processing and Optimization for Agentic Workflows</a></li>

</ul>
</details>

**Tags**: `#AI reproducibility`, `#financial AI`, `#determinism`, `#auditability`, `#machine learning`

---