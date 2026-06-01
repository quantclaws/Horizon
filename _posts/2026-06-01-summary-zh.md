---
layout: default
title: "Horizon Summary: 2026-06-01 (ZH)"
date: 2026-06-01
lang: zh
---

> From 18 items, 6 important content pieces were selected

---

1. [Cloudflare Turnstile requiring fingerprintable WebGL](#item-1) ⭐️ 8.0/10
2. [1-Bit Bonsai Image 4B Image Generation for Local Devices](#item-2) ⭐️ 8.0/10
3. [Dav2d：Hacker News 上推出的开源 AV2 解码器](#item-3) ⭐️ 8.0/10
4. [ChatGPT for Google Sheets 插件漏洞导致通过 Apps Script 数据外泄](#item-4) ⭐️ 8.0/10
5. [Linux 重启序列使得无锁临界区成为可能。](#item-5) ⭐️ 8.0/10
6. [It's Not Just X. It's Y](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare Turnstile requiring fingerprintable WebGL](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) ⭐️ 8.0/10

Cloudflare's Turnstile bot protection now mandates fingerprintable WebGL, prompting privacy concerns and debate over tracking versus bot mitigation.

hackernews · HypnoticOcelot · May 31, 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48345840)

**标签**: `#Cloudflare`, `#Turnstile`, `#WebGL fingerprinting`, `#privacy`, `#bot detection`

---

<a id="item-2"></a>
## [1-Bit Bonsai Image 4B Image Generation for Local Devices](https://prismml.com/news/bonsai-image-4b) ⭐️ 8.0/10

Researchers introduce a 1-bit quantized 4-billion-parameter diffusion model (Bonsai) that can generate images locally on consumer devices, reducing memory footprint while maintaining quality.

hackernews · modinfo · May 31, 15:04 · [社区讨论](https://news.ycombinator.com/item?id=48346257)

**标签**: `#AI/ML`, `#diffusion models`, `#model quantization`, `#edge computing`, `#image generation`

---

<a id="item-3"></a>
## [Dav2d：Hacker News 上推出的开源 AV2 解码器](https://jbkempf.com/blog/2026/dav2d/) ⭐️ 8.0/10

一篇 Hacker News 帖子介绍了 dav2d，一个基于 dav1d 的开源 AV2 视频解码器，引发了关于其计算复杂度和硬件可行性的讨论。 讨论指出 AV2 解码大约比 AV1 复杂五倍，这引发了对当前硬件实时播放能力的担忧，凸显了对优化实现或专用加速器的需求。 dav2d 基于 dav1d 代码库，旨在提供 AV2 的参考解码器，可在多数平台运行；但基准测试表明 AV2 解码需求远高于 AV1，目前尚未有广泛的硬件加速方案。

hackernews · captain_bender · May 31, 11:44 · [社区讨论](https://news.ycombinator.com/item?id=48344961)

**背景**: AV2 是 AV1 的继承者，由开放媒体联盟标准化，提供更高的压缩效率，适用于流媒体和视频会议。dav1d 是一款广泛使用的开源 AV1 解码器，以其性能和可移植性著称，为 dav2d 提供了代码基础。硬件视频加速 API（如 VAAPI）可以将解码任务卸载到 GPU，但现有实现主要支持 H.264、HEVC 和 AV1 等较旧的编解码器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AV2-1.0-Specification-Released">AV 2 v1.0 Specification Released For Next-Gen Video ... - Phoronix</a></li>
<li><a href="https://de.news.hada.io/topic?id=29105">dav 2 d – VideoLANs plattformübergreifender AV 2 - Decoder | GeekNews</a></li>
<li><a href="https://en.wikipedia.org/wiki/Video_coding_format">Video coding format - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 AV2 解码大约比 AV1 复杂五倍，对现有硬件上的实时软件解码表示怀疑，同时有人质疑仅 25% 的比特率降低是否值得放弃支持 AV1 的设备。还有人强调拥有参考解码器对于确定规范的重要性，并指出该帖子因流量过大而出现了 'Hug of Death'。

**标签**: `#video codec`, `#AV2`, `#dav2d`, `#decoder`, `#multimedia`

---

<a id="item-4"></a>
## [ChatGPT for Google Sheets 插件漏洞导致通过 Apps Script 数据外泄](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration) ⭐️ 8.0/10

ChatGPT for Google Sheets 插件存在安全漏洞，攻击者可诱使模型生成恶意的 Apps Script 代码以窃取工作簿数据；OpenAI 已通过禁用模型生成 Apps Script 的功能来缓解此问题。 此事件表明，LLM 与具备特权的自动化工具集成时可能成为数据外泄的途径，危及敏感企业信息；这凸显了在 SaaS 插件中对 AI 生成代码施加更严格控制的必要性。 利用此漏洞需要用户先授予 ChatGPT for Google Sheets 扩展对其电子表格的访问权限，随后通过精心构造的提示使模型输出 Apps Script，执行后可将表格数据发送给攻击者控制的服务器；OpenAI 的补丁彻底移除了模型生成 Apps Script 的能力。

hackernews · hackerBanana · May 31, 20:35 · [社区讨论](https://news.ycombinator.com/item?id=48349487)

**背景**: ChatGPT for Google Sheets 是 OpenAI 在 2026 年 5 月推出的 AI 驱动的侧边栏插件，使用户能够在不离开文件的情况下用自然语言构建、编辑和解释电子表格。Google Apps Script 是一个基于云的 JavaScript 平台，使用户能够自动化、定制和扩展 Google Workspace 应用程序，如 Sheets、Docs 和 Forms。能够调用外部工具的大型语言模型容易受到提示注入攻击，恶意输入可能导致模型生成有害代码或命令，从而造成数据泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ud.hk/en/blogs/insight/article/2026-05-29-chatgpt-spreadsheets">ChatGPT in Excel & Google Sheets : Practical Guide | UD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Apps_Script">Google Apps Script</a></li>
<li><a href="https://devstarsj.github.io/2026/02/07/llm-security-prompt-injection/">LLM Security in 2026: Defending Against Prompt Injection and Data ...</a></li>

</ul>
</details>

**社区讨论**: OpenAI 安全团队成员 Max Burkhardt 承认了该漏洞，感谢研究者，并表示他们已禁用 Apps Script 生成以保护用户；其他评论者主张在本地或容器中运行 LLM，批评披露后缺乏沟通，并警告不要在没有适当防护的情况下将 LLM 接入关键基础设施。

**标签**: `#AI security`, `#LLM vulnerabilities`, `#Google Workspace`, `#data exfiltration`, `#responsible disclosure`

---

<a id="item-5"></a>
## [Linux 重启序列使得无锁临界区成为可能。](https://justine.lol/rseq/) ⭐️ 8.0/10

文章介绍了 Linux 的重启序列（rseq）系统调用如何让用户空间程序向内核声明临界区，从而在不使用互斥锁或原子操作的情况下实现无锁同步。 通过提供一种由内核辅助的低开销方式来检测抢占并重启临界区，rseq 能提升无锁数据结构的性能并降低延迟敏感应用的开销。 rseq ABI 通过线程局部存储中的 struct rseq 及其 rseq_cs 指针标记当前临界区；当内核检测到抢占时会强制重启该段代码，而 librseq 库则提供了计数器和链表等现成的封装。

hackernews · grappler · May 31, 14:38 · [社区讨论](https://news.ycombinator.com/item?id=48346019)

**背景**: 重启序列（rseq）是 Linux 内核在 2019 年左右引入的一项特性，提供了系统调用 rseq(2) 来向内核通知用户空间的临界区。当线程在该区域内被抢占或迁移时，内核可以将该段代码重新启动到一个已知的安全点，从而免去传统锁或原子操作的需求。这使得用户空间能够以低开销实现每 CPU 的数据结构和无锁算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/">The 5-year journey to bring restartable sequences to Linux - EfficiOS</a></li>
<li><a href="http://www.gnu.org/software/libc/manual//html_node/Restartable-Sequences.html">Restartable Sequences (The GNU C Library)</a></li>
<li><a href="https://dynamorio.org/page_rseq.html">Restartable Sequences - DynamoRIO</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章对 rseq 的清晰解释，并指出 librseq 库提供了有用的抽象；同时也有读者觉得文章开头的语气令人不适。还有人将其与较早的抢占内省技术联系起来，并讨论了用 rseq 实现 load‑linked/store‑conditional 原语的可能性。

**标签**: `#Linux kernel`, `#restartable sequences`, `#lock-free programming`, `#systems programming`, `#rseq`

---

<a id="item-6"></a>
## [It's Not Just X. It's Y](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/) ⭐️ 8.0/10

The post examines detectable linguistic patterns in LLM-generated text and explores the consequences for detection methods, watermarking, and the pressure on human writing style.

hackernews · mooreds · May 31, 21:57 · [社区讨论](https://news.ycombinator.com/item?id=48350149)

**标签**: `#LLM`, `#AI detection`, `#post-training`, `#linguistic patterns`, `#societal impact`

---