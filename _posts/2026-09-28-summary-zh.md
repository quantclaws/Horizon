---
layout: default
title: "Horizon Summary: 2026-09-28 (ZH)"
date: 2026-09-28
lang: zh
---

> From 12 items, 2 important content pieces were selected

---

1. [Fireworks AI 发布了 Ember-1，这是一个基于 Kimi K3 并在推理过程中使用 40% 更少 token 的模型。](#item-1) ⭐️ 8.0/10
2. [谷歌搜索因 AI 摘要变得奇怪](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Fireworks AI 发布了 Ember-1，这是一个基于 Kimi K3 并在推理过程中使用 40% 更少 token 的模型。](https://fireworks.ai/blog/ember-1) ⭐️ 8.0/10

Fireworks AI 宣布推出 Ember-1，这是一个基于 Kimi K3 的专用模型，在保持相同质量的同时使用大约 40% 更少的 token，并以研究预览形式在其无服务器平台上发布。 Ember-1 表明通过后训练可以提高推理效率，降低开发者成本，并推动更小、更快的开源模型趋势。 Ember-1 通过在 Kimi K3 上进行后训练来缩短推理链，使每次输出的 token 数量减少约 40%；Fireworks 给出的定价为每百万输入 token 3 美元、每百万输出 token 15 美元（亦有提到 4.4 美元/百万输出），并提供两周的无服务器访问以收集社区反馈。

hackernews · gmays · Sep 27, 17:31 · [社区讨论](https://news.ycombinator.com/item?id=49868830)

**背景**: Kimi K3 是一种以强大推理能力著称的大型语言模型，但通常会消耗较多的 token。Fireworks AI 是一个提供模型托管、训练和推理服务的平台，常用于托管和服务开源模型。后训练（如强化学习或微调）可以在不改动模型核心权重的情况下调整其行为，例如让模型产生更短的推理链。通过减少 token 消耗，Ember-1 能降低延迟和成本，使得需要频繁调用的 AI 应用更具可及性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fireworks.ai/blog/ember-1">Introducing Ember-1</a></li>
<li><a href="https://fireworks.ai/">Fireworks AI</a></li>
<li><a href="https://sebastianraschka.com/blog/2026/focusing-on-llm-post-training.html">Focusing on Post-Training | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Ember-1 的效率提升和本地低成本模型训练的可能性表示兴奋，但也有人担心依赖 Fireworks 作为服务提供商，因为它同时扮演模型研究者和 API 供应商的双重角色。其他人指出 Ember-1 的定价相比 Kimi K3 等替代方案更具竞争力，并强调开源模型能够通过社区驱动的改进快于专有模型进步。还有用户讨论了对于简单任务（如代码或命令翻译）“思考更少”的模型的吸引力。

**标签**: `#AI/ML`, `#model release`, `#Fireworks AI`, `#open source`, `#Hacker News discussion`

---

<a id="item-2"></a>
## [谷歌搜索因 AI 摘要变得奇怪](https://sancho.bearblog.dev/google-weird/) ⭐️ 8.0/10

该博客文章讨论了谷歌搜索结果现在在顶部显示 AI 生成的摘要，导致用户困惑，例如在查询哈利法克斯流浪者时出现的情况。 这一变化反映了向对话式答案引擎的更广泛趋势，可能改变用户与信息的互动方式，并引发对准确性和信任的担忧。 AI 摘要错误地宣布哈利法克斯流浪者已经锁定季后赛席位，而用户清楚他们仍排名第五，这展示了 AI 幻觉答案的风险。

hackernews · sancho-panza · Sep 27, 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49870367)

**社区讨论**: 评论者意见分歧：一些人称赞 AI 摘要为普通用户带来的生活质量提升，而另一些人则觉得它们令人不安或具有操纵性，将这种变化与孤独和商业化联系起来；还有一位用户分享了一个无 AI 搜索的替代链接。

**标签**: `#Google`, `#Search`, `#AI`, `#User Experience`, `#HackerNews`

---