---
layout: default
title: "Horizon Summary: 2026-08-08 (EN)"
date: 2026-08-08
lang: en
---

> From 36 items, 5 important content pieces were selected

---

1. [Ex-NSA Chief Warns Against Internet-Connected Water System Controllers](#item-1) ⭐️ 8.0/10
2. [Postgres Made 300x Faster for Analytics via Batching, Fusion, and SIMD](#item-2) ⭐️ 8.0/10
3. [Website Owner Battles Bots Consuming 99% of Traffic on 1.5M-Page Site](#item-3) ⭐️ 8.0/10
4. [Unified Mathematical Theory of Volatility Surfaces via Hilbert Space Techniques](#item-4) ⭐️ 8.0/10
5. [Velocity- and Regime-Aware Detection of Intraday Options Market Manipulation with SHAP Explainability](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Ex-NSA Chief Warns Against Internet-Connected Water System Controllers](https://www.theregister.com/security/2026/08/07/water-system-controllers-dont-belong-on-the-internet-says-ex-nsa-chief-after-suspected-iran-attacks/5285070) ⭐️ 8.0/10

Former NSA chief Michael Hayden warned that water system controllers should not be connected to the internet following suspected Iranian cyberattacks on U.S. water infrastructure in 2026, sparking technical discussion about securing operational technology. This warning highlights growing risks to critical infrastructure as state-linked hackers increasingly target water systems, which could disrupt essential services and public safety if compromised. The discussion noted that many water systems use insecure RF or Bluetooth links even when not internet-exposed, and that legacy PLCs often run outdated firmware with known vulnerabilities like those affecting EtherNet/IP on port 44818.

hackernews · Bender · Aug 7, 21:19 · [Discussion](https://news.ycombinator.com/item?id=49216362)

**Background**: Operational Technology (OT) refers to hardware and software that monitors and controls industrial devices, such as PLCs in water treatment plants. These systems are increasingly targeted by cyberattacks due to their role in critical infrastructure, yet many lack modern security protections and are difficult to update without risking operational disruption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.epa.gov/system/files/documents/2024-03/assessing-if-a-wws-has-ot_508_c.pdf">Assessing if a Water & Wastewater System has Operational Technology</a></li>
<li><a href="https://colortokens.com/blogs/ot-security-water-utilities-microsegmentation/">Public Water Systems Are Targeted by State Actors: How to Protect PLCs and HMIs in the Operational Technology Network - ColorTokens</a></li>
<li><a href="https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/">OT Security Analysis: Exposed Devices Attacked in US Water Systems</a></li>
<li><a href="https://cybersecuritynews.com/internet-exposed-rockwell-plcs/">4,400+ Internet - Exposed Rockwell PLCs Expose Water Systems to...</a></li>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a">Iranian-Affiliated Cyber Actors Exploit Programmable Logic ... - CISA</a></li>
<li><a href="https://cybernews.com/security/michigan-georgia-water-system-attacks-iran/">Iran-linked water attacks spread to 12 US states | Cybernews</a></li>

</ul>
</details>

**Discussion**: Commenters debated the tradeoffs of connectivity, with some arguing that even air-gapped systems are vulnerable via wireless protocols like RF and Bluetooth, while others suggested modern zero-trust architectures could allow secure remote access when needed. One noted that legacy 30-year-old PLCs should remain disconnected until replaced.

**Tags**: `#cybersecurity`, `#critical infrastructure`, `#OT security`, `#PLC`, `#network security`

---

<a id="item-2"></a>
## [Postgres Made 300x Faster for Analytics via Batching, Fusion, and SIMD](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10

The author details how they achieved 300x faster analytical query performance in Postgres using batching, operator fusion, and SIMD vectorization in the pgrust project, a Rust rewrite of PostgreSQL that maintains wire and SQL compatibility. This achievement demonstrates the potential for modernizing legacy database systems with systems programming languages and hardware-aware optimizations, offering a path to significantly faster analytics without abandoning Postgres compatibility. The pgrust project uses formal verification and differential fuzz testing to ensure correctness, having proven over 1000 user-facing functions behave identically to stock Postgres, and passes all 46,066 regression tests.

hackernews · poly2it · Aug 7, 11:00 · [Discussion](https://news.ycombinator.com/item?id=49208535)

**Background**: PostgreSQL is a widely used open-source relational database traditionally written in C, whose row-oriented execution model can limit analytical query performance. Techniques like batching (processing multiple rows together), operator fusion (combining multiple operations into fewer passes), and SIMD (Single Instruction, Multiple Data) vectorization are commonly used in modern analytical databases to improve throughput by leveraging CPU parallelism and reducing memory bandwidth bottlenecks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now faster than ...</a></li>
<li><a href="https://pgrust.com/">pgrust — postgres, rewritten in rust</a></li>
<li><a href="https://betterstack.com/community/guides/databases/pgrust-postgres/">PGRust: A Rust Rewrite of PostgreSQL That Passes All Regression Tests</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights enthusiasm for the technical approach, with praise for correctness efforts via formal verification and fuzz testing, while some express skepticism about adoption due to trust in the core Postgres team and concerns about long-term maintenance, alongside interest in adaptive planning features.

**Tags**: `#PostgreSQL`, `#query optimization`, `#SIMD`, `#operator fusion`, `#database performance`

---

<a id="item-3"></a>
## [Website Owner Battles Bots Consuming 99% of Traffic on 1.5M-Page Site](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/) ⭐️ 8.0/10

A website owner revealed that 99% of their 1.5 million-page site's traffic consists of scrapers and bots, causing significant financial strain and operational challenges, as detailed in their public account. This highlights a growing threat to independent websites where bot traffic undermines value, increases costs, and erodes creator compensation, prompting urgent need for effective, accessible mitigation strategies. The owner reported normal hosting costs of ~$90/month spiking to 500% during bot surges, with AI crawlers like Claude-searchbot fetching over 200,000 pages in 72 hours for zero referral traffic, and discussed tools like Anubis using proof-of-work to distinguish real browsers.

hackernews · petercooper · Aug 7, 14:51 · [Discussion](https://news.ycombinator.com/item?id=49211386)

**Background**: Bot mitigation involves detecting and blocking automated traffic that abuses websites, using techniques like rate limiting, CAPTCHAs, behavioral analysis, and proof-of-work challenges. As scrapers grow more sophisticated—mimicking humans, rotating IPs, and using headless browsers—simple defenses fail, requiring layered strategies. Services like Cloudflare offer AI-driven crawl control but raise concerns about centralized control over who can access websites.

<details><summary>References</summary>
<ul>
<li><a href="https://queue-it.com/blog/bot-mitigation/">Bot Mitigation : How to Detect & Block Bots</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/">How to prevent web scraping</a></li>
<li><a href="https://blog.captcha.la/posts/2025-11-20-anti-scraping-measures">Essential Anti Scraping Measures to Protect Your... | CaptchaLa Blog</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about relying on centralized providers like Cloudflare, which can silently block users without recourse, undermining the open web. Others praised Anubis as an effective proof-of-work alternative for sites not using major CDNs, while some acknowledged irony in scraping data themselves while complaining about scrapers.

**Tags**: `#web scraping`, `#bot mitigation`, `#Cloudflare`, `#website performance`, `#open web`

---

<a id="item-4"></a>
## [Unified Mathematical Theory of Volatility Surfaces via Hilbert Space Techniques](https://arxiv.org/abs/2608.05198) ⭐️ 8.0/10

The paper develops a unified mathematical theory of implied, local, and learned volatility surfaces using infinite-dimensional state spaces and Hilbert-space techniques, establishing the topology and tangent geometry of arbitrage-free sets and deriving exact modal reduction with closed-form truncation error. This framework unifies representation, dynamics, arbitrage, dimension reduction, learning, simulation, and hedging in volatility modeling, offering quantitative finance researchers a rigorous foundation for arbitrage-free volatility surface construction and analysis. The paper proves that a nondegenerate Gaussian shock at an active constraint exits with probability tending to one half, derives the Musiela maturity-transport identity, identifies the portfolio derivative as a vega field, and obtains the covariance-optimal hedge α* = (H*CH)⁻¹H*Cν using Hilbert-space dynamics and Karhunen–Loève factors.

rss · arXiv Quantitative Finance · Aug 7, 04:00

**Background**: Volatility surfaces describe how implied volatility varies with strike price and time to maturity, and arbitrage-free constraints require positivity, calendar monotonicity, and the butterfly condition. Hilbert-space methods have been previously applied to model the evolution of implied volatility surfaces as solutions to stochastic PDEs, while Karhunen–Loève decomposition is a standard tool for dimensional reduction in functional data analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/0712.1343">[0712.1343] An Hilbert space approach for a class of arbitrage free implied volatilities models</a></li>
<li><a href="https://arxiv.org/html/2608.05198">The Mathematics of Volatility Surfaces Arbitrage Geometry, Local...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kosambi–Karhunen–Loève_theorem">Kosambi– Karhunen – Loève theorem - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#volatility modeling`, `#mathematical finance`, `#arbitrage theory`, `#functional analysis`, `#quantitative finance`

---

<a id="item-5"></a>
## [Velocity- and Regime-Aware Detection of Intraday Options Market Manipulation with SHAP Explainability](https://arxiv.org/abs/2608.05373) ⭐️ 8.0/10

This research introduces a velocity- and regime-aware detection method for intraday options market manipulation, using smoothed state velocity (option-Delta velocity for index options, price velocity for equities) and SHAP-based explainability to achieve perfect recall on regulator-identified manipulation days in out-of-sample testing on the Indian BANKNIFTY index-options dataset. The method addresses a critical challenge in financial surveillance by detecting brief, statistically elusive manipulation patterns that traditional approaches miss, offering regulators a more precise tool to identify pump-and-crash schemes in high-frequency options markets without overwhelming false alerts. The detection pipeline uses minute-level data, strictly out-of-sample testing with pre-fixed thresholds, and conditions detection on market regimes inferred via hidden Markov models; SHAP attribution shows unconfirmed alerts share near-identical feature importance profiles (cosine similarity 0.99) with confirmed manipulation days, suggesting precision limits stem from incomplete labeling rather than model failure.

rss · arXiv Quantitative Finance · Aug 7, 04:00

**Background**: Intraday market manipulation is difficult to detect because its signals are short-lived, buried in high-volume quote data, and statistically indistinguishable from normal volatility. Traditional detectors achieve high recall only by generating excessive false positives, collapsing precision to unusable levels. This paper argues that manipulation leaves a dynamic signature in the velocity (rate of change) of market state—such as option-Delta or price—rather than in absolute levels, making it detectable via velocity-based features.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05373">Velocity- and Regime - Aware Detection of Intraday Options Market ...</a></li>
<li><a href="https://shap.readthedocs.io/en/latest/index.html">Welcome to the SHAP documentation — SHAP latest documentation</a></li>

</ul>
</details>

**Tags**: `#market manipulation detection`, `#financial machine learning`, `#explainable AI`, `#intraday trading`, `#options market surveillance`

---