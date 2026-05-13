---
layout: default
title: "Horizon Summary: 2026-05-13 (EN)"
date: 2026-05-13
lang: en
---

> From 58 items, 18 important content pieces were selected

---

1. [: Needle: 26M Parameter Attention-Only Model for Tool Calling.](#item-1) ⭐️ 8.0/10
2. [CERT Discloses Six Critical CVEs in dnsmasq DNS/DHCP Server](#item-2) ⭐️ 8.0/10
3. [: Why Senior Developers Struggle to Communicate Their Expertise](#item-3) ⭐️ 8.0/10
4. [: ](#item-4) ⭐️ 8.0/10
5. [Quack: The DuckDB Client-Server Protocol](#item-5) ⭐️ 8.0/10
6. [: ](#item-6) ⭐️ 8.0/10
7. [: EFF Urges Warrant Requirement for Border Electronic Device Searches](#item-7) ⭐️ 8.0/10
8. [Canada's Bill C-22 revives surveillance measures.](#item-8) ⭐️ 8.0/10
9. [:Deep Learning Reveals Socio-Spatial Contagion Drives Off-Grid Solar Adoption](#item-9) ⭐️ 8.0/10
10. [:Resolution-Aware Perpetual Futures for Binary Prediction Markets Introduced](#item-10) ⭐️ 8.0/10
11. [A Taxonomy of Event-Linked Perpetual Futures: Variant Designs Beyond the Single-Market Binary Case](#item-11) ⭐️ 8.0/10
12. [: Quantifying Risk-Return Tradeoff in Forecasting Using Finance Metrics](#item-12) ⭐️ 8.0/10
13. [Scalable Order-Book-Dependent Hawkes Process for High-Frequency Trading](#item-13) ⭐️ 8.0/10
14. [: OrderFusion: Encoding Orderbook for End-to-End Probabilistic Intraday Electricity Price Forecasting](#item-14) ⭐️ 8.0/10
15. [:Scalable Open‑Source Deep Learning Models for Hourly Residential Heating and Electricity Demand Forecasting](#item-15) ⭐️ 8.0/10
16. [Mask-First Design Corrects Price-Limit Bias in A-Share Factor Models with GPU Acceleration](#item-16) ⭐️ 8.0/10
17. [: Calibrating Behavioral Parameters with Large Language Models](#item-17) ⭐️ 8.0/10
18. [: Linking CRRA Portfolio Selection to Rényi Information Projection](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [: Needle: 26M Parameter Attention-Only Model for Tool Calling.](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

We open-sourced Needle, a 26M‑parameter attention‑only model distilled from Gemini for single‑shot function calling, achieving 6000 tok/s prefill and 1200 tok/s decode on consumer hardware. Needle shows that tiny, attention‑only models can handle tool use efficiently, enabling agentic AI on phones, watches and other edge devices without large LLMs. The model contains no MLP/FFN layers, consists solely of attention and gating, was pretrained on 200B tokens on 16 TPU v6e for 27 h and post‑trained on 2B synthesized function‑calling tokens for 45 min using Gemini‑generated data across 15 tool categories.

hackernews · HenryNdubuaku · May 12, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48111896)

**Background**: Transformer models, introduced in the “Attention Is All You Need” paper, rely on self‑attention mechanisms and typically combine attention layers with feed‑forward networks (FFNs). Tool calling (or function calling) lets a language model invoke external APIs by predicting the tool name and extracting arguments into a structured JSON call. Recent work shows that for tasks where external knowledge is provided in the prompt, the FFN parameters can be omitted, allowing pure attention‑only architectures to perform well.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Attention_Is_All_You_Need">Attention Is All You Need - Wikipedia</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/function-calling">Function calling - OpenAI API</a></li>
<li><a href="https://arxiv.org/abs/1706.03762">[1706.03762] Attention Is All You Need - arXiv.org Attention Is All You Need: The Original Transformer Architecture Attention Mechanism in ML - GeeksforGeeks [PDF] Attention is All you Need | Semantic Scholar Images The Transformer Architecture - auroria.io A Tour of Attention-Based Architectures</a></li>

</ul>
</details>

**Discussion**: Commenters praised the tiny model’s potential for edge‑device agents and asked for more evidence of its discriminative ability on tool‑use tasks; several suggested publishing a live demo or playground to showcase performance. Others highlighted use cases such as natural‑language CLI tools and privacy‑first desktop/mobile agents, while noting the model’s small size (26 M parameters) makes it easy to experiment with.

**Tags**: `#machine learning`, `#tiny models`, `#tool use`, `#agentic AI`, `#open source`

---

<a id="item-2"></a>
## [CERT Discloses Six Critical CVEs in dnsmasq DNS/DHCP Server](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 8.0/10

CERT has released six new CVE identifiers for serious security vulnerabilities affecting the dnsmasq DNS and DHCP server, including out-of-bounds writes, infinite loops, and buffer overflows. These vulnerabilities affect millions of devices that rely on dnsmasq, such as home routers and IoT gadgets, and underscore the persistent risks posed by memory‑unsafe code in essential network infrastructure. The disclosed CVEs include a remote out‑of‑bounds write in the heap triggered by malformed DNS packets, an infinite loop that can halt dnsmasq’s query responses, and a buffer overflow exploitable via malicious DHCP requests.

hackernews · chizhik-pyzhik · May 12, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48112042)

**Background**: Dnsmasq is a lightweight, open‑source tool that provides DNS caching, DHCP server, TFTP, and router advertisement functions for small networks and is commonly found in home routers and IoT devices. A CVE (Common Vulnerabilities and Exposures) identifier is a standardized reference for publicly known security flaws, enabling coordinated tracking and remediation. Memory safety refers to protections that prevent software from accessing memory in invalid ways, such as buffer overflows; languages like C lack these protections, making them prone to the vulnerabilities seen in dnsmasq.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety</a></li>

</ul>
</details>

**Discussion**: Commenters noted that MaraDNS has undergone AI‑assisted audits with no serious bugs since 2023, argued that the flaws underscore the urgency of rewriting C‑based network code in memory‑safe languages like Rust or Go, and debated whether Debian’s stable branch will promptly patch dnsmasq or merely backport fixes. Others pointed out that OpenWRT is working on a new build and highlighted specific impacts such as heap OOB writes, infinite loops, and DHCP‑triggered buffer overflows.

**Tags**: `#security`, `#dnsmasq`, `#CVE`, `#vulnerability`, `#memory safety`

---

<a id="item-3"></a>
## [: Why Senior Developers Struggle to Communicate Their Expertise](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise) ⭐️ 8.0/10

The article explores why senior developers often fail to communicate their expertise, pointing to tacit knowledge, mismatched expectations, and junior colleagues' lack of interest in mentorship. Understanding these communication barriers is crucial for improving knowledge transfer, team productivity, and effective mentorship in software engineering teams. It notes that much of a senior developer's expertise resides in an internal 'world model' that is difficult to articulate, and that junior developers often do not seek out mentors despite available experience.

hackernews · nilirl · May 12, 15:08 · [Discussion](https://news.ycombinator.com/item?id=48109460)

**Background**: Tacit knowledge refers to skills and understanding that are gained through experience and are hard to formalize or transfer through words alone. Senior developers accumulate such knowledge over years of work, making it challenging to convey to less experienced colleagues. Effective mentorship relies on bridging this gap through communication, practice, and shared problem‑solving.

**Discussion**: Commenters highlighted the tacit, experience‑based nature of expertise, noted that junior developers often show little interest in seeking mentors, and debated whether AI could ever replace the need for human knowledge sharing.

**Tags**: `#software engineering`, `#communication`, `#mentorship`, `#senior developers`, `#soft skills`

---

<a id="item-4"></a>
## [: ](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 8.0/10

A detailed blog post explaining techniques for rendering realistic sky, sunsets, and planetary atmospheres using atmospheric scattering models.

hackernews · ibobev · May 12, 13:26 · [Discussion](https://news.ycombinator.com/item?id=48107997)

**Tags**: `#graphics rendering`, `#atmospheric scattering`, `#computer graphics`, `#procedural generation`, `#visualization`

---

<a id="item-5"></a>
## [Quack: The DuckDB Client-Server Protocol](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB unveils Quack, a client-server protocol enabling remote connections and horizontal scaling for its embedded analytical database.

hackernews · aduffy · May 12, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48111765)

**Tags**: `#DuckDB`, `#Quack protocol`, `#client-server`, `#analytics database`, `#remote access`

---

<a id="item-6"></a>
## [: ](https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/) ⭐️ 8.0/10

Jeff Geerling argues Bambu Lab is abusing the open source social contract by restricting third‑party access and using user‑agent blocking, sparking a lively debate on Hacker News.

hackernews · rubenbe · May 12, 14:54 · [Discussion](https://news.ycombinator.com/item?id=48109224)

**Tags**: `#open-source`, `#3D-printing`, `#Bambu-Lab`, `#ethics`, `#community-discussion`

---

<a id="item-7"></a>
## [: EFF Urges Warrant Requirement for Border Electronic Device Searches](https://www.eff.org/deeplinks/2026/05/eff-fourth-circuit-electronic-device-searches-border-require-warrant) ⭐️ 8.0/10

The Electronic Frontier Foundation (EFF) filed a brief with the U.S. Court of Appeals for the Fourth Circuit arguing that warrantless searches of electronic devices at the U.S. border violate the Fourth Amendment. If the court agrees, the ruling would strengthen digital privacy protections for millions of people living within the 100‑mile "border zone" where such searches are routinely conducted. EFF contends that the border‑search exception does not extend to devices containing vast amounts of personal data, and cites forensic tools like Cellebrite UFED and GrayKey as evidence of the intrusiveness of such searches.

hackernews · hn_acker · May 12, 21:48 · [Discussion](https://news.ycombinator.com/item?id=48115059)

**Background**: The border search exception allows routine inspections of persons and property at international borders without a warrant or probable cause, based on national security interests. However, courts have increasingly recognized that modern smartphones and laptops store extensive private information, raising questions about whether the traditional exception applies to digital devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cellebrite_UFED">Cellebrite UFED - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrayKey">GrayKey</a></li>

</ul>
</details>

**Discussion**: Commenters noted the trial judge’s skeptical view of the government's justification, pointed out that landmark rights cases often involve unsavory defendants, reiterated the article’s title, and highlighted that the 100‑mile border zone encompasses about 80% of the U.S. population.

**Tags**: `#privacy`, `#border search`, `#Fourth Amendment`, `#EFF`, `#legal case`

---

<a id="item-8"></a>
## [Canada's Bill C-22 revives surveillance measures.](https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare) ⭐️ 8.0/10

Canada's Bill C-22 reintroduces mandatory data retention rules requiring telecom and online services to store users' communication metadata for up to one year, and it grants the Minister of Public Safety authority to demand encryption backdoors in end-to-end encrypted messaging apps such as Signal, WhatsApp and iMessage. If enacted, the bill could force encrypted messaging providers to withdraw from Canada or weaken their security, jeopardizing the privacy of millions of Canadians and setting a dangerous precedent for government-mandated surveillance backdoors worldwide. The legislation mandates up to one year of metadata retention and gives the Minister of Public Safety the power to issue technical notices compelling companies to build surveillance backdoors; Apple and Meta have warned that such backdoors would be vulnerable to exploitation by malicious actors and would undermine the security guarantees of end-to-end encryption.

hackernews · Brajeshwar · May 12, 17:35 · [Discussion](https://news.ycombinator.com/item?id=48111531)

**Background**: Mandatory data retention laws require communications providers to store users' metadata—such as call times, numbers, and IP addresses—for set periods to aid law-enforcement investigations. Encryption backdoors are intentional weaknesses built into cryptographic systems that allow authorities to decrypt messages, but they also create exploitable vulnerabilities that can be used by hackers or hostile states. Past efforts, including the UK's Investigatory Powers Act and the stalled US EARN IT bill, have shown that such measures often clash with strong encryption and civil-liberties protections, a concern echoed by the Electronic Frontier Foundation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_retention">Data retention - Wikipedia</a></li>
<li><a href="https://www.eff.org/issues/mandatory-data-retention">Mandatory Data Retention | Electronic Frontier Foundation</a></li>
<li><a href="https://cambridgeanalytica.org/surveillance-privacy/canada-bill-c-22-encryption-backdoor-apple-meta-50971/">Apple and Meta just warned Canada's Bill C - 22 would force them to...</a></li>

</ul>
</details>

**Discussion**: Commenters warn that mandatory data retention and backdoor requirements could cause encrypted messaging services such as Signal, WhatsApp, iMessage and Matrix to block Canadian users and businesses. Others view the bill as a wake-up call that might drive innovation in censorship-resistant technologies, while a long-time Canadian privacy activist lamented that demoralization has left no political remedy. Several note that repeatedly reintroducing such legislation often leads to eventual passage, and one asks why the issue has not attracted more attention.

**Tags**: `#privacy`, `#surveillance`, `#legislation`, `#encryption`, `#Canada`

---

<a id="item-9"></a>
## [:Deep Learning Reveals Socio-Spatial Contagion Drives Off-Grid Solar Adoption](https://arxiv.org/abs/2605.09642) ⭐️ 8.0/10

Researchers used a deep learning segmentation model on a decade of satellite imagery to measure socio-spatial contagion dynamics in off-grid PV adoption across 507 settlement clusters. The study provides empirical evidence of socio-spatial contagion in data-scarce off-grid regions, informing policies that could accelerate renewable energy diffusion through targeted seeding interventions. SSC intensity peaks within 1–2 years of nearby installations and then weakens, while early adoption correlates with range expansion and later adoption with range contraction, indicating a shift from clustering to consolidation.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: Socio-spatial contagion refers to the amplification of technology diffusion through social ties embedded in physical space, where new adopters cluster around prior adopters. The researchers applied a deep learning segmentation model (e.g., Mask2Former or similar) to a ten‑year series of remote sensing images to detect photovoltaic installations across 507 off‑grid settlement clusters. Using spatio‑temporal point pattern inference, they quantified the range and intensity of clustering of new installations around existing ones to assess how contagion evolves over time.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.09642v1">From Expansion to Consolidation: Socio-Spatial Contagion ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0038092X24002330">Generalized deep learning model for photovoltaic module segmentation from satellite and aerial imagery - ScienceDirect</a></li>
<li><a href="https://journal.r-project.org/articles/RJ-2023-025/">Non-Parametric Analysis of Spatial and Spatio-Temporal Point Patterns</a></li>

</ul>
</details>

**Tags**: `#photovoltaic`, `#remote sensing`, `#socio-spatial contagion`, `#off-grid energy`, `#diffusion of innovations`

---

<a id="item-10"></a>
## [:Resolution-Aware Perpetual Futures for Binary Prediction Markets Introduced](https://arxiv.org/abs/2605.10400) ⭐️ 8.0/10

The paper introduces a resolution-aware perpetual futures design (PIRAP) for binary prediction markets and evaluates it empirically with Polymarket data from April 21‑27, 2026. It addresses the mismatch between standard perpetual futures mechanisms and bounded-event underlying assets, offering a risk‑design framework that could improve stability and capital efficiency in DeFi prediction markets. The framework comprises six components: an index estimator (mid‑price, depth‑weighted mid, time‑decayed VWAP), jump‑aware tiered margin, leverage compression schedule, resolution‑aware funding with boundary correction, a multi‑stage halt protocol, and an eligibility framework; empirical tests on Polymarket’s PMXT v2 archive show mixed results, with several pre‑registered floors failing.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: Binary prediction markets trade contracts that pay out based on the occurrence of a yes/no event, with prices reflecting the probability of that event. Perpetual futures are derivative contracts without expiry that rely on funding rates and margin requirements to keep the price close to an underlying index. When the underlying is a bounded‑event probability (which must converge to 0 or 1 at event resolution), standard basis‑only funding and static margin calibrated to continuous volatility can lead to mispricing, excessive liquidations, or bad debt. The paper proposes a resolution‑aware design that explicitly accounts for the impending collapse of the probability distribution as the event resolves.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.10400">Resolution - Aware Perpetual Futures on Binary Prediction Markets...</a></li>
<li><a href="https://github.com/ForesightFlow/event-linked-perps">ForesightFlow/event-linked-perps: Resolution - Aware Perpetual ...</a></li>
<li><a href="https://arxiv.org/pdf/2605.10400">Resolution-Aware Perpetual Futures on Binary Prediction ...</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#perpetual futures`, `#risk management`, `#DeFi`, `#Polymarket`, `#arXiv`

---

<a id="item-11"></a>
## [A Taxonomy of Event-Linked Perpetual Futures: Variant Designs Beyond the Single-Market Binary Case](https://arxiv.org/abs/2605.10428) ⭐️ 8.0/10

The paper introduces a formal taxonomy of seven canonical variants of event-linked perpetual futures that go beyond the simple binary probability-index perpetual, organizing them along four orthogonal design axes: underlying geometry, temporal structure, settlement structure, and venue composition. By systematizing the design space, the work enables developers and researchers to create new prediction‑market‑linked derivatives for DeFi platforms, improves risk‑aware contract design, and bridges theory with practical implementations in emerging financial infrastructure. Notably, the conditional variant suffers from denominator instability as the conditioning event becomes rare; the spread variant requires a three‑channel decomposition of resolution risk; the volatility/entropy variant avoids binary terminal collapse but introduces estimator‑convention and entropy‑decay challenges; and the basket variant needs multi‑period jump‑aware margin whose aggregation depends on correlation.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: Event‑linked perpetual futures are derivatives whose payoff tracks the evolving probability of an outcome in a prediction market, settling continuously as the event resolves. The resolution‑aware risk‑design framework (PIRAP) introduced in Paper 1 provides tools such as jump‑aware margin and index estimators to manage the unique risks of binary‑outcome contracts. Building on this foundation, the current paper extends the framework to more complex underlying structures like conditional probabilities, spreads, baskets, and volatility‑related derivatives, thereby broadening the design space for DeFi and prediction‑market applications.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.10400">[2605.10400] Resolution-Aware Perpetual Futures on Binary ...</a></li>
<li><a href="https://github.com/ForesightFlow/event-linked-perps">ForesightFlow/ event - linked -perps: Resolution-Aware Perpetual ...</a></li>

</ul>
</details>

**Tags**: `#event-linked perpetual futures`, `#derivatives`, `#prediction markets`, `#DeFi`, `#financial engineering`

---

<a id="item-12"></a>
## [: Quantifying Risk-Return Tradeoff in Forecasting Using Finance Metrics](https://arxiv.org/abs/2605.09712) ⭐️ 8.0/10

The paper treats forecast loss differentials relative to a benchmark as a return series and evaluates them with finance‑based risk‑adjusted metrics such as Sharpe, Sortino, Omega and drawdown measures, while introducing a novel Edge Ratio to capture a model’s propensity to deliver uniquely informative predictions. It shows that while average accuracy can often beat professional forecasters, doing so on a risk‑adjusted basis is much harder, highlighting the reliability and judgment value of expert forecasts. The framework applies Sharpe, Sortino, Omega and maximum drawdown to loss differentials, introduces the Edge Ratio, and finds that selected machine learning methods achieve attractive risk profiles for specific targets despite professionals’ low failure rates.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: In forecasting, the difference between a model’s loss and a benchmark’s loss can be treated as a return series, allowing performance to be judged by the same risk‑adjusted measures used for financial assets. Metrics such as the Sharpe ratio, Sortino ratio, Omega ratio and drawdown quantify excess return per unit of risk, downside risk, or tail‑risk, providing a more nuanced view than average accuracy. TabPFN is a foundation model designed for small‑ to medium‑sized tabular data, enabling strong predictions with limited training examples. The Survey of Professional Forecasters aggregates expert judgments on macroeconomic variables, serving as a strong benchmark in many forecasting studies.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.09712">Quantifying the Risk –Return Tradeoff in Forecasting</a></li>
<li><a href="https://en.wikipedia.org/wiki/TabPFN">TabPFN - Wikipedia</a></li>
<li><a href="https://www.financestrategists.com/wealth-management/financial-ratios/omega-ratio/">Omega Ratio | Definition, Components, Advantages & Limitations</a></li>

</ul>
</details>

**Tags**: `#forecasting`, `#risk-adjusted performance`, `#econometrics`, `#machine learning`, `#macroeconomics`

---

<a id="item-13"></a>
## [Scalable Order-Book-Dependent Hawkes Process for High-Frequency Trading](https://arxiv.org/abs/2307.09077) ⭐️ 8.0/10

The paper introduces an order-book-dependent Hawkes process where the intensity equals a standard Hawkes intensity multiplied by high-dimensional functions of order book covariates, and provides a scalable algorithm capable of handling billions of data points. It establishes stationarity, convergence, and consistency results, and validates the model on four NYSE stocks showing that capturing order book nonlinearity improves out-of-sample performance. By integrating detailed order book information into a self-exciting point process, the model offers a more realistic representation of high-frequency trading dynamics, which can improve trading strategy design and risk management. Its scalability to massive datasets makes it practical for real-world applications where high-frequency data across multiple instruments can reach billions of events. The paper states conditions for stationarity of the proposed process, presents an estimation algorithm based on approximate likelihood maximization and proves its convergence, establishes parameter consistency under weak conditions, and suggests a test statistic for out-of-sample model comparison. Empirical results on four NYSE stocks demonstrate that incorporating nonlinear order book features yields better predictive performance than a standard Hawkes process.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: A Hawkes process is a self-exciting point process in which the intensity of events increases after each occurrence, making it suitable for modeling clustered phenomena such as high-frequency trading arrivals. In limit order books, the state of the market is summarized by high-dimensional features (e.g., bid‑ask spread, order depth, imbalance) that evolve rapidly and influence the likelihood of future trades. Because high‑frequency datasets can contain billions of timestamped events, scalable estimation methods are required to fit complex models like the order‑book‑dependent Hawkes process to such data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hawkes_process">Hawkes process</a></li>
<li><a href="https://academic.oup.com/jfec/article/22/4/1098/7241580">Estimation of an Order Book Dependent Hawkes Process for ...</a></li>
<li><a href="https://experts.illinois.edu/en/publications/point-process-estimation-with-mirror-prox-algorithms/">Point Process Estimation with Mirror Prox Algorithms - Illinois Experts</a></li>

</ul>
</details>

**Tags**: `#Hawkes process`, `#high-frequency trading`, `#order book`, `#point process estimation`, `#scalable algorithms`

---

<a id="item-14"></a>
## [: OrderFusion: Encoding Orderbook for End-to-End Probabilistic Intraday Electricity Price Forecasting](https://arxiv.org/abs/2502.06830) ⭐️ 8.0/10

The paper introduces OrderFusion, an end-to-end probabilistic forecasting model that encodes the full limit order book structure using a 2.5D representation and fusion layers to capture buy‑sell interactions, and hierarchically estimates quantiles with non‑crossing constraints. Accurate intraday price forecasts are essential for market participants to manage imbalance risk amid growing renewable generation, and OrderFusion’s microstructure‑aware approach offers a principled way to improve forecast reliability and could be adapted to other continuous auction markets. OrderFusion uses a 2.5D orderbook encoding, fusion layers for interaction‑aware features, and a hierarchical quantile estimator that enforces monotonicity to avoid quantile crossing; ablation studies show each component improves performance, and the implementation is publicly available on GitHub.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: Continuous intraday (CID) markets allow participants to trade electricity close to delivery via continuously posted buy and sell orders, forming a limit order book that reflects real‑time supply‑demand dynamics. Probabilistic forecasting seeks to predict full distributions of future prices, but quantile crossing—where predicted quantiles violate ordering—can undermine reliability. Traditional methods summarize the orderbook with handcrafted features or treat it as a multivariate time series, neglecting the full interaction structure. OrderFusion addresses these gaps by learning an interaction‑aware representation directly from the raw orderbook.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.06830">[2502.06830] OrderFusion: Encoding Orderbook for End-to-End ...</a></li>
<li><a href="https://runyao-yu.com/OrderFusion/">OrderFusion: Encoding Orderbook for End-to-End Probabilistic ...</a></li>
<li><a href="https://www.mdpi.com/1996-1073/18/12/3097">A Review of Electricity Price Forecasting Models in the Day ...</a></li>

</ul>
</details>

**Tags**: `#electricity price forecasting`, `#order book encoding`, `#probabilistic forecasting`, `#intraday markets`, `#machine learning for energy`

---

<a id="item-15"></a>
## [:Scalable Open‑Source Deep Learning Models for Hourly Residential Heating and Electricity Demand Forecasting](https://arxiv.org/abs/2505.22873) ⭐️ 8.0/10

The paper presents scalable, high-resolution open-source probabilistic deep learning models that forecast hourly building-level residential heating and non-heating electricity demand using multimodal building and weather data. It shows RMSE reductions of 18.8% for heating and 27.6% for electricity versus NREL's ResStock model, with WIS improvement of 59%. The approach equips policymakers and grid planners with granular, open‑source tools to improve load forecasting, supporting decarbonization of the U.S. building stock and enhancing grid reliability amid growing renewable penetration. By outperforming the widely used ResStock benchmark, it could accelerate adoption of data‑driven demand forecasting in both research and practice. Models are trained on electricity consumption from a predominantly gas‑heated region, isolating non‑heating end uses such as lighting, appliances, and cooling. They ingest multimodal building attributes—footprint area, height, nearby building density, land use—and high‑resolution weather data, and are evaluated with RMSE and the Weighted Interval Score (WIS).

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: Accurate forecasting of residential heating and electricity demand is vital for grid operation, energy planning, and efforts to decarbonize the building sector. Traditional tools like NREL’s ResStock model provide standardized load profiles based on physics‑based simulations, but they often lack the spatial granularity and adaptability of data‑driven approaches. Recent work leverages deep learning and multimodal building data—such as footprint, height, surrounding density, land use, and high‑resolution weather—to capture demand heterogeneity and quantify forecast uncertainty through probabilistic methods.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2505.22873">Forecasting Residential Heating and Electricity Demand with Scalable...</a></li>
<li><a href="https://data.openei.org/submissions/153?source=post_page---------------------------">OEDI: Commercial and Residential Hourly Load Profiles for all...</a></li>
<li><a href="https://www.techscience.com/CMES/special_detail/power-energy-forecasting">CMES | Special Issues: AI-Driven Advancements in Power and Energy ...</a></li>

</ul>
</details>

**Tags**: `#energy forecasting`, `#deep learning`, `#residential demand`, `#probabilistic modeling`, `#open-source`

---

<a id="item-16"></a>
## [Mask-First Design Corrects Price-Limit Bias in A-Share Factor Models with GPU Acceleration](https://arxiv.org/abs/2507.07107) ⭐️ 8.0/10

The paper introduces a mask-first approach to eliminate upstream contamination from price limits in Chinese A-share factor models, and builds a GPU-vectorized 213-factor engine using PyTorch unfold. On synthetic and real A-share data (2022-2024) it achieves annualised Sharpe ratios of 2.05 and 1.63 respectively.

rss · arXiv Quantitative Finance · May 12, 04:00

**Tags**: `#quantitative finance`, `#machine learning`, `#factor modeling`, `#bias correction`, `#GPU acceleration`

---

<a id="item-17"></a>
## [: Calibrating Behavioral Parameters with Large Language Models](https://arxiv.org/abs/2602.01022) ⭐️ 8.0/10

The paper introduces a framework that treats LLMs as calibrated measurement instruments for behavioral parameters such as loss aversion, herding, extrapolation, and anchoring, using four models and 24,000 agent‑scenario pairs to reveal baseline biases and show that profile‑based calibration yields parameters aligned with human benchmarks. By providing systematic measurement ranges, calibration functions, and explicit boundaries for eight canonical behavioral biases, the work enables more reliable integration of LLMs into behavioral finance and asset‑pricing research. Baseline LLM behavior showed attenuated loss aversion, weak herding, and near‑zero disposition effects; profile‑based calibration induced large, stable shifts in loss aversion, herding, extrapolation, and anchoring. Embedding these calibrated parameters in an agent‑based asset pricing model reproduced short‑horizon momentum and long‑horizon reversal patterns consistent with empirical data.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: Behavioral parameters such as loss aversion, herding, and extrapolation are central to asset‑pricing models but are difficult to measure reliably in humans. Large language models can exhibit systematic rationality biases that deviate from human preferences, yet they can be adjusted through profile‑based calibration techniques. Agent‑based asset pricing models simulate heterogeneous agents to study market dynamics, allowing researchers to test how calibrated behavioral parameters influence price patterns such as momentum and reversal.

<details><summary>References</summary>
<ul>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6668018">Large Language Models as Calibrated Measurement Instruments for ...</a></li>
<li><a href="https://arxiv.org/html/2602.01022v1">Calibrating Behavioral Parameters with Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2409.17266v1">AAPM: Large Language Model Agent-based Asset Pricing Models</a></li>

</ul>
</details>

**Tags**: `#LLM calibration`, `#behavioral finance`, `#agent-based modeling`, `#loss aversion`, `#asset pricing`

---

<a id="item-18"></a>
## [: Linking CRRA Portfolio Selection to Rényi Information Projection](https://arxiv.org/abs/2605.03184) ⭐️ 8.0/10

: The paper shows that single-period CRRA portfolio optimization can be reformulated as a Rényi information‑projection problem, yielding a Blahut‑Arimoto‑style alternating optimization algorithm with closed‑form updates. : By connecting finance with information theory, the work provides a new computationally efficient method for portfolio optimization and opens avenues for cross‑disciplinary research. : The certainty‑equivalent growth rate is decomposed into a Rényi divergence term, a Rényi entropy term, and a log‑partition term; using a variational form of Rényi divergence leads to an alternating scheme with a closed‑form auxiliary update and a KL‑type portfolio step, which empirically converges faster than direct CRRA optimization in low risk‑aversion regimes.

rss · arXiv Quantitative Finance · May 12, 04:00

**Background**: : CRRA utility describes investors whose relative risk aversion is constant, leading to the iso‑elastic utility function. Rényi divergence generalizes the Kullback‑Leibler divergence and quantifies the difference between probability distributions with a tunable order α. The Blahut‑Arimoto algorithm is an iterative method for computing channel capacity or rate‑distortion functions by alternating between optimizing an auxiliary distribution and the input distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rényi_entropy">Rényi entropy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blahut–Arimoto_algorithm">Blahut–Arimoto algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Risk_aversion">Risk aversion - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#portfolio optimization`, `#information theory`, `#CRRA utility`, `#Rényi divergence`, `#Blahut-Arimoto algorithm`

---