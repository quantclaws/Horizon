---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> From 39 items, 15 important content pieces were selected

---

1. [Anthropic 发布 Claude Opus 5，具备增强能力且无数据保留要求](#item-1) ⭐️ 8.0/10
2. [Postgres LISTEN/NOTIFY 实际上可以扩展](#item-2) ⭐️ 8.0/10
3. [安全摄像头供应商泄露 GitHub 管理员令牌。](#item-3) ⭐️ 8.0/10
4. [尽管编码已解决，软件质量为何仍在下降？](#item-4) ⭐️ 8.0/10
5. [英伟达、微软、Meta 警告过度监管开放权重 AI](#item-5) ⭐️ 8.0/10
6. [Buz：使用现代 Zig 的 Bun 分支实现亚秒增量构建](#item-6) ⭐️ 8.0/10
7. [九十年技术变革未使电力需求对价格更敏感](#item-7) ⭐️ 8.0/10
8. [从关键词链接到 AI 代理委托决策的数字搜索演变。](#item-8) ⭐️ 8.0/10
9. [飞机登机分组：静态策略基准与深度强化学习动态分配优化](#item-9) ⭐️ 8.0/10
10. [人工智能替代原则预测层级组织中 AI 取代人类](#item-10) ⭐️ 8.0/10
11. [研究发现生成式 AI 可用性未导致大学课程成绩通胀](#item-11) ⭐️ 8.0/10
12. [简历审计发现雇佣歧视与工作任务内容高度相关。](#item-12) ⭐️ 8.0/10
13. [均匀损失自动做市商框架用于预测市场](#item-13) ⭐️ 8.0/10
14. [DatedGPT：通过时间感知预训练防止大型语言模型的前视偏差](#item-14) ⭐️ 8.0/10
15. [研究显示 AI 进展呈潮汐上升而非突浪](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 5，具备增强能力且无数据保留要求](https://www.anthropic.com/news/claude-opus-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 5，这是其旗舰大语言模型的最新版本，提供了改进的推理、编码和代理能力，同时保持了每百万输入 token 5 美元、输出 token 25 美元的定价以及 100 万 token 的上下文窗口。更重要的是，该模型在通用访问中保持无数据保留政策，缓解了隐私顾虑。 通过取消数据保留要求，Claude Opus 5 吸引了对数据隐私有严格需求的受监管行业企业，而其在编码和代理任务上的强劲表现使其成为复杂 AI 工作流的有竞争力的选择。此次发布也凸显了在不断扩大的 LLM 市场中，模型路由和定价透明度日益重要的趋势。 根据其系统卡，Claude Opus 5 支持多语言纯文本输出，具有 1,000,000 token 的上下文窗口，最大输出为 128,000 token，并通过 API 以每百万输入 token 5 美元、输出 token 25 美元的价格提供。该模型是多语言的，通常会以用户输入的同一种语言进行响应，并且在通用访问下不保留用户数据。

hackernews · alvis · Jul 24, 16:57 · [社区讨论](https://news.ycombinator.com/item?id=49038433)

**背景**: Claude 是 Anthropic 旗下的一系列大型语言模型，专为推理、编码和代理任务设计。早期版本如 Claude Opus 4 和 Opus 4.5 在有用性和安全性方面设定了基准。Opus 系列以其在专家提升试验和代理编码评估中的强劲表现著称，同时坚持最小化数据保留。Claude Opus 5 延续这一脉络，提供 100 万 token 的上下文窗口和不变的定价，强调纯文本、多语言输出。其发布体现了 Anthropic 在不施加用户数据存储义务的情况下提供前沿能力的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude+Opus+5+System+Card.pdf">Claude Opus 5 System Card</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.marktechpost.com/2026/07/24/meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing/">Meet the New Claude Opus 5: Frontier-Class Agentic Coding and Computer Use at Unchanged Opus Pricing - MarkTechPost</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了无数据保留是该模型相较于 Fable 等竞争对手的最重要优势。有人指出 Opus 5 在图像转 HTML 的转换准确性上优于 Fable，也有人观察到其写作风格保留了早期 Opus 版本特有的“Claude‑isms”。少数用户还提到，模型路由的快速增长是对日益增多的模型、模态和定价选项的一种回应。

**标签**: `#Claude Opus 5`, `#Anthropic`, `#LLM release`, `#AI models`, `#data retention`

---

<a id="item-2"></a>
## [Postgres LISTEN/NOTIFY 实际上可以扩展](https://www.dbos.dev/blog/postgres-listen-notify-scalability) ⭐️ 8.0/10

DBOS 博客表明，Postgres LISTEN/NOTIFY 能够在单个服务器上达到每秒 60,000 次写入，延迟在毫秒级，表明其能够处理高吞吐量的发布/订阅工作负载。 这挑战了 LISTEN/NOTIFY 不能扩展的常见看法，为在实时应用中使用 Postgres 作为低延迟持久消息代理提供了可能，无需外部队列。 该基准通过优化锁定和批处理实现，同时遵守 8000 字节有效载荷限制和同数据库限制；早期版本曾因锁定不佳而性能不佳，现已修正。

hackernews · KraftyOne · Jul 24, 19:05 · [社区讨论](https://news.ycombinator.com/item?id=49040296)

**背景**: PostgreSQL 的 LISTEN/NOTIFY 是一种异步的服务器到客户端通知机制：会话执行 NOTIFY 频道 [有效载荷]，之前已执行 LISTEN 频道的会话会收到该事件。有效载荷限制为 8000 字节，且仅在同一数据库实例内工作。传统上用于轻量级发布/订阅，但因所有通知共享单个数据库实例并可能出现锁争用而被认为不可扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dbos.dev/blog/postgres-listen-notify-scalability">Postgres LISTEN/NOTIFY Actually Scales | DBOS</a></li>
<li><a href="https://www.postgresql.org/docs/current/sql-notify.html">PostgreSQL: Documentation: 18: NOTIFY</a></li>
<li><a href="https://www.cybertec-postgresql.com/en/listen-notify-automatic-client-notification-in-postgresql/">LISTEN / NOTIFY: Automatic client notification in PostgreSQL</a></li>

</ul>
</details>

**社区讨论**: 评论者指出可扩展性是一个连续体，jerf 强调 60K 次写入/秒对某些工作负载可能足够，对另一些则不足。nzoschke 赞赏 DBOS 有效利用 Postgres，而 dang 链接到了早期质疑 LISTEN/NOTIFY 扩展性的 HN 帖子。vhiremath4 分享了在 LISTEN/NOTIFY 上构建队列以获得强一致性的经验，dietr1ch 回忆起早期的锁定问题现已得到修正。总体而言，讨论表现出对新基准的兴趣，承认其局限性，并赞赏 DBOS 的优化工作。

**标签**: `#Postgres`, `#LISTEN/NOTIFY`, `#scalability`, `#pub/sub`, `#database`

---

<a id="item-3"></a>
## [安全摄像头供应商泄露 GitHub 管理员令牌。](https://hhh.hn/hanwha-github-token/) ⭐️ 8.0/10

某安全摄像头供应商无意中将 GitHub 管理员令牌嵌入其设备登录页面，导致令牌在页面源码中可见。该暴露的令牌赋予了对供应商 GitHub 仓库的管理员级访问权限。 此事件表明物联网硬件中的硬编码凭据可能导致供应链被攻破，攻击者可窃取源代码、篡改 CI/CD 流程或注入恶意代码。这凸显了在设备固件中实施严格的密钥管理实践的必要性。 令牌以明文形式出现在登录页面的 HTML/JavaScript 中，具有管理员范围，可读取、修改或删除私有仓库并触发 GitHub Actions。撤销该令牌并审计所有依赖它的系统是缓解泄露的必要步骤。

hackernews · hhh · Jul 24, 11:54 · [社区讨论](https://news.ycombinator.com/item?id=49034292)

**背景**: 物联网设备常常出厂时携带硬编码凭据，如默认密码或 API 密钥，攻击者可从固件或网页界面提取这些凭据以获得未授权访问。GitHub 个人访问令牌（PAT）相当于用于 API 访问的密码，若具备管理员范围，则可读取、修改或删除仓库并触发 CI/CD 作业。供应链攻击若将此类令牌嵌入消费硬件，可能同时危及供应商内部开发环境以及依赖该代码的下游用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiespionage.net/cybersecurity/my-security-camera-shipped-a-github-admin-token-in-its-login-page/">My Security Camera Shipped A GitHub Admin Token In Its Login Page</a></li>
<li><a href="https://www.techtarget.com/searchsecurity/tip/How-hard-coded-credentials-threaten-industrial-control-systems">How hard - coded credentials threaten ICS security | TechTarget</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者指出物联网固件中硬编码密钥的普遍问题，建议将摄像头隔离在无互联网访问的 VLAN 中，并质疑是否存在可定制固件的白牌摄像头。有人对韩国安防产品表示不信任，并回忆起过去分配私有 IP 地址的临时做法。

**标签**: `#IoT security`, `#supply chain`, `#hardcoded credentials`, `#GitHub token`, `#vulnerability`

---

<a id="item-4"></a>
## [尽管编码已解决，软件质量为何仍在下降？](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/) ⭐️ 8.0/10

该文章认为，尽管编码问题基本得到解决，但软件质量却因错位激励、不断更换工具以及非技术决策者推动变革而持续下降。 它指出科技公司内部的系统性激励结构削弱了产品可靠性，影响开发者和最终用户，并表明需要将奖励从新颖转向质量。 文章举例说明工程师因构建闪亮的新工具而获得晋升，组织内部出现大量重叠工具，以及诸如 macOS 焦点抢夺错误等具体问题，这些都削弱了用户信任。

hackernews · pchm · Jul 24, 09:08 · [社区讨论](https://news.ycombinator.com/item?id=49033004)

**社区讨论**: 评论者普遍同意激励机制导致无谓的工具 proliferation，对软件更新感到恐惧，并批评非技术领导者追求新颖而牺牲稳定性，同时提及诸如 Slack 焦点抢夺等具体烦恼。

**标签**: `#software engineering`, `#software quality`, `#incentives`, `#tech industry`, `#productivity`

---

<a id="item-5"></a>
## [英伟达、微软、Meta 警告过度监管开放权重 AI](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) ⭐️ 8.0/10

英伟达、微软和 Meta 联合发布一封信，呼吁美国政府避免过度监管开放权重 AI 模型，以保护创新并维持美国领导地位。 这一联合立场表明主要科技公司对 AI 政策有重大影响，可能塑造未来的美国监管，影响开发者、初创公司以及全球 AI 竞争力。 该信件以 PDF 形式发布在 Nvidia 网站，并被 Jensen Huang 的推文突出显示，同时引用了关于开放权重与开源模型的相关讨论。

hackernews · louiereederson · Jul 24, 13:32 · [社区讨论](https://news.ycombinator.com/item?id=49035303)

**背景**: 开放权重模型是指其训练得到的参数（权重）公开发布，任何人都可以下载并使用，但不一定包含模型的源代码、训练数据或训练过程。与之不同，开源模型除了权重外还提供完整的源代码、训练脚本以及常用的数据集，允许用户从头研究、修改和重新训练模型。目前，美国政府正在考虑对 AI 模型进行监管，而一些公司担心过度限制会阻碍创新并削弱美国在全球 AI 竞争中的地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://medium.com/lets-code-future/open-weight-ai-models-what-they-are-and-why-openais-next-move-matters-f86fe481973a">Open-Weight AI Models: What They Are, and Why OpenAI’s Next Move Matters</a></li>
<li><a href="https://www.linkedin.com/posts/wisestack-ai_gptoss-opensource-openweight-activity-7359896881591701504-jEyz">Open weight models vs open source models : what's the... | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Anthropic 在为监管游说，并讽刺地使用 Kimi 等模型同时主张限制。其他人警告闭源利益正试图禁止开放权重，将其与过去的 SOPA 辩论类比，并猜测联合信背后的动机。还有人引用了相关的 HN 讨论，其中初创公司创始人呼吁美国不要切断对中国开放权重 AI 的获取。

**标签**: `#AI regulation`, `#open-weight models`, `#tech policy`, `#Nvidia`, `#Microsoft`, `#Meta`

---

<a id="item-6"></a>
## [Buz：使用现代 Zig 的 Bun 分支实现亚秒增量构建](https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891) ⭐️ 8.0/10

Buz 是 Bun 的工作中分支，用现代 Zig 重写，删除了超过 11,000 行死代码，并通过利用 Zig 标准库实现亚秒增量构建。 该项目表明，通过清理死代码并采用 Zig，JavaScript 工具链的显著性能提升是可能的，这可能影响未来的打包器和运行时设计。 Buz 目前尚未准备好用于生产，Zig 增量编译不支持 aarch64，只有 Linux 链接器支持二进制补丁；它依赖 Zig 标准库，并删除了超过 11,000 行死代码。

hackernews · kristoff_it · Jul 24, 09:26 · [社区讨论](https://news.ycombinator.com/item?id=49033099)

**背景**: Bun 是一个快速的 JavaScript 运行时和工具链，旨在以更快的启动速度和内置转译取代 Node.js。Zig 是一种通用系统编程语言，强调安全、性能以及与 C 的无缝互操作性，并拥有不断增长的标准库。增量构建通过重用之前的构建输出仅重新编译已更改的文件，从而大幅缩短开发期间的重建时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891">Buz - A drop-in replacement for Bun using modern Zig, with sub-1s incremental builds - Showcase - Ziggit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://rushjs.io/pages/advanced/incremental_builds/">Incremental builds | Rush</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Bun 中竟积累了超过 11,000 行死代码感到惊讶，认为此分支证明更快的构建本来就是可能的。他们也指出仍存在的障碍，如 Zig 增量编译尚不支持 aarch64 以及仅 Linux 链接器支持二进制补丁，并有人讽刺地指出使用大语言模型来清理其自身产生的混乱。

**标签**: `#JavaScript tooling`, `#Zig`, `#Bun`, `#incremental builds`, `#open-source fork`

---

<a id="item-7"></a>
## [九十年技术变革未使电力需求对价格更敏感](https://arxiv.org/abs/2607.21285) ⭐️ 8.0/10

该研究通过对 1934-2024 年间 462 项研究的 4,720 个自身价格弹性估计进行元分析，发现最可靠的研究表明短期价格弹性约为-0.09，基本不显著不同于零，且九十年来未见上升趋势。 这一结果挑战了脱碳规划中电力需求将随技术进步而变得更具价格弹性的假设，表明仅靠价格机制不足以实现所需的需求灵活性，必须通过技术、合同和政策设计来工程化实现。 在校正出版物偏差后， naive 估计的短期弹性约为-0.16（价格上涨 10%导致消费下降不到 2%），而最可靠研究的调整值为-0.09；长期弹性约为-0.38，且这一随时间调整的增长模式在数十年间保持稳定，技术丰富环境（如分时定价）反而表现出最低的总体价格响应。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 电力需求价格弹性衡量价格变动百分比导致的消费量百分比变化，是能源系统建模和脱碳情景中的重要参数。计量经济学家通过识别质量阶梯（从简单回归到随机实验）来评估弹性估计的可靠性，阶梯越高因果推断越可靠。出版偏倚——显著结果更易被发表——可能导致元分析中的平均弹性被高估，因此需要采用校正方法以获得无偏结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/269693689_Price_Elasticity_of_Demand_for_Electricity_A_Primer_and_Synthesis">(PDF) Price Elasticity of Demand for Electricity : A Primer and...</a></li>
<li><a href="https://www.aje.com/arc/assessing-and-avoiding-publication-bias-in-meta-analyses">Assessing and Avoiding Publication Bias in Meta - analyses | AJE</a></li>
<li><a href="https://openlibrary.org/works/OL1906567W/The_identification_problem_in_econometrics">The identification problem in econometrics by... | Open Library</a></li>

</ul>
</details>

**标签**: `#energy economics`, `#electricity demand`, `#price elasticity`, `#decarbonization`, `#meta-analysis`

---

<a id="item-8"></a>
## [从关键词链接到 AI 代理委托决策的数字搜索演变。](https://arxiv.org/abs/2607.21459) ⭐️ 8.0/10

该论文宣布 arXiv:2607.21459v1，描述数字搜索如何从传统的基于关键词的查询和排名链接列表转向 AI 代理中介的委托决策，用户用自然语言陈述目标，代理执行决策。这一变化将搜索从基于链接的界面转移到嵌入式系统组件，影响透明度、竞争和货币化。 这一变化很重要，因为它重新定义了搜索中信息质量、信任和激励一致性的管理方式，微小的设计选择对效率、竞争以及消费者和企业福利具有第一阶的影响。它凸显了需要开放、透明且具有竞争力的代理系统来塑造未来的市场结构和政策。 作者指出，诸如利益相关者如何获取信息、如何呈现选项以及如何执行操作等设计因素对结果有关键影响，这一点得到了实验性代理中介市场和经济理论的早期证据支持。这些发现表明，相较于排名算法的渐进改进，代理决策系统的架构更具影响力。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 在传统的数字搜索中，用户将意图转化为基于关键词的查询，评估排名链接列表，并在搜索界域外执行决策。在 AI 原生环境中，用户用自然语言表达目标，代理解释这些意图，并直接返回建议或执行决策，实现委托决策。这一转变引发了对透明度、偏见和市场力量的担忧，而代理中介市场则自动化撮合、调度和定价，影响竞争和福利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.21459">The Evolution of Digital Search: From Blue Links to Delegated ...</a></li>
<li><a href="https://medium.com/@drjohnmillar/when-the-buyer-is-a-machine-why-agentic-commerce-threatens-the-trillion-dollar-advertising-model-d8a03a583ffc">When the Buyer Is a Machine: Why Agentic Commerce... | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/umeshkribanandan_agenticcommerce-ecommerce-ai-activity-7414969236885942272-Ve9T">#agenticcommerce #ecommerce # ai #retail #digitalcommerce # search ...</a></li>

</ul>
</details>

**标签**: `#information retrieval`, `#AI agents`, `#search engines`, `#market design`, `#human-computer interaction`

---

<a id="item-9"></a>
## [飞机登机分组：静态策略基准与深度强化学习动态分配优化](https://arxiv.org/abs/2607.21512) ⭐️ 8.0/10

本文提出一种将飞机登机分组建模为马尔可夫决策过程并使用近端策略优化（PPO）以及卷积神经网络编码座位分配状态来求解的动态方法。在六种单双通道机型上的实验表明，该方法比最优的静态后前登机策略将总登机时间降低多达 9.8%、平均个人登机时间降低多达 22.8%。 提高登机效率能够直接缩短飞机周转时间、降低运营成本并改善乘客体验，因此对航空公司和机场具有重要价值。该研究将强化学习与运筹学结合，展示了人工智能在优化诸如乘客登机这类随机实际过程中的潜力。 该政策采用卷积神经网络对已登记的座位占用、组别和行李情况进行编码，并通过近端策略优化最大化兼顾总登机时间与平均个人登机时间的奖励。实验涵盖六种单双通道机型，并在不同载客率、同伴规模和行李负载下进行测试，表明策略在分布外条件下仍保持鲁棒性。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 飞机登机通常根据诸如后前或优化分块等静态规则将乘客分配到几个顺序的登机组，这些规则忽略了到达时间和座位选择的随机性。强化学习将决策建模为马尔可夫决策过程，智能体通过与环境交互学习以最大化累积奖励的策略。近端策略优化（PPO）是一种广泛使用的强化学习算法，通过裁剪代理目标来稳定训练；卷积神经网络擅长从网格状输入（如座位图）中提取空间特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proximal_policy_optimization">Proximal policy optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Convolutional_neural_network">Convolutional neural network - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2607.21512">Group boarding for airplanes : benchmarking static policies and...</a></li>

</ul>
</details>

**标签**: `#airplane boarding`, `#reinforcement learning`, `#operations research`, `#deep learning`, `#dynamic assignment`

---

<a id="item-10"></a>
## [人工智能替代原则预测层级组织中 AI 取代人类](https://arxiv.org/abs/2607.20781) ⭐️ 8.0/10

该论文（arXiv:2607.20781v1）提出了一种用于层级组织的分析性人工智能任务分配（HAT）模型，并推导出人工智能替代原则，该原则基于人类技能获取与 AI 能力扩展之间的经济不对称性，精确指出 AI 何时会取代人类劳动。 通过给出 AI 驱动的劳动替代的正式条件，该模型提供了一种严谨的工具，用于预测劳动力转型、指导组织重塑以及为 AI 治理和政策决策提供依据。 HAT 模型正式表征了人类技能获取的高成本与 AI 能力可扩展性之间的不对称性，表明 AI 采用可能导致突发的劳动力转变、在无最低人类比例要求下维持人机混合角色、使管理层级变得更扁平、且中层管理岗位特别容易被自动化，而高技能工人的脆弱性则取决于由组织深度、基础成本和风险差异塑造的技能阈值。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 层级组织由多个层级组成，任务根据技能和成本进行分配。人类技能的获取通常需要大量时间和投资，而 AI 的能力则可以以较低的边际成本快速扩展。这种经济不对称性导致在某些任务上 AI 可能比人力更具成本效益。HAT 模型将这种不对称性形式化，以预测在这些结构中 AI 何时何地会取代人类劳动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.20781">The Human - AI Substitution Principle : When will you be replaced by...</a></li>
<li><a href="https://arxiv.org/abs/2607.20781">The Human-AI Substitution Principle: When will you be replaced by AI in ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Human-AI collaboration`, `#Organizational economics`, `#Task allocation`, `#Substitution principle`

---

<a id="item-11"></a>
## [研究发现生成式 AI 可用性未导致大学课程成绩通胀](https://arxiv.org/abs/2607.21534) ⭐️ 8.0/10

该研究使用 2015‑2025 年大型美国大学的课程大纲和行政数据（156,135 名学生），通过差分‑差分设计和人工验证的 LLM 管道评估课程对生成式 AI 的敏感度，发现对成绩和自报理解没有显著影响，仅在假设疫情影响为暂时时对兴趣有显著效果。 它提供了关于生成式 AI 是否导致成绩通胀或满意度下降的严谨证据，为教育工作者和政策制定者提供了 AI 对高等教育学习成果实际影响的参考。 分析涵盖 87,936 门课程，采用人工验证的 LLM 管道从课程大纲中提取评估类型，并将 COVID‑19 影响建模为持续或暂时，仅在暂时假设下兴趣效果显著。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 差分‑差分（DiD）是一种准实验方法，通过比较接受干预的处理组和未接受干预的对照组随时间的变化来隔离因果效应。本研究中，处理是 ChatGPT 发布后的时期，敏感度通过使用经过人工验证的 LLM 管道从课程大纲中提取评估类型（如带回家的问题集、论文）来测量。这种方法使研究者能够检查在 AI 广泛可用后，更易受 AI 辅助的课程在成绩或满意度上的趋势是否有所不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>
<li><a href="https://python.useinstructor.com/">Instructor - Multi-Language Library for Structured LLM Outputs</a></li>
<li><a href="https://www.researchgate.net/publication/388313672_Appraising_higher_education_assessment_validity_Development_of_the_PANDORA_GenAI_Susceptibility_Rubric">(PDF) Appraising higher education assessment validity: Development...</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#higher education`, `#student performance`, `#AI impact`, `#differences-in-differences`

---

<a id="item-12"></a>
## [简历审计发现雇佣歧视与工作任务内容高度相关。](https://arxiv.org/abs/2604.01933) ⭐️ 8.0/10

研究人员向美国 9,220 份针对应届毕业生的职位广告投递了 36,880 份假简历，按种族、性别和广告文本测量回叫率。结果显示，黑人和西班牙裔申请者以及女性在管理岗位上的回叫率比白人男性低 28%‑43%，歧视集中在分析和人际需求高、常规任务低的工作中。 该研究表明，歧视并非在所有职业中均匀分布，而是随工作所需的具体任务而变化，指出了偏见最可能发生的地方。这些发现有助于雇主设计更客观的招聘流程，并为政策制定者提供减少劳动力市场不平等的依据。 研究利用 O*NET 任务测量，将评估自由度定义为基于主观评估的招聘决策比例；结果显示，主观评估会扩大回叫差距，而客观精度会缩小差距，且客户接触会在非常规工作中放大这一效应。在管理岗位上，黑人男性、黑人女性、白人女性和西班牙裔男性的回叫率比相同条件下的白人男性低 28%‑43%。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: O*NET 是美国劳工部的一个数据库，提供职业的任务、技能和能力的标准化测量，研究者常用它来量化工作内容，如分析、人际和常规需求。评估自由度在招聘中指的是依赖主观判断而非客观可验证标准的决策比例，先前研究表明，自由度越大，偏见越可能影响结果。简历审计通过发送仅在受保护特征（如暗示种族或性别的姓名）上不同的虚假申请到真实职位，测量回叫率的差异来直接检验歧视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.onetcenter.org/overview.html">About O * NET at O * NET Resource Center</a></li>
<li><a href="https://arxiv.org/pdf/2604.01933">Hiring Discrimination and the Task Content of Jobs: Evidence from...</a></li>
<li><a href="https://www.nber.org/system/files/working_papers/w21709/w21709.pdf">Discretion in Hiring</a></li>

</ul>
</details>

**标签**: `#hiring discrimination`, `#resume audit`, `#labor economics`, `#task content`, `#O*NET`

---

<a id="item-13"></a>
## [均匀损失自动做市商框架用于预测市场](https://arxiv.org/abs/2607.17428) ⭐️ 8.0/10

论文提出了预测市场的均匀损失自动做市商（AMM），其特征是瞬时损失与再平衡（LVR）与池价值成正比且与当前代币价格无关。该工作利用胜 martingale 过程进行表征，并将框架扩展到动态流动性管理。 通过提供一种理论工具来塑造补贴成本在价格状态和时间上的分布，该工作帮助 AMM 设计者和流动性提供者更好地管理预测市场中的不可避免损失。这推动了 DeFi 市场设计，并可能提升信念聚合机制的效率。 均匀 AMM 满足 LVR 与池价值成正比、与价格无关；对于任何足够正则的胜 martingale 过程，存在实现均匀 LVR 的定价函数，反之亦然。该框架还展示了如何随时间调整流动性水平以遵循目标预期累积损失计划。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 自动做市商（AMM）通过智能合约池子实现代币交易，无需订单簿；在预测市场中，AMM 通过补贴交易来聚合对未来事件的信念。损失与再平衡（LVR）衡量当 AMM 价格落后于外部市场时，流动性提供者所承担的成本。胜 martingale 是一种建模事件结果概率随时间演变的随机过程，在固定结算时间收敛于 0 或 1。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cow.fi/learn/what-is-loss-versus-rebalancing-lvr">What is Loss - Versus - Rebalancing ( LVR )? - CoW DAO</a></li>
<li><a href="https://www.emergentmind.com/topics/win-martingales">Win - Martingales : Models and Fluctuation Analysis</a></li>
<li><a href="https://formo.so/glossary/automated-market-maker-amm">Automated Market Maker ( AMM ) | Web3 & DeFi Data Glossary</a></li>

</ul>
</details>

**标签**: `#Automated Market Makers`, `#Prediction Markets`, `#Loss-Versus-Rebalancing`, `#DeFi`, `#Market Design`

---

<a id="item-14"></a>
## [DatedGPT：通过时间感知预训练防止大型语言模型的前视偏差](https://arxiv.org/abs/2603.11838) ⭐️ 8.0/10

DatedGPT 提供了十二个 1.3B 参数的语言模型，从头开始在约 1000 亿 token 上进行训练，采用 2013‑2024 年的年度数据截止，并配套每年的指令数据集 DatedInstruct 以防止泄漏。在使用 61,000 条公司‑日新闻标题的股票回报预测任务中，DatedGPT‑instruct 实现了年化夏普比率 3.20，而带有前视偏差的模型则每个标准差增加 26.4 个基点的溢价。 通过消除前视偏差，DatedGPT 使金融预测更加可靠，并提供了一个可控的基准来研究大型语言模型中的时间知识泄漏。该方法可推广到其他对时间敏感的领域，如经济学、公共政策和科学发现。 每个模型为 1.3B 参数的 Transformer，在约 1000 亿 token 上训练；基于困惑度的探测表明其知识受限于对应的截止年份。使用未来数据训练的带前视偏差的模型在统计上显著提升每个标准差 26.4 个基点的夏普比率，凸显了偏差的程度。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: 前视偏差是指语言模型在训练过程中无意中学习到了未来的信息，从而影响其在预测任务中的可靠性。时间感知预训练通过限制训练数据在特定截止时间之前，并在某些方法中注入显式时间标记，使模型学习时间嵌入，来减轻这种偏差。先前的工作如 ChronoLLM 和 TiMoE 已经探索了类似策略，而基于困惑度的探测是验证模型有效知识截止的标准技术。DatedGPT 结合严格的年度截止与匹配的指令数据集，以确保预训练和后训练阶段均无泄漏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2512.23847">Detecting Lookahead Bias in LLM Forecasts</a></li>
<li><a href="https://www.researchgate.net/publication/389510389_Chronologically_Consistent_Large_Language_Models">(PDF) Chronologically Consistent Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2508.08827">TiMoE: Time - Aware Mixture of Language Experts</a></li>

</ul>
</details>

**标签**: `#LLM`, `#lookahead bias`, `#time-aware pretraining`, `#financial forecasting`, `#research paper`

---

<a id="item-15"></a>
## [研究显示 AI 进展呈潮汐上升而非突浪](https://arxiv.org/abs/2604.01363) ⭐️ 8.0/10

该论文分析了 O*NET 数据库中超过 6000 项基于文本的任务以及超过 60000 次工人评估，发现 AI 表现呈潮汐式上升而非突发浪潮，成功率从 2024 年第二季度的约 60%提升至 2025 年第三季度以上 70%，若趋势持续，到 2030 年可达 88%-97%。 这挑战了普遍认为 AI 能力会在狭窄领域突然跃升的观点，而是表明其呈广泛而稳定的提升，对劳动力规划、教育以及 AI 自动化政策具有重要影响。 研究使用了超过 6000 项源自 O*NET 的任务和超过 60000 次有经验工人的评估，衡量人类大约需要 1.5 小时完成的任务成功率；2024 年第二季度前沿 LLM 成功率约为 60%，到 2025 年第三季度升至 70%以上，若趋势持续，到 2030 年可达 88%-97%。

rss · arXiv Quantitative Finance · Jul 24, 04:00

**背景**: O*NET 是美国劳工部的职业信息网络，提供了一种标准化的职业任务分类法，研究者常用它来映射可被 AI 处理的工作。该研究将 AI 自动化描述为“崩浪”（突然、狭窄的能力跃升）与“潮汐上升”（广泛、持续的改善）之间的连续体。被评估的主要 AI 系统是大型语言模型（LLMs），其表现通过在现实、有时限任务上的成功率来衡量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/epoch-ai-taxonomy-ai-rd-automation/">Epoch AI proposes O * NET -style taxonomy for AI R&D automation...</a></li>
<li><a href="https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-1.pdf">AI Use Taxonomy : A Human-Centered Approach</a></li>

</ul>
</details>

**标签**: `#AI automation`, `#labor market`, `#large language models`, `#task performance`, `#AI impact`

---