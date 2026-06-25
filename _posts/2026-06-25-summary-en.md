---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 35 items, 8 important content pieces were selected

---

1. [Polars 1.42.0 Release Adds Out-of-Core Spilling, Strict Mode, and SQL Implicit JOIN](#item-1) ⭐️ 8.0/10
2. [OpenAI unveils its first custom AI inference chip.](#item-2) ⭐️ 8.0/10
3. [Anthropic accuses Alibaba of illicitly extracting Claude AI model capabilities via distillation](#item-3) ⭐️ 8.0/10
4. [Qualcomm to Acquire AI Startup Modular for $4 Billion](#item-4) ⭐️ 8.0/10
5. [NVIDIA's 45°C Liquid Cooling Cuts Data Center Water Use Near Zero](#item-5) ⭐️ 8.0/10
6. [Nub: Bun-inspired all-in-one toolkit for Node.js using --require hook](#item-6) ⭐️ 8.0/10
7. [AI Tokenomics: The Economics of Tokens, Computation, and Pricing in Foundation Models](#item-7) ⭐️ 8.0/10
8. [TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Polars 1.42.0 Release Adds Out-of-Core Spilling, Strict Mode, and SQL Implicit JOIN](https://github.com/pola-rs/polars/releases/tag/py-1.42.0) ⭐️ 8.0/10

Polars 1.42.0 introduces performance improvements such as bytes‑based concurrency control for cloud I/O and elimination of empty‑chunk copies, adds experimental out‑of‑core spilling and strict mode, and adds support for SQL’s implicit JOIN syntax while deprecating string‑to‑temporal casts. These updates make Polars more scalable for larger‑than‑memory workloads and cloud‑native environments, while offering a stricter, more predictable API and easier SQL‑style querying, benefiting data engineers and analysts who rely on fast DataFrame operations. The release includes PR #27998 for naive out‑of‑core spilling, PR #28023 for experimental strict mode, PR #27890 for SQL implicit JOIN support, and performance PRs #27924 (bytes‑based concurrency control), #28013 (no flush on phase change), and #27953 (avoid copy on empty chunks).

github · github-actions[bot] · Jun 24, 05:20

**Background**: Polars is a high‑performance DataFrame library written in Rust with Python bindings, built on Apache Arrow and known for fast single‑node analytics. Out‑of‑core spilling allows processing datasets larger than RAM by spilling intermediate data to disk. Strict mode enforces stricter type checking and error handling to catch bugs early, while SQL implicit JOIN enables writing queries with comma‑separated tables in the FROM clause without explicit JOIN keywords.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pola-rs/polars">GitHub - pola-rs/polars: Extremely fast Query Engine for DataFrames...</a></li>
<li><a href="https://pola.rs/">Polars — DataFrames for the new era</a></li>
<li><a href="https://docs.pola.rs/api/python/dev/reference/sql/clauses.html">Query Clauses — Polars documentation</a></li>

</ul>
</details>

**Tags**: `#polars`, `#dataframe`, `#python`, `#performance`, `#release`

---

<a id="item-2"></a>
## [OpenAI unveils its first custom AI inference chip.](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 8.0/10

OpenAI announced its inaugural custom AI inference chip, named Jalapeno, co-designed with Broadcom and fabricated by TSMC, aiming to improve LLM inference efficiency. The chip signals OpenAI's move toward vertical integration in AI hardware, reducing reliance on Nvidia GPUs and potentially lowering inference costs for its services. Jalapeno was developed from design to production in nine months, leveraging OpenAI's own models to accelerate the design process, and is built using TSMC's advanced fabrication node.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference chips are specialized processors optimized for running trained models, offering better performance and energy efficiency than general-purpose GPUs. Broadcom provides ASIC design and packaging expertise, while TSMC is a leading semiconductor foundry that manufactures chips using advanced process nodes. OpenAI's partnership follows a trend where major AI firms develop custom silicon to improve scalability and reduce costs.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.933thedrive.com/2026/06/24/openai-unveils-custom-chip-it-designed-with-broadcom-to-boost-its-ai-infrastructure/">OpenAI unveils custom chip it designed with Broadcom to boost its AI infrastructure | 93.3 The Drive</a></li>
<li><a href="https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/">TSMC AI Fabricating Dominance: Chip Manufacturing Leadership in AI Era - Klover.ai</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism that the nine‑month development timeline might be overstated, likening it to generic marketing claims. Others highlighted the chip’s TSMC fabrication and discussed innovative architectures such as storing weights in ROM or burning models into silicon, referencing startups like Taalas. Some noted that Google’s long‑standing TPU lineage makes OpenAI’s entry seem less novel but still significant.

**Tags**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#Broadcom`, `#TSMC`

---

<a id="item-3"></a>
## [Anthropic accuses Alibaba of illicitly extracting Claude AI model capabilities via distillation](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 8.0/10

Anthropic said on June 24, 2026 that Alibaba illicitly extracted capabilities from its Claude AI model through model distillation and unauthorized access schemes, according to a letter seen by Reuters. The accusation highlights growing tensions over intellectual property in the AI industry, especially regarding model distillation practices that enable cheaper replication of advanced models. It could affect how AI firms protect their models and influence future licensing and legal frameworks. Anthropic described the activity as the largest known distillation attack on its models, involving adversarial distillation where a smaller model is trained on Claude’s outputs to mimic its capabilities at lower cost. The alleged scheme also included reselling Claude tokens at 70‑90% below official API prices and using user logs as training data.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Model distillation is a machine‑learning technique where a smaller “student” model learns to replicate the behavior of a larger “teacher” model, often using the teacher’s outputs as training data. While distillation can reduce computational costs, it raises concerns when performed without the teacher model’s owner permission, as it may constitute unauthorized extraction of proprietary capabilities. Anthropic’s Claude series are large language models accessed via API, and their outputs are considered valuable intellectual property.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API | OpenAI</a></li>
<li><a href="https://cybersecuritynews.com/anthropic-accuses-alibaba/">Anthropic Accuses Alibaba of 'Illicitly' Accessing Its Claude AI Models in Largest Known Distillation Attack</a></li>

</ul>
</details>

**Discussion**: Commenters noted the irony of Anthropic complaining about data use while its own models were trained on vast amounts of publicly available text, and some compared the situation to historic GUI copying disputes. Others explained the two main types of distillation—black‑box and targeted—and pointed out that reselling Claude tokens at steep discounts and harvesting user logs enable below‑cost operation.

**Tags**: `#AI`, `#model distillation`, `#intellectual property`, `#Alibaba`, `#Anthropic`

---

<a id="item-4"></a>
## [Qualcomm to Acquire AI Startup Modular for $4 Billion](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm announced on June 24, 2026 that it will acquire AI startup Modular, known for the Mojo programming language and MAX compiler stack, to bolster its AI inference portfolio. The move signals Qualcomm’s strategy to challenge NVIDIA’s CUDA dominance by integrating Modular’s software stack with its ARM‑based chips, offering developers an alternative for high‑performance AI inference. Modular’s Mojo language, built on the MLIR compiler framework, targets CPUs, GPUs, ASICs and other accelerators, while the MAX stack provides a CUDA‑alternative inference engine; the deal is valued at approximately $4 billion and awaits regulatory approval.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: AI inference refers to running trained machine‑learning models to make predictions, a workload traditionally accelerated by NVIDIA’s CUDA platform on GPUs. Modular’s Mojo language aims to combine Python‑like usability with system‑level performance by leveraging MLIR, a flexible compiler infrastructure that can target diverse hardware. The MAX compiler stack builds on Mojo to deliver an end‑to‑end toolchain for compiling AI kernels onto various accelerators, positioning it as a potential rival to CUDA‑based ecosystems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://krun.pro/mojo-ecosystem/">Mojo Ecosystem 2026: Infrastructure, Libraries, and the MAX ... - KruN</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise at the speed of the acquisition, mixed feelings about the Mojo language, optimism about Qualcomm’s ARM/RISC‑V ambitions, and skepticism that hardware firms can successfully build competitive AI software stacks.

**Tags**: `#Qualcomm`, `#Modular`, `#AI acquisition`, `#Mojo language`, `#AI inference`

---

<a id="item-5"></a>
## [NVIDIA's 45°C Liquid Cooling Cuts Data Center Water Use Near Zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA unveiled a 45°C liquid‑cooling architecture for AI factories that eliminates the need for chillers and cooling towers, cutting on‑site water consumption to near zero while enabling the captured waste heat to be used for district heating. By drastically reducing water use and repurposing heat, the design addresses sustainability pressures on data centers and offers a potential revenue stream or community benefit through district heating, aligning AI infrastructure growth with climate goals. The coolant operates at up to 45°C (113°F), allowing direct‑to‑chip cooling without chillers; the recovered heat can be transferred via heat exchangers to a district heating network, providing usable warmth for nearby buildings.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Traditional data centers rely on chillers and cooling towers that consume large amounts of water to reject heat from air‑cooled or liquid‑cooled systems. Liquid cooling delivers coolant directly to chips, improving thermal efficiency and allowing higher coolant temperatures. District heating systems distribute waste heat from centralized sources to residential or commercial buildings for space heating. By raising the coolant temperature to 45°C, NVIDIA’s design avoids water‑intensive heat rejection and makes the heat suitable for reuse in such networks.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/">Hotter Than a Hot Tub: The 45 ° C Breakthrough to Cool ... | NVIDIA Blog</a></li>
<li><a href="https://schemaninja.com/nvidia-says-its-hotter-than-a-hot-tub/">Nvidia Says Its "Hotter Than a Hot Tub" Cooling Can Cut AI Data...</a></li>
<li><a href="https://www.linkedin.com/pulse/how-innovation-sustainability-shaping-tomorrows-world-tiago-n7lgf">Repurposing Data Center Waste Heat : A Sustainable Solution for...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the potential to partner with district heating systems, noting that 45°C waste heat could provide valuable community benefits. Some questioned whether the approach is truly novel, pointing to existing liquid‑cooled facilities and asking for clarification on favorable climates. Others shared personal experiences with warm GPU coolant and cited prior art such as NASA Ames’ modular supercomputing facility.

**Tags**: `#liquid cooling`, `#data center`, `#AI infrastructure`, `#energy efficiency`, `#district heating`

---

<a id="item-6"></a>
## [Nub: Bun-inspired all-in-one toolkit for Node.js using --require hook](https://github.com/nubjs/nub) ⭐️ 8.0/10

Nub is a Bun-inspired all-in-one toolkit for Node.js that uses a --require preload hook to load an oxc-powered Node-API transpiler, registers a module resolution hook, and injects polyfills for APIs like Worker and Temporal while running on Node's actual engine. It brings Bun-like developer experience—fast startup, integrated transpilation and polyfills—to Node.js without leaving the Node runtime, offering Node developers a way to enjoy modern tooling while staying within the familiar ecosystem. Nub packages the oxc transpiler as a Node-API addon, uses Node's --require hook for preload and module.registerHooks for resolution, and injects needed polyfills; all code ultimately runs on stock Node's engine and stdlib.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Node.js provides a --require flag to load a module before the application starts, enabling runtime modifications such as transpilation or polyfill injection. The module.registerHooks API allows customizing how modules are resolved and loaded, supporting ESM and CJS interoperability. Oxc is a high-performance JavaScript toolchain written in Rust, offering a transpiler that can be compiled as a Node-API addon for near-native speed. Node-API addons are ABI-stable native modules that can be used across Node versions without recompilation.

<details><summary>References</summary>
<ul>
<li><a href="https://glebbahmutov.com/blog/hooking-into-node-loader-for-fun-and-profit/">Hooking into Node loader for fun and profit | Better world by better...</a></li>
<li><a href="https://stackoverflow.com/questions/24602136/import-hooks-in-node-js">javascript - Import hooks in Node . js - Stack Overflow</a></li>
<li><a href="https://git-stars.org/repositories/topic/transpiler">Top transpiler Repositories - GitHub Projects for transpiler ... | Git Stars</a></li>

</ul>
</details>

**Discussion**: Commenters praised the idea as a sensible way to bring Bun's developer experience to Node.js, questioned why not just use Bun, noted curiosity about the choice of --require over --import and its ESM implications, pointed out that Node now runs TypeScript natively, and shared a successful monorepo migration with zero issues and fast performance.

**Tags**: `#Node.js`, `#developer tooling`, `#transpilation`, `#Bun alternative`, `#JavaScript`

---

<a id="item-7"></a>
## [AI Tokenomics: The Economics of Tokens, Computation, and Pricing in Foundation Models](https://arxiv.org/abs/2606.24616) ⭐️ 8.0/10

The paper (arXiv:2606.24616v1) introduces a framework for AI tokenomics that studies how tokens are generated, consumed, priced, allocated, and optimized across foundation model services, linking token-level technical costs to workflow productivity and economic value. By distinguishing token expenditure from economic value, the framework offers a new lens for pricing AI services, guiding resource allocation and market design decisions that affect researchers, enterprises, and policymakers. The framework shows that token expenditure and economic value are distinct; value depends on marginal productivity, workflow position, hidden reasoning activity, risk, and downstream propagation effects. It also outlines open research directions such as hidden-token measurement, empirical calibration, token productivity, dynamic allocation, and token-based markets.

rss · arXiv Quantitative Finance · Jun 24, 04:00

**Background**: In modern foundation model services, tokens serve as the practical accounting unit that captures information processing, computation, memory use, and energy expenditure. Tokenomics examines how these tokens are generated, consumed, priced, allocated, and optimized, bridging technical costs with economic value and market dynamics. Understanding token-level economics helps providers design pricing strategies and users assess the true cost and value of AI-generated outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.24616">[2606.24616] AI Tokenomics: The Economics of Tokens ...</a></li>
<li><a href="https://pub.towardsai.net/thinking-tokens-are-not-free-most-pipelines-treat-them-like-they-are-846708fdcef1">Thinking Tokens Are Not Free. Most Pipelines Treat... | Towards AI</a></li>
<li><a href="https://www.linkedin.com/posts/artemnovichkov_tracking-token-usage-in-foundation-models-activity-7429490715279134720-56Jj">Measuring Token Usage in iOS 26.4 Foundation Models | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#AI economics`, `#tokenomics`, `#foundation models`, `#resource allocation`, `#market design`

---

<a id="item-8"></a>
## [TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load](https://arxiv.org/abs/2506.08026) ⭐️ 8.0/10

TIP-Search introduces a time-predictable inference scheduling framework that selects conformal latency-quantile feasible models and uses shielded constrained online experts to dispatch predictions over finite workers, achieving 0.994 raw accuracy and 0.991 timely accuracy on optimized deployable pools. On the TLOB FI-2010 benchmark (h=10), TIP-Search++ improves timely accuracy from 0.156 to 0.239 and deadline satisfaction from 0.391 to 0.962. The work advances real-time machine learning systems by providing a scheduling method that guarantees predictions arrive before decision deadlines under uncertain workloads, directly improving the usability of market prediction services. Its empirical gains in timely accuracy and deadline satisfaction demonstrate a practical path toward reliable financial forecasting in volatile environments. TIP-Search first filters predictors using conformal latency-quantile feasibility checks, then dispatches tasks over a finite pool of workers via shielded constrained online experts that balance accuracy, queue pressure, and deadline risk. Variants such as OCO-ACPO and SA-OCO-ACPO achieve statistically significant improvements (e.g., +0.00285 timely accuracy, p=0.0118; +0.0146 deadline satisfaction, p=1.5×10⁻⁵) over baselines like RAMSIS and SneakPeek.

rss · arXiv Quantitative Finance · Jun 24, 04:00

**Background**: Real-time market prediction services must produce correct forecasts before a fixed decision deadline; a prediction that arrives after the deadline is useless, making timeliness as important as accuracy. Conformal prediction provides distribution-free uncertainty quantification, allowing the construction of latency‑quantile feasible models that guarantee a user‑specified probability of meeting timing constraints. Online learning with experts (e.g., shielded constrained online experts) dynamically selects among models to balance accuracy while respecting resource constraints. Under uncertain workloads, where request arrival rates vary unpredictably, time‑predictable inference scheduling seeks to optimize both prediction quality and deadline satisfaction.

<details><summary>References</summary>
<ul>
<li><a href="https://ideas.repec.org/p/arx/papers/2506.08026.html">TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load - IDEAS/RePEc</a></li>
<li><a href="https://www.semanticscholar.org/paper/78470575239e46b5a8a19ca11b425874c3083866">[PDF] TIP-Search: Time-Predictable Inference Scheduling for Market ...</a></li>
<li><a href="https://arxiv.org/html/2506.08026v2">TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load - arXiv</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#real-time systems`, `#inference scheduling`, `#financial forecasting`, `#conformal prediction`

---