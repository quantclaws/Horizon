---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> From 37 items, 8 important content pieces were selected

---

1. [huggingface/transformers released v5.14.0](#item-1) ⭐️ 8.0/10
2. [思考机器发布了开放权重多模态模型 Inkling。](#item-2) ⭐️ 8.0/10
3. [xAI 开源 Grok Build，包含 Mermaid 渲染器](#item-3) ⭐️ 8.0/10
4. [Stripe 和 Advent 联合报价超过 530 亿美元收购 PayPal](#item-4) ⭐️ 8.0/10
5. [Model Combination in Risk Sharing under Ambiguity](#item-5) ⭐️ 8.0/10
6. [Taming Tail Risk: Regime-Weighted Conformal Calibration for Nonstationary Value-at-Risk](#item-6) ⭐️ 8.0/10
7. [基于 LLM 的故事期望建模框架](#item-7) ⭐️ 8.0/10
8. [基于 Transformer 的注意力机制用于非线性混合频率因子模型。](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [huggingface/transformers released v5.14.0](https://github.com/huggingface/transformers/releases/tag/v5.14.0) ⭐️ 8.0/10

Hugging Face Transformers v5.14.0 introduces the Inkling multimodal model (975B total, 41B active) supporting text, image, and audio inputs.

github · ArthurZucker · Jul 15, 19:02

**标签**: `#transformers`, `#huggingface`, `#multimodal`, `#large-language-model`, `#release`

---

<a id="item-2"></a>
## [思考机器发布了开放权重多模态模型 Inkling。](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

思考机器实验室宣布了 Inkling，这是一个拥有 9750 亿参数的开放权重多模态混合专家模型，其中有 410 亿活跃参数并具备可控的思考努力，于 2026 年 7 月 15 日发布。该模型支持音频，旨在作为企业微调的可定制基础。 通过提供开放权重的多模态基础，Inkling 使企业能够用自身数据定制强大模型，避免供应商锁定和高昂许可费用。其音频功能扩展了可用输入范围，使其成为闭源前沿模型的多功能替代方案。 Inkling 采用混合专家架构，总参数达 9750 亿，推理时激活参数为 410 亿，并具备可控的思考努力机制。模型支持音频输入，采用开放权重许可发布，可通过 llama.cpp、Unsloth 或 HuggingFace 的 GGUF/NVFP4 量化在本地运行，以便在 Tinker 平台进行微调。

hackernews · vimarsh6739 · Jul 15, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48924912)

**背景**: 开放权重模型将模型学习到的参数公开，任何人都可以下载、检查和微调，而无需依赖专有 API。多模态模型能够处理文本、图像、音频等多种数据类型，而混合专家（MoE）架构则在每个标记上只激活部分专家以提高效率。思考机器实验室是一家专注于构建协作、可定制企业 AI 系统的人工智能研究与产品公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/">Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights ...</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Inkling 的多模态音频支持和开放权重特性，认为它是企业微调的良好基础，尽管也有指出它并非目前最强的模型。多位评论者强调可以通过 llama.cpp、Unsloth 或 HuggingFace 的量化在本地运行，并希望看到其音频能力的实际表现。还有人期待出现能与之竞争的开源中文模型，并指出现代模型设计的复杂性在不断增加。

**标签**: `#open-weights`, `#multimodal`, `#AI model`, `#Thinking Machines`, `#fine-tuning`

---

<a id="item-3"></a>
## [xAI 开源 Grok Build，包含 Mermaid 渲染器](https://github.com/xai-org/grok-build) ⭐️ 8.0/10

xAI 已发布 Grok Build 的源代码，其构建工具包含一个使用 Unicode 盒绘字符的自包含终端 Mermaid 图表渲染器。 此次发布通过公开代码来应对之前的隐私争议，为开发者提供了可重用的绘图工具以及隐私导向分支的基础。 该仓库包含一个仅使用 Unicode 字符在终端中工作的自包含 Mermaid 图表渲染器，社区分支已去除遥测、选择性数据保留并阻止 x.ai 自动更新。

hackernews · skp1995 · Jul 15, 20:24 · [社区讨论](https://news.ycombinator.com/item?id=48926590)

**背景**: 此前，Grok CLI 工具因会将用户的整个工作目录上传至 xAI 的 Google Cloud 存储桶而受到批评，导致 SSH 密钥、密码管理器数据库等敏感文件被暴露；开源构建工具旨在通过展示代码来重建信任。

**社区讨论**: 评论者指出令人惊讶的 Unicode Mermaid 渲染器，因与埃隆·马斯克的关联而批评 Grok 品牌，并赞赏去除遥测、阻止自动更新的隐私导向分支，尽管也有人承认模型质量不错但对数据外泄表示担忧。

**标签**: `#open-source`, `#AI`, `#build-tools`, `#privacy`, `#Mermaid`

---

<a id="item-4"></a>
## [Stripe 和 Advent 联合报价超过 530 亿美元收购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 8.0/10

据路透社援引消息人士报道，Stripe 与私募股权公司 Advent 联合提出收购 PayPal 的报价超过 530 亿美元。 此次交易将合并两家最大的在线支付平台，引发重大反垄断担忧，并可能重塑数字支付市场的竞争格局。 该报价将 PayPal 估值超过 530 亿美元，分析师指出，将 Stripe、PayPal、Venmo、Braintree 和 Xoom 合并将导致卡不在场（CNP）交易市场高度集中。

hackernews · rvz · Jul 15, 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: Stripe 是一家为在线商户提供支付处理基础设施的技术公司，而 PayPal 运营着广泛使用的数字钱包，并拥有 Venmo、Braintree 和 Xoom 等子公司。Advent 是一家私募股权公司，以在各个行业进行大规模收购而闻名。将这些实体合并将使新所有者控制相当大比例的在线卡不在场（CNP）支付量，从而引起监管机构对潜在反竞争效应的审查。

**社区讨论**: 评论者普遍担心此次合并将大幅提高市场集中度，引发反垄断审查，并可能导致费用上升或商户政策更加严格。还有人对交易的战略逻辑表示怀疑，警告整合过程困难且不确定合并后的公司是否真的能惠及用户或股东。少数人认为此举早该发生，但多数强调需要剥离诸如 Venmo 和 Braintree 等重叠业务以监管顾虑。

**标签**: `#Payments`, `#Mergers & Acquisitions`, `#Antitrust`, `#Stripe`, `#PayPal`

---

<a id="item-5"></a>
## [Model Combination in Risk Sharing under Ambiguity](https://arxiv.org/abs/2504.02987) ⭐️ 8.0/10

The authors characterize optimal risk sharing contracts when an agent faces model uncertainty, using a chi-squared divergence-based criterion and proving admissibility and verification conditions.

rss · arXiv Quantitative Finance · Jul 15, 04:00

**标签**: `#risk sharing`, `#model uncertainty`, `#ambiguity aversion`, `#chi-squared divergence`, `#optimal contract`

---

<a id="item-6"></a>
## [Taming Tail Risk: Regime-Weighted Conformal Calibration for Nonstationary Value-at-Risk](https://arxiv.org/abs/2602.03903) ⭐️ 8.0/10

Proposes regime-weighted conformal calibration to improve VaR forecasts under nonstationary market conditions, validated on long-term equity data.

rss · arXiv Quantitative Finance · Jul 15, 04:00

**标签**: `#Value-at-Risk`, `#Conformal Prediction`, `#Regime Switching`, `#Financial Risk Management`, `#Quantitative Finance`

---

<a id="item-7"></a>
## [基于 LLM 的故事期望建模框架](https://arxiv.org/abs/2412.15239) ⭐️ 8.0/10

该论文提出了一种生成框架，利用大语言模型产生想象的故事续篇，并提取情感、 narrativa 路径等可解释特征来建模消费者的前瞻性故事期望。通过问卷调查和理性期望两种互补验证方法，分别在受控实验室问卷数据和在线阅读平台的观测数据上进行了验证。 提供了一种基于 LLM 的可扩展方法来衡量叙事期望，将计算方法与人类故事处理联系起来，为内容创作者、平台和计算社会科学研究者提供了实际价值。研究表明，模型衍生的期望能够预测读者在已消费内容之外的参与度。 该方法从预训练的大语言模型生成多个故事续篇，提取理论驱动的特征（如情感、叙事路径），并通过两种互补验证程序进行验证：基于问卷的人类信念比较和基于理性期望的实际故事结果比较。结果表明，LLM 衍生的期望在所有研究特征上既与人类报告的信念相关，也与实际故事续篇相关，并且能够在已消费内容之外预测参与度。

rss · arXiv Quantitative Finance · Jul 15, 04:00

**背景**: 读者会对故事接下来会发生什么形成期望，这些期望会影响他们的参与度、满意度以及后续行为。大型语言模型能够生成合理的文本续篇，因而成为近似此类前瞻性信念的自然候选者。然而，将原始模型输出转化为与心理学构造相符的可解释、理论驱动的特征仍然具挑战性。

**标签**: `#LLMs`, `#narrative modeling`, `#story expectations`, `#computational social science`, `#natural language processing`

---

<a id="item-8"></a>
## [基于 Transformer 的注意力机制用于非线性混合频率因子模型。](https://arxiv.org/abs/2601.16274) ⭐️ 8.0/10

本文提出了混合面板 Transformer 编码器（MPTE），利用 Transformer 风格的注意力机制在混合频率面板数据中估计非线性因子模型，通过自适应重加权扩展了经典因子模型并提供理论保证。 MPTE 提供了一种统一的方法来处理不同频率的变量并捕捉非线性关系，通过迁移学习实现效率提升，并增强宏观经济预测的可解释性。 在线性激活下，MPTE 得到的一致且渐近正态的因子和载荷估计器，将经典因子模型作为特例，并通过辅助面板间的迁移学习实现效率提升；在模拟以及对 13 个美国季度宏观目标（来源于 48 个 FRED 序列）的实证应用中，其表现与基准方法相当。

rss · arXiv Quantitative Finance · Jul 15, 04:00

**背景**: 因子模型通过提取少数公共因子来概括高维数据，传统上假设线性信号生成和均匀的采样频率。混合频率数据指变量在不同时间间隔（如月度与季度）被观测到，这使得标准因子分析难以直接应用。Transformer 架构利用自注意力机制在时间和序列间自适应地加权信息，从而在无需手动对齐的情况下实现灵活聚合。通过将注意力机制引入因子建模，MPTE 克服了线性、同频方法的局限性。

**标签**: `#factor models`, `#attention mechanism`, `#mixed-frequency data`, `#Transformer`, `#econometrics`

---