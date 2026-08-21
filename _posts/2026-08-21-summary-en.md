---
layout: default
title: "Horizon Summary: 2026-08-21 (EN)"
date: 2026-08-21
lang: en
---

> From 36 items, 14 important content pieces were selected

---

1. [Malicious Rust crate arrayref delivers build-time payload via proc macro](#item-1) ⭐️ 9.0/10
2. [GitHub details August 17 outage caused by retry loops and internal endpoint delays](#item-2) ⭐️ 8.0/10
3. [HN post compares Aaron Swartz prosecution to Meta's data scraping](#item-3) ⭐️ 8.0/10
4. [AliExpress uses silent WebAudio fingerprinting that disrupts Bluetooth multipoint](#item-4) ⭐️ 8.0/10
5. [Show HN: I trained a 125M model to autocomplete piano on-device](#item-5) ⭐️ 8.0/10
6. [Shot-scraper-style JSON API built with Bun 1.4's Bun.WebView](#item-6) ⭐️ 8.0/10
7. [Tradable Itô Signatures Enable Model-Free Dynamic Hedging](#item-7) ⭐️ 8.0/10
8. [FinSkillBench Benchmark Evaluates AI Agents in Investment Management](#item-8) ⭐️ 8.0/10
9. [AI leaderboards fail the Global South due to lack of governance.](#item-9) ⭐️ 8.0/10
10. [Shifting Social Dispositions, Stable Prosocial Traits: Global Age-Period-Cohort Analysis of Human Personality](#item-10) ⭐️ 8.0/10
11. [CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks](#item-11) ⭐️ 8.0/10
12. [Europe's Climate Ambition Under Scrutiny: Evidence from Deep Learning Emission Projections.](#item-12) ⭐️ 8.0/10
13. [Multidimensional Sorting: Comparative Statics of Technological Change](#item-13) ⭐️ 8.0/10
14. [AI‑derived monetary‑policy expectations predict Bitcoin returns, showing Bitcoin as a barometer of central‑bank signals](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Malicious Rust crate arrayref delivers build-time payload via proc macro](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 9.0/10

A compromised version of the popular Rust crate arrayref was published that depended on a typosquatted proc‑macro1 crate, whose build script downloaded and executed a remote binary during compilation. The incident highlights serious supply‑chain weaknesses in crates.io, showing how attackers can hijack trusted crates to execute arbitrary code on developers’ machines at build time. The malicious arrayref versions (e.g., 0.2.6) added a dependency on proc‑macro1, which used a build.rs script to fetch and run a payload from a command‑and‑control server; the compromised versions were later removed but no yank or security advisory was left on crates.io.

hackernews · abhisek · Aug 20, 13:23 · [Discussion](https://news.ycombinator.com/item?id=49374269)

**Background**: Rust crates are packages published to crates.io and consumed via Cargo; they can include build scripts (build.rs) and procedural macros that run code at compile time. A proc macro is a special crate that extends the Rust compiler’s syntax processing, and its build script can execute arbitrary commands before the macro is used. Supply‑chain attacks exploit these mechanisms by publishing malicious versions of trusted crates that execute harmful payloads during the build process.

<details><summary>References</summary>
<ul>
<li><a href="https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/">Malicious Rust Crate arrayref Runs a Build-Time Payload</a></li>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates with...</a></li>
<li><a href="https://doc.rust-lang.org/cargo/reference/build-scripts.html">Build Scripts - The Cargo Book</a></li>

</ul>
</details>

**Discussion**: Commenters criticized crates.io’s handling, noting the lack of a yank or advisory and calling for better incident response; several urged Cargo to sandbox build.rs scripts to prevent similar attacks, while others warned that Rust’s deep dependency trees make it vulnerable to supply‑chain threats similar to the JavaScript ecosystem.

**Tags**: `#rust`, `#supply-chain-security`, `#malware`, `#crates.io`, `#build-time attack`

---

<a id="item-2"></a>
## [GitHub details August 17 outage caused by retry loops and internal endpoint delays](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) ⭐️ 8.0/10

GitHub published a post‑mortem explaining that the August 17 outage was triggered by errors in internal services that caused client‑side retry loops, which amplified traffic by roughly 10× and delayed recovery of the Copilot Token Service due to delayed replies to a single internal endpoint. The incident highlights how retry loops and latency spikes can cascade in large‑scale SaaS platforms, offering lessons for DevOps teams on traffic amplification and resilience, while affecting millions of developers who rely on GitHub and Copilot for daily work. The retry loop increased traffic approximately tenfold, the internal endpoint delay exposed a latent bug in VS Code, and commit growth has surged from 1.4 billion to 2.9 billion per month since April; GitHub is implementing circuit breakers, exponential backoff, and enhanced observability to prevent recurrence.

hackernews · 0xedb · Aug 20, 19:22 · [Discussion](https://news.ycombinator.com/item?id=49378957)

**Background**: In distributed systems, retry loops intended to handle transient failures can unintentionally amplify traffic—a phenomenon known as the thundering herd—especially when clients employ fixed retry intervals without jitter. Latency in internal microservice endpoints often stems from network overhead, serialization/deserialization, and inter‑service dependencies, which can degrade user experience and threaten SLA compliance during high‑load periods. Understanding these dynamics helps explain how a delayed reply to a single endpoint triggered a large‑scale outage for GitHub.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thesoftwarefrontier.com/p/how-systems-really-fail-part-i">How Systems Really Fail, Part I</a></li>
<li><a href="https://www.zigpoll.com/content/how-can-we-reduce-latency-and-improve-response-times-across-our-distributed-microservices-architecture-for-high-traffic-events">Latency and response time optimization is a strategic process focused on identifying, analyzing, and improving the speed at which distributed microservices respond to requests—especially during high-traffic events. In a microservices architecture, applications are decomposed into loosely coupled services communicating over networks. While this design enhances flexibility and scalability, it often introduces latency due to network overhead, serialization/deserialization, and inter-service dependencies.</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the striking rise in monthly commits from 1.4 billion to 2.9 billion since April, with some calling it a “productivity panic.” Others debated whether GitHub should start charging for commits to curb AI‑heavy usage, while noting Microsoft’s incentive to keep developers using its AI models. Many praised the detailed post‑mortem, but warned that retry loops can leave users staring at spinners for hours if not properly mitigated.

**Tags**: `#github`, `#outage`, `#postmortem`, `#scaling`, `#devops`

---

<a id="item-3"></a>
## [HN post compares Aaron Swartz prosecution to Meta's data scraping](https://blog.curiousquail.com/im-upset-again-about-a-co-creator-of-rss-being-prosecuted-for-something-meta-is-doing-with-little-consequence/) ⭐️ 8.0/10

A Hacker News post titled 'Aaron Swartz was prosecuted for scraping, while Meta does it without consequence' garnered 900 upvotes and 206 comments, highlighting the perceived double standard between Swartz's CFAA prosecution and Meta's AI training data scraping. The discussion underscores concerns about unequal application of the Computer Fraud and Abuse Act, highlighting how individual activists face severe penalties while large corporations like Meta engage in similar data collection with little legal repercussion, influencing AI ethics and internet freedom debates. Swartz was charged under the CFAA for downloading JSTOR articles after bypassing network bans via MAC address spoofing, facing up to 35 years though prosecutors sought lesser penalties; Meta's AI training relies on scraping publicly available web content, which currently violates platforms' terms of service but is not prosecuted criminally under CFAA due to recent DOJ policy shifts and the Ninth Circuit's hiQ ruling.

hackernews · speckx · Aug 20, 20:07 · [Discussion](https://news.ycombinator.com/item?id=49379550)

**Background**: The Computer Fraud and Abuse Act (CFAA) prohibits accessing a computer without authorization or exceeding authorized access. Aaron Swartz was prosecuted under the CFAA after downloading millions of JSTOR articles while evading IP bans by spoofing his MAC address, a case that highlighted the law's broad reach. In contrast, the Ninth Circuit’s hiQ decision held that scraping a publicly available website without a cease‑and‑desist letter does not violate the CFAA, and the DOJ’s May 2022 policy revision allows such letters to revoke permission, leaving large‑scale scraping by companies like Meta primarily a civil, not criminal, issue.

<details><summary>References</summary>
<ul>
<li><a href="https://newmedialaw.proskauer.com/2022/05/24/doj-revises-policy-for-cfaa-prosecution-to-reflect-developments-in-web-scraping-and-other-matters/">DOJ Revises Policy for CFAA Prosecution to Reflect Developments in Web Scraping and Other Matters | New Media and Technology Law Blog</a></li>
<li><a href="https://www.rcfp.org/scraping-not-violation-cfaa/">Does scraping violate the Computer Fraud and Abuse Act? Federal appeals court says no.</a></li>
<li><a href="https://www.justthink.ai/blog/metas-ai-copyright-scandal-internal-documents-reveal-training-data-controversy">Meta's AI Copyright Scandal: Internal Documents Reveal Training Data Controversy — Just Think | Just Think AI</a></li>

</ul>
</details>

**Discussion**: Commenters debated the factual details of Swartz’s case, with some emphasizing that his actions involved trespassing and MAC address spoofing rather than simple web scraping, while others criticized the mythologizing of Swartz and pointed out prosecutorial overreach. Several noted the economic and political reluctance to pursue large corporations like Meta for similar data practices, highlighting a perceived double‑standard in enforcement. Overall, the discussion reflected concerns about selective application of the CFAA and its implications for AI training data and internet freedom.

**Tags**: `#Aaron Swartz`, `#web scraping`, `#AI ethics`, `#legal issues`, `#Meta`

---

<a id="item-4"></a>
## [AliExpress uses silent WebAudio fingerprinting that disrupts Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) ⭐️ 8.0/10

In August 2026, the AliExpress homepage was found to silently create two WebAudio graphs from heavily obfuscated Alibaba security scripts, generating and analyzing a waveform as part of a browser fingerprint and connecting them through a zero‑gain node to the system audio destination, which keeps the Bluetooth audio path active and prevents multipoint headphones from switching back to a phone. This technique highlights a privacy‑security flaw where silent audio fingerprinting can interfere with legitimate device functions, affecting anyone who relies on Bluetooth multipoint for seamless audio switching and raising concerns about browsers allowing hidden background audio that may also enable persistent tracking or background execution on mobile devices. The fingerprinting uses two WebAudio graphs, a zero‑gain node to silence output, and heavily obfuscated Alibaba security scripts to generate a waveform for entropy collection; it keeps the Bluetooth audio path active, thereby breaking multipoint switching, while Firefox has mitigations but other browsers remain vulnerable, and silent audio could allow websites to run in the background on mobile browsers.

hackernews · emctech · Aug 20, 10:08 · [Discussion](https://news.ycombinator.com/item?id=49372583)

**Background**: WebAudio fingerprinting exploits subtle differences in how devices process audio signals—using nodes such as DynamicsCompressor and OscillatorNode—to generate entropy that can uniquely identify a browser or device. Bluetooth multipoint is a feature that lets a pair of headphones maintain simultaneous connections to two source devices, enabling seamless switching between, for example, a phone and a computer without manual re‑pairing. When a webpage silently drives audio through the system audio destination, it can keep the Bluetooth audio channel active, preventing the headphones from releasing the connection to the secondary device.

<details><summary>References</summary>
<ul>
<li><a href="https://detect.expert/blog/web-audio-api-technology-in-anti-fraud-systems-and/">Web Audio API technology in Anti-Fraud systems and methods of user...</a></li>
<li><a href="https://www.digitaltrends.com/phones/what-is-bluetooth-multipoint/">What is Bluetooth multipoint and why your next... - Digital Trends</a></li>
<li><a href="https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html">laserphile: AliExpress webpage keeping multipoint Bluetooth headphones active with WebAudio fingerprinting</a></li>

</ul>
</details>

**Discussion**: Commenters noted that silent audio does not trigger the browser’s speaker icon, making the activity hard to detect; some reported hearing‑aid amplification changes and car audio glitches linked to the AliExpress iOS app; others pointed out that Firefox mitigates the fingerprinting but expressed concern about broader browser vulnerabilities and speculated that Apple might remove such apps from the App Store.

**Tags**: `#WebAudio`, `#fingerprinting`, `#Bluetooth`, `#privacy`, `#security`

---

<a id="item-5"></a>
## [Show HN: I trained a 125M model to autocomplete piano on-device](https://simedw.com/2026/08/20/midi-autocomplete/) ⭐️ 8.0/10

The author trained a 125M-parameter transformer model to autocomplete piano performances in real time, achieving about 108 notes per second on an iPhone 15. Users can play a few MIDI notes and the model continues the sequence entirely on-device, with a free app available for trial. This work shows that large transformer models can run efficiently on mobile devices for creative tasks, opening new possibilities for AI-assisted music composition and performance. It highlights the growing trend of on-device AI that reduces latency and privacy concerns while enabling interactive artistic tools. The model uses a transformer architecture with 125M parameters, processes MIDI token sequences, and was refined with aggressive data cleaning and DPO post‑training. On an iPhone 15 it generates roughly 108 notes per second via Core ML, and the accompanying app is free to download.

hackernews · simedw · Aug 20, 12:04 · [Discussion](https://news.ycombinator.com/item?id=49373456)

**Background**: Transformer‑based models have been applied to music generation, with examples such as Hookpad Aria’s 360M‑parameter model for pop‑song continuation and the Anticipatory Music Transformer for controllable infilling. On‑device inference is enabled by Apple’s Core ML framework, which optimizes models for the Neural Engine and has seen performance gains in recent iOS releases. These advances allow real‑time, low‑latency applications like MIDI autocomplete to run directly on smartphones without relying on cloud compute.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/hookpad-aria">Hookpad Aria: Generative AI for Pop Music</a></li>
<li><a href="https://crfm.stanford.edu/2023/06/16/anticipatory-music-transformer.html">Anticipatory Music Transformer: A Controllable</a></li>
<li><a href="https://blakecrosley.com/blog/core-ml-on-device-inference">Core ML On-Device Inference: The Patterns That Actually Ship</a></li>

</ul>
</details>

**Discussion**: Commenters noted the analogy to classical composer training and likened the tool to AI‑assisted UX design, emphasizing the role of taste in curating generations. Several asked for details about the training data size and compared the project to algorithmic melody generation efforts aimed at copyright issues. Overall, the discussion was enthusiastic, with interest in both the technical implementation and the creative possibilities.

**Tags**: `#machine learning`, `#music generation`, `#on-device AI`, `#transformer`, `#MIDI`

---

<a id="item-6"></a>
## [Shot-scraper-style JSON API built with Bun 1.4's Bun.WebView](https://simonwillison.net/2026/Aug/20/bun-webview-json-api/) ⭐️ 8.0/10

On August 20, 2026, Simon Willison demonstrated how to create a shot‑scraper‑like JSON API using Bun 1.4’s newly released Bun.WebView feature, which enables browser automation via WebKit or Chromium CDP. This example shows how Bun 1.4’s performance improvements and new APIs can be leveraged for lightweight web scraping and automation services, offering developers a fast, low‑memory alternative to traditional Node.js‑based tools. The implementation is a TypeScript server that loads a page with Bun.WebView, runs user‑supplied JavaScript, and returns the result as JSON; testing shows it runs comfortably in a 192 MB–256 MB container when using a full Chromium instance.

rss · Simon Willison · Aug 20, 15:37

**Background**: Bun is a fast JavaScript runtime that, starting with version 1.4, includes built‑in APIs such as Bun.WebView for controlling web browsers via WebKit or the Chrome DevTools Protocol. Shot‑scraper is a command‑line tool that can execute JavaScript on a web page and return the result as JSON, often used for lightweight data extraction. By combining Bun.WebView with a simple HTTP server, developers can expose shot‑scraper‑style functionality as a JSON API.

<details><summary>References</summary>
<ul>
<li><a href="https://bun.sh/blog/bun-v1.4">Bun 1 . 4 | Bun Blog</a></li>
<li><a href="https://shot-scraper.datasette.io/en/stable/javascript.html">Scraping pages using JavaScript - shot - scraper</a></li>
<li><a href="https://simonwillison.net/2026/Aug/20/bun-webview-json-api/">Research: A shot-scraper-style JSON API on Bun 1 . 4 's new...</a></li>

</ul>
</details>

**Tags**: `#Bun`, `#WebView`, `#JavaScript`, `#API`, `#shot-scraper`

---

<a id="item-7"></a>
## [Tradable Itô Signatures Enable Model-Free Dynamic Hedging](https://arxiv.org/abs/2608.18120) ⭐️ 8.0/10

The paper introduces an interpretable machine‑learning framework for dynamic hedging that uses the Itô signature transform to convert asset‑price paths into linear features, showing each discretized signature component can be perfectly replicated by a simple self‑financing strategy of underlying assets and cash. By providing a model‑free, transparent hedging basis with theoretical error bounds and low computational cost, the approach offers a practical alternative to neural‑network‑based methods for pricing and hedging both vanilla and path‑dependent options. The discretized Itô signature components are shown to be exactly replicable by self‑financing strategies using only the underlying and cash, enabling derivative payoffs to be approximated as linear combinations of these tradable bases; a signature‑kernel weighted version further localizes estimation to similar historical market paths, and simulations demonstrate strong sample efficiency at lower cost than neural‑network benchmarks.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: The Itô signature transform computes iterated integrals of a time series, turning asset‑price paths into a set of linear features that can universally represent nonlinear functions of the path. A self‑financing trading strategy is one where changes in portfolio value come solely from gains or losses on the holdings, without external cash inflows or outflows. Dynamic hedging aims to continuously adjust a portfolio so that its value replicates the payoff of a derivative, and the Itô signature provides a basis of tradable strategies for this replication.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.18120">[2608.18120] Tradable Itô Signatures : A Model-Free, Interpretable...</a></li>
<li><a href="https://www.researchgate.net/publication/347839887_Embedding_and_learning_with_signatures">Embedding and learning with signatures</a></li>
<li><a href="https://www.investopedia.com/terms/d/deltahedging.asp">investopedia.com/terms/d/deltahedging.asp</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#machine learning`, `#stochastic calculus`, `#dynamic hedging`, `#Itô signature`

---

<a id="item-8"></a>
## [FinSkillBench Benchmark Evaluates AI Agents in Investment Management](https://arxiv.org/abs/2608.18099) ⭐️ 8.0/10

FinSkillBench introduces a benchmark with 2,603 task episodes across portfolio construction, risk management, and fundamental analysis to test whether language model agents can apply financial skills. Results show curated skill packages improve performance from 0.366 to 0.528, while self‑generated skills give little benefit. The benchmark provides a standardized way to evaluate AI agents in high‑stakes finance, highlighting that reliable procedural skills can be as important as the underlying model. This guides researchers and practitioners toward skill‑centric development for trustworthy investment‑management AI. FinSkillBench comprises 12 subtasks, each episode supplies point‑in‑time inputs, hidden ground truth, and a task‑specific verifier; three skill conditions are tested (no skill, curated skill packages, self‑generated skills). Evaluations across nine models and an independent Hermes Agent replication confirm the performance gains of curated skills.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: Investment management requires AI agents to retrieve accurate, time‑specific data, combine it with correct computational inputs, invoke domain‑specific methods, and produce auditable outputs. Procedural skill packages—documents and executable components that encapsulate known financial workflows—can help agents perform these steps reliably. FinSkillBench was created to measure whether agents can effectively use such skills in realistic portfolio‑construction, risk‑management, and fundamental‑analysis scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/finskillbench/dataset_and_code_submission">GitHub - finskillbench /dataset_and_code_submission · GitHub</a></li>
<li><a href="https://insights.alphacert.com/agentic-ai-in-action-london">Agentic AI in Action: London Event</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#finance`, `#benchmark`, `#investment management`, `#evaluation`

---

<a id="item-9"></a>
## [AI leaderboards fail the Global South due to lack of governance.](https://arxiv.org/abs/2608.18117) ⭐️ 8.0/10

The position paper argues that AI leaderboards systematically neglect the Global South because they lack independent governance, conflict‑of‑interest policies, and mechanisms for metric evolution, using India’s linguistic diversity as a case study. Highlighting this structural inequity is crucial because it affects over a billion speakers of languages like Hindi, Swahili, and Arabic, and shows that without governance, AI performance gaps persist unaddressed. The paper notes that high‑quality regional benchmarks such as IndicSUPERB, MILU, and LAHAJA already exist for India, yet global leaderboards do not include them, and a consultation with 58 AI practitioners revealed a strong preference for formal governance and disclosure‑based conflict management.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: AI leaderboards rank models on standardized tasks, but their design often reflects the priorities of the Global North, leaving regions with limited influence. The Global South comprises low‑ and middle‑income countries where languages and contexts are under‑represented in mainstream AI evaluation. Existing benchmarks like IndicSUPERB for speech processing, MILU for multi‑task Indic language understanding, and LAHAJA for Hindi accent robustness demonstrate that quality data are available, yet they are omitted from global rankings due to missing governance structures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2208.11761">[2208.11761] IndicSUPERB : A Speech Processing Universal...</a></li>
<li><a href="https://benchlm.ai/benchmarks/milu">MILU Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>
<li><a href="https://arxiv.org/abs/2408.11440">[2408.11440] LAHAJA : A Robust Multi-accent Benchmark for...</a></li>

</ul>
</details>

**Tags**: `#AI fairness`, `#Global South`, `#AI benchmarks`, `#governance`, `#India`

---

<a id="item-10"></a>
## [Shifting Social Dispositions, Stable Prosocial Traits: Global Age-Period-Cohort Analysis of Human Personality](https://arxiv.org/abs/2608.18119) ⭐️ 8.0/10

Using Big Five personality data from 773,714 individuals assessed over 30 years, researchers applied age-period-cohort modeling to show that social interaction traits diverge across generations while a prosocial core remains stable; Generation Z exhibits lower excitement seeking and gregariousness but higher self-consciousness and anxiety. The study provides a rigorous method to separate true cohort effects from aging and period influences, offering clear evidence that personality change is selective rather than global, which informs psychology, sociology, and generational research. The sample comprised N=773,714 participants; the age-period-cohort model isolated cohort effects; social facets examined included excitement seeking, gregariousness, self-consciousness, and anxiety; the stable prosocial core was defined as morality, discipline, and emotional awareness.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: Age-period-cohort (APC) analysis is a statistical technique that attempts to disentangle the effects of age (biological maturation), period (historical time), and cohort (birth group) on outcomes such as personality traits. The Big Five model describes personality across five broad dimensions—Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism—each with specific facets like excitement seeking (under Extraversion) and self-consciousness (under Neuroticism). Prosociability refers to tendencies toward helpful, cooperative, and morally oriented behavior, often considered a core aspect of agreeableness and emotional stability.

<details><summary>References</summary>
<ul>
<li><a href="https://link.springer.com/rwe/10.1007/978-1-4419-1698-3_13">Age Period Cohort Analysis | Springer Nature Link</a></li>
<li><a href="https://www.verywellmind.com/the-big-five-personality-dimensions-2795422">verywellmind.com/the- big - five - personality -dimensions-2795422</a></li>
<li><a href="https://www.researchgate.net/publication/271061824_Positive_psychologists_on_positive_psychology_Michael_Steger">Positive psychologists on positive psychology : Michael Steger</a></li>

</ul>
</details>

**Tags**: `#personality psychology`, `#generational differences`, `#Big Five traits`, `#age-period-cohort analysis`, `#prosociability`

---

<a id="item-11"></a>
## [CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks](https://arxiv.org/abs/2608.18554) ⭐️ 8.0/10

The paper introduces CentaurBench, a unified benchmark that evaluates large language models both in automation mode (producing outputs directly) and augmentation mode (providing assistance text to a weaker worker model) across seven real-world tasks. Performance is measured via blind pairwise comparisons by an LLM judge panel, replicated over ten runs. The results show that automation performance is only weakly correlated with augmentation performance, indicating that excelling at fully automating tasks does not guarantee effective assistance. This highlights the need for benchmarks that reflect LLMs' roles in human‑AI or multi‑agent collaboration rather than automation alone. Across seven economically grounded tasks, an assistant model writes assistance for a standardized lower‑capacity worker model, while in automation mode it produces the deliverable directly; outputs are scored by blind pairwise comparisons from an LLM judge panel. Rankings differ markedly—the automation winner loses augmentation on five of seven tasks, and only one model’s guidance outperforms no guidance on average.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: Large language models are commonly benchmarked on their ability to automate tasks, but in practice they often serve as assistants to humans or other models. Evaluating both automation and augmentation requires a framework that measures how a model’s assistance changes the performance of a weaker partner. CentaurBench uses blind pairwise comparisons judged by LLMs with task‑specific rubrics to approximate human assessment of output quality. The benchmark runs each comparison ten times to ensure statistical robustness.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.18554">CentaurBench: Benchmarking LLM Capabilities on Augmenting vs....</a></li>
<li><a href="https://www.evidentlyai.com/llm-guide/llm-as-a-judge">LLM -as-a- judge : a complete guide to using LLMs for evaluations</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmarking`, `#augmentation`, `#automation`, `#evaluation`

---

<a id="item-12"></a>
## [Europe's Climate Ambition Under Scrutiny: Evidence from Deep Learning Emission Projections.](https://arxiv.org/abs/2608.18690) ⭐️ 8.0/10

Researchers applied deep learning to high-resolution socioeconomic and sectoral data from all EU27 member states through 2023 to project future CO₂ trajectories under current trends. The projection shows EU27 emissions will exceed the 2030 55% reduction target by 35%, revealing a large ambition‑implementation gap that signals the need for additional policy action. The model estimates a shortfall of 620 Mt CO₂ by 2030, with the power sector on track thanks to renewables while mobility accounts for over a third of emissions and shows minimal progress; projections extrapolate historical sectoral momentum without assuming future policy changes.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: The EU has pledged to cut greenhouse‑gas emissions 55% below 1990 levels by 2030 as part of its Fit for 55 package. Achieving this requires coordinated action across energy, transport, industry and agriculture sectors. Recent years have seen rapid renewable deployment in power but slower decarbonization in transport, highlighting sectoral inertia.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.18690">Europe's Climate Ambition Under Scrutiny: Evidence from Deep...</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7279062">Europe’s Climate Ambition Under Scrutiny: Evidence from... :: SSRN</a></li>

</ul>
</details>

**Tags**: `#climate change`, `#deep learning`, `#emissions projection`, `#EU policy`, `#sustainability`

---

<a id="item-13"></a>
## [Multidimensional Sorting: Comparative Statics of Technological Change](https://arxiv.org/abs/2512.10853) ⭐️ 8.0/10

The paper fully characterizes how symmetric and antisymmetric technological changes affect worker earnings and job allocation in multidimensional sorting models, showing that symmetric change passes entirely into earnings while antisymmetric change leads only to reallocation. These results provide a clear theoretical foundation for understanding how different types of technological progress influence labor markets, offering guidance for policy on skill‑biased change and matching efficiency. The analysis shows that symmetric technological change translates one‑for‑one into worker earnings, whereas antisymmetric change only reshuffles job assignments; the relative importance of each margin depends on the complementarity between worker and job traits and their distributions, illustrated quantitatively with U.S. data on cognitive skill‑biased technological change.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: Multidimensional sorting models study how workers with multiple skills are assigned to jobs that require multiple attributes, extending the classic one‑dimensional assignment problem. Comparative statics examine how equilibrium outcomes such as earnings and matching change when underlying parameters—like technology—are varied. Symmetric technological change raises productivity equally across dimensions, while antisymmetric change enhances some dimensions at the expense of others; cognitive skill‑biased technological change is a prominent example that increases the return to cognitive skills relative to manual tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.10853">Multidimensional Sorting : Comparative Statics</a></li>
<li><a href="https://www.albany.edu/sites/default/files/2019-08/MultiDSortingUnderRandomSearch.pdf">Multidimensional Sorting</a></li>
<li><a href="https://bfi.uchicago.edu/wp-content/uploads/BFI_WP_2019147.pdf">Technological Transitions with</a></li>

</ul>
</details>

**Tags**: `#multidimensional sorting`, `#assignment models`, `#labor economics`, `#technological change`, `#comparative statics`

---

<a id="item-14"></a>
## [AI‑derived monetary‑policy expectations predict Bitcoin returns, showing Bitcoin as a barometer of central‑bank signals](https://arxiv.org/abs/2604.08825) ⭐️ 8.0/10

The study constructs a weekly Monetary Policy Expectations (MPE) index by applying an LLM to over 118,000 market messages, then shows that changes in the index significantly predict Bitcoin returns through linear Granger causality and an LSTM‑SHAP model, revealing Bitcoin’s sensitivity to central‑bank signaling. By providing a high‑frequency, text‑based measure of monetary‑policy sentiment, the work links macroeconomic communication to cryptocurrency markets, offering investors and policymakers a new leading indicator for Bitcoin’s price dynamics. The MPE index captures hawkish versus dovish discourse; an LSTM network combined with SHAP values uncovers nonlinear, regime‑dependent effects, showing that hawkish narratives associate with negative Bitcoin returns even after controlling for contemporaneous Federal Funds Rate changes.

rss · arXiv Quantitative Finance · Aug 20, 04:00

**Background**: Monetary policy expectations reflect market anticipations of future central bank actions, often extracted from speeches, statements, and media. Large language models (LLMs) can classify vast amounts of text to quantify hawkish or dovish sentiment, producing indices like the MPE used here. Long Short‑Term Memory (LSTM) networks model temporal dependencies in time series, while SHAP (SHapley Additive exPlanations) explains model outputs by attributing predictions to input features.

<details><summary>References</summary>
<ul>
<li><a href="https://shap.readthedocs.io/en/latest/index.html">Welcome to the SHAP documentation — SHAP latest documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Long_short-term_memory">Long short - term memory - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/monetary-policy-expectations-mpe-index">Monetary Policy Expectations ( MPE ) Index</a></li>

</ul>
</details>

**Tags**: `#Bitcoin`, `#monetary policy`, `#large language models`, `#LSTM`, `#SHAP`, `#financial econometrics`

---