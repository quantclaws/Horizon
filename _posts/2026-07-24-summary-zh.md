---
layout: default
title: "Horizon Summary: 2026-07-24 (ZH)"
date: 2026-07-24
lang: zh
---

> From 38 items, 12 important content pieces were selected

---

1. [初创公司创始人呼吁美国政府不要禁止中国开放权重 AI 模型](#item-1) ⭐️ 8.0/10
2. [软件工厂为何在缺乏人工监督时会失败](#item-2) ⭐️ 8.0/10
3. [500 行 C++教程从零构建软件渲染器](#item-3) ⭐️ 8.0/10
4. [LearnOpenGL：全面的现代 OpenGL 教程资源](#item-4) ⭐️ 8.0/10
5. [DARPA 与美国空军试飞 AI 控制的 F-16。](#item-5) ⭐️ 8.0/10
6. [天文学家发现棕矮星周候系外卫星](#item-6) ⭐️ 8.0/10
7. [PyPI 禁止向超过 14 天的旧版本上传新文件](#item-7) ⭐️ 8.0/10
8. [供应链中联合企业失败导致的非线性系统性风险放大](#item-8) ⭐️ 8.0/10
9. [通量修正对角青蛙方案实现无条件正性和二阶精度。](#item-9) ⭐️ 8.0/10
10. [多层嵌套模拟使 CVA‑VaR 计算成本降低 1000 倍](#item-10) ⭐️ 8.0/10
11. [Reconstructing Large Scale Production Networks](#item-11) ⭐️ 8.0/10
12. [AI 自动化呈现潮汐上涨而非冲击波模式](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [初创公司创始人呼吁美国政府不要禁止中国开放权重 AI 模型](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992) ⭐️ 8.0/10

2026 年 7 月 22 日，一群初创公司创始人通过 Little Tech 发布信件，敦促美国政府不要禁止中国开放权重 AI 模型，称此禁令将阻碍创新且缺乏法律依据。 此事的结果可能塑造全球 AI 格局，影响初创公司竞争力、中美科技竞争，并为政府如何监管开放权重模型与专有 AI 设定先例。 该信件托管于 littletech.org 并链接至 Politico 的 PDF，指出禁止中国模型无法阻止滥用、无法阻止蒸馏，且可能仅违反服务条款而非知识产权法。

hackernews · theanonymousone · Jul 23, 15:18 · [社区讨论](https://news.ycombinator.com/item?id=49023016)

**背景**: 开放权重 AI 模型使得训练得到的参数（权重和偏差）公开可用，任何人都可以下载、运行和微调模型，而无需访问训练代码。中国公司如 DeepSeek、百度等已发布具有竞争力的开放权重模型，在性能上逐步缩小与美国前沿系统的差距，同时提供更低的成本。美国政府在中美科技竞争的背景下曾考虑对这些模型施加限制，理由涉及知识产权和国家安全。与开源软件不同，开放权重模型不要求公开训练代码或数据，因而涉及不同的法律和许可问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you've been told - Open Source Initiative</a></li>
<li><a href="https://www.csis.org/analysis/what-know-about-chinese-ai-models">What to Know About Chinese AI Models - CSIS</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weight-vs-source-everything-you-need-know-max-brodeur-urbas-rdnrc">Open weight vs open source : Everything you need to know</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑禁止中国模型的理由，指出恶意行为者会无视法律，禁令无法阻止蒸馏，且美国模型本身也在未经许可的情况下使用公开数据。一些人认为任何禁令在全球范围内难以执行，因为欧洲或其他地区的用户可以下载并向美国用户提供中国模型，法律挑战更可能集中在服务条款违反而非知识产权盗用。整体情绪对禁令的效果持怀疑态度，强调需要更清晰的法律框架而非限制性措施。

**标签**: `#AI policy`, `#open-weight models`, `#US-China tech competition`, `#startup advocacy`, `#AI regulation`

---

<a id="item-2"></a>
## [软件工厂为何在缺乏人工监督时会失败](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md) ⭐️ 8.0/10

humanlayer 仓库的文章指出，仅依赖 AI 编码代理的软件工厂在缺乏人工监督时会失败，强调需要理解用户意图并保持代码质量。文章还提到 2025 年 7 月的一次“全灯离线”实验，完全自动化的生产效果不佳。 这一观点对日益增长的完全自主 AI 驱动开发趋势提出挑战，提醒团队人工判断仍是将自动化与业务目标对齐、确保软件可靠性的关键。它影响开发者、工程经理以及投资 AI 编码代理的组织。 文章提出了“意图‑实现‑质量”问题，指出 AI 代理能够根据一句需求实现代码，却无法产生背后的人类意图，而理解代码库仍需人类速度的认知。同时强调 harness engineering 是塑造代理运行环境的必要实践。

hackernews · dhorthy · Jul 23, 15:18 · [社区讨论](https://news.ycombinator.com/item?id=49023019)

**背景**: 软件工厂将制造业原则应用于软件开发，通过标准化组件和自动化流程高效地生产产品变体。AI 编码代理是能够进行规划、编码、测试和决策的自主系统，在最少人工干预的情况下利用自然语言理解和程序合成。Harness engineering 是 Mitchell Hashimoto 在 2026 年初提出的概念，指设计代理运行的完整环境（如工具、检查和反馈回路），以确保其有效性和安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software_factory">Software factory - Wikipedia</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-are-ai-coding-agents">What Is an AI Coding Agent? How They Work and When to Use Them | MindStudio</a></li>
<li><a href="https://martinfowler.com/articles/harness-engineering.html">Harness engineering for coding agent users</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意，缺乏人工检查的‘暗工厂’会遗漏细微问题，许多人指出意图‑实现‑质量的差距以及需要人类速度来理解代码库。也有人持混合态度，承认 AI 的有用性，但强调监督和 harness 改进仍然至关重要。

**标签**: `#software engineering`, `#AI coding agents`, `#software factories`, `#automation`, `#developer productivity`

---

<a id="item-3"></a>
## [500 行 C++教程从零构建软件渲染器](https://haqr.eu/tinyrenderer/) ⭐️ 8.0/10

haqr.eu/tinyrenderer/ 上的教程提供了约 500 行的裸 C++ 实现，逐步引导读者构建软件渲染器，涵盖三角形光栅化、z‑buffer 和透视投影。 通过将核心图形概念浓缩到简洁易读的代码中，该教程降低了学习者掌握图形流水线基础的门槛，并激发动手实验的兴趣。 该实现仅使用标准 C++ 且不依赖外部图形库，实现了软件 z‑buffer 进行隐藏面消除，并手动推导透视投影矩阵以将三维坐标映射到二维屏幕空间。

hackernews · mpweiher · Jul 23, 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49022038)

**背景**: 软件渲染指的是仅使用 CPU 在没有 GPU 加速的情况下生成图像，其流程与硬件图形流水线相同：顶点变换、光栅化和片元处理。z‑buffer（深度缓冲区）为每个像素存储深度信息，以正确解决三角形重叠问题。透视投影通过根据距离缩放坐标来实现三维到二维的映射，从而模拟景深效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Graphics_pipeline">Graphics pipeline - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Z-buffering">Z-buffering - Wikipedia</a></li>
<li><a href="https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/building-basic-perspective-projection-matrix.html">Building a Basic Perspective Projection Matrix - Scratchapixel</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该教程清晰且富有教育价值，有人分享了他们移植到 Rust 并添加了着色器等功能的经验。多位用户指出教程未涉及三角形裁剪，认为这是实际渲染器必须面对的重要环节。还有人怀旧软件渲染，并提到 Foley‑Van Dam 等经典书籍作为补充资料。

**标签**: `#software rendering`, `#C++`, `#computer graphics`, `#tutorial`, `#HackerNews`

---

<a id="item-4"></a>
## [LearnOpenGL：全面的现代 OpenGL 教程资源](https://learnopengl.com/) ⭐️ 8.0/10

LearnOpenGL.com 教程站点被突出展示为学习 Modern OpenGL 的全面、社区认可的资源，获得了强烈好评和高社区参与度。 它作为图形编程新手的首选参考，帮助他们掌握核心渲染概念，这些概念是游戏开发、图形研究和 GPU 计算的基础。 该教程使用现代核心配置 OpenGL 讲解基础、中级和高级主题，包括着色器编程和 Hello Triangle 示例，并常得到社区建议去探索 Sokol 或 SDL‑GPU 等工具。

hackernews · ibobev · Jul 23, 14:53 · [社区讨论](https://news.ycombinator.com/item?id=49022634)

**背景**: OpenGL 是一种跨语言、跨平台的渲染 2D 和 3D 向量图形的 API，由 Khronos Group 管理。现代 OpenGL 指的是核心配置版本，它移除了已弃用的固定功能特性，强调可编程着色器和图形管线。图形管线通过顶点着色、曲面细分、几何着色、光栅化和片段着色等阶段处理顶点数据，以生成最终像素。如 LearnOpenGL 这样的学习资源通过动手示例教授这一管线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenGL">OpenGL - Wikipedia</a></li>
<li><a href="https://learnopengl.com/">Learn OpenGL, extensive tutorial resource for learning Modern OpenGL</a></li>
<li><a href="https://learnopengl.com/Getting-started/Hello-Triangle">LearnOpenGL - Hello Triangle</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞 LearnOpenGL 是图形编程的必备指南，敦促新手通过完成所有示例来掌握渲染基础。许多评论指出，掌握 OpenGL 后可以进一步学习诸如 CUDA 之类的低级 GPU 工作，而另一些则建议先从软件渲染器入手，或尝试使用 Sokol、SDL‑GPU 等更高层次的封装进行实际项目。

**标签**: `#OpenGL`, `#graphics programming`, `#tutorial`, `#computer graphics`, `#learning resource`

---

<a id="item-5"></a>
## [DARPA 与美国空军试飞 AI 控制的 F-16。](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16) ⭐️ 8.0/10

DARPA 和美国空军进行了 AI 控制的 F-16 飞行试验，飞行员可通过开关在人工控制与 AI 控制之间切换，以进行安全实验。 此次演示表明将自主 AI 融入战斗航空迈出重要一步，有望减轻飞行员工作负担并实现新的空战战术。 AI 算法在目视范围内的空战对抗中与有人驾驶的 F-16 进行测试，采用新型界面使飞行员可通过翻转开关放弃或恢复控制。

hackernews · r2sk5t · Jul 23, 13:51 · [社区讨论](https://news.ycombinator.com/item?id=49021597)

**背景**: DARPA 的空战演进（ACE）计划旨在开发能够自主执行空对空作战机动的 AI 算法，同时通过人工监督保证安全。该计划研究人机协同界面，使飞行员能够在手动和自动控制之间切换，以实现“人在回路”方式。此外，自适应神经网络飞行控制系统正被研究，以便 F-16 能根据损伤或飞行条件变化重新配置其控制面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://defensemirror.com/news/36591">DARPA Announces First-Ever AI - Controlled F - 16 In- Air Combat Tests</a></li>
<li><a href="https://www.nationalacademies.org/projects/DBASSE-BOHSI-21-02/publication/26355">Human-AI Teaming: State-of-the-Art and Research Needs 2022</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2405896315009404">Development of a Nonlinear Reconfigurable F-16 Model and Flight Control Systems Using Multilayer Adaptive Neural Networks - ScienceDirect</a></li>

</ul>
</details>

**社区讨论**: 社区反应普遍持怀疑和幽默的态度，部分评论者将 AI 控制的 F-16 与天网（Skynet）相比较，并质疑人工突然接管的安全性。还有人认为这不过是一架昂贵的无人机，并指出飞机的生命支持系统和飞行员承受的 G 力限制。总体而言，讨论既表现出技术兴趣，也暴露了对可靠性和成本的担忧。

**标签**: `#AI`, `#defense`, `#fighter jet`, `#DARPA`, `#autonomous systems`

---

<a id="item-6"></a>
## [天文学家发现棕矮星周候系外卫星](https://www.eso.org/public/news/eso2610/) ⭐️ 8.0/10

天文学家利用欧洲南方天文台的观测数据，发现一颗候选系外卫星围绕棕矮星 CD-35 2722 b 运行，这可能是首次确认的系外卫星发现。 确认系外卫星的存在将有助于理解次恒星天体周围的卫星形成过程，并扩展已知行星系统的多样性。 该候选卫星被称为 CD-35 2722 b I，围绕棕矮星 CD-35 2722 b 运行，距离较近，且该系统挑战了传统的行星-卫星定义。

hackernews · MarcoDewey · Jul 23, 14:02 · [社区讨论](https://news.ycombinator.com/item?id=49021783)

**背景**: 系外卫星是指围绕系外行星或其他非恒星外太天体运行的自然卫星，尽管已有许多候选者，但至今尚未有确认的发现。棕矮星是质量约为 13 到 80 倍木星质量的次恒星天体，质量不足以维持氢聚变，但能进行氘和锂的聚变，主要发射红外光。由于信号易被宿主天体的亮度掩盖，检测系外卫星需要高精度光度测量或时变方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exomoon">Exomoon</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brown_dwarf">Brown dwarf</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一潜在发现表示赞赏，但指出艺术想象图不准确地描绘了棕矮星和候选卫星的大小。一些人就该天体应称为系外卫星还是系外行星展开讨论，因为棕矮星的性质介于行星和恒星之间；另一些人则强调了智利黑暗天空对观测的有利条件。还有少数无关评论提到了网站的微小格式问题。

**标签**: `#astronomy`, `#exoplanets`, `#exomoon`, `#brown dwarf`, `#ESO`

---

<a id="item-7"></a>
## [PyPI 禁止向超过 14 天的旧版本上传新文件](https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything) ⭐️ 8.0/10

PyPI 已实施限制，拒绝向发布时间超过 14 天的旧版本上传新文件，正如 Seth Larson 在 PyPI 博客所宣布的。 此举通过阻止攻击者在获取发布令牌后毒害长期稳定版本来缓解供应链攻击，保护所有 Python 包维护者和用户。 该限制仅对超过 14 天的旧版本生效，通过 Warehouse 拉取请求 #19727 实施；目前尚未被利用，但可阻断可行的攻击途径。

rss · Simon Willison · Jul 23, 04:50

**背景**: Python 包索引（PyPI）是官方的 Python 包仓库，由 Warehouse Web 应用提供支持。包维护者通常使用长期有效的 API 令牌上传新版本，一旦令牌被泄露，攻击者可无限期利用它。供应链攻击常通过毒害已有版本向下游用户分发恶意代码。通过仅允许向最近的版本上传新文件，PyPI 大幅缩小了此类基于令牌的攻击窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://warehouse.pypa.io/">Warehouse Developer Documentation</a></li>
<li><a href="https://docs.pypi.org/trusted-publishers/">Getting Started - PyPI Docs</a></li>
<li><a href="https://github.com/pypi/warehouse">GitHub - pypi/warehouse: The Python Package Index · GitHub</a></li>

</ul>
</details>

**标签**: `#python`, `#packaging`, `#supply-chain`, `#security`, `#pypi`

---

<a id="item-8"></a>
## [供应链中联合企业失败导致的非线性系统性风险放大](https://arxiv.org/abs/2607.20068) ⭐️ 8.0/10

研究人员利用厄瓜多尔的企业级供应链数据发现，多家企业同时失败可使系统性风险放大至单个失败风险之和的 257 倍，远超线性预期。 这凸显了隐藏的系统性脆弱性，表明影响多家企业的事件（如自然灾害或战争）可能引发不成比例的大规模经济中断，为风险管理和政策提供重要参考。 仅有 0.14%的企业对表现出超过四倍的放大效应；研究者提出了一种简单方法来识别这些风险组合，并将其归因于供应商可替代性的破裂。

rss · arXiv Quantitative Finance · Jul 23, 04:00

**背景**: 供应链中的系统性风险源于一家企业的失败通过相互依赖的买卖关系引发级联失败。最近的进展使得能够重建国家层面的企业级供应链网络，从而量化单个和组合失败的影响。厄瓜多尔详细的税收记录提供了 2012 年至 2022 年近乎完整的正式交易视图，使其成为研究非线性风险放大的独特案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csh.ac.at/events/firm-level-resilience-and-shock-propagation-in-production-networks-after-the-2016-ecuador-earthquake/">Firm - Level Resilience And Shock Propagation In Production Networks ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666449625000684">Exploring cascading failures in supply chain risk management: A systematic review, 2013-2024 - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#systemic risk`, `#supply chain networks`, `#complexity science`, `#network science`, `#economic resilience`

---

<a id="item-9"></a>
## [通量修正对角青蛙方案实现无条件正性和二阶精度。](https://arxiv.org/abs/2607.20415) ⭐️ 8.0/10

论文提出了通量修正对角青蛙（FCDF）方案，将二阶方向算子分解为单调的 M-矩阵核心和反扩散通量，然后在隐式带求解器中迭代应用 Zalesak 型限制器，以实现 Fokker-Planck 方程的无条件正性、二阶精度和确切的质量守恒。 通过突破 Godunov 定律限制线性二阶方案无法保持正性的障碍，FCDF 方法在不受严格时间步长限制的情况下实现了 Fokker-Planck 方程的鲁棒、精确求解，对数值偏微分方程从业者及相关领域具有重要意义。 该方案采用 M-矩阵核心保证单调性，加入仅在未解析层激活的 Zalesak 型通量限制器，在对流步长限制下使用收缩的 Picard 迭代，进一步通过仅与正性绑定节点数量相关的半光滑牛顿方法求解的主动集重新表述，并采用缺陷修正的时间步进恢复二阶时间精度。

rss · arXiv Quantitative Finance · Jul 23, 04:00

**背景**: Fokker-Planck 方程描述概率密度的演化，广泛用于随机过程和统计物理，其数值求解需要保持解的非负性以避免非物理的负值。Godunov 定理表明，线性二阶有限差分格局无法同时达到二阶精度和正性保持，这促使研究者提出对角青蛙（DF）框架以实现最终的正性，但仅在施加严格的最小时间步长条件下才有效。本文通过在 DF 框架中引入非线性通量修正策略，消除了时间步长限制，同时保持二阶空间精度和质量的 Exact 守恒。

**标签**: `#numerical analysis`, `#Fokker-Planck equation`, `#positivity-preserving schemes`, `#flux correction`, `#Diagonal Frog`

---

<a id="item-10"></a>
## [多层嵌套模拟使 CVA‑VaR 计算成本降低 1000 倍](https://arxiv.org/abs/2301.05886) ⭐️ 8.0/10

该论文提出了一种基于多层嵌套模拟的层次估计器，用于高效计算信用估值调整的风险价值（CVA‑VaR），相比标准蒙特卡洛方法将计算复杂度降低了三个数量级。 此方法大幅降低了金融机构进行衍生品风险计算的计算成本，使得实时或高频的 CVA‑VaR 评估成为可能，对银行风险管理和监管报告具有重要影响。 研究利用了最近在概率多层嵌套模拟方面的进展，构造了处理三重嵌套期望的层次估计器，表明在给定误差容忍度下所需样本数从 O(ε⁻²)降至约 O(ε⁻²/³)，实现约 1000 倍的加速。

rss · arXiv Quantitative Finance · Jul 23, 04:00

**背景**: 信用估值调整（CVA）是衡量场外衍生品因交易对手违约而产生的信用风险的市场价格，其风险价值（VaR）通常需要计算三重嵌套期望。传统蒙特卡洛方法在处理多层嵌套期望时效率低下，计算成本随所需精度呈二次增长。多层嵌套模拟通过在不同细化层次上结合粗糙和精细样本，能够将这种复杂度降低数个数量级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2301.05886">Ecient Risk Estimation for the Credit Valuation Adjustment</a></li>
<li><a href="https://ryanoconnellfinance.com/credit-valuation-adjustment/">Credit Valuation Adjustment (CVA): Formula, Example, and XVA ...</a></li>
<li><a href="https://www.emergentmind.com/topics/nested-risk-evaluation">Nested Risk Evaluation: A Multilayer Approach</a></li>

</ul>
</details>

**标签**: `#Monte Carlo simulation`, `#Credit Valuation Adjustment`, `#Multilevel methods`, `#Financial risk management`, `#Quantitative finance`

---

<a id="item-11"></a>
## [Reconstructing Large Scale Production Networks](https://arxiv.org/abs/2512.02362) ⭐️ 8.0/10

The authors present a method to reconstruct national-scale weighted firm-to-firm networks using sectoral input-output tables and firm size distributions, validated on the US and several other countries.

rss · arXiv Quantitative Finance · Jul 23, 04:00

**标签**: `#network reconstruction`, `#input-output tables`, `#firm-to-firm networks`, `#economic networks`, `#computational economics`

---

<a id="item-12"></a>
## [AI 自动化呈现潮汐上涨而非冲击波模式](https://arxiv.org/abs/2604.01363) ⭐️ 8.0/10

该研究分析了超过 17,000 份来自 3,000 项 O*NET 衍生的文本任务的工人评估，发现 AI 自动化呈现潮汐上涨模式，AI 在 2024 年第二季度完成相当于人类 3‑4 小时工作的任务成功率约为 50%，到 2025 年第三季度升至约 65%。 由于潮汐上涨模式意味着 AI 能力的逐步、广泛提升，AI 对文本相关岗位的影响将在数年内逐步显现，这为企业和政策制定者提供了比突发冲击波情景更长的适应时间。 如果当前的增长趋势持续，到 2029 年大型语言模型在大多数文本相关任务上的平均成功率预计将达到 80‑95%，而达到近乎完美的表现仍需数年；该研究还与 METR 此前的冲击波假设形成对比。

rss · arXiv Quantitative Finance · Jul 23, 04:00

**背景**: O*NET 是美国劳工部的职业信息网络，用于对数千项工作任务进行分类，为 LLM 评估提供了一套标准化的文本活动。METR 是一个研究非营利组织，负责测量 AI 系统何时可能造成灾难性危害，并曾提出 AI 进步可能以突发的“冲击波”形式出现。冲击波与潮汐上涨框架将 AI 能力的突然、局部激增与在众多任务上平稳、广泛的提升进行对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.01363">Crashing Waves vs . Rising Tides : Preliminary Findings on AI ...</a></li>
<li><a href="https://metr.org/">METR</a></li>
<li><a href="https://techxplore.com/news/2026-04-tides-overturning-prior-views-ai.html">Crashing waves vs . rising tides : Overturning prior views about how...</a></li>

</ul>
</details>

**标签**: `#AI automation`, `#labor market`, `#large language models`, `#O*NET`, `#task evaluation`

---