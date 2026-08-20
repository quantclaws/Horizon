---
layout: default
title: "Horizon Summary: 2026-08-20 (EN)"
date: 2026-08-20
lang: en
---

> From 41 items, 14 important content pieces were selected

---

1. [Stripe to Acquire OpenRouter for Reported $7B+](#item-1) ⭐️ 8.0/10
2. [Go 1.27 Release Adds Generic Methods, uscale FP Parsing, Post‑Quantum Crypto, and UUID Package](#item-2) ⭐️ 8.0/10
3. [Google replaces Git tags with Google Drive requests.](#item-3) ⭐️ 8.0/10
4. [Unsloth Releases Dynamic 3.0 GGUF Quantization Format for LLMs](#item-4) ⭐️ 8.0/10
5. [Geolocating a Random Island Using Geometry and CUDA](#item-5) ⭐️ 8.0/10
6. [Hacker News Debates AI's Impact on Mathematical Research and Proof Clarity](#item-6) ⭐️ 8.0/10
7. [LLMs Transform Extensible, Sandboxed Software for Personal Workflows](#item-7) ⭐️ 8.0/10
8. [Stranded credentials: how a skill-signaling market absorbed generative AI](#item-8) ⭐️ 8.0/10
9. [COS-TT-CHF enables fast multi-asset option pricing.](#item-9) ⭐️ 8.0/10
10. [Conservation of Short-term Flows: Signed Optimal Transport](#item-10) ⭐️ 8.0/10
11. [Generative AI adoption reduces demand for social skills in U.S. jobs](#item-11) ⭐️ 8.0/10
12. [Multi-view contrastive learning framework for spatial embeddings in risk modelling](#item-12) ⭐️ 8.0/10
13. [This paper forecasts duration in high-frequency financial data using a self-exciting flexible residual point process.](#item-13) ⭐️ 8.0/10
14. [Geometric BSDEs and Two-Driver BSDEs Introduced for Financial Applications](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe to Acquire OpenRouter for Reported $7B+](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) ⭐️ 8.0/10

Stripe is reportedly acquiring OpenRouter, a unified API that aggregates access to over 400 LLM models from 60+ providers, in a deal valued at over $7 billion. The acquisition highlights the growing strategic importance of model aggregation infrastructure, giving Stripe a powerful tool to embed diverse AI capabilities into its payments platform and signaling strong market validation for LLM gateway services. OpenRouter provides a single OpenAI‑compatible interface with automatic failover, transparent usage‑based pricing, and access to models such as GPT‑5.2, Claude Opus 4.5, and Gemini 3 Pro Preview.

hackernews · rvz · Aug 19, 17:32 · [Discussion](https://news.ycombinator.com/item?id=49364559)

**Background**: OpenRouter acts as a unified API gateway that aggregates hundreds of AI models from dozens of providers, allowing developers to switch between models without changing code. It offers features like automatic failover, transparent pricing, and a dashboard for managing usage and costs. This aggregation layer reduces vendor lock‑in and enables price competition among model providers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.everydev.ai/tools/openrouter">OpenRouter - Unified API for Multiple LLMs | EveryDev.ai</a></li>
<li><a href="https://www.daidu.ai/products/openrouter-unified-api">OpenRouter – Unified API Hub for Multiple LLMs – Daidu.ai</a></li>
<li><a href="https://betterai.dev/openrouter">OpenRouter : Unified LLM API : 500+ models, 60+ providers via one...</a></li>

</ul>
</details>

**Discussion**: Commenters praised OpenRouter’s value as a proxy that fosters price and quality competition among LLM providers, while others warned that the acquisition could bring layoffs and cultural shifts. Some users questioned the use of 'Open' in a for‑profit VC‑backed name, and others asked about the exact revenue model, such as reselling enterprise token access.

**Tags**: `#AI/ML`, `#LLM`, `#API`, `#Acquisition`, `#Stripe`

---

<a id="item-2"></a>
## [Go 1.27 Release Adds Generic Methods, uscale FP Parsing, Post‑Quantum Crypto, and UUID Package](https://go.dev/blog/go1.27) ⭐️ 8.0/10

Go 1.27 introduces generic method support, allowing methods to be written with type parameters and used without explicit type arguments. It also adopts Russ Cox’s uscale algorithm for faster and more accurate floating‑point parsing, adds the crypto/mldsa post‑quantum signature package, and provides a standard library uuid package implementing RFC 4122. These changes improve language ergonomics, runtime performance, and security posture while reducing reliance on external dependencies. They align Go with industry trends toward generic programming, robust numeric handling, and migration to post‑quantum cryptography. Generic methods enable type inference so callers can omit type arguments, and the uscale algorithm parses IEEE‑754 floats at gigabyte‑per‑second speeds with correct rounding. The crypto/mldsa package follows FIPS 204 for ML‑DSA signatures, and the uuid package provides functions for generating and parsing UUIDs v1‑v5 as defined in RFC 4122.

hackernews · database64128 · Aug 19, 18:33 · [Discussion](https://news.ycombinator.com/item?id=49365405)

**Background**: Go introduced generic functions in Go 1.18, but generic methods were previously unavailable, limiting reusable APIs. Floating‑point parsing in the standard library relied on older algorithms that could be slow or produce rounding errors, prompting the adoption of the uscale algorithm. As quantum computers advance, industries are standardizing post‑quantum primitives such as ML‑DSA, and UUIDs are widely used identifiers that benefit from a stable, vetted standard‑library implementation.

<details><summary>References</summary>
<ul>
<li><a href="https://research.swtch.com/fp">research!rsc: Floating-Point Printing and Parsing Can Be ...</a></li>
<li><a href="https://medium.com/@mehmetirmaakk/post-quantum-cryptography-go-nodejs-python-2026-7498f8cd8b2b">Post-Quantum Cryptography in Go 1.27, Node.js & Python: Is ...</a></li>
<li><a href="https://rednafi.com/shards/2026/04/go-uuid/">Accepted proposal: UUID in the Go standard library | Redowan's Reflections</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the generic method ergonomics and highlighted the uscale algorithm’s performance gains. Many praised the crypto team’s proactive post‑quantum work and anticipated widespread adoption of the new uuid package to replace google/uuid. A few noted minor wishes such as syntax highlighting on the Go blog.

**Tags**: `#Go`, `#programming language`, `#release`, `#generics`, `#cryptography`

---

<a id="item-3"></a>
## [Google replaces Git tags with Google Drive requests.](https://grapheneos.social/@GrapheneOS/117057099753905023) ⭐️ 8.0/10

Google has stopped distributing certain Android source code via Git tags and now requires developers to submit a Google Form to receive the code through a Google Drive link. The change raises GPLv2 compliance concerns because the license requires source code to be made available in a manner that allows easy access, and a manual request process may hinder developers' ability to obtain and modify the code. The affected code includes parts of the Android Open Source Project that are GPL‑licensed, and users report slow responses and limited availability of the Google Drive links.

hackernews · Animux · Aug 19, 17:47 · [Discussion](https://news.ycombinator.com/item?id=49364745)

**Background**: The GNU General Public License version 2 (GPLv2) requires that anyone distributing binaries also make the corresponding source code available under the same terms. Previously, Google provided access to certain Android source components through immutable Git tags, allowing developers to clone or checkout specific versions directly. Now, Google directs requesters to fill out a Google Form, after which a human sends a Google Drive link containing the source code archive.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GNU_General_Public_License">GNU General Public License - Wikipedia</a></li>
<li><a href="https://source.android.com/opensourcerequest">Get Android source - Android Open Source Project</a></li>
<li><a href="https://git-scm.com/book/en/v2/Git-Basics-Tagging">Tagging - Git</a></li>

</ul>
</details>

**Discussion**: Commenters expressed worry that the new manual request process may violate GPLv2 by hindering source access, while others noted the change seems more inconvenient for Google and joked about future extremes like mailing printed code.

**Tags**: `#Android`, `#Open Source`, `#GPL`, `#Google`, `#Source Code Distribution`

---

<a id="item-4"></a>
## [Unsloth Releases Dynamic 3.0 GGUF Quantization Format for LLMs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) ⭐️ 8.0/10

Unsloth announced Dynamic 3.0 GGUFs, a new quantization format that delivers over 10% top‑1% better accuracy at the same model size compared to Dynamic v2.0, starting with Qwen3.8‑27B models released today. The update improves the accuracy‑size trade‑off for locally run LLMs, enabling developers to achieve higher performance on consumer hardware without increasing model footprint. Dynamic v3.0 removes the MTP component to boost speed, supports 1‑bit quants, and uses a revised layer selection strategy for GGUF files; however, the lack of version numbers in filenames causes confusion for users managing multiple downloads.

hackernews · jonesy827 · Aug 19, 18:36 · [Discussion](https://news.ycombinator.com/item?id=49365443)

**Background**: GGUF (GPT‑Generated Unified Format) is a file format for storing quantized large language models, designed to reduce memory usage and enable inference on consumer‑grade hardware. Quantization lowers the numerical precision of model weights, trading off some accuracy for significant size reductions. Dynamic quantization, as used by Unsloth, selects different precision levels per layer during inference to balance performance and accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://unsloth.ai/docs/basics/dynamic-3.0-ggufs">Unsloth Dynamic 3.0 GGUFs | Unsloth Documentation</a></li>
<li><a href="https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/discussions/74">unsloth/Qwen3.8-27B-GGUF · Introducing Unsloth Dynamic v3 Qwen3.8</a></li>
<li><a href="https://ggufloader.github.io/what-is-gguf.html">What is GGUF ? Complete Guide to GGUF Format & Quantization</a></li>

</ul>
</details>

**Discussion**: Users praise the quality of Unsloth’s GGUFs but request clearer versioning to avoid filename confusion, noting that identical names make it hard to distinguish old and new downloads. Some commenters highlight that removing MTP improves speed for memory‑constrained setups, while others ask for benchmarks measuring coding performance and multi‑step reasoning.

**Tags**: `#unsloth`, `#GGUF`, `#LLM quantization`, `#model deployment`, `#AI/ML`

---

<a id="item-5"></a>
## [Geolocating a Random Island Using Geometry and CUDA](https://yassa9.github.io/osint/gralhix-004/) ⭐️ 8.0/10

The author published a blog post detailing how geometric calculations (e.g., sun angle and shadow length) combined with GPU‑accelerated CUDA code were used to pinpoint the location of an unidentified island from a single photograph. This demonstrates how inexpensive OSINT techniques can leverage modern GPU parallelism for precise terrain matching, with direct relevance to military navigation (TERCOM) and autonomous landing systems such as Mars 2020. The method extracts terrain contours from the image, compares them to a digital elevation map using a CUDA‑implemented matching kernel, and refines the estimate with geometric constraints from sunlight direction.

hackernews · yassa9 · Aug 19, 12:19 · [Discussion](https://news.ycombinator.com/item?id=49360545)

**Background**: CUDA is NVIDIA’s parallel computing platform that enables general‑purpose code to run on GPUs, providing massive speed‑up for data‑parallel tasks such as image processing and pattern matching. Terrain matching algorithms compare observed terrain features (e.g., contours, elevations) with reference digital elevation maps to estimate a sensor’s location, a technique used in inertial navigation and planetary landing. OSINT practitioners often geolocate photographs by analyzing shadows, celestial cues, and visible landmarks, and can accelerate these searches with GPU‑based matching.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/index.html">CUDA Programming Guide — CUDA Programming Guide</a></li>
<li><a href="https://ieeexplore.ieee.org/document/68120">Navigation using image sequence analysis and 3-D terrain matching</a></li>
<li><a href="https://shadowdragon.io/resources/osint-techniques/">OSINT Techniques : Expert Tactics for Investigators (2026)</a></li>

</ul>
</details>

**Discussion**: Commenters praised the clear, enjoyable write‑up and noted connections to real‑world systems such as TERCOM and the Mars 2020 landing, while some suggested adding geoguessing or brute‑force checks and pointed out the irony of the article appearing alongside a piece about avoiding police‑state technologies.

**Tags**: `#geolocation`, `#CUDA`, `#computer vision`, `#OSINT`, `#terrain matching`

---

<a id="item-6"></a>
## [Hacker News Debates AI's Impact on Mathematical Research and Proof Clarity](https://arxiv.org/abs/2608.16753) ⭐️ 8.0/10

A Hacker News thread discussed how AI is reshaping mathematical research, featuring Terence Tao's rule of thumb that proofs should be explainable by experts and concerns that AI-generated proofs often obscure novel ideas. The discussion highlights growing tensions between AI-assisted proof generation and the mathematical community's values of clarity, attribution, and deep understanding, which could affect future research practices and funding priorities. Terence Tao's rule of thumb was cited, alongside his observation that AI-generated writing often dwells on trivialities while obscuring the novel core of arguments; the thread also referenced advances in Lean-based AI theorem provers such as DeepMind's 2024 Olympiad-level system and DeepSeek-Prover-V2.

hackernews · jonbaer · Aug 19, 15:14 · [Discussion](https://news.ycombinator.com/item?id=49362728)

**Background**: Artificial intelligence is increasingly used to assist in mathematical research, from generating proof sketches to automating formal verification in proof assistants such as Lean and Coq. These tools aim to increase reliability and speed, but they raise questions about the transparency and intelligibility of AI-produced arguments. The debate reflects broader concerns about how AI reshapes epistemic values in mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>
<li><a href="https://www.amazon.science/blog/how-ai-is-changing-the-nature-of-mathematical-research">How AI is changing the nature of mathematical research - Amazon Science</a></li>

</ul>
</details>

**Discussion**: Commentators expressed worry that AI-generated proofs may be correct yet incomprehensible to humans, echoing Tao's call for expert-level explainability. Others warned that AI writing often hides the most interesting parts of arguments while focusing on trivial details, and debated whether the drive for rapid AI-powered results could distort mathematical values. A few voices suggested that if AI outperforms humans, deep human understanding might become optional, likening it to benefiting from AI-optimized logistics without needing to comprehend the underlying mathematics.

**Tags**: `#AI`, `#mathematics`, `#proof verification`, `#Terence Tao`, `#research trends`

---

<a id="item-7"></a>
## [LLMs Transform Extensible, Sandboxed Software for Personal Workflows](https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/) ⭐️ 8.0/10

The article discusses how large language models enable personalized, pluggable software that sidesteps enterprise complexity, highlighting both opportunities and security challenges. This trend signals a move toward highly customizable AI‑augmented workflows that could reduce reliance on monolithic enterprise apps, while raising new concerns about sandbox safety and data governance. Commenters warn that users will want to share data‑driven apps among small groups, which can undermine sandbox security if data‑access logic is flawed.

hackernews · coloneltcb · Aug 19, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49363668)

**Background**: Extensibility in software refers to the ability to add features via plug‑ins, APIs, or updates without rewriting the core system. Sandboxing isolates code execution to limit potential harm from untrusted programs. Pluggable architectures define clear contracts that let third‑party modules be added or replaced at runtime. Large language models (LLMs) now enable non‑programmers to generate functional code, making it easier to create personal, automated tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extensibility">Extensibility - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/enterprise-software/definition/application-sandboxing">What is Application Sandboxing? | Enterprise Software</a></li>
<li><a href="https://userefract.io/blog/series/pluggable-by-design">Pluggable by Design · Refract</a></li>

</ul>
</details>

**Discussion**: Commenters agree that LLMs excel at building personal, workflow‑specific software that bypasses enterprise complexity, but they warn that sandboxed execution alone is not secure enough for sharing data‑driven apps. Some note that enterprise giants like Google or Microsoft are more likely to set the dominant patterns than Cloudflare, and a few envision LLM‑generated specifications taking over product‑manager roles.

**Tags**: `#LLMs`, `#extensible software`, `#sandboxing`, `#AI agents`, `#developer tools`

---

<a id="item-8"></a>
## [Stranded credentials: how a skill-signaling market absorbed generative AI](https://arxiv.org/abs/2608.17111) ⭐️ 8.0/10

Using Kaggle’s 2010‑2026 archive of 444,698 participations, the study shows that competition medals retain strong predictive power for future performance in the era of generative AI, while upload‑based competition medals lose much of their informational value. The findings reveal how generative AI reshapes skill signaling in online competitions, offering guidance for designing credentials that remain valid and for understanding AI’s broader impact on labor markets and talent assessment. Medals predict leaderboard performance mainly in the first year after earning; upload‑competition medal stocks lost 82% of their informativeness, with institutional stranding accounting for half to three‑quarters of that loss. Official lifetime‑tier rankings discard 13‑16% of medal information, whereas a simple index that weights recent medals more heavily—derived from pre‑AI data—outperforms the official tiers in predicting AI‑era performance.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: Kaggle hosts data science competitions in two formats: upload‑competitions, where submissions are scored on published data, and code‑competitions, where submissions are scored by running code on hidden data. The platform awards medals (e.g., Expert, Master, Grandmaster) that participants treat as professional credentials. Generative AI can now perform many of the tasks these competitions aim to measure, raising questions about the enduring signaling value of such credentials.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.17111">[2608.17111] Stranded credentials: how a skill - signaling market ...</a></li>
<li><a href="https://www.kaggle.com/docs/competitions-setup">Getting Started on Kaggle | Kaggle</a></li>
<li><a href="https://arxiv.org/html/2608.17111">Stranded credentials: how a skill - signaling market absorbed...</a></li>

</ul>
</details>

**Tags**: `#AI impact`, `#credential signaling`, `#Kaggle`, `#skill assessment`, `#generative AI`

---

<a id="item-9"></a>
## [COS-TT-CHF enables fast multi-asset option pricing.](https://arxiv.org/abs/2608.17636) ⭐️ 8.0/10

The paper introduces COS-TT-CHF, a tensor-train compression of characteristic-function tensors using the TT-cross algorithm to price arithmetic basket and min/max multi-asset options under Lévy and affine models. It demonstrates efficient post-setup strike-grid and Greeks calculations, achieving speed-ups over direct COS and QMC benchmarks in dimensions up to d=30 for GBM and d=20 for VG, NIG, and common-Heston. By mitigating the curse of dimensionality, COS-TT-CHF provides a practical low-rank approach that outperforms existing Fourier-based and Monte Carlo methods for high-dimensional multi-asset options, enabling faster pricing and risk sensitivity analysis in quantitative finance workflows. The method builds a low-rank tensor-train representation via TT-cross interpolation of sampled characteristic-function tensors, allowing rapid evaluation of option prices across strike grids and selected component Delta/Vega after an initial offline phase. Numerical experiments compare against adaptive-quadrature Fourier benchmarks, direct COS, a tensor-Fourier min-option baseline, and quasi-Monte Carlo Sobol references, showing favorable timings from d=2–4 onward and accurate results up to 30 assets for GBM and 20 assets for VG, NIG, and common-Heston models.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: The COS method prices options by expanding the characteristic function into a Fourier-cosine series, but a direct multi-asset implementation forms coefficient arrays that grow exponentially with the number of assets, known as the curse of dimensionality. Tensor-train (TT) decomposition mitigates this by representing high-dimensional tensors as a chain of low-rank cores, drastically reducing storage and computational cost. The TT-cross algorithm constructs such approximations from black-box function samples using adaptive cross interpolation, avoiding the need for full tensor evaluation. In this work, TT-cross compresses the characteristic-function tensor to obtain TT-COS coefficients for efficient basket and min/max option pricing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.17636">[2608.17636] COS-TT-CHF: A Tensor-Train Characteristic ...</a></li>
<li><a href="https://ttml.readthedocs.io/en/latest/tt_cross.html">TT Cross — ttml 1.0 documentation</a></li>
<li><a href="https://www.mdpi.com/2227-7390/13/11/1828">Learning Parameter Dependence for Fourier-Based Option ... - MDPI</a></li>

</ul>
</details>

**Tags**: `#option pricing`, `#tensor train`, `#characteristic function`, `#COS method`, `#multi-asset`

---

<a id="item-10"></a>
## [Conservation of Short-term Flows: Signed Optimal Transport](https://arxiv.org/abs/2608.17363) ⭐️ 8.0/10

The paper introduces a signed optimal transport framework that uses a global flatness regularizer derived from the continuum transport equation, proves existence and uniqueness of the optimal coupling, and presents an algorithmic scheme ensuring lossless information transport under bi-marginal constraints. By extending optimal transport to signed measures, the work enables modeling of flows with gains and losses—such as inventory adjustments, species migration, and traffic deviations—offering a principled tool for network analysis in supply chains, ecology, and transportation systems. The global flatness regularizer is induced by the continuum transport equation; the analysis adopts a harmonic analysis perspective on transport networks, solves a variational problem for optimal couplings, and provides an empirical analysis framework that is invariant under locally compact abelian groups, thus applicable to both time‑series and panel data.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: Optimal transport theory seeks the most cost‑efficient way to move mass between distributions, traditionally formulated for probability measures. Signed optimal transport generalizes this setting to allow positive and negative mass, which is necessary for representing imbalances such as deficits and surpluses in networks. The paper employs tools from harmonic analysis—particularly the structure of locally compact abelian groups—to define a global flatness regularizer derived from the continuum transport equation. Bi‑marginal constraints prescribe fixed source and target distributions, ensuring that the transport plan conserves the prescribed inflows and outflows at each node.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.17363">Conservation of Short-term Flows: Signed Optimal Transport</a></li>
<li><a href="https://arxiv.org/abs/2608.17363">[2608.17363] Conservation of Short-term Flows: Signed Optimal Transport</a></li>

</ul>
</details>

**Tags**: `#optimal transport`, `#signed measures`, `#harmonic analysis`, `#variational problem`, `#algorithmic scheme`

---

<a id="item-11"></a>
## [Generative AI adoption reduces demand for social skills in U.S. jobs](https://arxiv.org/abs/2503.09212) ⭐️ 8.0/10

Using seven million U.S. job postings from 595 firms that adopted generative AI in 2022‑2024, the study finds a 3.4% relative decline in demand for social skills while cognitive skill demand remained stable after ChatGPT’s launch. Challenges the prevailing view that AI shifts work toward social skills, showing instead that GenAI enables self‑service and reduces need for cross‑functional coordination, with implications for workforce training and job redesign. The analysis uses a difference‑in‑differences approach comparing adopting and non‑adopting roles around the ChatGPT launch, and notes the social‑skill decline is concentrated in non‑managerial positions and reflects added administrative tasks outside core functions.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: Generative AI refers to models like ChatGPT that can produce text, code, or other content, automating many cognitive tasks. Labor economists study how such automation changes the skill requirements expressed in job postings. The difference‑in‑differences (DID) method estimates causal effects by comparing changes over time between a treatment group (firms that adopted GenAI) and a control group (those that did not), controlling for common trends. This approach helps isolate the impact of AI adoption on skill demand from other economic fluctuations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>
<li><a href="https://www.weforum.org/publications/the-future-of-jobs-report-2025/">The Future of Jobs Report 2025 | World Economic Forum</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#labor economics`, `#skill demand`, `#job postings`, `#difference-in-differences`

---

<a id="item-12"></a>
## [Multi-view contrastive learning framework for spatial embeddings in risk modelling](https://arxiv.org/abs/2511.17954) ⭐️ 8.0/10

The paper introduces a multi-view contrastive learning framework that generates spatial embeddings by fusing satellite imagery and OpenStreetMap features across Europe, aligning these views with coordinate-based encodings. The resulting low-dimensional embeddings improve predictive accuracy in insurance risk models and can be generated directly from latitude‑longitude pairs. By turning raw geographic coordinates into informative spatial features, the method enhances underwriting precision and risk classification for insurers, while offering a transferable representation that works in regions without training data. This advances geospatial AI and provides a practical tool for integrating heterogeneous spatial data into predictive models. The framework was trained on a European dataset combining Sentinel‑2 satellite imagery and OSM tags, producing embeddings that boost performance of GLM, GAM, and gradient‑boosting models on French real‑estate prices and Belgian flood claims, while yielding interpretable spatial effects and generalizing to unseen locations. Embeddings can be extracted for any coordinate pair, eliminating the need to store or process the original satellite or map data during inference.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: Spatial embeddings convert complex geographic data such as satellite images and map tags into dense vectors that capture location‑based similarities for machine learning models. Contrastive learning learns these representations by encouraging similar views (e.g., satellite and OSM of the same place) to be close in embedding space while pushing dissimilar views apart. A multi‑view approach combines information from several data sources, and coordinate‑based encodings provide a way to condition the model on exact latitude‑longitude coordinates, enabling the embeddings to be queried directly from any georeferenced dataset.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2511.17954">A multi-view contrastive learning framework for spatial ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geographic_coordinate_system">Geographic coordinate system - Wikipedia</a></li>
<li><a href="https://www.openstreetmap.org/">OpenStreetMap</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#contrastive learning`, `#spatial embeddings`, `#risk modelling`, `#remote sensing`

---

<a id="item-13"></a>
## [This paper forecasts duration in high-frequency financial data using a self-exciting flexible residual point process.](https://arxiv.org/abs/2604.00346) ⭐️ 8.0/10

The paper introduces a self-exciting flexible residual point process model to forecast limit order book durations in ultra-high-frequency trading data, demonstrating strong predictive performance and establishing stochastic stability of the process. By combining a flexible residual distribution with self-exciting dynamics and proving stochastic stability, the model offers a robust tool for high-frequency trading analytics and advances point process methodology in finance. The model captures heavy-tailed interarrival times via flexible residuals while retaining the self-exciting and decay structure; under suitable conditions it is irreducible, aperiodic, positive Harris recurrent and admits a stationary distribution, and empirical tests show superior duration forecasts versus several baselines.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: In high-frequency trading, limit order books record the queue of buy and sell orders, and the time between successive events (durations) often exhibits heavy-tailed distributions, challenging conventional models. Self-exciting point processes capture the tendency of past events to increase the intensity of future events, and the proposed model extends this class by incorporating flexible residuals. Stochastic stability, analyzed via Harris chain theory and positive Harris recurrence, guarantees the existence of a stationary distribution and ensures predictable long‑term behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Harris_chain">Harris chain - Wikipedia</a></li>
<li><a href="https://link.springer.com/content/pdf/10.1007/978-3-031-11822-7_7.pdf?pdf=inline+link">Chapter 7 Harris and Positive Recurrence - Springer</a></li>
<li><a href="https://www.emergentmind.com/topics/self-exciting-flexible-residual-point-process">Self - Exciting Flexible Residual Point Process</a></li>

</ul>
</details>

**Tags**: `#high-frequency trading`, `#point processes`, `#limit order book`, `#stochastic stability`, `#forecasting`

---

<a id="item-14"></a>
## [Geometric BSDEs and Two-Driver BSDEs Introduced for Financial Applications](https://arxiv.org/abs/2405.09260) ⭐️ 8.0/10

The paper defines Geometric Backward Stochastic Differential Equations (GBSDEs) and two-driver BSDEs, reduces them to auxiliary ordinary BSDEs with logarithmic-singular quadratic growth y|ln(y)|+|z|^2/y to establish existence, regularity, uniqueness and stability, and applies the theory to stochastic differential utility portfolio optimization and dynamic return/star-shaped risk measures. By providing a rigorous framework for solving BSDEs with complex drivers under broad conditions, the work extends stochastic analysis tools to model multiplicative financial dynamics and risk measures, impacting both theory and practice in financial mathematics. The reduction uses auxiliary BSDEs with growth rate y|ln(y)|+|z|^2/y, allowing results for both bounded and unbounded driver coefficients and terminal conditions; the two-driver comparison theorem is used to prove optimality in stochastic differential utility portfolio optimization, and the theory characterizes positive homogeneity, star-shapedness and multiplicative convexity of dynamic return and star-shaped risk measures.

rss · arXiv Quantitative Finance · Aug 19, 04:00

**Background**: A backward stochastic differential equation (BSDE) is a stochastic differential equation with a terminal condition whose solution must be adapted to an underlying filtration. Geometric Brownian motion (GBM) models the multiplicative growth of asset prices, motivating the study of geometric BSDEs that arise naturally in dynamic return risk measures and recursive portfolio choice. Stochastic differential utility (SDU) extends recursive utility to continuous time, leading to portfolio optimization problems where the opportunity process satisfies an endogenously derived two-driver BSDE. Dynamic risk measures, such as L^p-norms and star-shaped measures, assess financial risk over time and can be represented via BSDEs under appropriate conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Backward_stochastic_differential_equation">Backward stochastic differential equation - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2405.09260">[2405.09260] Geometric BSDEs - arXiv.org Geometric BSDEs - arXiv.org (PDF) Geometric BSDEs - ResearchGate Geometric BSDEs - ADS Backward stochastic differential equation - Wikipedia Geometric BSDEs - IDEAS/RePEc Multi-dimensional Reflected Backward Stochastic Differential ...</a></li>
<li><a href="https://www.mdpi.com/2075-1680/13/6/354">One-Dimensional BSDEs with Jumps and Logarithmic Growth</a></li>

</ul>
</details>

**Tags**: `#BSDE`, `#stochastic calculus`, `#financial mathematics`, `#risk measures`, `#portfolio optimization`

---