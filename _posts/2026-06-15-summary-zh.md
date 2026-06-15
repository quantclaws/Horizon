---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 31 items, 11 important content pieces were selected

---

1. [形式方法与编程的未来](#item-1) ⭐️ 8.0/10
2. [阿兰·佩利斯 1982 年编程格言在 Hacker News 重新引发讨论](#item-2) ⭐️ 8.0/10
3. [Gary Bernhardt 2014 年演讲预测 JavaScript 向编译目标转变](#item-3) ⭐️ 8.0/10
4. [AI 未能取代软件工程师，且不会取代](#item-4) ⭐️ 8.0/10
5. [基于英国生活满意度调查估算公众社会福利函数](#item-5) ⭐️ 8.0/10
6. [LANTERN 框架能够从不规则数据中建模健康状态转移。](#item-6) ⭐️ 8.0/10
7. [几何理论揭示 LLM 提案何时突破发现瓶颈](#item-7) ⭐️ 8.0/10
8. [量子计算对比特币和以太坊威胁的评估](#item-8) ⭐️ 8.0/10
9. [检测 LLM 经济预测中的前视偏差](#item-9) ⭐️ 8.0/10
10. [从期权中恢复风险中性矩](#item-10) ⭐️ 8.0/10
11. [利用 elicitability 和深度学习求解带共噪声的 McKean-Vlasov FBSDE](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [形式方法与编程的未来](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

一篇 Hacker News 帖子分享了 Jane Street 关于形式方法的博客，引发了关于证明技术、富有表现力的类型系统以及 AI 辅助编程中验证作用的讨论。 此次讨论凸显了形式验证如何提升 AI 生成代码的可靠性，并将开发者的重点从编写代码转向证明正确性。 评论者提到他们过去使用 Boyer-Moore 证明器的经验，利用 Scala 3 的富有表现力的类型进行编译时证明，以及担心 AI 生成的代码量超过了人工审查能力，从而增加了对自动验证的需求。

hackernews · eatonphil · Jun 14, 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式方法是一套用于严格指定、开发和验证软件及硬件系统的数学技术。富有表现力的类型系统（如依赖类型）能够将程序属性直接编码到类型中，由编译器进行检查。随着 AI 辅助编程的兴起，研究者正在探索大型语言模型如何帮助自动化证明生成，例如为验证语言创建循环不变式或证明脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://old.lemmy.sdf.org/post/3148821">The Dafny Programming and Verification Language ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dependent_type">Dependent type - Wikipedia</a></li>
<li><a href="https://roars.dev/pubs/doan2025ai.pdf">PDF AI-Assisted Autoformalization of Combinatorics Problems in Proof Assistants</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对讨论的深度表示赞赏，分享了他们在老式证明器和现代类型驱动验证方面的个人经验，而一些人则对形式规范相较于传统测试的开销持怀疑态度。还有人指出，AI 生成的代码增加了人工审查的负担，使得自动验证更具吸引力。

**标签**: `#formal-methods`, `#programming-languages`, `#verification`, `#type-systems`, `#AI-code-generation`

---

<a id="item-2"></a>
## [阿兰·佩利斯 1982 年编程格言在 Hacker News 重新引发讨论](https://www.cs.yale.edu/homes/perlis-alan/quotes.html) ⭐️ 8.0/10

该新闻分享了阿兰·佩利斯 1982 年的编程格言合集（称为 Perlisisms），引发了关于其今日相关性的讨论。 佩利斯的格言继续影响软件工程思维，提供永恒的见解，与现代主题如语言设计和 AI 驱动的代码生成产生共鸣。 该文本来源于 1982 年 9 月 ACM SIGPLAN 文章《编程中的格言》，包含诸如‘一种不影响你思考编程方式的语言不值得学习’等著名引用。

hackernews · tosh · Jun 14, 14:56 · [社区讨论](https://news.ycombinator.com/item?id=48527820)

**背景**: 阿兰·杰伊·佩利斯是美国计算机科学家，第一位图灵奖得主，以在编程语言领域的开创性工作而闻名。 《编程中的格言》文章发表于 1982 年 9 月的 ACM SIGPLAN 出版物，收录了关于编程和语言设计的简洁而发人深省的陈述。 这些格言在计算机文化中被广泛引用，因其机智和对编程实践的洞察而备受推崇。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://static.hlt.bme.hu/semantics/external/pages/John_McCarthy/en.wikipedia.org/wiki/Alan_Perlis.html">Alan Perlis - Wikipedia</a></li>
<li><a href="http://www.cs.yale.edu/homes/perlis-alan/quotes.html">Perlisisms - "Epigrams in Programming" by Alan J. Perlis</a></li>

</ul>
</details>

**社区讨论**: 评论者对佩利斯的机智表示赞赏，指出其中许多语录在当今话题如大型语言模型和语言设计中仍具 relevance。一些用户特别提到关于语言影响和低级编程的格言，而其他人则分享了相关媒体或个人项目，例如 perl.is 域名。讨论体现了对这些永恒格言的怀旧敬意以及持续的参与。

**标签**: `#programming`, `#quotes`, `#Alan Perlis`, `#software engineering`, `#wisdom`

---

<a id="item-3"></a>
## [Gary Bernhardt 2014 年演讲预测 JavaScript 向编译目标转变](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

在 2014 年的题为《JavaScript 的出生与死亡》的演讲中，Gary Bernhardt 回顾了语言的历史，并预测其将发展为 C/C++ 等语言的编译目标，并通过 TypeScript、Electron 等工具成为更广泛的应用平台。 该演讲的预测基本实现，asm.js、WebAssembly、TypeScript 和 Electron 的广泛采用表明 JavaScript 在现代软件开发中的持久影响。 Bernhardt 强调 asm.js 是早期的编译目标，后来被 WebAssembly 取代，并提到 TypeScript 提供更安全的 JavaScript，Electron 则让 Web 技术用于构建桌面应用。

hackernews · subset · Jun 14, 12:38 · [社区讨论](https://news.ycombinator.com/item?id=48526661)

**背景**: JavaScript 是一种最初用于网页交互的高级动态类型语言。asm.js 是 JavaScript 的一个严格子集，旨在让 C、C++ 等语言编译的代码在网页中达到接近原生的性能，作为早期的编译目标。WebAssembly 于 2015 年宣布、2019 年成为 W3C 标准，提供便携的二进制格式，取代 asm.js 成为网页及其他环境的编译目标。TypeScript 为 JavaScript 添加了静态类型，而 Electron 则让开发者能够把基于 Web 的应用打包成跨平台的桌面程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emscripten">Emscripten</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该演讲的前瞻性，指出 Bernhardt 预测 JavaScript 通过 asm.js 和 WebAssembly 成为编译目标、通过 Electron 用于桌面应用、通过 TypeScript 提供更安全编码的说法基本实现。有人幽默地提到他关于 2020‑2025 年全球灾难的玩笑预测，也有人指出不断出现所谓‘更好’的 JavaScript 最终又被转译回 JavaScript 的循环。总体而言，讨论体现了对该演讲持久相关性和深刻见解的赞赏。

**标签**: `#JavaScript`, `#WebAssembly`, `#TypeScript`, `#Talk`, `#Programming Languages`

---

<a id="item-4"></a>
## [AI 未能取代软件工程师，且不会取代](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

阿尔文·纳拉亚南和萨亚什·卡普尔的论文指出，包括纽约州首年 AI 披露 WARN 申报中未出现任何 AI 相关裁员的数据在内，目前的证据不支持 AI 会导致软件工程师大规模失业的说法。 通过表明即便是高度可自动化的软件工程职业也未出现 AI 驱动的裁员，该分析表明大多数其他职业可能更具韧性，为职业建议和关于 AI 对劳动力影响的政策讨论提供依据。 2025 年 3 月，纽约州在 WARN 法案申报中增加了 AI 披露复选框；首年超过 160 家公司提交通知，均未勾选 AI 框。作者指出三项阻碍自动化的瓶颈：决定/明确要构建什么、验证/对交付内容负责，以及进行这些任务所需的对代码库、业务和环境的深入人类理解。

rss · Simon Willison · Jun 14, 23:54

**背景**: WARN 法案要求雇主在大规模裁员或厂房关闭前提前 60 天通知员工。纽约州是美国首个在 WARN 申报中加入 AI 特定披露复选框的州，旨在追踪 AI 是否被列为裁员原因。软件工程不仅仅是编写代码，还包括会议、调试、需求规格说明和系统问责等任务，这些任务高度依赖人类判断和情境理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Worker_Adjustment_and_Retraining_Notification_Act_of_1988">Worker Adjustment and Retraining Notification Act of 1988 - Wikipedia</a></li>
<li><a href="https://www.bloomberg.com/news/newsletters/2025-06-12/new-york-state-updates-warn-notices-to-identify-layoffs-tied-to-ai">New York State Updates WARN Notices to Identify Layoffs Tied to AI</a></li>
<li><a href="https://www.softwareseni.com/why-ai-layoff-disclosure-laws-are-not-working-and-what-would-actually-fix-them/">Why AI Layoff Disclosure Laws Are Not Working and... - SoftwareSeni</a></li>

</ul>
</details>

**标签**: `#AI impact`, `#software engineering`, `#labor market`, `#technology policy`, `#future of work`

---

<a id="item-5"></a>
## [基于英国生活满意度调查估算公众社会福利函数](https://arxiv.org/abs/2606.13752) ⭐️ 8.0/10

该研究使用新颖的调查工具，基于英国代表性样本（N=2,068）估算了公众对生活满意度的社会福利函数。结果显示中位数弹性参数α=0.48，表明对福祉不平等有显著厌恶，福利函数大约等于个体效用平方根之和。 该研究为福祉导向的政策评估和成本效益分析提供了具有伦理基础的分配权重，连接了理论与实践。它展示了如何量化公众对不平等的偏好，以便在社会福利评估中使用。 中位数弹性参数 0.48 表明，提升最不满意者福祉一个单位的价值大约是提升最满意者福祉一个单位价值的两倍。调查工具通过生活满意度得分来 eliciting 公众对效用的偏好。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 社会福利函数将个体效用汇总为集体福祉的度量，常采用特定的函数形式，如弹性（或 Cobb‑Douglas）形式。弹性参数α决定不平等厌恶程度：α 越低，对提升最不福祉者的福祉越重视。主观福祉通过生活满意度调查测量，提供了基数效用的代理，可直接从公众偏好估算此类函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Social_welfare_function">Social welfare function - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/economics-econometrics-and-finance/social-welfare-function">Social Welfare Function - an overview | ScienceDirect Topics</a></li>
<li><a href="https://cep.lse.ac.uk/_new/publications/abstract.asp?index=12290">What is the public's social welfare function?</a></li>

</ul>
</details>

**标签**: `#social welfare`, `#subjective wellbeing`, `#inequality aversion`, `#survey methods`, `#public policy`

---

<a id="item-6"></a>
## [LANTERN 框架能够从不规则数据中建模健康状态转移。](https://arxiv.org/abs/2606.13880) ⭐️ 8.0/10

本文提出 LANTERN，一种纵向属性条件神经网络，能够从时间不规则的纵向健康数据中估计多状态健康转移概率，并为健康、轻度残疾、重度残疾和死亡四种状态提供校准的预测。 LANTERN 在校准和转移矩阵误差方面优于传统精算模型和机器学习基线，为残疾保险定价、准备金和偿付能力评估提供了更可靠的工具，尤其在健康观测不规则时。 LANTERN 根据个体健康史、观测间隔时间以及人口社会经济属性来条件化转移概率，按年龄和起始状态将个体预测聚合为精算转移矩阵，并在健康与退休研究数据上与逻辑回归、梯度提升树、循环神经网络和最后状态持续基准进行了比较。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 纵向健康数据常常伴随着观测时间不规则的情况，不同个体的随访间隔可能与健康状况相关，这给假设等间隔测量的传统模型带来挑战。传统精算多状态模型通常依赖马尔可夫、半马尔可夫或比例风险假设，在老化模式非线性和协变量历史异质时可能受限。属性条件神经网络通过在预测中加入外部协变量（如年龄、性别、社会经济状况）来扩展标准神经网络，从而在不规则的纵向数据中捕捉复杂的历史依赖模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.13880">A Longitudinal Attribute-Conditioned Neural Network for ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-022-26933-1">Longitudinal individual predictions from irregular repeated ... Analysis of longitudinal data with irregular observation times Longitudinal individual predictions from irregular repeated ... A Longitudinal Attribute-Conditioned Neural Network for ... Accommodating informative visit times for analysing irregular ... Longitudinal Data Analysis | Springer Nature Link Broken Stick Model for Irregular Longitudinal Data</a></li>
<li><a href="https://www.rgare.com/knowledge-center/article/multi-state-models-and-their-applications-in-(re)insurance">Multi-state Models and their Applications in (Re)insurance - RGA</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#health informatics`, `#actuarial science`, `#longitudinal data`, `#neural networks`

---

<a id="item-7"></a>
## [几何理论揭示 LLM 提案何时突破发现瓶颈](https://arxiv.org/abs/2606.14386) ⭐️ 8.0/10

该论文形式化了三个几何条件——谱压缩、正交逃逸出已探索子空间以及与目标的残余信号对齐——在这些条件下，LLM 生成的非局部假设能够提升混合发现系统的性能。作者在合成环境、大规模 A 股因子发现和符号回归基准上进行了验证。 通过将 LLM 引导的探索转化为诊断程序，该工作告诉从业者何时应该在非局部提案上花费计算预算，从而在科学发现流程中可能节省资源。该框架将几何理论与实际混合搜索相结合，对各领域的机器学习驱动研究具有影响。 这三个条件是在理论上推导出来的，并且被证明是混合优势的必要条件；实验表明，随机正交跳跃虽然能增加覆盖但若没有预测对齐则不会提升产出，且随着假设空间接近满秩，混合增益会消失。作者还提供了一个公开的表格操作 sanity check 来验证相关的预算分配含义。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 混合发现系统将结构化的局部搜索（如基于梯度或贪婪的探索）与能够跳远离当前假设子空间的 LLM 生成的非局部提案相结合。当新假设不再提供独立信息时，即使名义上的假设空间仍然很大，科学发现也会停滞——这种现象被称为发现瓶颈。论文从几何角度解释瓶颈：谱压缩衡量已探索子空间捕获的方差程度，正交逃逸量化了相对于该子空间的外部运动，而残余信号对齐则检查新方向是否与目标信号相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jmlr.org/papers/volume13/rubinstein12a/rubinstein12a.pdf">A Geometric Approach to Sample Compression</a></li>
<li><a href="https://www.emergentmind.com/topics/spectral-compression-family">Spectral Compression : Frameworks & Applications</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#scientific discovery`, `#large language models`, `#geometric theory`, `#hybrid search`

---

<a id="item-8"></a>
## [量子计算对比特币和以太坊威胁的评估](https://arxiv.org/abs/2606.14484) ⭐️ 8.0/10

该论文分析了 Shor's algorithm 如何破解比特币和以太坊的签名，而 Grover's algorithm 仅对工作量证明提供有限的二次加速，并估计到 2050 年出现能破解密码的量子计算机的概率约为 60%。 了解这些量子风险有助于区块链开发者优先迁移到后量子签名，并告诉政策制定者主要障碍是治理而非技术。 Shor's algorithm 威胁 secp256k1 上的 ECDSA 和 BLS12-381 上的 BLS 签名，而 Grover's algorithm 仅对挖矿提供二次加速，受故障 tolerant 成本和难度调整限制；蒙特卡洛预测给出双峰到达分布，2035 年约六分之一概率，2040 年约 30%，2050 年约 60%，且大多数暴露的币可迁移。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 量子计算机可以运行 Shor's algorithm 来分解大整数，从而破解椭圆曲线签名，如比特币使用的 ECDSA 和以太坊 2.0 使用的 BLS 签名，而 Grover's algorithm 仅对诸如工作量证明挖矿之类的暴力搜索提供二次加速。由于挖矿难度会自动调整，并且每次 Grover 操作都带来高故障 tolerant 开销，因此对比特币工作量证明的影响有限，而签名方案则直接面临威胁。该论文通过将硬件规模预测、专家调查和故障 tolerant 准备程度纳入蒙特卡洛模型，来估算出现能破解密码的量子计算机的时间。研究表明，虽然有相当数量的币面临风险，但大多数可以通过迁移到后量子签名方案得到保护，因而治理成为关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grover's_algorithm">Grover's algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BLS_digital_signature">BLS digital signature - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#blockchain security`, `#cryptocurrency`, `#post‑quantum cryptography`, `#risk assessment`

---

<a id="item-9"></a>
## [检测 LLM 经济预测中的前视偏差](https://arxiv.org/abs/2512.23847) ⭐️ 8.0/10

该论文提出了一种名为 Lookahead Propensity（LAP）的统计量，通过仅使用日期的召回查询估计 LLM 内化未来信息的概率，从而检测 LLM 生成的经济预测中的前视偏差。该方法被应用于新闻标题预测股票收益和财报电话会议记录预测资本支出两项任务。 提供一种成本低效的诊断工具来检测前视偏差，有助于从业者评估基于 LLM 的预测可靠性，这对金融决策和确保 AI 模型不会无意泄漏未来数据至关重要。该方法凸显了 LLM 在预测任务中训练数据污染的普遍问题。 LAP 通过对公司‑日期对仅使用日期的提示查询 LLM，并测量该提示出现在其训练数据中的可能性来估计；在样本内期间 LAP 显著为正，而在模型训练数据截止后几乎降至零。回归中 LAP 与预测准确率的显著正交互表明存在前视偏差污染，论文中的两项应用表明大约 37%的明显预测效应是由记忆放大的。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 前视偏差是指模型在预测时无意中使用了当时不可获得的信息，从而虚高其表现。大型语言模型在训练时会吸收大量文本，其中可能包含未来日期的经济数据、新闻或报告，因此在被要求进行预测时，模型可能会“记住”这些实际结果。这种污染从输入本身难以察觉，因而需要像 LAP 这样的统计代理来估计训练数据的重叠程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.23847">A Test of Lookahead Bias in LLM Forecasts</a></li>
<li><a href="https://www.emergentmind.com/topics/lookahead-propensity-lap">Lookahead Propensity in Estimation & LLMs</a></li>
<li><a href="https://connect.cfauk.org/discussion/llms-research-lookahead-bias-for-prediction-tasks">LLMs Research - Lookahead Bias for Prediction Tasks | Technology...</a></li>

</ul>
</details>

**标签**: `#LLM bias detection`, `#economic forecasting`, `#lookahead bias`, `#machine learning`, `#statistical testing`

---

<a id="item-10"></a>
## [从期权中恢复风险中性矩](https://arxiv.org/abs/2601.14852) ⭐️ 8.0/10

本文提出了一种投影估计器，利用观察到的期权组合来近似多资产收益，从而在不完整市场中提取风险中性依赖。将该方法应用于瑞士国家银行两次意外的 EUR/CHF 底价公告，结果表明依赖解释了联合崩溃概率变化的约三分之二。 提供一种可操作的方法来衡量风险中性依赖，能够改善期权定价、风险管理以及评估政策对多资产市场的影响。有限样本误差界还为估计器的可靠性提供了实际指导。 该估计器通过构建期权组合来近似两种或多种基础资产的收益函数，推导出有限样本误差界，并利用 SNB 公告进行验证，结果显示依赖变化解释了联合崩溃概率变化的约 66%。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: 风险中性矩总结了在风险中性度量下资产价格的分布，传统上通过 Carr–Madan 公式等方法从期权价格中提取。在不完整市场中，由于无法完全复制所有收益，仅凭期权数据估计多资产之间的依赖关系具有挑战性。该投影估计器通过构建交易期权的组合来近似多资产收益函数，从而能够推断依赖关系并提供有限样本误差界。该方法建立在将风险中性累积量与随机波动率模型中的潜在因素关联的文献基础上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.14852">[2601.14852] Beyond Carr Madan: A Projection Approach to Risk-Neutral Moment Estimation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Risk-neutral_measure">Risk-neutral measure - Wikipedia</a></li>
<li><a href="https://www.snb.ch/en/the-snb/mandates-goals/monetary-policy/decisions">The SNB’s monetary policy decisions | Swiss National Bank</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#options pricing`, `#risk-neutral moments`, `#financial econometrics`, `#econometric estimation`

---

<a id="item-11"></a>
## [利用 elicitability 和深度学习求解带共噪声的 McKean-Vlasov FBSDE](https://arxiv.org/abs/2512.14967) ⭐️ 8.0/10

作者提出了一种结合 Picard 迭代、elicitatility 和深度学习的新型数值方法，用于近似求解带共噪声的 McKean-Vlasov 前向-后向随机微分方程，并在一个银行间借贷系统性风险模型上进行了验证。 该方法免去了昂贵的嵌套蒙特卡罗模拟，为求解高维均值场随机系统提供了高效且可扩展的工具，直接适用于系统性风险建模和均值场博弈。 均值场交互项通过一个在可 elicitatility 得分上最小化的循环神经网络参数化，而后向过程则由一个代表解耦场的混合前馈-循环网络近似；该算法在具有已知解析解的模型上进行测试，扩展到量化中介的交互，并应用于非平稳的 Aiyagari-Bewley-Huggett 经济增长模型。

rss · arXiv Quantitative Finance · Jun 15, 04:00

**背景**: McKean-Vlasov 前向-后向随机微分方程（MV-FBSDEs）描述了其动态依赖于状态自身分布的系统，常见于均值场博弈和金融建模。共噪声是所有代理共享的不确定性来源，增加了分析复杂性，需要诸如 Malliavin 可微性等专门技术。elicitatility 指的是某些统计泛函（如均值、分位数）可以表示为适当得分函数的唯一最小化器，这使得可以基于机器学习构建路径 wise 损失函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://carmona.princeton.edu/document/351">[PDF] FORWARD-BACKWARD STOCHASTIC DIFFERENTIAL EQUATIONS AND CONTROLLED MCKEAN VLASOV DYNAMICSS The purpose of this paper is to provid - Princeton University</a></li>
<li><a href="https://ai.stanford.edu/~shoham/www+papers/SIGECOM2008-elicitability.pdf">PDF Eliciting Properties of Probability Distributions: the Highlights</a></li>
<li><a href="https://www.researchgate.net/publication/396095149_Malliavin_differentiability_of_McKean-Vlasov_SDEs_with_common_noise">(PDF) Malliavin differentiability of McKean-Vlasov SDEs with common noise</a></li>

</ul>
</details>

**标签**: `#deep learning`, `#McKean-Vlasov FBSDE`, `#elicitiability`, `#stochastic differential equations`, `#systemic risk`

---