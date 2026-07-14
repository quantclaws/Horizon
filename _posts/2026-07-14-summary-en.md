---
layout: default
title: "Horizon Summary: 2026-07-14 (EN)"
date: 2026-07-14
lang: en
---

> From 34 items, 10 important content pieces were selected

---

1. [Build and ship Mac/iOS apps without opening Xcode.](#item-1) ⭐️ 8.0/10
2. [Linux ported to Sega 32X using software synchronization](#item-2) ⭐️ 8.0/10
3. [Telegram's t.me domain suspended amid legal dispute](#item-3) ⭐️ 8.0/10
4. [Samsung Health threatens data deletion for users refusing AI training consent](#item-4) ⭐️ 8.0/10
5. [DOOMQL: Terminal Doom-like game powered entirely by SQL queries](#item-5) ⭐️ 8.0/10
6. [Study shows generative AI boosts learning when used to explain concepts.](#item-6) ⭐️ 8.0/10
7. [Study finds 11% of S&P 500 firms deeply integrated AI by 2025.](#item-7) ⭐️ 8.0/10
8. [Quarter-Hour Periodic Algorithmic Trading Predicts Crypto Futures Returns](#item-8) ⭐️ 8.0/10
9. [Voting Biases in Decentralized Autonomous Organization (DAO) Governance](#item-9) ⭐️ 8.0/10
10. [Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Build and ship Mac/iOS apps without opening Xcode.](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 8.0/10

The article shows how to use command‑line tools such as xcodebuild, fastlane, and the App Store Connect API to compile, sign, notarize, and distribute macOS and iOS applications entirely from the terminal, without ever launching Xcode’s GUI. It also references community‑shared alternatives like xtool and the Axiom project for Linux‑based builds and LLM‑friendly utilities. This approach enables developers to integrate Apple platform builds into CI/CD pipelines, automate releases, and work from non‑macOS environments such as Linux while reducing reliance on Xcode’s heavyweight IDE. It also highlights security trade‑offs when running build agents on personal machines versus sandboxed environments. The guide relies on xcodebuild for building, fastlane for automating code signing, provisioning, and uploads, and the App Store Connect API for notarization and distribution; it notes that running the build agent on a Mac bypasses sandbox protections, potentially exposing SSH keys and other sensitive data.

hackernews · speckx · Jul 13, 18:22 · [Discussion](https://news.ycombinator.com/item?id=48896665)

**Background**: Xcode provides a graphical IDE and the command‑line tool xcodebuild for building Apple platform projects. Fastlane is an open‑source automation tool that handles repetitive tasks such as code signing, generating screenshots, and uploading to TestFlight or the App Store. The App Store Connect API allows programmatic upload, notarization, and management of apps outside Xcode, enabling fully scripted build and release workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/library/archive/technotes/tn2339/_index.html">Technical Note TN2339: Building from the Command Line with Xcode FAQ</a></li>
<li><a href="https://fastlane.tools/">fastlane - App automation done right</a></li>
<li><a href="https://developer.apple.com/app-store-connect/">App Store Connect - Apple Developer</a></li>

</ul>
</details>

**Discussion**: Commenters warned that running the build agent on a personal Mac sacrifices sandbox security, citing an incident where an AI agent uploaded a home directory including SSH keys. Others highlighted successful Linux‑based iOS builds using tools like xtool and praised complementary open‑source projects such as Axiom that provide LLM‑friendly utilities for Apple development.

**Tags**: `#iOS`, `#macOS`, `#development`, `#Xcode alternatives`, `#CI/CD`

---

<a id="item-2"></a>
## [Linux ported to Sega 32X using software synchronization](https://cakehonolulu.github.io/linux-on-32x/) ⭐️ 8.0/10

A developer successfully ran SMP-ready Linux on the Sega 32X add-on by implementing Petersen's algorithm as a software synchronization primitive, enabling symmetric multiprocessing without hardware support. This achievement demonstrates that OS porting ingenuity can overcome severe hardware limitations, inspiring retro‑computing enthusiasts and showing that SMP can be achieved on constrained platforms through clever software solutions. The port uses Petersen's algorithm for mutual exclusion between the two Hitachi SH‑2 processors, runs on the 32X's 23 MHz SH‑2 cores with limited RAM, and was tested primarily in an emulator before hardware verification.

hackernews · cakehonolulu · Jul 13, 18:18 · [Discussion](https://news.ycombinator.com/item?id=48896600)

**Background**: The Sega 32X is an add‑on for the Sega Genesis that contains two Hitachi SH‑2 (SH7095) 32‑bit RISC processors running at about 23 MHz, each with limited local memory and no built‑in hardware synchronization primitives for multiprocessing. Symmetric multiprocessing (SMP) allows an operating system to schedule threads across multiple identical cores, but requires mechanisms such as locks or semaphores to prevent race conditions. In the absence of hardware locks, software algorithms like Petersen's algorithm can provide mutual exclusion using only shared memory reads and writes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/32X">32X - Wikipedia</a></li>
<li><a href="https://consolemods.org/wiki/images/e/e9/32X_Hardware_Manual_1994_Sega_text.pdf">32X Hardware Manual (1994)(Sega) - consolemods.org</a></li>
<li><a href="https://linux-kernel-labs.github.io/refs/heads/master/lectures/smp.html">Symmetric Multi-Processing — The Linux Kernel documentation</a></li>

</ul>
</details>

**Discussion**: Commenters noted the SH‑2's inability to write to cartridge RAM, questioning whether the port was tested on real hardware or only in an emulator, while others highlighted the architectural similarities between SH‑2 and ARM's Thumb instruction set and expressed curiosity about using the serial port for terminal access. Several participants appreciated learning about Petersen's algorithm and referenced Lamport's fast mutex as a related alternative.

**Tags**: `#Linux`, `#Sega 32X`, `#operating systems`, `#retro computing`, `#synchronization algorithms`

---

<a id="item-3"></a>
## [Telegram's t.me domain suspended amid legal dispute](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram's t.me domain has been marked with the clientRenewProhibited status, effectively suspending the domain and breaking all t.me/short links while the Telegram app remains operational. The suspension disrupts the widely used short‑link system for inviting users to channels and groups, affecting millions of Telegram users worldwide and highlighting the platform’s dependence on a single registrar amid ongoing legal scrutiny. WHOIS records show the domain status as clientRenewProhibited, a code typically set during legal disputes or pending deletion, and the domain is registered with GoDaddy; Telegram has not issued an official statement.

hackernews · Tiberium · Jul 13, 19:52 · [Discussion](https://news.ycombinator.com/item?id=48897878)

**Background**: The clientRenewProhibited status code prevents a domain from being renewed without explicit consent, often applied during legal disputes or when a domain is slated for deletion. Telegram’s t.me domain is used globally for short links that redirect to channels, groups, or user profiles, so its suspension breaks those links while the core app continues to work. Reliance on a single registrar such as GoDaddy creates a single point of failure, especially if the registrar faces legal or compliance actions that affect domain management.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openprovider.com/glossary/clientRenewProhibited">What is clientRenewProhibited? - Openprovider</a></li>
<li><a href="https://glitchwire.com/news/telegrams-tme-domain-disappears-from-global-dns-with-no-explanation-pavel-durov/">Telegram's t.me Domain Disappears From Global DNS With No Explanation ...</a></li>
<li><a href="https://dn.org/registrar-level-security-and-the-role-of-domain-registrars-in-managing-risk/">Registrar-Level Security and the Role of Domain Registrars in ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern over Telegram’s reliance on GoDaddy and noted ongoing legal investigations in Russia, France, and India, while some shared that they had already migrated communities to platforms like Zulip. Others highlighted the usefulness of maintaining redirect strategies to mitigate such domain disruptions.

**Tags**: `#Telegram`, `#domain suspension`, `#legal issues`, `#GoDaddy`, `#community discussion`

---

<a id="item-4"></a>
## [Samsung Health threatens data deletion for users refusing AI training consent](https://neow.in/cWsyMTV3) ⭐️ 8.0/10

Samsung Health updated its settings to require users to consent to AI training; opting out triggers a pop‑up warning that all existing health data will be deleted and future syncing will be blocked. The policy forces users to surrender sensitive health data for AI model training or lose access to their own records, highlighting growing privacy tensions in consumer health tech. The AI training toggle covers sleep, medication, medical records, and cycle‑tracking data; disabling it stops cloud sync and triggers permanent deletion, with no built‑in export option mentioned.

hackernews · bundie · Jul 13, 20:01 · [Discussion](https://news.ycombinator.com/item?id=48897991)

**Background**: Samsung Health is a flagship health and fitness platform that aggregates data from Galaxy wearables and smartphones, allowing users to track activity, sleep, nutrition, and more. The app syncs this information to a Samsung account for backup and cross‑device access. Recent updates have introduced an optional AI training feature that uses aggregated health data to improve personalized insights, but the new policy makes participation mandatory for continued data sync.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5google.com/2026/07/13/samsung-health-ai-training-data-consent/">Samsung Health will delete your data without AI training consent</a></li>
<li><a href="https://www.androidauthority.com/samsung-health-train-ai-data-3686684/">Samsung will kill your health data if you don't consent to AI training - Android Authority</a></li>
<li><a href="https://m.gsmarena.com/samsung_health_data_ai_training_consent-news-73683.php">Samsung Health users asked to allow use of their health data for AI training or it will be deleted - GSMArena.com news</a></li>

</ul>
</details>

**Discussion**: Commenters criticized the ultimatum, noting that refusing AI training would render half of the watch’s features useless and questioning whether Samsung should refund device costs. Some sarcastically welcomed the prospect of having their sensitive health data deleted, while others pointed out the absence of a data export tool, making the threat feel like a loss of personal records.

**Tags**: `#privacy`, `#health data`, `#AI training`, `#Samsung Health`, `#user consent`

---

<a id="item-5"></a>
## [DOOMQL: Terminal Doom-like game powered entirely by SQL queries](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 8.0/10

Peter Gostev created DOOMQL, a terminal-based Doom-like game in which all game logic—movement, collision, enemies, combat, and rendering—is implemented as SQL queries using SQLite, built with the assistance of GPT‑5.6 Sol. DOOMQL shows that a lightweight relational database can serve as a full game engine, highlighting the expressive power of SQL for real‑time graphics and interactive simulations. The game uses a recursive CTE in SQLite to perform ray‑tracing, stores state in a file at /tmp/doomql/.doomql/doomql.sqlite, and can be inspected live with Datasette plus the Datasette Apps plugin; it is launched via a Python script run with uv.

rss · Simon Willison · Jul 13, 22:34

**Background**: SQLite is an embedded, zero‑configuration SQL database commonly used for local storage in applications, not typically employed for real‑time game logic. Recursive common table expressions (CTEs) allow SQLite to perform iterative computations, enabling techniques such as ray‑tracing entirely within SQL. Datasette is a tool for exploring and publishing SQLite databases, and its Apps plugin lets users run custom HTML/JavaScript interfaces that can query the database directly; uv is a fast Rust‑based Python package manager that simplifies installing dependencies and running scripts.

<details><summary>References</summary>
<ul>
<li><a href="https://forum.openmw.org/viewtopic.php?t=7193">SQLite based approach to storing game world state - openmw.org</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT - 5 . 6 Sol : a next-generation model | OpenAI</a></li>
<li><a href="https://docs.astral.sh/uv/guides/install-python/">Installing and managing Python | uv - Astral Docs</a></li>

</ul>
</details>

**Tags**: `#SQL`, `#game development`, `#Python`, `#novelty`, `#terminal`

---

<a id="item-6"></a>
## [Study shows generative AI boosts learning when used to explain concepts.](https://arxiv.org/abs/2607.08849) ⭐️ 8.0/10

A randomized controlled study found that giving undergraduates access to off‑the‑shelf generative AI raised immediate test scores by 0.27 standard deviations, with the gain persisting after one week. While essay quality did not change during AI use, it improved in style and relevance a week later, especially for students who used AI to explain concepts rather than to generate text. The study offers high‑quality experimental evidence that distinguishes between using AI as a learning aid (augmentation) and as a shortcut (automation), highlighting that only augmentation yields durable improvements. This helps educators and ed‑tech designers focus on AI applications that promote deeper understanding rather than mere answer generation. Key findings include a 0.27‑SD boost in immediate knowledge tests that persisted after one week, and delayed essay quality improvements that were larger for augmentation users who used AI to explain concepts. The authors attribute gains to students reallocating time from drafting to information seeking and reporting higher enjoyment.

rss · arXiv Quantitative Finance · Jul 13, 04:00

**Background**: Generative AI refers to models like GPT‑4 that can produce text, images, or other content based on prompts. In education, AI can be used either to automate tasks (e.g., generating answers) or to augment learning (e.g., explaining concepts). Randomized controlled trials are the gold standard for assessing causal effects of educational interventions. Understanding whether AI acts as a crutch or a tutor helps guide its integration into classrooms.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.08849">Experimental Evidence on the Learning Impact of Generative AI</a></li>
<li><a href="https://www.forbesindia.com/article/rotman/understanding-ais-effect-on-jobs-automation-versus-augmentation/95827/1">Understanding AI ’s effect on jobs: Automation versus augmentation</a></li>

</ul>
</details>

**Tags**: `#AI in Education`, `#Generative AI`, `#Learning Experiment`, `#Augmentation vs Automation`, `#Student Assessment`

---

<a id="item-7"></a>
## [Study finds 11% of S&P 500 firms deeply integrated AI by 2025.](https://arxiv.org/abs/2607.08920) ⭐️ 8.0/10

The study estimates deep AI adoption in S&P 500 firms using SEC 10-K filings, finding that 11% had AI deeply integrated into business processes by 2025. Adoption more than quadrupled from 5% in 2022, with technology firms driving two‑thirds of the deep integration. By grounding AI adoption in regulated SEC disclosures, the research offers a reliable metric to distinguish genuine integration from hype. These insights help policymakers, investors, and managers gauge enterprise‑level AI impact on productivity and labor markets. The measure classifies firms as having deep AI integration when AI is embedded in core processes, distinct from superficial AI use. Among technology firms, deeper adoption correlates with larger employee counts and higher Tobin’s q, while overall firms show a J‑curve profitability pattern but no significant changes in capex or measured productivity.

rss · arXiv Quantitative Finance · Jul 13, 04:00

**Background**: Artificial intelligence adoption by large enterprises is seen as a potential driver of aggregate productivity and labor‑market change. The S&P 500 index comprises 500 of the largest U.S. publicly traded companies, serving as a bellwether for corporate trends. SEC 10‑K filings are annual reports required by law, in which companies must avoid materially false or misleading statements, making them a credible source for assessing real AI deployment. The study focuses on deep integration—AI woven into business operations—rather than peripheral or experimental uses.

**Tags**: `#AI adoption`, `#enterprise AI`, `#SEC filings`, `#productivity`, `#labor market`

---

<a id="item-8"></a>
## [Quarter-Hour Periodic Algorithmic Trading Predicts Crypto Futures Returns](https://arxiv.org/abs/2607.09426) ⭐️ 8.0/10

The study identifies quarter-hour periodic bursts in cryptocurrency futures linked to algorithmic trading, using declining trade-size roundness as a signature, and shows that order imbalance at these openings predicts four-to-twelve-hour returns via the Autocorrelation Map. It provides novel empirical evidence of periodic algorithmic trading and a practical tool for return prediction, offering insights into crypto market microstructure that can inform traders, researchers, and regulators. Using six Binance perpetual contracts, the authors found trade-size roundness sharply declines within quarter-hour bursts, and the Autocorrelation Map revealed serial dependence in order flow and returns at these openings, with predictive power weakening at finer time marks.

rss · arXiv Quantitative Finance · Jul 13, 04:00

**Background**: Cryptocurrency futures are derivatives whose value is tied to digital assets, often traded on exchanges like Binance. Algorithmic trading uses computer programs to execute orders based on predefined rules, often leaving signatures such as rounded trade sizes. Periodic patterns in trading activity—such as bursts at regular intervals—have been observed in crypto markets and are thought to stem from algorithmic strategies or market mechanisms like funding rates.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09426">[2607.09426] The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures</a></li>
<li><a href="https://quantpedia.com/periodicity-in-cryptocurrencies-recurrent-patterns-in-volatility-and-volume/">Periodicity in Cryptocurrencies – Recurrent Patterns in Volatility and Volume - QuantPedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Algorithmic_trading">Algorithmic trading - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#algorithmic trading`, `#cryptocurrency futures`, `#market microstructure`, `#return predictability`, `#autocorrelation map`

---

<a id="item-9"></a>
## [Voting Biases in Decentralized Autonomous Organization (DAO) Governance](https://arxiv.org/abs/2607.09435) ⭐️ 8.0/10

The study finds that author-selected DAO proposals receive a 58.8% higher voting-power share, with additional advantages for approval-oriented and first-listed choices.

rss · arXiv Quantitative Finance · Jul 13, 04:00

**Tags**: `#DAO`, `#governance`, `#voting bias`, `#token-weighted voting`, `#blockchain`

---

<a id="item-10"></a>
## [Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics](https://arxiv.org/abs/2603.09006) ⭐️ 8.0/10

The paper introduces spectral portfolio theory by identifying SGD-trained neural network weight matrices as portfolio allocation matrices, showing that their spectral structure encodes factor decompositions and wealth concentration patterns. It further demonstrates how the three forces of SGD map to smart money, survival constraint, and endogenous diversification, and how the spectral statistics evolve from Marchenko-Pastur to inverse-Wishart via a free log-normal regime. By unifying machine learning and financial mathematics through a common spectral framework, the work offers new tools for portfolio design, wealth inequality measurement, tax policy analysis, and neural network diagnostics. This interdisciplinary bridge could inspire cross‑disciplinary research and practical applications in both AI-driven finance and the interpretation of deep learning models. The three forces governing SGD—gradient signal, dimensional regularisation, and eigenvalue repulsion—are shown to correspond respectively to smart money, survival constraint, and endogenous diversification in portfolio dynamics. A central Spectral Invariance Theorem states that any isotropic perturbation to the portfolio objective preserves the singular‑value distribution up to scale and shift, while anisotropic distortions scale with the cross‑asset variance of the perturbation.

rss · arXiv Quantitative Finance · Jul 13, 04:00

**Background**: Stochastic gradient descent (SGD) trains neural networks by iteratively updating weight matrices, which at initialization exhibit random matrix statistics described by the Marchenko‑Pastur law. The Marchenko‑Pastur distribution characterizes the asymptotic eigenvalue spectrum of large rectangular random matrices, providing a null model for the spectra of untrained weights. In the long‑run, multiplicative noise drives the spectrum toward an inverse‑Wishart law via a free log‑normal regime, analogous to the transition from daily asset returns to long‑run wealth compounding. The Bouchaud‑Mézard model describes wealth dynamics of interacting agents via a stochastic differential equation, capturing wealth concentration and redistribution processes that the paper links to the spectral properties of SGD weight matrices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Marchenko–Pastur_distribution">Marchenko–Pastur distribution - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2507.12709">From SGD to Spectra: A Theory of Neural Network Weight Dynamics</a></li>
<li><a href="https://arxiv.org/pdf/2603.09006">Spectral Portfolio Theory: From SGD Weight Matrices to Wealth ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#finance`, `#stochastic gradient descent`, `#spectral analysis`, `#portfolio theory`

---