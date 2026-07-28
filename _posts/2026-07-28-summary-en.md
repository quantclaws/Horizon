---
layout: default
title: "Horizon Summary: 2026-07-28 (EN)"
date: 2026-07-28
lang: en
---

> From 27 items, 9 important content pieces were selected

---

1. [Anthropic Advocates Mandatory Safety Testing for All Capable AI Models](#item-1) ⭐️ 8.0/10
2. [Self-contained highly-portable Python distributions are now maintained by Astral.](#item-2) ⭐️ 8.0/10
3. [Missing underscore in police software leads to wrongful 18‑month imprisonment](#item-3) ⭐️ 8.0/10
4. [Researcher exploits Volvo/Eicher fleet platform to gain vehicle control](#item-4) ⭐️ 8.0/10
5. [Release of Paged Out #9 hacker zine on low-level topics](#item-5) ⭐️ 8.0/10
6. [Judge Rejects Google's DMCA Claim Against Search Result Scraper](#item-6) ⭐️ 8.0/10
7. [Moonshot AI releases 2.8‑trillion‑parameter Kimi K3 model with new license](#item-7) ⭐️ 8.0/10
8. [Settlement Modernisation Index reveals S‑curve in inside money elasticity.](#item-8) ⭐️ 8.0/10
9. [Study Detects 1,012 Coordinated Wallet Cohorts on Solana's Pump.fun Marketplace](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic Advocates Mandatory Safety Testing for All Capable AI Models](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic released a position statement arguing that all sufficiently capable AI models, both open-weight and closed, should undergo mandatory safety testing instead of being banned outright. This stance could shape future AI regulation by promoting a safety‑first approach that affects developers of both open and proprietary models. Anthropic calls for independent safety testing, government authority to block or delay risky deployments, and argues that bans are ineffective while not advocating a ban on open‑weight models.

hackernews · surprisetalk · Jul 27, 22:03 · [Discussion](https://news.ycombinator.com/item?id=49076057)

**Background**: Open‑weight models are AI systems whose parameter weights are publicly available, though they may not include training code or data. Mandatory safety testing refers to independent evaluations of powerful AI models to assess risks such as misuse or unintended behavior before deployment. Model governance encompasses frameworks that ensure models operate as intended, remain compliant, and deliver trustworthy results throughout their lifecycle.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/bruceburke_policy-on-the-ai-exponential-activity-7470865808303489025-4mKI">Anthropic Calls for Mandatory Safety Testing of Powerful AI Models</a></li>
<li><a href="https://www.ibm.com/think/topics/model-governance">What Is Model Governance? | IBM</a></li>

</ul>
</details>

**Discussion**: Some commenters argue that mandatory testing requirements could act as a backdoor ban on open‑weight models, while others accuse Anthropic of self‑interest and virtue signaling. Several users pointed out perceived inconsistencies, such as supporting chip bans to China while opposing model bans. Overall, the discussion reflects mixed sentiment with significant skepticism about the proposal’s motives and practicality.

**Tags**: `#AI safety`, `#open-weight models`, `#Anthropic`, `#AI policy`, `#model governance`

---

<a id="item-2"></a>
## [Self-contained highly-portable Python distributions are now maintained by Astral.](https://gregoryszorc.com/docs/python-build-standalone/main/) ⭐️ 8.0/10

The python-build-standalone project releases self-contained, highly-portable Python distributions. Astral now maintains these builds, which are used by tools like uv, pipx, Hatch, Poetry, and Bazel to install Python portably. It allows developers to ship Python with applications or use isolated Python installations without relying on system Python, simplifying deployment and reducing environment conflicts. Its adoption by major tools like uv and pipx shows growing demand for portable Python ecosystems. The distributions bundle CPython binaries and the standard library into a self-contained directory or single file for Linux, macOS, Windows, and BSD variants, and are updated to track upstream CPython releases. Related projects like PyOxy add Rust code to produce single-file executables, while APE/Cosmopolitan offers cross‑platform binaries that run on many OSes.

hackernews · jcbhmr · Jul 27, 18:43 · [Discussion](https://news.ycombinator.com/item?id=49073942)

**Background**: Python builds typically require a system-installed interpreter and dependencies, making redistribution across machines complex. Portable Python distributions package the interpreter and its standard library into a self-contained bundle that can run on any compatible system without installation. Tools like uv and pipx leverage such bundles to provide fast, isolated Python tooling and application execution. The python-build-standalone project automates creation of these bundles for multiple operating systems.

<details><summary>References</summary>
<ul>
<li><a href="https://gregoryszorc.com/docs/python-build-standalone/main/">Python Standalone Builds — python-build-standalone documentation</a></li>
<li><a href="https://astral.sh/blog/python-build-standalone">A new home for python-build-standalone - Astral</a></li>
<li><a href="https://docs.astral.sh/uv/getting-started/installation/">uv is an extremely fast Python package and project manager, written...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the distributions for their reliability and widespread use in tools like uv and pipx, noting Astral's stewardship. Some highlighted related projects such as APE/Cosmopolitan cross‑platform binaries and PyOxy for single‑file executables, while others expressed interest in compiling Python to WebAssembly for desktop use.

**Tags**: `#python`, `#packaging`, `#distribution`, `#portable`, `#uv`

---

<a id="item-3"></a>
## [Missing underscore in police software leads to wrongful 18‑month imprisonment](https://arstechnica.com/tech-policy/2026/07/police-missed-one-underscore-and-sent-the-wrong-man-to-prison/) ⭐️ 8.0/10

A police investigation used a flawed software match caused by a missing underscore in a SQL LIKE clause, which falsely linked an innocent man to child exploitation charges, resulting in his conviction and 18‑month prison sentence. The case shows how a tiny programming oversight can produce severe real‑world harm, prompting calls for greater accountability, compensation for victims, and scrutiny of the 'Computers Don't Argue' mindset in law enforcement. The missing underscore acted as a wildcard that matched any single character, causing the software to return a false positive in a record‑linkage search; digital forensics experts note that similar tool errors can misinterpret evidence and lead to wrongful outcomes.

hackernews · quantified · Jul 27, 22:10 · [Discussion](https://news.ycombinator.com/item?id=49076116)

**Background**: In SQL, the underscore (_) is a wildcard that matches exactly one arbitrary character in a LIKE pattern, so a missing underscore can cause overly broad matches. Record linkage is the process of connecting records that refer to the same entity across datasets, and errors in this process can produce false positives. Digital forensics relies on automated tools; bugs or limitations in these tools can generate incorrect findings, as illustrated by cases where different software reported vastly different counts for the same artifact.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mssqltips.com/sqlservertip/5670/examples-and-function-for-using-sql-server-like-operator-and-wildcard-characters/">SQL LIKE Wildcard with Underscore and More Examples</a></li>
<li><a href="https://en.wikipedia.org/wiki/Record_linkage">Record linkage - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1355030617301508">“I couldn't find it your honour, it mustn't be there!” – Tool errors, tool limitations and user error in digital forensics - ScienceDirect</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the man received little beyond having his conviction vacated after serving 18 months, questioning whether any compensation was offered for lost income and reputational harm. Several referenced the 'Computers Don't Argue' phenomenon, warning that uncritical trust in automated matches can lead to injustice. Others pointed out weaknesses in the prosecution's evidence, the cross‑border nature of the case (US victim, Canadian defendant), and suggested that a stronger defense could have challenged the flawed match.

**Tags**: `#software-error`, `#wrongful-conviction`, `#legal-tech`, `#digital-forensics`, `#accountability`

---

<a id="item-4"></a>
## [Researcher exploits Volvo/Eicher fleet platform to gain vehicle control](https://eaton-works.com/2026/07/27/my-eicher-hack/) ⭐️ 8.0/10

A researcher disclosed a security flaw in Volvo/Eicher's fleet management platform in November 2025, which after months of no response was fixed by November 20, 2025, and the findings were published on July 27, 2026. The vulnerability could allow attackers to take control of numerous commercial vehicles and access user data, highlighting risks in IoT fleet systems and fueling debate over vehicle security and right-to-repair. The flaw resided in the platform's internal APIs, which were disabled after disclosure; the platform is operated by VE Connected Solutions, a 51:49 Volvo Eicher joint venture with iTriangle Infotech.

hackernews · EatonZ · Jul 27, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49070756)

**Background**: Volvo Eicher Commercial Vehicles partnered with iTriangle Infotech in May 2024 to create VE Connected Solutions, which provides the My Eicher fleet management and GPS tracking platform for commercial vehicles. The platform uses IoT telematics to monitor vehicles in real time, allowing fleet managers to track location, performance, and other data. Such interconnected systems can be vulnerable if internal APIs are not properly secured.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Eicher_Motors">Eicher Motors - Wikipedia</a></li>
<li><a href="https://eaton-works.com/2026/07/27/my-eicher-hack/">Exploiting Volvo/Eicher’s fleet management platform to gain control over all users and vehicles</a></li>
<li><a href="https://play.google.com/store/apps/details?id=in.here.volvo.android&hl=en_IN">MY EICHER – Apps on Google Play</a></li>

</ul>
</details>

**Discussion**: Many commenters worried that modern cars depend too much on cloud services for basic functions, pointing out the lengthy disclosure process as indicative of poor responsiveness. Others noted that older models like the 1981 Volvo 244 are unaffected and advocated for designs where phones pair directly with cars, using the cloud only as a proxy.

**Tags**: `#automotive security`, `#vulnerability disclosure`, `#fleet management`, `#IoT security`, `#right-to-repair`

---

<a id="item-5"></a>
## [Release of Paged Out #9 hacker zine on low-level topics](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 8.0/10

Paged Out #9, the ninth issue of the hacker zine Paged Out, has been released as a PDF, featuring articles on subpixel rendering, C programming, and other low‑level topics. The zine is praised for its technical depth, humor, and beautiful design, offering a curated resource for systems programmers and hacker enthusiasts. Notable contents include the 'Baby Steps in C' tutorial and the 'Subpixel Zoo' article on page 30, which explores subpixel rendering challenges; the print edition is awaited but not yet listed on Lulu.

hackernews · laurensr · Jul 27, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49070138)

**Background**: A hacker zine is a self‑published, often digital magazine that shares technical knowledge, code, and culture within the hacker and demoscene communities. Subpixel rendering is a display technique that increases the apparent resolution of color screens by addressing individual red, green, and blue subpixels, commonly used to improve text sharpness on LCDs. Paged Out #9 dives into this topic with a playful 'Subpixel Zoo' article, illustrating both the benefits and visual artifacts of the technique.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subpixel_rendering">Subpixel rendering</a></li>

</ul>
</details>

**Discussion**: Commenters praised the zine's humor, especially the 'Baby Steps in C' article, and its beautiful design, likening it to a modern 2600 or a Phrack with raster art. Several noted the technical depth of pieces like the Subpixel Zoo and expressed eagerness to purchase future print editions. One user asked when the printed version would be available, as it was not yet listed on Lulu.

**Tags**: `#systems programming`, `#low-level`, `#graphics`, `#hacker culture`, `#zine`

---

<a id="item-6"></a>
## [Judge Rejects Google's DMCA Claim Against Search Result Scraper](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

A U.S. district judge dismissed Google's DMCA lawsuit seeking to stop a third‑party service from scraping its search results, ruling that the results lack sufficient originality for copyright protection. The decision sets a precedent limiting copyright protection for search engine output, clarifying that scraping publicly available SERPs is not a DMCA violation and affecting how platforms can control access to their data. The ruling, issued on July 27, 2026, found that Google's search results are primarily factual compilations lacking the creative selection or arrangement required for copyright, thus invalidating the DMCA takedown claim against the scraper SearchGuard.

hackernews · cdrnsf · Jul 27, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49073513)

**Background**: The Digital Millennium Copyright Act (DMCA) allows copyright holders to issue takedown notices for allegedly infringing content, but it only applies to material protected by copyright. In the United States, copyright protection for compilations such as search results requires a minimum level of original creativity in the selection or arrangement of facts, which courts often find lacking. By contrast, the EU’s Copyright Directive includes a sui generis database right that can protect substantial investment in data collection regardless of creativity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/">Judge Rejects Google's Attempt To DMCA Its Way Out Of Being Scraped - Techdirt.</a></li>
<li><a href="https://www.quinnemanuel.com/the-firm/publications/the-legal-landscape-of-web-scraping/">The Legal Landscape of Web Scraping - Quinn Emanuel</a></li>
<li><a href="https://www.imperva.com/blog/is-web-scraping-illegal/">Is Web Scraping Illegal? | Imperva</a></li>

</ul>
</details>

**Discussion**: Commenters criticized Google for removing its public API and then suing scrapers, noting the irony that Google’s own success relied on crawling the open web. Some highlighted the legal divergence between the US, which requires creativity for copyright, and the EU, which protects databases based on investment. Others emphasized that scrapeable search results help combat advertising scams and that affordable alternatives are needed to deter scraping.

**Tags**: `#web scraping`, `#DMCA`, `#copyright law`, `#Google`, `#legal precedent`

---

<a id="item-7"></a>
## [Moonshot AI releases 2.8‑trillion‑parameter Kimi K3 model with new license](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 8.0/10

Moonshot AI released the 2.8 trillion‑parameter Kimi K3 model weights on Hugging Face, totaling approximately 1.56 TB, and introduced a modified license that requires attribution for large commercial users or a separate agreement for Model‑as‑a‑Service businesses. This release sets a new record for the largest open‑weight AI model, underscoring the rapid scaling of model size and prompting discussion about how licensing can keep pace with such massive models. The model contains 2.8 trillion parameters, occupies ~1.56 TB of storage, and its license mandates attribution for entities with >100 million monthly active users or >$20 million monthly revenue, while any Model‑as‑a‑Service business exceeding $20 million in annual revenue must negotiate a separate agreement with Moonshot AI.

rss · Simon Willison · Jul 27, 23:39

**Background**: Open‑weight models release the trained parameters publicly, allowing anyone to run or fine‑tune the model, unlike fully open‑source code which also includes training scripts. The traditional MIT License is a permissive license that imposes minimal restrictions, but Moonshot AI created a modified version for its K2 model that added an attribution clause for large commercial users. For Kimi K3, Moonshot replaced the “modified MIT” label with a new license that adds a separate‑agreement requirement for Model‑as‑a‑Service businesses exceeding certain revenue thresholds.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3">China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits | Tom's Hardware</a></li>
<li><a href="https://amplifilabs.com/post/kimi-k3-the-complete-guide-to-moonshot-ais-2-8t-model">Kimi K3: The Complete Guide to Moonshot AI's 2.8T Model - Amplifi Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/MIT_License">MIT License - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoonshotAI`, `#Kimi-K3`, `#HuggingFace`, `#AI-models`

---

<a id="item-8"></a>
## [Settlement Modernisation Index reveals S‑curve in inside money elasticity.](https://arxiv.org/abs/2607.22459) ⭐️ 8.0/10

The paper constructs the Settlement Modernisation Index (SMI) using a panel of 809 reform events across 24 advanced economies from 1993 to 2024. It documents an S‑curve in inside money elasticity with turning points at SMI = 0.27 and 0.93, and shows network‑conditional balance‑sheet efficiencies via a T2S event study and a synthetic‑control analysis of Switzerland’s post‑2021 SDX deployment. The framework provides policy‑relevant forecasts for DLT‑based settlement upgrades, predicting efficiency gains from the ECB’s Pontes initiative and from UK/US accession to the Appia composability layer. These insights help regulators and financial institutions assess the potential balance‑sheet benefits of adopting distributed ledger technology in wholesale payments. The SMI is decomposed into three economic channels and three adoption phases, yielding a saturation beta of +0.557 (p < 0.01) in the T2S‑EMIR event‑study. Based on this, the paper forecasts a +13.4 % efficiency recovery from Pontes over 2027‑2032, rising to +37.5 % if the UK and US join the Appia layer by 2028, and notes that atomic‑settlement efficiencies are a property of the bilateral pair, not the node.

rss · arXiv Quantitative Finance · Jul 27, 04:00

**Background**: Distributed ledger technology (DLT) enables atomic settlement, which can create network effects and balance‑sheet efficiencies in wholesale payment systems. Inside money elasticity measures how the amount of money created by private banks responds to changes in economic conditions or policy. Settlement modernisation refers to upgrades such as real‑time gross settlement (RTGS) systems and blockchain‑based platforms that improve the speed, safety, and cost of cross‑border payments. The paper builds a longitudinal Settlement Modernisation Index from historical reform events to capture these changes across advanced economies.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.22459">Settlement Infrastructure, Inside Money Elasticity, and the Network...</a></li>
<li><a href="https://www.retailbankerinternational.com/tag/settlement-modernisation/">settlement modernisation Archives - Retail Banker International</a></li>

</ul>
</details>

**Tags**: `#distributed ledger technology`, `#settlement systems`, `#financial infrastructure`, `#network economics`, `#inside money elasticity`

---

<a id="item-9"></a>
## [Study Detects 1,012 Coordinated Wallet Cohorts on Solana's Pump.fun Marketplace](https://arxiv.org/abs/2607.02795) ⭐️ 8.0/10

The study analyzed 1,578,333 buyer observations from 166,098 Solana pump.fun token launches between June 12 and June 26, 2026, using a two-stage detection pipeline to identify 1,012 persistent wallet cohorts (2–12 wallets each) that consistently act as early buyers. These cohorts show a >130% lift in first‑30‑minute buyer count and SOL inflow compared to matched launches. Revealing coordinated early‑buyer behavior highlights how market manipulation can inflate initial token prices on Solana’s pump.fun, underscoring the need for robust causal‑inference methods beyond naive matching to detect such activity in DeFi ecosystems. The detection pipeline first extracts intra‑launch first‑buyer windows, then builds a co‑occurrence graph across launches and applies union‑find to surface persistent cohorts; the largest cohort comprises nine wallets appearing among the first ten buyers in 42 launches with an average first‑buyer rank of 2.29. An activity‑matched placebo produced a larger estimated lift (+216.3%), indicating that the observed association is driven by selection rather than a causal cohort effect.

rss · arXiv Quantitative Finance · Jul 27, 04:00

**Background**: Pump.fun is a Solana‑based bonding‑curve marketplace where token price rises predictably as SOL is spent, enabling early buyers to acquire tokens at a fraction of the eventual market price. Coordinated buyer cohorts refer to groups of wallets that repeatedly purchase tokens shortly after launch, potentially influencing early price dynamics. The union‑find (disjoint‑set) data structure efficiently groups elements that co‑occur across many sets, making it suitable for detecting persistent wallet groups from large co‑occurrence graphs.

<details><summary>References</summary>
<ul>
<li><a href="https://j.tools/en/blog/pump-fun-bonding-curve-mechanics-explained">Pump . fun Bonding Curve Explained — Price, Graduation, Strategy</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/graph-data-structure-and-algorithms/">Graph Algorithms - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#DeFi`, `#market manipulation`, `#causal inference`, `#Solana`

---