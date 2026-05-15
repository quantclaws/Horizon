---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 35 items, 15 important content pieces were selected

---

1. [vLLM v0.21.0 Released with C++20 Requirement, Transformers v4 Deprecation, and Blackwell Backend](#item-1) ⭐️ 8.0/10
2. [: ](#item-2) ⭐️ 8.0/10
3. [: First public macOS kernel memory corruption exploit on Apple M5](#item-3) ⭐️ 8.0/10
4. [:RTX 5090 eGPU boosts gaming and LLM on M4 MacBook Air.](#item-4) ⭐️ 8.0/10
5. [: New Nginx-Rift Exploit Enables Remote Code Execution](#item-5) ⭐️ 8.0/10
6. [: Hard Drive and SSD Firmware Obfuscation Found Trivial via Simple seccomp Trick](#item-6) ⭐️ 8.0/10
7. [arXiv Announces One-Year Ban for Hallucinated References](#item-7) ⭐️ 8.0/10
8. [: ](#item-8) ⭐️ 8.0/10
9. [:What's in a GGUF, besides the weights – and what's still missing?](#item-9) ⭐️ 8.0/10
10. [: ](#item-10) ⭐️ 8.0/10
11. [: MIT President Kornbluth Discusses Funding Challenges and Talent Pipeline](#item-11) ⭐️ 8.0/10
12. [:Yield Curves Dynamics Using Variational Autoencoders Under No-arbitrage](#item-12) ⭐️ 8.0/10
13. [:Modeling Electricity Price Volatility via SPDE-Driven Latent Process](#item-13) ⭐️ 8.0/10
14. [Enhancing a Risk Model by Adding Transient Statistical Factors](#item-14) ⭐️ 8.0/10
15. [: Extending Martingale Schrödinger Bridges to Arbitrary Dimensions](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 Released with C++20 Requirement, Transformers v4 Deprecation, and Blackwell Backend](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM version 0.21.0 introduces a breaking C++20 compiler requirement, deprecates support for transformers v4, adds KV offload integrated with the Hybrid Memory Allocator, enables speculative decoding that respects thinking budgets, and provides a new TOKENSPEED_MLA attention backend optimized for NVIDIA Blackwell GPUs. These changes affect a broad user base by requiring toolchain upgrades and migration to newer transformers, while delivering performance gains for reasoning models and Blackwell‑based hardware, positioning vLLM for next‑generation LLM serving workloads. The release includes 367 commits from 202 contributors (49 new), integrates KV offloading with Hybrid Memory Allocator via PRs #41228, #41445, #39571, adds thinking‑budget aware speculative decoding (#34668), and introduces the TOKENSPEED_MLA backend for Blackwell GPUs (#41778).

github · khluu · May 14, 23:15

**Background**: vLLM is a high‑throughput, memory‑efficient library for serving large language models, relying on CUDA and PyTorch for GPU acceleration. The Hybrid Memory Allocator (HMA) enables differentiated KV cache allocation for models that mix attention types, such as sliding‑window and full‑attention layers. NVIDIA Blackwell GPUs (SM100) introduce new architectural features that benefit from specialized attention kernels like TOKENSPEED_MLA. Speculative decoding accelerates generation by using a draft model, and respecting a thinking budget ensures correct handling of reasoning tokens in models that produce chain‑of‑thought output.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/issues/11382">[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm-project/vllm</a></li>
<li><a href="https://pypi.org/project/tokenspeed-mla/">Speed-of-light TokenSpeed MLA kernels for Blackwell SM100 and...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/reasoning_outputs/">Reasoning Outputs - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#transformers`, `#CUDA`, `#Blackwell`

---

<a id="item-2"></a>
## [: ](https://antirez.com/news/165) ⭐️ 8.0/10

Antirez introduces DwarfStar4, a lightweight LLM inference runtime for running DeepSeek 4 models with Metal, CUDA, and ROCm backends, sparking discussion on local model capabilities and AI trends.

hackernews · caust1c · May 14, 22:29 · [Discussion](https://news.ycombinator.com/item?id=48142108)

**Tags**: `#LLM`, `#inference`, `#DeepSeek`, `#Metal`, `#CUDA`

---

<a id="item-3"></a>
## [: First public macOS kernel memory corruption exploit on Apple M5](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 8.0/10

Researchers from Calif.io disclosed the first public macOS kernel memory corruption exploit targeting Apple's M5 silicon, detailing the vulnerability and its exploitation method. This marks the first publicly known kernel exploit against Apple's latest M5 chip, highlighting that even the newest silicon with advanced mitigations can be vulnerable to memory corruption attacks. The exploit demonstrates a local, unprivileged application can corrupt kernel memory, potentially bypassing MTE protections, and could lead to full system compromise if chained with other bugs.

hackernews · quadrige · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: macOS relies on the XNU kernel, which manages hardware and enforces security boundaries between user apps and the system. The Apple M5 is a system‑on‑chip built on TSMC’s 3nm N3P process, integrating CPU, GPU, NPU and unified memory, and includes hardware mitigations such as Memory Tagging Extension (MTE) to detect memory corruption. Kernel memory corruption vulnerabilities, when exploited, can allow attackers to execute arbitrary code with privileged access, undermining the isolation guarantees of the operating system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/">Apple unleashes M5, the next big leap in AI performance for Apple silicon - Apple</a></li>
<li><a href="https://www.linkedin.com/pulse/critical-macos-kernel-vulnerability-exposed-how-protect-qsifc">Critical macOS Kernel Vulnerability Exposed: How to Protect Your...</a></li>

</ul>
</details>

**Discussion**: Commenters congratulated the Calif team on the achievement while some questioned the lack of technical detail and speculated about the exploit’s value in Apple’s bug bounty program. Others expressed sarcasm, suggesting the vulnerability might be fabricated, and a few users regretted purchasing the M5 chip for its MIE feature. Overall, the discussion reflects both technical curiosity and cautious skepticism.

**Tags**: `#macOS`, `#kernel exploit`, `#Apple M5`, `#memory corruption`, `#security`

---

<a id="item-4"></a>
## [:RTX 5090 eGPU boosts gaming and LLM on M4 MacBook Air.](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

The author connected an RTX 5090 GPU to an M4 MacBook Air via a Thunderbolt 4 eGPU enclosure, then measured gaming frame rates and LLM prompt processing speeds while documenting the setup's limitations and workarounds. This demonstrates that high‑end NVIDIA graphics can be harnessed on Apple Silicon Macs, opening up better gaming and AI workloads on a platform that otherwise lacks native GPU support, and it highlights a practical workaround for developers and enthusiasts. The RTX 5090 provides 21,760 CUDA cores, 32 GB GDDR7 VRAM and ~105 TFLOPS FP32 performance, while the M4 MacBook Air offers a 10‑core CPU and an 8‑core GPU; benchmarks showed playable frame rates in titles that were unplayable on the integrated GPU and a noticeable speedup in LLM prefill, though the solution relies on third‑party drivers and is limited by power and driver maturity.

hackernews · allenleee · May 14, 15:47 · [Discussion](https://news.ycombinator.com/item?id=48137145)

**Background**: Apple discontinued official eGPU support when it transitioned to Apple Silicon, stating that only Intel‑based Macs can use external GPUs; the RTX 5090 is based on Nvidia’s Blackwell architecture with fourth‑gen RT cores and fifth‑gen Tensor Cores, delivering substantial compute and memory bandwidth; the M4 MacBook Air features a 10‑core CPU, 8‑core GPU and up to 24 GB unified memory, providing a capable host for an external GPU via Thunderbolt 4.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GeForce_RTX_50_series">GeForce RTX 50 series - Wikipedia</a></li>
<li><a href="https://support.apple.com/en-us/102363">Use an external graphics processor with your Mac - Apple Support</a></li>
<li><a href="https://support.apple.com/en-us/122209">MacBook Air (13-inch, M4, 2025) - Tech Specs - Apple Support</a></li>

</ul>
</details>

**Discussion**: Commenters praised the feat as impressive and noted that it overturns the belief that eGPUs do not work on Apple Silicon, while also pointing out remaining hurdles such as lack of OpenGL/Vulkan support, the need for driver tweaks, and the desire for Apple to provide better native support; several highlighted the LLM performance gains as the most practical benefit.

**Tags**: `#eGPU`, `#Apple Silicon`, `#RTX 5090`, `#gaming`, `#LLM performance`

---

<a id="item-5"></a>
## [: New Nginx-Rift Exploit Enables Remote Code Execution](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

A newly disclosed exploit named Nginx-Rift (CVE-2026-42945) achieves unauthenticated remote code execution on Nginx servers when a rewrite directive contains a question mark and a subsequent set directive references an unnamed capture group ($1). Nginx is one of the most widely deployed web servers, so this vulnerability poses a significant risk to countless websites and services unless mitigated or patched. The exploit uses cross‑request heap feng shui to corrupt an adjacent ngx_pool_t cleanup pointer, redirecting it to a fake ngx_pool_cleanup_s that invokes system() on pool destruction. It requires a rewrite rule containing a '?' and a set directive such as 'set $var $1'; the published proof‑of‑concept assumes ASLR is disabled, although the authors claim a reliable ASLR bypass exists.

hackernews · hetsaraiya · May 14, 17:17 · [Discussion](https://news.ycombinator.com/item?id=48138268)

**Background**: Nginx is a high‑performance, open‑source web server and reverse proxy that uses the ngx_http_rewrite_module to manipulate URIs based on regular expressions. Address Space Layout Randomization (ASLR) is a security feature that randomizes memory addresses to hinder exploitation of memory corruption bugs. Heap feng shui is an attacker technique that manipulates heap allocations to position controlled data adjacent to target structures, facilitating pointer corruption.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/depthfirstdisclosures/nginx-rift">GitHub - DepthFirstDisclosures/Nginx-Rift: exploit for CVE-2026-42945 · GitHub</a></li>
<li><a href="https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability">NGINX Rift: Achieving NGINX Remote Code Execution via an 18-Year-Old Vulnerability | depthfirst</a></li>
<li><a href="https://almalinux.org/blog/2026-05-13-nginx-rift-cve-2026-42945/">NGINX Rift (CVE-2026-42945): Patched nginx available in testing</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the exploit requires specific nginx rewrite configurations and, in the published PoC, assumes ASLR is disabled, though the writeup alleges a reliable ASLR bypass exists. Several users pointed out the mitigation of using named captures instead of unnamed ones in rewrite rules, as advised by F5. Others debated whether memory‑safe alternatives like Caddy or Jetty truly avoid similar issues, noting they have their own vulnerability histories.

**Tags**: `#nginx`, `#security vulnerability`, `#exploit`, `#web server`, `#CVE`

---

<a id="item-6"></a>
## [: Hard Drive and SSD Firmware Obfuscation Found Trivial via Simple seccomp Trick](https://icode4.coffee/?p=1465) ⭐️ 8.0/10

A discussion revealed that hard drive and SSD firmware obfuscation is weak, with a simple technique—using seccomp to block the rmdir system call—forcing vendor firmware update utilities to output decrypted firmware to disk, allowing easy extraction without reverse engineering the updater. This shows that storage device firmware protections are inadequate, exposing devices to potential tampering, data theft, or persistent malware implantation by attackers with modest resources. The technique leverages seccomp to deny the rmdir call made by firmware update scripts, causing them to fall back to writing decrypted firmware to a temporary file before upload; no cryptographic keys or complex exploits are needed.

hackernews · jsploit · May 14, 16:19 · [Discussion](https://news.ycombinator.com/item?id=48137553)

**Background**: Hard drive and SSD firmware is low‑level code that controls the device’s hardware and is often distributed in encrypted or obfuscated form to prevent tampering. seccomp is a Linux kernel feature that can restrict which system calls a process may make, commonly used for sandboxing containers. Vendors sometimes rely on simple obfuscation rather than strong encryption, assuming that blocking certain syscalls will hide the firmware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Seccomp">seccomp - Wikipedia</a></li>
<li><a href="https://louwersj.medium.com/how-linux-seccomp-strengthens-container-security-without-you-noticing-dca2c3cce5de">How Linux seccomp Strengthens Container Security ... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the obfuscation is trivial, pointing out that a seccomp block on rmdir yields decrypted firmware without reverse engineering. They referenced prior decompilations of Samsung SSD firmware, suggested data‑recovery shops likely already reverse‑engineer these drives, and linked to additional HDD‑firmware hacking articles.

**Tags**: `#firmware`, `#reverse-engineering`, `#security`, `#SSD`, `#HDD`

---

<a id="item-7"></a>
## [arXiv Announces One-Year Ban for Hallucinated References](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv will impose a one-year ban on submissions that contain hallucinated (AI‑fabricated) references and will require any future arXiv posting to first be accepted by a reputable peer‑reviewed venue. The policy tackles the rising problem of AI‑generated hallucinated citations that threaten scholarly integrity, aiming to deter careless use of language models in academic writing. The ban lasts one year; after the ban, authors must first secure acceptance at a peer‑reviewed venue before they can resubmit to arXiv. The policy is not yet reflected on arXiv’s help page, suggesting it may be planned but not live.

hackernews · gjuggler · May 14, 20:39 · [Discussion](https://news.ycombinator.com/item?id=48140922)

**Background**: arXiv is a widely used open‑access preprint server where researchers share early versions of scholarly papers before formal peer review. Hallucinated references are fabricated citations generated by AI language models that do not correspond to any real publication, undermining the reliability of scholarly work. Tools such as ref‑check.org have been developed to detect these false citations by cross‑checking against databases like Crossref and Semantic Scholar.

<details><summary>References</summary>
<ul>
<li><a href="https://ref-check.org/">ref-check.org — Academic Reference Verification Tool</a></li>
<li><a href="https://arxiv.org/pdf/2604.16407">26-19 How unique are hallucinated citations 2026-03-31</a></li>
<li><a href="https://writemask.com/blog/aigenerated-detect-or-detection-or-detector-or-text-or-literature-or-references-or-manuscript-or-academic-or-hallucination-or-paper-or-article">AI Hallucinations in Academic Papers : 7 Problems No... — WriteMask</a></li>

</ul>
</details>

**Discussion**: Commenters generally welcomed the policy as a step toward safeguarding scientific integrity, with btown calling it "incredibly good for science" though noting the rule is not yet visible on arXiv’s policy page. Others emphasized the need for better citation‑management tools (mks_shuffle) and urged careful vetting before imposing bans (MinimalAction), while rgmerk argued that authors who fail to verify LLM output should not expect readers to trust their work.

**Tags**: `#arXiv`, `#academic publishing`, `#AI hallucinations`, `#research integrity`, `#policy`

---

<a id="item-8"></a>
## [: ](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771) ⭐️ 8.0/10

Ontario auditors found that AI-powered medical note-taking systems routinely introduce factual errors, potentially endangering patient care.

hackernews · sohkamyung · May 14, 22:37 · [Discussion](https://news.ycombinator.com/item?id=48142188)

**Tags**: `#AI`, `#healthcare`, `#medical documentation`, `#hallucinations`, `#patient safety`

---

<a id="item-9"></a>
## [:What's in a GGUF, besides the weights – and what's still missing?](https://nobodywho.ooo/posts/whats-in-a-gguf/) ⭐️ 8.0/10

The article explores what data is stored in GGUF model files beyond the weights and discusses missing features such as an external model architecture definition. Understanding GGUF's internals helps developers optimize model deployment for llama.cpp‑based projects and highlights the need for a portable architecture description to improve cross‑model support. GGUF contains a header, metadata, and tensor data, supporting quantizations from 2‑bit to 8‑bit as well as float16, float32 and bfloat16, but currently lacks a standardized way to describe model architecture outside the code.

hackernews · bashbjorn · May 14, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48138332)

**Background**: GGUF is a binary file format created for llama.cpp and based on the GGML tensor library, designed to store model weights and metadata in a single file for fast loading and efficient inference. It supports a variety of data types, including low‑bit integer quantizations and common floating‑point formats, enabling deployment across CPUs, GPUs and other hardware backends. While similar to safetensors in its ability to bundle extra data, GGUF is preferred by ggml‑based executors because of its tight integration with the GGML runtime.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>
<li><a href="https://apxml.com/courses/practical-llm-quantization/chapter-5-quantization-formats-tooling/gguf-format">GGUF File Format Explained (llama.cpp)</a></li>
<li><a href="https://huggingface.co/docs/hub/gguf">GGUF · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters noted that projection data is currently stored in separate files, contrary to GGUF’s original single‑file ethos, and expressed a desire to reunite them. They also praised GGML/GGUF for enabling cross‑platform projects like llama.cpp and whisper.cpp, while emphasizing that the biggest missing feature is an external, vendor‑validated way to define model architecture, possibly via a DSL.

**Tags**: `#GGUF`, `#llama.cpp`, `#model format`, `#ML infrastructure`, `#open-source AI`

---

<a id="item-10"></a>
## [: ](https://github.com/oven-sh/bun/pull/30412) ⭐️ 8.0/10

Bun's JavaScript runtime has been rewritten in Rust, merging a PR that adds over 1 million lines of Rust code.

hackernews · Chaoses · May 14, 08:15 · [Discussion](https://news.ycombinator.com/item?id=48132488)

**Tags**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#language rewrite`, `#open-source`

---

<a id="item-11"></a>
## [: MIT President Kornbluth Discusses Funding Challenges and Talent Pipeline](https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline) ⭐️ 8.0/10

MIT President Sally Kornbluth issued a message addressing funding challenges and the talent pipeline for PhD graduates, sparking discussion on Hacker News. The message highlights growing concerns about research funding and PhD career prospects, affecting academia and the broader STEM workforce. The message notes that the median science PhD takes six years, pay is low, job prospects are difficult, and many recent PhD graduates consider leaving academia.

hackernews · dmayo · May 14, 14:51 · [Discussion](https://news.ycombinator.com/item?id=48136262)

**Background**: MIT is a premier research university in the United States, known for strong STEM programs and significant federal research funding. Recent years have seen fluctuations in grant availability and increasing scrutiny of PhD outcomes. The talent pipeline refers to the flow of doctoral graduates into academic or industry positions.

**Discussion**: Commenters expressed mixed views, with many noting disillusionment among PhD graduates, concerns about long training periods and poor pay, while others argued that PhD value extends beyond academia, especially in fields like nanofabrication. Some also pointed to broader systemic issues and potential shifts in global education leadership.

**Tags**: `#academia`, `#research-funding`, `#PhD`, `#talent-pipeline`, `#MIT`

---

<a id="item-12"></a>
## [:Yield Curves Dynamics Using Variational Autoencoders Under No-arbitrage](https://arxiv.org/abs/2605.12764) ⭐️ 8.0/10

The paper introduces a two-stage architecture: a Student‑t Conditional Variational Autoencoder with Dynamic Level Injection (CVAEsT+LS) that learns a heavy‑tailed term‑structure manifold, followed by a continuous‑time Neural Stochastic Differential Equation (SDE) whose dynamics are penalized by a No‑Arbitrage PDE. Empirical tests on USD, GBP, and JPY yield curves show a 6.58 bps mean tenor RMSE, markedly outperforming the classical HJM model. By enforcing no‑arbitrage constraints within a deep generative framework, the method resolves the manifold collapse and arbitrage violations that plague standard models when forecasting term structures across diverse macroeconomic regimes. This advance offers a scalable, mathematically sound tool for fixed‑income pricing, risk management, and scenario generation, bridging machine learning flexibility with financial theory. The first stage employs a Student‑t likelihood to capture heavy‑tailed shocks and a dynamic level injection term to separate macro‑driven shape movements from absolute rate levels. The second stage models latent dynamics with a Neural SDE whose loss includes a penalty derived from the Heath‑Jarrow‑Morton (HJM) no‑arbitrage PDE, ensuring generated paths remain arbitrage‑free. Experiments demonstrate superior regime detection via phase‑space vector field analysis and high‑quality continuous‑time scenario generation.

rss · arXiv Quantitative Finance · May 14, 04:00

**Background**: Yield curves represent the relationship between bond yields and maturities, and their dynamics are central to fixed‑income pricing and risk management. Modeling them requires capturing complex, heavy‑tailed movements while respecting no‑arbitrage conditions that prevent risk‑free profit opportunities. Variational autoencoders are flexible generative models that can learn low‑dimensional manifolds from high‑dimensional data, but they often suffer from manifold collapse when applied to financial time series. Stochastic differential equations (SDEs) provide a continuous‑time framework for evolving latent states, and imposing no‑arbitrage PDE constraints helps ensure the generated paths are financially plausible.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.12764">Yield Curves Dynamics Using Variational Autoencoders Under...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variational_autoencoder">Variational autoencoder - Wikipedia</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/1350486X.2023.2257217">Arbitrage-Free Neural-SDE Market Models - Taylor & Francis</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#variational autoencoder`, `#finance`, `#yield curve modeling`, `#no-arbitrage`

---

<a id="item-13"></a>
## [:Modeling Electricity Price Volatility via SPDE-Driven Latent Process](https://arxiv.org/abs/2605.13320) ⭐️ 8.0/10

The paper models day-ahead electricity prices as local averages of a latent stochastic partial differential equation (SPDE) process to estimate weekly integrated variance and compare volatility drivers across Germany, Norway, and Spain. It provides the first rigorous SPDE-based analysis of electricity price volatility for a multi‑zone European panel, offering a new methodological tool for energy finance and risk management. The estimators incorporate mean‑reversion and semigroup‑smoothing effects, and a detailed decomposition reveals that each zone’s volatility drivers differ markedly, with apparent leverage effects disappearing once state variables are conditioned upon.

rss · arXiv Quantitative Finance · May 14, 04:00

**Background**: Electricity price volatility refers to the fluctuations of day‑ahead market prices, which are crucial for trading and risk assessment in energy finance. Modeling these prices as local averages of a latent SPDE‑driven process captures spatial and temporal dependencies inherent in power grids. Semigroup smoothing, a property of certain operators that regularizes estimates, must be accounted for when deriving variance estimators in this infinite‑dimensional setting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/2601235_Exact_Smoothing_Properties_of_Schrodinger_Semigroups">(PDF) Exact Smoothing Properties of Schrödinger Semigroups</a></li>

</ul>
</details>

**Tags**: `#electricity markets`, `#stochastic partial differential equations`, `#volatility estimation`, `#energy finance`, `#European energy zones`

---

<a id="item-14"></a>
## [Enhancing a Risk Model by Adding Transient Statistical Factors](https://arxiv.org/abs/2605.12977) ⭐️ 8.0/10

The paper proposes a maximum likelihood estimation (MLE) method to refine existing factor risk models and add transient statistical factors, using only observed returns and two hyperparameters: the number of extra factors and a half‑life weighting parameter. By capturing changing market regimes and transient influences that standard factor models miss, the approach can improve portfolio risk estimation and potentially enhance investment performance for equity investors. The method requires choosing the number of additional factors and a half‑life parameter that weights recent returns more heavily in the log‑likelihood, and it handles missing returns, making it applicable to typical equity datasets; it was tested on the Barra short‑term US risk model for large‑cap US stocks.

rss · arXiv Quantitative Finance · May 14, 04:00

**Background**: Factor risk models decompose asset return variability into a small set of common factors and asset‑specific idiosyncratic risk, providing a parsimonious view of portfolio risk. Maximum likelihood estimation is a statistical technique that selects model parameters making the observed data most probable under an assumed distribution. Transient factors are short‑lived sources of risk that arise from shifting market regimes and are often omitted from static factor models supplied by vendors such as Barra.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Maximum_likelihood_estimation">Maximum likelihood estimation - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0304407620303894">Maximum likelihood estimation and inference for high dimensional ...</a></li>
<li><a href="https://economics.yale.edu/sites/default/files/bai-121017.pdf">[PDF] Maximum likelihood estimation and inference for approximate factor ...</a></li>

</ul>
</details>

**Tags**: `#risk modeling`, `#factor models`, `#maximum likelihood`, `#finance`, `#statistical learning`

---

<a id="item-15"></a>
## [: Extending Martingale Schrödinger Bridges to Arbitrary Dimensions](https://arxiv.org/abs/2604.01299) ⭐️ 8.0/10

The paper shows that the martingale Schrödinger bridge introduced by Nutz and Wiesel extends naturally to arbitrary dimension. It identifies the continuous‑time counterpart as the minimizer of a weighted quadratic energy, proves its coincidence with the Föllmer martingale in the irreducible case, and relates it to the dual formulation of weak optimal transport. By linking the martingale Schrödinger bridge to the Föllmer martingale and weak optimal transport, the work unifies concepts from stochastic analysis, optimal transport, and mathematical finance. This provides a rigorous framework for constructing martingale transport plans that can be used for model calibration and risk‑sensitive applications. The authors prove that the martingale Schrödinger bridge exists in any dimension and can be characterized as the continuous martingale with prescribed marginals minimizing a weighted quadratic deviation from Brownian motion. In the irreducible case this bridge coincides with the Föllmer martingale, and more generally it is linked to a variational problem over base measures and to the dual formulation of weak optimal transport.

rss · arXiv Quantitative Finance · May 14, 04:00

**Background**: The classical Schrödinger bridge seeks a stochastic process with given marginals that minimizes relative entropy to a reference process, often Brownian motion. The martingale Schrödinger bridge, introduced by Nutz and Wiesel, restricts this problem to martingale transports between probability measures in convex order. The Föllmer martingale is the Doob martingale associated with a Föllmer process and appears in minimal martingale measures for incomplete markets. Weak optimal transport generalizes classical optimal transport by allowing costs that depend on conditional laws, leading to dual formulations involving base measures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.01299v1">Bridging classical and martingale Schrödinger bridges</a></li>
<li><a href="https://www.emergentmind.com/topics/follmer-measures">Föllmer Measures in Stochastic Analysis</a></li>
<li><a href="https://www.emergentmind.com/topics/weak-optimal-transport">Weak Optimal Transport Overview</a></li>

</ul>
</details>

**Tags**: `#optimal transport`, `#martingale theory`, `#Schrödinger bridge`, `#stochastic processes`, `#mathematical finance`

---