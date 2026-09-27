---
layout: default
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> From 10 items, 4 important content pieces were selected

---

1. [DeepSeek 发布 DSec 弹性计算平台，支持海量 AI 沙箱](#item-1) ⭐️ 8.0/10
2. [Reladraw：一种让你决定元素位置的图表语言](#item-2) ⭐️ 8.0/10
3. [Drawgent：AI 编码代理与实时 Excalidraw 画布交互。](#item-3) ⭐️ 8.0/10
4. [程序员讨论在 LLM 兴起中保持编程乐趣的方法](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 DSec 弹性计算平台，支持海量 AI 沙箱](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek 在最新的 arXiv 论文中介绍了 DSec，一个弹性计算平台，通过统一 SDK 提供 FnCall、容器、microVM 和全虚机沙箱后端，以支持数十万个并发 AI 沙箱。 DSec 能够实现巨量并发沙箱，消除了大规模智能体训练的关键瓶颈，有望加速 AI 研究并降低基础设施成本。 该平台部署在 160 基于 AMD Epyc 的服务器节点上，实现约 38 万个并发沙箱，作者名单多达 131 人，被部分评论者视为资产保护策略。

hackernews · shenli3514 · Sep 26, 18:22 · [社区讨论](https://news.ycombinator.com/item?id=49859112)

**背景**: 弹性计算平台能够根据工作负载需求动态分配计算资源，这对于具有波动计算需求的 AI 工作负载至关重要。沙箱执行可以隔离不可信代码，使得 AI 代理或生成的代码能够在不影响宿主系统的前提下安全运行。智能体训练涉及大规模自主 AI 代理的训练，需要海量的短暂、隔离的计算实例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22978">DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective ...</a></li>
<li><a href="https://technode.com/2026/09/23/deepseek-dsec-agent-training-sandbox-infrastructure/">DeepSeek details DSec sandbox infrastructure for agent training · TechNode</a></li>
<li><a href="https://news.ycombinator.com/item?id=49859112">DeepSeek Elastic Compute (DSec) - Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者指出作者名单异常庞大，猜测这可能是一种资产保护策略，以防关键人才被竞争对手挖走。还有人惊叹于其规模 —  — 在 160 台 Epyc 服务器上实现 38 万个并发沙箱 —  — 并质疑 131 名作者如何协作完成工作。一些人将其与 Google 的 AX 项目相提并论，并询问 DSec 是否充当智能体底层。

**标签**: `#DeepSeek`, `#Elastic Compute`, `#AI Infrastructure`, `#Distributed Systems`, `#HPC`

---

<a id="item-2"></a>
## [Reladraw：一种让你决定元素位置的图表语言](https://github.com/reladraw/reladraw) ⭐️ 8.0/10

Reladraw 引入了一种图表语言，用户可以以声明方式定义图表，同时精确指定节点和边的位置，将手动控制与声明语法结合。 它解决了 Mermaid/Graphviz 等自动布局工具与 Draw.io 等手动编辑器之间的权衡，为设计师和 AI 代理提供了一种高效生成精确、可编辑图表的方法。 该语言采用简洁的文本语法声明节点、边及其相对位置（例如 'from: left to: right'），并提供在线 playground、npm 包以及 Claude 代理技能，以实现程序化生成图表。

hackernews · jpwalsh234 · Sep 26, 17:10 · [社区讨论](https://news.ycombinator.com/item?id=49858513)

**背景**: 声明式图表语言如 Mermaid 和 Graphviz 会自动布局元素，限制了对外观的精细控制。手动工具如 Draw.io 虽然提供完全控制，但耗时且不易被 AI 代理操作。Reladraw 通过让用户保持声明式描述并在需要时覆盖布局来弥合这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49858513">Show HN: Reladraw – A diagram language where you decide where ...</a></li>
<li><a href="https://github.com/reladraw/reladraw">reladraw/reladraw - GitHub</a></li>
<li><a href="https://gtmdelta.com/how-to-create-diagrams-with-d2-a-beginners-guide/">D2 Diagram Tutorial: How to Create Diagrams in D2 | GTM Delta</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了显式的位置控制，指出它解决了他们对 Graphviz 自动布局的不满，并有助于 AI 代理的工作流。有人将其与自己之前计划的项目相比，认为更有用于高带宽对齐。也有少数人提到小 bug，例如边的曲率未能自动处理。

**标签**: `#diagramming`, `#visualization`, `#domain-specific language`, `#developer tools`, `#AI agents`

---

<a id="item-3"></a>
## [Drawgent：AI 编码代理与实时 Excalidraw 画布交互。](https://tangled.org/yanndegat.tngl.sh/drawgent) ⭐️ 8.0/10

Drawgent 引入了一个能够直接操作实时 Excalidraw 画布的 AI 编码代理，使用户能够通过自然语言提示生成和编辑图表，并进行实时协作。 此一体化将代码中心的 AI 助手与可视化设计工具连接起来，为需要共同创建图表和脚手架的架构师、开发者和团队提供了更直观的工作流。 该代理通过 Excalidraw 的开源 MCP 端点进行通信，能够创建、修改和删除图表元素，导出为 SVG/PNG，并同步更改至所有协作者。

hackernews · parasitid · Sep 26, 15:56 · [社区讨论](https://news.ycombinator.com/item?id=49857729)

**背景**: Excalidraw 是一个免费的基于网络的协作白板，模拟手绘草图并支持实时多人编辑。AI 编码代理是由语言模型驱动的系统，能够在自然语言指令下编写、修改和推理代码。将这两种技术结合，使代理能够将图表视为另一种可编辑的工件，从而在代码生成之外实现可视化脚手架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://excalidraw.com/">Free, collaborative whiteboard • Hand-drawn look & feel | Excalidraw</a></li>
<li><a href="https://agenticdiagrams.com/">Agentic Diagrams — Visualize AI Agent Architectures</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞实时画布交互能够将粗糙的 Excalidraw 草图转化为代码项目的有用脚手架。一些人指出 Excalidraw 自身的开源 MCP 端点和服务器，而另一些则更倾向于基于 Mermaid 的工作流或分享了类似的开源实验。总体情绪积极，凸显了这一创新的新颖性以及在将 AI 代理与可视化白板结合时的实际考量。

**标签**: `#AI agents`, `#Excalidraw`, `#collaborative tools`, `#coding assistants`, `#human-AI interaction`

---

<a id="item-4"></a>
## [程序员讨论在 LLM 兴起中保持编程乐趣的方法](https://discourse.haskell.org/t/how-to-keep-enjoying-programming-in-a-world-of-llms/14705) ⭐️ 8.0/10

一个标题为《如何在 LLM 世界中继续享受编程》的 Hacker News 帖子获得了 173 个赞和 222 条评论，开发者们分享了个人经验和策略，以保持编程乐趣并避免在 LLM 日益普及的情况下技能退化。 此次讨论凸显了人们对 LLM 时代技能退化和开发者体验的日益关注，提供了实际见解，可能帮助程序员在不失去核心能力的情况下适应变化。 评论者提到了多种方法：使用快速、低推理的 LLM 进行快速帮助，将乏味任务委托给 AI，以及有意识地避免过度依赖以防止架构规划困难。

hackernews · signa11 · Sep 26, 09:41 · [社区讨论](https://news.ycombinator.com/item?id=49854875)

**社区讨论**: 参与者表达了 zarówno 热情 也有 谨慎：一些人赞赏 LLM 能够自动化乏味工作并提供快速代码摘要，而另一些人则报告依赖生成的代码会导致错误、调试开销以及技能退化的感觉。几位评论者主张使用快速、低努力的模型以保持在编程过程中的参与感，还有少数人回顾了他们对编程的享受早于 LLM 的出现，并可能在 LLM 之后继续存在。

**标签**: `#programming`, `#LLMs`, `#developer experience`, `#skill atrophy`, `#community discussion`

---