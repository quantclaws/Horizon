---
layout: default
title: "Horizon Summary: 2026-07-20 (ZH)"
date: 2026-07-20
lang: zh
---

> From 14 items, 3 important content pieces were selected

---

1. [阿里巴巴宣布即将开源权重的 Qwen 3.8 2.4T 参数大语言模型](#item-1) ⭐️ 9.0/10
2. [展示 HN：我用 1600 美元的 ESP32 替换了价值 12 万美元的保龄球馆系统](#item-2) ⭐️ 8.0/10
3. [EFF 揭露德州警方利用 83,000 个 ALPR 摄像头追踪堕胎嫌疑人](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [阿里巴巴宣布即将开源权重的 Qwen 3.8 2.4T 参数大语言模型](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) ⭐️ 9.0/10

阿里巴巴通过 Twitter 暗示将很快发布 Qwen 3.8 的开源权重版本，这是一个 2.4 万亿参数的多模态大语言模型，预览版 Qwen3.8‑Max 于 2026 年 7 月 19 日宣布。 此次发布使阿里巴巴直接与 Moonshot AI 的 2.8 万亿参数 Kimi K3 竞争，加速了巨型开源权重模型的竞赛，有望让研究人员和开发者更易获得前沿 AI。 Qwen3.8‑Max 被描述为一个 2.4 万亿参数的多模态混合专家模型，计划发布更小的变体如 35B MoE 和 27B 密集模型以便本地部署；目前的 Qwen 3.7 Pro 因使用体验差和成本高而受到批评，相比之下 DeepSeek V4 Pro 表现更好。

hackernews · nh43215rgb · Jul 19, 08:44 · [社区讨论](https://news.ycombinator.com/item?id=48966120)

**背景**: 通义系列是阿里巴巴云的大语言模型族，包含从密集到混合专家（MoE）架构的各种规模，近期版本如通义 3.6 和 3.7 在推理和多语言能力上有所提升。开源权重发布意味着任何人都可以下载、微调并在本地运行模型，这与仅提供 API 的闭源模型形成对比。朝着万亿参数模型的发展反映了行业趋势：公司在规模上竞争的同时，也通过量化和 mtplx 等专用库探索高效推理技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buildfastwithai.com/blogs/qwen3-8-preview-2-4t-params-open-weights-release">Qwen3.8 Preview: 2.4T Params, Open Weights, Release</a></li>
<li><a href="https://kie.ai/blog/what-is-qwen3-8-max">What Is Qwen3.8-Max? Alibaba's 2.4T Flagship</a></li>
<li><a href="https://news.ycombinator.com/item?id=48966120">Qwen 3.8</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，阿里巴巴的此举似乎是对 Moonshot AI 发布 Kimi K3 的回应，有人希望能有更小的 Qwen 3.8 变体以便在个人硬件上本地运行。还有人称赞像 mtplx 这样的加速工具让大模型更易使用，而少数人则批评 Qwen 3.7 Pro 不稳定且成本高，不如 DeepSeek V4 Pro。

**标签**: `#LLM`, `#Qwen`, `#open-weights`, `#AI models`, `#HackerNews`

---

<a id="item-2"></a>
## [展示 HN：我用 1600 美元的 ESP32 替换了价值 12 万美元的保龄球馆系统](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

作者为他的 8 条车道保龄球馆构建了基于 ESP32 的计分和控制系统，每车道对成本约 200 美元，使用 ESPNow 星型网络并有 RS485 备用，树莓派网关将数据流送到 Redis。 这表明廉价的现成微控制器可以取代昂贵的传统保龄球计分硬件，为其他工业设备的低成本改造提供范例，并减少供应商锁定。 每对车道使用连接红外断 beam 传感器、光耦和继电器的 ESP32 节点，通过 ESPNow 通信；有线 RS485 总线在射频噪声环境下提供备用，而树莓派运行 Redis 和状态机将事件转换为 WebSocket/React 界面。

hackernews · section33 · Jul 19, 14:41

**背景**: 2000 年代的传统保龄球计分系统价值六位数，集成了基于摄像头的瓶子检测、ASIC 上的对象检测以及对机械拆瓶机和球回收装置的控制。ESP32 是一种低成本的双核微控制器，具备 Wi‑Fi/Bluetooth，能够通过 FreeRTOS 进行实时传感器处理，适合 DIY 替换此类旧系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.proculustech.com/esp32-board">ESP32 board guide: features, applications & how to use it</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pinsetter">Pinsetter - Wikipedia</a></li>
<li><a href="https://www.bowltech.com/forum/automatic-scoring-systems-forums/steltronic-scoring-system/1079665-adjusting-camera-to-detect-pins">Adjusting camera to detect pins - Bowl-Tech</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了热情，分享了改造旧机械设备的类似经验，并讨论了添加 LED/DMX 灯光、触摸付费亭和进一步自动化的想法，显示出对低成本嵌入式升级的广泛兴趣。

**标签**: `#ESP32`, `#embedded systems`, `#retrofitting`, `#IoT`, `#DIY`

---

<a id="item-3"></a>
## [EFF 揭露德州警方利用 83,000 个 ALPR 摄像头追踪堕胎嫌疑人](https://www.eff.org/deeplinks/2026/07/we-want-texans-know-their-rights-qa-mayday-health-impact-surveillance-abortion) ⭐️ 8.0/10

电子前线基金会（EFF）报道，德州执法部门搜索了超过 83,000 个自动车牌识别（ALPR）摄像头的数据，以追踪一名涉嫌自我管理堕胎的女性。 此案表明，原本用于公共安全的监控技术可能被用来监视个人的医疗决定，引发严重的隐私和公民自由问题。 警方调用的 ALPR 网络覆盖德州超过 83,000 个摄像头，且在未获搜查令的情况下查询了这些数据，以调查所谓的自我管理堕胎行为。

hackernews · amarcheschi · Jul 19, 22:03 · [社区讨论](https://news.ycombinator.com/item?id=48972062)

**背景**: 自动车牌识别（ALPR）系统通过摄像头和软件捕获、分析并存储车牌数据，常被宣传用于寻找被盗车辆或失踪人员。这些数据包含时间戳和位置信息，能够重建车辆随时间的行驶轨迹。虽然一些法院认为无搜查令的 ALPR 数据收集不构成个人信息，但其他法院认为具有侵入性，本案表明此类数据也可能被用于调查私人医疗决定，如自我管理的堕胎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number-plate recognition - Wikipedia</a></li>
<li><a href="https://www.dhs.gov/science-and-technology/saver/automatic-license-plate-readers">Automatic License Plate Readers | Homeland Security</a></li>
<li><a href="https://platerecognizer.com/">Automatic License Plate Recognition - High Accuracy ALPR</a></li>

</ul>
</details>

**社区讨论**: 几位评论者警告，此次 ALPR 查询表明监控工具可能被用来针对寻求堕胎的个人，引发对隐私和身体自主权的担忧。其他人则辩称此举是保护胎儿生命所必需的，这反映了隐私倡导者与反堕胎团体之间的更广泛冲突；还有人指出，即使经期追踪应用也不再安全，建议改用笔纸记录。

**标签**: `#surveillance`, `#privacy`, `#abortion rights`, `#ALPR`, `#civil liberties`

---