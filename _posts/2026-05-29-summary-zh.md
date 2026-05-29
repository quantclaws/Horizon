---
layout: default
title: "Horizon Summary: 2026-05-29 (ZH)"
date: 2026-05-29
lang: zh
---

> From 36 items, 7 important content pieces were selected

---

1. [蓝色起源的 New Glenn 火箭在静态燃烧测试中爆炸](#item-1) ⭐️ 8.0/10
2. [GitHub 封禁发布零日 Windows 漏洞的安全研究者](#item-2) ⭐️ 8.0/10
3. [在 PostgreSQL 上构建持久化工作流](#item-3) ⭐️ 8.0/10
4. [PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management](#item-4) ⭐️ 8.0/10
5. [从知道到做做：LLM 交易代理的记忆控制基准](#item-5) ⭐️ 8.0/10
6. [Infinite-Dimensional LQ Mean Field Games with Common Noise: Small and Arbitrary Finite Time Horizons](#item-6) ⭐️ 8.0/10
7. [从准确性到可审计性：金融 AI 系统的确定性调查](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [蓝色起源的 New Glenn 火箭在静态燃烧测试中爆炸](https://twitter.com/nasaspaceflight/status/2060164928472854821) ⭐️ 8.0/10

蓝色起源的 New Glenn 火箭在佛罗里达州的静态燃烧测试中发生灾难性故障，导致基础设施严重受损并推迟了火箭的开发时间表。 此次爆炸对蓝色起源的发射计划是重大挫折，影响了 NASA 的阿尔忒弥斯月球登陆器计划，并凸显了大型甲烷燃料火箭所伴随的风险。 此次静态燃烧测试涉及一枚估计装载约 1000 吨液态甲烷的助推器，其热能释放相当于约 13 千吨 TNT 的热效应。

hackernews · enraged_camel · May 29, 01:16 · [社区讨论](https://news.ycombinator.com/item?id=48317774)

**背景**: New Glenn 是蓝色起源开发的两级部分可重复使用发射载具，于 2016 年宣布，直径七米。静态燃烧测试是在火箭保持固定的情况下点燃发动机，以验证推进系统和地面支持设备的准备情况。此类测试是标准做法，用于确保发射系统能够安全进入轨道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/New_Glenn">New Glenn - Wikipedia</a></li>
<li><a href="https://www.blueorigin.com/new-glenn">New Glenn | Blue Origin</a></li>
<li><a href="https://en.wikipedia.org/wiki/Static_fire_test">Static fire test</a></li>

</ul>
</details>

**社区讨论**: 评论者哀叹基础设施受损，预计修复需超过一年，同时有人指出测试的甲烷能量相当于约 13 千吨 TNT。还有人认为此事对美国航天影响有限，因为 SpaceX 仍占主导，但希望蓝色起源能从中吸取教训，以支持未来的雄心。

**标签**: `#Blue Origin`, `#New Glenn`, `#rocket explosion`, `#static fire test`, `#space launch`

---

<a id="item-2"></a>
## [GitHub 封禁发布零日 Windows 漏洞的安全研究者](https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation) ⭐️ 8.0/10

GitHub 封禁了一位在未公开披露的情况下发布 Windows 零日漏洞概念验证代码的安全研究者，引发了关于负责任披露和平台审核的讨论。 此事件凸显了平台禁止发布漏洞代码的政策与安全社区依赖负责任披露来提升软件安全之间的冲突，可能影响漏洞赏金激励以及研究者与厂商的关系。 该研究者的帖子包含了 Windows 零日漏洞的利用概念验证代码；GitHub 的封禁据称是在微软施压后进行，评论者猜测可能涉及个人动机且未获得补偿。

hackernews · possibilistic · May 28, 21:45 · [社区讨论](https://news.ycombinator.com/item?id=48315968)

**背景**: 零日漏洞指的是在补丁发布前未被公开知晓的安全缺陷，攻击者可利用它进行攻击，通常会以概念验证代码形式公开以展示风险。负责任披露（亦称协调漏洞披露）鼓励研究者在向厂商私下报告漏洞后再公开，以便厂商有时间修补。漏洞赏金计划为负责任报告漏洞的研究者提供奖励，提供与协调披露一致的财务激励。GitHub 等代码托管平台需要在开放性与禁止发布有害利用代码的政策之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cyderes.com/howler-cell/windows-zero-day-bluehammer">BlueHammer: Inside the Windows Zero-Day</a></li>
<li><a href="https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-program">Coordinated Vulnerability Disclosure Program - CISA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bug_bounty_program">Bug bounty program - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对封禁表示困惑，猜测微软可能会后悔此举，质疑是否有任何公开声明，认为研究者可能怀有个人恩怨，并讨论平台是否现在对托管的利用代码承担编辑责任。

**标签**: `#cybersecurity`, `#zero-day exploits`, `#GitHub`, `#responsible disclosure`, `#bug bounty`

---

<a id="item-3"></a>
## [在 PostgreSQL 上构建持久化工作流](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

该博客文章探讨了将 PostgreSQL 作为持久化工作流引擎的核心存储和协调层，并对比了 absurd、Restate.dev、Cloudflare 工作流、Temporal 和 DBOS 等实现。 这表明传统关系数据库能够提供可靠、基于事务的执行来处理复杂工作流，从而减少对外部编排器的依赖并降低运营开销。 讨论中提到了具体系统——Armin Ronacher 的 absurd、用于自托管支付集成的 Restate.dev、用于廉价报告生成的 Cloudflare 工作流、将原子消息与 PostgreSQL 事务绑定的 DBOS，以及存在载荷大小限制的 Temporal。

hackernews · KraftyOne · May 28, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48313530)

**背景**: 持久化工作流引擎会保存执行状态，以便工作流在崩溃后能够从中断点准确恢复。PostgreSQL 提供强大的 ACID 事务、逻辑复制和变更数据捕获功能，使其非常适合存储工作流状态并协调各步骤。诸如 pg‑workflows 和 DBOS 之类的项目利用这些特性直接在 PostgreSQL 之上构建轻量级编排器，从而避免使用外部队列或专用状态存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dbos.dev/blog/why-postgres-durable-execution">Why Postgres is a Good Choice for Durable Workflow Execution | DBOS</a></li>
<li><a href="https://sokratisvidros.github.io/pg-workflows/">pg-workflows | The simplest Postgres workflow engine for TypeScript ...</a></li>
<li><a href="https://supabase.com/blog/durable-workflows-in-postgres-dbos">Running Durable Workflows in Postgres using DBOS</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Armin Ronacher 的 absurd 是一个基于 PostgreSQL 的工作流示例，讨论了受 Spanner 变更流启发的模式，分享了个人使用经验，比较了 Restate.dev、Cloudflare 工作流和 DBOS 在可靠性和成本方面的不同用途，并提出了关于 DBOS 与 Temporal 的疑问，特别是关于载荷限制和实际使用体验。

**标签**: `#PostgreSQL`, `#durable workflows`, `#workflow engines`, `#distributed systems`, `#DBOS`

---

<a id="item-4"></a>
## [PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management](https://arxiv.org/abs/2605.27887) ⭐️ 8.0/10

PortBench proposes a correlation-aware, full-pipeline benchmark for evaluating LLMs in portfolio management, combining static QA and dynamic allocation tasks.

rss · arXiv Quantitative Finance · May 28, 04:00

**标签**: `#LLM`, `#portfolio management`, `#benchmark`, `#finance`, `#AI`

---

<a id="item-5"></a>
## [从知道到做做：LLM 交易代理的记忆控制基准](https://arxiv.org/abs/2605.28359) ⭐️ 8.0/10

论文提出 KTD‑Fin，一种通过屏蔽历史标识符和日历信息来防止 LLM 记忆并采用 Barra 风格归因框架隔离股票选择 alpha 与市场 beta 的记忆控制基准。 通过将真实投资技能与被动市场曝露分离，KTD‑Fin 为评估 LLM 交易代理提供了更纯净的信号，引导研究者朝着更注重技能的模型开发方向前进。 KTD‑Fin 通过数据端屏蔽协议匿名化股票代码、日期和价格，随后采用 Barra 风格模型将收益分解为市场、风格和股票选择三部分；在 2024‑2026 年中国 CSI300 指数上对十种前沿 LLM 代理的测试表明，大部分收益可由市场和风格因素解释，持续的股票选择 alpha 有限。

rss · arXiv Quantitative Finance · May 28, 04:00

**背景**: 大型语言模型代理正越来越多地在端到端交易模拟中进行测试，它们基于历史市场数据进行买卖决策，并以投资组合回报作为性能指标。然而，这种回测可能受到记忆偏差的影响，因为模型在预训练期间可能已经见过相同的股票代码、日期或新闻，且原始回报会将技能与市场贝塔或风格曝露混淆。Barra 风格的归因框架能够将收益分解为市场、风格和股票选择（alpha）三部分，从而隔离真正的投资技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.28359">From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alpha_(finance)">Alpha (finance) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#trading benchmark`, `#financial AI`, `#evaluation methodology`, `#KTD-Fin`

---

<a id="item-6"></a>
## [Infinite-Dimensional LQ Mean Field Games with Common Noise: Small and Arbitrary Finite Time Horizons](https://arxiv.org/abs/2601.13493) ⭐️ 8.0/10

The work establishes well-posedness and epsilon-Nash properties for linear-quadratic mean field games in Hilbert spaces influenced by infinite-dimensional common noise across all time horizons.

rss · arXiv Quantitative Finance · May 28, 04:00

**标签**: `#mean field games`, `#stochastic control`, `#infinite-dimensional systems`, `#linear-quadratic`, `#common noise`

---

<a id="item-7"></a>
## [从准确性到可审计性：金融 AI 系统的确定性调查](https://arxiv.org/abs/2605.23955) ⭐️ 8.0/10

本文调研了表格模型、图神经网络和基于 LLM 的代理工作流在金融 AI 中的非确定性来源，量化了信用评分中的解释排名不稳定、基于 GNN 的欺诈检测中的预测翻转率以及 LLM 实体抽取中的张量并行导致的输出偏差。提出了一种将模态特定指标与审计准备度联系起来的分层评估框架。 在信用风险、欺诈检测和反洗钱等受监管的金融应用中，可重复性和可审计性至关重要；本调研为满足合规要求提供了可操作的见解。它帮助研究人员和从业者识别并缓解跨主导 AI 模态的确定性问题。 研究考察了三种模态：表格模型（事后解释方差）、图网络（随机采样和时间异步）以及基于 LLM 的代理工作流（批次依赖的偏差和轨迹漂移）。实验测量了解释排名不稳定性（RBO）、预测翻转率（D_cos）以及张量并行导致的输出偏差（TDI、PSD），并将这些指标与分层审计准备框架相关联。

rss · arXiv Quantitative Finance · May 28, 04:00

**背景**: 机器学习的确定性指在相同输入和模型状态下产生相同输出，这是金融监管中审计能力的基础。非确定性的来源包括硬件层面的变化、诸如图神经网络中随机采样之类的随机算法，以及 LLM 服务中的批次层面效应（例如 KV 缓存重用）。表格模型经常依赖事后解释方法，其排名可能会变化；图神经网络受采样随机性和时间错位的影响；LLM 工作流在并行处理相似批次时会出现偏差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post_hoc_analysis">Post hoc analysis - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2508.00267">Neighbor-Sampling Based Momentum Stochastic Methods for Training Graph ...</a></li>
<li><a href="https://arxiv.org/html/2509.02121v2">Batch Query Processing and Optimization for Agentic Workflows</a></li>

</ul>
</details>

**标签**: `#AI reproducibility`, `#financial AI`, `#determinism`, `#auditability`, `#machine learning`

---