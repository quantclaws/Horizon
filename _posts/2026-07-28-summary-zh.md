---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> From 27 items, 9 important content pieces were selected

---

1. [Anthropic 主张对所有能够模型进行强制安全测试](#item-1) ⭐️ 8.0/10
2. [自包含高度便携的 Python 分发版现由 Astral 维护。](#item-2) ⭐️ 8.0/10
3. [警察软件中缺失的下划线导致无辜男子被错误关押 18 个月](#item-3) ⭐️ 8.0/10
4. [研究人员利用沃尔沃/依维柯车队平台获取车辆控制权](#item-4) ⭐️ 8.0/10
5. [Paged Out #9 黑客志愿发布，聚焦底层技术](#item-5) ⭐️ 8.0/10
6. [法官驳回谷歌基于 DMCA 的针对搜索结果抓取服务的诉讼](#item-6) ⭐️ 8.0/10
7. [Moonshot AI 发布 2.8 万亿参数 Kimi K3 模型并附带新许可证](#item-7) ⭐️ 8.0/10
8. [结算现代化指数揭示内部货币弹性的 S 曲线。](#item-8) ⭐️ 8.0/10
9. [研究检测到 Solana Pump.fun 市场上的 1,012 个协同钱包队列](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 主张对所有能够模型进行强制安全测试](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布立场声明，主张所有足够强大的开放权重和封闭 AI 模型应接受强制安全测试，而非直接禁止。 该立场可能通过倡导安全优先的监管方式，塑造未来的 AI 监管，并影响开放和封闭模型的开发者。 Anthropic 主张独立的安全测试，赋予政府阻止或延迟高风险部署的权力，并认为禁令无效，同时不主张禁止开放权重模型。

hackernews · surprisetalk · Jul 27, 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开放权重模型是指其参数权重公开可用的 AI 系统，但可能不包含训练代码或数据。强制安全测试是指对强大 AI 模型进行独立评估，以在部署前评估滥用或意外行为等风险。模型治理涵盖确保模型按预期运行、保持合规并在整个生命周期内提供可信结果的框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/bruceburke_policy-on-the-ai-exponential-activity-7470865808303489025-4mKI">Anthropic Calls for Mandatory Safety Testing of Powerful AI Models</a></li>
<li><a href="https://www.ibm.com/think/topics/model-governance">What Is Model Governance? | IBM</a></li>

</ul>
</details>

**社区讨论**: 一些评论者认为强制性测试要求实际上是对开放权重模型的变相禁令，也有用户指责 Anthropic 出自自利和虚伪的信号发送。还有用户指出其在支持对华芯片禁用同时反对模型禁令的 perceived 不一致。总体而言，讨论呈现出混合情绪，对该提案的动机和可行性存在较大怀疑。

**标签**: `#AI safety`, `#open-weight models`, `#Anthropic`, `#AI policy`, `#model governance`

---

<a id="item-2"></a>
## [自包含高度便携的 Python 分发版现由 Astral 维护。](https://gregoryszorc.com/docs/python-build-standalone/main/) ⭐️ 8.0/10

python-build-standalone 项目发布自包含、高度便携的 Python 分发版。Astral 现在维护这些构建，它们被 uv、pipx、Hatch、Poetry 和 Bazel 等工具用于便携式 Python 安装。 它使开发者能够随应用一起交付 Python 或使用不依赖系统 Python 的隔离安装，简化部署并减少环境冲突。uv 和 pipx 等主要工具的采用表明对便携式 Python 生态系统的需求在增长。 这些分发版将 CPython 二进制文件和标准库打包成适用于 Linux、macOS、Windows 和 BSD 变体的自包含目录或单文件，并会跟踪上游 CPython 发布进行更新。相关项目如 PyOxy 通过添加 Rust 代码来生成单文件可执行文件，而 APE/Cosmopolitan 提供可在多种操作系统上运行的跨平台二进制文件。

hackernews · jcbhmr · Jul 27, 18:43 · [社区讨论](https://news.ycombinator.com/item?id=49073942)

**背景**: Python 构建通常需要系统已安装的解释器和依赖项，这使得跨机器重新分发变得复杂。便携式 Python 分发版将解释器及其标准库打包成自包含束缚，可在任何兼容系统上直接运行而无需安装。uv 和 pipx 等工具利用这些束缚提供快速、隔离的 Python 工具和应用执行。python-build-standalone 项目自动化了多种操作系统上这些束缚的创建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gregoryszorc.com/docs/python-build-standalone/main/">Python Standalone Builds — python-build-standalone documentation</a></li>
<li><a href="https://astral.sh/blog/python-build-standalone">A new home for python-build-standalone - Astral</a></li>
<li><a href="https://docs.astral.sh/uv/getting-started/installation/">uv is an extremely fast Python package and project manager, written...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这些分发版的可靠性以及它们在 uv、pipx 等工具中的广泛使用，并指出 Astral 的维护责任。一些人提到了相关项目，如 APE/Cosmopolitan 跨平台二进制文件和用于生成单文件可执行文件的 PyOxy，而另一些人则对将 Python 编译为 WebAssembly 以在桌面环境中运行表达了兴趣。

**标签**: `#python`, `#packaging`, `#distribution`, `#portable`, `#uv`

---

<a id="item-3"></a>
## [警察软件中缺失的下划线导致无辜男子被错误关押 18 个月](https://arstechnica.com/tech-policy/2026/07/police-missed-one-underscore-and-sent-the-wrong-man-to-prison/) ⭐️ 8.0/10

警方在调查中使用了一个因 SQL LIKE 语句中缺失下划线而出错的软件匹配，错误地将一名无辜男子与儿童剥削指控关联，导致他被定罪并监禁 18 个月。 此案表明一个微小的编程疏忽可能造成严重现实伤害，引发对问责、受害者赔偿以及执法中‘计算机不会争论’思维的审查。 缺失的下划线在 LIKE 查询中被当作匹配任意单个字符的通配符，导致记录关联搜索返回假阳性；数字取证专家指出，类似的工具错误可能误解证据并导致错误判决。

hackernews · quantified · Jul 27, 22:10 · [社区讨论](https://news.ycombinator.com/item?id=49076116)

**背景**: 在 SQL 中，下划线(_)是一个通配符，在 LIKE 模式下匹配恰好一个任意字符；如果下划线缺失，可能导致匹配过于宽泛。记录关联是指将指向同一实体的不同数据集中的记录连接起来的过程，这一过程中的错误可能产生假阳性。数字取证依赖自动化工具；这些工具中的错误或局限可能产生不正确的结论，正如某些案例中不同软件对同一工件报告的计数相差甚远所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mssqltips.com/sqlservertip/5670/examples-and-function-for-using-sql-server-like-operator-and-wildcard-characters/">SQL LIKE Wildcard with Underscore and More Examples</a></li>
<li><a href="https://en.wikipedia.org/wiki/Record_linkage">Record linkage - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1355030617301508">“I couldn't find it your honour, it mustn't be there!” – Tool errors, tool limitations and user error in digital forensics - ScienceDirect</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该男子在服刑 18 个月后仅得到定罪被撤销，几乎没有获得其他赔偿，质疑是否有补偿其收入损失和声誉伤害。多次提及‘计算机不会争论’现象，警告对自动匹配的盲目信任可能导致不公正。还有人指出控方证据的不足、案件的跨境性质（美国受害者、加拿大被告），并认为更强有力的辩护本可以质疑这一有缺陷的匹配。

**标签**: `#software-error`, `#wrongful-conviction`, `#legal-tech`, `#digital-forensics`, `#accountability`

---

<a id="item-4"></a>
## [研究人员利用沃尔沃/依维柯车队平台获取车辆控制权](https://eaton-works.com/2026/07/27/my-eicher-hack/) ⭐️ 8.0/10

一名研究员在 2025 年 11 月披露了沃尔沃/依维柯车队管理平台的安全漏洞，在多次未获回应后，该漏洞于 2025 年 11 月 20 日被修复，并于 2026 年 7 月 27 日公开披露。 该漏洞可能使攻击者控制众多商用车辆并获取用户数据，凸显物联网车队系统的安全风险，并推动了关于车辆安全和维修权的讨论。 该漏洞存在于平台的内部 API 中，披露后这些 API 被禁用；该平台由沃尔沃依维柯与 iTriangle Infotech 的 51:49 合资企业 VE Connected Solutions 运营。

hackernews · EatonZ · Jul 27, 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49070756)

**背景**: 沃尔沃依维柯商用车于 2024 年 5 月与 iTriangle Infotech 合资成立 VE Connected Solutions，提供 My Eicher 车队管理和 GPS 追踪平台。该平台利用物联网远程信息处理实时监控车辆，使车队经理能够追踪位置、性能等数据。若内部 API 未得到妥善保护，此类互联系统可能存在安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Eicher_Motors">Eicher Motors - Wikipedia</a></li>
<li><a href="https://eaton-works.com/2026/07/27/my-eicher-hack/">Exploiting Volvo/Eicher’s fleet management platform to gain control over all users and vehicles</a></li>
<li><a href="https://play.google.com/store/apps/details?id=in.here.volvo.android&hl=en_IN">MY EICHER – Apps on Google Play</a></li>

</ul>
</details>

**社区讨论**: 许多评论者担心现代汽车过度依赖云服务来实现基本功能，并指出漏洞披露过程漫长反映出响应不及时。还有人指出像 1981 年沃尔沃 244 这样的旧车型不受影响，并主张让手机直接与汽车配对，仅将云用作代理。

**标签**: `#automotive security`, `#vulnerability disclosure`, `#fleet management`, `#IoT security`, `#right-to-repair`

---

<a id="item-5"></a>
## [Paged Out #9 黑客志愿发布，聚焦底层技术](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 8.0/10

Paged Out 第 9 期作为 PDF 发布，收录了关于次像素渲染、C 语言编程及其他底层主题的文章。 该志愿因其技术深度、幽默感和精美设计受到赞誉，为系统程序员和黑客爱好者提供了精心策划的资源。 亮点内容包括《Baby Steps in C》教程和第 30 页的《Subpixel Zoo》文章，探讨次像素渲染的挑战；印刷版尚未在 Lulu 上架，读者期待其发售。

hackernews · laurensr · Jul 27, 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49070138)

**背景**: 黑客志愿是指黑客和演示场景社区中自行出版的、常以数字形式发布的杂志，用于分享技术知识、代码和文化。次像素渲染是一种显示技术，通过单独寻址红、绿、蓝三个子像素来提升彩色屏幕的表观分辨率，常用于改善 LCD 上的文字锐度。Paged Out 第 9 期通过有趣的《Subpixel Zoo》文章深入探讨此技术，展示其优点及可能产生的视觉伪影。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subpixel_rendering">Subpixel rendering</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该志愿的幽默感，特别是《Baby Steps in C》文章，以及其精美的设计，将其比作现代的 2600 或带有光栅艺术的 Phrack。多位读者指出像《Subpixel Zoo》这样的文章技术深度，并表示期待购买未来的印刷版。还有用户询问印刷版何时上架，因为目前在 Lulu 上尚未列出。

**标签**: `#systems programming`, `#low-level`, `#graphics`, `#hacker culture`, `#zine`

---

<a id="item-6"></a>
## [法官驳回谷歌基于 DMCA 的针对搜索结果抓取服务的诉讼](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

美国地区法院驳回了谷歌基于 DMCA 的诉讼，该诉讼试图阻止第三方服务抓取其搜索结果，法院认为搜索结果缺乏足够的原创性而不受版权保护。 此判决为限制搜索引擎输出的版权保护设定了先例，明确抓取公开可用的 SERP 不构成 DMCA 侵权，影响平台如何控制数据访问。 该裁决于 2026 年 7 月 27 日作出，认定谷歌的搜索结果主要是事实的编译，缺乏受版权保护所需的创造性选择或排列，因而对抓取服务 SearchGuard 的 DMCA 下架主张不成立。

hackernews · cdrnsf · Jul 27, 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: 《数字千年版权法》（DMCA）允许版权持有人对涉嫌侵权的内容发出下架通知，但仅适用于受版权保护的材料。在美国，对搜索结果等事实编译的版权保护需要在事实的选择或排列中具备一定程度的原创创意，法院经常认为这一点不成立。相比之下，欧盟的版权指令包含一种独占的数据库权，可以在不管创意的情况下保护对数据收集的实质性投资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/">Judge Rejects Google's Attempt To DMCA Its Way Out Of Being Scraped - Techdirt.</a></li>
<li><a href="https://www.quinnemanuel.com/the-firm/publications/the-legal-landscape-of-web-scraping/">The Legal Landscape of Web Scraping - Quinn Emanuel</a></li>
<li><a href="https://www.imperva.com/blog/is-web-scraping-illegal/">Is Web Scraping Illegal? | Imperva</a></li>

</ul>
</details>

**社区讨论**: 评论者批评谷歌在移除公开 API 后仍起诉抓取服务，指出讽刺之处在于谷歌自身的成功正是建立在爬取开放网络之上。一些人强调美国与欧盟在版权上的分歧：美国要求创意才能受保护，而欧盟则根据投资保护数据库。还有人指出，可抓取的搜索结果有助于打击广告诈骗，且需要提供负担得起的替代方案以减少抓取行为。

**标签**: `#web scraping`, `#DMCA`, `#copyright law`, `#Google`, `#legal precedent`

---

<a id="item-7"></a>
## [Moonshot AI 发布 2.8 万亿参数 Kimi K3 模型并附带新许可证](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 8.0/10

Moonshot AI 在 Hugging Face 发布了约 1.56 TB 的 2.8 万亿参数 Kimi K3 模型权重，并推出了一种修改后的许可证，对大型商业用户要求署名，对 Model‑as‑a‑Service 业务要求单独协议。 此次发布创下了最大开放权重 AI 模型的新纪录，凸显了模型规模的快速增长，并引发了关于许可证如何跟上如此庞大模型的讨论。 该模型拥有 2.8 万亿参数，存储约 1.56 TB，其许可证要求月活跃用户超过 1 亿或月收入超过 2000 万美元的商业实体进行署名，而年收入超过 2000 万美元的 Model‑as‑a‑Service 业务则需与 Moonshot AI 另行签订协议。

rss · Simon Willison · Jul 27, 23:39

**背景**: 开放权重模型公开发布训练好的参数，使任何人都可以下载、运行或微调模型，但不一定包括训练代码等完整源码。传统的 MIT 许可证是一种宽松许可证，施加的限制极少，而 Moonshot AI 此前为 K2 模型修改了 MIT 许可证，增加了对月活跃用户超过 1 亿或月收入超过 2000 万美元的商业实体的署名要求。对于 Kimi K3，Moonshot 不再使用“修改后的 MIT”名称，而是推出了一种新许可证，对年收入超过 2000 万美元的 Model‑as‑a‑Service 业务要求签订单独协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3">China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits | Tom's Hardware</a></li>
<li><a href="https://amplifilabs.com/post/kimi-k3-the-complete-guide-to-moonshot-ais-2-8t-model">Kimi K3: The Complete Guide to Moonshot AI's 2.8T Model - Amplifi Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/MIT_License">MIT License - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoonshotAI`, `#Kimi-K3`, `#HuggingFace`, `#AI-models`

---

<a id="item-8"></a>
## [结算现代化指数揭示内部货币弹性的 S 曲线。](https://arxiv.org/abs/2607.22459) ⭐️ 8.0/10

该论文使用 1993 年至 2024 年间 24 个发达经济体的 809 项改革事件构建了结算现代化指数（SMI）。它记录了内部货币弹性的 S 曲线，转折点位于 SMI = 0.27 和 0.93，并通过 T2S 事件研究以及对瑞士 2021 年后 SDX 部署的合成控制分析展示了网络条件下的资产负债表效率。 该框架为基于分布式账本技术的结算升级提供了政策相关的预测，预测了 ECB 的 Pontes 计划以及英国和美国加入 Appia 可组合层所带来的效率提升。这些见解有助于监管机构和金融机构评估在批发支付中采用分布式账本技术的潜在资产负债表收益。 SMI 被分解为三个经济渠道和三个采纳阶段，在 T2S‑EMIR 事件研究中得到饱和度系数+0.557（p<0.01）。基于此，论文预测 Pontes 在 2027‑2032 年将带来+13.4%的效率恢复，如果英国和美国在 2028 年前加入 Appia 层，这一数字将上升至+37.5%，并指出原子结算的效率是双边对的属性，而非节点的属性。

rss · arXiv Quantitative Finance · Jul 27, 04:00

**背景**: 分布式账本技术（DLT）实现原子结算，这可以在批发支付系统中产生网络效应和资产负债表效率。内部货币弹性衡量私人银行创造的货币数量对经济状况或政策变化的响应程度。结算现代化指的是诸如实时总额结算（RTGS）系统和基于区块链的平台等升级，这些升级提升了跨境支付的速度、安全性和降低了成本。论文通过历史改革事件构建了纵向的结算现代化指数，以捕捉发达经济体中的这些变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.22459">Settlement Infrastructure, Inside Money Elasticity, and the Network...</a></li>
<li><a href="https://www.retailbankerinternational.com/tag/settlement-modernisation/">settlement modernisation Archives - Retail Banker International</a></li>

</ul>
</details>

**标签**: `#distributed ledger technology`, `#settlement systems`, `#financial infrastructure`, `#network economics`, `#inside money elasticity`

---

<a id="item-9"></a>
## [研究检测到 Solana Pump.fun 市场上的 1,012 个协同钱包队列](https://arxiv.org/abs/2607.02795) ⭐️ 8.0/10

该研究分析了 2026 年 6 月 12 日至 6 月 26 日期间 Solana pump.fun 上 166,098 次代币发行的 1,578,333 条买家观察数据，采用两阶段检测管道识别出 1,012 个持久钱包队列（每队列 2–12 个钱包），这些队列持续担任早期买家。相较于匹配发行，这些队列使前 30 分钟买家人数和 SOL 流入提升超过 130%。 揭示协同早期买家行为凸显了市场操纵如何在 Solana 的 pump.fun 上人为抬高初始代币价格，强调需要超越简单匹配的稳健因果推断方法来在 DeFi 生态中检测此类活动。 检测管道首先提取每次发行的首买窗口，随后构建跨发行的共现图并使用 union‑find 算法提取持久队列；最大队列由九个钱包组成，在 42 次发行中均出现在前十名买家之列，平均首买排名为 2.29。活动匹配的安慰剂估计得到更大的提升（+216.3%），表明观察到的关联受选择偏差驱动而非队列的因果影响。

rss · arXiv Quantitative Finance · Jul 27, 04:00

**背景**: Pump.fun 是基于 Solana 的 bonding‑curve 市场，代币价格随 SOL 支出而可预测上升，使早期买家能够以远低于最终市场价的成本获取代币。协同买家队列指的是一组钱包在代币发布后反复进行早期购买，可能影响早期价格动态。并查集（disjoint‑set）数据结构能够高效地将在众多集合中共同出现的元素分组，因而适用于从大规模共现图中检测持久的钱包群体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://j.tools/en/blog/pump-fun-bonding-curve-mechanics-explained">Pump . fun Bonding Curve Explained — Price, Graduation, Strategy</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/graph-data-structure-and-algorithms/">Graph Algorithms - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#DeFi`, `#market manipulation`, `#causal inference`, `#Solana`

---