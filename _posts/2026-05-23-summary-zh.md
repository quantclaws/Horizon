---
layout: default
title: "Horizon Summary: 2026-05-23 (ZH)"
date: 2026-05-23
lang: zh
---

> From 35 items, 7 important content pieces were selected

---

1. [Anthropic 发布 Project Glasswing 初步更新](#item-1) ⭐️ 8.0/10
2. [SpaceX 发射 Starship v3 原型机，部分成功](#item-2) ⭐️ 8.0/10
3. [CISA 努力控制敏感 SF-86 表格泄漏](#item-3) ⭐️ 8.0/10
4. [Deno 2.8](#item-4) ⭐️ 8.0/10
5. [Antigravity 2.0 领先 OpenSCAD 建筑 3D LLM 基准测试](#item-5) ⭐️ 8.0/10
6. [同构动态规划](#item-6) ⭐️ 8.0/10
7. [最大可提取价值拍卖中的不完美承诺](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Project Glasswing 初步更新](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 8.0/10

Anthropic 的 Project Glasswing 推出了一套 AI 驱动的代码安全漏洞检测系统，独立安全公司验证显示，1,752 个高危或严重漏洞中有 90.6% 被确认为真阳性，其中 62.4% 被判定为高危或严重级别。 独立验证表明，AI 驱动的静态分析能够在传统工具基础上显著提升漏洞检测效果，可能改变开发者保护关键软件的方式。 该评估由六家独立安全研究公司审查系统标记的漏洞；Anthropic 还提到，使用其 Codex Security 集成的用户报告准确率约为 90%，并能在代码提交过程中持续发现问题。

hackernews · louiereederson · May 22, 19:31 · [社区讨论](https://news.ycombinator.com/item?id=48240419)

**背景**: Project Glasswing 是 Anthropic 在 2026 年 4 月 7 日启动的行业范围网络安全计划，旨在利用先进 AI 保护关键软件基础设施。该计划随 Claude Mythos 大语言模型的受控预览一同宣布，该模型为漏洞检测能力提供技术支撑。Project Glasswing 的目标是在关键基础设施领域评估下一代 AI 驱动的防御安全工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Project_Glasswing">Project Glasswing</a></li>
<li><a href="https://grokipedia.com/page/Project_Glasswing">Project Glasswing</a></li>

</ul>
</details>

**社区讨论**: 热情的用户声称该工具已成为必备，指出其高准确率和持续发现漏洞的能力；怀疑者如 curl 维护者则认为相较于现有静态分析工具，其改进有限。争论的焦点在于 AI 驱动的 SAST 是否相较于传统 linters 提供了显著价值，以及其成本是否值得采用。

**标签**: `#AI security`, `#static analysis`, `#vulnerability detection`, `#Anthropic`, `#code analysis`

---

<a id="item-2"></a>
## [SpaceX 发射 Starship v3 原型机，部分成功](https://www.nbcnews.com/now/video/spacex-successfully-launches-prototype-of-starship-rocket-263835205505) ⭐️ 8.0/10

SpaceX 发射了 Starship v3 原型机（Flight 12），在助推器出现异常的情况下，返回大气层时热防护表现得到改善。 此次飞行标志着 SpaceX Starship 开发的重要里程碑，为可重复使用发射系统提供了关键测试数据，并在航空航天社区引发了广泛的技术讨论。 在上升阶段，助推器的一台 Raptor 发动机故障且助推器返回点火未成功，导致着陆点偏离且水面冲击较硬；上层在分离后不久失去一台发动机，但其六边形热防护瓷砖未出现明显热点，同时可见的假载荷卫星和 Starlink 质量模拟器按预期部署并烧毁。

hackernews · busymom0 · May 22, 23:41 · [社区讨论](https://news.ycombinator.com/item?id=48242959)

**背景**: SpaceX 的 Starship 是一种两级完全可重复使用的超重型运载火箭，正在研发中，旨在取代 Falcon 9 和 Falcon Heavy，用于近地轨道、月球和火星任务。其动力来自 Raptor 发动机，采用液氧和甲烷的全流量分级燃烧循环，既有海平面型也有真空型。热防护系统采用六边形陶瓷瓷砖，能够承受极端再入温度，此技术经过了多次测试，在此次飞行中表现良好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://nextspaceflight.com/starship/">Starship | Next Spaceflight</a></li>
<li><a href="https://www.linkedin.com/posts/harry-topham_when-is-the-next-starship-launch-spacex-activity-7384276771623444480-Uhoz">SpaceX reveals Starship V 3 : taller, more efficient, and ready... | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，虽然助推器出现发动机故障且返回点火失败，导致偏离目标且硬着水面，但上层的热防护表现出色，未见明显热点。多位观众赞扬了导航软件在发动机异常情况下仍能保持船体对准目标，并注意到假载荷卫星和 Starlink 质量模拟器在再入过程中烧毁的壮观景象。

**标签**: `#SpaceX`, `#Starship`, `#rocket launch`, `#aerospace`, `#reusable launch vehicles`

---

<a id="item-3"></a>
## [CISA 努力控制敏感 SF-86 表格泄漏](https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/) ⭐️ 8.0/10

CISA 正试图控制一次数据泄漏，该泄漏暴露了包括用于联邦背景调查的 SF-86 表格在内的敏感信息，促使立法者要求解释并引发公众批评。 此次泄漏引发对政府安全审查流程安全性的严重担忧，凸显联邦网络安全实践中的漏洞，可能影响国家安全和公众信任。 暴露的 SF-86 表格包含详细的个人数据，如就业史、外国联系人和心理健康信息；CISA 初始称没有数据被泄露的迹象，但批评者指出泄漏似乎源于凭证意外存放在 Git 仓库中。

hackernews · speckx · May 22, 16:54 · [社区讨论](https://news.ycombinator.com/item?id=48238429)

**背景**: 美国网络和基础设施安全局（CISA）是负责保护国家关键基础设施免受网络和物理威胁的联邦机构。SF-86 表格是美国人事管理局用于进行国家安全职位背景调查的问卷，用于收集详尽的个人和历史信息。由于该表格包含敏感细节，其泄露对个人隐私和国家安全构成重大风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cybersecurity_and_Infrastructure_Security_Agency">Cybersecurity and Infrastructure Security Agency - Wikipedia</a></li>
<li><a href="https://www.pdfrun.com/form/sf-86">Fillable Form SF 86 (Rev. Nov. 2016) | PDFRun</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，参议员曾质疑 CISA 削减选举安全工作，并注意到 Tulsi Gabbard 辞职的时机。一些人回忆起之前曾泄露一百万份 SF-86 表格，并批评 CISA 声称没有数据被泄露，指出凭证似乎被存放在 Git 仓库中。还有人担心，如果负责网络安全的机构自身都无法保护数据，那么更广泛的互联网安全令人怀疑。

**标签**: `#cybersecurity`, `#data breach`, `#CISA`, `#government security`, `#SF-86`

---

<a id="item-4"></a>
## [Deno 2.8](https://deno.com/blog/v2.8) ⭐️ 8.0/10

Deno 2.8 introduces updates to its permission model, TypeScript support, and runtime performance, continuing its growth as a secure, Rust-based alternative to Node.js.

hackernews · roflcopter69 · May 22, 11:23 · [社区讨论](https://news.ycombinator.com/item?id=48234380)

**标签**: `#deno`, `#javascript`, `#typescript`, `#runtime`, `#webdev`

---

<a id="item-5"></a>
## [Antigravity 2.0 领先 OpenSCAD 建筑 3D LLM 基准测试](https://modelrift.com/blog/openscad-llm-benchmark/) ⭐️ 8.0/10

Antigravity 2.0 在一项新基准测试中得分最高，该测试评估大语言模型生成参数化 OpenSCAD 建筑模型的能力，具体是模拟帕特农神庙的内部天花板图案。 这一结果表明大语言模型能够生成可用的参数化 CAD 代码来表达复杂的建筑特征，推动了 AI 辅助设计的实际应用。 Antigravity 2.0 是唯一成功复刻帕特农神庙通过眼镜孔可见的重复方形凹槽图案的自主代理，而基准测试指出其他模型在几何上较为粗糙或需要多次尝试。

hackernews · jetter · May 22, 10:38 · [社区讨论](https://news.ycombinator.com/item?id=48234090)

**背景**: OpenSCAD 是一种基于脚本的开源 CAD 工具，用户可以通过描述性语言定义 3D 对象，因而适合由 AI 模型进行程序化生成。近期工作探索使用大语言模型输出 OpenSCAD 代码，以快速创建用于工程和建筑的参数化模型。Antigravity 2.0 是一个集成的人工智能开发环境，内置旨在协助开发者完成 CAD 任务的 LLM 驱动代码生成代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48234090">Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark</a></li>
<li><a href="https://www.reddit.com/r/google_antigravity/comments/1tke0mp/antigravity_20_tops_the_openscad_architectural_3d/">Antigravity 2.0 tops the OpenSCAD architectural 3D LLM benchmark</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenSCAD">OpenSCAD - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Antigravity 2.0 能生成准确的参数化 OpenSCAD 模型，有用户报告打印出近乎完美的自行车零件垫圈，另一位指出它成功复刻了帕特农神庙的内部天花板图案。然而，也有人指出其使用体验问题，如强制浏览器登录和 IDE 不更新，还有人认为基准仅依赖单一模型，难以反映整体性能。

**标签**: `#LLM`, `#OpenSCAD`, `#3D modeling`, `#code generation`, `#benchmark`

---

<a id="item-6"></a>
## [同构动态规划](https://arxiv.org/abs/2605.22076) ⭐️ 8.0/10

本文提出利用顺序同构将动态规划相互关联，表明最优性质可以在同构形式之间传递。作者将此应用于带时间偏好冲击的 Epstein–Zin 偏好，证明乘法 Kreps–Porteus 偏好与风险敏感偏好等价，并在多部门实际商业循环模型中展示了两个数量级的数值精度提升。 通过提供严格的同构框架，该工作使得已知的最优性结果能够在不同的动态规划形式之间转移，从而丰富了经济理论和计算实践。这种跨学科的联系有助于提高依赖递归效用和偏好规范的宏观经济模型的准确性和可求解性。 利用动力系统理论中的共轭方法，论文构建了不同动态规划的贝尔曼算子之间的顺序同构。这导致了带时间偏好冲击的 Epstein–Zin 偏好的尖锐最优性条件，表明乘法 Kreps–Porteus 偏好与风险敏感偏好同构，并在多部门实际商业循环模型中实现了大约两个数量级的数值精度提升。

rss · arXiv Quantitative Finance · May 22, 04:00

**背景**: 动态规划是一种通过将顺序决策问题分解为更简单的子问题并使用贝尔曼方程计算价值函数来求解的方法。顺序同构是两个偏序集之间的双射单调映射，它保持顺序结构，使得诸如最优性之类的性质在集合之间通过这样的映射传递成为可能。Epstein–Zin 偏好通过将风险厌恶与时间弹性分离来推广预期效用，而 Kreps–Porteus 和风险敏感偏好是特定的递归效用形式；实际商业循环（RBC）模型利用技术冲击模拟宏观经济波动，并且经常依赖于价值函数的数值近似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Isomorphism">Isomorphism - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conjugation">Conjugation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epstein–Zin_preferences">Epstein – Zin preferences - Wikipedia</a></li>

</ul>
</details>

**标签**: `#dynamic programming`, `#economic preferences`, `#order isomorphism`, `#numerical methods`, `#real business cycle`

---

<a id="item-7"></a>
## [最大可提取价值拍卖中的不完美承诺](https://arxiv.org/abs/2605.22667) ⭐️ 8.0/10

该论文建模了以太坊区块构建者在以概率 ε 背叛的情况下，会复制获胜 MEV 机会的类型特定比例 γ(τ)。搜索者预期此行为，在风险的第一价出价和安全的威慑出价之间进行选择，从而得到一个分段均衡，并利用 libmev 数据集进行理论和实证分析。 通过量化构建者承诺缺陷对拍卖收入和剩余价值提取的影响，该研究表明可信的 MEV 拍卖不仅需要合适的拍卖设计，还需要限制构建者事后使用出价信息的能力。这为协议设计者提供了参考，并指出哪些 MEV 类型最容易受到构建者背叛的影响。 模型假设构建者以概率 ε 背叛，并在背叛时获胜者的 MEV 中捕获比例 γ(τ)；搜索者可以出第一价出价 v 或威慑出价 b = γ(τ)v 使背叛无利可图，从而得到取决于可复制性和竞争的分段均衡。实证上，γ(τ) 通过 libmev 数据集中右尾贿赂平台估计，显示三明治机会竞争激烈，而裸奔 arbitrage 和清算则暴露出大量剩余价值。

rss · arXiv Quantitative Finance · May 22, 04:00

**背景**: 在以太坊中，区块构建者进行密封拍卖，搜索者提交交易捆绑并支付贿赂以使其捆绑被包含；构建者随后选择获胜捆绑并构建区块。协议并未强制构建者在看到捆绑后遵守拍卖结果，由此产生承诺问题。第一价拍卖将最高出价者作为获胜者，而威慑出价则设定为使任何拍卖后的利用行为无利可图。libmev 数据集记录了历史贿赂和捆绑结果，从而能够测量构建者在背叛后能够复制的 MEV 量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.22667">Imperfect Commitment in Maximal Extractable Value Auctions</a></li>
<li><a href="https://arxiv.org/html/2605.22667v1">Imperfect Commitment in Maximal Extractable Value Auctions - arXiv</a></li>
<li><a href="https://www.researchgate.net/publication/382445216_Who_Wins_Ethereum_Block_Building_Auctions_and_Why">(PDF) Who Wins Ethereum Block Building Auctions and Why?</a></li>

</ul>
</details>

**标签**: `#MEV`, `#blockchain auctions`, `#Ethereum`, `#game theory`, `#empirical analysis`

---