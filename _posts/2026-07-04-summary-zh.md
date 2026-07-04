---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> From 56 items, 11 important content pieces were selected

---

1. [AMD MI355X 运行 GLM5.2 达 2626 tok/s/node，成本优势超过 Blackwell 2 倍](#item-1) ⭐️ 8.0/10
2. [Jamesob 发布本地运行最先进 LLM 的指南](#item-2) ⭐️ 8.0/10
3. [欧洲议会间谍软件调查委员会成员多次感染 Pegasus](#item-3) ⭐️ 8.0/10
4. [非洲人转向星链获取互联网接入](#item-4) ⭐️ 8.0/10
5. [Wordgard：来自 ProseMirror 创作者的浏览器内富文本编辑器](#item-5) ⭐️ 8.0/10
6. [PostgreSQL 与 OOM 杀手：为何使用严格内存过提交](#item-6) ⭐️ 8.0/10
7. [基准天花板：人类判断、评估稀缺与 AI 能力测量](#item-7) ⭐️ 8.0/10
8. [社交平台模态间的参与分配对电商表现的影响](#item-8) ⭐️ 8.0/10
9. [LLM 能以低成本准确提取历史车辆数据](#item-9) ⭐️ 8.0/10
10. [风险敏感专家路由提升 ETF 波动率预测](#item-10) ⭐️ 8.0/10
11. [未被选中的 Token：采样、状态与 AI 代理的随机性](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AMD MI355X 运行 GLM5.2 达 2626 tok/s/node，成本优势超过 Blackwell 2 倍](https://www.wafer.ai/blog/glm52-amd) ⭐️ 8.0/10

基准测试显示，AMD 的 MI355X 加速器在运行 GLM-5.2 模型时实现每节点 2626 token/秒，成本效益超过 Nvidia Blackwell 的两倍。 此结果凸显了 AMD 在 AI 推理硬件上的竞争力日益增强，为大规模 LLM 部署提供了比 Nvidia 最新 Blackwell 架构更具成本效益的替代方案。 基准测试在类似生产环境的批次大小下测量持续生成速度，且模型采用了量化形式（社区评论提到的 MXFP4），这可能导致一定精度损失。

hackernews · latchkey · Jul 3, 21:49 · [社区讨论](https://news.ycombinator.com/item?id=48780417)

**背景**: GLM-5.2 是来自 Z.ai 的 7440 亿参数开源大语言模型，具有 100 万 token 的上下文窗口，并采用 IndexShare 架构以提升长距离任务效率。AMD 的 Instinct MI355X 加速器是其最新的数据中心 GPU，专注于 AI 推理，宣称在每美元性能上优于竞争对手。Nvidia 的 Blackwell 架构于 2024 年发布，支撑 GB200 超级芯片，专为高吞吐 AI 工作负载优化，在此基准测试中作为性能基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://build.nvidia.com/z-ai/glm-5.2/modelcard">glm-5.2 Model by Z-ai | NVIDIA NIM</a></li>
<li><a href="https://au.finance.yahoo.com/news/amd-gains-nvidia-lisa-su-201608311.html">AMD gains on Nvidia? Lisa Su reveals new chips in heated AI...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者呼吁加入每瓦性能指标，以更好地评估 AMD 的效率，并指出从 FP8 到 MXFP4 量化时出现明显的精度下降，同时质疑实际价格和真实成本优势。还有人提到 Nvidia 即将发布的 Rubin 架构据说比 Blackwell 快五倍，并质疑所假设的 60% 缓存命中率和量化模型对吞吐量的贡献程度。

**标签**: `#AMD`, `#MI355X`, `#GLM5.2`, `#AI inference`, `#hardware benchmark`

---

<a id="item-2"></a>
## [Jamesob 发布本地运行最先进 LLM 的指南](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 在 GitHub 上发布了名为 local-llm 的指南，提供在本地运行最先进大语言模型的步骤，涵盖硬件、量化和成本考量。 该指南帮助从业者评估在个人硬件上部署前沿模型的可行性和权衡，为成本、性能和模型质量的决策提供参考。 指南提到的模型包括 Qwen 3.6‑27B、GLM‑5.2 和 DeepSeek V4‑Pro，讨论了 INT8、NVFP4 量化以及 REAP 剪枝等技术，并列出了从双 RTX 3090 到多卡 H200 的硬件方案，成本从几千到数万美元不等。

hackernews · livestyle · Jul 3, 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 在本地运行大语言模型需要足够的 GPU 显存和系统内存来存储模型权重，最先进的模型常常超过 100 GB，因此常通过量化来降低大小。INT8、INT4 以及混合精度格式（如 NVFP4）等技术可以在保持大部分能力的同时减小内存占用。消费级显卡如 RTX 4090（24 GB VRAM）或苹果统一内存（如 M5 MacBook Pro 48 GB）能够支持较小的量化模型，而更大的模型则需要多张高端数据中心 GPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48775921">Jamesob's guide to running SOTA LLMs locally | Hacker News</a></li>
<li><a href="https://deepintellica.com/ai-work/jamesob-s-guide-to-running-sota-llms-locally/">Jamesob's Guide To Running SOTA LLMs Locally - Deep Intellica</a></li>
<li><a href="https://medium.com/@gautsoni/llm-quantization-the-practical-guide-and-why-it-matters-for-inference-and-training-8668f4b91dcc">LLM Quantization: The Practical Guide (and Why It Matters for Inference and Training) | by gautam soni | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出顶级配置成本高昂（例如 4 万至 5.5 万美元的多卡 H200 方案），并建议理性预期，同时指出更实惠的方案如双 RTX 3090 可运行 Qwen 3.6‑27B 模型。还有人讨论了量化的权衡以及统一内存架构（如苹果 M5）作为折中方案的潜力。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#quantization`, `#AI`

---

<a id="item-3"></a>
## [欧洲议会间谍软件调查委员会成员多次感染 Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

根据 Citizen Lab 的法医分析，欧洲议会 PEGA 委员会调查间谍软件的成员在 2022 年 10 月 21 日左右以及 2023 年 3 月 6 日和 7 日两次成功感染了 Pegasus 间谍软件。 这一事件凸显了国家赞助的 Pegasus 行动的广泛渗透，引发了对欧盟立法机构安全的严重担忧。可能推动对间谍软件出口和使用的更严格监管和监督。 首次感染与先前针对俄罗斯和白俄罗斯语使用的流亡记者和活动家的 Pegasus 活动重叠，表明负责的客户有权在多个欧洲国家进行间谍活动。被入侵的设备可能暴露了机密个人医疗信息和敏感政府文件。

hackernews · ledoge · Jul 3, 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: Pegasus 是由以色列网络武器公司 NSO Group 开发的间谍软件，能够零点击地 covertly 安装在 iOS 和 Android 设备上，窃取数据并发送至 NSO 服务器。欧洲议会于 2022 年 3 月成立 PEGA 委员会（调查 Pegasus 和等效监视间谍软件的委员会），为期十二个月，任务是调查欧盟法律在间谍软件技术方面的所谓侵犯。该委员会的工作旨在约束间谍软件的滥用并制定相关标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus ( spyware ) - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/news/2021/jul/18/what-is-pegasus-spyware-and-how-does-it-hack-phones">What is Pegasus spyware and how does it hack... | The Guardian</a></li>
<li><a href="https://ijclinic.law.uci.edu/2023/01/25/the-european-parliaments-pega-committee-a-regional-effort-to-constrain-spyware-technology/">The European Parliament’s PEGA Committee: A Regional Effort to Constrain Spyware Technology – International Justice Clinic</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，第一次感染与之前针对俄罗斯和白俄罗斯语使用的流亡记者的活动重叠，暗示存在跨国授权的 Pegasus 客户。有人质疑欧洲议会是否有将工作和个人设备分离的政策，担心机密医疗和政府文件同时泄露。还有人提到希腊等欧盟成员国曾被指控滥用 Pegasus，导致以色列公司切断与某些国家的合作。

**标签**: `#Pegasus`, `#spyware`, `#European Parliament`, `#cybersecurity`, `#espionage`

---

<a id="item-4"></a>
## [非洲人转向星链获取互联网接入](https://www.economist.com/middle-east-and-africa/2026/07/02/africans-are-turning-to-starlink) ⭐️ 8.0/10

非洲人正越来越多地采用星链卫星互联网，以在缺乏传统宽带基础设施的地区获得连接，正如 2026 年 7 月《经济学人》文章所述。 这一趋势表明卫星星座可以让发展地区跳过传统有线基础设施，推动数字包容和经济机遇，类似于非洲移动电话的快速普及。 星链通过低地球轨道卫星网络、用户终端和地面站提供互联网服务，速度满足 FCC 宽带标准，月费约 55 美元，可由小型便携电池供电。

hackernews · bookofjoe · Jul 3, 21:08 · [社区讨论](https://news.ycombinator.com/item?id=48779977)

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，由数千颗低地球轨道（LEO）卫星组成，轨道高度在 160–2000 公里之间。LEO 星座相比传统地球同步卫星互联网具有更低延迟和更高吞吐量，通过星间链路和地面站进行通信。用户需要安装相控阵天线和调制解调器，将卫星信号转换为 Wi‑Fi 或以太网供终端设备使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Low_Earth_orbit">Low Earth orbit - Wikipedia</a></li>
<li><a href="https://www.aptiv.com/en/insights/article/what-is-a-leo-satellite">What Is a LEO Satellite?</a></li>
<li><a href="https://www.linkedin.com/pulse/guide-how-starlink-internet-works-patrick-mutabazi-rtr2e">A Guide to How Starlink Internet Works</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞星链为服务不足地区带来互联网，将其与非洲移动电话快速普及和美国农村连接挑战作类比，强调其便携性和可用小型电池供电的能力。同时也有提醒避免听起来像广告的声音，并分享了在偏远地区改善连接的个人经历。

**标签**: `#Starlink`, `#satellite internet`, `#Africa`, `#connectivity`, `#rural broadband`

---

<a id="item-5"></a>
## [Wordgard：来自 ProseMirror 创作者的浏览器内富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 是由 ProseMirror 作者 Marijn Haverbeke 创建的新一代浏览器内富文本编辑器，已发布 0.1 版本，并附有详细文档以及社区讨论，突出其与 ProseMirror 的相似之处和不同之处。 它为开发者提供了一个全新的 ProseMirror 替代方案，解决了诸如缺乏静态类型文档模型和 ProseMirror 基于步骤的变更系统复杂等痛点，可能影响未来富文本编辑器的选择。 Wordgard 的文档变更模型与 ProseMirror 的步骤模型不同，虽然复用了许多核心概念，但没有直接的升级路径，并且其架构受到 CodeMirror v6 重构的启发。

hackernews · indy · Jul 3, 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个 JavaScript 工具包，开发者通过定义 schema 并使用离散的事务步骤来构建自定义富文本编辑器。Wordgard 由同一作者在 ProseMirror 演进九年后推出，吸取了其中的经验并借鉴了 CodeMirror v6 重构的设计理念，以提供一种新的编辑模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://marijnhaverbeke.nl/blog/wordgard-0.1.html">Wordgard Release 0.1</a></li>
<li><a href="https://wordgard.net/docs/prosemirror/">Wordgard from ProseMirror</a></li>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了编辑器的设计，并对其与 ProseMirror 的相似之处感到兴奋，同时指出缺乏直接的升级路径以及对静态类型文档模型的需求。一些人表示 Wordgard 验证了他们自己的实验，还有人回顾了长期以来缺乏网页标准所见即所得编辑器的现状。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#JavaScript`, `#open-source`

---

<a id="item-6"></a>
## [PostgreSQL 与 OOM 杀手：为何使用严格内存过提交](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

文章解释说，将 vm.overcommit_memory=2 设置为严格内存过提交可以在内存压力下防止 Linux OOM 杀手终止 PostgreSQL 进程，这是基于 Ubicloud 的运营经验。 此指南帮助数据库管理员避免意外的 OOM 杀手终止，提高 PostgreSQL 稳定性并减少生产环境中的停机时间。 在 overcommit_mode=2 下，内核会拒绝导致超过提交限制的内存分配，导致 malloc 返回错误，PostgreSQL 能够妥善处理；而默认的启发式模式可能让 OOM 杀手将 PostgreSQL 选为牺牲目标。

hackernews · furkansahin · Jul 3, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: 当系统可用内存不足时，Linux OOM 杀手会根据进程的“坏分数”选择一个进程终止，以防止系统崩溃。内存过提交决定内核如何处理内存分配请求；模式 0 使用启发式判断，模式 1 始终允许过提交，模式 2 强制根据交换空间和过提交比率施加严格限制。PostgreSQL 经常通过 malloc 分配内存并依赖 fork 创建后台工作进程，因此意外的 OOM 终止可能导致操作中断或数据损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@msmkumar.eee/out-of-memory-oom-killer-in-linux-what-it-is-and-when-its-triggered-751cf7823de8">Out-Of-Memory ( OOM ) Killer in Linux: What It Is and When... | Medium</a></li>
<li><a href="https://dev.to/yugabyte/mirage-of-memory-part-3-overcommit-5g84">Mirage of memory, part 3: overcommit - DEV Community</a></li>
<li><a href="https://www.crunchydata.com/blog/deep-postgresql-thoughts-the-linux-assassin">Deep PostgreSQL Thoughts: The Linux Assassin | Crunchy Data Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Linux 默认内存设置在压力下可能导致问题，警告说严格过提交可能干扰分配大量虚拟内存的应用，并分享了将 PostgreSQL 与内存密集型工作负载结合使用后出现不稳定的经验，同时也同意在充分测试后该设置能提升数据库稳定性。

**标签**: `#PostgreSQL`, `#Linux memory management`, `#OOM killer`, `#system administration`, `#performance tuning`

---

<a id="item-7"></a>
## [基准天花板：人类判断、评估稀缺与 AI 能力测量](https://arxiv.org/abs/2607.01254) ⭐️ 8.0/10

论文提出基准天花板问题，表明随着 AI 模型在简单基准项上饱和，有效区分需要依赖稀缺的专家判断来处理难尾项。它提出了基准信号贬值的正式模型，利用 micro1 平台对超过一千名认证专业人士的数据记录了高判断评估劳动的稀缺溢价，并阐述了治理含义。 指出基准天花板揭示了当前 AI 评估方法的局限，凸显了对昂贵专家判断日益增长的需求，这影响着研究者、开发者和政策制定者。理解这一动态对于设计有效的基准和制定健全的 AI 治理政策至关重要。 正式模型将基准得分视为其精度取决于基准有效性的公开信号，表明有效信号集中在难尾项，且替代成本随前沿能力呈凸增长。基于 micro1 平台超过一千名认证专业人士的数据，作者量化了低可编码性、高判断评估劳动的稀缺溢价，并认为私人基准生产者在有效性上的投资低于社会最优水平。

rss · arXiv Quantitative Finance · Jul 3, 04:00

**背景**: AI 基准是衡量和比较模型能力的标准工具，但随着模型性能提升，它们常常达到现有测试套件的性能天花板，导致难以区分渐进的改进。当简单项被饱和时，剩余的区分力集中在需要顶尖专家判断来设计的难题上，而这种专家判断资源在结构上是稀缺的。这种稀缺导致政治经济学问题：私人 actors 在生产高质量基准项方面投资不足，相对于社会需求而言。论文将此框架为基准天花板问题，源于测量工具随时间的贬值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.01254">[2607.01254] The Benchmark Ceiling: Human Judgment, Evaluation Scarcity, and the Political Economy of AI Capability Measurement</a></li>
<li><a href="https://arxiv.org/html/2607.01254">The Benchmark Ceiling: Human Judgment, Evaluation Scarcity, and the Political Economy of AI Capability Measurement</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#benchmarking`, `#human judgment`, `#AI safety`, `#measurement theory`

---

<a id="item-8"></a>
## [社交平台模态间的参与分配对电商表现的影响](https://arxiv.org/abs/2503.09083) ⭐️ 8.0/10

该研究基于 2012 年至 2019 年约 2000 家美国在线零售商的面板数据，发现用户在五大主要社交平台上的参与度更加多元化与更高的网络销售额相关，这一提升来源于转化率和流量质量的改善，而不仅仅是参与总量的增加。 结果表明，参与在图像、视频和混合等内容模态之间的分配方式比仅仅在多个平台上存在更为重要，为营销人员在多渠道数字策略中优化投资回报提供了可操作的指导。 销售提升源于跨模态互补性——即在图像、视频和混合等异质格式之间分散参与能产生强化的品牌曝光——并且仅在平台间受众存在足够重叠时出现，而不仅仅取决于平台数量或总参与量。

rss · arXiv Quantitative Finance · Jul 3, 04:00

**背景**: 参与多元化是指企业将用户互动（如点赞、评论、分享）分散到多个社交媒体平台，而不是集中在单一渠道。面板数据分析通过追踪同一企业在不同时间点的表现，可以控制未观察到的异质性并评估因果关系。在数字营销中，不同平台侧重不同的内容模态——例如 Instagram 侧重图像，TikTok 侧重视频，Facebook 支持混合格式——因此在这些模态之间分配参与可以产生互补的品牌曝光，从而提升转化率和电子商务网站流量的质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://madoc.bib.uni-mannheim.de/60488/">Panel Data Analysis : A nontechnical introduction for marketing ...</a></li>
<li><a href="https://malaysiainfluencer.com/influencer-tips-pros-and-cons-of-managing-multiple-platforms">Influencer Tips : Pros and Cons of Managing Multiple Platforms</a></li>

</ul>
</details>

**标签**: `#social media marketing`, `#e-commerce`, `#engagement diversification`, `#conversion rate optimization`, `#panel data analysis`

---

<a id="item-9"></a>
## [LLM 能以低成本准确提取历史车辆数据](https://arxiv.org/abs/2505.11599) ⭐️ 8.0/10

该研究提出了一种多模态 LLM 流水线，用于从早期 20 世纪美国县级车辆登记表中提取结构化数据，实现 95.4% 的精确单元格匹配率，将解析错误从 61.4% 降至 0.35%，且成本仅为传统外包的约 1/50。 这项工作表明，LLM 可以取代昂贵的人工转录历史表格数据，使研究人员能够快速、廉价地构建大规模面板数据集，从而开启新的经济史分析。 该流水线对关联的数值单元格精确匹配率达到 96.7%，平均绝对百分比误差为 0.7%，在类别对齐方面与人类表现相当，且案例研究的回归结果在使用 LLM 提取数据与黄金标准数据时在统计上无显著差异。

rss · arXiv Quantitative Finance · Jul 3, 04:00

**背景**: 面板数据将多个实体（如县）在不同时间点的观察结合起来，使研究者能够研究诸如技术采纳之类的动态。历史表格常以图像形式扫描，包含宝贵的社会经济信息，但需要劳动密集型的转录才能使用。多模态 LLM 能够同时理解视觉布局和文本内容，从而在不依赖低级别 OCR 技能的情况下实现自动化提取，利用领域知识。这大幅减少了对专业标注员的依赖并显著降低了成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2505.11599">Can LLMs Credibly Transform the Creation of Panel Data from...</a></li>
<li><a href="https://novaresearch.unl.pt/en/publications/benchmarking-table-extraction-multimodal-llms-vs-traditional-ocr">Benchmarking Table Extraction : Multimodal LLMs vs Traditional OCR</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#historical data digitization`, `#panel data`, `#multimodal models`, `#data extraction`

---

<a id="item-10"></a>
## [风险敏感专家路由提升 ETF 波动率预测](https://arxiv.org/abs/2604.10402) ⭐️ 8.0/10

本文提出了一种风险敏感专家路由框架，通过状态依赖的门控机制结合多个波动率预测器，以适应平静和压力市场状态。实验结果表明，相对于滚动最佳基线，高波动率预测损失降低约 24%，欠预测损失降低约 22%。 通过明确建模依赖于市场状态的性能，该方法为改善 ETF 的波动率预测提供了实际途径，从而提升金融市场的风险管理和交易决策。此外，它展示了如何将在线风险敏感评估与门控机制结合，构建自适应预测系统。 该框架在六只 ETF 的日度面板上采用滚动走前验证进行评估，结果显示最强预测器在平静和压力状态下会变化。它使用在线风险敏感评估和状态依赖门控来结合专家预测器，从而实现了所述的损失降低。

rss · arXiv Quantitative Finance · Jul 3, 04:00

**背景**: 波动率预测旨在预测资产收益的未来波动性，但市场条件的变化会导致模型在不同状态下的表现不一。专家路由通过门控机制根据可观测状态选择或加权多个专家模型。风险敏感评估优化的是非对称损失偏好而非平均误差，这在金融应用中尤为重要，因为预测偏低或偏高的成本不同。交易所交易基金（ETF）提供对底层指数的流动性、多样化敞口，其波动率是投资组合构建和风险管理的重要输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.10402v3">Risk - Sensitive Specialist Routing for Volatility Forecasting</a></li>
<li><a href="https://arxiv.org/html/2604.10402v2">Regime-Aware Specialist Routing for Volatility Forecasting</a></li>
<li><a href="https://www.preprints.org/manuscript/202509.0997">Volatility Forecasting Using GARCH Models in... | Preprints.org</a></li>

</ul>
</details>

**标签**: `#volatility forecasting`, `#specialist routing`, `#risk-sensitive learning`, `#ETF`, `#time series analysis`

---

<a id="item-11"></a>
## [未被选中的 Token：采样、状态与 AI 代理的随机性](https://arxiv.org/abs/2606.08998) ⭐️ 8.0/10

该论文（arXiv:2606.08998v3）分析了基础模型中 token 采样的随机性如何传播导致不同的计划、工具调用和代理状态，并将内在的 token 采样随机性与外在因素（如环境变化和服务基础设施）区分开来。 理解这些变异来源对于提升具象 AI 系统的可重复性和可靠性至关重要，有助于开发者判断何时确定性设置足够，何时需要额外控制措施。 它指出内在变异来源于下一个 token 概率的伪随机采样，可能导致不同的行为级联；外在变异则来自环境变化、实时数据、批次效应和数值细节；此外，研究还强调即使是确定性执行也无法保证在实际部署中行为完全相同。

rss · arXiv Quantitative Finance · Jul 3, 04:00

**背景**: 具象 AI 系统通常以基础模型为核心，模型在编排循环中负责规划、调用工具、观察结果并更新状态。在每个时间步，模型先计算各 token 的得分，再转换为概率，最后通过伪随机数生成器采样下一个 token，这一过程引入了内在随机性。微小的采样差异可能在编排循环中被放大，导致不同的计划、工具调用或代理状态。此外，环境变化、实时数据、服务基础设施和数值精度等外在因素也会加剧系统的可观测变异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.08998v3">The Token Not Taken: Sampling , State, and the Stochasticity of AI...</a></li>
<li><a href="https://medium.com/@chitrakumarsai/token-sampling-methods-temperature-to-heat-things-up-af0c1e36dafc">Token Sampling Methods — Temperature to heat things up. | Medium</a></li>
<li><a href="https://mindra.co/blog/human-in-the-loop-ai-orchestration-when-agents-should-ask-for-help">Human-in-the- Loop AI Orchestration : When Your Agents Should Ask...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Foundation Models`, `#Token Sampling`, `#Stochastic Behavior`, `#Reproducibility`

---