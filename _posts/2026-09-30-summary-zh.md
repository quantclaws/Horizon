---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> From 47 items, 11 important content pieces were selected

---

1. [OpenAI 发布 GPT-6.1 Sol，近 Astra 性能仅五分之一价格](#item-1) ⭐️ 8.0/10
2. [PS5 Relapse 漏洞利用通过 WebKit 漏洞实现越狱](#item-2) ⭐️ 8.0/10
3. [德里如何将电力损失从 50%降至 5%。](#item-3) ⭐️ 8.0/10
4. [Backblaze 2026 年第二季度硬盘可靠性统计显示故障率下降及寿命延长](#item-4) ⭐️ 8.0/10
5. [展示 HN：NSL – Linux 上的类 WSL 体验](#item-5) ⭐️ 8.0/10
6. [Vermont replacing power plants with home batteries](#item-6) ⭐️ 8.0/10
7. [Simon Willison 现场直播 OpenAI DevDay 2026 主题演讲，地点 Fort Mason](#item-7) ⭐️ 8.0/10
8. [Dyson-Schwinger 有效作用方法用于粗糙波动率期权定价。](#item-8) ⭐️ 8.0/10
9. [并非所有 LP 都相同：自动做市商流动性提供中的主动-被动差距](#item-9) ⭐️ 8.0/10
10. [提出用于金融对数收益预测的 CZAR 损失函数](#item-10) ⭐️ 8.0/10
11. [多期鞅最优运输框架及神经加速](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6.1 Sol，近 Astra 性能仅五分之一价格](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 8.0/10

OpenAI 在 2026 年 9 月发布了 GPT-6.1 Sol，这是一个多模态语言模型，上下文窗口为 110 万标记，输入标记每百万 2 美元，缓存输入每百万 0.10 美元，输出每百万 10 美元，性能接近旗舰 GPT-6 Astra，但价格仅约为其五分之一。 此次发布加剧了 AI 模型市场的价格竞争，使高性能模型对开发者和企业更具可负担性，同时迫使 Anthropic、DeepSeek 等竞争对手降低成本或提升价值。 GPT-6.1 Sol 在 GDP.pdf 基准测试中得分高于 Opus，其缓存输入价格比 GPT‑6 Sol 低 50 %，并在 GPT‑6 系列中定位于旗舰 GPT‑6 Astra 之下；其真实世界表现仍在评估中。

hackernews · crorella · Sep 29, 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**背景**: OpenAI 的 GPT 系列经历了多次迭代，GPT‑6 家族包括旗舰 Astra、Sol 和 Opus 等变体。性能常通过 GDP.pdf 基准测试衡量，该测试评估模型在复杂 PDF 文档上的专业级问答能力。随着上下文窗口扩大和 token 成本成为主要开支，定价竞争已成为关键区分因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT - 6 . 1 Sol | OpenAI</a></li>
<li><a href="https://llm-stats.com/models/gpt-6.1-sol">GPT - 6 . 1 Sol Benchmarks, Pricing & Context Window</a></li>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-astra">GPT-6 Astra Models - Intelligence, Performance & Price ...</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有人称赞其低成本并倾向于更便宜的替代方案如 DeepSeek；有人猜测 Sol 6.1 可能是 Astra‑Minor 的改名，因为之前的版本表现不佳；还有人批评早期 GPT‑6 模型不可靠，并强调 token 价格对行业投资者的战略意义。

**标签**: `#GPT-6.1`, `#AI language models`, `#pricing`, `#OpenAI`, `#Hacker News discussion`

---

<a id="item-2"></a>
## [PS5 Relapse 漏洞利用通过 WebKit 漏洞实现越狱](https://github.com/ntfargo/Relapse-Exploit) ⭐️ 8.0/10

Relapse 漏洞在 GitHub 上发布，利用 WebKit/JavaScriptCore 漏洞与内核竞态条件相结合，实现对 PS5 7.00‑13.60 固件的越狱，从而启用家庭自制软件和存档备份。 此越狱使用户能够备份游戏存档并运行家庭自制软件，挑战了索尼依赖付费云备份的模式，并凸显了基于浏览器的持续攻击面。 该漏洞完全通过 PS5 内置网页浏览器利用，无需硬件转储或等待时间，利用了 JavaScriptCore JIT 引擎中的使用后释放/未初始化内存漏洞，并结合内核竞态条件。

hackernews · therepanic · Sep 29, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49895304)

**背景**: 越狱使用户能够在主机上运行未签名的代码，绕过厂商限制。PS5 的系统软件内置了基于 WebKit 的浏览器用于访问在线服务，而其 JavaScriptCore 引擎中的漏洞可被利用以实现任意代码执行。7.00‑13.60 版固件仍然易受攻击，因为其中的 WebKit 组件在这些版本中未被修补，使得 Relapse 链能够将浏览器漏洞与内核竞态条件结合，获得持久访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ntfargo/Relapse-Exploit">GitHub - ntfargo/Relapse-Exploit: Exploit chain for PS5 7.00 ...</a></li>
<li><a href="https://elsolitario.org/en/2026/09/29/relapse-repo-claims-ps5-exploit-firmware-7-00-to-13-60/">PS5 Jailbreak: What Is Relapse Exploit and Its Scope</a></li>
<li><a href="https://www.cvedetails.com/vulnerability-list/vendor_id-8331/product_id-14494/Webkit-Javascriptcore.html">Webkit Javascriptcore : Security vulnerabilities, CVEs</a></li>

</ul>
</details>

**社区讨论**: 评论者对备份游戏存档和运行家庭自制软件表现出兴趣，有人质疑索尼是否会禁用 JavaScriptCore 的 JIT 以缓解此漏洞。还有人希望该漏洞能让 PS5 运行 Steam 游戏或等待 GTA 6 的发布，显示出社区既有实际需求也有更广泛的期待。

**标签**: `#PS5`, `#exploit`, `#jailbreak`, `#security`, `#gaming`

---

<a id="item-3"></a>
## [德里如何将电力损失从 50%降至 5%。](https://spectrum.ieee.org/delhi-electricity-loss) ⭐️ 8.0/10

文章报道，德里通过基础设施升级、反盗窃措施和智能计量的推广，将电力输配损失从 50%降低到 5%。 这一显著的损失降低为全球电力公司提供了重要案例，表明技术升级和政策执行可以削减浪费、缓解限电并提高快速增长能源市场的可靠性。 该推广包括部署带有射频树冠的高级计量基础设施（AMI）、对电力线路进行绝缘以防盗窃（这无意中为猴子提供了通道），以及解决技术和商业两方面的综合技术与商业损失（AT&C）。

hackernews · rbanffy · Sep 29, 12:43 · [社区讨论](https://news.ycombinator.com/item?id=49892245)

**背景**: 电力传输和配电损失通常以综合技术与商业损失（AT&C）来衡量，包括线路和变压器电阻造成的技术损失以及盗窃、计费错误和未付款造成的商业损失。许多印度城市的损失曾超过 40%，主要原因是基础设施老化和广泛的电力盗窃，导致频繁限电。智能计量和高级计量基础设施（AMI）实现实时监控、盗窃检测和准确计费，而诸如绝缘导线之类的防盗措施则减少非法接线。这些工具在德里的共同应用使损失降至个位数百分比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S037877962600756X">Smart-meter-based electricity theft detection and inspection ...</a></li>
<li><a href="https://www.fuelsandlubes.com/newswire/landisgyr-tata-power-ddl-partner-to-deploy-smart-metering-infrastructure-in-delhi/">Landis+Gyr & Tata Power-DDL Partner to Deploy Smart Metering ...</a></li>
<li><a href="https://jetir.org/papers/JETIRDJ06008.pdf">Study on aggregate technical</a></li>

</ul>
</details>

**社区讨论**: 评论者回忆了二十年前频繁的限电和电压浪涌，指出绝缘电力线无意中为猴子提供了在社区间穿行的便捷通道，并建议扩大太阳能、电池存储和垂直光伏以进一步减少对电网的依赖。还有人强调电力盗窃既由有权势的精英也由贫困居民实施，凸显了问题的社会维度。

**标签**: `#electricity`, `#infrastructure`, `#infrastructure`, `#smart grid`, `#India`, `#energy loss`

---

<a id="item-4"></a>
## [Backblaze 2026 年第二季度硬盘可靠性统计显示故障率下降及寿命延长](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/) ⭐️ 8.0/10

Backblaze 发布了 2026 年第二季度硬盘可靠性统计，报告称年度失效率降低且中位使用寿命延长。 这些数据为存储专业人士提供了最新的纵向洞察，以便规划驱动器更换周期和评估存储投资，反映了硬盘可靠性整体提升的行业趋势。 这些统计数据来源于 Backblaze 的 Drive Stats 数据集，该数据集跟踪 SMART 属性并计算年度失效率，但不包括在第一天就故障的驱动器。

hackernews · HieronymusBosch · Sep 29, 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49893002)

**背景**: 年度失效率（AFR）根据观测到的故障和运行时间估算硬盘一年内失效的概率。SMART 属性是硬盘内部监控指标，Backblaze 通过监控这些指标来帮助预测故障并计算可靠性统计。Backblaze 发布季度 Drive Stats 报告，汇总其生产存储机群的数据，以提供公开的可靠性指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Annualized_failure_rate">Annualized failure rate - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology">Self-Monitoring, Analysis and Reporting Technology - Wikipedia</a></li>
<li><a href="https://www.backblaze.com/blog/backblaze-drive-stats-academic-ai-ml-research/">How the Backblaze Drive Stats Dataset Powers Academic and AI/ML...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出故障率下降、使用寿命延长的积极趋势，有用户强调从 3 年左右 14% 的失效率下降到 10 年左右 5%。其他人对报告的 UI、个人经历中出现的早期硬盘故障、价格上升以及容量增长而传输速度停滞的权衡表示担忧，并质疑 Backblaze 为何不采用主机管理的 SMR 进行分层存储。

**标签**: `#storage`, `#hard drives`, `#reliability`, `#Backblaze`, `#data center`

---

<a id="item-5"></a>
## [展示 HN：NSL – Linux 上的类 WSL 体验](https://frostyard.github.io/nsl/) ⭐️ 8.0/10

NSL 通过在单个 VM 中运行一个或多个 systemd-nspawn 容器，为 Linux 提供类似 WSL 的开发环境，实现多发行版的隔离。 它使得在不可变或原子 Linux 主机上的开发者能够在不污染基础系统的情况下，跨多个发行版进行测试和开发，提供类似 Windows WSL2 的工作流。 NSL 使用单个 QEMU 虚拟机及 virtiofs 实现文件共享，并依赖 systemd-nspawn 容器提供进程和命名空间隔离，已在 Snow Linux 13（systemd 261.2）上测试。

hackernews · bketelsen · Sep 29, 14:51 · [社区讨论](https://news.ycombinator.com/item?id=49894351)

**背景**: WSL2 是微软的一个子系统，通过运行一个轻量级虚拟机并提供 Linux 内核，在 Windows 上实现近原生的 Linux 二进制兼容性。systemd-nspawn 是内置于 systemd 的容器管理器，能够创建隔离的进程、文件系统和 IPC 命名空间，类似于轻量级虚拟机。原子 Linux 发行版（如 Fedora Silverblue）被设计为不可变，通过基于镜像的事务进行更新，以保持基础系统的稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux">Windows Subsystem for Linux - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/Systemd-nspawn">systemd - nspawn - ArchWiki</a></li>
<li><a href="https://www.zdnet.com/article/atomic-vs-immutable-linux-distro-how-to-decide/">Atomic vs. immutable Linux : Why choose one when these... - ZDNET</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 NSL 提供了类似 WSL 的干净体验，简化了在多个发行版上的工作；同时也有人质疑为何需要额外的 VM，因为在 Linux 上直接使用 systemd-nspawn 似乎就足够。还有人将其与 distrobox、toolbx 等现有工具进行比较，询问为何不基于这些项目构建，而是推出另一个选项。

**标签**: `#WSL`, `#Linux`, `#containers`, `#development-tools`, `#systemd-nspawn`

---

<a id="item-6"></a>
## [Vermont replacing power plants with home batteries](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms) ⭐️ 8.0/10

Vermont utilities are using a network of residential batteries to form a virtual power plant that supplies power during storms, reducing reliance on traditional power plants.

hackernews · devonnull · Sep 29, 18:19 · [社区讨论](https://news.ycombinator.com/item?id=49897993)

**标签**: `#virtual power plant`, `#home battery storage`, `#grid modernization`, `#renewable energy`, `#energy resilience`

---

<a id="item-7"></a>
## [Simon Willison 现场直播 OpenAI DevDay 2026 主题演讲，地点 Fort Mason](https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/) ⭐️ 8.0/10

Simon Willison 正在为 OpenAI DevDay 2026 的主题演讲和现场笔记进行直播博客，并提到他获得了免费门票以及创作者区的座位。 此直播博客提供了 OpenAI 最新公告的实时见解，使开发者和研究者能够立即获取技术细节，从而影响 AI 产品的开发。 Willison 提到，就像去年一样，他获得了免费门票和创作者区座位，并且他将在一天内持续发布更新。

rss · Simon Willison · Sep 29, 15:55

**背景**: OpenAI DevDay 是 OpenAI 每年举办的开发者大会，用于发布新模型、工具和平台更新。2026 年版于 9 月 29 日在旧金山的 Fort Mason 举行。知名技术作家和直播博主 Simon Willison 获得免费门票并坐在创作者区，正在实时记录主题演讲和其他会议的内容。

**标签**: `#openai`, `#devday`, `#ai`, `#llms`, `#live-blog`

---

<a id="item-8"></a>
## [Dyson-Schwinger 有效作用方法用于粗糙波动率期权定价。](https://arxiv.org/abs/2609.37741) ⭐️ 8.0/10

论文提出了一种基于 Dyson-Schwinger 有效作用的非微扰随机波动率期权定价框架，利用两粒子不可约(2PI)有效作用和间隙方程推导出价格和波动率联合律的自洽高斯近似。在 exp-OU、SABR、粗糙 Bergomi 和粗糙 SABR 等模型中，所得的确定性引擎与 PDE 或准蒙特卡洛参考结果在从亚基点到数十基点的误差范围内吻合。 这项工作将量子场论与量化金融相结合，提供了一种非微扰工具，能够提升异国期权的校准和定价，同时减少对昂贵蒙特卡洛模拟的依赖。通过将波动率视为相互作用的量子场，该方法为马尔可夫和粗糙（Volterra）波动率模型提供了统一的确定性引擎。 该方法在对数价格、对数波动率或 Lamperti 坐标下工作，将联合律近似为自洽高斯，其均值和有效扩散由 2PI 稳定性条件决定，漂移通过统计线性化获得。指数笑容生成和 CEV 等相互作用项通过高斯矩生成函数精确评估，而着装逆传播子的局部性决定了马尔可夫模型（简化为常微分方程）与粗糙模型（保留完整双时间传播子）的区别，从而通过单次收缩高效计算冲动-维加曲线。

rss · arXiv Quantitative Finance · Sep 30, 04:00

**背景**: 在量子场论中，Dyson-Schwinger 方程是格林函数的确切运动方程，而两粒子不可约(2PI)有效作用提供了一种非微扰框架，通过自洽高斯近似重求传播子。粗糙波动率模型（如粗糙 Bergomi）使用由分数布朗运动驱动的 Volterra 过程来捕捉资产波动率的观测到的粗糙（低赫斯特）行为，其中记忆核导致非局部时间传播子。论文表明，当着装逆传播子在时间上是局部的时候，间隙方程简化为几个常微分方程（马尔可夫情况），而对于粗糙的 Volterra 模型则必须保留完整的双时间传播子，使特征函数变为对数方差场上的高斯积分。这使得确定性引擎能够在各种随机波动率规范上与 PDE 或准蒙特卡洛解决方案进行基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/two-particle-irreducible-effective-action">2PI Effective Action in Field Theory - emergentmind.com</a></li>
<li><a href="https://bsic.it/rough-volatility-a-fractional-brownian-motion-approach/">Rough volatility: A Fractional Brownian Motion Approach. – BSIC | Bocconi Students Investment Club</a></li>
<li><a href="https://medium.com/@ibrahimlanre1890/volterra-processes-modelling-market-memory-412283cea6c3">Volterra Processes: Modelling Market Memory | by Ibrahim Lanre Adedimeji | Medium</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#stochastic volatility`, `#rough volatility`, `#Dyson-Schwinger`, `#option pricing`

---

<a id="item-9"></a>
## [并非所有 LP 都相同：自动做市商流动性提供中的主动-被动差距](https://arxiv.org/abs/2609.37963) ⭐️ 8.0/10

该论文提出了一种基于 markout 的框架，通过 LIFO 减法法和无限小 LP 基准，将 Uniswap 流动性提供者的盈利分解为主动和被动两部分。在以太坊、Arbitrum 和 Base 上的 Uniswap v2、v3 和 v4 池子中实证显示，被动 LP 的盈利可能与池子整体盈利存在显著差异。 通过揭示 AMM 中的不利选择在流动性提供者之间并不均匀分布，该研究为 LP 策略设计、费用层级优化以及更准确的去中心化交易所市场质量测量提供了可操作的见解。这有助于协议和投资者更好地分配资本并减少集中流动性 AMM 中的损失。 该方法包括两种互补手段：一种是 LIFO 减法，通过匹配短寿命的铸造-销毁头寸并按流动性份额分配 swap 级 markout；另一种是无限小 LP 基准，从 AMM 价格路径估算完全被动、始终在范围内的边际 LP 表现。结果表明，被动盈利与池子总体盈利存在分歧，以太坊上的主动-被动差距较二层网络更大，而高费用池子中的被动 LP 表现更好；两种方法在大多数池子中给出方向上一致的估计。

rss · arXiv Quantitative Finance · Sep 30, 04:00

**背景**: 自动做市商（AMM）通过汇集流动性提供者（LP）的资产来实现代币交易，LP 因而获得交易费用，但也会面临因价格偏离而导致的无常损失。在 Uniswap v3 和 v4 等集中流动性 AMM 中，LP 可以将资本集中在特定价格区间，并能够根据交易流动主动再仓位，从而产生不同的策略。传统的池子层面分析假设所有 LP 是同质的，掩盖了主动（再平衡）和被动（静止）流动性提供之间的差异。markout 衡量 LP 头寸因价格变动而产生的价值变化，使研究者能够将费用收入（被动部分）与因交易时机产生的利润（主动部分）分开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://efalken.substack.com/p/markouts-for-lp-profitability">Markouts for LP Profitability - by Eric Falkenstein</a></li>
<li><a href="https://arxiv.org/pdf/2606.23070">Mitigating Adverse Selection in Concentrated Liquidity AMMs ...</a></li>
<li><a href="https://developers.uniswap.org/docs/protocols/v4/guides/managing-liquidity/decrease-liquidity">Decrease Liquidity | Uniswap Developers</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#AMM`, `#liquidity provision`, `#Uniswap`, `#blockchain`

---

<a id="item-10"></a>
## [提出用于金融对数收益预测的 CZAR 损失函数](https://arxiv.org/abs/2609.36061) ⭐️ 8.0/10

论文提出了 CZAR（零不可知回报）损失，一种专门用于金融对数收益预测的分段二次目标函数。通过在零处消失的不对称性以及对低估和错误方向预测的惩罚，它旨在防止模型预测为零。 标准的对称损失（MSE、MAE）在金融对数收益条件均值接近零时，使得常数零预测成为近似最优，掩盖了真正的方向技能。CZAR 降低了击败零预测所需的方向准确率阈值，有望提升量化金融中的模型表现。 CZAR 在预测上是凸的，具有适用于梯度提升库的闭形式梯度和 Hessian，其四个超参数通过关联默认值简化为单一有效选择。在 intraday BTC 对数收益上的 LightGBM 实验表明，使用 CZAR 训练的模型减少了零收益偏差，并在大幅度收益上提升了方向准确率。

rss · arXiv Quantitative Finance · Sep 30, 04:00

**背景**: 金融对数收益的条件均值通常接近零，因此对称损失（如 MSE 或 MAE）在训练和评估期间会使常数零预测成为近似最优。这会导致“零收益偏差”，即模型倾向于收缩到零，而缺乏真实预测能力的简单预测者仍可能获得高排名。在高斯线性模型下，击败零预测所需的方向准确率阈值会在预测噪声接近收益标准差时急剧上升，使得噪声较大的模型难以成功。CZAR 的设计旨在即使在重尾噪声下也将此阈值保持在接近 50% 随机猜测的水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.allora.network/research/introducing-the-czar-loss-a-tailored-objective-function-for-financial-log-return-predictions">Introducing the CZAR Loss : A Tailored Objective Function for...</a></li>
<li><a href="https://stats.stackexchange.com/questions/442803/have-log-returns-series-almost-always-conditional-mean-zero-i-presume-no">Have log returns series almost always conditional mean zero ...</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/00036846.2024.2393902">Full article: Assessing the accuracy of directional forecasts</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#quantitative finance`, `#loss function`, `#financial modeling`, `#regression`

---

<a id="item-11"></a>
## [多期鞅最优运输框架及神经加速](https://arxiv.org/abs/2601.05290) ⭐️ 8.0/10

该论文提出了一种多期鞅最优运输（MMOT）的计算框架，给出新的收敛速率，提出增量更新和自适应稀疏网格，并展示了一种混合神经‑投影求解器，实现了 1,597 倍的加速，同时保持鞅约束精度达到 10⁻⁶。 通过将求解时间从秒级降到毫秒级，该方法能够实现复杂金融模型的实时校准，并将最优运输理论与现代机器学习技术结合，可能对计算金融和算法最优运输研究产生重大影响。 理论上，离散收敛率为 O(√Δt log(1/Δt))，线性收敛率为(1−κ)^{2/3}；算法上提出 O(M²)的增量更新和自适应稀疏网格；混合求解器结合 Transformer warm‑starting 和牛顿‑拉夫森投影，使纯神经推理时间从 4.7 s 降至 2.9 ms，鞅约束误差低于 10⁻⁶。

rss · arXiv Quantitative Finance · Sep 30, 04:00

**背景**: 多期鞅最优运输经典最优运输的推广，要求在相邻时间点的边缘分布之间的耦合构成鞅过程，以建模无套利的金融价格演化。求解 MMOT 通常涉及规模大的线性规划，复杂度随时间步数和资产数增加，因而需要增量更新和自适应稀疏网格等算法改进来缓解维度灾难。最近的工作利用神经网络（尤其是基于 Transformer 的 warm‑starting）提供高质量的初始猜测，以加速如牛顿‑拉夫森这样的迭代求解器，同时保持可行性。本文将这些思想融合到混合神经‑投影求解器中，实现显著加速且不牺牲金融校准所需的精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.05290v1">Multi-Period Martingale Optimal Transport: Classical Theory ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0307904X25005402">Structural properties of multi-period martingale optimal ...</a></li>
<li><a href="https://www.emergentmind.com/topics/adaptive-graphs-via-quadratic-optimal-transport">Adaptive Graphs via Quadratic OT</a></li>

</ul>
</details>

**标签**: `#optimal transport`, `#martingale`, `#neural networks`, `#financial modeling`, `#algorithmic acceleration`

---