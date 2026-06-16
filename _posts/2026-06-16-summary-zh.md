---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> From 42 items, 16 important content pieces were selected

---

1. [vLLM v0.23.0 发布，包含 DeepSeek-V4 优化和 Model Runner V2 扩展](#item-1) ⭐️ 8.0/10
2. [恶意领英职位伪装 npm 后门在 GitHub 仓库中。](#item-2) ⭐️ 8.0/10
3. [禁书图书馆隐藏在 Wi‑Fi 智能灯泡中](#item-3) ⭐️ 8.0/10
4. [Iroh 1.0 发布支持可插拔传输的 P2P 库，实现直接应用间通信](#item-4) ⭐️ 8.0/10
5. [HN 用户讨论用本地模型替代 Claude/GPT 进行编码。](#item-5) ⭐️ 8.0/10
6. [无人经济？技术上并非不可能](#item-6) ⭐️ 8.0/10
7. [福克斯据报道寻求收购流媒体巨头 Roku](#item-7) ⭐️ 8.0/10
8. [Salesforce 将以 36 亿美元收购 Fin（前身为 Intercom）](#item-8) ⭐️ 8.0/10
9. [TimescaleDB 的 Hypercore 压缩技术用于时序数据](#item-9) ⭐️ 8.0/10
10. [Anthropic 推出 Claude Corps 非营利组织奖学金计划](#item-10) ⭐️ 8.0/10
11. [分析显示 Rust 与 C/C++ 的内存安全 CVE 差异](#item-11) ⭐️ 8.0/10
12. [基于英国生活满意度调查估算公众社会福利函数](#item-12) ⭐️ 8.0/10
13. [在价格不确定性下使用均值-CVaR 建模电池出价](#item-13) ⭐️ 8.0/10
14. [量子视界：评估量子对比特币和以太坊的威胁](#item-14) ⭐️ 8.0/10
15. [新型 Lookahead Propensity 统计量检测 LLM 预测偏差](#item-15) ⭐️ 8.0/10
16. [新投影估计器从期权组合中提取风险中性依赖。](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.23.0 发布，包含 DeepSeek-V4 优化和 Model Runner V2 扩展](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 8.0/10

vLLM v0.23.0 包含来自 200 名贡献者的 408 次提交（其中 63 人为新贡献者），并在多个后端对 DeepSeek-V4 进行了主要优化。它将 Model Runner V2 设为 Llama 和 Mistral 密集模型的默认选项，新增 FlashInfer 采样器、可中断的 CUDA 图、流水线并行气泡消除以及统一解析器，并带来其他内核和性能增强。 这些改进显著提升了诸如 DeepSeek-V4 这类最先进的混合专家模型的推理吞吐量和延迟，使得大规模 AI 应用的部署更快。通过将 Model Runner V2 扩展到更多架构并增加 Rust 前端功能，vLLM 扩大了其硬件和语言支持，巩固了其作为领先开源 LLM 推理引擎的地位。 DeepSeek-V4 获得了解耦的稀疏 MLA 元数据、TRTLLM-gen 注意力内核、对 Mega-MoE 的 EPLB 支持、选择性前缀缓存保留、DSA MTP 的索引共享功能，并脱离 torch.compile，注意力和 RoPE 路径被重构，新增 XPU 注意力解码路径。Model Runner V2 成为 Llama 和 Mistral 密集模型的默认选择，新增 FlashInfer 采样器、可中断的 CUDA 图、流水线并行气泡消除、混合模型的内核块大小支持、Gemma 4 MTP；Rust 前端加入流式 generate、动态 LoRA 端点以及版本/服务信息 API；多层级 KV 缓存卸载增加对象存储二级层和按请求策略，统一解析器整合了推理和工具调用处理。

github · khluu · Jun 15, 05:27

**背景**: vLLM 是一个高吞吐量、内存高效的库，用于服务大型语言模型，采用 PagedAttention 和连续批处理等技术来最大化 GPU 利用率。Model Runner V2 是对 vLLM 核心执行引擎的重新设计，旨在通过从第一原则重新实现模型运行器来实现更清晰、更模块化的代码和更好的性能。DeepSeek‑V4 是 2026 年发布的混合专家语言模型，参数规模最高可达 1.6 万亿，支持长达一百万标记的上下文长度，需要专门的内核来实现高效推理。TRTLLM‑gen 注意力内核是基于 TensorRT‑LLM 的实现，提供了针对生成阶段的优化注意力操作，通常需要特定的 KV‑cache 布局，例如在较新 GPU 上的 HND 布局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html">Multi-Head, Multi-Query, and Group-Query Attention — TensorRT-LLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#Model Runner V2`, `#release`

---

<a id="item-2"></a>
## [恶意领英职位伪装 npm 后门在 GitHub 仓库中。](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 8.0/10

一名领英招聘者冒充招聘经理，向求职者发送一个 prétend 为破损的 Node.js 项目的公开 GitHub 仓库。该仓库的 npm prepare 脚本在 `npm install` 后自动运行，执行连接攻击者控制服务器的后门。 此事件展示了攻击者如何将社会工程学与软件供应链战术结合，以求职者为目标——这一群体在面试任务中评估代码时可能警觉性较低。这也凸显了开发者审查 npm 生命周期脚本的必要性，以及平台改进恶意仓库举报和下架机制的紧迫性。 恶意 payload 隐藏在仓库的 `prepare` 脚本中，npm 在依赖安装后会自动执行该脚本，使攻击者能够在受害者机器上运行任意代码。该脚本被埋藏在大量注释掉的测试文件之间，随意检查难以发现威胁。

hackernews · lwhsiao · Jun 15, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: npm 在执行 `npm install` 后会自动运行包的 `prepare` 脚本，此机制原本用于构建本地资源等任务，但也可能被滥用以执行任意代码。npm 生态系统中的供应链攻击日益普遍，威胁行为者通过发布或破坏包来分发恶意软件，正如最近的 CISA 警报所示。了解这些机制有助于开发者识别看似无害的仓库在依赖安装时可能触发的危险行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/?v=true">scripts - npm Docs</a></li>
<li><a href="https://www.tutorialpedia.org/blog/why-is-npm-running-prepare-script-after-npm-install-and-how-can-i-stop-it/">Why Does npm Run the Prepare Script After npm install? (And ...</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem</a></li>

</ul>
</details>

**社区讨论**: 评论者指出此类骗局正变得越来越频繁且令人信服，许多人在过去几个月里多次遇到类似尝试。他们对缺乏明确的网络犯罪举报渠道感到沮丧，并指出即使向 GitHub 和 LinkedIn 报告，恶意仓库也常常仍然在线。一些人建议求职者在检查不明代码之前应避免直接运行 `npm install`。

**标签**: `#security`, `#supply-chain attack`, `#npm`, `#LinkedIn scam`, `#social engineering`

---

<a id="item-3"></a>
## [禁书图书馆隐藏在 Wi‑Fi 智能灯泡中](https://www.richardosgood.com/posts/banned-book-library/) ⭐️ 8.0/10

开发者改装了一款基于 ESP8266 的 Wi‑Fi 智能灯泡，使其运行一个隐藏的 HTTP 服务器，托管诸如杰克·伦敦的《野性的呼唤》和马克·吐温的《哈克贝利·费恩历险记》等禁书的 EPUB 文件，以便在局域网内隐蔽获取审查文学作品。 该项目展示了低成本的物联网硬件如何被改造用于规避审查，提供了一种保护言论自由和隐私的易于获取的方法，尤其在限制性环境中具有重要意义。 该灯泡的 ESP8266 芯片被刷入自定义的 Tasmota/ESPHome 固件，从而运行一个轻量级 Web 服务器来提供存储的 EPUB 文件；受限于闪存容量（通常约 1 MB），只能存放少量文本，且需要处于同一局域网或通过 mDNS 发现设备才能访问。

hackernews · sohkamyung · Jun 15, 22:37 · [社区讨论](https://news.ycombinator.com/item?id=48547985)

**背景**: ESP8266 是一种低成本的 Wi‑Fi 微控制器，常用于 DIY 智能家居设备如 Wi‑Fi 灯泡，可被重新刷入开源固件如 Tasmota 或 ESPHome 以添加自定义功能。通过在芯片上运行嵌入式 HTTP 服务器，灯泡能够直接在同一网络的客户端之间提供文件，这在多个 IoT 网页服务器教程中有所演示。此方法与早期的 PirateBox 项目类似，后者将无线接入点改造成离线文件共享中心，表明简单硬件也可用于规避基于网络的审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.instructables.com/DIY-IoT-Lamp-for-Home-Automation-ESP8266-Tutorial/">DIY IoT Lamp for Home Automation || ESP8266 Tutorial : 13 Steps (with Pictures) - Instructables</a></li>
<li><a href="https://admantium.medium.com/tasmotizer-try-to-flash-a-wifi-led-light-with-a-custom-firmware-e9f0baed3bca">Tasmotizer: Try to Flash a WiFi LED Light with a Custom Firmware | by Sebastian | Medium</a></li>
<li><a href="https://www.microej.com/vee-features/hoka-http-web-server/">MicroEJ - Hoka HTTP Web Server for IoT Devices</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目的创意及其与言论自由的关联，认为这种低成本的硬件黑客行为有助于保存对审查作品的访问。几位评论者将其与 PirateBox 进行比较，并提出将想法扩展为使用太阳能灯的 mesh 网络。总体情绪积极，许多人表达了对正式化或扩展该概念的兴趣。

**标签**: `#hardware hacking`, `#IoT`, `#censorship circumvention`, `#DIY`, `#free speech`

---

<a id="item-4"></a>
## [Iroh 1.0 发布支持可插拔传输的 P2P 库，实现直接应用间通信](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 是一个用 Rust 编写的点对点网络库，已发布，能够通过公钥直接让应用间通信，使用 QUIC 并提供可插拔传输，开发者可自行扩展。 通过抽象传输细节并消除对中心化协调的需求，Iroh 简化了去中心化应用的构建，降低了开发者创建有弹性的点对点服务的门槛。其可扩展的传输模型使应用能够在各种网络环境中工作，而无需用户管理账户或外部 VPN 客户端。 Iroh 使用 QUIC 进行洞穿打孔的直接连接，提供 iroh‑blobs 层实现内容寻址数据传输，内置 IPv4、IPv6 和中继传输，并允许开发者用 Rust 实现自定义传输以避免特性标记爆炸。其 API 围绕通过公钥拨号展开，自动选择最快路径并维持连接。

hackernews · chadfowler · Jun 15, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48542480)

**背景**: 点对点（P2P）网络使设备能够在不依赖中心服务器的情况下直接通信，通常需要 NAT 穿越技术（如洞穿打孔）来在私有网络之间建立连接。QUIC 是一种现代传输协议，结合了低延迟的连接建立和内置加密，并支持基于 UDP 的洞穿打孔。可插拔传输最初由 Tor 项目提出用于规避审查，是一种可以转换网络流量的模块化组件，使核心协议能够通过更换自定义传输来适应不同的网络环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/n0-computer/iroh">n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. - GitHub</a></li>
<li><a href="https://www.iroh.computer/">Iroh</a></li>
<li><a href="https://torproject.gitlab.io/torspec/pt-spec.html">Pluggable Transport Specification (Version 1)</a></li>

</ul>
</details>

**社区讨论**: 评论者将 Iroh 与 Tailscale 进行比较，但指出其侧重于应用层，apitman 将其描述为“应用层的 Tailscale”。开发者强调了可扩展传输的必要性，rklaehn 解释说自定义传输的支持可以避免难以维护的特性标记迷宫。一些用户要求更清晰地解释用于拨号的加密密钥，而另一些人则质疑另一层 P2P 的必要性，还有少数人对去中心化网络的可能性表达了热情。

**标签**: `#peer-to-peer`, `#networking`, `#Iroh`, `#release`, `#custom transports`

---

<a id="item-5"></a>
## [HN 用户讨论用本地模型替代 Claude/GPT 进行编码。](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

一个 Ask HN 帖子询问是否有人已经将 Claude 或 GPT 完全替换为本地模型作为主要编码工具，促使用户分享他们的设置、性能数字以及数据隐私和成本节约等动机。 此次讨论凸显了向本地运行的大语言模型转变的趋势，反映了对隐私、订阅成本的担忧以及对离线、可定制 AI 助手的需求。 用户报告的设置包括在配备 128 GB RAM 的 Mac Studio 上运行 Qwen3.6‑35B（仅 3B 活跃参数），以及双 RTX3090 工作站通过 Unsloth Studio 运行 Qwen 和 Gemma 模型达到约 150 token/s，并指出虽然性能足以完成大多数编码任务，但仍不及 Claude Code 等前沿模型。

hackernews · cloudking · Jun 15, 14:46

**背景**: 本地大语言模型是指可以在个人硬件上运行的开放权重或源代码可用的模型，提供离线推理和相比专有 API 更高的数据隐私。阿里巴巴云开发的 Qwen 系列包括在 Apache 2.0 许可下发布的 Qwen3.6‑35B 等模型。谷歌 DeepMind 的 Gemma 系列是一组轻量级的开放权重大语言模型，例如在 2026 年发布的 Gemma 4‑26B。这些模型使开发者能够在控制成本和数据暴露的情况下，实验或替代商业编码助手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemma_(language_model)">Gemma (language model)</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍报告说用本地 Qwen 和 Gemma 变体替换专有模型的经验较为积极，他们提到隐私、成本节约以及日常编码的性能足够，而少数人指出本地模型在性能上仍落后于 Claude Code 等前沿模型，并且为了高风险工作付出的努力可能不值得。一些用户还强调了所需的硬件（大容量内存或多块高端 GPU）以及使用 Unsloth Studio 和容器化的 Pi coding harness 来确保离线运行。

**标签**: `#LLM`, `#local AI`, `#coding assistants`, `#privacy`, `#HN discussion`

---

<a id="item-6"></a>
## [无人经济？技术上并非不可能](https://gmalandrakis.com/writings/ad-economicum.html) ⭐️ 8.0/10

该文章探讨在人工智能和自动化推动下，经济是否能够在没有人类劳动的情况下运行，并分析其技术可行性及更广泛的社会经济影响。 这很重要，因为它涉及人工智能导致的就业替代和未来工作的紧张辩论，为政策制定者、企业和工人提供了潜在经济转型的参考。 文章通过引用当前的人工智能驱动自动化技术来评估技术可行性，并讨论了财富集中、全民基本收入以及后稀缺悖论等社会经济方面。

hackernews · l0new0lf-G · Jun 15, 21:10 · [社区讨论](https://news.ycombinator.com/item?id=48547062)

**背景**: 人工智能驱动的自动化是指利用人工智能和机器人来完成传统由人类执行的任务，这可以提高生产率但也可能导致劳动力被取代。后稀缺经济设想在先进自动化和人工智能的推动下，商品和服务变得丰富，从而减少对人类劳动的需求。诸如全民基本收入之类的概念常被讨论为在这种经济中分配财富的手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/councils/forbesbusinesscouncil/2023/07/10/how-ai-and-automation-are-transforming-the-world/">How AI And Automation Are Transforming The World - Forbes Rebalancing AI-Daron Acemoglu Simon Johnson How new technologies enable the human-machine economy</a></li>
<li><a href="https://medium.com/chain-reaction/living-in-a-post-scarcity-society-how-automation-ai-and-universal-basic-income-could-reshape-the-de5b44704d7b">Living in a Post-Scarcity Society: How Automation, AI, and Universal Basic Income Could Reshape the Global Economy | by Daniel Bron | Chain Reaction | Medium</a></li>
<li><a href="https://economiclens.org/ai-and-automation-navigating-job-displacement-economic-inequality-in-2026/">AI and Automation: Job Displacement and Economic Inequality</a></li>

</ul>
</details>

**社区讨论**: 评论者反应褒贬不一：有人称文章令人烦躁，有人警告 AI 可能导致赢家通吃、财富高度集中；有人质疑消费驱动型经济的动机，建议应听取经济学家而非工程师的意见，还有人指责作者对货币概念的误解。

**标签**: `#AI`, `#automation`, `#economics`, `#future of work`, `#technology impact`

---

<a id="item-7"></a>
## [福克斯据报道寻求收购流媒体巨头 Roku](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

据《华尔街日报》报道，福克斯公司据称正在就收购流媒体硬件和平台服务领先提供商 Roku 进行谈判。 此次交易将使一家大型媒体集团直接控制广泛使用的流媒体平台，可能重塑美国电视生态系统中的广告格局和内容分发。 Roku 提供流媒体播放器、智能电视及其操作系统，而福克斯拥有多个有线电视网络和自家流媒体服务（如 Fox Nation），但交易的报价和时间表尚未披露。

hackernews · thm · Jun 15, 12:50 · [社区讨论](https://news.ycombinator.com/item?id=48540499)

**背景**: Roku 生产流媒体播放器并将其操作系统授权给电视制造商，使用户能够通过互联网连接访问数千个流媒体频道，无需传统有线电视订阅。公司还提供广告支持的内容并运营自有的 Roku 频道。福克斯公司是美国主要的媒体集团，拥有广播网络、有线频道（如福克斯新闻和 FX）以及流媒体服务 Fox Nation。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.roku.com/what-is-roku">What is Roku – How the Roku Experience Works | Roku</a></li>
<li><a href="https://www.roku.com/products?srsltid=AfmBOoqedEmh5W94ve41pfCISDYeHOt1gM1X_b0uJdD5gQtSmWphAiot">Roku Streaming, TV, & Smart Home Products</a></li>

</ul>
</details>

**社区讨论**: 许多评论者担心福克斯的收购会破坏 Roku 的中立平台属性，增加广告并可能引入诸如‘Fox News’按钮之类的党派内容。一些长期 Roku 用户表示他们已经转向如 Nvidia Shield 之类的替代方案，以避免广告并保持简洁的界面。总体而言，讨论反映了对该交易对用户体验和平台独立性影响的怀疑。

**标签**: `#media acquisition`, `#streaming`, `#Roku`, `#Fox`, `#business`

---

<a id="item-8"></a>
## [Salesforce 将以 36 亿美元收购 Fin（前身为 Intercom）](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce 宣布已签署最终协议，以约 36 亿美元收购前身为 Intercom 的 AI 客服平台 Fin。此次收购旨在将 Fin 的 AI 代理整合到 Salesforce 的 Agentforce 平台，以提升自动化客服能力。 此次交易巩固了 Salesforce 在快速增长的 AI 驱动客服市场中的地位，并有助于对抗 Sierra、Decagon 等竞争对手。同时，它为 Salesforce 带来了超过 3 万家企业客户以及能够自主解决 76% 支持请求的 AI 代理。 Fin 的 AI 代理基于其 Apex 驱动的平台构建，能够自主处理大量支持工单。此次收购需按照惯例进行价格调整，并在获得监管批准后预计完成。

hackernews · colesantiago · Jun 15, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48540126)

**背景**: Salesforce 是全球客户关系管理（CRM）软件的领导者，提供销售、服务和营销的云端应用套件。Fin 前身为 Intercom，是一个提供 AI 驱动的客服和消息平台的公司，使用预训练的代理自主解决支持查询。Fin 成立于 2011 年，服务超过 3 万家企业，宣称其 AI 代理能够自主处理 76% 的请求而无需人工干预。Salesforce 的 Agentforce 是其在企业范围内提供自主 AI 代理的计划，Fin 的加入有助于扩展这一能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fin_(company)">Fin (company) - Wikipedia</a></li>
<li><a href="https://qz.com/salesforce-acquires-fin-intercom-ai-customer-service-061526">Salesforce acquires Fin, formerly Intercom, for $3.6 billion</a></li>
<li><a href="https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/">Salesforce Signs Definitive Agreement to Acquire Fin</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有人认为 AI 在执行得当时能提升支持体验，也有人质疑传统帮助台 SaaS 的长期价值或批评 Salesforce 让产品变得过于复杂。多位评论者指出 AI 客服代理领域的竞争日益激烈（如 Sierra、Decagon），并认为此次收购是为了让 AI 代理留在 Salesforce 生态内，防止其成为独立的控制点。还有用户分享了他们使用 Hermes 等工具以及本地 Gemma 4 模型进行自托管代理的实验。

**标签**: `#Salesforce`, `#acquisition`, `#AI customer service`, `#Fin`, `#CRM`

---

<a id="item-9"></a>
## [TimescaleDB 的 Hypercore 压缩技术用于时序数据](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

文章解释了 TimescaleDB 如何通过其 Hypercore 列式存储引擎实现高达 98% 的时序数据压缩率，新数据先写入基于 PostgreSQL 的行式块，旧数据块会自动转换为压缩的列式格式。 高压缩率能够降低存储成本同时保持数据可查询性，使 TimescaleDB 在大规模物联网、监控和分析场景中更具吸引力，因为这些场景需要高效访问历史数据。 Hypercore 是一种混合行列存储：最近的写入保持在可变的 PostgreSQL 行中以实现快速写入，而较旧的数据块则被转换为列式并采用字典编码和 delta‑of‑delta 等技术进行压缩，可实现高达 98% 的体积减少。

hackernews · lkanwoqwp · Jun 15, 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48544451)

**背景**: TimescaleDB 是一个开源的 PostgreSQL 扩展，通过基于时间的自动分区（chunk）来优化时序数据的存储和查询性能。其 Hypercore 引擎采用混合行列存储方式，新数据保持行式格式以支持高吞吐写入，旧数据则自动转换为列式格式以实现高效压缩和分析扫描。列式存储使得字典编码和 delta‑of‑delta 等压缩算法能够获得高压缩比，同时仍能快速进行聚合和过滤操作。这种设计旨在平衡存储效率与查询速度，解决数据库压缩中经典的 I/O 与 CPU 权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://roszigit.com/en/blog/timescaledb-compression-hypercore">TimescaleDB Compression: Hypercore and Columnar Storage with up to 98% Ratio in PostgreSQL</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/hypercore/">Tiger Data Documentation | Hypercore</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了压缩对查询性能的影响，gopalv 强调任何压缩方法应当提高过滤拒绝或扫描速度，而不仅仅是用 CPU 换取 I/O。其他人则提到了 tudorg 的 deltax 扩展（使用最小/最大值、求和、布隆过滤器）、heliosAtwork 提到的用于物联网的 swinging‑door 压缩以及 blackoil 指出的 Facebook Gorilla 采用 delta 和 delta‑of‑delta 的做法，表明大家都在探索如何同时优化存储和分析性能。

**标签**: `#TimescaleDB`, `#time-series databases`, `#compression`, `#PostgreSQL`, `#Hypercore`

---

<a id="item-10"></a>
## [Anthropic 推出 Claude Corps 非营利组织奖学金计划](https://www.anthropic.com/news/claude-corps) ⭐️ 8.0/10

Anthropic 宣布推出 Claude Corps，这是一个全额资助的 12 个月付费奖学金计划，将早期职业 AI 人才安置在美国的非营利组织中部署 Claude 模型，CodePath 将担任奖学金获得者的官方雇佣方。 该计划旨在加速使命驱动型组织的 AI 应用，同时引发关于长期成本、可持续性以及在非营利部门部署强大 AI 系统的伦理影响的讨论。 奖学金获得者将全职在宿主非营利组织工作，开发的软件在奖学金结束后由组织保留，由 CodePath 雇佣；项目承担差旅和后勤费用，并得到 Anthropic 1.5 亿美元资助的支持。

hackernews · Mustan · Jun 15, 17:41 · [社区讨论](https://news.ycombinator.com/item?id=48544637)

**背景**: Claude 是 Anthropic 推出的一系列大型语言模型，采用宪法 AI 技术进行训练以提升对齐和安全性。自推出以来，Anthropic 一直强调负责任的 AI 部署，并发布了关于工作岗位流失和模型治理的框架。Claude Corps 奖学金紧随科技公司将 AI 人才安置在社会部门组织以推动影响并审视社会效应的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-corps/fellow">Claude Corps fellows FAQ \ Anthropic</a></li>
<li><a href="https://dmbio.com/blog/what-is-the-claude-corps">What Is the Claude Corps and How Does Anthropic's $150... | dmbio</a></li>
<li><a href="https://www.reddit.com/r/aicuriosity/comments/1u30eq1/anthropic_launches_claude_corps_fellowship/">Anthropic Launches Claude Corps Fellowship Program to Support US Nonprofits with AI : r/aicuriosity - Reddit</a></li>

</ul>
</details>

**社区讨论**: 评论者担心非营利组织可能会获得昂贵的 AI 系统却缺乏内部专业知识进行维护，质疑该计划类似于 “AI 传教士”，并讨论这是否会导致工作岗位流失，尽管 Anthropic 声称旨在防止此类情况。

**标签**: `#AI`, `#Anthropic`, `#nonprofit`, `#fellowship`, `#AI ethics`

---

<a id="item-11"></a>
## [分析显示 Rust 与 C/C++ 的内存安全 CVE 差异](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html) ⭐️ 8.0/10

该文章由 kobzol 于 2026 年 6 月 15 日发表，分析了 Rust 和 C/C++ 项目中内存安全 CVE 的报告方式及其差异，认为直接比较 CVE 数量是衡量语言安全的误导性指标。 通过指出简单 CVE 比较的缺陷，该分析为开发者和安全团队提供了更细致的漏洞评估视角，有助于在评估 Rust 与 C/C++ 代码库时做出更明智的决策。 文章指出，原始 CVE 总数可能受披露实践差异、Rust 中不安全代码的作用以及严重程度阈值变化等因素的扭曲，并引用社区反馈警告不要过度依赖 CVE 数量。

hackernews · nicoburns · Jun 15, 16:11 · [社区讨论](https://news.ycombinator.com/item?id=48543392)

**社区讨论**: 评论者普遍同意，直接比较 Rust 和 C/C++ 的原始 CVE 数量具有误导性，指出 Rust 的类型系统将漏洞类别转移（例如，恐慌与未定义行为）。一些人认为 Rust 的安全保证将某些错误转变为拒绝服务问题，而另一些人则指出 C 缺乏前置条件可能导致 Rust 能捕获的可利用缺陷。总体而言，讨论强调需要基于上下文的漏洞指标，而非简单的数量统计。

**标签**: `#Rust`, `#C/C++`, `#memory safety`, `#CVEs`, `#software security`

---

<a id="item-12"></a>
## [基于英国生活满意度调查估算公众社会福利函数](https://arxiv.org/abs/2606.13752) ⭐️ 8.0/10

作者使用一种新颖的调查工具，对英国代表性样本（N=2,068）进行了生活满意度的社会福利函数估计，得到中位数弹性参数 α = 0.48。 该研究为基于主观幸福感的政策评估和成本效益分析提供了具有伦理基础的分配权重，填补了利用主观 wellbeing 测量效用的公众偏好 elicitation 的空白。 中位数弹性参数 α = 0.48 显示出对幸福感不平等的强烈厌恶，表明提升最不满意者生命满意度一个单位的价值大约是提升最满意者同样单位价值的两倍。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 等弹性社会福利函数通过一个常数不平等厌恶参数 α 来聚合个体效用，其中 α 越小表示对提升较差者福利的权重越大。以往大量研究利用收入作为效用的代理来估算福利函数，而本文直接从主观幸福感（生活满意度）中 eliciting 公众对效用的偏好。这种方法填补了方法学空白，提供了可用于基于幸福感的成本效益分析的经验得出的分配权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.statisticalconsultants.co.nz/blog/social-welfare-functions.html">Social Welfare Functions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isoelastic_utility">Isoelastic utility - Wikipedia</a></li>
<li><a href="https://web.stanford.edu/~yyye/GeometricAggregationofSWChicago.pdf">Geometric Aggregation of the Social Welfare Function in ...</a></li>

</ul>
</details>

**标签**: `#social welfare function`, `#subjective wellbeing`, `#inequality aversion`, `#public policy`, `#survey methodology`

---

<a id="item-13"></a>
## [在价格不确定性下使用均值-CVaR 建模电池出价](https://arxiv.org/abs/2606.14050) ⭐️ 8.0/10

作者提出一种资产层次的价格接受者电池模型，在有限价格情景下提交阶梯式买卖出价曲线，以均值‑CVaR 目标进行优化。他们证明混合整数线性规划可以精确改写为线性规划，并通过实证表明表面上的囤积行为可能在无市场支配力的情况下出现。 该研究提供了一个可求解的精确线性规划工具，用于分析电池出价行为，帮助市场运营者区分战略囤积与价格不确定性和风险偏好的理性反应。这推动了能源系统建模和批发市场设计。 模型假设有限的价格情景集、阶梯式出价曲线以及物理约束（荷电状态限制、充放电速率）。通过去除整数决策，作者得到精确的线性规划改写；实证结果揭示三个见解：无市场支配力的囤积、荷电状态依赖的不确定性影响以及风险管理导致的分层出价曲线。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 在批发电力市场中，发电机和储能资源会向当天前市场提交出价曲线，市场价格根据供需平衡确定。价格不确定性源于提交出价时未来市场价格未知，这促使参与者进行风险管理。条件价值风险（CVaR）衡量分布尾部最坏情况下的预期损失，均值‑CVaR 目标在期望收益与风险厌恶之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.14050">Battery Bidding under Price Uncertainty in Wholesale Electricity ...</a></li>
<li><a href="https://www.financestrategists.com/wealth-management/risk-profile/conditional-value-at-risk-cvar/">Conditional Value at Risk ( CVaR ) | Meaning , Pros, and Cons</a></li>

</ul>
</details>

**标签**: `#electricity markets`, `#battery storage`, `#optimization`, `#risk management`, `#wholesale markets`

---

<a id="item-14"></a>
## [量子视界：评估量子对比特币和以太坊的威胁](https://arxiv.org/abs/2606.14484) ⭐️ 8.0/10

该论文分析了量子计算对比特币和以太坊的威胁，表明 Shor 算法能够破坏椭圆曲线签名（ECDSA over secp256k1，BLS over BLS12‑381），而 Grover 算法仅对工作量证明挖矿提供有限的二次加速。通过结合硬件规模、专家调查和容错延迟的蒙特卡洛预测，研究估计在 2035 年约有六分之一的概率出现具备密码学相关能力的量子计算机，2040 年约 30%，2050 年约 60%。 了解这些风险有助于区块链开发者和用户在足够强大的量子计算机出现之前优先迁移到后量子签名，凸显主要障碍在于治理而非技术。研究结果还为更广泛的加密货币生态系统提供参考，因为前二十种加密货币目前尚未完全实现后量子安全。 研究指出，在大约六百万枚面临量子风险的比特币中，只有约 230 万枚不可避免地处于风险之中，而以太坊的 50%至 65%处于密钥已公开的账户，可采用后量子签名。此外，论文区分了 Shor 算法对 ECDSA 的指数级破坏与 Grover 算法对挖矿仅有的二次影响，并提供了每个定量主张的可重现蒙特卡洛模型。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 量子计算机能够在特定问题上运行优于经典算法的算法。Shor 算法能够在多项式时间内分解整数，从而破坏比特币和以太坊使用的椭圆曲线数字签名算法 ECDSA。Grover 算法仅提供二次加速的无结构搜索，这对工作量证明挖矿的影响有限。后量子密码学旨在用被认为能抵御量子攻击的算法替换易受攻击的签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grover's_algorithm">Grover's algorithm - Wikipedia</a></li>
<li><a href="https://www.flavius.io/media/a-word-on-secp256k1-and-ecdsa">What exactly are secp256k1, ECDSA and Keccak256 ?</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#blockchain`, `#cryptography`, `#Bitcoin`, `#Ethereum`

---

<a id="item-15"></a>
## [新型 Lookahead Propensity 统计量检测 LLM 预测偏差](https://arxiv.org/abs/2512.23847) ⭐️ 8.0/10

论文提出了 Lookahead Propensity（LAP），一种基于日期仅召回的统计量，用于估计 LLM 内化已实现结果的概率，并用于检测 LLM 生成的经济预测中的前视偏差。 检测前视偏差对于确保金融和政策领域 AI 辅助预测的有效性至关重要，所提出的检验提供了一种低成本的诊断工具，可适用于任何 LLM 预测任务。 LAP 通过对每个公司‑日期对进行仅日期的召回查询来计算；在样本内期间其值显著为正，在模型训练数据截止后几乎降至零，且 LAP 与 LLM 预测在准确率回归中的显著正交互表明存在前视偏差污染。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 前视偏差是指模型在预测时无意中使用了未来的信息，导致其表现被人为抬高。在大型语言模型进行预测时，如果模型在训练过程中已经看到未来的结果并将其内存，就会产生这种偏差。论文提出的仅日期召回查询通过判断模型是否能仅凭日期检索到实际结果，来衡量这种未来知识的内化程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.23847">A Test of Lookahead Bias in LLM Forecasts</a></li>
<li><a href="https://www.emergentmind.com/topics/lookahead-propensity-lap">Lookahead Propensity in Estimation & LLMs</a></li>
<li><a href="https://openreview.net/pdf/fd5f42fe9f767b50e90cf6ad3f7e2528f0f3d759.pdf">[PDF] Recall as a Diagnostic for LLM Forecasting Errors - OpenReview</a></li>

</ul>
</details>

**标签**: `#LLM`, `#forecasting`, `#lookahead bias`, `#econometrics`, `#machine learning`

---

<a id="item-16"></a>
## [新投影估计器从期权组合中提取风险中性依赖。](https://arxiv.org/abs/2601.14852) ⭐️ 8.0/10

该论文提出了一种基于观察到的期权组合的投影估计器，用于估计风险中性依赖，改进单变量估计并给出有限样本误差界，并通过分析瑞士国家银行意外公告对欧元/瑞郎和美元/瑞郎联动变化的影响进行了示例。 该方法解决了自 Ross（1976）以来提取期权价格中风险中性依赖的长期悬而未决问题，能够改善不完全市场下的风险评估和组合管理，并通过瑞士国家银行事件的实证验证展示其实际影响，表明依赖因素解释了联合极端移动概率变化的三分之二。 估计器采用投影方法近似多资产收益函数，推导出有限样本界表明其在可交易期权收益张量内的定价误差接近最小；应用于 SNB 意外公告表明依赖因素解释了欧元/瑞郎和美元/瑞郎同时大幅下跌概率变化的三分之二。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 风险中性 moments（如方差、偏度、峰度）可以通过期权价格推导得到，但它们仅描述单一资产的分布，无法直接给出多资产之间的依赖结构。在不完全市场中，无法仅凭套利价格唯一确定风险中性测度，因而需要额外的假设或约束来估计依赖。Carr–Madan 公式表明可以通过期权组合复制任意支付函数的傅里叶变换，但提取高阶联合 moments 仍然是一个开放问题。本文提出的投影估计器利用可交易期权的张量空间，在有限样本下提供可控的误差界，从而在不完全市场中近似多资产风险中性依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.14852v1">Beyond Carr–Madan: A Projection Approach to Risk-Neutral ... - arXiv</a></li>
<li><a href="https://www.researchgate.net/publication/335993382_Option_Implied_Dependence">(PDF) Option Implied Dependence</a></li>
<li><a href="https://bsic.it/risk-neutral-density-estimation-from-option-prices/">Risk Neutral Density Estimation from Option Prices – BSIC</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#options pricing`, `#risk-neutral moments`, `#dependence estimation`, `#econometrics`

---