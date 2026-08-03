---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> From 12 items, 4 important content pieces were selected

---

1. [安德烈·卡帕西的鹈鹕绘画引发 AI 基准讨论](#item-1) ⭐️ 8.0/10
2. [Kakehashi：实验性用户空间层，用于在 Linux ARM 上运行 macOS 二进制文件](#item-2) ⭐️ 8.0/10
3. [英语学习者必备词汇从 1953 到 2023 的变化](#item-3) ⭐️ 8.0/10
4. [eBay 骚扰活动导致 5600 万美元和解及刑事定罪](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [安德烈·卡帕西的鹈鹕绘画引发 AI 基准讨论](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

安德烈·卡帕西发布了一条让模型画鹈鹕的推文，这在 Hacker News 上引发了关于利用此类绘画任务作为多模态 AI 模型物理和空间推理基准的讨论。 这场讨论凸显了人们对简单、定性基准的兴趣，这些基准能揭示 AI 模型对现实世界物理和空间关系的理解程度，从而指导未来的评估方法。 评论者提到了 Simon Willison 的“骑自行车的鹈鹕”SVG 基准，指出当前模型绘制的鹈鹕相似导致测试区分度降低，并强调需要可重复的提示以及定性/主观评分。

hackernews · delichon · Aug 2, 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: 多模态模型正越来越多地通过生成或解释视觉输出的任务进行评估，例如用 SVG 绘制动物，以测试其对解剖学、物理学和空间布局的理解。最近的基准如 PhysUniBench 通过文本‑图对评估本科水平的物理推理，而 SpatiaLab 则专注于视觉‑语言模型的空间推理。鹈鹕绘画任务位于这些努力的交叉点，充当轻量级探测，以考察模型是否能够输出连贯且物理上合理的图像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gigazine.net/gsc_news/en/20250609-llms-pelicans-on-bicycles/">Here's what happens when you run the AI benchmark ' Draw ...</a></li>
<li><a href="https://arxiv.org/abs/2506.17667">[2506.17667] PhysUniBench: A Multi-Modal Physics Reasoning ... PhysUniBench: Multimodal Benchmark for Physics Reasoning PhysUniBench: A Multi-Modal Physics Reasoning Benchmark at ... Images PHYSUNIBENCH: A MULTI-MODALPHYSICSREA SONINGBENCHMARK ... GitHub - PrismaX-Team/PhysUniBenchmark PhysUniBench: An Undergraduate-Level Physics Reasoning ... PhysUniBench: An Undergraduate-Level Physics Reasoning ...</a></li>
<li><a href="https://arxiv.org/abs/2602.03916v1">SpatiaLab: Can Vision-Language Models Perform Spatial Reasoning in the ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为鹈鹕任务能够揭示模型对物理世界的理解，但指出提示缺乏可重复性以及评分的主观性；有人将其与之前的独角兽‑TikZ 基准相比较，并主张采用定性测量来跟踪进展。

**标签**: `#AI`, `#multimodal models`, `#benchmarking`, `#Andrej Karpathy`, `#pelican`

---

<a id="item-2"></a>
## [Kakehashi：实验性用户空间层，用于在 Linux ARM 上运行 macOS 二进制文件](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Show HN 帖子介绍了 Kakehashi，一个实验性的用户空间兼容层，旨在在 Linux ARM64 上运行 macOS CLI 二进制文件，已有 7‑Zip 和 curl 的工作原型。 如果成功，Kakehashi 将使 Linux ARM 用户能够在不使用虚拟化或双启动的情况下运行 macOS 命令行工具，从而在树莓派以及在 Mac 上运行 Linux 的设备上扩展软件可用性。 该项目在用户空间将 Darwin 系统调用翻译为 Linux，加载 Mach‑O 可执行文件，提供独立的 libSystem，目前 7‑Zip 的运行速度约为原生 Linux 的 5.2 倍慢，而 curl 已通过超过 200 条命令行测试。

hackernews · vlad_kalinkin · Aug 2, 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: 兼容层通过将一种操作系统的系统调用转换为另一种操作系统的系统调用，使得外来二进制文件能够在宿主系统上运行而无需完全仿真。macOS 可执行文件采用 Mach‑O 格式，与 Linux 的 ELF 格式不同，因而需要一个能够解析 Mach‑O 并映射其库的层。在 Linux ARM 上运行 macOS 二进制文件还需要兼容不同的 CPU 架构，增加了系统调用和可执行格式翻译的复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Compatibility_layer">Compatibility layer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mach-O">Mach-O - Wikipedia</a></li>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对该项目的潜力表示兴趣，将其与 Darling 项目进行比较并询问是否可以合作，同时也有人批评项目名称。其他人指出该项目仍处于早期阶段，询问未来计划，并讨论是否采用免虚拟化的方式能够简化实现。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#compatibility layer`, `#userspace`

---

<a id="item-3"></a>
## [英语学习者必备词汇从 1953 到 2023 的变化](https://pudding.cool/2026/07/essential-words/) ⭐️ 8.0/10

Pudding 文章分析了英语学习者所学核心词汇的演变，对比了 1953 年的一般服务表与 2023 年的更新，突出显示了被删除和新增的词汇。 这一变化揭示了更广泛的社会语言学趋势，有助于教育者和课程设计者将教材与当代文化优先事项（如身份、性别和全球交流）保持一致。 1953 年列表中近四分之一的词汇消失，而 2023 年列表中有 39%是新词；例如，谦逊、忠诚和 fellowship 被社区、身份、组织、种族、性别和叙事等词取代，而“社会‑交际”类别的规模基本未变。

hackernews · c-oreills · Aug 2, 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49145590)

**背景**: 一般服务表（GSL）最初由迈克尔·韦斯特于 1953 年出版，包含约 2000 个被视为日常英语必备的高频词。诸如新一般服务表之类的更新版本，以及学术词表和牛津 3000 等相关资源，为语言教学和学习中的词汇选择提供了参考点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Service_List">General Service List - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/New_General_Service_List">New General Service List - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Academic_Word_List">Academic Word List</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，有用的词汇取决于学习者的目标——旅行、媒体或学术——并强调没有单一的“正确”列表。一些人将从谦逊、忠诚等词转向身份导向词的变化与日益增长的社会不平等联系起来，而另一些人则对呈现问题或为其他语言创建无偏差的频率列表的困难感到沮丧。

**标签**: `#language learning`, `#linguistics`, `#education`, `#vocabulary`, `#sociolinguistics`

---

<a id="item-4"></a>
## [eBay 骚扰活动导致 5600 万美元和解及刑事定罪](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 8.0/10

eBay 前安全团队成员对一对批评夫妇实施协调骚扰，导致认罪、监禁以及 5600 万美元的和解。 此案凸显内部安全团队被滥用进行恐吓的行为，凸显企业监督不力及大型科技公司需要更强问责机制的问题。 七名 eBay 安全团队成员，包括前警察队长，参与了骚扰行动；Brian Gilbert 获得缓刑并处以 20,000 美元罚款，Jim Baugh 被判处 57 个月监禁，David Harville 亦被判处监禁（具体刑期未在摘录中披露）。受害者最终与 eBay 达成 5600 万美元的和解协议。

hackernews · JumpCrisscross · Aug 2, 19:19 · [社区讨论](https://news.ycombinator.com/item?id=49147435)

**背景**: eBay 的全球安全团队负责保护公司资产和调查威胁，但在此案中，成员 allegedly 利用其职权恐吓批评者。企业安全人员发动的骚扰行动罕见，但可能包括监视、人肉搜索和法律威胁。受害者向执法部门报告后，案件引起关注并导致联邦调查。此类事件凸显当安全职能缺乏适当监督和问责时所带来的风险。

**社区讨论**: 评论者详细列出了 eBay 安全人员受刑罚的情况，并怀疑骚扰行为仅限于斯坦纳夫妇，呼吁调查其他可能的目标。一些人讨论了更广泛的影响，例如需要监控曾任执法人员的企业安全岗位，而另一些人则转向无关话题，如 eBay 的费用结构或对无监督下不良行为的一般观察。

**标签**: `#eBay`, `#corporate misconduct`, `#harassment`, `#legal settlement`, `#tech ethics`

---