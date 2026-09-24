---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> From 41 items, 9 important content pieces were selected

---

1. [高通为骁龙 X2 系列上游 Linux 驱动程序](#item-1) ⭐️ 8.0/10
2. [Claude 发现具有 CRISPR 样重复的新型酶系统。](#item-2) ⭐️ 8.0/10
3. [谷歌发布 Gemini 3.8 文本转语音模型，具备声音克隆和水印](#item-3) ⭐️ 8.0/10
4. [审视职场沟通中的‘我不想知道细节’](#item-4) ⭐️ 8.0/10
5. [Gemini 3.8 TTS 播放场发布，提供 2000+声音及自定义声音。](#item-5) ⭐️ 8.0/10
6. [以太坊 MEV 交易重排导致用户每月损失 720 万美元](#item-6) ⭐️ 8.0/10
7. [稀疏性在复杂性中的美德。](#item-7) ⭐️ 8.0/10
8. [机器学习衡量高频交易流动性供给与需求](#item-8) ⭐️ 8.0/10
9. [神经算子在结构化 BSDEs 上的多项式尺度得以实现](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [高通为骁龙 X2 系列上游 Linux 驱动程序](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) ⭐️ 8.0/10

高通宣布将为骁龙 X2 系列上游核心 Linux 驱动程序，包括 Hexagon NPU 和 Adreno GPU，以在这些 ARM 笔记本上提供更好的 GPU、NPU 和硬件支持。 此举增强了 ARM 笔记本上的 Linux 兼容性，使高通成为苹果 M 系列芯片和传统 x86 厂商更有力的竞争对手，并可能推动 Linux 在骁龙设备上的更广泛采用。 高通计划在 2026 年底实现 Debian 支持，2027 年获得 Ubuntu 认证，重点是 GPU 和 NPU 驱动，但实际就绪程度会因 OEM 设计和具体 X2 变体而异。

hackernews · aaronday · Sep 23, 22:38 · [社区讨论](https://news.ycombinator.com/item?id=49823582)

**背景**: 骁龙 X2 系列是高通最新的基于 ARM 的笔记本平台，集成了用于 AI 工作负载的 Hexagon NPU 和用于图形的 Adreno GPU。历史上，高通移动焦点 SoC 上的 Linux 支持仅限于下游或专有驱动，导致 GPU 和 NPU 功能存在缺口。通过将这些驱动上游到主线 Linux 内核，高通使社区开发者能够基于开源支持进行构建，并提升长期可维护性。这符合硬件厂商向 Linux 贡献核心组件以提高开放性和 ARM 设备性能的更广泛行业趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/news/999664/qualcomm-snapdragon-x2-linux-support-arm">Qualcomm will finally support Linux on Snapdragon X2 chips. | The Verge</a></li>
<li><a href="https://xenospectrum.com/en/snapdragon-x2-linux-preview-ubuntu/">Snapdragon X2 Laptops Get Linux Roadmap: Debian This Year, Ubuntu Certification by 2027 | XenoSpectrum</a></li>
<li><a href="https://www.xda-developers.com/qualcomm-is-helping-linux-run-better-on-snapdragon-x2-laptops-with-an-early-developer-preview/">Qualcomm is helping Linux run better on Snapdragon X2 laptops with an Early Developer Preview</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞其性能潜力，认为可与苹果 M 系列媲美并超越当前的 Intel/AMD 产品，并欢迎这一开源做法，相较于半专有的 ChromeOS 支持。一些人担心 OEM 差异、缺少台式机或其他外形覆盖以及需要主板可升级性，而另一些人则指出相关的 OpenBSD 进展以及 KVM/EL2 支持，表明具备虚拟化能力。

**标签**: `#Linux`, `#ARM`, `#Qualcomm`, `#Snapdragon X2`, `#open-source drivers`

---

<a id="item-2"></a>
## [Claude 发现具有 CRISPR 样重复的新型酶系统。](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic 的 AI 助手 Claude 自主分析基因组数据，发现了一种以前未知的酶系统，该系统靠近逆转录酶基因，旁边有一段长的 DNA 重复序列，类似于 CRISPR 数组。 这一发现展示了大型语言模型如何加速生物信息学研究，揭示可能用于基因编辑或合成生物学的新型酶功能。 该酶系统位于一种与 CRISPR 重复具有结构相似的串联重复数组旁边，但其关联酶似乎是逆转录酶相关的核酸酶，而非 Cas 蛋白；目前这一发现仅为计算预测，尚需实验验证。

hackernews · raahelb · Sep 23, 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR 系统由一种由 RNA 引导的 Cas 核酸酶组成，该酶能识别间隔有来源于外源基因的 spacer DNA 的短重复序列。逆转录酶是能够从 RNA 模板合成 DNA 的酶，常见于诸如 retron 和噬菌体等流动遗传元件。Anthropic 的 Claude 在科学文献上进行训练，并被赋予自主探索基因组数据集的任务，使其能够检测到可能被传统方法忽略的重复数组等模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system \ Anthropic</a></li>
<li><a href="https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats">Anthropic says Claude found a new enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 能够发现新的生物学模式感到兴奋，并欣赏能够查看 Claude 内部推理的转录本；与此同时，也有人质疑语言模型如何能够对生化结构进行推理，并提醒这一发现目前仅是计算预测。还有人指出治疗应用仍受递送限制，并有少数人敦促 Anthropic 明确其在 AI 驱动的生物工程方面的立场。

**标签**: `#AI`, `#bioinformatics`, `#CRISPR`, `#enzyme discovery`, `#genomics`

---

<a id="item-3"></a>
## [谷歌发布 Gemini 3.8 文本转语音模型，具备声音克隆和水印](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 文本转语音模型，能够从 30 秒音频样本克隆声音，内置 SynthID 水印和 C2PA 凭证，并在 Google AI Studio、Gemini API、Gemini Enterprise、Gemini Notebook 和 Google Vids 上提供服务。 此次发布推动了逼真的合成语音技术发展，并加入内置同意验证和防篡改水印，可能扩大在内容创作、无障碍和媒体溯源中的应用，同时也凸显了谷歌 AI 产品推出时的碎片化问题。 该模型基于 Gemini 3 Pro，可接受最多 8K 令牌的文本并输出最多 64K 令牌的音频；声音克隆需要经过验证的同意检查，输出音频携带 SynthID 水印和 C2PA 元数据以实现来源追溯。

hackernews · swolpers · Sep 23, 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49817615)

**背景**: 文本转语音（TTS）系统将书面文本转换为语音音频，最近的进展使得声音克隆成为可能——从短音频样本复制一个人的声音。水印技术如 SynthID 会嵌入不可感知的信号以识别合成音频，而 C2PA 提供了一种为媒体文件附加来源元数据的标准。谷歌的 Gemini 系列包括多模态模型，其中 3.8 系列侧重于音频功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 text-to-speech says hello</a></li>
<li><a href="https://www.unite.ai/google-rolls-out-gemini-3-8-speech-models-in-api-and-ai-studio/">Google Rolls Out Gemini 3.8 Speech Models In API And AI Studio – Unite.AI</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏声音克隆的保真度和本地托管的使用场景，但反复批评谷歌在消费者、专业消费者和云平台之间的可用性不一致以及功能差异，指出在某些环境中视频输出等功能可能缺失。

**标签**: `#Gemini`, `#text-to-speech`, `#AI`, `#voice cloning`, `#Google`

---

<a id="item-4"></a>
## [审视职场沟通中的‘我不想知道细节’](https://michaelheap.com/i-dont-want-the-details/) ⭐️ 8.0/10

文章探讨了领导者使用‘我不想知道细节’这句话，分析其在工程团队中对信任、能力以及监督与自主权平衡的含义。 理解这句话有助于领导者认识沟通方式如何影响团队信任和问责，为改进工程管理实践提供见解。 讨论呈现出不同观点：有些人认为这句话表示信任和授权，而另一些人则警告它可能导致责任推卸并阻碍根本原因分析。

hackernews · mooreds · Sep 23, 13:04 · [社区讨论](https://news.ycombinator.com/item?id=49815466)

**背景**: 在软件工程领导中，诸如‘我不想知道细节’之类的短语常常出现在经理授权时，体现了在信任团队执行与保持监督以进行风险管理之间的紧张关系。这种动态影响决策、事件响应和组织学习。

**社区讨论**: 评论者们就这句话是否表示真正的信任还是缺乏问责展开辩论，有人赞赏其授权的语气，也有人认为它回避了必要的监督和根本原因调查。讨论还涉及了应如何处理最后时刻的变更和系统性修复，而不是将责任归咎于个人。

**标签**: `#communication`, `#management`, `#software engineering`, `#leadership`, `#trust`

---

<a id="item-5"></a>
## [Gemini 3.8 TTS 播放场发布，提供 2000+声音及自定义声音。](https://simonwillison.net/2026/Sep/23/gemini-tts-playground/) ⭐️ 8.0/10

Google 发布了 Gemini 3.8 Flash TTS 和 Gemini 3.8 Flash-Lite TTS 模型，提供超过 2000 种声音，并支持仅凭 30 秒音频样本创建自定义声音。Simon Willison 还推出了一个交互式播放场，让开发者使用自己的 API 密钥尝试这些模型。 这些模型降低了创建富有表现力、多说话者文本转语音应用的门槛，使开发者能够在无需大量训练数据的情况下生成逼真的角色对话和自定义声音。此次发布体现了 AI 语音合成向高可控性、低成本方向发展的趋势，适用于创意和企业场景。 这两个模型分别称为 gemini-3.8-flash-tts 和 gemini-3.8-flash-lite-tts；播放场展示了直接 API 连接，仅在内存中保存用户的 API 密钥，并演示使用 Flash 模型生成 1 分 18 秒音频的成本约为 2.74 美分。它还支持为对话中的每个说话者分配不同的声音和语音风格。

rss · Simon Willison · Sep 23, 17:12

**背景**: 文本转语音（TTS）系统将书面文本转换为语音音频，近年来的进展使得仅凭短音频样本即可克隆声音。Google 的 Gemini 系列包含多模态模型；3.8 Flash 变体在保持高表现力的同时针对速度和成本进行了优化。Gemini API 的开放 CORS 策略允许网页应用进行直接的跨源请求，使得 Simon Willison 的播放场能够安全地发送 API 密钥而不进行存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS - The Keyword</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://toolchase.com/blog/ai-voice-cloning/">AI Voice Cloning in 2026 | ToolChase</a></li>

</ul>
</details>

**标签**: `#text-to-speech`, `#Gemini`, `#AI models`, `#voice synthesis`, `#developer tools`

---

<a id="item-6"></a>
## [以太坊 MEV 交易重排导致用户每月损失 720 万美元](https://arxiv.org/abs/2508.04003) ⭐️ 8.0/10

论文发现，目前两个 MEV 构建者生产了以太坊近 80%的区块，用户需要每月支付约 720 万美元才能确保其交易处于区块的第一四分之一。三明治攻击出现在超过每两个区块中的一个，而这些攻击的 gas 费用大约占验证者获得的 MEV 的 9.6%。 这些结果量化了 MEV 对普通以太坊用户的经济负担，并凸显了区块构建权力的集中，为协议设计者和用户提供了改革方向以降低有害的交易排序。研究结果支持诸如 gas 费优先机制或私有交易池之类的提案，以减轻 MEV 的提取。 研究指出，三明治攻击会在受害者交易前后插入交易，而这些攻击的 gas 费用大约占支付给验证者的总 MEV 的 9.6%。它还提到了提出者‑构建者分离（PBS）路线图作为解决构建者主导问题的潜在结构性 remedy。

rss · arXiv Quantitative Finance · Sep 23, 04:00

**背景**: 最大可提取价值（MEV）是指验证者通过重新排序、包含或排除交易而获得的超出标准区块奖励和 gas 费用的额外利润。三明治攻击是一种特定的 MEV 策略，攻击者在受害者交易前后各插入一笔交易，以从价格波动中获利。在以太坊上，区块构建者将交易组装进区块并可以重新排序以最大化 MEV，而提出者‑构建者分离（PBS）升级旨在将区块构建与区块提案分离，以降此类权力集中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ethereum.org/developers/docs/mev/">Maximal extractable value (MEV) | ethereum.org</a></li>
<li><a href="https://www.gate.com/learn/articles/what-is-a-sandwich-attack/936">What Is a Sandwich Attack? Definition & How It Works | Gate Learn</a></li>
<li><a href="https://financefeeds.com/how-block-builders-select-transactions/">How Block Builders Order Ethereum Transactions</a></li>

</ul>
</details>

**标签**: `#Ethereum`, `#MEV`, `#blockchain`, `#transaction ordering`, `#sandwich attacks`

---

<a id="item-7"></a>
## [稀疏性在复杂性中的美德。](https://arxiv.org/abs/2604.17166) ⭐️ 8.0/10

作者表明，在扩大候选因子空间的同时通过基础追踪（basis pursuit）强制因子稀疏性，可以得到在最大规模下优于密集无正则基准的稀疏投资组合，其外部样本夏普比率更高、定价误差更低。 通过区分容量稀疏性和因子稀疏性，论文调和了模型丰富性与简约性之间的明显张力，表明扩大候选集合并施加稀疏性可以互补，这对金融建模和高维机器学习具有重要影响。 该方法将基础追踪优化与非线性特征扩展相结合，通过列生成和 GPU 加速将规模扩展到 4.32 亿个候选因子，实证表明在最大规模下稀疏投资组合的夏普比率更高、定价误差更低，优于密集无正则基准。

rss · arXiv Quantitative Finance · Sep 23, 04:00

**背景**: 高维资产定价涉及众多潜在风险因子，稀疏性寻求简洁的表示。基础追踪是ℓ₁最小化问题，用于求解不完全确定线性系统的最稀疏解。列生成是一种迭代算法，通过每次仅考虑变量子集来求解大型线性规划，GPU 加速可提升定价核的计算速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Basis_pursuit">Basis pursuit - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Column_generation">Column generation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#asset pricing`, `#sparsity`, `#machine learning`, `#high-dimensional statistics`, `#basis pursuit`

---

<a id="item-8"></a>
## [机器学习衡量高频交易流动性供给与需求](https://arxiv.org/abs/2608.00858) ⭐️ 8.0/10

作者利用专有的纳斯达克数据训练机器学习模型，构建了 2010 年至 2023 年美国所有股票的日频流动性供给和需求 HFT 度量，表明该度量优于标准代理并在泛欧交易所巴黎市场推广。 该新度量为研究者提供了一种可靠的、专门针对高频交易的工具，可在 14 年面板数据上研究流动性动态和市场质量，改进了常用代理并实现跨市场比较。 该方法采用在纳斯达克专有 HFT 标签上训练的集成机器学习模型，将其映射到公开的盘内变量，生成的日度序列能够吸收标准代理并在训练后多年保持预测力；在 COVID‑19 期间，流动性供给型 HFT 与点差收窄更紧密相关。

rss · arXiv Quantitative Finance · Sep 23, 04:00

**背景**: 高频交易（HFT）是指使用强大的算法在毫秒或微秒级别执行大量订单，既可以充当流动性提供者（报出买卖价），也可以充当流动性需求者（吃掉现有报价）。公开数据通常不标记哪些交易属于 HFT，而常用的代理变量如成交量或换手率无法区分流动性提供型和流动性需求型策略。作者通过在纳斯达克的专有 HFT 数据集上训练机器学习模型，将其映射到可观测的盘内变量，从而能够为美国所有股票构建日频流动性供给和需求的度量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High-frequency_trading">High-frequency trading - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/h/high-frequency-trading.asp">Understanding High-Frequency Trading (HFT): Basics, Mechanics ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.00858">Data -Driven Measures of High-Frequency Trading</a></li>

</ul>
</details>

**标签**: `#high-frequency trading`, `#machine learning`, `#market microstructure`, `#liquidity measurement`, `#financial econometrics`

---

<a id="item-9"></a>
## [神经算子在结构化 BSDEs 上的多项式尺度得以实现](https://arxiv.org/abs/2410.14788) ⭐️ 8.0/10

该论文表明，通过利用额外的问题结构——即分解相关半线性椭圆偏微分方程 Green 函数的奇异部分，并将 BSDE 的共同非马尔可夫因子的 Doléans‑Dade 指数融入网络的解码层——神经算子架构能够对特定非马尔可夫后向随机微分方程族实现多项式逼近速率。 此结果首次确立了神经算子对结构化 BSDE 解算子的多项式尺度逼近 regime，突破了一般算子类的指数下界，从而推动了随机分析中算子学习的理论基础及其在高维偏微分方程求解中的应用。 作者研究了终端条件和生成器的加性非线性扰动均为 Sobolev 正则的 BSDE 族；通过去除奇异 Green 函数部分并在解码器中嵌入 Doléans‑Dade 指数来定制神经算子，并证明实现均匀ε精度逼近所需的可训练参数数量随 1/ε的多项式增长。

rss · arXiv Quantitative Finance · Sep 23, 04:00

**背景**: 神经算子是一类专为学习无穷维函数空间之间映射而设计的深度学习模型，将传统神经网络推广到算子学习。后向随机微分方程（BSDEs）是一类由终端条件决定解的随机方程；非马尔可夫 BSDEs 依赖于整个过去路径，因而更难以逼近。对于仅由正则性定义的一般算子类，信息论下界表明最优逼近误差仅以 1/ε的指数形式衰减，这就促使人们寻找能够实现多项式尺度的额外结构假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2410.14788">Polynomial Scaling is Possible For Neural Operator Approximations of...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_operators">Neural operators - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Backward_stochastic_differential_equation">Backward stochastic differential equation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#neural operators`, `#BSDEs`, `#polynomial scaling`, `#stochastic analysis`, `#machine learning theory`

---