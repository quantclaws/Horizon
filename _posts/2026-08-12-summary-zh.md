---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> From 63 items, 12 important content pieces were selected

---

1. [压缩与预测在本质上是等价的](#item-1) ⭐️ 8.0/10
2. [研究人员从专有 LLM API 窃取推理轨迹](#item-2) ⭐️ 8.0/10
3. [英国交通警察将实时人脸识别试点扩展至伦敦地铁站](#item-3) ⭐️ 8.0/10
4. [形式化 conformal 预测中的信息间隙](#item-4) ⭐️ 8.0/10
5. [LLM 代理在供应链谈判中展现出能力驱动的效率和分配偏差](#item-5) ⭐️ 8.0/10
6. [具有防篡改日志的自适应生成式 AI 遥测框架](#item-6) ⭐️ 8.0/10
7. [联合李雅普诺夫证书实现多智能体生成式 AI 的零知识治理](#item-7) ⭐️ 8.0/10
8. [数据分割导致 AI 在定价博弈中暗中串通](#item-8) ⭐️ 8.0/10
9. [ParlayMarket 提出用于联合合约的统一流动性池自动做市商](#item-9) ⭐️ 8.0/10
10. [扩展状态依赖霍克斯过程模拟限价单簿动态](#item-10) ⭐️ 8.0/10
11. [只有当人类准确感知 AI 能力时，AI 扩展才能提升人机团队表现](#item-11) ⭐️ 8.0/10
12. [论文提出金融领域智能体 AI 的四层治理框架](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [压缩与预测在本质上是等价的](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

ngrok 博客文章认为数据压缩和预测在本质上是等价的过程，解释高效压缩依赖于对数据模式的预测，这一概念源于信息论和机器学习。 这一见解统一了信息论、机器学习和人工智能的概念，表明理解压缩可以带来更好的预测模型和更智能的系统，对数据效率和人工智能发展具有重要意义。 文章通过 Kolmogorov 复杂度、归一化压缩距离（NCD）和基于部分匹配的预测（PPM）等概念，将压缩与预测联系起来，强调压缩通过建模和预测数据模式来实现。

hackernews · nikolay · Aug 11, 19:49 · [社区讨论](https://news.ycombinator.com/item?id=49263497)

**背景**: 在信息论中，数据压缩通过使用更少的位来编码信息以减少冗余，而预测则涉及基于过去模式预测未来的数据点。Kolmogorov 复杂度衡量数据的内在复杂性，定义为能生成该数据的最短程序的长度，从而将可压缩性与可预测性联系起来。这些思想为理解学习和智能如何可能从类似压缩的过程中形成提供了理论基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov_complexity">Kolmogorov complexity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_compression">Data compression - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了压缩与预测之间的细微差别，指出等价性仅在训练数据完全代表未来分布时成立；一些人引用了剑桥大学的课程、Grant Sanderson 的视频以及 PPM 和 Kolmogorov 复杂度等相关概念，而其他人则认为压缩更多是关于抽象，而解压缩则涉及外推。

**标签**: `#information theory`, `#machine learning`, `#data compression`, `#prediction`, `#Kolmogorov complexity`

---

<a id="item-2"></a>
## [研究人员从专有 LLM API 窃取推理轨迹](https://stolen-thoughts.com/) ⭐️ 8.0/10

研究人员展示了一种通过将前沿 LLM 的输出重放到较弱模型中，并利用越狱或工具使用技巧来恢复思维链推理的方法，从而窃取其内部推理轨迹。 此技术对 AI 安全、知识产权保护和模型蒸馏提出重大担忧，因为它允许未经授权从 LLM API 中提取专有推理能力，可能削弱竞争优势和安全防护。 该攻击涉及将前沿模型的输出重放到较弱的姐妹模型中，然后通过越狱或工具使用提示来引出原本在 API 响应中被隐藏的内部思维链推理。

hackernews · quantumgarbage · Aug 11, 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49257876)

**背景**: 推理轨迹是大型语言模型在生成最终答案之前产生的中间推理步骤，通常通过思维链提示来鼓励，以提高在复杂任务上的表现。专有 LLM API 通常会隐藏这些轨迹，仅向用户暴露最终输出。模型提取攻击旨在通过 API 查询复制模型的行为或知识，对知识产权和 AI 安全构成风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.23163v1">Probing the Trajectories of Reasoning Traces in Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2506.22521v1">A Survey on Model Extraction Attacks and Defenses for</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者就该技术的伦理问题展开了讨论，一些人认为从已付费使用的模型中提取推理轨迹并不算真正的“盗窃”，而另一些人则强调了跨模型重放输出的新颖性，并指出类似效果也可通过使用工具或在某些模型中禁用思考模式来实现。

**标签**: `#LLM security`, `#AI safety`, `#model extraction`, `#reasoning traces`, `#proprietary models`

---

<a id="item-3"></a>
## [英国交通警察将实时人脸识别试点扩展至伦敦地铁站](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 8.0/10

英国交通警察正在将其实时人脸识别（LFR）试点扩展至伦敦交通局地铁站，部署摄像头实时扫描乘客面部并与警察名单进行比对。 此次扩展引发重大隐私和公民自由担忧，因为它在未经明确公众同意的情况下在公共交通中实现了大规模监视，可能会冷却匿名出行，并为更广泛的国家监视树立先例。 该 LFR 系统旨在识别警察名单上涉及性犯罪、抢劫和持刀犯罪等“高危害”罪行的个人，试点已于 2026 年 2 月 11 日在选定的交通枢纽开始，随后扩展至地铁站。

hackernews · BlueBerry2001 · Aug 11, 09:40 · [社区讨论](https://news.ycombinator.com/item?id=49255496)

**背景**: 实时人脸识别（LFR）技术使用人工智能驱动的摄像头实时分析面部特征，并将其与通缉人员数据库进行比对。虽然支持者认为它能通过更快速地识别嫌疑人来提升公共安全，但批评者警告其存在误识别、功能漂移以及公共空间匿名性被侵蚀的风险。英国一直是公共场所部署 LFR 的领导者，尽管其必要性和比例性仍面临法律挑战和公众辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/">BTP expands Live Facial Recognition (LFR) trial into London Underground stations | British Transport Police</a></li>
<li><a href="https://www.btp.police.uk/police-forces/british-transport-police/areas/about-us/about-us/facial-recognition-technology/">British Transport Police use of Live Facial Recognition Technology | British Transport Police</a></li>
<li><a href="https://www.mylondon.news/news/british-transport-police-trial-live-34435589">British Transport Police to trial live facial recognition cameras at London Tube stations - My London</a></li>

</ul>
</details>

**社区讨论**: 评论者对隐私侵蚀表达了强烈担忧，有人指出由于非接触式支付系统，地铁上的匿名出行已经减少；其他人则批评此次试点是奥威尔式的，质疑其效果和民主合法性，认为它更可能实现监视过度而非真正的犯罪预防。

**标签**: `#facial recognition`, `#surveillance`, `#privacy`, `#civil liberties`, `#public safety`

---

<a id="item-4"></a>
## [形式化 conformal 预测中的信息间隙](https://arxiv.org/abs/2608.07479) ⭐️ 8.0/10

该论文形式化了 conformal 预测中的残差信息间隙，表明相对于 oracle 的 log-score 遗憾恰好等于残差与输入之间的互信息，而 conformalization 无法减少这一量。 这项工作澄清了 conformal 预测的一个基本局限性：它保证覆盖率但无法提高预测锐度，纠正了不确定性量化领域的常见误解，并为更好地评估预测系统提供指导。 对于单形状残差预测系统，相对于 oracle 的 log-score 遗憾恰好等于残差 R 与输入 X 之间的互信息 I(R;X)；conformalization 影响覆盖率但不影响此量，因为它取决于预测器的形状类而非校准。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: conformal 预测在可交换性假设下提供有限样本、分布自由的边际覆盖率保证，能为任何点预测器生成有效的预测区间。然而，这种有效性并不意味着预测质量或锐度，且该方法常被误解为预测性能良好的指标。该论文通过信息理论区分了 conformal 保证的覆盖率和其无法提升的锐度，形式化了这一间隙。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.07479">[2608.07479] Marginally Useful: Formalizing the Information Gap in Conformal Prediction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2608.07479">Marginally Useful Formalizing the Information Gap in Conformal Prediction</a></li>

</ul>
</details>

**标签**: `#conformal prediction`, `#uncertainty quantification`, `#machine learning theory`, `#information theory`, `#calibration`

---

<a id="item-5"></a>
## [LLM 代理在供应链谈判中展现出能力驱动的效率和分配偏差](https://arxiv.org/abs/2608.07538) ⭐️ 8.0/10

一项研究评估了来自 OpenAI、Google 和 阿里巴巴 的九个 LLM 在 9,840 次具有非对称信息的自主供应链谈判中，发现高能力模型能够实现近乎最优的剩余价值，但需要更多谈判轮次，而较弱模型以显著比例接受非理性合同。 研究结果揭示了在自主采购中部署 LLM 代理的关键权衡：能力既影响价值创造也影响可靠性，而提供商身份和提示词显著影响剩余分配，这需要基于能力的防护措施和战略性部署选择。 高能力 LLM 捕获了 95.4% 的第一最优剩余价值，但平均谈判轮次为 2.98（均衡基准为 1.25），这种延迟导致 21-34% 的剩余价值流失；基线模型有 19.2% 的比例接受了非理性合同，而中级和旗舰模型仅为 0.0-0.6%。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 该研究构建了一个典型的供应链谈判场景：买方拥有私有需求信息，与未获知情的卖方谈判数量-付款合同，并以完美贝叶斯均衡作为非对称信息下理性行为的基准。研究进行了 LLM 之间的谈判，以隔离人类影响并考察代理行为，测试部署的代理是否能在自主环境中复制经济理性结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perfect_Bayesian_equilibrium">Perfect Bayesian equilibrium - Wikipedia</a></li>
<li><a href="https://pubsonline.informs.org/doi/10.1287/mnsc.2014.1938">Dynamic Bargaining in a Supply Chain with Asymmetric Demand Information | Management Science</a></li>
<li><a href="https://www.labarna.ai/blog/autonomous-agent-negotiation-protocols-strategies">Autonomous Agent Negotiation: Protocols and Strategies</a></li>

</ul>
</details>

**标签**: `#LLM Agents`, `#Multi-agent Systems`, `#Game Theory`, `#Supply Chain Optimization`, `#Autonomous Negotiation`

---

<a id="item-6"></a>
## [具有防篡改日志的自适应生成式 AI 遥测框架](https://arxiv.org/abs/2608.09069) ⭐️ 8.0/10

该论文提出了一种针对自适应生成式 AI 系统的双重遥测架构，结合离散梅克尔链用于权重序列日志记录，并通过伊藤公式实现连续时间推广，以实现可审计性并检测未授权的模型更改。 该框架通过为持续自适应模型提供可验证的日志记录，填补了模型风险管理中的关键空白，因为这些模型违反了传统的静态模型假设，需要新的治理方法来确保 AI 安全和监管合规。 该架构建立了用于审计的最小充分统计量，使用梅克尔链实现防篡改的离散日志记录，通过伊藤公式推导连续时间遥测（以平方变化作为遥测标量），并采用 KL 分歧停止时间进行事件驱动日志记录，同时形式化了六种对抗性模型隐藏策略及其对应的对策。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 模型风险管理传统上假设模型在部署后是静态的，但自适应生成式 AI 系统会在运行过程中持续更新自身权重，使得时间点验证变得无效。这导致了一种治理挑战：未经授权或有害的模型更改可能在没有持续监控和防篡改日志机制的情况下不被发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.09069">Telemetry and Concealment in Self - Adapting Generative AI : Logging...</a></li>
<li><a href="https://speytech.com/insights/merkle-chains-ml-audit/">Merkle Chains for ML Audit Trails | SpeyTech</a></li>
<li><a href="https://arxiv.org/html/2608.09069">Telemetry and Concealment in Self-Adapting Generative AI: Logging...</a></li>

</ul>
</details>

**标签**: `#AI Governance`, `#Model Risk Management`, `#Telemetry`, `#Self-Adapting Systems`, `#Adversarial Robustness`

---

<a id="item-7"></a>
## [联合李雅普诺夫证书实现多智能体生成式 AI 的零知识治理](https://arxiv.org/abs/2608.09087) ⭐️ 8.0/10

该论文提出联合李雅普诺夫证书（JLC）来治理 K 智能体生成式 AI 系统，通过一种加密协议证明随机稳定性并检测出现的集合层面风险，在不揭示专有模型权重的情况下证明模型风险管理合规性。 此框架填补了 AI 治理中的关键空白：单个模型的稳定性并不保证耦合生成式 AI 系统的整体稳定性，使得在多智能体 AI 系统中能够实现可验证且保护隐私的法规合规。 该工作推导出均方稳定性失效的确切临界耦合阈值，建立了零知识证明目标的噪声底线定理，并构建了基于实时权重的每轮 SNARK，通过五个数值研究在多智能体 softmax 系统上进行验证。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 模型风险管理（MRM）传统上依赖于单智能体李雅普诺夫分析来确保单个 AI 模型的稳定性，但当模型通过相互作用矩阵耦合时，这种方法会失效——即使每个模型在隔离状态下看似稳定，系统层面仍可能出现新兴风险。联合李雅普诺夫分析通过考察互联系统的集体动态来弥补这一不足，这对于具有元学习耦合的自适应生成式 AI 尤为重要。零知识证明（如 SNARKs）允许一方在不揭示底层数据的情况下证明某个陈述的有效性，因此非常适合在保护知识产权的同时证明 AI 系统的合规性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.09087v1">Joint Lyapunov Certificates for 𝐾-Agent Generative AI ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.09087">Joint Lyapunov Certificates for K-Agent Generative AI Governance...</a></li>
<li><a href="https://www.nist.gov/itl/ai-risk-management-framework">AI Risk Management Framework | NIST</a></li>

</ul>
</details>

**标签**: `#AI Governance`, `#Lyapunov Stability`, `#Multi-Agent Systems`, `#Zero-Knowledge Proofs`, `#Model Risk Management`

---

<a id="item-8"></a>
## [数据分割导致 AI 在定价博弈中暗中串通](https://arxiv.org/abs/2403.06150) ⭐️ 8.0/10

该研究表明，当消费者数据被标记和分割时，AI 定价算法可以通过市场分配或诱饵-约束-剥削策略实现暗中串通，即使没有直接沟通。 这挑战了更多数据总是能改善竞争的假设，揭示了数据优势如何导致有害的 AI 行为，监管者必须加以监控以保护消费者。 在对称分割下，每个 AI 垄断高支付意愿的细分市场并定高于竞争价格；在不对称分割下，细分程度更高的 AI 采用诱饵-约束-剥削策略，诱导另一个 AI 串通。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 多市场接触是指企业在多个市场中竞争，这可能促进暗中串通。在 AI 定价博弈中，算法通过学习数据来定价，而数据标签创造的人工市场细分会增加 AI 之间的战略相互依赖，即使没有明确沟通，也更可能导致协调结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.06150">[2403.06150] Artificial Intelligence, Data and Competition</a></li>
<li><a href="https://arxiv.org/html/2403.06150">Artificial Intelligence, Data and CompetitionThis paper was previously circulated as “Algorithmic Collusion and Price Discrimination: the Over-Useage of Data.” We thank Giacomo Calzolari, Jean-Edouard Colliard, Francesco Decarolis, Bo Hu, Bruno Jullien, Sanxi Li, Tristan Tomala, Daniel Yi Xu, Jidong Zhou for their valuable comments and suggestions. We also thank seminar audiences at Fudan University, Nanjing University, Shandong University, University of International Business and Economics, the 2024 Be</a></li>
<li><a href="https://arxiv.org/pdf/2403.06150">Artificial Intelligence, Data and Competition - arXiv.org</a></li>

</ul>
</details>

**标签**: `#AI and competition`, `#algorithmic collusion`, `#market segmentation`, `#pricing games`, `#data strategy`

---

<a id="item-9"></a>
## [ParlayMarket 提出用于联合合约的统一流动性池自动做市商](https://arxiv.org/abs/2603.22596) ⭐️ 8.0/10

ParlayMarket 提出了一种用于 parlay 风格联合合约的自动做市商，通过维护共享的成对指数族信念状态，实现基础市场和组合市场之间的一致定价，仅需 O(M²) 个充分统计量。 这解决了预测市场中的一个关键限制，使得在不碎片化流动性的情况下能够高效交易相关的联合结果，并在理论上保证收敛以及损失随基础事件数量的平方增长而非指数增长。 该机制将 2^M 个结果空间压缩为 O(M²) 个充分统计量，确保所有价格来源于一个一致分布的边缘，并表明 parlay 交易相比仅从边缘学习能降低稳态误差，且在密集成对依赖情况下，二次损失是最坏情况下最优的。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 预测市场能够聚合信息，但通常仅限于单事件合约；parlay 风格的联合合约（如体育串关）涉及对多个相关结果的下注，而当前平台往往禁止此类交易或因忽略相关性而导致定价低效。指数族分布提供了一种灵活的方式来建模信念，而充分统计量则允许对复杂分布进行紧凑表示。像 LMSR 这样的自动做市商通过根据交易更新价格来维持流动性并激励真实信息的透露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.22596">ParlayMarket: Automated Market Making for Parlay-style Joint ...</a></li>
<li><a href="https://arxiv.org/html/2603.22596v1">ParlayMarket: Automated Market Making for Parlay-style Joint ...</a></li>
<li><a href="https://www.emergentmind.com/topics/parlaymarket">ParlayMarket: AMM for Joint Contracts - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#automated market making`, `#parlay contracts`, `#exponential family`, `#mechanism design`

---

<a id="item-10"></a>
## [扩展状态依赖霍克斯过程模拟限价单簿动态](https://arxiv.org/abs/2604.23961) ⭐️ 8.0/10

本文提出扩展状态依赖霍克斯过程（ExsdHawkes），通过允许状态消失来模拟限价单簿动态，并使用 KKT 条件证明最大似然估计的可分性。实证表明，该模型通过识别可交易限价单作为局部超临界状态的驱动因素，成功再现了波动率签名图。 该模型通过提供一个物理上一致的框架，填补了金融数学中的关键空白，能够准确捕捉高频交易中的宏观波动模式。它为量化金融从业者提供了一种理论基础扎实的工具，用于以更高的稳定性和真实性模拟限价单簿。 ExsdHawkes 通过在不可接受期间强制物理几何来暂停残余累积，从而防止无约束模型中出现的爆炸性分支比率。该模型在三菱 UFJ 金融集团（8306）三个月的高频 tick 数据上进行了验证，展示了其在波动率签名图上坡部分的独特再现能力。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 限价单簿（LOB）是指金融资产的买卖订单列表，在交易过程中实时更新。霍克斯过程是一种自激时间点过程，用于建模聚类事件，如交易或订单提交，其中过去的事件会增加未来事件发生的可能性。状态依赖变体允许过程强度根据系统当前状态（如订单簿失衡或价格压力）进行变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.23961">[2604.23961] Extended State-dependent Hawkes Process for ...</a></li>
<li><a href="https://arxiv.org/html/2604.23961v2">Extended State-dependent Hawkes Process for Limit Order Books ...</a></li>
<li><a href="https://www.semanticscholar.org/paper/Extended-State-dependent-Hawkes-Process-for-Limit-Kimura/2da2e0d216ccdd84275a129633eadc572cdc11cc">Extended State-dependent Hawkes Process for Limit Order Books ...</a></li>

</ul>
</details>

**标签**: `#quantitative finance`, `#high-frequency trading`, `#Hawkes process`, `#limit order book`, `#market microstructure`

---

<a id="item-11"></a>
## [只有当人类准确感知 AI 能力时，AI 扩展才能提升人机团队表现](https://arxiv.org/abs/2608.00818) ⭐️ 8.0/10

一篇新的 arXiv 论文表明，只有当人类准确感知 AI 能力时，AI 扩展才能提升人机团队表现；否则，过度估计会导致“扩展悖论”，即更强的 AI 反而降低整体表现，而低估则会使性能提升变得缓慢。 这挑战了更大 AI 系统总能提升性能的假设，凸显了管理人类感知和信任与技术扩展同样重要，对实际 AI 部署具有关键意义。 研究表明，过度感知会导致扩展悖论，使联合系统性能下降并增加利润损失；而低估感知则使性能提升变慢。研究进一步提出，通过感知一致等运营政策可以缓解这些影响。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: AI 定律描述了模型能力如何随着计算、数据或参数的增加而可预测地提升。然而，现实中的 AI 系统通常需要与人类协作，此时人类对 AI 能力的信任、偏见和感知会超越模型本身的性能，影响最终结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.00818">[2608.00818] The Scaling Paradox in Human - AI Collaboration</a></li>
<li><a href="https://ideas.repec.org/p/arx/papers/2608.00818.html">The Scaling Paradox in Human - AI Collaboration</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7207559">The Scaling Paradox in Human - AI Collaboration by Anyan... :: SSRN</a></li>

</ul>
</details>

**标签**: `#human-AI collaboration`, `#AI scaling laws`, `#cognitive modeling`, `#system performance`, `#trust and perception`

---

<a id="item-12"></a>
## [论文提出金融领域智能体 AI 的四层治理框架](https://arxiv.org/abs/2608.02311) ⭐️ 8.0/10

该 arXiv 论文指出金融领域智能体 AI 存在治理缺口，调查显示 88%的专业人士缺乏运营框架，并提出一个由政策、工程、组成和系统四层组成的框架，得益于合成模拟和真实案例的支持。 该框架旨在应对金融中持续学习 AI 系统带来的风险，为机构提供实用指导以管理系统性风险，如联合回撤，模拟显示若无适当治理，该风险可能从 39.2%升至 79.3%。 该框架基于两个合成示例（后悔-协方差漂移监控器和人群模拟）以及三个真实案例构建，包括嵌入 LLM 的交易策略和一只 450 亿美元基金的爆仓事件，并提出了 90 天的实施序列。

rss · arXiv Quantitative Finance · Aug 11, 04:00

**背景**: 智能体 AI 指的是能够在最少人工监督下自主决策和行动的 AI 系统，正日益被用于金融交易和资产管理。传统治理框架是为静态模型设计的，无法应对持续再训练政策带来的风险，因此需要具备适应性的系统级监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iofm.com/ap/webinars/agentic-ai-boardroom-building-governance-framework-for-autonomous-finance">Agentic AI & The Boardroom: Building a Governance Framework for...</a></li>
<li><a href="https://pub.towardsai.net/agentic-ai-and-the-smb-banking-advantage-0e75e0514707">Agentic AI and the SMB Banking Advantage | Towards AI</a></li>
<li><a href="https://www.omniscient.media/post/the-market-already-voted-on-agentic-ai-regulators-are-still-finding-their-seats">The Market Already Voted on Agentic AI .... | Omniscient Media</a></li>

</ul>
</details>

**标签**: `#AI Governance`, `#Agentic AI`, `#Finance`, `#Financial Regulation`, `#Systemic Risk`

---