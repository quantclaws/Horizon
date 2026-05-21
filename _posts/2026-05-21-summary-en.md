---
layout: default
title: "Horizon Summary: 2026-05-21 (EN)"
date: 2026-05-21
lang: en
---

> From 44 items, 15 important content pieces were selected

---

1. [:OpenAI model disproves central discrete geometry conjecture](#item-1) ⭐️ 9.0/10
2. [: SpaceX S‑1 Reveals $1.25B/Month AI Compute Deal with Anthropic](#item-2) ⭐️ 9.0/10
3. [: GitHub confirms breach of 3,800 repos via malicious VSCode extension](#item-3) ⭐️ 8.0/10
4. [Colorado Amended SB051 to Exclude Open Source Projects from Age Verification Bill](#item-4) ⭐️ 8.0/10
5. [: Qwen3.7-Max introduces a new agent‑oriented LLM with SOTA non‑hallucination claims.](#item-5) ⭐️ 8.0/10
6. [: Mozilla drops asm.js support in SpiderMonkey, favoring WebAssembly](#item-6) ⭐️ 8.0/10
7. [Railway GCP Account Suspended on May 19, 2026 Causing Service Outage](#item-7) ⭐️ 8.0/10
8. [: Google Shifts Focus to AI Answers, Threatening Open Web Traffic](#item-8) ⭐️ 8.0/10
9. [: Meta blocks human rights accounts in Saudi Arabia, UAE](#item-9) ⭐️ 8.0/10
10. [: Amortizing Perpetual Options: A New On-Chain DeFi Risk Primitive](#item-10) ⭐️ 8.0/10
11. [:Valuing Winners: When and How to Correct for Selection Bias in Randomized Experiments](#item-11) ⭐️ 8.0/10
12. [: Study Quantifies MEV Builder Influence and Sandwich Attack Frequency on Ethereum](#item-12) ⭐️ 8.0/10
13. [:AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration](#item-13) ⭐️ 8.0/10
14. [: RobustiPy: New Python Library for Multiverse Analysis and Model Uncertainty.](#item-14) ⭐️ 8.0/10
15. [: Quantitative Universal Approximation Theorem for Noisy Quantum Neural Networks](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [:OpenAI model disproves central discrete geometry conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) ⭐️ 9.0/10

An internal OpenAI language model generated a counterexample that disproves the 80‑year‑old unit distance conjecture in discrete geometry, a problem originally posed by Paul Erdős. This result marks a milestone in AI‑driven mathematics, showing that large language models can contribute novel insights to long‑standing theoretical problems and may accelerate future research in discrete geometry and beyond. The model’s counterexample was formulated and verified in the Lean proof assistant, drawing on sophisticated ideas from algebraic number theory to construct a finite point set with unit distances that violates the conjecture.

hackernews · tedsanders · May 20, 19:05 · [Discussion](https://news.ycombinator.com/item?id=48212493)

**Background**: Discrete geometry studies combinatorial properties of geometric objects such as points, lines, and distances in finite settings. The unit distance problem asks for the maximum number of times the same distance can occur among n points in the plane; Erdős conjectured that this number grows roughly n^{1+c/log log n} for some constant c, a statement that remained open for decades. Recent AI work has begun to assist mathematicians by generating proofs or counterexamples, shifting the focus from solely proof‑automation to also discovering falsifying instances.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry | OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2603.19514">[2603.19514] Learning to Disprove: Formal Counterexample Generation ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the novelty of using an LLM to find a counterexample, noting that the proof draws on unexpected algebraic number‑theory ideas and is formalized in Lean. Some remarked that while a counterexample is easier to obtain than a proof of the conjecture, the work still demonstrates the model’s capacity to cross‑disciplinary reasoning and could help overcome increasing specialization in science. Others highlighted the broader implication that AI‑driven counterexample generation may soon become a routine tool in mathematical discovery.

**Tags**: `#AI`, `#mathematics`, `#discrete geometry`, `#OpenAI`, `#theorem proving`

---

<a id="item-2"></a>
## [: SpaceX S‑1 Reveals $1.25B/Month AI Compute Deal with Anthropic](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 9.0/10

SpaceX’s S‑1 filing shows it has entered into Cloud Services Agreements with Anthropic to provide $1.25 billion per month of AI compute capacity via its COLOSSUS and COLOSSUS II systems, with the contract running through May 2029. The agreement marks SpaceX’s bold push into the AI cloud sector, potentially altering the competitive dynamics for large‑scale AI training and delivering a huge, steady revenue stream that could bolster its lofty valuation. Capacity will ramp up in May and June 2026 at a reduced fee, the deal can be terminated with 90 days’ notice, and the same COLOSSUS infrastructure is also used to train SpaceX’s own Grok 5 model on COLOSSUS II.

rss · Simon Willison · May 20, 22:26

**Background**: SpaceX, best known for its launch services and Starlink satellite constellation, has been developing the COLOSSUS supercomputer to power its internal AI projects such as the Grok series of language models. COLOSSUS, located in Memphis, Tennessee, began construction in 2024 and became operational in mid‑2024, scaling to hundreds of thousands of GPUs and aiming for a million‑GPU footprint. Anthropic PBC is an AI research and public‑benefit corporation known for its Claude language models, and the S‑1 filing is a Securities and Exchange Commission document that companies submit when preparing for an initial public offering.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://x.ai/news/anthropic-compute-partnership">New Compute Partnership with Anthropic | xAI</a></li>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about SpaceX’s financial health, noting its relatively low revenue compared to its high valuation and questioning the profitability of such a massive AI compute deal. Several doubted the feasibility of placing data centers in space, arguing that cooling and engineering challenges would outweigh any potential advantages. Others pointed out that Starlink generates strong cash flow, which could fund AI bets, while some were surprised that SpaceX’s revenue trails many smaller firms despite its lofty market perception.

**Tags**: `#SpaceX`, `#Anthropic`, `#AI compute`, `#Cloud services`, `#SEC filing`

---

<a id="item-3"></a>
## [: GitHub confirms breach of 3,800 repos via malicious VSCode extension](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) ⭐️ 8.0/10

GitHub confirmed that a malicious Visual Studio Code extension compromised an employee device in May 2026, leading to the exfiltration of approximately 3,800 internal repositories. The threat group TeamPCP claimed responsibility and attempted to sell the stolen data for over $50,000. The breach underscores the growing risk of supply‑chain attacks targeting developer workstations, showing that trusted tools like VS Code extensions can become vectors for large‑scale data theft. It affects confidence in the VS Code Marketplace and highlights the need for stronger extension verification and monitoring. The malicious extension leveraged VS Code’s auto‑update feature to spread like a worm, bypassing signature verification when disabled or using a compromised GitHub PAT to publish the tainted package. TeamPCP claimed to have stolen the data and offered it for sale on underground markets.

hackernews · Timofeibu · May 20, 13:43 · [Discussion](https://news.ycombinator.com/item?id=48207660)

**Background**: VS Code extensions are packaged and signed; the marketplace verifies signatures upon installation to ensure integrity and authenticity. However, extensions can auto‑update without user interaction, allowing attackers to push malicious code silently if signing checks are bypassed. Developer workstations have become a prime target in software supply chains because they often have broad access to internal code and credentials.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/github-breached-vs-code-extension">GitHub Breached via VS Code Extension | Developer Supply Chain Attack 2026</a></li>
<li><a href="https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html">Self-Spreading 'GlassWorm' Infects VS Code Extensions in Widespread ...</a></li>
<li><a href="https://code.visualstudio.com/docs/configure/extensions/extension-marketplace">Extension Marketplace</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that extension security has long been a weak point, with some noting the surprise that attackers could maintain a long enough uptime window to exfiltrate data. Others speculated about a specific compromised extension (nx‑console) and called for the companies behind VS Code, npm, and GitHub to collaborate on a solution.

**Tags**: `#security`, `#VSCode`, `#GitHub`, `#supply-chain`, `#extension vulnerability`

---

<a id="item-4"></a>
## [Colorado Amended SB051 to Exclude Open Source Projects from Age Verification Bill](https://legiscan.com/CO/bill/SB051/2026) ⭐️ 8.0/10

Colorado's SB051 age verification bill was amended to exclude open source projects from its coverage, adding an exemption for software that comes from a free, publicly available code repository. The amendment specifies that a “covered application” does not include applications from such repositories. The exemption signals legislative recognition that open‑source software should not bear the compliance burden of age‑verification mandates, potentially influencing similar bills in other states. It affects developers, open‑source projects, and OS providers who must still verify ages for covered applications. The bill defines a “covered application” as consumer software accessed through a covered application store, and excludes (i) apps that do not process users’ personal data and (ii) apps from a free, publicly available code repository. OS providers such as Apple, Google, and Microsoft remain responsible for age‑verification obligations.

hackernews · ki4jgt · May 20, 20:28 · [Discussion](https://news.ycombinator.com/item?id=48213651)

**Background**: Colorado lawmakers have been pushing for age‑verification requirements at the operating‑system level, targeting companies like Apple, Google and Microsoft to verify users’ ages before allowing access to certain content. Similar proposals have appeared in other states, often justified as child‑safety measures but criticized for privacy and security implications. Open‑source developers have warned that such mandates could impose unreasonable compliance burdens on projects that do not collect personal data. The amendment adds an explicit exemption for software sourced from free, publicly available code repositories, addressing those concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://yro.slashdot.org/story/26/04/25/2124221/colorado-adds-open-source-exemption-to-age-verification-bill">Colorado Adds Open-Source Exemption to Age-Verification Bill - Slashdot</a></li>
<li><a href="https://www.theregister.com/2026/04/22/linux_us_state_age_verificaiton_laws/">Linux may get exemption from Colorado age-check bill • The Register</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pHaWRESkVCSHN0Rkx3eml2RjhDZ0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - California law requires age verification in operating...</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the open‑source exemption as a sign that the bill’s sponsors recognize it is not about safety, while others criticized the legislation as an overreaching “think of the children” move and warned of a slippery slope. Some joked that the exemption could lead to a wave of porn‑related open‑source applications in Colorado.

**Tags**: `#legislation`, `#open source`, `#age verification`, `#policy`, `#Colorado`

---

<a id="item-5"></a>
## [: Qwen3.7-Max introduces a new agent‑oriented LLM with SOTA non‑hallucination claims.](https://qwen.ai/blog?id=qwen3.7) ⭐️ 8.0/10

The model's strong non-hallucination rates and agentic capabilities could reduce reliance on proprietary APIs for complex reasoning tasks, offering a competitive open-weight alternative for developers and enterprises. Qwen3.7-Max employs an orthogonal decoupling architecture and a 1M-token context window, enabling explicit chain-of-thought reasoning. It has secured top rankings in multiple domestic evaluations and is positioned as a well‑priced model in its class.

hackernews · kevinsimper · May 20, 10:35 · [Discussion](https://news.ycombinator.com/item?id=48205626)

**Background**: Agent-oriented language models are designed to perform multi-step tasks such as planning, tool use, and code generation beyond simple question answering. Reducing hallucinations—where models generate false or unsupported information—remains a core challenge in LLMs, with recent research suggesting fundamental limits to eliminating them entirely. Open‑source Qwen models can be deployed locally via tools like Ollama, vLLM, or Open WebUI, and accessed through APIs such as DashScope or OpenAI‑compatible wrappers.

<details><summary>References</summary>
<ul>
<li><a href="https://news.aibase.com/news/28161">Tongyi Lab Launches Qwen 3 . 7 - Max with Orthogonal Decoupling...</a></li>
<li><a href="https://arxiv.org/abs/2401.11817">[2401.11817] Hallucination is Inevitable: An Innate Limitation of Large Language Models</a></li>
<li><a href="https://huggingface.co/blog/daya-shankar/open-source-llms">Best Open - Source LLM Models in 2026: Coding, Local, Agentic AI...</a></li>

</ul>
</details>

**Discussion**: Commenters praised Qwen3.7-Max’s claimed state‑of‑the‑art non‑hallucination rate, noting it exceeds Opus 4.7, Gemini 3.1 Pro and GPT‑5.5, while also appreciating the model as a free, capable alternative to proprietary coding assistants. Some users urged clearer comparisons with the latest competitor releases, requested US‑domiciled hosting via hyperscaler partnerships, and inquired about practical hosted options such as OpenRouter for low‑latency access.

**Tags**: `#Qwen`, `#LLM`, `#AI agents`, `#non-hallucination`, `#open-source models`

---

<a id="item-6"></a>
## [: Mozilla drops asm.js support in SpiderMonkey, favoring WebAssembly](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html) ⭐️ 8.0/10

Mozilla's SpiderMonkey blog announced the removal of asm.js support, marking its official deprecation after being superseded by WebAssembly. The deprecation highlights asm.js's historical role in enabling near‑native web performance and its influence on the development of WebAssembly, affecting developers who relied on it for porting C/C++ code to the web. SpiderMonkey will drop asm.js‑specific optimizations in a future Firefox release, so existing asm.js code will continue to run but without the performance boost. This change aligns with the broader industry shift to WebAssembly as the preferred compilation target for high‑performance web applications.

hackernews · eqrion · May 20, 12:01 · [Discussion](https://news.ycombinator.com/item?id=48206340)

**Background**: asm.js is a strict subset of JavaScript designed to allow near‑native performance for code compiled from C/C++, first optimized in Firefox starting with version 22. It was created as Mozilla’s answer to technologies like NaCl and PNaCl, and later superseded by WebAssembly. SpiderMonkey is Mozilla’s JavaScript and WebAssembly engine that powers Firefox and is also used in projects such as MongoDB and Adobe Acrobat, featuring multiple JIT generations including WarpMonkey.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpiderMonkey_(Javascript_engine)">SpiderMonkey (Javascript engine)</a></li>

</ul>
</details>

**Discussion**: Commenters recalled asm.js’s pivotal role in early web performance demos such as Figma and Unreal Engine, expressing nostalgia but acknowledging that the shift to WebAssembly brought tangible improvements like faster load times. Several noted the technology’s historical importance while accepting its deprecation as sensible progress.

**Tags**: `#WebAssembly`, `#asm.js`, `#JavaScript`, `#browser technology`, `#deprecation`

---

<a id="item-7"></a>
## [Railway GCP Account Suspended on May 19, 2026 Causing Service Outage](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage) ⭐️ 8.0/10

On May 19, 2026, Railway’s Google Cloud Platform (GCP) account was suspended, causing an outage of its services and prompting the company to publish a detailed post‑mortem. The incident sparked a large community discussion on Hacker News about Google Cloud’s reliability and customer impact. The suspension highlights the risks of relying on a single cloud provider and raises concerns about arbitrary account actions that can affect downstream customers. It has fueled debate among engineers about multi‑cloud strategies and the need for greater transparency from cloud vendors. Railway stated it is planning to remove GCP services from its data plane’s hot path, retaining them only for secondary/failover use, while the post‑mortem did not disclose the exact reason for the suspension. Google Cloud suspensions can result from ToS violations, missed payments, or suspected fraud, and this is not the first such incident reported for Railway.

hackernews · 0xedb · May 20, 08:37 · [Discussion](https://news.ycombinator.com/item?id=48204770)

**Background**: Railway is an all‑in‑one cloud platform that lets developers deploy applications without managing networking or infrastructure, positioning itself as a competitor to traditional PaaS offerings. A Google Cloud account suspension occurs when Google disables a billing account or project due to policy violations, unpaid bills, or suspected fraud, cutting off access to all associated GCP resources until the issue is resolved.

<details><summary>References</summary>
<ul>
<li><a href="https://railway.com/">Railway | The all-in-one intelligent cloud provider</a></li>
<li><a href="https://cloud.google.com/channel/docs/concepts/google-cloud/suspension">Google Cloud suspensions overview | Channel Services | Google Cloud Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration over what they perceive as arbitrary and frequent GCP account suspensions, questioning Google Cloud’s trustworthiness as a B2B provider. Several noted that Railway should have anticipated the risk and is now planning to reduce its dependence on GCP, while others praised the company’s candid post‑mortem and accepted responsibility for the outage.

**Tags**: `#GCP`, `#cloud outage`, `#incident report`, `#Railway`, `#cloud reliability`

---

<a id="item-8"></a>
## [: Google Shifts Focus to AI Answers, Threatening Open Web Traffic](https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/) ⭐️ 8.0/10

The article argues that Google is increasingly prioritizing AI-generated answers over traditional search links, reducing referral traffic to websites. This shift threatens the revenue model of publishers and creators who rely on Google traffic, raising broader concerns about AI's impact on the open web ecosystem. Google's Search Generative Experience (SGE) and AI Overviews now answer queries directly, with studies showing up to 75% of queries satisfied without clicks, and publishers reporting 40‑60% drops in search‑referred traffic.

hackernews · cdrnsf · May 20, 21:33 · [Discussion](https://news.ycombinator.com/item?id=48214449)

**Background**: Google's Search Generative Experience (SGE), introduced at Google I/O 2023, uses generative AI to provide direct answers in search results, reducing the need for users to click through to source websites. Historically, websites allowed Google to crawl their content in exchange for referral traffic, creating a symbiotic relationship that benefited both publishers and the search engine. At the same time, AI companies scrape publicly available web content to train large language models, raising legal and ethical questions about data use and compensation.

<details><summary>References</summary>
<ul>
<li><a href="https://seo.ai/blog/search-generative-experience-impact-seo">How Search Generative Experience Will Impact SEO: 5 Insights</a></li>
<li><a href="https://www.toprankmarketing.com/blog/ai-search-trends-google-sge-organic-traffic/">Age of SGE: How Will AI Affect Search Traffic in the Next Decade?</a></li>
<li><a href="https://searchengineland.com/ai-answers-disrupting-publisher-revenue-advertising-465185">How AI answers are disrupting publisher revenue and advertising</a></li>

</ul>
</details>

**Discussion**: Commenters expressed worry that AI systems are appropriating creative work without compensation, forcing creators to consider paywalls or abandon publishing altogether. Some noted the symbiotic nature of Google's crawling and warned that cutting off traffic removes the incentive for sites to allow indexing, while others lamented the loss of independent traffic sources like StumbleUpon and criticized AI summaries for being often inaccurate.

**Tags**: `#Google`, `#web`, `#AI`, `#content scraping`, `#internet policy`

---

<a id="item-9"></a>
## [: Meta blocks human rights accounts in Saudi Arabia, UAE](https://www.alqst.org/ar/posts/1190) ⭐️ 8.0/10

Meta has restricted the Facebook and Instagram accounts of independent NGOs, researchers, and civil society figures so they cannot be seen by users in Saudi Arabia and the United Arab Emirates, according to rights groups. This follows government requests and adds to a pattern of tech platforms complying with repressive regimes. The move raises concerns about corporate complicity in censorship and threatens freedom of expression for activists in the Gulf, highlighting the power of social media platforms to shape public discourse under authoritarian pressure. It also fuels debate over the responsibility of tech companies to resist government demands that violate human rights. The restriction applies to both Facebook and Instagram, preventing the accounts from appearing in users’ feeds or search results in the two countries, and was disclosed by a coalition of rights groups that condemned Meta’s decision. No public statement from Meta has been released, and the action is believed to be executed via geo‑blocking tools that limit content by location.

hackernews · giuliomagnifico · May 20, 12:43 · [Discussion](https://news.ycombinator.com/item?id=48206768)

**Background**: Meta (formerly Facebook) operates the world’s largest social networks and routinely uses geo‑blocking to comply with local laws, a practice that can be employed to silence dissent when governments request it. Content moderation policies on platforms like Facebook and Instagram involve both automated systems and human reviewers, and governments often exploit these tools to suppress critical speech. Shadow banning—making content hard to discover without an outright ban—is another tactic that platforms may use, either voluntarily or under pressure, to limit the reach of certain accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alqst.org/ar/posts/1190">Meta blocks human rights accounts from reaching audiences in Saudi Arabia and the UAE</a></li>
<li><a href="https://jsis.washington.edu/news/german-content-moderation-and-platform-liability-policies/">German Content Moderation and Platform Liability Policies</a></li>
<li><a href="https://www.business-humanrights.org/it/ultime-notizie/alleged-shadow-banning-of-palestinian-supporters-on-instagram-tiktok/">Alleged 'shadow banning' of Palestinian supporters on ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the Alqst site itself is blocked in the UAE, requiring a VPN to access the article, and criticized Meta for prioritizing profit over principles. Some argued that refusing to comply could lead to worse local alternatives, while others called Meta the worst platform and expressed personal disengagement from its services.

**Tags**: `#social media`, `#content moderation`, `#human rights`, `#tech ethics`, `#Middle East`

---

<a id="item-10"></a>
## [: Amortizing Perpetual Options: A New On-Chain DeFi Risk Primitive](https://arxiv.org/abs/2605.19146) ⭐️ 8.0/10

The paper introduces a design for amortizing perpetual options (AmPOs) tailored to blockchain constraints, presenting a decentralized market framework with minimal consistency requirements. This contract serves as a foundational risk primitive for DeFi, enabling endogenous collateralization and explicitly priced de‑peg insurance. By providing a trustless, oracle‑light derivative, AmPOs allow protocols to mutualize tail risk without relying on centralized clearing, potentially expanding the range of on‑chain financial products. This could improve DeFi stability and open new use cases such as protocol‑level insurance and collateralization. AmPOs are fungible, continuous‑installment options that amortize premium payments over time, eliminating the need for high‑frequency price feeds or aggressive liquidation mechanisms. The design operates under adversarial blockchain assumptions and maintains correctness with only minimal consistency guarantees.

rss · arXiv Quantitative Finance · May 20, 04:00

**Background**: Perpetual options are derivatives that give the holder the right, but not the obligation, to buy or sell an asset at a predetermined price without an expiry date. On‑chain implementations have struggled because they usually require frequent oracle updates and robust liquidation engines to manage risk, which can fail during market stress. Amortizing perpetual options address these challenges by spreading premium costs over time and reducing reliance on real‑time data, making them more suitable for the decentralized, adversarial environment of blockchains.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.19146">Designing On - Chain Options : Amortizing Perpetual Options</a></li>
<li><a href="https://arxiv.org/abs/2512.06505">[2512.06505] Amortizing Perpetual Options - arXiv</a></li>
<li><a href="https://panoptic.xyz/docs/trading/perpetual-options">Perpetual options - Panoptic</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#on-chain options`, `#blockchain finance`, `#risk primitives`, `#perpetual options`

---

<a id="item-11"></a>
## [:Valuing Winners: When and How to Correct for Selection Bias in Randomized Experiments](https://arxiv.org/abs/2605.18887) ⭐️ 8.0/10

The paper distinguishes global and selective winner's curse biases in randomized experiments, links them to regret, and shows that bias corrections must match the decision‑maker's evaluation target. It also introduces an adaptive empirical likelihood procedure that yields asymptotically valid confidence intervals across settings. Understanding which bias correction to use depends on the specific goal of an experiment, helping practitioners avoid overestimating treatment effects in A/B testing and causal inference. The framework guides method selection, improving decision quality when deploying the best‑performing treatment. The authors define seven decision‑relevant evaluation targets (mean bias, MSE, CI coverage for global and selective winner's curse, plus mean regret) and show that no single method dominates: plug‑in estimators excel with large treatment differences, cross‑fitting works best when treatments are similar, and resampling methods achieve low MSE for moderate differences. Their adaptive empirical likelihood procedure provides tuning‑free, asymptotically valid CIs.

rss · arXiv Quantitative Finance · May 20, 04:00

**Background**: In randomized experiments, selecting the treatment with the highest observed outcome can induce a winner's curse: the chosen treatment's estimated effect is upwardly biased because random noise inflates its apparent performance. This bias leads to regret when the selected treatment is not truly the best. Correcting for this selection bias is crucial for reliable inference in fields such as online A/B testing and medical trials.

<details><summary>References</summary>
<ul>
<li><a href="https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1006916">Statistical correction of the Winner ’ s Curse explains... | PLOS Genetics</a></li>
<li><a href="https://www.kdd.org/kdd2018/accepted-papers/view/winners-curse-bias-estimation-for-total-effects-of-features-in-online-contr">KDD 2018 | Winner ’ s Curse : Bias Estimation for Total Effects of...</a></li>
<li><a href="https://www.investopedia.com/terms/w/winnerscurse.asp">investopedia.com/terms/w/winnerscurse.asp</a></li>

</ul>
</details>

**Tags**: `#A/B testing`, `#selection bias`, `#winner's curse`, `#causal inference`, `#experimental design`

---

<a id="item-12"></a>
## [: Study Quantifies MEV Builder Influence and Sandwich Attack Frequency on Ethereum](https://arxiv.org/abs/2508.04003) ⭐️ 8.0/10

The paper finds that two MEV builders produce nearly 80% of Ethereum blocks and would collectively spend about $14 million per month to remain in the top quartile of block builders. It also reports that sandwich attacks occur more than once per block on average, with gas fees from these attacks accounting for roughly 15% of the MEV paid to validators. The results highlight the growing concentration of block-building power among a few entities, revealing significant economic incentives that could undermine transaction fairness and increase extraction costs for DeFi users. Understanding these dynamics is crucial for designing mitigations such as gas fee priority mechanisms or private transaction pools to reduce harmful MEV. The study estimates that the two dominant builders would need to spend nearly $14 million per month collectively to stay in the top quartile, and that sandwich attacks average more than one per block, with their Gas fees representing about 15% of the MEV paid to validators. It also notes that reforms like Gas fee priority or private transaction pools could help mitigate these effects.

rss · arXiv Quantitative Finance · May 20, 04:00

**Background**: MEV (Miner Extractable Value) refers to the extra value block producers can gain by reordering, including, or excluding transactions beyond the standard block reward and gas fees. On Ethereum, block builders (under proposer‑builder separation) assemble transactions into blocks and can extract MEV through strategies such as arbitrage, liquidations, and sandwich attacks. A sandwich attack occurs when an attacker fronts‑runs and then backs‑runs a user’s transaction, profiting from the price movement caused by the victim’s trade. Private transaction pools (or private RPCs) send transactions directly to builders, hiding them from public mempools and reducing exposure to searchers who seek MEV opportunities.

<details><summary>References</summary>
<ul>
<li><a href="https://ethereum.org/developers/docs/mev/">Maximal extractable value ( MEV ) | ethereum.org</a></li>
<li><a href="https://www.coingecko.com/learn/sandwich-attacks-prevention-crypto">What Are Sandwich Attacks in Crypto and How to... | CoinGecko</a></li>
<li><a href="https://dev.to/moonsoon69/how-to-build-a-mev-protected-swap-service-in-typescript-3lo1">How to Build a MEV -Protected Swap Service in... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#Ethereum`, `#MEV`, `#blockchain`, `#transaction ordering`, `#sandwich attacks`

---

<a id="item-13"></a>
## [:AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration](https://arxiv.org/abs/2509.25055) ⭐️ 8.0/10

The paper introduces AlphaSAGE, a framework that combines a structure-aware Relational Graph Convolutional Network encoder with Generative Flow Networks (GFlowNets) and a dense multi-faceted reward to mine diverse, non-correlated predictive alphas. It is presented in arXiv:2509.25055v3 and accompanied by open-source code at https://github.com/BerkinChen/AlphaSAGE. AlphaSAGE tackles three core limitations of existing RL‑based alpha mining—reward sparsity, inadequate sequential expression representations, and lack of diversity—by providing a principled, exploration‑friendly method that can yield a richer portfolio of trading signals. This advancement could improve the robustness and performance of quantitative trading strategies. The framework employs a Relational Graph Convolutional Network (RGCN) to encode the syntactic and semantic structure of mathematical expressions, uses GFlowNets to sample expressions proportionally to a learned reward, and incorporates a dense reward design that provides feedback at intermediate steps. Code and experiments are publicly available on GitHub.

rss · arXiv Quantitative Finance · May 20, 04:00

**Background**: Automated alpha mining seeks to discover predictive formulas from financial data, a task often framed as reinforcement learning where an agent builds expressions step‑by‑step. Traditional RL approaches suffer from sparse rewards (only complete formulas yield feedback), use simple sequential representations that ignore expression structure, and optimize for a single high‑reward mode, limiting diversity. Generative Flow Networks (GFlowNets) address these issues by training a policy to sample objects with probability proportional to a reward, enabling efficient exploration of structured, multimodal spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/aiguys/gflownets-the-next-big-idea-in-ai-d2ad78e3a88f">GFlowNets , Generative Flow Networks | AIGuys</a></li>
<li><a href="https://arxiv.org/html/2509.25055v1">AlphaSAGE: Structure - Aware Alpha Mining via GFlowNets for...</a></li>
<li><a href="https://www.emergentmind.com/topics/generative-flow-networks-gflownets">Generative Flow Networks ( GFlowNets )</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#alpha mining`, `#GFlowNets`, `#reinforcement learning`, `#structured representation`

---

<a id="item-14"></a>
## [: RobustiPy: New Python Library for Multiverse Analysis and Model Uncertainty.](https://arxiv.org/abs/2506.19958) ⭐️ 8.0/10

RobustiPy is an open‑source Python package that integrates bootstrap inference, combinatorial specification search, model selection/averaging, and explainable AI to perform large‑scale multiverse analysis and model‑uncertainty quantification. By providing a unified, computationally efficient framework for robustness checks, RobustiPy helps researchers assess the sensitivity of their results to analytical choices, improving reproducibility across economics, sociology, psychology, and medicine. The library was benchmarked on approximately 672 million simulated regressions, demonstrating state‑of‑the‑art speed while supporting out‑of‑sample validation and covariate contribution quantification.

rss · arXiv Quantitative Finance · May 20, 04:00

**Background**: Multiverse analysis examines how different defensible modeling choices affect results for a single hypothesis, addressing researcher degrees of freedom and the replication crisis. Model‑uncertainty quantification quantifies the uncertainty arising from selecting among competing statistical models, often using Bayesian or information‑criteria approaches. Bootstrap inference resamples data with replacement to estimate sampling distributions and construct confidence intervals without relying on parametric assumptions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multiverse_analysis">Multiverse analysis</a></li>
<li><a href="https://www.researchgate.net/publication/361558260_How_is_model-related_uncertainty_quantified_and_reported_in_different_disciplines">(PDF) How is model -related uncertainty quantified and reported in...</a></li>
<li><a href="https://medium.com/data-science/bootstrap-and-statistical-inference-in-python-a06d098a8bfd">Bootstrap and Statistical Inference in Python | by Leihua Ye... | Medium</a></li>

</ul>
</details>

**Tags**: `#Python`, `#multiverse analysis`, `#model uncertainty`, `#explainable AI`, `#bootstrap`

---

<a id="item-15"></a>
## [: Quantitative Universal Approximation Theorem for Noisy Quantum Neural Networks](https://arxiv.org/abs/2604.02064) ⭐️ 8.0/10

The paper presents a quantitative universal approximation theorem for noisy quantum neural networks, providing explicit non‑asymptotic error bounds that depend on circuit depth, width, and noise strength. It further validates the theorem with numerical experiments on actual noisy quantum hardware, focusing on finance‑relevant expectation estimation. By delivering rigorous error guarantees for QNNs under realistic noise, the work bridges the gap between theoretical approximation theory and near‑term quantum device experiments. This enables trustworthy application of quantum machine learning in quantitative finance and other domains where precise error control is essential. The theorem states that for any target function expressible as an expectation, a QNN with sufficient layers and neurons can approximate it within an error ε that scales polynomially with the inverse of the noise level and inversely with network size. Experiments were conducted on IBM’s superconducting qubit processors, demonstrating convergence of the estimated expectation values to classical Monte‑Carlo baselines under realistic depolarizing noise.

rss · arXiv Quantitative Finance · May 20, 04:00

**Background**: Universal approximation theorems guarantee that a family of neural networks can densely approximate any continuous function, forming the theoretical foundation of classical deep learning. Extending this concept to quantum neural networks requires accounting for inevitable hardware noise, which can disrupt the unitary evolution and degrade expressivity. In the context of quantitative finance, where target functions often appear as expectations of stochastic processes, having explicit error bounds for noisy QNNs is crucial for guaranteeing reliable predictions on near‑term devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem - Wikipedia</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/40202891/">Universal Approximation Theorem and Error Bounds for Quantum ...</a></li>
<li><a href="https://arxiv.org/html/2604.02064v3">Quantitative Universal Approximation for Noisy Quantum Neural Networks</a></li>

</ul>
</details>

**Tags**: `#quantum machine learning`, `#universal approximation`, `#noisy quantum neural networks`, `#quantum finance`, `#hardware experiments`

---