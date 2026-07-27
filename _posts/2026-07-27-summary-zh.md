---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> From 15 items, 4 important content pieces were selected

---

1. [vLLM v0.26.0 发布，新增 Inkling 模型族及性能提升](#item-1) ⭐️ 8.0/10
2. [PGSimCity：PostgreSQL 内部工作原理的交互式可视化指南](#item-2) ⭐️ 8.0/10
3. [法国消防员首次遇见积雨云状火云](#item-3) ⭐️ 8.0/10
4. [欧盟委员会提出浏览器级隐私设置以取代 Cookie 横幅](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布，新增 Inkling 模型族及性能提升](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM 版本 0.26.0 引入了 Inkling 模型族的完整支持、DeepSeek‑V4 在多厂商上的性能优化、通过 head_dtype 启用 fp32 lm_head 以提升生成准确率，以及每个 KV‑cache 组可选择的灵活注意力后端。此版本包含 411 次提交，来自 212 名贡献者（其中 61 人为新贡献者）。 这些改进提升了 LLM 推理的准确性和吞吐量，使 vLLM 在各种硬件平台上更具竞争力，并扩展了可高效服务的模型范围。开发者能够获得更高的生成质量以及更便捷地部署如 Inkling 和 DeepSeek‑V4 等前沿模型。 可以通过 head_dtype 标志启用 fp32 lm_head，且已扩展到 LoRA 路径并提供 ROCm 的 torch.mm 快速路径；DeepSeek‑V4 获得了专用路由内核和 fused_topk_bias 优化。注意力后端现在可按 KV‑cache 组选择，滑动窗口支持被暴露为显式后端能力；Inkling 支持包括 Mamba‑混合 MoE 架构、分段 CUDA 图、LoRA 以及 NVFP4 量化。

github · khluu · Jul 27, 01:06

**背景**: vLLM 是一个开源库，专为大型语言模型的高吞吐量服务而设计，采用了连续批处理、PagedAttention 和 CUDA 捕获图等技术。lm_head 层将模型的内部隐藏状态转换为 token logits，以 fp32 而非低精度运行该层可以提升数值稳定性和生成质量。注意力后端决定如何访问键值缓存；使其可按缓存组选择，可支持混合模型（如滑动窗口与全注意力的组合）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek AI: R1 Reasoning, API & Local Deployment 2026</a></li>
<li><a href="https://www.remio.ai/post/vllm-v0-26-0-turns-the-amd-github-story-into-a-cross-vendor-inference-contest">vLLM v0.26.0 Turns the AMD GitHub Story Into a Cross-Vendor...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release notes`, `#performance optimization`, `#model support`

---

<a id="item-2"></a>
## [PGSimCity：PostgreSQL 内部工作原理的交互式可视化指南](https://nikolays.github.io/PGSimCity/) ⭐️ 8.0/10

PGSimCity 是一个开源的交互式网页工具，可视化展示 PostgreSQL 的内部架构和查询执行流程，使用户能够探索规划器、执行器、缓冲管理器和 WAL 等组件。 通过将复杂的数据库内部机制转化为直观的城市景观可视化，PGSimCity 降低了开发者和学生理解和优化 PostgreSQL 的门槛，并可能激发其他系统的类似教育工具。 该工具使用 HTML、CSS 和 JavaScript 构建，托管在 GitHub Pages 上，用户可以点击查看解析、规划、执行和清理等阶段，并突出显示组件之间的数据流。

hackernews · jonbaer · Jul 27, 00:19 · [社区讨论](https://news.ycombinator.com/item?id=49063754)

**背景**: PostgreSQL 使用基于成本的查询规划器，评估多个执行计划并选择估计成本最低的一个，这一过程可通过 EXPLAIN 命令观察。缓冲管理器通过环形缓冲区和本地缓冲池管理共享内存与磁盘之间的数据移动，影响读写性能。预写日志（WAL）在更改应用到数据页之前先记录到日志，以确保持久性和崩溃安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pganalyze.com/docs/explain/basics-of-postgres-query-planning">The Basics of Postgres Query Planning · pganalyze</a></li>
<li><a href="https://www.interdb.jp/pg/pgsql08.html">8. Buffer Manager :: Hironobu SUZUKI @ InterDB</a></li>
<li><a href="https://www.postgresql.org/docs/current/wal-intro.html">PostgreSQL : Documentation: 18: 28.3. Write - Ahead Logging ( WAL )</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 PGSimCity 使复杂的 PostgreSQL 内部机制变得易于理解且富有吸引力，并指出其在云计算或 Kubernetes 等其他领域的潜在 reuse。一些用户希望增加更多交互性，例如能够输入自定义查询并跟踪其执行过程，以及提供更清晰的叙事以突出客户端和数据的角色。总体反馈积极，并伴随着改善清晰度和用户控制的建设性建议。

**标签**: `#postgresql`, `#database-internals`, `#visualization`, `#education`, `#open-source`

---

<a id="item-3"></a>
## [法国消防员首次遇见积雨云状火云](https://www.france24.com/en/live-news/20260726-french-firefighters-face-pyrocumulonimbus-for-first-time) ⭐️ 8.0/10

法国消防员在兰德-梅多克地区的大规模野火中首次遇见积雨云状火云，导致大规模疏散。 此事件凸显气候变化正在推动更极端的火灾行为，为全球的灾害管理和环境监测带来新挑战。 该积雨云状火云形成于兰德-梅多克的人工松林种植园，这是 19 世纪拿破仑三世时期建造的易燃单一树种林；此类云可以产生闪电、强风，有时还有降雨，尽管火生成的云常常缺乏降水。

hackernews · saaaaaam · Jul 26, 17:49 · [社区讨论](https://news.ycombinator.com/item?id=49060495)

**背景**: 积雨云状火云（也称积雨云火生成云）是在大型野火或火山喷发等强热源上方形成的雷雨云，当剧烈的上升气流将水分和灰烬带入大气层时形成。它们能产生闪电、冰雹和强外流风，影响火势蔓延并对航空和地面人员构成危害。兰德-梅多克地区拥有大片 19 世纪人工松林，原为排湿而植，导致地表均匀易燃且缺乏天然防火带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cumulonimbus_flammagenitus">Cumulonimbus flammagenitus - Wikipedia</a></li>
<li><a href="https://www.rmets.org/metmatters/pyrocumulonimbus-clouds">Pyrocumulonimbus Clouds | Royal Meteorological Society</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该地区人工松林单一树种及其高度易燃，争论是否应称为积云而非积雨云，因为“nimbus”暗示携带降雨，描述了 20 万人疏散的末日景象，分享了华盛顿州的类似经历，并以“不要抬头”作为网络梗进行警告。

**标签**: `#wildfire`, `#pyrocumulonimbus`, `#climate change`, `#firefighting`, `#environmental science`

---

<a id="item-4"></a>
## [欧盟委员会提出浏览器级隐私设置以取代 Cookie 横幅](https://killthecookiebanner.eu/) ⭐️ 8.0/10

欧盟委员会提出浏览器级隐私设置，用户可在浏览器中一次性设置跟踪偏好，从而无需再看到每个网站的 Cookie 横幅。 如果被采纳，该提案可能简化网页浏览，减少同意疲劳，并为用户提供更强、具有法律约束力的跟踪控制，影响网站、广告商和隐私技术生态。 该提案基于 ePrivacy 法规，将依赖类似已废止的 Do Not Track 头的机器可读浏览器信号，但具法律强制力；仍可为功能必要的 Cookie 保留站点特定例外。

hackernews · rapnie · Jul 26, 11:53 · [社区讨论](https://news.ycombinator.com/item?id=49057175)

**背景**: ePrivacy 法规旨在通过将同意从每个网站的横幅转移到浏览器级设置来更新欧盟 Cookie 法律，建立在之前的 Do Not Track 头和 IAB 透明度与同意框架之上，后者目前通过同意管理平台管理同意。与 DNT 不同，新方法将在欧盟法律下具有法律约束力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EPrivacy_Regulation">ePrivacy Regulation - Wikipedia</a></li>
<li><a href="https://browserinsight.net/blog/do-not-track-header">The Do Not Track ( DNT ) Header : Why It Failed, and... - BrowserInsight</a></li>
<li><a href="https://www.cookiebot.com/en/iab-tcf-cookies/">IAB TCF v 2 .3 - Transparency and Consent Framework</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者就该提案的可行性展开讨论，有人认为 Cookie 横幅是无效的同意机制，也有人警告浏览器级信号可能在没有强制执行的情况下被忽视，还有少数人认为直接拒绝追踪就能消除横幅的必要。

**标签**: `#privacy`, `#cookie law`, `#EU regulation`, `#web browsing`, `#Hacker News`

---