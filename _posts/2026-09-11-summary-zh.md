---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> From 41 items, 16 important content pieces were selected

---

1. [Shopify 从 React Native 转回原生 Swift 和 Kotlin 开发](#item-1) ⭐️ 8.0/10
2. [关于研究人员是否可信任 OpenAI 处理未发表数学思想的更多疑问](#item-2) ⭐️ 8.0/10
3. [OpenAI 发布 Agents API，托管式 AI 代理开发](#item-3) ⭐️ 8.0/10
4. [谷歌签署 22 年协议购买芬兰洛维萨核电站 50%输出](#item-4) ⭐️ 8.0/10
5. [Forgejo 16.0.3 及以下版本存在严重远程代码执行漏洞。](#item-5) ⭐️ 8.0/10
6. [微软宣布 Rust 成为一级语言](#item-6) ⭐️ 8.0/10
7. [硅谷在军工复合体中的角色日益增长](#item-7) ⭐️ 8.0/10
8. [Trynix.dev 通过 QEMU-WASM 在浏览器中运行任意 Nix 包](#item-8) ⭐️ 8.0/10
9. [Shopify 因 AI 辅助开发回归原生移动应用。](#item-9) ⭐️ 8.0/10
10. [信息干预降低处方错误：医疗运营中的野外实验](#item-10) ⭐️ 8.0/10
11. [针对 P2P 贷款的表格信用评分进行多攻击鲁棒性评估的对抗训练研究](#item-11) ⭐️ 8.0/10
12. [去中心化交易所套利者之间的 Gas 费竞争建模](#item-12) ⭐️ 8.0/10
13. [AI 编程工具与数字创业：软件专业知识的作用](#item-13) ⭐️ 8.0/10
14. [重建大规模生产网络](#item-14) ⭐️ 8.0/10
15. [生成式 AI 在 FactSet 的应用提升分析师报告丰富度但预测准确率下降](#item-15) ⭐️ 8.0/10
16. [布朗签名的全局普适近似](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Shopify 从 React Native 转回原生 Swift 和 Kotlin 开发](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 宣布将其移动应用从 React Native 迁移回使用 Swift 开发 iOS 和使用 Kotlin 开发 Android 的原生代码库，并阐述了迁移的动机和经验教训。 这一决定凸显了对大型应用跨平台框架日益增长的怀疑，可能影响其他公司在性能与开发速度之间的权衡评估。 Shopify 提到 React Native 在处理复杂 UI 交互和性能方面存在局限，并且他们构建了内部的 Playwright 风格驱动程序以帮助迁移后的自动化测试。

hackernews · fnthawar2 · Sep 10, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是一个基于 JavaScript 的框架，使开发者能够使用单一代码库构建 iOS 和 Android 应用。Swift 是苹果公司用于 iOS 开发的现代编程语言，而 Kotlin 是 JetBrains 开发并得到官方支持的 Android 原生语言。企业有时会采用 React Native 以减少开发工作量，但在需要更好性能或更深层平台集成时可能会转回原生语言。

**社区讨论**: 几位评论者分享了他们自己从 React Native 迁移到原生 Swift/Kotlin 的经验，指出这项工作往往在 LLM 辅助之前就已经完成。其他人则认可 Shopify 的决定，特别是长期主张原生开发的 iOS 工程师。还有几位强调了 Shopify 自定义的 Playwright 风格驱动程序在加速验证方面的实用性，并表示希望了解更多细节。

**标签**: `#mobile development`, `#React Native`, `#Swift`, `#Kotlin`, `#Shopify`

---

<a id="item-2"></a>
## [关于研究人员是否可信任 OpenAI 处理未发表数学思想的更多疑问](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

黑客新闻的一个帖子引发担忧，认为 OpenAI 可能在未经适当署名的情况下，将聊天中共享的未发表数学思想用于模型训练，引发了关于研究诚信和 AI 伦理的争论。 此讨论凸显了若研究者担心其未发表思想被 AI 模型吸收而不获署名，学术合作可能面临风险，从而削弱对 AI 辅助研究的信任。 OpenAI 的政策允许用户退出训练，且临时聊天会在 30 天内自动删除，但评论者指出模型参数可能仍保留此类互动的潜在痕迹。

hackernews · pred_ · Sep 10, 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: 大型语言模型是在巨大的文本语料上训练的，除非用户选择退出，否则用户提供的聊天可能被纳入训练数据，从而影响模型的潜在表示。AI 生成内容的署名问题，尤其是在数学领域，仍然存在争议，因为思想可能在未明确署名的情况下被复制。最近的研究警告，未受控制的 AI 生成数学可能削弱学术文献的溯源性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt">Chat and File Retention Policies in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance">How your data is used to improve model performance | OpenAI Help Center</a></li>
<li><a href="https://arxiv.org/html/2608.02859v1">The crisis of AI-generated mathematics</a></li>

</ul>
</details>

**社区讨论**: 评论者将此情况比作不署名使用他人思想的不道德人类合作者，而另一些人则认为模型改进和独立发现可以共存。还有人质疑在开放问题上的快速进展是否真实，或是受到 monetize AI 服务压力的驱动。

**标签**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#machine learning`, `#mathematics`

---

<a id="item-3"></a>
## [OpenAI 发布 Agents API，托管式 AI 代理开发](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI 发布了 Agents API，这是一项托管服务，使开发者能够创建和运行具备内置工具支持、自动上下文压缩、多代理编排和持久状态管理的 AI 代理。 该 API 通过托管基础设施降低了构建复杂 LLM 代理的门槛，加快了原型开发和生产部署速度，并且通过可选的自托管沙盒减轻了供应商锁定的担忧。 Agents API 围绕 Agent、Environment、Session 和 Events/items 四个核心概念构建，运行 Codex harness，支持 MCP 服务器，并提供自动上下文压缩和可编程工具调用。

hackernews · aquir · Sep 10, 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**背景**: AI 代理将语言模型与工具和记忆结合，以自主方式执行任务，通常要求开发者管理工具执行、上下文窗口和持久状态。Codex harness 是 OpenAI 的内部运行时，为如 Codex 之类的模型提供动力，负责代码执行和环境交互。状态管理即服务指的是在多次调用之间持久化代理的会话数据（如对话历史和工具输出），从而免除开发者自行构建存储方案的需要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents SDK | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/State_management">State management - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏该 API 能够抽象掉复杂的 harness 基础设施，使代理即服务成为可能，同时也有人警告潜在的供应商锁定风险，并主张通过自托管沙盒来缓解。还有人指出在个人环境（如 QEMU 虚拟机）中运行代理的实际价值，并更倾向于直接获取原始推理标记而非更高层次的抽象。总体而言，讨论显示出浓厚兴趣，围绕抽象层次、锁定风险以及替代部署方案展开辩论。

**标签**: `#OpenAI`, `#Agents API`, `#AI development`, `#LLM tools`, `#API`

---

<a id="item-4"></a>
## [谷歌签署 22 年协议购买芬兰洛维萨核电站 50%输出](https://www.bbc.com/news/articles/c8r6y4me2g6o) ⭐️ 8.0/10

谷歌同意在与芬兰公用事业公司 Fortum 签订的 22 年合同中，购买洛维萨核电站最高 50%的电力输出，以供其数据中心使用。 此协议为谷歌不断扩张的 AI 驱动数据中心提供了大规模、低碳且可靠的电力来源，凸显了科技公司锁定清洁能源以满足算力增长和气候承诺的趋势。 洛维萨核电站拥有两座 VVER-440 压水反应堆，每机组约 507 MW，总装机容量约 1 GW；谷歌的份额最高可达约 500 MW。22 年的合同期限以及芬兰凉爽的气候、低碳电网和相对未拥堵的输电网使该地点对数据中心运营商具有吸引力。

hackernews · lukaspetersson · Sep 11, 00:42 · [社区讨论](https://news.ycombinator.com/item?id=49652105)

**背景**: 芬兰的电力结构中核能和可再生能源占比较高，导致其电力碳强度在欧洲较低。由 Fortum 运营的洛维萨核电站拥有两座苏联设计的 VVER-440 反应堆，提供全国约 10%的电力。数据中心运营商倾向于选择芬兰，因为其凉爽气候降低了制冷成本，且电网既低碳又相对未拥堵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Loviisa_Nuclear_Power_Plant">Loviisa Nuclear Power Plant</a></li>
<li><a href="https://www.fortum.com/energy-production/nuclear-power/plants/loviisa">Loviisa Nuclear Power Plant | Fortum</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞芬兰的低碳电力，并欢迎谷歌的举措，认为这是 AI 公司自担电力成本、不让纳税人买单的负责任做法。还有人指出该电站总装机约 1 GW，推测谷歌未全额购买是因为电力公司希望保持多元化的客户群。

**标签**: `#Google`, `#nuclear energy`, `#data centers`, `#low-carbon electricity`, `#AI infrastructure`

---

<a id="item-5"></a>
## [Forgejo 16.0.3 及以下版本存在严重远程代码执行漏洞。](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo 16.0.3 及以前版本存在关键的远程代码执行漏洞，原因是在从模板仓库初始化新仓库时进行了不安全的模板变量展开。该问题已在 Forgejo 16.0.4 中修复，发布日期为 2026 年 9 月 10 日。 此漏洞使攻击者能够在运行 Forgejo 的服务器上执行任意代码，可能导致源代码、构建系统和内部网络被入侵。及时修补对所有自托管 Forgejo 实例至关重要，以防止被利用。 当 Forgejo 克隆模板仓库、删除其 .git 目录，然后对 .forgejo/template 中列出的文件进行变量模板展开时，攻击者可控制的内容可能注入 shell 命令并在展开过程中被执行。该漏洞被分配为 CVE‑2026-89094，并通过一个阻止模板展开在 git 仓库初始化期间的 pull request 得到修复。

hackernews · weierstass · Sep 10, 15:57 · [社区讨论](https://news.ycombinator.com/item?id=49645907)

**背景**: Forgejo 是一个自托管的轻量级 Git 服务，源自 Gitea 的分支，旨在提供易于安装和低维护的仓库托管。它提供模板仓库功能，用户可基于预定义模板创建新仓库，系统会自动复制文件并进行变量替换。在此过程中，Forgejo 会删除模板的 .git 目录，并对 .forgejo/template 中列出的文件进行变量展开，若模板包含恶意构造则可能被滥用。这解释了为何不安全的模板展开会导致远程代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thehackerwire.com/vulnerability/CVE-2026-89094/">CVE-2026-89094 - Critical Vulnerability - TheHackerWire</a></li>
<li><a href="https://news.ycombinator.com/item?id=49645907">Forgejo <=16.0.3 Critical RCE | Hacker News</a></li>
<li><a href="https://noise.getoto.net/2026/09/10/forgejo-16-0-4-and-15-0-8-address-critical-security-vulnerability/">Forgejo 16.0.4 and 15.0.8 address critical security vulnerability | Noise</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了修复该问题的 pull request，指出 Gitea 不受影响，并对项目在 LLM 贡献方面的立场表示担忧。一些用户强调了修复的技术细节，而另一些则警告不要羞辱漏洞报告者。总体而言，讨论表达了真正的关切和对透明度的需求。

**标签**: `#Forgejo`, `#Security`, `#RCE`, `#Git`, `#Self-hosted`

---

<a id="item-6"></a>
## [微软宣布 Rust 成为一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

微软正式将 Rust 指定为一级语言，赋予其在开发工具链中的全面支持，并表明将更深入地将其融入其软件生态系统。 此举凸显 Rust 日益成熟，使其成为 C 和 C++ 在系统编程领域的可行替代方案，将影响行业采用和开发者工具选择。 该声明与微软内部目标一致，即通过自动化工具在 2030 年前将十亿行代码转换为 Rust，并指出 Rust 现在正与 MSVC 后端集成，而不是 LLVM。

hackernews · mmastrac · Sep 10, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**社区讨论**: 评论者指出微软计划通过自动化工具在 2030 年前将十亿行代码转换为 Rust，并赞赏 Rust 已成熟，能够与 C++ 和 C# 竞争。他们还注意到 RustConf 的讨论已从“用 Rust 重写”转向 C++、Python 和 JavaScript 的互操作性，并强调将 LLVM 替换为 MSVC 后端是一项重要的技术变化。

**标签**: `#Rust`, `#Microsoft`, `#systems programming`, `#language adoption`, `#open source`

---

<a id="item-7"></a>
## [硅谷在军工复合体中的角色日益增长](https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex) ⭐️ 8.0/10

最近，战争成本项目的一份报告审视了大型科技公司和硅谷如何日益深入军工复合体，引发了黑客新闻的讨论。评论者指出了历史联系、伦理担忧，以及诸如中央情报局支持的 In‑Q‑Tel 对 Keyhole 的种子资助等例子，Keyhole 后来成为谷歌地球。 这一趋势凸显了商业技术与国防能力的深度融合，引发了对企业伦理、工人责任以及创新方向的质疑。它还影响了公共政策关于监督技术‑国防合作伙伴关系的辩论。 报告指出，费尔柴尔德半导体早期的军事合同为硅谷与国防的联系奠定了基础，而 In‑Q‑Tel 在 2003 年为 Keyhole 提供了种子资金，导致该技术在美国军队在伊拉克的使用中快速普及，随后被谷歌收购。评论者还提到了个人行动，例如因 alleged complicity in war crimes 而辞职微软。

hackernews · paimapi · Sep 10, 15:47 · [社区讨论](https://news.ycombinator.com/item?id=49645754)

**背景**: 军工复合体指的是一个国家的武装力量与为其提供装备的国防产业之间的紧密关系。历史上，硅谷的发展深受国防合同的影响，像费尔柴尔德半导体这样的公司为导弹系统生产了集成电路。In‑Q‑Tel 是中央情报局的风险投资部门，资助初创公司，使其技术可用于情报和军事目的，正如 Keyhole 最终演变为谷歌地球所展示的那样。

**社区讨论**: 评论者就硅谷参与国防是否不可避免或存在伦理问题展开辩论，有人认为拒绝军事合同会阻碍技术进步，而另一些人则主张通过工人 activism 和辞职来抗议共谋。还有人强调了历史先例，指出公司长期同时服务于民用和军用市场，并担心制造用于战争的工具在道德上的影响。

**标签**: `#defense technology`, `#tech ethics`, `#military-industrial complex`, `#Silicon Valley`, `#public policy`

---

<a id="item-8"></a>
## [Trynix.dev 通过 QEMU-WASM 在浏览器中运行任意 Nix 包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Trynix.dev 提供了一个基于 WebAssembly 的 x86_64 Linux 虚拟机，利用 qemu-wasm 项目，能够启动过去 13 年内的任意 Nix 包并直接在浏览器中提供交互式 shell。用户可以通过 URL 参数访问特定版本，例如 python3@3.6.2，并有一个 GitHub Action 可让他们在同一 VM 中启动构建来预览拉取请求。 通过免除本地安装或远程服务器的需求，Trynix.dev 提高了可重复性、教育价值和开发者工作流程，使得历史软件环境能够即时访问并简化拉取请求审查。这展示了 WebAssembly 如何将完整的系统虚拟化带入浏览器，对 Nix 生态系统的工具链产生影响。 该虚拟机由 qemu-wasm 的 TCG 后端驱动，将客机代码翻译为 WebAssembly 并利用浏览器 API 执行，支持网络和文件系统挂载。任何 Nix 包都可以通过 ?pkg= 查询参数指定，而 trynix-preview GitHub Action 会发布一个指向拉取请求构建的实时 VM 的链接。

rss · Simon Willison · Sep 10, 23:44

**背景**: Nix 是一个纯函数式包管理器，将软件包视为不可变的值，从而实现跨系统的可重复构建和回滚。QEMU-WASM 是 QEMU 模拟器的实验性 WebAssembly 移植，使得未修改的客机操作系统（如 Linux）能够通过 TCG JIT 和浏览器提供的执行环境在浏览器中运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>

</ul>
</details>

**标签**: `#Nix`, `#WebAssembly`, `#QEMU`, `#developer tools`, `#reproducibility`

---

<a id="item-9"></a>
## [Shopify 因 AI 辅助开发回归原生移动应用。](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify 于 2026 年 9 月 10 日宣布，将其移动应用从 React Native 迁回至独立的 Swift（iOS）和 Kotlin（Android）原生代码库。这一转变得益于 AI 编码代理能够完成大量的实现、翻译、测试和审查工作，从而降低了维护双平台原生应用的成本。 此决定凸显了 AI 辅助开发如何改变原生移动开发的经济性，可能促使其他公司更看重性能而非跨平台便利。同时，这也表明 AI 编码代理已经成熟到能够可靠地协助平台特定代码的生成与翻译。 Shopify 维护着三个广泛使用的 React Native 库——react-native-skia、flash-list 和 restyle——其中前两个将移交给新维护者，而 restyle 计划在 2026 年底归档。公司指出，AI 代理在编写、翻译、测试和审查 Swift 和 Kotlin 代码方面提供帮助，使得双平台工作变得可以接受。

rss · Simon Willison · Sep 10, 21:11

**背景**: React Native 使开发者能够使用单一的 JavaScript 代码库同时在 iOS 和 Android 上运行，从而减少了重复构建功能的需求。传统的原生开发需要分别使用 Swift 和 Kotlin 编写代码库，这会增加实现和维护的成本。最近的 AI 编码代理如 GitHub Copilot、Claude Code 以及 AI 驱动的 Swift‑到‑Kotlin 翻译器可以自动化大量代码生成、翻译、测试和审查工作，从而降低了采用双原生方法的成本门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.codeconvert.ai/swift-to-kotlin-converter">Free Swift to Kotlin Converter - AI Code Translation | CodeConvert AI</a></li>

</ul>
</details>

**标签**: `#mobile development`, `#React Native`, `#native apps`, `#AI-assisted coding`, `#Shopify`

---

<a id="item-10"></a>
## [信息干预降低处方错误：医疗运营中的野外实验](https://arxiv.org/abs/2609.09673) ⭐️ 8.0/10

研究使用印度最大的电子病历平台，对 1700 名医生的 281 万张处方进行随机田野实验；接受实时非强制性药物相互作用信息的医生处方错误下降 8.6%，相当于每年约 480 万美元的住院费用节省和大约 134 条潜在生命的挽救。 该研究表明，低负担的非强制性信息干预能在不造成警报疲劳的情况下提升患者安全，提供一种可扩展的方法来降低昂贵的药物相互作用错误及其相关的发病率。 作者采用差分‑差分设计，发现两种机制：反应性纠正（在被标记后删除错误）和主动学习（在警报出现前避免错误），学习效应随时间增长并超越特定药物对，同时医生的生产力和护理质量未受影响。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 药物相互作用（DDI）错误是指两种或多种药物相互影响活性，可能导致不良事件或住院等严重风险。传统的临床决策支持系统经常产生强制性警报，干扰工作流并导致高覆盖率，这种现象称为警报疲劳。非强制性信息干预向临床医生提供相关安全数据，但不要求立即响应，旨在减少错误同时保持工作流程。差分‑差分方法通过比较接受干预的治疗组和未接受干预的对照组随时间的变化，来隔离干预的因果影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/drug-drug-interaction">sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical...</a></li>
<li><a href="https://www.verahealth.ai/">Vera Health - Evidence-Based Clinical Answers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>

</ul>
</details>

**标签**: `#healthcare`, `#patient safety`, `#decision support`, `#field experiment`, `#prescription errors`

---

<a id="item-11"></a>
## [针对 P2P 贷款的表格信用评分进行多攻击鲁棒性评估的对抗训练研究](https://arxiv.org/abs/2609.09945) ⭐️ 8.0/10

该研究在大规模 Lending Club 数据子集上，评估了逻辑回归、前馈神经网络和表格 Transformer 在 FGSM、PGD、盐椒噪声和 DeepFool 四种攻击及混合攻击下的对抗训练与鲁棒性，用于 P2P 贷款信用评分。 它填补了对抗鲁棒性研究主要集中在图像和文本领域的空白，为表格信用评分模型提供了系统基准，这与机器学习安全和金融科技应用直接相关。 对抗训练显著提升对所训练攻击的鲁棒性，并在基于梯度的攻击族间（FGSM ↔ PGD）良好迁移，但对非梯度损伤（盐椒噪声、DeepFool）迁移较弱；混合攻击训练在保持干净测试性能的同时提供了最均衡的鲁棒性，这是通过分层交叉验证得到的。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 对抗机器学习研究故意施加的微小扰动如何导致模型预测错误，其中 FGSM 和 PGD 等技术生成基于梯度的样本，而盐椒噪声和 DeepFool 则代表非梯度扰动。在点对点（P2P）贷款中，信用评分模型基于申报的表格特征（如收入、就业和信用历史）预测违约风险，因而容易受到这些特征的战略性操纵。表格数据不具备图像或文本中固有的空间或序列结构，因此将逻辑回归、前馈网络和表格 Transformer 等模型应用于此类数据需要对类别和数值字段进行特殊预处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/beginner/fgsm_tutorial.html">Adversarial Example Generation — PyTorch Tutorials 2.14.0 ...</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/️white-box-adversarial-attacks-and-how-to-stop-them-eb19a003463b">White-Box Adversarial Attacks and How to Stop Them | Medium</a></li>
<li><a href="https://github.com/XavierSpycy/tabtransformers">GitHub - XavierSpycy/tabtransformers: A PyTorch-based ...</a></li>

</ul>
</details>

**标签**: `#adversarial machine learning`, `#credit scoring`, `#tabular data`, `#robustness evaluation`, `#P2P lending`

---

<a id="item-12"></a>
## [去中心化交易所套利者之间的 Gas 费竞争建模](https://arxiv.org/abs/2507.08302) ⭐️ 8.0/10

本文首次提出了两个套利者在去中心化交易所（DEX）上，在无回滚、自动回滚和可选择回滚三种交易回滚机制下的 Gas 费竞争均衡模型，并推导出唯一的混合策略均衡。研究利用 Binance 和 Uniswap V2 的实证数据验证了模型，发现 Gas 费和交易量随价格差异和流动性增加而上升。 通过建模套利者之间的竞争，该工作填补了去中心化金融市场微观结构研究的空白，为协议设计者提供了优化费用结构和交易排序的见解。结果还帮助流动性提供者和交易者了解库存风险和回滚机制如何影响盈利能力和效率。 分析表明不存在纯对称均衡，但可以为每种回滚机制刻画出唯一的混合策略均衡。实证结果显示，Gas 费和交易量随价格差异和流动性上升；在低库存风险下，无回滚设置最有利于套利者，而在高库存风险下，无回滚和可选择回滚设置在盈利和效率上均优于自动回滚设置。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 去中心化交易所（DEX）使用自动做市商（AMM）来实现交易，这会导致其价格与中心化交易所（CEX）出现差异，套利者可以利用这一差异获利。在区块链上执行套利需要支付 Gas 费用，并且交易的排序可能受到回滚规则的影响：交易可能永不回滚（no-revert）、失败时自动回滚（auto-revert）或允许用户选择是否回滚（selectable-revert）。从博弈论角度看，套利者通过选择 Gas 费进行竞争，当纯策略无法达到稳定时，会出现混合策略纳什均衡。理解这些动态对于评估去中心化金融市场效率和设计稳健的 AMM 协议至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.08302">Arbitrage on Decentralized Exchanges</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5347630">Arbitrage on Decentralized Exchanges by Xue Dong He... :: SSRN</a></li>
<li><a href="https://medium.com/authereum/getting-ethereum-transaction-revert-reasons-the-easy-way-24203a4d1844">Getting Ethereum Transaction Revert Reasons the Easy Way | Medium</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#Arbitrage`, `#Automated Market Makers`, `#Game Theory`, `#Blockchain`

---

<a id="item-13"></a>
## [AI 编程工具与数字创业：软件专业知识的作用](https://arxiv.org/abs/2511.06545) ⭐️ 8.0/10

研究发现，接触 AI 编程工具会提高 2022 年第四季度以后的首次创业启动数量，但降低一年存活率；具备软件工作经验的创始人推动更多启动，在自动化仅部分进行时减轻存活率下降，并解释了融资增加的原因。 该研究提供了关于 AI 编程工具如何影响创业创立和存活的新颖实证证据，突显了创始人软件专业知识的调节作用，帮助政策制定者和创业者理解 AI 驱动自动化的局限与收益。 作者采用预 LLM 产品描述来衡量产品类别的 AI 编程工具暴露度，并将其与创业启动、流量和融资数据关联，发现启动增加、存活率下降但条件下融资上升，具备软件经验的创始人占新创业更大比例，在部分自动化时减轻存活率下降，并解释了所有融资增长。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 诸如 GitHub Copilot、Claude Code 和 Cursor 之类的 AI 编程工具利用大型语言模型自动生成代码，降低了软件创作的技术门槛。数字创业利用这些工具使非技术背景的创始人也能启动企业。软件工作经验指的是之前在软件开发领域的就业经历，这为创始人提供了更深的技术知识和问题解决能力，能够补充或替代 AI 生成的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.podcosmos.com/ycombinator/startup-school/how-to-get-the-most-out-of-vibe-coding-startup-school">Key Insights: How To Get The Most Out Of Vibe Coding | PodCosmos</a></li>
<li><a href="https://arxiv.org/html/2511.06545v3">AI Coding Tools and Digital Entrepreneurship: The Role of Software...</a></li>

</ul>
</details>

**标签**: `#AI coding tools`, `#digital entrepreneurship`, `#software expertise`, `#venture survival`, `#startup financing`

---

<a id="item-14"></a>
## [重建大规模生产网络](https://arxiv.org/abs/2512.02362) ⭐️ 8.0/10

作者提出一种算法，先使用部门感知的重力模型绘制二元买卖骨架，再通过最小能量程序分配权重，从公开的部门投入产出表和企业规模分布重建国家层面的企业对企业生产网络。在美国，该方法产生约 650 万家企业和 3.4 亿条链接，在单个工作站上约需四小时；日本、英国、澳大利亚、芬兰和丹麦也得到了类似重建。 重建的加权企业对企业网络使得宏观经济模拟和系统性风险评估更加真实，表明企业规模、度或部门位置都不能可靠地预测单个企业失败导致的总损失。这凸显了在经济政策和风险管理中需要详细网络数据的必要性。 算法首先使用部门感知的重力模型构建二元骨架，然后求解最小能量权重方案，使其一步企业平衡和部门流与观测数据保持一致，同时通过马尔可夫闭包确保网络为原始的并具有唯一的平稳分布。实验表明重建的日本网络再现了观测到的重尾度分布，且尽管买卖方对称处理，客户尾部仍比供应商尾部更重。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 部门投入产出表记录了各行业之间商品和服务的货币流动，展示了每个部门的输出如何成为其他部门的输入，常用于研究行业间依赖关系。重力模型在网络重建中根据两个实体的大小（或质量）和距离预测链接出现的可能性，这里被调整为使用部门特定的企业规模分布来生成合理的二元骨架。最小能量权重通过在保持观测总量不变的约束下最小化能量函数来分配链接权重，从而在满足闭包和平稳性等理论性质的同时使网络保持与数据的接近。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bea.gov/data/industries/input-output-accounts-data">Input-Output Accounts | U.S. Bureau of Economic Analysis (BEA)</a></li>
<li><a href="https://www.researchgate.net/figure/Heatmaps-of-migrants-normalized-by-the-gravity-model-The-following-heatmaps-depict-the_fig3_337451749">Fig 5. Heatmaps of migrants normalized by the gravity model . The...</a></li>
<li><a href="https://arxiv.org/html/2512.02362v1">Reconstructing Large Scale Production Networks</a></li>

</ul>
</details>

**标签**: `#network reconstruction`, `#input-output tables`, `#firm-to-firm networks`, `#economic modeling`, `#algorithm`

---

<a id="item-15"></a>
## [生成式 AI 在 FactSet 的应用提升分析师报告丰富度但预测准确率下降](https://arxiv.org/abs/2512.19705) ⭐️ 8.0/10

2023 年生成式 AI 被整合到 FACTSET 后，分析师报告中的不同信息来源增加了 26%，主题覆盖面扩大了 24%，分析方法增加了 21%，并且及时性得到提升。然而，尽管信息更丰富，分析师在信息处理需求增加时预测准确率下降，而使用相同输入的机器学习基准则没有出现类似下降。 研究结果表明，虽然生成式 AI 减轻了信息获取的限制，但人类注意力成为知识工作中的新瓶颈，这凸显了需要设计能够辅助而非加重分析师负担的 AI 工具。这些见解对 AI 增强型职业具有广泛影响，表明仅仅提升数据丰富度并不能自动带来更好的决策，除非同时解决认知限制。 该研究将 FACTSET 的 GenAI 推广视为一种自然实验，利用其他数据供应商的安慰剂测试排除平台范围的趋势，并将人类分析师的表现与处理相同可观测输入的机器学习基准进行比较。报告丰富度指标显著提升（来源增加 26%，主题增加 24%，方法增加 21%），但在信息处理负担增加时分析师的相对预测准确率下降，而机器学习基准的准确率保持稳定。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 生成式人工智能（GenAI）是指能够基于学习到的模式生成文本、数据或模型的人工智能系统，近年来已被越来越多地嵌入金融数据平台。FACTSET 是金融数据、分析和工作流工具的主要提供者，被分析师用于制作投资研究报告。在 2023 年之前，分析师在信息收集和综合方面面临限制；将 GenAI 整合到 FACTSET 旨在通过自动化数据检索和丰富来缓解这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geminibrief.com/factset-research-systems-inc-fds-the-open-platform-architect-of-the-financial-intelligence-era/">FactSet Research Systems Inc. (FDS): The Open Platform Architect of...</a></li>
<li><a href="https://integrations.sh/factset.com/">factset .com — integrations</a></li>
<li><a href="https://www.youtube.com/watch?v=1lknhrlWe0U">FactSet Generative AI - YouTube</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#financial analysis`, `#human-AI interaction`, `#information processing`, `#empirical study`

---

<a id="item-16"></a>
## [布朗签名的全局普适近似](https://arxiv.org/abs/2512.16396) ⭐️ 8.0/10

作者证明，时间粗糙路径的签名上的线性泛函在 L^p 意义上是稠密的，从而为任何 p 可积的适应随机过程（包括随机微分方程的解）提供了普适近似定理。 该结果将粗糙路径理论、签名方法和机器学习近似理论联系起来，为从序列数据学习以及分析高斯过程（如分数布朗运动）提供了新工具。 该定理适用于加权粗糙路径空间，并且对高斯过程成立；特别是，时间延伸布朗运动签名上的线性泛函可以逼近任何布朗滤波下 p 可积的随机过程。

rss · arXiv Quantitative Finance · Sep 10, 04:00

**背景**: 粗糙路径是对路径的受控增强，使得对不规则信号的积分成为可能；其签名是一系列迭代积分，编码了路径的形状。经典的普适近似定理表明，神经网络可以在紧致集上稠密地逼近连续函数。本文将此思想推广，表明签名元素的线性组合在路径依赖泛函的 L^p 空间中是稠密的，从而将近似理论推广到粗糙和高斯路径空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2512.16396">Global universal approximation with Brownian signatures</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/brownian-signature-variables">Brownian Signature Variables Overview</a></li>

</ul>
</details>

**标签**: `#signature methods`, `#rough paths`, `#universal approximation`, `#stochastic processes`, `#fractional Brownian motion`

---