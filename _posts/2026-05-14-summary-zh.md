---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 39 items, 5 important content pieces were selected

---

1. [作者将个人仓库从 GitHub 迁移到自托管 Forgejo](#item-1) ⭐️ 8.0/10
2. [作者将个人数字栈迁移到欧洲云服务提供商](#item-2) ⭐️ 8.0/10
3. [深度学习框架用于定价带有重置和赎回条款的可转换债券](#item-3) ⭐️ 8.0/10
4. [GeomHerd 利用 Ricci 曲率在 LLM 模拟市场中预测 herd 行为](#item-4) ⭐️ 8.0/10
5. [贝叶斯动态建模实现波动率用于金融资产价格预测](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [作者将个人仓库从 GitHub 迁移到自托管 Forgejo](https://jorijn.com/en/blog/leaving-github-for-forgejo/) ⭐️ 8.0/10

作者描述将个人 Git 仓库从 GitHub 迁移到自托管的 Forgejo 实例，阐述了去中心化和对 AI 抓取器的担忧等动机，并提及了社区反馈。 这一举动体现了对代码托管去中心化的日益关注，并凸显了 ActivityPub 等联邦化努力在减少对中心化平台依赖方面的相关性。 Forgejo 是一个轻量级的自托管 Git 代码托管平台，正积极通过 ActivityPub 的 ForgeFed 扩展实现联邦化，作者还提到使用 GitSocial 保留社交图谱和镜像等工具。

hackernews · jorijn · May 13, 12:54 · [社区讨论](https://news.ycombinator.com/item?id=48121266)

**背景**: GitHub 是一个广泛使用的集中式平台，用于托管 Git 仓库，提供问题跟踪、拉取请求和 CI/CD 集成等功能。Forgejo 是 Gitea 的社区驱动分支，旨在提供轻量级的自托管 Git 服务，可在个人硬件上运行或通过 Docker 部署。自托管使个人能够掌控自己的数据并避免依赖第三方服务，而像 ActivityPub 这样的联邦协议旨在实现不同代码托管平台之间的互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forgejo.org/faq/">Forgejo FAQ | Forgejo – Beyond coding. We forge.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://antoniosarro.dev/blogs/forgejo-homelab">Self - Hosted Git with Forgejo : Your Own GitHub Alternative in Docker</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了回归 Git 去中心化根源的愿望，批评了围绕 GitHub 的工具集中化，并强调了 Forgejo 中联邦化支持的重要性。一些人担心 AI 抓取器会消耗自托管内容并需要进行阻拦，而另一些人则称赞如 GitSocial 之类的工具能够保留社交图谱，并鼓励捐款以加速联邦化的发展。

**标签**: `#GitHub`, `#Forgejo`, `#self-hosting`, `#decentralization`, `#federation`

---

<a id="item-2"></a>
## [作者将个人数字栈迁移到欧洲云服务提供商](https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/) ⭐️ 8.0/10

作者将个人数字基础设施迁移到欧洲服务提供商，阐述了动机、挑战以及他们为实现跨区域高可用性而构建的 Terraform 配置。 此举凸显了对数据主权、欧盟法规（如 GDPR 和 CLOUD Act）日益增长的担忧，并展示了开发者如何通过多元化基础设施降低对美国云服务的依赖。 作者利用 Terraform 构建了跨提供商、跨区域的高可用性架构，将 Cloudflare 映射到 Bunny CDN，并使用 OVHcloud、Hetzner 等欧盟本地提供商的裸金属和托管服务。

hackernews · monokai_nl · May 13, 11:42 · [社区讨论](https://news.ycombinator.com/item?id=48120629)

**背景**: 欧洲的数据主权工作在 GDPR 以及 Schrems II 等裁决的推动下，要求个人和组织的数据必须存储在欧盟内部，以避免受到如美国 CLOUD Act 等法律的域外访问。OVHcloud 和 Hetzner 等提供商的数据中心完全位于欧洲，并具备符合性认证，使其成为注重主权的工作负载的理想选择。Terraform 常用于定义跨区域、多提供商的架构，以满足高可用性和灾难恢复需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hivenet.com/post/understanding-european-tech-sovereignty-challenges-and-opportunities">Understanding European Tech Sovereignty : Challenges and...</a></li>
<li><a href="https://gartsolutions.com/ovh-vs-hetzner/">OVH vs Hetzner: Which European CloudProvider Wins? - Gart</a></li>
<li><a href="https://foggykitchen.com/2025/09/20/oci-data-guard-terraform/">OCI Data Guard Terraform : Cross - Region Setup (2025 Guide)</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到欧盟政府官员越来越要求服务完全在欧盟内部托管，这反映出数据本地化压力的增加。虽然许多人称赞此举带来多元化和更好的隐私，但也有人警告欧洲并非绝对的避风港，指出可能的 VPN 限制以及与美国的持续合作，暗示地域转移可能只是用一套风险换取另一套。

**标签**: `#data sovereignty`, `#cloud infrastructure`, `#EU regulations`, `#DevOps`, `#digital migration`

---

<a id="item-3"></a>
## [深度学习框架用于定价带有重置和赎回条款的可转换债券](https://arxiv.org/abs/2605.12189) ⭐️ 8.0/10

本文提出一种基于深度学习的框架，通过将估值建模为路径依赖偏微分方程并用神经网络逼近条件期望，来定价具有下行转换价格重置和发行人赎回条款的可转换债券。 该方法为定价复杂路径依赖特征的可转换债券提供了高效且灵活的工具，对量化金融和机器学习社区具有重要意义，能够提升广泛使用证券的定价准确性。 研究在地几何布朗运动、常数弹性方差和 Heston 随机波动三种基础动态下推导了一致的路径依赖偏微分方程，并在中国中信银行可转换债券上的实证测试表明框架产生稳定准确的价格和敏感度；三个关键经济洞察表明合同特征主导价值、赎回条款削减上行收益、下行重置意外降低价格。

rss · arXiv Quantitative Finance · May 13, 04:00

**背景**: 可转换债券是一种混合证券，可以按预定比例转换为发行公司的股票。当债券包含路径依赖特征（如下行转换价格重置和发行人赎回条款）时，其估值变得复杂，因为这些特征取决于基础股票价格的历史路径。路径依赖偏微分方程（PPDE）通过将债券价值条件化于基础资产的完整历史以及不断变化的转换价格来捕捉这种依赖关系。滚动窗口触发规则根据最近一段时间内的价格变动来决定这些合同特征何时被激活。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12189">[2605.12189] A deep learning approach for pricing convertible bonds with path-dependent reset and call provisions</a></li>
<li><a href="https://www.investopedia.com/terms/c/convertiblebond.asp">investopedia.com/terms/c/convertiblebond.asp</a></li>
<li><a href="https://scispace.com/pdf/a-neural-rde-based-model-for-solving-path-dependent-pdes-2ef6q6tk.pdf">A Neural RDE-based model for solving path - dependent PDEs</a></li>

</ul>
</details>

**标签**: `#deep learning`, `#convertible bonds`, `#pricing`, `#path‑dependent PDE`, `#financial engineering`

---

<a id="item-4"></a>
## [GeomHerd 利用 Ricci 曲率在 LLM 模拟市场中预测 herd 行为](https://arxiv.org/abs/2605.11645) ⭐️ 8.0/10

本文提出 GeomHerd，一种前瞻性框架，通过在 LLM 驱动的多智能体模拟生成的代理交互图上计算离散 Ollivier--Ricci 曲率，在 herd 行为影响市场回报之前量化 herd 行为。实验表明，探测器在顺参数 onset 前中位数提前 272 步触发，传染探测器在 318 步前召回 65% 的关键轨迹。 GeomHerd 提供了系统性风险的早期预警信号，克服了传统价格相关方法的滞后性，并提供了一种可融入风险监控系统的几何替代方案。其提前预测 herd 行为的能力有助于监管者和交易者在损失发生前降低市场脆弱性。 该方法在动作图上跟踪离散 Ollivier--Ricci 曲率，建立到经典 CSAD herd 统计量的均场桥梁，并指出在级联过程中代理行为的有效词汇会收缩。基于曲率的预测头相较于探测器条件和仅价格基线降低了级联窗口对数回报 MAE。

rss · arXiv Quantitative Finance · May 13, 04:00

**背景**: 当代理人行为趋同时会发生 herd 行为，放大市场脆弱性；传统度量依赖于价格相关性，仅在其影响回报后才检测到协调。Ollivier--Ricci 曲率度量图上概率质量的发散或聚合，提供局部网络拓扑的几何代理。Cividino--Sornette 连续自旋代理基质作为测试平台，通过 n 维 Ising 模型模拟带有噪声交易者 herd 行为的金融市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ricci_curvature">Ricci curvature - Wikipedia</a></li>
<li><a href="https://doi.org/10.2139/ssrn.3960979">Multi-asset financial bubbles in an agent-based model with noise traders’ herding described by an n-vector Ising model by Davide Cividino, Rebecca Westphal, Didier Sornette :: SSRN</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S000187081930369X">Ollivier Ricci curvature for general graph Laplacians: Heat ...</a></li>

</ul>
</details>

**标签**: `#herding detection`, `#Ricci curvature`, `#agent-based simulation`, `#LLM multi-agent`, `#financial systemic risk`

---

<a id="item-5"></a>
## [贝叶斯动态建模实现波动率用于金融资产价格预测](https://arxiv.org/abs/2605.12099) ⭐️ 8.0/10

本文提出了一类新的贝叶斯动态模型，将动态伽马过程用于实现波动率，与传统的贝叶斯动态线性模型（DLMs）结合，以利用高频内日数据改善股票收益预测。 通过将实现波动率代理纳入条件 DLMs 来捕捉波动率杠杆和反馈效应，该模型在 S&P 板块 ETF 上的实证验证展示了方法学创新，有望提升定量金融的预测能力和风险管理。 该模型使用共轭形式的动态伽马过程建模实现波动率，并与价格序列的贝叶斯 DLMs 相结合，便于顺序滤波、计算开销甚小以及基于模拟的预测；在 S&P 板块 ETF 上的实证表明相较于标准模型预测精度有所提升。

rss · arXiv Quantitative Finance · May 13, 04:00

**背景**: 贝叶斯动态线性模型（DLM）是一种状态空间模型，采用修改后的卡尔曼滤波器和折扣技术，在时间上更新线性高斯关系以进行时间序列预测。伽马过程是一种非递减的 Lévy 过程，常用于建模正值量如实现波动率，能够捕捉其跳跃和连续累积。实现波动率是通过高频内日收益计算得到的可观测代理，表现出杠杆效应——负收益往往比同幅度的正收益导致更大的波动率增加。这种不对称的波动率动态对于准确预测和风险建模非常重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pydlm.github.io/pydlm_user_guide.html">Dynamic linear models — user manual — PyDLM 0.1.1.13 documentation</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/full/10.1002/fut.22241">Forecasting realized volatility: The role of implied volatility, leverage effect, overnight returns, and volatility of realized volatility - Kambouroudis - 2021 - Journal of Futures Markets - Wiley Online Library</a></li>
<li><a href="https://arxiv.org/abs/2605.12099">[2605.12099] Bayesian Dynamic Modeling of Realized Volatility in Financial Asset Price Forecasting</a></li>

</ul>
</details>

**标签**: `#Bayesian statistics`, `#financial econometrics`, `#realized volatility`, `#dynamic linear models`, `#time series forecasting`

---