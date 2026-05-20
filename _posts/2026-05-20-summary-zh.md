---
layout: default
title: "Horizon Summary: 2026-05-20 (ZH)"
date: 2026-05-20
lang: zh
---

> From 79 items, 25 important content pieces were selected

---

1. [Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks](#item-1) ⭐️ 9.0/10
2. [谷歌云因滥用/垃圾邮件问题封禁 Railway。](#item-2) ⭐️ 8.0/10
3. [谷歌宣布 Gemini 3.5 Flash AI 模型，定价提升](#item-3) ⭐️ 8.0/10
4. [虚拟操作系统博物馆提供基于浏览器的近乎所有操作系统档案](#item-4) ⭐️ 8.0/10
5. [谷歌用 AI 生成答案取代传统搜索结果](#item-5) ⭐️ 8.0/10
6. [Remove–AI–Watermarks 命令行工具与库，用于去除 AI 生成的水印](#item-6) ⭐️ 8.0/10
7. [OpenAI 将在 AI 生成图像中嵌入 Google SynthID 水印并提供验证工具](#item-7) ⭐️ 8.0/10
8. [苹果发布由 Apple Intelligence 驱动的新无障碍功能](#item-8) ⭐️ 8.0/10
9. [安德烈·卡帕西加入 Anthropic 预训练团队](#item-9) ⭐️ 8.0/10
10. [CISA Admin Leaked AWS GovCloud Keys on GitHub](#item-10) ⭐️ 8.0/10
11. [Gentoo 警告三个新的 Linux 内核本地提权漏洞](#item-11) ⭐️ 8.0/10
12. [开源项目失败的愚蠢方式：来自 Hacker News 的见解](#item-12) ⭐️ 8.0/10
13. [Global Automation Atlas](#item-13) ⭐️ 8.0/10
14. [几何可观测量在金融 regime 检测中的应用](#item-14) ⭐️ 8.0/10
15. [使用看外期权隐含概率的稳健波动率指数计算方法](#item-15) ⭐️ 8.0/10
16. [参与度与承诺度：极化新闻内容的经济权衡](#item-16) ⭐️ 8.0/10
17. [SaaS 定价的保险建模框架](#item-17) ⭐️ 8.0/10
18. [无惩罚流水线提升量子退火器投资组合优化](#item-18) ⭐️ 8.0/10
19. [URGE：用于扩散模型引导的无导数重要性重采样](#item-19) ⭐️ 8.0/10
20. [随机化无法改善最优执行博弈均衡](#item-20) ⭐️ 8.0/10
21. [解释解释者：能否用 LLM 代理建模欧洲央行会议后波动？](#item-21) ⭐️ 8.0/10
22. [自杀区域：期权博弈与通往人工通用智能的竞赛](#item-22) ⭐️ 8.0/10
23. [An Explicit Solution to Black-Scholes Implied Volatility](#item-23) ⭐️ 8.0/10
24. [Auditing the Auditors: Does Community-based Moderation Get It Right?](#item-24) ⭐️ 8.0/10
25. [用 LLM 裁判的多维行为评估框架用于代理股票预测](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks](https://github.com/antoinezambelli/forge) ⭐️ 9.0/10

Forge is an open-source reliability layer that adds guardrails to local LLMs, boosting an 8B model's success on agentic tasks from ~53% to ~99% without modifying the model.

hackernews · zambelli · May 19, 12:23 · [社区讨论](https://news.ycombinator.com/item?id=48192383)

**标签**: `#LLM`, `#agentic AI`, `#guardrails`, `#open-source`, `#tool-calling`

---

<a id="item-2"></a>
## [谷歌云因滥用/垃圾邮件问题封禁 Railway。](https://status.railway.com/?date=20260519) ⭐️ 8.0/10

2026 年 5 月 19 日，谷歌云因检测到其基础设施来源的滥用和垃圾邮件而暂停了 Railway 的托管服务，如其状态页面所示。 此事件凸显了云服务提供商的滥用预防措施与依赖其服务的平台可靠性期望之间的紧张关系，影响使用 Railway 进行部署的开发者。 根据状态更新，暂停是在收到滥用/垃圾邮件报告后进行的，直至谷歌云支持团队与 Railway 取得联系，响应时间超过一小时。

hackernews · aarondf · May 20, 00:23 · [社区讨论](https://news.ycombinator.com/item?id=48201484)

**背景**: Railway 是一种平台即服务（PaaS），让开发者能够在不管理底层基础设施的情况下部署和扩展应用。谷歌云使用自动化滥用检测系统，在发现垃圾邮件、欺诈或政策违规时可以暂停账户，正如其滥用预防指南所述。这些政策旨在保护更广泛的云生态系统，但如果触发条件过于敏感，也可能误伤合法用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cloud-security/cloud-service-provider-abuse/">Cloud Service Provider Abuse Explained | CrowdStrike</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cloud-security/cloud-security-policies/">Cloud Security Policies: Top 6 Policies - SentinelOne</a></li>

</ul>
</details>

**社区讨论**: 评论者对谷歌云倾向于在没有直接人工联系的情况下暂停初创公司的做法表示不满，认为这与 AWS 和 Azure 更具沟通性的方式形成对比。一些人指出 Railway 自身的滥用预防似乎薄弱，引用其 IP 地址来源的大量垃圾邮件为证，而另一些人则质疑在他人基础设施之上构建平台的明智性。

**标签**: `#Google Cloud`, `#Railway`, `#cloud outage`, `#abuse prevention`, `#platform reliability`

---

<a id="item-3"></a>
## [谷歌宣布 Gemini 3.5 Flash AI 模型，定价提升](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) ⭐️ 8.0/10

在谷歌 I/O 2026 上，谷歌发布了 Gemini 3.5 Flash，这是 Gemini Flash 系列的更新版本，提供了更强的编码和代理能力，并引入了新的定价层级。 该模型更高的输入/输出 token 价格表明谷歌正在向高端代理工作负载转移，这会影响开发者的成本估算，并使 Gemini 3.5 Flash 成为更高端 Pro 模型的竞争者。 Gemini 3.5 Flash 的定价为每百万输入 token 1.50 美元，每百万输出 token 9.00 美元，支持 100 万 token 的上下文窗口，提供可选的思考级别以平衡质量、成本和延迟，并在 TPU 8i 硬件上运行，速度大约是同类模型的四倍。

hackernews · spectraldrift · May 19, 17:43 · [社区讨论](https://news.ycombinator.com/item?id=48196570)

**背景**: 谷歌的 Gemini 系列是一组能够处理文本、图像、视频、音频和 PDF 的多模态大语言模型。Flash 变体针对低延迟和高吞吐量进行了优化，面向实时代理应用。Gemini 3.5 Flash 在 Gemini 3 Flash 基础上增加了思考级别控制和改进的推理能力，并在谷歌的 TPU 8i 加速器上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-5-flash/">Gemini 3.5 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/">With Gemini 3.5 Flash, Google bets its next AI wave on agents, not ...</a></li>
<li><a href="https://www.digitaltrends.com/computing/gemini-3-5-flash-is-googles-new-default-ai-model-and-its-built-to-act-not-just-answer/">Gemini 3.5 Flash is Google's new default AI model, and it's built to ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，虽然谷歌未公开确切参数规模，但可以根据 TPU 8i 规格进行估算；他们强调该模型定价显著上升——每百万 token 输入 1.50 美元，输出 9.00 美元——与 Gemini 2.5 Pro 相当；用户分享了诸如生成动画 SVG 大约花费 13 美分的 token 用量示例；还有人调侃 “Flash” 一词如今更让人想起 HTML5。

**标签**: `#Gemini`, `#AI models`, `#Google`, `#LLM`, `#pricing`

---

<a id="item-4"></a>
## [虚拟操作系统博物馆提供基于浏览器的近乎所有操作系统档案](https://virtualosmuseum.org/) ⭐️ 8.0/10

作者推出了虚拟操作系统博物馆，这是一个在线收藏，提供了几乎所有操作系统的截图和可运行的模拟器，可通过适用于 QEMU、VirtualBox 或 UTM 的 Linux 虚拟机访问。 该博物馆为历史学家、开发者和爱好者提供了教育资源，保存了可能因过时而丢失的计算机遗产。 该博物馆以预配置的 Linux 虚拟机形式提供，内含自定义的与模拟器无关的启动器，使用户能够直接启动每个操作系统而无需额外配置。

hackernews · andreww591 · May 19, 15:53 · [社区讨论](https://news.ycombinator.com/item?id=48195009)

**背景**: 虚拟博物馆将截图、二进制文件和模拟器等数字文物汇集到一个可在线访问的展览中。操作系统模拟使现代硬件能够通过模拟原始 CPU、内存和 I/O 设备来运行旧软件。像虚拟操作系统博物馆这样的项目使用预配置的 Linux 虚拟机，结合 QEMU、VirtualBox 或 UTM，提供可直接运行的历史操作系统实例。这种方法帮助研究者在不需要稀有实体硬件的情况下研究界面演变、软件兼容性和计算文化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.virtualosmuseum.org/">The Virtual OS Museum</a></li>
<li><a href="https://www.stromasys.com/">Emulation solution for Sun SPARC, VAX, Alpha legacy hardware</a></li>
<li><a href="https://oses.ioblako.com/">V86 x86 Emulator - Run Vintage Operating Systems in Browser</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞此次策展工作令人印象深刻，但指出一些展示的版本并非最具代表性或最有趣的发行版。多位评论者提到遗漏或鲜为人知的系统，如 Domain/OS、Pick 和 Temple OS，并讨论了如 Domain/OS 垫片等特色功能。总体情感积极，大家肯定其教育价值，并希望覆盖更广泛的系统。

**标签**: `#operating systems`, `#virtual museum`, `#emulation`, `#computing history`, `#hobbyist`

---

<a id="item-5"></a>
## [谷歌用 AI 生成答案取代传统搜索结果](https://blog.google/products-and-platforms/products/search/search-io-2026/) ⭐️ 8.0/10

在 2026 年 Google I/O 大会上，公司推出了改版的搜索框，用由 Gemini 大语言模型驱动的 AI 生成答案取代传统的网页链接列表，引入了 AI Overviews 和对话式 AI Mode。 这一转变可能大幅减少对外部网站的推荐流量，引发对 AI 生成信息可靠性的担忧，并预示着向‘Google Zero’的更广泛趋势——搜索向开放网站发送的流量将变得很少。 AI Overviews 使用 Gemini Nano、Flash 或 Pro 模型生成带有来源链接的简洁摘要，而 AI Mode 则允许用户以聊天式界面提出后续问题；该功能于 2026 年 5 月起开始向移动用户推出。

hackernews · berkeleyjunk · May 19, 18:34 · [社区讨论](https://news.ycombinator.com/item?id=48197370)

**背景**: 谷歌的搜索生成式体验（SGE）于 2023 年作为一项实验推出，利用生成式 AI 重新组织搜索结果。其底层技术是 Gemini 系列大语言模型，该模型驱动 AI Overviews 等功能，能够将多个网页的信息合成为单一答案。AI Overviews 现已广泛提供，提供带有原始来源链接的快照摘要，旨在让用户获得更快的答案，同时仍提供深入探索的途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/products-and-platforms/products/search/generative-ai-search/">How Google is improving Search with Generative AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://www.gradually.ai/en/gemini-models/">Gemini Models: All Google Models at a Glance</a></li>

</ul>
</details>

**社区讨论**: 几位评论者批评 AI 答案听起来像系统的文献综述，将随机网页评论当作权威来源。其他人则提出了‘Google Zero’的担忧，警告谷歌可能很快停止向外部网站发送流量。许多用户表示他们不信任 LLM 生成的事实，更倾向于查看原始资料，并指出 AI 可能会混合过时或相互矛盾的信息。

**标签**: `#Google Search`, `#AI`, `#User Interface`, `#Search Engine`, `#LLMs`

---

<a id="item-6"></a>
## [Remove–AI–Watermarks 命令行工具与库，用于去除 AI 生成的水印](https://github.com/wiltodelta/remove-ai-watermarks) ⭐️ 8.0/10

GitHub 项目 remove-ai-watermarks 提供了命令行界面和 Python 库，尝试去除图像中的 AI 生成水印（如 SynthID），引发了关于其影响的讨论。 该工具凸显了 AI 来源追踪与用户隐私之间的张力，引发了关于版权执行、深度伪造检测以及绕过水印伦理的疑问。 该仓库指出，对于 Gemini 模型它仅去除可见水印，而要消除 SynthID 需要在低噪声下用 SDXL 重新生成图像，这可能会损失细节且在更高分辨率下可能失效。

hackernews · janalsncm · May 19, 22:30 · [社区讨论](https://news.ycombinator.com/item?id=48200569)

**背景**: AI 水印技术通过在 AI 生成的内容中嵌入不可感知或可见的信号来标示来源并防止滥用。例如 SynthID 等技术将水印嵌入扩散模型的噪声层，使其可检测且设计为抗移除。深度伪造检测方法常依赖于发现不一致或伪影，而水印可以作为这些系统的来源信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_content_watermarking">AI content watermarking - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/watermarking">AI Watermarking 101: Tools and Techniques - Hugging Face</a></li>
<li><a href="https://picdefense.io/blog/how-ai-creates-adaptive-watermarks/">How AI Creates Adaptive Watermarks - picdefense.io</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有人称赞该工具能保护隐私并防止人类艺术被误标为 AI 生成；也有人警告它会削弱版权保护并助长滥用。还有人指出技术局限，例如通过 SDXL 重新生成去除 SynthID 时会导致细节损失。

**标签**: `#AI watermarking`, `#image processing`, `#ethics`, `#CLI tool`, `#deepfake detection`

---

<a id="item-7"></a>
## [OpenAI 将在 AI 生成图像中嵌入 Google SynthID 水印并提供验证工具](https://openai.com/index/advancing-content-provenance/) ⭐️ 8.0/10

OpenAI 宣布将把 Google 的 SynthID 隐形水印嵌入 AI 生成的图像中，并推出验证工具以检测合成内容。 此举推进了 AI 内容溯源，有助于用户区分真实与 AI 生成媒体，应对日益增长的虚假信息担忧。 该水印对人眼不可感知，直接嵌入图像像素中，可通过 OpenAI 的验证工具检测，且不影响图像质量。

hackernews · smooke · May 19, 19:34 · [社区讨论](https://news.ycombinator.com/item?id=48198291)

**背景**: SynthID 是 Google DeepMind 的一种技术，能够在 AI 生成的媒体中嵌入不可感知的数字水印，通过调整令牌或像素的概率分布实现，人眼无法察觉但可被检测工具识别。OpenAI 采用此技术符合行业提升生成式 AI 透明度和安全性的总体趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://arstechnica.com/google/2026/05/googles-synthid-ai-watermarking-tech-is-being-adopted-by-openai-nvidia-and-more/">Google's SynthID AI watermarking tech is being adopted by ...</a></li>
<li><a href="https://openai.com/index/advancing-content-provenance/">Advancing content provenance for a safer, more transparent... | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了水印是否能在截图中保留，指出在深色背景下可看到淡淡的纹理并可通过像素掩蔽技术去除，询问可编码的数据量，还有人批评这是多余的 DRM，可能会阻碍正常使用。

**标签**: `#AI safety`, `#content provenance`, `#watermarking`, `#OpenAI`, `#SynthID`

---

<a id="item-8"></a>
## [苹果发布由 Apple Intelligence 驱动的新无障碍功能](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) ⭐️ 8.0/10

苹果宣布了一系列使用 Apple Intelligence 的新无障碍功能，包括眼动控制、适用于聋人或听力障碍者的音乐触觉反馈以及增强的语音转文字功能。 这些更新展示了苹果如何将设备端 AI 融入日常辅助工具，可能为数百万残障用户提升独立性，并在科技行业树立 AI 驱动无障碍的先例。 眼动追踪全部数据在设备端处理，音乐触觉利用 iPhone 的 Taptic 引擎传递节奏与质感，语音转文字的提升依赖于 Apple Intelligence 的语言模型；这些功能需要 iOS/iPadOS 18 及苹果自研芯片设备。

hackernews · interpol_p · May 19, 12:04 · [社区讨论](https://news.ycombinator.com/item?id=48192224)

**背景**: Apple Intelligence 是苹果在 2024 年推出的设备端 AI 系统，提供写作工具、图像生成、通知摘要等功能，并与 ChatGPT 集成，仅在苹果自研芯片的 Mac 和 iOS 设备上运行。眼动追踪让用户通过注视来控制 iPhone 或 iPad，屏幕上会出现随眼球移动的指针，凝视停留即可触发点击，所有数据均在设备端处理。音乐触觉是一项无障碍功能，它通过 iPhone 的 Taptic 引擎将音乐转化为振动，使聋人或听力障碍者能够“感受”音乐。这些功能共同体现了苹果利用 AI 提升无障碍体验、同时保障隐私的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence - Wikipedia</a></li>
<li><a href="https://support.apple.com/guide/iphone/control-iphone-with-the-movement-of-your-eyes-iph66057d0f6/ios">Control iPhone with the movement of your eyes - Apple Support</a></li>
<li><a href="https://www.apple.com/newsroom/2024/05/apple-announces-new-accessibility-features-including-eye-tracking/">Apple announces new accessibility features, including Eye... - Apple</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，苹果常常通过无障碍功能悄悄引入如代理 AI 等先进技术，认为这是其一贯的低调推出方式。一些用户分享了在 Be My Eyes 上帮助视力正常志愿者的积极体验，而另一些则批评 iOS 目前的语音转文字和打字纠错仍然不如预期，落后很多。还有几条评论较为轻松，玩笑说该视频的播放速度对盲人用户来说是不可访问的。

**标签**: `#Apple`, `#accessibility`, `#AI`, `#assistive technology`, `#HackerNews`

---

<a id="item-9"></a>
## [安德烈·卡帕西加入 Anthropic 预训练团队](https://twitter.com/karpathy/status/2056753169888334312) ⭐️ 8.0/10

安德烈·卡帕西在 Twitter 上宣布他已加入 Anthropic 的预训练团队，并将于本周开始工作，参与支撑 Claude 模型族的大规模训练。 他深厚的深度学习专长和教育者声誉预计将增强 Anthropic 的模型训练能力，加剧与 OpenAI 等其他前沿实验室的竞争。 在加入 Anthropic 之前，卡帕西曾领导特斯拉的 AI 工作，是 OpenAI 的研究科学家，并在 Coursera 上创建了流行的《深度学习专项课程》；他的转职凸显了顶尖 AI 实验室之间的人才流动。

hackernews · dmarcos · May 19, 15:07 · [社区讨论](https://news.ycombinator.com/item?id=48194352)

**背景**: Anthropic 是一家成立于 2021 年的专注于 AI 安全的公司，以其使用宪法 AI 技术训练的 Claude 系列大型语言模型而闻名。预训练团队负责进行巨大的计算运行，以教会这些模型核心语言理解，随后再进行特定任务的微调。安德烈·卡帕西是著名的 AI 研究者和教育者，曾在特斯拉领导 Autopilot 视觉系统的构建，并在线教授深度学习，惠及数十万学生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model)</a></li>
<li><a href="https://www.anthropic.com/news/introducing-claude">Introducing Claude \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎此次聘任，指出卡帕西在最近的采访中曾暗示可能会这样转职，并赞赏他的教学能力；有人希望他在受 NDA 限制的情况下仍能继续教育工作，也有人用流行文化的引用增添轻松氛围。总体情绪积极且对他的潜在影响充满期待。

**标签**: `#AI`, `#Anthropic`, `#Andrej Karpathy`, `#Hiring`, `#Machine Learning`

---

<a id="item-10"></a>
## [CISA Admin Leaked AWS GovCloud Keys on GitHub](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) ⭐️ 8.0/10

A CISA administrator accidentally published AWS GovCloud access keys and plaintext passwords in a public GitHub repo, sparking widespread criticism and debate over secret handling practices.

hackernews · LelouBil · May 19, 07:45 · [社区讨论](https://news.ycombinator.com/item?id=48190454)

**标签**: `#cybersecurity`, `#government`, `#cloud security`, `#secret leakage`, `#GitHub`

---

<a id="item-11"></a>
## [Gentoo 警告三个新的 Linux 内核本地提权漏洞](https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html) ⭐️ 8.0/10

2026 年 5 月 19 日，Gentoo 宣布披露了三个新的 Linux 内核本地提权漏洞——Copy Fail（CVE-2026-31431）、Dirty Frag（CVE-2026-43284/CVE-2026-43500）和 Fragnesia（CVE-2026-46300），并敦促用户及时升级内核或使用实时补丁进行缓解。 这些漏洞影响众多 Linux 发行版，使普通用户能够获得 root 权限，凸显了内核安全的持续挑战以及实时补丁在快速缓解中的重要性。 Copy Fail 源自 algif_aead.c 中不安全的就地优化，导致页面缓存页被链接到可写散列表；Dirty Frag 利用 ESP 相关内核模块；Fragnesia 针对 XFRM ESP‑in‑TCP 子系统，分别通过恢复特定提交或应用独立补丁进行修复。

hackernews · akhuettel · May 19, 15:27 · [社区讨论](https://news.ycombinator.com/item?id=48194614)

**背景**: Linux 内核是操作系统的核心，本地提权（LPE）漏洞使得拥有有限权限的攻击者能够以 root 身份执行任意代码。实时补丁可以在不重启的情况下更新内核，但可能导致不稳定或内核恐慌。Gentoo 建议通过 emerge -u @world 定期升级内核，并研究从上游自动化实时补丁的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html">Copy Fail, Dirty Frag, and Fragnesia kernel vulnerabilities</a></li>
<li><a href="https://en.wikipedia.org/wiki/Copy_Fail">Copy Fail - Wikipedia</a></li>
<li><a href="https://www.tenable.com/blog/dirty-frag-cve-2026-43284-cve-2026-43500-frequently-asked-questions-linux-kernel-lpe">Dirty Frag (CVE-2026-43284,CVE-2026-43500): Linux Kernel ... - Tenable</a></li>

</ul>
</details>

**社区讨论**: 评论者们讨论实时补丁是否应成为标准的自动化内核更新机制，同时警告恶意补丁可能大规模传播。有人建议通过在 gVisor 等沙箱中运行更多工作负载来降低内核漏洞的影响，还有人嘲弄 LLM 生成补丁的想法。少数人质疑 Gentoo 的做法是否独特或在各发行版中普遍存在。

**标签**: `#kernel`, `#vulnerabilities`, `#Linux`, `#security`, `#live-patching`

---

<a id="item-12"></a>
## [开源项目失败的愚蠢方式：来自 Hacker News 的见解](https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html) ⭐️ 8.0/10

文章概述了导致开源项目失败的常见愚蠢方式，这些方式来源于 Hacker News 的讨论，包括动机变化、有毒行为、自信过度的分叉、安全扫描器的无意义 PR 以及范围蔓延。 了解这些失败模式有助于维护者避免常见错误，从而提升项目的寿命和健康，有利于整个开源生态系统。 关键细节包括‘自信过度的分叉’模式——因愤怒或 hubris 而产生的分叉往往缺乏关键质量；安全扫描器的无意义 PR 只为在 README 中植入徽章；以及由声音最大的用户驱动的范围蔓延导致项目臃肿。文章还提到 OpenSSH、Jenkins 和 LibreOffice 作为成功分叉的反例。

hackernews · chmaynard · May 19, 19:22 · [社区讨论](https://news.ycombinator.com/item?id=48198127)

**背景**: 开源软件项目通常由志愿者或贡献者维护，他们通过拉取请求（PR）提交代码更改。项目的可持续性依赖于积极的维护、清晰的治理以及健康的社区文化。常见的威胁包括动机丧失、有毒互动、缺乏动机的分叉以及功能无控制增长。

**社区讨论**: 评论者基本同意文章的观点，并补充了诸如出于愤怒的过度自信的分叉、仅为放置徽章的安全扫描器无意义 PR，以及由声音最大的用户驱动的范围蔓延等额外失败模式。许多人强调了明确的贡献指南的重要性以及抵制 tangential 特性以保持项目专注。总体而言，讨论反映了对维护健康、可持续开源项目的共同关注。

**标签**: `#open-source`, `#project-maintenance`, `#community`, `#software-engineering`, `#lessons-learned`

---

<a id="item-13"></a>
## [Global Automation Atlas](https://arxiv.org/abs/2605.17086) ⭐️ 8.0/10

The paper introduces a Global Automation Atlas that provides task-level automation exposure measures for 124 countries, covering 99% of world GDP and population. It distinguishes labor-substituting from labor-augmenting automation and reports exposure ranging from 3.3% in South Sudan to 61.6% in China. By offering a comparable, country-specific measure, the atlas enables researchers and policymakers to analyze how automation affects labor markets across development stages. The findings reveal strong income-related patterns, within-group variation, and gender disparities, highlighting where substitution versus augmentation dominates and guiding targeted interventions. The methodology uses O*NET task statements (18,797 tasks) and classifies each task-country pair by whether available technology can substitute, augment, or both, while also identifying the technology channel and AI involvement. Results show that less technologically advanced automation accounts for over half of exposed tasks in low-income countries but only about a quarter in high-income countries, and AI tends to augment labor in high-income settings while substituting in low-income settings.

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: Automation exposure measures often assign fixed scores to tasks or occupations, limiting cross-country comparisons because the same task may be automated differently depending on local technology availability and costs. A task-based approach, drawing on detailed task descriptions from sources like O*NET, allows analysts to assess whether specific technologies can perform or transform a task's core activities at sufficient quality and cost. By distinguishing substitution (labor-replacing) from augmentation (labor-enhancing) effects, researchers can better understand the distinct economic and social impacts of automation technologies.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.17086">Global Automation Atlas - arXiv.org</a></li>
<li><a href="https://automationatlas.org/">Global Automation Atlas | Task-by-task automation exposure</a></li>
<li><a href="https://github.com/prashgarg/global-automation-atlas/blob/main/README.md">global-automation-atlas/README.md at main - GitHub</a></li>

</ul>
</details>

**标签**: `#automation`, `#labor economics`, `#AI impact`, `#cross-country analysis`, `#task-based measurement`

---

<a id="item-14"></a>
## [几何可观测量在金融 regime 检测中的应用](https://arxiv.org/abs/2605.17117) ⭐️ 8.0/10

该论文提出四种几何可观测量——贝里相位率、谱熵、约化态纯度和哈密顿敏感度——从股指收益率的学习谱嵌入中提取，并在 2000 年至 2024 年的 17 次历史危机中，对比 46 种经典和机器学习基线方法评估其作为 regime 检测器的表现。 该研究表明贝里相位率获得中位数 Cohen's d 为 0.72，相比监督随机森林将误报率降低约 67%，展示了一种受量子启发的新方法在检测市场 regime 转变时能够优于众多现有技术。 在走前嵌套超参数选择下，贝里相位率的无偏外部样本中位数 Cohen's d 为 0.72（95% 置信区间[0.34,1.18]），年均误报约 1.2 次，而监督随机森林为 3.6 次；约化态纯度在样本内可分离性最高（d=0.83），几何与经典特征的平均绝对相关系数约为 0.22，表明它们捕捉到的风险信号 largely independent。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 金融 regime 检测旨在识别市场状态的转变，例如波动率、相关性或流动性的变化，这些变化预示着不同的风险 regime。谱嵌入将股指收益率时间序列映射到射影希尔伯特空间，其中可以计算源自量子力学的几何量——贝里相位、谱熵、态纯度和哈密顿敏感度。这些可观测量捕捉嵌入动态的曲率和信息论特性，提供无监督的特征，能够补充传统的统计和机器学习预测方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.17117">[2605.17117] Geometric Observables for Financial Regime Detection</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6685298">Geometric Observables for Financial Regime Detection by... :: SSRN</a></li>
<li><a href="https://www.mathworks.com/help/signal/ref/spectralentropy.html">spectralEntropy - Spectral entropy for signals and ...</a></li>

</ul>
</details>

**标签**: `#finance`, `#regime detection`, `#geometric observables`, `#machine learning`, `#time series`

---

<a id="item-15"></a>
## [使用看外期权隐含概率的稳健波动率指数计算方法](https://arxiv.org/abs/2605.17446) ⭐️ 8.0/10

本文提出了一种方法，构建符合观察到的看外期权买卖价差且满足无套利条件的连续欧洲期权定价函数，所需市场参数较现有方法更少。 通过解决模型自由方差估计中的离散行权价限制，该方法能够在流动性较低的市场中提供更可靠的波动率指数计算，对从业者和学者均有益。 所构建的定价函数满足单调性和凸性，仅依赖看外期权价格，且因参数需求较少，在流动性极低时仍能保持稳健。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 模型自由方差估计将对数价格的二次变化的期望表示为跨越连续行权价的欧洲期权价格积分，正如卡尔-马丹公式所示。实际上，期权仅在离散行权价交易，导致理论积分与可用市场数据之间存在差距。波动率指数（如 VIX）通常基于看外期权价格来近似该积分，因此需要从稀疏数据重建满足无套利条件的连续期权价格曲面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Carr–Madan_formula">Carr–Madan formula - Wikipedia</a></li>
<li><a href="https://www.fma.org/assets/docs/Derivatives2025/Vladimirov.pdf">Functional Estimation of Option Pricing Models</a></li>
<li><a href="https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Options_Probabilities_Exhibit_Link.pdf">How Options Implied Probabilities Are Calculated</a></li>

</ul>
</details>

**标签**: `#volatility index`, `#option pricing`, `#implied variance`, `#financial mathematics`, `#discrete strikes`

---

<a id="item-16"></a>
## [参与度与承诺度：极化新闻内容的经济权衡](https://arxiv.org/abs/2605.18357) ⭐️ 8.0/10

研究使用深度学习分类器和针对多党系统定制的大型语言模型，衡量主要新闻平台文章的极化程度，发现供给驱动的极化内容增加提升用户参与度（停留时间），但不增加订阅；在高 salience 选举期间，同样的内容会降低订阅并加速用户流失。 结果表明，数字出版商存在非对称的权衡：极化内容能够可靠地吸引注意力，但难以转化为付费订阅，且在政治 salience 高时可能损害用户承诺，这为平台设计和监管提供了参考。 极化程度通过深度学习分类器和针对多党对话微调的大型语言模型进行测量；因果效应通过巴特克工具（捕捉供给侧编辑变化）和选举工具（捕捉需求侧政治 salience）进行识别。研究发现，情感极化驱动了参与度与订阅效应之间的最大分歧，而预设的意识形态代理变量并不调节这些效应；当出版商同时覆盖议题的两面时，出现平衡消费现象。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 极化内容是指能够引发强烈情感或意识形态反应的新闻，往往会提升用户在平台上的停留时间（参与度）。参与度（停留时间）和承诺度（订阅和留存）是出版商需要平衡的两种不同结果。为了估计极化内容对这些结果的因果影响，研究使用了工具变量方法，其中巴特克工具通过当地行业份额与全国增长率的交互来捕捉供给侧编辑变化，而选举工具则利用政治 salience 的波动来捕捉需求侧变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nber.org/system/files/working_papers/w24408/revisions/w24408.rev0.pdf">BARTIK INSTRUMENTS: WHAT, WHEN, WHY, AND HOW</a></li>
<li><a href="https://www2.stat.duke.edu/~fl35/teaching/640/Chapter6.1_InstrumentalVariables.pdf">STA 640 — Causal Inference 0.4cm Chapter 6.1 Instrumental ...</a></li>
<li><a href="https://www.aeaweb.org/articles?id=10.1257/aer.20181047">Bartik Instruments: What, When, Why, and How - American ...</a></li>

</ul>
</details>

**标签**: `#media economics`, `#political polarization`, `#news engagement`, `#causal inference`, `#machine learning`

---

<a id="item-17"></a>
## [SaaS 定价的保险建模框架](https://arxiv.org/abs/2605.16699) ⭐️ 8.0/10

该论文提出了一种基于保险的频率‑严重程度模型，用于封顶使用量的 SaaS 定价，结合保费计算原则和蒙特卡洛准备金充足性分析。它将框架映射到 LLM 服务（如 Claude Code、ChatGPT）和云平台（如 Vercel、Cloudflare Workers）的可观察订阅层级。 通过将精算科学与 SaaS 定价相结合，该工作为从业者提供了一种具体的工具，用于为使用量封顶的服务定价并管理尾部风险敞口，有望提高提供商的收入稳定性和风险管理能力。 该框架将需求分解为频率和严重程度两个部分，应用经典的保费计算公式，并通过蒙特卡洛模拟评估在极端使用情景下的准备金充足性。论文通过 LLM 订阅和云平台的示例进行演示，强调其为操作性而非理论性的贡献。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 封顶使用量的 SaaS 产品无论实际消耗多少都收取固定保费，但用户需求具有随机性且可能呈现重尾严重程度，这类似于带有上限（类似免赔额）的保险合同。精算的频率‑严重程度模型用于估计事件的期望数量及其平均成本，而蒙特卡洛准备金分析则通过模拟众多可能结果来确保在尾部风险下准备金充足。保险经济学中的保费计算原则（如期望损失加载）被改编用于确定此类服务的周期性费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/f/frequencyseverity-method.asp">Understanding the Frequency-Severity Method in Insurance Claims</a></li>
<li><a href="https://en.wikipedia.org/wiki/Actuarial_science">Actuarial science - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_as_a_service">Software as a service - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SaaS`, `#pricing`, `#actuarial science`, `#insurance modeling`, `#Monte Carlo`

---

<a id="item-18"></a>
## [无惩罚流水线提升量子退火器投资组合优化](https://arxiv.org/abs/2605.17628) ⭐️ 8.0/10

论文表明，标准的惩罚编码 QUBO 用于直接量子退火器投资组合优化会产生密集的全一交互项，导致 D‑Wave Pegasus 和 Zephyr 硬件上的链断率达到 83‑92 %，并且无法得到可行样本。通过放弃惩罚项并在采样仅含目标的 QUBO 后用经典方法强制基数约束，链断率降至 ≤0.04 %，并获得可行的低能量投资组合。 将惩罚项确定为根本原因解释了为什么当前量子退火器在投资组合优化中表现不佳，并将研究方向转向混合经典‑量子流水线，以在保持量子优势的同时避免硬件导致的不可行性。这一见解有助于提升 D‑Wave 设备在金融建模及类似组合问题上的实际适用性。 在惩罚 formulation 下，链断率在 N=24 时达到 83 %，在 N=49 时达到 92 %，导致没有可行样本；采用无惩罚方法后，Advantage/Advantage2 上每样本的平均链断率降至 ≤0.04 %，测试范围包括最多 N=49 的股票和 N=48 的博彩问题。后处理遗憾度在所有规模上均 ≤0.03 %，且 QPU 在 N=39 和 48 的博彩问题上产生的可行投资组合能量低于贪心启发式算法。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 量子退火通过将优化问题映射到 D‑Wave 的 Pegasus 或 Zephyr 量子处理器上的 Ising 模型来求解，这些处理器的量子比特按稀疏、非完全图排列。投资组合优化常被编码为带有基数惩罚的 QUBO，以强制恰好选择 K 项资产；该惩罚项贡献一个与全一矩阵成正比的密集秩‑一项，使得逻辑交互图变成完全图，与问题的协方差结构无关。在如此密集的逻辑图上，将其嵌入到稀疏硬件需要形成长链的物理量子比特，这些链容易断裂，导致高链断率和不可行样本。论文表明，去除惩罚项并将基数约束经典化处理可以避免这一密集项，从而大幅降低链断率并获得有用的量子样本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.17628">A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio ...</a></li>
<li><a href="https://www.dwavequantum.com/media/2uznec4s/14-1056a-a_zephyr_topology_of_d-wave_quantum_processors.pdf">Zephyr Topology of D-Wave Quantum Processors</a></li>
<li><a href="https://www.mdpi.com/2624-960X/7/2/17">Analysis of D-Wave Topologies with k-Hop-Based Graph Metrics</a></li>

</ul>
</details>

**标签**: `#quantum annealing`, `#portfolio optimization`, `#QUBO`, `#D-Wave`, `#optimization`

---

<a id="item-19"></a>
## [URGE：用于扩散模型引导的无导数重要性重采样](https://arxiv.org/abs/2605.18745) ⭐️ 8.0/10

论文提出了 URGE（无偏重采样通过 Girsanov 估计），一种无导数的推理时缩放算法，通过 Girsanov 测度变换对扩散轨迹进行重要性重加权，无需计算得分、梯度或黑塞矩阵。 URGE 消除了现有引导方法的计算偏差和开销，提供了一种更简单、无偏的替代方案，能够在无需梯度的情况下提升扩散生成模型的样本质量。 该方法为每条模拟轨迹附加一个简单的乘法权重并定期重采样，建立了路径级与粒子级 SMC 的理论等价，并在合成及扩散模型基准上实证优于现有引导基线。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 基于扩散的生成模型通过逆转随机过程来生成样本，常在推理时通过添加漂移项或重加权来实现特定目标的引导。现有的引导技术通常需要重复计算得分或梯度，这可能带来偏差和计算开销。Girsanov 定理提供了一种通过改变底层概率度量来改变随机过程漂移的方法，从而在无需梯度计算的情况下实现无偏重加权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Girsanov_theorem">Girsanov theorem - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2605.18745">[2605.18745] SURGE: Approximation-free Training Free Particle ...</a></li>
<li><a href="https://www.machinebrief.com/news/can-urge-revolutionize-ais-generative-game-23go">Can URGE Revolutionize AI's Generative Game? | Machine Brief</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#generative models`, `#importance sampling`, `#particle filtering`, `#inference-time guidance`

---

<a id="item-20"></a>
## [随机化无法改善最优执行博弈均衡](https://arxiv.org/abs/2503.08833) ⭐️ 8.0/10

作者表明，在具有瞬态价格冲击的最优执行博弈中，任何随机交易策略都可以通过简单平均得到一个非随机策略，其预期成本更低，因而纳什均衡不能包含随机策略且均衡是唯一的。 此结果解决了关于随机化是否能恢复最优执行博弈均衡存在的公开问题，并确立了均衡的唯一性，对市场微观结构理论和算法交易实践具有直接影响。 去随机化通过对随机策略进行时间平均实现，证明在假设严格正定冲击衰减核和凸交易成本的一般交易成本模型下成立。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 最优执行研究交易者如何在最小化市场冲击成本的前提下平仓大额头寸，瞬态价格冲击模型描述了交易的影响会随时间衰减。在多交易者的竞争环境中，纯纳什均衡可能不存在，因而研究者探讨是否允许随机策略能够恢复均衡的存在。论文假设冲击衰减核是严格正定的，这保证了核定义了有效的内积并导致最优策略具有良好行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/1901.02327">Optimal VWAP execution under transient price impact</a></li>
<li><a href="https://arxiv.org/abs/1310.4471v3">[1310.4471v3] Multivariate transient price impact and matrix ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Positive-definite_kernel">Positive-definite kernel - Wikipedia</a></li>

</ul>
</details>

**标签**: `#optimal execution`, `#market microstructure`, `#game theory`, `#Nash equilibrium`, `#algorithmic trading`

---

<a id="item-21"></a>
## [解释解释者：能否用 LLM 代理建模欧洲央行会议后波动？](https://arxiv.org/abs/2508.13635) ⭐️ 8.0/10

本文提出了一种基于大语言模型的代理框架，模拟 30 名具有不同偏好的合成交易者解读欧洲央行新闻发布会 transcripts，得到的跨部分分歧度能够比标准文本方法更好地预测隔夜指数掉期（OIS）波动。 该框架能够事先估计市场对央行沟通的解读方式，为政策制定者提供预测市场反应和改进沟通策略的实用工具。同时，它展示了大语言模型在金融领域的新型跨学科应用，将人工智能研究与实际市场分析联系起来。 在 1998 年至 2026 年的 293 次理事会会议中，LLM 暗示的分歧度与实际隔夜指数掉期波动的相关系数约为 0.5，优于基线文本特征；在 2025 年 1 月以后真正未见过的会议上的外部样本验证中结果依然稳健，且当向代理提供历史的会议前后波动示例时，校准效果会提升。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 隔夜指数掉期（OIS）是一种浮动利率与隔夜利率复利挂钩的利率掉期，其波动率反映了市场对短期利率走势的预期。大语言模型代理可以被赋予不同的风险偏好、认知偏差和解读风格，以在基于代理的模拟中充当合成交易者。基于代理的模型通过模拟众多自治代理的相互作用来重现诸如市场分歧等复杂系统层面的现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Overnight_indexed_swap">Overnight indexed swap - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/o/overnightindexswap.asp">How to Calculate an Overnight Index Swap (OIS) and Its Benefits</a></li>
<li><a href="https://arxiv.org/html/2508.13635v3">Interpreting the Interpreter: Can We Model post-ECB ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#central banking`, `#financial volatility`, `#NLP`, `#agent-based simulation`

---

<a id="item-22"></a>
## [自杀区域：期权博弈与通往人工通用智能的竞赛](https://arxiv.org/abs/2512.07526) ⭐️ 8.0/10

该论文将 AGI 竞赛建模为具有内生存在性风险的连续时间抢占博弈，表明风险项在均衡无差条件中相互抵消。这解释了为何主权行为者在承认灾难性失败风险的情况下仍在加速 AGI 投资。 通过将实物期权理论与 AI 安全联系起来，该工作为观察到的 AGI 竞赛动态提供了理论解释，并强调了诸如内化毁灭成本之类的政策杠杆，这些杠杆可能阻止危险的加速。它对博弈论文献和 AI 治理讨论都有贡献。 模型引入了一个与开发速度相关且全球共享的系统性毁灭参数 D；由于 D 同时出现在双方的收益函数中，它在均衡条件中相互抵消，从而在即使风险调整后净现值为负的情况下形成‘自杀区域’，促使理性主体提前部署 AGI。论文还表明，次生存灾难（'警告射击'）无法阻止加速，并推导出恢复等待期权价值所需的私人责任阈值。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 实物期权理论将金融期权估值应用于资本预算决策，表明在高不确定性下投资应被推迟。连续时间抢占博弈建模了定时竞争，玩家试图在对手之前行动，其均衡表现为相互抢占。存在性风险指可能导致人类灭绝或文明永久崩溃的威胁，常被建模为与活动水平相关的系统性毁灭参数。在 AGI 竞赛中，这一毁灭参数是共享的，并随开发速度增加，从而影响战略激励。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/239811294_Equilibria_in_Continuous_Time_Preemption_Games_with_Markovian_Payoffs">(PDF) Equilibria in Continuous Time Preemption Games with...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Real_options_valuation">Real options valuation - Wikipedia</a></li>
<li><a href="https://medium.com/@qhsestandard/the-problem-of-ruin-why-the-5x5-risk-matrix-is-mathematically-suicidal-0753ba8fd629">The Problem of Ruin: Why the 5x5 Risk Matrix is ... - Medium</a></li>

</ul>
</details>

**标签**: `#AGI`, `#game theory`, `#AI safety`, `#existential risk`, `#real options`

---

<a id="item-23"></a>
## [An Explicit Solution to Black-Scholes Implied Volatility](https://arxiv.org/abs/2604.24480) ⭐️ 8.0/10

该论文通过将 Black‑Scholes 隐含波动率表示为逆高斯分布的分位函数，导出了显式解析公式，实现了机器精度且计算速度优于现有求解器。 提供精确的闭式表达式消除了对迭代近似的需求，为期权定价、风险管理和希腊字母计算提供了更快、更可靠的波动率提取。 该公式将隐含波动率表达为由可观察期权价格决定的逆高斯分布的分位函数，实现机器精度，且比最先进的基准求解器快约 3.4 倍。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: Black‑Scholes 模型假设恒定波动率来定价欧式期权，隐含波动率是使模型价格与市场观察价格相等的波动率值。由于缺乏解析逆函数，传统上需要通过数值求解来获取隐含波动率。论文表明，归一化的期权价格等于逆高斯分布的累积概率，因此隐含波动率对应于该分布的分位函数。这种重新解释提供了一个分布变换，也使得希腊字母和无套利条件在方差‑分位坐标下的表达更为简洁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.24480v1">An Explicit Solution to Black–Scholes Implied Volatility</a></li>
<li><a href="https://www.emergentmind.com/topics/explicit-solution-to-black-scholes-implied-volatility">Explicit Black-Scholes Implied Volatility</a></li>

</ul>
</details>

**标签**: `#Black-Scholes`, `#implied volatility`, `#quantitative finance`, `#option pricing`, `#analytic solution`

---

<a id="item-24"></a>
## [Auditing the Auditors: Does Community-based Moderation Get It Right?](https://arxiv.org/abs/2603.18053) ⭐️ 8.0/10

The study examines how consensus-based auditing in X's Community Notes leads minority contributors to align with majority views and reduces their engagement on controversial issues.

rss · arXiv Quantitative Finance · May 19, 04:00

**标签**: `#content moderation`, `#social platforms`, `#community notes`, `#auditing`, `#behavioral model`

---

<a id="item-25"></a>
## [用 LLM 裁判的多维行为评估框架用于代理股票预测](https://arxiv.org/abs/2605.05739) ⭐️ 8.0/10

该论文提出了一种多维行为评估框架，使用三个大型语言模型裁判对代理股票预测系统的六个维度中的中间决策进行评分，显示出高度的一致性判断以及与金融表现的强相关。 该方法通过评估决策过程而不仅仅是输出，推进了自主 AI 的评估，使得可以有针对性地改进代理交易策略，从而可能提高鲁棒性和盈利能力。 该框架在六个维度（制度检测、路由、适应、风险校准、策略连贯性、错误恢复）上使用三个 LLM 裁判进行评分，获得 Krippendorff's alpha = 0.85，并且与实现的 20 日夏普比率的 Spearman rho = 0.72；将不足分数转换为 Soft Actor‑Critic 惩罚并经过三轮微调，使一天的 MAPE 从 0.61%降至 0.54%（相对下降 11.5%）。

rss · arXiv Quantitative Finance · May 19, 04:00

**背景**: 代理 AI 是指能够在有限监督下感知、推理并行动以追求目标的自主系统，通常由多个机器学习组件构成。大型语言模型裁判是通过提示让 AI 模型对系统行为的特定方面进行评估和打分，提供了一种可扩展的方式来评估中间决策。在股票预测中，强化学习框架如 Soft Actor‑Critic 通过最大化预期回报来学习交易策略，而夏普比率衡量风险调整后的表现。闭环反馈将评估信号重新注入学习过程，以随时间推移优化代理的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Krippendorff's_alpha">Krippendorff's alpha - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/404627669_Multi-Dimensional_Behavioral_Evaluation_of_Agentic_Stock_Prediction_Systems_Using_LLM_Judges_with_Closed-Loop_Reinforcement_Learning_Feedback">Multi-Dimensional Behavioral Evaluation of Agentic Stock ...</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#stock prediction`, `#LLM evaluation`, `#behavioral assessment`, `#reinforcement learning`

---