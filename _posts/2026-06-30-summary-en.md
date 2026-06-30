---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 33 items, 11 important content pieces were selected

---

1. [vLLM v0.24.0 Released with MiniMax-M3, DeepSeek-V4, AMD ROCm Enhancements](#item-1) ⭐️ 8.0/10
2. [RocketLab Acquires Iridium to Build Vertically Integrated Space Company](#item-2) ⭐️ 8.0/10
3. [Supreme Court Rules Geofence Warrants Need Constitutional Protections](#item-3) ⭐️ 8.0/10
4. [WATaBoy JIT compiles Game Boy CPU to WebAssembly, beating native interpreter](#item-4) ⭐️ 8.0/10
5. [Explaining the Full CUDA Kernel Launch Process from Host to GPU](#item-5) ⭐️ 8.0/10
6. [Exploring the limits of formal verification in software.](#item-6) ⭐️ 8.0/10
7. [Study finds algorithmic landlord concentration drives higher rent growth in minority neighborhoods.](#item-7) ⭐️ 8.0/10
8. [Study finds uneven EV subsidy benefits and welfare losses in China.](#item-8) ⭐️ 8.0/10
9. [Decision Geometry Links Covariance Error to GMVP Regret under Heavy Tails](#item-9) ⭐️ 8.0/10
10. [LLMs Reduce Demand and Supply in Freelance Markets, Intensifying Competition](#item-10) ⭐️ 8.0/10
11. [Study Quantifies $2.04B Daily US Losses from Extreme Geomagnetic Storm](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.24.0 Released with MiniMax-M3, DeepSeek-V4, AMD ROCm Enhancements](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 includes 571 commits from 256 contributors, adding support for the MiniMax-M3 model with BF16/FP8 indexer, MXFP4 quantization, FP8 sparse GQA and extensive AMD/ROCm tuning, plus major optimizations for DeepSeek-V4 such as FlashInfer sparse index cache and prefill chunk‑planning. The release broadens model coverage, improves inference efficiency across multiple hardware platforms, and demonstrates strong community engagement, positioning vLLM as a more versatile and performant LLM serving solution. MiniMax-M3 support includes BF16/FP8 indexer via MSA, MXFP4, FP8 sparse GQA, and ROCm‑specific tweaks such as mxfp8 MoE/linear on gfx950 and FP8 KV‑cache fixes. DeepSeek‑V4 gains a FlashInfer sparse index cache (2–4% TTFT improvement), prefill chunk‑planning (4% end‑to‑end throughput), cluster‑cooperative topK kernel, and native DSA indexer decode on SM100/SM120.

github · khluu · Jun 29, 19:41

**Background**: vLLM is an open‑source library for high‑throughput LLM inference that supports CUDA, AMD ROCm, and other backends. It enables serving of large models with techniques like paged attention, quantization, and model‑specific kernels. Adding new model support and hardware optimizations expands its applicability to emerging models such as MiniMax‑M3 and DeepSeek‑V4.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-m3">MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model - MiniMax Research | MiniMax</a></li>
<li><a href="https://groundy.com/articles/duquant-makes-fp4-quantization-practical-for-llm-inference-what-fine-grained/">DuQuant++ Makes FP 4 Quantization Practical for LLM... | Groundy</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer -ai/ flashinfer : FlashInfer : Kernel Library for LLM...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#MiniMax-M3`, `#DeepSeek-V4`, `#AMD ROCm`

---

<a id="item-2"></a>
## [RocketLab Acquires Iridium to Build Vertically Integrated Space Company](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

RocketLab announced that it has acquired satellite communications operator Iridium, combining its launch services with Iridium’s global low‑Earth‑orbit constellation. The deal creates a major vertically integrated space firm that can guarantee launch demand for its own constellation while gaining Iridium’s profitable satellite‑phone spectrum and revenue stream. Iridium operates 66 active LEO satellites with spares providing L‑band voice and data globally, and its NEXT generation consists of 81 satellites built by Thales Alenia Space.

hackernews · everfrustrated · Jun 29, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48719485)

**Background**: RocketLab is a US-based launch provider known for its Electron rocket and Photon satellite platform, offering frequent small-sat launches. Iridium is a global LEO satellite constellation delivering voice and data services via 66 operational satellites in polar orbit at about 781 km altitude, with inter-satellite Ka-band links enabling seamless coverage. The constellation's L-band spectrum supports satellite phones and IoT connectivity, making it a valuable revenue-generating asset.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Iridium_Communications">Iridium Communications - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the acquisition mirrors SpaceX's use of Starlink to secure steady launch demand, while others warned that cheaper launches could exacerbate space-junk proliferation. Some expressed nostalgia for RocketLab's New Zealand roots and questioned its shift to a US entity, and several highlighted the gain of Iridium's valuable spectrum and profitable satellite-phone business.

**Tags**: `#space`, `#satellite`, `#acquisition`, `#RocketLab`, `#Iridium`

---

<a id="item-3"></a>
## [Supreme Court Rules Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 8.0/10

On June 29, 2026, the U.S. Supreme Court held that law enforcement must obtain constitutional protections before using geofence warrants to access location data held by technology companies such as Google. The decision extends Fourth Amendment protections to a widely used surveillance tool, setting a precedent that could limit mass location data requests and affect privacy practices nationwide. The ruling noted that in the case under review Google supplied law enforcement with three tranches of data, including a list of 19 accounts linked to devices within 150 meters of a bank during a robbery, and cited Riley v. California to justify the need for a warrant.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: Geofence warrants, also called reverse location warrants, allow police to ask tech firms for all mobile devices that were inside a defined geographic area during a specific time period. Previously, courts often treated these requests as less intrusive than traditional searches, but growing concerns over privacy have led to calls for stronger safeguards. The Supreme Court’s decision now requires that such warrants meet the same constitutional standards as other searches, including probable cause and particularity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>
<li><a href="https://grokipedia.com/page/reverse_search_warrant">Reverse search warrant</a></li>
<li><a href="https://mjlst.lib.umn.edu/2025/01/20/caught-in-the-digital-dragnet-the-controversy-over-geofence-warrants-and-privacy-rights/">Caught in the Digital Dragnet: The Controversy Over Geofence ...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the factual details from the opinion, noting how Google’s data was released in tranches and citing the case as an example of modern surveillance capabilities. Some pointed out that even without a phone, individuals can be identified through other data, while others welcomed the Court’s inclusion of sources and stressed that easier surveillance technology warrants stronger judicial oversight.

**Tags**: `#Supreme Court`, `#geofence warrants`, `#privacy law`, `#Fourth Amendment`, `#law enforcement technology`

---

<a id="item-4"></a>
## [WATaBoy JIT compiles Game Boy CPU to WebAssembly, beating native interpreter](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

The author’s WATaBoy project implements a just‑in‑time compiler that translates the Game Boy’s SM83 CPU instructions into WebAssembly modules at runtime, achieving higher frame‑rate performance than a traditional native interpreter. This demonstrates that WebAssembly can serve as a high‑performance target for JIT‑based emulation, opening a path to run complex emulators in browsers and on platforms like iOS where native JIT is restricted. The JIT detects hot instruction blocks, compiles them to optimized WebAssembly, caches the results, and falls back to the interpreter for cold code; it relies on browser JIT tiers (e.g., SpiderMonkey, V8) to further turn Wasm into native machine code.

hackernews · energeticbark · Jun 29, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48720190)

**Background**: The Game Boy uses a custom SM83 processor with a CISC, variable‑length instruction set that must be decoded and executed by an emulator. WebAssembly is a portable binary instruction format designed for near‑native performance in web browsers, where it can be further optimized by the browser’s JIT compiler. A JIT that translates SM83 instructions to Wasm leverages this pipeline, allowing the emulator to benefit from both ahead‑of‑time Wasm compilation and runtime native code generation.

<details><summary>References</summary>
<ul>
<li><a href="https://the-pi-guy.com/blog/justintime_compilation_the_future_of_webassembly_performance/">Just-In-Time Compilation: The Future of WebAssembly Performance</a></li>
<li><a href="https://gbdev.io/pandocs/CPU_Instruction_Set.html">CPU Instruction Set - Pan Docs</a></li>

</ul>
</details>

**Discussion**: Several commenters remarked that a JIT can be easily prototyped with JavaScript’s eval or new Function, and referenced Andrew Kelley’s 2013 NES static recompilation effort as prior work. Others highlighted the iOS JIT restriction loophole through browser JavaScriptCore/WebKit, noted Firefox’s Wasm performance lagging behind Chrome and Safari, and emphasized that WebAssembly’s ~20% overhead is far smaller than an interpreter’s ~1000% overhead.

**Tags**: `#WebAssembly`, `#JIT compilation`, `#Game Boy emulation`, `#performance optimization`, `#systems programming`

---

<a id="item-5"></a>
## [Explaining the Full CUDA Kernel Launch Process from Host to GPU](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/) ⭐️ 8.0/10

The article details the sequence of events when a CUDA kernel is launched, covering CPU-side driver actions, doorbell writes, queue submission, and GPU warp eligibility and execution. Understanding these low-level steps helps developers optimize performance and debug GPU programs more effectively. It also clarifies how CUDA abstracts hardware details compared to lower-level APIs like Vulkan. The walkthrough includes host‑side driver calls, writing to a doorbell register to signal the GPU, submission of a queue‑management descriptor (QMD), and the GPU’s warp scheduler determining which warps are eligible for execution.

hackernews · mezark · Jun 29, 13:11 · [Discussion](https://news.ycombinator.com/item?id=48718863)

**Background**: CUDA is NVIDIA’s parallel computing platform that allows developers to write kernels executed on GPUs. When a kernel is launched, the CPU-side CUDA driver prepares the launch, writes a doorbell to notify the GPU, and submits a QMD that describes the work. The GPU then schedules warps—groups of 32 threads—based on eligibility criteria such as resource availability and dependencies.

**Discussion**: Commenters praised the article for clarifying the CPU‑to‑GPU path, especially the doorbell and QMD steps, and noted its usefulness for learning CUDA. Some highlighted the implicit synchronization in CUDA streams versus Vulkan’s explicit sync, while others speculated about future kernel‑optimization services being overtaken by open‑source tools or acquired by large providers.

**Tags**: `#CUDA`, `#GPU programming`, `#parallel computing`, `#NVIDIA`, `#HPC`

---

<a id="item-6"></a>
## [Exploring the limits of formal verification in software.](https://queue.acm.org/detail.cfm?id=3819084) ⭐️ 8.0/10

The ACM Queue article examines which parts of software can be formally guaranteed, noting that core logic such as invariants and state transitions can be verified while UI, networking, and database interactions typically remain outside the verification boundary. Understanding these limits helps developers apply formal verification where it is most effective and avoid overestimating its reach, guiding better investment in verification efforts for critical components. The article cites an e‑commerce example where refund‑management logic was verified, but emphasizes that effect‑free core logic is airtight while side‑effects like UI calls, network requests, and DB accesses are not covered by the proof.

hackernews · eatonphil · Jun 29, 14:12 · [Discussion](https://news.ycombinator.com/item?id=48719521)

**Background**: Formal verification uses mathematical proofs to show that a system meets a specification, and has been applied successfully to projects like the CompCert C compiler and the seL4 OS kernel. However, proving properties of interactive components such as graphical user interfaces, network protocols, or persistent storage is challenging because they involve external interactions and nondeterminism, which are difficult to model exhaustively.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_verification_and_validation">Software verification and validation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters note that formal verification remains too limited for most application developers, praising its ability to improve core code quality while criticizing its inability to handle UI, networking, and database concerns; some share personal experiences of using verification to produce cleaner code, and others mention the maintenance burden of proofs as code evolves.

**Tags**: `#formal verification`, `#software correctness`, `#ACM Queue`, `#verification limits`, `#guarantees`

---

<a id="item-7"></a>
## [Study finds algorithmic landlord concentration drives higher rent growth in minority neighborhoods.](https://arxiv.org/abs/2606.27525) ⭐️ 8.0/10

The paper uses SEC EDGAR 10-K property filings geocoded to U.S. census tracts to measure corporate landlord concentration and links it to Zillow Observed Rent Index data from 2019‑2023. It finds that doubling REIT concentration is associated with a 2.8‑percentage‑point increase in rent growth, with a significantly larger effect in majority‑minority tracts. The results provide the first tract‑level evidence that algorithmic rent‑setting by concentrated corporate landlords may worsen racial disparities in housing costs, offering direct relevance to the ongoing DOJ antitrust case against RealPage. Policymakers can use these findings to assess whether algorithmic pricing tools need stricter oversight to protect minority communities. The study constructs a novel Algorithmic Housing Burden Index (AHBI) from ACS data to control for pre‑existing rent burden and market tightness, and employs an XGBoost model with SHAP values showing that corporate landlord concentration contributes positively to rent growth in minority tracts and negatively in white tracts. Statistical significance is reported at p = 0.039 for the differential effect between high‑CLC majority‑minority and comparable white tracts.

rss · arXiv Quantitative Finance · Jun 29, 04:00

**Background**: Algorithmic landlord concentration refers to the degree to which a few corporate landlords, often using algorithmic pricing platforms, own or manage rental units within a geographic area. Researchers measured this concentration by extracting property addresses from SEC EDGAR 10‑K filings of major residential REITs and geocoding them to census tracts via the U.S. Census Geocoder. Rent changes were tracked with the Zillow Observed Rent Index (ZORI), which measures asking‑rent trends while controlling for changes in rental‑unit quality. To isolate the effect of concentration, the authors controlled for a newly created Algorithmic Housing Burden Index (AHBI) that combines ACS‑based rent burden and market tightness measures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zillow.com/research/methodology-zori-repeat-rent-27092/">Methodology: Zillow Observed Rent Index (ZORI)</a></li>
<li><a href="https://www.sec.gov/search-filings">SEC .gov | Search Filings</a></li>
<li><a href="https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html">census .gov/programs-surveys/geography/technical-documentation...</a></li>

</ul>
</details>

**Tags**: `#housing economics`, `#algorithmic pricing`, `#racial disparities`, `#antitrust`, `#urban studies`

---

<a id="item-8"></a>
## [Study finds uneven EV subsidy benefits and welfare losses in China.](https://arxiv.org/abs/2606.27924) ⭐️ 8.0/10

The paper models China's EV adoption from 2015 to 2024 using an equilibrium differentiated-products model and finds that each yuan of 2024 EV subsidy generated about 3.38 yuan of private surplus, but this surplus was unevenly distributed. Removing the subsidy would cause per‑capita consumer‑surplus loss five times larger in Tier 1 cities than in the rest of the country, with roughly half of the aggregate welfare loss stemming from Wright’s‑law learning effects and EV‑native firms retaining 16‑27% of their 2024 business versus 11% for traditional state‑owned manufacturers. This study provides a rigorous equilibrium framework to quantify the welfare and reallocation effects of China’s EV industrial policy, highlighting heterogeneous impacts across consumer tiers and firm types. Its findings offer concrete guidance for designing subsidies that maximize social surplus while accounting for learning‑by‑doing and product‑quality improvements. Using a Berry‑Levinsohn‑Pakes (BLP) differentiated‑products model, a Shapley value decomposition attributes the 2015‑2024 EV share rise primarily to product‑quality gains (+45.49%), choice‑set expansion (+14.81%), and battery‑cost decline (+8.20%), while the subsidy block contributes –13.63% due to phased‑down payments. Counterfactual removal of the 2024 subsidy lowers the EV market share by 23‑33%, and Wright’s‑law learning accounts for about half of the total welfare loss from subsidy withdrawal.

rss · arXiv Quantitative Finance · Jun 29, 04:00

**Background**: Between 2015 and 2024, China’s electric‑vehicle sales share grew from roughly 1% to about 45%, driven by rapid technological change and policy support. Wright’s‑law learning posits that each doubling of cumulative output reduces unit costs by 20‑30%, generating indirect welfare effects beyond direct cash transfers. The Shapley value allocates the total outcome among contributing factors such as quality, variety, battery costs, subsidies, residual, and market effects. The Berry‑Levinsohn‑Pakes (BLP) approach estimates demand in differentiated‑product markets by accounting for price endogeneity and heterogeneous consumer preferences.

<details><summary>References</summary>
<ul>
<li><a href="https://galepooley.substack.com/p/musk-is-on-a-learning-curve-for-2000">Musk Is On A Learning Curve For $2,000 Robots</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shapley_value">Shapley value - Wikipedia</a></li>
<li><a href="https://pages.stern.nyu.edu/~wgreene/Econometrics/BLP.pdf">Automobile Prices in Market Equilibrium - New York University</a></li>

</ul>
</details>

**Tags**: `#electric vehicles`, `#China`, `#industrial policy`, `#technology adoption`, `#welfare analysis`

---

<a id="item-9"></a>
## [Decision Geometry Links Covariance Error to GMVP Regret under Heavy Tails](https://arxiv.org/abs/2606.27462) ⭐️ 8.0/10

The paper proves an exact regret identity showing how covariance-estimation error translates into global minimum‑variance portfolio (GMVP) suboptimality, with regret depending only on the error projected onto the portfolio‑weight directions. It then extends this result to heavy‑tailed returns with tail index κ∈(2,4), deriving the implied regret convergence rate from the centred operator‑norm rate. By providing a decision‑focused geometric characterization of covariance estimation, the work shifts evaluation from generic matrix norms to the actual impact on portfolio performance, offering sharper constants and a concentration discount for robust portfolio construction. This bridges robust statistics and financial decision‑making, benefiting practitioners dealing with non‑Gaussian, heavy‑tailed market data. The regret is invariant to a (p‑1)-dimensional subspace of the p²‑dimensional error matrix, with invariance to the covariance‑scale direction as an exact special case; under heavy tails the convergence rate follows the centred operator‑norm rate, yielding a sharper constant but not a faster rate. The theory is validated on a skew‑t / t‑copula simulation design with pre‑registered analysis.

rss · arXiv Quantitative Finance · Jun 29, 04:00

**Background**: The global minimum‑variance portfolio (GMVP) is the portfolio with smallest variance achievable from a given covariance estimate, and its performance depends on how well the estimated covariance captures the directions that actually affect portfolio weights. Traditional evaluation of covariance estimators uses matrix‑norm losses, which do not directly reflect decision‑relevant error. Decision‑focused learning seeks to align estimator accuracy with the specific loss incurred by downstream decisions, such as portfolio regret. Heavy‑tailed returns, characterized by a tail index κ between 2 and 4, exhibit infinite variance or infinite kurtosis, challenging standard Gaussian‑based covariance estimation techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.27462">The Decision Geometry of Covariance Estimation for the Global...</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3768292.3770378">Estimating Covariance for Global Minimum Variance Portfolio ...</a></li>
<li><a href="https://arxiv.org/html/2606.27462v1">The Decision Geometry of Covariance Estimation for the Global ...</a></li>

</ul>
</details>

**Tags**: `#portfolio optimization`, `#covariance estimation`, `#heavy-tailed distributions`, `#decision theory`, `#financial mathematics`

---

<a id="item-10"></a>
## [LLMs Reduce Demand and Supply in Freelance Markets, Intensifying Competition](https://arxiv.org/abs/2308.05201) ⭐️ 8.0/10

Using data from a major online labor platform, the authors found that skills closely aligned with LLM capabilities experience both reduced demand and reduced supply, with the supply decline being smaller, thereby intensifying freelancer competition, especially in programming‑heavy submarkets. The study provides rigorous empirical evidence of LLMs’ simultaneous impact on labor demand and supply, revealing how AI‑driven skill transitions can worsen competition for workers and informing policy responses to AI‑induced labor market shifts. The analysis shows that while both demand and supply fall for LLM‑aligned skills, the smaller reduction in supply raises the applicant‑to‑job ratio, and high‑skilled freelancers disproportionately move into programming tasks, amplifying competition in those niches.

rss · arXiv Quantitative Finance · Jun 29, 04:00

**Background**: Large Language Models are general‑purpose AI systems that can perform or augment many job functions, creating both displacement and new opportunities in labor markets. Online freelance platforms record detailed data on job postings, worker profiles, and hiring outcomes, enabling researchers to measure shifts in demand and supply for specific skill sets. Studies on skill‑transition effects show that AI lowers the barrier to entering certain occupations, prompting workers—especially high‑skill ones—to shift into new tasks, while displacement effects describe the overall contraction of markets where AI substitutes human labor.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.11379v1">Evaluating LLM Behavior in Hiring: Implicit Weights, Fairness Across Groups, and Alignment with Human Preferences</a></li>
<li><a href="https://www.weforum.org/stories/2026/02/ai-improving-wages-job-quality/">How AI skills and experience are transforming the workplace | World Economic Forum</a></li>
<li><a href="https://www.imf.org/en/blogs/articles/2026/01/14/new-skills-and-ai-are-reshaping-the-future-of-work">New Skills and AI Are Reshaping the Future of Work</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Labor Economics`, `#Large Language Models`, `#Online Freelancing`, `#Empirical Study`

---

<a id="item-11"></a>
## [Study Quantifies $2.04B Daily US Losses from Extreme Geomagnetic Storm](https://arxiv.org/abs/2412.18032) ⭐️ 8.0/10

The paper presents a coupled physics‑engineering‑economic model that estimates daily U.S. economic losses of about $2.04 billion from transformer thermal heating during a 250‑year geomagnetic storm, affecting roughly 5.7 million people and 150,000 businesses. By linking space‑weather physics to engineering impacts and macroeconomic losses, the work provides the first nationwide end‑to‑end quantification of extreme space‑weather risk, offering a scalable framework for infrastructure resilience planning and policy. The model yields a 95 % confidence interval of $1.86–2.22 billion per day, considers only transformer thermal heating (a conservative lower bound), and excludes voltage collapse, cascading failures and restoration costs.

rss · arXiv Quantitative Finance · Jun 29, 04:00

**Background**: A geomagnetic storm is a temporary disturbance of Earth's magnetosphere driven by solar wind variations, which can induce geoelectric fields that drive geomagnetically induced currents (GICs) in long conductors such as power‑grid transmission lines. These GICs can cause half‑cycle saturation in power transformers, leading to localized hot‑spot heating and potential equipment damage. Assessing the resulting geoelectric hazards helps utilities identify where to strengthen grid resilience against space‑weather impacts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geomagnetic_storm">Geomagnetic storm - Wikipedia</a></li>
<li><a href="https://pubs.usgs.gov/fs/2024/3036/fs20243036.pdf">The Solar Cycle, Geology, and Geoelectric Hazards for Power Grids</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geomagnetically_induced_current">Geomagnetically induced current - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space weather`, `#geomagnetic storm`, `#risk assessment`, `#power grid vulnerability`, `#socio-economic modeling`

---