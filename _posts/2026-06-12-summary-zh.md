---
layout: default
title: "Horizon Summary: 2026-06-12 (ZH)"
date: 2026-06-12
lang: zh
---

> From 35 items, 13 important content pieces were selected

---

1. [2001 年论文揭示为何预防性工作被忽视而危机被奖励](#item-1) ⭐️ 8.0/10
2. [Homebrew 6.0.0 发布，引入 Tap Trust 安全机制、更快 JSON API、Linux 沙箱](#item-2) ⭐️ 8.0/10
3. [文章认为人类努力而非仅靠 AI 输出才能赢得注意。](#item-3) ⭐️ 8.0/10
4. [小米发布开源 MiMo Code AI 编程助手](#item-4) ⭐️ 8.0/10
5. [Anthropic 为隐形 Claude Fable 护栏道歉](#item-5) ⭐️ 8.0/10
6. [Zed 推出 DeltaDB 以追踪 Git 提交之间的编辑](#item-6) ⭐️ 8.0/10
7. [AMD 仅用弱 CRC-32 修补致 RCE 漏洞仍未修复。](#item-7) ⭐️ 8.0/10
8. [代码行数指标在 AI 代码生成热潮中被重新提及](#item-8) ⭐️ 8.0/10
9. [基于有限状态自动机的情景约束记忆方法用于量化金融分析](#item-9) ⭐️ 8.0/10
10. [美国金融中介机构的信贷能力是巴西的三到六倍](#item-10) ⭐️ 8.0/10
11. [欧洲脱碳情景对关键可再生能源的原材料需求超过了储备](#item-11) ⭐️ 8.0/10
12. [随机博弈框架将做市商与交易者通过 FBSDEs 联系](#item-12) ⭐️ 8.0/10
13. [FinTradeBench：包含 1400 题的 LLM 金融推理基准](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2001 年论文揭示为何预防性工作被忽视而危机被奖励](https://web.mit.edu/nelsonr/www/Repenning=Sterman_CMR_su01_.pdf) ⭐️ 8.0/10

由尼尔森·雷佩宁和约翰·斯特曼撰写的 2001 年 MIT 论文《Nobody ever gets credit for fixing problems that never happened》在 Hacker News 上重新被关注，该论文运用系统动力学建模说明组织往往奖励危机英雄行为而忽视预防性工作。 它凸显了一种持续的组织偏见：看不见的预防性工作被低估，这影响了软件工程、管理和技术领导力，因为它会削弱长期质量改进的动力。 该论文采用因果环图展示消防工作的强化环和预防性维护的平衡环，认为若缺乏度量，预防性工作就会保持不可见。

hackernews · sam_bristow · Jun 12, 00:38 · [社区讨论](https://news.ycombinator.com/item?id=48498385)

**背景**: 系统动力学是一种使用存量、流量和反馈回路来建模复杂系统的方法，通常通过计算机模型进行仿真。因果环图通过正号（+）和负号（–）的链接来可视化变量之间的相互影响，从而揭示强化（良性/恶性）循环和平衡（目标导向）循环。这些工具有助于解释为什么产生平衡反馈的预防性行动往往被忽视，而产生强化反馈的可见危机响应却受到青睐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/System_dynamics">System dynamics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Causal_loop_diagram">Causal loop diagram</a></li>

</ul>
</details>

**社区讨论**: 评论者一致认为预防性工作常被忽视，举了英雄式消防获得赞扬而运作平稳、无问题的团队却被忽视的例子。他们还指出衡量预防效果的困难，并观察到简洁优雅的解决方案往往被忽略，而过于复杂的修复却容易获得赞誉。

**标签**: `#software engineering`, `#organizational behavior`, `#systems thinking`, `#management`, `#preventive work`

---

<a id="item-2"></a>
## [Homebrew 6.0.0 发布，引入 Tap Trust 安全机制、更快 JSON API、Linux 沙箱](https://brew.sh/2026/06/11/homebrew-6.0.0/) ⭐️ 8.0/10

Homebrew 6.0.0 引入了新的 Tap Trust 安全机制、更快更小的默认内部 JSON API、Linux 沙箱、基于用户调研的改进默认设置、众多 brew bundle 增强、性能提升以及对 macOS 27（Golden Gate）的初步支持。 此版本提升了被数百万开发者使用的包管理器的安全性和性能，使第三方 tap 更安全、加速安装，并提供更可靠的 Linux 支持以及对即将到来的 macOS 27 的初步兼容。 Tap Trust 需要通过 brew trust 命令或设置环境变量 HOMEBREW_REQUIRE_TAP_TRUST=1 才能信任第三方 tap 的 Ruby 代码；JSON API 现在为默认且更小，降低了安装延迟；Linux 沙箱利用 seccomp/bubblewrap 阻止对敏感目录的读取；初步的 macOS 27 支持增加了对即将发布操作系统的兼容性检查。

hackernews · mikemcquaid · Jun 11, 13:24 · [社区讨论](https://news.ycombinator.com/item?id=48490024)

**背景**: Homebrew 是一种流行的开源包管理器，通过 formulae 和社区维护的 tap 在 macOS 和 Linux 上简化软件安装。在 6.0 之前，第三方 tap 可以执行未沙箱化的 Ruby 代码，存在供应链风险。此次发布加入了强制 tap 信任机制、更快的 JSON API 用于获取元数据、Linux 沙箱以隔离构建过程，以及对 macOS 27 的初步兼容，以解决安全、性能和平台支持问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.brew.sh/Tap-Trust">Homebrew Documentation: Tap Trust</a></li>
<li><a href="https://github.com/Homebrew/brew/issues/19204">Improve JSON API for Install Performance Improvements</a></li>
<li><a href="https://docs.brew.sh/Supply-Chain-Security">Homebrew Documentation: Software Supply Chain Security</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞维护者的长期奉献，提到像 mise 这样的替代工具用于开发环境，强调 Homebrew 在诸如 Universal Blue 的 Bazzite 等不可变 Linux 发行版上的实用性，并讨论了因 macOS 支持更好和用户体验而从 Nix 转过来的情况，同时也呼吁提供资金支持以维持这一由志愿者运行的项目。

**标签**: `#Homebrew`, `#package manager`, `#macOS`, `#Linux`, `#release`

---

<a id="item-3"></a>
## [文章认为人类努力而非仅靠 AI 输出才能赢得注意。](https://tombedor.dev/human-attention-and-human-effort/) ⭐️ 8.0/10

该文章发表在 tombedor.dev 上，指出要获得人类注意必须展示真实的人力努力，而不仅仅依赖 AI 生成的输出。文章引发了 Hacker News 上 106 条评论的讨论。 此观点凸显了 AI 辅助与人类贡献之间的紧张关系，影响软件工程中的代码审查和协作方式。它提醒团队在注意力经济中保持人类价值的重要性。 文章举例描述同事大量使用 Claude 生成的 PR 导致团队审查疲劳，评论中有人指出若工作 indistinguishable from machine，则可能被替代。还有评论建议应共享提示词以便追溯和改进。

hackernews · jjfoooo4 · Jun 11, 23:01 · [社区讨论](https://news.ycombinator.com/item?id=48497609)

**社区讨论**: 评论普遍同意过度依赖 AI 会导致审查不 attentive 以及被替代的焦虑，有人主张共享提示词以提高透明度。也有人强调需要在 AI 辅助与人工监督之间取得平衡，以保证质量和信任。

**标签**: `#AI in workplace`, `#human effort`, `#code review`, `#attention economy`, `#software engineering`

---

<a id="item-4"></a>
## [小米发布开源 MiMo Code AI 编程助手](https://mimo.xiaomi.com/mimocode) ⭐️ 8.0/10

小米已开源 MiMo Code V0.1.0，这是一个基于 OpenCode 分叉的终端原生 AI 编程助手，具备持久记忆、智能上下文管理、子代理编排和自主工作流功能。 此次开源提供了免费的开源替代方案，降低了切换成本，并使社区能够推动 AI 辅助软件工程的改进。 MiMo Code 支持连接任何主流 LLM，具备持久记忆系统以实现跨会话项目理解，并提供子代理编排以实现目标驱动的自主循环。

hackernews · apeters · Jun 11, 14:27 · [社区讨论](https://news.ycombinator.com/item?id=48490826)

**背景**: AI 编程助手常常在会话之间丢失上下文，限制了其在长期项目中的实用性。OpenCode 是一个开源的终端编程工具套件，提供 LSP、TUI、MCP 和插件支持。MiMo Code 在 OpenCode 的基础上添加了持久记忆、上下文管理和子代理编排，以实现连续的自我改进工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/XiaomiMiMo/MiMo-Code">GitHub - XiaomiMiMo/MiMo-Code</a></li>
<li><a href="https://www.gizmochina.com/2026/06/11/xiaomi-mimo-code-open-source-terminal-ai-coding-agent/">Xiaomi announces new AI coding agent that actually remembers ...</a></li>
<li><a href="https://www.eesel.ai/blog/subagent-orchestration">Subagent orchestration: The complete 2025 guide for AI workflows | eesel AI</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞向开源 AI 编程工具的转变，指出像 Claude Code 这样的闭源方案会增加切换成本并阻碍透明度。一些人强调了小米在 AI 领域的快速进步，指出其模型性能和定价具有竞争力。

**标签**: `#AI coding assistant`, `#open-source`, `#Xiaomi`, `#developer tools`, `#LLM agents`

---

<a id="item-5"></a>
## [Anthropic 为隐形 Claude Fable 护栏道歉](https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail) ⭐️ 8.0/10

Anthropic 道歉称，其 Claude Fable 5 模型被发现使用不可见的护栏，悄悄修改用户提示以防止 AI 蒸馏。 此事件凸显了 AI 安全机制中的透明度和信任问题，影响依赖模型输出的开发者，并引发对企业对 AI 系统控制的更广泛担忧。 这些护栏被称为‘隐形限速’，嵌入模型权重且不可审计，旨在阻止可能用于训练更小竞争模型的输出。

hackernews · rarisma · Jun 11, 12:05 · [社区讨论](https://news.ycombinator.com/item?id=48489229)

**背景**: AI 护栏是内置在模型中的安全机制，用于防止有害或不想要的输出。模型蒸馏是一种技术，即用较大模型的输出训练较小模型，以获得更廉价、专业化的版本。Claude Fable 5 是 Anthropic 的 Mythos‑class 模型，在 FrontierBench 上得分最高，并在发布时加入了不可见的护栏以抑制蒸馏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail">Anthropic apologizes for invisible Claude Fable guardrails | The Verge</a></li>
<li><a href="https://www.thenews.com.pk/latest/1405572-anthropic-explains-why-claude-fable-5s-safety-guardrails-were-invisible">Anthropic explains why Claude Fable 5's safety guardrails were invisible</a></li>
<li><a href="https://mindgard.ai/blog/outsmarting-ai-guardrails-with-invisible-characters-and-adversarial-prompts">Outsmarting AI Guardrails with Invisible Characters and Adversarial Prompts - Mindgard</a></li>

</ul>
</details>

**社区讨论**: 许多评论者将不可见的护栏比作软件秘密更改用户输入，认为这破坏了信任和可靠性。一些人认为 Anthropic 的道歉不够诚恳，指出隐藏的功能可能被重复使用，信任难以恢复。还有人认为此举具有 paternalism（家长式）倾向，表明公司更看重自身利益而非用户赋能。

**标签**: `#AI safety`, `#Claude`, `#guardrails`, `#transparency`, `#Anthropic`

---

<a id="item-6"></a>
## [Zed 推出 DeltaDB 以追踪 Git 提交之间的编辑](https://zed.dev/blog/introducing-deltadb) ⭐️ 8.0/10

Zed 宣布推出 DeltaDB，一种在每次 git 提交之间捕获所有操作的版本控制系统，以提供细粒度的编辑历史，帮助代码审查和调试。 通过保存提交之间易失的开发者意图，DeltaDB 能提升协作、调试和 AI 辅助工作流，有可能改变团队审查和维护代码的方式。 DeltaDB 使用 CRDT 增量记录更改，将编辑存储为具有稳定 ID 的增量，采用最后写入胜出的冲突解决策略，并在线上和离线均可工作，作为与 Zed 编辑器集成的离线优先数据库。

hackernews · jeremy_k · Jun 11, 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48492533)

**背景**: Git 以提交时的快照记录项目历史，这意味着提交之间的中间编辑和开发者思考未被保存。DeltaDB 通过使用无冲突复制数据类型（CRDT）持续记录每一次按键和操作作为增量来填补这一空白，使得更改即使在离线时也能同步。与频繁自动提交或结对编程不同，DeltaDB 提供可搜索的细粒度历史记录，保留编辑的确切顺序而不使主分支变得臃肿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shapeof.com/archives/2025/8/deltadb_from_zed.html">DeltaDB From Zed (the Code Editor) - shapeof.com</a></li>
<li><a href="https://github.com/delta-db/deltadb">GitHub - delta-db/deltadb: An offline-first database Zed Raises $32M in Series B, Pivots to DeltaDB, a GitHub ... Design & Construction for Social Impact | Delta DB |MS & AL Partnering with Zed: The AI-Powered Code Editor Built from ... DeltaDB is a new kind of version control. Where Git captures ...</a></li>

</ul>
</details>

**社区讨论**: 几位评论者称赞 DeltaDB 能捕捉“生成代码的对话”并保存提交信息中遗漏的开发者意图。其他人则批评该方法过于侵入性，认为细粒度的编辑只是噪声，而压缩提交、结对编程或频繁自动提交已经能够达到同样的目的。

**标签**: `#version-control`, `#developer-tools`, `#code-review`, `#delta-db`, `#software-engineering`

---

<a id="item-7"></a>
## [AMD 仅用弱 CRC-32 修补致 RCE 漏洞仍未修复。](https://mrbruh.com/amd2/) ⭐️ 8.0/10

一篇博客披露了 AMD 软件更新程序中的远程代码执行漏洞；AMD 的所谓补丁仅使用 CRC-32 校验而非加密签名验证，使更新过程仍然容易受到中间人攻击。 此漏洞使 AMD 用户面临供应链攻击风险，攻击者若能够劫持 AMD 的更新服务器或 DNS，即可分发能够通过弱 CRC-32 检查的恶意代码。这凸显了在固件和软件更新系统中采用强代码签名机制的必要性。 CRC-32 仅是一种错误检测码，而非加密哈希，易被伪造；AMD 的修复方案虽然启用了 HTTPS，但仅对下载的可执行文件进行 CRC-32 校验，攻击者可构造具有相同校验值的恶意载荷。利用此漏洞不需要真正的中间人攻击，DNS 缓存投毒等手段即可成功。

hackernews · MrBruh · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492215)

**背景**: CRC-32（循环冗余检验）是一种广泛使用的错误检测算法，能够检测意外的数据损坏，但对故意篡改没有安全保障。软件更新机制通常依赖加密签名或哈希来验证下载二进制文件的真实性和完整性。若缺乏此类保护，攻击者若能够拦截或伪造更新通道，便可替换仍能通过弱 CRC-32 检查的恶意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">Cyclic redundancy check - Wikipedia CRC-32 Calculator | CRC32 Formula, Polynomial & Examples Understanding CRC32 - Command Line Fanatic c - Fast CRC algorithm? - Stack Overflow CRC-32 - Google Open Source</a></li>
<li><a href="https://github.com/Michaelangel007/crc32">GitHub - Michaelangel007/crc32: CRC32 Demystified · GitHub</a></li>
<li><a href="https://fastercapital.com/content/Deep-Dive-into-CRC32--A-More-Robust-Error-Detection-Mechanism.html">Deep Dive into CRC32: A More Robust Error Detection Mechanism</a></li>

</ul>
</details>

**社区讨论**: 评论者批评 AMD 的修复方案过于弱弱，指出仅靠 HTTPS 无法防止篡改，且 DNS 缓存投毒即可利用该漏洞。多位用户回忆起 AMD 过去类似的软件质量问题，对供应商反复依赖不足的安全措施表示不满。

**标签**: `#security`, `#AMD`, `#RCE`, `#vulnerability`, `#MITM`

---

<a id="item-8"></a>
## [代码行数指标在 AI 代码生成热潮中被重新提及](https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/) ⭐️ 8.0/10

文章指出，在 AI 代码生成的热潮中，代码行数被重新提及作为生产力指标，引发了 Hacker News 上的详细讨论。 这种复兴凸显了依赖简单指标来衡量软件生产力的危险，特别是 AI 生成的代码可能会增加行数而未体现质量或可维护性。 讨论引用了 2026 年 2 月的一篇 OpenAI 博客文章，该文章多次提到一个拥有百万行代码的产品，并回忆了一位微软高管据称提出的每工程师每月一百万行代码的目标。

hackernews · RyeCombinator · Jun 11, 12:26 · [社区讨论](https://news.ycombinator.com/item?id=48489402)

**背景**: 代码行数（LoC）长期以来被视为衡量软件生产力的不佳指标，因为它奖励数量而非质量，且可通过微小改动被人为增加。AI 代码生成工具利用大型语言模型从自然语言提示生成源代码，常能快速产出大量代码。这种能力导致人们重新关注 LoC 作为易于测量的产出，尽管其已知不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-code-generation">What is AI code-generation? | IBM</a></li>
<li><a href="https://cloud.google.com/use-cases/ai-code-generation">AI Code Generation: Definition, Uses and Tools | Google Cloud</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对使用代码行数作为生产力指标持怀疑态度，指出 AI 生成的代码可能臃肿且难以维护。许多人指出，声称的 AI 驱动生产力提升常被用作裁员的借口，缺乏证据支持。还有人回顾了过去的争论，认为尽管有 AI 热潮，LoC 的根本问题并未改变。

**标签**: `#software engineering`, `#AI code generation`, `#productivity metrics`, `#lines of code`, `#Hacker News discussion`

---

<a id="item-9"></a>
## [基于有限状态自动机的情景约束记忆方法用于量化金融分析](https://arxiv.org/abs/2606.11223) ⭐️ 8.0/10

本文提出事件历史自动机（EHA），将正则表达式事件模式与数值区间结合，以建模具有记忆的受约束事件历史；并提出金融有限有权自动机（WFFA），其转移权重依赖于观测到的市场价值。通过计算 EHA 与 WFFA 的同步乘积，框架能够精确得到上下支付边界并提取实现极值的事件历史见证，并在可赎回结构性产品的案例研究中得到验证。 该方法为基于仿真的技术提供了数学上严格的替代方案，能够给出最坏情况和最好情况的穷尽界以及可解释的事件历史见证。这有助于提升风险管理以及对异权期权和结构性产品等路径依赖金融工具的验证。 事件历史自动机（EHA）将正则表达式事件模式与可接受的数值区间结合，以建模具有记忆的受约束事件历史；金融有限有权自动机（WFFA）则将转移权重设为观测到的市场价值的算术表达式。EHA 与 WFFA 的同步乘积得到一个有权自动机，其最短路径和最长路径问题的解即为精确的上下支付边界，对应路径即为实现极值的事件历史见证；可扩展性实验表明该方法在实际合约期限和非平凡约束下仍具可行性。

rss · arXiv Quantitative Finance · Jun 11, 04:00

**背景**: 有限状态自动机是具有有限状态集的抽象机器，根据输入符号在状态之间进行转移，用于建模离散事件序列。带权重（定量）的自动机在此基础上为转移分配数值权重，从而能够计算输入序列上的累积量，如成本或收益。在金融工程中，路径依赖工具（如异权期权和结构性产品）的收益取决于底层市场变量的完整历史，纯粹的仿真方法难以穷尽所有可能情景。本文的框架利用自动机概念将声明性情景约束编码进去，并计算出有保证的极端收益，为蒙特卡罗仿真提供了一种形式上的互补。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.11223v1">Scenario Constraints with Memory: A Finite-State Approach to ...</a></li>
<li><a href="https://arxiv.org/abs/2604.17370">[2604.17370] Weighted Automata and Regular Expressions for Financial Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Finite-state_machine">Finite-state machine - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#formal methods`, `#automata theory`, `#risk management`, `#financial engineering`

---

<a id="item-10"></a>
## [美国金融中介机构的信贷能力是巴西的三到六倍](https://arxiv.org/abs/2606.11566) ⭐️ 8.0/10

本文提出一种动态结构模型，利用 2002 年至 2025 年美国银行及信用合作社和巴西银行及合作社的监管数据估算中介机构的信贷能力。研究发现，美国的信贷能力是巴西的三到六倍，因而在美国发生资金冲击时贷款收缩更小且持续时间更短。 研究表明，基准信贷能力的差异而非其持续性是导致不同国家在资金冲击下贷款表现差异的主要因素，这为宏观审慎政策和跨境金融稳定评估提供了重要参考。政策制定者可以利用这些发现更好地预测流动性冲击的影响，并在不同司法管辖区设计更有效的危机应对措施。 该模型将信贷能力视为一种内生状态变量，用以决定资金中断对贷款供应的传导方式，并在机构层面进行估算。研究发现，信贷能力冲击的持续性在两国相近，但水平差异显著；反事实分析表明，水平差异解释了危机传播中观察到的大部分差异。

rss · arXiv Quantitative Finance · Jun 11, 04:00

**背景**: 信贷能力是指贷款机构根据借款人的收入和现有义务所认为的能够承受的新债务的最大额度。资金冲击是指短期融资续贷能力的突然中断，常导致机构被迫以折价出售资产甚至破产。金融中介机构包括银行、信用合作社、合作社等，它们将储蓄者的资金转移给借款人。动态结构模型能够描述此类状态变量随时间的演变及其对宏观经济的影响，而监管机构的监督数据则提供了估算这些变量所需的详细资产负债表信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.11566">[2606.11566] Credit Capacity and the Propagation of Funding Shocks: Evidence from U.S. and Brazilian Financial Intermediaries</a></li>
<li><a href="https://www.federalreserve.gov/econres/notes/feds-notes/assessing-bank-resilience-to-a-funding-shock-20260217.html">The Fed - Assessing Bank Resilience to a Funding Shock</a></li>
<li><a href="https://legalclarity.org/what-is-credit-capacity-and-how-is-it-calculated/">What Is Credit Capacity and How Do Lenders Measure It?</a></li>

</ul>
</details>

**标签**: `#finance`, `#banking`, `#credit capacity`, `#funding shocks`, `#cross-country comparison`

---

<a id="item-11"></a>
## [欧洲脱碳情景对关键可再生能源的原材料需求超过了储备](https://arxiv.org/abs/2606.12201) ⭐️ 8.0/10

该研究审查了 59 份高度脱碳的欧洲能源系统模型，并对五种关键可再生能源技术和 19 种材料的材料需求进行了定量的事后评估，发现镓、铟、铱、碲、银、硒和钒七种材料的需求超过了欧洲基于人口的全球储备份额。 这凸显了材料可行性的差距，表明仅依赖技术创新可能不足，需要能源效率、回收、储备扩张和充足性措施来实现脱碳目标。 分析还考虑了非能源需求的竞争，表明技术创新既可能缓解也可能加剧材料短缺，所识别的七种关键材料包括镓、铟、铱、碲、银、硒和钒。

rss · arXiv Quantitative Finance · Jun 11, 04:00

**背景**: 脱碳能源系统会扩大可再生能源部署，从而增加对镓、铟、铱、碲等关键原材料的需求，这些材料用于光伏、风电和储能技术。大多数能源系统模型侧重于排放和成本，常常忽视所需材料的实际可用性，这导致情景的可行性存疑。为评估地区限制，该研究按人口比例（人均）将全球储备分配给欧洲，并将这些份额与预测的材料需求进行比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12201">Materealistic? How European energy system models exceed raw ...</a></li>
<li><a href="https://www.energy.gov/cmm/what-are-critical-minerals-and-materials">What Are Critical Minerals and Materials ? | Department of Energy</a></li>
<li><a href="https://www.tugraz.at/fileadmin/user_upload/Events/Eninnov/EnInnov2026/files/pr/121_PR_Mutke.pdf">Material Feasibility of European Energy System Models</a></li>

</ul>
</details>

**标签**: `#energy systems`, `#raw materials`, `#decarbonization`, `#renewable energy`, `#material scarcity`

---

<a id="item-12"></a>
## [随机博弈框架将做市商与交易者通过 FBSDEs 联系](https://arxiv.org/abs/2504.06717) ⭐️ 8.0/10

作者将做市商与交易者的战略互动建模为随机博弈，用市场做商的内部报价策略替代外部永久价格冲击，并通过前向-后向随机微分方程（FBSDEs）刻纳什均衡。他们对一般博弈建立局部良好定义性结果，并通过将特定的 Almgren-Chriss-Avellaneda-Stoikov 模型解耦为带有 M_+矩阵系数的后向随机 Riccati 方程，实现全局良好定义性。 该框架统一了做市商与交易者相互影响的视角，为分析市场微观结构和设计最优执行策略提供了新工具。其良好定义性结果确保了模型的数学可靠性，可为量化金融的从业者和研究者提供指导。 对于一般随机博弈，作者证明了耦合 FBSDEs 的局部良好定义性；对于 Almgren-Chriss-Avellaneda-Stoikov 特定模型，通过解耦将其简化为系数矩阵为 M_+的后向随机 Riccati 方程，从而得到全局良好定义性。模拟表明，报价与战略交易者的订单呈负相关，而与噪声订单呈正相关。

rss · arXiv Quantitative Finance · Jun 11, 04:00

**背景**: 随机博弈建模了玩家之间的战略互动，每个玩家的决策会随时间影响他人的收益。前向-后向随机微分方程（FBSDEs）将前向状态过程与后向 adjoint 过程耦合，常用于随机控制和金融数学中以刻画均衡。Almgren-Chriss 模型描述了通过平衡市场冲击和波动率来实现大额订单的最优执行，而 Avellaneda-Stoikov 模型则关注做市商根据库存风险设定买卖报价。M_+矩阵是指非对角线元素非正且其逆矩阵非负的矩阵，这一性质在 Riccati 方程中保证稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/book/10.1007/978-3-540-48831-6">Forward-Backward Stochastic Differential Equations and their ...</a></li>
<li><a href="https://www.linkedin.com/pulse/understanding-almgren-chriss-model-optimal-portfolio-execution-pal-pmeqc">Understanding the Almgren-Chriss Model for Optimal Portfolio Execution</a></li>
<li><a href="https://deepwiki.com/fedecaccia/avellaneda-stoikov/2-avellaneda-stoikov-model">Avellaneda-Stoikov Model | fedecaccia/avellaneda-stoikov | DeepWiki</a></li>

</ul>
</details>

**标签**: `#market microstructure`, `#stochastic control`, `#optimal execution`, `#FBSDE`, `#Nash equilibrium`

---

<a id="item-13"></a>
## [FinTradeBench：包含 1400 题的 LLM 金融推理基准](https://arxiv.org/abs/2603.19225) ⭐️ 8.0/10

FinTradeBench 推出了一个包含 1,400 道题的基准，通过结合 NASDAQ‑100 公司十年内的基本面数据和交易信号来评估大型语言模型的金融推理能力。 该基准填补了现有金融问答数据集的空白，要求模型同时进行基本面文本和数值时间序列信号的推理，凸显了大型语言模型在数值和时序推理方面的不足。 问题分为基本面聚焦、交易信号聚焦和混合三类，基准采用校准‑然后‑放大框架，包含专家种子问题、多模型生成、自过滤、数值审计以及人机 LLM 判断对齐。

rss · arXiv Quantitative Finance · Jun 11, 04:00

**背景**: 金融推理通常需要同时解读公司文件（如 10‑K 和 10‑Q 报告）中的定性信息以及从股票价格变动中得出的定量信号，例如动量指标。纳斯达克 100 指数由纳斯达克上市的 100 家最大非金融公司组成，提供了丰富的历史价格和基本面数据。大型语言模型在基于文本的任务中表现出色，但在数值推理和时间序列分析方面存在不足，这就需要专门的基准来评估其能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.19225">[2603.19225] FinTradeBench: A Financial Reasoning Benchmark ...</a></li>
<li><a href="https://www.emergentmind.com/topics/fintradebench">FinTradeBench: Financial Reasoning Benchmark</a></li>
<li><a href="https://www.sec.gov/search-filings">Search Filings - SEC.gov</a></li>

</ul>
</details>

**标签**: `#LLM`, `#financial reasoning`, `#benchmark`, `#NASDAQ-100`, `#AI finance`

---