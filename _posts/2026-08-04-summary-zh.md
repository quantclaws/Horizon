---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> From 48 items, 13 important content pieces were selected

---

1. [Optuna 5.0.0-rc1 发布，多变量 TPE 成为默认采样器](#item-1) ⭐️ 8.0/10
2. [LLMs 奖励专业知识](#item-2) ⭐️ 8.0/10
3. [OpenAI 指出数学和理论计算机科学的十项最新进展](#item-3) ⭐️ 8.0/10
4. [开发者工具必须开源：LLM 使终端用户定制成为可能](#item-4) ⭐️ 8.0/10
5. [Cloudflare 通过 KV 缓存量化规模运行 Kimi 和 GLM 模型](#item-5) ⭐️ 8.0/10
6. [ComfyUI 添加 MiniMax H3 开放权重 2K 视频模型的 Day‑0 支持](#item-6) ⭐️ 8.0/10
7. [Andy Pavlo 加入 ClickHouse 成立 ClickHouse Labs。](#item-7) ⭐️ 8.0/10
8. [Pandoc 庆祝二十年文档转换卓越成就](#item-8) ⭐️ 8.0/10
9. [研究发现印度厕所补贴使河流粪便污染增加 72%](#item-9) ⭐️ 8.0/10
10. [论文分析人工智能供应链瓶颈与工业政策的影响。](#item-10) ⭐️ 8.0/10
11. [半线性随机 HJB 方程的策略迭代方案及其指数收敛](#item-11) ⭐️ 8.0/10
12. [错误且更自信：LLM 在研究生经济学考试中的表现](#item-12) ⭐️ 8.0/10
13. [统一的连续时间 Q-学习用于均场博弈与控制](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Optuna 5.0.0-rc1 发布，多变量 TPE 成为默认采样器](https://github.com/optuna/optuna/releases/tag/v5.0.0-rc1) ⭐️ 8.0/10

Optuna 5.0.0-rc1 将带有常量说谑策略的多变量 TPE 设为单目标优化的默认采样器，并采用多目标 TPE 替代 NSGA-II 成为多目标任务的默认采样器。同时引入条件 PED-ANOVA 作为默认超参数重要性算法，并新增约束优化的 API。 这些改动将最先进的贝叶斯优化技术带入 Optuna 的默认设置，提高了高维和条件超参数搜索的效率和可扩展性。从业者将获得更好的开箱即用性能，无需手动调整采样器。 多变量 TPE 引入了 Watanabe 2023 的增强带宽计算并使用常量说谑策略；多目标 TPE 取代 NSGA-II 成为多目标优化的默认采样器；来自 KDD 2026 论文的条件 PED-ANOVA 成为默认重要性评估器。破坏性变更包括删除 optuna.multi_objective 模块和废弃 constraints_func 参数。

github · c-bata · Aug 3, 05:30

**背景**: Optuna 是一个开源的超参数优化框架，其单目标任务的默认采样器是 Tree-structured Parzen Estimator（TPE）。以前，多目标优化默认使用 NSGA-II，尽管多目标 TPE（MOTPE）已可用。像 PED-ANOVA 这样的超参数重要性方法有助于用户了解哪些参数对目标影响最大，特别是在条件或层次化搜索空间中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/optuna/multivariate-tpe-makes-optuna-even-more-powerful-63c4bfbaebe2">“ Multivariate ” TPE Makes Optuna Even More Powerful | Medium</a></li>
<li><a href="https://arxiv.org/pdf/2304.11127">Tree-Structured Parzen Estimator: Understanding Its Algorithm ...</a></li>
<li><a href="https://medium.com/optuna/significant-speed-up-of-multi-objective-tpesampler-in-optuna-v4-0-0-2bacdcd1d99b">Significant Speed Up of Multi-Objective TPESampler in Optuna v4.0.0 | by Shuhei Watanabe | Optuna | Medium</a></li>

</ul>
</details>

**标签**: `#optuna`, `#hyperparameter optimization`, `#TPE`, `#multi-objective optimization`, `#software release`

---

<a id="item-2"></a>
## [LLMs 奖励专业知识](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 8.0/10

文章认为，大型语言模型会放大已具备领域专业知识的用户的能力，而不是取代技能。 这表明在 AI 辅助工作中，专业知识仍然至关重要，影响开发者和专业人士应如何看待并培养技能。 文章指出，有效的提示工程需要对模型行为的理解，而具备更深领域知识的用户能够编写更好的提示，从而获得更优的输出。

hackernews · MaxMussio · Aug 3, 21:13 · [社区讨论](https://news.ycombinator.com/item?id=49161518)

**背景**: 大型语言模型（LLMs）基于从海量数据中学习的模式生成文本，其输出在很大程度上取决于输入提示的质量。提示工程是设计提示以引导 LLMs 产生期望结果的实践，涉及少样本、思维链等技巧。文章表明，已经具备领域理解的用户能够更好地利用这些技巧，使 LLMs 成为现有专业知识的放大器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_engineering">Prompt engineering</a></li>
<li><a href="https://www.promptingguide.ai/">Prompt Engineering Guide | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意 LLMs 就像用户专业知识的镜子，指出有效使用需要对特定代码库的熟悉和谨慎的提示，同时也有人警告确认偏误和过度依赖模型的风险。

**标签**: `#LLMs`, `#AI`, `#software development`, `#prompt engineering`, `#expertise`

---

<a id="item-3"></a>
## [OpenAI 指出数学和理论计算机科学的十项最新进展](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 8.0/10

OpenAI 发布了一篇文章，概述了数学和理论计算机科学领域的十项最新进展，重点强调了语言模型辅助定理证明等 AI 驱动的进展以及悬而未决的问题。 这些进展展示了 AI 如何重塑数学研究，有望加速证明发现并影响密码学和算法设计等领域。 文章提到了 Lean 生态中的 AI 驱动形式定理证明、用于数学推理的神经符号集成以及 OpenAI 的 GPT‑f 模型用于自动猜想生成。

hackernews · milkshakes · Aug 3, 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49157930)

**背景**: 最近的工作表明，大型语言模型可以通过生成证明步骤和验证正确性来辅助如 Lean 的形式定理证明器，正如 Lean 生态计划所探讨的。神经符号方法将符号推理与深度学习结合以提升数学推理能力，这一点在神经符号 AI 的调查中有所描述。此外，诸如 OpenAI 的 GPT‑f 之类的模型已被用于自动生成猜想，扩展了 AI 在数学发现中的应用范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuro-symbolic_AI">Neuro-symbolic AI - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2404.09939v1">A Survey on Deep Learning for Theorem Proving</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 在数学中的指数级进展感到兴奋，同时质疑哪些人类创造力方面可能仍难以触及，指出该帖在 Hacker News 上的异常推送，并讨论了诸如对后量子密码学的实际影响以及模型在反驳猜想中的作用等实际意义。

**标签**: `#mathematics`, `#theoretical computer science`, `#AI`, `#research advances`, `#OpenAI`

---

<a id="item-4"></a>
## [开发者工具必须开源：LLM 使终端用户定制成为可能](https://blog.exe.dev/devtools-must-be-open-source) ⭐️ 8.0/10

博客文章认为所有开发者工具都应开源，并指出大语言模型现在使终端用户能够实际地检查、修改和重建这些工具。 如果开发者工具变为开源且 LLM 辅助定制普及，这可能降低工具适配门槛，促进创新，并将软件工具的经济模式转向更多用户驱动的开发。 评论者指出，虽然开源赋予修改代码的自由，但大多数用户依赖他人来完成修改。他们讨论 LLM 在每次更改时重建工具是否高效、可靠，或者考虑到作者自己使用闭源服务的情况是否具有虚伪性。

hackernews · bryanmikaelian · Aug 3, 14:15 · [社区讨论](https://news.ycombinator.com/item?id=49156111)

**背景**: 开发者工具是程序员用来创建和维护其他软件的软件应用，例如编辑器、编译器和调试器。开源意味着源代码公开可用，任何人都可以研究、修改和再分发它。大语言模型（LLM）是经过海量文本训练的人工智能系统，能够生成或转换代码。通过理解自然语言指令，LLM 可以潜在地自动化获取源代码、应用更改并重新构建工具的过程，使终端用户定制变得更加可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意开发者工具应当开源，但对，但对使用 LLM 不断为微小更改重建工具的实际操作性存在分歧，认为这效率低且不可靠。一些人指出作者在倡导开源理想同时却依赖众多闭源服务的讽刺，还担心自动化的夜间更新可能会破坏工作流。

**标签**: `#open-source`, `#developer-tools`, `#LLMs`, `#software-engineering`, `#hackernews`

---

<a id="item-5"></a>
## [Cloudflare 通过 KV 缓存量化规模运行 Kimi 和 GLM 模型](https://blog.cloudflare.com/smaller-faster-safer-models/) ⭐️ 8.0/10

Cloudflare 发布了一篇博客，详细说明他们如何使用 KV 缓存量化技术大规模部署 Kimi 和 GLM 大语言模型，以实现更小、更快、更安全的 AI 推理。 这展示了实际的 LLM 优化策略，能够降低开发者使用 AI API 时的延迟和成本，同时也凸显了模型质量的权衡。 他们对键值缓存应用了 FP8 量化，主要测试了 Kimi K2.6，并指出 KV 量化可能比权重量化更易导致输出质量下降。

hackernews · ascorbic · Aug 3, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=49158581)

**背景**: Kimi 是由 Moonshot AI 开发的一系列长上下文大语言模型，可通过 Kimi API 平台使用。GLM（通用语言模型）是 Z.ai 的开源权重大语言模型系列，首次以 ChatGLM 形式在 2023 年发布。KV 缓存量化通过以降低精度存储键和值激活来减少内存带宽和计算开销，这一技术在如 KVQuant 等工作中被探讨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/models">Model List - Kimi API Platform</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2401.18079">[2401.18079] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了隐私和透明度方面的担忧，希望看到更详细的跨模型家族评估和更清晰的定价；一些人建议使用如 NF4 等其他量化格式，并询问了招聘需求。

**标签**: `#LLM inference`, `#model quantization`, `#Cloudflare`, `#AI optimization`, `#KV cache`

---

<a id="item-6"></a>
## [ComfyUI 添加 MiniMax H3 开放权重 2K 视频模型的 Day‑0 支持](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 8.0/10

ComfyUI 现已原生支持刚刚发布的 MiniMax H3 模型，提供开放权重、多模态输入、原声立体声以及生成最长 15 秒的 2K 视频片段。 此集成使得消费级显卡也能实现高保真视频合成，降低了创作者本地制作专业级视听内容的门槛。 该模型的调制权重（约占总参数的 40%）可用查找表替换，使显存占用降低约 66%（从 123.6 GB 减至 42.5 GB），并通过动态显存卸载在 RTX 3060 上实现 2K 生成；用户反馈表明在 RTX 4070 Ti Super 上生成 10 秒 480p 视频约需 10 分钟。

hackernews · vblanco · Aug 3, 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49155629)

**背景**: ComfyUI 是一个开源的基于节点的界面，用户可以通过它构建和运行用于图像、视频、3D 和音频的生成式 AI 工作流，使用扩散模型等工具。MiniMax H3 是最近发布的开放权重通用多模态模型，能够将文本、图像、视频和音频作为统一输入，输出包含原声立体声的高达 2K 分辨率的连贯视频片段。该模型在采用权重剪枝和动态显存卸载等优化后，能够在消费级硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video Model | fal</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，将约 40% 的调制权重替换为查找表可在不损失质量的情况下将显存减少三分之二，并报告在 RTX 4070 Ti Super 上生成 10 秒 480p 视频大约需要 10 分钟。他们称赞模型在鼠标渲染方面的表现和整体质量，但也指出在某些罕见提示下会出现 AI 平滑伪影和不稳定性，暗示可以采用传统特写渲染与 AI 生成的宽镜头相结合的混合工作流。

**标签**: `#generative-video`, `#AI-models`, `#ComfyUI`, `#open-weights`, `#video-synthesis`

---

<a id="item-7"></a>
## [Andy Pavlo 加入 ClickHouse 成立 ClickHouse Labs。](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 8.0/10

知名数据库研究员 Andy Pavlo 来自卡内基梅隆大学，已加入 ClickHouse 担任数据库研究副总裁，以成立 ClickHouse Labs，这是一个专注于基础数据库和数据架构研究的新机构。 此举表明 ClickHouse 致力于超越短期产品周期的长期基础数据库研究，有望推进 OLAP 性能并惠及更广泛的数据基础设施生态。 ClickHouse Labs 将面向 ClickHouse 和 PostgreSQL 开展查询处理、系统性能和基础设施研究，力求成为一流的行业研究机构。

hackernews · nikolay_sivko · Aug 3, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49156011)

**背景**: ClickHouse 是一个开源的列存储 OLAP 数据库管理系统，通过按列存储数据来实现快速的分析查询。Andy Pavlo 是卡内基梅隆大学的教授，以其数据库系统课程、自适应索引、OLTP 研究以及受欢迎的讲座系列而闻名。像 ClickHouse Labs 这样的企业研究实验室旨在将学术见解与工业开发结合起来，专注于长期技术挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clickhouse.com/docs/en/faq/general/columnar-database">What is a columnar database ? | ClickHouse Docs</a></li>
<li><a href="https://clickhouse.com/blog/andy-pavlo-founding-clickhouse-labs">ClickHouse launches ClickHouse Labs with Andy Pavlo as VP of Database Research | ClickHouse</a></li>
<li><a href="https://www.businesswire.com/news/home/20260803890510/en/ClickHouse-Launches-ClickHouse-Labs-With-Andy-Pavlo-as-VP-of-Database-Research">ClickHouse Launches ClickHouse Labs With Andy Pavlo as VP of Database Research</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎此举，称赞 Pavlo 的教学并希望他的讲座能以赞助形式继续。一些人敦促 ClickHouse 资助学术数据库研究，并好奇解耦计算/存储趋势（如 Trino、Iceberg）对摄取和索引的影响。

**标签**: `#databases`, `#ClickHouse`, `#research`, `#Andy Pavlo`, `#OLAP`

---

<a id="item-8"></a>
## [Pandoc 庆祝二十年文档转换卓越成就](https://pandoc.org/twenty-years-of-pandoc.html) ⭐️ 8.0/10

Pandoc 项目在其二十周年之际发布回顾，强调其 N×M 读取器‑写入器模块化架构、在学术和工业中的广泛采用以及作为文档转换工具的持久实用性。 作为一种免费的文档转换器，Pandoc 能够连接数十种标记格式，支撑着无数学术出版工作流，并展示了设计良好的开源工具如何能够保持二十年的相关性。 其设计将 N 个解析器（读取器）与 M 个渲染器（写入器）分离，实现 N×M 种转换；它支持 Lua 和 JSON 过滤器来操作中间抽象语法树，并能输出干净的 HTML、LaTeX 或 Markdown。

hackernews · fiddlosopher · Aug 3, 15:04 · [社区讨论](https://news.ycombinator.com/item?id=49156750)

**背景**: Pandoc 是一种用 Haskell 编写的免费开源文档转换器，能够读取一种标记格式并输出另一种。它支持多种输入和输出格式，包括 Markdown、LaTeX、HTML、reStructuredText、EPUB 和 Microsoft Word docx。得益于其模块化的读取器‑写入器架构和可扩展的过滤器系统，Pandoc 在学术出版、技术文档和网页内容工作流中成为基础工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pandoc">Pandoc - Wikipedia</a></li>
<li><a href="https://opensource.com/article/20/5/pandoc-cheat-sheet">Convert documents with Pandoc like a pro | Opensource.com</a></li>
<li><a href="https://pandoc.org/">Pandoc - index</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Pandoc 的输出整洁、日常使用中的实用性（例如在邮件和代码之间移动内容），并指出一位哲学教授创造了被数百万人使用的工具。许多用户分享了个人脚本，如极简静态站点生成器，展示了 Pandoc 的灵活性和持久吸引力。

**标签**: `#pandoc`, `#document conversion`, `#open source`, `#software longevity`, `#markup`

---

<a id="item-9"></a>
## [研究发现印度厕所补贴使河流粪便污染增加 72%](https://arxiv.org/abs/2607.29371) ⭐️ 8.0/10

该研究估计，印度对超过 1 亿座厕所的补贴使河流粪便污染增加 72%，在上游缺乏足够废水处理设施的地区抵消了儿童健康益处。 这表明卫生政策可能产生意外的水污染外部性，若未配套足够的粪便污泥处理设施，将抵消健康收益。 该研究利用土壤特性变异作为工具变量，发现河流粪便污染上升 72%，且在缺乏上游废水处理的地区死亡率下降效果消失。

rss · arXiv Quantitative Finance · Aug 3, 04:00

**背景**: 许多发展中国家通过补贴建造厕所来减少露天排便并改善儿童健康。若缺乏适当的粪便污泥处理，坑式厕所的废物可能渗入地下水和地表水，尤其是在土壤渗透性高或地下水浅的地区。这些意外的污染外部性可能通过增加病原体暴露而抵消健康收益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fecal_sludge_management">Fecal sludge management - Wikipedia</a></li>
<li><a href="https://www.wateraid.org/in/sites/g/files/jkxoof336/files/strategy-for-faecal-sludge-management-in-rural-india-.pdf">Strategy for Faecal Sludge Management in Rural India</a></li>
<li><a href="https://sswm.info/sites/default/files/reference_attachments/pit+latrines.pdf">Pit Latrines and Their Impacts on Groundwater</a></li>

</ul>
</details>

**标签**: `#sanitation`, `#water quality`, `#public health`, `#development economics`, `#environmental policy`

---

<a id="item-10"></a>
## [论文分析人工智能供应链瓶颈与工业政策的影响。](https://arxiv.org/abs/2607.29572) ⭐️ 8.0/10

该研究使用赫芬达尔-希施曼指数（HHI）量化人工智能堆栈每一层的集中度。结果显示下游 HHI 低于 1,800（美国监管机构认为高度集中的阈值），而上游极度集中：先进封装得分 8,100，前沿光刻达到最高值 10,000，关键矿物（如镓）的生产或提炼几乎被单一国家垄断。 研究结果表明，上游层构成了反垄断无法触及的战略瓶颈，因此出口管制和国内工业政策成为保障人工智能供应链的主要手段。这为政策制定者指出了应集中干预以降低集中度风险的关键领域。 下游层（如模型使用和云服务）的赫芬达尔-希施曼指数低于美国监管机构用来判定高度集中的 1,800 阈值，表明市场力量较弱。相反，上游层表现出极端集中：先进封装得分 8,100，前沿光刻达到最高值 10,000，关键矿物（如镓）的生产或提炼几乎被单一国家垄断；此外，这些上游输入的价格上涨对最终产品成本影响甚微，因此真正的风险在于输入可能被切断而非价格上涨。

rss · arXiv Quantitative Finance · Aug 3, 04:00

**背景**: 人工智能依赖于一个分层的供应链：AI 模型运行在计算硬件上，而计算硬件又依赖于通过先进封装和前沿光刻等工艺制造的先进半导体芯片，这些芯片还需要电力和精炼矿物。研究采用赫芬达尔-希施曼指数（HHI）来衡量市场集中度，其中低于 1,500 表示竞争性市场，1,500‑2,500 为中等集中，高于 2,500 为高度集中，美国监管机构将 1,800 视为高度集中的阈值。先进封装通过将多个芯片集成在一个封装内来提升性能并减少信号路径，而极紫外光刻（EUV）几乎由 ASML 垄断供应，是制造最先进 AI 芯片所必需的关键工艺；关键矿物（如镓）的精炼仅在少数几个国家进行，使这些国家对这一关键上游输入拥有不成比例的控制力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_(semiconductors)">Advanced packaging (semiconductors) - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://en.wikipedia.org/wiki/Herfindahl–Hirschman_index">Herfindahl–Hirschman index - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#supply chain`, `#industrial policy`, `#HHI`, `#semiconductors`

---

<a id="item-11"></a>
## [半线性随机 HJB 方程的策略迭代方案及其指数收敛](https://arxiv.org/abs/2607.29024) ⭐️ 8.0/10

作者提出了一种基于策略迭代的算法，将半线性随机 HJB 方程线性化为一系列线性方程，并证明近似序列在均方意义下对值函数具有单调指数收敛。 这为非马尔可夫随机最优控制问题提供了首个可证明指数收敛的策略迭代方法，为以前难以求解的一类问题提供了理论上可靠且计算上可行的方法。 该算法通过对半线性随机 HJB 方程进行连续线性化，得到一系列线性后向随机微分方程，其解在 L²范数下单调且以指数速率收敛。

rss · arXiv Quantitative Finance · Aug 3, 04:00

**背景**: 随机 Hamilton-Jacobi-Bellman（SHJB）方程出现在随机最优控制中，当价值函数依赖于随机场时；在非马尔可夫情况下，它们变为含有可测随机性的半线性偏微分方程，直接求解数值上具有挑战性。策略迭代是求解马尔可夫决策过程和连续时间控制问题的经典技术，通过策略评估和改进迭代进行。指数收敛意味着误差随着迭代次数以常数的负指数形式减少，这是一种在非线性随机偏微分方程中罕见的强保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.math.univ-brest.fr/perso/rainer.buckdahn/March+2010/presentation/School/RoscoffFuhrman2010.pdf">Hamilton - Jacobi - Bellman equations</a></li>
<li><a href="https://arxiv.org/html/2508.01718v1">Neural Policy Iteration for Stochastic Optimal Control ...</a></li>
<li><a href="https://www.researchgate.net/publication/341299714_Exponential_Convergence_and_Stability_of_Howard's_Policy_Improvement_Algorithm_for_Controlled_Diffusions">Exponential Convergence and Stability of Howard's Policy ...</a></li>

</ul>
</details>

**标签**: `#stochastic optimal control`, `#Hamilton-Jacobi-Bellman equations`, `#policy iteration`, `#exponential convergence`, `#stochastic PDEs`

---

<a id="item-12"></a>
## [错误且更自信：LLM 在研究生经济学考试中的表现](https://arxiv.org/abs/2607.23424) ⭐️ 8.0/10

该研究在新提出的研究生经济推理基准（GERB）的六十道研究生水平微观经济学问题中加入无关干扰信息（红鲱鱼），发现大型语言模型的正确答题率平均下降约 12.3 个百分点。 这表明大型语言模型对无关信息极其敏感，削弱了它们在嘈杂真实环境中的可靠性，并提供了 GERB 作为衡量推理鲁棒性的基准。 在无干扰的问题上，模型平均正确率为 52.5%；加入红鲱鱼后正确率下降 12.3 个百分点，约为其平均表现的四分之一，且无论模型是否具备推理能力，这一影响没有显著差异——不过具备推理能力的模型答案会摇摆不定，而无推理能力的模型则倾向于重复同样的错误答案；开放权重模型在每个正确答案的成本上更低，却能达到相近的准确率。

rss · arXiv Quantitative Finance · Aug 3, 04:00

**背景**: 大型语言模型（LLMs）是通过预测下一个标记来生成文本的人工智能系统，常被用于推理任务以评估其遵循逻辑步骤的能力。“红鲱鱼”是指在问题中插入的无关信息，用于检测模型的推理是否会被噪声干扰。评估对这种干扰的鲁棒性很重要，因为现实世界的输入经常包含无关内容，可能导致性能下降。该研究采用了被试内 2×2 因子实验设计，即每个模型在四种条件下（有/无红鲱鱼以及是/否要求解释）回答所有问题，从而能够直接比较同一模型在不同处理下的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Di-viner/LLM-Robustness-to-Irrelevant-Information">GitHub - Di-viner/LLM-Robustness-to-Irrelevant-Information: [COLM'24] "How Easily do Irrelevant Inputs Skew the Responses of Large Language Models?"</a></li>
<li><a href="https://blog.mirkopeters.com/decoding-the-intricacies-an-in-depth-exploration-of-within-subject-design-0b0c31712527">Decoding the Intricacies: An In-depth Exploration of Within - Subject ...</a></li>

</ul>
</details>

**标签**: `#LLM robustness`, `#reasoning`, `#economics benchmark`, `#AI evaluation`, `#experimental study`

---

<a id="item-13"></a>
## [统一的连续时间 Q-学习用于均场博弈与控制](https://arxiv.org/abs/2407.04521) ⭐️ 8.0/10

本文提出了一种统一的连续时间 Q-学习方法，使用解耦的积分 Q-函数（decoupled Iq-function）来求解均场博弈（MFG）和均场控制（MFC）问题。 通过提供鞅刻画和参数算法，该工作将强化学习与均场控制理论桥接，为广泛的随机多智能体系统提供了单一框架。 解耦的积分 Q-函数被证明是鞅，使得在无法直接获取种群分布的情况下也能进行策略评估；所得算法利用测试策略和平均鞅正交条件来学习 MFG 和 MFC 策略，在 LQ 和非 LQ 环境中得到验证。

rss · arXiv Quantitative Finance · Aug 3, 04:00

**背景**: 均场博弈研究通过代表智能体的 Hamilton–Jacobi–Bellman 方程与 Fokker–Planck 方程耦合来描述大量智能体的战略互动。均场控制则相反，优化单个智能体对分布的影响的成本函数。连续时间 Q-学习将时序差分学习扩展到随机微分方程，常用于包含扩散和突跳的跳扩散模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mean-field_game_theory">Mean-field game theory - Wikipedia</a></li>
<li><a href="https://bactra.org/notebooks/mean-field-games-and-control.html">Mean Field Games and Mean Field Control</a></li>
<li><a href="https://arxiv.org/html/2407.03888v4">Continuous - time q - learning in jump - diffusion models under Tsallis...</a></li>

</ul>
</details>

**标签**: `#mean-field games`, `#reinforcement learning`, `#continuous-time control`, `#Q-learning`, `#stochastic systems`

---