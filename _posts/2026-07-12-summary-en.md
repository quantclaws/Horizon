---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 13 items, 2 important content pieces were selected

---

1. [vLLM v0.25.0 Release: Model Runner V2 Default, PagedAttention Removed](#item-1) ⭐️ 8.0/10
2. [UPI: Anatomy of a Payment Transaction](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0 Release: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models, removes the legacy PagedAttention implementation, and accelerates the Transformers backend to match native vLLM performance. It also adds support for several new models, introduces a unified streaming parser engine, and enables universal speculative decoding with heterogeneous vocabularies. This release represents a major architectural shift that simplifies the serving stack while boosting performance, making LLM inference more efficient and easier to deploy. The broadened model support and improved backend compatibility lower barriers for developers adopting vLLM in production. The release includes 558 commits from 232 contributors (64 new), introduces EVS, realtime embeddings, Mamba hybrid prefix caching, multimodal-prefix bidirectional attention, and dynamic speculative decoding compatible with full CUDA graphs. It also adds support for models such as LLaVA-OneVision-2, Unlimited OCR, MOSS-Transcribe-Diarize, openai/privacy-filter, Hy3, GLM-5/DeepSeek-V3.2, and MiniMax-M3 with pipeline parallelism and NVFP4.

github · khluu · Jul 11, 20:06

**Background**: vLLM is a high-throughput LLM serving engine that originally relied on PagedAttention to manage key-value cache memory efficiently. Model Runner V2 is an updated execution path that adds features like quantized-model support, EVS, and improved scheduling, and has now become the default for dense models. The Transformers backend, which allows vLLM to run models from the Hugging Face Transformers library, has been optimized to match the performance of vLLM's native kernels, enabling FP8 MoE and better CUDA graph integration.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/cuda_graphs/">CUDA Graphs - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#Model Runner V2`, `#PagedAttention removal`, `#Transformers backend`

---

<a id="item-2"></a>
## [UPI: Anatomy of a Payment Transaction](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

The article provides a step‑by‑step technical deep‑dive into the architecture and processing flow of a Unified Payments Interface (UPI) transaction in India. It highlights UPI’s engineering excellence, scalability and global relevance, sparking discussion about how its design could inform payment systems worldwide. The piece details the roles of NPCI’s central switch, issuer and acquirer banks, Payment Service Providers, and the use of Virtual Payment Addresses (VPAs), noting typical limits of ₹1 lakh per day and ~20 transactions per day, and mentions the recent outage caused by missing transaction‑status checks.

hackernews · prtk25 · Jul 11, 16:33 · [Discussion](https://news.ycombinator.com/item?id=48873457)

**Background**: Unified Payments Interface (UPI) is India’s real‑time payment system operated by the National Payments Corporation of India (NPCI), enabling instant bank‑to‑bank transfers via mobile apps using a Virtual Payment Address instead of bank details. Transactions flow through NPCI’s switch, which routes, validates and settles payments between issuer and acquirer banks, often mediated by PSPs such as Google Pay, PhonePe or Paytm. Settlement follows a hub‑based deferred net model, and the system handles billions of transactions annually.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://medium.com/@avinashkariya05910/deep-dive-system-design-of-upi-unified-payments-interface-eff3b0334b0d">Deep Dive: System Design of UPI (Unified Payments Interface) | by Avinash Kariya | Medium</a></li>
<li><a href="https://www.npci.org.in/PDF/npci/others/UPI-Settlement-Process.pdf">National Payments Corporation of India (NPCI) - Enabling digital payments in India</a></li>

</ul>
</details>

**Discussion**: Commenters praised UPI as a remarkable engineering achievement that brought digital payments to the masses, while some questioned its centralized, KYC‑dependent nature and compared it to Alipay/WeChat Pay. Others noted the transaction volume (~22 B yearly, ~700 QPS average) and recent outage causes, highlighting both strengths and areas for improvement.

**Tags**: `#UPI`, `#payment systems`, `#fintech`, `#software architecture`, `#India`

---