---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> From 15 items, 3 important content pieces were selected

---

1. [GLM 5.2 在 Semgrep 网络安全基准测试中击败 Claude](#item-1) ⭐️ 8.0/10
2. [布朗教授揭露大规模 AI 辅助考试作弊。](#item-2) ⭐️ 8.0/10
3. [Tokenmaxxing 已死，Tokenmaxxing 长存](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM 5.2 在 Semgrep 网络安全基准测试中击败 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

GLM 5.2 是 Z.ai 的 7440 亿参数开放权重 Mixture-of-Experts 模型，在 Semgrep 的内部网络安全基准测试中获得 39% F1 分数，超过了 Claude Code 的 37%。 这一结果表明，开放权重模型能够在专门的安全任务中匹配甚至超越专有大语言模型，为开发者和安全团队提供了具成本效益的替代方案。 GLM 5.2 总参数 7440 亿，采用 256 专家（8+1 活跃）的 MoE 架构，每步活跃参数 400 亿，上下文窗口 100 万 token，使用 DeepSeek 稀疏注意力；本地运行需要大量显存/内存，例如多块 RTX 3090 或统一内存方案。

hackernews · jms703 · Jun 28, 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: GLM 5.2 是中国 AI 实验室 Z.ai（智普 AI）在 2026 年 6 月发布的最新旗舰大语言模型，采用开放权重的混合专家（MoE）架构，上下文窗口达 100 万 token。Semgrep 的内部网络安全基准测试评估模型发现类似其 Mythos 静态分析引擎所识别漏洞的能力。Claude 指的是 Anthropic 的 Claude 系列大语言模型，其中 Claude Code 是一个使用如 Opus 4.6 等模型的代理 harness，用于代码相关任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buildfastwithai.com/blogs/glm-5-2-review-2026">GLM - 5 . 2 Review 2026: Z.ai's 1M-Context AI Model</a></li>
<li><a href="https://aiproductivity.ai/news/glm-52-edges-claude-semgrep-security-benchmark/">GLM 5.2 vs Claude: Semgrep Cyber Benchmark | AI:PRODUCTIVITY</a></li>
<li><a href="https://unsloth.ai/docs/models/glm-5.2">Run the new GLM - 5 . 2 model by Z.ai on local hardware !</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 GLM 5.2 是日常编程的可靠工作马，指出其在高成本专有模型中表现强劲。一些用户强调该模型巨大的参数规模（约 7530 亿）及其本地运行所需的硬件，而另一些则在更广泛的基准测试中认为其不如 DeepSeek V4 Pro。还有评论澄清 Claude Code 是代理 harness，而非独立的 LLM，这会影响直接比较。

**标签**: `#LLM`, `#GLM-5.2`, `#benchmark`, `#Claude`, `#AI models`

---

<a id="item-2"></a>
## [布朗教授揭露大规模 AI 辅助考试作弊。](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 8.0/10

2026 年 6 月 28 日，布朗大学的一位教授公开谴责了考试中广泛使用 AI 进行的作弊行为，引发了 Hacker News 上的大规模讨论，涉及作弊和评估方法。 此事件凸显了随着生成式 AI 工具普及而带来的学术诚信威胁，促使教育者重新思考考试设计和评估政策。 该 Hacker News 帖子获得 312 个点赞和 418 条评论，参与者提出了诸如现场手写考试、口头面试和 AI 监考软件等应对作弊的方案。

hackernews · geox · Jun 28, 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48708991)

**背景**: 生成式 AI 模型能够生成论文、代码和答案，难以与学生的原创工作区分，从而引发不可检测作弊的担忧。高校已开始部署基于 AI 的抄袭检测工具，如 Turnitin 的 AI 作弊检测器以及远程监考系统，这些系统可监控屏幕活动、注视和生物特征。这些技术旨在维护学术诚信，同时应对 AI 能力的不断提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.washingtonpost.com/technology/2023/06/02/turnitin-ai-cheating-detector-accuracy/">washingtonpost.com/technology/2023/06/02/turnitin- ai - cheating ...</a></li>
<li><a href="https://www.wecreateproblems.com/blog/ai-proctoring-tools-for-universities">Top 15 AI Proctoring Tools for Universities in 2026</a></li>
<li><a href="https://www.compilatio.net/en">Plagiarism & AI Checker | #1 Trusted by Students and Universities</a></li>

</ul>
</details>

**社区讨论**: 评论者对传统评估方式被 AI 轻易绕过表示沮丧，主张采用现场手写考试或口头面试来验证学生的理解。也有人认为 AI 可能实际上提高大学学位的信号价值，因为它迫使机构依赖更古老、低技术的评估方法。还有人指出法学院已使用封闭式文字处理器进行考试，并呼吁在更广泛的范围内采用安全的考试平台。

**标签**: `#AI ethics`, `#academic integrity`, `#higher education`, `#cheating`, `#Hacker News`

---

<a id="item-3"></a>
## [Tokenmaxxing 已死，Tokenmaxxing 长存](https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing) ⭐️ 8.0/10

文章认为，tokenmaxxing 作为绩效指标正在消逝，被‘复合正确性’新范式所取代——更多的 token 消耗能够带来更好的 AI 代理结果。 这一转变表明从浪费的 token 消耗转向以价值驱动的结果，影响着 AI/ML 从业者和工程师如何衡量生产力和分配 AI 预算。 ‘复合正确性’认为增加 token 使用能提升代理任务的正确性，这与 tokenmaxxing 仅追求数量形成对比；评论者指出其局限，例如在安全漏洞挖掘中更多 token 不一定带来更好结果。

hackernews · theahura · Jun 28, 16:24 · [社区讨论](https://news.ycombinator.com/item?id=48708795)

**背景**: Tokenmaxxing 是一种工作场所的生产力指标，用于追踪员工使用 AI 服务时消耗的 LLM token 数量，如维基百科和行业文章所述。该指标曾在 Meta、OpenAI、Shopify 等公司内部被用来游戏化 AI 使用，但因鼓励浪费性消耗而受到越来越多的批评。相比之下，‘复合正确性’描述了一种范式：在任务上花费更多 token 能提高获得正确结果的可能性，例如 Claude 3.5 在 2024 年 10 月的更新使得长时程 agentic 编码工作流能够在先前正确性的基础上叠加，而非累积错误。这一转变反映了人们对 token 支出如何转化为 AI 代理性能的看法正在演变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://ctaio.dev/en/labs/tokenmaxxing/">What Is Tokenmaxxing? The AI Productivity Metric Explained (2026)</a></li>
<li><a href="https://xiumu.com/the-software-factory-when-ai-agents-write-all-your-code/">The Software Factory: When AI Agents Write All Your Code - Xiumu AI</a></li>

</ul>
</details>

**社区讨论**: 评论者认为 tokenmaxxing 是一种过渡性工具，曾让员工有意义地使用 AI，而其他人则对‘复合正确性’的普遍益处持怀疑态度，指出往往需要清除上下文，且如安全漏洞挖掘等任务并不会因更多 token 消耗而改善；还有些评论带有幽默或比喻色彩，反映出对该指标消亡的复杂情感。

**标签**: `#AI`, `#token usage`, `#LLMs`, `#AI agents`, `#productivity`

---