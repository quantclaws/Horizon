---
layout: default
title: "Horizon Summary: 2026-06-10 (EN)"
date: 2026-06-10
lang: en
---

> From 71 items, 20 important content pieces were selected

---

1. [Initial Impressions of Claude Fable 5 Reveal Powerful but Slow, Expensive Model](#item-1) ⭐️ 9.0/10
2. [Sleep reminder nudge backfires, boosting late-night usage via algorithmic adaptation.](#item-2) ⭐️ 9.0/10
3. [Universal Approximation Theorem Extended to Differentiable Maps on Infinite-Dimensional Weighted Manifolds](#item-3) ⭐️ 9.0/10
4. [Apple releases open-source macOS Container Machines for OCI containers.](#item-4) ⭐️ 8.0/10
5. [npm v12 to disable allowScripts by default and fix decade‑old vulnerability](#item-5) ⭐️ 8.0/10
6. [German court rules Google liable for AI Overviews false answers.](#item-6) ⭐️ 8.0/10
7. [Concerns Rise Over Silent AI Model Degradation for Competitors](#item-7) ⭐️ 8.0/10
8. [Making Graphics Like it's 1993](#item-8) ⭐️ 8.0/10
9. [Paper Introduces Five‑Component Taxonomy for Real‑World Asset Tokenization](#item-9) ⭐️ 8.0/10
10. [Planning resilient hydrogen supply chains under disruption risk](#item-10) ⭐️ 8.0/10
11. [Paper reviews execution assumptions and reproducibility in LLM‑based trading systems.](#item-11) ⭐️ 8.0/10
12. [TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing for Optimal Trade Execution](#item-12) ⭐️ 8.0/10
13. [Bayesian VAR & Elliptical Black-Litterman for Portfolio Optimization](#item-13) ⭐️ 8.0/10
14. [Transferring high-cost capacity to efficient leader lowers prices despite higher concentration](#item-14) ⭐️ 8.0/10
15. [AI adoption boosts demand for human skills like analytical thinking.](#item-15) ⭐️ 8.0/10
16. [The Value of Personalized Recommendations: Evidence from Netflix](#item-16) ⭐️ 8.0/10
17. [Differential ML method prices 0DTE options with stochastic volatility and jumps.](#item-17) ⭐️ 8.0/10
18. [Unified Framework Shows Avellaneda-Stoikov and Cartea-Jaimungal Models Are Not Independent.](#item-18) ⭐️ 8.0/10
19. [Tech-Risk Dual-Factor Model Quantifies AI Occupational Substitution Beyond Capability.](#item-19) ⭐️ 8.0/10
20. [Polymarket-v1 Database Released with Ground-Truth Aggressor Direction](#item-20) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Initial Impressions of Claude Fable 5 Reveal Powerful but Slow, Expensive Model](https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything) ⭐️ 9.0/10

Simon Willison spent about 5.5 hours testing Anthropic’s newly released Claude Fable 5, describing it as a powerful model that is slow and expensive with aggressive safety guardrails. He notes it matches the performance of Claude Mythos 5 but adds strict classifiers that often trigger refusals and offer an automatic fallback option. The release highlights the trade‑off between cutting‑edge capability and safety in frontier LLMs, showing how stricter guardrails can affect usability and cost. It also signals pricing trends for massive‑context models that may influence developers’ choices for long‑horizon agentic tasks. Claude Fable 5 features a 1 million‑token context window, 128 000 maximum output tokens, a knowledge cutoff of January 2026, and is priced at $10 per million input tokens and $50 per million output tokens—roughly twice the cost of Claude Opus 4.5‑4.8. Its safety classifiers trigger frequently, prompting API‑level refusal notifications and an optional automatic fallback to another model.

rss · Simon Willison · Jun 9, 23:59

**Background**: Claude Fable 5 is the latest frontier model from Anthropic, positioned as a Mythos‑class system with the same raw capabilities as Claude Mythos 5 but equipped with additional safety classifiers to mitigate harmful use. Frontier models are the most advanced AI systems available at a given time, trained on massive datasets to deliver state‑of‑the‑art performance across reasoning, language, and agentic tasks. The model’s 1M‑token context enables analysis of very large inputs such as entire codebases or long documents, a capability increasingly sought after for complex workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**Discussion**: Commenters praised Fable 5’s raw power, noting it can tackle very difficult problems that previously stalled them. Some highlighted improvements in frontend design and token efficiency, suggesting the effective cost can be comparable to Opus 4.8 for certain workloads. Others pointed out new interventions that limit the model’s usefulness for frontier LLM development, and noted a temporary free‑access window in subscription plans ending June 23.

**Tags**: `#Claude`, `#Anthropic`, `#LLM`, `#AI models`, `#frontier models`

---

<a id="item-2"></a>
## [Sleep reminder nudge backfires, boosting late-night usage via algorithmic adaptation.](https://arxiv.org/abs/2606.08265) ⭐️ 9.0/10

In a large-scale field experiment on a short-video platform, a 'sleep reminder' nudge intended to reduce late-night viewing instead increased late-night engagement by 14.75% and overall platform usage by 2.18%, with the effects persisting for weeks after the campaign ended. The study shows that user-facing interventions can retrain recommendation algorithms, producing durable system-wide shifts that undermine standard evaluation metrics and highlight the need for dynamic, feedback-aware platform governance. The increase stemmed from a forced-exploration mechanism: the sleep reminder exposed high latent demand for the promoted content, prompting the algorithm to update its recommendation policy in a way that reinforced the very engagement loops the nudge sought to mitigate.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Recommender systems continuously learn from user interactions, creating feedback loops where the algorithm’s outputs shape future inputs. Interventions such as nudges are usually evaluated as static changes, ignoring that the resulting behavior can trigger policy updates via forced exploration, especially on platforms like short-video apps where rapid content turnover amplifies these dynamics. The cited work on degenerate feedback loops and breaking feedback loops illustrates how such cycles can unintentionally amplify engagement, while research on short-video recommendation mechanisms shows how algorithmic updates can quickly reshape content distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@curioushruti/degenerate-feedback-loops-in-recommender-systems-3f47e9f3b9bc">Degenerate Feedback Loops in Recommender Systems | Medium</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3728372">Breaking Feedback Loops in Recommender Systems with Causal ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2772941924001005">The short video platform recommendation mechanism based on the improved neural network algorithm to the mainstream media - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#recommender systems`, `#field experiment`, `#unintended consequences`, `#algorithmic feedback`, `#short-video platform`

---

<a id="item-3"></a>
## [Universal Approximation Theorem Extended to Differentiable Maps on Infinite-Dimensional Weighted Manifolds](https://arxiv.org/abs/2606.09820) ⭐️ 9.0/10

The authors generalize the universal approximation theorem for functional input neural networks to differentiable maps on infinite-dimensional weighted manifolds, proving a weighted Nachbin theorem that also approximates derivatives. They apply the result to non‑anticipative functionals and show that linear signature functions can approximate path‑space functionals and their directional derivatives. This theoretical advance bridges classical approximation theory with modern deep learning, providing a foundation for neural operators that can learn derivatives and complex functionals on infinite‑dimensional data. It is likely to influence research in scientific machine learning, rough path theory, and the design of architectures for processing sequential or functional data. The proof relies on a weighted Nachbin theorem that extends Nachbin’s weighted approximation result to vector‑valued Stone‑Weierstrass settings, allowing a functional input neural network to map from an infinite‑dimensional weighted manifold through a nonlinear activation to a Banach‑space readout. Consequently, horizontal and vertical derivatives of non‑anticipative functionals are approximable, and linear combinations of the signature can approximate path‑space functionals and their directional derivatives.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: The classical universal approximation theorem states that shallow neural networks can uniformly approximate any continuous function on a compact domain. Functional input neural networks (FNNs) extend this idea by taking infinite‑dimensional inputs (e.g., paths or functions) and mapping them through a nonlinear hidden layer to produce outputs in a Banach space. On infinite‑dimensional weighted manifolds, a weighted version of the Nachbin theorem provides the necessary density result to approximate not only the map itself but also its derivatives, while the signature of a path offers a linearized representation that can capture the geometry of path‑space functionals.

<details><summary>References</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s00365-025-09726-3">Global Universal Approximation of Functional Input Maps on Weighted ...</a></li>
<li><a href="https://b-thi.github.io/FNN/index.html">Functional Neural Networks • FuncNN - GitHub Pages</a></li>
<li><a href="https://arxiv.org/html/2412.14723v2">Dimension reduction for path signatures - arXiv</a></li>

</ul>
</details>

**Tags**: `#universal approximation theorem`, `#neural networks`, `#functional analysis`, `#infinite-dimensional manifolds`, `#signature method`

---

<a id="item-4"></a>
## [Apple releases open-source macOS Container Machines for OCI containers.](https://github.com/apple/container/blob/main/docs/container-machine.md) ⭐️ 8.0/10

Apple has open-sourced a container machine system for macOS that runs OCI containers with persistence and filesystem mount support, providing developers a lightweight Linux environment. The tool is written in Swift and optimized for Apple Silicon. This gives macOS developers a fast, low-overhead alternative to Docker Desktop for Linux container workloads, improving startup times and resource usage. It also aligns with Apple’s push to provide native virtualization tools on its platform. Each container runs in its own lightweight virtual machine, with spawn times reported between 200‑400 ms, and the system supports persistent storage and host‑directory mounts. It is fully OCI‑compliant and leverages Apple’s Hypervisor framework.

hackernews · timsneath · Jun 10, 00:29 · [Discussion](https://news.ycombinator.com/item?id=48469658)

**Background**: OCI containers are standardized Linux containers that can run on any OCI‑compliant runtime, ensuring portability across platforms like Docker and Kubernetes. On macOS, traditional containers require a Linux VM layer, which adds overhead. Apple’s container machines aim to reduce that overhead by integrating tightly with the Hypervisor framework and Apple Silicon.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_Container_Initiative">Open Container Initiative - Wikipedia</a></li>
<li><a href="https://github.com/apple/container/blob/main/docs/container-machine.md">container /docs/ container - machine .md at main · apple / container</a></li>
<li><a href="https://nanoclaws.io/blog/apple-container-macos-agent-sandbox">Apple Container on macOS : Why NanoClaw Uses Apple 's New...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the system adds persistence and mount support, making it a useful lightweight Linux environment. Some compared its performance to OrbStack, asked whether containers share a kernel (they run in separate VMs), inquired about using external drives for volumes, and wondered why Apple didn’t adopt a WSL‑1‑style approach.

**Tags**: `#macOS`, `#containers`, `#developer tools`, `#virtualization`, `#OCI`

---

<a id="item-5"></a>
## [npm v12 to disable allowScripts by default and fix decade‑old vulnerability](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/) ⭐️ 8.0/10

npm announced that version 12 will turn off the allowScripts setting by default, preventing install scripts from running unless explicitly allowed. It will also patch a vulnerability that has been known for about ten years. The change improves security by reducing the risk of malicious postinstall scripts, aligning npm with pnpm’s safer defaults. Fixing the long‑standing vulnerability removes a persistent attack vector that has affected the Node.js ecosystem for years. In current npm releases the allowScripts field is advisory, but in v12 it will be enforced off by default unless packages are whitelisted via the approve‑scripts command. The patched vulnerability corresponds to VU#319816, disclosed roughly a decade ago, which allowed hijacked packages to exfiltrate API keys through obfuscated install scripts.

hackernews · plasma · Jun 9, 21:01 · [Discussion](https://news.ycombinator.com/item?id=48467705)

**Background**: npm is the default package manager for JavaScript and Node.js projects, allowing packages to define install scripts (such as preinstall, install, postinstall) that run automatically during dependency installation. The allowScripts field in package.json records which dependencies are permitted to execute these scripts; currently it is advisory, meaning scripts still run by default but a warning is shown. About ten years ago, vulnerability VU#319816 was disclosed, showing that malicious packages could abuse install scripts to steal secrets, prompting long‑term security concerns that the upcoming change addresses.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/commands/npm-approve-scripts/">npm-approve-scripts | npm Docs</a></li>
<li><a href="https://www.nodejs-security.com/blog/npm-ignore-scripts-best-practices-as-security-mitigation-for-malicious-packages">NPM Ignore Scripts Best Practices as Security Mitigation for Malicious Packages</a></li>

</ul>
</details>

**Discussion**: Commenters noted that disabling allowScripts by default follows pnpm’s lead after roughly 18 months, and some suggested using per‑package whitelists or linters to enforce safe defaults. Others pointed out the long‑known nature of the fixed vulnerability, referencing the ten‑year‑old bug report, and remarked on npm’s ownership by GitHub. Overall, the discussion welcomed the security improvement while asking for tooling to manage script allowances.

**Tags**: `#npm`, `#package-manager`, `#breaking-changes`, `#security`, `#JavaScript`

---

<a id="item-6"></a>
## [German court rules Google liable for AI Overviews false answers.](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/) ⭐️ 8.0/10

A German regional court ruled that Google is liable for false information generated by its AI Overviews feature, treating the AI-generated text as Google's own content. The decision stems from a case where the AI incorrectly linked two publishers to scams. The ruling sets a legal precedent in the EU that providers of generative AI can be held liable for inaccuracies, potentially affecting how AI search features are deployed and regulated. It may encourage other jurisdictions to adopt similar liability frameworks for AI-generated content. The court found that Google's AI Overviews incorrectly associated two publishers with fraudulent schemes, and held Google responsible as the publisher of the AI-generated text. The decision does not apply to mere linking of third‑party web pages, only to content created by Google's AI.

hackernews · ahlCVA · Jun 10, 01:44 · [Discussion](https://news.ycombinator.com/item?id=48470248)

**Background**: AI Overviews is a feature of Google Search that uses generative AI to produce concise summaries of search results, introduced as part of the Search Generative Experience (SGE) at Google I/O in May 2023 and rebranded as AI Overviews in May 2024. The feature provides AI‑generated snapshots with links to deeper information and is gradually being rolled out to more languages and regions. Because the summaries are generated by Google's AI, the company argues they are not its own editorial content, but the German court rejected that distinction.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://support.google.com/websearch/answer/14901683?hl=en&co=GENIE.Platform=Desktop">Find information in faster & easier ways with AI Overviews in ...</a></li>
<li><a href="https://www.search.google/ways-to-search/ai-overviews/">Google AI Overviews - Search anything, effortlessly</a></li>

</ul>
</details>

**Discussion**: Commenters generally agreed that Google should be liable for content it generates, contrasting it with mere linking of third‑party results. Some warned that the ruling could lead Google to withdraw AI Overviews from the EU, while others questioned whether users expect truthfulness from a free service.

**Tags**: `#AI liability`, `#Google`, `#legal ruling`, `#AI Overviews`, `#EU regulation`

---

<a id="item-7"></a>
## [Concerns Rise Over Silent AI Model Degradation for Competitors](https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html) ⭐️ 8.0/10

A Hacker News post warns that Anthropic's newly released Claude Fable 5 could covertly reduce helpfulness for users deemed competitors, following its June 9, 2026 launch. Such silent degradation raises alarms about anti‑competitive practices in AI services, erodes trust in model reliability, and could pressure regulators to demand greater transparency from providers. Commenters note that Claude Fable 5 exceeds all prior benchmarks, while its sibling Claude Mythos 5 has safeguards lifted in some areas, and that silent nerfing could be implemented via preference‑vector alignment or shadow‑banning‑style opaque responses.

hackernews · mips_avatar · Jun 9, 21:19 · [Discussion](https://news.ycombinator.com/item?id=48467896)

**Background**: Claude Fable 5 is Anthropic's latest state‑of‑the‑art large language model, released in June 2026, that excels on standard AI benchmarks and can process complex documents, charts, and code. Model providers can adjust the trade‑off between helpfulness and harmlessness using techniques such as preference‑vector alignment, which lets them tune behavior without overtly changing the model’s weights. This capability opens the door to covertly reducing helpfulness for specific users—e.g., perceived competitors—while maintaining apparent safety scores, a practice likened to shadow banning. Critics warn that such silent nerfing could create false‑positive safety triggers and give providers an anti‑competitive edge if not disclosed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html">Anthropic releases Mythos-like AI model to the public, Claude Fable 5</a></li>
<li><a href="https://arxiv.org/html/2504.20106v3">Adaptive Helpfulness–Harmlessness Alignment with Preference Vectors</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights worries that providers could silently nerf models for rivals, that false‑positive safety flags may already be causing hidden degradation, and that the practice resembles long‑standing shadow‑banning tactics, with some urging market competition to push for higher transparency and lower error rates.

**Tags**: `#AI`, `#LLM safety`, `#AI competition`, `#model alignment`, `#Hacker News`

---

<a id="item-8"></a>
## [Making Graphics Like it's 1993](https://staniks.github.io/articles/catlantean-3d-blog-1/) ⭐️ 8.0/10

The article presents a tutorial for building a 1990s‑style raycasting graphics engine inspired by Wolfenstein 3D, complete with code snippets and explanations of VGA memory addressing and lightmap techniques. It offers developers hands‑on knowledge of retro rendering methods that can inform modern software rendering, demoscene projects, and educational projects about graphics history. The tutorial covers raycasting basics, writing pixels to VGA memory at segment 0xA0000, using 8×8 or 16×16 lightmaps for dynamic lighting, and references community contributions such as gibs generation and an SDL2 snippet for palletized framebuffers.

hackernews · sklopec · Jun 9, 10:46 · [Discussion](https://news.ycombinator.com/item?id=48459294)

**Background**: Raycasting renders a 3D scene by casting rays from the viewer's position for each screen column and drawing wall slices based on distance, a technique popularized by Wolfenstein 3D. The VGA graphics mode 320×200 uses a linear framebuffer located at memory segment 0xA0000, allowing direct pixel writes in real‑mode x86 code. Lightmaps are pre‑computed texture layers that modulate surface brightness, enabling effects like flickering torches or baked global illumination without runtime lighting calculations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Video_Graphics_Array">Video Graphics Array - Wikipedia</a></li>
<li><a href="https://lodev.org/cgtutor/raycasting.html">Raycasting - Lode V</a></li>
<li><a href="https://www.reddit.com/r/gamedev/comments/yypkh9/how_do_you_get_that_90s_early_2000s_retro_style/">How do you get that 90s / early 2000s retro style 3d graphics? - Reddit</a></li>

</ul>
</details>

**Discussion**: Commenters praised the tutorial for its nostalgic depth, noting its similarity to Wolfenstein 3D’s raycasting rather than Doom’s BSP engine. Several highlighted personal experiences with 8×8 lightmaps for dynamic torch and rocket lighting, and explained the convenience of VGA memory addressing at 0xA0000 for 16‑bit code. Others shared useful resources such as an SDL2 snippet for transferring palletized framebuffers to modern screens and expressed enjoyment of the gibs technique.

**Tags**: `#graphics programming`, `#raycasting`, `#retro gaming`, `#software rendering`, `#game development`

---

<a id="item-9"></a>
## [Paper Introduces Five‑Component Taxonomy for Real‑World Asset Tokenization](https://arxiv.org/abs/2606.08534) ⭐️ 8.0/10

The paper presents a new taxonomy that organizes 23 dimensions into five components—governance, asset structure, token properties, distributed ledger technology, and economy—to classify and compare real‑world asset (RWA) tokenization systems. By providing a systematic, systems‑level framework, the taxonomy fills a literature gap and enables researchers and practitioners to compare RWA designs across asset classes and implementation models. The taxonomy identifies hybrid architectures as predominant, where blockchain tokens handle representation and transfer while legal guarantees remain off‑chain, and highlights recurring gaps in voting rights, dispute forums, burn mechanics, supply constraints, and reserve verification.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Real‑world asset tokenization creates a digital representation of physical or financial assets on a blockchain, preserving the underlying legal rights through structures such as SPVs, trusts, or funds. Distributed ledger technology records these tokens, enabling transfer, pricing, and composability, but legal custody, compliance, and verification often remain off‑chain. Because these on‑chain and off‑chain elements are described separately, existing systems are difficult to compare without a unified framework.

<details><summary>References</summary>
<ul>
<li><a href="https://www.britannica.com/money/real-world-asset-tokenization">What Is Asset Tokenization? Meaning, Examples, Pros, & Cons ...</a></li>
<li><a href="https://arxiv.org/html/2606.08534v1">A Taxonomy of Real-World Asset Tokenization for Blockchain-Based Financial Infrastructure Omitted for a double blind review.</a></li>
<li><a href="https://www.legalnodes.com/article/rwa-tokenization-in-the-eu-most-suitable-jurisdictions-and-regulatory-frameworks-for-2025-and-beyond">RWA Tokenization in the EU: Most Suitable Jurisdictions and Regulatory Frameworks for 2025 and Beyond</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#real-world asset tokenization`, `#decentralized finance`, `#financial infrastructure`, `#taxonomy`

---

<a id="item-10"></a>
## [Planning resilient hydrogen supply chains under disruption risk](https://arxiv.org/abs/2606.09190) ⭐️ 8.0/10

The study shows that risk-aware planning of EU hydrogen imports can avoid about 12% welfare losses (≈24 billion EUR) by diversifying import corridors and over‑investing in infrastructure, despite higher upfront costs. Incorporating supply disruption risks into hydrogen infrastructure planning helps prevent welfare losses and structural vulnerabilities similar to those seen in fossil‑fuel systems, guiding more secure and cost‑effective energy transitions. Using a stochastic optimization model, naive planning yields 12% welfare loss versus risk‑aware planning; the resilient strategy involves diversifying import corridors and strategic over‑investment, increasing intra‑European transport capacity, expanding import pipelines, and building costly hydrogen‑carrier shipping terminals.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Hydrogen is seen as a key green fuel for decarbonizing industry and transport, but its supply chain faces uncertainties such as production variability, geopolitical disruptions, and transport bottlenecks. Stochastic optimization methods incorporate probabilistic disruptions into planning models to evaluate trade‑offs between cost and resilience. Energy security concerns have grown as countries seek to reduce dependence on volatile fossil‑fuel imports, making risk‑aware infrastructure essential for future hydrogen economies.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.09190">Planning resilient hydrogen supply chains under disruption risk</a></li>
<li><a href="https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/07-schmidt-liquid-organic-hydrogen-carriers.pdf">Liquid Organic Hydrogen Carrier Technologies</a></li>

</ul>
</details>

**Tags**: `#hydrogen supply chain`, `#stochastic optimization`, `#energy security`, `#infrastructure planning`, `#risk management`

---

<a id="item-11"></a>
## [Paper reviews execution assumptions and reproducibility in LLM‑based trading systems.](https://arxiv.org/abs/2606.08285) ⭐️ 8.0/10

The paper presents a topical review and reproducibility audit of 30 LLM‑based trading studies, highlighting inconsistencies in data provenance, temporal splits, execution timing, and transaction‑cost modeling. By exposing execution‑assumption gaps, the work provides a needed foundation for comparable, economically interpretable LLM trading results and guides researchers toward clearer reporting standards. The audit uses a coded evidence matrix to evaluate point‑in‑time controls, split transparency, held‑out evaluation, cost and turnover treatment, execution semantics, universe definition, and artifact release, and includes a 10‑equity worked example to show how friction and timing choices compress strategy returns.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: LLM‑based trading systems propose to use large language models as agents that generate trading signals, but their reported performance depends heavily on how data are split, how trades are executed, and what transaction costs are assumed. Proper temporal split discipline (e.g., purged cross‑validation) and point‑in‑time controls are required to avoid look‑ahead bias and ensure that backtests reflect realistic market conditions. Without standardized reporting of execution semantics, cost models, and evaluation protocols, results across studies cannot be compared or reproduced.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Purged_cross-validation">Purged cross-validation - Wikipedia</a></li>
<li><a href="https://letsdatascience.com/news/llm-based-trading-research-exposes-reproducibility-gaps-e76503bd">LLM-Based Trading Research Exposes Reproducibility Gaps</a></li>
<li><a href="https://github.com/gg-lol-123/ai-trading-strategy-generator">GitHub - gg-lol-123/ai- trading -strategy-generator: AI-powered trading ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#trading systems`, `#reproducibility`, `#financial AI`, `#execution assumptions`

---

<a id="item-12"></a>
## [TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing for Optimal Trade Execution](https://arxiv.org/abs/2606.08379) ⭐️ 8.0/10

The paper introduces TT-DAC-PS, a deterministic actor-critic algorithm that combines twin exponential-moving-average critic targets, pessimistic min backup, TD3-style policy smoothing noise, delayed actor updates, and conservative Q regularization, and applies it to limit order book data for ten U.S. stocks to solve optimal trade execution. TT-DAC-PS consistently lowers the mean implementation shortfall percentage with competitive variance, outperforming classical benchmarks (TWAP, VWAP, AC) and standard RL baselines (PPO, SAC, A2C), thereby offering a more cost‑effective solution for large‑scale stock liquidation. TT-DAC-PS uses twin critic targets with pessimistic min backup, adds TD3‑style policy smoothing noise, delays actor updates, and applies conservative Q‑regularization; exploration employs Ornstein‑Uhlenbeck noise with a hybrid schedule (deterministic decay, variance‑guided adjustment, and a learned SAC‑style temperature), while the environment integrates Almgren‑Chriss market impact, normalized LOB features, per‑step volume caps, and a utility‑based reward.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Optimal trade execution aims to minimize market impact and timing risk when liquidating large positions, often modeled using the Almgren‑Chriss framework that balances temporary and permanent price impact against volatility. Limit order book (LOB) data provides the finest granularity of market depth, capturing bid‑ask prices and volumes at each price level. Deterministic actor‑critic methods, such as TD3, improve stability by learning a deterministic policy while using twin critics to reduce overestimation; policy smoothing and target regularization further enhance robustness in noisy financial environments.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.08379v1">TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing ...</a></li>
<li><a href="https://www.simtrade.fr/blog_simtrade/understanding-almgren-chriss-model-for-optimal-trade-execution/">Understanding the Almgren-Chriss Model for Optimal Trade ...</a></li>
<li><a href="https://www.kaggle.com/datasets/praanj/limit-orderbook-data">Limit Orderbook data | Kaggle</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#optimal execution`, `#finance`, `#actor-critic`, `#limit order book`

---

<a id="item-13"></a>
## [Bayesian VAR & Elliptical Black-Litterman for Portfolio Optimization](https://arxiv.org/abs/2606.09104) ⭐️ 8.0/10

The paper introduces the BAVAR-BLED algorithm, which integrates Bayesian-Averaging Vector Autoregression (BAVAR) and the Black-Litterman model under Elliptical Distributions (BLED) within a TD3 deep reinforcement learning framework. Tested on 29 Dow Jones Industrial Average stocks over ten years, it achieved Sharpe 1.72, Sortino 2.70, and total return 57.26%. By explicitly modeling regime shifts and fat‑tailed returns, the method addresses two key shortcomings of existing DRL‑based portfolio optimizers, potentially delivering more robust performance in real‑world markets. This could influence quantitative finance practice and inspire further hybrid econometric‑RL approaches. BAVAR supplies multi‑scale, regime‑aware return expectations and dispersion matrices that serve as priors for BLED, which uses Student’s t‑distributions to capture heavy tails. View construction employs transformer networks, risk‑aversion estimation uses CNNs, and the whole pipeline is embedded in a TD3 actor‑critic architecture.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Bayesian Vector Autoregression (BVAR) treats VAR coefficients as random variables with priors, allowing richer modeling of temporal dependencies. The Black‑Litterman model combines market equilibrium returns with investor views; extending it to elliptical distributions (e.g., Student’s t) accommodates fat‑tailed asset returns. Twin Delayed DDPG (TD3) improves deep deterministic policy gradient learning by using twin critics and delayed updates to reduce overestimation bias.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_vector_autoregression">Bayesian vector autoregression - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Black–Litterman_model">Black–Litterman model - Wikipedia</a></li>
<li><a href="https://spinningup.openai.com/en/latest/algorithms/td3.html">Twin Delayed DDPG — Spinning Up documentation - OpenAI</a></li>

</ul>
</details>

**Tags**: `#portfolio optimization`, `#Bayesian VAR`, `#Black-Litterman`, `#heavy-tailed returns`, `#deep reinforcement learning`

---

<a id="item-14"></a>
## [Transferring high-cost capacity to efficient leader lowers prices despite higher concentration](https://arxiv.org/abs/2407.03504) ⭐️ 8.0/10

The paper shows that transferring higher-cost capacity from less efficient firms to the most efficient firm can increase market concentration yet reduce electricity prices, contradicting standard antitrust expectations, and validates this with data from Colombia's wholesale electricity market. The finding challenges conventional wisdom that higher concentration always raises prices, offering new insights for antitrust policy, capacity caps, divestitures, and merger reviews in industries with technology portfolios. The model assumes firms compete via supply schedules with multiple technologies, each having constant marginal cost up to a capacity limit; small transfers of high-cost capacity to the efficient leader lower prices, while larger transfers raise them, producing a non‑monotonic price‑concentration relationship.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: In supply schedule competition, firms submit quantity‑price functions and the market clears where supply meets demand; each technology offered by a firm has a constant marginal cost up to its capacity limit. A technology portfolio refers to a firm’s mix of generation assets (e.g., hydropower, thermal) that differ in cost and flexibility, influencing its market power. In Colombia’s wholesale electricity market, weather‑driven variations in hydropower output shift capacity across firms, providing a natural experiment for studying how transfers of higher‑cost capacity affect prices and concentration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scirp.org/journal/paperinformation?paperid=104166">Marginal Cost versus John M. Clark's Workable Competition Pricing</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0140988320300335">Value of technology in the U.S. electric power sector ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hydroelectricity">Hydroelectricity - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#industrial organization`, `#electricity markets`, `#market power`, `#antitrust`, `#oligopoly theory`

---

<a id="item-15"></a>
## [AI adoption boosts demand for human skills like analytical thinking.](https://arxiv.org/abs/2412.19754) ⭐️ 8.0/10

Using nearly 30 million job postings from the US, UK, and Australia between 2018 and 2024, the study finds that AI-intensive roles increasingly require non‑technical skills such as analytical thinking, resilience, and digital literacy, which are linked to wage premiums. The results show that AI acts as a complement to human abilities rather than a substitute, implying that workers who strengthen skills like judgment and collaboration will benefit from higher pay and greater job security. Specifically, analytical thinking, resilience and digital literacy see increased demand and pay, while substitutable tasks such as summarisation, translation and routine customer service decline, especially as AI spreads within firms and industries.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Artificial intelligence is reshaping workplaces by automating certain tasks while creating new demands for human‑centric capabilities. Researchers often debate whether AI will replace workers or enhance their productivity, a distinction known as substitution versus complementarity. Large‑scale job‑posting datasets allow scholars to track evolving skill requirements across countries and industries.

**Tags**: `#AI impact`, `#labor market`, `#skill demand`, `#job postings`, `#human-AI complementarity`

---

<a id="item-16"></a>
## [The Value of Personalized Recommendations: Evidence from Netflix](https://arxiv.org/abs/2511.07280) ⭐️ 8.0/10

The authors estimate that replacing Netflix's recommendation algorithm with a matrix factorization baseline would reduce user engagement by 4%, while a popularity-based baseline would cut engagement by 12%, and both alternatives would lower content diversity. This study provides a causal quantification of the incremental value of personalized recommendations, offering concrete metrics that can guide platform design and investment decisions. Using a discrete choice model that incorporates recommendation-induced utility, low-rank heterogeneity, and flexible state dependence on Netflix viewership data, the authors exploit algorithmic idiosyncrasies to identify these components and compute model-free diversion ratios for validation.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Discrete choice models are econometric tools that predict decisions among a finite set of alternatives by modeling the utility associated with each option. Low-rank heterogeneity captures unobserved user and item factors in a compressed representation, allowing recommendation systems to model complex preference patterns efficiently. Diversion ratios measure the share of users who would switch from one item to another when the first becomes less attractive, serving as a validation metric for counterfactual simulations in recommendation research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Discrete_choice">Discrete choice - Wikipedia</a></li>
<li><a href="https://medium.com/data-science-collective/discrete-choice-models-an-introduction-to-demand-estimation-and-product-and-price-differentiation-099028c91410">Discrete Choice Models : An Introduction to Demand... | Medium</a></li>
<li><a href="https://chrisconlon.github.io/site/diversion.pdf">Empirical Properties of Diversion Ratios</a></li>

</ul>
</details>

**Tags**: `#recommendation systems`, `#Netflix`, `#engagement analysis`, `#counterfactual evaluation`, `#discrete choice model`

---

<a id="item-17"></a>
## [Differential ML method prices 0DTE options with stochastic volatility and jumps.](https://arxiv.org/abs/2603.07600) ⭐️ 8.0/10

The paper introduces a differential machine learning approach for zero‑days‑to‑expiry (0DTE) options under a stochastic‑volatility jump‑diffusion model, expressing the option price in Black‑Scholes form with a maturity‑gated variance correction and combining price/Greek supervision with a PIDE‑residual penalty. A jump‑operator network is trained jointly in a three‑stage procedure, improving jump‑term approximation, hedge stability and computational speed versus Fourier benchmarks. Accurate pricing and hedging of ultra‑short‑maturity options are critical for market makers and risk managers; the method delivers more reliable jump‑term estimates, stable delta hedges and faster evaluation, thereby bridging modern ML techniques with practical quantitative finance needs. A single neural network outputs both option price and all Greeks, while a separate jump‑operator network captures the jump component; training proceeds in three stages (price/Greek supervision, PIDE residual, jump‑operator fitting) using a maturity‑gated variance correction. Experiments show reduced Greek errors, stable one‑day delta hedges and significant speed‑ups over Fourier‑based pricing, with additional tests on a jump rough Heston model.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Zero‑days‑to‑expiry (0DTE) options expire within a single trading day, requiring models that capture rapid price dynamics and jump risks. Stochastic‑volatility jump‑diffusion models (e.g., Heston with jumps) describe asset prices driven by a continuous variance process and discontinuous jumps, leading to a partial integro‑differential equation (PIDE) for option pricing. Differential machine learning combines automatic differentiation with neural networks to enforce model‑based residuals (such as the PIDE) while learning from data, enabling accurate and efficient pricing of complex derivatives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stochastic_volatility_jump_models">Stochastic volatility jump models - Wikipedia</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3591734">Differential Machine Learning by Brian Norsk Huge, Antoine... :: SSRN</a></li>
<li><a href="https://arxiv.org/html/2603.07600v3">Differential Machine Learning for 0DTE Options with ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#options pricing`, `#stochastic volatility`, `#jump diffusion`, `#Greeks`, `#0DTE`

---

<a id="item-18"></a>
## [Unified Framework Shows Avellaneda-Stoikov and Cartea-Jaimungal Models Are Not Independent.](https://arxiv.org/abs/2606.01477) ⭐️ 8.0/10

The authors prove that the Avellaneda-Stoikov and Cartea-Jaimungal inventory market‑making frameworks are not independent; the Cartea‑Jaimungal model emerges as a second‑order Taylor expansion of the Avellaneda‑Stoikov model when the market maker’s preference functional satisfies cash‑additivity, normalization, concavity, strong dynamic consistency and law‑invariance, which forces it to be the entropic certainty‑equivalent functional. This unification reveals that the risk‑aversion parameter γ and the running‑penalty coefficient φ are not free but tied by φ = γσ²/2, offering a consistency check for calibrated parameters and deepening understanding of inventory‑risk pricing. It bridges two widely used models, potentially simplifying theory and guiding more robust model selection in algorithmic trading. Under the stated axioms the preference functional is uniquely the entropic certainty‑equivalent on liquidation‑adjusted terminal wealth, parametrized by a single positive scalar γ; the Avellaneda‑Stoikov framework is the exact representative, while the Cartea‑Jaimungal framework corresponds to its second‑order expansion, yielding φ = γσ²/2 and, under mild regularity, α = ½ L''(0). The relation is invertible, γ = 2φ/σ², providing a cross‑check for independently calibrated desk parameters.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: In inventory market making, a trader balances earning the bid‑ask spread against the risk of holding unwanted inventory, and models such as Avellaneda‑Stoikov and Cartea‑Jaimungal provide optimal quote policies based on different mathematical formulations. The Avellaneda‑Stoikov model treats the risk‑aversion parameter γ as a measure of how penalized inventory is, leading to an exponential utility‑based reservation price, whereas the Cartea‑Jaimungal framework introduces a running‑penalty coefficient φ that penalizes inventory quadratically over time. Both models rely on dynamic preference functionals; imposing cash‑additivity, normalization, concavity, strong dynamic consistency and law‑invariance forces the functional to be the entropic certainty‑equivalent, which underlies the unification proved in the paper.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.01477">[2606.01477] Avellaneda-Stoikov and Cartea-Jaimungal as One ...</a></li>
<li><a href="https://medium.com/@DolphinDB_Inc/taming-inventory-risk-building-a-smarter-crypto-market-maker-with-avellaneda-stoikov-7dcc334b0172">Taming Inventory Risk: Building a Smarter Crypto Market ... | Medium</a></li>
<li><a href="https://hummingbot.org/blog/guide-to-the-avellaneda--stoikov-strategy/">Guide to the Avellaneda & Stoikov Strategy - Hummingbot</a></li>

</ul>
</details>

**Tags**: `#market making`, `#quantitative finance`, `#Avellaneda-Stoikov`, `#Cartea-Jaimungal`, `#stochastic control`

---

<a id="item-19"></a>
## [Tech-Risk Dual-Factor Model Quantifies AI Occupational Substitution Beyond Capability.](https://arxiv.org/abs/2604.04464) ⭐️ 8.0/10

The paper introduces a Tech-Risk Dual-Factor Model that combines technical feasibility with business risk factors to estimate AI-driven occupational substitution. It applies a multi-agent LLM ensemble and Human-in-the-Loop validation with experts to 923 U.S. occupations broken down into 2,087 Detailed Work Activities. By incorporating liability, compliance, and safety risks, the model moves beyond theoretical capability exposure to provide a more realistic estimate of AI’s impact on jobs. This helps policymakers and businesses anticipate which occupations are truly vulnerable and informs strategies for workforce transition. The analysis decomposed 923 occupations into 2,087 Detailed Work Activities, scored each for technical feasibility and business risk via a multi-agent LLM ensemble, and validated the scores with variance-based Human-in-the-Loop expert panels. Results show a high Occupational Automation Index (OAI ≈ 0.70) for data‑intensive cognitive roles, while unstructured physical trades and high‑stakes caretaking jobs exhibit near‑zero OAI, revealing a cognitive risk asymmetry and suggesting a 'compliance premium' that ties wage resilience to risk‑absorption capacity.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Recent advances in Large Language Models (LLMs) have raised concerns about widespread technological unemployment, yet most analyses only assess technical exposure to AI capabilities. Traditional task‑based approaches overlook real‑world barriers such as liability, compliance, and physical safety that slow adoption. The paper introduces a Tech‑Risk Dual‑Factor Model that couples feasibility scores with risk assessments, using Detailed Work Activities (DWAs) from O*NET and Human‑in‑the‑Loop validation to ground predictions in institutional constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.04464">Bounded by Risk, Not Capability: Quantifying AI Occupational ...</a></li>
<li><a href="https://www.onetcenter.org/dl_files/DWA_2014.pdf">A Multi-Phase Rational Method for Developing Area Work Activities</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI impact on labor`, `#occupational substitution`, `#Large Language Models`, `#risk assessment`, `#Human-in-the-Loop validation`

---

<a id="item-20"></a>
## [Polymarket-v1 Database Released with Ground-Truth Aggressor Direction](https://arxiv.org/abs/2606.04217) ⭐️ 8.0/10

The paper introduces the Polymarket-v1 Database, a complete on-chain trade archive of Polymarket's first-generation CTF Exchange on Polygon covering 2022-11-21 to 2026-04-28, with 1.20 billion trade records across 1.30 million markets and $61 billion nominal volume, featuring 100% ground-truth aggressor direction derived from the blockchain settlement layer. Providing verified aggressor direction enables rigorous microstructure analysis and improves the reliability of downstream metrics such as VPIN and OFI, which are critical for transaction cost analysis and prediction market design research. The dataset shows that standard classifiers (tick rule and bulk volume classification) achieve near-random accuracy (49.83% and 50.51%) but hide a systematic price‑level gradient due to positive trade direction autocorrelation and concentrated market‑making; these errors bias VPIN and OFI estimates, while ground‑truth VPIN positively predicts Brier scores and Gibbs spread negatively predicts them, a relationship attenuated when using classified proxies.

rss · arXiv Quantitative Finance · Jun 9, 04:00

**Background**: Polymarket is a leading prediction market that operates on the Polygon blockchain using the Conditional Token Framework (CTF) for all trades, positions, and payouts. Market microstructure research often infers trade aggressor direction (whether a trade was initiated by a buyer or seller) using heuristics such as the tick rule or bulk volume classification, which can be inaccurate. The settlement layer of a blockchain provides definitive, on‑chain records of transaction ordering, allowing ground‑truth aggressor direction to be extracted directly from the ledger.

<details><summary>References</summary>
<ul>
<li><a href="https://cointrenches.io/how-to-find-polymarket-whales-polygonscan-guide/">How to Find Polymarket Whales on Polygonscan: Full... | Cointrenches</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2182819">Bulk Volume Classification versus the Tick Rule and the Lee-Ready ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0378426619300858">Bulk volume classification and information detection - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#blockchain data`, `#market microstructure`, `#dataset`, `#Polymarket`

---