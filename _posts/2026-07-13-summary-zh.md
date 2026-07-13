---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> From 13 items, 3 important content pieces were selected

---

1. [Chromium 148 的 Math.tanh 通过 JavaScript 指纹泄露操作系统。](#item-1) ⭐️ 8.0/10
2. [陶哲轩使用 LLM 编码代理构建教育应用。](#item-2) ⭐️ 8.0/10
3. [乔治·霍茨批评 LLM 炒作并警告估值被高估。](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Chromium 148 的 Math.tanh 通过 JavaScript 指纹泄露操作系统。](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 8.0/10

从 Chromium 148 开始，V8 引擎将 Math.tanh 从捆绑的 fdlibm 实现切换为宿主操作系统的原生 libm，导致不同操作系统产生不同的浮点结果，可通过 JavaScript 读取。 这一细微差异产生了一个新的浏览器指纹向量，使网站能够推断用户的底层操作系统，可能削弱隐私保护和 User‑Agent 欺骗。 此更改使 Math.tanh 成为 Chromium 148 中唯一一个随操作系统变化的标准 JavaScript Math 函数，而其他 Math 函数仍然使用捆绑的 fdlibm，因而保持 OS 独立。

hackernews · joahnn_s · Jul 12, 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 在 Chromium 148 之前，V8 使用可移植的 fdlibm 实现来计算 Math.tanh，在所有操作系统上得到相同的结果。从版本 148 开始，V8 将计算委托给平台的 libm 库，这导致在 Linux、macOS 和 Windows 上的某些输入产生略微不同的最后位值。由于 IEEE 754 标准不对超越函数的正确舍入提出要求，这些微小差异可以通过 JavaScript 测量并用作指纹信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scrapfly.dev/posts/browser-math-os-fingerprint/">Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev</a></li>
<li><a href="https://geekhaus.club/feed/2026/07/12/chrome-s-switch-to-os-native-math-tanh-exposes-a">Chrome’s switch to OS-native Math.tanh exposes a subtle ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/system.math.tanh?view=net-10.0">Math.Tanh (Double) Method (System) | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，一次 tanh 调用即可揭示操作系统，甚至可能暗示浏览器版本范围；也有人质疑文章的动机，认为它来自一家爬虫服务公司。另一些评论欢迎这一技术洞见，建议推动正确舍入的超越函数，并指出即使像 Tor 这样的隐私浏览器也基本放弃了隐藏操作系统的努力。

**标签**: `#browser fingerprinting`, `#JavaScript`, `#privacy`, `#Chromium`, `#OS detection`

---

<a id="item-2"></a>
## [陶哲轩使用 LLM 编码代理构建教育应用。](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 8.0/10

在 2026 年 7 月的博客文章中，菲尔兹奖得主陶哲轩描述了他如何使用现代 LLM 编码代理来创建交互式可视化和小型教学应用，同时指出了这种方法的生产力提升及其当前局限。 陶哲轩的经历表明，LLM 驱动的编码代理正成为非传统软件工程领域专家的实用工具，有望跨学科加速教育内容的创作。 他特别提到使用 Claude 在几天内设计了一个简化的 8 位计算机可视化，并指出虽然 LLM 生成的代码提高了生产力，但仍需要人工监督以确保正确性和集成。

hackernews · subset · Jul 12, 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: 现代 LLM 编码代理已经超越简单的自动补全，能够根据自然语言提示生成完整功能、调试复杂问题、重构遗留代码甚至自主部署更改。2026 年，存在多种成熟工具如 OpenCode、Gemini CLI 和 Codex，它们支持数十种 LLM 提供者以及通过 Ollama 和 LM Studio 等平台使用本地模型。这些 AI 辅助编程系统旨在增强而非取代人类程序员的生产力，但仍然需要人工验证和集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.morphllm.com/best-ai-coding-agents-2026">Best AI Coding Agents (June 2026): Scored Leaderboard</a></li>
<li><a href="https://openagents.org/blog/posts/2026-05-21-best-ai-coding-agents">10 Best AI Coding Agents in 2026 — Complete Guide ...</a></li>
<li><a href="https://benchlm.ai/coding">Best LLMs for Coding — July 2026 Leaderboard | BenchLM.ai</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 LLM 编码代理能够快速创建教育可视化并填补教学资源的空白，同时指出这些工具最适合非关键任务且仍需人工监督。一些人强调了非传统领域对软件的巨大未被满足的需求，认为即使是当前的能力也需要数年才能完全消化。还有人用幽默的类比，将这种体验比作米其林星级厨师发现微波餐，突显了对 AI 生成代码的兴奋与怀疑。

**标签**: `#LLM`, `#coding agents`, `#AI-assisted programming`, `#software engineering`, `#Terry Tao`

---

<a id="item-3"></a>
## [乔治·霍茨批评 LLM 炒作并警告估值被高估。](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

在 2026 年 7 月 12 日的博客文章中，乔治·霍茨认为虽然大型语言模型确实有用，但围绕它们的炒作导致前沿 AI 实验室的估值被夸大，并讨论了这对生产力和开源软件的影响。 他的批评凸显了 AI 投资炒作与实际价值捕获之间日益扩大的脱节，警告投资者和开发者当前估值可能不可持续。 霍茨指出，前沿实验室每月收取 100–200 美元以获得有限的 token 使用量，暗示用户为有限访问支付了溢价，并且他观察到生产力提升往往表现为私人的一次性工具而非广泛的软件。

hackernews · therepanic · Jul 12, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: 像 GPT‑4 和 Claude 这样的大型语言模型推动了 AI 初创公司估值的激增，投资者押注其变革性经济影响。前沿实验室常通过 API 订阅变现，声称能带来跨行业的大幅生产力提升。与此同时，开源社区利用 LLM 加速软件开发，但对模型可靠性和炒作驱动的融资可持续性仍有担忧。

**社区讨论**: 评论者普遍同意霍茨对估值被夸大的怀疑，指出当前的订阅读的订阅价格使前沿模型对许多用户来说是‘不二之选’。一些人提出开源担忧，认为轻松 fork LLMs 减少了贡献上游的动机，而其他人则强调他们通过 LLM 构建利基一次性工具获得的个人生产力提升。

**标签**: `#LLMs`, `#AI hype`, `#valuation`, `#open source`, `#productivity`

---