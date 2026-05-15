---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 35 items, 15 important content pieces were selected

---

1. [vLLM v0.21.0 发布，要求 C++20，弃用 transformers v4，新增 Blackwell 后端](#item-1) ⭐️ 8.0/10
2. [A few words on DS4](#item-2) ⭐️ 8.0/10
3. [首次公开的苹果 M5 内核内存损坏利用](#item-3) ⭐️ 8.0/10
4. [RTX 5090 外接显卡提升 M4 MacBook Air 游戏与 LLM 性能。](#item-4) ⭐️ 8.0/10
5. [新型 Nginx-Rift 漏洞实现远程代码执行](#item-5) ⭐️ 8.0/10
6. [硬盘和 SSD 固件混淆被发现通过简单的 seccomp 技巧变得微不足道](#item-6) ⭐️ 8.0/10
7. [arXiv 宣布对 hallucinated references 实施一年禁令](#item-7) ⭐️ 8.0/10
8. [Ontario auditors find doctors' AI note takers routinely blow basic facts](#item-8) ⭐️ 8.0/10
9. [GGUF 中除了权重还有什么，以及仍缺少什么？](#item-9) ⭐️ 8.0/10
10. [Rewrite Bun in Rust has been merged](#item-10) ⭐️ 8.0/10
11. [MIT 校长科恩布拉斯讨论资金挑战与人才管道](#item-11) ⭐️ 8.0/10
12. [使用变分自编码器在无套利条件下的收益曲线动态建模](#item-12) ⭐️ 8.0/10
13. [SPDE 驱动的电价波动建模](#item-13) ⭐️ 8.0/10
14. [通过添加暂时统计因子增强风险模型](#item-14) ⭐️ 8.0/10
15. [: 将马尔廷格尔薛定谔桥推广到任意维度](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 发布，要求 C++20，弃用 transformers v4，新增 Blackwell 后端](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM 0.21.0 版本引入了强制 C++20 编译器要求，弃用 transformers v4 支持，增加了与 Hybrid Memory Allocator 集成的 KV 卸载功能，支持考虑思考预算的推测解码，并提供了针对 NVIDIA Blackwell GPU 的新 TOKENSPEED_MLA 注意力后端。 这些更改影响广泛用户，需要升级工具链并迁移到较新的 transformers，同时为推理模型和 Blackwell 硬件带来性能提升，使 vLLM 能更好地服务于下一代 LLM 工作负载。 此版本包含 367 次提交，来自 202 名贡献者（其中 49 人为新贡献者），通过 PR #41228、#41445、#39571 将 KV 卸载与 Hybrid Memory Allocator 集成，加入了考虑思考预算的推测解码（#34668），并发布了针对 Blackwell GPU 的 TOKENSPEED_MLA 后端（#41778）。

github · khluu · May 14, 23:15

**背景**: vLLM 是一个高吞吐、内存高效的大型语言模型服务库，依赖 CUDA 和 PyTorch 进行 GPU 加速。混合内存分配器（HMA）能够为混合注意力类型的模型（如滑动窗口和全注意力层）提供不同的 KV 缓存分配。NVIDIA Blackwell GPU（SM100）引入了新的架构特性，可从专用注意力内核如 TOKENSPEED_MLA 中受益。推测解码通过使用草稿模型来加速生成，而尊重思考预算则确保了对产生思维链输出的模型中推理令牌的正确处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/issues/11382">[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm-project/vllm</a></li>
<li><a href="https://pypi.org/project/tokenspeed-mla/">Speed-of-light TokenSpeed MLA kernels for Blackwell SM100 and...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/reasoning_outputs/">Reasoning Outputs - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#transformers`, `#CUDA`, `#Blackwell`

---

<a id="item-2"></a>
## [A few words on DS4](https://antirez.com/news/165) ⭐️ 8.0/10

Antirez introduces DwarfStar4, a lightweight LLM inference runtime for running DeepSeek 4 models with Metal, CUDA, and ROCm backends, sparking discussion on local model capabilities and AI trends.

hackernews · caust1c · May 14, 22:29 · [社区讨论](https://news.ycombinator.com/item?id=48142108)

**标签**: `#LLM`, `#inference`, `#DeepSeek`, `#Metal`, `#CUDA`

---

<a id="item-3"></a>
## [首次公开的苹果 M5 内核内存损坏利用](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 8.0/10

来自 Calif.io 的研究人员披露了首个针对苹果 M5 硅片的公开 macOS 内核内存损坏利用，详细说明了该漏洞及其利用方法。 这标志着首次公开的针对苹果最新 M5 芯片的内核利用凸显，即便是具有先进缓解措施的最新硅片也可能受到内存损坏攻击的威胁。 该利用表明一个本地非特权应用程序可以损坏内核内存，可能绕过 MTE 保护，并在与其他漏洞链式使用时导致完全系统被攻破。

hackernews · quadrige · May 14, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48139219)

**背景**: macOS 依赖 XNU 内核来管理硬件并在用户应用与系统之间强制执行安全边界。苹果 M5 是基于台积电 3nm N3P 工艺的系统级芯片，集成了 CPU、GPU、NPU 和统一内存，并包含诸如内存标记扩展（MTE）之类的硬件缓解措施以检测内存损坏。内核内存损坏漏洞若被利用，可让攻击者获得特权执行任意代码的能力，从而破坏操作系统的隔离保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/">Apple unleashes M5, the next big leap in AI performance for Apple silicon - Apple</a></li>
<li><a href="https://www.linkedin.com/pulse/critical-macos-kernel-vulnerability-exposed-how-protect-qsifc">Critical macOS Kernel Vulnerability Exposed: How to Protect Your...</a></li>

</ul>
</details>

**社区讨论**: 评论者祝贺 Calif 团队的成就，但也有人质疑技术细节的缺失并猜测该利用在苹果漏洞赏金计划中的价值。部分用户讽刺性地认为该漏洞可能是被捏造的，还有人 lamented 购买 M5 仅为了其 MIE 特性。总体而言，讨论表现出技术好奇心和审慎怀疑的混合情绪。

**标签**: `#macOS`, `#kernel exploit`, `#Apple M5`, `#memory corruption`, `#security`

---

<a id="item-4"></a>
## [RTX 5090 外接显卡提升 M4 MacBook Air 游戏与 LLM 性能。](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

作者通过雷电 4 外接显卡盒将 RTX 5090 GPU 连接到 M4 MacBook Air，随后测量了游戏帧率和 LLM 提示处理速度，并记录了设置的限制和变通方案。 这表明高端 NVIDIA 显卡可以在 Apple Silicon Mac 上被利用，为原本缺乏原生 GPU 支持的平台带来更好的游戏和 AI 工作负载，并为开发者和爱好者提供了一种实用的变通方案。 RTX 5090 提供 21,760 个 CUDA 核心、32 GB GDDR7 显存以及约 105 TFLOPS 的 FP32 性能，而 M4 MacBook Air 配备 10 核 CPU 和 8 核 GPU；基准测试显示，在原本无法使用集成 GPU 运行的游戏中可以获得可玩的帧率，LLM 的预填充速度也有明显提升，但该方案依赖第三方驱动，并受功率和驱动成熟度的限制。

hackernews · allenleee · May 14, 15:47 · [社区讨论](https://news.ycombinator.com/item?id=48137145)

**背景**: Apple 在转向 Apple Silicon 时停止了官方 eGPU 支持，称只有基于 Intel 的 Mac 才能使用外部 GPU；RTX 5090 基于 Nvidia 的 Blackwell 架构，具备第四代 RT 核心和第五代 Tensor 核心，提供巨大的计算和内存带宽；M4 MacBook Air 配备 10 核 CPU、8 核 GPU 和最高 24 GB 统一内存，通过雷电 4 为外部 GPU 提供了有能力的宿主。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GeForce_RTX_50_series">GeForce RTX 50 series - Wikipedia</a></li>
<li><a href="https://support.apple.com/en-us/102363">Use an external graphics processor with your Mac - Apple Support</a></li>
<li><a href="https://support.apple.com/en-us/122209">MacBook Air (13-inch, M4, 2025) - Tech Specs - Apple Support</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这一成就令人印象深刻，认为它推翻了 eGPU 在 Apple Silicon 上不可用的看法，同时也指出仍存在的障碍，如 OpenGL/Vulkan 支持不足、需要驱动调整，以及希望 Apple 提供更好的原生支持；几位评论者强调 LLM 性能提升是最具实际价值的好处。

**标签**: `#eGPU`, `#Apple Silicon`, `#RTX 5090`, `#gaming`, `#LLM performance`

---

<a id="item-5"></a>
## [新型 Nginx-Rift 漏洞实现远程代码执行](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

新披露的名为 Nginx-Rift（CVE-2026-42945）的漏洞，在 Nginx 配置中出现包含问号的 rewrite 指令，随后使用 set 指引用未命名捕获组（如 $1）时，可实现未经身份验证的远程代码执行。 Nginx 是全球部署最广的 Web 服务器之一，此漏洞若未及时修复或缓解，将对大量网站和服务构成严重威胁。 该漏洞利用跨请求堆喷射技术破坏相邻的 ngx_pool_t 清理指针，将其指向伪造的 ngx_pool_cleanup_s 以在池销毁时调用 system()。利用前提是配置中存在包含问号的 rewrite 指令以及形如 set $var $1 的 set 指引；公开的 PoC 假设 ASLR 已关闭，但作者宣称存在可靠的 ASLR 绕过方法。

hackernews · hetsaraiya · May 14, 17:17 · [社区讨论](https://news.ycombinator.com/item?id=48138268)

**背景**: Nginx 是一种高性能的开源 Web 服务器和反向代理，其 ngx_http_rewrite_module 通过正则表达式来重写请求 URI。地址空间布局随机化（ASLR）是一项安全机制，通过随机化进程的内存布局来增加利用内存损坏漏洞的难度。堆喷射（heap feng shui）是攻击者用来精准控制堆布局，使攻击数据靠近关键结构体以实现指针劫持的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/depthfirstdisclosures/nginx-rift">GitHub - DepthFirstDisclosures/Nginx-Rift: exploit for CVE-2026-42945 · GitHub</a></li>
<li><a href="https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability">NGINX Rift: Achieving NGINX Remote Code Execution via an 18-Year-Old Vulnerability | depthfirst</a></li>
<li><a href="https://almalinux.org/blog/2026-05-13-nginx-rift-cve-2026-42945/">NGINX Rift (CVE-2026-42945): Patched nginx available in testing</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该漏洞利用需要特定的 Nginx rewrite 配置，且公开的 PoC 假设 ASLR 已关闭，尽管作者声称存在可靠的 ASLR 绕过方法。多位用户提到 F5 建议的缓解措施——在 rewrite 规则中使用命名捕获而非未命名捕获（如 $user_id、$section）来替代 $1、$2。还有人讨论使用内存安全语言编写的替代方案（如 Caddy、Jetty）是否真的更安全，指出它们也有其他类型的漏洞历史。

**标签**: `#nginx`, `#security vulnerability`, `#exploit`, `#web server`, `#CVE`

---

<a id="item-6"></a>
## [硬盘和 SSD 固件混淆被发现通过简单的 seccomp 技巧变得微不足道](https://icode4.coffee/?p=1465) ⭐️ 8.0/10

讨论显示，硬盘和 SSD 固件的混淆非常脆弱，仅需使用 seccomp 阻止 rmdir 系统调用，就能迫使厂商固件更新工具将解密后的固件写入磁盘，从而轻松获取固件而无需逆向更新程序。 这表明存储设备固件保护不足，可能导致设备被篡改、数据盗窃或持久性恶意植入，即使攻击者资源有限也能利用。 该技术利用 seccomp 拒绝固件更新脚本中的 rmdir 调用，迫使其在上传前将解密固件写入临时文件，无需破解加密密钥或复杂利用。

hackernews · jsploit · May 14, 16:19 · [社区讨论](https://news.ycombinator.com/item?id=48137553)

**背景**: 硬盘和 SSD 固件是控制设备硬件的底层代码，通常以加密或混淆形式发布以防止篡改。seccomp 是 Linux 内核的一项安全特性，能够限制进程可使用的系统调用，常用于容器沙箱。一些厂商仅依赖简单的混淆而非强加密，认为阻塞特定系统调用即可隐藏固件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Seccomp">seccomp - Wikipedia</a></li>
<li><a href="https://louwersj.medium.com/how-linux-seccomp-strengthens-container-security-without-you-noticing-dca2c3cce5de">How Linux seccomp Strengthens Container Security ... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出固件混淆非常简单，使用 seccomp 阻止 rmdir 即可得到解密固件而无需逆向。他们提到之前对三星 SSD 固件的反编译，猜测数据恢复店可能已经常规逆向这些驱动器，并分享了其他关于 HDD 固件黑客的文章链接。

**标签**: `#firmware`, `#reverse-engineering`, `#security`, `#SSD`, `#HDD`

---

<a id="item-7"></a>
## [arXiv 宣布对 hallucinated references 实施一年禁令](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv 将对包含 hallucinated references（AI 编造的引用）的论文实施一年禁令，且后续投稿必须先在 reputable peer‑reviewed venue 获得接受。 此政策针对 AI 生成的 hallucinated 引用日益增长的问题，旨在维护学术诚信并阻止研究者在论文中随意使用语言模型。 禁令期为一年；禁令结束后，作者必须先在 peer‑reviewed venue 获得接受，才能重新在 arXiv 投稿。该政策目前尚未出现在 arXiv 的帮助页面，表明可能仍在规划中，尚未上线。

hackernews · gjuggler · May 14, 20:39 · [社区讨论](https://news.ycombinator.com/item?id=48140922)

**背景**: arXiv 是一个广泛使用的开放获取预印本服务器，研究者在此分享尚未经过正式同行评审的论文早期版本。Hallucinated references 是由 AI 语言模型生成的虚假引用，这些引用不对应任何真实出版物，会削弱学术工作的可靠性。诸如 ref‑check.org 之类的工具通过与 Crossref、Semantic Scholar 等数据库交叉核对来检测这些虚假引用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ref-check.org/">ref-check.org — Academic Reference Verification Tool</a></li>
<li><a href="https://arxiv.org/pdf/2604.16407">26-19 How unique are hallucinated citations 2026-03-31</a></li>
<li><a href="https://writemask.com/blog/aigenerated-detect-or-detection-or-detector-or-text-or-literature-or-references-or-manuscript-or-academic-or-hallucination-or-paper-or-article">AI Hallucinations in Academic Papers : 7 Problems No... — WriteMask</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎此政策，认为这是维护科学诚信的一步，btown 称其为 "对科学极其有益"，但指出该规则目前尚未出现在 arXiv 的政策页面中。其他评论者强调需要更好的引用管理工具（mks_shuffle），并主张在实施禁令前进行仔细审查（MinimalAction），而 rgmerk 则认为未核对 LLM 输出的作者不应期望读者信任其工作。

**标签**: `#arXiv`, `#academic publishing`, `#AI hallucinations`, `#research integrity`, `#policy`

---

<a id="item-8"></a>
## [Ontario auditors find doctors' AI note takers routinely blow basic facts](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771) ⭐️ 8.0/10

Ontario auditors found that AI-powered medical note-taking systems routinely introduce factual errors, potentially endangering patient care.

hackernews · sohkamyung · May 14, 22:37 · [社区讨论](https://news.ycombinator.com/item?id=48142188)

**标签**: `#AI`, `#healthcare`, `#medical documentation`, `#hallucinations`, `#patient safety`

---

<a id="item-9"></a>
## [GGUF 中除了权重还有什么，以及仍缺少什么？](https://nobodywho.ooo/posts/whats-in-a-gguf/) ⭐️ 8.0/10

文章探讨了 GGUF 模型文件中除了权重之外存储的数据，并讨论了诸如外部模型架构定义之类的缺失功能。 了解 GGUF 的内部结构有助于开发者优化基于 llama.cpp 的模型部署，并凸显出对便携式架构描述的需求，以提升跨模型支持。 GGUF 包含头部、元数据和张量数据，支持 2‑bit 到 8‑bit 的量化以及 float16、float32 和 bfloat16，但目前缺乏一种在代码之外描述模型架构的标准方式。

hackernews · bashbjorn · May 14, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48138332)

**背景**: GGUF 是为 llama.cpp 创建的二进制文件格式，基于 GGML 张量库，旨在将模型权重和元数据存储在单个文件中，以实现快速加载和高效推理。它支持多种数据类型，包括低位整数量化和常见的浮点格式（float16、float32、bfloat16），从而在 CPU、GPU 和其他硬件后端上进行部署。虽然与 safetensors 类似，都能捆绑额外数据，但 GGUF 因其与 GGML 运行时的紧密集成而被 ggml‑based 执行器所青睐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>
<li><a href="https://apxml.com/courses/practical-llm-quantization/chapter-5-quantization-formats-tooling/gguf-format">GGUF File Format Explained (llama.cpp)</a></li>
<li><a href="https://huggingface.co/docs/hub/gguf">GGUF · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，投影数据目前被存储在单独的文件中，这与 GGUF 原始的单文件理念相悖，并表达了希望将它们重新合并的愿望。他们还赞扬了 GGML/GGUF 使得 llama.cpp、whisper.cpp 等跨平台项目成为可能，同时强调最大的缺失功能是缺乏外部、经过厂商验证的模型架构定义方式，可能需要通过 DSL 来实现。

**标签**: `#GGUF`, `#llama.cpp`, `#model format`, `#ML infrastructure`, `#open-source AI`

---

<a id="item-10"></a>
## [Rewrite Bun in Rust has been merged](https://github.com/oven-sh/bun/pull/30412) ⭐️ 8.0/10

Bun's JavaScript runtime has been rewritten in Rust, merging a PR that adds over 1 million lines of Rust code.

hackernews · Chaoses · May 14, 08:15 · [社区讨论](https://news.ycombinator.com/item?id=48132488)

**标签**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#language rewrite`, `#open-source`

---

<a id="item-11"></a>
## [MIT 校长科恩布拉斯讨论资金挑战与人才管道](https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline) ⭐️ 8.0/10

MIT 校长萨莉·科恩布拉斯发表了一则信息，针对博士毕业生的资金挑战和人才管道进行阐述，引发了 Hacker News 的广泛讨论。 该信息凸显了对科研经费和博士职业前景日益增长的担忧，这对学术界以及更广泛的 STEM 劳动力都有影响。 信息中指出，科学博士的中位数完成时间为六年，薪酬低，就业前景艰难，许多最近毕业的博士生正考虑离开学术界。

hackernews · dmayo · May 14, 14:51 · [社区讨论](https://news.ycombinator.com/item?id=48136262)

**背景**: 麻省理工学院是美国顶尖的研究型大学，以强势的 STEM 项目和可观的联邦研究经费著称。近年来，经费拨款出现波动，博士生的就业结果受到越来越多的审视。人才管道指的是博士毕业生进入学术界或产业界的流动。

**社区讨论**: 评论者表达了混合观点，许多人指出博士毕业生中普遍存在幻灭感，担心培训时间长且薪酬低；也有人认为博士的价值不仅限于学术界，尤其在纳米制造等领域。还有评论者指出更广泛的系统性问题以及全球教育领导格局可能的转变。

**标签**: `#academia`, `#research-funding`, `#PhD`, `#talent-pipeline`, `#MIT`

---

<a id="item-12"></a>
## [使用变分自编码器在无套利条件下的收益曲线动态建模](https://arxiv.org/abs/2605.12764) ⭐️ 8.0/10

该论文提出了一种两阶段架构：首先使用带动态水平注入的 Student‑t 条件变分自编码器（CVAEsT+LS）学习具有重尾特征的期限结构流形；其次，通过一个受无套利偏微分方程（PDE）约束的连续时间神经随机微分方程（SDE）演化潜变量。在美元、英镑和日元的收益曲线上实验表明，平均期限 RMSE 达到 6.58 bps，显著优于经典的 HJM 模型。 通过在深度生成框架中嵌入无套利约束，该方法解决了标准模型在跨宏观经济 régime 预测期限结构时出现的流形崩塌和套利违规问题。这项进展提供了一个可扩展且数学严谨的工具，用于固定收益定价、风险管理和情景生成，将机器学习的灵活性与金融理论结合起来。 第一阶段采用 Student‑t 似然来捕捉重尾冲击，并使用动态水平注入项将宏观驱动的形状变动与绝对利率水平分离。第二阶段使用神经随机微分方程（SDE）建模潜变量动态，其损失函数包含来源于 Heath‑Jarrow‑Morton（HJM）无套利偏微分方程的惩罚项，以确保生成路径无套利。实验表明，通过相空间向量场分析实现了卓越的宏观经济 régime 检测，并能生成高质量的连续时间情景。

rss · arXiv Quantitative Finance · May 14, 04:00

**背景**: 收益曲线描述了不同到期债券收益率之间的关系，是固定收益定价和风险管理的核心。对其建模需要捕捉复杂的重尾波动，同时必须满足无套利条件以避免无风险套利机会。变分自编码器是一种灵活的生成模型，能够从高维数据中学习低维流形，但在应用于金融时间序列时易出现流形崩塌。随机微分方程（SDE）提供了一种连续时间框架来演化潜变量，施加无套利偏微分方程约束有助于确保生成路径在金融上是合理的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.12764">Yield Curves Dynamics Using Variational Autoencoders Under...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variational_autoencoder">Variational autoencoder - Wikipedia</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/1350486X.2023.2257217">Arbitrage-Free Neural-SDE Market Models - Taylor & Francis</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#variational autoencoder`, `#finance`, `#yield curve modeling`, `#no-arbitrage`

---

<a id="item-13"></a>
## [SPDE 驱动的电价波动建模](https://arxiv.org/abs/2605.13320) ⭐️ 8.0/10

该论文将当日前电价建模为由随机偏微分方程驱动的潜在过程的局部平均值，以估算每周积分方差并比较德国、挪威和西班牙的波动驱动因素。 它首次提供了基于 SPDE 的严格电价波动分析，覆盖多个欧洲区域，为能源金融和风险管理提供了新的方法论工具。 估计器考虑了均值回归和半群平滑效应，详细分解表明各区域的波动驱动因素存在显著差异，表面上的杠杆效应在控制状态变量后消失。

rss · arXiv Quantitative Finance · May 14, 04:00

**背景**: 电价波动指的是日前市场价格的波动，这对能源金融中的交易和风险评估至关重要。将这些价格建模为由随机偏微分方程驱动的潜在过程的局部平均值，可以捕捉电网固有的空间时间依赖性。半群平滑是某些算子的一种正则化性质，在无限维环境中推导方差估计时必须考虑这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/2601235_Exact_Smoothing_Properties_of_Schrodinger_Semigroups">(PDF) Exact Smoothing Properties of Schrödinger Semigroups</a></li>

</ul>
</details>

**标签**: `#electricity markets`, `#stochastic partial differential equations`, `#volatility estimation`, `#energy finance`, `#European energy zones`

---

<a id="item-14"></a>
## [通过添加暂时统计因子增强风险模型](https://arxiv.org/abs/2605.12977) ⭐️ 8.0/10

本文提出了一种基于最大似然估计（MLE）的方法，用于改进现有因子风险模型并添加暂时统计因子，仅需观察到的收益序列和两个超参数：额外因子的数量以及决定收益在对数似然目标中权重的半衰期参数。 通过捕捉标准因子模型所遗漏的市场 regime 变化和暂时性影响，该方法能够改善投资组合风险估计，并可能提升股票投资者的投资表现。 该方法需要选择额外因子的数量和一个半衰期参数，以在对数似然中赋予最近收益更大的权重，并且能够处理缺失收益，适用于典型的股票数据集；作者在 Barra 短期美国风险模型（用于大盘美国股票）上进行了验证。

rss · arXiv Quantitative Finance · May 14, 04:00

**背景**: 因子风险模型将资产收益的变异分解为少数几个共同因子和资产特有的 idiosyncratic 风险，从而提供投资组合风险的简洁视图。最大似然估计是一种统计技术，通过使观测数据在假设分布下的概率最大化来选择模型参数。暂时因子是指来源于市场 regime 转变的短期风险来源，这类因子常被 Barra 等供应商提供的静态因子模型所遗漏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Maximum_likelihood_estimation">Maximum likelihood estimation - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0304407620303894">Maximum likelihood estimation and inference for high dimensional ...</a></li>
<li><a href="https://economics.yale.edu/sites/default/files/bai-121017.pdf">[PDF] Maximum likelihood estimation and inference for approximate factor ...</a></li>

</ul>
</details>

**标签**: `#risk modeling`, `#factor models`, `#maximum likelihood`, `#finance`, `#statistical learning`

---

<a id="item-15"></a>
## [: 将马尔廷格尔薛定谔桥推广到任意维度](https://arxiv.org/abs/2604.01299) ⭐️ 8.0/10

论文表明，Nutz 和 Wiesel 最近提出的马尔廷格尔薛定谔桥自然地推广到任意维度。它将连续时间的对应物识别为最小化加权二次能量的过程，在不可约情况下证明其与 Föllmer 马尔廷格尔重合，并将其与弱最优传输的对偶形式联系起来。 通过将马尔廷格尔薛定谔桥与 Föllmer 马尔廷格尔和弱最优传输相联系，该工作统一了随机分析、最优传输和数学金融中的概念。这为构建可用于模型校准和风险敏感应用的马尔廷格尔传输计划提供了严格的框架。 作者证明马尔廷格尔薛定谔桥在任意维度存在，并且可以表征为具有规定边缘分布的连续马尔廷格尔，其最小化相对于布朗运动的加权二次偏差。在不可约情况下，该桥与 Föllmer 马尔廷格尔重合；更一般地，它与基准度量上的变分问题以及弱最优传输的对偶形式相关联。

rss · arXiv Quantitative Finance · May 14, 04:00

**背景**: 经典薛定谔桥寻找具有给定边缘分布且相对于参考过程（通常是布朗运动）具有最小相对熵的随机过程。由 Nutz 和 Wiesel 提出的马尔廷格尔薛定谔桥将此问题限制为处于凸顺序的概率测度之间的马尔廷格尔传输。Föllmer 马尔廷格尔是与 Föllmer 过程相关的 Doob 马尔廷格尔，出现在不完整市场的最小马尔廷格尔测度中。弱最优传输推广了经典最优传输，允许成本依赖于条件律，从而导致涉及基准度量的对偶形式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.01299v1">Bridging classical and martingale Schrödinger bridges</a></li>
<li><a href="https://www.emergentmind.com/topics/follmer-measures">Föllmer Measures in Stochastic Analysis</a></li>
<li><a href="https://www.emergentmind.com/topics/weak-optimal-transport">Weak Optimal Transport Overview</a></li>

</ul>
</details>

**标签**: `#optimal transport`, `#martingale theory`, `#Schrödinger bridge`, `#stochastic processes`, `#mathematical finance`

---