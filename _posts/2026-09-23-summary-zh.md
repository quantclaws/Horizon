---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> From 62 items, 21 important content pieces were selected

---

1. [vLLM v0.30.0 新增模型支持、GPU 权重缓存及性能提升](#item-1) ⭐️ 8.0/10
2. [Claude Opus 5.5](#item-2) ⭐️ 8.0/10
3. [黑客声称已获取所有 FBI 员工数据](#item-3) ⭐️ 8.0/10
4. [SAML：糟糕设计的分形](#item-4) ⭐️ 8.0/10
5. [Claude Opus 5.5 的智能、性能与价格分析（不同推理设置）](#item-5) ⭐️ 8.0/10
6. [WordPress 7.1.2 修复了未授权路径遍历导致的条件性 RCE 漏洞。](#item-6) ⭐️ 8.0/10
7. [五角大楼称 AI 过度依赖导致伊朗学校误击](#item-7) ⭐️ 8.0/10
8. [苹果在 iOS 中加入持久广告，引发用户不满](#item-8) ⭐️ 8.0/10
9. [Claude Opus 5.5 与 GPT-6 Sol/Luna 同步发布，价格大幅下降](#item-9) ⭐️ 8.0/10
10. [帕雷托改进定价：为什么 3 比 2 更好](#item-10) ⭐️ 8.0/10
11. [通用扩散模型学习期权波动率曲面的共享动态](#item-11) ⭐️ 8.0/10
12. [基于价差的时序层次预测提升日前电力市场利润。](#item-12) ⭐️ 8.0/10
13. [配对模糊框架下的深度学习反射 BSDE 求最优停止](#item-13) ⭐️ 8.0/10
14. [预测市场在多数城市击败公开天气预报](#item-14) ⭐️ 8.0/10
15. [后训练 LLMs 增加相关偏见及招聘中的系统性排斥。](#item-15) ⭐️ 8.0/10
16. [社会影响降低 AI 代理选择多样化科学论文的程度。](#item-16) ⭐️ 8.0/10
17. [漏积分器方法抑制递归预测中的误差累积。](#item-17) ⭐️ 8.0/10
18. [时间解释将期望效用理论与非遍历经济学联系起来](#item-18) ⭐️ 8.0/10
19. [通过 Heston 模型方差积分反驳 Gatheral 猜想](#item-19) ⭐️ 8.0/10
20. [LLM 文本测量提升再犯预测和同伴效应估计。](#item-20) ⭐️ 8.0/10
21. [包含 44 个专门代理的 Agentic AI 管道用于机构资产管理](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.30.0 新增模型支持、GPU 权重缓存及性能提升](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM v0.30.0 包含来自 315 名贡献者的 762 次提交，新增对 DeepSeek-V4.1-Flash、GLM-5.3-Flash 等模型的支持，并引入持久化每 GPU 权重缓存守护进程，通过 CUDA IPC 实现快速引擎启动。该版本还在 Qwen3.8-Flash-Next、Kimi K3、HiSparse 和 Model Runner V2 等方面带来了大量性能改进。 新的权重缓存守护进程大幅缩短引擎重启时间，降低 LLM 服务工作负载的延迟；扩展的模型支持和量化改进使 vLLM 能够适用于更多前沿模型。这些进步巩固了 vLLM 作为大规模 LLM 生产部署的高性能推理引擎的地位。 主要特性包括在 SM100 上通过 FlashMLA V4.1 实现 KV 缓存的 MXFP8 量化、用于稀疏 MLA 解码的 HiSparse 主机居民层、具备双批次重叠和完整 CUDA 图的 Model Runner V2，以及 Qwen3.8-Flash-Next 的优化，如独立的 prefill/decode QSA 索引器内核和 FP8 索引器缓存。权重缓存守护进程现在还支持 FP4 检查点和多节点张量并行。

github · khluu · Sep 22, 05:20

**背景**: vLLM 是一个用于快速高效 LLM 推理的库，利用 GPU 内核、张量并行和量化来降低延迟和内存使用。MXFP8（微缩放 FP8）是 OCP 定义的格式，将 32 个元素分组以共享一个尺度，在保持 8 位位宽的同时提升相较于逐通道 FP8 的精度。FlashMLA 提供了优化的多头潜在注意力内核，而持久化 GPU 权重缓存守护进程则将量化权重保留在 GPU 内存中，以避免在引擎重启时昂贵的磁盘重新加载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/projects/vllm-omni/en/latest/user_guide/quantization/mxfp8/">MXFP8 W8A8 - vLLM-Omni</a></li>
<li><a href="https://github.com/vllm-project/vllm/pull/56893">[Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record) by zyongye · Pull Request #56893 · vllm-project/vllm</a></li>
<li><a href="https://www.lmsys.org/blog/2026-08-21-sglang-fast-recovery">Fast Engine Recovery: Sub-Second Engine Restart for SGLang via Weight Cache Daemon - LMSYS Org</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#GPU caching`, `#model support`

---

<a id="item-2"></a>
## [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) ⭐️ 8.0/10

Anthropic unveiled Claude Opus 5.5, a updated version of its flagship language model featuring reduced token pricing and improved natural, clear communication.

hackernews · km144 · Sep 22, 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**标签**: `#LLM`, `#Claude Opus`, `#Anthropic`, `#AI model release`, `#pricing`

---

<a id="item-3"></a>
## [黑客声称已获取所有 FBI 员工数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

黑客声称来自 ShinyHunters 组织，称他们已经获取了所有 FBI 员工的个人数据，据 404media 报道。 此类泄露将暴露联邦执法人员的敏感信息，对国家安全和个人隐私构成严重威胁。 黑客表示他们不打算以金钱勒索 FBI，称其动机是胁迫而非敲诈，并威胁除非满足某些要求否则将公开数据。

hackernews · spenvo · Sep 22, 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49805278)

**社区讨论**: 评论者对保护大型数据库的能力表示怀疑，提到 2015 年 OPM 泄露事件导致 2210 万条记录暴露。有人以黑色幽默指出只有完全隔离的系统才能真正安全，也有人开玩笑建议荒谬的对策，比如让 FBI 特工在公共场所跳舞。总体情绪认为大规模数据泄露难以避免，现有防御措施不足。

**标签**: `#cybersecurity`, `#data breach`, `#FBI`, `#hacking`, `#government security`

---

<a id="item-4"></a>
## [SAML：糟糕设计的分形](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/) ⭐️ 8.0/10

2026 年 9 月 21 日，Trail of Bits 发布了一篇题为《SAML：糟糕设计的分形》的博客文章，详细列出了 SAML 的众多安全缺陷，并引发了关于 SAML 与 OpenID Connect（OIDC）权衡的深入讨论。 该批评凸显了许多企业仍然依赖 SAML 进行单点登录，因此了解其弱点对于提升身份验证安全性和指导协议选择至关重要。 文章指出了若干具体漏洞，例如 XML 签名验证可通过攻击者控制的密码进行 HMAC 欺骗，以及接受 Web PKI 签名，使攻击者能够用自己的 TLS 密钥对 SAML 文档进行签名。文章还指出 SAML 基于 XML 的沉重设计导致复杂的解析攻击，而 OIDC 虽然规避了许多这些问题，但仍存在 JWT 算法混淆和缺失受众检查等问题。

hackernews · aray07 · Sep 22, 18:57 · [社区讨论](https://news.ycombinator.com/item?id=49806335)

**背景**: SAML（安全断言标记语言）是一种基于 XML 的开放标准，用于在身份提供者和服务提供者之间交换身份验证和授权数据，广泛用于企业单点登录。OIDC（OpenID Connect）是构建在 OAuth 2.0 之上的身份验证层，使用 JSON Web Token（JWT）传输身份信息。与 SAML 不同，OIDC 依赖于 JSON 和 RESTful 流程，降低了解析复杂性，但引入了不同的安全考量，如 JWT 验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SAML">SAML - Wikipedia</a></li>
<li><a href="https://auth0.com/intro-to-iam/saml-vs-openid-connect-oidc">What is OpenID vs SAML? Find out the Differences | Auth0</a></li>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/saml-vs-oidc-decision-guide">SAML versus OpenID Connect: Choose the right SSO protocol</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意 SAML 的 XML 复杂性带来严重的安全隐患，举例包括基于 HMAC 的签名绕过和 Web PKI 的滥用。有人指出 SAML 仍然提供一些企业特有的功能，如 IdP‑initiated 流，而 OIDC 缺乏；也有人警告 OIDC 同样存在问题，如 JWT 算法混淆和缺失受众检查，得出结论：许多组织在可预见的未来仍需要同时支持两种协议。

**标签**: `#SAML`, `#authentication`, `#security`, `#OIDC`, `#web standards`

---

<a id="item-5"></a>
## [Claude Opus 5.5 的智能、性能与价格分析（不同推理设置）](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

一篇 Hacker News 帖子分享了对 Claude Opus 5.5 在 max、xhigh 和 medium 三种推理设置下的智能、性能与价格的分析，引发了关于成本效益及可能性能回退的讨论。 该分析有助于开发者判断 Claude Opus 5.5 是否相较于之前的 Opus 版本及竞争对手提供更好的性价比，从而影响成本敏感型 AI 应用的模型选择。 max 设置的完成 token 上限为 128,000，在复杂提示下可能耗尽预算；高努力设置的每任务成本据说比 Opus 5 低一半；同时有用户表示 Opus 4.8 在遵循指令方面比 Opus 5.5 更稳定。

hackernews · theanonymousone · Sep 22, 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**背景**: Claude Opus 5.5 是 Anthropic 最新的旗舰大语言模型，拥有 1,000,000 token 的上下文窗口，并支持最多 128,000 token 的完成输出。该模型提供 max、xhigh 和 medium 三种推理设置，以调整推理过程中的计算量，从而影响性能和成本。它主要面向 agentic 编程、计算机使用和知识工作等任务，其价格随供应商而异，且可通过缓存和折扣进一步降低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 (max with fallback) - Intelligence... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，max 推理设置在处理复杂提示时可能耗尽其 128,000 token 的预算；也有用户强调，高努力设置相比 Opus 5 能将每任务成本降低一半。部分用户反映出现性能回退，倾向于使用更稳定的 Opus 4.8，还有人对‘在同样价位的模型中略显昂贵’的表述提出疑问。

**标签**: `#Claude Opus 5.5`, `#LLM evaluation`, `#AI pricing`, `#reasoning settings`, `#model performance`

---

<a id="item-6"></a>
## [WordPress 7.1.2 修复了未授权路径遍历导致的条件性 RCE 漏洞。](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 8.0/10

WordPress 7.1.2 之前的版本存在未授权路径遍历漏洞，可能在特定条件下导致远程代码执行；该漏洞已在 7.1.2 版本中修复，并回移植到所有受支持的分支，直至 4.7。 由于 WordPress 驱动着大量网站，未授权路径遍历若能导致 RCE 将构成广泛威胁，攻击者可能利用此漏洞入侵数百万站点。及时修复并回移植到旧版分支体现了项目对遗留系统安全的承诺。 该漏洞位于模板文件选择逻辑中，用户提供的输入未被检查是否包含 '../' 序列，因而可导致任意本地 PHP 文件的包含。利用通常需要能够将文件写入可预测位置，或将此漏洞与其他漏洞链接以实现远程代码执行。

hackernews · vntok · Sep 22, 16:33 · [社区讨论](https://news.ycombinator.com/item?id=49803959)

**背景**: WordPress 是一种广泛使用的开源内容管理系统，驱动着数百万网站。路径遍历漏洞使攻击者能够跳过预定的目录结构，读取或包含本应不可访问的文件。当被包含的文件包含可执行的 PHP 代码时，攻击者可实现远程代码执行，但这通常依赖于额外条件，如写入权限或其他漏洞的配合。该漏洞影响 7.1.2 之前的版本，已在 7.1.2 版本中修复，并回移植到旧分支。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-9145/">CVE-2026-9145: WordPress Plugin Path Traversal Vulnerability</a></li>
<li><a href="https://hadrian.io/vulnerability-alerts/cve-2026-87902-working-poc-wordpress-critical-path-traversal">CVE-2026-87902: A Working PoC for WordPress's Critical Path Traversal</a></li>
<li><a href="https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html">WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，由于 WordPress 的广泛使用，它经常成为自动攻击的目标，有人甚至转向静态站点生成器以规避风险。也有人称赞及时的补丁及其向旧分支的回移植，并引用一条多年前的官方文档评论，认为它早已准确描述了此漏洞。

**标签**: `#WordPress`, `#security vulnerability`, `#path traversal`, `#RCE`, `#patch`

---

<a id="item-7"></a>
## [五角大楼称 AI 过度依赖导致伊朗学校误击](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 8.0/10

五角大楼的一份报告指出，过度依赖 AI 进行目标选择导致对伊朗学校的误导飞弹袭击，报告称未能核实目标并对平民风险表现出鲁莽。 该发现凸显了在战争中使用 AI 所带来的严重伦理、法律和技术风险，强调需要在自动目标选择中加强人工监督和问责。 报告指出，由于数据过时，米纳布站被错误标记为伊朗革命卫队设施，随后被输入 Maven AI 系统，使目标选择时间从数小时缩短至数分钟，且在明知存在重大平民风险的情况下仍实施了打击。

hackernews · devonnull · Sep 22, 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49806430)

**背景**: Maven 是美国军方用于加速潜在威胁识别的 AI 驱动目标选择平台。对这种自动化的过度依赖一直存在争议，因为它虽然能加快决策，但在数据出错或缺乏情境时会增加错误风险。以往事件显示 AI 可能将民用物体误认为军事目标，这引发了对自主战争中问责制的担忧。

**社区讨论**: 评论者就 AI 是否为主要原因展开讨论，有人认为真正问题是数据过时和加速目标选择的压力，而另一些人则强调需要问责和对救援人员的保护。还有人提到类似的近失事件，例如 AI 误识别的中国船只，凸显自动化战争的更广泛风险。

**标签**: `#AI ethics`, `#military AI`, `#autonomous weapons`, `#target identification`, `#Pentagon report`

---

<a id="item-8"></a>
## [苹果在 iOS 中加入持久广告，引发用户不满](https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy) ⭐️ 8.0/10

苹果开始在 iPhone 屏幕顶部显示持久的促销广告，推广 iCloud+ 存储、Apple Music/Apple TV 试用以及 AppleCare+ 等服务。 这一举措表明苹果正在偏离其传统的无广告用户体验，可能削弱用户信任并影响他们对平台价值的感知。 这些广告以横幅形式出现在屏幕顶部，只有等待促销过期（数周或数月）或订阅被宣传的服务才能消除。

hackernews · MC995 · Sep 22, 14:30 · [社区讨论](https://news.ycombinator.com/item?id=49801939)

**背景**: iOS 是苹果用于 iPhone 和 iPad 的移动操作系统，以其简洁的界面和有限的第三方广告而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy">‘I wish Apple would just stop that crap': Apple has added persistent ‘ads’ to iOS, and it’s driving users crazy | TechRadar</a></li>
<li><a href="https://mjtsai.com/blog/2026/09/22/persistent-ads-in-ios-settings/">Michael Tsai - Blog - Persistent Ads in iOS Settings</a></li>

</ul>
</details>

**社区讨论**: 评论者抱怨这些广告降低了 iOS 的高端体验，一些用户因此转而使用 Google 地图以避免侵入式促销。

**标签**: `#iOS`, `#advertising`, `#user experience`, `#Apple`, `#mobile OS`

---

<a id="item-9"></a>
## [Claude Opus 5.5 与 GPT-6 Sol/Luna 同步发布，价格大幅下降](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

2026 年 9 月 22 日，Anthropic 发布了 Claude Opus 5.5，随后 OpenAI 推出了 GPT-6 Sol 和 GPT-6 Luna，新模型的 API 价格比 GPT-5.6 低廉一半。 同步发布及大幅降价加剧了大语言模型的价格战，使高性能模型对开发者和企业更具可负担性，预示着 AI 服务将朝着更具成本效益的方向发展。 GPT-6 Luna 的输入价格为每百万 token 0.10 美元，缓存输入 0.01 美元/百万，输出 0.50 美元/百万；GPT-6 Sol 输入 2 美元/百万，缓存输入 0.20 美元/百万，输出 10 美元/百万；Claude Opus 5.5 输入 4 美元/百万，缓存输入 0.20 美元/百万，输出 20 美元/百万。GPT-5.6 系列将在 11 月涨价 25%，因此 GPT-6 的价格相当于 GPT-5.6 促销价的一半。

rss · Simon Willison · Sep 22, 23:46

**背景**: 大型语言模型（LLM）提供商通常按照每百万 token 的使用量计费，分别设定输入、缓存输入和输出的价格。Claude Opus 和 GPT 系列分别是 Anthropic 和 OpenAI 的旗舰模型族，新版本在追求性能提升的同时也致力于降低成本。价格下降往往反映了市场竞争、推理效率的提升以及吸引企业级工作负载的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT-6 Sol and Luna | OpenAI</a></li>
<li><a href="https://kingy.ai/blog/gpt-6-sol-luna-specs-benchmarks-pricing-comparison/">GPT-6 Sol and GPT-6 Luna: Specs, Benchmarks, Pricing and How They Compare to Claude Opus 5.5, Fable 5.1 and Gemini - Kingy AI</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Claude Opus`, `#GPT-6`, `#AI pricing`, `#model releases`

---

<a id="item-10"></a>
## [帕雷托改进定价：为什么 3 比 2 更好](https://arxiv.org/abs/2609.22652) ⭐️ 8.0/10

该研究表明，三层优先定价方案可以通过提供收费的高质量层、补偿的低质量层以及基准质量的中间层，实现对均等分配的帕雷托改进，而任何两层方案都无法做到。 这一结果提供了一种实用的机制设计工具，能够让所有参与者受益，从而解决道路定价和公共物品等服务中长期存在的效率-公平权衡。 证明表明，通过三个层级——付费获得高质量、补偿获得低质量以及基准质量的中间层——可以让每个代理人都严格受益，而任何两层配置都会使至少一人变得更糟。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 帕雷托改进指的是至少一人受益且没有人受损的资源重新分配，表明存在使所有人都更好的机会。优先定价系统根据代理人的支付意愿分配不同的服务质量或价格，常常在公平（均等获取）和效率（为付费者提供更高质量）之间产生权衡。本文研究的环境是：提高某些代理人的质量会降低可以提供的平均质量，这种情形适用于拥堵、排队或逆选择下的保险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.22652">Pareto-Improving Pricing: Why 3 Is Better Than 2 - arXiv.org</a></li>
<li><a href="https://ziyangkang.com/files/PIP.pdf">Pareto-ImprovingPricing:Why3IsBetterThan2</a></li>
<li><a href="https://www.investopedia.com/terms/p/paretoimprovement.asp">investopedia.com/terms/p/paretoimprovement.asp</a></li>

</ul>
</details>

**标签**: `#pricing theory`, `#mechanism design`, `#Pareto improvement`, `#tiered pricing`, `#economics`

---

<a id="item-11"></a>
## [通用扩散模型学习期权波动率曲面的共享动态](https://arxiv.org/abs/2609.22893) ⭐️ 8.0/10

作者提出了一种通用条件扩散模型，能够联合生成次日的隐含波动率曲面增量及基础股票的收益率，在 50 只股票的数据上训练，并在 50 只样本内和 50 只样本外股票上进行测试。 该模型表明所学动态能够泛化到未见过的股票，为期权定价、对冲和风险管理提供了更可靠的工具，在套利削减和风险预测方面均优于之前的 VolGAN 基准。 训练目标主要是最小化均方误差（MSE），可选择加入平滑性和静态套利惩罚；评估指标包括套利违规程度、股票风险预测准确率以及前三个主成分解释的方差比例。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 隐含波动率曲面（IVS）描述了不同月份和行权价的期权隐含波动率如何变化，其动态对于期权定价和对冲至关重要。之前的生成方法如 VolGAN 采用生成对抗网络（GAN）建模 IVS 的变化，但在跨股票泛化方面表现有限。扩散模型通过逐步去噪来学习复杂分布，为学习高维金融数据中的共享时间模式提供了一种有前景的替代方案。

**标签**: `#diffusion models`, `#implied volatility`, `#option pricing`, `#financial machine learning`, `#generative modeling`

---

<a id="item-12"></a>
## [基于价差的时序层次预测提升日前电力市场利润。](https://arxiv.org/abs/2609.23223) ⭐️ 8.0/10

该研究表明，通过时序层次预测（THieF）框架 jointly 预测小时电价和所有 intraday 价差，能够提升欧洲日前电力市场的预测准确度和交易利润。基于德国和西班牙五年的 out‑of‑sample 数据，预测准确度最高提升 19.7%，利润最高提升 10.4%，相较于未 reconciled 的小时价格预测，这一改进在三种不同预测架构以及预训练的 TabPFN 基础模型上均得到验证。 结果表明，利用经济相关预测目标之间的一致性关系可以同时提升预测准确度和决策价值，说明更好的统计预测不一定带来更好的经济决策。这一发现对能源交易者、电池套利策略以及侧重市场导向评估的预测研究具有重要参考价值。 THieF 框架对小时价格和所有可能的 intraday 价差进行预测协调，以确保在不同时间聚合层次上的一致性。该改进在三种不同的模型架构（如统计模型、机器学习和深度学习）中均得到验证，即使基础预测由预训练的 TabPFN 基础模型生成，收益仍然显著，表明该方法具有良好的鲁棒性。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 时序层次预测（THieF）通过在不同时间粒度（如小时、日、周）上生成预测并进行协调，以确保各层次预测的一致性，该方法最初用于一般时间序列。预测协调通过调整单点预测使其在汇总时保持一致，已被证明能在多个领域提高准确度，包括能源市场。TabPFN 是一种基于 Transformer 的表格数据基础模型，利用上下文学习在极少训练的情况下实现强大性能，因而可作为电力价格预测的高质量基线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cran.r-project.org/web/packages/thief/thief.pdf">thief : Temporal Hierarchical Forecasting</a></li>
<li><a href="https://business-science.github.io/modeltime/reference/temporal_hierarchy.html">General Interface for Temporal Hierarchical Forecasting ( THIEF )...</a></li>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular...</a></li>

</ul>
</details>

**标签**: `#electricity price forecasting`, `#temporal hierarchy`, `#day-ahead markets`, `#battery arbitrage`, `#forecast reconciliation`

---

<a id="item-13"></a>
## [配对模糊框架下的深度学习反射 BSDE 求最优停止](https://arxiv.org/abs/2609.23768) ⭐️ 8.0/10

本文提出了一种用于动态风险度量下最优停止的配对模糊框架，并将停止值刻画为上反射后向随机微分方程（BSDE）。随后开发了一种深度学习方案来求解反射二次 BSDE，并在美式期权定价上进行了演示。 该研究给出了停止算子的结构性质，在若干基准情况下给出了显式解，并提出了一种收敛的深度学习算法，为风险敏感的最优停止问题连接了金融数学与机器学习。 该工作将 Girsanov 模型不确定性与现金次加性风险评估相结合，研究了源自熵风险度量的二次驱动项，并通过离散反射和截断将二次 BSDE 化为全局 Lipschitz 系统，收敛性分析将 BSDE 离散误差与神经网络逼近误差结合起来。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 最优停止问题涉及选择最佳时机以最大化预期回报或最小化成本。动态风险度量将经典期望推广以考虑模型不确定性和时间一致的风险厌恶。后向随机微分方程（BSDE）是表示这种风险调整值的有力工具，而反射 BSDE 则引入约束以防止解低于给定的障碍，这对于美式期权尤为重要。

**标签**: `#risk measures`, `#BSDE`, `#deep learning`, `#optimal stopping`, `#financial mathematics`

---

<a id="item-14"></a>
## [预测市场在多数城市击败公开天气预报](https://arxiv.org/abs/2609.23969) ⭐️ 8.0/10

研究人员分析了 Kalshi 在七个美国城市过去五年的逐小时温度预测市场数据，发现市场隐含预报在六个城市中击败了国家模式融合（NBM），在交易第一小时后使均方根误差降低约 10%。 这一结果表明，预测市场能够比传统公开天气预报更快速、更准确地聚合分散信息，为决策者提供潜在有价值的互补工具，并支持群体智慧理论。 研究从 Kalshi 合约中提取逐小时市场隐含预报，并与 NBM 预报进行比较，发现市场的信息向 NBM 靠近的距离是 NBM 向市场靠近的四倍；市场不对 NBM 的更新作出反应，而 NBM 则慢慢吸收市场中已有的信息。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 像 Kalshi 这样的预测市场让用户可以买卖未来事件的合约，合约价格反映了集体对结果的看法。国家模式融合（NBM）是 NOAA 制作的预报，通过融合多个天气模式输出提供一致且准确的格点预报起点。预报精度通常使用均方根误差（RMSE）来衡量，RMSE 量化预测误差的平均幅度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kalshi.com/hub/weather">Weather Forecast Markets | Kalshi</a></li>
<li><a href="https://blend.mdl.nws.noaa.gov/nbm-dashboard">NBM Dashboard - National Oceanic and Atmospheric Administration</a></li>
<li><a href="https://en.wikipedia.org/wiki/Root_mean_square_deviation">Root mean square deviation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#weather forecasting`, `#forecast evaluation`, `#information aggregation`, `#Kalshi exchange`

---

<a id="item-15"></a>
## [后训练 LLMs 增加相关偏见及招聘中的系统性排斥。](https://arxiv.org/abs/2609.22169) ⭐️ 8.0/10

研究发现，后训练的大语言模型对年长申请人的回叫率降低 3.6%，且模型决策的相关性增加导致全球系统性排斥率从 5.6%升至 17.3%。 这表明在招聘中使用 LLMs 可能放大偏见，导致对年长者和交叉群体的不公平排斥，凸显了在 AI 招聘工具中进行偏见缓解的必要性。 论文评估了十个 LLMs 的基础模型与后训练版本，发现后训练模型对年长申请人的回叫率降低 3.6%，模型决策之间的相关性显著上升，使系统性排斥率从 5.6%升至 17.3%，交叉性排斥率最高达 21.7%，偏见主要由年龄歧视驱动并在后训练过程中加剧。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 大语言模型正被越来越多的雇佣方用于自动化简历筛选和面试评估。基础模型是在广泛语料上预训练得到的，而后训练则通过特定任务数据（如招聘数据）进一步微调以提升性能。当多个后训练模型在相似数据上训练时，它们的决策倾向于高度相关，这种同质化被称为 monocultural bias，会导致劳动力市场中某些人口群体被系统性地排除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.22169v1">Monocultural Biases: Correlated biases in large language ...</a></li>
<li><a href="https://aichanging.work/zh/blog/monocultural-bias-llm-hiring-systemic-exclusion-2026">AI Hiring Monoculture: Exclusion Triples to 17.3% | AI ...</a></li>
<li><a href="https://arxiv.org/html/2506.07962v1">Correlated Errors in Large Language Models - arXiv.org</a></li>

</ul>
</details>

**标签**: `#LLM bias`, `#hiring automation`, `#AI ethics`, `#monocultural bias`, `#systemic discrimination`

---

<a id="item-16"></a>
## [社会影响降低 AI 代理选择多样化科学论文的程度。](https://arxiv.org/abs/2609.22408) ⭐️ 8.0/10

在一个包含 1000 个 AI 代理、从 114 篇经济学论文中选择的实验中，社会影响条件下的代理每个代理选择的论文减少了 17.2%，选择更加集中，合计仅覆盖 73 篇不同论文，而独立条件下覆盖了 90 篇。后续测试表明，赋予论文初始提升可使其后续选择率提高 45.55 个百分点。 研究结果表明，简单的社会信号就能显著扭曲 AI 驱动的文献关注，这引发了对自动化研究评估系统中偏见和同质化的担忧。理解这些动态有助于设计能够更好反映科学多样重要性而非仅仅受欢迎程度的 AI 代理。 该研究包括五个独立组和五个社会影响组，每组 100 个按顺序行动的 AI 代理；社会影响组每个代理选择的论文减少了 17.2%，选择更集中，合计覆盖 73 篇不同论文而独立组覆盖 90 篇，且社会信息下组间差异更大。第二个实验中，200 个代理分布在二十个社会社区中，随机为五篇论文提供初始选择，使这些论文的后续选择概率提高 45.55 个百分点（95%置信区间：41.20–49.90）；与外部引用计数的对应关系 modest，与下载计数的对应关系 negligible。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 论文将最初用于研究社会影响如何塑造音乐流行度的 Music Lab 实验设计改编到了学术注意力市场，其中 AI 代理根据标题和摘要选择论文。顺序决策框架描述了每个代理的选择在可见社会信息时如何影响后续代理。通过将 AI 代理视为人工“市场”的参与者，研究隔离了简单流行度信号对集体注意模式的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.simplypsychology.org/experimental-designs.html">Experimental Design - Simply Psychology Research Design and Methods | MUsic Technology Online Repository Experimental Design - Types, Methods, Guide - Research Method Chrome Music Lab - Experiments with Google The studio as experimental lab (Chapter 8) - Music Technology Guide to Experimental Design | Overview, Steps, & Examples</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/sequential-decision-problems-in-ai/">Sequential Decision Problems in AI - GeeksforGeeks</a></li>
<li><a href="https://musiclab.chromeexperiments.com/">Chrome Music Lab</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#social influence`, `#scientific attention`, `#experimental economics`, `#research evaluation`

---

<a id="item-17"></a>
## [漏积分器方法抑制递归预测中的误差累积。](https://arxiv.org/abs/2609.23378) ⭐️ 8.0/10

论文提出了一种免训练的漏积分器重建方法，通过将积分器的极点移动到单位圆内部（H(z)=1/(1‑γz⁻¹)，γ<1）来限制递归差分时间序列预测中的误差累积。 该方法提供了一种简单且通用的修复方案，适用于各种神经架构和数据集，能够在长期预测 horizon 上将误差降低多达约 50%，而在不存在误差累积时不会造成伤害，因而可作为任何预测器的安全默认设置。 使用固定的 γ=0.9（无需重新训练，仅需两行代码更改），在七种发散架构和二十个数据集上，平均误差提升从 horizon 24 的约 3% 增长到 horizon 336 的约 51%，且在预测器已经稳定时该方法理论上不会产生影响。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 递归差分预测通过预测一步变化并使用累积求和来重建序列，这相当于一个极点位于单位圆上的离散积分器。当非线性模型进行递归推演时，这个极点会导致误差累积并发散，从而在长期预测 horizon 上产生较大误差。漏积分器通过将极点移动到单位圆内部来替代纯积分器，从而在保持信号重建能力的同时抑制误差的累积。该修改可以在推理时直接应用，无需对底层模型进行重新训练。

**标签**: `#time-series forecasting`, `#error accumulation`, `#leaky integrator`, `#recursive differencing`, `#machine learning`

---

<a id="item-18"></a>
## [时间解释将期望效用理论与非遍历经济学联系起来](https://arxiv.org/abs/1801.03680) ⭐️ 8.0/10

该论文表明，遍历经济学中的增长最优性通过将遍历转换视为效用函数，与期望效用理论对应，并将其推广到一般的财富动态类别。 这种联系为基于财富动态选择效用函数提供了理论基础，并表明风险偏好由经济过程的性质决定，可能影响经济建模和决策理论。 作者将增长最优性从加法和乘法赌注扩展到广泛的财富动态类别，表明遍历转换充当效用函数，并且财富动态强烈决定风险偏好。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 遍历经济学区分时间平均和期望值，主张代理人应最大化财富的时间平均增长率（增长最优性），而不是效用的期望值。期望效用理论是占主导的模型，假设代理人最大化心理转换后财富的期望值。论文表明，当遍历转换被视为效用函数时，两种框架等价，从而在它们之间架起了一座桥梁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ergodicity_economics">Ergodicity economics - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1801.03680">[1801.03680] The time interpretation of expected utility theory The time interpretation of expected utility theory - IDEAS/RePEc Expected Growth Criterion: An Axiomatization - arXiv.org LongEU: Long-Term Expected Utility Analysis Ergodicity Economics in Plain English - Researchers.One</a></li>
<li><a href="https://christophegaron.com/articles/research/understanding-the-time-interpretation-of-expected-utility-theory-in-ergodicity-economics/">Understanding the Time Interpretation of Expected Utility ...</a></li>

</ul>
</details>

**标签**: `#ergodicity economics`, `#expected utility theory`, `#time averages`, `#wealth dynamics`, `#growth optimality`

---

<a id="item-19"></a>
## [通过 Heston 模型方差积分反驳 Gatheral 猜想](https://arxiv.org/abs/2609.05047) ⭐️ 8.0/10

作者证明，在完全负相关的 Heston 模型下，其方差积分在凸序上严格小于校准局部波动率模型的方差积分，从而反驳了 Gatheral 的猜想。 该结果解决了量化金融中的一个悬而未决的问题，表明在负相关情况下局部波动率模型可能高估尾部风险，对模型校准和风险管理有实际影响。 证明表明对于所有 T>0 和 K>0，有𝔼[(I_T^H−K)^+] < 𝔼[(I_T^LV−K)^+]，这意味着严格的凸序关系；该结果基于现货与方差过程完全负相关（ρ = −1）的假设。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: Heston 模型是一种随机波动率模型，其中方差遵循均值回归的平方根过程；其局部波动率投影是匹配该模型边际分布的一维扩散。凸序通过函数（如看涨期权收益（X−K)^+）的期望来比较两个随机变量。Gatheral 的猜想认为，Heston 模型的方差积分在凸序上不会大于其局部波动率投影的方差积分。

**标签**: `#quantitative finance`, `#Heston model`, `#local volatility`, `#convex order`, `#Gatheral conjecture`

---

<a id="item-20"></a>
## [LLM 文本测量提升再犯预测和同伴效应估计。](https://arxiv.org/abs/2509.20634) ⭐️ 8.0/10

作者从低安全级别监狱居民的超过 20 万段书面交流中提取 LLM 嵌入并进行零样本分类，表明这些文本表示使再犯的样本外预测相比基线模型（使用 LASSO 和 LoRA 微调）提高了多达 30%。他们还提出了一种新的工具变量估计器用于同伴效应，能够处理多变量结果、稀疏网络和多维潜在同质性，并将少量人工标注与 LLM 零样本向量结合在预测驱动的同伴推断（PPPI）框架中，以获得无偏估计。 通过将自然语言处理与因果推断和犯罪学相结合，这项工作为预测再犯和量化矫正环境中的社会影响提供了更准确的工具，可为康复计划和政策决策提供信息。在稀疏网络条件下的理论保证将同伴效应方法扩展到了超越文献中占主导地位的密集网络假设，从而扩大了其在真实世界社会网络中的适用性。 预测的提升是通过 LASSO 正则化的逻辑回归和 LoRA 适配的 LLM 微调实现的，而同伴效应估计器在稀疏松弛假设下被证明是√N 一致且渐近正态的。PPPI 方法将少量人工标注的例子与 LLM 得出的零样本向量结合，以校正偏差并为同伴效应估计产生有效的置信区间。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: 再犯预测旨在预测释放个体是否会再次犯罪，传统上依赖静态协变量，如年龄和犯罪史。同伴效应估计旨在衡量个体行为如何受到同伴的影响，但标准方法常假设社会网络密集且网络形成是外生的。大型语言模型的最新进展使得从原始文本中提取语义嵌入和进行零样本分类成为可能，从而让研究人员能够将非结构化的监狱交流转化为可量化的行为度量。

**标签**: `#LLM`, `#recidivism prediction`, `#peer effects`, `#instrumental variable`, `#social science`

---

<a id="item-21"></a>
## [包含 44 个专门代理的 Agentic AI 管道用于机构资产管理](https://arxiv.org/abs/2604.02279) ⭐️ 8.0/10

论文提出了一种用于战略资产配置的 Agentic AI 管道，其中 44 个专门代理生成资本市场假设，使用 21 种竞争方法构建投资组合，并相互评议和投票。研究代理提出新的投资组合构建方法，元代理通过学习过去的预测来重写代理代码和提示，全部在投资政策声明的治理下进行。 这种架构通过自动化传统需要专家人类分析师完成的复杂资产配置任务，代表了重要的跨学科进步。通过元代理实现自我改进并用投资政策声明约束行为，它为机构提供了一条通往更高效、透明且可治理的 AI 驱动投资流程的途径。 该系统由 44 个专门代理、21 种投资组合构建技术、一个用于发明新方法的研究代理以及一个根据预测误差更新代理代码和提示的元代理组成。所有代理在投资政策声明的约束下运行，论文指出该管道的性能经验验证仍在进行中。

rss · arXiv Quantitative Finance · Sep 22, 04:00

**背景**: Agentic AI 是指能够追求目标、使用工具并具有一定自主性的系统，超越了像聊天机器人这样的狭窄工具式 AI。在多代理系统中，元代理（或元推理层）监视并修改其他代理的行为，从而实现自我改进。投资政策声明（IPS）是一份正式文件，概述了投资者的目标、风险承受能力、时间范围和限制，这里它被用来治理自治代理的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.academia.edu/66102021/Metareasoning_Structures_Problems_and_Modes_for_Multiagent_Systems_A_Survey">(PDF) Metareasoning Structures, Problems, and Modes for Multiagent ...</a></li>
<li><a href="https://enterprisedna.co/resources/guides/financial-advisory-automate-ips-creation/">How to Automate Investment Policy Statement Creation ...</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#asset allocation`, `#finance`, `#multi-agent systems`, `#machine learning`

---