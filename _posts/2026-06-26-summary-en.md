---
layout: default
title: "Horizon Summary: 2026-06-26 (EN)"
date: 2026-06-26
lang: en
---

> From 35 items, 10 important content pieces were selected

---

1. [First Full Herculaneum Scroll Read Using AI-Based Unwrapping and Ink Detection](#item-1) ⭐️ 9.0/10
2. [Apple Skips M6 Chips, Launches AI‑Optimized M7 Line for Macs](#item-2) ⭐️ 8.0/10
3. [The 'papers, please' era of the internet threatens user privacy](#item-3) ⭐️ 8.0/10
4. [Zig Introduces Endian‑agnostic bitCast and LLVM Backend Improvements](#item-4) ⭐️ 8.0/10
5. [German Court Holds Google Liable for AI Overview Errors](#item-5) ⭐️ 8.0/10
6. [Hierarchical Graph Learning Improves Calendar Spread Strategies in Commodity Futures](#item-6) ⭐️ 8.0/10
7. [Multi-Stream Temporal Fusion for Financial Fraud Detection](#item-7) ⭐️ 8.0/10
8. [Power-law scaling in limit order book prediction and FastBiNLOB architecture](#item-8) ⭐️ 8.0/10
9. [Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform](#item-9) ⭐️ 8.0/10
10. [The Token Not Taken: Sampling, State, and the Stochasticity of AI Agents](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [First Full Herculaneum Scroll Read Using AI-Based Unwrapping and Ink Detection](https://scrollprize.org/firstscroll) ⭐️ 9.0/10

Researchers have successfully read an entire Herculaneum scroll for the first time using AI-based segmentation, virtual unwrapping, and ink detection, revealing previously inaccessible ancient text. This achievement shows how AI can unlock damaged cultural heritage, opening the door to reading other carbonized scrolls and potentially recovering lost works from antiquity. The team captured 3D X‑ray tomography scans of the scroll, used AI to segment its internal layers, virtually flattened them for imaging, and applied a machine‑learning model trained on carbon‑ink fragments to visualize the hidden text.

hackernews · verditelabs · Jun 25, 15:48 · [Discussion](https://news.ycombinator.com/item?id=48675179)

**Background**: Herculaneum was buried by the eruption of Mount Vesuvius in 79 AD, carbonizing its library’s papyrus scrolls into fragile, blackened bundles that cannot be physically unrolled without damage. Since the early 2000s, researchers have used X‑ray phase‑contrast tomography to create non‑destructive 3D images of the scrolls, then applied virtual‑unwrapping algorithms to flatten those images for analysis. Recent advances in deep learning enable ink‑detection models to identify carbon ink within the scanned volumes, making it possible to read the text without ever touching the artifact.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/inside-the-ai-competition-that-decoded-an-ancient-scroll-and-changed/">Inside the AI Competition That Decoded an Ancient Herculaneum Scroll | Scientific American</a></li>
<li><a href="https://www.nationalgeographic.com/history/article/herculaneum-scrolls-mount-vesuvius-ai">Inside the stunning recovery of the lost Herculaneum Scrolls | National Geographic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Virtual_unfolding">Virtual unfolding - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters marveled at the thought of ancient writers imagining their works surviving millennia, noted that only about 20 % of the Herculaneum site has been excavated so many more scrolls may await discovery, and welcomed the project as a hopeful example of technology used for cultural good rather than advertising. One former team lead also shared that 140 additional columns of text were recently unwrapped in another scroll.

**Tags**: `#archaeology`, `#AI`, `#cultural heritage`, `#Vesuvius challenge`, `#text recovery`

---

<a id="item-2"></a>
## [Apple Skips M6 Chips, Launches AI‑Optimized M7 Line for Macs](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true) ⭐️ 8.0/10

Apple announced it will skip the high‑end M6 Pro and Max chip variants and instead accelerate the release of an AI‑focused M7 family (Pro, Max, Ultra) aimed at improving local large language model inference on Mac computers. This shift signals Apple’s commitment to embedding AI workloads directly into its silicon, potentially giving Mac users stronger on‑device LLM performance and reducing reliance on cloud APIs. The base M7 is targeting ~240 GB/s memory bandwidth, with future variants possibly reaching 1,200–1,500 GB/s and up to 512 GB of unified memory, and may be fabricated on Intel’s 18A process node.

hackernews · scrlk · Jun 25, 17:38 · [Discussion](https://news.ycombinator.com/item?id=48676795)

**Background**: Apple’s M‑series chips integrate CPU, GPU, and a Neural Engine with a unified memory architecture that allows the processor and graphics cores to share a single pool of high‑bandwidth RAM, eliminating the VRAM bottleneck that limits large model inference on discrete GPUs. Since the M1 launch in 2020, each generation has increased memory bandwidth and AI acceleration capabilities, enabling developers to run large language models locally on MacBooks and Mac Studios. The upcoming M7 line is designed to further boost memory bandwidth and AI compute to support more demanding on‑device LLM workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macworld.com/article/3177046/report-apple-to-skip-m6-pro-max-chips-fast-track-m7-for-local-ai.html">Report: Apple to skip M6 Pro/Max chips, fast-track M7 for local AI</a></li>
<li><a href="https://www.sitepoint.com/local-llms-apple-silicon-mac-2026/">Local LLMs Apple Silicon Mac 2026 | M1 M2 M3 Guide</a></li>
<li><a href="https://www.cultofmac.com/news/apple-will-skip-m6-pro-and-max-chips">Apple will skip M6 Pro and Max chips, fast-track M7 — here's why</a></li>

</ul>
</details>

**Discussion**: Several commenters praised the strategic fit of focusing on AI‑optimized silicon for local LLM inference, citing the planned 240 GB/s bandwidth and the possibility of much higher bandwidth variants. Others raised concerns about contingency plans if AI adoption slows and debated the risks associated with adopting Intel’s 18A process node for early M7 production.

**Tags**: `#Apple`, `#M7 chip`, `#AI hardware`, `#Mac processors`, `#semiconductor roadmap`

---

<a id="item-3"></a>
## [The 'papers, please' era of the internet threatens user privacy](https://expression.fire.org/p/the-papers-please-era-of-the-internet) ⭐️ 8.0/10

The article warns that increasing online identity checks, often framed as age verification, are eroding user privacy and examines technical mitigations such as anonymous credentials and zero‑knowledge proofs. As governments push for mandatory age verification and identity verification, the lack of privacy‑preserving mechanisms could enable mass surveillance and data misuse, affecting all internet users. Anonymous credentials let users prove attributes (e.g., being over a certain age) without revealing their identity, using schemes like Microsoft’s U‑Prove or IBM’s Idemix, while zero‑knowledge proofs enable age verification without disclosing birthdates or other personal data.

hackernews · bilsbie · Jun 25, 21:44 · [Discussion](https://news.ycombinator.com/item?id=48679608)

**Background**: Recent legislative efforts in various countries require online platforms to verify users’ ages before granting access to certain content, prompting a rise in ‘papers, please’ style identity checks. Anonymous credentials, first introduced by Chaum and later refined by Brands and Camenisch‑Lysyanskaya, provide a way to prove claims while keeping the holder’s identity hidden. Zero‑knowledge proofs complement this by allowing verifiers to confirm a statement’s truth without learning any underlying data, making them attractive for privacy‑preserving age assurance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/computer-science/anonymous-credential">Anonymous Credential - an overview | ScienceDirect Topics</a></li>
<li><a href="https://www.newamerica.org/insights/exploring-privacy-preserving-age-verification/">Age Verification to Protect Youth Online: Using Zero Knowledge Proofs</a></li>
<li><a href="https://brave.com/blog/zkp-age-verification-limits/">The limits of zero-knowledge for age-verification - Brave</a></li>

</ul>
</details>

**Discussion**: Commenters noted that anonymous credentials offer a technical fix (j2kun), debated the perceived cost‑benefit of privacy loss (tqi), expressed intent to retreat from the digital world (HoldOnAMinute), questioned the necessity of constant online access for children (mossTechnician), and predicted upcoming UK policies combining age gating with a national identity passport (AJRF).

**Tags**: `#privacy`, `#identity verification`, `#internet policy`, `#anonymous credentials`, `#age verification`

---

<a id="item-4"></a>
## [Zig Introduces Endian‑agnostic bitCast and LLVM Backend Improvements](https://ziglang.org/devlog/2026/#2026-06-25) ⭐️ 8.0/10

Zig has updated its @bitCast operation to be endian‑agnostic, meaning the result no longer depends on the target’s byte order, and has made accompanying improvements to its LLVM backend to better support these semantics. It also benefits packed struct manipulation and arbitrary‑width integer support, making Zig more attractive for low‑level programming. The semantics were formalized in language proposal #19755 and are already implemented in the self‑hosted x86_64 backend.

hackernews · kouosi · Jun 25, 14:19 · [Discussion](https://news.ycombinator.com/item?id=48673825)

**Background**: LLVM is a compiler infrastructure that Zig uses for code generation, and improvements to its backend can affect how bitcasts and packed structs are lowered to machine instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://ziglang.org/devlog/2026/?from_theconsensus=1">Devlog ⚡ Zig Programming Language - ziglang.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Endianness">Endianness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLVM">LLVM - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Several users highlighted how the change simplifies packed‑struct manipulation, while a few questioned whether arbitrary‑width integers are worth the added complexity compared to manual packing.

**Tags**: `#Zig`, `#programming languages`, `#bitcast`, `#LLVM`, `#systems programming`

---

<a id="item-5"></a>
## [German Court Holds Google Liable for AI Overview Errors](https://simonwillison.net/2026/Jun/25/ai-and-liability/#atom-everything) ⭐️ 8.0/10

A German court ruled that Google is liable for false information in its AI-generated search overviews, treating the AI output as Google's own statements. Bruce Schneier commented that AI agents should be considered extensions of their deployers. The ruling sets a precedent that could make tech companies directly liable for AI-generated content, influencing how firms deploy generative AI and manage risk. It challenges the notion that AI can shield businesses from accountability for errors. The decision specifically concerns Google's AI Overviews feature, which provides summarized answers in search results, and holds Google responsible for inaccuracies as if they were its own statements. Schneier argues that allowing companies to hide behind AI errors would create bad incentives and discourage hiring human experts.

rss · Simon Willison · Jun 25, 22:28

**Background**: AI Overviews are generative AI-generated summaries that Google displays atop search results to answer user queries directly. Legal liability for AI-generated content is an emerging issue, with courts beginning to consider whether AI outputs should be attributed to their deployers. The German case marks one of the first rulings treating AI output as the company's own speech.

<details><summary>References</summary>
<ul>
<li><a href="https://dublinpost.ie/policy/german-court-rules-on-google-ai-overviews-liability">German court rules on Google AI Overviews liability</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/">Nobody needs AI to search the Internet, court says in ruling against...</a></li>
<li><a href="https://www.techsterhub.com/news/google-expands-ai-generated-overviews-for-search-engine-results/">Google Expands AI - Generated Overviews For Search Engine Results</a></li>

</ul>
</details>

**Tags**: `#AI liability`, `#legal policy`, `#AI ethics`, `#Google`, `#German ruling`

---

<a id="item-6"></a>
## [Hierarchical Graph Learning Improves Calendar Spread Strategies in Commodity Futures](https://arxiv.org/abs/2606.25811) ⭐️ 8.0/10

The paper introduces a hierarchical graph learning framework that models commodity futures hierarchically and applies it to calendar spread strategies, showing improved prediction and trading performance on CME data. By addressing the lack of learning‑based methods for calendar spread strategies and ignoring maturity‑dependent relationships, the work fills two notable gaps in ML finance and could inspire new quantitative trading approaches. The method constructs a two‑level graph (underlying assets and individual contracts) with intra‑ and cross‑level edges, learns representations via hierarchical graph neural networks, converts predictions into calendar spread positions, and empirically outperforms benchmark models on CME‑traded commodity futures.

rss · arXiv Quantitative Finance · Jun 25, 04:00

**Background**: Commodity futures are often organized by underlying asset and contract maturity, enabling a hierarchical representation where assets sit at the top level and individual futures contracts at the lower level. A calendar spread involves simultaneously buying and selling futures of the same underlying asset with different expiration dates, aiming to profit from changes in the term structure. Hierarchical graph learning extends graph neural networks to capture patterns across multiple scales of a graph, allowing models to exploit both intra‑asset correlations and maturity‑dependent links.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Calendar_spread">Calendar spread - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2606.25811">[2606.25811] Hierarchical Graph Learning for Calendar Spread ...</a></li>
<li><a href="https://johnnylu305.github.io/data/Hierarchical_Graph_Learning_20250327.pdf">Hierarchical Graph Learning for Spectral Clustering</a></li>

</ul>
</details>

**Tags**: `#hierarchical graph learning`, `#calendar spread`, `#commodity futures`, `#machine learning`, `#quantitative finance`

---

<a id="item-7"></a>
## [Multi-Stream Temporal Fusion for Financial Fraud Detection](https://arxiv.org/abs/2606.25007) ⭐️ 8.0/10

The paper introduces the Multi-Stream Fraud Transformer (MSFT), which independently encodes heterogeneous event streams (transactions, login sessions, risk signals) with separate Transformer encoders and fuses their representations via configurable mechanisms. On a large‑scale dataset of 10M users with a 1.5% fraud rate, MSFT achieves 0.99 AUROC, substantially outperforming gradient‑boosted trees on aggregated features (0.74 AUROC). By demonstrating that sequence‑level multi‑stream modeling can surpass traditional tree‑based methods, the work suggests a path toward more accurate and deployable fraud detection systems in digital banking. The ablation study also highlights which fusion and positional encoding strategies are most effective, guiding practitioners in architecture selection. The authors compared five fusion strategies—concatenation, gated fusion, time‑aware positional encoding, cross‑stream attention, and a full combination—finding that time‑aware positional encoding yields the highest AUROC (0.9961) while gated fusion gives the best precision (0.989). An ablation showed that a single‑stream Transformer with matched parameters reaches only 0.82 AUROC, confirming the necessity of multi‑stream encoding, and the risk event stream contributed the strongest individual signal. Validation on proprietary production data showed over 22% relative AUROC improvement over an XGBoost baseline.

rss · arXiv Quantitative Finance · Jun 25, 04:00

**Background**: Financial fraud detection often requires analyzing multiple heterogeneous event streams—such as transactions, login sessions, and risk signals—that individually look benign but collectively reveal fraudulent patterns. Traditional approaches aggregate these streams into handcrafted features and apply gradient‑boosted trees, which can miss subtle temporal dependencies. Transformer‑based models excel at capturing long‑range sequences, and multi‑stream architectures allow each modality to be encoded separately before fusion, preserving modality‑specific information while enabling cross‑stream interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.25007">Multi - Stream Temporal Fusion for Financial Fraud Detection</a></li>
<li><a href="https://arxiv.org/pdf/2206.06488">Multimodal Learning with Transformers</a></li>
<li><a href="https://arxiv.org/html/2509.14640">DyWPE: Signal- Aware Dynamic Wavelet Positional Encoding for ...</a></li>

</ul>
</details>

**Tags**: `#financial fraud detection`, `#transformer`, `#multi-stream learning`, `#time series`, `#machine learning`

---

<a id="item-8"></a>
## [Power-law scaling in limit order book prediction and FastBiNLOB architecture](https://arxiv.org/abs/2606.25986) ⭐️ 8.0/10

The paper demonstrates that predictive loss versus compute follows a power law with R^2=0.941 for limit order book models. It introduces FastBiNLOB, a latency‑efficient dense axis‑separable LOB mixer that achieves higher macro‑F1 scores than prior SOTA at lower latency. This work connects ML scaling theory to high‑frequency trading, providing a principled way to balance compute and latency for LOB prediction. It impacts both the design of efficient trading systems and the broader ML systems community interested in inference‑compute frontiers. Experiments used the FI‑2010 dataset, evaluating models from decision trees to MLPLOB and other neural LOB architectures; a power‑law fit to low‑ and mid‑compute non‑MLPLOB points extrapolated to the high‑compute MLPLOB frontier with R^2=0.941. FastBiNLOB employs dense axis‑separable temporal and feature mixing, exceeding the published y10 and y100 macro‑F1 targets at notably lower latency than existing SOTA.

rss · arXiv Quantitative Finance · Jun 25, 04:00

**Background**: Limit order book (LOB) prediction aims to forecast short‑term price movements from the sequence of buy and sell orders, a task crucial for high‑frequency trading. Scaling laws in machine learning describe how model performance improves predictably with increased compute or data, often following a power law. MLPLOB is a simple multilayer perceptron baseline for LOB prediction, frequently used as a reference architecture in benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.25986">The Inference-Compute Frontier and a Latency-Efficient Architecture ...</a></li>
<li><a href="https://openreview.net/forum?id=CYT5zrOfK5">LOBBen-TM: A Benchmark Study of Limit Order Book Prediction ...</a></li>
<li><a href="https://www.researchgate.net/publication/389315687_TLOB_A_Novel_Transformer_Model_with_Dual_Attention_for_Stock_Price_Trend_Prediction_with_Limit_Order_Book_Data">(PDF) TLOB: A Novel Transformer Model with Dual Attention for Stock...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#limit order book`, `#scaling laws`, `#financial trading`, `#neural architecture`

---

<a id="item-9"></a>
## [Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform](https://arxiv.org/abs/2606.17397) ⭐️ 8.0/10

The study introduces a thresholded eligibility control (TEC) recommender that reallocates template exposure based on posting activity and unfilled capacity, raising the job-finding rate from 57.6% to 70.0% in simulations and a prefecture-level field experiment. It addresses recommendation bias in scarce-opportunity two-sided markets, improving matching efficiency for labor platforms while offering a scalable, parallelizable exposure-control solution. TEC is fully parallelizable for large-scale digital platforms; the field experiment increased matches and exposure per active template, reduced the share of low-exposure templates, and improved impression-level favoriting and downstream matching.

rss · arXiv Quantitative Finance · Jun 25, 04:00

**Background**: Spot-work platforms match temporary workers with short-lived job shifts, where workers favorite job templates and receive notifications when firms post shifts from those templates. Traditional recommenders often concentrate exposure on popular templates, leaving high-demand but less popular templates under-exposed. In two-sided markets, platforms must balance exposure to improve matches for both workers and firms.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.17397">Designing Recommendation Exposure and Favorite Lists : A Field...</a></li>
<li><a href="https://www.mdc.e.u-tokyo.ac.jp/news/9401/">[UTMD-136] Designing Recommendation Exposure and Favorite Lists...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Two-sided_market">Two - sided market - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#recommender systems`, `#field experiment`, `#two-sided markets`, `#labor platforms`, `#exposure control`

---

<a id="item-10"></a>
## [The Token Not Taken: Sampling, State, and the Stochasticity of AI Agents](https://arxiv.org/abs/2606.08998) ⭐️ 8.0/10

The arXiv preprint 2606.08998v2 analyzes how token sampling and extrinsic factors cause variability in agentic AI behavior, proposing a framework to separate intrinsic and extrinsic sources of stochasticity and to mitigate their effects. Understanding these sources of stochasticity is crucial for improving the reliability, reproducibility, and safety of deployed AI agents, guiding better system design and evaluation practices. The paper identifies intrinsic variability from token generation—where a model’s probability distribution is sampled via a pseudo‑random number generator—and shows how a single token change can alter tool calls, code edits, or agent state; extrinsic sources include shifting environments, live data, serving infrastructure, batch effects, and numerical precision.

rss · arXiv Quantitative Finance · Jun 25, 04:00

**Background**: Agentic AI systems are built around a foundation model that is placed in an orchestration loop responsible for planning, invoking tools, observing outcomes, and updating internal state. Token sampling introduces intrinsic randomness because the model converts logits to probabilities and selects the next token using a pseudo‑random number generator, which can propagate small changes into divergent behavior. Extrinsic factors such as changing environments, live data feeds, serving infrastructure variations, batch effects, and numerical details further contribute to run‑to‑run variability. By separating these layers, the paper clarifies when observed stochasticity is reproducible and when deterministic execution still yields different results in deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://charanhu.medium.com/how-large-language-models-like-gpt-generate-text-a-deep-dive-into-stochastic-decoding-3d7219dfe0a3">How Large Language Models Like GPT Generate Text... | Medium</a></li>
<li><a href="https://github.com/crewAIInc/crewAI">GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing...</a></li>
<li><a href="https://www.engineering.fyi/article/stanford-s-marin-foundation-model-the-first-fully-open-model-developed-using-jax">Stanford’s Marin foundation model : The first fully... | Engineering.fyi</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#token sampling`, `#stochasticity`, `#foundation models`, `#reproducibility`

---