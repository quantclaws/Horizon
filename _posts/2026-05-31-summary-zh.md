---
layout: default
title: "Horizon Summary: 2026-05-31 (ZH)"
date: 2026-05-31
lang: zh
---

> From 16 items, 7 important content pieces were selected

---

1. [微软计划将永久授权的 Office 2019/2021 for Mac 转换为仅查看模式，时间定为 2026 年](#item-1) ⭐️ 8.0/10
2. [Zig ELF Linker Improvements Devlog](#item-2) ⭐️ 8.0/10
3. [Openrsync：OpenBSD 团队的安全 rsync 重新实现，使用 pledge 和 unveil](#item-3) ⭐️ 8.0/10
4. [OpenRouter 获得 1.13 亿美元 B 轮融资](#item-4) ⭐️ 8.0/10
5. [Leo's first encyclical attacks technological messianism](#item-5) ⭐️ 8.0/10
6. [Anthropic 详细说明 Claude 在各产品中的沙箱方案](#item-6) ⭐️ 8.0/10
7. [通过 Pyodide 和 Service Worker 在浏览器中运行 Python ASGI 应用](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软计划将永久授权的 Office 2019/2021 for Mac 转换为仅查看模式，时间定为 2026 年](https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)) ⭐️ 8.0/10

微软宣布，从 2026 年起，永久授权的 Office 2019 和 2021 for Mac 将自动切换为仅查看模式，禁用编辑功能但保留文档阅读能力。 此举破坏了永久授权的承诺，将用户推向基于订阅的 Microsoft 365，并在澳大利亚等司法管辖区引发消费者保护法的法律疑问。 仅查看转换将影响桌面应用（Word、Excel、PowerPoint、Outlook），但不会从设备中移除软件；切换后将不再提供功能更新或安全补丁。

hackernews · antipurist · May 30, 23:26 · [社区讨论](https://news.ycombinator.com/item?id=48341578)

**背景**: 永久 Office 许可证是一次性购买，用户期望软件能够无限期使用且不被强制更新。仅查看模式会禁用编辑功能，但仍允许用户打开和阅读文档，这通常用于试用或评估版本。在澳大利亚，消费者法律保证产品必须符合广告用途，并且买家享有不受干扰的占有权，若微软更改已售永久许可证的功能可能构成违法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)">Microsoft Office 2019 and 2021 for Mac view - only conversion (2026)</a></li>
<li><a href="https://licendi.com/en/blog/microsoft-office-perpetual-licenses-vs-subscriptions/">Microsoft Office perpetual licenses vs. subscriptions</a></li>
<li><a href="https://www.microsoft.com/licensing/guidance/Office-LTSC">Office LTSC Licensing Guidance - microsoft.com</a></li>

</ul>
</details>

**社区讨论**: 评论者强烈反对，呼吁用户停止购买微软软件并转向如 LibreOffice 之类的替代品。有人指出这可能侵犯澳大利亚的消费者保证，也有人猜测此举是为了让每个 AI 代理实例单独许可。总体而言，讨论将此变更视为反消费者的策略，可能加速用户远离永久许可证的趋势。

**标签**: `#Microsoft`, `#Office`, `#licensing`, `#consumer rights`, `#SaaS`

---

<a id="item-2"></a>
## [Zig ELF Linker Improvements Devlog](https://ziglang.org/devlog/2026/#2026-05-30) ⭐️ 8.0/10

Zig team shares progress on ELF linker enhancements aimed at faster compilation and positioning Zig as a viable C alternative.

hackernews · kristoff_it · May 30, 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48338673)

**标签**: `#Zig`, `#ELF linker`, `#compiler improvements`, `#systems programming`, `#language development`

---

<a id="item-3"></a>
## [Openrsync：OpenBSD 团队的安全 rsync 重新实现，使用 pledge 和 unveil](https://github.com/kristapsdz/openrsync) ⭐️ 8.0/10

Openrsync 是由 OpenBSD 团队开发的 rsync 新实现，利用 pledge(2) 和 unveil(2) 系统调用增强安全性。 它提供了比传统 rsync 更安全的替代方案，尤其适用于需要严格限制系统访问的环境，并展示了 OpenBSD 的安全创新。 Openrsync 使用 pledge 限制程序的系统能力，使用 unveil 限制可见的文件系统路径，并且该项目正在作为 RPKI 验证器开发的一部分进行。

hackernews · sph · May 30, 10:51 · [社区讨论](https://news.ycombinator.com/item?id=48334854)

**背景**: OpenBSD 的 pledge() 系统调用允许进程承诺仅使用有限的一组系统资源，从而降低被攻击的影响。unveil() 系统调用限制进程可以访问的文件系统部分，将其余部分隐藏起来。二者共同提供了一种深度防御机制，即使程序被利用也能限制其可执行操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://man.openbsd.org/pledge">pledge (2) - OpenBSD manual pages</a></li>
<li><a href="https://man.openbsd.org/unveil">unveil (2) - OpenBSD manual pages</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD_security_features">OpenBSD security features - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏 Openrsync 的进展和安全重点，指出其可用性不断提升；有人指出与 Samba rsync 的微小兼容性差距，而其他人则强调其在 RPKI 验证器开发中的作用，并讨论 pledge 和 unveil 的重要性，少数人质疑 pledge 在 Linux 上的可用性。

**标签**: `#rsync`, `#OpenBSD`, `#security`, `#open-source`, `#file-synchronization`

---

<a id="item-4"></a>
## [OpenRouter 获得 1.13 亿美元 B 轮融资](https://openrouter.ai/announcements/series-b) ⭐️ 8.0/10

OpenRouter 宣布完成 1.13 亿美元 B 轮融资，以扩展其 LLM 代理服务，该服务提供统一 API 访问多种语言模型并内置计费上限。 这笔巨额投资表明投资者对 LLM 聚合平台充满信心，预示着统一模型访问工具在开发者中的采用将进一步加速。 OpenRouter 表示将保持创始人领导和控制，长期服务全球开发者；其代理服务最大特点是提供低门槛的模型试用以及硬性计费上限。

hackernews · freeCandy · May 30, 17:27 · [社区讨论](https://news.ycombinator.com/item?id=48338660)

**背景**: LLM 代理服务充当一个网关，提供统一的（通常是 OpenAI 兼容的）API，将请求路由到不同的语言模型供应商，从而免去管理多个供应商 SDK 的麻烦。这些代理可以在不改动代码的情况下增加计费上限、缓存、故障转移和使用分析等功能。例如 LiteLLM Proxy 和 Arbio 的云端 LLM 代理展示了统一接口如何简化模型试用和成本控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://litellm.vercel.app/docs/providers/litellm_proxy">LiteLLM Proxy ( LLM Gateway) | liteLLM</a></li>
<li><a href="https://www.arbio.ai/">Secure LLM Proxy Service | Arbio</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 OpenRouter 低门槛尝试众多模型以及计费上限的价值，部分人最初对代理的必要性持怀疑态度。创始人兼 COO 强调公司将保持创始人领导，而用户则指出该服务便于试用新模型，但对通过平台路由昂贵模型的成本效益表示疑问。

**标签**: `#AI`, `#LLM`, `#funding`, `#developer tools`, `#OpenRouter`

---

<a id="item-5"></a>
## [Leo's first encyclical attacks technological messianism](https://www.economist.com/europe/2026/05/28/leos-first-encyclical-attacks-technological-messianism) ⭐️ 8.0/10

Pope Leo's first encyclical critiques the belief that technology, especially AI, can serve as a messianic savior, urging ethical caution.

hackernews · 1vuio0pswjnm7 · May 30, 10:30 · [社区讨论](https://news.ycombinator.com/item?id=48334710)

**标签**: `#AI ethics`, `#religion`, `#technology criticism`, `#papal encyclical`, `#techno-optimism`

---

<a id="item-6"></a>
## [Anthropic 详细说明 Claude 在各产品中的沙箱方案](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything) ⭐️ 8.0/10

Anthropic 发布了详细说明，说明他们如何在 Claude.ai、Claude Code 和 Cowork 中使用 gVisor、Seatbelt 和 Bubblewrap 对 Claude 进行沙箱隔离。 这种透明度有助于开发者和安全从业者评估 AI 代理的安全性，并为生成式 AI 系统的沙箱最佳实践提供参考。 Claude.ai 使用 gVisor，Claude Code 在 macOS 上使用 Seatbelt，在 Linux 上使用 Bubblewrap，而 Claude Cowork 在 macOS 上通过 Apple 虚拟化框架运行完整 VM，在 Windows 上使用 HCS。

rss · Simon Willison · May 30, 21:36

**背景**: 沙箱通过限制进程对系统资源的访问来实现隔离，从而降低恶意或意外行为的风险。gVisor 是一种用户空间内核，它拦截系统调用，提供类似容器的隔离而无需完整虚拟机。Seatbelt 是 macOS 的强制访问控制框架，在内核级别限制文件系统、网络和系统调用；Bubblewrap 则利用 Linux 名称空间创建非特权容器。完整虚拟机（如 Claude Cowork 所用）通过 hypervisor（如 Apple 的虚拟化框架或 Windows 的 HCS）运行独立的虚拟机，提供最强的隔离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GVisor">gVisor - Wikipedia</a></li>
<li><a href="https://deepwiki.com/waywardgeek/gemini-cli/11.2-macos-seatbelt-sandboxing">macOS Seatbelt Sandboxing | waywardgeek/gemini-cli | DeepWiki</a></li>
<li><a href="https://wiki.archlinux.org/title/Bubblewrap">Bubblewrap - ArchWiki</a></li>

</ul>
</details>

**标签**: `#sandboxing`, `#AI safety`, `#Anthropic`, `#Claude`, `#security`

---

<a id="item-7"></a>
## [通过 Pyodide 和 Service Worker 在浏览器中运行 Python ASGI 应用](https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything) ⭐️ 8.0/10

Simon Willison 演示了如何将 Pyodide 与 Service Worker 结合，在浏览器中运行 Python ASGI 应用，克服了之前 JavaScript 脚本无法执行的限制。他提供了 ASGI FastCGI 演示和运行 Datasette 1.0a31 的演示。 此进展使客户端 Python Web 应用能够完整执行 JavaScript，从而支持之前受限的插件和交互功能。它扩展了 ASGI 框架（如 Datasette）在浏览器中构建富交互工具的可能性。 该方案利用 Service Worker 的 fetch 事件拦截网络请求，提供由 Pyodide 中运行的 ASGI 应用生成的 HTML，从而使 <script> 标签得以执行。Simon 在 Claude Opus 4.8 的帮助下制作了原型，并计划将其集成到 Datasette Lite。

rss · Simon Willison · May 30, 21:02

**背景**: Pyodide 将 CPython 解释器编译为 WebAssembly，使得 Python 代码能够直接在浏览器中运行，并可使用 NumPy、Pandas 等库。ASGI（异步服务器网关接口）是 WSGI 的继承者，提供了异步 Python Web 服务器、框架和应用之间的标准接口。Service Worker 是运行在后台的脚本，能够拦截 fetch 事件以修改或提供网络响应，从而实现客户端请求处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.com/">Pyodide – Run Python in Browser with WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface">Asynchronous Server Gateway Interface - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event">ServiceWorkerGlobalScope: fetch event - Web APIs | MDN</a></li>

</ul>
</details>

**标签**: `#Pyodide`, `#ASGI`, `#WebAssembly`, `#Service Workers`, `#Datasette`

---