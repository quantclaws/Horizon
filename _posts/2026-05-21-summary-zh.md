---
layout: default
title: "Horizon Summary: 2026-05-21 (ZH)"
date: 2026-05-21
lang: zh
---

> From 44 items, 15 important content pieces were selected

---

1. [OpenAI 模型反驳了离散几何中的核心猜想](#item-1) ⭐️ 9.0/10
2. [SpaceX S‑1 揭示每月 12.5 亿美元 AI 计算服务协议与 Anthropic](#item-2) ⭐️ 9.0/10
3. [GitHub 确认恶意 VS Code 扩展导致 3,800 个仓库被泄露](#item-3) ⭐️ 8.0/10
4. [科罗拉多州修订 SB051 法案，将开源项目排除在年龄验证要求之外](#item-4) ⭐️ 8.0/10
5. [Qwen3.7-Max: The Agent Frontier](#item-5) ⭐️ 8.0/10
6. [Mozilla 在 SpiderMonkey 中移除 asm.js 支持，转向 WebAssembly](#item-6) ⭐️ 8.0/10
7. [Railway 在 2026 年 5 月 19 日 GCP 账户被暂停导致服务中断](#item-7) ⭐️ 8.0/10
8. [谷歌转向 AI 答案，威胁开放网络流量](#item-8) ⭐️ 8.0/10
9. [Meta 在沙特阿拉伯和阿联酋封锁人权账号](#item-9) ⭐️ 8.0/10
10. [摊销永续期权：一种新的链上 DeFi 风险基元](#item-10) ⭐️ 8.0/10
11. [估值获胜者：何时及如何在随机实验中纠正选择偏差](#item-11) ⭐️ 8.0/10
12. [研究量化 MEV 构建者影响和以太坊三明治攻击频率](#item-12) ⭐️ 8.0/10
13. [AlphaSAGE：基于 GFlowNets 的结构感知 Alpha 挖掘框架，实现鲁棒探索](#item-13) ⭐️ 8.0/10
14. [RobustiPy：用于多宇宙分析和模型不确定性的新 Python 库。](#item-14) ⭐️ 8.0/10
15. [噪声量子神经网络的量化通用逼近定理](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 模型反驳了离散几何中的核心猜想](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) ⭐️ 9.0/10

OpenAI 内部的语言模型生成了一个反例，推翻了离散几何中由保罗·埃尔德什提出的 80 年历史的单位距离猜想。 这一结果标志着 AI 驱动的数学取得里程碑，表明大型语言模型能够为长期悬而未决的理论问题提供新见解，并有望加速离散几何及其他领域的研究。 该模型的反例在 Lean 证明助手中被形式化并验证，构造过程中借鉴了代数数论的深刻思想，给出了一组有限点集，其单位距离关系违背了原猜想。

hackernews · tedsanders · May 20, 19:05 · [社区讨论](https://news.ycombinator.com/item?id=48212493)

**背景**: 离散几何研究点、线、距离等几何对象在有限设置下的组合性质。单位距离问题询问在平面上 n 个点中，相同距离出现的最大次数；埃尔德什猜想该数量大约按 n^{1+c/log log n} 增长，这一猜想悬而未决数十年。近期的人工智能工作开始协助数学家生成证明或反例，将重点从纯粹的证明自动化扩展到也寻找 falsifying 实例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry | OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2603.19514">[2603.19514] Learning to Disprove: Formal Counterexample Generation ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对使用大型语言模型寻找反例的新颖性表示兴奋，指出该证明借鉴了出人意料的代数数论思想，并在 Lean 中进行了形式化。一些人认为虽然得到反例比证明猜想正确更容易，但这项工作仍展示了模型跨学科推理的能力，有助于应对科学日益增加的专业化。还有人强调，AI 驱动的反例生成可能很快成为数学发现的常规工具。

**标签**: `#AI`, `#mathematics`, `#discrete geometry`, `#OpenAI`, `#theorem proving`

---

<a id="item-2"></a>
## [SpaceX S‑1 揭示每月 12.5 亿美元 AI 计算服务协议与 Anthropic](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 9.0/10

SpaceX 的 S‑1 档案显示，其已与 Anthropic 签订云服务协议，以每月 12.5 亿美元的价格通过 COLOSSUS 和 COLOSSUS II 系统提供 AI 计算能力，合同有效期直至 2029 年 5 月。 此协议标志着 SpaceX 进军 AI 云计算市场的大胆举措，可能改变大规模 AI 训练的竞争格局，并提供巨额稳定的收入流，有助于支撑其高估值。 容量将在 2026 年 5 月和 6 月以降低费用逐步提升，协议可在 90 天通知后终止，且同样的 COLOSSUS 基础设施也用于在 COLOSSUS II 上训练 SpaceX 自身的 Grok 5 模型。

rss · Simon Willison · May 20, 22:26

**背景**: SpaceX 最以其发射服务和 Starlink 卫星星座而闻名，一直在开发 COLOSSUS 超级计算机以支持其内部 AI 项目，如 Grok 系列语言模型。COLOSSUS 位于美国田纳西州孟菲斯，建设始于 2024 年，于 2024 年中旬投入运营，规模已扩展到数十万块 GPU，并瞄准达到百万 GPU 的规模。Anthropic PBC 是一家专注于 AI 研究并以公共利益公司形式运营的企业，以其 Claude 语言模型而知名；S‑1 档案是公司在准备首次公开募股（IPO）时向美国证券交易委员会（SEC）提交的文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://x.ai/news/anthropic-compute-partnership">New Compute Partnership with Anthropic | xAI</a></li>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>

</ul>
</details>

**社区讨论**: 评论者对 SpaceX 的财务状况表示怀疑，指出其收入相对较低却估值极高，并质疑如此巨额 AI 计算协议的盈利能力。几位评论者怀疑在太空中建设数据中心的可行性，认为散热和工程挑战将超过任何潜在优势。也有评论者指出 Starlink 产生强劲现金流，可用于资助 AI 投资，而另一些人则惊讶于 SpaceX 的收入竟然低于许多规模较小的公司，尽管市场对其估值很高。

**标签**: `#SpaceX`, `#Anthropic`, `#AI compute`, `#Cloud services`, `#SEC filing`

---

<a id="item-3"></a>
## [GitHub 确认恶意 VS Code 扩展导致 3,800 个仓库被泄露](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) ⭐️ 8.0/10

GitHub 确认，一个恶意的 Visual Studio Code 扩展在 2026 年 5 月 compromises 一名员工的设备，导致约 3,800 个内部仓库被泄露。威胁组织 TeamPCP 声称负责此次攻击，并试图以超过 50,000 美元出售被盗数据。 此次泄露凸显了针对开发者工作站的供应链攻击风险日益增加，表明像 VS Code 扩展这样的受信任工具可能成为大规模数据盗窃的途径。这影响了对 VS Code 市场的信任，并凸显了加强扩展验证和监控的必要性。 该恶意扩展利用 VS Code 的自动更新功能像蠕虫一样传播，在签名验证被禁用或使用被泄露的 GitHub PAT 发布受污染包时绕过验证。TeamPCP 声称已窃取数据并在地下市场出售。

hackernews · Timofeibu · May 20, 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48207660)

**背景**: VS Code 扩展会被打包并签名；市场在安装时会验证签名以确保完整性和真实性。然而，扩展可以在无需用户交互的情况下自动更新，如果签名验证被绕过，攻击者可以悄悄推送恶意代码。开发者工作站已成为软件供应链的主要攻击目标，因为它们通常能够访问内部代码和凭据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/github-breached-vs-code-extension">GitHub Breached via VS Code Extension | Developer Supply Chain Attack 2026</a></li>
<li><a href="https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html">Self-Spreading 'GlassWorm' Infects VS Code Extensions in Widespread ...</a></li>
<li><a href="https://code.visualstudio.com/docs/configure/extensions/extension-marketplace">Extension Marketplace</a></li>

</ul>
</details>

**社区讨论**: 评论者对扩展安全长期存在的薄弱环节表示担忧，有人惊讶攻击者能够保持足够长的在线时间窗口来窃取数据。其他人推测可能是 nx‑console 扩展被破坏，并呼吁负责 VS Code、npm 和 GitHub 的公司共同寻找解决方案。

**标签**: `#security`, `#VSCode`, `#GitHub`, `#supply-chain`, `#extension vulnerability`

---

<a id="item-4"></a>
## [科罗拉多州修订 SB051 法案，将开源项目排除在年龄验证要求之外](https://legiscan.com/CO/bill/SB051/2026) ⭐️ 8.0/10

科罗拉多州的 SB051 年龄验证法案已修订，将开源项目排除在其覆盖范围之外，新增豁免条款，排除来自免费公开代码仓库的应用程序。修订后明确规定，“受保护应用”不包括来源于免费公开代码仓库的软件。 此豁免表明立法机构认识到开源软件不应承担年龄验证强制要求的合规负担，可能影响其他州的类似法案。这对开发者、开源项目以及仍需为受保护应用执行年龄验证的操作系统提供者产生影响。 法案将“受保护应用”定义为通过受保护应用商店访问的消费者软件，并排除（i）不处理用户个人数据的应用，（ii）来源于免费公开代码仓库的应用。苹果、谷歌、微软等操作系统提供者仍需承担年龄验证义务。

hackernews · ki4jgt · May 20, 20:28 · [社区讨论](https://news.ycombinator.com/item?id=48213651)

**背景**: 科罗拉多州立法者一直在推动在操作系统层面实施年龄验证要求，目标是让苹果、谷歌、微软等公司在用户访问某些内容前验证年龄。其他州也出现类似提案，常以保护儿童为名，但引发隐私和安全方面的批评。开源开发者警告说，此类强制要求可能给不收集个人数据的项目带来不合理的合规负担。该修订增加了对来自免费公开代码仓库的软件的明确豁免，以回应这些担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yro.slashdot.org/story/26/04/25/2124221/colorado-adds-open-source-exemption-to-age-verification-bill">Colorado Adds Open-Source Exemption to Age-Verification Bill - Slashdot</a></li>
<li><a href="https://www.theregister.com/2026/04/22/linux_us_state_age_verificaiton_laws/">Linux may get exemption from Colorado age-check bill • The Register</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pHaWRESkVCSHN0Rkx3eml2RjhDZ0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - California law requires age verification in operating...</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎开源豁免，认为这表明法案的赞助者认识到这与安全无关；其他人则批评该立法是过度的“为孩子着想”举动，并警告这是滑坡的开始。有人开玩笑说，该豁免可能导致科罗拉多州出现大量与色情相关的开源应用。

**标签**: `#legislation`, `#open source`, `#age verification`, `#policy`, `#Colorado`

---

<a id="item-5"></a>
## [Qwen3.7-Max: The Agent Frontier](https://qwen.ai/blog?id=qwen3.7) ⭐️ 8.0/10

Qwen 发布了 Qwen3.7-Max，这是一个具代理能力的语言模型，拥有 100 万 token 上下文窗口并使用显式链式思考推理，声称其反幻觉性能达到业界领先，超越 Opus 4.7 和 Gemini 3.1 Pro 等模型。 其高反幻觉率和代理功能可能降低对专有 API 的依赖，为复杂推理任务提供具有竞争力的开放权重替代方案，惠及开发者和企业。 Qwen3.7-Max 采用正交解耦架构并具备 100 万 token 上下文窗口，支持显式链式思考推理。该模型在多项国内评测中排名领先，并以具有竞争力的价格定位。

hackernews · kevinsimper · May 20, 10:35 · [社区讨论](https://news.ycombinator.com/item?id=48205626)

**背景**: 代理导向的语言模型被设计用于执行多步骤任务，如规划、调用工具和代码生成，而不仅仅是简单的问答。减少幻觉——模型生成虚假或无依据信息——仍然是大型语言模型的核心挑战，最近的研究表明完全消除幻觉可能存在根本限制。开源的 Qwen 模型可通过 Ollama、vLLM 或 Open WebUI 等工具在本地部署，亦可通过 DashScope API 或 OpenAI 兼容的包装器进行访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/28161">Tongyi Lab Launches Qwen 3 . 7 - Max with Orthogonal Decoupling...</a></li>
<li><a href="https://arxiv.org/abs/2401.11817">[2401.11817] Hallucination is Inevitable: An Innate Limitation of Large Language Models</a></li>
<li><a href="https://huggingface.co/blog/daya-shankar/open-source-llms">Best Open - Source LLM Models in 2026: Coding, Local, Agentic AI...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Qwen3.7-Max 声称的最先进反幻觉率，认为其超越 Opus 4.7、Gemini 3.1 Pro 和 GPT‑5.5，同时也欣赏该模型作为免费且强大的专有编码助手替代品。一些用户呼吁给出与最新竞争对手版本的更清晰比较，希望通过超大规模云服务商合作实现美国本地托管，并询问诸如 OpenRouter 之类的实际托管方案以获得低延迟访问。

**标签**: `#Qwen`, `#LLM`, `#AI agents`, `#non-hallucination`, `#open-source models`

---

<a id="item-6"></a>
## [Mozilla 在 SpiderMonkey 中移除 asm.js 支持，转向 WebAssembly](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html) ⭐️ 8.0/10

Mozilla 的 SpiderMonkey 博客宣布移除 asm.js 支持，标志着其正式被废弃，因为已被 WebAssembly 取代。 此次废弃凸显了 asm.js 在实现近原生网页性能方面的历史作用及其对 WebAssembly 发展的影响，影响着依赖它将 C/C++ 代码移植到网页的开发者。 SpiderMonkey 将在未来的 Firefox 版本中移除 asm.js 专用优化，现有 asm.js 代码仍可运行但不会获得性能提升。此举符合将 WebAssembly 作为首选编译目标的总体趋势，以支持高性能网页应用。

hackernews · eqrion · May 20, 12:01 · [社区讨论](https://news.ycombinator.com/item?id=48206340)

**背景**: asm.js 是一种严格的 JavaScript 子集，旨在让从 C/C++ 编译的代码在网页中实现近原生性能，最早从 Firefox 22 开始进行优化。它是 Mozilla 对 NaCl 和 PNaCl 等技术的回答，后来被 WebAssembly 取代。SpiderMonkey 是 Mozilla 的 JavaScript 和 WebAssembly 引擎，驱动 Firefox 并在 MongoDB、Adobe Acrobat 等项目中使用，拥有包括 WarpMonkey 在内的多代 JIT 编译器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpiderMonkey_(Javascript_engine)">SpiderMonkey (Javascript engine)</a></li>

</ul>
</details>

**社区讨论**: 评论者回忆起 asm.js 在 Figma、Unreal Engine 等早期网页性能演示中的关键作用，表达怀念之情但承认转向 WebAssembly 带来了如加载时间更快等实际改进。多位评论者指出其历史意义，同时接受其废弃是合理的进步。

**标签**: `#WebAssembly`, `#asm.js`, `#JavaScript`, `#browser technology`, `#deprecation`

---

<a id="item-7"></a>
## [Railway 在 2026 年 5 月 19 日 GCP 账户被暂停导致服务中断](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage) ⭐️ 8.0/10

2026 年 5 月 19 日，Railway 的 Google Cloud Platform（GCP）账户被暂停，导致其服务中断，并促使公司发布了详细的事后分析。此事件在 Hacker News 上引发了关于谷歌云可靠性及客户影响的广泛讨论。 此次暂停凸显了依赖单一云供应商的风险，以及任意账户操作可能对下游客户造成的影响。它激发了工程师们关于多云策略以及需要云供应商更大透明度的讨论。 Railway 表示计划将 GCP 服务从数据平面的热路径中移除，仅保留作为次要/故障转移使用，而事后分析未披露暂停的确切原因。谷歌云暂停可能由服务条款违规、未付款或疑似欺诈导致，这并不是 Railway 首次遇到此类事件。

hackernews · 0xedb · May 20, 08:37 · [社区讨论](https://news.ycombinator.com/item?id=48204770)

**背景**: Railway 是一个一体化的云平台，使开发者能够在不管理网络或基础设施的情况下部署应用，定位为传统 PaaS 的竞争者。当谷歌因政策违规、未付款或疑似欺诈而暂停一个账户或项目时，所有关联的 GCP 资源将被切断，直至问题得到解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://railway.com/">Railway | The all-in-one intelligent cloud provider</a></li>
<li><a href="https://cloud.google.com/channel/docs/concepts/google-cloud/suspension">Google Cloud suspensions overview | Channel Services | Google Cloud Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者对他们认为的任意且频繁的 GCP 账户暂停表示不满，质疑谷歌云作为 B2B 供应商的可信度。一些人指出 Railway 应该提前预见到这种风险并正在计划减少对 GCP 的依赖，而另一些人则赞赏公司诚实的事后分析并接受了此次中断的责任。

**标签**: `#GCP`, `#cloud outage`, `#incident report`, `#Railway`, `#cloud reliability`

---

<a id="item-8"></a>
## [谷歌转向 AI 答案，威胁开放网络流量](https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/) ⭐️ 8.0/10

文章认为谷歌正在越来越多地优先考虑 AI 生成的答案，而不是传统搜索链接，从而减少了对网站的推荐流量。 这种转变威胁到依赖谷歌流量的出版者和创作者的收入模式，引发了对 AI 对开放网络生态系统影响的更广泛担忧。 谷歌的搜索生成式体验（SGE）和 AI 概览现在直接回答查询，研究表明多达 75%的查询可以在不点击的情况下得到满足，出版商报告称搜索引荐流量下降了 40‑60%。

hackernews · cdrnsf · May 20, 21:33 · [社区讨论](https://news.ycombinator.com/item?id=48214449)

**背景**: 谷歌的搜索生成式体验（SGE）是在 2023 年 Google I/O 上推出的，利用生成式 AI 直接在搜索结果中提供答案，从而减少用户点击进入源网站的需求。过去，网站允许谷歌抓取其内容，以换取推荐流量，形成了对出版商和搜索引擎都有利的共生关系。同时，AI 公司抓取公开可用的网页内容来训练大型语言模型，这引发了关于数据使用和补偿的法律和伦理问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seo.ai/blog/search-generative-experience-impact-seo">How Search Generative Experience Will Impact SEO: 5 Insights</a></li>
<li><a href="https://www.toprankmarketing.com/blog/ai-search-trends-google-sge-organic-traffic/">Age of SGE: How Will AI Affect Search Traffic in the Next Decade?</a></li>
<li><a href="https://searchengineland.com/ai-answers-disrupting-publisher-revenue-advertising-465185">How AI answers are disrupting publisher revenue and advertising</a></li>

</ul>
</details>

**社区讨论**: 评论者担心 AI 系统在未补偿的情况下挪用创意作品，迫使创作者考虑付费墙或完全放弃出版。一些人指出谷歌抓取与流量的共生关系，警告切断流量会移除网站允许索引的动机，而另一些人则怀念像 StumbleUpon 这样的独立流量来源，并批评 AI 摘要经常不准确。

**标签**: `#Google`, `#web`, `#AI`, `#content scraping`, `#internet policy`

---

<a id="item-9"></a>
## [Meta 在沙特阿拉伯和阿联酋封锁人权账号](https://www.alqst.org/ar/posts/1190) ⭐️ 8.0/10

Meta 限制了独立非政府组织、研究人员和公民社会人士的 Facebook 和 Instagram 账户，使其在沙特阿拉伯和阿联酋的用户看不到，这是在政府要求下进行的，且符合科技公司顺从压迫性政权的模式。 此举引发人们对企业在审查中的共谋的担忧，威胁到海湾地区活动人士的言论自由，凸显了社交媒体平台在威权压力下塑造公共话语的能力。同时也引发了关于科技公司应抵制侵犯人权的政府要求的责任争论。 该限制同时适用于 Facebook 和 Instagram，使这些账户在沙特阿拉伯和阿联酋的用户动态和搜索结果中不可见，权利组织联盟披露了此决定并予以谴责。Meta 尚未发表公开声明，该行动被认为是通过地理封锁工具按地区限制内容实现的。

hackernews · giuliomagnifico · May 20, 12:43 · [社区讨论](https://news.ycombinator.com/item?id=48206768)

**背景**: Meta（前身为 Facebook）运营着全球最大的社交网络，并常常使用地理封锁来遵守当地法律，这一做法在政府要求时可被用来沉默异议。Facebook 和 Instagram 等平台的内容审核政策涉及自动化系统和人工审核，政府常利用这些工具压制批评性言论。影子封禁——使内容难以被发现而不直接封禁——是平台可能采用的另一种策略，无论是自愿还是在压力下，以限制特定账号的传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alqst.org/ar/posts/1190">Meta blocks human rights accounts from reaching audiences in Saudi Arabia and the UAE</a></li>
<li><a href="https://jsis.washington.edu/news/german-content-moderation-and-platform-liability-policies/">German Content Moderation and Platform Liability Policies</a></li>
<li><a href="https://www.business-humanrights.org/it/ultime-notizie/alleged-shadow-banning-of-palestinian-supporters-on-instagram-tiktok/">Alleged 'shadow banning' of Palestinian supporters on ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Alqst 网站本身在阿联酋也被封锁，需要使用 VPN 才能阅读文章，并批评 Meta 将利润置于原则之上。有人认为拒绝配合可能导致更糟的本地替代品，而另一些人则称 Meta 是最差的平台，并表示个人已经远离其服务。

**标签**: `#social media`, `#content moderation`, `#human rights`, `#tech ethics`, `#Middle East`

---

<a id="item-10"></a>
## [摊销永续期权：一种新的链上 DeFi 风险基元](https://arxiv.org/abs/2605.19146) ⭐️ 8.0/10

该论文提出了一种适应链上约束的摊销永续期权（AmPOs）设计，提供了一种需求一致性最低的去中心化市场框架。该合约作为 DeFi 的基础风险基元，能够实现内生抵押和明确定价的去挂钩保险。 通过提供无需信任且 oracle 轻量的衍生品，AmPOs 使协议能够在不依赖中心化清算的情况下共担尾部风险，从而可能扩展链上金融产品的范围。这有望提升 DeFi 稳定性，并催生诸如协议级保险和抵押等新用例。 AmPOs 是可互换的、分期付款的永续期权，通过随时间摊销保费来减少对高频价格喂食或激进清算机制的需求。该设计在对抗性链上假设下运行，仅需最低的一致性保证即可保证正确性。

rss · arXiv Quantitative Finance · May 20, 04:00

**背景**: 永续期权是一种赋予持有者在预定价格买卖资产的权利但没有义务的衍生品，且没有到期日。链上实现一直面临挑战，因为它们通常需要频繁的 oracle 更新和强大的清算引擎来管理风险，这些在市场压力下可能失效。摊销永续期权通过随时间分摊保费成本并降低对实时数据的依赖来解决这些问题，使其更适合去中心化且对抗性的区块链环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.19146">Designing On - Chain Options : Amortizing Perpetual Options</a></li>
<li><a href="https://arxiv.org/abs/2512.06505">[2512.06505] Amortizing Perpetual Options - arXiv</a></li>
<li><a href="https://panoptic.xyz/docs/trading/perpetual-options">Perpetual options - Panoptic</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#on-chain options`, `#blockchain finance`, `#risk primitives`, `#perpetual options`

---

<a id="item-11"></a>
## [估值获胜者：何时及如何在随机实验中纠正选择偏差](https://arxiv.org/abs/2605.18887) ⭐️ 8.0/10

该文区分了随机实验中的全局和选择性胜者诅咒偏差，将其与 regret 联系起来，并表明偏差校正必须与决策者的评估目标相匹配。此外，它提出了一种自适应经验似然过程，能够在各种设置下提供渐近有效的置信区间。 了解根据实验的具体目标选择哪种偏差校正方法，有助于从业者在 A/B 测试和因果推断中避免高估治疗效果。该框架指导方法选择，提高在部署表现最佳治疗时的决策质量。 作者定义了七个与决策相关的评估目标（全局和选择性胜者诅咒的均值偏差、均方误差、置信区间覆盖率以及均值 regret），并表明没有单一方法在所有情况下占优：插值估计器在治疗差异大时表现最佳，交叉拟合在治疗相似时最优，重抽样方法在中等差异下均方误差低。他们的自适应经验似然过程提供免调参、渐近有效的置信区间。

rss · arXiv Quantitative Finance · May 20, 04:00

**背景**: 在随机实验中，选择观察结果最高的治疗可能导致胜者诅咒：所选治疗的估计效应会被随机噪声抬高而出现向上偏差。这种偏差会导致 regret，因为所选治疗可能并非真正最佳。纠正这种选择偏差对于在线 A/B 测试和医学试验等领域的可靠推断至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1006916">Statistical correction of the Winner ’ s Curse explains... | PLOS Genetics</a></li>
<li><a href="https://www.kdd.org/kdd2018/accepted-papers/view/winners-curse-bias-estimation-for-total-effects-of-features-in-online-contr">KDD 2018 | Winner ’ s Curse : Bias Estimation for Total Effects of...</a></li>
<li><a href="https://www.investopedia.com/terms/w/winnerscurse.asp">investopedia.com/terms/w/winnerscurse.asp</a></li>

</ul>
</details>

**标签**: `#A/B testing`, `#selection bias`, `#winner's curse`, `#causal inference`, `#experimental design`

---

<a id="item-12"></a>
## [研究量化 MEV 构建者影响和以太坊三明治攻击频率](https://arxiv.org/abs/2508.04003) ⭐️ 8.0/10

论文发现，两个 MEV 构建者生产了以太坊近 80%的区块，他们若想保持在前四分之一的区块构建者中，将需要合计每月约 1400 万美元。此外，三明治攻击平均每区块发生超过一次，这些攻击的 Gas 费用占支付给验证者的 MEV 的约 15%。 结果凸显了少数实体在区块构建权力中的日益集中，揭示了可能破坏交易公平性并增加 DeFi 用户提取成本的显著经济激励。理解这些动态对于设计诸如 Gas 费优先机制或私有交易池等缓解措施以减少有害 MEV 至关重要。 该研究估计，两个主导构建者需要合计每月花费近 1400 万美元才能保持在前四分之一，且三明治攻击平均每区块发生超过一次，其 Gas 费用占支付给验证者的 MEV 的约 15%。研究还指出，Gas 费优先或私有交易池等改革可能有助于缓解这些影响。

rss · arXiv Quantitative Finance · May 20, 04:00

**背景**: MEV（Miner Extractable Value）指的是矿区块生产者通过重新排序、包含或排除交易，在标准区块奖励和 Gas 费之外所能获得的额外价值。在以太坊上，区块构建者（在提出者‑构建者分离机制下）将交易组装成区块，并可通过套利、清算和三明治攻击等策略提取 MEV。三明治攻击是指攻击者先抢先交易再倒挂交易，从受害者交易引起的价格波动中获利。私有交易池（或私有 RPC）将交易直接发送给构建者，使其对公共内存池不可见，从而降低被寻求 MEV 机会的搜索者发现的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ethereum.org/developers/docs/mev/">Maximal extractable value ( MEV ) | ethereum.org</a></li>
<li><a href="https://www.coingecko.com/learn/sandwich-attacks-prevention-crypto">What Are Sandwich Attacks in Crypto and How to... | CoinGecko</a></li>
<li><a href="https://dev.to/moonsoon69/how-to-build-a-mev-protected-swap-service-in-typescript-3lo1">How to Build a MEV -Protected Swap Service in... - DEV Community</a></li>

</ul>
</details>

**标签**: `#Ethereum`, `#MEV`, `#blockchain`, `#transaction ordering`, `#sandwich attacks`

---

<a id="item-13"></a>
## [AlphaSAGE：基于 GFlowNets 的结构感知 Alpha 挖掘框架，实现鲁棒探索](https://arxiv.org/abs/2509.25055) ⭐️ 8.0/10

该论文提出了 AlphaSAGE 框架，将结构感知的关系图卷积网络编码器与生成流网络（GFlowNets）以及密集的多方面奖励相结合，以挖掘多样且不相关的预测性 Alpha。该工作发表在 arXiv:2509.25055v3，并提供了开源代码 https://github.com/BerkinChen/AlphaSAGE。 AlphaSAGE 解决了现有基于强化学习的 Alpha 挖掘方法的三个核心限制——奖励稀疏、表达式的顺序表示不足以及缺乏多样性——通过提供一种原则性的、探索友好的方法，能够产生更丰富的交易信号组合。这一进展有望提升量化交易策略的鲁棒性和表现。 该框架采用关系图卷积网络（RGCN）来编码数学表达式的语法和语义结构，使用 GFlowNets 按照学习到的奖励采样表达式，并引入密集奖励设计以在中间步骤提供反馈。代码和实验在 GitHub 上公开提供。

rss · arXiv Quantitative Finance · May 20, 04:00

**背景**: 自动化 Alpha 挖掘旨在从金融数据中发现预测公式，通常被建模为强化学习任务，其中智能体逐步构建表达式。传统的 RL 方法面临奖励稀疏（仅完整公式才有反馈）、使用忽略表达式结构的简单顺序表示，以及优化单一高奖励模式导致多样性不足的问题。生成流网络（GFlowNets）通过训练策略使得对象的采样概率与奖励成比例，从而在结构化、多模态空间中实现高效探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/aiguys/gflownets-the-next-big-idea-in-ai-d2ad78e3a88f">GFlowNets , Generative Flow Networks | AIGuys</a></li>
<li><a href="https://arxiv.org/html/2509.25055v1">AlphaSAGE: Structure - Aware Alpha Mining via GFlowNets for...</a></li>
<li><a href="https://www.emergentmind.com/topics/generative-flow-networks-gflownets">Generative Flow Networks ( GFlowNets )</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#alpha mining`, `#GFlowNets`, `#reinforcement learning`, `#structured representation`

---

<a id="item-14"></a>
## [RobustiPy：用于多宇宙分析和模型不确定性的新 Python 库。](https://arxiv.org/abs/2506.19958) ⭐️ 8.0/10

RobustiPy 是一个开源的 Python 包，它整合了 bootstrap 推断、组合规范搜索、模型选择/平均以及可解释人工智能方法，以实现大规模多宇宙分析和模型不确定性量化。 通过提供统一且计算高效的鲁棒性检验框架，RobustiPy 帮助研究人员评估其结果对分析选择的敏感性，从而在经济学、社会学、心理学和医学等领域提高可重复性。 该库在约 6.72 亿次模拟回归上进行基准测试，展示了最先进的计算速度，同时支持样本外验证和协变量贡献量化。

rss · arXiv Quantitative Finance · May 20, 04:00

**背景**: 多宇宙分析考察不同可辩护的建模选择如何影响同一假设的结果，以解决研究者自由度和复制危机问题。模型不确定性量化衡量因在竞争统计模型之间选择而产生的不确定性，常使用贝叶斯或信息准则方法。Bootstrap 推断通过有放回重抽样数据来估计抽样分布并构建置信区间，无需依赖参数假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multiverse_analysis">Multiverse analysis</a></li>
<li><a href="https://www.researchgate.net/publication/361558260_How_is_model-related_uncertainty_quantified_and_reported_in_different_disciplines">(PDF) How is model -related uncertainty quantified and reported in...</a></li>
<li><a href="https://medium.com/data-science/bootstrap-and-statistical-inference-in-python-a06d098a8bfd">Bootstrap and Statistical Inference in Python | by Leihua Ye... | Medium</a></li>

</ul>
</details>

**标签**: `#Python`, `#multiverse analysis`, `#model uncertainty`, `#explainable AI`, `#bootstrap`

---

<a id="item-15"></a>
## [噪声量子神经网络的量化通用逼近定理](https://arxiv.org/abs/2604.02064) ⭐️ 8.0/10

该论文提出了噪声量子神经网络的量化通用逼近定理，给出了依赖于电路深度、宽度和噪声强度的显式非渐近误差界。随后，作者在实际噪声量子硬件上进行了数值实验，重点验证了金融相关的期望估计。 通过在真实噪声下为量子神经网络提供严格的误差保证，该工作连接了理论逼近与近期量子设备实验之间的差距。这使得量子机器学习在量化金融及其他需要精确误差控制的领域中的应用变得可信。 该定理表明，对于任何可表示为期望的目标函数，足够深度和宽度的噪声量子神经网络能够以误差 ε 进行逼近，其中 ε 与噪声水平的倒数呈多项式关系，并与网络规模成反比。实验在 IBM 的超导量子比特处理器上进行，展示了在现实去极化噪声下估计的期望值与经典蒙特卡罗基线的收敛。

rss · arXiv Quantitative Finance · May 20, 04:00

**背景**: 通用逼近定理保证一族神经网络能够稠密逼近任何连续函数，构成了经典深度学习的理论基础。将此概念推广到量子神经网络时，必须考虑不可避免的硬件噪声，因为噪声会破坏幺正演化并降低表达能力。在量化金融领域，目标函数常常表现为随机过程的期望，因此为噪声量子神经网络提供显式误差界对于在近期设备上保证可靠预测至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem - Wikipedia</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/40202891/">Universal Approximation Theorem and Error Bounds for Quantum ...</a></li>
<li><a href="https://arxiv.org/html/2604.02064v3">Quantitative Universal Approximation for Noisy Quantum Neural Networks</a></li>

</ul>
</details>

**标签**: `#quantum machine learning`, `#universal approximation`, `#noisy quantum neural networks`, `#quantum finance`, `#hardware experiments`

---