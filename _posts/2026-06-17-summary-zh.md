---
layout: default
title: "Horizon Summary: 2026-06-17 (ZH)"
date: 2026-06-17
lang: zh
---

> From 58 items, 19 important content pieces were selected

---

1. [GrapheneOS 已移植至 Android 17，官方版本即将发布。](#item-1) ⭐️ 8.0/10
2. [2026 年本地运行大语言模型变得可行](#item-2) ⭐️ 8.0/10
3. [Wolfram Language 和 Mathematica 版本 15 发布，内置 AI 助手及符号音乐功能。](#item-3) ⭐️ 8.0/10
4. [交互式指南用可视化解释机械表原理](#item-4) ⭐️ 8.0/10
5. [Qwen 发布面向物理世界的机器人基础模型套件](#item-5) ⭐️ 8.0/10
6. [Meta 是否在毁掉其工程组织？](#item-6) ⭐️ 8.0/10
7. [苹果将限制 Hide My Email 别名创建，削弱其隐私实用性](#item-7) ⭐️ 8.0/10
8. [Lean 4 机器检查的布朗运动伊托微积分形式化](#item-8) ⭐️ 8.0/10
9. [信念面临风险：使用 LLM 推断的贝叶斯状态过滤器量化代理 AI 模型风险](#item-9) ⭐️ 8.0/10
10. [基于预训练神经网络的快速可验证误差有界期权定价方法（适用于 GJR-GARCH）](#item-10) ⭐️ 8.0/10
11. [Hyperliquid 上可见的 TWAP 订单相比隐藏 metaorder 降低执行成本](#item-11) ⭐️ 8.0/10
12. [链式任务，重塑工作：AI 自动化理论](#item-12) ⭐️ 8.0/10
13. [概率方法识别脱碳能源系统中的技术临界点](#item-13) ⭐️ 8.0/10
14. [PHINN：受持久同调启发的神经网络用于罕见事件时间序列生成](#item-14) ⭐️ 8.0/10
15. [面向自主 AI 代理的博弈抗性保险合同及策略证明收费机制](#item-15) ⭐️ 8.0/10
16. [微笑的个人资料提升效率并减少差距。](#item-16) ⭐️ 8.0/10
17. [最优报价框架应对逆向选择和价格泄露](#item-17) ⭐️ 8.0/10
18. [本文提出了一种混合保持、无套利的波动曲面插值方法。](#item-18) ⭐️ 8.0/10
19. [Shachi：基于 LLM 的模块化代理建模框架用于研究涌现集体行为](#item-19) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GrapheneOS 已移植至 Android 17，官方版本即将发布。](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) ⭐️ 8.0/10

GrapheneOS 已成功移植至 Android 17，开发团队宣布官方版本即将发布。 此次更新确保注重隐私的用户能够在最新 Android 版本上继续获得安全加固，延长 GrapheneOS 在新款 Pixel 设备上的生命周期。 此次移植基于 Android 17（API 级别 35），并包含常规的 GrapheneOS 安全加固补丁；官方版本预计将在受支持的 Pixel 机型上尽快发布。

hackernews · Cider9986 · Jun 16, 20:34 · [社区讨论](https://news.ycombinator.com/item?id=48561654)

**背景**: GrapheneOS 是一个开源的、注重隐私的操作系统，通过去除 Google 服务并添加利用缓解措施来加固 Android，主要面向 Pixel 智能手机。Android 17 是 Android 平台最新的主要版本，引入了新的 API 和系统更改；其版本历史记载在 Android 版本历史维基页面。此次移植将 GrapheneOS 的安全增强带到该最新基线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Android_version_history">Android version history - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对 GrapheneOS 的隐私优势表示满意，称不会回到原生 Android。一些用户指出缺少滑动光标移动和反应表情处理的便利功能，以及某些银行和健身应用（如 Strava）的兼容性问题。还有人强调 Pixel 设备在全球的可用性有限，期待看到 GrapheneOS 在更多硬件上运行，甚至有一位长期 iPhone 用户考虑转换。

**标签**: `#GrapheneOS`, `#Android`, `#privacy`, `#mobile security`, `#open source`

---

<a id="item-2"></a>
## [2026 年本地运行大语言模型变得可行](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) ⭐️ 8.0/10

2026 年 6 月 15 日，Vicki Boykis 发表博客文章，认为在本地运行大语言模型已经变得可行，文中讨论了模型类型、量化、硬件需求以及对商业 API 提供商的影响。 这一转变降低了开发者和小团队尝试最先进 AI 的门槛，无需昂贵的云订阅，可能迫使托管模型提供商调整定价并提高可及性。 文章指出，像 Qwen 27B 和 Gemma 31B 这样的密集模型知识丰富但运行缓慢，而诸如 Gemma 26B 和 Qwen 35B 这样的混合专家模型速度更快却容易出错；4 位量化虽然降低了显存需求，但会削弱工具调用能力；现代显卡如 RTX 5090 或 Apple M4 Ultra 提供了足够的 VRAM 以实现本地推理。

hackernews · jfb · Jun 16, 14:36 · [社区讨论](https://news.ycombinator.com/item?id=48555993)

**背景**: 大型语言模型需要大量内存和计算资源，过去在本地部署时面临困难。量化技术通过降低权重的数值精度来减小模型体积和推理开销，同时保持一定的性能。近期的消费级 GPU 如 NVIDIA RTX 5090 和 Apple M4 Ultra 已经提供了足够的 VRAM，能够在桌面机器上运行量化后的 LLM，这一点在硬件对比和压缩调研中得到验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://michielh.medium.com/llm-quantization-techniques-balancing-performance-and-efficiency-bc348eed3816">LLM Quantization Techniques : Balancing Performance and... | Medium</a></li>
<li><a href="https://www.fazb.com.sa/fast-local-llm-inference-hardware-choices-tuning/">Fast Local LLM Inference , Hardware ... - Faz Business | فاز الأعمال</a></li>
<li><a href="https://www.projectpro.io/article/llm-compression/1179">LLM Compression Techniques to Build Faster and Cheaper LLMs</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了复杂的情感：有人抱怨密集的本地模型仍然很慢，量化会削弱工具使用；也有人因成本和对 Claude Sonnet 4.6 等托管模型的不满而更倾向于使用本地模型；还有人指出这将给提供商带来经济压力，并希望看到具体的代码示例来评估可用性。

**标签**: `#LLM`, `#local models`, `#AI`, `#machine learning`, `#Hacker News`

---

<a id="item-3"></a>
## [Wolfram Language 和 Mathematica 版本 15 发布，内置 AI 助手及符号音乐功能。](https://writings.stephenwolfram.com/2026/06/launching-version-15-of-wolfram-language-mathematica-built-in-useful-ai-lots-of-new-core-functionality/) ⭐️ 8.0/10

Wolfram 发布了 Wolfram Language 和 Mathematica 版本 15，新增内置 AI 助手（以聊天栏形式出现在笔记本中）以及符号音乐功能，可直接进行 MIDI 风格的音符合成。 此次发布将 AI 助手更深入地融入技术工作流，提升科学家和工程师的生产力；符号音乐工具则拓展了平台的创意应用，显示 Wolfram 为了在日益增长的开源替代品中保持竞争力所做的努力。 AI 助手需要 Wolfram Language 14.1 或更高版本，并在升级到 Version 15 前安装一个 paclet；聊天栏默认位于笔记本底部，可关闭。符号音乐利用语言原生的 MIDI 风格基于音符的声音合成，用户可直接从符号表达式生成音乐。

hackernews · alok-g · Jun 16, 23:15 · [社区讨论](https://news.ycombinator.com/item?id=48563609)

**背景**: Wolfram Language 及其旗舰产品 Mathematica 长期用于符号计算、数据分析和技术原型，广泛应用于学术和工业领域。早期的 WolframTones 项目展示了平台在算法音乐生成方面的能力，而 Sound and Sonification 文档则说明了其对任意波形和 MIDI 风格合成的支持。版本 15 在此基础上内置了对话式 AI 助手，并将符号音乐功能正式纳入核心语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://writings.stephenwolfram.com/2011/06/music-mathematica-and-the-computational-universe/">Music, Mathematica, and the Computational Universe—Stephen Wolfram Writings</a></li>
<li><a href="https://reference.wolfram.com/language/guide/SoundAndSonification.html">Sound and Sonification - Wolfram Language Documentation</a></li>
<li><a href="https://www.wolfram.com/ai-assistant/">Wolfram AI Assistant</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏 Mathematica 在制作分形和动画方面的易用性，但批评其高昂的成本和封闭特性，认为 AI 助手不如 Claude 等替代品。一些人对符号音乐功能感兴趣，质疑其在实际工业中的应用，并提到免费开源替代品如 Hissab。

**标签**: `#Wolfram Language`, `#Mathematica`, `#Version 15`, `#AI assistant`, `#symbolic music`

---

<a id="item-4"></a>
## [交互式指南用可视化解释机械表原理](https://ciechanow.ski/mechanical-watch/) ⭐️ 8.0/10

2022 年，Ciechanowski 发布了一篇交互式文章，通过逐步解释和可视化带领读者了解机械表的内部工作原理。 它为钟表爱好者和学习者提供了卓越的教育资源，展示了交互式网页内容如何有效教授复杂的机械概念。 该网站仅使用原生 HTML、CSS 和 JavaScript，无需框架，因而能在旧款 iPhone 7 上运行；页面包含手绘插图以及齿轮系、擒纵机构和发条的交互式图解。

hackernews · razin · Jun 16, 11:26 · [社区讨论](https://news.ycombinator.com/item?id=48553550)

**背景**: 钟表学是研究计时装置的学科，特别是机械钟表。机械表通过上链发条储存能量，发条释放动力经过齿轮系驱动指针。擒纵机构调节这种释放，使齿轮系以离散的跳动前进，产生典型的滴答声。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Horology">Horology</a></li>
<li><a href="https://www.firgelliauto.com/blogs/mechanisms/escapement">Escapement Mechanism : How It Works, Diagram & Examples</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章清晰、富有启发性且教育价值高，有人表示因此受到激励去制作实物爆炸视图模型。他们还强调了使用原生 HTML/CSS/JS 的简洁性，指出该网站在旧设备上运行良好，并赞赏作者在自我推广上的克制。

**标签**: `#mechanical watch`, `#interactive visualization`, `#education`, `#horology`, `#web development`

---

<a id="item-5"></a>
## [Qwen 发布面向物理世界的机器人基础模型套件](https://qwen.ai/blog?id=qwen-robotsuite) ⭐️ 8.0/10

Qwen 发布了 Qwen-Robot Suite，包含 Qwen-RobotNav、Qwen-RobotManip 和 Qwen-RobotWorld 三个基础模型，实现感知、规划与控制的集成。 该套件旨在弥补具身 AI 中的感知‑行动差距，有望加速智能机器人在制造、物流等物理世界场景中的部署。 Qwen-RobotNav 负责视觉语言导航，Qwen-RobotManip 提供通用视觉语言动作能力，Qwen-RobotWorld 则是用于预测和仿真的视频世界模型。

hackernews · ilreb · Jun 16, 13:15 · [社区讨论](https://news.ycombinator.com/item?id=48554814)

**背景**: 基础模型是指在广泛数据上训练的大规模 AI 模型，能够适应多种下游任务。物理世界智能指的是 AI 系统能够感知、理解并作用于真实环境，这是机器学习中的核心挑战。感知‑规划‑控制范式将机器人行为分解为感知环境、制定计划和执行动作三个步骤。Qwen-Robot Suite 将这些阶段统一为一套模型，以实现端到端的机器人智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48554814">Qwen-Robot Suite: A Foundation Model Suite for Physical World Intelligence | Hacker News</a></li>
<li><a href="https://letsdatascience.com/news/alibaba-unveils-qwen-robot-suite-for-embodied-ai-d7c90c5a">Alibaba Unveils Qwen Robot Suite for Embodied AI | Let's Data Science</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈的热情，指出该套件有望开拓比软件服务更大的机器人市场。有人猜测可能实现快速量产，设想每年产量可达百万级，也有人希望得到技术评估以及与现有替代方案的对比。

**标签**: `#robotics`, `#foundation models`, `#Qwen`, `#AI`, `#physical world intelligence`

---

<a id="item-6"></a>
## [Meta 是否在毁掉其工程组织？](https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering) ⭐️ 8.0/10

Hacker News 上的讨论审视了关于 Meta 工程组织因 AI 痴迷、过度招聘和文化问题而恶化的说法，并包含前员工的第一手经历。 此次讨论凸显了 AI 驱动的变革对工程文化、职场毒性和人才保留的更广泛影响，这可能预示着科技公司在优先考虑 AI 举措方面将出现行业范围的变化。 评论者指出，运作良好的团队往往来自收购（WhatsApp、Reality Labs、Instagram），描述了过度招聘和需求变动，提到有 30‑50% 的基础设施工程师被调入 ADO 组织，引用了长期任职的 CISO Guy Rosen 的离职，并指责 Scale AI 创始人挖走 Meta 的顶尖工程师去做数据标注工作。

hackernews · throwarayes · Jun 16, 16:42 · [社区讨论](https://news.ycombinator.com/item?id=48558045)

**背景**: Meta 正在大力投资人工智能，成立了诸如 ADO（AI 数据运营）之类的新组织以支持其 AI 野心。这种快速的人才再分配导致了内部重组、优先级变动以及工程师压力增大的报告。公司的规模和收购成功产品的历史，使得整合后的收购团队与自建团队之间形成对比，一些员工认为自建团队管理较差。

**社区讨论**: 讨论呈现出批评与个人轶事的混合，许多人对 AI 痴迷和被感知的毒性表示担忧，而一些人则认为这些问题反映了更广泛的行业趋势，而非 Meta 特有。少数评论者为公司辩护，指出问题可能源于过度招聘和快速变化，而非故意恶意。

**标签**: `#Meta`, `#engineering culture`, `#AI impact`, `#workplace toxicity`, `#Hacker News`

---

<a id="item-7"></a>
## [苹果将限制 Hide My Email 别名创建，削弱其隐私实用性](https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/) ⭐️ 8.0/10

苹果即将对 Hide My Email 别名生成施加更严格的限制，包括每小时至少 30 个别名的速率限制以及总数上限，达到上限后用户必须删除旧别名才能创建新别名。 此更改削弱了 iCloud+ 订阅者的核心隐私工具，迫使注重隐私的用户寻求别名替代方案或采用更繁琐的变通方法，凸显了苹果生态系统在便利性与更严格控制之间的权衡。 有报道称用户达到约 1,047 个别名的上限，出现 "Email Address Limit Reached" 错误；新政策还要求服务预注册发送地址，这可能导致付款处理器或物流公司的通知中断。

hackernews · SXX · Jun 16, 18:37 · [社区讨论](https://news.ycombinator.com/item?id=48559935)

**背景**: Hide My Email 是 iCloud+ 的一项功能，能够创建唯一的随机电子邮件地址并转发到用户的真实收件箱，从而在注册时不泄露真实地址；与简单的加号地址不同，这些别名不会被跟踪网络剥离。电子邮件别名一般来说可以隐藏真实地址，并可根据需要禁用或撤销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/guide/icloud/set-up-hide-my-email-mm9d9012c9e8/icloud">Set up and use Hide My Email in iCloud+ on all your devices - Apple Support</a></li>
<li><a href="https://www.privacyguides.org/en/email-aliasing/">Email Aliasing - Privacy Guides</a></li>
<li><a href="https://apple.stackexchange.com/questions/441028/limit-number-for-hide-my-email">icloud - Limit number for " Hide my Email "? - Ask Different</a></li>

</ul>
</details>

**社区讨论**: 评论者批评预先生成别名带来的麻烦，建议使用带有捕获全部转发的自定义域名，并推荐 SimpleLogin 或 Fastmail 等服务以获得更好的灵活性；他们还指出服务必须预注册发送地址，导致错过如送货更新或发票等通知。

**标签**: `#privacy`, `#Apple`, `#Hide My Email`, `#email aliasing`, `#security`

---

<a id="item-8"></a>
## [Lean 4 机器检查的布朗运动伊托微积分形式化](https://arxiv.org/abs/2606.15089) ⭐️ 8.0/10

该论文提出了在 Lean 4 中对布朗运动在 [0,T] 上的 L^2 伊托微积分的形式化，将伊托积分构造为希尔伯特空间的等距映射，并证明了 C^3 函数（导数有界）的伊托公式。 这项工作首次在任何证明助手中给出了伊托公式的机器检验证明，并首次构造了伊托积分作为鞅值过程，推进了验证性随机分析和形式化方法。 该工作基于 Mathlib 和 BrownianMotion 包在 Lean 4 中完成，约 7,200 行代码分布在 22 个无 sorry 的模块中，通过可预测矩形 π‑系统和简单适应过程的密度构造积分，并利用离散到连续的论证给出带有显式 L^2 余项界的伊托公式。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: Lean 4 是一种函数式编程语言和证明助手，其社区维护的库 Mathlib 致力于形式化研究水平的数学。布朗运动（维纳过程）是随机微积分中的核心连续时间随机过程，其伊托积分被定义为从简单可预测过程的希尔伯特空间到 L^2 的等距映射。形式化这些概念需要将积分构造为鞅值过程并证明伊托公式，该公式将函数关于该过程的微分与其平方变化联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://reservoir.lean-lang.org/@RemyDegenne/BrownianMotion">BrownianMotion | Reservoir</a></li>
<li><a href="https://getacademy.blog/ito-isometry-theorem-guide">Ito Isometry Theorem: The Ultimate Guide... - GetAcademy.blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hilbert_space">Hilbert space - Wikipedia</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#stochastic calculus`, `#Lean 4`, `#Ito integral`, `#Mathlib`

---

<a id="item-9"></a>
## [信念面临风险：使用 LLM 推断的贝叶斯状态过滤器量化代理 AI 模型风险](https://arxiv.org/abs/2606.15473) ⭐️ 8.0/10

本文提出了一种贝叶斯过滤框架，将大型语言模型视为部分可观测马尔可夫决策过程中的不确定语义观测模型，以量化代理 AI 系统的不确定性和风险。 通过为受监管环境中的代理 AI 验证提供严格的数学基础，该工作连接了 AI 安全、模型风险管理和定量风险测量，可能影响金融和高风险 AI 的部署。 该框架将不确定性量化（后验熵、信念漂移、校准误差）与风险度量（信念下的损失分离）分开，利用 LLM 将证据映射到潜在 regimes 的概率向量，并以 Massive.com 的调整后日股票回报为例，展示了如何得到 regime 概率和类 VaR/CVaR 的风险度量。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 部分可观测马尔可夫决策过程（POMDP）建模的是决策过程，其中底层状态是隐藏的，必须通过观测来推断。贝叶斯过滤通过传感器模型和时间动态递归地更新对隐藏状态的信念，从而得到一致的后验分布。在此工作中，大型语言模型被用作不确定的观测模型，将高维证据转换为对潜在 regimes 的概率分布，而过滤器则施加时间一致性。该框架还联系了尾部风险函数如 VaR 和 CVaR，它们量化超过某个概率阈值的预期损失，以及基于推断信念自主行动的代理 AI 概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process">Partially observable Markov decision process - Wikipedia</a></li>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tail_value_at_risk">Tail value at risk - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#agentic AI`, `#Bayesian filtering`, `#LLM`, `#risk quantification`

---

<a id="item-10"></a>
## [基于预训练神经网络的快速可验证误差有界期权定价方法（适用于 GJR-GARCH）](https://arxiv.org/abs/2606.15502) ⭐️ 8.0/10

该论文提出了一种混合密度网络（MDN） surrogate，将模型参数和期权到期映射为高斯混合的终端收益率密度，从而得到封闭形式的无套利期权价格、隐含波动率和希腊字母，并提供可验证的误差界。 该方法既提供微秒级的定价速度，又给出严格的误差保证，使得像 GJR‑GARCH 这样的模拟密集型模型能够用于实时风险管理和交易，从而在机器学习与量化金融之间架起桥梁。 该 surrogate 采用与定价误差对齐的 CDF‑matching 损失，其精度受分布无关的蒙特卡洛噪声底限 √(1/(6N)) 限制；在 GJR‑GARCH 上，外部样本 CDF 误差达到 1.4×10⁻⁴，接近噪声底限的 10%，定价每个期权在 CPU 上只需几微秒，在 GPU 上甚至低于一微秒。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 许多金融模型（如 GJR‑GARCH）没有封闭形式的期权定价公式，因而只能依赖缓慢且带噪声的蒙特卡洛模拟进行定价。虽然神经 surrogate 能提升速度，但过去缺乏误差保证。GJR‑GARCH 模型在标准 GARCH 基础上加入指示项，以捕捉杠杆效应——负收益会比同幅度的正收益更显著地提升波动率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity">Autoregressive conditional heteroskedasticity - Wikipedia</a></li>
<li><a href="https://vlab.stern.nyu.edu/docs/volatility/GJR-GARCH">V-Lab: GJR-GARCH Volatility Documentation</a></li>
<li><a href="https://arxiv.org/html/2606.15502">Fast, Reliable, and Error-Bounded Option Pricing with Pretrained...</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#option pricing`, `#neural networks`, `#GJR-GARCH`, `#surrogate modeling`

---

<a id="item-11"></a>
## [Hyperliquid 上可见的 TWAP 订单相比隐藏 metaorder 降低执行成本](https://arxiv.org/abs/2606.15715) ⭐️ 8.0/10

该研究分析了 Hyperliquid 上的 430 万个隐藏 metaorder 和 46.5 万个可见 TWAP 执行，发现可见 TWAP 的执行成本和永久价格冲击均低于可比的隐藏 metaorder。 它提供了实证证据，表明在链上预先宣布交易可以减少逆向选择，为算法交易者和考虑使用透明订单类型的 DeFi 平台提供指导。 隐藏 metaorder 遵循与瞬态冲击最优执行一致的前加载 U 形调度，而 TWAP 几乎均匀交易；可见 TWAP 增加了显示深度并使订单簿向吸收方向倾斜。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 阳光交易理论（Admati & Pfleiderer，1991）预测，公开披露交易意图可以减少逆向选择并吸引流动性，从而降低执行成本。Hyperliquid 运行一个完全在链上的限价订单簿，用于加密货币永续期货，其中其原生 TWAP 订单从一开始就是可见的并保持活跃，为阳光交易提供了自然环境。瞬态冲击最优执行模型描述了如何切分大订单以最小化暂时市场冲击，通常会导致前加载的 U 形交易模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bankofcanada.ca/wp-content/uploads/2012/11/Session-3-Kumar-Venkataraman.pdf">Predatory or Sunshine Trading ? Evidence from Crude Oil ETF Rolls...</a></li>
<li><a href="https://medium.com/@gwrx2005/hyperliquid-on-chain-order-book-6df27cbce416">Hyperliquid On - Chain Order Book . Hyperliquid ... | Medium</a></li>
<li><a href="https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/cfm-imperial-institute-of-quantitative-finance/events/Lillo-Imperial-Lecture1.pdf">Market impact models and optimal execution algorithms</a></li>

</ul>
</details>

**标签**: `#market microstructure`, `#cryptocurrency`, `#algorithmic trading`, `#sunshine trading`, `#Hyperliquid`

---

<a id="item-12"></a>
## [链式任务，重塑工作：AI 自动化理论](https://arxiv.org/abs/2606.15960) ⭐️ 8.0/10

作者提出一种理论模型，其中生产步骤被组织为手动、AI 增强或完全自动化的连续链，展示了企业如何最优地分配人类和 AI 到各步骤，并从 AI 质量提升中获得非线性生产率收益。 该框架揭示了 AI 如何超越简单任务自动化重塑工作设计，强调当 AI 步骤形成链时，比较优势 reasoning 可能失效。这对生产率预测、劳动力规划以及应对 AI 驱动的劳动力市场变化的政策具有重要意义。 该模型在宏观层面可表现为常数弹性替代（CES）形式，并预测 AI 执行的步骤倾向于出现在连续链中，AI 暴露步骤的分散程度越高，工作层面的 AI 使用越低，而一个步骤成为 AI 执行的概率与其相邻的 AI 执行步骤数量正相关。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 在生产理论中，任务通常被视为可以由劳动力、资本或两者组合完成的一系列步骤。传统的比较优势理论建议将每个步骤分配给能够更高效完成它的要素（人或 AI），前提是步骤之间是独立的。然而，当 AI 能够执行多个连续步骤时，协调成本降低，产生协同效应，导致最优分配偏离简单的比较优势。该文通过建模连续的 AI 执行链来正式化这一思想，并表明这种链式结构可以产生非线性的生产率提升，可通过 CES 总生产函数来捕捉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.libertify.com/interactive-library/nber-ai-task-chaining-job-automation-theory/">AI Task Chaining and Job Automation: NBER Theory of How AI ...</a></li>
<li><a href="https://www.linkedin.com/posts/jaiganesh_how-ai-is-reshaping-workflows-and-redefining-activity-7453707992266391552-mQoc">AI Task Chaining Transforms Workflows and Job Design | LinkedIn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Macroeconomic_model">Macroeconomic model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI automation`, `#labor economics`, `#task chaining`, `#productivity theory`, `#human-AI collaboration`

---

<a id="item-13"></a>
## [概率方法识别脱碳能源系统中的技术临界点](https://arxiv.org/abs/2606.16469) ⭐️ 8.0/10

该研究将部门联合国家优化模型与蒙特卡洛抽样（10,000 次）相结合，应用于德国和英国，以量化不确定性并确定风能、太阳能、碳捕获与储存以及负排放技术具有竞争力的成本阈值。 通过提供技术路径的概率分布，该研究有助于政策制定者制定能够考虑技术成本和性能不确定性的稳健净零战略，并凸显跨国差异的重要性。 临界点成本阈值：如果英国 2035 年的核能成本低于 4700 欧元/千瓦，则投资核能；否则偏好海上风电。德国的可调度低碳选项取决于气体 CCS（低于 2100 欧元/千瓦）、生物质 CCS（低于 4200 欧元/千瓦）或氢气电解（低于 560 欧元/千瓦）。风能与太阳能的未来角色仍然高度不确定。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 部门联合国家优化模型将能源供需及跨部门政策整合起来，以求得最低成本路径。蒙特卡洛模拟通过数千次模型运行传播技术成本、燃料价格、需求和天气的不确定性，从而生成概率分布。技术临界点是指技术竞争力发生显著转变的成本或性能水平，这会影响脱碳电力系统中的投资决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/385131637_A_regional_energy_system_transition_modeling_tool_for_decision_support_-_A_case_study_of_the_Groningen_province_in_the_Northern_Netherlands">(PDF) A regional energy system transition modeling tool for decision...</a></li>
<li><a href="https://www.weforum.org/stories/2015/09/have-we-reached-a-tipping-point-for-technology/">Have we reached a tipping point for technology ? | World Economic...</a></li>
<li><a href="https://www.researchgate.net/publication/386749180_Negative_emissions_technologies_in_energy_system_models_and_mitigation_scenarios_-a_systematic_review">(PDF) Negative emissions technologies in energy system models...</a></li>

</ul>
</details>

**标签**: `#energy systems`, `#decarbonization`, `#Monte Carlo simulation`, `#technology tipping points`, `#power systems`

---

<a id="item-14"></a>
## [PHINN：受持久同调启发的神经网络用于罕见事件时间序列生成](https://arxiv.org/abs/2606.15452) ⭐️ 8.0/10

我们提出了 PHINN，一种基于流匹配的框架，利用动态 Betti 曲线作为条件并优化持久景观损失来生成具有高拓扑保真度的罕见事件时间序列。该方法还提供自然语言界面来设定 Betti 目标，支持跨域元学习、少样本生成，并提供认证的对抗鲁棒性。 PHINN 解决了数据稀缺导致的罕见事件建模难题，在拓扑保真度上优于统计和扩散基线，beta‑RMSE 降低 41‑63%，转换准确率提升最高达 84%。其认证鲁棒性和跨域适用性使其在金融、流行病学等需要可靠极端事件模拟的领域具有重要价值。 在金融、流行病学和多模态基准上，PHINN 在尾部覆盖方面与跳扩散模型相当，而在形状保真度上更优，所有结果均附带 95%置信区间。该框架支持多变量数据，接受自然语言的 Betti 目标，能够进行少样本和跨域元学习，并提供可证的对抗鲁棒性保证。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 持久同调在不同尺度上度量数据的形状特征，用贝蒂数（Betti numbers）来计数连通分量、环和空洞等拓扑特征。贝蒂曲线随过滤参数绘制这些数值，提供了一种在罕见事件期间会显著变化的稳定特征。持久景观将持久图转换为可用于损失驱动学习的函数形式，而流匹配则通过学习速度场将噪声转换为数据，提供了一种无需模拟的生成范式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://giotto-ai.github.io/gtda-docs/latest/modules/generated/diagrams/representations/gtda.diagrams.BettiCurve.html">BettiCurve — giotto-tda 0.5.1 documentation</a></li>
<li><a href="https://jmlr.org/papers/volume16/bubenik15a/bubenik15a.pdf">Statistical Topological Data Analysis using Persistence</a></li>
<li><a href="https://arxiv.org/abs/2210.02747">[2210.02747] Flow Matching for Generative Modeling</a></li>

</ul>
</details>

**标签**: `#time-series generation`, `#persistent homology`, `#rare events`, `#flow matching`, `#topological data analysis`

---

<a id="item-15"></a>
## [面向自主 AI 代理的博弈抗性保险合同及策略证明收费机制](https://arxiv.org/abs/2606.16326) ⭐️ 8.0/10

该论文定义了自主 AI 代理保险合同的五种攻击空间，并提出了共同控制聚合、接口故障处理和模型身份菜单等新合同条款，使精算运时对博弈具有策略证明性。它还展示了这些条款如何与先前的运行时组合以实现联合激励兼容性，以及如何通过两参数保费族满足个体理性和弱预算平衡。 通过提供正式的博弈抗性保险框架，该工作推进了 AI 安全和机制设计，使得在需要将副作用财务内部化的环境中可靠部署自主代理成为可能。该方法可能影响 AI 系统的监管标准和保险产品。 五种攻击空间包括事后安全默认选择、边界内动作拆分、跨边界重新路由、接口故障和模型身份误报；相应条款封闭前两种攻击并引入共同控制聚合、接口合规惩罚以及用于真实报告的分量级最小惩罚表。两参数保费族在真实均衡下确保个体理性和弱预算平衡。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 该论文建立在先前的精算运行时之上，该运行时为自主代理的每个副作用-bearing 动作分配基于合同安全默认的时间一致的反事实风险费用，并通过准备金预算控制执行。先前的运行时将运营商视为被动；此工作通过刻画攻击表面和设计合同条款以防止博弈，将其扩展到战略运营商。共同控制聚合的概念来源于机制设计文献，其中协调控制可以防止跨边界利益转移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.26508">Foundations of a Time -Consistent Counterfactual Actuarial Runtime ...</a></li>
<li><a href="https://arxiv.org/abs/2606.16326">[2606.16326] Gaming-Resistant Insurance Contracts for Autonomous...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#mechanism design`, `#autonomous agents`, `#insurance contracts`, `#game theory`

---

<a id="item-16"></a>
## [微笑的个人资料提升效率并减少差距。](https://arxiv.org/abs/2209.01235) ⭐️ 8.0/10

研究人员结合因果推断和计算机视觉方法表明，鼓励与微笑相关的个人资料修改可以提升交易效率，同时减少点对点借贷平台的人口统计学差距。 该研究为在线平台提供了一种通过调整易于改变的个人资料特征来平衡效率与公平的实际方法，为构建更具包容性的市场提供政策依据。 该方法将不可变的“类型”特征（如性别、年龄）与可变的“风格”特征（如微笑）区分开来，利用因果推断处理观测数据并结合基于生成模型的调查实验来估计影响，并发现风格差异常常加剧类型差异。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 在线点对点借贷平台依赖个人资料图片来传递可信度，但人口统计特征可能导致贷款决策偏差。因果推断方法能够从非实验数据中估计因果关系，而计算机视觉算法可自动检测面部属性如微笑。研究市场效率与差距减少之间的权衡是平台公平研究的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marvik.ai/blog/introduction-to-causal-inference-understanding-cause-and-effect-relationships">Introduction to Causal Inference : Understanding Cause and... — Marvik</a></li>
<li><a href="https://reubensinha7.medium.com/smile-detection-a-hello-world-for-computer-vision-1b70dc65b9dc">Smile Detection — A “Hello World” for Computer Vision | Medium</a></li>
<li><a href="https://facerate.ai/">FaceRate.ai: Face Attractiveness Test & Detailed Face Analysis Tool</a></li>

</ul>
</details>

**标签**: `#online marketplaces`, `#fairness`, `#causal inference`, `#computer vision`, `#peer-to-peer lending`

---

<a id="item-17"></a>
## [最优报价框架应对逆向选择和价格泄露](https://arxiv.org/abs/2508.20225) ⭐️ 8.0/10

arXiv:2508.20225v5 的作者提出了一种可计算的最优报价框架，该框架同时考虑了来自知情交易者的逆向选择以及市场制造者自身报价导致的价格泄露风险。 该框架连接了从业者关注与学术模型之间的差距，为算法交易和量化金融提供了可操作的见解，解决了市场制造中长期存在的两大风险。 该模型在 Ho 和 Stoll（1981）以及 Avellaneda‑Stoikov（2008）的基础上进行扩展，使市场制造者能够在考虑知情流动以及自身报价无意泄露库存的情况下调整买卖价差。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 做市商通过持续报出买入和卖出价格来提供流动性，这一实践在早期模型如 Ho 和 Stoll（1981）中得到形式化，该模型从经销商的期望效用最大化中推导出最优点差。后来，Avellaneda 和 Stoikov（2008）将此框架扩展到高频环境，采用指数效用和泊松交易到达，重点关注库存风险。实际上，做市商还面临来自知情交易者的逆向选择风险，以及自身报价可能无意泄露库存方向的价格读取风险。尽管这些风险在从业者中众所周知，但在定量金融文献中除了风格化的玩具模型外，它们得到的关注有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.09454">Axiomatic Market Making</a></li>
<li><a href="https://uditsamani.com/avellaneda-stoikov/">Optimal Market Making ( Avellaneda - Stoikov ) | Udit Samani</a></li>
<li><a href="https://en.wikipedia.org/wiki/Price_action_trading">Price action trading - Wikipedia</a></li>

</ul>
</details>

**标签**: `#market making`, `#adverse selection`, `#algorithmic trading`, `#quantitative finance`, `#price reading`

---

<a id="item-18"></a>
## [本文提出了一种混合保持、无套利的波动曲面插值方法。](https://arxiv.org/abs/2606.12717) ⭐️ 8.0/10

该论文提出了一种基于固定 2N 分量混合框架的波动曲面插值方法，通过冻结两个到期支柱的分量而仅调整其权重来实现混合保持和无套利。 该插值保证了非负的 Dupire 局部波动率，从而得到唯一的连续局部波动扩散，为跨期限的衍生品定价和对冲提供了理论上严格且实用的工具。 该构造在固定的 2N 分量族中保持两个支柱混合的组成不变，仅转移它们的权重，以满足孔雀（凸序）性质，从而确保局部波动率非负。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 波动曲线图展示了隐含波动率随行权价格和到期时间的变化，无套利插值确保了不同到期日的风险中性密度按照凸序排列，这相当于杜皮尔局部波动率非负。混合模型将风险中性密度表示为高斯或对数正态等核函数的加权和；在插值过程中保持混合结构可以保持模型的可处理性。Brigo–Mercurio 混合期限结构模型采用这种混合形式来描述远期利率，而 SANOS 模型则提供了完全自由的每击宽度表示；新方法在这两者之间搭建了桥梁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12717v2">Mixture-Preserving, Arbitrage- Free Interpolation for Volatility - Surface ...</a></li>
<li><a href="https://quant.stackexchange.com/questions/83652/arbitrage-free-interpolation/83662">volatility - Arbitrage - free interpolation - Quantitative Finance Stack...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Damiano_Brigo">Damiano Brigo - Wikipedia</a></li>

</ul>
</details>

**标签**: `#volatility surface`, `#arbitrage-free interpolation`, `#mixture models`, `#quantitative finance`, `#local volatility`

---

<a id="item-19"></a>
## [Shachi：基于 LLM 的模块化代理建模框架用于研究涌现集体行为](https://arxiv.org/abs/2509.21862) ⭐️ 8.0/10

论文提出了 Shachi，一个将 LLM 代理认知分解为配置、记忆和工具三个组件的模块化框架，从而实现对涌现集体行为的受控扰动研究。 Shachi 填补了研究微层认知特征如何影响宏观动态的 principled 仿真工具的空白，为人工生命和多智能体 LLM 研究提供了严谨的开源平台。 该框架将内在身份（Configuration）、情境连续性（Memory）和扩展能力（Tools）三个认知组件隔离，由 LLM 推理引擎协调，并在 10 任务基准及美国关税冲击案例中验证了跨环境记忆迁移和跨环境干扰。

rss · arXiv Quantitative Finance · Jun 16, 04:00

**背景**: 基于代理的建模（ABM）通过模拟相互作用的自主智能体来研究由局部交互产生的涌现集体行为。当这些代理由大型语言模型（LLM）驱动时，其认知过程既丰富又不透明，难以系统地改变个体特征并观察群体层面的模式。Shachi 提供了一种原则性的、模块化的 LLM 代理认知分解方法，将其划分为可控制的组件，使研究者能够进行扰动实验，追踪记忆、身份或工具使用的变化如何影响宏观动态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2509.21862">Reimagining Agent - based Modeling with Large Language Model ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_life">Artificial life - Wikipedia</a></li>
<li><a href="https://www.ruh.ai/blogs/agentic-reasoning-fixing-llm-limitations">How Agentic Reasoning Is Fixing the Fundamental... - Ruh AI Blog</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#agent-based modeling`, `#emergent behavior`, `#artificial life`, `#framework`

---