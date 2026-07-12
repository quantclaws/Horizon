---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 13 items, 2 important content pieces were selected

---

1. [vLLM v0.25.0 发布：Model Runner V2 成为默认，移除 PagedAttention](#item-1) ⭐️ 8.0/10
2. [UPI：支付交易的解剖](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0 发布：Model Runner V2 成为默认，移除 PagedAttention](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有密集模型的默认执行路径，移除了遗留的 PagedAttention 实现，并将 Transformers 后端提升至与原生 vLLM 相当的性能。此外，它还增加了多种新模型支持，引入了统一的流式解析引擎，并实现了支持异构词汇表的通用推测解码。 此次发布代表了一次主要的架构转变，既简化了服务又提升了性能，使得大语言模型推理更加高效且部署更简便。广泛的模型支持和后端兼容性提升降低了开发者在生产环境中采用 vLLM 的门槛。 此版本包含来自 232 名贡献者（其中 64 人为新贡献者）的 558 次提交，引入了 EVS、实时嵌入、Mamba 混合前缀缓存、多模态前缀双向注意力以及与完整 CUDA 图兼容的动态推测解码。新增对 LLaVA-OneVision-2、Unlimited OCR、MOSS-Transcribe-Diarize、openai/privacy-filter、Hy3、GLM-5/DeepSeek-V3.2 以及具备流水线并行和 NVFP4 的 MiniMax-M3 等模型的支持。

github · khluu · Jul 11, 20:06

**背景**: vLLM 是一种高吞吐的大语言模型服务引擎，最初依赖 PagedAttention 来高效管理键值缓存内存。Model Runner V2 是一种更新的执行路径，增加了量化模型支持、EVS 和改进的调度等功能，现已成为密集模型的默认路径。Transformers 后端使 vLLM 能够运行来自 Hugging Face Transformers 库的模型，经过优化后其性能已与 vLLM 原生内核相当，支持 FP8 MoE 和更好的 CUDA 图集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/cuda_graphs/">CUDA Graphs - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#Model Runner V2`, `#PagedAttention removal`, `#Transformers backend`

---

<a id="item-2"></a>
## [UPI：支付交易的解剖](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

该文章提供了对印度统一支付接口（UPI）交易架构和处理流程的逐步技术深度解析。 它凸显了 UPI 的工程卓越性、可扩展性和全球相关性，引发了关于其设计如何能够为全球支付系统提供借鉴的讨论。 文章详细说明了 NPCI 中央开关、发行和收单银行、支付服务提供方以及虚拟支付地址（VPA）的作用，指出典型的每日限额为 10 万卢比、每日约 20 笔交易，并提到最近一次因缺少交易状态检查导致的宕机。

hackernews · prtk25 · Jul 11, 16:33 · [社区讨论](https://news.ycombinator.com/item?id=48873457)

**背景**: 统一支付接口（UPI）是由印度国家支付公司（NPCI）运营的实时支付系统，通过移动应用使用虚拟支付地址（VPA）实现即时银行间转账。交易通过 NPCI 的开关进行路由、验证和结算，在发行银行和收单银行之间进行，通常由 Google Pay、PhonePe 或 Paytm 等支付服务提供方（PSP） mediating。结算采用基于中心的延迟净额模型，系统每年处理数十亿笔交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://medium.com/@avinashkariya05910/deep-dive-system-design-of-upi-unified-payments-interface-eff3b0334b0d">Deep Dive: System Design of UPI (Unified Payments Interface) | by Avinash Kariya | Medium</a></li>
<li><a href="https://www.npci.org.in/PDF/npci/others/UPI-Settlement-Process.pdf">National Payments Corporation of India (NPCI) - Enabling digital payments in India</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 UPI 是一项了不起的工程成就，让大众实现了数字支付；也有人质疑其集中式、依赖 KYC 的特点，并将其与支付宝/微信支付进行比较。还有人指出其交易量（约 220 亿笔/年，平均约 700 QPS）以及最近一次因缺少交易状态检查导致的宕机，突显了其优势与改进空间。

**标签**: `#UPI`, `#payment systems`, `#fintech`, `#software architecture`, `#India`

---