---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 41 items, 16 important content pieces were selected

---

1. [Shopify Shifts from React Native to Native Swift and Kotlin Apps](#item-1) ⭐️ 8.0/10
2. [More questions about whether researchers can trust OpenAI with unpublished math](#item-2) ⭐️ 8.0/10
3. [OpenAI launches Agents API for managed AI agent development](#item-3) ⭐️ 8.0/10
4. [Google signs 22-year deal for 50% of Finland's Loviisa nuclear output](#item-4) ⭐️ 8.0/10
5. [Critical RCE vulnerability discovered in Forgejo versions up to 16.0.3.](#item-5) ⭐️ 8.0/10
6. [Microsoft declares Rust a tier-1 language](#item-6) ⭐️ 8.0/10
7. [Silicon Valley's Growing Role in the Military-Industrial Complex](#item-7) ⭐️ 8.0/10
8. [Trynix.dev runs any Nix package in-browser via QEMU-WASM](#item-8) ⭐️ 8.0/10
9. [Shopify returns to native mobile apps using AI-assisted development.](#item-9) ⭐️ 8.0/10
10. [Reducing Prescription Errors Through Information Intervention: A Field Experiment in Healthcare Operations](#item-10) ⭐️ 8.0/10
11. [Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending](#item-11) ⭐️ 8.0/10
12. [Modeling Gas Fee Competition Between Arbitrageurs on Decentralized Exchanges](#item-12) ⭐️ 8.0/10
13. [AI Coding Tools and Digital Entrepreneurship: The Role of Software Expertise](#item-13) ⭐️ 8.0/10
14. [Reconstructing Large Scale Production Networks](#item-14) ⭐️ 8.0/10
15. [Generative AI Integration Boosts Analyst Reports but Limits Forecast Accuracy](#item-15) ⭐️ 8.0/10
16. [Global universal approximation with Brownian signatures](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Shopify Shifts from React Native to Native Swift and Kotlin Apps](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is migrating its mobile applications from React Native back to fully native codebases using Swift for iOS and Kotlin for Android, detailing the motivations and lessons learned from the move. The decision highlights growing skepticism about cross‑platform frameworks for large‑scale apps and may influence other companies evaluating performance versus development speed trade‑offs. Shopify cited limitations of React Native in handling complex UI interactions and performance, and mentioned building an internal Playwright‑style driver to aid automated testing after the migration.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is a JavaScript‑based framework that allows developers to write a single codebase for both iOS and Android apps. Swift is Apple’s modern programming language for iOS development, while Kotlin is JetBrains’ language officially supported for Android native apps. Companies sometimes adopt React Native to reduce development effort, but may switch to native languages when they need better performance or deeper platform integration.

**Discussion**: Several commenters shared their own experiences migrating from React Native to native Swift/Kotlin, noting that the work often predated LLM assistance. Others expressed validation of Shopify’s decision, especially iOS engineers who have long advocated for native development. A few highlighted the usefulness of Shopify’s custom Playwright‑style driver for faster verification and expressed interest in learning more about it.

**Tags**: `#mobile development`, `#React Native`, `#Swift`, `#Kotlin`, `#Shopify`

---

<a id="item-2"></a>
## [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A Hacker News thread raised concerns that OpenAI might be using unpublished mathematical ideas shared in chats to train its models without proper attribution, sparking debate over research integrity and AI ethics. The discussion highlights risks to academic collaboration if researchers fear their unpublished ideas could be absorbed into AI models without credit, potentially undermining trust in AI-assisted research. OpenAI’s policy lets users opt out of training and automatically deletes Temporary Chat data after 30 days, but commentators note that model parameters may still retain latent traces of such interactions.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Large language models are trained on vast text corpora, and user‑provided chats can be included in that data unless opted out, influencing the model’s latent representations. Attribution of AI‑generated content, especially in mathematics, remains a contentious issue because ideas can be reproduced without clear credit. Recent work warns that unchecked AI‑generated mathematics could erode provenance in scholarly literature.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt">Chat and File Retention Policies in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance">How your data is used to improve model performance | OpenAI Help Center</a></li>
<li><a href="https://arxiv.org/html/2608.02859v1">The crisis of AI-generated mathematics</a></li>

</ul>
</details>

**Discussion**: Commenters compared the situation to an unethical human collaborator who uses ideas without attribution, while others argued that model improvements and independent discoveries could coexist. Some questioned whether rapid progress on open problems is genuine or driven by pressure to monetize AI services.

**Tags**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#machine learning`, `#mathematics`

---

<a id="item-3"></a>
## [OpenAI launches Agents API for managed AI agent development](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI released the Agents API, a managed service that lets developers create and operate AI agents with built‑in tool support, automatic context compaction, multi‑agent orchestration, and persistent state management. The API lowers the barrier to building sophisticated LLM‑based agents by handling infrastructure concerns, enabling faster prototyping and production deployment while reducing vendor lock‑in concerns through optional self‑hosted sandboxes. The Agents API is built around Agent, Environment, Session, and Events/items concepts, runs the Codex harness, supports MCP servers, and offers automatic context compaction and programmatic tool calling.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: An AI agent combines a language model with tools and memory to perform tasks autonomously, often requiring developers to manage tool execution, context windows, and persistent state. The Codex harness is OpenAI’s internal runtime that powers models like Codex, handling code execution and environment interactions. State management as a service refers to persisting an agent’s session data (such as conversation history and tool outputs) across calls, relieving developers from building their own storage solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents SDK | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/State_management">State management - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the API for abstracting away complex harness infrastructure and enabling agents as a service, while some warned about potential vendor lock‑in and advocated for self‑hosted sandboxes as a mitigation. Others highlighted the practical usefulness of running agents in personal setups (e.g., QEMU VMs) and expressed a preference for accessing raw reasoning tokens rather than higher‑level abstractions. Overall, the discussion shows strong interest with debates over abstraction level, lock‑in risks, and alternative deployment options.

**Tags**: `#OpenAI`, `#Agents API`, `#AI development`, `#LLM tools`, `#API`

---

<a id="item-4"></a>
## [Google signs 22-year deal for 50% of Finland's Loviisa nuclear output](https://www.bbc.com/news/articles/c8r6y4me2g6o) ⭐️ 8.0/10

Google has agreed to buy up to 50% of the electricity output from Finland's Loviisa nuclear power plant under a 22-year contract with utility Fortum to supply its data centers. The deal secures a large, low-carbon and reliable power source for Google's expanding AI-driven data centers, highlighting a trend of tech firms locking in clean energy to meet rising compute demands and climate commitments. Loviisa houses two VVER-440 pressurized water reactors, each about 507 MW, giving the plant a total capacity of roughly 1 GW; Google's share would be up to about 500 MW. The 22-year term and Finland's cool climate, low-carbon grid and uncongested transmission network make the site attractive for data-center operators.

hackernews · lukaspetersson · Sep 11, 00:42 · [Discussion](https://news.ycombinator.com/item?id=49652105)

**Background**: Finland generates a significant share of its electricity from nuclear and renewable sources, resulting in one of the lowest carbon intensities in Europe. The Loviisa plant, operated by Fortum, supplies about 10% of the nation's electricity with two Soviet-designed VVER-440 reactors. Data-center operators favor Finland because its cool climate reduces cooling costs and its grid is both low-carbon and relatively uncongested.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Loviisa_Nuclear_Power_Plant">Loviisa Nuclear Power Plant</a></li>
<li><a href="https://www.fortum.com/energy-production/nuclear-power/plants/loviisa">Loviisa Nuclear Power Plant | Fortum</a></li>

</ul>
</details>

**Discussion**: Commenters praised Finland's low-carbon electricity and welcomed Google's move as a responsible way for AI firms to cover their own power costs rather than burden taxpayers. Some noted the plant's total capacity of about 1 GW and speculated that Google did not take the full output because the utility wants a diversified customer base.

**Tags**: `#Google`, `#nuclear energy`, `#data centers`, `#low-carbon electricity`, `#AI infrastructure`

---

<a id="item-5"></a>
## [Critical RCE vulnerability discovered in Forgejo versions up to 16.0.3.](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo versions up to 16.0.3 contain a critical remote code execution vulnerability caused by unsafe template expansion during repository initialization from a template repository. The issue was fixed in Forgejo 16.0.4 released on September 10, 2026. This vulnerability allows attackers to execute arbitrary code on the server hosting Forgejo, potentially compromising source code, build systems, and internal networks. Prompt patching is essential for all self‑hosted Forgejo installations to prevent exploitation. The flaw occurs when Forgejo clones a template repository, deletes its .git directory, then performs variable template expansion on files listed in .forgejo/template; attacker‑controlled content can inject shell commands that are executed during the expansion. The vulnerability is tracked as CVE‑2026-89094 and was mitigated by a pull request that blocks template expansion during git repo initialization.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Background**: Forgejo is a self‑hosted, lightweight Git service forked from Gitea, designed for easy installation and low‑maintenance repository hosting. It includes a template repository feature that lets users create new repositories from predefined templates, automatically copying files and performing variable substitution. During this process, Forgejo removes the template’s .git folder and expands variables in files listed in .forgejo/template, which can be abused if the template contains malicious constructs. This background explains why unsafe template expansion can lead to remote code execution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thehackerwire.com/vulnerability/CVE-2026-89094/">CVE-2026-89094 - Critical Vulnerability - TheHackerWire</a></li>
<li><a href="https://news.ycombinator.com/item?id=49645907">Forgejo <=16.0.3 Critical RCE | Hacker News</a></li>
<li><a href="https://noise.getoto.net/2026/09/10/forgejo-16-0-4-and-15-0-8-address-critical-security-vulnerability/">Forgejo 16.0.4 and 15.0.8 address critical security vulnerability | Noise</a></li>

</ul>
</details>

**Discussion**: Commenters shared the pull request that fixes the issue, noted that Gitea is not affected, and expressed concern about the project’s stance on LLM contributions. Some users highlighted the technical details of the fix, while others warned against shaming vulnerability reporters. Overall, the discussion reflects genuine concern and a desire for transparency.

**Tags**: `#Forgejo`, `#Security`, `#RCE`, `#Git`, `#Self-hosted`

---

<a id="item-6"></a>
## [Microsoft declares Rust a tier-1 language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

Microsoft has officially designated Rust as a tier‑1 language, granting it full support across its development tooling and signaling deeper integration into its software ecosystem. This move underscores Rust’s growing maturity and positions it as a viable alternative to C and C++ for systems programming, influencing industry adoption and developer tooling choices. The announcement coincides with Microsoft’s internal goal to convert one billion lines of code to Rust by 2030 using automated tooling, and notes that Rust is now being integrated with MSVC’s backend instead of LLVM.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Discussion**: Commenters noted Microsoft’s goal to convert one billion lines of code to Rust by 2030 via automated tooling, and praised Rust’s maturity as a serious competitor to C++ and C#. They also observed that RustConf discussions now focus on C++, Python, and JavaScript interop rather than outright rewrites, and highlighted the switch from LLVM to MSVC’s backend as a notable development.

**Tags**: `#Rust`, `#Microsoft`, `#systems programming`, `#language adoption`, `#open source`

---

<a id="item-7"></a>
## [Silicon Valley's Growing Role in the Military-Industrial Complex](https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex) ⭐️ 8.0/10

A recent report from the Costs of War project examines how big tech firms and Silicon Valley are increasingly involved in the military-industrial complex, sparking a Hacker News discussion. Commenters highlighted historical ties, ethical concerns, and examples such as CIA‑backed In‑Q‑Tel’s funding of Keyhole, which became Google Earth. The trend underscores the deepening integration of commercial technology with defense capabilities, raising questions about corporate ethics, worker accountability, and the direction of innovation. It also influences public policy debates on oversight of tech‑defense partnerships. The report notes that Fairchild Semiconductor’s early military contracts laid a foundation for Silicon Valley’s defense ties, and that In‑Q‑Tel provided seed funding to Keyhole in 2003, leading to rapid adoption by U.S. forces in Iraq before Google’s acquisition. Commenters also cited personal actions, such as quitting Microsoft over alleged complicity in war crimes.

hackernews · paimapi · Sep 10, 15:47 · [Discussion](https://news.ycombinator.com/item?id=49645754)

**Background**: The military‑industrial complex describes the close relationship between a nation’s armed forces and the defense industry that supplies them. Historically, Silicon Valley’s growth was shaped by defense contracts, with companies like Fairchild Semiconductor producing integrated circuits for missile systems. In‑Q‑Tel, a venture‑capital arm of the CIA, funds startups whose technologies can be repurposed for intelligence and military use, as illustrated by the Keyhole‑to‑Google Earth trajectory.

**Discussion**: Commenters debated whether Silicon Valley’s defense involvement is inevitable or ethically problematic, with some arguing that refusing military contracts would hinder technological progress, while others advocated worker activism and resignations to protest complicity. Several highlighted historical precedents, noting that firms have long served both civilian and military markets, and expressed concern over the moral implications of building tools used in warfare.

**Tags**: `#defense technology`, `#tech ethics`, `#military-industrial complex`, `#Silicon Valley`, `#public policy`

---

<a id="item-8"></a>
## [Trynix.dev runs any Nix package in-browser via QEMU-WASM](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Trynix.dev offers a WebAssembly-powered x86_64 Linux VM, built from the qemu-wasm project, that can boot any Nix package from the past 13 years and provide an interactive shell directly in the browser. Users can access specific versions via URL parameters, such as python3@3.6.2, and a GitHub action lets them preview pull requests by booting the build in the same VM. By eliminating the need for local installation or remote servers, Trynix.dev enhances reproducibility, education, and developer workflows, allowing instant access to historical software environments and simplifying pull‑request review. This showcases how WebAssembly can bring full system virtualization to the browser, impacting tooling across the Nix ecosystem. The VM is powered by qemu-wasm’s TCG backend, which translates guest code to WebAssembly and uses browser APIs to execute it, supporting networking and file system mounts. Any Nix package can be specified via the ?pkg= query parameter, and the trynix-preview GitHub action posts a link to a live VM for a pull request’s build.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a purely functional package manager that treats packages as immutable values, enabling reproducible builds and rollbacks across systems. QEMU-WASM is an experimental port of the QEMU emulator to WebAssembly, allowing unmodified guest operating systems (such as Linux) to run inside a browser via the TCG JIT and browser‑provided execution environment.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#QEMU`, `#developer tools`, `#reproducibility`

---

<a id="item-9"></a>
## [Shopify returns to native mobile apps using AI-assisted development.](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify announced on September 10, 2026 that it is moving its mobile apps from React Native back to separate Swift (iOS) and Kotlin (Android) codebases. The shift is made feasible by AI coding agents that handle much of the implementation, translation, testing, and review work, reducing the cost of maintaining dual native platforms. This decision highlights how AI‑assisted development is changing the economics of native mobile development, potentially encouraging other companies to prioritize performance over cross‑platform convenience. It also signals a maturing of AI coding agents that can now reliably assist with platform‑specific code generation and translation. Shopify maintains three widely used React Native libraries—react-native-skia, flash-list, and restyle—with the first two being transferred to new maintainers and restyle slated for archival at the end of 2026. The company notes that AI agents assist in writing, translating, testing, and reviewing Swift and Kotlin code, making the dual‑platform effort acceptable.

rss · Simon Willison · Sep 10, 21:11

**Background**: React Native enables developers to write a single JavaScript‑based codebase that runs on both iOS and Android, reducing the need to build features twice. Traditional native development requires separate Swift and Kotlin codebases, which increases implementation and maintenance costs. Recent AI coding agents such as GitHub Copilot, Claude Code, and AI‑powered Swift‑to‑Kotlin translators can automate large portions of code generation, translation, testing, and review, lowering the cost barrier for dual‑native approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://www.codeconvert.ai/swift-to-kotlin-converter">Free Swift to Kotlin Converter - AI Code Translation | CodeConvert AI</a></li>

</ul>
</details>

**Tags**: `#mobile development`, `#React Native`, `#native apps`, `#AI-assisted coding`, `#Shopify`

---

<a id="item-10"></a>
## [Reducing Prescription Errors Through Information Intervention: A Field Experiment in Healthcare Operations](https://arxiv.org/abs/2609.09673) ⭐️ 8.0/10

A randomized field experiment using India's largest electronic medical record platform analyzed 2.81 million prescriptions from 1,700 physicians; treatment physicians received real-time, non-mandatory drug-drug interaction information and saw an 8.6% reduction in prescribing errors, translating to about US$4.8 million in annual hospitalization cost savings and roughly 134 lives potentially saved. The study demonstrates that a low‑burden, non‑mandatory information intervention can improve patient safety without triggering alert fatigue, offering a scalable way to cut costly drug‑interaction errors and associated morbidity. Using a difference‑in‑differences design, the authors identified two mechanisms: reactive correction (removing errors after they are flagged) and proactive learning (avoiding errors before alerts appear), with learning effects growing over time and generalizing beyond specific drug pairs, while physician productivity and care quality remained unchanged.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: Drug‑drug interaction (DDI) errors occur when two or more drugs affect each other's activity, posing serious risks such as adverse events or hospitalization. Traditional clinical decision‑support systems often generate mandatory alerts that disrupt workflow and lead to high override rates, a phenomenon known as alert fatigue. A non‑mandatory information intervention provides clinicians with relevant safety data without requiring an immediate response, aiming to reduce errors while preserving workflow. The difference‑in‑differences method compares changes over time between a treatment group receiving the intervention and a control group that does not, isolating the causal impact of the intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/drug-drug-interaction">sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical...</a></li>
<li><a href="https://www.verahealth.ai/">Vera Health - Evidence-Based Clinical Answers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#healthcare`, `#patient safety`, `#decision support`, `#field experiment`, `#prescription errors`

---

<a id="item-11"></a>
## [Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending](https://arxiv.org/abs/2609.09945) ⭐️ 8.0/10

The paper evaluates adversarial training and robustness of logistic regression, feed‑forward neural networks, and tabular transformers against four attacks (FGSM, PGD, Salt‑and‑Pepper, DeepFool) and a mixed‑attack regime on a large Lending Club subset for P2P lending credit scoring. It fills a gap in adversarial‑robustness research that has mostly focused on image and text domains, providing a systematic benchmark for tabular credit‑scoring models that is directly relevant to ML security and fintech applications. Adversarial training markedly improves robustness against the attack it is trained on and transfers well within the gradient‑based family (FGSM ↔ PGD) but shows weak transfer to non‑gradient corruptions (Salt‑and‑Pepper, DeepFool); mixed‑attack training yields the most balanced robustness while preserving clean‑test performance, as measured by stratified cross‑validation.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: Adversarial machine learning studies how small, intentional perturbations to input data can cause model mispredictions, with techniques like FGSM and PGD generating gradient‑based examples and Salt‑and‑Pepper or DeepFool representing non‑gradient corruptions. In peer‑to‑peer (P2P) lending, credit‑scoring models predict loan default risk from applicant‑reported tabular features such as income, employment, and credit history, making them vulnerable to strategic manipulation of those features. Tabular data lacks the natural spatial or sequential structure of images or text, so adapting models like logistic regression, feed‑forward networks, and tabular transformers requires special preprocessing of categorical and numerical fields.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/beginner/fgsm_tutorial.html">Adversarial Example Generation — PyTorch Tutorials 2.14.0 ...</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/️white-box-adversarial-attacks-and-how-to-stop-them-eb19a003463b">White-Box Adversarial Attacks and How to Stop Them | Medium</a></li>
<li><a href="https://github.com/XavierSpycy/tabtransformers">GitHub - XavierSpycy/tabtransformers: A PyTorch-based ...</a></li>

</ul>
</details>

**Tags**: `#adversarial machine learning`, `#credit scoring`, `#tabular data`, `#robustness evaluation`, `#P2P lending`

---

<a id="item-12"></a>
## [Modeling Gas Fee Competition Between Arbitrageurs on Decentralized Exchanges](https://arxiv.org/abs/2507.08302) ⭐️ 8.0/10

The paper introduces the first equilibrium model of gas fee competition between two arbitrageurs on DEXs under three transaction reversion regimes—no-revert, auto-revert, and selectable-revert—and derives unique mixed-strategy equilibria. It then validates the model using Binance and Uniswap V2 data, showing that gas fees and trading volumes rise with price discrepancies and liquidity. By modeling arbitrageur competition, the work fills a gap in DeFi market microstructure research and offers insights for protocol designers seeking to optimize fee structures and transaction ordering. The results also help liquidity providers and traders understand how inventory risk and reversion settings affect profitability and efficiency. The analysis shows no pure symmetric equilibrium exists, but a unique mixed-strategy equilibrium can be characterized for each reversion regime. Empirically, gas fees and traded amounts increase with price discrepancies and liquidity, while under low inventory risk the no-revert setting benefits arbitrageurs most, and under high inventory risk both no-revert and selectable-revert dominate auto-revert in profit and efficiency.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: Decentralized exchanges (DEXs) use automated market makers (AMMs) to enable trading, creating price discrepancies with centralized exchanges (CEXs) that arbitrageurs can exploit. Executing arbitrage on a blockchain requires paying gas fees, and transaction ordering can be affected by reversion rules: transactions may never revert (no-revert), automatically revert on failure (auto-revert), or allow users to select whether to revert (selectable-revert). In game-theoretic terms, arbitrageurs compete by choosing gas fees, leading to a mixed-strategy Nash equilibrium when pure strategies fail to stabilize. Understanding these dynamics is essential for assessing DeFi market efficiency and designing robust AMM protocols.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.08302">Arbitrage on Decentralized Exchanges</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5347630">Arbitrage on Decentralized Exchanges by Xue Dong He... :: SSRN</a></li>
<li><a href="https://medium.com/authereum/getting-ethereum-transaction-revert-reasons-the-easy-way-24203a4d1844">Getting Ethereum Transaction Revert Reasons the Easy Way | Medium</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#Arbitrage`, `#Automated Market Makers`, `#Game Theory`, `#Blockchain`

---

<a id="item-13"></a>
## [AI Coding Tools and Digital Entrepreneurship: The Role of Software Expertise](https://arxiv.org/abs/2511.06545) ⭐️ 8.0/10

The study finds that exposure to AI coding tools raises first-time venture launches after 2022Q4, but lowers one-year survival; founders with software work experience drive more launches, mitigate the survival loss when automation is partial, and explain the increase in venture financing. It provides novel empirical evidence on how AI coding tools affect venture creation and survival, highlighting the moderating role of founders' software expertise, which helps policymakers and entrepreneurs understand the limits and benefits of AI‑driven automation. Using pre‑LLM product descriptions to measure product‑category AI coding exposure and linking it to venture launch, traffic, and financing data, the authors show increased launches, lower survival but higher conditional financing, and that software‑experienced founders account for a larger share of new ventures, ameliorate survival decline under partial automation, and explain all financing gains.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: AI coding tools such as GitHub Copilot, Claude Code, and Cursor use large language models to automate code generation, lowering the technical barrier to software creation. Digital entrepreneurship leverages these tools to enable non‑technical founders to launch ventures. Software work experience refers to prior employment in software development, which provides founders with deeper technical knowledge and problem‑solving skills that can complement or substitute for AI‑generated code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.podcosmos.com/ycombinator/startup-school/how-to-get-the-most-out-of-vibe-coding-startup-school">Key Insights: How To Get The Most Out Of Vibe Coding | PodCosmos</a></li>
<li><a href="https://arxiv.org/html/2511.06545v3">AI Coding Tools and Digital Entrepreneurship: The Role of Software...</a></li>

</ul>
</details>

**Tags**: `#AI coding tools`, `#digital entrepreneurship`, `#software expertise`, `#venture survival`, `#startup financing`

---

<a id="item-14"></a>
## [Reconstructing Large Scale Production Networks](https://arxiv.org/abs/2512.02362) ⭐️ 8.0/10

The authors present an algorithm that combines a sector‑aware gravity model to draw a binary buyer‑seller backbone and a minimum‑energy program to assign weights, reconstructing national‑scale firm‑to‑firm production networks from public sectoral input‑output tables and firm‑size distributions. For the United States the method yields about 6.5 million firms and 340 million links in roughly four hours on a single workstation, and similar networks are built for Japan, the UK, Australia, Finland and Denmark. Reconstructed weighted firm‑to‑firm networks enable realistic macroeconomic simulations and systemic‑risk assessments, showing that neither firm size, degree nor sectoral position reliably predicts the aggregate losses from a firm’s failure. This underscores the need for detailed network data in economic policy and risk management. The algorithm first constructs a binary backbone using a sector‑aware gravity model, then solves a minimum‑energy weighting program that keeps one‑step firm balances and sectoral flows close to the observed data while enforcing a Markov closure to guarantee a primitive network with a unique stationary distribution. Experiments show the reconstructed Japanese network reproduces the observed heavy‑tailed degree distribution, and the resulting customer tails are heavier than supplier tails despite symmetric treatment of buyers and sellers.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: Sectoral input‑output tables record the monetary flows of goods and services between industries, showing how each sector’s output serves as input to others and are commonly used to study inter‑industrial dependencies. A gravity model in network reconstruction predicts the likelihood of a link between two entities based on their sizes (or masses) and distance, often adapted here to sector‑specific firm size distributions to generate a plausible binary backbone. Minimum‑energy weighting assigns link weights by minimizing an energy function subject to constraints that preserve observed aggregates, yielding a network that stays close to the data while satisfying theoretical properties such as closure and stationarity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bea.gov/data/industries/input-output-accounts-data">Input-Output Accounts | U.S. Bureau of Economic Analysis (BEA)</a></li>
<li><a href="https://www.researchgate.net/figure/Heatmaps-of-migrants-normalized-by-the-gravity-model-The-following-heatmaps-depict-the_fig3_337451749">Fig 5. Heatmaps of migrants normalized by the gravity model . The...</a></li>
<li><a href="https://arxiv.org/html/2512.02362v1">Reconstructing Large Scale Production Networks</a></li>

</ul>
</details>

**Tags**: `#network reconstruction`, `#input-output tables`, `#firm-to-firm networks`, `#economic modeling`, `#algorithm`

---

<a id="item-15"></a>
## [Generative AI Integration Boosts Analyst Reports but Limits Forecast Accuracy](https://arxiv.org/abs/2512.19705) ⭐️ 8.0/10

The 2023 integration of generative AI into FACTSET led to analyst reports containing 26% more distinct information sources, 24% broader topical coverage, and 21% more analytical methods, with improved timeliness. Yet, despite richer information, analysts' forecast accuracy declined under higher information‑processing demands, while a machine‑learning benchmark using the same inputs showed no similar drop. The findings reveal that while generative AI eases information‑acquisition constraints, human attention becomes the new bottleneck in knowledge work, highlighting the need to design AI tools that complement rather than overload analysts. These insights have broad implications for AI‑augmented professions, suggesting that gains in data richness do not automatically translate into better decisions without addressing cognitive limits. The study uses the exogenous rollout of FACTSET’s GenAI as a natural experiment, employs placebo tests with other data vendors to rule out platform‑wide trends, and compares human analyst performance to an ML benchmark that processes the same observable inputs. Report richness metrics rose significantly (sources +26%, topics +24%, methods +21%), but relative forecast accuracy fell when analysts faced greater information‑processing load, whereas the ML benchmark’s accuracy remained stable.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: Generative artificial intelligence (GenAI) refers to AI systems that can create text, data, or models based on learned patterns, and has been increasingly embedded in financial data platforms. FACTSET is a major provider of financial data, analytics, and workflow tools used by analysts to produce investment research. Prior to 2023, analysts faced constraints in gathering and synthesizing information; the integration of GenAI into FACTSET was intended to alleviate those constraints by automating data retrieval and enrichment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geminibrief.com/factset-research-systems-inc-fds-the-open-platform-architect-of-the-financial-intelligence-era/">FactSet Research Systems Inc. (FDS): The Open Platform Architect of...</a></li>
<li><a href="https://integrations.sh/factset.com/">factset .com — integrations</a></li>
<li><a href="https://www.youtube.com/watch?v=1lknhrlWe0U">FactSet Generative AI - YouTube</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#financial analysis`, `#human-AI interaction`, `#information processing`, `#empirical study`

---

<a id="item-16"></a>
## [Global universal approximation with Brownian signatures](https://arxiv.org/abs/2512.16396) ⭐️ 8.0/10

The authors prove that linear functionals on the signatures of time‑extended rough paths are dense in L^p, thus providing a universal approximation theorem for any p‑integrable adapted stochastic process, including solutions of stochastic differential equations. This result connects rough path theory, signature methods, and machine learning approximation theory, offering a new tool for learning from sequential data and for analyzing Gaussian processes such as fractional Brownian motion. The theorem holds for weighted rough path spaces and applies to Gaussian processes; in particular, linear functionals on the signature of time‑extended Brownian motion can approximate any p‑integrable stochastic process adapted to the Brownian filtration.

rss · arXiv Quantitative Finance · Sep 10, 04:00

**Background**: A rough path is a controlled enhancement of a path that allows the definition of integrals against irregular signals; its signature is a collection of iterated integrals that encodes the path’s shape. The classical universal approximation theorem states that neural networks can densely approximate continuous functions on compact sets. Extending this idea, the paper shows that linear combinations of signature elements form a dense set in L^p spaces of path‑dependent functionals, thereby generalizing approximation theory to rough and Gaussian path spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2512.16396">Global universal approximation with Brownian signatures</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/brownian-signature-variables">Brownian Signature Variables Overview</a></li>

</ul>
</details>

**Tags**: `#signature methods`, `#rough paths`, `#universal approximation`, `#stochastic processes`, `#fractional Brownian motion`

---