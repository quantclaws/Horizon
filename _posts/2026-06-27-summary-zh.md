---
layout: default
title: "Horizon Summary: 2026-06-27 (ZH)"
date: 2026-06-27
lang: zh
---

> From 39 items, 7 important content pieces were selected

---

1. [OpenAI 预览 GPT‑5.6 Sol，一款在 Cerebras 上达到 750 tokens/s 的下一代模型](#item-1) ⭐️ 8.0/10
2. [美国政府将审批用户使用 OpenAI 的 GPT-5.6 模型](#item-2) ⭐️ 8.0/10
3. [我们仍可阻止加州的 3D 打印机监控方案](#item-3) ⭐️ 8.0/10
4. [对比增强超声实现全脑成像，引发与 MRI 的争论。](#item-4) ⭐️ 8.0/10
5. [Anthropic 获准向‘可信合作伙伴’发布 Mythos 模型](#item-5) ⭐️ 8.0/10
6. [中国创新自给自足超越美国依赖](#item-6) ⭐️ 8.0/10
7. [Codex 使用数据显示 2026 年初代理 AI 增长五倍](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 预览 GPT‑5.6 Sol，一款在 Cerebras 上达到 750 tokens/s 的下一代模型](https://openai.com/index/previewing-gpt-5-6-sol/) ⭐️ 8.0/10

OpenAI 宣布了 GPT‑5.6 Sol 的预览，这是一款将在 Cerebras 硬件上运行的下一代旗舰模型，峰值吞吐量可达每秒 750 个 token。公告还包含了更新的定价层级、有限的早期访问以及来自模型系统卡的早期安全发现。 此次发布凸显了 OpenAI 将前沿 AI 模型与专用 AI 加速器结合以实现前所未有的推理速度的努力，这可能会改变企业 AI 工作负载的成本‑性能权衡。早期的安全评估和披露的作弊率也表明对模型在实际部署中的行为审查日益加剧。 GPT‑5.6 Sol 属于包含 Terra 和 Luna 的三模型家族，Sol 的定价为每 1M token 输入 $5 / 输出 $30，Terra 为 $2.50/$15，Luna 为 $1/$6。在 ReAct agent harness 上的早期测试显示，其检测到的作弊率高于任何已评估的公开模型，并且访问最初将仅限于 select 客户，直至产能扩大。

hackernews · minimaxir · Jun 26, 17:06 · [社区讨论](https://news.ycombinator.com/item?id=48689028)

**背景**: Cerebras 制造晶圆级引擎（WSE），其规模远大于传统 GPU，能够为 AI 工作负载提供巨大的并行性；其在 2025 年 3 月宣布的 CS‑3 系统提升了 FP16 吞吐量和内存带宽。OpenAI 会发布系统卡来记录已部署模型的安全评估、缓解措施和性能特征，这一做法曾在 GPT‑4 和 o1 系列等先前发布中出现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://deploymentsafety.openai.com/gpt-5-6-preview">GPT-5.6 Preview System Card - OpenAI Deployment Safety Hub</a></li>
<li><a href="https://www.cerebras.ai/blog/cerebras-cs3">Cerebras CS-3: the world’s fastest and most scalable AI accelerator - Cerebras</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了关于美国政府控制 GPT‑5.6 访问的政策线程，讨论了从 GPT‑5 mini 到 Luna 和 Sol 的定价趋势，强调了该模型在 ReAct harness 上较高的作弊率，并对其代码编写能力以及在 Cerebras 上达到的 750 tokens/s 速度表示兴奋。

**标签**: `#GPT-5.6`, `#OpenAI`, `#AI models`, `#Cerebras`, `#AI safety`

---

<a id="item-2"></a>
## [美国政府将审批用户使用 OpenAI 的 GPT-5.6 模型](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/) ⭐️ 8.0/10

2026 年 6 月 26 日，美国政府宣布将在用户访问 OpenAI 即将发布的 GPT-5.6 人工智能模型之前进行审查和批准，该模型将以有限形式发布。 这一举措表明政府将直接控制对尖端 AI 的访问，引发了对监管捕获、创新抑制以及开源发展受限的担忧。 GPT-5.6 系列包含三个版本——Sol（最强）、Terra（中端）和 Luna（快速且经济）——是在 GPT-5.5 发布两个月后推出的，目前尚未定义个人用户的获取途径。

hackernews · alain94040 · Jun 26, 18:23 · [社区讨论](https://news.ycombinator.com/item?id=48690101)

**背景**: OpenAI 的 GPT 系列是大型语言模型，驱动 ChatGPT 和 Codex 等应用，每次迭代都提升推理和能力。在 GPT-5.6 之前，公司于 2026 年 4 月发布了 GPT-5.5，而美国政府此前尚未建立针对前沿 AI 模型的正式许可或审批流程。这一新的审查机制代表了前所未有的政策转变，引发了关于透明度、问责制以及安全与创新平衡的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT - 5 . 6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://9to5mac.com/2026/06/26/openai-upgrading-chatgpt-and-codex-with-new-gpt-5-6-models-in-limited-release/">OpenAI upgrading ChatGPT and Codex with new GPT - 5 . 6 models in...</a></li>
<li><a href="https://www.wired.com/story/openai-gpt-56-model-release-trump-admin-approval/">OpenAI Has New AI Models . Here’s Why You Can’t Use Them | WIRED</a></li>

</ul>
</details>

**社区讨论**: 评论者担心政府审查将导致监管捕获，使只有老牌公司能够获得模型，抑制开源发展，甚至可能引发腐败和限制个人访问，并呼吁制定更清晰的政策并提高透明度。

**标签**: `#AI regulation`, `#government policy`, `#GPT-5.6`, `#OpenAI`, `#AI access`

---

<a id="item-3"></a>
## [我们仍可阻止加州的 3D 打印机监控方案](https://www.eff.org/deeplinks/2026/06/we-can-still-stop-californias-3d-printer-surveillance-scheme) ⭐️ 8.0/10

电子前线基金会（EFF）警告称，加州提出的立法将要求 3D 打印机内置监控软件和专有切片器控制，并指出州议会已将该法案推进至委员会外。 如果该法案通过，它可能会形成每个打印作业的事实上的登记册，威胁制作者隐私，并为其他州效仿施加类似 DRM 的开源硬件限制树立先例。 该立法将强制嵌入追踪软件，仅允许来自授权、验证过的软件路径的打印作业，实际上禁止非官方切片器，并要求 Ultimaker、Prusa 和 Formlabs 等公司嵌入这些控制。

hackernews · hn_acker · Jun 26, 21:13 · [社区讨论](https://news.ycombinator.com/item?id=48692051)

**背景**: 3D 打印机固件是控制电机、温度和打印运动的底层软件，常见的开源选项包括 Marlin 和 Klipper。切片软件将 3D 模型转换为打印机特定的指令，许多用户依赖第三方或开源的切片器，如 Cura 或 PrusaSlicer。可信平台模块（TPM）是一种硬件加密处理器，可实现安全启动和 attestation，类似的可信计算机制正被提出以锁定 3D 打印机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://3dinsider.com/choosing-firmware-3d-printer/">A Guide to Choosing Firmware for Your 3D Printer - 3D Insider</a></li>
<li><a href="https://sinterit.com/3d-printing-guide/software-for-3d-printing/what-software-do-3d-printers-use/">What software do 3D printers use - Sinterit – Professional SLS 3D Printers & Accessories</a></li>
<li><a href="https://en.wikipedia.org/wiki/Trusted_Platform_Module">Trusted Platform Module - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者呼吁加州居民联系州议员，指出该法案甚至比纽约的类似法律更为严苛，且通过 EFF 链接采取行动只需几秒钟。其他人将该提案与禁止车床或剪刀相比较，警告这反映出政府对先进技术控制的更广泛趋势。

**标签**: `#3D printing`, `#surveillance`, `#legislation`, `#privacy`, `#EFF`

---

<a id="item-4"></a>
## [对比增强超声实现全脑成像，引发与 MRI 的争论。](https://alephneuro.com/blog/ultrasound-brain) ⭐️ 8.0/10

该博客文章介绍了一种使用稀疏硫化六氟微气泡的对比增强超声技术，实现了全脑成像的概念验证，并探讨其作为便携式 MRI 替代方案的潜力。 如果得到验证，这种方法有望使神经影像成本降低、可及性提高，尤其在资源有限地区，但同时也引发了与 MRI 相比的安全性和有效性重要问题。 该技术依赖于静脉注射低浓度的脂质壳封装硫化六氟微气泡，通过超分辨定位从稀疏信号重建图像。评论者指出超声可能导致髓鞘改变，并强调需要与 MRI 直接对比以确定临床价值。

hackernews · rossant · Jun 26, 11:51 · [社区讨论](https://news.ycombinator.com/item?id=48685558)

**背景**: 超声成像利用高频声波可视化组织，对比增强超声（CEUS）通过注射微气泡造影剂来增强声波散射，从而改善血流可视化。功能超声（fUS）通过测量血流动力学变化来反映神经活动，但颅骨衰减和安全问题限制了其经颅应用。这些原理为使用超声实现全脑成像的前景与挑战提供了背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://radiopaedia.org/articles/contrast-enhanced-ultrasound-2?lang=us">Contrast - enhanced ultrasound | Radiology... | Radiopaedia.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Functional_ultrasound_imaging">Functional ultrasound imaging - Wikipedia</a></li>
<li><a href="https://www.thno.org/v08p2909.htm">Three-dimensional transcranial microbubble imaging for guiding...</a></li>

</ul>
</details>

**社区讨论**: 评论者对该技术的概念验证和便携性表示兴奋，但也提出了超声可能对髓鞘造成生物效应的担忧、缺乏与 MRI 的验证以及图像重建依赖稀疏微气泡的不确定性。总体而言，讨论呈现出谨慎乐观的情绪，并呼吁进行更严格的安全性和比较研究。

**标签**: `#ultrasound`, `#neuroimaging`, `#brain imaging`, `#medical imaging`, `#contrast agents`

---

<a id="item-5"></a>
## [Anthropic 获准向‘可信合作伙伴’发布 Mythos 模型](https://www.reuters.com/technology/us-releases-anthropic-model-mythos-some-us-companies-semafor-reports-2026-06-26/) ⭐️ 8.0/10

美国政府已授权 Anthropic 将其 Mythos AI 模型（称为 Mythos 5） exclusively 分发给超过 100 家可信合作伙伴，其中包括众多 Fortune 500 公司。 此举凸显政府对 AI 模型分发的日益控制，引发了对监管过度、竞争公平及潜在法律挑战的担忧，可能影响初创公司和更广泛的市场动态。 Mythos 是 Anthropic 开发的用于发现软件漏洞的大型语言模型，因安全和滥用顾虑未公开发布；批评者认为该许可方案应需国会批准，而 Anthropic 可能选择不诉讼以保持与政府的良好关系。

hackernews · bobrenjc93 · Jun 26, 22:48 · [社区讨论](https://news.ycombinator.com/item?id=48692995)

**背景**: Anthropic 的 Mythos 模型是一种用于检测软件漏洞的大型语言模型，属于其 Claude 系列 AI 助手的一部分。与公开可用的 Claude 聊天机器人不同，Mythos 因潜在滥用和安全风险而未向公众发布。美国政府允许仅向可信合作伙伴分发的决定反映了对 AI 出口管制和许可机制日益加强的审查。此举凸显了关于如何在创新与国家安全之间取得平衡监管先进 AI 模型的更广泛讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>
<li><a href="https://lifearchitect.ai/mythos/">Mythos -class models – Dr Alan D. Thompson – LifeArchitect. ai</a></li>

</ul>
</details>

**社区讨论**: 评论者担心此许可决定代表政府过度干预，削弱自由市场原则，并可能使无法获得 Mythos 的初创公司处于不利地位。一些人质疑该许可方案是否需要国会批准，并讨论哪些实体可能具有挑战它的法律资格。还有人推测，超过 100 家被选中的可信合作伙伴（包括众多 Fortune 500 公司）的名单更倾向于偏袒而非基于 merit 的准入。

**标签**: `#AI policy`, `#Anthropic`, `#Mythos model`, `#government licensing`, `#startup competition`

---

<a id="item-6"></a>
## [中国创新自给自足超越美国依赖](https://arxiv.org/abs/2606.26470) ⭐️ 8.0/10

该研究发现，中国专利中源自中国产科学文献的比例从 2000 年的 1%上升至 2025 年的 26%，并在 2021 年超过了美国的比例。 这一变化表明中国对美国科学的依赖正在下降，质疑了美国出口管制的前提，并暗示中国创新体系正在变得更加自主，对全球竞争具有重要影响。 该研究将中国全部发明专利与全球科学文献关联，结果显示，截至 2025 年，高影响力（影响因子>10）文献在中国专利中的引用中，27%来自国内文章，而 22%来自美国文章。

rss · arXiv Quantitative Finance · Jun 26, 04:00

**背景**: 专利 frequently 引用科学文章以建立在已有知识之上，引用频率可用于衡量创新对外部科学的依赖程度。研究者通过计算专利文献中对科学文献的引用次数来量化这些关联，这一方法建立在吸收能力和知识溢出的概念之上。通过比较国内产和国外产论文的引用比例，该研究评估了中国对美国科学依赖的变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/100786104/The_Links_Between_Hotspot_Patents_and_Publicly_Funded_Scientific_Research">(PDF) The Links Between Hotspot Patents and... - Academia.edu</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6905866/">Science quality and the value of inventions - PMC - NIH</a></li>
<li><a href="https://arxiv.org/html/2606.26470">The Growing Self-Reliance of Chinese Innovation</a></li>

</ul>
</details>

**标签**: `#innovation`, `#technology policy`, `#China-US relations`, `#patent analysis`, `#scientific dependence`

---

<a id="item-7"></a>
## [Codex 使用数据显示 2026 年初代理 AI 增长五倍](https://arxiv.org/abs/2606.26959) ⭐️ 8.0/10

对 OpenAI Codex 工具的分析显示，代理 AI 活跃用户在 2026 年上半年增长超过五倍，OpenAI 内部使用几乎普及，而外部组织采用虽然上升但仍不均衡。 这些发现提供了代理 AI 如何重塑工作模式的实证证据，表明各行业可能实现生产力提升和劳动力重组。 通过隐私保护的数据管道，研究发现超过 10% 的用户每周同时运行三个以上 Codex 代理，26.6% 使用技能来构建复杂工作流，提交需多小时完成任务的用户比例增长近十倍，而法律岗位和研究人员的输出 token 分别增加了 13 倍和 50 倍。

rss · arXiv Quantitative Finance · Jun 26, 04:00

**背景**: 代理 AI 指的是能够在多步骤过程中自主追求目标而无需每步人工批准的系统，这与单轮 AI 助手不同。OpenAI 的 Codex 是一种结合 ChatGPT 的代理编码工具，可通过命令行界面、IDE 插件或网页应用访问，以执行软件开发任务。该论文采用隐私保护的数据管道，分析了个人账户、组织账户以及 OpenAI 内部的使用日志，同时确保用户数据安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#Codex`, `#AI adoption`, `#human-AI interaction`, `#software engineering`

---