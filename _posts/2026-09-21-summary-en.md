---
layout: default
title: "Horizon Summary: 2026-09-21 (EN)"
date: 2026-09-21
lang: en
---

> From 23 items, 6 important content pieces were selected

---

1. [Polars releases py-2.0.0-rc.2 with breaking changes, new Map dtype, and performance enhancements](#item-1) ⭐️ 8.0/10
2. [Samsung will more than double its HBM4 and HBM4E DRAM output next year.](#item-2) ⭐️ 8.0/10
3. [ChatGPT Uses Ad Tracking Pixels to Monitor Cross‑Site Browsing](#item-3) ⭐️ 8.0/10
4. [The Snowden archive's fate is examined.](#item-4) ⭐️ 8.0/10
5. [Qwen releases 7B open-weight text-to-image model Image 2.1 with native transparency](#item-5) ⭐️ 8.0/10
6. [Terry Tao Questions Need for Human Mathematicians Amid AI Advances](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Polars releases py-2.0.0-rc.2 with breaking changes, new Map dtype, and performance enhancements](https://github.com/pola-rs/polars/releases/tag/py-2.0.0-rc.2) ⭐️ 8.0/10

Polars released py-2.0.0-rc.2, a release candidate for version 2.0. It includes breaking changes like reading Parquet ENUM as pl.String and deprecating cut/qcut, introduces the Map dtype, and brings many performance improvements. This release marks Polars' transition to a major 2.0 version, requiring users to adapt to breaking changes while gaining new capabilities like the Map dtype for flexible key‑value columns. The performance enhancements target Parquet scanning, join ordering, and memory usage, benefiting data‑intensive workloads. Notable changes include PR #29331 (Parquet ENUM → pl.String), PR #28984 (Map dtype introduction), and PR #29329 (deprecation of cut/qcut). Performance work spans PRs #29397‑#29092, covering predicate push‑off, float literal handling, OOM fixes, and join‑order optimizations.

github · github-actions[bot] · Sep 20, 17:36

**Background**: Polars is a high‑performance DataFrame library implemented in Rust with Python bindings, offering both eager and lazy APIs and columnar execution similar to Apache Arrow. It is designed for fast data manipulation and competes with pandas by leveraging parallelism and cache‑friendly algorithms. The 2.0 series aims to stabilize the API while introducing new data types and execution improvements.

**Tags**: `#polars`, `#python`, `#dataframe`, `#release`, `#performance`

---

<a id="item-2"></a>
## [Samsung will more than double its HBM4 and HBM4E DRAM output next year.](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) ⭐️ 8.0/10

Samsung is expected to more than double its production of HBM4 and HBM4E DRAM to meet rising demand from AI hardware manufacturers, according to industry sources. The increase will alleviate a critical bottleneck in AI accelerator supply chains, enabling higher performance GPUs and ASICs while influencing global DRAM pricing and competition among memory makers. Samsung plans to expand output using its 1c (10nm-class) DRAM base die and advanced packaging, targeting HBM4 with a 2,048‑pin interface and HBM4E with a 512‑bit external interface for up to 16‑layer stacks.

hackernews · giuliomagnifico · Sep 20, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49778029)

**Background**: High Bandwidth Memory (HBM) is a stacked DRAM technology that delivers very high memory bandwidth with low power consumption, making it essential for AI accelerators. The HBM4 standard, ratified by JEDEC in April 2025, doubles the I/O pin count to 2,048, providing several terabytes per second of bandwidth. HBM4E retains the HBM4 core but uses a narrower 512‑bit external interface, allowing high bandwidth on standard organic substrates without a silicon interposer.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiconductor.samsung.com/dram/hbm/hbm4/">HBM4 | DRAM | Samsung Semiconductor Global</a></li>
<li><a href="https://www.jedec.org/standards-documents/docs/jesd270-4a">High Bandwidth Memory (HBM4) DRAM | JEDEC</a></li>

</ul>
</details>

**Discussion**: Commenters noted that HBM capacity, not processors or lithography equipment, is the main bottleneck for Chinese AI accelerator production, and praised the scalability of die‑thinning processes. They also questioned why HBM isn’t used in consumer electronics, warned of possible consumer DRAM price increases, and wondered whether the output boost will satisfy AI’s growing demand.

**Tags**: `#HBM`, `#Samsung`, `#AI hardware`, `#memory technology`, `#semiconductor supply`

---

<a id="item-3"></a>
## [ChatGPT Uses Ad Tracking Pixels to Monitor Cross‑Site Browsing](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) ⭐️ 8.0/10

The article reports that ChatGPT now embeds standard ad‑tracking pixels that collect data on users’ browsing activity across other websites, enabling cross‑site tracking. This development highlights how AI products are adopting invasive advertising techniques, raising serious privacy concerns and potentially attracting regulatory scrutiny. The tracking mechanism relies on a tiny invisible pixel or JavaScript snippet that fires when ChatGPT loads, sending browsing data to third‑party ad networks; browsers such as Firefox, Brave and Safari block it by default, while Chrome and Edge do not.

hackernews · lmbbuchodi · Sep 20, 15:18 · [Discussion](https://news.ycombinator.com/item?id=49776729)

**Background**: A tracking pixel is a small, often invisible image or script that loads when a user visits a page and sends information about that visit to an analytics or advertising platform. Third‑party cookies enable domains other than the one being visited to store data in a user's browser, allowing cross‑site tracking of browsing patterns and preferences. These technologies are widely used in adtech to build user profiles for targeted advertising, but they also raise privacy concerns because they can monitor users without explicit consent.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalmarketer.com/blog/what-is-tracking-pixel/">What is a Tracking Pixel—Explained in 800 Words or Less | DigitalMarketer</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Third-party_cookies">Third-party cookies - Privacy on the web | MDN</a></li>
<li><a href="https://improvado.io/blog/what-is-tracking-pixel">What Is a Tracking Pixel? Complete 2026 Guide</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed EU efforts to curb such practices, noting that while the legislation can be annoying, it protects consumer privacy. Others expressed discomfort that a standard ad‑tech technique is now being used in an AI chat product, with some joking about a possible referral kickback from OpenAI. Several users pointed out that browsers like Firefox, Brave and Safari block the tracking, whereas Chrome and Edge do not.

**Tags**: `#AI`, `#Privacy`, `#Web Tracking`, `#ChatGPT`, `#AdTech`

---

<a id="item-4"></a>
## [The Snowden archive's fate is examined.](https://libroot.org/posts/what-happened-to-the-snowden-archive) ⭐️ 8.0/10

The article examines what became of the Snowden archive, noting how media coverage declined, public interest shifted, and the implications for journalism and responsible disclosure of classified information. It highlights how the waning attention affects oversight of surveillance programs and raises questions about the long‑term viability of responsible disclosure in the face of changing public sentiment. The piece references the Intercept’s Snowden archive series, notes that Snowden retains copies in Russia, and discusses the shifting Overton window and ambivalence toward his revelations.

hackernews · EXHades · Sep 20, 22:35 · [Discussion](https://news.ycombinator.com/item?id=49780820)

**Background**: Edward Snowden, a former NSA contractor, leaked a trove of classified documents in 2013 that became known as the Snowden archive, revealing global surveillance programs. Responsible disclosure refers to the practice of sharing such information with journalists and the public in a way that minimizes harm while informing democratic debate. The Overton window describes the range of ideas tolerated in public discourse, which can shift over time. Media coverage of the archive initially surged but later waned as the news cycle moved on.

**Discussion**: Commenters noted that media interest in the Snowden archive has faded and that public opinion has shifted, with some viewing the revelations as now ordinary. Several remarked on the changing Overton window and questioned whether responsible disclosure still holds meaning, while others pointed out that Snowden retains copies and remains influential despite his exile in Russia.

**Tags**: `#Snowden`, `#privacy`, `#surveillance`, `#journalism`, `#responsible disclosure`

---

<a id="item-5"></a>
## [Qwen releases 7B open-weight text-to-image model Image 2.1 with native transparency](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen announced Image 2.1, a 7B parameter open-weight text-to-image model that natively outputs RGBA images with transparency and features improved text rendering. The model provides a compact, open-weight alternative with native transparency, addressing the need for smaller, editable AI-generated images and sparking discussion about its licensing and performance relative to larger models. Built on a 32-layer Single-Stream DiT architecture, Qwen Image 2.1 generates images up to 2K resolution, outputs real alpha channels, and is released under a license that is more restrictive than earlier Apache-licensed Qwen models.

hackernews · jmillikin · Sep 20, 13:09 · [Discussion](https://news.ycombinator.com/item?id=49775499)

**Background**: An open-weight model makes its trained parameters publicly downloadable, allowing anyone to run and inspect the model, though training code and data may remain closed. Native transparency refers to the model's ability to generate images with an alpha channel directly, enabling transparent backgrounds without post-processing. Qwen is Alibaba's series of large multimodal models, and Image 2.1 follows the earlier 20B-parameter Qwen-Image, offering a smaller footprint while retaining advanced generation and editing capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">GitHub - QwenLM/Qwen-Image-2.1: Qwen's most powerful open-source image generation model · GitHub</a></li>
<li><a href="https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight">Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and Editing, Now with Transparency</a></li>
<li><a href="https://d-central.tech/mining-glossary/open-weight-model/">Open - Weight Model Meaning | Bitcoin Mining Glossary</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the model's small size (7B vs 20B predecessor) and its native transparency as notable advantages, with some praising its superior text rendering compared to other open-weight models. Others pointed out the more restrictive license shown on GitHub, raising concerns about commercial use, and asked how to run the model locally similar to llama-server. Overall, the discussion reflects excitement about the model's capabilities tempered by licensing and usability questions.

**Tags**: `#AI`, `#image generation`, `#Qwen`, `#open-weight models`, `#text-to-image`

---

<a id="item-6"></a>
## [Terry Tao Questions Need for Human Mathematicians Amid AI Advances](https://terrytao.wordpress.com/2026/09/19/why-do-we-need-human-mathematicians-anymore/) ⭐️ 8.0/10

On September 19, 2026, Terry Tao published an essay on his blog asking whether human mathematicians are still needed given recent AI advances, arguing that understanding, creativity, and the formulation of new problems remain uniquely human. The essay highlights ongoing debates about AI's role in mathematical discovery, influencing how researchers view human‑AI collaboration and the future direction of pure mathematics. Tao emphasizes that while AI can assist with proof search and computation, it lacks genuine understanding and the ability to pose new mathematical questions, a point echoed by commenters referencing the Library of Babel and the fractal nature of math.

hackernews · auggierose · Sep 20, 10:49 · [Discussion](https://news.ycombinator.com/item?id=49774521)

**Background**: In recent years, AI systems such as large language models and automated theorem provers have been employed to assist with proof verification, conjecture generation, and symbolic computation. Terry Tao, a Fields Medalist renowned for his work in harmonic analysis, partial differential equations, and additive number theory, frequently engages with the implications of AI for mathematical practice. The essay contributes to a broader conversation about whether machines can truly replicate human insight and creativity in science.

**Discussion**: Commenters emphasized that without human understanding, AI-generated results remain meaningless, likening the situation to the Library of Babel where information lacks significance until interpreted. Others pointed out the infinite, fractal nature of mathematics, arguing that solving problems continually opens new ones, so AI cannot exhaust the field. A few speculated that AI might eventually steer mathematical research, while skeptics noted current AI is merely sophisticated brute‑force search relying on human‑produced knowledge.

**Tags**: `#mathematics`, `#AI`, `#human-AI collaboration`, `#philosophy of science`, `#Terry Tao`

---