---
layout: default
title: "Horizon Summary: 2026-07-08 (ZH)"
date: 2026-07-08
lang: zh
---

> From 81 items, 23 important content pieces were selected

---

1. [Kokoro：CPU 友好、高质量开源 TTS 模型](#item-1) ⭐️ 8.0/10
2. [欧盟聊天控制 1.0 和 2.0 提案解释](#item-2) ⭐️ 8.0/10
3. [欧盟要求所有新车从 2026 年起配备驾驶员监控摄像头](#item-3) ⭐️ 8.0/10
4. [介绍 PgDog：支持预编译语句的新 Postgres 连接池。](#item-4) ⭐️ 8.0/10
5. [微软裁掉 id Software 的 idTech 引擎团队，转向虚幻引擎 5](#item-5) ⭐️ 8.0/10
6. [sqlite-utils 4.0 添加数据库架构迁移、嵌套事务和复合外键支持](#item-6) ⭐️ 8.0/10
7. [在 Pump.fun 检测到 1,012 个协同钱包队列](#item-7) ⭐️ 8.0/10
8. [DSGE 作为结构化世界模型：在经济世界中基准测试反事实泛化](#item-8) ⭐️ 8.0/10
9. [点过程的精确条件模拟用于路径依赖的市场冲击估计](#item-9) ⭐️ 8.0/10
10. [谱方差比推广产生五因子模型适用于美国股票回报](#item-10) ⭐️ 8.0/10
11. [提出 GAICF 以使生成式 AI 治理符合 SR 26-2 银行监管](#item-11) ⭐️ 8.0/10
12. [用于具有递归效用的动态规划的深度学习](#item-12) ⭐️ 8.0/10
13. [研究表明上审查提升 Q 学习定价算法的利润](#item-13) ⭐️ 8.0/10
14. [WorldTensor：用于地球系统基础模型的全球协调数据集](#item-14) ⭐️ 8.0/10
15. [将前视自由形式化为时间非干扰以实现可验证的交易管道](#item-15) ⭐️ 8.0/10
16. [最终赔率不足以推断赛马中的信念。](#item-16) ⭐️ 8.0/10
17. [内生网格方法通过幂变换扩展至 Epstein-Zin 偏好](#item-17) ⭐️ 8.0/10
18. [城市聚集为 17 种增长制度，传播经济冲击](#item-18) ⭐️ 8.0/10
19. [基于物理信息的 VAE-神经 SDE 模型实现无套利收益率曲线预测](#item-19) ⭐️ 8.0/10
20. [概率方法证明最优停止边界的连续可微性。](#item-20) ⭐️ 8.0/10
21. [用于无界扩散过程的自适应分区强化学习及其遗憾界](#item-21) ⭐️ 8.0/10
22. [基于布朗运动签名的随机过程通用逼近。](#item-22) ⭐️ 8.0/10
23. [AI Premium](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kokoro：CPU 友好、高质量开源 TTS 模型](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

文章介绍了 Kokoro，一个拥有 8200 万参数的开源文本转语音模型，能够在 CPU 和 Apple Silicon 上高效运行，无需 NVIDIA GPU 即可合成高质量语音。 Kokoro 通过免除 GPU 依赖降低了高质量 TTS 的门槛，使 modeste 硬件的开发者和用户也能使用先进语音合成，其 IPA 支持还能提升语言应用中的发音准确性。 该模型支持手动添加 IPA 发音指南，可通过微调提供多种声音，并以 CLI 工具及 mlx-audio 库形式在 Apple Silicon 上运行；但用户报告有时会误读同形异音词，且在极短语句上的表现略显不足。

hackernews · speckx · Jul 7, 18:24 · [社区讨论](https://news.ycombinator.com/item?id=48821576)

**背景**: 大多数高质量的神经文本转语音模型依赖 NVIDIA GPU 进行实时推理，这限制了它们在低端或仅有 CPU 的系统上的使用。Kokoro 是一个开源的 8200 万参数 TTS 模型，专为在 CPU 和 Apple Silicon 上高效运行而设计，利用 mlx-audio 框架。它能够生成自然的语音，同时规避了 GPU 依赖方案带来的硬件门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kokoro_TTS">Kokoro TTS</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Kokoro 能在 modeste 硬件上实现高质量 TTS，称赞其 IPA 支持以及在无障碍工具、文章朗读器和浏览器扩展中的易用性。一些用户指出其在同形异音词上的偶发误读以及极短语句合成时的自然度不足。总体而言，社区对 Kokoro 的 CPU 友好方案表现出浓厚兴趣并认可其实用价值。

**标签**: `#TTS`, `#Kokoro`, `#CPU-friendly`, `#accessibility`, `#open-source`

---

<a id="item-2"></a>
## [欧盟聊天控制 1.0 和 2.0 提案解释](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

该文章概述了欧盟的聊天控制 1.0（允许自愿扫描私人消息的临时豁免）和聊天控制 2.0（强制扫描加密通信的提案），说明其范围并引发了关于监视和加密的社区讨论。 这些提案威胁到端到端加密，因为它们可能要求客户端扫描或后门访问，引发隐私倡导者、工程师和更广泛的数字权利社区对潜在大规模监视和隐私保护削弱的担忧。 聊天控制 1.0 于 2021 年通过，创建了电子隐私指令的临时豁免，允许提供者自愿使用 AI 和哈希匹配扫描已知的 CSAM；聊天控制 2.0 则旨在使此类扫描成为强制性要求，并应用于加密消息，可能通过客户端扫描或中间人解密实现，影响所有用户而不仅仅是嫌疑人。

hackernews · gasull · Jul 7, 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48818311)

**背景**: 电子隐私指令保护欧盟电子通信的保密性，但 2021 年欧盟理事会引入了临时豁免（聊天控制 1.0），以允许自愿扫描儿童性虐待材料。聊天控制 2.0 在此基础上提出永久框架，要求扫描加密聊天，引发了对客户端扫描技术的担忧，该技术在加密前分析内容。这些提案与关于在儿童保护与加密及隐私权之间取得平衡的持续辩论相交叉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html">Chat Control 1.0: EU Council forces messenger scans via fast-track | heise online</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍担忧这些提案构成过度，认为鉴于犯罪者仅占少数，广泛的监视措施缺乏正当性。一些人指出技术上的担忧，如对加密消息的影响以及客户端扫描可能削弱隐私；还有人提到尽管聊天控制 1.0 已到期，自愿扫描仍在继续。

**标签**: `#privacy`, `#encryption`, `#EU policy`, `#chat control`, `#surveillance`

---

<a id="item-3"></a>
## [欧盟要求所有新车从 2026 年起配备驾驶员监控摄像头](https://allaboutcookies.org/eu-mandatory-distracted-driver-system) ⭐️ 8.0/10

欧盟将要求其成员国所有新车从 2026 年 7 月起配备驾驶员监控摄像头系统，以检测分心驾驶。 此规定标志着汽车安全政策的重大转变，将影响数百万新车，促使制造商集成先进感测技术，同时引发隐私和用户体验方面的担忧。 该规定源于欧盟一般安全法规（GSR），要求驾驶员疲劳和注意力警告（DDAW）系统使用红外摄像头跟踪注视、头部位置和眼闭合，适用于 M 和 N 类车辆。

hackernews · nickslaughter02 · Jul 7, 20:50 · [社区讨论](https://news.ycombinator.com/item?id=48823557)

**背景**: 驾驶员监控系统（DMS）使用摄像头和红外传感器通过跟踪驾驶员的面部、眼睛和头部位置来检测分心或疲劳的迹象。欧盟的一般安全法规（GSR）最早于 2019 年制定，已要求车辆配备驾驶员疲劳和注意力警告（DDAW）系统，而即将修订的条款将从 2026 年 7 月起使此类摄像头在所有新注册的汽车、货车、卡车和公共汽车上成为强制要求。这些系统可以与预碰撞安全功能协同工作，旨在减少因注意力不集中导致的事故。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smarteye.se/blog/the-general-safety-regulations-gsr-and-driver-monitoring-systems-dms/">How Driver Monitoring Systems (DMS) Are Being Made Mandatory in 18 Million European Cars - Smart Eye</a></li>
<li><a href="https://www.idtechex.com/en/research-article/regulations-drivers-for-mandating-driver-monitoring-systems/30322">Regulations - Drivers for Mandating Driver Monitoring Systems | IDTechEx Research Article</a></li>
<li><a href="https://medium.com/@shahadilh18/your-car-will-soon-watch-your-eyes-b8e78dcfb114">Your Car Will Soon Watch Your Eyes. Here Is the Real Story Behind the EU’s Driver Monitoring Mandate | by Shahadilh | Medium</a></li>

</ul>
</details>

**社区讨论**: 许多评论者抱怨这些新系统会产生烦人的误报、过于激进的车道保持提示音以及糟糕的用户体验，尤其是与 Android Auto 集成时。也有人指出该技术能够准确检测到诸如与乘客交谈或调节空调等细微分心行为，并相信它可以挽救生命。隐私担忧和数据滥用的疑虑也被提出，部分用户甚至表示因为这些侵入式功能而不愿购买较新的汽车。

**标签**: `#EU regulation`, `#automotive safety`, `#driver monitoring`, `#privacy`, `#vehicle technology`

---

<a id="item-4"></a>
## [介绍 PgDog：支持预编译语句的新 Postgres 连接池。](https://pgdog.dev/blog/why-yet-another-connection-pooler) ⭐️ 8.0/10

作者介绍了 PgDog，一个支持预编译语句、采用 AGPL 许可证的新 Postgres 连接池，旨在解决现有连接池的连接状态泄漏等不足。 PgDog 填补了连接池中对预编译语句的支持空白，提升查询性能和可扩展性；其 AGPL 许可证保证网络服务软件的开源友好，且提供负载均衡和分片功能，使 Postgres 能在不修改应用的情况下实现水平扩展。 PgDog 工作在 OSI 第七层，能够解析 Postgres 协议，代理多个副本和主节点，均匀分发事务，并在客户端之间重置会话状态以防止连接状态泄漏。它采用 AGPL‑3.0 许可证，支持预编译语句处理并提供可选的查询缓存功能。

hackernews · levkk · Jul 7, 15:36 · [社区讨论](https://news.ycombinator.com/item?id=48819308)

**背景**: 连接池通过复用数据库连接来降低开销，但可能导致会话状态（如预编译语句、临时表）从一个客户端泄漏到另一个客户端，引发错误。预编译语句让数据库只需解析和规划一次查询，随后重复使用执行计划，从而提升性能。AGPL 许可证是一种强 copyleft 许可证，专为网络访问的软件设计，确保对网络服务软件的修改也必须以相同许可证发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pgdog.dev/blog/why-yet-another-connection-pooler">Why we built yet another Postgres connection pooler - PgDog</a></li>
<li><a href="https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License">GNU Affero General Public License - Wikipedia</a></li>
<li><a href="https://www.postgresql.org/docs/current/sql-prepare.html">PostgreSQL: Documentation: 18: PREPARE</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 PgDog 对预编译语句的支持及其 AGPL 许可证，担心在典型 Postgres 部署中会出现连接状态泄漏，并询问是否会加入查询缓存以及适用于 Django‑tenant 等多租户框架的模式切换功能。

**标签**: `#PostgreSQL`, `#connection pooling`, `#PgDog`, `#database infrastructure`, `#open source`

---

<a id="item-5"></a>
## [微软裁掉 id Software 的 idTech 引擎团队，转向虚幻引擎 5](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

微软已经裁掉了 id Software 的整个 idTech 引擎团队，确认将采用 Epic 的虚幻引擎 5 作为未来 id Software 游戏的引擎。这一裁员消息由 GameFromScratch 报道，引发了关于内部引擎开发影响的广泛讨论。 这一决定表明了从专有内部引擎转向授权第三方技术的重大转变，可能降低开发成本但也可能失去定义 id Software 旗舰系列的独特技术身份。这也反映了行业更广泛的趋势，即即使是老牌工作室也采用虚幻引擎 5 以保持竞争力。 裁员影响了整个 idTech 团队，该团队自 id Tech 5 以来一直维护引擎，并参与了 id Tech 6 和 id Tech 7 的开发，这些引擎用于最近的《毁灭战士》作品。微软和 id Software 尚未发布官方声明，文章也指出缺乏具体证据确认哪些员工被裁。

hackernews · bauc · Jul 7, 15:33 · [社区讨论](https://news.ycombinator.com/item?id=48819244)

**背景**: id Software 开发了 idTech 系列专有游戏引擎，从用于原版《毁灭战士》的 id Tech 1 开始，经过 id Tech 5（首次出现在《Rage》中）和 id Tech 7（驱动《毁灭战士：永恒》），这些引擎以其前沿图形和与 id 游戏设计的紧密集成而闻名。近年来，许多工作室转向授权虚幻引擎 5 等引擎以降低内部维护成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_tech_5_engine">Id tech 5 engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech_5">id Tech 5 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者担心失去 idTech 团队会削弱 id Software 的技术独特性，导致输出趋于同质化并依赖虚幻引擎 5，有人批评微软的举措是垄断性失误，使 Epic 受益。也有人质疑裁员的证据，指出文章更多依赖猜测而非确认的报道。

**标签**: `#Microsoft`, `#id Software`, `#game engine`, `#layoffs`, `#Unreal Engine 5`

---

<a id="item-6"></a>
## [sqlite-utils 4.0 添加数据库架构迁移、嵌套事务和复合外键支持](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

Simon Willison 在 2026 年 7 月 7 日发布了 sqlite-utils 4.0，首次引入数据库架构迁移、通过 db.atomic() 实现的嵌套事务以及复合外键支持。 此版本显著简化了 SQLite 数据库的演进和事务管理，对使用 Datasette 和 sqlite-utils 的开发者尤为有价值。 迁移通过 Python 的 Migrations 类和 table.transform() 方法定义，嵌套事务利用保存点实现 db.atomic()，复合外键允许多列外键约束，同时包含一些破坏性変更的升级指南。

rss · Simon Willison · Jul 7, 19:32

**背景**: sqlite-utils 是一个流行的 Python 命令行工具和库，用于操作 SQLite 数据库，常与 Datasette 配合使用。数据库架构迁移允许开发者用 Python 脚本描述表结构的变更，并通过跟踪已应用的版本来自动执行待处理的迁移。嵌套事务利用 SQLite 的保存点机制，使得事务可以在更大的事务内部安全地嵌套。复合外键则支持基于多列的外键约束，以实现更复杂的关系模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/">sqlite-utils 4.0rc1 adds migrations and nested transactions</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#database-migrations`, `#python`, `#datasette`, `#release`

---

<a id="item-7"></a>
## [在 Pump.fun 检测到 1,012 个协同钱包队列](https://arxiv.org/abs/2607.02795) ⭐️ 8.0/10

研究人员使用两阶段检测管道分析了 2026 年 6 月 12 日至 6 月 26 日期间 166,098 次 Solana pump.fun 代币发行的 158 万条买家观察数据，发现了 1,012 个持久钱包队列（每队列 2‑12 个钱包），这些队列反复出现为早期买家。这些队列与首 30 分钟买家数量增加+132.3%以及 SOL 流入增加+136.5%相关，相比未受队列影响的发行。 该研究表明，协同买家群体能够显著夸大早期发行指标，暴露了 Solana meme‑token 市场中的操纵风险。监管者、开发者和分析师可采用所提出的检测管道来监控此类行为，并改进链上活动的因果推断方法。 检测管道首先提取每次发行的首买窗口，然后构建跨发行的共现图并应用 union‑find 算法，以筛选出由 2‑12 个钱包组成的持久队列。虽然受队列影响的发行显示买家流量提升+132.3%，但活动匹配的安慰剂产生更大的+216.3%提升，表明存在选择偏差；作者以 CC‑BY‑4.0 许可证发布了完整的队列目录、代码和鲁棒性工件，命名为 RED‑COHORT‑2026‑v1。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: Pump.fun 使用键合曲线机制，其中代币价格是流通供应量的确定性函数，使得无需订单簿即可实现即时交易。union‑find 数据结构能够高效地将反复共同出现的元素分组，适用于发现跨多次代币发行而共同担任早期买家的钱包集合。首买窗口提取将在代币发行初期购买的钱包隔离出来，为检测协同狙击行为提供所需信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pump.fun/docs/bonding-curve">The Pump.fun bonding curve | Pump</a></li>
<li><a href="https://github.com/laurentpetit/union-find">GitHub - laurentpetit/union-find: Persistent Union-Find ...</a></li>
<li><a href="https://docs.mobula.io/guides/how-to-track-token-first-buyers">How to Track Token First Buyers Across Solana, Ethereum, BNB ...</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#DeFi`, `#market manipulation`, `#Solana`, `#wallet clustering`

---

<a id="item-8"></a>
## [DSGE 作为结构化世界模型：在经济世界中基准测试反事实泛化](https://arxiv.org/abs/2607.03144) ⭐️ 8.0/10

论文认为动态随机一般均衡（DSGE）模型是结构化的世界模型，并提出了 DSGE‑Gym 基准，包含八个带有离轨反事实测试集的 DSGE 环境，规模达到欧洲央行 230 变量的新区域宽模型。结果表明，学习的世界模型在路径上能匹配动态，但在离轨状态下表现崩溃，尾部 RMSE 可达到路径上的约 40 倍；在 DSGE 生成的数据上训练可使尾部误差减半，并将政策 regime 误差降低 10‑280。 将 DSGE 经济模型与机器学习世界模型结合，为衡量和提升反事实泛化提供了一种 principled 方法，这正是当前强化学习代理的关键弱点。该基准为经济学家和 AI 研究者提供了共享的测试床，以评估结构性知识如何合成缺失的数据分布，从而实现稳健的政策分析和决策。 DSGE‑Gym 包含八个 DSGE 环境，从简单的教科书模型到欧洲央行的 230 变量新区域宽模型，每个环境都配备了由罕见且反事实的政策生成的离轨测试集，这些测试集无法从单一历史轨迹中采样得到。标准世界模型架构在路径上能匹配动态，但在离轨情况下尾部 RMSE 可升至路径水平的约 40 倍；在 DSGE 生成的数据上训练可使尾部误差减半，并在政策 regime 误差方面下降 10‑280，当反事实规则改变遍历支持时；所有代码和环境已公开以确保可重复性。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 动态随机一般均衡（DSGE）模型是一种宏观经济框架，描述经济作为在市场清算的情况下，互 temporally 最优化的智能体的随机演化，提供了具有因果结构和硬约束的经济动态表示。机器学习世界模型如 Dreamer、IRIS、Genie 和 JEPA 通过观察轨迹学习环境的内部信念状态，并预测其随动作的变化，但其转移函数仅在已见数据的区域可靠。反事实泛化指的是模型在从未见过的状态上做出准确预测的能力，这对于在分布偏移或新政策下进行稳健决策至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_stochastic_general_equilibrium">Dynamic stochastic general equilibrium - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/decision-transformer-with-counterfactuals">Decision Transformer with Counterfactuals - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#DSGE`, `#world models`, `#counterfactual generalization`, `#reinforcement learning`, `#economics`

---

<a id="item-9"></a>
## [点过程的精确条件模拟用于路径依赖的市场冲击估计](https://arxiv.org/abs/2607.03239) ⭐️ 8.0/10

本文提出了一种在扰动强度下点过程的精确条件模拟算法，利用稀薄表示在共同随机性源上重构反事实价格路径。 这使得可以对各种执行策略进行严格的路径依赖市场冲击估计，解决了量化金融中关键的不可观测反事实问题。 该方法刻画了稀薄表示中隐含泊松随机测度的条件律，从而得到一个事件驱动的精确模拟器，适用于激进、被动和混合交易策略。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 点过程用于建模离散事件的时间序列，如交易或价格跳跃，其强度通常依赖于过去的事件历史。在稀薄表示中，点过程通过以时间变化的接受概率稀薄均匀泊松过程产生，引入一个隐含的泊松随机测度。市场冲击被定义为在给定执行策略下观测到的价格轨迹与未执行该策略时的不可观测反事实轨迹之间的差异，因此需要在相同的市场随机性下模拟替代路径。

**标签**: `#point processes`, `#market impact`, `#stochastic simulation`, `#quantitative finance`, `#thinning representation`

---

<a id="item-10"></a>
## [谱方差比推广产生五因子模型适用于美国股票回报](https://arxiv.org/abs/2607.03858) ⭐️ 8.0/10

作者提出了 Lo‑MacKinlay（1988）方差比的多变量推广，将长期股票回报动态分解为独立的回报通道和波动率通道记忆分量，从而得到一个简洁的五因子模型。 该框架能够同时拟合多个美国和欧洲股票面板，恢复七个长期动态的风格化事实，并揭示了美国波动率记忆的 regime 转变，为量化金融和因子投资提供了新工具。 该模型捕捉了回报和波动率中的持续性、反持续性和多尺度记忆；滚动窗口 bootstrap 将波动率记忆的 regime 转变定位在 20 世纪 80 年代末，最慢分量从约 2 年延长至约 4 年；跨通道 beta‑反转检验拒绝共享载荷，表明回报通道和波动率通道记忆的驱动因素不同。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: Lo‑MacKinlay 方差比检验由 Lo 和 MacKinlay 在 1988 年提出，是检验随机游走假设的广泛使用的参数检验，通过比较不同 horizon 的方差估计量来实现。谱推广将此思想扩展到通过频率分析协方差矩阵的特征结构，从而能够将回报动态分解为记忆分量。金融时间序列中的长记忆过程指的是自相关缓慢衰减，这种现象既可以出现在回报中也可以出现在波动率中。因子模型如 Fama‑French 框架通过少量风险因子来捕捉横截面回报模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://metricgate.com/docs/lo-mackinlay-variance-ratio/">Lo-MacKinlay Variance Ratio Test Calculator | MetricGate</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spectral_density">Spectral density - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S154461232502197X">Long memory of stock market return volatility and its impact ...</a></li>

</ul>
</details>

**标签**: `#financial econometrics`, `#factor models`, `#variance ratio`, `#spectral analysis`, `#equity returns`

---

<a id="item-11"></a>
## [提出 GAICF 以使生成式 AI 治理符合 SR 26-2 银行监管](https://arxiv.org/abs/2607.04103) ⭐️ 8.0/10

本文提出了生成式 AI 控制框架（GAICF），旨在与美国金融机构更新的 SR 26-2 模型风险管理指导相兼容。 GAICF 通过将 SR 26-2 的基于风险的原则扩展到处于传统模型边界之外但影响监管决策的生成式 AI 用途，填补了关键空白，帮助银行满足监管期望。 GAICF 将模型风险管理的核心概念——如治理、验证和监控——转化为适用于生成式 AI 工作流的分层控制结构，这些工作流虽然位于正式模型边界之外，但仍嵌入银行业务流程中。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: SR 26-2 于 2026 年 4 月发布，取代 SR 11-7 成为美国联邦储备银行的模型风险管理监管指导，将以前的处方清单转变为基于原则、以风险为中心的方法，扩大了模型的定义并增加了明确的 AI/ML 要求。尽管 SR 26-2 现代化了模型风险管理，但未明确涵盖生成式和代理 AI，这使得在这些技术被用于监控解释、政策分析或不利行动语言起草等场景的金融机构面临治理空白。因此，需要一个补充框架，使生成式 AI 治理与 SR 26-2 的基于风险的期望保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf">FRB: Supervisory Letter SR 26-2 on Revised Guidance on Model ...</a></li>
<li><a href="https://tanukamandal.com/sr-11-7-vs-sr-26-2-guide-to-model-risk-evolution/">SR 11-7 vs SR 26-2 Detail Guide to Evolution of Model Risk</a></li>
<li><a href="https://coalitiongreenwichuat.crisil.com/content/dam/crisil-integral-iq/what-we-think/all-our-thinking/reports/2026/04/navigating-the-mrm-framework-shift--from-sr-11-7-to-sr-26-2/navigating-the-mrm-framework-shift-from-sr-11-7-to-sr-26-2.pdf">Navigating the MRM framework shift From SR 11-7 to SR 26-2</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#model risk management`, `#financial regulation`, `#SR 26-2`, `#AI governance`

---

<a id="item-12"></a>
## [用于具有递归效用的动态规划的深度学习](https://arxiv.org/abs/2607.04278) ⭐️ 8.0/10

该论文提出了确定性等价学习（CEL）算法，一种深度学习方法，直接学习确定性等价值以求解高维离散时间递归效用动态规划问题。 CEL 是首个用于递归效用动态规划的深度学习方法，能够在高维情况下进行无网格、基于仿真的求解，无需欧拉方程或可微性，为复杂的经济和金融建模提供了新途径。 CEL 算法使用神经网络联合近似价值函数、策略函数和确定性等价函数；在折线指数二次高斯控制、小噪声鲁棒控制、Epstein-Zin DSGE 和多变量战略资产配置问题上的测试表明，贝尔曼误差在 1.0e-4 到 1.0e-3 之间。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 递归效用（例如 Epstein-Zin 偏好）将效用表示为当前消费和未来效用的函数，缺乏显式闭式形式，导致贝尔曼方程中的确定性等价难以评估。传统动态规划依赖基于网格的价值函数迭代或欧拉方程，在高维情况下变得不可行。确定性等价是指具有相同预期效用的确定金额，直接学习它可以避免解析积分或求导的需要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_economics">Recursive economics - Wikipedia</a></li>

</ul>
</details>

**标签**: `#deep learning`, `#dynamic programming`, `#recursive utility`, `#reinforcement learning`, `#numerical methods`

---

<a id="item-13"></a>
## [研究表明上审查提升 Q 学习定价算法的利润](https://arxiv.org/abs/2607.04345) ⭐️ 8.0/10

本文考察了三种信息披露规则——无披露、全披露和上审查——在企业将定价委托给 Q 学习算法且需求随机的情况下。结果显示，上审查带来的利润高于全披露，但出现利润逆转：高折扣因子时无披露更有利，低折扣因子时全披露更有利。 这些发现挑战了经典的串通理论，并表明当 AI 定价代理足够耐心时，限制信息共享可能适得其反，为监管者制定遏制算法串通的政策提供了直接依据。该研究将理论与仿真结合，凸显了在 AI 中介市场中重新评估信息设计方法的必要性。 上审查会真实透露低需求状态，同时将高需求状态合并。研究表明，Q 学习代理的利润随折扣因子γ系统变化：高γ时无披露更有利，低γ时全披露更有利，这一模式与传统串通理论的预测恰好相反。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: Q‑learning 是一种无模型的强化学习算法，通过贝尔曼方程更新动作价值，并使用折扣因子平衡即时奖励与未来奖励。在算法定价中，企业将价格决策委托给这样的 Q‑learning 代理，代理从随机需求中学习最优价格。信息设计研究第三方中介的披露规则——如无披露、全披露或上审查——如何影响代理的学习结果和市场表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Q-learning">Q-learning - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2607.04345v1">Strategic Information Disclosure in Algorithmic Pricing</a></li>
<li><a href="https://economics.mit.edu/sites/default/files/inline-files/Platform+Price+Recommendations_2.pdf">Algorithm Design Meets Information Design: Price ...</a></li>

</ul>
</details>

**标签**: `#algorithmic pricing`, `#information design`, `#Q-learning`, `#AI regulation`, `#algorithmic collusion`

---

<a id="item-14"></a>
## [WorldTensor：用于地球系统基础模型的全球协调数据集](https://arxiv.org/abs/2607.03298) ⭐️ 8.0/10

论文介绍了 WorldTensor，一个将数百个环境和社会经济变量对齐到 0.25°空间网格和年度时间框架的全球协调数据集，用于训练地球系统基础模型。 通过提供一个统一的多模态训练资源，将物理气候数据与人类系统连接起来，WorldTensor 使得更全面的地球系统基础模型成为可能，解决了气候 AI 研究中的关键数据限制。 WorldTensor 整合了再分析产品、遥感、排放清单、土地利用重建、水文观测、基础设施和灾害数据以及社会经济指标，所有数据均重新网格化到统一的 0.25°网格，并以符合 CF 元数据约定的 NetCDF 文件形式发布。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 地球系统基础模型是指在多种物理气候和天气数据上训练的大型 AI 模型，以学习变量之间的统计关系，用于下游预测和分析任务。0.25°空间网格对应大约 27.75 公里的分辨率，提供了一种常用于全球再分析数据集（如 ERA5）的精细规则经纬度网格。再分析产品将历史观测与模型模拟结合，生成全球一致的大气、海洋和陆地变量格点场，是气候研究的基础数据来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-09005-y">A foundation model for the Earth system - Nature</a></li>
<li><a href="https://confluence.ecmwf.int/spaces/CKB/pages/65237704/ERA5+What+is+the+spatial+reference">ERA5: What is the spatial reference - Copernicus Knowledge ...</a></li>
<li><a href="https://climatedataguide.ucar.edu/climate-data/atmospheric-reanalysis-overview-comparison-tables">Atmospheric Reanalysis: Overview & Comparison Tables</a></li>

</ul>
</details>

**标签**: `#Earth system science`, `#foundation models`, `#climate data`, `#multimodal datasets`, `#geospatial AI`

---

<a id="item-15"></a>
## [将前视自由形式化为时间非干扰以实现可验证的交易管道](https://arxiv.org/abs/2607.04958) ⭐️ 8.0/10

该论文将前视偏差形式化为时间非干扰，证明其在一般情况下不可判定（Π₁⁰-难），并提供了一个可判定的片段，配合类型-效应系统用于回测和智能体交易管道。 通过连接形式化方法和量化金融，该工作提供了一种可验证的正确性属性，能够检测出现有差分和 tiling 检测器遗漏的前视泄漏，从而提升回测和部署交易算法的可靠性。 可判定的片段涵盖窗口、重采样、连接、点-in-time/复古读取以及智能体检索；由此得到的检查器线性时间运行、健全，并能捕捉到所有被差分和 tiling 检测器遗漏的植入泄漏。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 前视偏差发生在模型使用决策时刻尚未可用的未来信息时，导致回测结果过于乐观。将此偏差视为信息流属性，时间非干扰确保后期数据不会影响早期决策。论文通过时间索引信息格建模数据可用性，并使用管道微积分将数据的可用性与其参考时间分离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.04958v1">Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable ...</a></li>
<li><a href="https://matproof.com/regulatory-updates/arxiv-look-ahead-freedom-as-temporal-non-interference-a-verifiable-correctness-p-6856">arXiv: Look-Ahead-Freedom as Temporal Non-Interference: A ...</a></li>

</ul>
</details>

**标签**: `#look-ahead bias`, `#temporal non-interference`, `#backtesting`, `#formal verification`, `#agentic trading`

---

<a id="item-16"></a>
## [最终赔率不足以推断赛马中的信念。](https://arxiv.org/abs/2509.14645) ⭐️ 8.0/10

该研究利用赛马的临时赔率表明，实现的收益不仅取决于最终赔率，还取决于赔率达到的路径，即在最后五分钟赔率下降的马匹相比最终赔率相似的马匹获得更高的回报。 这一发现挑战了仅凭最终市场价格推断风险偏好或信念的常见做法，强调了博彩市场中的路径依赖可能导致此类推断失真。 作者将奥塔维亚尼－索伦森信息基础模型扩展到两个时期，表明后期知情投注者的下注导致最终阶段赔率下降并产生路径依赖的回报，因此最终赔率－回报模式无法区分信息聚合与概率扭曲。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 在 pari‑mutuel 投注中，所有赌注被合并到一个池子中，赔率在池子封闭后根据池子分配计算，因此投注者无法根据最终赔率下注。奥塔维亚尼－索伦森模型解释了私人信息如何通过知情交易者在下注时更新赔率而导致热门‑长赔偏差。临近比赛时，赔率常因知情交易者的晚间下注而波动，产生路径依赖，即赔率的变化路径会影响回报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Parimutuel_betting">Parimutuel betting - Wikipedia</a></li>
<li><a href="https://igier.unibocconi.eu/sites/default/files/media/attach/131205.pdf">Noise, Information and the Favorite-Longshot Bias∗</a></li>
<li><a href="https://caanberry.com/what-causes-betting-odds-to-change/">What Causes Betting Odds to Change? - Caan Berry Why Do Horse Betting Odds Change? - TheHorseBet.com A Deep Dive Podcast into Betting Odds, Market Efficiency ... Understanding the Key Factors That Influence Betting Odds in ... Horse Racing Winning Odds Statistics: 2026 Market Report</a></li>

</ul>
</details>

**标签**: `#market microstructure`, `#information aggregation`, `#parimutuel betting`, `#behavioral finance`, `#economics`

---

<a id="item-17"></a>
## [内生网格方法通过幂变换扩展至 Epstein-Zin 偏好](https://arxiv.org/abs/2601.04438) ⭐️ 8.0/10

论文表明，通过对价值函数进行幂变换，内生网格方法（EGM）可以应用于 Epstein-Zin 偏好，从而无需求根。该算法相比价值函数迭代实现了一到两个数量级的速度提升，并将准确度提高了超过一个数量级。 这一方法学进步使经济学家能够以更高的速度和准确度求解包含 Epstein-Zin 偏好的动态规划问题，从而促进更大规模的宏观金融建模。通过规避传统价值函数迭代和时间迭代的速度-准确度权衡，它扩展了递归效用模型的可行计算前沿。 幂变换将 Epstein-Zin 欧拉方程转化为可由内生网格方法求逆的形式，得到无需求根的算法，在相同精度下比价值函数迭代快两到三个数量级。数值实验表明相较于标准价值函数迭代，速度提升达 10‑1000 倍，准确度提升超过 10 倍。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 内生网格方法（EGM）是克里斯·卡罗尔提出的一种数值技术，通过求逆欧拉方程来避免求根，用于求解动态规划问题。Epstein‑Zin 偏好是一种递归效用规范，它将风险厌恶与弹性 intertemporal 替代分离，广泛应用于宏观金融和资产定价。由于在 Epstein‑Zin 偏好下价值函数出现在欧拉方程内部，标准的 EGM 无法直接使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://julia.quantecon.org/dynamic_programming/egm_policy_iter.html">37. Optimal Growth III: The Endogenous Grid Method ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epstein-Zin_preferences">Epstein-Zin preferences</a></li>

</ul>
</details>

**标签**: `#endogenous grid method`, `#Epstein-Zin preferences`, `#dynamic programming`, `#computational economics`, `#algorithmic improvement`

---

<a id="item-18"></a>
## [城市聚集为 17 种增长制度，传播经济冲击](https://arxiv.org/abs/2603.16007) ⭐️ 8.0/10

研究人员利用卫星夜间灯光数据，构建了 1993 年至 2019 年跨 165 个国家的 8,808 个功能城市区域的 GDP 轨迹，通过聚类完整时间序列识别出 17 种不同且持续的增长制度。 研究表明，经济收敛发生在这些制度内部而非全球范围，冲击传播遵循结构相似性而非地理邻近，这改变了我们对城市不平等和政策效果的认识。 制度成员国解释了超越国家固定效应的国内增长方差的 16%；发达经济体倾向于输出冲击，而新兴经济体则吸收或放大冲击，且随着工业化成熟度提高，空间不平等下降，因为增长从领先城市扩散到整个城市系统。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 功能城市区（FUA）根据通勤区域捕捉城市的经济范围，而不仅仅是行政边界。夜间灯光卫星影像作为经济活动的代理，可在官方数据缺乏时估算 GDP。通过聚类完整时间序列，可根据相似的长期增长模式、波动性和冲击响应将城市分组。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Functional_Urban_Area">Functional urban area - Wikipedia</a></li>
<li><a href="https://www.earthdata.nasa.gov/topics/human-dimensions/nighttime-lights">Nighttime Lights - NASA Earthdata</a></li>
<li><a href="https://arxiv.org/abs/2603.16007">[2603.16007] Cities cluster into growth regimes that ...</a></li>

</ul>
</details>

**标签**: `#urban economics`, `#economic growth`, `#nighttime lights`, `#clustering analysis`, `#regional development`

---

<a id="item-19"></a>
## [基于物理信息的 VAE-神经 SDE 模型实现无套利收益率曲线预测](https://arxiv.org/abs/2605.12764) ⭐️ 8.0/10

本文提出两阶段框架：首先，学生 t 条件变分自编码器带动态水平注入（CVAEsT+LS）学习重尾期限结构流形；其次，潜在动态由严格受无套利偏微分方程（PDE）惩罚的神经随机微分方程（SDE）建模。该模型在美国、英国和日本国债收益率曲线上的实验表明，其平均期限 RMSE 达到 6.58 个基点，并消除了经典 HJM 模型在极端环境中出现的平行漂移和零下界违背。 通过将无套利偏微分方程约束嵌入深度生成模型中，该方法将神经网络的灵活性与固定收益建模的严格理论要求相结合，从而降低套利机会并提高投资者、监管者和风险管理者的预测可靠性。此外，该方法能够实现无监督的宏观经济 regime 检测和连续时间情景生成，为不同经济环境下的期限结构分析提供可扩展的工具。 模型采用带动态水平注入的学生 t 条件变分自编码器（CVAEsT+LS）来将宏观经济形状动态与绝对基准利率解耦，从而捕捉收益率曲线的重尾变化。潜在演化遵循一个神经随机微分方程（SDE），其损失函数包含源自 HJM 无套利偏微分方程（PDE）的惩罚项；实验结果表明，在美元、英镑和日元收益率曲线上平均期限 RMSE 达到 6.58 个基点，并且相空间向量场分析成功实现了宏观经济 regime 检测。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 收益率曲线描述了债券利率与到期时间的关系，其准确建模对定价、风险管理和货币政策至关重要。无套利条件在 Heath‑Jarrow‑Morton（HJM）框架中被形式化为一个偏微分方程（PDE），任何可接受的期限结构模型都必须满足该方程以避免无风险套利机会。变分自编码器（VAE）是一种生成式深度学习模型，能够学习数据的低维潜在表示；神经随机微分方程（SDE）则利用神经网络来参数化连续时间动态的漂移和扩散项。物理信息生成模型将深度学习的灵活性与以微分方程形式表达的物理定律相结合，确保生成的样本符合已知的理论约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12764">[2605.12764] Yield Curves Dynamics Using Variational ... Yield Curve Dynamics Using Variational Autoencoders Under No ... Yield Curves Dynamics Using Variational ... - EconPapers Physics-guided deep learning for crop yield estimation A physics-informed GAN framework based on model-free data ... Yashsethi24/Forecast_Treasury_Curve - GitHub Exploring Physics-Informed Neural Networks for Crop Yield ...</a></li>
<li><a href="https://sungchullee.github.io/financial_math_book_writing/ch24/deep_learning/neural_sde_models/">Neural Stochastic Differential Equation Models - Quant ...</a></li>
<li><a href="https://mlanthology.org/iclr/2024/kim2024iclr-3variational/">$t^3$-Variational Autoencoder: Learning Heavy-Tailed Data ...</a></li>

</ul>
</details>

**标签**: `#variational autoencoder`, `#yield curve modeling`, `#no-arbitrage`, `#neural SDE`, `#finance`

---

<a id="item-20"></a>
## [概率方法证明最优停止边界的连续可微性。](https://arxiv.org/abs/2405.16636) ⭐️ 8.0/10

作者首次提供了时间非齐次扩散过程中带有非光滑收益和折扣的时依赖最优停止边界连续可微性的概率证明，并将价值函数与斯蒂凡问题的解联系起来。 此结果将先前的正则性推广到更一般的情境，对随机控制、金融数学以及自由边界偏微分方程理论具有重要影响。 证明采用局部论证，能够处理有时空依赖的折扣率、有限或无限时间范围以及非光滑收益函数，并且作为副产品建立了最优停止价值函数与斯蒂凡问题之间的概率联系。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 最优停止问题涉及决定何时停止随机过程以最大化预期收益或最小化成本，这类问题与偏微分方程理论中的自由边界问题紧密相关。一维时间非齐次扩散是指其漂移率和波动率可以随时间变化的随机过程，能够灵活建模许多实际应用。斯蒂凡问题描述了相变界面（如冰‑水）的演化，是一种经典的自由边界问题，其解可以与某些最优停止任务的价值函数关联起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2405.16636">[2405.16636] A probabilistic approach to continuous ... 14 Optimal stopping – Stochastic Control and Decision Theory OPTIMAL STOPPING PROBLEMS FOR TIME-HOMOGENEOUS ... - Springer [2110.03831v1] The Stefan problem and free targets of optimal ... Threshold Stopping Rules for Diffusion Processes and Stefan’s ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Optimal_stopping">Optimal stopping - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0168202408702947">Chapter VII Problems of Optimal Stopping - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#optimal stopping`, `#stochastic processes`, `#free boundary problems`, `#probability theory`, `#PDE`

---

<a id="item-21"></a>
## [用于无界扩散过程的自适应分区强化学习及其遗憾界](https://arxiv.org/abs/2512.14991) ⭐️ 8.0/10

该论文提出了一种基于模型的强化学习算法，通过自适应分割受控扩散过程的联合状态‑动作空间，在每个分区内维持漂移、波动率和奖励的估计器，并在估计偏差超过统计置信度时细化分区。其遗憾界依赖于问题 horizon、状态维度、奖励增长阶以及新定义的 zooming dimension，并在诸如多资产均值‑方差组合选择等高维金融任务上进行了数值验证。 该工作首次为无界连续状态扩散过程的基于模型的强化学习提供了遗憾界分析，从而在金融、经济和运筹学中出现的问题上连接了理论与实践。其界限将有界域的先前结果作为特例恢复，因而将保证扩展到更广泛的随机控制问题类别。 算法在每个分区内保持独立的漂移、波动率和奖励估计器，当偏差超过置信阈值时触发细化，以平衡探索与近似。遗憾界表示为 O(√(H·d·ρ·ζ))，其中 H 为 horizon，d 为状态维度，ρ 为奖励增长阶，ζ 为 zooming dimension；在状态空间有界时退化为已知界。数值实验包括一个 10 资产均值‑方差组合选择问题，展示了可扩展性。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 受控扩散过程描述了由随机微分方程驱动的连续状态系统的演变，常用于金融中的资产价格建模。在此类环境中进行强化学习具有挑战性，因为状态空间是无限且高维的，导致传统的表格或函数近似方法效率低下。基于模型的强化学习会学习系统动态（漂移和波动率）和奖励函数的估计，以进行自适应规划或行动。自适应分区仅根据估计的统计置信度在需要的地方细化状态‑动作离散化，从而减轻维度灾难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.14991">[2512.14991] Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes</a></li>
<li><a href="https://arxiv.org/html/2512.14991v1">Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes</a></li>
<li><a href="https://thequant.space/flowcharts/adaptive-partitioning-and-learning-for-stochastic-control-of/">Adaptive Partitioning and Learning for Stochastic Control of ...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#stochastic control`, `#diffusion processes`, `#adaptive partitioning`, `#regret bounds`

---

<a id="item-22"></a>
## [基于布朗运动签名的随机过程通用逼近。](https://arxiv.org/abs/2512.16396) ⭐️ 8.0/10

作者证明，时间延伸布朗运动的签名上的线性泛函在 L^p 意义下对任何 p 可积的适应随机过程稠密，从而在粗糙路径空间上建立了 L^p 通用逼近定理。该结果发表在 arXiv:2512.16396v2。 这将通用逼近理论扩展到随机分析，表明基于签名的方法可以建模和学习一般的随机微分方程和分数布朗运动。它将粗糙路径理论与机器学习联系起来，对定量金融和路径依赖建模等领域产生影响。 证明构造了加权粗糙路径空间，并表明线性签名泛函在 L^p 范数下能够逼近任何适应过程，包括由布朗过滤驱动的 SDE 的解。该定理进一步适用于高斯过程，特别是分数布朗运动，通过验证所需的正则性条件。

rss · arXiv Quantitative Finance · Jul 7, 04:00

**背景**: 粗糙路径理论为由不规则信号（如分数布朗运动）驱动的微分方程提供了一个框架，其中路径的签名将其迭代积分编码为张量代数中的元素。期望签名的作用类似于随机变量的特征函数，捕捉路径的基本统计信息。签名的通用逼近结果表明，线性泛函可以在粗糙路径空间上稠密逼近连续泛函，这一性质现在已扩展到高斯过程的 L^p 设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rough_path">Rough path - Wikipedia</a></li>
<li><a href="https://projecteuclid.org/journals/annals-of-probability/volume-43/issue-5/Expected-signature-of-Brownian-motion-up-to-the-first-exit/10.1214/14-AOP949.pdf">Expected signature of Brownian motion up to the first exit ...</a></li>
<li><a href="https://arxiv.org/abs/2603.03058">[2603.03058] Universal approximation by signatures for ... Universal approximation by signatures for infinite ... Full article: Universal Approximation on Non-geometric Rough ... Notes on Signature and Rough Path Asma Khedher: Universal approximation by signatures for ... - KTH Universal Approximation on Non-geometric Rough Paths and ...</a></li>

</ul>
</details>

**标签**: `#rough paths`, `#signature methods`, `#universal approximation`, `#stochastic analysis`, `#fractional Brownian motion`

---

<a id="item-23"></a>
## [AI Premium](https://arxiv.org/abs/2606.30583) ⭐️ 8.0/10

The authors construct an AI factor from massive LLM token consumption data and show that firms with higher AI beta earn excess returns, revealing a substantial and heterogeneous AI premium.

rss · arXiv Quantitative Finance · Jul 7, 04:00

**标签**: `#AI economics`, `#factor investing`, `#machine learning`, `#finance`, `#token consumption`

---