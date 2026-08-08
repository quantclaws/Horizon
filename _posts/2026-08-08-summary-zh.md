---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> From 36 items, 5 important content pieces were selected

---

1. [前 NSA 局长警告不要将水系统控制器连接到互联网](#item-1) ⭐️ 8.0/10
2. [通过批处理、算子融合和 SIMD 使 Postgres 在分析场景下提速 300 倍](#item-2) ⭐️ 8.0/10
3. [网站所有者与消耗其 150 万页面站点 99%流量的机器人进行斗争](#item-3) ⭐️ 8.0/10
4. [通过希尔伯特空间技术的波动性表面统一数学理论](#item-4) ⭐️ 8.0/10
5. [基于速度和市场状态的期权市场操纵检测方法及 SHAP 可解释性](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [前 NSA 局长警告不要将水系统控制器连接到互联网](https://www.theregister.com/security/2026/08/07/water-system-controllers-dont-belong-on-the-internet-says-ex-nsa-chief-after-suspected-iran-attacks/5285070) ⭐️ 8.0/10

前 NSA 局长迈克尔·海登警告称，水系统控制器不应连接到互联网，此前发生疑似伊朗对美国水务基础设施的网络攻击，引发了关于保障运营技术安全的技术讨论。 此警告凸显了关键基础设施面临的日益增长风险，因为国家支持的黑客越来越多地针对水务系统发动攻击，一旦被入侵可能会破坏基本服务和公共安全。 讨论指出，许多即使未连接互联网的水务系统仍使用不安全的 RF 或蓝牙链接，且老旧 PLC 常运行过时固件，存在如以太网/IP 在 44818 端口等已知漏洞。

hackernews · Bender · Aug 7, 21:19 · [社区讨论](https://news.ycombinator.com/item?id=49216362)

**背景**: 运营技术（OT）是指用于监控和控制工业设备的硬件和软件，例如水处理厂中的可编程逻辑控制器（PLC）。这些系统因其在关键基础设施中的作用而日益成为网络攻击目标，但许多系统缺乏现代安全防护，且在不影响运行的情况下难以进行更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.epa.gov/system/files/documents/2024-03/assessing-if-a-wws-has-ot_508_c.pdf">Assessing if a Water & Wastewater System has Operational Technology</a></li>
<li><a href="https://colortokens.com/blogs/ot-security-water-utilities-microsegmentation/">Public Water Systems Are Targeted by State Actors: How to Protect PLCs and HMIs in the Operational Technology Network - ColorTokens</a></li>
<li><a href="https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/">OT Security Analysis: Exposed Devices Attacked in US Water Systems</a></li>
<li><a href="https://cybersecuritynews.com/internet-exposed-rockwell-plcs/">4,400+ Internet - Exposed Rockwell PLCs Expose Water Systems to...</a></li>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a">Iranian-Affiliated Cyber Actors Exploit Programmable Logic ... - CISA</a></li>
<li><a href="https://cybernews.com/security/michigan-georgia-water-system-attacks-iran/">Iran-linked water attacks spread to 12 US states | Cybernews</a></li>

</ul>
</details>

**社区讨论**: 评论者就连接的利弊展开了讨论，有人认为即使是气隙系统也可能通过 RF 和蓝牙等无线协议受到攻击，而另一些人则认为现代零信任架构在需要时可以实现安全的远程访问。还有人指出，应将 30 年老旧的 PLC 保持断开状态直至更换。

**标签**: `#cybersecurity`, `#critical infrastructure`, `#OT security`, `#PLC`, `#network security`

---

<a id="item-2"></a>
## [通过批处理、算子融合和 SIMD 使 Postgres 在分析场景下提速 300 倍](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10

作者详细说明了他们如何通过在 pgrust 项目中使用批处理、算子融合和 SIMD 向量化，使 Postgres 在分析查询上的性能提升了 300 倍，pgrust 是一个用 Rust 重写的 PostgreSQL，保持了线路和 SQL 兼容性。 这一成就展示了使用系统编程语言和硬件感知优化来现代化传统数据库系统的潜力，提供了一条在不牺牲 Postgres 兼容性的前提下实现分析性能大幅提升的路径。 pgrust 项目通过形式验证和差分模糊测试来确保正确性，已证明超过 1000 个面向用户的函数与原生 Postgres 行为完全一致，并通过了全部 46,066 个回归测试。

hackernews · poly2it · Aug 7, 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: PostgreSQL 是一种广泛使用的开源关系型数据库，传统上使用 C 语言编写，其面向行的执行模型可能限制分析查询性能。批处理（一次处理多行）、算子融合（将多个操作合并为更少的传递）和 SIMD（单指令多数据）向量化等技术在现代分析数据库中被广泛使用，通过利用 CPU 并行性和减少内存带宽瓶颈来提高吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now faster than ...</a></li>
<li><a href="https://pgrust.com/">pgrust — postgres, rewritten in rust</a></li>
<li><a href="https://betterstack.com/community/guides/databases/pgrust-postgres/">PGRust: A Rust Rewrite of PostgreSQL That Passes All Regression Tests</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示对该技术方法的热情，称赞其通过形式验证和模糊测试确保正确性的努力，但也有人对采用持怀疑态度，认为人们可能不会选择 pgrust 而非原生 Postgres，因为信任核心团队和长期维护是关键，同时也有人对自适应规划功能表达兴趣。

**标签**: `#PostgreSQL`, `#query optimization`, `#SIMD`, `#operator fusion`, `#database performance`

---

<a id="item-3"></a>
## [网站所有者与消耗其 150 万页面站点 99%流量的机器人进行斗争](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/) ⭐️ 8.0/10

一位网站所有者透露，其 150 万页面网站中 99%的流量由爬虫和机器人组成，导致严重的财务压力和运营挑战，正如其公开账户所述。 这凸显了对独立网站日益增长的威胁，机器人流量削弱了网站价值，增加了成本，并侵蚀了创作者的收益，促使人们迫切需要有效且易于使用的缓解策略。 该所有者报告称，正常托管成本约为每月 90 美元，在机器人激增期间飙升至 500%，而像 Claude-searchbot 这样的 AI 爬虫在 72 小时内抓取了超过 200,000 页却几乎没有带来推荐流量，并讨论了如 Anubis 这样的工具，它使用工作量证明来区分真实浏览器。

hackernews · petercooper · Aug 7, 14:51 · [社区讨论](https://news.ycombinator.com/item?id=49211386)

**背景**: 机器人缓解涉及检测和阻止滥用网站的自动化流量，使用诸如速率限制、验证码、行为分析和工作量证明挑战等技术。随着爬虫变得越来越复杂——模拟人类行为、轮换 IP 地址和使用无头浏览器——简单的防御措施已失效，需要分层策略。像 Cloudflare 这样的服务提供 AI 驱动的爬虫控制，但引发了对谁可以访问网站的集中控制的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://queue-it.com/blog/bot-mitigation/">Bot Mitigation : How to Detect & Block Bots</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/">How to prevent web scraping</a></li>
<li><a href="https://blog.captcha.la/posts/2025-11-20-anti-scraping-measures">Essential Anti Scraping Measures to Protect Your... | CaptchaLa Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者对依赖 Cloudflare 等集中式提供商表示担忧，因为它们可以静默地封锁用户而无需申诉，这削弱了开放网络的原则。其他人称赞 Anubis 作为一种有效的工作量证明替代方案，适用于未使用主要 CDN 的网站，而一些人则承认自己在抓取数据的同时却抱怨爬虫存在讽刺意味。

**标签**: `#web scraping`, `#bot mitigation`, `#Cloudflare`, `#website performance`, `#open web`

---

<a id="item-4"></a>
## [通过希尔伯特空间技术的波动性表面统一数学理论](https://arxiv.org/abs/2608.05198) ⭐️ 8.0/10

该论文利用无限维状态空间和希尔伯特空间技术，发展了隐含、局部和学习波动性表面的统一数学理论，建立了无套利集合的拓扑和切线几何，并推导出具有封闭形式截断误差的确切模态简化。 该框架统一了波动性建模中的表示、动态、无套利、维度降低、学习、模拟和对冲，为定量金融研究者提供了构建和分析无套利波动性表面的严格基础。 该论文证明，在活跃约束处的非退化高斯冲击以趋近于一半的概率退出，推导出 Musiela 到期运输同一性，将投资组合导数识别为维加场，并通过希尔伯特空间动态和 Karhunen–Loève 因子获得协方差最优对冲α* = (H*CH)⁻¹H*Cν。

rss · arXiv Quantitative Finance · Aug 7, 04:00

**背景**: 波动性表面描述了隐含波动性如何随行权价格和到期时间变化，而无套利约束要求正性、日历单调性和蝴蝶条件。希尔伯特空间方法曾被用于将隐含波动性表面的演化建模为随机偏微分方程的解，而 Karhunen–Loève 分解是函数数据分析中降维的标准工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/0712.1343">[0712.1343] An Hilbert space approach for a class of arbitrage free implied volatilities models</a></li>
<li><a href="https://arxiv.org/html/2608.05198">The Mathematics of Volatility Surfaces Arbitrage Geometry, Local...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kosambi–Karhunen–Loève_theorem">Kosambi– Karhunen – Loève theorem - Wikipedia</a></li>

</ul>
</details>

**标签**: `#volatility modeling`, `#mathematical finance`, `#arbitrage theory`, `#functional analysis`, `#quantitative finance`

---

<a id="item-5"></a>
## [基于速度和市场状态的期权市场操纵检测方法及 SHAP 可解释性](https://arxiv.org/abs/2608.05373) ⭐️ 8.0/10

该研究提出了一种基于速度和市场状态的期权市场操纵检测方法，使用平滑后的状态速度（指数期权的期权 Delta 速度，股票的价格速度）和基于 SHAP 的可解释性，在印度 BANKNIFTY 指数期权的测试集上实现了对监管机构标记的操纵日的 100%召回率。 该方法解决了金融监管中的关键挑战，能够检测传统方法易漏的短暂且统计难以区分的操纵模式，为监管机构提供了一种更精准的工具来识别高频期权市场中的拉高出货骗局，而不会产生过多误报。 检测管道使用分钟级数据，采用严格的样本外测试和预设阈值，并通过隐马尔可夫模型推断市场状态来条件化检测；SHAP 归因表明未确认的警报与确认的操纵日在特征重要性分布上高度相似（余弦相似度 0.99），表明精度上限源于标签不完整而非模型失效。

rss · arXiv Quantitative Finance · Aug 7, 04:00

**背景**: 当日内市场操纵难以检测，因为其信号短暂、掩没在高频报价数据中，且在统计上与正常波动难以区分。传统检测器只有通过产生大量误报才能实现高召回率，导致精度降至不可用的水平。本文认为，操纵会在市场状态的速度（变化率）中留下动态特征——如期权 Delta 或价格——而不仅仅在绝对水平上，因此可通过基于速度的特征进行检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05373">Velocity- and Regime - Aware Detection of Intraday Options Market ...</a></li>
<li><a href="https://shap.readthedocs.io/en/latest/index.html">Welcome to the SHAP documentation — SHAP latest documentation</a></li>

</ul>
</details>

**标签**: `#market manipulation detection`, `#financial machine learning`, `#explainable AI`, `#intraday trading`, `#options market surveillance`

---