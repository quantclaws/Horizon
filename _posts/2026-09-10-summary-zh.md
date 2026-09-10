---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> From 23 items, 9 important content pieces were selected

---

1. [WeWorm：AI 辅助的零点击蠕虫通过微信通话在 iOS 和 Android 上传播](#item-1) ⭐️ 9.0/10
2. [vLLM v0.29.0 已发布，Model Runner V2 成为默认。](#item-2) ⭐️ 8.0/10
3. [Hugging Face Transformers v5.17.0 新增对 780B 参数 Hy4‑Preview MoE 模型的支持](#item-3) ⭐️ 8.0/10
4. [Shopify 收购 Tailwind CSS](#item-4) ⭐️ 8.0/10
5. [GPT-6 Astra 使用循环变换器实现隐式推理](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 的推理前缀与 GPT-5.5 Pro 相似](#item-6) ⭐️ 8.0/10
7. [我如何利用 Google Ads 漏洞投放恶意软件](#item-7) ⭐️ 8.0/10
8. [Planet Labs 发布开放卫星数据馈送访问指南](#item-8) ⭐️ 8.0/10
9. [对 Read the Docs 近期大规模 DDoS 攻击的分析](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [WeWorm：AI 辅助的零点击蠕虫通过微信通话在 iOS 和 Android 上传播](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，这是一种通过微信语音通话在 iOS 和 Android 上传播的零点击蠕虫，无需任何用户交互。借助 AI 辅助，团队在约两天内发现漏洞并构建了首个远程代码执行（RCE）利用，随后又用一周完成了蠕虫。 如果属实，WeWorm 揭示了一个严重的移动安全漏洞，攻击者可能利用它大规模劫持微信账户，这表明 AI 能显著加速漏洞利用的开发。这凸显了新兴威胁格局：AI 辅助工具降低了制造复杂零点击恶意软件的门槛。 即使目标不接听电话，受害者也不会听到任何声音，漏洞仍能成功，通过微信语音通话实现远程代码执行。Calif 团队利用 AI 发现漏洞并编写利用代码，仅提供目标选择和安全测试的判断，随后腾讯阻断了该利用。

rss · Simon Willison · Sep 10, 00:56

**背景**: 零点击利用无需受害者任何交互，仅通过接收恶意通话或消息即可设备被入侵。微信的语音通话功能在用户接听前就会处理传入的音频数据，这为内存损坏漏洞提供了攻击面，可能导致远程代码执行。近期趋势显示，AI 模型正在协助安全研究人员进行漏洞发现，大幅缩短识别和武器化漏洞所需的时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm - First 0-Click Worm Spreading Through WeChat Calls Across iOS and Android</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery">The First CVE Wave: Signs That AI-Assisted Vulnerability Discovery Is Reshaping Disclosure Volumes | Blog | VulnCheck</a></li>

</ul>
</details>

**标签**: `#ai-security-research`, `#ai`, `#mobile-security`, `#zero-click`, `#wechat-vulnerability`

---

<a id="item-2"></a>
## [vLLM v0.29.0 已发布，Model Runner V2 成为默认。](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0 包含来自 277 名贡献者的 594 次提交，将 Model Runner V2 设为默认推理引擎，并新增对 Hy4-preview、Qwen3.8-Flash-Next、GraniteSWA 等模型的支持。此外，它还带来了性能提升，如用于 KV 缓存自动调整的 CUDA 图内存分析以及减少每步 logits 内存的批量分片采样。 此次发布表明社区活跃度高，并通过将先进的 Model Runner V2 设为默认来提高 LLM 服务效率，降低内存开销并加速解码。扩展的模型支持和性能优化对研究人员和生产环境中的大语言模型用户都有好处。 关键技术新增包括用于自动 KV 缓存大小的 CUDA 图内存分析、将 logits 内存减少到 1/张量并行度的批量分片采样以及 prompt embeds 支持。破坏性变更移除了十个已弃用的模型架构，并将若干模型迁移到 Transformers 后端，同时废弃的 `python -m vllm.entrypoints.openai.api_server` 入口被 `vllm serve` 取代。

github · khluu · Sep 9, 08:54

**背景**: vLLM 是一个开源库，专为高吞吐量的大语言模型推理而设计，使用 PagedAttention 高效管理键值缓存内存。Model Runner V2（MRV2）是下一代推理运行器，引入了 CUDA 图捕获、动态 KV 缓存大小调整和批量分片采样等特性，以降低内存占用并提升延迟。此版本将 MRV2 设为大多数模型的默认选项，标志着从早期 MRV1 的转变，后者仅在某些 ROCm 配置下仍被使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/configuration/conserving_memory/">Conserving Memory - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/v0.8.5/getting_started/examples/batch_llm_inference.html">Batch LLM Inference — vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#Model Runner V2`, `#release`, `#AI/ML`

---

<a id="item-3"></a>
## [Hugging Face Transformers v5.17.0 新增对 780B 参数 Hy4‑Preview MoE 模型的支持](https://github.com/huggingface/transformers/releases/tag/v5.17.0) ⭐️ 8.0/10

Hugging Face Transformers 库的 v5.17.0 版本新增了对 Hy4‑Preview 780B 参数混合专家（MoE）语言模型的支持，该模型每个 token 激活 49B 参数，并具备多头潜在注意力、DeepSeek 稀疏注意力、带可学习注意力沉门的门控 MLA 以及独立超连接。该版本还加入了用于多说话人语音合成的 VibeVoice、多模态编码器 NeoMME 以及多语言语音识别模型 Fun‑ASR‑Nano。 此更新使研究人员和开发者能够在广泛使用的 Transformers 库中直接实验目前最大的开放权重 MoE 模型及其新颖注意力机制，从而降低扩展大语言模型研究和应用的门槛。 Hy4‑Preview 总参数量为 770B，每个 token 激活 49B 参数，上下文窗口为 1M token，每个 MoE 层包含 256 个路由专家和一个始终激活的共享专家，每个 token 被路由到 8 个专家；实现时省略了多 token 预测层，但在加载时保留其权重以供其他运行时进行 speculative decoding。

github · vasqu · Sep 9, 15:42

**背景**: Hugging Face Transformers 是一个广受欢迎的开源库，提供自然语言处理、计算机视觉和音频任务的预训练模型和工具。混合专家（MoE）层通过将 token 路由到一组专门的专家网络来增加模型容量，使得巨型模型在每个 token 的计算开销相对较低的情况下仍可运行。多头潜在注意力将键/值状态压缩为低秩表示以降低内存带宽，而 DeepSeek 稀疏注意力则为每个查询选择有限的键集以减少计算量。这些技术共同使得像 Hy4‑Preview 这样 780B 参数的超大语言模型能够高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/ Hy 4 - preview · Hugging Face</a></li>
<li><a href="https://medium.com/data-science/deepseek-v3-explained-1-multi-head-latent-attention-ed6bee2a67c4">DeepSeek-V3 Explained 1: Multi - head Latent Attention | Medium</a></li>
<li><a href="https://www.emergentmind.com/topics/deepseek-sparse-attention-dsa">DeepSeek Sparse Attention Mechanism ( DSA )</a></li>

</ul>
</details>

**标签**: `#huggingface`, `#transformers`, `#release`, `#Mixture-of-Experts`, `#large language model`

---

<a id="item-4"></a>
## [Shopify 收购 Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 宣布收购 Tailwind CSS，将这款流行的工具优先 CSS 框架纳入其旗下。 此举可能影响数百万网页开发者使用的广泛采样的 styling 工具，并塑造电子商务平台前端技术的未来方向。 Tailwind CSS 仍然是一种工具优先的框架，提供 flex、pt‑4、text‑center 等类直接在 HTML 中使用；此次收购包含 Tailwind Labs 团队和品牌，尽管最近 AI 对业务造成冲击导致文档流量下降约 40%。

hackernews · EdwinHoksberg · Sep 9, 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一种工具优先的 CSS 框架，开发者可以通过在标记中直接组合低级别的实用类来构建样式，无需编写自定义 CSS。该框架在 Web 开发社区中获得了广泛采用，因其能够快速构建 UI 并保持设计一致性。Shopify 是领先的电子商务平台，为商家提供创建在线商店的工具，并经常集成前端技术以增强店铺定制能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailwindcss.com/">Tailwind CSS - Rapidly build modern websites without ever leaving...</a></li>
<li><a href="https://github.com/tailwindlabs/tailwindcss">GitHub - tailwindlabs/tailwindcss: A utility - first CSS framework for...</a></li>
<li><a href="https://www.npmjs.com/package/tailwindcss">tailwindcss - npm</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 导致的 Tailwind Labs 团队裁员表示同情，同时祝贺创始人实现成功退出。有人质疑在现代 CSS 能力下 Tailwind 是否仍然必要，也有人希望此次收购能保留如《Refactoring UI》等教育资源。总体而言，讨论既体现了对该框架影响的赞赏，也透露了对其在 Shopify 底下未来方向的不确定性。

**标签**: `#Shopify`, `#Tailwind CSS`, `#acquisition`, `#web development`, `#CSS framework`

---

<a id="item-5"></a>
## [GPT-6 Astra 使用循环变换器实现隐式推理](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 8.0/10

Sebastian Raschka 的近期文章探讨了据称的 GPT-6 Astra 如何使用循环变换器来实现隐式推理，引发了关于其可行性的讨论。 如果实现，循环变换器可能提升长度泛化能力并降低 GPU 内存消耗，同时使模型推理过程更不透明，这对 AI 安全和效率研究都有影响。 循环变换器会重复使用共享的 Transformer 块，通过权重复用来模拟更深的网络；隐式推理指的是未输出的内部计算，类似于 "neuralese"。文章指出此想法仍属推测，尚未得到证实。

hackernews · ModelForge · Sep 9, 14:37 · [社区讨论](https://news.ycombinator.com/item?id=49627370)

**背景**: 标准变换器使用固定层数处理输入；循环变换器块允许相同的权重被多次应用，这可以在节省内存的同时模拟任意计算。大型语言模型中的隐式推理指的是推理步骤停留在内部状态而未体现在生成文本中，因而难以监控。近期研究将循环变换器与长度泛化联系起来，并提出随机循环次数以提高鲁棒性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.15647">[2409.15647] Looped Transformers for Length Generalization GPT-6 Astra, Looped Transformers, and Hidden Reasoning [2301.13196] Looped Transformers as Programmable Computers GitHub - asimfish/awesome_loop_transformer: Awesome list ... GitHub - huskydoge/Awesome-Loop-Models: A curated list of ... OpenAI Astra and Looped Transformers | Sebastian Raschka, PhD What Is A Looped Transformer, Which OpenAI Is Using In Its ...</a></li>
<li><a href="https://arxiv.org/abs/2301.13196">[2301.13196] Looped Transformers as Programmable Computers GitHub - asimfish/awesome_loop_transformer: Awesome list ... GitHub - huskydoge/Awesome-Loop-Models: A curated list of ... OpenAI Astra and Looped Transformers | Sebastian Raschka, PhD What Is A Looped Transformer, Which OpenAI Is Using In Its ...</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and">GPT-6 Astra, Looped Transformers, and Hidden Reasoning</a></li>

</ul>
</details>

**社区讨论**: 评论者对潜在能力表示兴奋，引用了 Will Merrill 关于计算限制的工作，并争论循环变换器是否真的隐藏了推理或仅仅是权重复用；一些人认为这更像是一种节省内存的技巧，而不是新颖的推理机制。

**标签**: `#LLM`, `#transformers`, `#hidden reasoning`, `#GPT-6`, `#AI research`

---

<a id="item-6"></a>
## [Qwen 3.8 的推理前缀与 GPT-5.5 Pro 相似](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 8.0/10

Hacker News 的讨论指出，Qwen 3.8 表现出的推理前缀与 GPT-5.5 Pro 高度相似，暗示可能存在蒸馏或共享训练数据。 这种相似性引发了对数据泄露或未经授权使用专有模型输出的担忧，可能影响开源模型的可信度以及未来 AI 训练的做法。 讨论指出，Qwen 3.8 0902 在 2024 年 8 月 10 日之后训练，而当时盗取思维论文已经公开，因此模型可能直接看到那些推理痕迹。

hackernews · wsxiaoys · Sep 9, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=49630026)

**背景**: 推理前缀是指在语言模型生成思维链之前提供的初始 token，用于引导其输出，这一技术在最近的 prefill awareness 论文中被研究。Qwen 是阿里巴巴云开发的一系列开源大语言模型，其中 Qwen 3.8-27B 专注于编码和代理任务。GPT-5.5 Pro 是 OpenAI 的前沿模型，提供更强的推理能力和更高的 token 效率，适用于专业工作负载。蒸馏指的是通过模仿更大（通常是专有）模型的输出或内部表示，将其知识转移到较小的开源模型的过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12747v1">Prefill Awareness in Large Language Models</a></li>
<li><a href="https://ollama.com/library/qwen3.8">qwen 3 . 8</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.5">GPT - 5 . 5 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 评论者们就这种相似性是否源于蒸馏、直接接触泄露的推理痕迹，或是在相似基准解决方案上的巧合训练展开了辩论。有人强调了从专有模型中恢复思维链的技术，而另一些人则质疑原始推理标记的可访问性。总体而言，讨论反映了对模型来源的好奇以及对潜在数据泄露的警惕。

**标签**: `#LLM`, `#reasoning`, `#distillation`, `#Qwen`, `#GPT-5.5`

---

<a id="item-7"></a>
## [我如何利用 Google Ads 漏洞投放恶意软件](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 8.0/10

作者详细说明了如何绕过 Google Ads 的自动审核系统投放传播恶意软件的广告，并在黑客新闻公开舆论压力后账号被恢复。 这揭示了 Google 自动广告审核中的关键漏洞，可能被用于大规模恶意广告，威胁用户安全并削弱对网络广告的信任。 该方法利用了 cloaking 技术——向审核系统展示无害的创意和 URL，而实际用户被重定向到恶意落地页——作者指出，无论是人工审核还是某个触发器导致了账号的恢复。

hackernews · xlii · Sep 9, 11:43 · [社区讨论](https://news.ycombinator.com/item?id=49624856)

**背景**: Google Ads 会对每则广告进行自动审核，广告状态显示为“Under review”，任何修改都会重新启动审核流程，Google 保留优先或重新审核的权利以确保系统稳定。 恶意广告者常使用 cloaking 技术，向审核系统展示无害的创意和落地页，而在特定条件下向真实用户提供恶意内容，从而隐藏恶意落地页。 攻击者通过利用这些 cloaking 方法或被入侵的网站来规避广告政策执行，正如 Google 的广告政策帮助文档和新兴的 cloaking 平台（如 1Campaign）所述。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/google-ads/answer/1722120?hl=en-WS">About the ad review process - Google Ads Help</a></li>
<li><a href="https://www.humansecurity.com/learn/blog/digital-disguise-understanding-cloakings-role-in-malvertising/">Digital Disguise: Understanding Cloaking's Role in Malvertising - HUMAN Security</a></li>
<li><a href="https://www.varonis.com/blog/1campaign">1Campaign: A New Cloaking Platform Helping Attackers Abuse ...</a></li>

</ul>
</details>

**社区讨论**: 评论者批评 Google 过度依赖自动审核，称平台充斥诈骗广告，主张增加人工干预；也有评论指出，作者的账号只有在 Hacker News 引发广泛关注后才被恢复，这类问题早在十年前就曾出现过。

**标签**: `#Google Ads`, `#malvertising`, `#cybersecurity`, `#ad fraud`, `#online advertising`

---

<a id="item-8"></a>
## [Planet Labs 发布开放卫星数据馈送访问指南](https://tech.marksblogg.com/planet-labs-open-satellite-feed.html) ⭐️ 8.0/10

该博客文章详细介绍了如何通过 Planet Labs API、STAC 目录和 Cloud Optimized GeoTIFF 格式访问其开放卫星数据馈送，并包含了社区关于定价、替代方案和技术可用性的反馈。 通过提供开放的高分辨率每日 PlanetScope 影像，该馈送降低了研究人员、非营利组织和开发者监测环境变化和构建地理空间应用的门槛。 该馈送以 Cloud Optimized GeoTIFF 形式提供 3‑5 米分辨率的 PlanetScope 影像，可通过 Planet API 和公开的 STAC 目录获取；社区反馈指出非营利组织的年费约为 3 万美元（仅限小范围条带），并提到 Sentinel、Google Earth 和 Nimbo 等替代数据源。

hackernews · marklit · Sep 9, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49628429)

**背景**: Planet Labs 运营着一颗颗小型卫星（Dove），在 PlanetScope 项目中每日捕捉地球表面的 3‑5 米多光谱影像。公司还提供更高分辨率的 SkySat 和旧版 RapidEye 数据。为提高可发现性和互操作性，Planet 通过 SpatioTemporal Asset Catalog（STAC）发布其数据集，并以 Cloud Optimized GeoTIFF（COG）形式分发，以支持网络上的高效部分检索。这些开放数据产品让用户能够在不下载完整大场景的情况下访问和分析卫星影像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.planet.com/">Planet Labs : Satellite Imagery & Earth Data Analytics</a></li>
<li><a href="https://www.planet.com/data/stac/browser/">Planet Labs - Open Data</a></li>
<li><a href="https://cogeo.org/">Cloud Optimized GeoTIFF</a></li>

</ul>
</details>

**社区讨论**: 评论者呼吁为非营利和保护工作提供更实惠的定价，称赞该博客文章实用且易于复现，指出了 Sentinel、Google Earth、Nimbo 以及即将发布的 Mapterhorn PMtiles 等替代数据源，并质疑 Planet 的卫星是否主要服务于美国监控承包商 Flock。

**标签**: `#satellite imagery`, `#open data`, `#geospatial`, `#remote sensing`, `#Planet Labs`

---

<a id="item-9"></a>
## [对 Read the Docs 近期大规模 DDoS 攻击的分析](https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/) ⭐️ 8.0/10

最近一次大规模 DDoS 攻击针对 Read the Docs，绕过了 Cloudflare 防御，并引发了对 AI 驱动战术的怀疑，如该平台 2026 年 9 月的博客文章所述。 此事件凸显了能够绕过主流缓解服务的不断演变的 DDoS 威胁，并强调了需要更好的法律和技术响应来保护关键的开源文档基础设施。 攻击者使用了一个能够绕过 Cloudflare L7 防护的分布式僵尸网络，引发社区对 AI 编排流量的猜测以及关于启用 Cloudflare 的'Under Attack'模式是否能减轻影响的讨论。

hackernews · davidfischer · Sep 9, 15:55 · [社区讨论](https://news.ycombinator.com/item?id=49628614)

**背景**: Read the Docs 是一个广泛使用的服务，用于托管开源项目的版本化技术文档，依赖静态内容分发和 CDN 缓存。分布式拒绝服务（DDoS）攻击会从许多来源向目标发送大量流量以破坏可用性，其中第 7 层（应用层）攻击专门针对 Web 特定资源。虽然 Cloudflare 在网络层提供强大的 DDoS 缓解，但其 L7 防御可能被能够模仿合法浏览器行为的自适应 AI 驱动流量绕过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.a10networks.com/blog/the-machine-war-has-begun-cybercriminals-leveraging-ai-in-ddos-attacks/">AI DDoS Attacks : How Cybercriminals Use AI | A10 Networks</a></li>
<li><a href="https://www.intelligentciso.com/2026/09/01/cloudflare-ddos-threat-report-h1-2026-1-tbps-attacks-soar-as-dns-floods-and-geopolitical-tensions-drive-a-new-wave/">Cloudflare DDoS Threat Report H1 2026: 1 Tbps attacks soar as ...</a></li>

</ul>
</details>

**社区讨论**: 评论者呼吁采取法律手段追责攻击者，包括起诉设备制造商，而另一些人则质疑为何未启用 Cloudflare 的'Under Attack'模式。有几人推测此次攻击可能是 AI 驱动的，或许旨在剥夺竞争对手的训练数据，并指出攻击轻松绕过了 L7 防护。

**标签**: `#DDoS`, `#cybersecurity`, `#Cloudflare`, `#Read the Docs`, `#network security`

---