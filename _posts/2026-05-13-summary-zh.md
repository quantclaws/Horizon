---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 58 items, 18 important content pieces were selected

---

1. [Needle：26M 参数注意力仅模型用于工具调用。](#item-1) ⭐️ 8.0/10
2. [CERT 披露 dnsmasq 中的六个严重 CVE 漏洞](#item-2) ⭐️ 8.0/10
3. [资深开发者为何难以传达其专业知识](#item-3) ⭐️ 8.0/10
4. [Rendering the Sky, Sunsets, and Planets](#item-4) ⭐️ 8.0/10
5. [Quack: The DuckDB Client-Server Protocol](#item-5) ⭐️ 8.0/10
6. [Bambu Lab is abusing the open source social contract](#item-6) ⭐️ 8.0/10
7. [EFF 呼吁第四巡回法院要求边境电子设备搜查需持令状](#item-7) ⭐️ 8.0/10
8. [加拿大法案 C-22 复活监控措施。](#item-8) ⭐️ 8.0/10
9. [深度学习揭示社会空间传染推动离网光伏采用](#item-9) ⭐️ 8.0/10
10. [针对二元预测市场的分辨率感知永续期货框架](#item-10) ⭐️ 8.0/10
11. [事件关联永续期货的分类学：超越单市场二元情况的变体设计](#item-11) ⭐️ 8.0/10
12. [使用金融指标量化预测的风险收益权衡](#item-12) ⭐️ 8.0/10
13. [可扩展的订单簿依赖霍克斯过程用于高频交易](#item-13) ⭐️ 8.0/10
14. [OrderFusion：通过编码订单簿实现端到端概率内日电价预测](#item-14) ⭐️ 8.0/10
15. [可扩展开源深度学习模型进行小时级住宅供暖和用电需求预测](#item-15) ⭐️ 8.0/10
16. [掩码优先设计纠正 A 股价格涨跌停偏差，配合 GPU 加速](#item-16) ⭐️ 8.0/10
17. [使用大型语言模型校准行为参数](#item-17) ⭐️ 8.0/10
18. [: 将 CRRA 投资组合选择与 Rényi 信息投射相联系](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Needle：26M 参数注意力仅模型用于工具调用。](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

我们开源了 Needle，一个从 Gemini 蒸馏而来的 26M 参数仅注意力模型，用于单次函数调用，在消费级硬件上实现 6000 tok/s 前填充和 1200 tok/s 解码。 Needle 表明微小的仅注意力模型能够高效处理工具使用，使得代理 AI 能够在手机、手表及其他边缘设备上运行，无需依赖巨大模型。 该模型完全去掉了 MLP/FFN，仅由注意力和门控组成；在 16 颗 TPU v6e 上预训练了 200B tokens（约 27 小时），随后用 Gemini 生成的跨 15 类工具的 2B tokens 合成数据进行后训练（约 45 分钟）。

hackernews · HenryNdubuaku · May 12, 18:03 · [社区讨论](https://news.ycombinator.com/item?id=48111896)

**背景**: Transformer 模型源自《Attention Is All You Need》论文，依赖自注意力机制，通常将注意力层与前馈网络（FFN）结合使用。工具调用（函数调用）使语言模型能够通过预测工具名称并提取参数来调用外部 API，生成结构化的 JSON 调用。最近的研究表明，当外部知识已在提示中提供时，可以省略 FFN 参数，纯注意力仅架构仍能表现良好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Attention_Is_All_You_Need">Attention Is All You Need - Wikipedia</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/function-calling">Function calling - OpenAI API</a></li>
<li><a href="https://arxiv.org/abs/1706.03762">[1706.03762] Attention Is All You Need - arXiv.org Attention Is All You Need: The Original Transformer Architecture Attention Mechanism in ML - GeeksforGeeks [PDF] Attention is All you Need | Semantic Scholar Images The Transformer Architecture - auroria.io A Tour of Attention-Based Architectures</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏该微型模型在边缘设备代理方面的潜力，并要求提供更多关于其在工具使用任务中的辨别能力的证据；几位建议发布现场演示或游乐场来展示性能。其他人则强调了诸如自然语言 CLI 工具和隐私优先的桌面/移动代理等使用场景，同时指出该模型只有 26M 参数，便于实验。

**标签**: `#machine learning`, `#tiny models`, `#tool use`, `#agentic AI`, `#open source`

---

<a id="item-2"></a>
## [CERT 披露 dnsmasq 中的六个严重 CVE 漏洞](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 8.0/10

CERT 已发布六个新的 CVE 编号，涉及 dnsmasq DNS 和 DHCP 服务器的严重安全漏洞，包括越界写入、无限循环和缓冲区溢出。 这些漏洞影响数百万依赖 dnsmasq 的设备，如家庭路由器和物联网设备，凸显了关键网络基础设施中内存不安全代码所带来的持续风险。 披露的 CVE 包括由恶意 DNS 数据包触发的堆上远程越界写入、可导致 dnsmasq 停止响应查询的无限循环，以及可通过恶意 DHCP 请求利用的缓冲区溢出。

hackernews · chizhik-pyzhik · May 12, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48112042)

**背景**: dnsmasq 是一种轻量级的开源软件，提供 DNS 缓存、DHCP 服务器、TFTP 和路由器广告功能，广泛用于小型网络、家庭路由器和物联网设备。CVE（Common Vulnerabilities and Exposures）是一个用于标识已公开安全漏洞的标准化编号，便于跟踪和修复。内存安全是指防止软件以非法方式访问内存的保护措施，例如防止缓冲区溢出；C 语言缺乏这些保护，因而容易出现 dnsmasq 中看到的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 MaraDNS 自 2023 年以来在 AI 辅助审计中未发现严重漏洞，认为这些问题凸显了用 Rust 或 Go 等内存安全语言重写基于 C 的网络代码的紧迫性，并讨论 Debian 的稳定分支是否会及时补丁 dnsmasq 或仅仅回港修复。还有人提到 OpenWRT 正在开发新版本，并强调了堆越界写入、无限循环和由 DHCP 触发的缓冲区溢出等具体影响。

**标签**: `#security`, `#dnsmasq`, `#CVE`, `#vulnerability`, `#memory safety`

---

<a id="item-3"></a>
## [资深开发者为何难以传达其专业知识](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise) ⭐️ 8.0/10

文章探讨了资深开发者为何难以传达其专业知识，指出原因包括隐性知识、期望不匹配以及初级同事对导师缺乏兴趣。 理解这些沟通障碍对于提升知识转移、团队生产力以及软件工程团队中的有效 mentorship 至关重要。 文章指出，资深开发者的许多专业知识存在于难以言说的内部‘世界模型’中，而初级开发者常常不主动寻求导师尽管经验丰富。

hackernews · nilirl · May 12, 15:08 · [社区讨论](https://news.ycombinator.com/item?id=48109460)

**背景**: 隐性知识是指通过经验获得且难以用语言完全表达的技能和理解。资深开发者在多年工作中积累了大量隐性知识，因而难以向经验较少的同事传达。有效的 mentorship 需要通过沟通、实践和共同解决问题来弥合这一差距。

**社区讨论**: 评论者强调了专业知识的隐性和经验性质，指出初级开发者常对寻求导师缺乏兴趣，并讨论了 AI 是否能取代人类知识共享的必要性。

**标签**: `#software engineering`, `#communication`, `#mentorship`, `#senior developers`, `#soft skills`

---

<a id="item-4"></a>
## [Rendering the Sky, Sunsets, and Planets](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 8.0/10

A detailed blog post explaining techniques for rendering realistic sky, sunsets, and planetary atmospheres using atmospheric scattering models.

hackernews · ibobev · May 12, 13:26 · [社区讨论](https://news.ycombinator.com/item?id=48107997)

**标签**: `#graphics rendering`, `#atmospheric scattering`, `#computer graphics`, `#procedural generation`, `#visualization`

---

<a id="item-5"></a>
## [Quack: The DuckDB Client-Server Protocol](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB unveils Quack, a client-server protocol enabling remote connections and horizontal scaling for its embedded analytical database.

hackernews · aduffy · May 12, 17:54 · [社区讨论](https://news.ycombinator.com/item?id=48111765)

**标签**: `#DuckDB`, `#Quack protocol`, `#client-server`, `#analytics database`, `#remote access`

---

<a id="item-6"></a>
## [Bambu Lab is abusing the open source social contract](https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/) ⭐️ 8.0/10

Jeff Geerling argues Bambu Lab is abusing the open source social contract by restricting third‑party access and using user‑agent blocking, sparking a lively debate on Hacker News.

hackernews · rubenbe · May 12, 14:54 · [社区讨论](https://news.ycombinator.com/item?id=48109224)

**标签**: `#open-source`, `#3D-printing`, `#Bambu-Lab`, `#ethics`, `#community-discussion`

---

<a id="item-7"></a>
## [EFF 呼吁第四巡回法院要求边境电子设备搜查需持令状](https://www.eff.org/deeplinks/2026/05/eff-fourth-circuit-electronic-device-searches-border-require-warrant) ⭐️ 8.0/10

电子前线基金会（EFF）向美国第四巡回上诉法院提交了一份意见书，主张在美边境无令状搜查电子设备违反第四修正案。 如果法院同意这一主张，该裁决将加强居住在美国境内 100 英里边境区域内数百万人的数字隐私保护。 EFF 主张边境搜查例外不适用于存储大量个人数据的电子设备，并引用 Cellebrite UFED 和 GrayKey 等取证工具来说明此类搜查的侵入性。

hackernews · hn_acker · May 12, 21:48 · [社区讨论](https://news.ycombinator.com/item?id=48115059)

**背景**: 边境搜查例外允许在国际边境对人员和财物进行常规检查，而无需搜查令或可能原因，理由是国家安全。然而，法院越来越认识到现代智能手机和笔记本电脑存储了大量私人信息，这引发了对传统例外是否适用于数字设备的质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cellebrite_UFED">Cellebrite UFED - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrayKey">GrayKey</a></li>

</ul>
</details>

**社区讨论**: 评论者指出审判法官对政府理由的怀疑，强调具有里程碑意义的权利案件常涉及不讨喜的被告，重复了文章标题，并指出 100 英里边境区域覆盖了美国约 80%的人口。

**标签**: `#privacy`, `#border search`, `#Fourth Amendment`, `#EFF`, `#legal case`

---

<a id="item-8"></a>
## [加拿大法案 C-22 复活监控措施。](https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare) ⭐️ 8.0/10

加拿大法案 C-22 重新引入强制数据保留规定，要求电信和在线服务存储用户通信元数据长达一年，并赋予公共安全部长权力要求在 Signal、WhatsApp、iMessage 等端到端加密消息应用中植入加密后门。 如果该法案通过，可能会迫使加密消息服务提供商退出加拿大或削弱其安全性，危及数百万加拿大人的隐私，并在全球树立政府强制加密后门的危险先例。 该立法强制要求最多保留一年的元数据，并赋予公共安全部长发布技术通知的权力，迫使公司建设监控后门；苹果和 Meta 警告称，此类后门将易受恶意行为者利用，并将破坏端到端加密的安全保证。

hackernews · Brajeshwar · May 12, 17:35 · [社区讨论](https://news.ycombinator.com/item?id=48111531)

**背景**: 强制数据保留法律要求通信服务提供商存储用户的元数据——例如通话时间、号码和 IP 地址——在规定期限内，以协助执法调查。加密后门是故意内置于加密系统中的弱点，使当局能够解密消息，但同时也会创建可被黑客或敌对国家利用的可利用漏洞。过去的努力，包括英国的调查权力法案和美国停滞的 EARN IT 法案，表明此类措施常常与强加密和民权保护发生冲突，这一点得到了电子前线基金会的呼应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_retention">Data retention - Wikipedia</a></li>
<li><a href="https://www.eff.org/issues/mandatory-data-retention">Mandatory Data Retention | Electronic Frontier Foundation</a></li>
<li><a href="https://cambridgeanalytica.org/surveillance-privacy/canada-bill-c-22-encryption-backdoor-apple-meta-50971/">Apple and Meta just warned Canada's Bill C - 22 would force them to...</a></li>

</ul>
</details>

**社区讨论**: 评论者警告，强制数据保留和后门要求可能导致 Signal、WhatsApp、iMessage 和 Matrix 等加密消息服务封锁加拿大用户和企业。另一些人认为该法案是一个警钟，可能推动抗审查技术的创新；而一位长期关注隐私的加拿大活动家感到沮丧，认为已经没有政治解决方案。还有人指出，反复重新提出此类立法往往最终会得到通过，也有人质疑为何此议题未得到更多关注。

**标签**: `#privacy`, `#surveillance`, `#legislation`, `#encryption`, `#Canada`

---

<a id="item-9"></a>
## [深度学习揭示社会空间传染推动离网光伏采用](https://arxiv.org/abs/2605.09642) ⭐️ 8.0/10

研究人员利用深度学习分割模型对十年卫星影像进行分析，测量了 507 个离网定居点聚类中的光伏采用的社会空间传染动态。 该研究在数据匮乏的离网地区提供了社会空间传染的实证证据，为通过有针对性的种植干预加速可再生能源扩散的政策提供了依据。 社会空间传染的强度在邻近安装后 1–2 年内达到峰值随后减弱，早期采纳与范围扩张相关，后期采纳与范围收缩相关，表明从聚集到巩固的转变。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 社会空间传染指的是通过嵌入物理空间的社会关系放大技术扩散，新采纳者倾向于聚集在先前采纳者周围。研究人员使用深度学习分割模型（如 Mask2Former 等）对十年的遥感影像序列进行分析，以检测 507 个离网定居点聚类中的光伏安装。通过时空点模式推断，他们量化了新安装相对于现有安装的聚集范围和强度，以评估传染效应随时间的演变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.09642v1">From Expansion to Consolidation: Socio-Spatial Contagion ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0038092X24002330">Generalized deep learning model for photovoltaic module segmentation from satellite and aerial imagery - ScienceDirect</a></li>
<li><a href="https://journal.r-project.org/articles/RJ-2023-025/">Non-Parametric Analysis of Spatial and Spatio-Temporal Point Patterns</a></li>

</ul>
</details>

**标签**: `#photovoltaic`, `#remote sensing`, `#socio-spatial contagion`, `#off-grid energy`, `#diffusion of innovations`

---

<a id="item-10"></a>
## [针对二元预测市场的分辨率感知永续期货框架](https://arxiv.org/abs/2605.10400) ⭐️ 8.0/10

本文提出了一种基于 Polymarket 数据的分辨率感知永续期货设计（PIRAP），并对其在 2026 年 4 月 21 日至 27 日的实证表现进行了反事实评估。 该框架专门针对二元预测市场中受限事件（bounded‑event）的特性，弥补了传统永续期货资金费率和静态保证金在概率趋近 0 或 1 时的失效，有望提升 DeFi 预测市场的稳定性和资本效率。 PIRAP 包含六个组成部分：综合指数估计器（中价、深度加权中价、时间衰减 VWAP）、跳跃感知分层保证金、向结算压缩杠杆的调度、带边界校正的分辨率感知资金费率、多阶段熔断机制以及资格准入框架；在 Polymarket PMXT v2 档案上的实证测试显示结果混合，多个预设底线未达标。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 二元预测市场交易的合约根据某个是/否事件的发生情况结算，其价格反映了事件发生的概率。永续期货是一种没有到期日的衍生品，依赖资金费率和保证金机制使其价格紧跟指数。当标的资产是必须在事件解决时收敛到 0 或 1 的概率时，传统仅基于基差的资金费率和以连续波动率校准的静态保证金会导致定价偏差、频繁强平或坏账。本文提出的分辨率感知设计通过在事件临近解决时明确考虑概率分布的坍塌来弥补这些不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.10400">Resolution - Aware Perpetual Futures on Binary Prediction Markets...</a></li>
<li><a href="https://github.com/ForesightFlow/event-linked-perps">ForesightFlow/event-linked-perps: Resolution - Aware Perpetual ...</a></li>
<li><a href="https://arxiv.org/pdf/2605.10400">Resolution-Aware Perpetual Futures on Binary Prediction ...</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#perpetual futures`, `#risk management`, `#DeFi`, `#Polymarket`, `#arXiv`

---

<a id="item-11"></a>
## [事件关联永续期货的分类学：超越单市场二元情况的变体设计](https://arxiv.org/abs/2605.10428) ⭐️ 8.0/10

本文提出了一套正式的分类学，涵盖七种超越简单二元概率指数永续的事件关联永续期货变体，并按照四个正交设计轴——底层几何、时间结构、结算结构和场所组织——进行组织。 通过系统化设计空间，该工作为开发者和研究人员提供了在去中心化金融平台上构建新颖预测市场关联衍生品的路径，提升了风险感知的合约设计，并将理论与新兴金融基础设施的实际实现联系起来。 值得注意的是，条件变体在条件事件变得罕见时会出现分母不稳定性；价差变体需要对解决风险进行三通道分解；波动率/熵变体虽然规避了二元终端崩溃，但引入了估计器约定和熵衰减问题；篮子变体则需要多时期跳感知保证金，其聚合取决于相关性。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 事件关联永续期货是一类衍生品，其收益随预测市场中事件结果概率的演变而变化，并在事件解决过程中持续结算。Paper 1 中提出的解决感知风险设计框架（PIRAP）提供了诸如跳感知保证金和指数估计器等工具，以管理二元结果合约特有的风险。在此基础上，本文将框架扩展到更复杂的底层结构，如条件概率、价差、篮子以及波动率相关衍生品，从而为去中心化金融和预测市场应用拓宽了设计空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.10400">[2605.10400] Resolution-Aware Perpetual Futures on Binary ...</a></li>
<li><a href="https://github.com/ForesightFlow/event-linked-perps">ForesightFlow/ event - linked -perps: Resolution-Aware Perpetual ...</a></li>

</ul>
</details>

**标签**: `#event-linked perpetual futures`, `#derivatives`, `#prediction markets`, `#DeFi`, `#financial engineering`

---

<a id="item-12"></a>
## [使用金融指标量化预测的风险收益权衡](https://arxiv.org/abs/2605.09712) ⭐️ 8.0/10

该论文将基准的预测损失差异视为收益序列，使用夏普、索提诺、奥米茄和回撤等金融风险调整指标进行评估，并提出了新颖的 Edge Ratio 来衡量模型提供独特信息预测的倾向。 它表明虽然平均准确度常能超越专业预测者，但在风险调整基准上击败他们要困难得多，凸显了专家预测的可靠性和判断价值。 该框架将夏普、索提诺、奥米茄和最大回撤应用于损失差异，提出 Edge Ratio，并发现某些机器学习方法在特定目标上具有吸引人的风险特征，尽管专业预测者很少出现灾难性失败。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 在预测中，模型的损失与基准损失的差异可以视为收益序列，因而可以用金融资产所使用的风险调整度量来评估表现。夏普比率、索提诺比率、奥米茄比率和回撤等指标衡量每单位风险的超额收益、下行风险或尾部风险，提供比平均准确度更细致的视角。TabPFN 是一种专为小型到中型表格数据设计的基础模型，能够在训练样本有限时仍给出强预测。专业预测者调查（Survey of Professional Forecasters）汇总了宏观变量的专家判断，在许多预测研究中被用作强基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.09712">Quantifying the Risk –Return Tradeoff in Forecasting</a></li>
<li><a href="https://en.wikipedia.org/wiki/TabPFN">TabPFN - Wikipedia</a></li>
<li><a href="https://www.financestrategists.com/wealth-management/financial-ratios/omega-ratio/">Omega Ratio | Definition, Components, Advantages & Limitations</a></li>

</ul>
</details>

**标签**: `#forecasting`, `#risk-adjusted performance`, `#econometrics`, `#machine learning`, `#macroeconomics`

---

<a id="item-13"></a>
## [可扩展的订单簿依赖霍克斯过程用于高频交易](https://arxiv.org/abs/2307.09077) ⭐️ 8.0/10

该论文提出了一种订单簿依赖的霍克斯过程，其强度是标准霍克斯强度与高维订单簿协变量函数的乘积，并给出了能够处理数十亿数据点的可扩展估计算法。论文还给出了平稳性、收敛性和一致性的理论保证，并在纽约证券交易所的四只股票上进行实证验证，表明考虑订单簿非线性能提升样本外预测表现。 将订单簿的细节信息纳入自激点过程，能够更真实地描述高频交易的动态，有助于交易策略的设计和风险管理。该方法可扩展到数十亿数据点，使其在实际的多工具高频数据场景中具有实用价值。 论文给出了过程平稳性的条件，提出了一种基于近似似然的估计算法并证明其收敛，在弱条件下建立了参数的一致性结果，并提出了一种用于样本外模型比较的检验统计量。在四只纽约证券交易所股票上的实证表明，考虑订单簿的非线性特征相比标准霍克斯过程能显著提升预测能力。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 霍克斯过程是一种自激点过程，其强度在每次事件发生后会增加，适用于建模诸如高频交易到达这样的聚簇现象。在限价订单簿中，市场状态由高维特征（如买卖价差、订单深度、失衡）描述，这些特征变化快速并影响未来交易的概率。由于高频数据集可能包含数十亿个带时间戳的事件，因此需要可扩展的估计方法才能将诸如订单簿依赖霍克斯过程这样的复杂模型拟合到如此规模的数据上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hawkes_process">Hawkes process</a></li>
<li><a href="https://academic.oup.com/jfec/article/22/4/1098/7241580">Estimation of an Order Book Dependent Hawkes Process for ...</a></li>
<li><a href="https://experts.illinois.edu/en/publications/point-process-estimation-with-mirror-prox-algorithms/">Point Process Estimation with Mirror Prox Algorithms - Illinois Experts</a></li>

</ul>
</details>

**标签**: `#Hawkes process`, `#high-frequency trading`, `#order book`, `#point process estimation`, `#scalable algorithms`

---

<a id="item-14"></a>
## [OrderFusion：通过编码订单簿实现端到端概率内日电价预测](https://arxiv.org/abs/2502.06830) ⭐️ 8.0/10

本文提出 OrderFusion，一种端到端概率预测模型，通过 2.5D 表示和融合层编码完整的限价订单簿结构以捕捉买卖互动，并采用分层非交叉约束估计分位数。 准确的内日电价预测对于市场参与者在可再生能源增加的情况下管理失衡风险至关重要，OrderFusion 的微观结构感知方法提供了一种改善预测可靠性的 principled 途径，并可推广至其他连续竞价市场。 OrderFusion 采用 2.5D 订单簿编码、融合层提取交互感知特征，以及强制单调性的分层分位数估计器以避免分位数交叉；消融研究表明各组件均有贡献，且代码已在 GitHub 上公开。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 连续内日（CID）市场允许参与者通过持续发布的买卖订单在交付前进行交易，形成反映实时供需动态的限价订单簿。概率预测旨在预测未来价格的完整分布，但分位数交叉——即预测分位数违反顺序——会削弱可靠性。传统方法通常使用手工特征或将订单簿视为多变量时间序列，忽略了买卖的完整互动结构。OrderFusion 通过直接从原始订单簿学习交互感知表示来弥补这些不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.06830">[2502.06830] OrderFusion: Encoding Orderbook for End-to-End ...</a></li>
<li><a href="https://runyao-yu.com/OrderFusion/">OrderFusion: Encoding Orderbook for End-to-End Probabilistic ...</a></li>
<li><a href="https://www.mdpi.com/1996-1073/18/12/3097">A Review of Electricity Price Forecasting Models in the Day ...</a></li>

</ul>
</details>

**标签**: `#electricity price forecasting`, `#order book encoding`, `#probabilistic forecasting`, `#intraday markets`, `#machine learning for energy`

---

<a id="item-15"></a>
## [可扩展开源深度学习模型进行小时级住宅供暖和用电需求预测](https://arxiv.org/abs/2505.22873) ⭐️ 8.0/10

本文提出可扩展的高分辨率开源概率深度学习模型，利用多模态建筑和天气数据进行小时级住宅供暖和非供暖用电需求预测。相较于 NREL 的 ResStock 模型，供暖和用电的 RMSE 分别降低 18.8%和 27.6%，加权区间得分（WIS）提升 59%。 该方法为政策制定者和电网规划者提供了细粒度的开源工具，以改善负荷预测，助力美国建筑股去碳化并在可再生能源渗透增加时提升电网可靠性。由于在广泛使用的 ResStock 基准上实现了显著性能提升，该工作有望推动数据驱动的需求预测在能源研究与实践中的采用。 模型在以燃气供暖为主的地区的电力消耗数据上训练，从而捕捉非供暖末端用途（照明、电器、制冷）的用电模式。它们融合建筑足迹、高度、周边建筑密度、土地利用等多模态属性以及高分辨率天气数据，并通过 RMSE 和加权区间得分（WIS）进行评估。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 准确预测住宅供暖和用电需求对电网运行、能源规划以及建筑部门去碳化工作至关重要。传统工具如 NREL 的 ResStock 模型基于物理仿真提供标准化负荷曲线，但往往缺乏数据驱动方法的空间细粒度和适应性。近期研究利用深度学习和多模态建筑数据（如足迹、高度、周边密度、土地利用和高分辨率天气）来捕捉需求异质性，并通过概率方法量化预测不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2505.22873">Forecasting Residential Heating and Electricity Demand with Scalable...</a></li>
<li><a href="https://data.openei.org/submissions/153?source=post_page---------------------------">OEDI: Commercial and Residential Hourly Load Profiles for all...</a></li>
<li><a href="https://www.techscience.com/CMES/special_detail/power-energy-forecasting">CMES | Special Issues: AI-Driven Advancements in Power and Energy ...</a></li>

</ul>
</details>

**标签**: `#energy forecasting`, `#deep learning`, `#residential demand`, `#probabilistic modeling`, `#open-source`

---

<a id="item-16"></a>
## [掩码优先设计纠正 A 股价格涨跌停偏差，配合 GPU 加速](https://arxiv.org/abs/2507.07107) ⭐️ 8.0/10

The paper introduces a mask-first approach to eliminate upstream contamination from price limits in Chinese A-share factor models, and builds a GPU-vectorized 213-factor engine using PyTorch unfold. On synthetic and real A-share data (2022-2024) it achieves annualised Sharpe ratios of 2.05 and 1.63 respectively.

rss · arXiv Quantitative Finance · May 12, 04:00

**标签**: `#quantitative finance`, `#machine learning`, `#factor modeling`, `#bias correction`, `#GPU acceleration`

---

<a id="item-17"></a>
## [使用大型语言模型校准行为参数](https://arxiv.org/abs/2602.01022) ⭐️ 8.0/10

该论文提出了一种框架，将大型语言模型视为行为参数（如损失厌恶、从众、外推和锚定）的校准测量工具，使用四种模型和 24,000 个代理‑情景对揭示基线偏差，并表明基于档案的校准能得到与人类基准一致的参数。 通过为八种典型行为偏差提供系统的测量范围、校准函数和明确的边界，该工作使得大型语言模型在行为金融和资产定价研究中的集成更加可靠。 基线 LLM 行为表现出减弱的损失厌恶、较弱的从众效应以及接近零的处置效应；基于档案的校准在损失厌恶、从众、外推和锚定方面引发了大而稳定的偏移。将这些校准后的参数嵌入基于代理的资产定价模型中，产生了与实证数据一致的短期动量和长期反转模式。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: 损失厌恶、从众和外推等行为参数是资产定价模型的核心，但在人类中难以可靠测量。大型语言模型可能表现出与人类偏好偏离的系统理性偏差，但可以通过基于档案的校准技术进行调整。基于代理的资产定价模型模拟异质代理以研究市场动态，使研究者能够测试校准后的行为参数如何影响诸如动量和反转之类的价格模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6668018">Large Language Models as Calibrated Measurement Instruments for ...</a></li>
<li><a href="https://arxiv.org/html/2602.01022v1">Calibrating Behavioral Parameters with Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2409.17266v1">AAPM: Large Language Model Agent-based Asset Pricing Models</a></li>

</ul>
</details>

**标签**: `#LLM calibration`, `#behavioral finance`, `#agent-based modeling`, `#loss aversion`, `#asset pricing`

---

<a id="item-18"></a>
## [: 将 CRRA 投资组合选择与 Rényi 信息投射相联系](https://arxiv.org/abs/2605.03184) ⭐️ 8.0/10

: 该论文表明，单期 CRRA 投资组合优化可以重新表述为 Rényi 信息投射问题，从而得到具有闭形式更新的 Blahut‑Arimoto 风格交替优化算法。 : 通过将金融与信息理论联系起来，该工作提供了一种新的计算高效的投资组合优化方法，并为跨学科研究开辟了新途径。 : 确定性等效增长率被分解为 Rényi 散度项、Rényi 熵项和对数配分函数项；利用 Rényi 散度的变分形式得到一种交替方案，包含闭形式的辅助更新和 KL 型投资组合步骤，在低风险厌恶情况下经验上收敛速度快于直接 CRRA 优化。

rss · arXiv Quantitative Finance · May 12, 04:00

**背景**: : CRRA 效用描述了相对风险厌恶不变的投资者，对应于等弹性效用函数。Rényi 散度是 Kullback‑Leibler 散度的推广，用可调节的阶数α来衡量两个概率分布之间的差异。Blahut‑Arimoto 算法是一种交替优化方法，用于计算信道容量或速率失真函数，通过在辅助分布和输入分布之间交替求解实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rényi_entropy">Rényi entropy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blahut–Arimoto_algorithm">Blahut–Arimoto algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Risk_aversion">Risk aversion - Wikipedia</a></li>

</ul>
</details>

**标签**: `#portfolio optimization`, `#information theory`, `#CRRA utility`, `#Rényi divergence`, `#Blahut-Arimoto algorithm`

---