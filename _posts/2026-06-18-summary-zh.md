---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> From 46 items, 15 important content pieces were selected

---

1. [GLM-5.2 可能是目前最强的文本-only 开放权重 LLM](#item-1) ⭐️ 9.0/10
2. [Epic Games 发布开源 Lore 版本控制系统，专注可扩展游戏资产管理](#item-2) ⭐️ 8.0/10
3. [美国科学面临资金危机、签证障碍和研究人员外流](#item-3) ⭐️ 8.0/10
4. [特斯科因博通定价争议迁移 4 万 VMware 工作负载](#item-4) ⭐️ 8.0/10
5. [大众汽车因要求 Play Protect 认证而封锁 GrapheneOS 用户](#item-5) ⭐️ 8.0/10
6. [GLM-5.2 成为 Artificial Analysis 指数领先的开放权重模型](#item-6) ⭐️ 8.0/10
7. [PIVOT 提供可微分层连接 Black-Scholes 价格与隐含波动率。](#item-7) ⭐️ 8.0/10
8. [代理 AI 系统的模型验证：基于 POMDP 的信念状态、预测和策略验证框架](#item-8) ⭐️ 8.0/10
9. [研究揭示非洲和拉美预测市场的选择偏差](#item-9) ⭐️ 8.0/10
10. [纽约市拥堵收费后公共交通增长及空间不均的出行需求变化](#item-10) ⭐️ 8.0/10
11. [CARLOS：用于连续时间最优停止的深度强化学习算法](#item-11) ⭐️ 8.0/10
12. [LLM 消费行为理论：新兴研究领域的基础](#item-12) ⭐️ 8.0/10
13. [风能现在成为德州日前电价的主要驱动因素，超过天然气](#item-13) ⭐️ 8.0/10
14. [用于期权定价中计划事件风险的非跨度识别协议](#item-14) ⭐️ 8.0/10
15. [动态配额交易市场中的交易摩擦](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM-5.2 可能是目前最强的文本-only 开放权重 LLM](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

2026 年 6 月 16 日，Z.ai 发布了 GLM-5.2，这是一个具有 7530 亿参数的 Mixture‑of‑Experts 文本-only 大语言模型，拥有 100 万 token 上下文窗口，并采用 MIT 许可证，此前于 6 月 13 日已向编码计划订阅者提前发布。 GLM-5.2 在 Artificial Analysis Intelligence Index 上排名第一，并在编码基准测试中表现突出，表明巨型开放权重 MoE 模型能够在 MIT 许可证下实现最先进性能，这可能推动研究和商业应用的加速。 该模型总参数为 7530 亿，但推理时仅激活约 400 亿参数，采用 IndexShare 稀疏注意力机制以高效处理长上下文，并支持 100 万 token 的上下文窗口。在基准测试中每任务约消耗 43k 输出 token，在 Artificial Analysis Intelligence Index v4.1 上排名第一，在 Code Arena WebDev 排行榜上排名第二，且通过 OpenRouter 提供，输入约 1.40 美元/百万 token，输出约 4.40 美元/百万 token。

rss · Simon Willison · Jun 17, 23:58

**背景**: 混合专家（MoE）架构使模型能够拥有巨量的总参数，但在每次输入时只激活一小部分动态选择的专家，从而降低计算成本。100 万 token 的上下文窗口使模型能够一次性处理极长的输入，如完整代码库或长文档。采用 MIT 许可证发布模型权重意味着可自由使用、修改和再分发，这有助于在学术界和工业界广泛传播。Z.ai 的 GLM 系列在之前的 GLM‑5 和 GLM‑5.1 基础上进行了规模和上下文长度的提升，同时保持了纯文本输入的定位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apidog.com/blog/glm-5-2-what-is/">What Is GLM - 5 . 2 ?</a></li>
<li><a href="https://medium.com/@divagr1925/breaking-the-scaling-wall-an-introduction-to-mixture-of-experts-in-llm-f8447a337a05">Breaking the Scaling Wall: An Introduction to Mixture of Experts in...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-weights`, `#Mixture-of-Experts`, `#AI research`, `#large language model`

---

<a id="item-2"></a>
## [Epic Games 发布开源 Lore 版本控制系统，专注可扩展游戏资产管理](https://lore.org/) ⭐️ 8.0/10

Epic Games 宣布了 Lore，一个为可扩展性而构建的开源版本控制系统，专门用于处理游戏开发中的大型二进制资产，旨在成为 Perforce 的替代方案。 Lore 解决了游戏工作室长期以来对能够高效管理巨型美术、模型和音频文件的版本控制系统的需求，有望减少对专有 Perforce 许可证的依赖。 Lore 支持任意内容类型、多轴规模、多租户安全以及公开的版本化规范，采用宽松的开源许可证，但 UEFN 构建目前使用尚未在开源版本中提供的专有压缩格式。

hackernews · regnerba · Jun 17, 14:30 · [社区讨论](https://news.ycombinator.com/item?id=48571081)

**背景**: 在游戏开发中，团队需要协作处理大型二进制文件，如纹理、3D 模型和音频，传统面向文本的系统如 Git 在没有 Git LFS 等扩展的情况下处理效率低下。Perforce（Helix Core）因其对大文件、文件锁定和细粒度权限的支持，长期成为该领域的行业标准，但它是专有软件，成本较高。Lore 旨在提供一个开源替代方案，将 Perforce 在二进制资产上的可扩展性与宽松许可证和现代设计相结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open-Source Version Control System</a></li>
<li><a href="https://www.perforce.com/blog/vcs/version-control-for-binary-files">Version Control for Binary Files: Manage Large ... | Perforce Software</a></li>

</ul>
</details>

**社区讨论**: 评论者强调 Lore 不 intended 与 Git 在一般软件开发中竞争，而是旨在挑战 Perforce 在游戏开发工作流中的地位。多位用户指出它可能通过文件锁定和高效处理大型二进制资产来改善艺术家的工作流程，而另一些人则认为 Perforce 因熟悉度和现有工具而仍然根深蒂固。还有人提到 Git 的界面冗长，并希望 Lore 能提供更简洁的体验。

**标签**: `#version-control`, `#game-development`, `#open-source`, `#scalability`, `#Perforce-alternative`

---

<a id="item-3"></a>
## [美国科学面临资金危机、签证障碍和研究人员外流](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 8.0/10

《科学美国人》杂志的文章认为，美国科学与政治之间的历史性协定已经破裂，导致经费严重短缺、对外国研究者的签证规定更加严格，以及越来越多的科学家离开美国。 这一破裂威胁到美国在全球研究中的领导地位，可能导致人才外流，使创新转移到其他国家，并破坏科学合作所依赖的稳定经费和开放的国际交流。政策制定者和机构需要采取措施以保护国家的科学能力。 评论者描述了具体影响：一位光学陷阱专家在资金压力下哭泣后考虑移民；教授们因签证限制无法招聘外国研究生；许多人感到政府决策日益政治化，导致一些人考虑完全离开科学领域。这些个人轶事说明了研究生态系统所面临的系统性压力。

hackernews · presspot · Jun 17, 09:54 · [社区讨论](https://news.ycombinator.com/item?id=48568058)

**背景**: 美国长期依赖联邦科学机构（如 NIH 和 NSF）与私人 philanthropy 的合作来资助基础研究，同时通过 H‑1B 和 J‑1 等签证吸引全球人才。二战后，这种合作推动了战后创新和经济增长。近年来，政治两极分化加剧，围绕气候变化和公共卫生等问题的争论使这种关系紧张，导致经费不确定和移民审查趋严。

**社区讨论**: 评论者对经费削减和签证障碍表示沮丧和个人困扰，许多人描述同事离开或考虑搬迁到国外。一些人指出科学问题日益政治化，而少数人怀念地提出重建贝尔实验室等机构以振兴研究。

**标签**: `#science policy`, `#research funding`, `#academia`, `#US science`, `#visa restrictions`

---

<a id="item-4"></a>
## [特斯科因博通定价争议迁移 4 万 VMware 工作负载](https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/) ⭐️ 8.0/10

特斯科正在将约 4 万台服务器工作负载从 VMware 基础设施迁移到其他虚拟化平台，原因是博通终止了支持并提高了价格。 此次大规模迁移凸显了企业对供应商锁定和博通收购 VMware 后昂贵许可证变更的日益反感，预示着向更具灵活性和成本效益的基础设施转移。 特斯科称博通于 2026 年 1 月停止对其 VMware 产品的支持，迫使零售商支付第三方支持费用，并在英国高等法院起诉博通涉嫌滥用行为。

hackernews · Bender · Jun 17, 21:00 · [社区讨论](https://news.ycombinator.com/item?id=48576838)

**背景**: VMware 提供虚拟化软件，使企业能够在共享服务器上运行多个工作负载，从而减少硬件依赖。博通在 2023 年收购 VMware 后，修改了许可证和支持政策，导致价格大幅上涨且对现有客户的支持减少。企业常通过将工作负载迁移到其他平台或公共云来避免供应商锁定并控制成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/">Tesco moving 40,000 server workloads off VMware ... - Ars Technica</a></li>
<li><a href="https://nsaneforums.com/news/software-news/300-percent-price-hikes-push-disgruntled-vmware-customers-toward-broadcom-rivals-r26310/">300 percent price hikes push disgruntled VMware ... - Nsane Forums</a></li>
<li><a href="https://slashdot.org/story/24/10/01/216232/att-claims-vmware-by-broadcom-offered-it-a-1050-price-increase">AT&T Claims VMware By Broadcom Offered It a 1,050% Price ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出博通的激进定价策略，提到如 Proxmox 等替代方案，并指出迁移过程中与备份软件的兼容性挑战，同时许多人认为类似经历在 VMware 客户中普遍存在。

**标签**: `#VMware`, `#Broadcom`, `#enterprise IT`, `#virtualization`, `#cloud migration`

---

<a id="item-5"></a>
## [大众汽车因要求 Play Protect 认证而封锁 GrapheneOS 用户](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3) ⭐️ 8.0/10

大众汽车将其车辆应用更新为仅支持 Play Protect 认证的 Android 设备，从而有效封锁了使用隐私焦点操作系统 GrapheneOS 的用户。 此举剥夺了注重隐私的 Android 用户对远程空调、充电等车辆功能的访问，凸显了企业对设备兼容性日益增长的控制，并引发了对用户权利的担忧。 该应用现在依赖 Play Protect 认证，而 GrapheneOS 设备因未通过 SafetyNet 认证而无法通过此检查；因此，基于社区的集成和使用大众 API 的第三方工具均已失效。

hackernews · microtonal · Jun 17, 15:04 · [社区讨论](https://news.ycombinator.com/item?id=48571526)

**背景**: GrapheneOS 是一个注重隐私、经过加固的 Android 分支，省略了 Google Play 服务，并且经常无法通过 Google 的 SafetyNet/Play Protect 检查。Play Protect 认证是谷歌的一个项目，用于验证设备是否通过了 Android 兼容性测试并包含有授权的 Google 应用；只有通过认证的设备才能访问某些 API。SafetyNet  attestation（现在属于 Play Integrity API）会检查设备完整性以检测自定义 ROM、root 或篡改，这会导致像 GrapheneOS 这样的未通过认证的 ROM 被阻止。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/googleplay/answer/7165974?hl=en">Check & fix Play Protect certification status - Google Play Help</a></li>
<li><a href="https://www.android.com/certified/">Android – Certified</a></li>

</ul>
</details>

**社区讨论**: 评论者对大众限制隐私导向选项表示失望和批评，有人表示会重新考虑购买大众汽车。还有人指出官方应用广告较多，更倾向于使用 Home Assistant 等替代方案进行车辆控制。

**标签**: `#Volkswagen`, `#GrapheneOS`, `#Android`, `#privacy`, `#automotive API`

---

<a id="item-6"></a>
## [GLM-5.2 成为 Artificial Analysis 指数领先的开放权重模型](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) ⭐️ 8.0/10

GLM-5.2 在 Artificial Analysis 智能指数上排名第一，成为领先的开放权重模型，标志着 GLM 系列的新里程碑。该模型最近发布，展现出在长时程任务和编码方面的强大能力。 其排名第一表明开放权重模型现在能够在推理和编码方面与专有系统竞争，为开发者和研究者提供了具成本效益的替代方案。这一趋势可能加速开放 LLMs 在实际软件工程中的采用。 GLM-5.2 支持 100 万 token 的上下文窗口，在长时程 agentic 工作流中表现出色，并在 Hugging Face 的 zai-org/GLM-5.2 仓库中提供。用户报告称其推理阶段消耗大量 token，编码任务响应速度相比某些替代方案较慢。

hackernews · himata4113 · Jun 17, 09:12 · [社区讨论](https://news.ycombinator.com/item?id=48567759)

**背景**: 人工分析智能指数是一个综合基准，用于评估语言模型在推理、编码、知识、指令遵循、科学推理和多步任务完成方面的表现。开放权重模型是指其参数公开可用的模型，任何人都可以使用、微调或部署而不依赖专有 API。GLM-5.2 属于智谱 AI 的 GLM 系列，该系列侧重于 agentic 软件工程和长时程任务，而不仅仅是聊天机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM-5.2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 GLM-5.2 的强大性能和低成本，指出一些提供商以每月 50 美元提供无限 token，远低于专有 API 的价格。然而，也有用户指出该模型在推理上耗费过多时间和 token——例如，为一个小型编码任务花费超过 15 分钟和 45k token——使其速度不如 Codex 5.5 或 Composer 2.5 等替代方案。

**标签**: `#LLM`, `#open weights`, `#GLM-5.2`, `#Artificial Analysis`, `#AI benchmark`

---

<a id="item-7"></a>
## [PIVOT 提供可微分层连接 Black-Scholes 价格与隐含波动率。](https://arxiv.org/abs/2606.17065) ⭐️ 8.0/10

论文提出 PIVOT，一种可微分翻译器，在保持高效 LBR 求解器前向传递不变的同时，通过对 Black-Scholes 价格映射进行隐式求导来计算梯度，并显式处理低维伽奇点。 通过在价格空间和隐含波动率空间之间提供梯度兼容的接口，PIVOT 使机器学习模型能够直接优化期权定价目标，提升校准精度并实现量化金融中的端到端可微分流程。 PIVOT 对光滑的 Black‑Scholes/Black‑76 价格映射进行隐式求导，采用门控合约：无效域返回 NaN，良好条件的行传递精确的 1/vega 梯度，低维伽行被衰减；融合的 Triton 内核在 H100 上达到每秒 1.79×10⁹ 次隐含波动率评估，相对于参考 C 求解器的最大相对误差为 9.3×10⁻¹⁴。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: Black‑Scholes 模型将期权价格映射到隐含波动率，这一变换是单调的但没有闭形式逆，因而需要数值求解器，如 Jäckel 的 'Let’s Be Rational'（LBR）算法。虽然 LBR 能以机器精度高效求逆，但其前向传递包含分支逻辑，无法直接用自动求导，因而成为基于梯度学习的瓶颈。在低维伽区域，逆映射出现奇点，导致梯度 1/vega 发散，必须显式处理以避免数值不稳定。PIVOT 通过保持 LBR 前向传递不变，并利用隐式求导提供梯度，配合门控机制对奇点区域进行适当处理，从而弥补这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.17065">PIVOT: Bridging Black - Scholes Implied-Volatility and Price Objectives...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Differentiation_rules">Differentiation rules - Wikipedia</a></li>
<li><a href="https://quant.stackexchange.com/questions/27603/understanding-vega-calculation-in-black-scholes-model">Understanding Vega calculation in black Scholes model - Quantitative...</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#option pricing`, `#differentiable programming`, `#Black-Scholes`, `#machine learning`

---

<a id="item-8"></a>
## [代理 AI 系统的模型验证：基于 POMDP 的信念状态、预测和策略验证框架](https://arxiv.org/abs/2606.17383) ⭐️ 8.0/10

该论文提出了一种基于部分可观测马尔可夫决策过程（POMDP）的框架，用于独立验证代理 AI 系统的信念状态、预测和策略，并将大型语言模型形式化为近似贝叶斯滤波算子。通过投资组合管理案例研究（涉及隐含市场 regime 推断和 Black‑Litterman 投资组合构建）进行演示。 该工作填补了自主智能体模型风险验证的空白，为 AI 安全、治理和监控提供了严格的理论基础，可能对依赖自主决策的金融、医疗等行业产生广泛影响。 框架将自主决策分解为信息、信念、预测、行动和效用六个组成部分，每部分可独立验证；将大型语言模型建模为近似贝叶斯滤波算子。提出涵盖状态空间、滤波、预测、策略、效用规范和参数风险的模型风险分类法；通过信念校准、覆盖测试、消融研究和参数敏感性分析进行经验验证。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 部分可观测马尔可夫决策过程（POMDP）是马尔可夫决策过程的推广，用于建模代理在无法直接观察环境真实状态的情况下进行决策的情形。代理 AI 系统能够持续获取信息、形成对潜在环境状态的信念、生成预测、选择行动并随时间调整行为，这使得传统的预测准确性验证方法不足以评估其决策过程。论文将大型语言模型视为近似贝叶斯滤波算子，即在不确定环境中对隐藏状态进行递归估计的方法。基于 POMDP 的验证框架则把模型风险扩展到信念校准、预测覆盖、策略鲁棒性等多个维度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process">Partially observable Markov decision process - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/partially-observable-markov-decision-process-pomdp-in-ai/">Partially Observable Markov Decision Process (POMDP) in AI - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#Agentic AI`, `#POMDP`, `#Model Validation`, `#Large Language Models`, `#Reinforcement Learning`

---

<a id="item-9"></a>
## [研究揭示非洲和拉美预测市场的选择偏差](https://arxiv.org/abs/2606.17503) ⭐️ 8.0/10

本文提出了一种结算可读性的编码度量，并将其应用于 Polymarket 和 Kalshi 上 6,047 个非洲和拉美主题的预测市场合约。结果显示，市场形成具有选择性，非洲合约主要集中在足球，而拉美合约则以委内瑞拉相关的公民事件为主。 结果表明，预测市场的库存反映了平台能够结算的内容，而非公众关注的焦点，提醒研究者和政策制定者不要将市场活动等同于公众兴趣。这一发现有助于改善不同地区预测市场的设计和解释。 结算可读性度量在主要维度上的独立双评分达到了 0.92 和 0.96 的序列信度，盲测人类基准达到 0.97 和 0.92。可读性将体育和选举排在最高，冲突排在最低；在已上架的合约中，可读性与交易价值呈负相关。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 预测市场让参与者买卖基于未来事件结果的合约，通过价格聚合信念。结算可读性指的是不确定性能够被清晰描述、来源并由第三方可信解决的程度，这决定了合约是否能够上架。Polymarket 和 Kalshi 是两个主要的全球预测市场平台，通常费用低且几乎不需要 KYC。聚焦非洲和拉美地区，可以看出哪些不确定性在这些地区变得可交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.17503">[2606.17503] What Prediction Markets Can See: Market Formation, Settlement Legibility, and the Geography of Tradable Uncertainty in Africa and Latin America</a></li>
<li><a href="https://polymarket.com/">Polymarket | The World's Largest Prediction Market</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-04-09/how-prediction-markets-are-blurring-the-line-between-trading-and-betting?trk=article-ssr-frontend-pulse_little-text-block">How Prediction Markets Are Blurring the Line Between... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#settlement legibility`, `#market formation`, `#Africa`, `#Latin America`

---

<a id="item-10"></a>
## [纽约市拥堵收费后公共交通增长及空间不均的出行需求变化](https://arxiv.org/abs/2606.17530) ⭐️ 8.0/10

研究发现，纽约市的拥堵收费显著增加了公交和地铁客流，而整体出行需求仅 modestly 下降，且这些效应在空间和人口统计学上存在不均。 该研究为评估拥堵收费政策提供了实证，揭示了空间异质性影响，对城市交通规划和基于 AI/ML 的政策评估方法具有重要参考价值。 研究使用时间序列基础模型生成概率型反事实需求预测，分析了公交、地铁和总出行量数据，发现政策后公交和地铁客流显著上升，总出行需求小幅下降，减少主要集中在拥堵缓解区，而交通增长延伸至曼哈顿核心以外，且不同社区的适应程度存在差异。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 拥堵收费是指对进入特定收费区域的车辆收费，以减少交通拥堵并鼓励使用公共交通。时间序列基础模型是大规模预训练模型，能够在不重新训练的情况下对新序列进行预测，实现零样本预测。概率型反事实预测生成没有政策时需求的分布，从而在考虑不确定性的情况下进行因果推断。这些方法共同使研究者在缺乏理想对照组的情况下评估城市范围的干预措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jscastanoc.github.io/blog/foundation-models-for-time-series/">Foundation Models for Time Series —A Case Study Using Brain...</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/10962247.2022.2100510">Full article: Cordon screen: A cordon - based congestion pricing ...</a></li>
<li><a href="https://scispace.com/pdf/causal-effect-estimation-with-global-probabilistic-1ozepqd9.pdf">Causal Effect Estimation with Global Probabilistic</a></li>

</ul>
</details>

**标签**: `#congestion pricing`, `#urban mobility`, `#public transit`, `#time series forecasting`, `#policy evaluation`

---

<a id="item-11"></a>
## [CARLOS：用于连续时间最优停止的深度强化学习算法](https://arxiv.org/abs/2606.17545) ⭐️ 8.0/10

本文提出了一种名为 CARLOS 的自适应深度强化学习算法，通过在逐步细化的时间网格上优化联合时空决策边界来学习连续时间的最优停止策略。 通过消除粗离散化的需求，CARLOS 能够获得高于传统伯蒙特求解器的行权价格，并逼近美式期权上界，为金融和运筹学提供更精确、高效的工具。 CARLOS 采用聚合深度神经网络（ADNN）来表示停止边界，从粗时间网格开始并迭代细化网格同时训练 ADNN，并使用自适应采样策略将训练样本集中在学习到的边界附近。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 最优停止问题涉及在何时执行某个动作以最大化预期收益，常见于美式期权定价。传统数值方法通过离散时间求解，粗网格会导致低估，而细网格则在后向递归中积累误差。强化学习提供了一种基于仿真的替代方法，能够直接从采样路径中学习策略而无需显式离散化。CARLOS 中的聚合深度神经网络同时建模状态和时间对停止决策的影响，从而能够在任意精细的时间分辨率下学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.17545">[2606.17545] Continuous-time Optimal Stopping through Deep ...</a></li>
<li><a href="https://www.columbia.edu/~xz2574/download/DSXZ2.pdf">Learning to Optimally Stop Diffusion Processes, with</a></li>

</ul>
</details>

**标签**: `#optimal stopping`, `#reinforcement learning`, `#deep learning`, `#stochastic control`, `#finance`

---

<a id="item-12"></a>
## [LLM 消费行为理论：新兴研究领域的基础](https://arxiv.org/abs/2606.18005) ⭐️ 8.0/10

该论文提出 LLM 消费行为理论，这是一个新的跨学科框架，正式化了大语言模型代理如何反映人类偏好以及它们的个体决策如何在代理市场中汇总为市场需求。 通过将 LLM、代理决策以及经典/行为经济学联系起来，该理论为研究 AI 驱动的市场提供了统一视角，指出传统经济假设可能失效的地方，为 AI 和经济学领域提供了新的研究议程。 该工作结合 NLP 进展和经济模型，描述了偏好表示、对齐挑战以及 LLM 代理中的异质性，同时指出理性等假设可能失效；虽然未提供实证验证，但列出了关于对齐、偏好 elicitation 和市场动态的开放问题。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 大语言模型正越来越多地被用作自主代理，代表用户做出购买决策，这使得消费理论的研究重点从人类决策者转向 AI 驱动的代理。消费理论传统上研究个体如何在约束下分配有限资源以最大化效用，基于偏好和约束。代理市场用买方和卖方软件代理取代直接的人与人交换，代理之间自主互动产生新的市场动态，因而需要更新的理论框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/agentic-markets">Agentic Markets : Autonomous Economic Platforms</a></li>
<li><a href="https://www.investopedia.com/terms/c/consumer-theory.asp">investopedia.com/terms/c/ consumer - theory .asp</a></li>
<li><a href="https://blog.synapticlabs.ai/eliciting-human-preferences-with-language-models">Eliciting Human Preferences with Language Models</a></li>

</ul>
</details>

**标签**: `#LLM`, `#consumer behavior`, `#agentic markets`, `#theoretical economics`, `#NLP`

---

<a id="item-13"></a>
## [风能现在成为德州日前电价的主要驱动因素，超过天然气](https://arxiv.org/abs/2604.14257) ⭐️ 8.0/10

研究者利用因果发现方法发现，风能已成为德州日前电价的主要驱动因素，其影响强度超过天然气的三倍，但在峰期其抑价效应减弱，并将拥堵成本转移至远端负荷中心。 该研究颠覆了德州电价由天然气驱动的传统观点，凸显了规划者和投资者必须考虑风能日益增长的影响及其时空特征对价格风险和基础设施需求的重要性。 研究采用因果发现算法（如 GES、PC、LiNGAM）对 ERCOT 的批发电价时间序列进行分析，发现风能的因果影响超过天然气的三倍，同时指出风能增长导致远端负荷中心的拥堵成本上升。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: ERCOT 运营着德州大部分地区的日前和实时电力市场，价格通过反映发电报价、负荷需求和输电限制的拍卖来确定。风能和太阳能的快速增长，以及电气化和数据中心负荷的上升，正在改变曾经高度依赖天然气发电机的传统价格形成机制。诸如贪婪等价搜索（GES）算法之类的因果发现技术能够从观测数据中推断出方向性关系，帮助区分真正的驱动因素和单纯的相关性。当功率流超过线路限制时会发生输电拥堵，导致重新调度并产生被转移到远端负荷中心的额外成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modoenergy.com/research/jp/ercot-energy-academy-power-markets-real-time-day-ahead-sced-ordc-qse-lse-ancillary-services-price-adders-system-lamdba-locational-marginal-prices">ERCOT : The Energy Academy - How do power markets in Texas work?</a></li>
<li><a href="https://www.pywhy.org/dowhy/v0.10/example_notebooks/dowhy_causal_discovery_example.html">Causal Discovery example — DoWhy documentation</a></li>
<li><a href="https://www.utilitydive.com/news/grid-congestion-costs-transmission-gets-grid-strategies-report/687309/">US grid congestion costs jumped 56% to $20.8B in 2022... | Utility Dive</a></li>

</ul>
</details>

**标签**: `#electricity markets`, `#causal discovery`, `#renewable energy`, `#Texas power grid`, `#price formation`

---

<a id="item-14"></a>
## [用于期权定价中计划事件风险的非跨度识别协议](https://arxiv.org/abs/2606.12872) ⭐️ 8.0/10

论文提出了一种非跨度识别协议，将美联储 FOMC 决策、CPI 和 NFP 公告建模为风险中性期权定价中的确定时间跳跃，利用非跨度到期估计无事件波动率表面，用跨度到期报价校准计划跳跃，并在 2022 年 5 月至 2025 年 8 月的 SPX 期权上进行验证。 通过将计划宏观公告跳跃风险与连续波动率表面清晰分离，该协议提升了短期期权定价的准确性，为量化金融中的风险管理和模型校准提供了更清晰的信号。 实证结果表明，高斯跳跃和两成分混合跳跃在跨式和角落式期权上显著降低持有外定价误差，而受污染表面的压力测试证实将事件跨度报价纳入无事件拟合会吸收跳跃溢价而非识别它们；amortized MDN 基准显示跨事件迁移有限，对 CPI 和 FOMC 的识别最强，对 NFP 较弱。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 在期权定价中，诸如美联储 FOMC 会议、CPI 发布和 NFP 报告等计划宏观公告会在已知时间导致资产价格出现突跳。交易者通常从波动率表面推断此风险，但使用跨越事件的报价拟合的表面可能吸收跳跃溢价，导致跳跃成分无法被识别。本文通过提出一种利用非跨度到期隔离底层无事件表面的协议来解决此识别问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12872">Non-Spanning Identification of Scheduled Event Risk in Option Pricing</a></li>

</ul>
</details>

**标签**: `#option pricing`, `#quantitative finance`, `#jump diffusion`, `#event risk`, `#volatility surface`

---

<a id="item-15"></a>
## [动态配额交易市场中的交易摩擦](https://arxiv.org/abs/2606.03767) ⭐️ 8.0/10

本文提出了一种动态随机模型，用于包含慢速参与、有限中介和异质信息的配额交易市场，推导出均衡市场准入和交割月溢价的闭式表达，并使用 2005‑2021 年欧盟碳交易体系的 270 万条交易记录进行验证。 通过将多种摩擦统一到一个框架中并提供理论与实证双重验证，该研究揭示了市场不完善如何影响价格形成和排放交易方案的有效性，为政策制定者设计或改进碳市场提供了重要参考。 模型给出准入选择的闭式解，证明均衡溢价的唯一性，表明内生准入会削弱单一摩擦对价格的影响，而多种摩擦的相互作用可能是非加性的并放大价格波动；实证发现约 40%的运营商每年不进行交易，交易集中在 4 月且回报率系统偏高，运营商流动能够预测未来回报。

rss · arXiv Quantitative Finance · Jun 17, 04:00

**背景**: 配额交易（或排放交易）是一种基于市场的政策，通过设定总污染上限并允许企业买卖配额来为排放定价。欧盟碳交易体系（EU ETS）是全球最大的此类系统，涵盖发电厂、工厂以及自 2024 年起的海运 transport，合规期通常在每年 4 月结束。交易摩擦包括慢速参与（市场进入延迟）、有限中介（经纪人或中介的约束）以及异质信息（对未来价格的不同预期），这些因素可能扭曲配额价格并削弱市场纠正外部性的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.03767">[2606.03767] Trading Frictions in Dynamic Cap - and - Trade Markets</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Union_Emissions_Trading_System">European Union Emissions Trading System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emissions_trading">Emissions trading - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cap-and-trade`, `#environmental economics`, `#market frictions`, `#stochastic modeling`, `#EU ETS`

---