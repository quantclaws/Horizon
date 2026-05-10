---
layout: default
title: "Horizon Summary: 2026-05-10 (ZH)"
date: 2026-05-10
lang: zh
---

> From 22 items, 3 important content pieces were selected

---

1. [研究发现主流 AI 回答偏向日本和美国](#item-1) ⭐️ 8.0/10
2. [NASA 推进新型旋翼技术突破](#item-2) ⭐️ 8.0/10
3. [报告揭秘中国 Claude API 灰产：一折低价背后是数据窃取与模型掉包](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [研究发现主流 AI 回答偏向日本和美国](https://cybernews.com/ai-news/every-ai-answer-japan/) ⭐️ 8.0/10

巴斯克大学和卡迪夫大学的研究测试了八个主流大模型，覆盖 24 种语言，共 31,680 个文化问题，发现模型倾向于将答案锚定在日本或美国，其中五个模型更偏向日本，两个更偏向美国。 该研究表明，这种文化偏差主要是在监督微调阶段形成的，可能影响多语言环境下 AI 系统的公平性和可靠性，凸显了需要更平衡的训练数据。 偏差来源于监督微调阶段，基础预训练模型相对均衡；低资源语言更容易输出指向本国的回答。

telegram · zaihuapd · May 9, 10:02

**背景**: 监督微调（SFT）是在预训练模型上使用标注数据进行进一步训练，以使其适应特定任务，是开发大型语言模型的常见步骤。低资源语言是指数字文本和语言资源有限的语言，这使得模型难以学习准确的表示。LLM 中的文化偏差指的是模型输出中反映训练数据中文化视角过度代表的系统性倾向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)">Fine - tuning (deep learning) - Wikipedia</a></li>
<li><a href="https://poeditor.com/blog/low-resource-languages/">Low - resource languages : A localization challenge - POEditor Blog</a></li>
<li><a href="https://arxiv.org/pdf/2604.21751">Why are all LLMs Obsessed with Japanese Culture ? On the Hidden...</a></li>

</ul>
</details>

**标签**: `#AI bias`, `#LLM`, `#cultural bias`, `#supervised fine-tuning`, `#multilingual`

---

<a id="item-2"></a>
## [NASA 推进新型旋翼技术突破](https://arstechnica.com/space/2026/05/engineers-at-nasas-jet-propulsion-lab-make-a-breakthrough-in-rotor-technology/) ⭐️ 8.0/10

NASA engineers have developed a new rotor design that improves lift and efficiency in thin Martian atmospheres, paving the way for larger, more capable next-generation Mars flyers.

telegram · zaihuapd · May 9, 14:21

**标签**: `#NASA`, `#rotor technology`, `#Mars exploration`, `#aerospace engineering`, `#space technology`

---

<a id="item-3"></a>
## [报告揭秘中国 Claude API 灰产：一折低价背后是数据窃取与模型掉包](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data) ⭐️ 8.0/10

牛津中国政策实验室研究员 Zilan Qian 的调查显示，中国的灰市代理服务以官方价格十分之一甚至更低的价格转售 Anthropic 的 Claude 模型访问权，同时收集用户的提示词和输出，并经常用更便宜或国产模型冒充高端 Claude Opus。 此行为将使用户面临严重的隐私和安全风险，包括专有代码和商业机密被盗，并通过促进模型欺诈和非法数据收集用于模型蒸馏，破坏合法的 AI 服务市场。 这些代理运营商通过盗刷信用卡、批量注册账户或招募低收入国家人员完成身份验证来获取访问权；随后他们要么返回廉价模型的结果，要么收集用户的提示词和输出转售作为模型蒸馏的训练数据。

telegram · zaihuapd · May 10, 01:48

**背景**: Anthropic 的 Claude API 提供对其大型语言模型（包括高端 Claude Opus 变体）的编程访问，正常情况下需支付较高费用。在中国，灰市形成了一套通过非官方渠道转售该访问的代理服务生态系统，常常利用被盗凭证或招募低成本验证者等欺诈手段降低成本。这些代理经常将用户请求的模型替换为更便宜或本地开发的模型，并收集用户的提示词和输出，这些数据可用于模型蒸馏——即通过大型模型的输出训练较小模型以复制其能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data">Chinese grey market sells Claude API access at 90% off by using stolen credentials, model substitution, and harvesting users' prompts and outputs for resale as AI training data — 'transfer stations' operate through proxy networks that harvest user data | Tom's Hardware</a></li>
<li><a href="https://letsdatascience.com/news/grey-market-proxies-resell-claude-api-access-at-discount-7a0032fe">Grey-market proxies resell Claude API access at discount | Let's Data Science</a></li>
<li><a href="https://www.scmp.com/tech/big-tech/article/3296827/deepseeks-ai-distillation-theft-openai-seeks-answers-over-chinas-breakthrough">OpenAI says DeepSeek stole its AI data, but how common is ‘distillation’?</a></li>

</ul>
</details>

**标签**: `#AI security`, `#Claude API`, `#grey market`, `#data privacy`, `#model fraud`

---