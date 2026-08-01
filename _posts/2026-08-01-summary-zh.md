---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> From 63 items, 21 important content pieces were selected

---

1. [无状态 MCP 2.0 发布引发新兴趣并激发新工具](#item-1) ⭐️ 9.0/10
2. [AI 语音代理在大规模实地实验中提升录用率和留存率](#item-2) ⭐️ 9.0/10
3. [黑客新闻帖子将电梯调度算法与磁盘调度和游戏联系起来](#item-3) ⭐️ 8.0/10
4. [介绍 qm：面向协同工作的多智能体代理套件](#item-4) ⭐️ 8.0/10
5. [Tailscale 解释可重用认证密钥泄露导致 Hugging Face 入侵](#item-5) ⭐️ 8.0/10
6. [Go 提议在 container/ 包中添加泛型 Set 和 Heap 类型](#item-6) ⭐️ 8.0/10
7. [在 5‑10 GB 内存中运行十亿边图算法使用 DataFusion](#item-7) ⭐️ 8.0/10
8. [DeepSeek 发布 304B 参数 V4‑Flash 模型。](#item-8) ⭐️ 8.0/10
9. [Simon Willison 在 Oxide and Friends 播客中讨论开放权重 AI 革命](#item-9) ⭐️ 8.0/10
10. [幸运还是实力？结果噪声、有效样本量与技能归因](#item-10) ⭐️ 8.0/10
11. [企业社会立场通过一致消费者支出提升收入。](#item-11) ⭐️ 8.0/10
12. [AI 谄媚与决策](#item-12) ⭐️ 8.0/10
13. [新空间 Econ-SIR 模型将经济与流行病动态联系起来](#item-13) ⭐️ 8.0/10
14. [基于 LLM 的多智能体注意力增强模型预测碳强度以实现低碳调度](#item-14) ⭐️ 8.0/10
15. [FinSMART：市场对齐强化学习框架用于金融情感分析](#item-15) ⭐️ 8.0/10
16. [LLM 驱动的 PACE 框架提升深交所父母订单执行](#item-16) ⭐️ 8.0/10
17. [自动做市商中的最优动态费用](#item-17) ⭐️ 8.0/10
18. [女性担忧，男性采用？生成式 AI 采用中的性别风险感知](#item-18) ⭐️ 8.0/10
19. [研究表明无关文本使 LLM 在研究生经济考试中的正确率下降约 12 个百分点](#item-19) ⭐️ 8.0/10
20. [连续时间强化学习框架用于多 regime 最优切换并采用熵正则化](#item-20) ⭐️ 8.0/10
21. [研究发现以太坊日内 gas 费峰值与套利活动相关，企业调度响应呈异质性](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [无状态 MCP 2.0 发布引发新兴趣并激发新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

Simon Willison 讨论了 Stateless MCP 日以及 2026-07-28 发布的 MCP 2.0 规范，该规范将协议简化为单个 HTTP 请求，激发了他开发 mcp-explorer 和 datasette-mcp 项目。 无状态设计降低了实现复杂度和服务器端状态需求，使 MCP 更具可扩展性，即使是运行在笔记本上的小模型也能使用，从而重新点燃了人们对 LLM 工具集成标准的兴趣。 无状态 MCP 用单个 POST 请求取代了先初始化再调用工具的两步状态流，请求中包含 MCP‑Protocol‑Version、Mcp‑Method 和 Mcp‑Name 头，不再需要跟踪 Mcp‑Session‑Id。Simon 构建了 mcp‑explorer（用于探测 MCP 服务器的 CLI）和 datasette‑mcp 来展示新工作流。

rss · Simon Willison · Jul 31, 23:13

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在让基于 LLM 的代理通过统一接口调用外部工具。2025 年初兴趣激增后，由于 Anthropic 的 Skills 展示了带有 curl 的 shell 可以实现类似灵活性，关注度有所下降。2026 年 7 月 28 日发布的无状态 MCP 2.0 规范通过移除会话状态来简化协议，提高了可扩展性和实现的简便性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>

</ul>
</details>

**标签**: `#Model Context Protocol`, `#MCP 2.0`, `#LLM agents`, `#Anthropic`, `#Stateless MCP`

---

<a id="item-2"></a>
## [AI 语音代理在大规模实地实验中提升录用率和留存率](https://arxiv.org/abs/2607.28222) ⭐️ 9.0/10

在一项大规模自然实地实验中，70,000 名求职者被随机分配给人类招聘者或 AI 语音代理进行面试，接受 AI 面试的求职者获得录用 offer 的概率高出 12%。这些求职者还表现出更高的入职率和更好的留存率，而被录用员工的生产力没有下降。 结果表明，利用 AI 自动化信息收集可以降低方差并提高招聘决策质量，提供一种可扩展的方式使招聘更公平更有效。这对寻求更好人才匹配的雇主以及希望面临较少偏见筛选的求职者都有重要影响。 AI 语音代理进行了更结构化且一致的面试，同时仍能根据个别求职者做出响应，这与收集到更多与招聘相关的信息相关。人类招聘者仍然评估面试并做出最终录用决定，而被录用员工的生产力未出现下降。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 结构化面试通过标准化问题和评估标准，已被证明能够降低偏见并提高招聘决策的可靠性。自然实地实验让研究者能够在真实的组织环境中操纵自变量（如面试者类型），以观察因果效应。AI 语音代理利用自然语言处理技术，为大量求职者提供既一致又能适应个体差异的面试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recruiter.daily.dev/resources/technical-interview-best-practices-reducing-bias-improving-signal/">Technical Interview Best Practices: Reducing Bias and...</a></li>
<li><a href="https://cards.algoreducation.com/en/content/sU9ajQ5z/natural-experiments-psychology">Natural Experiments in Psychological Research | Algor Cards</a></li>
<li><a href="https://www.talkpush.com/voice-ai">Voice AI | Talkpush</a></li>

</ul>
</details>

**标签**: `#AI hiring`, `#field experiment`, `#voice agents`, `#recruitment`, `#decision making`

---

<a id="item-3"></a>
## [黑客新闻帖子将电梯调度算法与磁盘调度和游戏联系起来](https://john.fun/elevators) ⭐️ 8.0/10

一篇关于电梯调度算法的黑客新闻帖子引发了广泛讨论，将其与磁盘调度算法、目的地调度电梯系统和交互式模拟游戏联系起来。 该讨论凸显了经典计算机科学概念（如电梯 SCAN 算法）在不同领域的适用性，提供了教育价值，并为优化存储 I/O 和建筑人流等实际系统提供了见解。 评论者指出电梯 SCAN 算法与磁盘 SCAN 算法的相似性，分享了在建筑中使用目的地调度系统的经验，并提到了模拟电梯控制的游戏，如 Elevator Saga 和 Sky Lobby。

hackernews · Jrh0203 · Jul 31, 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49124218)

**背景**: 电梯算法（也称为 SCAN）通过在一个方向上移动磁盘臂直到尽头然后反转来服务请求，这就像电梯服务楼层一样。磁盘调度算法对 I/O 请求进行排序以最小化寻道时间并提高吞吐量。目的地调度系统根据乘客目的地将其分组，以减少多电梯建筑中的等待和旅行时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elevator_algorithm">Elevator algorithm - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/operating-systems/disk-scheduling-algorithms/">Disk Scheduling Algorithms - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Destination_dispatch">Destination dispatch - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者回忆起在学校实现电梯模拟的经历，根据实际交通模式讨论目的地调度的有效性，分享了电梯控制游戏如 Elevator Saga 和 Sky Lobby 的链接，并指出用户常见的错误，如同时按下上下按钮。

**标签**: `#elevator algorithms`, `#disk scheduling`, `#destination dispatch`, `#CS education`, `#simulation`

---

<a id="item-4"></a>
## [介绍 qm：面向协同工作的多智能体代理套件](https://github.com/yc-software/qm) ⭐️ 8.0/10

qm 是 YC 软件发布的开源多智能体代理套件，让每位员工或项目都能拥有独立作用域的 AI 代理，并通过 Slack 和网页共享协作空间来处理仓库管理、邮件分类和内部应用构建等任务。 通过解决多智能体部署中的作用域和协作难题，qm 为团队提供了一种安全并行运行众多 AI 代理的实用方案，有望提升生产力并降低 AI 增强型工作场所的管理开销。 该系统提供每个人的作用域，限制每个代理仅能访问其所需的工具和资源；共享房间让代理可以交换消息并协作。它与 Slack 和网页界面集成，支持任意语言模型，并基于 YC 内部运行超过 50 个代理的经验。

hackernews · tosh · Jul 31, 18:04 · [社区讨论](https://news.ycombinator.com/item?id=49126604)

**背景**: 多智能体系统常常在权限管理和协调上面临挑战，这会带来安全风险和重复劳动。已出现诸如 scoped credentials 和 per‑agent 访问控制等方法来实施最小权限原则，而共享工作空间则旨在让代理在共同任务上协作。虽然已有 Claude Cowork 和 OpenClaw 等产品提供代理框架，但很少将细粒度的 per‑person 作用域与持久的共享房间结合用于工作场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/yc-software/qm">GitHub - yc-software/qm: Multiplayer agent harness for work</a></li>
<li><a href="https://qm.ycombinator.com/index.html">QM — Open-Source Agent Harness from YC</a></li>
<li><a href="https://www.arthur.ai/column/access-management-ai-agents-scope-permissions">Access Management for AI Agents: Scope What They Touch | Arthur</a></li>

</ul>
</details>

**社区讨论**: 评论者们反应幽默且好奇，指出代理能自主安排会议（luciana1u），质疑 qm 与现有工具如 Claude Cowork 有何不同（recsv‑heredoc），称赞其作用域和共享房间设计是公司级助手的现实方案（knighthacker），提及相关项目如 Gary Tan 的 gstack 和 AQ（mellosouls、knighthacker），并询问开源替代方案 Hermes 以及 OpenClaw 类系统的实际使用情况（yewenjie）。总体情绪是积极的兴趣，同时伴随着对比较细节的需求。

**标签**: `#multi-agent systems`, `#AI agents`, `#developer tools`, `#Y Combinator`, `#collaboration`

---

<a id="item-5"></a>
## [Tailscale 解释可重用认证密钥泄露导致 Hugging Face 入侵](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 8.0/10

Tailscale 的博客文章透露，Hugging Face 的 CI 环境中意外泄露的可重用认证密钥被攻击者利用，在数天内将 181 个恶意节点加入到他们的 tailnet。 此事件凸显了长期有效、可重用凭证的危险，表明即便是受信任的网状 VPN 工具也可能因密钥管理不善被滥用，影响所有使用类似访问密钥的组织。 攻击者利用泄露的密钥创建了 181 个 CI 节点，每个节点获得的 Tailscale 身份标签授予与合法 CI 节点相同的广泛访问权限；Tailscale 确认其产品本身没有漏洞，仅是密钥被误用，并建议轮换密钥、使用短期令牌以及通过标签或节点审批限制 auth‑key 使用。

hackernews · bluehatbrit · Jul 31, 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49127306)

**背景**: tailnet 是 Tailscale 为用户设备创建的私有虚拟网络，用于实现安全的网状连接。可重用认证密钥是一种长期有效的令牌，可用于向 tailnet 添加新节点，但若泄露则允许任何人添加任意机器。Hugging Face 的 CI/CD 流程常将诸如 API 密钥之类的密钥注入环境变量，若以明文形式存储则容易泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/docs/concepts/tailnet">What is a tailnet ? · Tailscale Docs</a></li>
<li><a href="https://tailscale.com/docs/features/access-control/auth-keys">Auth keys · Tailscale Docs</a></li>
<li><a href="https://www.gitguardian.com/remediation/hugging-face-user-access-token">Remediating Hugging Face user access token leaks | GitGuardian</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Tailscale 本身没有漏洞，批评可重用密钥的做法就像把钥匙留在门口，称赞公司的透明度，并建议增加自动安全检查或使用短期凭证等功能以防止类似事件。

**标签**: `#security`, `#Tailscale`, `#Hugging Face`, `#intrusion analysis`, `#CI/CD`

---

<a id="item-6"></a>
## [Go 提议在 container/ 包中添加泛型 Set 和 Heap 类型](https://github.com/golang/go/issues/80590) ⭐️ 8.0/10

Go 问题 #80590 提议在标准库的 container/ 包中添加泛型集合类型，如 Set 和 Heap，最初作为非导出的抽象类型以记录约定。 这填补了 Go 标准库长期存在的空白，为开发者提供了现成的、类型安全的数据结构，减少了对临时实现的依赖。 所提出的 Set 和 Heap 类型目前是非导出的，仅用作文档；未来可能在积累经验后导出，用户可以定义最小的约束类型来使用它们，如示例中的泛型 Take 函数所示。

hackernews · jabits · Jul 31, 18:39 · [社区讨论](https://news.ycombinator.com/item?id=49127031)

**背景**: Go 在 1.18 版本中引入了泛型（type parameters），使得可重用的数据结构成为可能。container/ 包已经提供了堆接口，但没有标准的 Set 类型，开发者通常用 map[T]struct{} 来模拟集合。该提案旨在将泛型 Set 和 Heap 类型纳入标准库，以提供一致且类型安全的实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/golang/go/issues/80590">proposal: container/...: generic collection types · Issue #80590 · golang/go</a></li>
<li><a href="https://www.dolthub.com/blog/2024-07-01-golang-generic-collections/">Writing generic collection types in Go: the missing documentation | DoltHub Blog</a></li>
<li><a href="https://stackoverflow.com/questions/34018908/golang-why-dont-we-have-a-set-datastructure">data structures - Golang why don't we have a set ... - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎此提案，认为这是迟到的功能，有“better late than never”等赞誉，终于能得到 Set 和 Heap 类型。也有人担心 API 中混合了变异方法，质疑以这种方式加入泛型是否合适，希望未来的 Go v2 能从根本上解决问题。总体情绪积极，伴随着建设性的批评。

**标签**: `#Go`, `#generics`, `#standard library`, `#data structures`, `#language proposal`

---

<a id="item-7"></a>
## [在 5‑10 GB 内存中运行十亿边图算法使用 DataFusion](https://semyonsinchenko.github.io/ssinchenko/post/datafusion-graphs-cc-2/) ⭐️ 8.0/10

作者展示了 DataFusion 能够在仅使用 5 GB 内存的情况下计算出十亿边有向图的 PageRank，并在使用 10 GB 内存的情况下检测出两百亿边图的弱连通分量，性能优于传统的内存图库如 NetworkX 和 Igraph。 这表明大规模图分析可以在普通硬件上完成，减少对 Spark 等重量级分布式框架的依赖，使图处理能够在笔记本、边缘设备和成本敏感的环境中进行。 该实现利用 Apache Arrow 的列式内存格式和 DataFusion 可扩展的查询引擎来执行外核图算法，使用了 Graphalytics 基准中的 Graph500‑26 和 Twitter_MPI 数据集。

hackernews · speckx · Jul 31, 15:53 · [社区讨论](https://news.ycombinator.com/item?id=49124658)

**背景**: Apache DataFusion 是一个基于 Rust 的可嵌入查询引擎，使用 Apache Arrow 的列式内存模型进行快速分析。Apache Arrow 提供了一种与语言无关的列式格式，使得大数据集在 CPU 和 GPU 上的处理更加高效。外核处理允许算法在内存不足时通过分块从磁盘读取数据进行计算，这一技术在数据库中常见，但在图算法中较少应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/apache/datafusion">apache/ datafusion | DeepWiki</a></li>
<li><a href="https://arrow.apache.org/docs/format/Columnar.html">Arrow Columnar Format — Apache Arrow v25.0.0</a></li>
<li><a href="https://subscription.packtpub.com/book/programming/9781838554491/16/ch16lvl1sec95/out-of-core-distributed-graph-processing">Out - of - core distributed graph processing | Hands-On Software...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 DataFusion 的强大和可扩展性，认为其能够支持自定义查询语言。一些人提到了相关的先前工作，如 GraphChi 和 Icebug/LadybugDB 项目，它们同样基于 Arrow 实现外核图处理。还有一位新手寻求关于学习图算法和知识图谱以进行大数据挖掘的指导。

**标签**: `#DataFusion`, `#graph algorithms`, `#out-of-core processing`, `#Apache Arrow`, `#big data`

---

<a id="item-8"></a>
## [DeepSeek 发布 304B 参数 V4‑Flash 模型。](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek‑AI 发布了 DeepSeek‑V4‑Flash‑0731，这是一个参数量为 3040 亿、在 Hugging Face 上占用 167 GB 的语言模型，具备显著增强的代理能力。其输入 token 价格为 0.14 美元/百万，输出 token 价格为 0.27 美元/百万，在 Artificial Analysis 智能指数上的得分超过更大的 MiniMax M3 模型。 该模型表明，参数规模更小也能实现更高的智能‑每‑美元性能，使其成为对成本敏感的 AI 应用的有力选择。其具有竞争力的定价以及在智能‑vs‑成本图表上的优异表现预示着行业正朝着更高效的大型语言模型发展。 该模型拥有 3040 亿参数，存储占用约 167 GB；在默认推理级别下它只能画出粗糙的鹈鹕草图，而将 reasoning_effort 设置为 high 时则能生成鹈鹕骑自行车的详细插画。在 Artificial Analysis 上，其智能得分约为 50，每任务成本仅 0.028 美元，位于帕累托线左侧，性价比优于同等智能但成本高出十倍的模型。

rss · Simon Willison · Jul 31, 23:59

**背景**: 代理能力是指语言模型能够像自主代理一样，通过使用工具和反馈来完成纯文本生成以外的任务。Artificial Analysis 智能指数将多个基准测试（如 GPQA、人类最后考试）汇总为一个分数，以反映模型的整体智能水平。每百万 token 的成本是比较运行 LLMs 价格的标准指标，数值越低表示经济效益越高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/developing-agentic-capabilities-llms-automate-business-workflows-mp1tf">Developing Agentic Capabilities for LLMs to automate business...</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://groq.com/pricing">Groq On-Demand Pricing for Tokens -as-a-Service | Groq is fast, low...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#DeepSeek`, `#AI models`, `#agentic capabilities`, `#cost efficiency`

---

<a id="item-9"></a>
## [Simon Willison 在 Oxide and Friends 播客中讨论开放权重 AI 革命](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 8.0/10

2026 年 7 月 31 日，Simon Willison 加入 Bryan Cantrill 和 Adam Leventhal 参加 Oxide and Friends 播客，讨论开放权重 AI 模型的快速进展，包括 Kimi K3 与专有模型相当的表现、最近的网络安全事件以及公开的开放权重倡议书。 此次讨论凸显开放权重模型正在缩小与专有前沿系统之间的差距，正在影响 AI 政策辩论和行业倡导。 播客提到 Kimi K3 拥有 2.8 万亿参数的开放权重模型，DeepSeek V4 Flash 0731 为稀疏混合专家模型（激活 13B 占总 284B），并指出 Anthropic 最近发生尴尬的网络安全事件，同时提到开放权重倡议书已获多数主要 AI 公司签署，唯 Anthropic 未参与。

rss · Simon Willison · Jul 31, 21:33

**背景**: 开放权重 AI 模型在特定条款下发布模型的权重参数，使研究者能够检查、微调和部署模型而无需完整源代码。与完全开源的 AI 不同，开放权重发布可能对修改或再分发施加限制，但仍提供显著的透明度和可访问性。最近的发布如 Kimi K3（2.8 万亿参数）和 DeepSeek V4 Flash 0731 表明开放权重模型可以在性能上与专有前沿模型竞争，从而促使政策倡议书主张开放权重以维持美国的 AI 领导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weight models`, `#LLM`, `#podcast`, `#AI policy`

---

<a id="item-10"></a>
## [幸运还是实力？结果噪声、有效样本量与技能归因](https://arxiv.org/abs/2607.27544) ⭐️ 8.0/10

该文提出了一种两参数框架——结果噪声和有效样本量——用于判断结果记录何时能可靠地反映技能，表明许多高风险领域缺乏足够的信号来进行个体层面的推断。 通过澄清何时运气主导结果，该框架有助于投资者、董事会和政策制定者在金融、风险资本和高管薪酬中避免错误归因技能，从而改进评估实践。 该模型将每个结果视为底层技能的噪声观测，包含噪声水平和有效独立结果数量两个参数；共同基金管理和风险投资等领域位于信号过弱的区域，因而需要借鉴医学中的人群层面验证方法。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 结果噪声指的是掩盖每次观测结果中真实技能信号的随机变化，而有效样本量则衡量在一定观察窗口内可获得的独立观测数量。决策理论研究在不确定性下如何做选择，常依赖信噪比的考量。在医学领域，当个体数据过于嘈杂无法直接推断技能时，会采用人群层面的经验验证方法，例如检查从业者是否遵循与更好结果相关的证据实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openbizindex.com/topics/skill-attribution-bias">Skill attribution bias at Work | OpenBizIndex</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decision_theory">Decision theory - Wikipedia</a></li>
<li><a href="https://www.verywellhealth.com/using-validation-therapy-for-people-with-dementia-98683">verywellhealth.com/using- validation -therapy-for-people-with-dementia...</a></li>

</ul>
</details>

**标签**: `#decision theory`, `#skill attribution`, `#outcome noise`, `#performance evaluation`, `#economics`

---

<a id="item-11"></a>
## [企业社会立场通过一致消费者支出提升收入。](https://arxiv.org/abs/2607.27569) ⭐️ 8.0/10

该研究使用支付卡交易数据发现，企业公开发表社会立场后，收入平均增加，最认同立场的消费者在事件后一个月内提升消费约 19%，而最反对的消费者则削减消费约 12%。这些分歧的消费反应随时间减弱，但即使一年后仍可检测到。 结果表明，消费者的支出会对企业的社会行动产生有意义的反应，为企业参与社会问题提供了利润动机。这为经济学、营销和公司战略提供了关于公开立场在争议话题上财务回报的参考。 研究人员通过交易模式预测持卡人的社会立场，并在广为人知的立场事件周围测量消费变化。分析显示存在显著异质性，尽管效应随时间减弱，但在十二个月后仍具有统计显著性。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 企业社会责任（CSR）指的是企业在法律义务之外自愿采取的应对社会和环境问题的行动。支付卡交易数据提供了高频、大规模的实际消费支出代理，能够精确测量行为反应。先前的研究多使用调查或社交媒体来衡量消费者反应，而本研究则利用实际购买记录来量化企业社会立场的财务影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Corporate_social_responsibility">Corporate social responsibility - Wikipedia</a></li>
<li><a href="https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers">Credit Card customers | Kaggle</a></li>
<li><a href="https://nielseniq.com/">NIQ - The Full View™ of Consumer Intelligence</a></li>

</ul>
</details>

**标签**: `#consumer behavior`, `#corporate social responsibility`, `#empirical economics`, `#payment transaction analysis`, `#social activism`

---

<a id="item-12"></a>
## [AI 谄媚与决策](https://arxiv.org/abs/2607.28133) ⭐️ 8.0/10

一项涉及 1,500 名参与者、覆盖 30 种决策环境的研究发现，尽管 AI 建议具有谄媚倾向，但总体上会使人类选择去极化，使其远离初始倾向；更高的谄媚程度会削弱这一去极化效应。 该研究挑战了 AI 谄媚会加剧两极化的假设，表明信息丰富的 AI 建议能够抵消偏见，并为 AI 对齐及人机交互的更安全设计提供参考。 谄媚通过大语言模型倾向于提供支持用户初始观点的考量并使用赞美语言来衡量；去极化在道德、非道德、客观、主观、战略、非战略、简单和复杂任务中均出现；谄媚程度增加会削弱去极化效应，而基线谄媚水平与当前领先模型相当且未随时间上升。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 大型语言模型的谄媚是指模型倾向于生成迎合用户预期偏好的回应，通常通过赞美或顺从的语言来衡量。去极化是指建议使个体远离极端或两极化的立场，趋向更为中庸的选择。在实验经济学中，决策环境涵盖从道德判断到策略博弈的各种任务，使研究者能够考察建议在不同领域对行为的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.28133">AI Sycophancy and Decisions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sycophancy_(artificial_intelligence)">Sycophancy (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI alignment`, `#sycophancy`, `#decision making`, `#human-AI interaction`, `#experimental economics`

---

<a id="item-13"></a>
## [新空间 Econ-SIR 模型将经济与流行病动态联系起来](https://arxiv.org/abs/2607.28348) ⭐️ 8.0/10

本文构建并估计了一个空间微观基础的 Econ-SIR 模型，同步捕捉经济变量与疫情传播，并基于美国县级每日健康、流动性、就业及非药物干预数据进行实证。结果表明，只有在疫苗两年内可用时，封锁才能改善结果；而戴口罩等减毒传播的措施既能降低病毒传播又能提升经济活动。 通过将经济行为与流行病动态相结合，该模型为政策制定者在权衡封锁与疫苗时间表时提供了具体指导，强调在疫苗尚未 imminent 时严格非药物干预的有限价值。其空间化、高频方法推动了跨学科流行病学研究，并可为未来的大流行准备提供参考。 该模型预测在无干预情况下病例会先呈指数增长，随后进入病例水平基本持续且经济活动下降的长期平台期；只有在疫苗预计两年内到来时，封锁才能显著改善结果，而戴口罩等降低传播的措施既能减少病毒传播又能提升经济产出。估计使用了新颖的美国县级每日健康、流动性、就业及非药物干预数据集。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 传统的 SIR 模型将人群划分为易感、感染和康复三个 compartment，仅描述疾病传播而不考虑影响接触率的经济决策。Econ‑SIR 模型在此基础上引入了根据感染风险和政府政策（如封锁或口罩令）调整行为的最优化代理人。通过将模型空间化并利用美国县级的高频数据进行估计，作者能够捕捉到流动性、就业和健康结果的局部差异。该框架评估了一位旨在最大化社会福利的功利主义政策制定者，并将其与没有任何干预的 laissez‑faire 均衡进行比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.28348v1">Economics and Epidemics: Evidence from an Estimated Spatial Econ-SIR ...</a></li>
<li><a href="https://www.federalreserve.gov/econres/feds/files/2020091pap.pdf">Economics and Epidemics: Evidence from an Estimated Spatial...</a></li>
<li><a href="https://docs.iza.org/dp13797.pdf">Economics and Epidemics: Evidence from an Estimated Spatial ...</a></li>

</ul>
</details>

**标签**: `#epidemiology`, `#economics`, `#COVID-19`, `#policy analysis`, `#spatial modeling`

---

<a id="item-14"></a>
## [基于 LLM 的多智能体注意力增强模型预测碳强度以实现低碳调度](https://arxiv.org/abs/2607.26560) ⭐️ 8.0/10

本文提出一种主动的前瞻性空间-时间碳响应框架，采用深度学习模型并融合双阶段注意力机制和 LLM 驱动的多智能体合作，以预测次日节点碳强度并整合地理可调度负荷，实现低碳电力调度。 该框架在修改后的 IEEE 33 节点系统上实现了调度延迟减少一小时时超过 30%的排放削减，提供了一种主动的碳管理方法，有助于电力系统脱碳和可持续生产目标。 框架采用分层深度学习设计，包含双阶段注意力和基于大语言模型的多智能体合作系统，并将移动储能系统和分布式数据中心作为地理可调度负荷；仿真表明在减少一小时调度延迟的情况下可实现超过 30%的减排。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 节点碳强度（NCI）是指电网中特定节点处的单位电力所对应的碳排放强度，常用于碳感知的优化调度。双阶段注意力机制通过两步逐步细化特征选择，能够有效抑制噪声并提升时间序列预测性能。地理可调度负荷（如移动储能系统和分布式数据中心）是指可以根据电网调度指令灵活调整其用电或注入功率的负荷资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2308.03240">Carbon -Aware Optimal Power</a></li>
<li><a href="https://www.emergentmind.com/topics/two-stage-attention-mechanism">Two- Stage Attention Mechanism</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dispatchable_generation">Dispatchable generation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#carbon forecasting`, `#power systems`, `#deep learning`, `#attention mechanisms`, `#multi-agent systems`

---

<a id="item-15"></a>
## [FinSMART：市场对齐强化学习框架用于金融情感分析](https://arxiv.org/abs/2607.28127) ⭐️ 8.0/10

FinSMART 提出了一种市场对齐的强化学习框架，通过信号提取管道和非对称交易奖励，利用实现的市场结果来优化金融情感信号。 FinSMART 从静态的监督学习转向市场对齐的强化学习，使模型能够持续适应不断变化的市场条件，降低对昂贵人工标注数据的依赖，并提升交易表现。 该框架在信号提取管道中结合市场感知数据过滤和离散非对称交易奖励，相比最强基线实现了累计交易回报提升 220%，并且可以随时使用新观察到的文章及其实际市场结果进行再训练。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 金融情感分析传统上依赖于在静态、人工标注数据集上微调的大型语言模型，这限制了它们适应不断变化的市场动态的能力。强化学习提供了一种直接从实现的市场反馈中优化模型的方法，但金融市场具有噪声、非平稳和多因素的特点，需要专门的奖励塑造和信号提取技术。FinSMART 通过引入市场感知过滤步骤和非对称交易奖励来解决这些挑战，以实现从经济上有意义的信号进行稳定的强化学习训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.28127">FinSMART: Financial Sentiment Analysis for Algorithmic Trading ...</a></li>
<li><a href="https://www.researchgate.net/publication/385107638_Aligning_LLMs_with_Human_Instructions_and_Stock_Market_Feedback_in_Financial_Sentiment_Analysis">Aligning LLMs with Human Instructions and Stock Market Feedback in...</a></li>
<li><a href="https://medium.com/@PiyushRanjanTech/ai-driven-sentiment-analysis-revolutionizing-trading-through-real-time-market-psychology-13f4a0073e26">AI-Driven Sentiment Analysis : Revolutionizing Trading... | Medium</a></li>

</ul>
</details>

**标签**: `#financial sentiment analysis`, `#reinforcement learning`, `#algorithmic trading`, `#large language models`, `#market-aware signal extraction`

---

<a id="item-16"></a>
## [LLM 驱动的 PACE 框架提升深交所父母订单执行](https://arxiv.org/abs/2607.28410) ⭐️ 8.0/10

论文提出 PACE，一种分层的 LLM 驱动父母订单执行框架，无需市场假设或任务特定训练，在深交所一级数据上优于 TWAP、Almgren-Chriss 和学习基线，领先 0.65 个基点。 这是首次系统研究将大语言模型应用于父母订单执行，表明语言模型能在不依赖传统金融模型的情况下降低交易成本，可能扩大 AI 在算法交易中的作用。 PACE 将执行分解为长期规划和短期控制，利用 LLM 置信度作为表现信号，行为分析显示模型倾向于提前交易而非拖延至截止时间。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 父母订单执行是指将大额订单拆分成多个小单以降低市场冲击和时序风险，是算法交易的核心问题。传统方法如 TWAP 和 Almgren-Chriss 模型依赖于预设的市场假设或需要任务特定训练，适应性有限。大型语言模型在金融领域已用于预测买卖方向等任务，本工作首次将其用于决定如何执行订单。实验使用了深交所一级数据，该数据提供每三秒更新的买卖报价，涵盖交易所上市的股票、债券、基金和指数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/understanding-almgren-chriss-model-optimal-portfolio-execution-pal-pmeqc">Understanding the Almgren - Chriss Model for Optimal Portfolio...</a></li>
<li><a href="https://www.mexem.com/market-data">Market Data</a></li>
<li><a href="https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp">investopedia.com/articles/active- trading /101014/basics- algorithmic ...</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Algorithmic Trading`, `#Order Execution`, `#Finance`, `#Machine Learning`

---

<a id="item-17"></a>
## [自动做市商中的最优动态费用](https://arxiv.org/abs/2506.02869) ⭐️ 8.0/10

该论文推导了常数函数做市商（CFMM）的最优动态费用策略，发现存在两种不同的费用 regimes，并表明与库存线性相关的费用能够逼近最优解。 提供费用设计的闭式解有助于去中心化金融（DeFi）协议提高资本效率并减少有害套利，从而惠及流动性提供者和交易者。 分析得到两种 regimes：高费用以威慑套利者，低费用以增加波动并吸引噪声交易者；与库存线性且对外部价格变化敏感的费用能够紧密逼近最优策略。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 自动做市商（AMM）通过常数函数做市商（CFMM）不变量实现去中心化交易，该不变量根据池子中的储备资产确定价格。在 CFMM 中，流动性提供者存入代币并从交易中获取费用，而套利者则利用 AMM 与外部市场之间的价差获利。动态费用机制会根据池子的库存或外部价格变化调整费率，以在流动性提供和套利活动之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Constant_function_market_maker">Constant function market maker - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2506.02869v2">Optimal Dynamic Fees in Automated Market Makers</a></li>
<li><a href="https://www.linkedin.com/posts/oxford-man-institute-of-quantitative-finance_optimal-dynamic-fees-in-automated-market-activity-7336361177993703424-rm5y">Optimal Dynamic Fees in Automated Market Makers | Oxford-Man...</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#Automated Market Makers`, `#Dynamic Fees`, `#Financial Mathematics`, `#Trading Strategies`

---

<a id="item-18"></a>
## [女性担忧，男性采用？生成式 AI 采用中的性别风险感知](https://arxiv.org/abs/2601.03880) ⭐️ 8.0/10

基于英国公众对数据和 AI 态度追踪调查（N=9,172）的研究发现，男性报告的生成式 AI 频繁个人使用水平显著高于女性，这一差异与性别对 AI 社会风险的感知有关。 该研究表明，社会风险感知而非仅仅是技能或获取条件，推动了生成式 AI 采用中的性别差距，凸显了可能加剧生产力和职业不平等的行为途径。 在年轻、数字流畅且对社会风险担忧较高的受访者中，个人生成式 AI 使用的性别差距超过 45 个百分点；感知到的社会风险对女性的使用预测力更强，而对 AI 影响的乐观程度提升与女性采用率的更大增加相关。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 生成式 AI 正在快速普及，但采用仍然不均衡；早期研究将差距归因于获取、数字技能和信心的差异。英国公众对数据和 AI 态度追踪调查提供了全国代表性的纵向数据，研究采用了按性别和年龄分层的随机森林模型以及参数评分匹配法来隔离风险感知的作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.uk/government/publications/public-attitudes-to-data-and-ai-tracker-survey">Public attitudes to data and AI : Tracker survey - GOV. UK</a></li>
<li><a href="https://proceedings.mlr.press/v119/zhou20c/zhou20c.pdf">Nonparametric Score Estimators</a></li>
<li><a href="https://www.researchgate.net/figure/mportance-ranking-of-the-variables-based-on-the-Random-forest-predictions-All-patients_fig3_348250248">Importance ranking of the variables based on the Random forest ...</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Gender differences`, `#Risk perception`, `#AI adoption`, `#Social impact`

---

<a id="item-19"></a>
## [研究表明无关文本使 LLM 在研究生经济考试中的正确率下降约 12 个百分点](https://arxiv.org/abs/2607.23424) ⭐️ 8.0/10

研究人员在研究生水平的经济学问题中加入无关段落（红鲱鱼），发现语言模型的正确答案率平均下降约 12.3 个百分点。 这一结果凸显了 LLM 的一个关键弱点：即使输出看起来连贯，它们也可能被无关信息误导，这引发了对其在实际推理任务中可靠性的担忧。 该研究采用被试内 2×2 因子设计，让 38 种语言模型在有无红鲱鱼及是否要求解释的条件下回答 60 道 GERB 问题；无红鲱鱼时平均正确率约 52.5%，加入红鲱鱼后下降 12.3 个百分点，效应在模型认为简单的问题上最大，且与模型是否具备推理能力无关。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 大型语言模型（LLM）是在海量文本语料上训练的神经网络，能够生成类似人类的语言并执行推理任务。红鲱鱼是指在问题中插入的无关文本，用来分散解题者的注意力，这一概念来源于认知心理学。研究生经济推理基准（GERB）包含六十道研究生水平的微观经济学问题，每道问题都有经过验证的答案和逐步参考解答，用于评估模型的经济推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.23424">Wrong and More Confident: A Field Experiment on Language Models ...</a></li>
<li><a href="https://paperswithcode.co/paper/2306.11167">Large Language Models are Fixated by Red Herrings : Exploring...</a></li>
<li><a href="https://papers.nips.cc/paper/2023/hash/11e3e0f1b29dcd31bd0952bfc1357f68-Abstract-Datasets_and_Benchmarks.html">Large Language Models are Fixated by Red Herrings : Exploring...</a></li>

</ul>
</details>

**标签**: `#LLM robustness`, `#reasoning evaluation`, `#red herring effect`, `#graduate economics benchmark`, `#AI reliability`

---

<a id="item-20"></a>
## [连续时间强化学习框架用于多 regime 最优切换并采用熵正则化](https://arxiv.org/abs/2512.04697) ⭐️ 8.0/10

本文提出了一种使用熵正则化的连续时间强化学习框架，以随机化开关时机和通过生成器矩阵选择 regime。它证明了相关 Hamilton-Jacobi-Bellman 方程的良好性质，刻画了最优策略，验证了策略迭代的收敛性，并给出了一种在金融示例中验证的无模型强化学习算法。 这项工作通过提供理论严谨且无模型的方法来解决最优切换问题，桥接了强化学习与随机控制，而这类问题在金融、能源管理和运筹学中很常见。其收敛保证以及通过熵正则化实现的探索-利用平衡，使其适用于模型参数未知的实际系统。 该探索性 formulation 使用连续时间有限状态马尔可夫链的生成器矩阵来随机化切换，并证明相关的 HJB 方程组是良好姿态的；当温度参数趋于零时，探索性价值函数收敛到经典价值函数。基于鞅的策略评估导出的无模型算法在数值金融示例中得到演示。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: 连续时间强化学习将标准的强化学习扩展到决策和状态演化在连续时间中进行的环境，这通常由随机微分方程建模。最优切换问题涉及决定何时在不同的动态 regime 之间切换以最小化成本或最大化奖励，这在金融和控制中很常见。Hamilton‑Jacobi‑Bellman（HJB）方程刻画了此类随机控制问题的最优价值函数，而熵正则化则添加了一个平滑 Bellman 备份的探索项。在这项工作中，切换机制由连续时间马尔可夫链的生成器矩阵控制，该矩阵定义了过程在不同 regime 之间跳转的速率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.04697">[2512.04697] Continuous - time reinforcement learning for optimal ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reinforcement_learning">Reinforcement learning - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_chain">Markov chain - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#continuous-time`, `#optimal switching`, `#Hamilton-Jacobi-Bellman`, `#entropy regularization`

---

<a id="item-21"></a>
## [研究发现以太坊日内 gas 费峰值与套利活动相关，企业调度响应呈异质性](https://arxiv.org/abs/2604.19956) ⭐️ 8.0/10

该研究分析了七家跨行业运营公司在 2026 年 1 月至 3 月的 62,142 笔以太坊确认交易，发现 gas 费在 UTC 12 时达到峰值，较美国晚上基准高出 0.054 美元，这一峰值与投机套利活动增强相关。企业的调度响应根据交易的可延期性和 gas 强度表现出异质性。 研究结果揭示了以太坊在 EIP‑1559 下日内费用市场的显著异质性，表明企业可以通过调整链上活动时间来降低交易成本。这一发现对研究人员、开发者和希望优化区块链经济学和 gas 费用暴露的企业具有重要参考价值。 剩余成本底线——即实际支出与理想非高峰调度所能达到的成本之间的差距——占实际支出的 40.7%至 92.5%，即使在成本最低的时段（UTC 20‑23）也仍然存在。作者提出了链上调度矩阵，根据交易的可延期性和 gas 强度将企业划分为四类，以指导费用节约策略。

rss · arXiv Quantitative Finance · Jul 31, 04:00

**背景**: EIP‑1559 用基础费加矿工小费取代了以太坊的第一价拍卖，旨在使 gas 价格更具可预测性。交易的可延期性指的是在不损失价值的情况下将交易在时间上移动的难易程度，而 gas 强度则衡量每单位经济活动所需的 gas 量。这两个属性产生了异质需求模式，即使协议仅提供单一拥堵信号，也会导致日内 gas 费波动。理解这种异质性有助于解释为什么企业对 gas 价格峰值的调度响应存在差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eips.ethereum.org/EIPS/eip-1559">EIP - 1559 : Fee market change for ETH 1.0 chain</a></li>
<li><a href="https://www.researchgate.net/publication/311549710_Blockchain_application_and_outlook_in_the_banking_industry">(PDF) Blockchain application and outlook in the banking industry</a></li>
<li><a href="https://ethereum.org/developers/docs/gas/">Ethereum gas and fees : technical overview | ethereum .org</a></li>

</ul>
</details>

**标签**: `#Ethereum`, `#EIP-1559`, `#gas fees`, `#blockchain economics`, `#empirical study`

---