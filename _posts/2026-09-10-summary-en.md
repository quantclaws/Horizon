---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 23 items, 9 important content pieces were selected

---

1. [WeWorm: AI-assisted zero-click worm spreads via WeChat calls on iOS/Android](#item-1) ⭐️ 9.0/10
2. [vLLM v0.29.0 has been released with Model Runner V2 as default.](#item-2) ⭐️ 8.0/10
3. [Hugging Face Transformers v5.17.0 Adds Support for 780B‑Parameter Hy4‑Preview MoE Model](#item-3) ⭐️ 8.0/10
4. [Shopify acquires Tailwind CSS](#item-4) ⭐️ 8.0/10
5. [GPT-6 Astra Uses Looped Transformers for Hidden Reasoning](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 Shows Reasoning Prefills Similar to GPT-5.5 Pro](#item-6) ⭐️ 8.0/10
7. [How I Advertised Malware via Google Ads Exploiting Review Flaws](#item-7) ⭐️ 8.0/10
8. [Planet Labs Releases Open Satellite Feed Access Guide](#item-8) ⭐️ 8.0/10
9. [Analysis of Recent Large-Scale DDoS Attack on Read the Docs](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [WeWorm: AI-assisted zero-click worm spreads via WeChat calls on iOS/Android](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, a proof‑of‑concept zero‑click worm that propagates through WeChat voice calls on both iOS and Android without any user interaction. Using AI assistance, the team discovered the underlying bug and built the first remote‑code‑execution exploit in about two days, then completed the worm in another week. If accurate, WeWorm reveals a severe mobile‑security flaw that could let attackers hijack WeChat accounts en masse, demonstrating how AI can dramatically accelerate exploit development. This underscores an emerging threat landscape where AI‑assisted tools lower the barrier for creating sophisticated, zero‑click malware. The worm works even if the target does not answer the call; the victim hears nothing and the exploit still succeeds, achieving RCE via a WeChat voice‑call vulnerability. Calif’s team used AI to find the bug and write the exploit, providing only judgment on targeting and safe testing, and noted that Tencent later blocked the exploit.

rss · Simon Willison · Sep 10, 00:56

**Background**: Zero‑click exploits require no interaction from the victim and can compromise devices simply by receiving a malicious communication, such as a phone call or message. WeChat’s voice‑call feature processes incoming audio data before the user answers, providing an attack surface for memory‑corruption bugs that can lead to remote code execution. Recent trends show AI models assisting security researchers in vulnerability discovery, dramatically reducing the time needed to identify and weaponize flaws.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm - First 0-Click Worm Spreading Through WeChat Calls Across iOS and Android</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery">The First CVE Wave: Signs That AI-Assisted Vulnerability Discovery Is Reshaping Disclosure Volumes | Blog | VulnCheck</a></li>

</ul>
</details>

**Tags**: `#ai-security-research`, `#ai`, `#mobile-security`, `#zero-click`, `#wechat-vulnerability`

---

<a id="item-2"></a>
## [vLLM v0.29.0 has been released with Model Runner V2 as default.](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0 includes 594 commits from 277 contributors, makes Model Runner V2 the default inference engine, and adds support for new models such as Hy4-preview, Qwen3.8-Flash-Next, and GraniteSWA. It also brings performance enhancements like CUDA graph memory profiling for KV cache auto-sizing and batch-sharded sampling that reduces per-step logits memory. This release signals strong community activity and improves LLM serving efficiency by making the advanced Model Runner V2 the default, which reduces memory overhead and speeds up decoding. The expanded model support and performance optimizations benefit researchers and production users deploying large language models. Key technical additions include CUDA graph memory profiling for automatic KV cache sizing, batch-sharded sampling that cuts logits memory by 1/tensor parallelism, and prompt embeds support. Breaking changes remove ten deprecated model architectures and migrate several models to the Transformers backend, while the deprecated `python -m vllm.entrypoints.openai.api_server` entry point is replaced by `vllm serve`.

github · khluu · Sep 9, 08:54

**Background**: vLLM is an open-source library designed for high-throughput LLM inference, employing PagedAttention to manage key-value cache memory efficiently. Model Runner V2 (MRV2) is the next-generation inference runner that introduces features such as CUDA graph capture, dynamic KV cache sizing, and batch-sharded sampling to reduce memory footprint and improve latency. The release makes MRV2 the default for most models, marking a shift from the earlier MRV1 which remains used only for certain ROCm configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/configuration/conserving_memory/">Conserving Memory - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/v0.8.5/getting_started/examples/batch_llm_inference.html">Batch LLM Inference — vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#Model Runner V2`, `#release`, `#AI/ML`

---

<a id="item-3"></a>
## [Hugging Face Transformers v5.17.0 Adds Support for 780B‑Parameter Hy4‑Preview MoE Model](https://github.com/huggingface/transformers/releases/tag/v5.17.0) ⭐️ 8.0/10

The release v5.17.0 of the Hugging Face Transformers library adds support for the Hy4‑Preview 780B‑parameter mixture‑of‑experts language model, which activates 49B parameters per token and features Multi‑head Latent Attention, DeepSeek Sparse Attention, gated MLA with learnable attention sinks, and Independent Hyper‑Connections. It also introduces VibeVoice for multi‑speaker speech synthesis, NeoMME multimodal encoders, and Fun‑ASR‑Nano for multilingual speech recognition. This update enables researchers and developers to experiment with one of the largest open‑weight MoE models and novel attention mechanisms directly within the widely used Transformers library, lowering the barrier for scaling up LLM research and applications. Hy4‑Preview has 770B total parameters, 49B activated per token, a 1M‑token context window, 256 routed experts plus one shared expert per MoE layer, and routes each token to 8 experts; the implementation omits the multi‑token prediction layers but retains their weights for speculative decoding.

github · vasqu · Sep 9, 15:42

**Background**: Hugging Face Transformers is a popular open‑source library that provides pre‑trained models and tools for natural language processing, computer vision, and audio tasks. Mixture‑of‑Experts (MoE) layers increase model capacity by routing tokens to a subset of specialized expert networks, allowing massive models to be run with relatively low compute per token. Multi‑head Latent Attention compresses key/value states into a low‑rank representation to reduce memory bandwidth, while DeepSeek Sparse Attention selects a limited set of keys per query to cut computation. These techniques together enable efficient inference of very large language models such as the 780B‑parameter Hy4‑Preview.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/ Hy 4 - preview · Hugging Face</a></li>
<li><a href="https://medium.com/data-science/deepseek-v3-explained-1-multi-head-latent-attention-ed6bee2a67c4">DeepSeek-V3 Explained 1: Multi - head Latent Attention | Medium</a></li>
<li><a href="https://www.emergentmind.com/topics/deepseek-sparse-attention-dsa">DeepSeek Sparse Attention Mechanism ( DSA )</a></li>

</ul>
</details>

**Tags**: `#huggingface`, `#transformers`, `#release`, `#Mixture-of-Experts`, `#large language model`

---

<a id="item-4"></a>
## [Shopify acquires Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify announced the acquisition of Tailwind CSS, bringing the popular utility‑first CSS framework under its ownership. The move could shape the future of a widely‑used styling tool, affecting millions of web developers and influencing how e‑commerce platforms integrate frontend technologies. Tailwind CSS remains a utility‑first framework that provides classes like flex, pt‑4 and text‑center directly in HTML; the acquisition includes the Tailwind Labs team and brand, despite recent AI‑driven business challenges that cut documentation traffic by about 40%.

hackernews · EdwinHoksberg · Sep 9, 13:27 · [Discussion](https://news.ycombinator.com/item?id=49626190)

**Background**: Tailwind CSS is a utility‑first CSS framework that lets developers style applications by composing low‑level utility classes directly in markup, eliminating the need for custom CSS. It has gained widespread adoption in the web development community for rapid UI building and design consistency. Shopify is a leading e‑commerce platform that provides merchants with tools to create online stores and often integrates frontend technologies to enhance storefront customization.

<details><summary>References</summary>
<ul>
<li><a href="https://tailwindcss.com/">Tailwind CSS - Rapidly build modern websites without ever leaving...</a></li>
<li><a href="https://github.com/tailwindlabs/tailwindcss">GitHub - tailwindlabs/tailwindcss: A utility - first CSS framework for...</a></li>
<li><a href="https://www.npmjs.com/package/tailwindcss">tailwindcss - npm</a></li>

</ul>
</details>

**Discussion**: Commenters expressed sympathy for the Tailwind Labs team after AI‑related layoffs, while also congratulating the founders on a successful exit. Some questioned whether Tailwind remains necessary given modern CSS capabilities, and others hoped the acquisition would preserve educational resources like the Refactoring UI series. Overall, the discussion reflects both appreciation for the framework’s impact and uncertainty about its future direction under Shopify.

**Tags**: `#Shopify`, `#Tailwind CSS`, `#acquisition`, `#web development`, `#CSS framework`

---

<a id="item-5"></a>
## [GPT-6 Astra Uses Looped Transformers for Hidden Reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 8.0/10

Sebastian Raschka's recent article examines how the speculated GPT-6 Astra could employ looped transformers to achieve hidden reasoning in large language models, sparking debate on its feasibility. If realized, looped transformers could improve length generalization and reduce GPU memory usage while making model reasoning less transparent, affecting both AI safety and efficiency research. Looped transformers repeatedly apply a shared Transformer block, reusing weights to emulate deeper networks; hidden reasoning refers to internal computation that is not emitted as output, akin to "neuralese". The article notes the idea is speculative and not a confirmed breakthrough.

hackernews · ModelForge · Sep 9, 14:37 · [Discussion](https://news.ycombinator.com/item?id=49627370)

**Background**: Standard transformers process input with a fixed stack of layers; looping a transformer block allows the same weights to be applied multiple times, which can emulate arbitrary computation while saving memory. Hidden reasoning in LLMs describes reasoning steps that remain in internal states rather than being expressed in generated text, making them hard to monitor. Recent work links looped transformers to length generalization and proposes stochastic loop counts to improve robustness.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.15647">[2409.15647] Looped Transformers for Length Generalization GPT-6 Astra, Looped Transformers, and Hidden Reasoning [2301.13196] Looped Transformers as Programmable Computers GitHub - asimfish/awesome_loop_transformer: Awesome list ... GitHub - huskydoge/Awesome-Loop-Models: A curated list of ... OpenAI Astra and Looped Transformers | Sebastian Raschka, PhD What Is A Looped Transformer, Which OpenAI Is Using In Its ...</a></li>
<li><a href="https://arxiv.org/abs/2301.13196">[2301.13196] Looped Transformers as Programmable Computers GitHub - asimfish/awesome_loop_transformer: Awesome list ... GitHub - huskydoge/Awesome-Loop-Models: A curated list of ... OpenAI Astra and Looped Transformers | Sebastian Raschka, PhD What Is A Looped Transformer, Which OpenAI Is Using In Its ...</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and">GPT-6 Astra, Looped Transformers, and Hidden Reasoning</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about potential capabilities, cited works by Will Merrill on computational limits, and debated whether looped transformers truly hide reasoning or merely reuse weights; some viewed the idea as a memory-saving trick rather than a novel reasoning mechanism.

**Tags**: `#LLM`, `#transformers`, `#hidden reasoning`, `#GPT-6`, `#AI research`

---

<a id="item-6"></a>
## [Qwen 3.8 Shows Reasoning Prefills Similar to GPT-5.5 Pro](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 8.0/10

A Hacker News discussion highlights that Qwen 3.8 exhibits reasoning prefills that closely resemble those of GPT-5.5 Pro, suggesting possible distillation or shared training data. The similarity raises concerns about data leakage or unauthorized use of proprietary model outputs, which could affect trust in open-source models and influence future AI training practices. The discussion notes that Qwen 3.8 0902 was trained after August 10, 2024, when the stolen-thoughts paper exposing GPT-5.5 reasoning traces was released, making direct exposure possible.

hackernews · wsxiaoys · Sep 9, 17:24 · [Discussion](https://news.ycombinator.com/item?id=49630026)

**Background**: Reasoning prefills are initial tokens provided to a language model to guide its chain-of-thought output, a technique studied in recent papers on prefill awareness. Qwen is a family of open-source large language models developed by Alibaba Cloud, with Qwen 3.8-27B targeting coding and agentic tasks. GPT-5.5 Pro is OpenAI’s frontier model offering enhanced reasoning and token efficiency for professional workloads. Distillation refers to transferring knowledge from a larger, often proprietary model to a smaller open-source model by mimicking its outputs or internal representations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12747v1">Prefill Awareness in Large Language Models</a></li>
<li><a href="https://ollama.com/library/qwen3.8">qwen 3 . 8</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.5">GPT - 5 . 5 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the observed similarity stems from distillation, direct exposure to leaked reasoning traces, or coincidental training on similar benchmark solutions. Some highlighted techniques for recovering chain-of-thought outputs from proprietary models, while others questioned the accessibility of raw reasoning tokens. Overall, the discussion reflects curiosity about model provenance and caution about potential data leakage.

**Tags**: `#LLM`, `#reasoning`, `#distillation`, `#Qwen`, `#GPT-5.5`

---

<a id="item-7"></a>
## [How I Advertised Malware via Google Ads Exploiting Review Flaws](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 8.0/10

The author detailed a technique to bypass Google Ads' automated review and serve ads that delivered malware, later reporting that their ad account was reinstated after public outcry on Hacker News. This exposes a critical gap in Google's automated ad moderation that can be abused for large‑scale malvertising, endangering users and undermining trust in online advertising. The method relied on cloaking—showing harmless creatives and URLs to reviewers while redirecting real users to malicious landing pages—and the author noted that either a human review or a system trigger led to the account’s reinstatement.

hackernews · xlii · Sep 9, 11:43 · [Discussion](https://news.ycombinator.com/item?id=49624856)

**Background**: Google Ads subjects each ad to an automated review process where the ad status is “Under review” and any changes restart the review, with Google reserving the right to prioritize or re‑review ads to maintain system stability. Malvertisers often use cloaking techniques that present benign creatives and URLs to scanners while serving harmful content to users under certain conditions, effectively hiding malicious landing pages. Attackers abuse the ad network by exploiting these cloaking methods or compromised sites to evade policy enforcement, as documented in resources such as Google’s Advertising Policies Help and emerging cloaking platforms like 1Campaign.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/google-ads/answer/1722120?hl=en-WS">About the ad review process - Google Ads Help</a></li>
<li><a href="https://www.humansecurity.com/learn/blog/digital-disguise-understanding-cloakings-role-in-malvertising/">Digital Disguise: Understanding Cloaking's Role in Malvertising - HUMAN Security</a></li>
<li><a href="https://www.varonis.com/blog/1campaign">1Campaign: A New Cloaking Platform Helping Attackers Abuse ...</a></li>

</ul>
</details>

**Discussion**: Commenters criticized Google’s reliance on automated moderation, noting pervasive scam ads and the need for human oversight, while others pointed out that the author’s account was only restored after widespread online attention, echoing earlier incidents where compromised sites were used for malvertising.

**Tags**: `#Google Ads`, `#malvertising`, `#cybersecurity`, `#ad fraud`, `#online advertising`

---

<a id="item-8"></a>
## [Planet Labs Releases Open Satellite Feed Access Guide](https://tech.marksblogg.com/planet-labs-open-satellite-feed.html) ⭐️ 8.0/10

The blog post walks readers through accessing Planet Labs' open satellite feed using its API, STAC catalog, and Cloud Optimized GeoTIFF format, and includes community feedback on pricing, alternatives, and technical usability. By providing open access to high‑resolution, daily PlanetScope imagery, the feed lowers barriers for researchers, nonprofits, and developers to monitor environmental change and build geospatial applications. The feed delivers 3‑5 meter PlanetScope scenes as Cloud Optimized GeoTIFFs, accessible via the Planet API and a public STAC catalog, while community notes cite nonprofit pricing around $30 k per year for limited strips and mention alternatives such as Sentinel, Google Earth, and Nimbo imagery.

hackernews · marklit · Sep 9, 15:44 · [Discussion](https://news.ycombinator.com/item?id=49628429)

**Background**: Planet Labs operates a fleet of small satellites (Doves) that capture daily 3‑5 meter multispectral imagery of the Earth’s surface under the PlanetScope program. The company also provides higher‑resolution SkySat and legacy RapidEye data. To improve discoverability and interoperability, Planet publishes its datasets through a SpatioTemporal Asset Catalog (STAC) and distributes them as Cloud Optimized GeoTIFFs (COGs), which enable efficient partial retrieval over the web. These open data offerings allow users to access and analyze satellite imagery without needing to download large full scenes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.planet.com/">Planet Labs : Satellite Imagery & Earth Data Analytics</a></li>
<li><a href="https://www.planet.com/data/stac/browser/">Planet Labs - Open Data</a></li>
<li><a href="https://cogeo.org/">Cloud Optimized GeoTIFF</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a desire for more affordable pricing for nonprofit and conservation work, praised the blog’s practical, reproducible style, pointed to alternative sources like Sentinel, Google Earth, Nimbo, and the upcoming Mapterhorn PMtiles, and questioned whether Planet’s satellites are primarily serving the US surveillance contractor Flock.

**Tags**: `#satellite imagery`, `#open data`, `#geospatial`, `#remote sensing`, `#Planet Labs`

---

<a id="item-9"></a>
## [Analysis of Recent Large-Scale DDoS Attack on Read the Docs](https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/) ⭐️ 8.0/10

A recent large-scale DDoS attack targeted Read the Docs, bypassing Cloudflare defenses and raising suspicions of AI-driven tactics, as detailed in the platform's September 2026 blog post. The incident highlights evolving DDoS threats that can evade mainstream mitigation services and underscores the need for better legal and technical responses to protect critical open‑source documentation infrastructure. Attackers used a distributed botnet that evaded Cloudflare's L7 protections, prompting community speculation about AI‑orchestrated traffic and debates over whether enabling Cloudflare's 'Under Attack' mode could have mitigated the impact.

hackernews · davidfischer · Sep 9, 15:55 · [Discussion](https://news.ycombinator.com/item?id=49628614)

**Background**: Read the Docs is a widely used service that hosts versioned technical documentation for open‑source projects, relying on static content delivery and CDN caching. Distributed Denial‑of‑Service (DDoS) attacks flood a target with traffic from many sources to disrupt availability, with Layer 7 (application‑layer) attacks targeting web‑specific resources. While Cloudflare offers robust DDoS mitigation across network layers, its L7 defenses can be evaded by adaptive, AI‑driven traffic that mimics legitimate browser behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.a10networks.com/blog/the-machine-war-has-begun-cybercriminals-leveraging-ai-in-ddos-attacks/">AI DDoS Attacks : How Cybercriminals Use AI | A10 Networks</a></li>
<li><a href="https://www.intelligentciso.com/2026/09/01/cloudflare-ddos-threat-report-h1-2026-1-tbps-attacks-soar-as-dns-floods-and-geopolitical-tensions-drive-a-new-wave/">Cloudflare DDoS Threat Report H1 2026: 1 Tbps attacks soar as ...</a></li>

</ul>
</details>

**Discussion**: Commenters urged pursuing legal remedies against the attackers, including suing device manufacturers, while others questioned why Cloudflare's 'Under Attack' mode was not activated. Several speculated that the attack might be AI‑driven and possibly aimed at denying training data to competitors, and noted the ease with which the assault evaded L7 protections.

**Tags**: `#DDoS`, `#cybersecurity`, `#Cloudflare`, `#Read the Docs`, `#network security`

---