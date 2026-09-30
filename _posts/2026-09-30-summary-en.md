---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 47 items, 11 important content pieces were selected

---

1. [OpenAI launches GPT-6.1 Sol, near-Astra performance at one‑fifth the price](#item-1) ⭐️ 8.0/10
2. [PS5 Relapse Exploit Enables Jailbreak via WebKit Vulnerability](#item-2) ⭐️ 8.0/10
3. [How Delhi cut electricity loss from 50 to 5 percent.](#item-3) ⭐️ 8.0/10
4. [Backblaze Q2 2026 Drive Stats Show Improved Reliability and Longer Useful Life](#item-4) ⭐️ 8.0/10
5. [Show HN: NSL – A WSL-like Experience for Linux](#item-5) ⭐️ 8.0/10
6. [Vermont replacing power plants with home batteries](#item-6) ⭐️ 8.0/10
7. [Simon Willison live blogs OpenAI DevDay 2026 keynote from Fort Mason](#item-7) ⭐️ 8.0/10
8. [Dyson-Schwinger effective-action method applied to rough volatility option pricing.](#item-8) ⭐️ 8.0/10
9. [Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision](#item-9) ⭐️ 8.0/10
10. [Introducing the CZAR Loss for Financial Log-Return Prediction](#item-10) ⭐️ 8.0/10
11. [Multi-Period Martingale Optimal Transport Framework with Neural Acceleration](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI launches GPT-6.1 Sol, near-Astra performance at one‑fifth the price](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 8.0/10

OpenAI introduced GPT-6.1 Sol in September 2026, a multimodal language model with a 1.1M‑token context window priced at $2.00 per million input tokens, $0.100 per million cached input tokens, and $10.00 per million output tokens, delivering performance close to the flagship GPT-6 Astra at roughly one‑fifth the cost. The release intensifies price competition in the AI model market, making high‑capability models more affordable for developers and enterprises while pressuring rivals such as Anthropic and DeepSeek to lower costs or improve value. GPT-6.1 Sol scores higher than Opus on the GDP.pdf benchmark, offers 50 % cheaper cached input pricing than GPT‑6 Sol, and is positioned below the flagship GPT‑6 Astra in the GPT‑6 series; its real‑world performance is still being evaluated.

hackernews · crorella · Sep 29, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49896586)

**Background**: OpenAI’s GPT series has evolved through successive generations, with the GPT‑6 family including variants such as Astra (flagship), Sol, and Opus. Performance is often measured on benchmarks like GDP.pdf, which evaluates professional‑level question answering over complex PDF documents. Pricing competition has become a key differentiator, especially as context windows grow larger and token costs dominate operational expenses.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT - 6 . 1 Sol | OpenAI</a></li>
<li><a href="https://llm-stats.com/models/gpt-6.1-sol">GPT - 6 . 1 Sol Benchmarks, Pricing & Context Window</a></li>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-astra">GPT-6 Astra Models - Intelligence, Performance & Price ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some praised the low cost and preferred cheaper alternatives like DeepSeek, others speculated that Sol 6.1 is a rebranded Astra‑Minor due to prior underwhelming releases, while several criticized earlier GPT‑6 models for unreliability and highlighted the strategic importance of token pricing for industry investors.

**Tags**: `#GPT-6.1`, `#AI language models`, `#pricing`, `#OpenAI`, `#Hacker News discussion`

---

<a id="item-2"></a>
## [PS5 Relapse Exploit Enables Jailbreak via WebKit Vulnerability](https://github.com/ntfargo/Relapse-Exploit) ⭐️ 8.0/10

The Relapse exploit, released on GitHub, chains a WebKit/JavaScriptCore vulnerability with a kernel race condition to jailbreak PS5 firmware versions 7.00 through 13.60, enabling homebrew execution and save backups. This jailbreak restores user ability to back up game saves and run homebrew on a current‑generation console, challenging Sony’s reliance on paid cloud backups and highlighting ongoing browser‑based attack surfaces. The exploit works entirely from the PS5’s built‑in web browser, requires no hardware dump or waiting period, and leverages a use‑after‑free/uninitialized memory bug in JavaScriptCore’s JIT engine combined with a kernel race condition.

hackernews · therepanic · Sep 29, 15:44 · [Discussion](https://news.ycombinator.com/item?id=49895304)

**Background**: A jailbreak allows users to run unsigned code on a console, bypassing manufacturer restrictions. The PS5’s system software includes a WebKit‑based browser for accessing online services, and vulnerabilities in its JavaScriptCore engine can be exploited to gain arbitrary code execution. Firmware versions 7.00‑13.60 remain vulnerable because the underlying WebKit component has not been patched in those releases, enabling the Relapse chain to combine a browser exploit with a kernel race condition for persistent access.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ntfargo/Relapse-Exploit">GitHub - ntfargo/Relapse-Exploit: Exploit chain for PS5 7.00 ...</a></li>
<li><a href="https://elsolitario.org/en/2026/09/29/relapse-repo-claims-ps5-exploit-firmware-7-00-to-13-60/">PS5 Jailbreak: What Is Relapse Exploit and Its Scope</a></li>
<li><a href="https://www.cvedetails.com/vulnerability-list/vendor_id-8331/product_id-14494/Webkit-Javascriptcore.html">Webkit Javascriptcore : Security vulnerabilities, CVEs</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about backing up game saves and running homebrew, with some questioning whether Sony will disable JavaScriptCore’s JIT to mitigate the exploit. Others wished the exploit could enable playing Steam games or awaited a GTA 6 release, highlighting both practical hopes and broader aspirations within the community.

**Tags**: `#PS5`, `#exploit`, `#jailbreak`, `#security`, `#gaming`

---

<a id="item-3"></a>
## [How Delhi cut electricity loss from 50 to 5 percent.](https://spectrum.ieee.org/delhi-electricity-loss) ⭐️ 8.0/10

The article reports that Delhi reduced its electricity transmission and distribution losses from 50% to 5% by upgrading infrastructure, implementing anti‑theft measures, and rolling out smart metering. This dramatic loss reduction serves as a valuable case study for utilities worldwide, showing how technical upgrades and policy enforcement can cut waste, ease load shedding, and improve reliability in fast‑growing energy markets. The rollout included deploying advanced metering infrastructure (AMI) with radio‑frequency canopy, insulating power lines to deter theft (which unintentionally created monkey pathways), and addressing both technical and commercial components of aggregate technical and commercial (AT&C) losses.

hackernews · rbanffy · Sep 29, 12:43 · [Discussion](https://news.ycombinator.com/item?id=49892245)

**Background**: Electricity transmission and distribution losses, often measured as AT&C losses, comprise technical losses from resistance in lines and transformers and commercial losses from theft, billing errors, and non‑payment. In many Indian cities, losses exceeded 40% due to aging infrastructure and widespread electricity theft, leading to frequent load shedding. Smart metering and AMI enable real‑time monitoring, theft detection, and accurate billing, while anti‑theft measures such as insulated conductors reduce illegal hookups. These tools together have been used in Delhi to bring losses down to single‑digit percentages.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S037877962600756X">Smart-meter-based electricity theft detection and inspection ...</a></li>
<li><a href="https://www.fuelsandlubes.com/newswire/landisgyr-tata-power-ddl-partner-to-deploy-smart-metering-infrastructure-in-delhi/">Landis+Gyr & Tata Power-DDL Partner to Deploy Smart Metering ...</a></li>
<li><a href="https://jetir.org/papers/JETIRDJ06008.pdf">Study on aggregate technical</a></li>

</ul>
</details>

**Discussion**: Commenters recalled the frequent load shedding and voltage surges of two decades ago, noted that insulated power lines unintentionally created easy pathways for monkeys to travel between neighborhoods, and suggested expanding solar, battery storage, and vertical photovoltaics to further reduce reliance on the grid. Some also highlighted that electricity theft was committed by both powerful elites and poor residents, underscoring the social dimension of the problem.

**Tags**: `#electricity`, `#infrastructure`, `#infrastructure`, `#smart grid`, `#India`, `#energy loss`

---

<a id="item-4"></a>
## [Backblaze Q2 2026 Drive Stats Show Improved Reliability and Longer Useful Life](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/) ⭐️ 8.0/10

Backblaze released its Q2 2026 hard drive reliability statistics, reporting lower annualized failure rates and a longer median useful life compared to previous years. The data provides storage professionals with up-to-date longitudinal insights for planning drive replacement cycles and evaluating storage investments, reflecting broader industry trends of increasing HDD reliability. The statistics are derived from Backblaze’s Drive Stats dataset, which tracks SMART attributes and calculates annualized failure rates, excluding drives that fail before their first day in production.

hackernews · HieronymusBosch · Sep 29, 13:34 · [Discussion](https://news.ycombinator.com/item?id=49893002)

**Background**: Annualized failure rate (AFR) estimates the yearly probability of a hard drive failure based on observed failures and operating hours. SMART attributes are internal drive metrics that Backblaze monitors to help predict failures and compute reliability statistics. Backblaze publishes quarterly Drive Stats reports that aggregate data from its production storage fleet to provide public reliability metrics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Annualized_failure_rate">Annualized failure rate - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology">Self-Monitoring, Analysis and Reporting Technology - Wikipedia</a></li>
<li><a href="https://www.backblaze.com/blog/backblaze-drive-stats-academic-ai-ml-research/">How the Backblaze Drive Stats Dataset Powers Academic and AI/ML...</a></li>

</ul>
</details>

**Discussion**: Commenters noted the encouraging trend of declining failure rates and increasing useful life over the years, with one user highlighting the shift from ~14% failure at 3‑year intervals to ~5% at 10‑year intervals. Others raised concerns about the report’s UI, personal experiences with premature drive failures, rising prices, and the trade‑off between growing capacities and stagnant transfer speeds, while questioning why Backblaze does not adopt host‑managed SMR for tiered storage.

**Tags**: `#storage`, `#hard drives`, `#reliability`, `#Backblaze`, `#data center`

---

<a id="item-5"></a>
## [Show HN: NSL – A WSL-like Experience for Linux](https://frostyard.github.io/nsl/) ⭐️ 8.0/10

NSL provides a WSL-like development environment on Linux by running a single VM that hosts one or more systemd-nspawn containers for isolated distro instances. It lets developers on immutable or atomic Linux hosts test and develop across multiple distributions without polluting the base system, offering a workflow similar to WSL2 on Windows. NSL uses a single QEMU VM with virtiofs for file sharing and relies on systemd-nspawn containers to provide process and namespace isolation, tested on Snow Linux 13 with systemd 261.2.

hackernews · bketelsen · Sep 29, 14:51 · [Discussion](https://news.ycombinator.com/item?id=49894351)

**Background**: WSL2 is a Microsoft subsystem that runs a lightweight VM with a Linux kernel to provide near-native Linux binary compatibility on Windows. systemd-nspawn is a container manager built into systemd that creates isolated namespaces for processes, filesystems, and IPC, similar to lightweight VMs. Atomic Linux distributions, such as Fedora Silverblue, are designed to be immutable, with updates applied via image-based transactions to keep the base system stable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux">Windows Subsystem for Linux - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/Systemd-nspawn">systemd - nspawn - ArchWiki</a></li>
<li><a href="https://www.zdnet.com/article/atomic-vs-immutable-linux-distro-how-to-decide/">Atomic vs. immutable Linux : Why choose one when these... - ZDNET</a></li>

</ul>
</details>

**Discussion**: Commenters praised NSL for delivering a clean, WSL-like experience that simplifies working with multiple distros, while some questioned the need for a VM when systemd-nspawn alone could suffice on Linux. Others compared it to existing tools like distrobox and toolbx, asking why NSL wasn't built on top of those projects instead of creating another option.

**Tags**: `#WSL`, `#Linux`, `#containers`, `#development-tools`, `#systemd-nspawn`

---

<a id="item-6"></a>
## [Vermont replacing power plants with home batteries](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms) ⭐️ 8.0/10

Vermont utilities are using a network of residential batteries to form a virtual power plant that supplies power during storms, reducing reliance on traditional power plants.

hackernews · devonnull · Sep 29, 18:19 · [Discussion](https://news.ycombinator.com/item?id=49897993)

**Tags**: `#virtual power plant`, `#home battery storage`, `#grid modernization`, `#renewable energy`, `#energy resilience`

---

<a id="item-7"></a>
## [Simon Willison live blogs OpenAI DevDay 2026 keynote from Fort Mason](https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/) ⭐️ 8.0/10

Simon Willison is live blogging the OpenAI DevDay 2026 keynote and event notes from Fort Mason, San Francisco, noting he received a free ticket and a seat in the creator area. The live blog provides real‑time insights into OpenAI’s latest announcements, offering developers and researchers immediate access to technical details that can influence AI product development. Willison mentions that, as in the previous year, he was granted a complimentary ticket and a creator‑area seat, and he will continue to post updates throughout the day.

rss · Simon Willison · Sep 29, 15:55

**Background**: OpenAI DevDay is an annual developer conference hosted by OpenAI where the company unveils new models, tools, and platform updates. The 2026 edition took place on September 29, 2026 at Fort Mason in San Francisco. Simon Willison, a well‑known technical writer and live‑blogger, attended the event with a complimentary ticket and a seat in the creator area, and is providing real‑time notes of the keynote and other sessions.

**Tags**: `#openai`, `#devday`, `#ai`, `#llms`, `#live-blog`

---

<a id="item-8"></a>
## [Dyson-Schwinger effective-action method applied to rough volatility option pricing.](https://arxiv.org/abs/2609.37741) ⭐️ 8.0/10

The paper introduces a non-perturbative Dyson-Schwinger effective-action framework for stochastic-volatility option pricing, using the two-particle-irreducible (2PI) effective action and gap equations to derive self-consistent Gaussian approximations for the joint law of price and volatility. Across models such as exp-OU, SABR, rough Bergomi and rough SABR, the resulting deterministic engines match PDE or quasi-Monte-Carlo references from sub‑basis‑point to tens of basis points accuracy. This work bridges quantum field theory and quantitative finance, offering a non-perturbative tool that can improve calibration and pricing of exotic options while reducing reliance on costly Monte‑Carlo simulations. By treating volatility as an interacting quantum field, the method provides a unified deterministic engine applicable to both Markovian and rough (Volterra) volatility models. The approach works in log‑price, log‑volatility or Lamperti coordinates, approximating the joint law by a self‑consistent Gaussian whose mean and effective diffusion follow from 2PI stationarity conditions, with drift obtained via statistical linearisation. Interactions such as exponential smile‑generating and CEV terms are evaluated exactly through the Gaussian moment‑generating function, and the locality of the dressed inverse propagator distinguishes Markovian models (reducing to ODEs) from rough models where the full two‑time propagator is retained, enabling efficient impulse‑vega curve computation via a single contraction.

rss · arXiv Quantitative Finance · Sep 30, 04:00

**Background**: In quantum field theory, the Dyson-Schwinger equations are the exact equations of motion for Green’s functions, and the two-particle-irreducible (2PI) effective action provides a non‑perturbative framework that resums propagators via a self‑consistent Gaussian approximation. Rough volatility models, such as rough Bergomi, employ Volterra processes driven by fractional Brownian motion to capture the observed rough (low‑Hurst) behavior of asset volatility, where the memory kernel leads to a non‑local in‑time propagator. The paper shows that when the dressed inverse propagator is local in time the gap equation collapses to a few ordinary differential equations (Markovian case), whereas for rough Volterra models the full two‑time propagator must be kept, turning the characteristic function into a Gaussian integral over the log‑variance field. This allows the deterministic engine to be benchmarked against PDE or quasi‑Monte‑Carlo solutions across a range of stochastic‑volatility specifications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/two-particle-irreducible-effective-action">2PI Effective Action in Field Theory - emergentmind.com</a></li>
<li><a href="https://bsic.it/rough-volatility-a-fractional-brownian-motion-approach/">Rough volatility: A Fractional Brownian Motion Approach. – BSIC | Bocconi Students Investment Club</a></li>
<li><a href="https://medium.com/@ibrahimlanre1890/volterra-processes-modelling-market-memory-412283cea6c3">Volterra Processes: Modelling Market Memory | by Ibrahim Lanre Adedimeji | Medium</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#stochastic volatility`, `#rough volatility`, `#Dyson-Schwinger`, `#option pricing`

---

<a id="item-9"></a>
## [Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision](https://arxiv.org/abs/2609.37963) ⭐️ 8.0/10

The paper introduces a markout-based framework that decomposes Uniswap liquidity provider profitability into active and passive components using a LIFO subtraction method and an infinitesimal LP benchmark. Applying this to Uniswap v2, v3, and v4 pools on Ethereum, Arbitrum, and Base shows that passive LP returns can differ significantly from aggregate pool returns. By revealing that adverse selection in AMMs is unevenly distributed among liquidity providers, the study offers actionable insights for LP strategy design, fee‑tier optimization, and more accurate measurement of DEX market quality. This can help protocols and investors better allocate capital and mitigate losses in concentrated liquidity AMMs. The analysis uses two complementary methods: a LIFO subtraction that matches short‑lived mint‑burn positions and assigns swap‑level markouts by liquidity share, and an infinitesimal LP benchmark that estimates the performance of a fully passive, always‑in‑range marginal LP from the AMM price path. Results show passive profitability diverges from aggregate returns, with a wider active‑passive gap on Ethereum than on Layer‑2 chains and better passive performance in higher‑fee pools; the two methods give consistent directional estimates across most pools.

rss · arXiv Quantitative Finance · Sep 30, 04:00

**Background**: Automated market makers (AMMs) enable token trading by pooling assets supplied by liquidity providers (LPs), who earn fees but also face impermanent loss when token prices diverge. In concentrated liquidity AMMs such as Uniswap v3 and v4, LPs can allocate capital to specific price ranges and actively rebalance positions around trades, creating heterogeneous strategies. Traditional pool‑level analysis assumes all LPs are homogeneous, masking differences between active (rebalancing) and passive (static) liquidity provision. A markout measures the change in value of an LP’s position due to price movements, allowing researchers to separate profit from fees (passive) from profit generated by timing trades (active).

<details><summary>References</summary>
<ul>
<li><a href="https://efalken.substack.com/p/markouts-for-lp-profitability">Markouts for LP Profitability - by Eric Falkenstein</a></li>
<li><a href="https://arxiv.org/pdf/2606.23070">Mitigating Adverse Selection in Concentrated Liquidity AMMs ...</a></li>
<li><a href="https://developers.uniswap.org/docs/protocols/v4/guides/managing-liquidity/decrease-liquidity">Decrease Liquidity | Uniswap Developers</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#AMM`, `#liquidity provision`, `#Uniswap`, `#blockchain`

---

<a id="item-10"></a>
## [Introducing the CZAR Loss for Financial Log-Return Prediction](https://arxiv.org/abs/2609.36061) ⭐️ 8.0/10

The paper introduces the CZAR (Composite Zero-Agnostic Return) loss, a piecewise quadratic objective function designed specifically for predicting financial log-returns. It aims to prevent models from collapsing to zero forecasts by incorporating asymmetry that vanishes at zero and penalizing undershoots and wrong-direction predictions. Standard symmetric losses (MSE, MAE) become near‑optimal for the constant zero predictor because financial log‑returns have a conditional mean close to zero, masking genuine directional skill. CZAR lowers the breakeven directional accuracy needed to beat the zero predictor, potentially improving model performance in quantitative finance applications. CZAR is convex in the prediction, has a closed‑form gradient and Hessian suitable for gradient‑boosted libraries, and its four hyperparameters reduce to a single effective choice via correlated defaults. In a LightGBM experiment on intraday BTC log‑returns, CZAR‑trained models reduced the zero‑returns bias and improved directional accuracy on large‑magnitude returns.

rss · arXiv Quantitative Finance · Sep 30, 04:00

**Background**: Financial log‑returns are often modeled with a conditional mean near zero, so symmetric losses such as MSE or MAE make the constant zero forecast a near‑optimal solution during training and evaluation. This creates a “zero‑returns bias” where models shrink toward zero and trivial forecasters can rank highly despite lacking real predictive skill. Under a Gaussian linear model, the breakeven directional accuracy required to beat the zero predictor rises sharply as prediction noise approaches the return standard deviation, making it difficult for noisy models to succeed. CZAR was designed to keep this breakeven accuracy close to the 50% chance level even under heavy‑tailed noise.

<details><summary>References</summary>
<ul>
<li><a href="https://www.allora.network/research/introducing-the-czar-loss-a-tailored-objective-function-for-financial-log-return-predictions">Introducing the CZAR Loss : A Tailored Objective Function for...</a></li>
<li><a href="https://stats.stackexchange.com/questions/442803/have-log-returns-series-almost-always-conditional-mean-zero-i-presume-no">Have log returns series almost always conditional mean zero ...</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/00036846.2024.2393902">Full article: Assessing the accuracy of directional forecasts</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#quantitative finance`, `#loss function`, `#financial modeling`, `#regression`

---

<a id="item-11"></a>
## [Multi-Period Martingale Optimal Transport Framework with Neural Acceleration](https://arxiv.org/abs/2601.05290) ⭐️ 8.0/10

The paper introduces a computational framework for Multi-Period Martingale Optimal Transport (MMOT) that establishes new convergence rates, proposes incremental updates and adaptive sparse grids, and presents a hybrid neural‑projection solver achieving a 1,597× speed‑up while preserving martingale constraints to 10⁻⁶ precision. By drastically reducing solution time from seconds to milliseconds, the method enables real‑time calibration of complex financial models and bridges optimal transport theory with modern machine‑learning techniques, potentially impacting both computational finance and algorithmic optimal transport research. Theoretical results include discrete convergence O(√Δt log(1/Δt)) and linear convergence (1−κ)^{2/3}; algorithmic contributions feature O(M²) incremental updates and adaptive sparse grids; the hybrid solver combines transformer‑based warm‑starting with Newton‑Raphson projection, yielding a pure neural inference time of 2.9 ms versus 4.7 s and martingale constraint violation below 10⁻⁶.

rss · arXiv Quantitative Finance · Sep 30, 04:00

**Background**: Multi-Period Martingale Optimal Transport extends classical optimal transport by requiring that the coupling between marginal distributions at successive times forms a martingale, modeling arbitrage‑free price evolution in financial markets. Solving MMOT typically involves large‑scale linear programs whose complexity grows with the number of time steps and assets, motivating algorithmic advances such as incremental updates and adaptive sparse grids to mitigate the curse of dimensionality. Recent work leverages neural networks—especially transformer‑based warm‑starting—to provide high‑quality initial guesses that accelerate iterative solvers like Newton‑Raphson while preserving feasibility. The paper integrates these ideas into a hybrid neural‑projection solver that achieves substantial speed‑ups without sacrificing the precision required for financial calibration.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.05290v1">Multi-Period Martingale Optimal Transport: Classical Theory ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0307904X25005402">Structural properties of multi-period martingale optimal ...</a></li>
<li><a href="https://www.emergentmind.com/topics/adaptive-graphs-via-quadratic-optimal-transport">Adaptive Graphs via Quadratic OT</a></li>

</ul>
</details>

**Tags**: `#optimal transport`, `#martingale`, `#neural networks`, `#financial modeling`, `#algorithmic acceleration`

---