---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 36 items, 15 important content pieces were selected

---

1. [vLLM v0.21.0 发布，弃用 Transformers v4 并新增多项功能](#item-1) ⭐️ 8.0/10
2. [Erlang/OTP 29.0 发布：安全默认及新增 io_ansi 模块](#item-2) ⭐️ 8.0/10
3. [警告：公司可能正在遭受 AI 精神病的影响。](#item-3) ⭐️ 8.0/10
4. [Zulip 宣布成立独立非营利基金会。](#item-4) ⭐️ 8.0/10
5. [Google Project Zero 揭示针对 Pixel 10 的零点击利用链](#item-5) ⭐️ 8.0/10
6. [California bill would require patches or refunds when online games shut down](#item-6) ⭐️ 8.0/10
7. [sigmoids 不会救你：AI 增长预测的缺陷](#item-7) ⭐️ 8.0/10
8. [Image-blaster: Creates 3D environments, SFX, and meshes from a single image](#item-8) ⭐️ 8.0/10
9. [U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app](#item-9) ⭐️ 8.0/10
10. [OCaml 带栈注解在低地球轨道卫星有效载荷中的应用](#item-10) ⭐️ 8.0/10
11. [Jump-HMM 驱动的 Heston 模型生成合成美式期权价格](#item-11) ⭐️ 8.0/10
12. [研究显示跨链桥活动影响 DeFi 借贷协议的 TVL 和收入](#item-12) ⭐️ 8.0/10
13. [对齐训练放大了语言模型在招聘决策中的人口统计偏见](#item-13) ⭐️ 8.0/10
14. [研究利用 300 亿事件揭示 Polymarket 订单簿微观结构](#item-14) ⭐️ 8.0/10
15. [The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 发布，弃用 Transformers v4 并新增多项功能](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM 发布 0.21.0 版本，弃用 transformers v4 支持并要求 C++20 兼容编译器。新增 KV 卸载与混合内存分配器、尊重思考预算的推测解码以及针对 Blackwell GPU 的 TOKENSPEED_MLA 后端。 此版本引入的破坏性变更使 vLLM 迈向现代工具链，同时为最新硬件和推理模型带来性能提升。这表明项目已为下一代大语言模型和基于 Blackwell 的推理 workload 做好准备。 现在强制使用 transformers v5，编译需要 C++20。KV 卸载集成了混合内存分配器，包含调度端滑动窗口组。推测解码现在会强制执行思考 token 预算，TOKENSPEED_MLA 后端为 Blackwell GPU 上的 DeepSeek‑R1/Kimi‑K25 提供优化的注意力计算。

github · khluu · May 15, 08:44

**背景**: vLLM 是一种高吞吐量的大语言模型推理引擎，支持通过 KV 缓存卸载、推测解码和自定义注意力内核等技术实现 GPU 加速服务。混合内存分配器（HMA）按类型分组 KV 缓存层以共享内存张量，从而减少碎片。NVIDIA Blackwell GPU 引入了新架构，可从如 TOKENSPEED_MLA 这样的专用后端中受益，以加速长上下文模型的矩阵乘法运算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/hybrid_kv_cache_manager/">Hybrid KV Cache Manager - vLLM</a></li>
<li><a href="https://fenado.ai/articles/lightseek-foundation-unveils-open-source-tokenspeed-llm-engine-with-vllm-integration-for-nvidia-blackwell">LightSeek Foundation Unveils Open-Source TokenSpeed LLM Engine with vLLM Integration for NVIDIA Blackwell | TokenSpeed, LLM inference engine, Fenado AI</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/39573">[Bug]: Thinking token budget not enforced with MTP ... - GitHub</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#transformers`, `#CUDA`, `#speculative decoding`

---

<a id="item-2"></a>
## [Erlang/OTP 29.0 发布：安全默认及新增 io_ansi 模块](https://www.erlang.org/news/188) ⭐️ 8.0/10

Erlang/OTP 29.0 默认禁用 SSH 守护进程和 SFTP 子系统，以提升安全性，并新增 io_ansi 模块用于发送 ANSI 序列以构建更丰富的 CLI 应用。该版本还加入了实验性原生记录、多值推导、新的 is_integer/3 守护 BIF，并在 SSL 中优先使用后量子混合密钥交换。 安全默认的改变降低了 Erlang 节点的攻击面，使部署更安全；io_ansi 则降低了开发者创建跨节点、带颜色的命令行工具的门槛。二者共同表明 OTP 正在不断演进以满足现代的安全性和易用性需求。 SSH 守护进程在 shell 和 exec 服务上默认被禁用，启动 SSH 守护进程时 SFTP 子系统也不再默认启用。io_ansi 模块可向终端发送虚拟终端序列（ANSI 码）以实现着色、样式或全屏应用。其他新特性包括实验性原生记录（EEP‑79）、多值推导（EEP‑78）、新的 is_integer/3 守护 BIF，以及在 SSL 中优先使用后量子混合密钥交换 x25519mlkem768。

hackernews · pyinstallwoes · May 15, 23:33 · [社区讨论](https://news.ycombinator.com/item?id=48155297)

**背景**: Erlang/OTP 是一套用于构建高可靠性、容错系统的库和设计原则，最初用于电信领域，如今广泛用于分布式应用。SSH 守护进程提供远程 shell 和文件传输访问，若默认启用则可能带来安全风险。ANSI 序列是终端解释的转义码，用于改变文本颜色、样式或光标位置，从而实现丰富的命令行界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.erlang.org/news/188">Erlang/OTP 29.0 - Erlang/OTP</a></li>
<li><a href="https://github.com/erlang/otp/releases">Releases · erlang/otp</a></li>

</ul>
</details>

**社区讨论**: 评论者对安全改进表示欢迎，指出默认禁用 SSH 和 SFTP 是良好的做法。他们强调 io_ansi 模块对构建 CLI 应用很有用，对新的实验性记录将如何被采用感到好奇，并请求更深入地解释此版本的内部细节。总体情绪积极，大家对安全变更和新特性都表现出浓厚兴趣。

**标签**: `#Erlang`, `#OTP`, `#release`, `#security`, `#CLI`

---

<a id="item-3"></a>
## [警告：公司可能正在遭受 AI 精神病的影响。](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

由 Mitchell H 的推文引发的 Hacker News 帖子警告称，许多公司可能正在经历‘AI 精神病’，即将关键思考和决策完全交给 AI 而缺乏足够的人工监督。 这一趋势具有重要意义，因为无监督的 AI 依赖可能削弱人类判断力，增加系统性错误，并在各行业引发伦理问题，凸显加强 AI 治理和保持批判性思考的必要性。 这种现象表现为员工直接接受 AI 生成的答案而不进行验证，可能传播幻觉或偏见，导致决策缺乏人工审查，尤其在金融和风险投资等高风险领域。

hackernews · reasonableklout · May 15, 20:26 · [社区讨论](https://news.ycombinator.com/item?id=48153379)

**背景**: AI 精神病是一个非正式术语，描述因长期与 AI 聊天机器人互动而可能出现的类似精神病的症状，如偏执和妄想。它与将批判性思维外包给 AI 的做法密切相关，即用户不加判断地接受 AI 生成的输出，专家警告这可能削弱人类能力并增加对可能有缺陷的 AI 推理的依赖。2025‑2026 年的讨论显示，技术和心理健康专家对这种模式在企业环境中的扩散日益担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chatbot_psychosis">Chatbot psychosis - Wikipedia</a></li>
<li><a href="https://medium.com/@andy25/ai-psychosis-is-real-its-spreading-and-nobody-is-talking-about-it-ba73859291cf">AI Psychosis Is Real, It’s Spreading, and Nobody Is Talking... | Medium</a></li>
<li><a href="https://www.lesswrong.com/posts/xXYuns8inHD9ogoth/the-dangers-of-outsourcing-thinking-losing-our-critical">The Dangers of Outsourcing Thinking: Losing Our Critical ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为，盲目相信 AI 输出而不进行批判性审查构成危险的‘AI 精神病’，同时承认将 AI 作为工具（例如用于代码生成）是有益的；他们还警告，对 AI 驱动自动化的过度信任可能导致不安全的做法和隐藏的系统性风险，尽管少数人指出，谨慎的慢速采用者可能获得竞争优势。

**标签**: `#AI`, `#AI safety`, `#decision-making`, `#tech culture`, `#overreliance`

---

<a id="item-4"></a>
## [Zulip 宣布成立独立非营利基金会。](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

2026 年 5 月 15 日，Zulip 宣布成立 Zulip 基金会，一个独立的非营利组织，将成为 Zulip 开源聊天平台的正式管理者。 该基金会通过确保项目保持社区驱动且不受可能影响用户数据或插入广告的商业压力，解决了长期的可持续性和信任问题。 该基金会将接收 Zulip 领导层捐赠的公司，包括 Tim Abbott 和三位将加入 Anthropic 的高级成员，其使命是在服务公共利益的同时开发最佳的团队聊天体验。

hackernews · boramalper · May 15, 18:37 · [社区讨论](https://news.ycombinator.com/item?id=48152168)

**背景**: Zulip 是一个由 Jeff Arnold、Waseem Daher、Jessica McKellar 和 Tim Abbott 在 2012 年创建的开源团队聊天应用程序。它提供线程对话功能，并被定位为 Slack 等专有平台的免费替代品。该项目一直由其创始人和志愿者社区维护，最近的 Zulip 12.0 版本于 2026 年 4 月发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zulip">Zulip - Wikipedia</a></li>
<li><a href="https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/">Announcing the Zulip Foundation</a></li>
<li><a href="https://zulip.com/history/">History of the Zulip project</a></li>

</ul>
</details>

**社区讨论**: 评论者表示赞赏基金会有助于缓解信任担忧，同时对核心团队成员的离去既感到兴奋又感到悲伤，质疑宣布时机，称赞 Zulip 的界面优于 Discord，并提到最近的 Zulip 12.0 发布。

**标签**: `#zulip`, `#open source`, `#foundation`, `#nonprofit`, `#chat platform`

---

<a id="item-5"></a>
## [Google Project Zero 揭示针对 Pixel 10 的零点击利用链](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 8.0/10

2026 年 5 月，Google Project Zero 披露了一条针对即将发布的 Pixel 10 智能手机的零点击利用链，该利用链将 Dolby 解码漏洞与新发现的 VPU 驱动特权提升漏洞串联，实现完全内核控制。 此漏洞表明 AI 驱动的功能（如设备端媒体分析）扩大了移动攻击面，若供应商未加固 AI 相关代码路径，Pixel 10 用户将面临风险。 利用链首先利用零点击 Dolby 漏洞在无需用户交互的情况下处理传入视频，随后利用 Pixel 10 专属的 VPU 驱动漏洞将芯片硬件接口暴露给用户空间，从而实现提升到 root 的权限提升。

hackernews · happyhardcore · May 15, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=48148460)

**背景**: 零点击漏洞无需用户交互，仅在设备处理恶意数据（如视频或图像）时自动触发。现代智能手机越来越多地使用设备端 AI 模型来分析媒体（例如用于搜索或转录），这意味着媒体必须在用户看到之前被解码和解释，从而扩大了攻击面。Pixel 10 的新 Tensor G5 芯片包含一个视频处理单元（VPU）驱动，该驱动在此被发现将低级硬件接口暴露给非特权进程，使得利用链的特权提升步骤成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0 - click exploit chain for the Pixel 10 : When a Door... - Project Zero</a></li>
<li><a href="https://gbhackers.com/pixel-10-zero-click-exploit-chain/">Google Project Zero Details Pixel 10 Zero - Click Exploit Chain</a></li>
<li><a href="https://logicity.in/en/blog/google-project-zero-finds-0-click-root-exploit-in-pixel-10">Google Project Zero Finds 0 - Click Root Exploit in Pixel 10 | Logicity</a></li>

</ul>
</details>

**社区讨论**: 评论者担忧 AI 驱动的功能正在增加零点击风险，有用户呼吁厂商不要在未经同意的情况下处理消息。其他人指出，对已报告的驱动漏洞的 unusually fast 90 天修复是积极信号，但同时质疑漏洞披露是否真的在增加，还是仅因 AI 热度而获得更多关注。还有人好奇 AI 是否会让 NSO 等组织过时，或者反而让它们变得更强大。

**标签**: `#mobile security`, `#zero-click exploit`, `#Pixel 10`, `#Android vulnerability`, `#AI attack surface`

---

<a id="item-6"></a>
## [California bill would require patches or refunds when online games shut down](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 8.0/10

A California bill would mandate that online game publishers either provide patches to keep games playable or offer refunds when they shut down services.

hackernews · Lihh27 · May 15, 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48152994)

**标签**: `#legislation`, `#gaming`, `#consumer protection`, `#online services`, `#policy`

---

<a id="item-7"></a>
## [sigmoids 不会救你：AI 增长预测的缺陷](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you) ⭐️ 8.0/10

该文章认为，依赖 sigmoid 曲线外推来预测 AI 持续进步是误导的，因为技术进步遵循会最终平台期的 S 曲线。 此批评凸显了简单数学模型在预测变革性技术方面的局限，促使政策制定者和投资者采用更稳健、不确定性感知的方法。 文章通过螺旋桨、涡喷和冲压发动机的历史例子说明 S 曲线行为，讨论了林迪效应作为替代启发式方法，并提到作者自己预测 AGI 将在一到两年内出现。

hackernews · Tomte · May 15, 10:51 · [社区讨论](https://news.ycombinator.com/item?id=48147021)

**背景**: sigmoid 函数是形状像 S 的数学曲线，通常以逻辑函数为例，用于描述起初缓慢、随后加速、最后趋于平稳的过程。在技术预测中，sigmoid 曲线常被用来表示创新的生命周期，捕捉早期采用、快速增长以及最终饱和。林迪效应（Lindy’s law）认为，非易逝实体（如技术或思想）的未来寿命与其当前年龄成正比，即越持久的技术越可能继续存在。这些概念共同构成了关于 AI 进步是否会无限持续或最终平台期的讨论基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sigmoid_curve">Sigmoid curve</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lindy's_law">Lindy's law</a></li>

</ul>
</details>

**社区讨论**: 评论者指出文章似乎在早期就回答了自己的问题，但随后未充分探讨其含义。几位参与者强调了林迪效应作为估计技术寿命的启发式方法的价值，同时强调任何预测仍然高度不确定。还有用户提到作者对近期 AGI 的个人投入，暗示可能存在偏好林迪观点而非 sigmoid 外推的倾向。

**标签**: `#AI`, `#technology forecasting`, `#sigmoid curves`, `#Lindy's law`, `#HN discussion`

---

<a id="item-8"></a>
## [Image-blaster: Creates 3D environments, SFX, and meshes from a single image](https://github.com/neilsonnn/image-blaster) ⭐️ 8.0/10

Image-blaster is an open‑source project that creates 3D environments, sound effects, and meshes from a single image using AI models like Worldlabs.

hackernews · MattRogish · May 15, 15:42 · [社区讨论](https://news.ycombinator.com/item?id=48150069)

**标签**: `#3D generation`, `#AI`, `#computer vision`, `#generative models`, `#graphics`

---

<a id="item-9"></a>
## [U.S. DOJ demands Apple and Google unmask over 100k users of car-tinkering app](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

The U.S. Department of Justice is demanding that Apple and Google reveal the identities of more than 100,000 users of a popular car‑tinkering app used to bypass emissions controls.

hackernews · tencentshill · May 15, 17:28 · [社区讨论](https://news.ycombinator.com/item?id=48151383)

**标签**: `#privacy`, `#government surveillance`, `#automotive emissions`, `#app store`, `#legal`

---

<a id="item-10"></a>
## [OCaml 带栈注解在低地球轨道卫星有效载荷中的应用](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

博客文章描述了如何使用带有栈注解的 OCaml（即 O(x)Caml）在低地球轨道卫星有效载荷上运行，实现了亚 10 纳秒延迟并消除了垃圾回收停顿。 这表明即使是带有垃圾回收的函数式语言也能满足航空航天的严格实时要求，为更安全、可维护的卫星软件铺平道路。 通过栈注解减少堆分配，使得分发热路径的 p99.9 延迟从 29 ns 降至 9 ns，且在 2500 万个数据包上未出现 minor GC；软件以 SystemD 服务形式运行，通过 DBus 与平台通信，并实现了 CCSDS‑to‑DBus 桥以及对称密钥加密。

hackernews · yminsky · May 15, 10:55 · [社区讨论](https://news.ycombinator.com/item?id=48147058)

**背景**: OCaml 是一种静态类型函数式语言，带有分代垃圾回收器；通过栈注解，程序员可以提示某些数据应分配在栈上，从而减少堆压力和 GC 停顿。低地球轨道（LEO）卫星以约 7.8 km/s 的速度运行，提供低延迟链路和频繁的地面站可见窗口，适合实时有效载荷处理。卫星有效载荷软件通常以独立服务形式运行，通过 CCSDS、DBus 等协议通信，对可预测的时序要求很高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ocaml.org/docs/garbage-collector">Understanding the Garbage Collector · OCaml Documentation</a></li>
<li><a href="https://ocaml.org/manual/5.2/api/Stack.html">OCaml library : Stack</a></li>
<li><a href="https://en.wikipedia.org/wiki/Low_Earth_orbit">Low Earth orbit - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 OCaml 已在 2016 年的 GHGSat‑D 卫星上飞行，赞赏栈注解带来的延迟提升，并讨论是否有必要重新造 CCSDS 加密轮子，而不使用如 TLS 这样的成熟方案。有人质疑让带 GC 的语言适应硬实时工作负载的难度，也有人强调其安全性优势。

**标签**: `#OCaml`, `#systems programming`, `#aerospace`, `#garbage collection`, `#performance optimization`

---

<a id="item-11"></a>
## [Jump-HMM 驱动的 Heston 模型生成合成美式期权价格](https://arxiv.org/abs/2605.13998) ⭐️ 8.0/10

该论文提出了一种由 Jump 隐马尔可夫模型驱动的 Heston 框架，将隐含波动率视为结构性股票收益模型的输出，从而能够生成逼真的合成美式期权价格。 通过打破隐含波动率与期权价格之间的循环依赖，该方法为机器学习和风险分析提供了可靠的合成数据来源，对量化金融具有重要意义。 该框架结合了用于多资产价格路径的 Jump HMM、依赖于 regimes 的 Heston 方差过程以及重组二叉树来定价美式期权，通过在每个行权价‑到期对上将方差初始化为其均值回复目标，使得波动率微笑、偏斜和期限结构能够自然产生，无需外部校准。

rss · arXiv Quantitative Finance · May 15, 04:00

**背景**: 跳隐马尔可夫模型（Jump HMM）能够捕捉不可观察的市场状态并包含突发跳跃，从而再现股票收益率的波动聚类和厚尾等特征。Heston 随机波动率模型将方差视为均值回复过程，通过使其长期水平依赖于 regimes、到期时间、 moneyness 以及市场情绪指标，能够生成反映微笑、偏斜和期限结构的隐含波动率曲面。美式期权通常通过重组二叉树（Cox‑Ross‑Rubinstein）进行定价，该方法通过逆向 induction 考虑提前行权。生成合成期权价格通常需要隐含波动率作为输入，而隐含波动率本身又是从观察到的期权价格中校准得到的，这就形成了循环依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Heston_model">Heston model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice_model_(finance)">Lattice model (finance) - Wikipedia</a></li>
<li><a href="https://www.daytrading.com/hidden-markov-models">Hidden Markov Models in Finance, Markets & Trading</a></li>

</ul>
</details>

**标签**: `#option pricing`, `#stochastic volatility`, `#hidden Markov model`, `#synthetic data`, `#quantitative finance`

---

<a id="item-12"></a>
## [研究显示跨链桥活动影响 DeFi 借贷协议的 TVL 和收入](https://arxiv.org/abs/2605.12508) ⭐️ 8.0/10

该论文采用带固定效应的面板回归和 OLS 模型，实证分析了跨链桥活动对十五个 DeFi 借贷协议在九个 EVM 兼容链上（2022 年 10 月至 2025 年 1 月）的 TVL 和总收入的影响。 通过量化桥梁交易量、黑客攻击和新网络启动的异质性影响，该研究为 DeFi 风险管理者提供了可操作的见解，以在日益多链的生态系统中将跨链指标纳入风险模型并采用层级感知方法。 数据集涵盖 15 个借贷协议、53 个跨链桥和九个 EVM 链；桥梁黑客攻击与 TVL 和收入呈显著正相关，而桥梁集成增加则与 TVL 和收入下降相关，表明流动性外流；以太坊吸引大额存款者，而 Layer‑2 则倾向于零售用户，且模型获得高 R‑squared 值。

rss · arXiv Quantitative Finance · May 15, 04:00

**背景**: DeFi 借贷协议允许用户存入资产以获得利息，总锁定价值（TVL）衡量这些合约中锁定的资产的总美元价值。跨链桥使得不同区块链之间能够转移资产和数据，促进互操作性但也带来新的风险。面板回归结合固定效应和普通最小二乘（OLS）是一种计量经济学技术，可控制实体和时间之间的未观测异质性，适用于分析多链和多时期的协议表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@V-Blaze/cross-chain-interoperability-bridging-asset-chain-with-other-blockchain-networks-1a3bd628025b">Cross - Chain Interoperability: Bridging Asset Chain with... | Medium</a></li>
<li><a href="https://www.investopedia.com/total-value-locked-7486821">Understanding Total Value Locked (TVL) in Cryptocurrency and DeFi</a></li>
<li><a href="https://www.econometrics-with-r.org/10-rwpd.html">10 Regression with Panel Data | Introduction to Econometrics ...</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#cross-chain`, `#lending protocols`, `#risk modeling`, `#blockchain interoperability`

---

<a id="item-13"></a>
## [对齐训练放大了语言模型在招聘决策中的人口统计偏见](https://arxiv.org/abs/2605.13866) ⭐️ 8.0/10

A study of 27 language models across 177 occupations found that models favor female and Black candidates while disadvantaging disabled candidates, and that post‑training alignment amplifies these biases—boosting advantages for female and Black applicants by ~325‑330% and disadvantages for disabled applicants by ~171%.

rss · arXiv Quantitative Finance · May 15, 04:00

**标签**: `#AI fairness`, `#language models`, `#hiring bias`, `#AI alignment`, `#ethics`

---

<a id="item-14"></a>
## [研究利用 300 亿事件揭示 Polymarket 订单簿微观结构](https://arxiv.org/abs/2604.24366) ⭐️ 8.0/10

该论文分析了 Polymarket 的公开订单簿馈送，包含 52 天内的 300 亿个逐笔事件，并将其与链上交易记录关联，报告了该市场微观结构的八个风格化事实。 理解 Polymarket 的微观结构有助于去中心化预测市场的设计和监管，并凸显仅依赖公开馈送推断交易方向的局限性。 研究发现包括长期冲刺溢价、接近均匀的深度曲线、几乎不存在的区块时钟对齐效应、制造者钱包多样但尾部集中、类别条件下的有效点差差异、中位数低于 50 ms 的馈送摄入延迟伴有多秒尾部、中位数仅 1%的洗盘交易比例，以及仅约 59%的交易方向推断准确率（远低于纳斯达克的约 80%）。

rss · arXiv Quantitative Finance · May 15, 04:00

**背景**: Polymarket 是全球最大的链上预测市场，运行在 Polygon 网络上，并使用 UMA 的乐观甲骨文（Optimistic Oracle）以稳定币结算对真实世界事件的赌注。预测市场允许参与者买卖其收益取决于未来事件结果的合约，从而将分散的信息汇总到市场价格中。市场微观结构研究交易场所的具体规则——如订单簿结构、匹配逻辑和延迟——如何影响价格发现、流动性和执行质量。在链上研究这些机制有助于评估去中心化场所是否能够复制传统交易所的效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://polymarket.com/">Polymarket | The World's Largest Prediction Market</a></li>
<li><a href="https://lesaker.substack.com/p/on-chain-market-microstructure-amms">On-Chain Market Microstructure: AMMs, Orderbooks, and RFQs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prediction_market">Prediction market - Wikipedia</a></li>

</ul>
</details>

---

<a id="item-15"></a>
## [The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot](https://arxiv.org/abs/2410.02091) ⭐️ 8.0/10

The paper shows GitHub Copilot increases open-source code contributions by about 6% through higher developer participation and individual productivity, while also raising coordination time by 8% due to more code discussions.

rss · arXiv Quantitative Finance · May 15, 04:00

**标签**: `#Generative AI`, `#GitHub Copilot`, `#Open-source software`, `#Developer productivity`, `#Collaborative development`

---