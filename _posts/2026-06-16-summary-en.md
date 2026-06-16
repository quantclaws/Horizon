---
layout: default
title: "Horizon Summary: 2026-06-16 (EN)"
date: 2026-06-16
lang: en
---

> From 42 items, 16 important content pieces were selected

---

1. [vLLM v0.23.0 released with DeepSeek-V4 optimizations and Model Runner V2 expansion](#item-1) ⭐️ 8.0/10
2. [Malicious LinkedIn job offer hides npm backdoor in GitHub repo.](#item-2) ⭐️ 8.0/10
3. [Banned Book Library Hidden in Wi‑Fi Smart Light Bulb](#item-3) ⭐️ 8.0/10
4. [Iroh 1.0 launches P2P library with pluggable transports for direct app communication](#item-4) ⭐️ 8.0/10
5. [HN users discuss replacing Claude/GPT with local models for coding.](#item-5) ⭐️ 8.0/10
6. [Peopleless economy? Not technically impossible](#item-6) ⭐️ 8.0/10
7. [Fox Reportedly Seeks to Acquire Streaming Giant Roku](#item-7) ⭐️ 8.0/10
8. [Salesforce to Acquire Fin (formerly Intercom) for $3.6 Billion](#item-8) ⭐️ 8.0/10
9. [TimescaleDB's Hypercore Compression for Time-Series Data](#item-9) ⭐️ 8.0/10
10. [Anthropic launches Claude Corps fellowship for nonprofits](#item-10) ⭐️ 8.0/10
11. [Analysis Shows Memory Safety CVEs Differ Between Rust and C/C++](#item-11) ⭐️ 8.0/10
12. [Estimating Public Social Welfare Function from UK Life Satisfaction Survey](#item-12) ⭐️ 8.0/10
13. [Modeling Battery Bidding under Price Uncertainty with Mean-CVaR](#item-13) ⭐️ 8.0/10
14. [Quantum Horizon: Evaluating Quantum Threats to Bitcoin and Ethereum](#item-14) ⭐️ 8.0/10
15. [New Lookahead Propensity Statistic Detects LLM Forecast Bias](#item-15) ⭐️ 8.0/10
16. [New projection estimator extracts risk-neutral dependence from option portfolios.](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.23.0 released with DeepSeek-V4 optimizations and Model Runner V2 expansion](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 8.0/10

vLLM v0.23.0 includes 408 commits from 200 contributors (63 new) and introduces major optimizations for DeepSeek-V4 across multiple backends. It expands Model Runner V2 to be the default for Llama and Mistral dense models, adds FlashInfer sampler, breakable CUDA graphs, pipeline-parallel bubble elimination, and a unified parser, among other kernel and performance enhancements. These improvements significantly boost inference throughput and latency for state-of-the-art Mixture-of-Experts models like DeepSeek-V4, enabling faster deployment of large-scale AI applications. By extending Model Runner V2 to more architectures and adding Rust frontend features, vLLM broadens its hardware and language support, strengthening its position as a leading open‑source LLM inference engine. DeepSeek-V4 gains decoupled sparse MLA metadata, TRTLLM-gen attention kernels, EPLB support for Mega-MoE, selective prefix-cache retention, index-share for DSA MTP, and is detached from torch.compile with refactored attention/RoPE paths and an XPU decode path. Model Runner V2 now defaults for Llama and Mistral dense models, adds FlashInfer sampler, breakable CUDA graphs, pipeline-parallel bubble elimination, kernel block-size support for hybrid models, Gemma 4 MTP, while the Rust frontend introduces streaming generate, dynamic LoRA endpoints, and version/info APIs; multi‑tier KV cache offloading gains an object‑store secondary tier and per‑request policies, and a unified parser consolidates reasoning and tool‑call handling.

github · khluu · Jun 15, 05:27

**Background**: vLLM is a high‑throughput, memory‑efficient library for serving large language models, using techniques like PagedAttention and continuous batching to maximize GPU utilization. Model Runner V2 is a redesign of vLLM’s core execution engine that aims for cleaner, more modular code and better performance by re‑implementing the model runner from first principles. DeepSeek‑V4 is a Mixture‑of‑Experts language model released in 2026 with up to 1.6 trillion parameters and support for context lengths of one million tokens, requiring specialized kernels for efficient inference. The TRTLLM‑gen attention kernel is a TensorRT‑LLM‑based implementation that provides optimized attention operations for generation phases, often requiring specific KV‑cache layouts such as HND on newer GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html">Multi-Head, Multi-Query, and Group-Query Attention — TensorRT-LLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#Model Runner V2`, `#release`

---

<a id="item-2"></a>
## [Malicious LinkedIn job offer hides npm backdoor in GitHub repo.](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 8.0/10

A LinkedIn recruiter posed as a hiring manager and sent a job seeker a public GitHub repository supposedly containing a broken proof‑of‑concept for a Node.js project. The repository’s npm prepare script runs automatically after `npm install`, executing a backdoor that contacts an attacker‑controlled server. This incident illustrates how attackers combine social engineering with software supply‑chain tactics to target job seekers, a group that may be less cautious when evaluating code for interview tasks. It underscores the need for developers to scrutinize npm lifecycle scripts and for platforms to improve reporting and takedown mechanisms for malicious repos. The malicious payload is hidden in the repository’s `prepare` script, which npm executes automatically after dependencies are installed, allowing the attacker to run arbitrary code on the victim’s machine. The script was buried among commented‑out test files, making casual inspection unlikely to reveal the threat.

hackernews · lwhsiao · Jun 15, 20:00 · [Discussion](https://news.ycombinator.com/item?id=48546294)

**Background**: npm automatically runs a package’s `prepare` script after `npm install`, which is intended for tasks like building native assets but can be abused to execute arbitrary code. Supply‑chain attacks in the npm ecosystem have become increasingly common, with threat actors publishing or compromising packages to distribute malware, as highlighted by recent CISA alerts. Understanding these mechanisms helps developers recognize when a seemingly innocuous repository could trigger harmful behavior during dependency installation.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/?v=true">scripts - npm Docs</a></li>
<li><a href="https://www.tutorialpedia.org/blog/why-is-npm-running-prepare-script-after-npm-install-and-how-can-i-stop-it/">Why Does npm Run the Prepare Script After npm install? (And ...</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem</a></li>

</ul>
</details>

**Discussion**: Commenters observed that such scams are becoming more frequent and convincing, with several reporting similar attempts multiple times in recent months. They expressed frustration over the lack of a clear cybercrime reporting channel and noted that malicious repositories often remain online despite reports to GitHub and LinkedIn. Some advised caution, suggesting that job seekers should avoid running `npm install` on unfamiliar code without inspection.

**Tags**: `#security`, `#supply-chain attack`, `#npm`, `#LinkedIn scam`, `#social engineering`

---

<a id="item-3"></a>
## [Banned Book Library Hidden in Wi‑Fi Smart Light Bulb](https://www.richardosgood.com/posts/banned-book-library/) ⭐️ 8.0/10

A developer modified an ESP8266‑based Wi‑Fi smart light bulb to run a covert HTTP server that hosts EPUB copies of banned books such as Jack London’s *Call of the Wild* and Mark Twain’s *Adventures of Huckleberry Finn*, allowing discreet access to censored literature over the local network. The project shows how inexpensive IoT hardware can be repurposed for censorship circumvention, highlighting a low‑cost, accessible method to protect free speech and privacy in restrictive environments. The bulb’s ESP8266 chip was flashed with custom Tasmota/ESPHome firmware, enabling a lightweight web server that serves stored EPUB files; storage is limited to the flash memory (typically ~1 MB), so only a small selection of texts can be hosted, and access requires being on the same LAN or using mDNS to locate the device.

hackernews · sohkamyung · Jun 15, 22:37 · [Discussion](https://news.ycombinator.com/item?id=48547985)

**Background**: ESP8266 is a low‑cost Wi‑Fi microcontroller commonly used in DIY smart home devices such as Wi‑Fi light bulbs, and can be reprogrammed with open‑source firmware like Tasmota or ESPHome to add custom functionality. By running an embedded HTTP server on the chip, the bulb can serve files directly to clients on the same network, a technique demonstrated in various IoT web‑server tutorials. This approach mirrors earlier projects like PirateBox, which turned a wireless access point into an offline file‑sharing hub, showing how simple hardware can be used to bypass network‑based censorship.

<details><summary>References</summary>
<ul>
<li><a href="https://www.instructables.com/DIY-IoT-Lamp-for-Home-Automation-ESP8266-Tutorial/">DIY IoT Lamp for Home Automation || ESP8266 Tutorial : 13 Steps (with Pictures) - Instructables</a></li>
<li><a href="https://admantium.medium.com/tasmotizer-try-to-flash-a-wifi-led-light-with-a-custom-firmware-e9f0baed3bca">Tasmotizer: Try to Flash a WiFi LED Light with a Custom Firmware | by Sebastian | Medium</a></li>
<li><a href="https://www.microej.com/vee-features/hoka-http-web-server/">MicroEJ - Hoka HTTP Web Server for IoT Devices</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project’s ingenuity and its relevance to free speech, noting that such low‑cost hardware hacks could help preserve access to censored works. Several drew parallels to PirateBox and suggested extending the idea into a mesh network using solar‑powered lamps. Overall sentiment was enthusiastic, with many expressing interest in seeing the concept formalized or expanded.

**Tags**: `#hardware hacking`, `#IoT`, `#censorship circumvention`, `#DIY`, `#free speech`

---

<a id="item-4"></a>
## [Iroh 1.0 launches P2P library with pluggable transports for direct app communication](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0, a peer-to-peer networking library written in Rust, was released to enable direct app-to-app communication by dialing peers via public keys, using QUIC and offering pluggable transports that developers can extend. By abstracting transport details and removing the need for centralized coordination, Iroh simplifies building decentralized applications and lowers the barrier for developers to create resilient, peer‑based services. Its extensible transport model lets apps work across diverse networks without requiring users to manage accounts or external VPN clients. Iroh uses QUIC for hole‑punched direct connections, provides an iroh‑blobs layer for content‑addressed data transfer, and ships with IPv4, IPv6, and relay transports while allowing developers to implement custom transports in Rust to avoid a proliferation of feature flags. The library’s API centers on dialing by public key, automatically selecting the fastest available path and maintaining connections.

hackernews · chadfowler · Jun 15, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48542480)

**Background**: Peer‑to‑peer (P2P) networking allows devices to communicate directly without relying on central servers, often requiring NAT traversal techniques such as hole punching to establish connections across private networks. QUIC is a modern transport protocol that combines low‑latency connection establishment with built‑in encryption and supports UDP‑based hole punching. Pluggable transports, originally devised by the Tor Project to circumvent censorship, are modular components that transform network traffic, enabling a core protocol to adapt to different network environments by swapping in custom transport implementations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/n0-computer/iroh">n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. - GitHub</a></li>
<li><a href="https://www.iroh.computer/">Iroh</a></li>
<li><a href="https://torproject.gitlab.io/torspec/pt-spec.html">Pluggable Transport Specification (Version 1)</a></li>

</ul>
</details>

**Discussion**: Commenters compared Iroh to Tailscale but noted its application‑layer focus, with apitman describing it as “Tailscale at the application layer.” Developers highlighted the need for extensible transports, with rklaehn explaining that custom transport support avoids an unmaintainable maze of feature flags. Some users asked for clearer explanations of the cryptographic keys used for dialing, while others questioned the necessity of another P2P layer, and a few expressed enthusiasm for decentralized networking possibilities.

**Tags**: `#peer-to-peer`, `#networking`, `#Iroh`, `#release`, `#custom transports`

---

<a id="item-5"></a>
## [HN users discuss replacing Claude/GPT with local models for coding.](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

An Ask HN post asked whether anyone has fully replaced Claude or GPT with a local model as their main coding tool, prompting users to share their setups, performance numbers, and motivations such as data privacy and cost savings. The discussion highlights a growing trend toward locally run LLMs for coding, reflecting concerns about privacy, subscription costs, and the desire for offline, customizable AI assistants. Users reported setups ranging from a Mac Studio with 128 GB RAM running Qwen3.6‑35B (3B active parameters) to a dual RTX3090 workstation achieving ~150 tokens/s with Qwen and Gemma models via Unsloth Studio, and noted performance sufficient for most coding tasks though not matching frontier models like Claude Code.

hackernews · cloudking · Jun 15, 14:46

**Background**: Local large language models are open‑weight or source‑available models that can be run on personal hardware, offering offline inference and greater data privacy compared to proprietary APIs. The Qwen family, developed by Alibaba Cloud, includes models such as Qwen3.6‑35B released under the Apache 2.0 license. Gemma is a series of lightweight open‑weight LLMs from Google DeepMind, with versions like Gemma 4‑26B released in 2026 under a similar open‑access policy. These models enable developers to experiment with or replace commercial coding assistants while controlling costs and data exposure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemma_(language_model)">Gemma (language model)</a></li>

</ul>
</details>

**Discussion**: Commenters generally reported positive experiences swapping proprietary models for local Qwen and Gemma variants, citing privacy, cost savings, and sufficient performance for everyday coding, while a few noted that local models still lag behind frontier models like Claude Code and that the effort may not be worth it for high‑stakes work. Several highlighted the hardware needed (large RAM or multiple high‑end GPUs) and the use of tools like Unsloth Studio and containerized Pi harness to ensure offline operation.

**Tags**: `#LLM`, `#local AI`, `#coding assistants`, `#privacy`, `#HN discussion`

---

<a id="item-6"></a>
## [Peopleless economy? Not technically impossible](https://gmalandrakis.com/writings/ad-economicum.html) ⭐️ 8.0/10

The article examines whether an economy could operate without human labor as AI and automation advance, analyzing both technical feasibility and broader socioeconomic implications. It matters because it addresses a pressing debate about AI-driven job displacement and the future of work, informing policymakers, businesses, and workers about potential economic transformations. The piece weighs technical feasibility by referencing current AI‑driven automation technologies and discusses socioeconomic aspects such as wealth concentration, universal basic income, and the post‑scarcity paradox.

hackernews · l0new0lf-G · Jun 15, 21:10 · [Discussion](https://news.ycombinator.com/item?id=48547062)

**Background**: AI-driven automation refers to the use of artificial intelligence and robotics to perform tasks traditionally done by humans, increasing productivity while potentially displacing workers. A post-scarcity economy envisions a state where advanced automation and AI produce abundant goods and services, reducing the need for human labor. Concepts such as universal basic income are often discussed as mechanisms to distribute wealth in such an economy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/councils/forbesbusinesscouncil/2023/07/10/how-ai-and-automation-are-transforming-the-world/">How AI And Automation Are Transforming The World - Forbes Rebalancing AI-Daron Acemoglu Simon Johnson How new technologies enable the human-machine economy</a></li>
<li><a href="https://medium.com/chain-reaction/living-in-a-post-scarcity-society-how-automation-ai-and-universal-basic-income-could-reshape-the-de5b44704d7b">Living in a Post-Scarcity Society: How Automation, AI, and Universal Basic Income Could Reshape the Global Economy | by Daniel Bron | Chain Reaction | Medium</a></li>
<li><a href="https://economiclens.org/ai-and-automation-navigating-job-displacement-economic-inequality-in-2026/">AI and Automation: Job Displacement and Economic Inequality</a></li>

</ul>
</details>

**Discussion**: Commenters reacted with a mix of criticism and skepticism: some called the article annoying, others warned of a winner‑takes‑all outcome where AI concentrates wealth, questioned the motives of a consumer‑based economy, suggested listening to economists rather than engineers, and accused the author of misunderstanding money.

**Tags**: `#AI`, `#automation`, `#economics`, `#future of work`, `#technology impact`

---

<a id="item-7"></a>
## [Fox Reportedly Seeks to Acquire Streaming Giant Roku](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

Fox Corporation is reportedly in talks to acquire Roku, the leading provider of streaming hardware and platform services, according to sources cited by the Wall Street Journal. The deal would give a major media conglomerate direct control over a widely used streaming platform, potentially reshaping ad dynamics and content distribution in the U.S. TV ecosystem. Roku provides streaming players, smart TVs, and a platform that hosts thousands of channels; Fox owns numerous cable networks and a streaming service (Fox Nation), but neither party has disclosed an offer price or timeline.

hackernews · thm · Jun 15, 12:50 · [Discussion](https://news.ycombinator.com/item?id=48540499)

**Background**: Roku manufactures streaming players and licenses its operating system to TV makers, allowing users to access thousands of streaming channels over an internet connection without a traditional cable subscription. The company also sells ad‑supported content and operates its own Roku Channel. Fox Corporation is a major American media company that owns broadcast networks, cable channels such as Fox News and FX, and the streaming service Fox Nation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.roku.com/what-is-roku">What is Roku – How the Roku Experience Works | Roku</a></li>
<li><a href="https://www.roku.com/products?srsltid=AfmBOoqedEmh5W94ve41pfCISDYeHOt1gM1X_b0uJdD5gQtSmWphAiot">Roku Streaming, TV, & Smart Home Products</a></li>

</ul>
</details>

**Discussion**: Many commenters worry that Fox’s acquisition would compromise Roku’s neutral platform, increase ads, and introduce partisan content such as a ‘Fox News’ button. Some long‑time Roku users say they have already moved to alternatives like the Nvidia Shield to avoid ads and maintain a clean interface. Overall, the discussion reflects skepticism about the deal’s impact on user experience and platform independence.

**Tags**: `#media acquisition`, `#streaming`, `#Roku`, `#Fox`, `#business`

---

<a id="item-8"></a>
## [Salesforce to Acquire Fin (formerly Intercom) for $3.6 Billion](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce announced a definitive agreement to acquire Fin, the AI-driven customer service platform formerly known as Intercom, for approximately $3.6 billion. The acquisition aims to integrate Fin’s AI agent into Salesforce’s Agentforce platform to enhance autonomous customer service capabilities. The deal strengthens Salesforce’s position in the rapidly growing AI‑powered customer service market and counters competitors like Sierra and Decagon. It also brings over 30,000 business customers and a proven AI agent that resolves 76% of support requests autonomously into Salesforce’s ecosystem. Fin’s AI agent is built on its Apex‑powered platform and has been trained to autonomously handle a large share of support tickets. The acquisition is subject to customary purchase price adjustments and is expected to close pending regulatory approvals.

hackernews · colesantiago · Jun 15, 12:08 · [Discussion](https://news.ycombinator.com/item?id=48540126)

**Background**: Salesforce is a global leader in customer relationship management (CRM) software, offering a suite of cloud‑based applications for sales, service, and marketing. Fin, formerly Intercom, provides an AI‑driven customer service and messaging platform that uses pre‑trained agents to autonomously resolve support inquiries. Founded in 2011, Fin serves over 30,000 businesses and claims its AI agent can handle 76% of requests without human intervention. Salesforce’s Agentforce is its initiative to deliver autonomous AI agents across the enterprise, making Fin a strategic fit for expanding those capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fin_(company)">Fin (company) - Wikipedia</a></li>
<li><a href="https://qz.com/salesforce-acquires-fin-intercom-ai-customer-service-061526">Salesforce acquires Fin, formerly Intercom, for $3.6 billion</a></li>
<li><a href="https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/">Salesforce Signs Definitive Agreement to Acquire Fin</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some highlighted that AI can improve support when properly implemented, while others doubted the long‑term value of traditional helpdesk SaaS or criticized Salesforce’s tendency to make products overly complex. Several noted the growing competition in the AI customer‑agent space (e.g., Sierra, Decagon) and saw the acquisition as a move to keep AI agents within the Salesforce ecosystem rather than letting them become independent control points. A few users shared personal experiments with self‑hosted agents using tools like Hermes and local Gemma 4 models.

**Tags**: `#Salesforce`, `#acquisition`, `#AI customer service`, `#Fin`, `#CRM`

---

<a id="item-9"></a>
## [TimescaleDB's Hypercore Compression for Time-Series Data](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

The article explains how TimescaleDB achieves compression ratios of up to 98% for time-series data using its Hypercore columnar storage engine, which stores new data in row-based PostgreSQL chunks and automatically converts older chunks to a compressed columnar format. High compression reduces storage costs while preserving queryability, making TimescaleDB more attractive for large-scale IoT, monitoring, and analytics workloads where efficient historical data access is crucial. Hypercore is a hybrid row‑columnar store: recent inserts stay in mutable Postgres rows for fast writes, while older chunks are column‑compressed using techniques such as dictionary encoding and delta‑of‑delta, achieving up to 98% size reduction.

hackernews · lkanwoqwp · Jun 15, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48544451)

**Background**: TimescaleDB is an open-source extension of PostgreSQL that optimizes storage and query performance for time-series data by automatically partitioning data into time-based chunks. Its Hypercore engine implements a hybrid row‑columnar layout where newer data remains in row format for high‑throughput writes, and older data is converted to a columnar format that enables efficient compression and analytical scans. Columnar storage allows compression algorithms like dictionary encoding and delta‑of‑delta to achieve high ratios while still supporting fast aggregation and filtering. This design aims to balance storage efficiency with query speed, addressing the classic IO‑vs‑CPU trade‑off in database compression.

<details><summary>References</summary>
<ul>
<li><a href="https://roszigit.com/en/blog/timescaledb-compression-hypercore">TimescaleDB Compression: Hypercore and Columnar Storage with up to 98% Ratio in PostgreSQL</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/hypercore/">Tiger Data Documentation | Hypercore</a></li>

</ul>
</details>

**Discussion**: Commenters debated how compression affects query performance, with gopalv emphasizing that any method should improve filter rejection or scan speed rather than merely trading I/O for CPU. Others highlighted alternative approaches such as tudorg’s deltax extension using min/max, sum, bloom filters, heliosAtwork’s reference to swinging‑door compression for IoT, and blackoil’s note on Gorilla’s delta‑of‑delta, showing broad interest in optimizing both storage and analytics.

**Tags**: `#TimescaleDB`, `#time-series databases`, `#compression`, `#PostgreSQL`, `#Hypercore`

---

<a id="item-10"></a>
## [Anthropic launches Claude Corps fellowship for nonprofits](https://www.anthropic.com/news/claude-corps) ⭐️ 8.0/10

Anthropic announced Claude Corps, a fully‑funded, 12‑month paid fellowship that places early‑career AI‑skilled talent inside U.S. nonprofits to deploy Claude models, with CodePath serving as the fellows’ employer of record. The program seeks to accelerate AI adoption in mission‑driven organizations while sparking debate over potential long‑term costs, sustainability, and ethical implications of placing powerful AI systems in nonprofits. Fellows work full‑time inside host nonprofits, develop software that the organization retains after the fellowship, and are employed by CodePath; the program covers travel and logistics and is backed by Anthropic’s $150 million commitment.

hackernews · Mustan · Jun 15, 17:41 · [Discussion](https://news.ycombinator.com/item?id=48544637)

**Background**: Claude is Anthropic’s family of large language models trained with constitutional AI to improve alignment and safety. Since its inception, Anthropic has emphasized responsible AI deployment and has published frameworks addressing job displacement and model governance. The Claude Corps fellowship follows a growing trend of tech companies placing AI talent in social‑sector organizations to drive impact while examining societal effects.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-corps/fellow">Claude Corps fellows FAQ \ Anthropic</a></li>
<li><a href="https://dmbio.com/blog/what-is-the-claude-corps">What Is the Claude Corps and How Does Anthropic's $150... | dmbio</a></li>
<li><a href="https://www.reddit.com/r/aicuriosity/comments/1u30eq1/anthropic_launches_claude_corps_fellowship/">Anthropic Launches Claude Corps Fellowship Program to Support US Nonprofits with AI : r/aicuriosity - Reddit</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns that nonprofits may inherit expensive AI systems without in‑house expertise to maintain them, questioned the program’s similarity to “AI missionaries,” and debated whether it risks job displacement despite Anthropic’s stated goals.

**Tags**: `#AI`, `#Anthropic`, `#nonprofit`, `#fellowship`, `#AI ethics`

---

<a id="item-11"></a>
## [Analysis Shows Memory Safety CVEs Differ Between Rust and C/C++](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html) ⭐️ 8.0/10

The article, published June 15, 2026 by kobzol, examines how memory safety CVEs are reported in Rust and C/C++ projects and argues that comparing raw CVE counts is a misleading metric for language safety. Highlighting the flaws in simple CVE comparisons, the analysis guides developers and security teams toward more nuanced vulnerability assessments when evaluating Rust versus C/C++ codebases. The piece notes that raw CVE totals can be skewed by factors such as differing disclosure practices, the role of unsafe code in Rust, and varying severity thresholds, and it cites community feedback warning against overreliance on CVE numbers.

hackernews · nicoburns · Jun 15, 16:11 · [Discussion](https://news.ycombinator.com/item?id=48543392)

**Discussion**: Commenters generally agree that comparing raw CVE counts between Rust and C/C++ is misleading, noting that Rust's type system shifts vulnerability classes (e.g., panics vs undefined behavior). Some argue that Rust's safety guarantees move certain bugs into denial-of-service territory, while others point out that C's lack of preconditions can lead to exploitable flaws that Rust would catch. Overall, the discussion emphasizes the need for context‑aware vulnerability metrics rather than simple tallies.

**Tags**: `#Rust`, `#C/C++`, `#memory safety`, `#CVEs`, `#software security`

---

<a id="item-12"></a>
## [Estimating Public Social Welfare Function from UK Life Satisfaction Survey](https://arxiv.org/abs/2606.13752) ⭐️ 8.0/10

Using a novel survey instrument with a representative UK sample of 2,068 respondents, the authors estimate the public's social welfare function for life satisfaction, finding a median isoelastic parameter α = 0.48. The results provide ethically grounded distributional weights for wellbeing‑based policy evaluation and cost‑benefit analysis, addressing a gap in eliciting public preferences over utility measured by subjective wellbeing. The median isoelastic parameter α = 0.48 indicates strong aversion to wellbeing inequality, implying that improving the least satisfied person's life satisfaction by one unit is valued about twice as much as improving the most satisfied person's by one unit.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: An isoelastic social welfare function aggregates individual utilities with a constant inequality aversion parameter α, where lower α places greater weight on improving the welfare of worse‑off individuals. While many studies have estimated SWFs using income as the proxy for utility, this paper directly elicits public preferences over utility measured by subjective wellbeing (life satisfaction). The approach fills a methodological gap by providing empirically derived distributional weights that can be applied in wellbeing‑based cost‑benefit analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://www.statisticalconsultants.co.nz/blog/social-welfare-functions.html">Social Welfare Functions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isoelastic_utility">Isoelastic utility - Wikipedia</a></li>
<li><a href="https://web.stanford.edu/~yyye/GeometricAggregationofSWChicago.pdf">Geometric Aggregation of the Social Welfare Function in ...</a></li>

</ul>
</details>

**Tags**: `#social welfare function`, `#subjective wellbeing`, `#inequality aversion`, `#public policy`, `#survey methodology`

---

<a id="item-13"></a>
## [Modeling Battery Bidding under Price Uncertainty with Mean-CVaR](https://arxiv.org/abs/2606.14050) ⭐️ 8.0/10

The authors develop an asset‑level model of a price‑taking battery that submits stepwise buy and sell bid curves in the day‑ahead market under a finite set of price scenarios, optimizing a mean‑CVaR objective. They show the mixed‑integer formulation can be exactly reformulated as a linear program and provide empirical evidence that apparent withholding can arise without market power. The work offers a tractable, exact LP tool for analyzing battery bidding behavior, helping market operators distinguish strategic withholding from rational responses to price uncertainty and risk preferences. This advances both energy‑systems modeling and wholesale market design. The model assumes a finite set of price scenarios, stepwise bid curves, and physical constraints (state‑of‑charge limits, charge/discharge rates). By relaxing integer decisions, the authors obtain an exact LP reformulation; empirical results reveal three insights: withholding without market power, state‑of‑charge‑dependent impact of uncertainty, and layered bid curves from risk management.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: In wholesale electricity markets, generators and storage assets submit bid curves to the day‑ahead market, where prices are set based on supply‑demand equilibrium. Price uncertainty arises because future market prices are unknown when bids are submitted, prompting participants to manage risk. Conditional Value at Risk (CVaR) measures the expected loss in the worst‑case tail of a distribution, and a mean‑CVaR objective balances expected profit against risk aversion.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.14050">Battery Bidding under Price Uncertainty in Wholesale Electricity ...</a></li>
<li><a href="https://www.financestrategists.com/wealth-management/risk-profile/conditional-value-at-risk-cvar/">Conditional Value at Risk ( CVaR ) | Meaning , Pros, and Cons</a></li>

</ul>
</details>

**Tags**: `#electricity markets`, `#battery storage`, `#optimization`, `#risk management`, `#wholesale markets`

---

<a id="item-14"></a>
## [Quantum Horizon: Evaluating Quantum Threats to Bitcoin and Ethereum](https://arxiv.org/abs/2606.14484) ⭐️ 8.0/10

The paper analyzes quantum computing threats to Bitcoin and Ethereum, showing that Shor's algorithm can break the elliptic‑curve signatures (ECDSA over secp256k1, BLS over BLS12‑381) that authorize transactions, while Grover's algorithm only gives a limited quadratic speedup to proof‑of‑work mining. Using a Monte‑Carlo forecast that folds hardware scaling, expert surveys and fault‑tolerance lag, it estimates about a one‑in‑six chance of a cryptographically relevant quantum computer by 2035, near 30% by 2040 and about 60% by 2050. Understanding these risks helps blockchain developers and users prioritize migration to post‑quantum signatures before a sufficiently powerful quantum computer appears, highlighting that the main barrier is governance rather than technology. The findings also inform broader cryptocurrency ecosystems, as none of the top twenty coins are currently fully post‑quantum secure. The study notes that of Bitcoin’s roughly six million quantum‑exposed coins only about 2.3 million are irreducibly at risk, while 50‑65% of Ether resides in key‑revealed accounts that can adopt post‑quantum signatures. It also distinguishes Shor’s exponential break of ECDSA from Grover’s merely quadratic impact on mining, and provides reproducible Monte‑Carlo models for each quantitative claim.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Quantum computers can run algorithms that outperform classical ones for specific problems. Shor’s algorithm factors integers in polynomial time, breaking elliptic‑curve digital signatures such as ECDSA used by Bitcoin and Ethereum. Grover’s algorithm offers only a quadratic speedup for unstructured search, which translates to a limited advantage for proof‑of‑work mining. Post‑quantum cryptography aims to replace vulnerable signatures with algorithms believed to resist quantum attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grover's_algorithm">Grover's algorithm - Wikipedia</a></li>
<li><a href="https://www.flavius.io/media/a-word-on-secp256k1-and-ecdsa">What exactly are secp256k1, ECDSA and Keccak256 ?</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#blockchain`, `#cryptography`, `#Bitcoin`, `#Ethereum`

---

<a id="item-15"></a>
## [New Lookahead Propensity Statistic Detects LLM Forecast Bias](https://arxiv.org/abs/2512.23847) ⭐️ 8.0/10

The paper introduces Lookahead Propensity (LAP), a date-only recall-based statistic that estimates the probability an LLM has internalized realized outcomes, and uses it to test for lookahead bias in LLM-generated economic forecasts. Detecting lookahead bias is crucial for ensuring the validity of AI-assisted forecasts in finance and policy, and the proposed test offers a low‑cost diagnostic that can be applied to any LLM forecasting task. LAP is computed via a date‑only recall query for each firm‑date pair; it is substantially positive during the in‑sample period and drops to near zero after the model’s training‑data cutoff, and a significant positive interaction between LAP and the LLM forecast in an accuracy regression indicates lookahead‑bias contamination.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Lookahead bias occurs when a model inadvertently uses information from the future to make predictions, inflating its apparent performance. In LLM forecasting, this can happen if the model has seen future outcomes during training and retains them in its parameters. The paper’s date‑only recall query isolates whether the model can retrieve the actual outcome based only on the date, providing a proxy for such inadvertent future knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.23847">A Test of Lookahead Bias in LLM Forecasts</a></li>
<li><a href="https://www.emergentmind.com/topics/lookahead-propensity-lap">Lookahead Propensity in Estimation & LLMs</a></li>
<li><a href="https://openreview.net/pdf/fd5f42fe9f767b50e90cf6ad3f7e2528f0f3d759.pdf">[PDF] Recall as a Diagnostic for LLM Forecasting Errors - OpenReview</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#forecasting`, `#lookahead bias`, `#econometrics`, `#machine learning`

---

<a id="item-16"></a>
## [New projection estimator extracts risk-neutral dependence from option portfolios.](https://arxiv.org/abs/2601.14852) ⭐️ 8.0/10

The paper proposes a projection estimator that uses portfolios of observed options to approximate payoffs depending on multiple assets, delivering estimates of risk-neutral dependence, improving univariate estimates, and providing finite-sample error bounds, illustrated by analyzing Swiss National Bank announcements' effect on EUR/CHF and USD/CHF joint movements. It solves a long‑standing open problem of extracting dependence from option prices, enabling better risk assessment and portfolio management in incomplete markets, with empirical evidence from Swiss National Bank policy shocks showing that dependence accounts for two‑thirds of the change in joint extreme‑move probabilities. The estimator projects multi‑asset payoffs onto the span of traded option payoffs, derives a finite‑sample bound showing it attains (up to a constant) the smallest pricing error within that span, and finds that dependence explains about 66% of the probability change when EUR/CHF and USD/CHF both fall sharply after SNB floor announcements.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Risk‑neutral moments (variance, skewness, kurtosis) can be inferred from option prices but only describe the distribution of a single asset; they do not directly reveal dependence between assets. In incomplete markets, arbitrage pricing does not uniquely determine the risk‑neutral measure, so additional assumptions or constraints are needed to estimate dependence. While the Carr–Madan formula shows how to replicate any payoff via option portfolios, extracting higher‑order joint moments has remained an open problem. The proposed projection estimator works within the tensor space of traded options, providing controllable error bounds in finite samples and thus approximating multi‑asset risk‑neutral dependence.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.14852v1">Beyond Carr–Madan: A Projection Approach to Risk-Neutral ... - arXiv</a></li>
<li><a href="https://www.researchgate.net/publication/335993382_Option_Implied_Dependence">(PDF) Option Implied Dependence</a></li>
<li><a href="https://bsic.it/risk-neutral-density-estimation-from-option-prices/">Risk Neutral Density Estimation from Option Prices – BSIC</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#options pricing`, `#risk-neutral moments`, `#dependence estimation`, `#econometrics`

---