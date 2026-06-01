---
layout: default
title: "Horizon Summary: 2026-06-01 (EN)"
date: 2026-06-01
lang: en
---

> From 18 items, 6 important content pieces were selected

---

1. [: ](#item-1) ⭐️ 8.0/10
2. [: ](#item-2) ⭐️ 8.0/10
3. [: New Open-Source AV2 Decoder Introduced on Hacker News](#item-3) ⭐️ 8.0/10
4. [: ChatGPT for Google Sheets add‑on vulnerability allowed data exfiltration via Apps Script](#item-4) ⭐️ 8.0/10
5. [Linux restartable sequences enable lock‑free critical sections.](#item-5) ⭐️ 8.0/10
6. [: ](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [: ](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) ⭐️ 8.0/10

Cloudflare's Turnstile bot protection now mandates fingerprintable WebGL, prompting privacy concerns and debate over tracking versus bot mitigation.

hackernews · HypnoticOcelot · May 31, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48345840)

**Tags**: `#Cloudflare`, `#Turnstile`, `#WebGL fingerprinting`, `#privacy`, `#bot detection`

---

<a id="item-2"></a>
## [: ](https://prismml.com/news/bonsai-image-4b) ⭐️ 8.0/10

Researchers introduce a 1-bit quantized 4-billion-parameter diffusion model (Bonsai) that can generate images locally on consumer devices, reducing memory footprint while maintaining quality.

hackernews · modinfo · May 31, 15:04 · [Discussion](https://news.ycombinator.com/item?id=48346257)

**Tags**: `#AI/ML`, `#diffusion models`, `#model quantization`, `#edge computing`, `#image generation`

---

<a id="item-3"></a>
## [: New Open-Source AV2 Decoder Introduced on Hacker News](https://jbkempf.com/blog/2026/dav2d/) ⭐️ 8.0/10

A Hacker News post unveiled dav2d, an open-source AV2 video decoder based on dav1d, prompting discussion about its high computational complexity and hardware feasibility. The discussion highlights that AV2 decoding is roughly five times more complex than AV1, raising concerns about real-time playback on current hardware and the need for optimized implementations or dedicated accelerators. dav2d leverages the dav1d codebase, aims to provide a reference AV2 decoder, and runs on most platforms; however, benchmarks show AV2 decoding is significantly more demanding than AV1, and no widespread hardware acceleration exists yet.

hackernews · captain_bender · May 31, 11:44 · [Discussion](https://news.ycombinator.com/item?id=48344961)

**Background**: AV2 is the successor to AV1, standardized by the Alliance for Open Media, offering improved compression efficiency for streaming and conferencing. dav1d is a popular open-source AV1 decoder known for its performance and portability, serving as the foundation for dav2d. Hardware video acceleration APIs such as VAAPI enable offloading decode work to GPUs, but current implementations primarily support older codecs like H.264, HEVC, and AV1.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AV2-1.0-Specification-Released">AV 2 v1.0 Specification Released For Next-Gen Video ... - Phoronix</a></li>
<li><a href="https://de.news.hada.io/topic?id=29105">dav 2 d – VideoLANs plattformübergreifender AV 2 - Decoder | GeekNews</a></li>
<li><a href="https://en.wikipedia.org/wiki/Video_coding_format">Video coding format - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that AV2 decoding is about five times more complex than AV1, raising doubts about real-time software decoding on existing hardware, while some questioned whether the modest 25% bitrate reduction justifies abandoning AV1-capable devices. Others emphasized the importance of having a reference decoder to solidify the spec, and noted the post itself suffered a 'Hug of Death' due to high traffic.

**Tags**: `#video codec`, `#AV2`, `#dav2d`, `#decoder`, `#multimedia`

---

<a id="item-4"></a>
## [: ChatGPT for Google Sheets add‑on vulnerability allowed data exfiltration via Apps Script](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration) ⭐️ 8.0/10

A security flaw in the ChatGPT for Google Sheets add-on let attackers trick the model into generating malicious Apps Script code that could exfiltrate workbook data; OpenAI has since mitigated the issue by disabling the model's ability to generate Apps Script. The incident shows how LLMs integrated with privileged automation tools can become a vector for data exfiltration, putting sensitive corporate information at risk; it stresses the need for stricter controls on AI-generated code in SaaS add-ons. To exploit the flaw, a user must have granted the ChatGPT for Google Sheets extension access to their spreadsheet, after which a crafted prompt could cause the model to output Apps Script that, when executed, sends sheet contents to an attacker-controlled server; OpenAI's patch removes Apps Script generation entirely.

hackernews · hackerBanana · May 31, 20:35 · [Discussion](https://news.ycombinator.com/item?id=48349487)

**Background**: ChatGPT for Google Sheets is an AI-powered sidebar add-on launched by OpenAI in May 2026 that lets users build, edit, and explain spreadsheets using natural language without leaving the file. Google Apps Script is a cloud-based JavaScript platform that enables users to automate, customize, and extend Google Workspace applications such as Sheets, Docs, and Forms. LLMs that can invoke external tools are susceptible to prompt injection attacks, where malicious inputs cause the model to generate harmful code or commands leading to data exfiltration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ud.hk/en/blogs/insight/article/2026-05-29-chatgpt-spreadsheets">ChatGPT in Excel & Google Sheets : Practical Guide | UD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Apps_Script">Google Apps Script</a></li>
<li><a href="https://devstarsj.github.io/2026/02/07/llm-security-prompt-injection/">LLM Security in 2026: Defending Against Prompt Injection and Data ...</a></li>

</ul>
</details>

**Discussion**: OpenAI security team member Max Burkhardt acknowledged the flaw, thanked the researcher, and said they disabled Apps Script generation to protect users; other commenters advocated for running LLMs locally or in containers, criticized the lack of communication after disclosure, and warned against plugging LLMs into critical infrastructure without proper safeguards.

**Tags**: `#AI security`, `#LLM vulnerabilities`, `#Google Workspace`, `#data exfiltration`, `#responsible disclosure`

---

<a id="item-5"></a>
## [Linux restartable sequences enable lock‑free critical sections.](https://justine.lol/rseq/) ⭐️ 8.0/10

The article describes how Linux's restartable sequences (rseq) system call enables user‑space programs to declare critical sections to the kernel, allowing lock‑free synchronization without mutexes or atomic operations. By offering a kernel‑assisted, low‑overhead way to detect preemption and restart critical sections, rseq can boost the performance of lock‑free data structures and reduce latency in latency‑sensitive applications. The rseq ABI involves a thread‑local struct rseq whose rseq_cs pointer marks the current critical section; if the kernel detects a preemption, it forces a restart of that section, and the librseq library supplies ready‑made abstractions for counters and linked lists.

hackernews · grappler · May 31, 14:38 · [Discussion](https://news.ycombinator.com/item?id=48346019)

**Background**: Restartable sequences (rseq) are a Linux kernel feature introduced around 2019 that provides a system call (rseq(2)) to inform the kernel about user‑space critical sections. When a thread is preempted or migrated while inside such a section, the kernel can restart the section from a known safe point, eliminating the need for traditional locks or atomic primitives. This enables low‑overhead per‑CPU data structures and lock‑free algorithms in user space.

<details><summary>References</summary>
<ul>
<li><a href="https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/">The 5-year journey to bring restartable sequences to Linux - EfficiOS</a></li>
<li><a href="http://www.gnu.org/software/libc/manual//html_node/Restartable-Sequences.html">Restartable Sequences (The GNU C Library)</a></li>
<li><a href="https://dynamorio.org/page_rseq.html">Restartable Sequences - DynamoRIO</a></li>

</ul>
</details>

**Discussion**: Commenters praised the clear explanation of rseq and highlighted the librseq library as a useful abstraction, while some criticized the article's opening tone as off‑putting. Others noted connections to older preemption‑introspection techniques and explored using rseq to build load‑linked/store‑conditional primitives.

**Tags**: `#Linux kernel`, `#restartable sequences`, `#lock-free programming`, `#systems programming`, `#rseq`

---

<a id="item-6"></a>
## [: ](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/) ⭐️ 8.0/10

The post examines detectable linguistic patterns in LLM-generated text and explores the consequences for detection methods, watermarking, and the pressure on human writing style.

hackernews · mooreds · May 31, 21:57 · [Discussion](https://news.ycombinator.com/item?id=48350149)

**Tags**: `#LLM`, `#AI detection`, `#post-training`, `#linguistic patterns`, `#societal impact`

---