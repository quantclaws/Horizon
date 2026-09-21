---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> From 23 items, 6 important content pieces were selected

---

1. [Polars 发布 py-2.0.0-rc.2 候选版，包含破坏性更改、新增 Map 类型及性能提升](#item-1) ⭐️ 8.0/10
2. [三星预计明年将 HBM4 和 HBM4E 产能提升超过一倍。](#item-2) ⭐️ 8.0/10
3. [ChatGPT 通过广告追踪像素监控跨站浏览](#item-3) ⭐️ 8.0/10
4. [对斯诺登档案的命运进行考察。](#item-4) ⭐️ 8.0/10
5. [Qwen 发布 7B 参数开放权重文本到图像模型 Image 2.1，支持原生透明度](#item-5) ⭐️ 8.0/10
6. [陶哲轩质疑在 AI 进步下人类数学家的必要性](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Polars 发布 py-2.0.0-rc.2 候选版，包含破坏性更改、新增 Map 类型及性能提升](https://github.com/pola-rs/polars/releases/tag/py-2.0.0-rc.2) ⭐️ 8.0/10

Polars 发布了 py-2.0.0-rc.2，这是即将到来的 2.0 版本的候选版本。该版本引入了如将 Parquet ENUM 读取为 pl.String、废弃 cut/qcut 等破坏性更改，新增 Map 数据类型，并带来众多性能优化。 此次发布标志着 Polars 向主要的 2.0 版本过渡，用户需要适应破坏性更改，同时获得如 Map 类型这样的新功能，以支持灵活的键值列。性能改进集中在 Parquet 扫描、连接顺序和内存使用方面，将显著提升数据密集型工作负载的效率。 重要更改包括 PR #29331（将 Parquet ENUM 读取为 pl.String）、PR #28984（引入 Map 类型）以及 PR #29329（废弃 cut/qcut）。性能工作涵盖 PR #29397 至 #29092，诸如谓词下推顺序调整、浮点字面量处理、OOM 修复以及连接顺序优化等。

github · github-actions[bot] · Sep 20, 17:36

**背景**: Polars 是一种用 Rust 实现的高性能 DataFrame 库，提供 Python 绑定，支持即时和惰性两种 API，其列式执行模型类似于 Apache Arrow。它通过并行和缓存友好的算法实现快速数据操作，常被视为 pandas 的替代品。2.0 系列旨在稳定 API，同时引入新数据类型和执行改进，以进一步提升易用性和性能。

**标签**: `#polars`, `#python`, `#dataframe`, `#release`, `#performance`

---

<a id="item-2"></a>
## [三星预计明年将 HBM4 和 HBM4E 产能提升超过一倍。](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) ⭐️ 8.0/10

三星预计将 HBM4 和 HBM4E 的产能提升超过一倍，以满足 AI 硬件制造商日益增长的需求。 这一提升将缓解 AI 加速器供应链中的关键瓶颈，使 GPU 和 ASIC 性能得到提升，并影响全球 DRAM 定价及内存厂商之间的竞争。 三星计划采用其 1c（10nm 级）DRAM 基础晶圆和先进封装技术扩产，针对 HBM4 的 2,048 针接口和 HBM4E 的 512 位外部接口，以实现最高 16 层堆叠。

hackernews · giuliomagnifico · Sep 20, 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49778029)

**背景**: 高带宽内存（HBM）是一种堆叠 DRAM 技术，能够提供极高的内存带宽且功耗低，对 AI 加速器至关重要。HBM4 标准由 JEDEC 于 2025 年 4 月批准，将 I/O 引脚数量翻倍至 2,048，提供数 TB/s 的带宽。HBM4E 保留 HBM4 核心但采用更窄的 512 位外部接口，使其能够在标准有机基板上实现高带宽，无需硅间隔器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiconductor.samsung.com/dram/hbm/hbm4/">HBM4 | DRAM | Samsung Semiconductor Global</a></li>
<li><a href="https://www.jedec.org/standards-documents/docs/jesd270-4a">High Bandwidth Memory (HBM4) DRAM | JEDEC</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，HBM 产能而非处理器或光刻设备是中国 AI 加速器产量的主要瓶颈，并称赞了晶圆薄化工艺的可扩展性。他们还质疑为什么 HBM 不用于消费电子，警告可能导致消费者 DRAM 价格上涨，并怀疑产能提升是否能满足 AI 的需求。

**标签**: `#HBM`, `#Samsung`, `#AI hardware`, `#memory technology`, `#semiconductor supply`

---

<a id="item-3"></a>
## [ChatGPT 通过广告追踪像素监控跨站浏览](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) ⭐️ 8.0/10

文章报道称，ChatGPT 现在嵌入了标准的广告追踪像素，用于收集用户在其他网站上的浏览活动数据，实现跨站追踪。 此发展凸显了 AI 产品正在采用侵入性广告技术，引发严重隐私担忧，并可能招致监管审查。 该追踪机制依赖一个微小的不可见像素或 JavaScript 片段，在加载 ChatGPT 时触发，将浏览数据发送至第三方广告网络；Firefox、Brave 和 Safari 默认会阻止它，而 Chrome 和 Edge 不会。

hackernews · lmbbuchodi · Sep 20, 15:18 · [社区讨论](https://news.ycombinator.com/item?id=49776729)

**背景**: 追踪像素是一种小型且通常不可见的图像或脚本，当用户访问页面时加载，并将访问信息发送给分析或广告平台。第三方 Cookie 使得被访问域以外的域能够在用户浏览器中存储数据，从而实现跨站追踪浏览模式和偏好。这些技术在广告技术中被广泛用于构建用户画像以进行定向广告，但也引发隐私担忧，因为它们可以在未经明确同意的情况下监控用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalmarketer.com/blog/what-is-tracking-pixel/">What is a Tracking Pixel—Explained in 800 Words or Less | DigitalMarketer</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Third-party_cookies">Third-party cookies - Privacy on the web | MDN</a></li>
<li><a href="https://improvado.io/blog/what-is-tracking-pixel">What Is a Tracking Pixel? Complete 2026 Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎欧盟遏制此类做法的努力，指出虽然立法可能令人烦恼，但它保护了消费者隐私。其他人则对标准广告技术如今被用于 AI 聊天产品感到不适，有人开玩笑说可能存在来自 OpenAI 的推荐返佣。有用户指出，Firefox、Brave 和 Safari 会阻止该追踪，而 Chrome 和 Edge 不会。

**标签**: `#AI`, `#Privacy`, `#Web Tracking`, `#ChatGPT`, `#AdTech`

---

<a id="item-4"></a>
## [对斯诺登档案的命运进行考察。](https://libroot.org/posts/what-happened-to-the-snowden-archive) ⭐️ 8.0/10

文章考察了斯诺登档案的去向，指出媒体报道减少、公众兴趣转移，以及对新闻业和负责任披露机密信息的影响。 这凸显了注意力减弱如何影响对监控项目的监督，并引发了在公众情绪变化中负责任披露长期可行性的疑问。 文章引用了拦截者的斯诺登档案系列，指出斯诺登在俄罗斯仍保有副本，并讨论了奥弗顿窗口的转变以及公众对其揭露的漠然态度。

hackernews · EXHades · Sep 20, 22:35 · [社区讨论](https://news.ycombinator.com/item?id=49780820)

**背景**: 爱德华·斯诺登是前美国国家安全局承包商，他在 2013 年泄露了一大批被归类为机密的文件，这些文件合称为斯诺登档案，揭露了全球监控项目。负责任披露是指以最小化潜在伤害的方式将此类信息交给记者和公众，以促进民主辩论。奥弗顿窗口描述的是在公共话语中被容忍的思想范围，这一范围会随时间推移而变化。最初对该档案的媒体报道激增，但随后随着新闻周期的转移而减弱。

**社区讨论**: 评论者指出媒体对斯诺登档案的兴趣已经减弱，公众看法也发生了转移，有人认为这些揭露如今已经变得司空见惯。几位评论者提到奥弗顿窗口的变化，并质疑负责任披露是否仍有意义，同时也有人指出斯诺登仍保有文件副本，尽管身在俄罗斯仍具影响力。

**标签**: `#Snowden`, `#privacy`, `#surveillance`, `#journalism`, `#responsible disclosure`

---

<a id="item-5"></a>
## [Qwen 发布 7B 参数开放权重文本到图像模型 Image 2.1，支持原生透明度](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen 宣布发布 Image 2.1，这是一个 7B 参数的开放权重文本到图像模型，能够原生输出带透明度的 RGBA 图像，并具有改进的文本渲染能力。 该模型提供了一个体积小巧、支持原生透明度的开放权重替代方案，满足对更小、可编辑 AI 生成图像的需求，并引发了关于其许可证及相较于更大模型性能的讨论。 该模型基于 32 层 Single-Stream DiT 架构，可生成最高 2K 分辨率的图像，输出真实的 alpha 通道，并采用比之前 Qwen 模型更为严格的许可证发布。

hackernews · jmillikin · Sep 20, 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**背景**: 开放权重模型指的是其训练得到的参数被公开下载，任何人都可以在自己选择的硬件上运行和检查模型，尽管训练代码和数据可能仍然闭源。原生透明度是指模型能够直接生成带有 alpha 通道的图像，从而在不需要后处理的情况下实现透明背景。Qwen 是阿里巴巴的一系列大型多模态模型，Image 2.1 在此基础上推出，参数量仅为 7B，比之前的 20B 版本更小，同时保留了先进的生成和编辑功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">GitHub - QwenLM/Qwen-Image-2.1: Qwen's most powerful open-source image generation model · GitHub</a></li>
<li><a href="https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight">Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and Editing, Now with Transparency</a></li>
<li><a href="https://d-central.tech/mining-glossary/open-weight-model/">Open - Weight Model Meaning | Bitcoin Mining Glossary</a></li>

</ul>
</details>

**社区讨论**: 评论者们强调了该模型的小巧规模（7B 参数，比之前的 20B 版本小）和原生透明度作为显著优势，有人称赞其文本渲染优于其他开放权重模型。另一些人则指出 GitHub 上显示的更为严格的许可证，对商业使用提出担忧，并询问如何像使用 llama-server 那样在本地运行该模型。总体而言，讨论反映了对模型能力的兴奋，同时也伴随着许可证和使用便利性的疑虑。

**标签**: `#AI`, `#image generation`, `#Qwen`, `#open-weight models`, `#text-to-image`

---

<a id="item-6"></a>
## [陶哲轩质疑在 AI 进步下人类数学家的必要性](https://terrytao.wordpress.com/2026/09/19/why-do-we-need-human-mathematicians-anymore/) ⭐️ 8.0/10

2026 年 9 月 19 日，陶哲轩在其博客发表文章，质疑在 AI 进步下人类数学家是否仍然必要，认为理解、创造力和提出新问题仍是人类独有的角色。 该文章凸显了关于 AI 在数学发现中角色的持续辩论，影响研究者对人工智能协作的看法以及纯数学的未来方向。 陶哲轩强调，尽管 AI 可以辅助证明搜索和计算，但它缺乏真正的理解和提出新数学问题的能力，这一点得到了引用《巴别图书馆》和数学分形特性的评论者的呼应。

hackernews · auggierose · Sep 20, 10:49 · [社区讨论](https://news.ycombinator.com/item?id=49774521)

**背景**: 近年来，诸如大型语言模型和自动定理证明器之类的 AI 系统被用于辅助证明验证、猜想生成和符号计算。陶哲轩是享有盛誉的菲尔兹奖得主，以其在调和分析、偏微分方程和加性数论方面的工作而闻名，他经常探讨 AI 对数学实践的影响。该文章为关于机器是否能够真正复制人类在科学中的洞察力和创造力的更广泛讨论作出了贡献。

**社区讨论**: 评论者强调，没有人类的理解，AI 生成的结果仍然毫无意义，将其比作《巴别图书馆》——信息只有在被解释后才具有意义。其他人指出数学具有无限的分形特性，解决问题会不断产生新问题，因此 AI 不可能穷尽整个领域。少数人推测 AI 可能最终引领数学研究，而怀疑者则指出当前的 AI 仅仅是依赖人类产生知识的复杂暴力搜索。

**标签**: `#mathematics`, `#AI`, `#human-AI collaboration`, `#philosophy of science`, `#Terry Tao`

---