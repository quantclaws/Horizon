---
layout: default
title: "Horizon Summary: 2026-07-20 (EN)"
date: 2026-07-20
lang: en
---

> From 14 items, 3 important content pieces were selected

---

1. [Alibaba Announces Upcoming Open-Weights Qwen 3.8 2.4T Parameter LLM](#item-1) ⭐️ 9.0/10
2. [Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s](#item-2) ⭐️ 8.0/10
3. [EFF reveals Texas police used ALPR data from 83k cameras to track abortion suspect](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Alibaba Announces Upcoming Open-Weights Qwen 3.8 2.4T Parameter LLM](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) ⭐️ 9.0/10

Alibaba signaled via Twitter that it will soon release the open‑weights version of Qwen 3.8, a 2.4‑trillion‑parameter multimodal LLM previewed as Qwen3.8‑Max on July 19, 2026. The release positions Alibaba directly against Moonshot AI’s 2.8T‑parameter Kimi K3, accelerating the race for massive open‑weight models that could democratize access to cutting‑edge AI for researchers and developers. Qwen3.8‑Max is described as a 2.4T‑parameter multimodal mixture‑of‑experts model, with plans to release smaller variants such as the 35B MoE and 27B dense models for local deployment. Current Qwen 3.7 Pro has been criticized for poor usability and high cost compared to DeepSeek V4 Pro.

hackernews · nh43215rgb · Jul 19, 08:44 · [Discussion](https://news.ycombinator.com/item?id=48966120)

**Background**: The Qwen series is Alibaba Cloud’s family of large language models, ranging from dense to mixture‑of‑experts architectures, with recent versions like Qwen 3.6 and Qwen 3.7 focusing on improved reasoning and multilingual capabilities. Open‑weight releases allow anyone to download, fine‑tune, and run models locally, contrasting with API‑only offerings. The move toward trillion‑parameter models reflects industry trends where companies compete on scale while also exploring efficient inference techniques such as quantization and specialized libraries like mtplx.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buildfastwithai.com/blogs/qwen3-8-preview-2-4t-params-open-weights-release">Qwen3.8 Preview: 2.4T Params, Open Weights, Release</a></li>
<li><a href="https://kie.ai/blog/what-is-qwen3-8-max">What Is Qwen3.8-Max? Alibaba's 2.4T Flagship</a></li>
<li><a href="https://news.ycombinator.com/item?id=48966120">Qwen 3.8</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Alibaba’s move appears responsive to Moonshot AI’s Kimi K3 announcement, with some hoping for smaller Qwen 3.8 variants to run locally on personal hardware. Others praised recent speed‑up tools like mtplx that make large models more usable, while a few criticized Qwen 3.7 Pro as unstable and expensive compared to DeepSeek V4 Pro.

**Tags**: `#LLM`, `#Qwen`, `#open-weights`, `#AI models`, `#HackerNews`

---

<a id="item-2"></a>
## [Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

The author built an ESP32‑based scoring and control system for his 8‑lane bowling alley that costs roughly $200 per lane pair, using ESPNow mesh networking with an RS485 fallback and a Raspberry Pi gateway that streams data to Redis. This demonstrates that inexpensive off‑the‑shelf microcontrollers can replace costly legacy bowling scoring hardware, offering a model for low‑cost retrofits of other industrial equipment and reducing vendor lock‑in. Each lane pair uses ESP32 nodes wired to IR break‑beam sensors, optocouplers and relays, communicating via ESPNow; a wired RS485 bus provides fallback in noisy RF environments, while a Raspberry Pi runs Redis and a state machine that translates events into a WebSocket/React UI.

hackernews · section33 · Jul 19, 14:41

**Background**: Traditional bowling scoring systems from the 2000s cost six figures, integrating camera‑based pin detection, object detection on ASICs, and control of mechanical pinsetters and ball returns. The ESP32 is a low‑cost dual‑core microcontroller with Wi‑Fi/Bluetooth, capable of real‑time sensor processing via FreeRTOS, making it suitable for DIY replacements of such legacy systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.proculustech.com/esp32-board">ESP32 board guide: features, applications & how to use it</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pinsetter">Pinsetter - Wikipedia</a></li>
<li><a href="https://www.bowltech.com/forum/automatic-scoring-systems-forums/steltronic-scoring-system/1079665-adjusting-camera-to-detect-pins">Adjusting camera to detect pins - Bowl-Tech</a></li>

</ul>
</details>

**Discussion**: Commenters expressed enthusiasm, shared similar experiences retrofitting old mechanical equipment, and discussed ideas such as adding LED/DMX lighting, touch‑to‑pay kiosks, and further automation, reflecting broad interest in low‑cost embedded upgrades.

**Tags**: `#ESP32`, `#embedded systems`, `#retrofitting`, `#IoT`, `#DIY`

---

<a id="item-3"></a>
## [EFF reveals Texas police used ALPR data from 83k cameras to track abortion suspect](https://www.eff.org/deeplinks/2026/07/we-want-texans-know-their-rights-qa-mayday-health-impact-surveillance-abortion) ⭐️ 8.0/10

The Electronic Frontier Foundation reported that Texas law enforcement searched data from over 83,000 automated license plate reader (ALPR) cameras to locate a woman suspected of self‑managed abortion. This case shows how surveillance technologies originally marketed for public safety can be repurposed to monitor private healthcare decisions, raising serious privacy and civil‑liberties concerns. The ALPR network accessed by the sheriff’s office spans more than 83,000 cameras across Texas, and the data was queried without a warrant as part of an investigation into alleged self‑managed abortion.

hackernews · amarcheschi · Jul 19, 22:03 · [Discussion](https://news.ycombinator.com/item?id=48972062)

**Background**: Automatic License Plate Recognition (ALPR) systems use cameras and software to capture, analyze, and store license plate data, often promoted for locating stolen vehicles or missing persons. The collected data includes timestamps and locations, allowing the reconstruction of a vehicle’s travel patterns over time. While some courts have ruled that warrantless ALPR collection does not constitute personal information, others have found it invasive, and this case shows how the data can be repurposed to investigate private healthcare decisions such as self‑managed abortion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number-plate recognition - Wikipedia</a></li>
<li><a href="https://www.dhs.gov/science-and-technology/saver/automatic-license-plate-readers">Automatic License Plate Readers | Homeland Security</a></li>
<li><a href="https://platerecognizer.com/">Automatic License Plate Recognition - High Accuracy ALPR</a></li>

</ul>
</details>

**Discussion**: Several commenters warned that the ALPR query demonstrates how surveillance tools can be weaponized against individuals seeking abortion, raising alarms about privacy and bodily autonomy. Others defended the action as necessary to protect fetal life, reflecting a broader clash between privacy advocates and anti‑abortion groups, while some noted that even period‑tracking apps are now considered unsafe, prompting a return to pen‑and‑paper methods.

**Tags**: `#surveillance`, `#privacy`, `#abortion rights`, `#ALPR`, `#civil liberties`

---