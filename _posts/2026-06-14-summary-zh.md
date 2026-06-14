---
layout: default
title: "Horizon Summary: 2026-06-14 (ZH)"
date: 2026-06-14
lang: zh
---

> From 15 items, 10 important content pieces were selected

---

1. [人口普查局禁止在统计产品中使用噪声注入](#item-1) ⭐️ 8.0/10
2. [GLM-5.2 开放权重大语言模型由 Z.ai 发布](#item-2) ⭐️ 8.0/10
3. [每帧完美：macOS UI 中的不完美帧如何提升感知运动](#item-3) ⭐️ 8.0/10
4. [治疗胰腺肿瘤可能揭示癌症的主开关](#item-4) ⭐️ 8.0/10
5. [亚马逊 CEO 与美国官员会谈引发对 Anthropic AI 模型的监管打压](#item-5) ⭐️ 8.0/10
6. [德比郡警官因使用 AI 制造证据被调查](#item-6) ⭐️ 8.0/10
7. [谷歌提出利用退役智能手机的低碳计算平台](#item-7) ⭐️ 8.0/10
8. [RTX 5080 加 RTX 3090 配置在 Qwen 3.6 27B Q8 上达到约 80 Tok/s](#item-8) ⭐️ 8.0/10
9. [阿拉伯排版渲染挑战与技术债务](#item-9) ⭐️ 8.0/10
10. [Pyodide 314.0 实现 WASM 轮子发布到 PyPI](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [人口普查局禁止在统计产品中使用噪声注入](https://desfontain.es/blog/banning-noise.html) ⭐️ 8.0/10

特朗普政府发布命令，禁止人口普查局和经济分析局在发布的统计产品中使用噪声注入——一种用于保护个人隐私的差分隐私技术。 移除噪声注入削弱了隐私保证，增加了重新识别的风险，并削弱了公众对政府数据收集的信任。 该命令指示机构优先使用粗化和抑制而非任何基于随机性的方法，实际上终止了自 2020 年人口普查起使用的差分隐私。

hackernews · nl · Jun 13, 13:54 · [社区讨论](https://news.ycombinator.com/item?id=48517377)

**背景**: 差分隐私是一种数学框架，通过向查询结果添加校准噪声来防止个人身份被识别，同时保持数据的整体实用性。噪声注入是该框架中的主要技术，人口普查局曾使用它来保护 2020 年人口普查数据免受重建攻击。先前的研究表明，未加此类保护的聚合人口普查数据可能被逆推以揭示个人信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2026/06/12/nx-s1-5855734/census-bureau-data-differential-privacy">A Trump push to cut 'statistical noise' could mean less data from the Census Bureau</a></li>
<li><a href="https://desfontain.es/blog/banning-noise.html">Banning noise will be a disaster for statistical data ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Differential_privacy">Differential privacy - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者担心禁令会削弱信任，可能导致敏感数据被滥用，并使强大行为者能够重建个人记录；少数人认为国家需要细粒度数据以进行有效政策制定。

**标签**: `#data privacy`, `#differential privacy`, `#Census Bureau`, `#government data`, `#statistics`

---

<a id="item-2"></a>
## [GLM-5.2 开放权重大语言模型由 Z.ai 发布](https://twitter.com/jietang/status/2065784751345287314) ⭐️ 8.0/10

Z.ai 宣布发布 GLM-5.2，这是一种新的开放权重大语言模型，正值关于开放 AI 访问和美国对前沿模型限制的讨论之际。 此次发布凸显了开放权重模型与地缘政治限制之间的张力，提供了一种可自由获取的替代方案，有可能普及前沿人工智能能力。 GLM-5.2 采用 permissive 许可证发布，其发布时间正值美国政府致 Anthropic 的限制模型访问的信件之时，但尚未发布官方基准结果。

hackernews · aloknnikhil · Jun 13, 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48518684)

**背景**: Z.ai 前身为 Zhipu AI，研发 GLM（通用语言模型）系列大语言模型，自 2025 年 7 月起采用 MIT 许可证开源发布。其前身模型 GLM-5 具有 745B 参数、44B 激活参数的混合专家架构，展示出前沿水平的推理和编码能力。开放权重大语言模型使模型参数公开可得，允许免费使用、修改和复现，这与受许可证或地缘政治限制的受限权重模型形成对比。美国最近将多家中国 AI 公司列入实体清单，加剧了对前沿模型获取的担忧，从而推动了对开放权重替代方案的呼声。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://glm5.net/">GLM-5 | Zhipu AI's Next-Generation Large Language Model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z.ai - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/open-weight-large-language-models-llms">Open-Weight Large Language Models - emergentmind.com</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞中国 AI 实验室保持开放并以许可证宽松的方式发布模型，这与美国的限制形成对比。多位评论者指出此次发布的时间正值 Anthropic 受限信件发布之际，认为开放权重模型能免受地缘政治限制。总体情绪支持开放权重模型的发布，作为应对前沿模型获取限制的战略回应。

**标签**: `#GLM-5.2`, `#large language models`, `#open source AI`, `#AI geopolitics`, `#model release`

---

<a id="item-3"></a>
## [每帧完美：macOS UI 中的不完美帧如何提升感知运动](https://tonsky.me/blog/every-frame-perfect/) ⭐️ 8.0/10

文章认为，macOS UI 动画中看似不完美或错位的帧实际上通过利用人类视觉系统的特性来增强平滑运动的感知。 了解如何通过故意的不完美来提升感知运动可以帮助设计师创建更有效的动画，使其在不需要更高帧率的情况下感觉更响应。 作者引用了 macOS 中的特定 UI 元素——如摇晃的保存对话框、Notes 窗格过渡以及 Preview 的光标滞后——作为例子，说明这些看似不完美的帧如何利用时间别帧和帧丢弃技巧欺骗眼睛看到更平滑的运动。

hackernews · ravenical · Jun 13, 11:40 · [社区讨论](https://news.ycombinator.com/item?id=48516251)

**背景**: 人类视觉通过离散的采样来感知运动，大脑在这些样本之间进行插值以产生平滑的感知，这一原理被运动模糊和时间反走样等技术所利用。在计算机图形学中，有意丢帧或引入轻微的偏移可以减少抖动并在采样与眼睛的时间分辨率相匹配时提升感知流畅度。macOS 在其界面中使用了许多细微的动画，帧时序的变化往往是渲染管线的副产物，也可以被用来获得感知上的好处。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Temporal_anti-aliasing">Temporal anti-aliasing - Wikipedia</a></li>
<li><a href="https://rd.springer.com/content/pdf/10.1007/s42486-021-00059-1.pdf">How does frame-loss affect users perception of smoothness?</a></li>
<li><a href="https://forums.macrumors.com/threads/discussion-why-does-osx-lag-in-ui-animation-when-compared-to-windows.1844493/">(Discussion) Why does OSX lag in UI animation when compared to Windows? | MacRumors Forums</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人承认某些动画瑕疵可能是有益的，也有人认为文章的例子仅仅是 bug，且缺乏有力证据或替代方案。多位用户希望看到去除这些“不完美”帧的对比，并质疑所展示的所有运动是否真的必要。

**标签**: `#UI/UX`, `#animation`, `#human-computer interaction`, `#macOS`, `#design`

---

<a id="item-4"></a>
## [治疗胰腺肿瘤可能揭示癌症的主开关](https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch) ⭐️ 8.0/10

研究发现，治疗胰腺肿瘤揭示了 KRAS 驱动癌症的一个关键弱点，暗示可能存在癌症治疗的主开关。该研究强调了实验药物达拉克西布（daraxonrasib），它能够靶向存在于大多数胰腺肿瘤中的 KRAS 突变。 这一发现解决了肿瘤学中长期存在的挑战，表明曾被认为不可成药的 KRAS 现在可以被靶向，这有望改善众多 KRAS 驱动癌症的预后。它还为开发针对其他‘不可成药’蛋白质的疗法提供了概念验证，可能重塑药物发现格局。 该弱点在约 20%的检查肿瘤中被观察到，方法是通过小分子达拉克西布抑制突变型 KRAS。然而，目前只有某些 KRAS 等位基因（如 G12C）可以被靶向，且临床疗效仍需在更大规模试验中验证。

hackernews · andsoitis · Jun 13, 13:34 · [社区讨论](https://news.ycombinator.com/item?id=48517199)

**背景**: KRAS 是一种 GTP 结合蛋白，突变后会被锁定在活跃状态，驱动胰腺腺癌等癌症的不受控制的细胞增殖。数十年来，KRAS 因其光滑表面缺乏深度口袋而被认为是不可成药的，这限制了小分子药物的研发。胰腺癌是最致命的恶性肿瘤之一，五年生存率低于 10%，且约 90%的病例携带 KRAS 突变。最近的共价抑制剂和生物制剂进展开始克服这些障碍，使得达拉克西布等靶向策略成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scienceinsights.org/what-is-a-kras-mutation-and-how-does-it-drive-cancer/">What Is a KRAS Mutation and How Does It Drive Cancer?</a></li>
<li><a href="https://bmjoncology.bmj.com/content/4/1/e000946">KRAS-targeted therapies in cancer: novel approaches and ...</a></li>
<li><a href="https://www.mskcc.org/news/new-kras-targeted-therapy-shows-promise-against-pancreatic">New KRAS Targeted Therapy Shows Promise Against Pancreatic Cancer</a></li>

</ul>
</details>

**社区讨论**: 评论者指出文章标题夸大其词，认为所发现的弱点仅适用于大约 20%的肿瘤，而非所有癌症。其他人则强调终于能够靶向曾被认为不可成药的 KRAS 的重要性，并分享了相关临床试验和研究存档的链接。还有一条评论表达了对美国科学经费削减提案的担忧，担心这将危及未来的研究。

**标签**: `#cancer research`, `#KRAS`, `#drug discovery`, `#oncology`, `#biomedical breakthrough`

---

<a id="item-5"></a>
## [亚马逊 CEO 与美国官员会谈引发对 Anthropic AI 模型的监管打压](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578?st=Yct6gx&reflink=desktopwebshare_permalink) ⭐️ 8.0/10

亚马逊首席执行官安迪·贾西最近与美国政府官员的会谈促使监管机构审查并限制 Anthropic 的 Claude AI 模型的部署，理由是安全和对齐问题。 此事件凸显了企业快速推进 AI 与政府监管之间日益加剧的摩擦，可能影响大型科技公司与 AI 初创企业的合作方式，并塑造未来的 AI 监管格局。 亚马逊是 Anthropic 的主要投资者，且 AWS 与 Anthropic 合作开展 Project Glasswing 项目，旨在发现开源和关键基础设施软件中的漏洞；社区评论指出人们对模型越狱限制的担忧以及缺乏明确的监管门槛。

hackernews · ls612 · Jun 13, 16:57 · [社区讨论](https://news.ycombinator.com/item?id=48519092)

**背景**: Anthropic 开发了 Claude 系列大型语言模型，这些模型采用宪法 AI 技术进行训练，以提升伦理和法律合规性。自 Claude 3 起，模型以 Haiku、Sonnet 和 Opus 三种规模发布，此外还有如 Claude Mythos 等面向特定企业客户的专用版本。AI 社区近期的讨论强调了需要安全措施和监管框架来应对诸如越狱和滥用等 LLM 风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://www.confident-ai.com/blog/the-comprehensive-llm-safety-guide-navigate-ai-regulations-and-best-practices-for-llm-safety">The Comprehensive LLM Safety Guide: Navigate AI regulations ...</a></li>
<li><a href="https://github.com/requie/LLMSecurityGuide">️ LLM Security 101: The Complete Guide (2026 Edition)</a></li>

</ul>
</details>

**社区讨论**: 评论者对监管行动的依据表示怀疑，认为所有 LLM 都可被越狱，质疑 Anthropic 模型据称超越了哪些具体限制。有人引用汉隆剃刀，认为这可能是误解而非恶意意图；也有人指出技术担忧，如提示注入漏洞以及 Opus 4.8 与 Fable 等模型之间的差异。

**标签**: `#AI regulation`, `#Anthropic`, `#Amazon`, `#AI policy`, `#LLM safety`

---

<a id="item-6"></a>
## [德比郡警官因使用 AI 制造证据被调查](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661) ⭐️ 8.0/10

据天空新闻报道，德比郡的一名警官因涉嫌使用人工智能在多起刑事案件中制造或伪造证据而正接受调查。 此案凸显了人工智能在执法中被滥用的日益增长的担忧，威胁司法证据的完整性，并促使人们呼吁对警方使用的 AI 工具进行更严格的监督。 调查集中在该警官利用人工智能生成或篡改证据材料上，但德比郡警方尚未透露所涉及的具体伪造证据类型（如深度伪造视频、修改后的照片）。

hackernews · austinallegro · Jun 13, 19:54 · [社区讨论](https://news.ycombinator.com/item?id=48520807)

**背景**: 人工智能在刑事调查中被越来越多地用于人脸识别、预测性警务和证据分析等任务，但人工智能生成或辅助的证据引发了对其可靠性和可采纳性的质疑。深度伪造技术能够制作出逼真的但虚构的音频、视频或图像，使得区分真实证据与合成媒体变得困难。法院和法律学者正在制定框架来评估人工智能生成数据的证据价值，并检测合成操纵。专有 AI 工具缺乏透明度进一步复杂化了正当程序和公众信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.americanbar.org/groups/criminal_justice/resources/magazine/2026-spring/ai-criminal-courts-balancing-innovation-justice/">AI in the Criminal Courts: Balancing Innovation and Justice</a></li>
<li><a href="https://www.unesco.org/en/articles/deepfakes-and-crisis-knowing">Deepfakes and the crisis of knowing | UNESCO</a></li>
<li><a href="https://www.researchgate.net/publication/395329220_Deepfake_Detection_and_Multimedia_Forensics_Investigating_Synthetic_Media_Image_Forgery_and_Video_Manipulation_in_Cybercrime_Cases">(PDF) Deepfake Detection and Multimedia Forensics ...</a></li>

</ul>
</details>

**社区讨论**: 评论者们好奇到底是何种 AI 生成的证据以及是如何被发现的，警告人工智能可能导致各类证据失去可信度，推测该警官的动机，并指出警方未透露证据材料的具体细节。

**标签**: `#AI ethics`, `#law enforcement`, `#deepfakes`, `#evidence tampering`, `#HackerNews`

---

<a id="item-7"></a>
## [谷歌提出利用退役智能手机的低碳计算平台](https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/) ⭐️ 8.0/10

谷歌研究提出一种低碳计算平台，将退役智能手机改造成分布式边缘计算节点，计划在更新系统以关闭省电守护进程后，将 2000 部退役 Pixel 手机主板组成集群。 这种方法通过赋予旧硬件第二次生命，减少电子废弃物和碳排放，同时为研究和工业提供可扩展的低成本边缘计算资源。 该平台需要更新手机操作系统以关闭低内存杀手守护进程等面向消费者的保护机制，使设备能够持续运行工作负载；但性能受硬件异质性、电池限制以及锁定的引导加载程序阻碍安全更新的影响。此外，社区指出专有固件 Blob 和 OEM 支持期限短导致这些设备在失去官方更新后易受攻击。

hackernews · vikas-sharma · Jun 13, 09:38 · [社区讨论](https://news.ycombinator.com/item?id=48515336)

**背景**: 边缘计算通过在许多地理位置分散的节点上分配工作负载，将计算带得更靠近数据来源，常使用异构硬件。低碳计算旨在通过重用现有设备和提高能源效率来最小化信息技术基础设施的环境影响。利用退役智能手机可以发挥其广泛可用性和内置传感器的优势，但需要克服软件锁定、有限的电池寿命以及不稳定的网络条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/">A low-carbon computing platform from your retired phones</a></li>
<li><a href="https://www.technobezz.com/news/google-plans-to-use-2000-retired-pixel-phones-for-low-carbon-computing-clusters">Google Plans to Use 2,000 Retired Pixel Phones for Low-Carbon ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Edge_computing">Edge computing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞让旧手机为边缘工作负载提供第二次生命的想法，指出这类似于过去的爱好者集群，如 PS3 超级计算机，适合运行 CFD 等批处理作业。然而，许多人警告专有固件 Blob、锁定的引导加载程序以及 OEM 短暂的支持期会使退役手机缺乏安全性，若没有强制要求可解锁引导加载程序的法规，则不适合面向互联网的服务。还有人推测离网、后末日场景的使用，既显示热情也凸显实际限制。

**标签**: `#sustainability`, `#edge computing`, `#mobile hardware reuse`, `#Google research`, `#e-waste reduction`

---

<a id="item-8"></a>
## [RTX 5080 加 RTX 3090 配置在 Qwen 3.6 27B Q8 上达到约 80 Tok/s](https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/) ⭐️ 8.0/10

一则 Hacker News 帖子报道，RTX 5080 与 RTX 3090 组合在运行 Qwen 3.6 27B Q8 量化模型时达到约 80 tokens/秒，并分享了最佳推理参数。 此基准表明消费级 GPU 能够提供具有竞争力的大模型推理速度，有助于开发者评估本地部署可行性并为经济高效的 AI 工作负载选择硬件。 Qwen 3.6 27B Q8 模型占用约 39 GB 显存，使得双 GPU 配置能够在 Q8 量化的 KV‑cache 下运行该模型；社区评论建议思考模式使用 `--temp 1.0 --top-p 0.95 --top-k 20` 等参数。

hackernews · iMil · Jun 13, 09:55 · [社区讨论](https://news.ycombinator.com/item?id=48515454)

**背景**: NVIDIA GeForce RTX 5080 于 2025 年 1 月发布，基于 5 nm GB203 GPU，配备 16 GB GDDR7 显存并支持最新的 AI 加速功能。Qwen 3.6 27B Q8 是 Qwen 3.6 27B 模型的 8‑bit 量化版本，内存占用降至约 29 GB，同时保持近乎原始的质量，使其在高端消费级 GPU 上可行。使用 llama.cpp 等工具的多 GPU 推理可以通过 PCIe 在卡之间分割模型层，使得 RTX 5080（16 GB）和 RTX 3090（24 GB）的合计显能够容纳该模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/gpu-specs/geforce-rtx-5080.c4217">NVIDIA GeForce RTX 5080 Specs | TechPowerUp GPU Database</a></li>
<li><a href="https://aiproductivity.ai/news/qwen-36-27b-quantization-bf16-q8-q4km-comparison/">Qwen 3.6 27B Quantization Tested: BF16 vs Q8_0 vs Q4_K_M</a></li>
<li><a href="https://bestgpuforllm.com/articles/best-multi-gpu-setup-for-llm/">Best Multi-GPU Setup for Local LLM in 2026 (Dual) - Best GPU for LLM</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞该配置的性能，有一位用户表示这与他们自己的体验相符，并且在某些任务上更倾向于使用 Qwen 而非 Claude。其他人分享了详细的采样参数和 MTP 建议，而有些人则指出加州的高电费使云服务更具经济性。还有人希望看到在有无 speculative decoding 以及并行解码增强下的性能表现。

**标签**: `#LLM inference`, `#GPU benchmark`, `#Qwen`, `#RTX 5080`, `#performance tuning`

---

<a id="item-9"></a>
## [阿拉伯排版渲染挑战与技术债务](https://lr0.org/blog/p/arabic/) ⭐️ 8.0/10

文章考察了在软件中渲染阿拉伯脚本所涉及的复杂性和累积的技术债务，突出了用户在光标行为和左右混合编辑中的挫败感。 理解这些问题对构建国际化应用的开发者至关重要，因为阿拉伯脚本影响着大量用户，并揭示了复杂文本排布的更广泛挑战。 文章引用了 OpenType 形状特性、HarfBuzz 文本塑形引擎以及 Unicode 双向算法，这些是处理阿拉伯连写行为和从右到左方向性的核心技术。

hackernews · bookofjoe · Jun 13, 12:40 · [社区讨论](https://news.ycombinator.com/item?id=48516710)

**背景**: 阿拉伯文字是一种连写的、从右到左的书写系统，大多数字母会根据其在单词中的位置而改变形状，因而需要上下文塑形和连字应用。正确渲染依赖于 OpenType 布局表、如 HarfBuzz 的塑形引擎以及 Unicode 双向算法来处理左右混合文本的重新排序。长期以来，许多应用通过采取临时的修补而非完整支持这些复杂排版机制，积累了技术债务，导致文章中描述的用户挫败感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/typography/script-development/arabic">Developing OpenType Fonts for Arabic Script - Typography | Microsoft Learn</a></li>
<li><a href="https://github.com/harfbuzz/harfbuzz">GitHub - harfbuzz/harfbuzz: HarfBuzz text shaping engine</a></li>
<li><a href="https://www.unicode.org/reports/tr9/">UAX #9: Unicode Bidirectional Algorithm</a></li>

</ul>
</details>

**社区讨论**: 评论者对阿拉伯用户在混合语言编辑器中遇到的光标行为问题表示同情，指出即使是双语流利的工程师也常转为单语输入以避免挫败感。还有人指出所有脚本都有隐藏的复杂性，分享了关于阿拉伯对齐的学术资源，赞赏阿拉伯文字的美感，并建议更广泛使用脱离字体以减轻渲染问题。

**标签**: `#typography`, `#internationalization`, `#Arabic script`, `#software engineering`, `#technical debt`

---

<a id="item-10"></a>
## [Pyodide 314.0 实现 WASM 轮子发布到 PyPI](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 8.0/10

Pyodide 314.0 现在允许开发者将编译为 WebAssembly（WASM）轮子的 Python 包直接发布到 PyPI，可通过 micropip 在 Pyodide 中安装，无需维护者手动构建。 这减轻了 Pyodide 维护者的负担，扩展了浏览器兼容 Python 包的生态系统，并使任何包作者能够像发布原生轮子一样轻松分发 WASM 轮子。 此功能依赖 PEP 783 中的 PyEmscripten 平台标签，以及在 2026 年 4 月 21 日合并的 PyPI PR（warehouse#19804）。例如，luau‑wasm 包提供一个 276 KB 的轮子（luau_wasm-0.1a0-cp314-cp314-pyemscripten_2026_0_wasm32.whl），可通过 micropip 安装。

rss · Simon Willison · Jun 13, 23:55

**背景**: Pyodide 是将 CPython 移植到 WebAssembly 的项目，使得 Python 包能够在浏览器中运行。WASM 轮子是预编译的二进制分发文件，可直接被 Pyodide 加载，从而避免运行时编译。PEP 783 引入了 PyEmscripten 平台标签，以在 PyPI 上标准化这些轮子，使其能够像普通 Python 轮子一样发布和安装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps.python.org</a></li>
<li><a href="https://pyodide.org/en/314.0.0/development/abi.html">The PyEmscripten Platform — Version 314.0.0 - pyodide.org</a></li>
<li><a href="https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/">Publishing WASM wheels to PyPI for use with Pyodide</a></li>

</ul>
</details>

**标签**: `#Python`, `#WebAssembly`, `#Pyodide`, `#PyPI`, `#packaging`

---