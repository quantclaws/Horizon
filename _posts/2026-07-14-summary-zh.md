---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> From 34 items, 10 important content pieces were selected

---

1. [无需打开 Xcode 构建并发布 Mac 和 iOS 应用。](#item-1) ⭐️ 8.0/10
2. [Linux 在 Sega 32X 上通过软件同步移植](#item-2) ⭐️ 8.0/10
3. [Telegram 的 t.me 域名因法律争议被暂停](#item-3) ⭐️ 8.0/10
4. [Samsung Health 威胁删除用户健康数据 若不同意 AI 训练](#item-4) ⭐️ 8.0/10
5. [DOOMQL：终端版类 Doom 游戏，全部由 SQL 驱动](#item-5) ⭐️ 8.0/10
6. [生成式 AI 助学，解释概念更持久。](#item-6) ⭐️ 8.0/10
7. [研究发现 2025 年 11%的标普 500 公司深度融合 AI。](#item-7) ⭐️ 8.0/10
8. [季度小时周期性算法交易预测加密货币期货收益](#item-8) ⭐️ 8.0/10
9. [Voting Biases in Decentralized Autonomous Organization (DAO) Governance](#item-9) ⭐️ 8.0/10
10. [谱组合理论：从 SGD 权重矩阵到财富动态](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [无需打开 Xcode 构建并发布 Mac 和 iOS 应用。](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 8.0/10

文章展示了如何使用命令行工具（如 xcodebuild、fastlane 和 App Store Connect API）在终端中完成 macOS 和 iOS 应用的编译、签名、公证和分发，完全不需要打开 Xcode 图形界面。它还提到了社区分享的替代方案，如 xtool 和 Axiom 项目，用于 Linux 构建和 LLM 友好的实用程序。 这种方法使开发者能够将 Apple 平台的构建融入 CI/CD 流程，实现自动化发布，并在非 macOS 环境（如 Linux）上工作，同时减少对 Xcode 重量级 IDE 的依赖。它还强调了在个人机器上运行构建代理与沙箱环境相比的安全权衡。 该指南依赖 xcodebuild 进行构建，fastlane 自动化代码签名、配置文件和上传，以及 App Store Connect API 进行公证和分发；它指出在 Mac 上运行构建代理会绕过沙箱保护，可能暴露 SSH 密钥等敏感数据。

hackernews · speckx · Jul 13, 18:22 · [社区讨论](https://news.ycombinator.com/item?id=48896665)

**背景**: Xcode 提供图形化 IDE 和命令行工具 xcodebuild 用于构建 Apple 平台项目。Fastlane 是一个开源自动化工具，处理诸如代码签名、生成截图以及上传到 TestFlight 或 App Store 等重复任务。App Store Connect API 允许以编程方式上传、公证和管理应用，无需 Xcode，从而实现完全脚本化的构建和发布流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/library/archive/technotes/tn2339/_index.html">Technical Note TN2339: Building from the Command Line with Xcode FAQ</a></li>
<li><a href="https://fastlane.tools/">fastlane - App automation done right</a></li>
<li><a href="https://developer.apple.com/app-store-connect/">App Store Connect - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 评论者警告说，在个人 Mac 上运行构建代理会牺牲沙箱安全，曾有 AI 代理上传包含 SSH 密钥的主目录。其他人则强调了使用 xtool 等工具在 Linux 上成功构建 iOS 应用，并称赞了提供 LLM 友好实用程序的开源项目 Axiom。

**标签**: `#iOS`, `#macOS`, `#development`, `#Xcode alternatives`, `#CI/CD`

---

<a id="item-2"></a>
## [Linux 在 Sega 32X 上通过软件同步移植](https://cakehonolulu.github.io/linux-on-32x/) ⭐️ 8.0/10

一位开发者通过实现 Petersen 算法作为软件同步原语，在 Sega 32X 附加板上成功运行了支持 SMP 的 Linux，无需硬件同步原语即可实现对称多处理。 这一成就表明，操作系统移植的创意可以克服严重的硬件限制，激发了复古计算爱好者的兴趣，并表明即使在受限平台上也可以通过巧妙的软件方案实现对称多处 该移植采用 Petersen 算法在两个 Hitachi SH‑2 处理器之间实现互斥，运行在 32X 的 23 MHz SH‑2 核心上，内存有限，主要在模拟器中测试，随后进行硬件验证。

hackernews · cakehonolulu · Jul 13, 18:18 · [社区讨论](https://news.ycombinator.com/item?id=48896600)

**背景**: Sega 32X 是 Sega Genesis 的一个附加板，内含两个运行约 23 MHz 的 Hitachi SH‑2（SH7095）32 位 RISC 处理器，各自拥有有限的本地内存，且缺乏用于多处理的硬件同步原语。对称多处理（SMP）使得操作系统能够在多个相同内核上调度线程，但需要诸如锁或信号量之类的机制来防止竞争条件。在没有硬件锁的情况下， Petersen 算法等软件算法可以仅通过共享内存的读写来实现互斥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/32X">32X - Wikipedia</a></li>
<li><a href="https://consolemods.org/wiki/images/e/e9/32X_Hardware_Manual_1994_Sega_text.pdf">32X Hardware Manual (1994)(Sega) - consolemods.org</a></li>
<li><a href="https://linux-kernel-labs.github.io/refs/heads/master/lectures/smp.html">Symmetric Multi-Processing — The Linux Kernel documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 SH‑2 无法写入卡带 RAM，质疑该移植是否在真实硬件上测试还是仅在模拟器中进行，而其他人则强调 SH‑2 与 ARM Thumb 指令集的相似性，并对使用串口进行终端访问表达了兴趣。几位参与者表示欣赏了解 Petersen 算法，并引用了 Lamport 的快速互斥作为相关替代方案。

**标签**: `#Linux`, `#Sega 32X`, `#operating systems`, `#retro computing`, `#synchronization algorithms`

---

<a id="item-3"></a>
## [Telegram 的 t.me 域名因法律争议被暂停](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram 的 t.me 域名被标记为 clientRenewProhibited 状态，导致域名被暂停，所有 t.me/短链接失效，但 Telegram 应用仍可正常使用。 此次暂停破坏了广泛使用的短链接邀请系统，影响全球数百万 Telegram 用户，凸显了该平台对单一注册商的依赖及其面临的法律审查。 WHOIS 记录显示域名状态为 clientRenewProhibited，该码通常在法律争议或待删除期间设置，且该域名注册于 GoDaddy；Telegram 尚未发布官方声明。

hackernews · Tiberium · Jul 13, 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48897878)

**背景**: clientRenewProhibited 状态码会阻止域名在未获得明确同意的情况下续期，通常在法律争议或域名即将被删除时被设置。Telegram 的 t.me 域名用于全球的短链接，用于跳转到频道、群组或用户资料，因此其暂停会导致这些链接失效，而核心应用仍能正常运行。依赖单一注册商（如 GoDaddy）会产生单点故障风险，特别是当注册商面临法律或合规行动时可能影响域名管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openprovider.com/glossary/clientRenewProhibited">What is clientRenewProhibited? - Openprovider</a></li>
<li><a href="https://glitchwire.com/news/telegrams-tme-domain-disappears-from-global-dns-with-no-explanation-pavel-durov/">Telegram's t.me Domain Disappears From Global DNS With No Explanation ...</a></li>
<li><a href="https://dn.org/registrar-level-security-and-the-role-of-domain-registrars-in-managing-risk/">Registrar-Level Security and the Role of Domain Registrars in ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Telegram 依赖 GoDaddy 表示担忧，并提到俄罗斯、法国和印度的法律调查，一些人表示他们已经将社区迁移到如 Zulip 等平台。其他人则强调保持重定向策略的重要性，以减轻此类域名中断的影响。

**标签**: `#Telegram`, `#domain suspension`, `#legal issues`, `#GoDaddy`, `#community discussion`

---

<a id="item-4"></a>
## [Samsung Health 威胁删除用户健康数据 若不同意 AI 训练](https://neow.in/cWsyMTV3) ⭐️ 8.0/10

Samsung Health 更新了其设置，要求用户同意 AI 训练；选择退出会弹出警告，称所有现有健康数据将被删除且以后将无法同步。 该政策迫使用户为了 AI 模型训练而交出敏感健康数据，否则将失去访问自身记录的权利，凸显了消费者健康科技中日益增长的隐私紧张。 AI 训练开关涵盖睡眠、药物、医疗记录和月经周期追踪数据；关闭后将停止云同步并触发永久删除，且未提及内置导出选项。

hackernews · bundie · Jul 13, 20:01 · [社区讨论](https://news.ycombinator.com/item?id=48897991)

**背景**: Samsung Health 是三星旗舰的健康与健身平台，汇集来自 Galaxy 可穿戴设备和智能手机的数据，使用户能够追踪活动、睡眠、营养等。该应用会将这些信息同步到三星账户以实现备份和跨设备访问。最近的更新引入了一项可选的 AI 训练功能，利用聚合健康数据来改进个性化洞察，但新政策使得持续数据同步必须参与该功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5google.com/2026/07/13/samsung-health-ai-training-data-consent/">Samsung Health will delete your data without AI training consent</a></li>
<li><a href="https://www.androidauthority.com/samsung-health-train-ai-data-3686684/">Samsung will kill your health data if you don't consent to AI training - Android Authority</a></li>
<li><a href="https://m.gsmarena.com/samsung_health_data_ai_training_consent-news-73683.php">Samsung Health users asked to allow use of their health data for AI training or it will be deleted - GSMArena.com news</a></li>

</ul>
</details>

**社区讨论**: 评论者批评这一最后通牒，指出拒绝 AI 训练将使手表的一半功能无法使用，并质疑三星是否应退还设备费用。一些人讽刺地欢迎删除敏感健康数据的前景，而另一些人则指出缺少数据导出工具，使得威胁感觉像是个人记录的丧失。

**标签**: `#privacy`, `#health data`, `#AI training`, `#Samsung Health`, `#user consent`

---

<a id="item-5"></a>
## [DOOMQL：终端版类 Doom 游戏，全部由 SQL 驱动](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 8.0/10

彼得·戈斯特夫创建了 DOOMQL，这是一个基于终端的类 Doom 游戏，其中所有游戏逻辑——移动、碰撞、敌人、战斗和渲染——都通过 SQL 查询在 SQLite 中实现，并在 GPT‑5.6 Sol 的协助下构建。 DOOMQL 表明轻量级关系数据库可以充当完整的游戏引擎，凸显了 SQL 在实时图形和交互式模拟中的表达能力。 该游戏使用 SQLite 的递归 CTE 进行光线追踪，将状态存储在/tmp/doomql/.doomql/doomql.sqlite 文件中，并可通过 Datasette 及其 Datasette Apps 插件实时检查；它通过 uv 运行的 Python 脚本启动。

rss · Simon Willison · Jul 13, 22:34

**背景**: SQLite 是一种嵌入式、零配置的 SQL 数据库，常用于应用程序的本地存储，通常不用于实时游戏逻辑。递归公共表表达式（CTE）使 SQLite 能够执行迭代计算，从而可以完全在 SQL 中实现诸如光线追踪之类的技术。Datasette 是一个用于探索和发布 SQLite 数据库的工具，其 Apps 插件允许用户运行可以直接查询数据库的自定义 HTML/JavaScript 界面；uv 是一种基于 Rust 的快速 Python 包管理器，简化了依赖项的安装和脚本的运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.openmw.org/viewtopic.php?t=7193">SQLite based approach to storing game world state - openmw.org</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT - 5 . 6 Sol : a next-generation model | OpenAI</a></li>
<li><a href="https://docs.astral.sh/uv/guides/install-python/">Installing and managing Python | uv - Astral Docs</a></li>

</ul>
</details>

**标签**: `#SQL`, `#game development`, `#Python`, `#novelty`, `#terminal`

---

<a id="item-6"></a>
## [生成式 AI 助学，解释概念更持久。](https://arxiv.org/abs/2607.08849) ⭐️ 8.0/10

一项随机对照研究发现，让本科生使用现成的生成式 AI 可使即时考试成绩提高 0.27 个标准差，且这一提升在一周后仍然存在。虽然在使用 AI 时作文质量没有变化，但一周后学生在无 AI 的情况下作文的风格和相关性有所提升，尤其是那些用 AI 来解释概念而非生成文本的学生。 该研究提供了高质量的实验证据，区分了 AI 作为学习辅助（增强）和作为捷径（自动化）的使用方式，表明只有增强方式才能带来持久的学习提升。这有助于教育者和教育技术设计者将注意力集中在促进深层理解而非仅仅生成答案的 AI 应用上。 主要发现包括即时知识测试成绩提升 0.27 个标准差且在一周后仍然存在，延迟的作文质量提升在使用 AI 解释概念的增强型用户中更为显著。研究者认为这些收益来源于学生将时间从起草文本转向阅读和信息搜索，并报告了更高的学习享受度。

rss · arXiv Quantitative Finance · Jul 13, 04:00

**背景**: 生成式 AI 是指如 GPT‑4 之类的模型，能够根据提示生成文本、图像或其他内容。在教育领域，AI 既可以用于自动化任务（例如生成答案），也可以用于增强学习（例如解释概念）。随机对照试验是评估教育干预因果效应的金标准。了解 AI 是起到辅助作用还是充当导师，有助于指导其在课堂中的整合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.08849">Experimental Evidence on the Learning Impact of Generative AI</a></li>
<li><a href="https://www.forbesindia.com/article/rotman/understanding-ais-effect-on-jobs-automation-versus-augmentation/95827/1">Understanding AI ’s effect on jobs: Automation versus augmentation</a></li>

</ul>
</details>

**标签**: `#AI in Education`, `#Generative AI`, `#Learning Experiment`, `#Augmentation vs Automation`, `#Student Assessment`

---

<a id="item-7"></a>
## [研究发现 2025 年 11%的标普 500 公司深度融合 AI。](https://arxiv.org/abs/2607.08920) ⭐️ 8.0/10

该研究通过 SEC 10-K 文件估算标普 500 公司的深度 AI 采用，发现到 2025 年有 11%的公司将 AI 深度融入业务流程。采用率从 2022 年的 5%增长了四倍多，其中技术公司贡献了深度融合的三分之二。 通过将 AI 采用与受监管的 SEC 披露挂钩，该研究提供了一种可靠的指标来区分真实融合与炒作。这些见解有助于政策制定者、投资者和经理评估企业层面 AI 对生产率和劳动力市场的影响。 该指标将 AI 嵌入核心业务流程的公司视为深度融合，区别于表面的 AI 使用。在技术公司中，更深的采用与员工人数增加和 Tobin’s q 升高相关；总体企业呈现利润的 J 曲线，但资本支出和可测生产率没有显著变化。

rss · arXiv Quantitative Finance · Jul 13, 04:00

**背景**: 大型企业的人工智能采用被视为推动总体生产率和劳动力市场变化的潜在动力。标普 500 指数包含美国 500 家最大的上市公司，是企业趋势的风向标。SEC 10-K 文件是法律要求的年度报告，公司必须避免重大虚假或误导性陈述，因此它们是评估真实 AI 部署的可信来源。该研究关注深度融合——AI 编织进业务运营——而非外围或实验性使用。

**标签**: `#AI adoption`, `#enterprise AI`, `#SEC filings`, `#productivity`, `#labor market`

---

<a id="item-8"></a>
## [季度小时周期性算法交易预测加密货币期货收益](https://arxiv.org/abs/2607.09426) ⭐️ 8.0/10

该研究发现加密货币期货中存在与算法交易相关的季度小时周期性爆发，以交易规模整数度下降为特征，并表明这些开盘时的订单失衡能够通过自相关图预测四到十二小时的收益。 它提供了周期性算法交易的新颖实证证据以及收益预测的实用工具，揭示了加密货币市场微观结构，可为交易者、研究者和监管者提供参考。 作者使用六个 Binance 永续合约发现，在季度小时爆发期间交易规模整数度急剧下降，自相关图显示这些开盘时的订单流和收益存在序列依赖，且在更细的时间尺度上预测能力减弱。

rss · arXiv Quantitative Finance · Jul 13, 04:00

**背景**: 加密货币期货是价值与数字资产挂钩的衍生品，常在币安等交易所交易。算法交易是指使用计算机程序根据预设规则执行订单，通常会留下诸如交易规模整数化等特征。加密货币市场中出现的定期交易活动爆发（如在固定时间间隔出现的激增）被认为与算法策略或资金费率等市场机制有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09426">[2607.09426] The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures</a></li>
<li><a href="https://quantpedia.com/periodicity-in-cryptocurrencies-recurrent-patterns-in-volatility-and-volume/">Periodicity in Cryptocurrencies – Recurrent Patterns in Volatility and Volume - QuantPedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Algorithmic_trading">Algorithmic trading - Wikipedia</a></li>

</ul>
</details>

**标签**: `#algorithmic trading`, `#cryptocurrency futures`, `#market microstructure`, `#return predictability`, `#autocorrelation map`

---

<a id="item-9"></a>
## [Voting Biases in Decentralized Autonomous Organization (DAO) Governance](https://arxiv.org/abs/2607.09435) ⭐️ 8.0/10

The study finds that author-selected DAO proposals receive a 58.8% higher voting-power share, with additional advantages for approval-oriented and first-listed choices.

rss · arXiv Quantitative Finance · Jul 13, 04:00

**标签**: `#DAO`, `#governance`, `#voting bias`, `#token-weighted voting`, `#blockchain`

---

<a id="item-10"></a>
## [谱组合理论：从 SGD 权重矩阵到财富动态](https://arxiv.org/abs/2603.09006) ⭐️ 8.0/10

本文提出谱组合理论，将随机梯度下降训练的神经网络权重矩阵视为投资组合配置矩阵，并表明其谱结构编码了因子分解和财富集中模式。此外，它展示了 SGD 的三种力量——梯度信号、维度正则化和特征值排斥——如何分别对应聪明资金、生存约束和内生多样化，以及谱统计如何从 Marchenko-Pastur 演化到通过自由对数正态分布的逆威沙特。 通过共享的谱框架将机器学习与金融数学统一，该工作为投资组合设计、财富不平等测度、税收政策分析和神经网络诊断提供了新工具。这种跨学科的桥梁有望在 AI 驱动的金融和深度学习模型解释中激发实际应用和进一步研究。 SGD 的三种力量——梯度信号、维度正则化和特征值排斥——分别对应投资组合动态中的聪明资金、生存约束和内生多样化。核心的谱不变性定理表明，任何各向同性的扰动只会在尺度和位置上保持奇异值分布不变，而各向异性的扰动则会导致与扰动的跨资产方差成比例的谱失真。

rss · arXiv Quantitative Finance · Jul 13, 04:00

**背景**: 随机梯度下降（SGD）通过迭代更新权重矩阵来训练神经网络，这些矩阵在初始时表现出由 Marchenko‑Pastur 定律描述的随机矩阵统计特性。Marchenko‑Pastur 定律描述了大型矩形随机矩阵的特征值渐近分布，作为未训练权重谱的零模型。在长期乘法噪声的作用下，谱会通过自由对数正态 regime 演化为逆威沙特分布，这类似于从日常资产收益到长期财富复利的转变。Bouchaud‑Mézard 模型通过随机微分方程描述相互作用代理人的财富动态，捕捉财富集中和再分配过程，本文将这些过程与 SGD 权重矩阵的谱性质联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Marchenko–Pastur_distribution">Marchenko–Pastur distribution - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2507.12709">From SGD to Spectra: A Theory of Neural Network Weight Dynamics</a></li>
<li><a href="https://arxiv.org/pdf/2603.09006">Spectral Portfolio Theory: From SGD Weight Matrices to Wealth ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#finance`, `#stochastic gradient descent`, `#spectral analysis`, `#portfolio theory`

---