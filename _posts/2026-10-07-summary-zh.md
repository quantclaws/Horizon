---
layout: default
title: "Horizon Summary: 2026-10-07 (ZH)"
date: 2026-10-07
lang: zh
---

> From 61 items, 14 important content pieces were selected

---

1. [OpenAI 分享 AI 生成的开放数学问题证明](#item-1) ⭐️ 9.0/10
2. [Mistral 发布 1 万亿参数 Mistral Large 4 预览版](#item-2) ⭐️ 9.0/10
3. [Polars 发布 py-2.0.0，包含破坏性更改和性能优化](#item-3) ⭐️ 8.0/10
4. [谷歌发布 EmbeddingGemma 2，一个开放轻量的多模态嵌入模型](#item-4) ⭐️ 8.0/10
5. [AnyPS5：在不使用模拟的情况下将 PS5 二进制文件移植到 PC（系统库映射率 87%）](#item-5) ⭐️ 8.0/10
6. [考虑评审偏差后揭示 AI 面试代理可靠性提升](#item-6) ⭐️ 8.0/10
7. [基于状态依赖霍克斯过程的连续日内电力市场制度转移建模](#item-7) ⭐️ 8.0/10
8. [专家验证的 AI 学习材料提升成绩并缩小大学经济课的达成差距](#item-8) ⭐️ 8.0/10
9. [WRAP：非平稳市场中的深度对冲漂移感知对抗训练](#item-9) ⭐️ 8.0/10
10. [Understanding Interfirm AI Talent Flow Networks through Online Professional Profiles](#item-10) ⭐️ 8.0/10
11. [拥堵感知推荐提升纽约高中匹配结果](#item-11) ⭐️ 8.0/10
12. [Data-driven measures of high-frequency trading](#item-12) ⭐️ 8.0/10
13. [Dyson-Schwinger 有效作用方法用于粗波动：用于校准、异期权和风险的关联-响应架构](#item-13) ⭐️ 8.0/10
14. [Lévy 过程的信息几何及其在金融模型中的应用](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 分享 AI 生成的开放数学问题证明](https://openai.com/index/sharing-ai-progress-in-mathematics/) ⭐️ 9.0/10

OpenAI 宣布其内部前沿 AI 模型已为多个长期悬而未决的数学问题生成机器检验的证明，其中包括 Barnette 猜想，并将结果及 Lean 形式化代码发布在其 GitHub 仓库 openai/math 上。 这表明先进的 AI 能够参与解决深奥的数学猜想，有可能改变数学家进行证明工作的方式，并加速图论和组合数学等领域的研究。 该仓库包含证明 Barnette 猜想（问题 180）的预印本以及相应的 Lean 证明脚本，表明 AI 生成的证明经过形式化验证。

hackernews · OfficialTurkey · Oct 6, 22:17 · [社区讨论](https://news.ycombinator.com/item?id=49984923)

**背景**: Barnette 猜想提出于 1969 年，断言每个 3‑连通二分立方平面图都包含一个哈密顿环，尽管经过广泛研究，该猜想至今仍未被证明。自动定理证明利用计算机程序推导数学证明，而 Lean 等证明助手能够机械检验 AI 生成推导的正确性。OpenAI 在现有数学基准测试饱和后，将其内部前沿模型用于开放研究问题的评估，从而产生了此次共享的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Barnette's_conjecture">Barnette's conjecture - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://github.com/openai/math">GitHub - openai/math</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 Barnette 猜想的个人联系，有人回顾了数十年的努力并对看到证明感到惊讶。其他人指出证明的易懂性，并认为 AI 有望协助解决其他长期悬而未决的问题，虽然也有人警告其重要性可能不如独特游戏猜想等问题。

**标签**: `#AI`, `#mathematics`, `#theorem proving`, `#OpenAI`, `#Barnette's conjecture`

---

<a id="item-2"></a>
## [Mistral 发布 1 万亿参数 Mistral Large 4 预览版](https://simonwillison.net/2026/Oct/6/le-chonk/) ⭐️ 9.0/10

Mistral 发布了 Mistral Large 4 的预览版，这是一个具有 1 万亿总参数、490 亿活跃参数的模型，在 3,800 块 NVIDIA Grace Blackwell GPU 上训练，并承诺在本月底发布开放权重。 此次公告表明模型规模和性能迈出重要一步，使 Mistral 接近大语言模型的前沿，并承诺提供开放权重的万亿参数模型。 该模型仅通过 API 支持两种推理级别——“none”和“high”，在 Artificial Analysis 上得分 38（落后于 DeepSeek 4.1 Flash），高推理下输出 2,717 个 token，而无推理下为 3,275 个 token。

rss · Simon Willison · Oct 6, 20:18

**背景**: Mistral 之前的旗舰模型 Mistral Large 3 在同一基准上仅得 9 分，说明此次能力提升显著。该模型的 490 亿活跃参数体现了混合专家（MoE）设计，即每个 token 只使用 1 万亿总参数中的一部分，从而提高效率。在 NVIDIA Grace Blackwell GPU 上训练利用了 Blackwell 架构的增强 NVLink 和保密计算，以支持巨大的 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-sg/data-center/technologies/blackwell-architecture/">NVIDIA Blackwell : GPU Architecture for Generative AI & HPC | NVIDIA</a></li>
<li><a href="https://0xbenzo.dev/blog/understanding-model-parameters/">Understanding Model Parameters: Total Parameters vs Active ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出推理设置奇怪——高推理产生的输出 token 反而比无推理少，但 pelican 图像更好。一些人强调了模型在视觉和网络安全基准上的强势表现，认为它可能成为顶级防御模型；其他人则强调其在欧盟训练和推理方面的主权意义。

**标签**: `#Mistral`, `#Large Language Model`, `#AI`, `#GPU training`, `#open weights`

---

<a id="item-3"></a>
## [Polars 发布 py-2.0.0，包含破坏性更改和性能优化](https://github.com/pola-rs/polars/releases/tag/py-2.0.0) ⭐️ 8.0/10

Polars 版本 py-2.0.0 引入了破坏性更改，例如在分组行上运行 SQL 窗口函数、将 Parquet ENUM 类型读取为 pl.String，以及废弃 cut/qcut，同时带来了大量跨连接、分组和 I/O 路径的性能提升。 作为广泛使用的 Polars 库的主要版本更新，此次发布通过提供性能提升影响数据工程工作流，同时要求用户适应破坏性 API 更改的代码。 关键更改包括在 SQL 窗口函数中在投影前评估 QUALIFY、将 Parquet ENUM 列视为 pl.String、允许确定性表达式插件选择加入 CSE/CSPE，以及性能调整如修改连接哈希表布局、流式外核排序以及改进 Iceberg 和 Lance 的下推过滤器。

github · github-actions[bot] · Oct 6, 11:52

**背景**: Polars 是一种用 Rust 实现并在 Python 中提供 API 的快速 DataFrame 库，提供惰性和即时执行以进行数据操作任务。它常被用作 pandas 的替代品，用于大规模数据处理，因为其列式内存架构和并行性。像 2.0.0 这样的主要版本更新通常会引入破坏性更改，以提升性能和 API 一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pola.rs/api/python/stable/reference/sql/clauses.html">Query Clauses — Polars documentation</a></li>
<li><a href="https://github.com/pola-rs/polars/issues/29165">Expression plugins lost CSE in 1.41 with no way to ... - GitHub</a></li>
<li><a href="https://kimbodo.com/why-polars-2-0s-performance-and-parquet-changes-matter-for-production-python-data-stacks/">Why Polars 2.0’s Performance and Parquet ... | Kimbodo AI Research</a></li>

</ul>
</details>

**标签**: `#polars`, `#python`, `#dataframe`, `#release`, `#performance`

---

<a id="item-4"></a>
## [谷歌发布 EmbeddingGemma 2，一个开放轻量的多模态嵌入模型](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) ⭐️ 8.0/10

谷歌宣布发布 EmbeddingGemma 2，这是一个基于 Apache 2.0 许可证的开放权重多模态嵌入模型，专为大规模文本和视觉嵌入任务设计，具有轻量和高效的特点。 通过提供开放且宽松许可的模型，EmbeddingGemma 2 减少了供应商锁定，使开发者能够在设备上或大规模运行多模态嵌入，用于语义搜索、RAG 和跨模态检索等应用。 该模型包含 2.7 亿参数的文本编码器、1.7 亿参数的视觉编码器和 3 亿参数的音频编码器（总计约 7.4 亿参数），将输入映射到统一的 768 维空间，支持 8K 上下文窗口和 100+ 种语言，并采用 Apache 2.0 许可证发布。

hackernews · ilreb · Oct 6, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49980487)

**背景**: 多模态嵌入模型将文本、图像、音频和视频等不同模态的数据映射到共享的向量空间，使语义相似的项目在空间中更接近。Gemma 系列是谷歌的一套开放权重语言模型，EmbeddingGemma 2 在 Gemma 4 的基础上加入了视觉和音频模态，同时保持模型规模在 10 亿参数以下。该模型采用 Apache 2.0 许可证发布，允许免费使用、修改和再分发，这对于需要存储数百万向量的嵌入工作负载尤为重要。这种方式支持设备端部署，降低对专有、仅托管的嵌入 API 的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/">EmbeddingGemma 2: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/">EmbeddingGemma 2 is a best-in-class open model for natively ...</a></li>
<li><a href="https://unsloth.ai/docs/models/embeddinggemma-2">EmbeddingGemma 2 - Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Apache 2.0 许可证能够避免在需要存储数百万向量的嵌入工作负载中出现供应商锁定。他们强调该模型适用于多模态 “Jev‑like” 任务，如同时处理文本和图像，并指出其适度的规模（文本 2.7 亿 + 视觉 1.7 亿 + 音频 3 亿 ≈ 7.4 亿参数）是一个实际优势。还有评论者注意到该发布中提到了谷歌的趋势决策 API，暗示其用途不仅限于纯嵌入。

**标签**: `#embedding`, `#multimodal`, `#open-source`, `#Google`, `#AI/ML`

---

<a id="item-5"></a>
## [AnyPS5：在不使用模拟的情况下将 PS5 二进制文件移植到 PC（系统库映射率 87%）](https://github.com/boykopovar/AnyPS5) ⭐️ 8.0/10

开源的 AnyPS5 项目将 PlayStation 5 可执行文件重新链接为原生 Windows/Linux 二进制文件，并重新实现了主机的系统库，在不使用任何模拟层的情况下实现了 87% 的库兼容性。 通过使 PS5 游戏能够在 PC 上原生运行，该项目可能减少对重量级模拟器的依赖，简化保存工作，并引发关于主机到 PC 移植的法律和行业问题。 AnyPS5 包含一个重新链接器，可将 PS5 ELF 可执行文件转换为主机的原生格式，并提供重新实现的 PRX 系统库以供动态链接，报道称已映射了 87% 的主机系统库。

hackernews · Fe2O3 · Oct 6, 23:28 · [社区讨论](https://news.ycombinator.com/item?id=49985664)

**背景**: PlayStation 5 游戏以依赖主机操作系统提供的专有系统库（PRX）的 ELF 二进制形式发布。传统模拟会复制整个 CPU 和硬件，而二进制翻译则在替换这些库后将可执行文件重新链接以直接在宿主操作系统上运行。AnyPS5 采用后者，旨在避免完整模拟带来的性能开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/boykopovar/AnyPS5">GitHub - boykopovar/AnyPS5: Tool for automatic PS5 ...</a></li>
<li><a href="https://www.techpowerup.com/353098/anyps5-project-skips-emulation-entirely-aims-to-port-playstation-5-games-to-pc-directly">AnyPS5 Project Skips Emulation Entirely, Aims to Port ...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏该技术成就及其对抗供应商锁定的潜力，但警告这可能会索尼推向仅云游戏，并带来类似 Yuzu 和 Ryujinx 的法律下架风险。有人开玩笑说即将推出的作品如 GTA 6 会立即有 PC 移植版，也有人质疑如果游戏能够当天被破解，对软件行业会产生什么影响。

**标签**: `#reverse-engineering`, `#PS5`, `#gaming`, `#PC-port`, `#system-libraries`

---

<a id="item-6"></a>
## [考虑评审偏差后揭示 AI 面试代理可靠性提升](https://arxiv.org/abs/2610.07003) ⭐️ 8.0/10

该研究考察了已部署语音‑视频面试 AI 代理的 2,611 条评分规则评分的生产访谈，在考虑评审者严格程度和漂移后发现，可靠性从 2026 年 3 月到 8 月提升了 0.53 个标准差。研究还发现可靠性随记录的部署而变化，且面试相关的支持工单相较于技术问题工单每月下降约 10%。 考虑评审者效应和漂移对于获得 AI 代理性能的可信纵向测量至关重要，可避免对改进或退化得出误导性结论。该研究提供了一种实用框架——评审者之间的可比性、漂移下的证据时效性以及与运营结果的 corroboration——供依赖重复人工评估的企业评估已部署 AI 系统时使用。 两位评审者对同一批次的评分严格程度相差 0.79 个标准差，且评审者组成的变化使原始可靠性趋势变平。在校正评审严格程度和漂移后，可靠性从 2026 年 3 月到 8 月提升了 0.53 个标准差，预测不确定度在约五周后达到最大部署对比的幅度，面试相关支持工单相较于技术问题工单每月下降约 10%。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: 公司通常通过收集重复的人工评分来评估已部署的 AI 代理，但得分变化可能反映评审者严格程度、漂移或代理自身的变化。将可靠性建模为潜在状态有助于将真实性能变化与测量噪声分离，尤其是在评审者组合随时间变化时。诸如严格程度调整（来源于医疗保险风险调整等领域）和潜在状态空间建模等方法可以得到可比较且已校正漂移的可靠性估计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.07003">[2610.07003] Reliability of AI Agents : Rater Effects , Drift, and the...</a></li>
<li><a href="https://sk.sagepub.com/ency/edvol/healthservices/chpt/severity-adjustment">Severity Adjustment</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0951832026005442">Reliability evaluation of highly reliable multi-state systems ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#evaluation`, `#rater bias`, `#reliability`, `#human-in-the-loop`

---

<a id="item-7"></a>
## [基于状态依赖霍克斯过程的连续日内电力市场制度转移建模](https://arxiv.org/abs/2610.08169) ⭐️ 8.0/10

本文提出了一种基于新提出的流动性压力指数的多维状态依赖霍克斯过程模型，以捕捉欧洲日内电力市场的制度转换订单流动态。该模型使用了 2024 年 1 月至 3 月 EPEX SPOT 荷兰日内跨境小时订单数据进行校准。 通过将订单流强度与流动性压力挂钩，该模型为衡量市场压力和预测短期价格波动提供了更真实的工具，对应对可再生能源驱动波动的交易者、风险经理和量化分析师具有重要价值。它还展示了依赖制度的点过程如何改善能源市场的微观结构建模。 流动性压力指数由买卖价差、订单簿成交量和中间价波动率组成；模型识别出三种流动性状态，表明订单流具有强烈的自激特性且接近临界点，成交主要触发同方向订单而跨方向影响较弱。稳健性检验表明三状态模型优于两状态，而单一状态霍克斯过程的拟合效果显著较差。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: 霍克斯过程是一种自激点过程，过去的事件会增加未来事件发生的可能性，常用于建模限价订单簿中的订单流。状态依赖霍克斯过程在此基础上扩展，使得激励核心可以根据底层市场状态过程而变化，该状态过程可以在事件发生时切换。在欧洲日内电力市场中，可再生能源渗透率的提升导致波动加剧和流动性压力增加，因而需要诸如流动性压力指数之类的综合指标，以买卖价差、订单簿成交量和中间价波动率来衡量压力。将状态依赖霍克斯过程与该指数相结合，能够捕捉在不同流动性条件下的制度特定订单流动态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/1809.08060">State - dependent Hawkes processes and their application to limit...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2405851326000218">Quantifying electricity market stress: Constructing and ...</a></li>
<li><a href="https://www.researchgate.net/publication/327835452_State-dependent_Hawkes_processes_and_their_application_to_limit_order_book_modelling">State - dependent Hawkes processes and their application to limit...</a></li>

</ul>
</details>

**标签**: `#Hawkes process`, `#electricity markets`, `#regime shifts`, `#liquidity stress index`, `#intraday trading`

---

<a id="item-8"></a>
## [专家验证的 AI 学习材料提升成绩并缩小大学经济课的达成差距](https://arxiv.org/abs/2610.07097) ⭐️ 8.0/10

在一年级大学经济课程中，一半学生获得了由源头基础模型生成并由具名研究生助教验证的 AI 生成播客、常见问题和测验学习指南。 该研究表明，将 AI 输出的判断负担从学生转移到专家验证者可以改善学习效果，特别是对表现较差的学生，并缩小成就差距。 干预使用源头基础（RAG）模型生成材料，随后由具名研究生助教审核；分析采用了两个队列的差分‑差分设计，涉及 170 名学生和 340 道考试分数。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: 源头基础 AI 模型（常称为 RAG 或 AI 笔记本）仅从用户提供的文档中检索信息来生成输出，从而减少幻觉并提高可信度。差分‑差分是一种准实验方法，通过比较处理组和控制组随时间的变化来推断因果影响。在英国荣誉学位制度中，上二等荣誉（2:1）通常对应 60%‑69%的分数范围，是学术成就的重要基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.endorphindigital.com/post/what-are-source-grounded-ai-models-how-to-use-them-in-your-business">What Are Source - Grounded AI Models & How to Use Them in Your...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>
<li><a href="https://www.theacademicpapers.co.uk/blog/2026/10/03/uk-degree-classifications/">UK Degree Classifications Explained: First, 2 :1, 2 : 2</a></li>

</ul>
</details>

**标签**: `#AI in Education`, `#Expert Verification`, `#Learning Gains`, `#Generative AI`, `#Higher Education`

---

<a id="item-9"></a>
## [WRAP：非平稳市场中的深度对冲漂移感知对抗训练](https://arxiv.org/abs/2610.07162) ⭐️ 8.0/10

本文提出 WRAP（Wasserstein-重扰动对抗扰动），一种用于非平稳市场深度对冲的漂移感知对抗训练方法，采用包含 Wasserstein 和φ-发散约束的两预算分布鲁棒优化框架。在 Heston 动态和广义仿射扩散上的实验表明，该方法在非平稳条件下提升了鲁棒性。 WRAP 为在随时间变化的市场动态中对冲金融衍生品提供了一种 principled 的方法，解决了现有深度对冲方法假设平稳性的关键限制。其结合重加权和传输扰动的方式有望改进风险管理实践，并推动金融机器学习中更多分布鲁棒优化方法的发展。 该方法通过一阶展开将轨迹重加权（对冲损失的离散度）和路径传输（损失对扰动的敏感度）的影响分离，从而得到可求解的有限维对抗攻击。它通过在加权经验参考分布上设定固定基线权重，以平衡采样不确定性与时间漂移。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: 深度对冲利用机器学习从历史或模拟的市场路径中学习最优交易策略，假设这些路径能代表未来状况。在非平稳市场中，底层数据分布会随时间变化，导致历史轨迹难以用于训练。分布鲁棒优化（DRO）通过在由 Wasserstein 距离和φ‑发散等约束定义的模糊集内寻找最坏情况分布来对抗这种不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.14757v2">Distributional Adversarial Attacks and Training in Deep Hedging</a></li>
<li><a href="https://arxiv.org/pdf/2412.20708">Two-Stage Distributionally Robust Optimization: Intuitive ...</a></li>
<li><a href="https://arxiv.org/pdf/2309.03791v3">Optimal Transport Regularized Divergences: Application to ...</a></li>

</ul>
</details>

**标签**: `#adversarial training`, `#deep hedging`, `#nonstationary markets`, `#distributionally robust optimization`, `#Wasserstein`

---

<a id="item-10"></a>
## [Understanding Interfirm AI Talent Flow Networks through Online Professional Profiles](https://arxiv.org/abs/2610.08264) ⭐️ 8.0/10

Analyzes global AI talent mobility networks from 2010-2022, showing increasing concentration among leading firms but a contestable core, and links network centrality to higher firm value beyond size and assets.

rss · arXiv Quantitative Finance · Oct 7, 04:00

**标签**: `#AI talent mobility`, `#labor network analysis`, `#firm value`, `#empirical study`, `#network centrality`

---

<a id="item-11"></a>
## [拥堵感知推荐提升纽约高中匹配结果](https://arxiv.org/abs/2610.08275) ⭐️ 8.0/10

该论文正式化了纽约高中匹配中的推荐诱导拥堵现象，表明天真的推荐会显著降低录取率，尤其是对附近选择较少的申请者。随后提出并在 2025‑26 学年招生周期中测试了一种拥堵感知的 bilevel optimize‑and‑simulate 方法，结果显示推荐项目的排名率提高了 57%，匹配率提高了 71%。 通过将推荐视为市场塑造干预，该工作提供了一种减少容量受限匹配市场（如学校选择）中算法差异的原则性方法。其见解可提升教育、劳动力和其他集中市场中推荐系统的公平性与效率。 该 bilevel optimize‑and‑simulate 方法通过分配推荐来避免热门项目被过度加载；在随机对照试验中，16.4% 的处理组申请者排名了推荐项目，而对照组为 10.5%（p=0.011），且有 5.6% 匹配到推荐项目，对照组为 3.3%（p=0.071），并且没有任何处理组申请者被推荐项目拒绝。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: 推荐系统帮助用户在大型市场中导航，但当许多用户被引导至同一容量有限的项目时，可能会引发拥堵，从而降低匹配率。纽约高中匹配是一个集中式的容量受限市场，学生在此排名学校并通过延迟接受算法进行分配。 bilevel 优化建模了层次决策，上层分配推荐，下层模拟由此产生的匹配均衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.08275v1">Personalized Recommendations Without Inducing Congestion ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bilevel_optimization">Bilevel optimization - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2308.09516.pdf">ReCon: Reducing Congestion in Job Recommendation using ...</a></li>

</ul>
</details>

**标签**: `#recommendation systems`, `#matching markets`, `#algorithmic fairness`, `#congestion`, `#education policy`

---

<a id="item-12"></a>
## [Data-driven measures of high-frequency trading](https://arxiv.org/abs/2405.08101) ⭐️ 8.0/10

The authors develop machine learning models to measure liquidity-supplying and liquidity-demanding high-frequency trading activity for all U.S. stocks from 2010 to 2023, showing these measures outperform standard proxies and generalize across markets.

rss · arXiv Quantitative Finance · Oct 7, 04:00

**标签**: `#high-frequency trading`, `#market microstructure`, `#machine learning`, `#financial econometrics`, `#market quality`

---

<a id="item-13"></a>
## [Dyson-Schwinger 有效作用方法用于粗波动：用于校准、异期权和风险的关联-响应架构](https://arxiv.org/abs/2609.37741) ⭐️ 8.0/10

本文提出了一种基于量子场论中两粒子不可约（2PI）有效作用和 Dyson-Schwinger 间隙方程的非摄动框架，用于随机波动期权定价。通过自洽高斯近似，将定价误差降低了 20‑130 倍，达到 0.01‑0.11 bp 的水平。 该方法将量子场论技术引入定量金融，实现了快速的确定性校准，并显著提升了粗波动模型在异期权和风险管理中的定价精度。其误差降至 0.01‑0.11 bp，可与蒙特卡洛基准竞争，有望在交易台和研究中得到更广泛应用。 在指数‑OU 情况下，该方法使 Hartree 误差降低 20‑130 倍至 0.01‑0.11 bp，在 H=0.07、ρ=‑0.9 的粗 Bergomi 模型下与蒙特卡洛参考结果吻合；在 72 个网格点、到期十年的 SABR 模型中定价误差为 0.97 bp（优于 Hagan 展开的 75 bp）。条件于波动场，远期起点微笑和连续监控障碍简化为场上的积分，因果响应块通过一次伴随收缩得到冲击 vega 曲线。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: 粗波动模型通过低赫斯特指数 H 的 Volterra 过程捕捉资产波动率观测到的粗糙、分形特征，这使得传统扰动方法在校准和定价上困难重重。两粒子不可约（2PI）有效作用是量子场论中的非摄动形式，能够通过 Dyson‑Schwinger 间隙方程自洽地重新求和传播子。将这一框架引入金融问题，可得到由稳定性条件确定的高斯近似，从而在短时间、小波动‑of‑vol regime 之外实现准确的期权定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.37741">[2609.37741] Dyson-Schwinger Effective-Action Methods for ...</a></li>
<li><a href="https://www.emergentmind.com/topics/two-particle-irreducible-effective-action">2PI Effective Action in Field Theory - emergentmind.com</a></li>
<li><a href="https://link.springer.com/book/10.1007/978-3-032-26576-0">Volterra Volatility Models: Option Pricing and Hedging ...</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#stochastic volatility`, `#rough volatility`, `#Dyson-Schwinger equations`, `#option pricing`

---

<a id="item-14"></a>
## [Lévy 过程的信息几何及其在金融模型中的应用](https://arxiv.org/abs/2507.23646) ⭐️ 8.0/10

该论文直接从 Lévy 过程的 Lévy 三元组推导出α-散度、Fisher 信息矩阵和α-连接，并在 tempered stable、CGMY、方差伽马和 Merton 模型上演示了该框架。 通过为 Lévy-based 金融模型提供信息几何视角，该工作使得在定量金融中可以实现更好的统计推断、偏差减少以及贝叶斯预测先验的构建。 α-散度被表达为由漂移、高斯系数和 Lévy 测度构成的 Lévy 三元组的函数；从该表达式导出 Fisher 信息度量和双连接，进而得到势函数，使得 Lévy 过程的指数族具有双平坦结构。

rss · arXiv Quantitative Finance · Oct 7, 04:00

**背景**: Lévy 过程是具有平稳独立增量的连续时间随机过程，包括布朗运动、泊松过程以及金融中广泛使用的许多跳跃驱动模型。信息几何为概率分布的流形赋予微分几何结构，使用α-散度等度量来衡量相似性并定义度量和连接。本文通过直接从 Lévy 三元组导出这些量，将信息几何方法推广到 Lévy 过程，从而将抽象的信息几何工具与 tempered stable、CGMY、方差伽马和 Merton 等具体金融模型联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lévy_process">Lévy process - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2507.23646">Information geometry of Lévy processes and financial models</a></li>
<li><a href="https://www.linkedin.com/posts/barbaresco_information-geometry-of-levy-processes-and-activity-7415670060473909248-owE1">Information geometry of levy processes and...</a></li>

</ul>
</details>

**标签**: `#information geometry`, `#Lévy processes`, `#financial modeling`, `#stochastic processes`, `#α-divergence`

---