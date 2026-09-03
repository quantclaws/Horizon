---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> From 41 items, 15 important content pieces were selected

---

1. [Polars 发布 py-2.0.0-rc.1，默认使用流式 SQL 引擎并提升性能](#item-1) ⭐️ 9.0/10
2. [可扩展的百万级多项 Probit 选择概率反演算法](#item-2) ⭐️ 9.0/10
3. [Meta 发布 Muse Spark 1.3，成本低廉且基准表现强劲的 LLM](#item-3) ⭐️ 8.0/10
4. [谷歌 DeepMind 发布 Gemini 3.8 Flash 及 Flash Cyber 模型。](#item-4) ⭐️ 8.0/10
5. [谷歌避免被迫拆分其广告技术业务](#item-5) ⭐️ 8.0/10
6. [三个网站生成超 21.5 万篇 AI 生成的“最佳软件”页面被 Perplexity 引用](#item-6) ⭐️ 8.0/10
7. [Mistral AI 的训练数据退出选项在 Hacker News 引发隐私争议](#item-7) ⭐️ 8.0/10
8. [Paint.NET 加入 AI 生成的 Direct2D 重写以支持 WINE。](#item-8) ⭐️ 8.0/10
9. [定价 DeFi 尾部风险：协议还是存款人定价操作风险？](#item-9) ⭐️ 8.0/10
10. [AI 作为资本、劳动、通用技术和基础设施的经济分析。](#item-10) ⭐️ 8.0/10
11. [代理经验资产定价：LLM 驱动的因子发现框架](#item-11) ⭐️ 8.0/10
12. [个性化算法建议稳定了古诺竞争，有偏建议促成默契串通](#item-12) ⭐️ 8.0/10
13. [基于仿射 Volterra 过程的带跳二次 BSDE 的显式解](#item-13) ⭐️ 8.0/10
14. [直接空气捕集在欧洲 2050 能源系统中的整合、存储与成本驱动因素](#item-14) ⭐️ 8.0/10
15. [燃油价格冲击揭示中美城市流动性适应的不平等](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Polars 发布 py-2.0.0-rc.1，默认使用流式 SQL 引擎并提升性能](https://github.com/pola-rs/polars/releases/tag/py-2.0.0-rc.1) ⭐️ 9.0/10

Polars 发布了 py-2.0.0-rc.1，将 SQL 默认引擎切换为流式引擎，并带来了诸如 Iceberg sink 复用原生元数据、SQL EXISTS 谓词下推以及将原始 group-by 聚合收集到单个 chunk 等性能提升。 此次 2.0 大版本引入了破坏性变更和显著的性能提升，使得 Polars 能够处理超出内存的数据集并更好地支持 Iceberg 等湖屋格式，对依赖 Polars 进行快速分析的数据工程师和分析师具有重要影响。 关键变更包括将流式引擎设为 SQL 默认（#28973）、在 Iceberg sink 中复用原生元数据（#29062）、在子查询之前下推 SQL EXISTS 谓词（#29078）以及将原始 group-by 聚合合并到单个 chunk（#28825）。

github · github-actions[bot] · Sep 2, 11:49

**背景**: Polars 是一种基于 Rust 的 DataFrame 库，提供即时和延迟两种 API，其流式引擎能够通过流水线方式处理大于内存的数据集。Iceberg 是一种用于大规模分析数据的开放表格式，Polars 支持读写 Iceberg 表，并可复用元数据以提升 sink 性能。谓词下推是一种查询优化技术，尽可能早地应用过滤条件以减少扫描的数据量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pola.rs/user-guide/concepts/streaming/">Streaming - Polars user guide</a></li>
<li><a href="https://docs.pola.rs/api/python/stable/reference/api/polars.scan_iceberg.html">polars.scan_iceberg — Polars documentation</a></li>
<li><a href="https://pola.rs/posts/predicate-pushdown-query-optimizer/">Polars — The power of predicate pushdown</a></li>

</ul>
</details>

**标签**: `#Polars`, `#Python`, `#DataFrame`, `#Release`, `#Performance`

---

<a id="item-2"></a>
## [可扩展的百万级多项 Probit 选择概率反演算法](https://arxiv.org/abs/2609.01133) ⭐️ 9.0/10

该论文提出了一种可扩展的多项 Probit 选择概率反演方法，可处理多达一百万个备选项，实现高精度且线性运行时间，远超传统的 GHK 模拟器。 这一进展使相关离散选择模型在现代数据规模下成为可能，可在机器学习、经济学和营销等大规模应用中使用，此时 logit 模型不足。 该方法利用因子、块和层次协方差结构的语法，实现线性时间计算，而 GHK 模拟器的成本大约随 n^2.8 增长，且在极端尾部概率下仍保持高精度。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 多项 Probit 模型将选择概率表示为高斯正交积分，缺乏封闭形式解，传统上通过模拟计算。Geweke‑Hajivassiliou‑Keane（GHK）模拟器是标准的重要性抽样方法，但其计算成本随备选项数量的增长呈超线性趋势。对于因子、块和层次协方差结构所属的某些语法，这些积分可以通过解析或快速的确定性方法计算，从而实现可扩展的反演。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GHK_algorithm">GHK algorithm - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/254324145_Analytic_approximations_for_computing_probit_choice_probabilities">(PDF) Analytic approximations for computing probit choice ...</a></li>
<li><a href="https://hal.science/hal-01289126/document">Estimating orthant probabilities of high dimensional Gaussian vectors...</a></li>

</ul>
</details>

**标签**: `#multinomial probit`, `#discrete choice modeling`, `#scalable inference`, `#GHk simulator`, `#choice probability inversion`

---

<a id="item-3"></a>
## [Meta 发布 Muse Spark 1.3，成本低廉且基准表现强劲的 LLM](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 宣布发布 Muse Spark 1.3，这是其 Muse Spark 大语言模型系列的最新版本，具备增强的代理任务推理能力和改进的真实世界可用性。 该模型在基准测试中表现出显著提升（例如 GDPval‑AA v2 +94 Elo，Tau3‑Bench Banking +12 分），同时保持低成本，表明正朝着高性能低成本的大语言模型方向发展，有助于开发者更广泛地使用。 Muse Spark 1.3 的 xhigh 和 max 版本在 Artificial Analysis Intelligence Index 上相较于 1.2 有所提升，代理评估中的 Elo 提升最高达 +139，并展示了更好的上下文跟踪、冲突处理以及主动请求输入的能力。

hackernews · bvaldivielso · Sep 2, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**背景**: Meta 的 Muse Spark 系列是一组旨在平衡性能与成本的大语言模型，面向需要强大能力但又不愿承担前沿模型高昂费用的开发者。早期版本如 Muse Spark 1.2 以低价和不错的通用任务表现著称。Muse Spark 1.3 引入了‘最大推理’模式，专注于具挑战性的推理和代理任务，同时保持上下文跟踪和处理模糊输入的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-spark-1-3">Introducing Muse Spark 1.3 | Meta AI Research</a></li>
<li><a href="https://developer.meta.com/ai/models/muse-spark/">Muse Spark 1.3 | Meta</a></li>
<li><a href="https://artificialanalysis.ai/articles/muse-spark-1-3">Muse Spark 1.3: Meta reaches the frontier | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了该模型的低廉成本，指出生成一个骑自行车的鹈鹕 SVG 仅需几分钱，并且输出质量明显优于 1.2 版。一些用户赞赏其透明的定价方式，使训练数据的价值变得明确；另一些人则指出其在基准测试中的高分（如 DeepSWE 75.4）以及由此带来的对竞争对手的价格压力。

**标签**: `#AI`, `#LLM`, `#Meta`, `#Muse Spark`, `#model release`

---

<a id="item-4"></a>
## [谷歌 DeepMind 发布 Gemini 3.8 Flash 及 Flash Cyber 模型。](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

谷歌 DeepMind 发布了 Gemini 3.8 Flash 和 Gemini 3.8 Flash Cyber，这是速度快的多模态 AI 模型，在与更大模型的基准测试中表现竞争力强，且擅长 HTML/JavaScript 生成。该模型在一天前通过 Google 博客和 DeepMind 模型卡公布。 此次发布之所以重要，是因为 Gemini 3.8 Flash 的智能得分与 Opus 5 medium 相当，同时作为低成本闪电模型，在代理工作流和软件工程中提供强大性能。此外，专门的 Gemini 3.8 Flash Cyber 变体在以更低成本实现更高漏洞发现召回率方面表现出色，吸引了开发者和安全研究人员。 Gemini 3.8 Flash 支持文本、图像、音频和视频输入，具备可配置的努力级别以平衡质量、成本和延迟，并保持与 3.7 Flash 系列相同的低价。Cyber 变体在内部渗透测试基准上实现了+7.5‑9.7%的更高召回率，而成本仅为其他前沿模型的 2.3‑5.2 倍。

hackernews · bratao · Sep 2, 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**背景**: Gemini 是由 Google DeepMind 开发的一系列多模态大语言模型，继承了 LaMDA 和 PaLM 2，并于 2023 年 12 月 6 日宣布。Flash 系列专为快速、低成本推理而设计，同时保持强大能力，早期版本如 Gemini 3.7 Flash 已在编码和代理任务中受到好评。Gemini 3.8 Flash 在其前身基础上提供了软件工程和代理知识工作流的性能提升，并引入了专注于自主漏洞发现和补丁生成的专门 Cyber 变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3 . 8 Flash and 3 . 8 Flash Cyber</a></li>
<li><a href="https://www.datacamp.com/blog/gemini-3-8-flash-cyber">Gemini 3 . 8 Flash : Features, Benchmarks, and Pricing | DataCamp</a></li>

</ul>
</details>

**社区讨论**: 社区反应强调了人们对模型速度、低成本以及强大 HTML/JavaScript 生成能力的兴奋，用户指出相较于 Gemini 3.7，在真实世界知识、行程规划、照片排名和文档解析方面有所改进。有人注意到相比 3.7 某些任务的成本略有增加，而其他人则称赞其多模态能力以及 Cyber 变体在漏洞发现方面相较其他前沿模型的出色表现。

**标签**: `#Gemini`, `#LLM`, `#Google DeepMind`, `#AI models`, `#Flash model`

---

<a id="item-5"></a>
## [谷歌避免被迫拆分其广告技术业务](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 8.0/10

谷歌击败了美国政府强制其出售广告技术业务的尝试，在法院认定其在该市场具有垄断地位后避免了结构性补救措施。 此决定保留了谷歌在数字广告领域的主导地位，表明反垄断执法面临限制，并将影响依赖广告技术生态系统的竞争对手、广告商和出版商。 法院认定谷歌的广告技术业务为垄断，但接受了行为补救措施而非强制剥离，指出该业务去年收入约 300 亿美元，约占 Alphabet 总收入的 8%。

hackernews · donohoe · Sep 2, 14:46 · [社区讨论](https://news.ycombinator.com/item?id=49537131)

**背景**: 广告技术（ad tech）指促进在线广告买卖和投放的技术和服务，包括广告服务器、交易所和数据平台。谷歌的广告技术堆栈包括 Google Ad Manager、AdSense 和 AdMob 等产品，这些共同贡献了 Alphabet 可观的广告收入。监管机构长期审查此类一体化平台是否通过偏向自身服务而抑制竞争。

**社区讨论**: 评论者就“广告技术”的含义展开讨论，指出虽然谷歌的广告技术收入仅占利润的一小部分，但其整体广告收入主导了 Alphabet 的收入。有人主张更强的结构性补救措施，也有人提出渐进式税收或简化合并撤销以遏制垄断力量。

**标签**: `#antitrust`, `#Google`, `#ad tech`, `#monopoly`, `#legal`

---

<a id="item-6"></a>
## [三个网站生成超 21.5 万篇 AI 生成的“最佳软件”页面被 Perplexity 引用](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

调查发现，三个网站生成了超过 215,128 个 AI 生成的“最佳软件”推荐页面，Perplexity 的 AI 在其回答中将这些页面作为来源引用。 这表明 AI 生成的 SEO 垃圾内容能够污染 LLM 的检索增强生成管道，导致幻觉推荐并削弱对 AI 驱动搜索的信任。 这些页面由三个网站生成，共计 215,128 条，旨在纯粹影响 AI 向量数据库而非人类读者；Perplexity 的引用系统将它们呈现为权威来源。

hackernews · jakobgreenfeld · Sep 2, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**背景**: 大型语言模型可能会产生幻觉，在其检索增强生成依赖受污染的数据时，会生成看似合理但实际不实的信息。Perplexity 通过检索‑排名‑生成的三阶段管道引用来源，抓取在相关性信号上得分高的网页。AI 生成的 SEO 垃圾内容会大规模产出低质量页面，专门为了操纵这些相关性信号并污染 LLM 使用的向量数据库。此次调查表明此类垃圾内容可能被当作事实引用，凸显了加强来源过滤的必要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloro.dev/perplexity/sources/">Perplexity Citations API — Sources & Citation Pills in JSON</a></li>
<li><a href="https://www.iloveseo.net/spam-in-the-age-of-ai-search/">Spam in the age of AI Search - I Love SEO</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，LLMs 往往倾向于偏好自身生成的文本而非人类撰写的内容，且 AI 生成的 SEO 页面可能被误认为是事实。还有人指出，通过操纵模型的思维链风格可以偏置其推荐，而另一些人则批评 Perplexity 为了速度牺牲质量，导致引用不可靠。

**标签**: `#AI`, `#misinformation`, `#LLMs`, `#SEO spam`, `#Perplexity`

---

<a id="item-7"></a>
## [Mistral AI 的训练数据退出选项在 Hacker News 引发隐私争议](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) ⭐️ 8.0/10

Hacker News 上的一篇帖子讨论了 Mistral AI 关于使用用户输入和输出数据进行模型训练的选择加入/退出设置，指出 Team 层级已被改为默认选择加入，用户分享了他们的体验和担忧。 此次讨论凸显了用户对 AI 厂商数据同意方式日益增长的不安，这可能影响整个行业对大语言模型服务的信任和采用。 根据 Mistral 帮助中心的说明，输入和输出数据默认用于训练，除非用户在管理面板的 Vibe > Privacy 中关闭相关开关；Team 层级最近被改为默认选择加入，免费的 Experiment 层级同样默认选择加入。

hackernews · teekert · Sep 2, 12:30 · [社区讨论](https://news.ycombinator.com/item?id=49535284)

**背景**: 许多大型语言模型通过使用用户交互数据进行训练来提升性能，但隐私法规和用户期望日益要求提供明确的退出机制。作为欧洲的 AI 提供商，Mistral 提供可配置的数据使用设置以符合类似 GDPR 的期望，尽管其不同服务层级的具体退出流程有所不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training">Can I opt out of my input or output data being used for training? | Mistral Help Center</a></li>
<li><a href="https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models">Do you use my user data to train your Artificial Intelligence models? | Mistral Help Center</a></li>
<li><a href="https://meetily.ai/llm-privacy/mistral">Mistral La Plateforme Data Retention Policy 2026 - Does Mistral Train on Your Data? | Meetily</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些用户愿意分享代码库和日志以帮助模型改进，而另一些则持怀疑态度，指出厂商往往不管同意与否都会使用数据进行训练，并批评默认选择加入的政策不可信赖。

**标签**: `#AI privacy`, `#data usage`, `#Mistral`, `#opt-out`, `#LLM training`

---

<a id="item-8"></a>
## [Paint.NET 加入 AI 生成的 Direct2D 重写以支持 WINE。](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET 现在包含一个由 AI 编写的、从零开始的干净室逆向工程 Direct2D 实现，通过 /wine 标志激活以在 WINE 上运行。该实现由 Claude 生成，约有 180,000 行代码。 这一成就展示了大型语言模型在巨大软件工程任务中的辅助潜力，可能降低跨平台兼容性的门槛。同时，它引发了关于代码质量、干净室逆向工程的合法性以及对 AI 生成代码信任的讨论。 该 Direct2D 重写位于 PaintDotNet.Windows.Direct2D1.Managed.dll 中，且未经过广泛人工审查，被称为 'vibe coding'。Rick Brewster 提到他需要监督 Claude 以确保资源管理和 COM 引用计数的正确性。

rss · Simon Willison · Sep 2, 05:50

**背景**: Direct2D 是微软在 Windows Vista 及以后版本中引入的二维图形 API，用于高性能渲染。WINE 是一个兼容层，使得 Windows 应用程序能够在类 Unix 系统上运行，但正确实现 Direct2D 一直是主要障碍。干净室逆向工程是指在不访问原始源代码的情况下，通过观察行为重新创建规范，以避免版权侵权。在这里，AI 模型 Claude 生成了大约 180,000 行 Direct2D 兼容代码，Paint.NET 现在通过 /wine 标志使用它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/direct2d/direct2d-overview">About Direct2D - Win32 apps | Microsoft Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI-generated code`, `#Direct2D`, `#WINE`, `#Paint.NET`, `#reverse engineering`

---

<a id="item-9"></a>
## [定价 DeFi 尾部风险：协议还是存款人定价操作风险？](https://arxiv.org/abs/2609.00911) ⭐️ 8.0/10

该论文使用新的事件数据集和巴塞尔损失分布方法量化了 DeFi 各部门的操作风险尾部，发现 Bridge、衍生品和其他部门表现出超过无限均值边界的重尾（尾指数估计约 1.6），而贷款部门在 VaR99.9 下需要相当于总价值锁定（TVL）18%的资本缓冲，但十大贷款平台平均仅持有约 5%的该缓冲。 结果表明，许多 DeFi 协议相对于其对存款人施加的尾部风险而言资本不足，意味着无法评估隐藏风险的零售用户承担了大部分损失，而仅靠市场纪律（约 125 个基点的利差）无法充分定价该风险。 研究按部门建模操作风险损失分布，估计 Bridge、衍生品和其他部门的尾指数ξ约为 1.6，超过ξ=1 的无限均值阈值，将其与 Moscadelli 银行业区间[0.85,1.39]比较，计算出贷款部门在 VaR99.9 下需 TVL 的 18%作为资本缓冲，而最大平台平均仅持有约 5%，并且无缓冲平台的中位数收益溢价为 125 个基点。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 在金融监管中，巴塞尔损失分布方法（LDA）通过结合损失频率和严重程度分布来估算操作风险所需的资本，是巴塞尔 II 高级计量方法的核心。重尾分布用尾指数ξ描述，当ξ>1 时分布的均值为无限，意味着极端损失可能对期望损失产生主导影响。Moscadelli 银行业给出了传统银行操作风险尾指数的经验范围[0.85,1.39]，作为评估 DeFi 部门尾部风险的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_measurement_approach">Advanced measurement approach - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heavy-tailed_distribution">Heavy - tailed distribution - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2609.00911">Pricing the DeFi Tail: Do Protocols or Depositors Price ...</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#operational risk`, `#risk management`, `#blockchain finance`, `#capital buffers`

---

<a id="item-10"></a>
## [AI 作为资本、劳动、通用技术和基础设施的经济分析。](https://arxiv.org/abs/2609.01263) ⭐️ 8.0/10

这篇 arXiv 论文（2609.01263v1）认为 AI 同时具有资本、合成劳动、通用技术和经济基础设施的属性，并探讨了其对生产率、就业、市场结构和福利的影响。 通过从多种经济视角审视 AI，该论文提供了一个统一框架，帮助研究者和政策制定者预见 AI 的广泛影响，并制定政策以最大化收益并减轻潜在危害。 它详细说明了 AI 通过自动化、增强、优化、预测和创新推动生产率，同时通过替代、互补和创造性毁灭重塑劳动，并分析了其对竞争、市场集中、创业以及消费者、生产者、工人、政府和社会福利的影响。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 人工智能可以被视为一种资本形式，因为它蕴含了能够提升未来生产的积累知识；当 AI 系统自主执行认知或体力任务以创造经济价值时，它也相当于合成劳动。作为通用技术，AI 类似于蒸汽机或电力等过去的创新，能够通过改善广泛的工艺来转变整个经济。此外，将 AI 视为经济基础设施强调其降低交易成本、在各部门扩散能力以及实现新数字服务的作用，这与宽带或电信网络的功能类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://khullani.medium.com/synthetic-labor-agents-and-the-workforce-of-the-future-bb02ab70528c">Synthetic Labor: Agents and the Workforce of the Future | by Khullani M. Abdullahi | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/General-purpose_technology">General-purpose technology - Wikipedia</a></li>
<li><a href="https://www.weforum.org/stories/geo-economics-and-politics/ai-infrastructure-critical-infrastructure/">It’s time to start treating AI infrastructure as critical infrastructure | World Economic Forum</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#productivity`, `#labor markets`, `#general-purpose technology`, `#public policy`

---

<a id="item-11"></a>
## [代理经验资产定价：LLM 驱动的因子发现框架](https://arxiv.org/abs/2609.00731) ⭐️ 8.0/10

该论文定义了代理经验资产定价（AEAP）作为 LLM 代理自主完成金融领域完整科学发现循环的范式。它提出了参考架构、评估标准，并测试了原型系统 SEADS 在两个美国股票面板上相较于五个基线的自动因子发现表现。 AEAP 将评估重点从仅回测因子输出转向评估发现系统自身，提供了自主金融研究的严格框架。这有望加速因子创新并将人工智能进步与量化金融实践结合。 SEADS 与五个重新实现的基线进行了比较；没有单一指标能一致地对系统排名，因而需要多轴评估。通过滚动重新执行评估发现过程本身（而不仅是静态因子）的可靠性，论文还报告了负面结果和局限性，指出未来评估中的进一步陷阱。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 大型语言模型（LLM）代理能够生成假设、形式化并评估结果，从而实现自主科学发现。在资产定价领域，研究者传统上通过在历史数据上回测交易策略来发现因子，但这常常忽略因子是如何被发现的。样本外测试通过在未见数据上评估策略来防止过拟合，论文将此做法扩展到了发现系统自身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.00731">Agentic Empirical Asset Pricing: Methodological Foundations</a></li>
<li><a href="https://commonplace.workforcefutures.net/paper/arxiv:2609.00731">Agentic Empirical Asset Pricing: Methodological Foundations ...</a></li>
<li><a href="https://quant.stackexchange.com/questions/50806/backtest-overfitting-in-sample-vs-out-of-sample">backtesting - Backtest overfitting - in-sample vs out - of - sample ...</a></li>

</ul>
</details>

**标签**: `#asset pricing`, `#LLM agents`, `#factor discovery`, `#empirical finance`, `#AI for finance`

---

<a id="item-12"></a>
## [个性化算法建议稳定了古诺竞争，有偏建议促成默契串通](https://arxiv.org/abs/2511.09454) ⭐️ 8.0/10

在 129 名参与者进行的古诺数量博弈实验中，个性化均衡一致的建议导致向纳什均衡稳定收敛，而战略性偏向的向下建议导致持续的产出不足和超额利润，表明存在默契串通。 研究表明，算法建议可以充当战略信号，在没有明确沟通的情况下促进协调，这引发了对算法串通的担忧，并凸显了在竞争性市场中对 AI 决策支持工具进行谨慎设计和监管的必要性。 获得个性化建议的参与者收敛到均衡产量的速度更快、更一致，而偏向的建议是向下偏移的，导致产出低于竞争基准且利润更高。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 古诺竞争是一种寡头垄断模型，企业同时选择产量，从而达到纳什均衡，此时任何单方面改变产量都不会增加利润。默契串通是指企业在没有明确沟通的情况下，通过间接协调产量或定价来减少产出并提高价格。本研究考察了算法建议如何作为战略信号影响这些动态，既能稳定均衡也能维持串通结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cournot_competition">Cournot competition - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tacit_collusion">Tacit collusion - Wikipedia</a></li>

</ul>
</details>

**标签**: `#algorithmic advice`, `#Cournot competition`, `#tacit collusion`, `#behavioral economics`, `#human-AI interaction`

---

<a id="item-13"></a>
## [基于仿射 Volterra 过程的带跳二次 BSDE 的显式解](https://arxiv.org/abs/2604.01300) ⭐️ 8.0/10

作者通过将带跳的二次 BSDE 与仿射 Volterra 过程耦合的问题归约为含有 Lévy 跳补偿项的积分 Riccati-Volterra 常微分方程，获得显式解，并将其应用于跳扩散、非马尔可夫环境下的连续时间 Markowitz 均值-方差组合选择问题。 该工作为在非鞅、非马尔可夫市场中求解带跳的二次后向随机微分方程提供了可解析处理的框架，从而得到均值-方差投资组合问题的闭式最优策略和有效前沿，填补了经典随机控制失效的空白。它连接了随机分析、Volterra 理论和数理金融，为建模粗糙波动和跳跃效应提供了新工具。 该约化产生一组广义非齐次积分 Riccati-Volterra 常微分方程，求解后可得到显式的最优反馈控制和均值-方差有效前沿；最优价值函数则通过相关的 Riccati BSDEJ 的解表示。在二维假平稳粗糙 Heston 模型上的数值实验展示了稳定粗糙波动率对 Markowitz 资产配置的影响。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 带跳的二次后向随机微分方程（BSDE）在随机控制和金融中常见，其生成器关于控制变量呈二次增长，且驱动噪声包含泊松随机测度。仿射 Volterra 过程是由具有仿射系数的随机卷积方程定义的解，通常既不是鞅过程也不是马尔可夫过程，因而能够刻画具有粗糙性和记忆依赖的波动。积分 Riccati-Volterra 常微分方程在这些 Volterra 系统的线性二次控制中出现，可通过不动点定理求解或研究，为获得显式的 BSDE 解提供了一条可行途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1708.08796">[1708.08796] Affine Volterra processes - arXiv.org AFFINE VOLTERRA PROCESSES - JSTOR Affine Volterra processes - Project Euclid Affine Volterra processes with jumps - ScienceDirect Affine Volterra processes with jumps - arXiv.org (PDF) Affine Volterra processes - ResearchGate Affine Volterra processes - Institut Polytechnique de Paris</a></li>
<li><a href="https://arxiv.org/abs/1911.01903">[1911.01903] Integral operator Riccati equations arising in ... Integral Operator Riccati Equations Arising in Stochastic ... On the convergence of collocation methods for Volterra ... Integral operator Riccati equations arising in stochastic ... Integral Operator Riccati Equations Arising in Stochastic ... Integral operator Riccati equations arising in stochastic ... On the convergence of collocation methods for Volterra ...</a></li>
<li><a href="https://theses.hal.science/tel-02886647/document">Contributions to quadratic backward stochastic differential equations...</a></li>

</ul>
</details>

**标签**: `#BSDE`, `#stochastic control`, `#Volterra processes`, `#mathematical finance`, `#jump-diffusion`

---

<a id="item-14"></a>
## [直接空气捕集在欧洲 2050 能源系统中的整合、存储与成本驱动因素](https://arxiv.org/abs/2604.05990) ⭐️ 8.0/10

该研究将直接空气碳捕集与封存（DACCS）纳入欧洲完全脱碳电力系统的 2050 年容量扩张模型，分析了 CO₂储存可用性（仅北海海上储存地点 vs 全欧洲分布）以及系统整合方式（孤立、完全整合、回溯添加）对总系统成本的影响。 研究发现，将 CO₂储存限制在北海地点会使捕获成本上升约 10%，而将 DACCS 视为独立技术（未整合）则会使成本增加高达 30%，凸显了储存地理位置和系统整合对欧洲实现净零目标的成本效益的重要性。 论文将捕集、运输和储存分离建模，使用容量扩张模型比较了三种整合方案（完全孤立、完全整合、回溯添加），并得出储存位置和整合程度对成本的敏感性定量结果。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 直接空气碳捕集与封存（DACCS）从环境空气中直接提取二氧化碳并进行长期储存，为减少难以抵消的排放提供了一条途径。容量扩张模型是一种优化工具，用于在政策约束下确定满足未来需求所需的发电、储存和输电投资组合，并已被用于描绘欧洲到 2050 年实现完全脱碳的电力系统。该研究将 DACCS 纳入此类模型，以评估储存可用性和电力系统交互如何影响净零欧洲的总系统成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct_air_capture">Direct air capture - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_energy_system_models">Open energy system models - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/373172609_Energy_System_2050_-_Towards_a_decarbonised_Europe">(PDF) Energy System 2050 - Towards a decarbonised Europe</a></li>

</ul>
</details>

**标签**: `#Direct Air Capture`, `#DACCS`, `#Energy System Modeling`, `#Carbon Storage`, `#Europe 2050`

---

<a id="item-15"></a>
## [燃油价格冲击揭示中美城市流动性适应的不平等](https://arxiv.org/abs/2608.12281) ⭐️ 8.0/10

研究利用 2026 年美伊油价冲击作为自然实验，对中国和美国 12.2 万个社区的 1.7 万亿次兴趣点访问数据应用分层面板回归中断设计。结果显示，近四分之三的社区出行范围下降，但应对方式因冲击前的城市条件而异。 该研究表明燃油价格冲击充当城市压力测试，揭示了流动性适应的不平等，为公平的交通政策和规划提供依据。相似的出行结果可能源于不同的适应或受限过程，有助于制定精准干预措施。 该研究使用分层面板回归中断设计，以到达冲击阈值的距离作为连续运行变量来估计因果效应。能源密集型出行暴露解释了异质性的最大部分，而更长的基线出行加剧了收缩，汽车依赖程度越高则调整空间越小。

rss · arXiv Quantitative Finance · Sep 2, 04:00

**背景**: 回归中断设计（RDD）是一种准实验方法，通过利用运行变量中的截止点来估计处理效应。兴趣点（POI）数据记录对特定地点的访问，越来越多地用于衡量人类流动性模式。诸如 2026 年美伊油价冲击之类的燃油价格冲击提供了旅行成本的外生变化，可作为自然实验来研究行为反应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2309.01404v3">Hierarchical Regression Discontinuity Design: Pursuing ...</a></li>
<li><a href="https://datapartnership.org/red-sea-monitoring/notebooks/mobility/visits.html">Estimating Activity Through Point of Interest Visits Using Mobility ...</a></li>
<li><a href="https://frontiergroup.org/articles/is-more-energy-always-better-why-pursuit-of-energy-abundance-risks-missing-the-point/">Is more energy always better? Why pursuit of " energy abundance..."</a></li>

</ul>
</details>

**标签**: `#urban mobility`, `#fuel price shock`, `#transportation inequality`, `#regression discontinuity`, `#point-of-interest data`

---