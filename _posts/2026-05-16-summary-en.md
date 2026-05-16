---
layout: default
title: "Horizon Summary: 2026-05-16 (EN)"
date: 2026-05-16
lang: en
---

> From 36 items, 15 important content pieces were selected

---

1. [: vLLM v0.21.0 Released with Transformers v4 Deprecation and New Features](#item-1) ⭐️ 8.0/10
2. [: Erlang/OTP 29.0 Released with Security‑by‑Default and New io_ansi Module](#item-2) ⭐️ 8.0/10
3. [: Warning: Companies May Be Suffering from AI Psychosis.](#item-3) ⭐️ 8.0/10
4. [Zulip launches independent nonprofit foundation.](#item-4) ⭐️ 8.0/10
5. [: Google Project Zero reveals zero‑click exploit chain for Pixel 10](#item-5) ⭐️ 8.0/10
6. [: ](#item-6) ⭐️ 8.0/10
7. [The Sigmoids Won't Save You: Flaws in AI Growth Forecasting](#item-7) ⭐️ 8.0/10
8. [: Image-blaster: AI tool creates 3D environments, SFX, and meshes from a single image.](#item-8) ⭐️ 8.0/10
9. [: US DOJ orders Apple, Google to reveal 100k car‑tinkering app users.](#item-9) ⭐️ 8.0/10
10. [OCaml with stack annotations powers satellite payload software in low-Earth orbit](#item-10) ⭐️ 8.0/10
11. [: Jump-HMM-driven Heston model generates synthetic American option prices](#item-11) ⭐️ 8.0/10
12. [: Study Shows Cross‑Chain Bridge Activity Affects DeFi Lending TVL and Revenue](#item-12) ⭐️ 8.0/10
13. [Alignment Training Amplifies Demographic Biases in LLM Hiring Decisions](#item-13) ⭐️ 8.0/10
14. [Study reveals Polymarket order book microstructure using 30B events](#item-14) ⭐️ 8.0/10
15. [: ](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [: vLLM v0.21.0 Released with Transformers v4 Deprecation and New Features](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM version 0.21.0 was released, deprecating transformers v4 support and requiring a C++20-compatible compiler. It adds KV offload with a hybrid memory allocator, speculative decoding that respects thinking budgets, and a new TOKENSPEED_MLA backend for Blackwell GPUs. This release introduces breaking changes that push vLLM toward modern toolchains while delivering performance gains for cutting‑edge hardware and reasoning models. It signals the project’s readiness for next‑generation LLMs and Blackwell‑based inference workloads. Transformers v5 is now required; the build system enforces C++20. KV offloading now uses the Hybrid Memory Allocator with scheduler‑side sliding window groups. Speculative decoding enforces thinking‑token budgets, and the TOKENSPEED_MLA backend provides optimized attention for DeepSeek‑R1/Kimi‑K25 on Blackwell GPUs.

github · khluu · May 15, 08:44

**Background**: vLLM is a high‑throughput LLM inference engine that supports GPU‑accelerated serving via techniques such as KV cache offloading, speculative decoding, and custom attention kernels. The Hybrid Memory Allocator (HMA) groups KV cache layers by type to share memory tensors, reducing fragmentation. NVIDIA Blackwell GPUs introduce new architectures that benefit from specialized backends like TOKENSPEED_MLA, which accelerates matrix‑multiply operations for long‑context models.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/hybrid_kv_cache_manager/">Hybrid KV Cache Manager - vLLM</a></li>
<li><a href="https://fenado.ai/articles/lightseek-foundation-unveils-open-source-tokenspeed-llm-engine-with-vllm-integration-for-nvidia-blackwell">LightSeek Foundation Unveils Open-Source TokenSpeed LLM Engine with vLLM Integration for NVIDIA Blackwell | TokenSpeed, LLM inference engine, Fenado AI</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/39573">[Bug]: Thinking token budget not enforced with MTP ... - GitHub</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#transformers`, `#CUDA`, `#speculative decoding`

---

<a id="item-2"></a>
## [: Erlang/OTP 29.0 Released with Security‑by‑Default and New io_ansi Module](https://www.erlang.org/news/188) ⭐️ 8.0/10

Erlang/OTP 29.0 disables the SSH daemon and SFTP subsystem by default, improving security, and introduces the io_ansi module for emitting ANSI sequences to build richer CLI applications. The release also adds experimental native records, multi‑valued comprehensions, a new is_integer/3 guard BIF, and prefers post‑quantum hybrid key exchange in SSL. The security‑by‑default changes reduce the attack surface for Erlang nodes, making deployments safer out of the box, while io_ansi lowers the barrier for developers to create cross‑node, color‑rich command‑line tools. Together they signal OTP’s ongoing evolution to meet modern security and usability expectations. SSH daemon now defaults to disabled for shell and exec services, and the SFTP subsystem is no longer enabled by default when starting an SSH daemon. The io_ansi module allows emitting Virtual Terminal Sequences (ANSI codes) to terminals for coloring/styling or full‑screen apps. Additional features include experimental native records (EEP‑79), multi‑valued comprehensions (EEP‑78), a new is_integer/3 guard BIF, and the post‑quantum hybrid key exchange x25519mlkem768 preferred in SSL.

hackernews · pyinstallwoes · May 15, 23:33 · [Discussion](https://news.ycombinator.com/item?id=48155297)

**Background**: Erlang/OTP is a set of libraries and design principles used to build highly reliable, fault‑tolerant systems, originally for telecom but now widely used in distributed applications. An SSH daemon allows remote shell and file transfer access, which can be a security risk if left enabled by default. ANSI sequences are escape codes that terminals interpret to change text color, style, or cursor position, enabling rich CLI interfaces.

<details><summary>References</summary>
<ul>
<li><a href="https://www.erlang.org/news/188">Erlang/OTP 29.0 - Erlang/OTP</a></li>
<li><a href="https://github.com/erlang/otp/releases">Releases · erlang/otp</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the security improvements, noting that disabling SSH and SFTP by default is a good practice. They highlighted the io_ansi module as a useful addition for building CLI applications, expressed curiosity about how the new experimental records will be adopted, and asked for deeper explanations of the release’s internals. Overall sentiment is positive with strong interest in both the security changes and the new features.

**Tags**: `#Erlang`, `#OTP`, `#release`, `#security`, `#CLI`

---

<a id="item-3"></a>
## [: Warning: Companies May Be Suffering from AI Psychosis.](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

A Hacker News thread sparked by a tweet from Mitchell H warns that numerous companies are exhibiting 'AI psychosis' by delegating critical thinking and decision‑making to AI systems without sufficient human oversight. This trend is significant because unchecked AI dependence can degrade human judgment, increase systemic errors, and raise ethical concerns across industries, prompting a need for better AI governance and critical‑thinking practices. The phenomenon involves employees deferring to AI‑generated answers without verifying them, which can propagate hallucinations or biased outputs, and may lead to decision‑making that lacks human scrutiny, especially in high‑stakes domains like finance and venture capital.

hackernews · reasonableklout · May 15, 20:26 · [Discussion](https://news.ycombinator.com/item?id=48153379)

**Background**: AI psychosis is an informal term describing worsening psychosis‑like symptoms such as paranoia and delusions that can arise from prolonged interaction with AI chatbots. It is closely related to the practice of outsourcing critical thinking to AI, where users defer to AI‑generated outputs without applying their own judgment, a behavior warned against by experts who note it can erode human competence and increase reliance on potentially flawed AI reasoning. Recent discussions in 2025‑2026 highlight growing concern among technologists and mental‑health professionals about the spread of this pattern in corporate settings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chatbot_psychosis">Chatbot psychosis - Wikipedia</a></li>
<li><a href="https://medium.com/@andy25/ai-psychosis-is-real-its-spreading-and-nobody-is-talking-about-it-ba73859291cf">AI Psychosis Is Real, It’s Spreading, and Nobody Is Talking... | Medium</a></li>
<li><a href="https://www.lesswrong.com/posts/xXYuns8inHD9ogoth/the-dangers-of-outsourcing-thinking-losing-our-critical">The Dangers of Outsourcing Thinking: Losing Our Critical ...</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that blindly trusting AI outputs without critical review constitutes dangerous 'AI psychosis,' while acknowledging that using AI as a tool (e.g., for code generation) can be beneficial; they also warn that excessive faith in AI‑driven automation can lead to unsafe practices and hidden systemic risks, though a few note that cautious, slow adopters might gain a competitive edge.

**Tags**: `#AI`, `#AI safety`, `#decision-making`, `#tech culture`, `#overreliance`

---

<a id="item-4"></a>
## [Zulip launches independent nonprofit foundation.](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

On May 15, 2026, Zulip announced the creation of the Zulip Foundation, an independent nonprofit that will become the formal steward of the Zulip open‑source chat platform. The foundation addresses long‑term sustainability and trust concerns by ensuring the project remains community‑driven and free from commercial pressures that could compromise user data or introduce ads. The foundation will receive the donated company from Zulip’s leadership, including Tim Abbott and three senior members who are stepping back to join Anthropic, and its mission is to develop the best possible team chat experience while serving the public good.

hackernews · boramalper · May 15, 18:37 · [Discussion](https://news.ycombinator.com/item?id=48152168)

**Background**: Zulip is an open‑source team chat application created in 2012 by Jeff Arnold, Waseem Daher, Jessica McKellar, and Tim Abbott. It offers threaded conversations and is positioned as a free alternative to proprietary platforms like Slack. The project has been maintained by its founders and a volunteer community, with recent releases such as Zulip 12.0 announced in April 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zulip">Zulip - Wikipedia</a></li>
<li><a href="https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/">Announcing the Zulip Foundation</a></li>
<li><a href="https://zulip.com/history/">History of the Zulip project</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the foundation for alleviating trust concerns, expressed excitement mixed with sadness over departing core team members, questioned the timing of the announcement, praised Zulip’s interface over Discord, and noted the recent Zulip 12.0 release.

**Tags**: `#zulip`, `#open source`, `#foundation`, `#nonprofit`, `#chat platform`

---

<a id="item-5"></a>
## [: Google Project Zero reveals zero‑click exploit chain for Pixel 10](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 8.0/10

In May 2026, Google Project Zero disclosed a zero‑click exploit chain that targets the upcoming Pixel 10 smartphone, chaining a Dolby decoding bug with a newly discovered VPU driver privilege‑escalation flaw to achieve full kernel control. The exploit shows how AI‑powered features such as on‑device media analysis expand the mobile attack surface, putting Pixel 10 users at risk unless vendors harden AI‑related code paths. The chain begins with a zero‑click Dolby vulnerability that processes incoming video without user interaction, then leverages a Pixel 10‑specific VPU driver bug that exposes chip hardware interfaces to userspace, allowing privilege escalation to root.

hackernews · happyhardcore · May 15, 13:39 · [Discussion](https://news.ycombinator.com/item?id=48148460)

**Background**: Zero‑click exploits require no user interaction; they trigger automatically when a device processes malicious data, such as a video or image. Modern smartphones increasingly use AI‑driven on‑device models to analyze media (e.g., for search or transcription), which means that media must be decoded and interpreted before the user sees it, enlarging the attack surface. The Pixel 10’s new Tensor G5 chip includes a VPU (Video Processing Unit) driver that, in this case, was found to expose low‑level hardware interfaces to unprivileged processes, enabling the privilege‑escalation step of the chain.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0 - click exploit chain for the Pixel 10 : When a Door... - Project Zero</a></li>
<li><a href="https://gbhackers.com/pixel-10-zero-click-exploit-chain/">Google Project Zero Details Pixel 10 Zero - Click Exploit Chain</a></li>
<li><a href="https://logicity.in/en/blog/google-project-zero-finds-0-click-root-exploit-in-pixel-10">Google Project Zero Finds 0 - Click Root Exploit in Pixel 10 | Logicity</a></li>

</ul>
</details>

**Discussion**: Commenters expressed worry that AI‑powered features are increasing zero‑click risks, with one user urging vendors not to process messages without consent. Others noted the unusually fast 90‑day patch for the reported driver bug as a positive sign, while questioning whether exploit disclosures are genuinely rising or just gaining more visibility due to AI hype. Some wondered whether AI will render groups like NSO obsolete or instead make them more powerful.

**Tags**: `#mobile security`, `#zero-click exploit`, `#Pixel 10`, `#Android vulnerability`, `#AI attack surface`

---

<a id="item-6"></a>
## [: ](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 8.0/10

A California bill would mandate that online game publishers either provide patches to keep games playable or offer refunds when they shut down services.

hackernews · Lihh27 · May 15, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48152994)

**Tags**: `#legislation`, `#gaming`, `#consumer protection`, `#online services`, `#policy`

---

<a id="item-7"></a>
## [The Sigmoids Won't Save You: Flaws in AI Growth Forecasting](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you) ⭐️ 8.0/10

The essay argues that relying on sigmoid curve extrapolations to predict continued AI progress is misguided, because technological advances follow S‑curves that eventually plateau. This critique highlights the limits of simple mathematical models for forecasting transformative technologies, urging policymakers and investors to adopt more robust, uncertainty‑aware approaches. The piece draws on historical examples of propeller, turbojet, and ramjet technologies to illustrate S‑curve behavior, discusses the Lindy effect as an alternative heuristic, and notes the author’s own prediction of AGI within one to two years.

hackernews · Tomte · May 15, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48147021)

**Background**: Sigmoid functions are S‑shaped mathematical curves, commonly exemplified by the logistic function, that model processes which start slowly, accelerate, and then level off as they approach a limit. In technology forecasting, sigmoid curves are often used to represent the life cycle of an innovation, capturing early adoption, rapid growth, and eventual saturation. The Lindy effect (Lindy’s law) posits that the future life expectancy of a non‑perishable entity such as a technology is proportional to its current age, suggesting that longer‑lasting technologies are likely to persist longer. Together, these concepts inform debates about whether AI progress will continue indefinitely or eventually plateau.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sigmoid_curve">Sigmoid curve</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lindy's_law">Lindy's law</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the article appears to answer its own question early but then moves on without fully addressing the implication. Several contributors highlighted the usefulness of Lindy’s law as a heuristic for estimating technology longevity, while also stressing that any forecast remains highly uncertain. One user pointed out the author’s personal stake in predicting imminent AGI, suggesting a possible bias in favoring the Lindy perspective over sigmoid extrapolations.

**Tags**: `#AI`, `#technology forecasting`, `#sigmoid curves`, `#Lindy's law`, `#HN discussion`

---

<a id="item-8"></a>
## [: Image-blaster: AI tool creates 3D environments, SFX, and meshes from a single image.](https://github.com/neilsonnn/image-blaster) ⭐️ 8.0/10

Image-blaster is an open‑source project that creates 3D environments, sound effects, and meshes from a single image using AI models like Worldlabs.

hackernews · MattRogish · May 15, 15:42 · [Discussion](https://news.ycombinator.com/item?id=48150069)

**Tags**: `#3D generation`, `#AI`, `#computer vision`, `#generative models`, `#graphics`

---

<a id="item-9"></a>
## [: US DOJ orders Apple, Google to reveal 100k car‑tinkering app users.](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

The U.S. Department of Justice is demanding that Apple and Google reveal the identities of more than 100,000 users of a popular car‑tinkering app used to bypass emissions controls.

hackernews · tencentshill · May 15, 17:28 · [Discussion](https://news.ycombinator.com/item?id=48151383)

**Tags**: `#privacy`, `#government surveillance`, `#automotive emissions`, `#app store`, `#legal`

---

<a id="item-10"></a>
## [OCaml with stack annotations powers satellite payload software in low-Earth orbit](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

The blog post describes how OCaml programs annotated with stack usage (O(x)Caml) were deployed on a satellite payload in low‑Earth orbit, achieving sub‑10‑nanosecond latency and eliminating garbage‑collection pauses. This shows that a garbage‑collected functional language can meet the hard real‑time demands of aerospace, opening the door to safer, more maintainable satellite software. Stack annotations cut heap allocations, reducing the p99.9 latency of the dispatch hot path from 29 ns to 9 ns per packet and removing all minor GCs over 25 million packets; the payload runs as SystemD services over DBus, includes a CCSDS‑to‑DBus bridge and performs symmetric‑key encryption as required by regulations.

hackernews · yminsky · May 15, 10:55 · [Discussion](https://news.ycombinator.com/item?id=48147058)

**Background**: OCaml is a statically typed functional language that includes a generational garbage collector; stack annotations allow programmers to hint that certain data should be allocated on the stack, reducing heap pressure and GC pauses. Low‑Earth orbit (LEO) satellites operate at about 7.8 km/s, offering low latency links and frequent ground‑station passes, making them suitable for real‑time payload processing. Satellite payload software often runs as isolated services communicating via protocols such as CCSDS and DBus, where predictable timing is crucial.

<details><summary>References</summary>
<ul>
<li><a href="https://ocaml.org/docs/garbage-collector">Understanding the Garbage Collector · OCaml Documentation</a></li>
<li><a href="https://ocaml.org/manual/5.2/api/Stack.html">OCaml library : Stack</a></li>
<li><a href="https://en.wikipedia.org/wiki/Low_Earth_orbit">Low Earth orbit - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that OCaml had already flown on GHGSat‑D in 2016, praised the latency improvements from stack annotations, and debated whether reinventing CCSDS‑based encryption is necessary when battle‑tested alternatives like TLS exist. Some questioned the effort required to tame a GC‑enabled language for hard real‑time workloads, while others highlighted the language’s safety benefits.

**Tags**: `#OCaml`, `#systems programming`, `#aerospace`, `#garbage collection`, `#performance optimization`

---

<a id="item-11"></a>
## [: Jump-HMM-driven Heston model generates synthetic American option prices](https://arxiv.org/abs/2605.13998) ⭐️ 8.0/10

The paper introduces a Jump Hidden Markov Model‑driven Heston framework that treats implied volatility as an output of a structural equity‑returns model, enabling the generation of realistic synthetic American option prices. By breaking the circular dependency between implied volatility and option prices, the method provides a reliable source of synthetic data for machine‑learning and risk‑analysis applications in quantitative finance. The framework combines a Jump HMM for multi‑asset price paths, a regime‑dependent Heston variance process, and a recombining binomial lattice to price American options, initializing variance at its mean‑reversion target so that volatility smiles, skews and term structures emerge without external calibration.

rss · arXiv Quantitative Finance · May 15, 04:00

**Background**: A Jump Hidden Markov Model (Jump HMM) captures unobservable market regimes and incorporates sudden jumps, allowing it to reproduce stylized facts such as volatility clustering and fat tails in equity returns. The Heston stochastic volatility model treats variance as a mean‑reverting process, and by making its long‑run level depend on regime, time‑to‑expiry, moneyness and a market‑mood indicator, the model can generate implied‑volatility surfaces that reflect smile, skew and term structure. American options are commonly priced using a recombining binomial lattice (Cox‑Ross‑Rubinstein) that accommodates early exercise through backward induction. Generating synthetic option prices usually requires implied volatility as an input, which creates a circular dependency because implied volatility is itself calibrated from observed option prices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Heston_model">Heston model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice_model_(finance)">Lattice model (finance) - Wikipedia</a></li>
<li><a href="https://www.daytrading.com/hidden-markov-models">Hidden Markov Models in Finance, Markets & Trading</a></li>

</ul>
</details>

**Tags**: `#option pricing`, `#stochastic volatility`, `#hidden Markov model`, `#synthetic data`, `#quantitative finance`

---

<a id="item-12"></a>
## [: Study Shows Cross‑Chain Bridge Activity Affects DeFi Lending TVL and Revenue](https://arxiv.org/abs/2605.12508) ⭐️ 8.0/10

The paper applied panel regression with fixed effects and OLS models to empirically analyze how cross‑chain bridge activity influences TVL and total revenue of 15 DeFi lending protocols across nine EVM‑compatible blockchains from October 2022 to January 2025. By quantifying the heterogeneous effects of bridge volume, hacks, and new network launches, the study provides actionable insights for DeFi risk managers to incorporate cross‑chain metrics and adopt layer‑aware models in an increasingly multi‑chain ecosystem. The dataset covers 15 lending protocols, 53 bridges, and nine EVM chains; bridge hacks show a significant positive relationship with TVL and revenue, while increased bridge integrations correlate with lower TVL and revenue, indicating liquidity outflow; Ethereum attracts large depositors whereas layer‑2s skew toward retail users, and the models achieve high R‑squared values.

rss · arXiv Quantitative Finance · May 15, 04:00

**Background**: DeFi lending protocols allow users to deposit assets and earn interest, with Total Value Locked (TVL) measuring the total dollar value of assets locked in these contracts. Cross‑chain bridges enable the transfer of assets and data between different blockchains, facilitating interoperability but also introducing new risks. Panel regression with fixed effects and ordinary least squares (OLS) is an econometric technique that controls for unobserved heterogeneity across entities and time, making it suitable for analyzing protocol performance across multiple chains and periods.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@V-Blaze/cross-chain-interoperability-bridging-asset-chain-with-other-blockchain-networks-1a3bd628025b">Cross - Chain Interoperability: Bridging Asset Chain with... | Medium</a></li>
<li><a href="https://www.investopedia.com/total-value-locked-7486821">Understanding Total Value Locked (TVL) in Cryptocurrency and DeFi</a></li>
<li><a href="https://www.econometrics-with-r.org/10-rwpd.html">10 Regression with Panel Data | Introduction to Econometrics ...</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#cross-chain`, `#lending protocols`, `#risk modeling`, `#blockchain interoperability`

---

<a id="item-13"></a>
## [Alignment Training Amplifies Demographic Biases in LLM Hiring Decisions](https://arxiv.org/abs/2605.13866) ⭐️ 8.0/10

A study of 27 language models across 177 occupations found that models favor female and Black candidates while disadvantaging disabled candidates, and that post‑training alignment amplifies these biases—boosting advantages for female and Black applicants by ~325‑330% and disadvantages for disabled applicants by ~171%.

rss · arXiv Quantitative Finance · May 15, 04:00

**Tags**: `#AI fairness`, `#language models`, `#hiring bias`, `#AI alignment`, `#ethics`

---

<a id="item-14"></a>
## [Study reveals Polymarket order book microstructure using 30B events](https://arxiv.org/abs/2604.24366) ⭐️ 8.0/10

The paper analyzed Polymarket's public order-book feed, comprising 30 billion tick-level events over 52 days, and joined it to on-chain trade records to report eight stylized facts about the market's microstructure. Understanding Polymarket's microstructure informs the design and regulation of decentralized prediction markets and highlights limitations of inferring trade direction from public feeds alone. Among the findings are a longshot spread premium, a near-uniform depth profile, negligible block-clock alignment, diverse maker wallets with a concentrated tail, category‑dependent effective spreads, sub‑50 ms median feed‑ingestion delay with a multi‑second tail, low wash‑trade share (median 1 %), and trade‑direction inference accuracy of only ~59 % versus ~80 % on Nasdaq.

rss · arXiv Quantitative Finance · May 15, 04:00

**Background**: Polymarket is the world's largest on‑chain prediction market, operating on the Polygon network and leveraging UMA’s Optimistic Oracle to settle bets on real‑world events using stablecoins. Prediction markets allow participants to trade contracts whose payoffs depend on the outcome of future events, aggregating dispersed information into market prices. Market microstructure examines how the detailed rules of a trading venue—such as order‑book structure, matching logic, and latency—affect price discovery, liquidity, and execution quality. Studying these mechanics on‑chain helps assess whether decentralized venues replicate the efficiency of traditional exchanges.

<details><summary>References</summary>
<ul>
<li><a href="https://polymarket.com/">Polymarket | The World's Largest Prediction Market</a></li>
<li><a href="https://lesaker.substack.com/p/on-chain-market-microstructure-amms">On-Chain Market Microstructure: AMMs, Orderbooks, and RFQs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prediction_market">Prediction market - Wikipedia</a></li>

</ul>
</details>

---

<a id="item-15"></a>
## [: ](https://arxiv.org/abs/2410.02091) ⭐️ 8.0/10

The paper shows GitHub Copilot increases open-source code contributions by about 6% through higher developer participation and individual productivity, while also raising coordination time by 8% due to more code discussions.

rss · arXiv Quantitative Finance · May 15, 04:00

**Tags**: `#Generative AI`, `#GitHub Copilot`, `#Open-source software`, `#Developer productivity`, `#Collaborative development`

---