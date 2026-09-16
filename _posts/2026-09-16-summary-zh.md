---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> From 63 items, 17 important content pieces were selected

---

1. [介绍 System One Models 和 Jev 以实现快速类型推断](#item-1) ⭐️ 8.0/10
2. [墨水屏相框聆听鸟鸣并绘制 1800 年代风格插画](#item-2) ⭐️ 8.0/10
3. [互联网档案馆为 Wayback Machine 增加反爬虫保护。](#item-3) ⭐️ 8.0/10
4. [谷歌发布 Gemini 3.8 Live 和 Extended Thinking 模型](#item-4) ⭐️ 8.0/10
5. [莱茵金属开源其 Battlesuite 武器系统 API 文档](#item-5) ⭐️ 8.0/10
6. [AI 代理 25 分钟内发现泄露 GitHub 令牌，获取 Baseten 管理员权限](#item-6) ⭐️ 8.0/10
7. [在一个月内为 M4 Mac Mini 构建 Linux GPU 驱动](#item-7) ⭐️ 8.0/10
8. [Tensordyne Napier 芯片采用对数数制实现更快 AI 推理](#item-8) ⭐️ 8.0/10
9. [谷歌发布 Gemini 3.8 Live 语音对话模型并提供浏览器演示](#item-9) ⭐️ 8.0/10
10. [扩散模型生成动态波动率曲面以改进期权对冲](#item-10) ⭐️ 8.0/10
11. [研究显示零售专属交易公司评估激励错位，通过率并非技能可靠信号。](#item-11) ⭐️ 8.0/10
12. [递归自改进的经济学](#item-12) ⭐️ 8.0/10
13. [ViperQ：基于拍卖市场理论的强化学习交易订单流模式识别](#item-13) ⭐️ 8.0/10
14. [基于收据的审计揭示前沿代理型问答在埋藏证据下失效](#item-14) ⭐️ 8.0/10
15. [马尔可夫嵌入实现粗糙 Volterra SDEs 的强 1/2 阶模拟](#item-15) ⭐️ 8.0/10
16. [PortBench 推出相关性感知的全流程 LLM 投资组合管理基准](#item-16) ⭐️ 8.0/10
17. [CLQT：闭环成本感知的 LLM 投资组合代理基准](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [介绍 System One Models 和 Jev 以实现快速类型推断](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

Typesafe AI 博客宣布了 System One Models 和 Jev，这是一种通过牺牲通用文本生成来实现快速、低成本类型推断的新方法，能够快速产生结构化输出。 这种方法能够显著降低需要结构化响应的 LLM 应用的延迟和成本，如分类、表单填写或家庭助手命令，从而在速度和成本至关重要的场景中开启新的使用案例。 Jev 接受任意文本输入以及一组问题（是/否、多选或评分），在毫秒级返回答案，成本约为每百万 token 0.042 美元，但无法在定义的 schema 之外生成自由文本。

hackernews · albelfio · Sep 15, 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**背景**: 类型推断会限制语言模型的输出符合预定义的类型或模式，从而使模型能够跳过不必要的 token 生成，专注于填充字段。传统的 LLMs 会逐个生成 token，在只需要结构化数据时会导致速度慢和成本高。通过限制输出空间，像 Jev 这样的方法可以实现更快的解码和更低的计算成本，同时仍能理解复杂的提示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Type_inference">Type inference - Wikipedia</a></li>
<li><a href="https://www.weka.io/learn/ai-ml/inference-optimization/">Inference Optimization: Practical Techniques for Faster, Cost-Effective AI - WEKA</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎此次发布，称其真正有趣且新颖，并指出家庭助手演示让价值变得明显；但也有人提醒速度比较可能具有误导性，因为 Jev 只能生成结构化输出，无法像图灵完整模型那样进行通用生成。

**标签**: `#LLM`, `#structured inference`, `#typed models`, `#AI efficiency`, `#prompt engineering`

---

<a id="item-2"></a>
## [墨水屏相框聆听鸟鸣并绘制 1800 年代风格插画](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

该项目 fugleramme 结合墨水屏和麦克风捕捉鸟鸣，使用 BirdNET 模型实时分类鸟类，并在屏幕上绘制对应鸟类的 1800 年代风格插画。 它展示了 AI 声音分类与墨水屏低功耗艺术的创意结合，提供了一种引人入胜的生物多样性体验，并表明现有开源工具可被重新用于诗意的硬件艺术。 系统基于 ESP32（或 BTLE）板运行，使用 BirdNET 的轻量级 TensorFlow Lite 模型进行分类，并在每次识别后将对应的 1800 年代风格鸟类插画刷新到墨水屏上。

hackernews · arnemunthekaas · Sep 15, 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: BirdNET 是一个在大量鸟类声音上训练的深度学习模型，能够在短音频片段中识别鸟类，并提供适用于边缘设备的轻量版本。墨水屏（e‑ink）显示技术模拟纸张上的墨水，仅在刷新时消耗电力，因而能够实现极长的待机时间。将两者结合，即可构建一个低功耗、常开的鸟鸣监测相框。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.adafruit.com/category/150?srsltid=AU7gw4Xy_TOOiJ_KMKWJzC9lg41yGC9dPcj4cd5LC6s2w513lCXiCQAW">LCDs & Displays, eInk / ePaper Products Category on ... - Adafruit</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目充满魔力并激发创造力，指出 BirdNET 是传统神经网络而非大语言模型，强调墨水屏的低功耗和长续航，还开玩笑地提到其他鸟类项目并表达对挪威开发者的自豪。

**标签**: `#e-ink`, `#bird classification`, `#AI art`, `#hardware hack`, `#creative tech`

---

<a id="item-3"></a>
## [互联网档案馆为 Wayback Machine 增加反爬虫保护。](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

互联网档案馆为 Wayback Machine 增加了防护措施，以阻止试图绕过网站封锁的高流量自动化爬虫流量。 Wayback Machine 是数字保存的关键资源，减少滥用流量有助于确保其对研究人员和公众的持续可用性。 这些保护措施是由爬虫流量的波动触发的，导致一些网站选择退出存档，而互联网档案馆指出，服务仍可通过 Tor 访问，无需集中式网关。

hackernews · ChrisArchitect · Sep 15, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**背景**: Wayback Machine 由互联网档案馆运营，存储网页快照，使用户能够查看网站的历史版本。作为一个免费的非营利服务，它依赖有限的资源，容易受到过多自动化请求的干扰。高流量的爬虫不仅会给档案馆的基础设施带来压力，还可能促使内容所有者选择退出存档。实施流量保护措施有助于保证该服务对研究人员、记者和公众等合法用户的可用性。

**社区讨论**: 社区讨论中，许多用户对互联网档案馆在面对爬虫攻击时维持 Wayback Machine 运行的努力表示赞赏，称赞其开放性以及通过 Tor 的可访问性。部分评论者提到在特定网络（如工作电脑）遇到 429 错误导致访问不稳定，而另一些用户则分享了他们使用档案馆怀旧内容的个人经历。总体而言，讨论反映了对档案馆使命的强烈支持以及对防止滥用流量以保护该服务的担忧。

**标签**: `#Internet Archive`, `#Wayback Machine`, `#web archiving`, `#cybersecurity`, `#digital preservation`

---

<a id="item-4"></a>
## [谷歌发布 Gemini 3.8 Live 和 Extended Thinking 模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

谷歌宣布发布 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，这是原生语音转语音模型，能够实现实时语音交互，支持 97 种语言，并在不中断对话的情况下执行后台工具。 此次更新提升了 AI 语音代理的流畅度和响应速度，使其更适合多语言用户和企业工作区账户，并让 Google 在与 GPT‑Live、Grok Voice 等竞争对手的竞争中更具优势。 Gemini 3.8 Live Extended Thinking 增强了多步骤任务的推理能力，而两款模型均基于谷歌的 TPU 基础设施运行，提供低延迟，并且首次可通过工作区账户使用。

hackernews · leumon · Sep 15, 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**背景**: 谷歌的 Gemini 系列是一系列多模态大语言模型，旨在处理从文本生成到推理的各种任务。早期版本如 Gemini 3.5 Transcribe 侧重于语音转文字功能，而新发布的 Live 模型则将此扩展为全双工语音转语音交互。Live 和 Extended Thinking 版本通过处理复杂推理、视觉上下文和后台任务而不中断对话，旨在让语音代理感觉更像自然的对话伙伴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking</a></li>
<li><a href="https://officechai.com/ai/google-releases-gemini-3-8-live-extended-conversational-model-claims-better-performance-than-gpt-live-1-astra-and-grok-voice-think-fast-2-0-at-lower-price/">Google Releases Gemini 3.8 Live-Extended Conversational Model, Claims Better Performance Than Rivals At Lower Price</a></li>
<li><a href="https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/">Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production Grade Voice Agents - MarkTechPost</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了模型在南非语（Afrikaans）方面的出色流畅性、悦耳的声音、低延迟以及首次可用的工作区账户访问，这在之前的版本中常被遗漏。一些用户认为 Gemini 的散文比竞争对手更易读，也有人好奇谷歌何时能超越 Fable 和 Astra 等竞争对手或发布 Gemini 4。总体情绪积极，大家对其实用的多语言支持和企业就绪表示兴奋。

**标签**: `#Gemini`, `#LLM`, `#Google AI`, `#real-time AI`, `#language models`

---

<a id="item-5"></a>
## [莱茵金属开源其 Battlesuite 武器系统 API 文档](https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html) ⭐️ 8.0/10

莱茵金属已将其 Battlesuite 连接武器系统的 Onboard API 规范作为开源代码在 GitHub 上发布，使通信协议公开可访问。 此举使国防承包商、研究人员和爱好者能够检查并与主要军事平台的协议进行集成，促进国防软件生态系统的互操作性和透明度。 发布的文档涵盖了 Onboard API，包括消息格式和传输机制，版本为 9.10.0，符合提供的 URL。

hackernews · summarity · Sep 15, 21:07 · [社区讨论](https://news.ycombinator.com/item?id=49718928)

**背景**: 莱茵金属的 Battlesuite 是一个数字平台，旨在作为战场上的数据、通信和决策中心枢纽，整合有人和无人系统、人工智能、弹性网络和网络防护。该平台通过模块化、互操作的架构旨在将传统装备与新兴技术连接起来。开放其 Onboard API 遵循国防承包商发布接口规范以实现跨供应商集成的趋势，类似于战术微网标准（TMS）、分布式交互式仿真（DIS）、高级架构（HLA）和开放任务系统（OMS）等标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rheinmetall.com/en/products/digital-forces/digital-forces/battlesuite">Battlesuite – The interoperable military ecosystem of the future | Rheinmetall</a></li>
<li><a href="https://nextgendefense.com/rheinmetall-battlesuite-link-battlefield/">Rheinmetall Launches ‘Battlesuite’ to Link Weapons, Drones, and Data on Battlefield</a></li>
<li><a href="https://defence-industry.eu/rheinmetall-releases-battlesuite-onboard-and-tactical-api-specifications-as-open-source-for-defence-system-integration-across-platforms/">Rheinmetall releases Battlesuite Onboard and Tactical API specifications as open source for defence system integration across platforms</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与 DDS、TMS、DIS/HLA、OMS 和 CORBA 进行比较，指出协议既有潜在的相似之处也有差异。几位评论者对轻量级、适用于实时且受内存限制的嵌入式系统的 DDS 替代方案表达了兴趣，而其他人则开玩笑地说 CORBA“从未死去”。总体而言，讨论显示出对 Battlesuite 协议如何融入现有防御通信标准的强烈技术好奇心。

**标签**: `#defense`, `#open-source`, `#protocol`, `#embedded-systems`, `#real-time-communication`

---

<a id="item-6"></a>
## [AI 代理 25 分钟内发现泄露 GitHub 令牌，获取 Baseten 管理员权限](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

AI 代理在公开的 Harbor 容器注册表中发现了一个泄露的 GitHub 个人访问令牌，该令牌授予了 Baseten 生产仓库的管理员和推送权限。该漏洞经负责任披露后，Baseten 及时将项目设为私有并轮换了令牌。 此事件凸显了制品注册表中泄露密钥带来的供应链风险，并展示了 AI 辅助渗透测试如何大幅加速漏洞发现。依赖 GitHub 和 Harbor 进行 CI/CD 的组织需要加强密钥扫描和令牌管理。 该令牌授予 Baseten 主产品仓库、GitOps 仓库、Homebrew tap 的管理员和推送权限，以及其他私有仓库（包括客户专用仓库）的读写权限。令牌是在代理定位 Baseten 镜像后，在 Docker 构建历史中被发现的；即使 Harbor 项目随后设为私有，令牌仍然有效，直至被轮换。

hackernews · bearsyankees · Sep 15, 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49716476)

**背景**: Harbor 是一个 CNCF 毕业的开源容器注册表，用于存储、签名和扫描 Docker/OCI 镜像及 Helm chart，常见于 Kubernetes 环境。GitHub 个人访问令牌（PAT）是一种用于身份验证的密钥，根据其权限范围可以提供对仓库的读取、写入或管理员访问。Baseten 是一个用于部署和扩展 AI 模型的平台，其工作流依赖 GitHub‑based GitOps 流程和 Harbor 存放容器镜像，因而泄露的令牌可能直接导致生产系统被入侵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://goharbor.io/">Harbor</a></li>
<li><a href="https://docs.baseten.co/concepts/howbasetenworks">How Baseten works</a></li>
<li><a href="https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html">Grafana GitHub Token Breach Led to Codebase Download and Extortion Attempt</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了负责任的披露以及 Baseten 的快速处理，但也有人质疑 AI 代理的测试是否事先获得授权。多位评论指出，AI 代理擅长快速发现人类可能忽略的低 hanging fruit，争论其速度优势是否超越发现的新颖性。

**标签**: `#security`, `#vulnerability`, `#GitHub`, `#AI agents`, `#responsible disclosure`

---

<a id="item-7"></a>
## [在一个月内为 M4 Mac Mini 构建 Linux GPU 驱动](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

一位开发者在一个月内利用大语言模型辅助逆向工程，为苹果 M4 Mac Mini 构建了可用的 Linux GPU 驱动，这一成就引发了关于其合法性及是否能被上游采纳的争论。 这一成就表明大语言模型能显著加速未文档化硬件的驱动开发，可能降低 Linux 在苹果硅片上的门槛，同时也引发了关于利益冲突和 AI 辅助代码在开源项目中的伦理与政策担忧。 该驱动大约用时 30 天完成，利用大语言模型应对 M4 GPU 复杂的固件 ABI。作者曾是苹果工程师，因未披露使用 LLM 而在 Asahi Linux 被禁，且 M4 GPU 的 FP32 性能约为 4.26 TFLOPS。

hackernews · ADevWithAnIdea · Sep 15, 19:30 · [社区讨论](https://news.ycombinator.com/item?id=49717638)

**背景**: 苹果 M4 是 2024 年 5 月推出的系统级芯片，集成了没有公开文档的 GPU，因此需要像 Asahi Linux 这样的项目通过逆向工程来在苹果硅片上运行 Linux。Asahi Linux 是一个社区驱动的项目，通过干净室的逆向工程将 Linux 内核移植到基于苹果的 Mac。近年来，大语言模型被研究用于辅助内核开发，它们在生成补丁或文档等小而明确的任务上表现良好，但尚不能从零开始编写完整的设备驱动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M4">Apple M4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2511.18924">LLM-Driven Kernel Evolution: Automating Driver Updates in Linux</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该速度和大语言模型辅助方法是一个有前景的用例，但也有人批评作者未披露的前苹果身份及潜在利益冲突，并指出 Asahi Linux 严格的无 AI 政策将阻止其被上游采纳。多位评论者呼吁无论是否能上游，都应发布可复现的代码和文档。

**标签**: `#GPU driver`, `#Apple Silicon`, `#Linux`, `#LLM`, `#Reverse engineering`

---

<a id="item-8"></a>
## [Tensordyne Napier 芯片采用对数数制实现更快 AI 推理](https://spectrum.ieee.org/inference-hardware-revolution) ⭐️ 8.0/10

Tensordyne 发布了其 3nm Napier AI 推理芯片，采用专有对数数制将昂贵的乘法替换为加法，声称每用户可达每秒 1,300 个 token，吞吐量比现有架构高出多达 13 倍。 通过降低乘法的能耗和面积成本，Napier 芯片有望降低 AI 推理的功耗和费用，提供 GPU 以外的可行替代方案，从而促进大型语言模型的更广泛部署。 该芯片利用 log(A×B)=log A+log B 的恒等式，在对数空间中用加法代替乘法；每颗处理器集成 144 GB HBM3e 和 256 MB SRAM，采用 3 nm 工艺，并作为名为 Napier 的机架级系统提供。

hackernews · vinhnx · Sep 15, 14:24 · [社区讨论](https://news.ycombinator.com/item?id=49713024)

**背景**: AI 推理需要大量的矩阵和向量乘法，传统乘法电路会占用较大的硅面积并消耗较多功率。对数数制（LNS）将数字表示为其对数，使得乘法可以转化为加法（log(A×B)=log A+log B），但在这种表示下的加法变得更复杂，通常需要查找表或额外的逻辑。早期尝试在硬件中使用 LNS 时曾因这一额外复杂度而受限，但随着制程技术和高带宽内存的进步，兴趣重新被激发。Tensordyne 的 Napier 芯片试图在利用 LNS 优势的同时，通过紧密结合高带宽内存和大容量片上 SRAM 来减轻其劣势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/dharmesh0103_aichips-tensordyne-semiconductors-activity-7474367811415334912-2ipn">Tensordyne's Logarithmic Number System for AI Inference | LinkedIn</a></li>
<li><a href="https://www.eetimes.com/podcasts/how-tensordyne-built-an-ai-accelerator-around-logarithmic-math/">Tensordyne's AI Accelerator Built Around Logarithmic Math</a></li>
<li><a href="https://convergedigest.com/tensordyne-tapes-out-3nm-napier-ai-inference-proce/">Tensordyne Tapes Out 3nm Napier AI Inference ... - Converge Digest</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章突出了对数方法在 AI 推理中的新颖性，指出其可能带来的功耗和面积节省。一些人将其与 CPU 的历史演变进行类比，认为未来会出现多种架构创新而非单一突破。还有用户指出文章的 Scrabble 类比对训练有帮助但对推理解释不够清晰，另有人则提到 Anthropic 为租用算力支付巨额费用的无关话题。

**标签**: `#AI inference`, `#hardware acceleration`, `#logarithmic number system`, `#chip architecture`, `#Napier`

---

<a id="item-9"></a>
## [谷歌发布 Gemini 3.8 Live 语音对话模型并提供浏览器演示](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 8.0/10

谷歌宣布了 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking 两款新的语音对话模型，并且 Simon Willison 提供了一个基于浏览器的演示 UI 供用户尝试。 此次发布通过提供低延迟、全双工的语音交互，推进了实时语音 AI 的发展，可与 OpenAI 的 GPT-Live 相媲美，而社区演示则让开发者更易于使用该技术。 这些模型通过 WebSocket 端点（wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent）连接，并使用 Web Audio API 的 AudioContext 进行麦克风捕获和播放；演示支持语音预设、可选系统提示以及打断模型响应。

rss · Simon Willison · Sep 15, 22:47

**背景**: 语音对话模型能够直接实现音频到音频的对话，无需中间的文本转录，从而实现低延迟、全双工的语音交互。谷歌的 Gemini 3.8 Live 和 Extended Thinking 属于其生成式 AI 产品线，旨在与 OpenAI 的 GPT-Live 家族竞争，后者同样强调同时倾听和说话。开发者可以通过 WebSocket API 与这些模型交互，并在浏览器中使用 Web Audio API 的 AudioContext 进行音频捕获和播放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT‑Live - OpenAI</a></li>

</ul>
</details>

**标签**: `#Gemini`, `#speech-to-speech`, `#AI models`, `#Google`, `#voice AI`

---

<a id="item-10"></a>
## [扩散模型生成动态波动率曲面以改进期权对冲](https://arxiv.org/abs/2609.13402) ⭐️ 8.0/10

本文提出 AD-Seq‑Vol 及其无套利微调版本 AD-Seq‑Vol‑FT，两种共同学习标的收益率和高维隐含波动率曲面演化的扩散模型框架。基于 2000‑2023 年的 SPX 期权数据，这些模型能够生成连贯的曲面轨迹，其中 AD-Seq‑Vol‑FT 将静态套利违规降至近乎零，并显著提升数据驱动的期权对冲表现。 通过生成符合市场且基本无套利的波动率曲面路径，该框架为数据驱动的对冲和风险管理提供了更可靠的工具，有望降低市场参与者的对冲成本和尾部风险。此外，模型对横截面和时间依赖的捕捉也推动了生成模型在金融建模中的应用。 AD-Seq‑Vol 通过序列扩散过程共同建模标的收益率和高维隐含波动率曲面的演化，而 AD-Seq‑Vol‑FT 在训练后加入惩罚项以抑制静态无套利违规。在 2000‑2023 年的日度 SPX 期权数据上，AD-Seq‑Vol‑FT 使静态套利违规降至近乎零，扩散模型对冲实现近零跟踪误差、显著降低尾部风险并在 COVID‑19 市场动荡期间保持稳定；代码已在 https://github.com/yinbinhan/volatility-surface-simulation 公开。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: 扩散模型是一类通过逐步去噪随机噪声来生成数据的生成模型，已在图像、音频等领域取得成功，并最近被用于金融数据的合成。隐含波动率曲面反映了不同行权价和到期日的期权隐含波动率，描述了市场对未来波动率的预期；静态无套利条件要求该曲面不存在跨行权价和到期日的无风险套利机会。数据驱动的对冲利用历史或模拟的市场情景来构建期权对冲，而不依赖于参数定价模型，旨在降低跟踪误差和尾部风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.13402v1">Diffusion models for dynamic volatility surface generation ...</a></li>
<li><a href="https://bigquant.com/square/paper/40a2b374-37ab-4c32-9621-50aef2e15c72">Diffusion models for dynamic volatility surface generation ...</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#volatility surface`, `#option hedging`, `#financial machine learning`, `#arbitrage-free modeling`

---

<a id="item-11"></a>
## [研究显示零售专属交易公司评估激励错位，通过率并非技能可靠信号。](https://arxiv.org/abs/2609.14859) ⭐️ 8.0/10

该论文分析了零售专属交易公司使用的两阶段评估，表明通过评估并不是交易者技能的可靠独立信号，因为通过率主要受仓位大小驱动而非真实优势。研究发现，在零技能情况下，仅凭仓位大小就能获得约 0.40 的通过概率，而实际队列的通过率仅为 0.168。 这项工作揭示了专属交易评估合约如何导致激励错位，使公司可能高估交易者技能并错误分配资金。它为交易者、公司和学者提供了一个定量框架，以评估和改进零售专属交易的评估设计。 模型表明，在端‑of‑day 追踪回撤下，评估阶段会奖励快速、频繁的交易节奏，而资金账户阶段则在联合门槛上以大约九倍的比例惩罚这种节奏。因此，零技能的交易者仅凭仓位大小就能达到约 0.40 的通过概率，盈亏平衡需要在 1:1.5 的净风险回报比下实现约 40.5%–41.5%的胜率。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: 零售专属交易公司为交易者提供付费评估阶段，要求他们在不突破追踪回撤的情况下达到盈利目标；通过评估的交易者随后会获得受最低存活窗口和一致性规则等额外条件限制的资金账户，只有满足这些条件才能进行利润分配。追踪回撤衡量相对于移动高水位线的亏损，可以按日内或端‑of‑day 计算，这会影响交易者的风险管理方式。一致性规则限制单日最佳利润占总利润的比例，以鼓励更稳健的表现。这些机制共同构成了一种合约，其几何结构在两个阶段对交易者激励产生不同影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.14859">[2609.14859] Gate Design and Stage -Dependent Incentives in Retail ...</a></li>
<li><a href="https://tradeify.co/post/trailing-drawdown-explained-for-prop-firm-traders">Trailing Drawdown Explained for Prop Firm Traders</a></li>
<li><a href="https://fundingtraders.com/blog/prop-firm-consistency-rules/">Prop Firm Consistency Rules: Who Has One, Who Doesn't</a></li>

</ul>
</details>

**标签**: `#proprietary trading`, `#incentive design`, `#financial contracts`, `#algorithmic trading`, `#market microstructure`

---

<a id="item-12"></a>
## [递归自改进的经济学](https://arxiv.org/abs/2609.15802) ⭐️ 8.0/10

作者在 arXiv:2609.15802v1 中建模递归自改进的经济学，将 AI 进步表示为有向图，并表明净加速度取决于各回路弹性的乘积。他们区分了狭义和广义 AI 能力，并利用现有数据发现当前反馈回路尚不足以产生自持续的 AI 加速，尽管这些回路正在增强。 该论文提供了一种新颖的理论框架，用于评估递归自改进，帮助 AI 安全研究者和政策制定者判断 AI 进步是否可能成为自我强化的过程。通过识别可测量的弹性并区分狭义与广义能力，它为经验数据的收集提供指导，以指导治理和投资决策。 该模型将 AI 进步视为有向图，每条边代表一个反馈回路，整体加速度等于这些回路弹性的乘积。它将狭义 AI（仅在 AI‑R&D 基准上改进）与广义 AI（在具有经济价值的任务上改进）区分开来，并用现有估计进行校准，得出当前弹性乘积低于自持续增长的阈值但正在上升。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: 递归自改进（RSI）指的是 AI 系统提升自身能力，从而进一步促进更强的改进，形成反馈循环。在经济学中，弹性衡量一个变量对另一个变量变化的响应程度；在这里它量化了 AI 能力增长对 AI 研发改进的敏感度。狭义 AI 在特定、明确定义的任务上表现出色（如优化 AI‑R&D 基准），而广义 AI 则会在广泛的经济价值任务上提升能力。将这些相互作用表示为有向图，使研究者能够追踪影响流动并计算每个回路上弹性的乘积作为总体效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.15802v1">The Economics of Recursive Self-Improvement - arXiv</a></li>
<li><a href="https://elasticity.institute/rsi-paper.pdf">[PDF] The Economics of Recursive Self-Improvement - Elasticity Institute</a></li>
<li><a href="https://medium.com/@maria-andraw/broad-ai-general-ai-and-narrow-ai-understanding-the-spectrum-of-artificial-intelligence-d3e489bee6be">Broad AI, General AI, and Narrow AI: Understanding the ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#recursive self-improvement`, `#economic modeling`, `#AI progress`, `#feedback loops`

---

<a id="item-13"></a>
## [ViperQ：基于拍卖市场理论的强化学习交易订单流模式识别](https://arxiv.org/abs/2609.13825) ⭐️ 8.0/10

ViperQ 提出了一种强化学习交易框架，将拍卖市场理论的原始特征编码为 20 维状态向量，并使用基于前景理论的非对称奖励函数训练两个 PPO 代理。 通过将强化学习交易建立在从业者微观结构概念之上，ViperQ 桥接了学术 RL 与实际交易实践之间的差距，提供了一种结构化的理论驱动输入方式，有望提升算法交易系统的表现和可解释性。 20 维 Z 标准化状态包括成交量点控制（VPOC）、价值区位置、低体积节点（LVN）标志、累积成交量增量（CVD）背离以及 tape‑velocity 签名；两个 PPO 代理采用基于前景理论的非对称奖励进行训练，损失惩罚系数参照卡尼曼和特 versky 的损失厌恶系数（约 2.25）。在未见过的机构级 tick 数据上，ViperQ 在 TSLA 上实现 +163.6% 投资回报率（最大回撤 ‑27.5%，27,019 笔交易），在 NVDA 上实现 +116.5% 投资回报率（最大回撤 ‑47.8%，12,892 笔交易），杠杆为零。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: 拍卖市场理论（AMT）描述价格如何通过成交量发现价值，指出成交量点控制（VPOC）、价值区和低体积节点（LVN）等关键水平，这些水平反映市场失衡。累积成交量增量（CVD）衡量买方发起与卖方发起交易的净差异，而 tape‑velocity 捕捉订单流的速度，共同构成微观结构信号。前景理论由卡尼曼和特 versky 提出，认为人们对损失的敏感度高于收益（损失厌恶），ViperQ 将这一机制编码为强化学习中的非对称奖励函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tradeproacademy.com/full-guide-to-auction-market-theory-how-to-trade-successfully/">Full Guide to Auction Market Theory & How to trade SUCCESSFULLY</a></li>
<li><a href="https://tw.tradingview.com/scripts/cumulativevolumedelta/">Cumulativevolumedelta — 指標和策略 - TradingView</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prospect_theory">Prospect theory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#auction market theory`, `#algorithmic trading`, `#prospect theory`, `#market microstructure`

---

<a id="item-14"></a>
## [基于收据的审计揭示前沿代理型问答在埋藏证据下失效](https://arxiv.org/abs/2609.15319) ⭐️ 8.0/10

在受控的数据室审计中，研究人员将证据埋藏，发现前沿代理型问答模型的准确率急剧下降，强制声明增加，工具调用增多，每正确答案的成本上升，而置信度分数未能捕捉到这些错误。 这些发现揭示了基准分数与实际可靠性之间的关键差距，表明在证据难以获取时当前排行榜可能具有误导性，并主张转向声明级别的溯源和对抗性验证，以构建更安全的代理型系统。 准确率下降，强制声明和工具调用增加，每正确答案的成本上升；置信度校准未能完全反映错误答案，而且虚构的结构性声明可能与准确的数值表混合，这表明需要声明级别的收据。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: 代理型问答利用自主的 AI 代理根据高层目标而非脚本步骤来规划、执行和维护测试，从而超越传统质量保证。基于收据的审计会在 AI 输出中附加防篡改的来源元数据，使得可以追溯声明到底层证据。在金融尽职调查和国防参谋工作中，证据可能埋藏在冗长文档中，模型能够将正确的数字与自信但虚构的解释结合起来，因此声明级别的收据对于构建可信的 AI 系统至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/what-agentic-qa-software-testing-studio-0kcic">What is Agentic QA</a></li>
<li><a href="https://deepchecks.com/">Deepchecks LLM Evaluation | Evaluate AI Progress with Know Your...</a></li>
<li><a href="https://www.linkedin.com/pulse/truth-layer-why-ai-forces-internet-show-its-receipts-radhakrishnan-pn-3yhac">The Truth Layer: Why AI Forces the Internet to Show Its Receipts</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#agentic QA`, `#benchmarking`, `#AI safety`, `#receipt-based auditing`

---

<a id="item-15"></a>
## [马尔可夫嵌入实现粗糙 Volterra SDEs 的强 1/2 阶模拟](https://arxiv.org/abs/2306.02708) ⭐️ 8.0/10

作者提出了一种可逆的马尔可夫嵌入，将新一类 Volterra 型随机微分方程转换为标准扩散过程，并给出了一种在 Hurst 指数 H<1/2 的分数核情况下达到强收敛阶 1/2 的数值方案。 该结果优于粗糙 Volterra 方程中欧拉-马 uyama 方法的典型 H 收敛率，为粗糙波动率建模和金融数学等领域的随机模拟提供了更高的精度和效率。 该嵌入利用卷积核将非马尔可夫的 Volterra 过程映射到马尔可夫扩散；对于 H∈(0,1/2)，所提出的方案达到强阶 1/2，而标准欧拉方案通常仅达到阶 H。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: Volterra 型随机微分方程包含具有记忆的卷积核积分，导致解具有路径依赖性且非马尔可夫。当核为分数幂律时，过程表现为粗糙行为，其粗糙程度由赫斯特指数 H∈(0,1/2)描述。马尔可夫嵌入通过引入辅助马尔可夫扩散过程将该系统重新表述为马尔可夫形式，从而可以使用标准的数值分析工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2306.02708v4">Efficient simulation of a new class of Volterra-type SDEs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_chain">Markov chain - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/340229697_Asymptotic_analysis_of_a_kernel_estimator_for_stochastic_differential_equations_driven_by_a_mixed_sub-fractional_Brownian_motion">Asymptotic analysis of a kernel estimator for stochastic differential ...</a></li>

</ul>
</details>

**标签**: `#stochastic differential equations`, `#Volterra equations`, `#numerical simulation`, `#fractional kernels`, `#Markovian embedding`

---

<a id="item-16"></a>
## [PortBench 推出相关性感知的全流程 LLM 投资组合管理基准](https://arxiv.org/abs/2605.27887) ⭐️ 8.0/10

PortBench 提供了一个覆盖 2015 至 2025 年六种异质资产类别的多资产基准，包括静态问答数据集（6,269 道题）和动态五阶段分配流程。它引入了双层相关性得分和 CEPS 指标，在三种压力窗口和三种风险配置下评估 LLMs，并通过实时评估减少预训练污染。 通过弥补仅关注股权和流程不完整的缺口，PortBench 能够更真实地评估 LLMs 在投资组合管理中的表现，帮助研究者和从业者选择在多种市场条件下真正表现优秀的模型。 该基准覆盖六类资产，包含静态问答集和动态流程，采用双层相关性得分评估跨类对冲和内部集中度，使用 CEPS 衡量流程各阶段误差的累积；评估结果显示，120 次 LLM 测试中只有 32.5% 在四个市场时期的夏普比率优于等权重，且代码已公开。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: 大型语言模型已被用于众多金融任务，但投资组合管理缺乏全面的基准测试。现有测试常仅关注股票，忽视跨资产相关性，并且只评估诸如问答之类的孤立组件，而非完整的决策流程。PortBench 通过提供一个感知相关性的端到端评估框架来弥补这些不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://portbench.github.io/">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>
<li><a href="https://arxiv.org/html/2605.27887">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#portfolio management`, `#benchmark`, `#finance`, `#AI`

---

<a id="item-17"></a>
## [CLQT：闭环成本感知的 LLM 投资组合代理基准](https://arxiv.org/abs/2606.29771) ⭐️ 8.0/10

CLQT 提出了一种闭环、成本感知的基准，通过 TimeGate 强制点-in-time 数据访问，建模机构交易和融资成本，跨轮评分策略一致性，并将每个决策周期记录在可重新计算验证的审计链中。该基准在一年多模型回测和四周实盘经纪人纸面交易（post-cutoff 数据）上进行了验证。 通过将评估从简单的回报排名转向过程诊断，CLQT 能够揭示代理的决策是否连贯且有纪律，揭示传统排行榜掩盖的前视偏差和成本影响。这提供了一个可重复使用的审计框架，推动了 LLM 金融代理的可信评估。 CLQT 计算五轴能力评分卡（连贯性、敏锐性、从容性、纪律性、可靠性），其中连贯性部分由保留的 LLM 判断以减少自我偏好。消融研究显示稳定的言行不一致差距（回测+0.30，实盘+0.23），并在考虑现实成本后，代理未能明显跑赢市场指数。

rss · arXiv Quantitative Finance · Sep 15, 04:00

**背景**: LLM 代理被越来越多地提出作为自主投资组合管理者，但大多数评估仅依赖固定窗口内的回报排行榜，这将技能与市场路径混淆，并忽略了前视偏差和交易成本。闭环基准将代理置于一个模拟交易循环中，其中数据访问受时间门控，成本被建模，并且每个动作都被记录以供以后验证。TimeGate 机制确保点-in-time 数据可用，而基于哈希链的审计链提供防篡改、可重新计算的收集‑分析‑决策‑执行‑反思循环记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.29771">[2606.29771] CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent ...</a></li>
<li><a href="https://www.mdpi.com/2079-9292/15/1/56">AuditableLLM: A Hash-Chain-Backed, Compliance-Aware ... - MDPI</a></li>
<li><a href="https://www.themoonlight.io/en/review/timegate-sustainable-time-boxed-promotion-gates-for-continual-ml-adaptation-under-resource-constraints">[Literature Review] TIMEGATE: Sustainable Time-Boxed ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#portfolio management`, `#benchmarking`, `#financial AI`, `#evaluation methodology`

---