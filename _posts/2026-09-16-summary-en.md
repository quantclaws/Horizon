---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 63 items, 17 important content pieces were selected

---

1. [Introducing System One Models and Jev for Fast Typed Inference](#item-1) ⭐️ 8.0/10
2. [E-Ink Frame Listens to Birds and Draws 1800s-Style Illustrations](#item-2) ⭐️ 8.0/10
3. [Internet Archive adds protections to Wayback Machine against scraper traffic.](#item-3) ⭐️ 8.0/10
4. [Google launches Gemini 3.8 Live and Extended Thinking models](#item-4) ⭐️ 8.0/10
5. [Rheinmetall open-sources Battlesuite weapon system API documentation](#item-5) ⭐️ 8.0/10
6. [AI Agent Finds Leaked GitHub Token, Grants Admin Access to Baseten in 25 Minutes](#item-6) ⭐️ 8.0/10
7. [Building a Linux GPU Driver for the M4 Mac Mini in One Month](#item-7) ⭐️ 8.0/10
8. [Tensordyne's Napier Chip Uses Logarithmic Number System for Faster AI Inference](#item-8) ⭐️ 8.0/10
9. [Google releases Gemini 3.8 Live speech-to-speech models with browser demo](#item-9) ⭐️ 8.0/10
10. [Diffusion Models Generate Dynamic Volatility Surfaces for Better Option Hedging](#item-10) ⭐️ 8.0/10
11. [Study shows retail prop firm evaluations misalign incentives and skill signals.](#item-11) ⭐️ 8.0/10
12. [The Economics of Recursive Self-Improvement](#item-12) ⭐️ 8.0/10
13. [ViperQ: Order Flow Pattern Recognition via Auction Market Theory for RL Trading](#item-13) ⭐️ 8.0/10
14. [Receipt-Based Audit Reveals Frontier Agentic QA Fails on Buried Evidence](#item-14) ⭐️ 8.0/10
15. [Markovian embedding enables strong 1/2-order simulation for rough Volterra SDEs](#item-15) ⭐️ 8.0/10
16. [PortBench Introduces Correlation-Aware Full-Pipeline Benchmark for LLM Portfolio Management](#item-16) ⭐️ 8.0/10
17. [CLQT: Closed-Loop Cost-Aware Benchmark for LLM Portfolio Agents](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Introducing System One Models and Jev for Fast Typed Inference](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

The Typesafe AI blog announced System One Models and Jev, a new method that enables rapid, low‑cost typed inference by trading general‑purpose text generation for fast, structured output. This approach can dramatically reduce latency and cost for LLM‑based applications that need structured responses, such as classification, form filling, or home‑assistant commands, opening up new use cases where speed and price are critical. Jev takes an arbitrary text input plus a set of questions (yes/no, multiple‑choice, or score) and returns answers in milliseconds at roughly $0.042 per million tokens, but it cannot generate free‑form text outside the defined schema.

hackernews · albelfio · Sep 15, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49717558)

**Background**: Typed inference constrains a language model’s output to conform to a predefined type or schema, allowing the model to skip unnecessary token generation and focus on filling in fields. Traditional LLMs generate text token‑by‑token, which can be slow and expensive when only structured data is needed. By limiting the output space, methods like Jev achieve faster decoding and lower compute cost while preserving the ability to understand complex prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Type_inference">Type inference - Wikipedia</a></li>
<li><a href="https://www.weka.io/learn/ai-ml/inference-optimization/">Inference Optimization: Practical Techniques for Faster, Cost-Effective AI - WEKA</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the launch as genuinely interesting, highlighting the home‑assistant demo that made the value click, while others cautioned that the speed claims may be misleading because Jev cannot perform general‑purpose generation like a Turing‑complete model.

**Tags**: `#LLM`, `#structured inference`, `#typed models`, `#AI efficiency`, `#prompt engineering`

---

<a id="item-2"></a>
## [E-Ink Frame Listens to Birds and Draws 1800s-Style Illustrations](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

The project fugleramme uses an e-ink display paired with a microphone to capture bird sounds, classifies them in real time with the BirdNET model, and renders 1800s-style illustrations of the identified birds on the screen. It demonstrates a creative, low-power intersection of AI sound classification and e-ink art, offering an engaging way to experience biodiversity while showcasing how existing open‑source tools can be repurposed for poetic hardware art. The system runs on an ESP32 (or BTLE) board, uses BirdNET’s lightweight TensorFlow Lite model for classification, and stores or generates 1800s‑style bird illustrations that are refreshed on the e‑ink screen after each identification.

hackernews · arnemunthekaas · Sep 15, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49711544)

**Background**: BirdNET is a deep learning model trained on audio to identify bird species, optimized for edge devices with lightweight TensorFlow Lite versions. E‑ink displays mimic paper, consuming power only when the image changes, which enables very long battery life for always‑on projects. Combining these technologies allows a low‑power, always‑on frame that listens for birds and displays artistic illustrations.

<details><summary>References</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.adafruit.com/category/150?srsltid=AU7gw4Xy_TOOiJ_KMKWJzC9lg41yGC9dPcj4cd5LC6s2w513lCXiCQAW">LCDs & Displays, eInk / ePaper Products Category on ... - Adafruit</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project as magical and inspiring, noting BirdNET is a traditional neural network rather than an LLM. They highlighted e‑ink’s low power consumption and long battery life, made playful references to other bird‑related projects, and expressed pride in the Norwegian developer.

**Tags**: `#e-ink`, `#bird classification`, `#AI art`, `#hardware hack`, `#creative tech`

---

<a id="item-3"></a>
## [Internet Archive adds protections to Wayback Machine against scraper traffic.](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

The Internet Archive has added protections to the Wayback Machine to block high-volume automated traffic from scrapers attempting to bypass site blocks. The Wayback Machine is a crucial resource for digital preservation, and mitigating abusive traffic helps ensure its continued availability for researchers and the public. The protections were prompted by waves of scraper traffic that also led some sites to opt out of archiving, and the Archive notes that service remains accessible via Tor without centralized gatekeepers.

hackernews · ChrisArchitect · Sep 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49716176)

**Background**: The Wayback Machine, operated by the Internet Archive, stores snapshots of web pages to enable users to view historical versions of websites. As a free, non-profit service, it relies on limited resources and can be disrupted by excessive automated requests. High-volume scraping not only strains the archive’s infrastructure but may also encourage content owners to withdraw their sites from archiving. Implementing traffic protections helps preserve the service’s availability for legitimate users such as researchers, journalists, and the public.

**Discussion**: Community discussion highlights appreciation for the Internet Archive’s efforts to maintain the Wayback Machine amid scraper attacks, with users praising its openness and accessibility via Tor. Some commenters report intermittent access problems, such as 429 errors on certain networks, while others share personal nostalgic uses of the archive. Overall, the thread reflects strong support for the Archive’s mission and concerns about preserving the service from abusive traffic.

**Tags**: `#Internet Archive`, `#Wayback Machine`, `#web archiving`, `#cybersecurity`, `#digital preservation`

---

<a id="item-4"></a>
## [Google launches Gemini 3.8 Live and Extended Thinking models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google announced the release of Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, native speech‑to‑speech models that enable real‑time voice interaction, support 97 languages, and allow background tool execution without interrupting conversation. The update improves the fluency and responsiveness of AI voice agents, making them more suitable for multilingual users and enterprise workspace accounts, and positions Google to compete more closely with rivals such as GPT‑Live and Grok Voice. Gemini 3.8 Live Extended Thinking adds enhanced reasoning capabilities for multi‑step tasks, while both models run on Google’s TPU infrastructure, deliver low latency, and are accessible via workspace accounts for the first time.

hackernews · leumon · Sep 15, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49715947)

**Background**: Google’s Gemini series is a family of multimodal large language models designed for tasks ranging from text generation to reasoning. Earlier versions such as Gemini 3.5 Transcribe focused on speech‑to‑text capabilities, while the new Live models extend this to full duplex speech‑to‑speech interaction. The Live and Extended Thinking variants aim to make voice agents feel more like natural conversation partners by handling complex reasoning, visual context, and background tasks without breaking dialogue.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking</a></li>
<li><a href="https://officechai.com/ai/google-releases-gemini-3-8-live-extended-conversational-model-claims-better-performance-than-gpt-live-1-astra-and-grok-voice-think-fast-2-0-at-lower-price/">Google Releases Gemini 3.8 Live-Extended Conversational Model, Claims Better Performance Than Rivals At Lower Price</a></li>
<li><a href="https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/">Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production Grade Voice Agents - MarkTechPost</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the model’s strong Afrikaans fluency, pleasant voices, low latency, and the newly available workspace‑account access, which many had missed in prior releases. Some noted that Gemini’s prose feels more bearable than competitors’, while others wondered when Google would overtake rivals like Fable and Astra or release a Gemini 4. Overall sentiment is positive, with excitement about practical multilingual use and enterprise readiness.

**Tags**: `#Gemini`, `#LLM`, `#Google AI`, `#real-time AI`, `#language models`

---

<a id="item-5"></a>
## [Rheinmetall open-sources Battlesuite weapon system API documentation](https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html) ⭐️ 8.0/10

Rheinmetall has published the Onboard API specification for its Battlesuite connected weapon system as open source on GitHub, making the communication protocol publicly accessible. The move allows defense contractors, researchers, and hobbyists to inspect and integrate with a major military platform’s protocol, fostering interoperability and transparency in defense software ecosystems. The released documentation covers the Onboard API, including message formats and transport mechanisms, and is versioned 9.10.0 according to the provided URL.

hackernews · summarity · Sep 15, 21:07 · [Discussion](https://news.ycombinator.com/item?id=49718928)

**Background**: Rheinmetall’s Battlesuite is a digital platform designed to act as a central hub for data, communication, and decision‑making on the battlefield, integrating manned and unmanned systems, AI, resilient networks and cyber protection. The platform aims to link legacy equipment with emerging technologies through a modular, interoperable architecture. Open‑sourcing its Onboard API follows a trend of defense contractors publishing interface specifications to enable cross‑vendor integration, similar to standards such as the Tactical Microgrid Standard (TMS), Distributed Interactive Simulation (DIS), High Level Architecture (HLA) and Open Mission Systems (OMS).

<details><summary>References</summary>
<ul>
<li><a href="https://www.rheinmetall.com/en/products/digital-forces/digital-forces/battlesuite">Battlesuite – The interoperable military ecosystem of the future | Rheinmetall</a></li>
<li><a href="https://nextgendefense.com/rheinmetall-battlesuite-link-battlefield/">Rheinmetall Launches ‘Battlesuite’ to Link Weapons, Drones, and Data on Battlefield</a></li>
<li><a href="https://defence-industry.eu/rheinmetall-releases-battlesuite-onboard-and-tactical-api-specifications-as-open-source-for-defence-system-integration-across-platforms/">Rheinmetall releases Battlesuite Onboard and Tactical API specifications as open source for defence system integration across platforms</a></li>

</ul>
</details>

**Discussion**: Commenters drew comparisons to DDS, TMS, DIS/HLA, OMS and CORBA, noting both the protocol’s potential similarities and its differences. Several expressed interest in a lightweight, real‑time friendly alternative to heavyweight DDS that works on memory‑constrained embedded systems, while others jokingly remarked that CORBA “never died”. Overall, the discussion reflected strong technical curiosity about how Battlesuite’s protocol fits within existing defense communication standards.

**Tags**: `#defense`, `#open-source`, `#protocol`, `#embedded-systems`, `#real-time-communication`

---

<a id="item-6"></a>
## [AI Agent Finds Leaked GitHub Token, Grants Admin Access to Baseten in 25 Minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

An AI agent discovered a leaked GitHub personal access token in a public Harbor container registry, granting admin and push access to Baseten's production repositories. The finding was responsibly disclosed, leading Baseten to secure the project and rotate the token within a day. The incident underscores supply-chain risks from exposed secrets in artifact registries and shows how AI‑assisted penetration testing can dramatically accelerate vulnerability discovery. Organizations relying on GitHub and Harbor for CI/CD must strengthen secret scanning and token hygiene. The token provided admin and push rights to Baseten’s main product repo, GitOps repo, Homebrew tap, and read/write access to other private repositories, including customer‑specific ones. It was found in the Docker build history after the agent located a Baseten image, and remained valid after the Harbor project was made private until the token was rotated.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**Background**: Harbor is a CNCF‑graduated open‑source container registry that stores, signs, and scans Docker/OCI images and Helm charts, commonly used in Kubernetes environments. A GitHub personal access token (PAT) is a secret that can authenticate API requests and, depending on its scopes, grant read, write, or admin access to repositories and related services. Baseten is a platform for deploying and scaling AI models, relying on GitHub‑based GitOps pipelines and Harbor for storing its container images, making leaked tokens a direct path to production systems.

<details><summary>References</summary>
<ul>
<li><a href="https://goharbor.io/">Harbor</a></li>
<li><a href="https://docs.baseten.co/concepts/howbasetenworks">How Baseten works</a></li>
<li><a href="https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html">Grafana GitHub Token Breach Led to Codebase Download and Extortion Attempt</a></li>

</ul>
</details>

**Discussion**: Commenters praised the responsible disclosure and Baseten’s swift response, while questioning whether the AI agent’s testing was authorized beforehand. Several noted that AI agents excel at quickly finding low‑hanging fruit that humans might overlook, debating whether the speed advantage outweighs novelty of discoveries.

**Tags**: `#security`, `#vulnerability`, `#GitHub`, `#AI agents`, `#responsible disclosure`

---

<a id="item-7"></a>
## [Building a Linux GPU Driver for the M4 Mac Mini in One Month](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

A developer created a functional Linux GPU driver for Apple's M4 Mac Mini within one month by employing large language models to assist reverse engineering, which ignited debate over the legitimacy of the achievement and its suitability for upstream inclusion. The feat highlights how LLMs can dramatically accelerate driver development for undocumented hardware, potentially lowering barriers for Linux on Apple Silicon, while also raising ethical and policy questions about conflicts of interest and AI-assisted code in open‑source projects. The driver was built in roughly 30 days, leveraging LLMs to navigate the M4 GPU's complex firmware ABI. The author is a former Apple engineer who was banned from Asahi Linux for undisclosed LLM use, and the M4 GPU delivers about 4.26 TFLOPS FP32 performance.

hackernews · ADevWithAnIdea · Sep 15, 19:30 · [Discussion](https://news.ycombinator.com/item?id=49717638)

**Background**: Apple's M4 is a system‑on‑chip introduced in May 2024 that integrates a GPU with no public documentation, requiring reverse‑effort projects like Asahi Linux to bring Linux to Apple Silicon. Asahi Linux is a community‑driven effort that ports the Linux kernel to Apple‑based Macs by clean‑room reverse engineering of the SoC. Large language models have recently been explored to assist kernel development, excelling at small, well‑defined tasks such as generating patches or documentation, though they are not yet capable of authoring entirely new device drivers from scratch.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M4">Apple M4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2511.18924">LLM-Driven Kernel Evolution: Automating Driver Updates in Linux</a></li>

</ul>
</details>

**Discussion**: Commenters praised the speed and LLM‑assisted approach as a promising use case, while others criticized the author's undisclosed former Apple ties and potential conflict of interest, noting Asahi Linux's strict no‑AI policy would block upstream inclusion. Several urged the release of reproducible code and documentation regardless of upstream prospects.

**Tags**: `#GPU driver`, `#Apple Silicon`, `#Linux`, `#LLM`, `#Reverse engineering`

---

<a id="item-8"></a>
## [Tensordyne's Napier Chip Uses Logarithmic Number System for Faster AI Inference](https://spectrum.ieee.org/inference-hardware-revolution) ⭐️ 8.0/10

Tensordyne announced its 3nm Napier AI inference chip, which employs a proprietary logarithmic number system to replace costly multiplications with additions, achieving up to 1,300 tokens per second per user and claiming up to 13× higher throughput than existing architectures. By cutting the energy and area costs of multiplication, the Napier chip could lower the power consumption and expense of AI inference workloads, offering a viable alternative to GPU‑centric accelerators and enabling broader deployment of large language models. The chip uses the identity log(A×B)=log A+log B, performing multiplication via addition in log space; it integrates 144 GB of HBM3e and 256 MB of SRAM per processor, is built on a 3 nm process, and is positioned as a rack‑scale system called Napier.

hackernews · vinhnx · Sep 15, 14:24 · [Discussion](https://news.ycombinator.com/item?id=49713024)

**Background**: AI inference involves repeatedly multiplying large matrices and vectors, a process that traditionally demands significant silicon area and power for multiplier circuits. A logarithmic number system (LNS) represents numbers as their logarithms, turning multiplication into addition because log(A×B)=log A+log B, but addition in LNS becomes more complex and often requires lookup tables or extra logic. Earlier efforts to apply LNS in hardware faced challenges due to this added complexity, yet recent advances in process technology and memory integration have renewed interest. Tensordyne’s Napier chip aims to exploit the LNS advantage while mitigating its drawbacks through tight coupling with high‑bandwidth memory and large on‑chip SRAM.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/dharmesh0103_aichips-tensordyne-semiconductors-activity-7474367811415334912-2ipn">Tensordyne's Logarithmic Number System for AI Inference | LinkedIn</a></li>
<li><a href="https://www.eetimes.com/podcasts/how-tensordyne-built-an-ai-accelerator-around-logarithmic-math/">Tensordyne's AI Accelerator Built Around Logarithmic Math</a></li>
<li><a href="https://convergedigest.com/tensordyne-tapes-out-3nm-napier-ai-inference-proce/">Tensordyne Tapes Out 3nm Napier AI Inference ... - Converge Digest</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article for highlighting a novel logarithmic approach to AI inference, noting the potential power and area savings. Some drew parallels to the historical evolution of CPUs, expecting multiple architectural advances rather than a single breakthrough. A few users pointed out that the article’s Scrabble analogy was helpful for training but less clear for inference, while others raised unrelated topics such as Anthropic’s large compute leasing deals.

**Tags**: `#AI inference`, `#hardware acceleration`, `#logarithmic number system`, `#chip architecture`, `#Napier`

---

<a id="item-9"></a>
## [Google releases Gemini 3.8 Live speech-to-speech models with browser demo](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 8.0/10

Google announced Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, two new speech-to-speech models, and Simon Willison created a browser-based demo UI for trying them out. The release advances real-time voice AI by offering low-latency, full-duplex interactions comparable to OpenAI's GPT-Live, and the community demo makes the technology more accessible to developers. The models connect via a WebSocket endpoint (wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent) and use the Web Audio API AudioContext for microphone capture and playback; the demo supports voice presets, optional system prompts, and interrupting the model's response.

rss · Simon Willison · Sep 15, 22:47

**Background**: Speech-to-speech models enable direct audio-to-audio conversation without intermediate text transcription, allowing low-latency, full-duplex voice interactions. Google's Gemini 3.8 Live and Extended Thinking are part of its generative AI lineup, designed to compete with OpenAI's GPT-Live family which also emphasizes simultaneous listening and speaking. Developers can interact with these models via a WebSocket API and handle audio capture/playback in the browser using the Web Audio API's AudioContext.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT‑Live - OpenAI</a></li>

</ul>
</details>

**Tags**: `#Gemini`, `#speech-to-speech`, `#AI models`, `#Google`, `#voice AI`

---

<a id="item-10"></a>
## [Diffusion Models Generate Dynamic Volatility Surfaces for Better Option Hedging](https://arxiv.org/abs/2609.13402) ⭐️ 8.0/10

The paper introduces AD-Seq-Vol and its arbitrage‑fine‑tuned variant AD-Seq-Vol-FT, two diffusion‑model frameworks that jointly learn the evolution of asset returns and high‑dimensional implied‑volatility surfaces. Using SPX options data from 2000‑2023, the models generate coherent surface trajectories and, especially AD-Seq-Vol-FT, reduce static‑arbitrage violations to near zero while improving data‑driven option hedging performance. By producing realistic, arbitrage‑free volatility surface paths, the framework offers a more reliable tool for data‑driven hedging and risk management, potentially lowering hedging costs and tail‑risk exposure for market participants. Its ability to capture cross‑sectional and temporal dependencies also advances the application of generative models in financial modeling. AD-Seq‑Vol jointly models the evolution of asset returns and the implied‑volatility surface using a sequential diffusion process, while AD-Seq‑Vol‑FT adds a post‑training penalty term that discourages static‑no‑arbitrage violations. On daily SPX options data (2000‑2023), AD-Seq‑Vol‑FT drives static‑arbitrage violations to near zero and the resulting diffusion‑based hedges maintain near‑zero tracking errors, substantially cut tail risk, and remain stable during the COVID‑19 market turmoil; the implementation is publicly available at https://github.com/yinbinhan/volatility-surface-simulation.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Diffusion models are generative models that create data by iteratively denoising a random noise sample, and have been successfully applied in image, audio, and more recently financial data synthesis. An implied‑volatility surface represents option implied volatilities across different strikes and maturities, capturing market expectations of future volatility; static no‑arbitrage conditions require that this surface be free of risk‑free profit opportunities across strikes and expiries. Data‑driven hedging uses historical or simulated market scenarios to construct option hedges without relying on parametric pricing models, aiming to reduce tracking error and tail risk.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.13402v1">Diffusion models for dynamic volatility surface generation ...</a></li>
<li><a href="https://bigquant.com/square/paper/40a2b374-37ab-4c32-9621-50aef2e15c72">Diffusion models for dynamic volatility surface generation ...</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#volatility surface`, `#option hedging`, `#financial machine learning`, `#arbitrage-free modeling`

---

<a id="item-11"></a>
## [Study shows retail prop firm evaluations misalign incentives and skill signals.](https://arxiv.org/abs/2609.14859) ⭐️ 8.0/10

The paper analyzes the two‑stage evaluation used by retail proprietary‑trading firms, showing that passing the evaluation is a poor standalone signal of trader skill because pass rates are heavily driven by position sizing rather than true edge. It finds that with zero skill, position sizing alone yields a pass probability of about 0.40, while the observed cohort pass rate is only 0.168. This work exposes how proprietary‑trading evaluation contracts can misalign incentives, causing firms to overestimate trader skill and potentially misallocate capital. It provides a quantitative framework for traders, firms, and academics to assess and improve evaluation designs in retail prop trading. The model shows that under end‑of‑day trailing drawdown the evaluation phase rewards a fast, lumpy trading cadence, whereas the funded account phase penalizes it by roughly a factor of nine in the joint gate. Consequently, a trader with zero skill can achieve a pass probability near 0.40 through position sizing alone, and break‑even requires a win rate of about 40.5%–41.5% at a 1:1.5 reward‑to‑risk ratio net of costs.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Retail proprietary‑trading firms offer traders a paid evaluation phase where they must reach a profit target without breaching a trailing drawdown; successful traders then receive a funded account subject to additional rules such as a minimum survival window and a consistency rule before any profit payout. The trailing drawdown measures losses relative to a moving high‑water mark, and can be calculated intraday or at end‑of‑day, affecting how traders manage risk. The consistency rule limits the proportion of total profit that may come from a single best day, encouraging more stable performance. These mechanisms together create a contract whose geometry influences trader incentives differently across the two stages.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.14859">[2609.14859] Gate Design and Stage -Dependent Incentives in Retail ...</a></li>
<li><a href="https://tradeify.co/post/trailing-drawdown-explained-for-prop-firm-traders">Trailing Drawdown Explained for Prop Firm Traders</a></li>
<li><a href="https://fundingtraders.com/blog/prop-firm-consistency-rules/">Prop Firm Consistency Rules: Who Has One, Who Doesn't</a></li>

</ul>
</details>

**Tags**: `#proprietary trading`, `#incentive design`, `#financial contracts`, `#algorithmic trading`, `#market microstructure`

---

<a id="item-12"></a>
## [The Economics of Recursive Self-Improvement](https://arxiv.org/abs/2609.15802) ⭐️ 8.0/10

The authors of arXiv:2609.15802v1 model the economics of recursive self‑improvement, representing AI progress as directed graphs and showing that net acceleration depends on the product of elasticities across feedback loops. They distinguish narrow from broad AI capabilities and, using existing data, find that current feedback loops are not strong enough to produce self‑sustaining AI acceleration, though they are strengthening. The paper offers a novel theoretical framework for evaluating recursive self‑improvement, helping AI safety researchers and policymakers gauge whether AI progress could become self‑reinforcing. By identifying measurable elasticities and distinguishing narrow versus broad capabilities, it guides empirical data collection that could inform governance and investment decisions. The model treats AI progress as a directed graph where each edge represents a feedback loop, and overall acceleration equals the product of the elasticities of those loops. It separates narrow AI (improving only on AI‑R&D benchmarks) from broad AI (improving on economically valuable tasks), and calibrates the model with existing estimates, concluding that the current product of elasticities is below the threshold for self‑sustaining growth but is increasing.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Recursive self‑improvement (RSI) refers to a process where an AI system enhances its own capabilities, which in turn enables further improvements, creating a feedback loop. In economics, elasticity measures how responsive one variable is to changes in another; here it quantifies how much AI capability growth responds to improvements in AI research and development. Narrow AI excels at specific, well‑defined tasks (such as optimizing AI‑R&D benchmarks), whereas broad AI would improve across a wide range of economically valuable activities. Representing these interactions as directed graphs allows researchers to trace the flow of influence and compute the overall effect as the product of elasticities along each loop.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.15802v1">The Economics of Recursive Self-Improvement - arXiv</a></li>
<li><a href="https://elasticity.institute/rsi-paper.pdf">[PDF] The Economics of Recursive Self-Improvement - Elasticity Institute</a></li>
<li><a href="https://medium.com/@maria-andraw/broad-ai-general-ai-and-narrow-ai-understanding-the-spectrum-of-artificial-intelligence-d3e489bee6be">Broad AI, General AI, and Narrow AI: Understanding the ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#recursive self-improvement`, `#economic modeling`, `#AI progress`, `#feedback loops`

---

<a id="item-13"></a>
## [ViperQ: Order Flow Pattern Recognition via Auction Market Theory for RL Trading](https://arxiv.org/abs/2609.13825) ⭐️ 8.0/10

ViperQ introduces a reinforcement learning trading framework that encodes Auction Market Theory primitives into a 20‑dimensional state representation and trains two PPO agents with an asymmetric prospect‑theory reward function. By grounding RL trading in practitioner microstructure concepts, ViperQ bridges the gap between academic RL and real‑world trading practice, offering a structured, theory‑driven input modality that could improve the performance and interpretability of algorithmic trading systems. The 20‑dimensional Z‑normalised state comprises Volume Point of Control, Value Area position, Low Volume Node flags, Cumulative Volume Delta divergence, and tape‑velocity signatures; two PPO agents are trained with a prospect‑theory‑based asymmetric reward that penalises losses according to Kahneman and Tversky’s loss‑aversion coefficient (~2.25). On unseen institutional tick data, ViperQ achieved +163.6% ROI on TSLA (‑27.5% max drawdown, 27,019 trades) and +116.5% ROI on NVDA (‑47.8% max drawdown, 12,892 trades) with zero leverage.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Auction Market Theory (AMT) describes how price discovers value through volume, identifying key levels such as the Volume Point of Control (VPOC), the Value Area, and Low Volume Nodes (LVNs) that signal imbalances. Cumulative Volume Delta (CVD) measures the net difference between buyer‑initiated and seller‑initiated trades, while tape‑velocity captures the speed of order flow, together forming microstructure signals. Prospect theory, developed by Kahneman and Tversky, posits that people weigh losses more heavily than gains (loss aversion), which ViperQ encodes into an asymmetric reward function for reinforcement learning.

<details><summary>References</summary>
<ul>
<li><a href="https://tradeproacademy.com/full-guide-to-auction-market-theory-how-to-trade-successfully/">Full Guide to Auction Market Theory & How to trade SUCCESSFULLY</a></li>
<li><a href="https://tw.tradingview.com/scripts/cumulativevolumedelta/">Cumulativevolumedelta — 指標和策略 - TradingView</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prospect_theory">Prospect theory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#auction market theory`, `#algorithmic trading`, `#prospect theory`, `#market microstructure`

---

<a id="item-14"></a>
## [Receipt-Based Audit Reveals Frontier Agentic QA Fails on Buried Evidence](https://arxiv.org/abs/2609.15319) ⭐️ 8.0/10

In a controlled data-room audit, researchers moved evidence into buried conditions and found that frontier agentic QA models suffered sharp drops in accuracy, increased forced declarations, more tool calls, and higher cost per correct answer, while confidence scores failed to capture the errors. The findings expose a critical gap between benchmark scores and real-world reliability, showing that current leaderboards can be misleading when evidence is hard to find, and they urge a shift toward claim‑level provenance and adversarial verification for safer agentic systems. Accuracy declined, forced declarations and tool calls rose, and cost per correct answer increased; confidence calibration did not fully reflect wrong answers, and fabricated structural claims could be mixed with accurate numeric tables, indicating a need for statement‑level receipts.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Agentic QA employs autonomous AI agents to plan, execute, and maintain tests based on high‑level goals rather than scripted steps, extending traditional quality assurance. Receipt‑based auditing attaches tamper‑evident provenance metadata to AI outputs, enabling traceability of claims to their source evidence. In financial due diligence and defense staff work, where evidence may be buried in lengthy documents, models can pair correct numbers with confident but fabricated explanations, making claim‑level receipts essential for trustworthy AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/what-agentic-qa-software-testing-studio-0kcic">What is Agentic QA</a></li>
<li><a href="https://deepchecks.com/">Deepchecks LLM Evaluation | Evaluate AI Progress with Know Your...</a></li>
<li><a href="https://www.linkedin.com/pulse/truth-layer-why-ai-forces-internet-show-its-receipts-radhakrishnan-pn-3yhac">The Truth Layer: Why AI Forces the Internet to Show Its Receipts</a></li>

</ul>
</details>

**Tags**: `#AI evaluation`, `#agentic QA`, `#benchmarking`, `#AI safety`, `#receipt-based auditing`

---

<a id="item-15"></a>
## [Markovian embedding enables strong 1/2-order simulation for rough Volterra SDEs](https://arxiv.org/abs/2306.02708) ⭐️ 8.0/10

The authors introduce a reversible Markovian embedding that transforms a new class of Volterra-type stochastic differential equations into standard diffusions, and they derive a numerical scheme achieving strong convergence order 1/2 for fractional kernels with Hurst index H<1/2. This result improves upon the typical Euler‑Maruyama rate of H for rough Volterra equations, offering higher accuracy and efficiency for stochastic simulations in fields such as rough volatility modeling and financial mathematics. The embedding uses convolution kernels to map the non‑Markovian Volterra process to a Markovian diffusion; for H∈(0,1/2) the proposed scheme attains strong order 1/2, whereas standard Euler schemes typically achieve only order H.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Volterra-type stochastic differential equations involve integrals with memory kernels, making the solution path‑dependent and non‑Markovian. When the kernel is a fractional power law, the process exhibits rough behavior characterized by the Hurst index H∈(0,1/2). A Markovian embedding rewrites such a system as an auxiliary Markovian diffusion, allowing standard numerical analysis tools to be applied.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2306.02708v4">Efficient simulation of a new class of Volterra-type SDEs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_chain">Markov chain - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/340229697_Asymptotic_analysis_of_a_kernel_estimator_for_stochastic_differential_equations_driven_by_a_mixed_sub-fractional_Brownian_motion">Asymptotic analysis of a kernel estimator for stochastic differential ...</a></li>

</ul>
</details>

**Tags**: `#stochastic differential equations`, `#Volterra equations`, `#numerical simulation`, `#fractional kernels`, `#Markovian embedding`

---

<a id="item-16"></a>
## [PortBench Introduces Correlation-Aware Full-Pipeline Benchmark for LLM Portfolio Management](https://arxiv.org/abs/2605.27887) ⭐️ 8.0/10

PortBench provides a multi-asset benchmark covering six heterogeneous asset classes from 2015 to 2025, comprising a static QA dataset of 6,269 questions and a dynamic five-stage allocation pipeline. It introduces a dual-layer correlation score and the CEPS metric to evaluate LLMs under three stress windows and three risk profiles, with real-time evaluation to reduce pretraining contamination. By filling the gaps of equity-only focus and incomplete pipeline evaluation, PortBench enables a more realistic assessment of LLMs for portfolio management, guiding researchers and practitioners toward models that truly perform well under diverse market conditions. The benchmark spans six asset classes, includes a static QA set and a dynamic pipeline, uses a dual-layer correlation score for inter‑class hedging and intra‑class concentration, and CEPS to measure error propagation across pipeline stages; evaluations show only 32.5% of 120 LLM tests beat equal‑weight Sharpe across four market periods, and code is publicly available.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: Large language models have been applied to various financial tasks, but portfolio management lacks a comprehensive benchmark. Existing tests often focus solely on equities, ignore cross‑asset correlations, and evaluate only isolated components such as QA rather than the full decision pipeline. PortBench addresses these shortcomings by providing a correlation‑aware, end‑to‑end evaluation framework.

<details><summary>References</summary>
<ul>
<li><a href="https://portbench.github.io/">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>
<li><a href="https://arxiv.org/html/2605.27887">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#portfolio management`, `#benchmark`, `#finance`, `#AI`

---

<a id="item-17"></a>
## [CLQT: Closed-Loop Cost-Aware Benchmark for LLM Portfolio Agents](https://arxiv.org/abs/2606.29771) ⭐️ 8.0/10

CLQT introduces a closed-loop, cost-aware benchmark that enforces point-in-time data via a TimeGate, models institutional transaction and financing costs, scores strategy consistency across rounds, and records each decision cycle in a recompute-verifiable audit chain. It was validated on a year-long multi-model backtest and a four-week live broker paper-trading track on post-cutoff data. By shifting evaluation from simple return ranking to process diagnosis, CLQT reveals whether agents’ decisions are coherent and disciplined, exposing look-ahead bias and cost effects that traditional leaderboards hide. This provides a reusable audit framework that advances credible assessment of LLM-based financial agents. CLQT computes a five‑axis capability scorecard (Coherence, Acuity, Composure, Discipline, Reliability), with Coherence partly judged by a held‑out LLM to reduce self‑preference bias. Ablation studies show a stable stating‑versus‑doing gap (+0.30 backtest, +0.23 live) and, net of realistic costs, agents fail to clearly outperform the market index.

rss · arXiv Quantitative Finance · Sep 15, 04:00

**Background**: LLM agents are increasingly proposed as autonomous portfolio managers, yet most evaluations rely on leaderboard returns over a fixed window, which conflates skill with market path and ignores look‑ahead bias and transaction costs. A closed‑loop benchmark forces the agent to operate within a simulated trading loop where data access is gated in time, costs are modeled, and every action is recorded for later verification. The TimeGate mechanism ensures point‑in‑time data availability, while a hash‑chain‑based audit chain provides tamper‑evident, recomputable records of the gather‑analyze‑decide‑execute‑reflect cycle.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.29771">[2606.29771] CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent ...</a></li>
<li><a href="https://www.mdpi.com/2079-9292/15/1/56">AuditableLLM: A Hash-Chain-Backed, Compliance-Aware ... - MDPI</a></li>
<li><a href="https://www.themoonlight.io/en/review/timegate-sustainable-time-boxed-promotion-gates-for-continual-ml-adaptation-under-resource-constraints">[Literature Review] TIMEGATE: Sustainable Time-Boxed ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#portfolio management`, `#benchmarking`, `#financial AI`, `#evaluation methodology`

---