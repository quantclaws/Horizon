---
layout: default
title: "Horizon Summary: 2026-06-21 (ZH)"
date: 2026-06-21
lang: zh
---

> From 13 items, 5 important content pieces were selected

---

1. [Loupe iOS 应用揭示原生应用可访问数据以突显隐私指纹](#item-1) ⭐️ 8.0/10
2. [SMPTE 将其标准库免费向全球开放](#item-2) ⭐️ 8.0/10
3. [Linux 内核在六年工作后移除不安全的 strncpy API](#item-3) ⭐️ 8.0/10
4. [晦涩悲伤词典的全盘抄袭](#item-4) ⭐️ 8.0/10
5. [Bun 提出为 JavaScriptCore 添加共享内存线程以实现真正多线程](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Loupe iOS 应用揭示原生应用可访问数据以突显隐私指纹](https://github.com/mysk-research/loupe) ⭐️ 8.0/10

Loupe 是由 mysk-research 在 GitHub 上发布的 iOS/iPadOS 应用，通过读取公开的 iOS API 并显示原始值来演示原生应用可访问的数据。 该应用突出了 iOS 特定的隐私泄漏（如音量创建日期和最后设置时间戳），这些泄漏可用于设备指纹识别，提高用户意识并促使 Apple 改进隐私保护。 Loupe 访问的 API 包括音量创建日期、设备擦除/设置时间、粘贴板变更计数以及已安装应用探测，展示看似无害的数据如何被组合用于指纹识别；它仅可视化这些泄漏而不进行阻止或缓解。

hackernews · Cider9986 · Jun 20, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48608645)

**背景**: iOS 设备指纹识别依赖于收集看似无害的硬件和软件信号——例如音量创建日期、粘贴板变更计数和已安装应用列表——以在未经用户同意的情况下唯一标识设备。近期研究已经梳理了这些信号，并探索了通过静态和动态分析应用来检测指纹的方法。Loupe 应用通过直接调用第三方应用也能访问的公开 iOS API，并将原始值呈现给用户，从而实现了这一研究的透明化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mysk-research/loupe">GitHub - mysk-research/loupe: A privacy-focused iOS app that ...</a></li>
<li><a href="https://blog.appicaptor.com/2023/06/29/device-fingerprinting-on-ios-apps/">Device Fingerprinting on iOS apps - Appicaptor Blog</a></li>
<li><a href="https://dl.acm.org/doi/fullHtml/10.1145/3590777.3590790">Towards detecting device fingerprinting on iOS with API ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出令人担忧的泄漏，如 iPhone 的最后设置或擦除时间戳和音量创建日期，并质疑用户能做何来缓解。其他人称赞 Loupe 满足了长期需求，指出限制安装的应用数量可以降低风险，并警告 TikTok、Facebook 等平台嵌入的 SDK 仍能在重新安装后关联活动，呼吁 Apple 对这些指纹进行随机化。

**标签**: `#iOS`, `#privacy`, `#security`, `#mobile`, `#fingerprinting`

---

<a id="item-2"></a>
## [SMPTE 将其标准库免费向全球开放](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community) ⭐️ 8.0/10

SMPTE 已经开放其全部标准库，免费提供所有已发布的 SMPTE 标准、推荐做法、工程指南和注册披露文件。 此举降低了开发者和工程师的门槛，促进了媒体技术生态系统的创新和互操作性，并符合行业向开放标准发展的趋势。 该库包含超过 800 项技术标准及相关文件，现通过 SMPTE 网站免费提供，作为组织现代化工作的一部分，采用了基于 GitHub 的工作流程、HTML 编写和集成出版流程，未来发布也将免费。

hackernews · zdw · Jun 20, 17:01 · [社区讨论](https://news.ycombinator.com/item?id=48610827)

**背景**: SMPTE 成立于 1916 年，是一个全球专业协会，负责为电影、电视和数字媒体技术制定标准。历来，其标准文件以 PDF 或印刷版出售，获取受限。通过免费提供标准，SMPTE 效仿 IETF 等开放标准组织的模式，旨在提高采用率和协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Society_of_Motion_Picture_and_Television_Engineers">Society of Motion Picture and Television Engineers - Wikipedia</a></li>
<li><a href="https://www.smpte.org/">SMPTE | The home of media professionals, technologists, and engineers</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎此决定，称赞这是迟到的开放举措，并将其比作 IETF 的开放标准模式；有人分享了以前购买标准 PDF 的个人经历，其他人则指出伴随的现代化工作，如 GitHub 工作流程，还有一条离题的评论提到了一张音乐专辑。

**标签**: `#SMPTE`, `#open standards`, `#media technology`, `#standards accessibility`, `#HackerNews`

---

<a id="item-3"></a>
## [Linux 内核在六年工作后移除不安全的 strncpy API](https://www.phoronix.com/news/Linux-7.2-Drops-strncpy) ⭐️ 8.0/10

Linux 内核开发者在历时六年、约 360 个补丁的工作后，彻底移除了 strncpy 函数，该更改已并入 Linux 7.2。 移除不安全的 strncpy API 能够减少内核中长期存在的错误和安全漏洞，从而提升依赖内核的系统可靠性和安全性。 此次移除涵盖了所有架构特定的 strncpy 实现，历经约 362 次提交，解决了 strncpy 无法保证空终止以及容易填充零的问题。

hackernews · simonpure · Jun 20, 20:59 · [社区讨论](https://news.ycombinator.com/item?id=48612943)

**背景**: strncpy 函数本意是按长度限制复制字符串，但它不能保证结果以空字符终止，并且会用零填充目标缓冲区，这可能导致错误和安全问题。Linux 内核在 Documentation/process/deprecated.html 中维护了一份废弃接口列表，以 discourage 使用不安全的 API。过去六年里，贡献者们在内核中用更安全的、显式长度检查的字符串复制替换了 strncpy。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.2-Drops-strncpy">Linux Finally Eliminates The strncpy API After Six Years Of Work, 360+ Patches - Phoronix</a></li>
<li><a href="https://developer.apple.com/forums/thread/658049">Security threat due to insecure function "strncpy ...</a></li>
<li><a href="https://docs.kernel.org/process/deprecated.html">Deprecated Interfaces, Language Features, Attributes, and Conventions — The Linux Kernel documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这项历时多年的清理工作是系统工程中的真正贡献，认为移除不良特性与添加新特性对内核这样的基础项目同样重要。一些人建议使用类似 C++ std::string 的带长度指针的方案，而另一些人则认为以空字符终止的字符串是历史上的错误。

**标签**: `#Linux`, `#kernel`, `#strncpy`, `#API removal`, `#systems programming`

---

<a id="item-4"></a>
## [晦涩悲伤词典的全盘抄袭](https://waxy.org/2026/06/the-wholesale-plagiarism-of-obscure-sorrows/) ⭐️ 8.0/10

一个名为 Qontour 的网站被指控全文复制了约翰·科尼格的《晦涩悲伤词典》，并使用 AI 工具进行再品牌化，随后通过 Amazon Associates 联盟链接变现。 此案凸显 AI 如何助长大规模抄袭，考验 DMCA 下架的有效性，并为开发者、出版商和平台带来伦理问题。 盗版站点逐字复制了书籍的 800 词前言及全部 311 个新造词，使用 Amazon Associates tag=promptdigital-20 获得推荐费，并宣称是 Webflow 高级合作伙伴，实际上可能只是在 AI 再品牌化步骤后直接复制粘贴。

hackernews · ridesisapis · Jun 20, 18:05 · [社区讨论](https://news.ycombinator.com/item?id=48611411)

**背景**: 《晦涩悲伤词典》是约翰·科尼格创作的一本收录用于描绘细微情感的造词集，由西蒙与舒斯特于 2021 年出版。Templafy 或 VIM Group 等 AI 再品牌化工具可以生成或迁移文本并使其适应新的品牌形象，但也可能被用来洗白抄袭内容。DMCA 为版权持有者提供了请求删除侵权材料的法律途径，但执行往往需要法院命令，谷歌和苹果等平台在没有命令的情况下可能会忽略下架通知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.templafy.com/rebranding-in-the-ai-era-key-strategies-and-insights/">Rebranding in the AI era: Key strategies and insights - Templafy</a></li>
<li><a href="https://coderfile.io/dmca">DMCA Policy & Takedown Procedure - CoderFile.io</a></li>
<li><a href="https://copyleaks.com/">AI Content & Text Authenticity Detection | Copyleaks</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了自己作品被复制并用 AI 重新品牌化的类似经历，批评平台处理 DMCA 下架无效，指出了通过 Amazon Associates 联盟链接盈利的方式，并呼吁追究责任，也有评论者认为 DMCA 下架正是为此类情况而设。

**标签**: `#plagiarism`, `#copyright`, `#AI`, `#intellectual property`, `#Hacker News`

---

<a id="item-5"></a>
## [Bun 提出为 JavaScriptCore 添加共享内存线程以实现真正多线程](https://github.com/oven-sh/WebKit/pull/249) ⭐️ 8.0/10

Bun 已提交一个大型拉取请求，向 JavaScriptCore 添加共享内存线程，引入新的 Thread() 原语，使闭包能够在独立的 OS 线程上运行同时共享同一 JavaScript 堆。该 PR 旨在为 JavaScript 带来真正的多线程能力。 真正的共享内存多线程将使 JavaScript 程序能够在不经过消息传递开销的情况下利用多核 CPU，从而可能提升计算密集型任务的性能。如果成功，这可能会影响更广泛的 JavaScript 生态系统，并减少对 Web Worker 或原生插件等变通方案的依赖。 该 PR 修改了 JavaScriptCore，公开一个接受函数的 Thread 构造函数，在独立的 OS 线程上运行并完全访问共享的 JS 堆，因而需要谨慎同步以避免数据竞争。该 PR 仍在审查中，尚未合并到 Bun 的主分支。

hackernews · gr4vityWall · Jun 20, 17:02 · [社区讨论](https://news.ycombinator.com/item?id=48610841)

**背景**: Bun 是一个 JavaScript 运行时、包管理器和测试运行器，它使用苹果的 JavaScriptCore 引擎而非 V8，旨在成为 Node.js 的快速替代品。JavaScriptCore 是驱动 Safari 的 JavaScript 引擎，也是 Bun 运行时所使用的引擎。共享内存线程允许多个线程直接访问相同的内存空间，这与传统的通过消息传递进行通信的 Web Worker 不同。在 JavaScriptCore 中实现此类线程将使单一 JavaScript 环境能够实现真正的并行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://byteiota.com/bun-new-thread-javascript-multithreading/">Bun’s new Thread () PR: JS Gets True Multithreading | byteiota</a></li>

</ul>
</details>

**社区讨论**: 评论者对 JavaScript 实现真正多线程的前景表示兴奋，但许多人对该 PR 的可信度表示担忧，特别是因为它是由 AI 生成且涉及大量文件更改。其他人则强调需要严格的正确性，并警告 AI 生成的代码可能不可靠，尤其是在复杂的并发编程中。

**标签**: `#JavaScript`, `#Bun`, `#multithreading`, `#JavaScriptCore`, `#WebKit`

---