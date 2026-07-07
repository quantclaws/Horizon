---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> From 13 items, 4 important content pieces were selected

---

1. [GLM 5.2 与即将到来的 AI 利润崩溃](#item-1) ⭐️ 8.0/10
2. [Anthropic 在语言模型中提出全局工作空间机制](#item-2) ⭐️ 8.0/10
3. [腾讯发布 Hy3，2950 亿参数 MoE 模型，激活参数 210 亿](#item-3) ⭐️ 8.0/10
4. [Simon Willison 发布 sqlite-utils 4.0rc3，加入复合外键支持](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM 5.2 与即将到来的 AI 利润崩溃](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/) ⭐️ 8.0/10

博客文章指出，Z.AI 三周前发布的旗舰模型 GLM-5.2 具备 1M-token 上下文和强长时序任务能力，预示着由于算力成本下降和竞争加剧而即将到来的 AI 利润崩溃。 AI 利润崩溃将侵蚀模型提供商的利润，推动 AI 服务趋向商品化定价，并迫使初创公司和投资者重新考虑商业模式和资本分配。 GLM-5.2 相较于 GLM-5.1 提供了稳定的 1M-token 上下文，专注于长时序和编码任务，可用于小程序开发；文章还提到了 Z.AI 的视觉 MCP 服务器和 ZCode 代码套件作为补充工具。

hackernews · martinald · Jul 6, 20:14 · [社区讨论](https://news.ycombinator.com/item?id=48809877)

**背景**: GLM 是 Z.AI 开发的一系列大语言模型，每个版本旨在提升推理和长上下文能力。AI 利润崩溃点是指 AI 功能的可变成本超过其产生的收入的使用水平，随着规模扩大，原本盈利的服务会变成亏损的引流产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://openlm.ai/glm-5.2/">GLM-5.2 | OpenLM.ai</a></li>
<li><a href="https://www.richardewing.io/glossary/ai-margin-collapse-point">What is AI Margin Collapse Point? | Richard Ewing</a></li>

</ul>
</details>

**社区讨论**: 评论者观点分歧：有人怀疑仅算力成本下降就会压缩利润，以云服务和开源软件为例；也有人指出 Z.AI 的视觉 MCP 和 ZCode 套件可以增加价值；还有少数人认为激烈竞争和模型易于复制将把 token 利润推向零，除非企业发生串通。

**标签**: `#AI`, `#machine learning`, `#economics`, `#GLM-5.2`, `#margin collapse`

---

<a id="item-2"></a>
## [Anthropic 在语言模型中提出全局工作空间机制](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic 在语言模型中提出全局工作空间机制，指出称为 J‑space 的内部激活子空间充当共享推理枢纽，类似于人类的意识觉醒。实验表明，屏蔽该子空间会削弱高阶认知功能，但基本语言能力仍然保持。 这项工作将认知科学与 AI 可解释性连接起来，提供了一种可检验的框架来定位大型语言模型中的推理过程，有助于设计更安全、更透明的模型。它可能影响未来关于模型意识、可编辑性和对齐的研究。 研究人员使用雅可比透镜（J‑lens）测量每层微小扰动对最终 logits 的影响，确定 J‑space 为影响最大的子空间。实验表明，去除 J‑space 活动会损害需要多步推理、算术和逻辑推断的任务表现，但流畅性和语法基本不受影响。

hackernews · in-silico · Jul 6, 17:44 · [社区讨论](https://news.ycombinator.com/item?id=48808002)

**背景**: 全局工作空间理论认为，当信息在全脑范围内广播时，意识就会产生，从而实现整合且灵活的认知。在 AI 可解释性领域，研究者寻找类似的子空间，其中激活是全局可访问且能影响行为的。先前的工作已将特定激活模式与诸如数学或语言等技能联系起来，但 Anthropic 的研究是首次在大型语言模型中明确测试全局工作空间式的结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_workspace_theory">Global workspace theory - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://transformer-circuits.pub/2026/workspace/index.html">Verbalizable Representations Form a Global Workspace in Language Models</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这与之前通过复制激活层来提升模型性能的实验相似，争论是否真的可以将其类比为人类的意识觉醒，并称赞了 Neel Nanda 所写的附带评论的可读性。有人对该研究可能带来的可解释性洞察感到兴奋，也有人呼吁需要更直接的证据来将 J‑space 与类人认知联系起来。

**标签**: `#language-models`, `#global-workspace-theory`, `#AI interpretability`, `#cognitive-science`, `#Anthropic research`

---

<a id="item-3"></a>
## [腾讯发布 Hy3，2950 亿参数 MoE 模型，激活参数 210 亿](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 8.0/10

腾讯发布了 Hy3，这是一个具有 2950 亿参数、210 亿激活参数和 38 亿 MTP 层参数的混合专家模型，采用 Apache 2.0 许可证，并在 OpenRouter 上免费提供直至 7 月 21 日。 此次发布展示了一个规模庞大的开源混合专家模型，在效率上可与更大的旗舰模型竞争，推动了开源大语言模型的可及性并促进了更广泛的实验。 Hy3 的完整模型大小为 598GB，FP8 量化版本为 300GB，支持 256K 的上下文长度，并在 Hugging Face 的 tencent/Hy3 仓库中提供。

rss · Simon Willison · Jul 6, 23:57

**背景**: 混合专家（MoE）模型通过条件计算在每个令牌上仅激活部分专家网络，从而在保持效率的同时实现大规模模型。FP8 量化采用 8 位浮点格式表示权重，显著降低内存占用且精度损失较小，使大型模型更易部署。Hy3 中的 MTP（混合令牌专家）层参数增加了令牌级路由的额外容量，有助于其出色表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://rcrtech.com/semiconductor-news/llms-quantization-fp8-fp4-int8/">LLMs and quantization: FP8, FP4, and INT8 explained</a></li>
<li><a href="https://huggingface.co/tencent/Hy3">tencent/Hy3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#large language models`, `#Mixture-of-Experts`, `#open source`, `#Tencent`, `#AI`

---

<a id="item-4"></a>
## [Simon Willison 发布 sqlite-utils 4.0rc3，加入复合外键支持](https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything) ⭐️ 8.0/10

Simon Willison 宣布发布 sqlite-utils 4.0rc3，这是即将到来的 4.0 稳定版的候选版本。该版本新增了复合外键的内省和创建支持，并使列名匹配不区分大小写，以遵循 SQLite 的惯例。 这些增强提升了库对复杂关系模式的建模能力，并使其更易于处理使用不区分大小写标识符的现有 SQLite 数据库。依赖 sqlite-utils 进行数据探索或 ETL 管道的开发者将受益于更准确的外键处理和更少的不匹配。 复合外键支持对 table.foreign_keys API 引入了微妙的破坏性更改，因而需要将主要版本提升至 4.0。不区分大小写的列名匹配需要在代码库的许多地方进行修改，以符合 SQLite 的默认行为。

rss · Simon Willison · Jul 6, 05:40

**背景**: sqlite-utils 是一个用于创建、修改和查询 SQLite 数据库的 Python 库和命令行工具，受到开发者的欢迎，用于快速数据原型设计。它提供了用于内省模式、插入数据和管理外键的辅助功能。复合外键指的是多个列共同引用另一张表的主键，SQLite 本身支持此特性，但 sqlite-utils 以前无法进行内省或创建。列名不区分大小写的匹配反映了 SQLite 在未加引号时对标识符的默认处理方式，使得库的行为与底层数据库保持一致。

**标签**: `#sqlite`, `#python`, `#library-release`, `#foreign-keys`, `#sqlite-utils`

---