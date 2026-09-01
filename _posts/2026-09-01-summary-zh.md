---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> From 22 items, 4 important content pieces were selected

---

1. [社区策划的 ChatGPT Work 工具参考指南，包含 Playwright 浏览器控制技能](#item-1) ⭐️ 8.0/10
2. [谷歌从 Chrome 网上应用店移除 Manifest V2 扩展](#item-2) ⭐️ 8.0/10
3. [防泄漏、搜索感知的系统纠正 LLM 交易策略偏差](#item-3) ⭐️ 8.0/10
4. [AI 代理削弱搜索中的位置偏差，更看重页面属性而非排名](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [社区策划的 ChatGPT Work 工具参考指南，包含 Playwright 浏览器控制技能](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 8.0/10

一个社区策划的 ChatGPT Work 参考指南已发布，展示了一个通过 Node.js REPL 使用 Playwright 控制浏览器的技能。该指南包含启动 Playwright 并通过 ChatGPT Work 检索浏览器文档的示例代码。 该参考指南提供了超越 ChatGPT Work 默认功能的实际扩展方式，展示了开发者如何集成浏览器自动化并减少对耗费大量 token 的手动操作的依赖。它还引发了关于 ChatGPT Work 与 Codex 的区别以及 token 使用效率的讨论。 该 Playwright 技能演示了如何启动浏览器实例、向其 Node.js REPL 写入数据以及调用 browser.documentation() 检索详细使用说明。该指南托管在 https://codex-tool-reference.simonw.chatgpt.site/，并包含社区关于 token 成本及与 Codex 比较的讨论。

hackernews · ijidak · Aug 31, 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49510000)

**背景**: ChatGPT Work 是一种工具，能够收集上下文、规划操作，并在应用、文件和桌面程序之间执行任务以生成电子表格、文档和幻灯片，由 GPT-5.6 驱动。Playwright 通过直接使用 DevTools 协议与浏览器通信，实现可靠的浏览器控制，使得导航、输入等命令能够在浏览器就绪时执行。这相比依赖抽象层的框架减少了不稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chatgpt.com/work/">ChatGPT Work for Every Team</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://www.browserstack.com/guide/playwright-vs-robot-framework">Playwright vs Robot Framework: How They Compare... | BrowserStack</a></li>

</ul>
</details>

**社区讨论**: Simonw 强调了该指南中最有趣的浏览器控制技能。Satvikpendem 质疑这与 Codex 有何区别，而 darepublic 警告某些工具可能会浪费大量 token。Enraged_camel 指出 AI 生成的网站往往外观相似，这让人想起早期 Bootstrap 时代的网站。

**标签**: `#ChatGPT`, `#AI tooling`, `#Playwright`, `#developer reference`, `#Hacker News`

---

<a id="item-2"></a>
## [谷歌从 Chrome 网上应用店移除 Manifest V2 扩展](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已从 Chrome 网上应用店下架所有 Manifest V2 扩展，包括广告拦截插件 uBlock Origin。 此举影响依赖 MV2 的广告拦截用户，促使他们转向 Firefox 或 MV3 版的 uBlock Origin Lite，凸显了谷歌对浏览器扩展生态的单方面控制。 Manifest V2 正被淘汰，取而代之的是施加更严格功能限制的 Manifest V3；uBlock Origin Lite 是目前在 Chrome 网上应用店提供的 MV3 兼容版本。

hackernews · twapi · Aug 31, 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 是 Chrome 旧版扩展框架，自 2020 年起 Chrome 就开始逐步淘汰，Chrome 网上应用店不再接受新的 MV2 提交。根据谷歌的时间表，MV2 扩展的支持将从 2025 年 6 月起在企业用户中被移除，随后逐步对所有用户生效，并在 2026 年 6 月的 Beta、Dev 和 Canary 渠道出现警告横幅。目前超过 85% 的积极维护扩展已迁移至 Manifest V3，主要内容拦截插件也提供了 MV3 版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://blog.google/chromium/manifest-v2-phase-out-begins/">Manifest V2 phase-out begins</a></li>
<li><a href="https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en">uBlock Origin Lite - Chrome Web Store</a></li>

</ul>
</details>

**社区讨论**: 评论者担心移除如 uBlock Origin 这样的 MV2 扩展会削弱对恶意广告的防护，尤其是对不太熟悉技术的用户。许多人表示他们将转向 Firefox 或使用分支版本，以避免谷歌对浏览器生态的单方面控制。还有人指出 uBlock Origin 在 Firefox 上表现更好，建议尽早迁移。

**标签**: `#Chrome`, `#Manifest V2`, `#Ad blocking`, `#Browser extensions`, `#Privacy`

---

<a id="item-3"></a>
## [防泄漏、搜索感知的系统纠正 LLM 交易策略偏差](https://arxiv.org/abs/2608.27734) ⭐️ 8.0/10

本文提出了一种防泄漏、搜索感知的系统，用于 LLM 驱动的交易策略发现，通过注册验证的工具在构造上排除前视偏差，并采用试验次数通缩来校正搜索强度。该方法在包含真实交易、冲击和借贷成本的 453 只美股点-in-time 宇宙和 39 只 ETF 多资产宇宙上进行评估，测试了两个前沿 LLM，最多 100 个候选策略，重复五次。 通过在结构上修正前视偏差和搜索过拟合，该工作解决了 LLM 金融研究中众所周知的方法论缺陷，提升了所发现策略的可信度。这对开发 LLM 交易工具的学者和依赖稳健策略验证的从业者都有益处。 该系统将代理限制在注册验证的工具上，这些工具的特征空间由构造排除前视信息，并记录每次策略评估，以试验次数通缩报告的表现，使用脱胎夏普比率和回测过拟合概率测试。即使是故意泄漏的预言机发出夏普比率 35 也无法通过这些测试；诚实评估在不同模型和搜索预算下拒绝所有 LLM 发现的策略，同时认证被动基准并在相同条件下评估人类交易者的规则系统。

rss · arXiv Quantitative Finance · Aug 31, 04:00

**背景**: 大型语言模型被越来越多地用于挖掘交易策略，但常见的流程会生成许多候选者，仅报告最佳者，却忽略前视偏差以及因搜索众多可能性而导致的性能通胀。脱胎夏普比率通过考虑独立试验的数量来校正原始表现，而回测过拟合的概率则衡量策略样本内优势归因于运气的可能性。注册验证的工具限制模型只能使用预先批准、无偏的函数，使得这种校正成为结构性的而非程序性的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quanterlab.com/articles/qlway-deflated-sharpe">The Deflated Sharpe Ratio: correcting for how many tries you took - QuanterLab</a></li>
<li><a href="https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf">THE PROBABILITY OF BACKTEST OVERFITTING David H. Bailey ∗ Jonathan M. Borwein †</a></li>
<li><a href="https://github.com/TauricResearch/TradingAgents">TauricResearch/TradingAgents: TradingAgents: Multi-Agents LLM ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#trading strategies`, `#look-ahead bias`, `#financial AI`, `#methodology`

---

<a id="item-4"></a>
## [AI 代理削弱搜索中的位置偏差，更看重页面属性而非排名](https://arxiv.org/abs/2608.22697) ⭐️ 8.0/10

该研究在 5000 次会话中随机化了 100 家酒店列表的顺序，使用四个大型语言模型作为 AI 代理，并将其行为与人类实地数据进行比较。结果显示，AI 代理检查结果的深度超过人类，从不放弃购买，并且表现出削弱且非单调的位置偏差，即列表中间的检查概率最低。 了解 AI 代理如何改变搜索行为对于设计在人类将搜索委托给 AI 时仍然有效的推荐和广告系统至关重要。结果表明，优化页面级属性可能比微调位置排名带来更好的回报。 该实验使用了四个未指定版本的大型语言模型来模拟 AI 代理，每个模型完成了 5000 次随机化会话；代理从未选择退出购买，并且收敛于同一个未被支配的酒店。位置对检查概率的影响较弱且非单调，列表中间的检查率最低，而底部的检查率高于中间。

rss · arXiv Quantitative Finance · Aug 31, 04:00

**背景**: 在传统的网络搜索中，排名较高的项目获得更多关注，因为用户会顺序扫描结果且时间有限，从而产生强烈的位置偏差。由大型语言模型驱动的 AI 代理可以一次性处理整个结果页面，从而可能减少对位置的依赖。本研究考察这种能力是否改变了用户（通过代理）的选择方式。它还凸显了 AI 中介搜索在电子商务和信息检索中的日益重要作用。

**标签**: `#AI agents`, `#search ranking`, `#position bias`, `#large language models`, `#human-computer interaction`

---