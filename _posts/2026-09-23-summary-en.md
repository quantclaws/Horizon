---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 62 items, 21 important content pieces were selected

---

1. [vLLM v0.30.0 adds new model support, GPU weight cache, and performance boosts](#item-1) ⭐️ 8.0/10
2. [Claude Opus 5.5](#item-2) ⭐️ 8.0/10
3. [Hackers Claim to Have Stolen Data on All FBI Employees](#item-3) ⭐️ 8.0/10
4. [SAML: A fractal of bad design](#item-4) ⭐️ 8.0/10
5. [Analysis of Claude Opus 5.5's Intelligence, Performance, and Price Across Reasoning Settings](#item-5) ⭐️ 8.0/10
6. [WordPress 7.1.2 patches unauthenticated path traversal leading to conditional RCE.](#item-6) ⭐️ 8.0/10
7. [Pentagon says AI overreliance led to mistaken strike on Iranian school](#item-7) ⭐️ 8.0/10
8. [Apple introduces persistent ads in iOS, sparking user backlash](#item-8) ⭐️ 8.0/10
9. [Claude Opus 5.5 and GPT-6 Sol/Luna Released with Major Price Cuts](#item-9) ⭐️ 8.0/10
10. [Pareto-Improving Pricing: Why 3 Is Better Than 2](#item-10) ⭐️ 8.0/10
11. [Universal Diffusion Model Learns Shared Dynamics of Option Volatility Surfaces](#item-11) ⭐️ 8.0/10
12. [Spread-based temporal hierarchy forecasting boosts day-ahead electricity market profits.](#item-12) ⭐️ 8.0/10
13. [Paired-Ambiguity Framework for Optimal Stopping via Deep Learning Reflected BSDE](#item-13) ⭐️ 8.0/10
14. [Prediction Markets Outperform Public Weather Forecasts for Daily High Temperatures](#item-14) ⭐️ 8.0/10
15. [Post-trained LLMs increase correlated bias and systemic exclusion in hiring.](#item-15) ⭐️ 8.0/10
16. [Social influence reduces AI agents' selection of diverse scientific papers.](#item-16) ⭐️ 8.0/10
17. [Leaky-integrator method tames error accumulation in recursive forecasting.](#item-17) ⭐️ 8.0/10
18. [Time Interpretation Links Expected Utility and Ergodicity Economics](#item-18) ⭐️ 8.0/10
19. [Disproof of Gatheral's Conjecture via Heston Model Integrated Variance](#item-19) ⭐️ 8.0/10
20. [LLM text measures boost recidivism prediction and peer effect estimation.](#item-20) ⭐️ 8.0/10
21. [Agentic AI Pipeline with 44 Specialized Agents for Institutional Asset Management](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.30.0 adds new model support, GPU weight cache, and performance boosts](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM v0.30.0 includes 762 commits from 315 contributors, adding support for models such as DeepSeek-V4.1-Flash and GLM-5.3-Flash, and introduces a persistent per-GPU weight-cache daemon that enables fast engine startup via CUDA IPC. The release also brings numerous performance improvements across Qwen3.8-Flash-Next, Kimi K3, HiSparse, and Model Runner V2. The new weight-cache daemon drastically reduces engine restart times, lowering latency for LLM serving workloads, while expanded model support and quantization improvements broaden vLLM’s applicability to cutting-edge models. These advances strengthen vLLM’s position as a high-performance inference engine for production-scale LLM deployments. Features include MXFP8 quantization of KV caches via FlashMLA V4.1 on SM100, a HiSparse host-resident tier for sparse-MLA decode, Model Runner V2 with dual-batch overlap and full CUDA graphs, and Qwen3.8-Flash-Next optimizations such as separate prefill/decode QSA indexer kernels and FP8 indexer cache. The weight-cache daemon now supports FP4 checkpoints and multi-node tensor parallelism.

github · khluu · Sep 22, 05:20

**Background**: vLLM is a library for fast and efficient LLM inference that leverages GPU kernels, tensor parallelism, and quantization to reduce latency and memory usage. MXFP8 (Microscaling FP8) is an OCP-defined format that groups 32 elements to share a scale, improving accuracy over channel-wise FP8 while keeping an 8-bit footprint. FlashMLA provides optimized multi-head latent attention kernels, and persistent GPU weight-cache daemons keep quantized weights in GPU memory to avoid costly disk reloads on engine restart.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/projects/vllm-omni/en/latest/user_guide/quantization/mxfp8/">MXFP8 W8A8 - vLLM-Omni</a></li>
<li><a href="https://github.com/vllm-project/vllm/pull/56893">[Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record) by zyongye · Pull Request #56893 · vllm-project/vllm</a></li>
<li><a href="https://www.lmsys.org/blog/2026-08-21-sglang-fast-recovery">Fast Engine Recovery: Sub-Second Engine Restart for SGLang via Weight Cache Daemon - LMSYS Org</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#GPU caching`, `#model support`

---

<a id="item-2"></a>
## [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) ⭐️ 8.0/10

Anthropic unveiled Claude Opus 5.5, a updated version of its flagship language model featuring reduced token pricing and improved natural, clear communication.

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**Tags**: `#LLM`, `#Claude Opus`, `#Anthropic`, `#AI model release`, `#pricing`

---

<a id="item-3"></a>
## [Hackers Claim to Have Stolen Data on All FBI Employees](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

Hackers claiming to be from the group ShinyHunters say they have obtained personal data on every FBI employee, according to a post on 404media. Such a breach would expose sensitive information of federal law‑enforcement personnel, posing serious risks to national security and individual privacy. The hackers said they do not plan to extort the FBI financially, describing their motive as coercion rather than money, and threatened to release the data unless certain demands are met.

hackernews · spenvo · Sep 22, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49805278)

**Discussion**: Commenters expressed skepticism about the ability to secure large databases, referencing the 2015 OPM breach that exposed 22.1 million records. Some used dark humor, noting that only a completely isolated system could be truly safe, while others jokingly suggested absurd counter‑measures like forcing FBI agents to dance in public. Overall sentiment reflects a belief that major data breaches are inevitable and that current defenses are inadequate.

**Tags**: `#cybersecurity`, `#data breach`, `#FBI`, `#hacking`, `#government security`

---

<a id="item-4"></a>
## [SAML: A fractal of bad design](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/) ⭐️ 8.0/10

On September 21, 2026, Trail of Bits published a blog post titled “SAML: A fractal of bad design” that outlines numerous security flaws in SAML and sparked a detailed discussion comparing it to OpenID Connect (OIDC). The critique underscores that many enterprises still depend on SAML for single sign‑on, so understanding its weaknesses is crucial for improving authentication security and guiding protocol selection. The article highlights specific vulnerabilities such as XML signature validation that can be tricked via HMAC with attacker‑controlled passwords and acceptance of Web PKI signatures, allowing attackers to sign SAML documents with their own TLS keys. It also notes SAML’s XML‑heavy design leads to complex parsing attacks, while OIDC avoids many of these issues but still suffers from JWT algorithm confusion and missing audience checks.

hackernews · aray07 · Sep 22, 18:57 · [Discussion](https://news.ycombinator.com/item?id=49806335)

**Background**: SAML (Security Assertion Markup Language) is an XML‑based open standard for exchanging authentication and authorization data between an identity provider and a service provider, widely used for enterprise single sign‑on. OIDC (OpenID Connect) is an authentication layer built on top of OAuth 2.0 that uses JSON Web Tokens (JWT) to convey identity information. Unlike SAML, OIDC relies on JSON and RESTful flows, which reduces parsing complexity but introduces different security considerations such as JWT validation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SAML">SAML - Wikipedia</a></li>
<li><a href="https://auth0.com/intro-to-iam/saml-vs-openid-connect-oidc">What is OpenID vs SAML? Find out the Differences | Auth0</a></li>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/saml-vs-oidc-decision-guide">SAML versus OpenID Connect: Choose the right SSO protocol</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed that SAML’s XML complexity creates serious security pitfalls, citing examples like HMAC‑based signature bypass and Web PKI misuse. Some noted that SAML still offers useful enterprise features such as IdP‑initiated flow that OIDC lacks, while others warned that OIDC also has flaws like JWT algorithm confusion and missing audience checks, concluding that many organizations will need to support both protocols for the foreseeable future.

**Tags**: `#SAML`, `#authentication`, `#security`, `#OIDC`, `#web standards`

---

<a id="item-5"></a>
## [Analysis of Claude Opus 5.5's Intelligence, Performance, and Price Across Reasoning Settings](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

A Hacker News post highlighted an analysis of Claude Opus 5.5's intelligence, performance, and pricing across its max, xhigh, and medium reasoning settings, sparking discussion about cost‑effectiveness and possible performance regression. The analysis helps developers evaluate whether Claude Opus 5.5 offers better value than prior Opus versions and competing models, influencing model selection for cost‑sensitive AI applications. The max setting uses a 128,000‑token completion limit and can exhaust the token budget on complex prompts, while the high‑effort setting reportedly halves the cost per task compared to Opus 5; users also report stability improvements in Opus 4.8 over Opus 5.5.

hackernews · theanonymousone · Sep 22, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49804316)

**Background**: Claude Opus 5.5 is Anthropic’s latest flagship large language model, featuring a 1,000,000‑token context window and support for up to 128,000 completion tokens. It is offered with multiple reasoning settings—max, xhigh, and medium—that adjust the amount of compute allocated to inference, influencing both performance and cost. The model is positioned for agentic coding, computer use, and knowledge‑work tasks, with pricing that varies by provider and can be reduced through caching and discounts.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 (max with fallback) - Intelligence... | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the max reasoning setting can run out of its 128,000‑token budget on complex prompts, while others highlighted that the high‑effort setting halves the cost per task compared to Opus 5. Some users reported performance regressions and preferred the older Opus 4.8 for its stability, and a few questioned the phrasing of ‘somewhat expensive when comparing to other models of similar price.’

**Tags**: `#Claude Opus 5.5`, `#LLM evaluation`, `#AI pricing`, `#reasoning settings`, `#model performance`

---

<a id="item-6"></a>
## [WordPress 7.1.2 patches unauthenticated path traversal leading to conditional RCE.](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 8.0/10

WordPress versions prior to 7.1.2 contain an unauthenticated path traversal vulnerability that can allow remote code execution under certain conditions; the flaw was fixed in version 7.1.2 and the patch has been backported to all supported branches back to 4.7. Because WordPress powers a large fraction of websites, an unauthenticated path traversal that can lead to RCE poses a widespread risk, potentially allowing attackers to compromise millions of sites if exploited. The prompt patching and backporting show the project's commitment to securing legacy installations. The vulnerability resides in the template file selection logic where user‑supplied input is not checked for '../' sequences, allowing inclusion of arbitrary local PHP files. Exploitation typically requires the ability to write a file to a predictable location or to chain the flaw with another vulnerability to achieve remote code execution.

hackernews · vntok · Sep 22, 16:33 · [Discussion](https://news.ycombinator.com/item?id=49803959)

**Background**: WordPress is a widely used open‑source content management system that powers millions of websites. A path traversal flaw lets an attacker navigate outside the intended directory structure to read or include files that should be inaccessible. When the included file contains executable PHP code, an attacker can achieve remote code execution, though this often depends on additional conditions such as write access or a secondary vulnerability. The disclosed flaw affects versions before 7.1.2 and was patched in the 7.1.2 release, with backports to older branches.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-9145/">CVE-2026-9145: WordPress Plugin Path Traversal Vulnerability</a></li>
<li><a href="https://hadrian.io/vulnerability-alerts/cve-2026-87902-working-poc-wordpress-critical-path-traversal">CVE-2026-87902: A Working PoC for WordPress's Critical Path Traversal</a></li>
<li><a href="https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html">WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers</a></li>

</ul>
</details>

**Discussion**: Commenters observe that WordPress’s popularity makes it a frequent target for automated attacks, with some noting they have moved to static site generators to avoid such risks. Others appreciate the timely patch and its backport to older branches, while an old documentation comment is cited as accurately describing the flaw years ago.

**Tags**: `#WordPress`, `#security vulnerability`, `#path traversal`, `#RCE`, `#patch`

---

<a id="item-7"></a>
## [Pentagon says AI overreliance led to mistaken strike on Iranian school](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 8.0/10

A Pentagon report concluded that excessive reliance on AI for target selection contributed to a mistaken missile strike on an Iranian school, citing failure to verify the target and reckless disregard for civilian risk. The finding underscores serious ethical, legal and technical risks of deploying AI in warfare, highlighting the need for stronger human oversight and accountability in automated target selection. The report noted that the Minab site was incorrectly labeled as an Islamic Revolutionary Guard Corps facility due to outdated data, fed into the Maven AI system which reduced target‑selection work from hours to minutes, and that the strike was carried out despite awareness of a substantial risk to civilians.

hackernews · devonnull · Sep 22, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49806430)

**Background**: Maven is a U.S. military AI‑driven target‑selection platform designed to accelerate the identification of potential threats. Overreliance on such automation has been debated because it can speed up decisions while increasing the chance of errors when data are flawed or context is missed. Previous incidents have shown AI misidentifying civilian objects as military targets, raising concerns about accountability in autonomous warfare.

**Discussion**: Commenters debated whether AI was the main cause, with some arguing the real problem was outdated data and the pressure to speed up targeting, while others stressed the need for accountability and protection for first responders. Several noted related near‑miss incidents, such as the AI‑misidentified Chinese boat, highlighting broader risks of automated warfare.

**Tags**: `#AI ethics`, `#military AI`, `#autonomous weapons`, `#target identification`, `#Pentagon report`

---

<a id="item-8"></a>
## [Apple introduces persistent ads in iOS, sparking user backlash](https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy) ⭐️ 8.0/10

Apple has begun showing persistent promotional ads at the top of the iPhone display in iOS, promoting services such as iCloud+ storage, Apple Music/Apple TV trials, and AppleCare+. The move signals a shift in Apple's traditionally ad‑free user experience, potentially eroding trust and affecting how users perceive the platform's value. The ads appear as banners near the top of the screen and can only be removed by waiting for the promotion to expire (weeks or months) or by subscribing to the advertised service.

hackernews · MC995 · Sep 22, 14:30 · [Discussion](https://news.ycombinator.com/item?id=49801939)

**Background**: iOS is Apple's mobile operating system for iPhone and iPad, known for its clean interface and limited third‑party advertising.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techradar.com/phones/iphone/i-wish-apple-would-just-stop-that-crap-apple-has-added-persistent-ads-to-ios-and-its-driving-users-crazy">‘I wish Apple would just stop that crap': Apple has added persistent ‘ads’ to iOS, and it’s driving users crazy | TechRadar</a></li>
<li><a href="https://mjtsai.com/blog/2026/09/22/persistent-ads-in-ios-settings/">Michael Tsai - Blog - Persistent Ads in iOS Settings</a></li>

</ul>
</details>

**Discussion**: Commenters express frustration that the ads degrade the premium iOS experience, with some abandoning Apple Maps for Google Maps due to intrusive promotions.

**Tags**: `#iOS`, `#advertising`, `#user experience`, `#Apple`, `#mobile OS`

---

<a id="item-9"></a>
## [Claude Opus 5.5 and GPT-6 Sol/Luna Released with Major Price Cuts](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

On September 22, 2026, Anthropic unveiled Claude Opus 5.5, and shortly afterward OpenAI launched GPT-6 Sol and GPT-6 Luna, introducing new API pricing where Luna and Sol are half the cost of their GPT-5.6 predecessors. The simultaneous releases and steep price reductions intensify the LLM price war, making high‑performance models more affordable for developers and enterprises and signaling a shift toward cost‑efficient AI services. GPT-6 Luna costs $0.10 per million input tokens, $0.01/M for cached input, and $0.50/M output; GPT-6 Sol is $2/M input, $0.20/M cached, $10/M output; Claude Opus 5.5 is $4/M input, $0.20/M cached, $20/M output. GPT-5.6 models are slated for a 25% price increase in November, so the GPT-6 prices are half of the promotional GPT-5.6 rates.

rss · Simon Willison · Sep 22, 23:46

**Background**: Large language model (LLM) providers typically price API usage per million tokens, with separate rates for input, cached input, and output. Claude Opus and the GPT series are flagship model families from Anthropic and OpenAI, respectively, where newer versions aim to improve performance while reducing cost. Price cuts often reflect competition, advances in inference efficiency, and efforts to attract enterprise workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT-6 Sol and Luna | OpenAI</a></li>
<li><a href="https://kingy.ai/blog/gpt-6-sol-luna-specs-benchmarks-pricing-comparison/">GPT-6 Sol and GPT-6 Luna: Specs, Benchmarks, Pricing and How They Compare to Claude Opus 5.5, Fable 5.1 and Gemini - Kingy AI</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Claude Opus`, `#GPT-6`, `#AI pricing`, `#model releases`

---

<a id="item-10"></a>
## [Pareto-Improving Pricing: Why 3 Is Better Than 2](https://arxiv.org/abs/2609.22652) ⭐️ 8.0/10

The study demonstrates that a three-tier priority pricing scheme can achieve a Pareto improvement over equal allocation by offering a high-quality tier for a fee, a low-quality tier with compensation, and a middle tier at the benchmark quality, whereas any two-tier scheme cannot. This result offers a practical mechanism design tool that can make all agents better off, addressing long-standing equity-efficiency tensions in services like road pricing and public goods. The proof shows that with three tiers—high quality for payment, low quality with subsidy, and middle quality at the baseline—every agent can be strictly better off, while any two-tier configuration leaves at least one agent worse off.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: A Pareto improvement occurs when at least one individual gains without anyone losing, highlighting situations where resources can be reallocated for mutual benefit. Priority pricing systems assign different service qualities (or prices) to agents based on their willingness to pay, often creating a tradeoff between equity (equal access) and efficiency (higher quality for those who pay). The paper studies environments where improving quality for some reduces the average quality that can be provided, a setting that captures congestion, waiting lines, or insurance under adverse selection.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.22652">Pareto-Improving Pricing: Why 3 Is Better Than 2 - arXiv.org</a></li>
<li><a href="https://ziyangkang.com/files/PIP.pdf">Pareto-ImprovingPricing:Why3IsBetterThan2</a></li>
<li><a href="https://www.investopedia.com/terms/p/paretoimprovement.asp">investopedia.com/terms/p/paretoimprovement.asp</a></li>

</ul>
</details>

**Tags**: `#pricing theory`, `#mechanism design`, `#Pareto improvement`, `#tiered pricing`, `#economics`

---

<a id="item-11"></a>
## [Universal Diffusion Model Learns Shared Dynamics of Option Volatility Surfaces](https://arxiv.org/abs/2609.22893) ⭐️ 8.0/10

The authors introduce a universal conditional diffusion model that jointly generates next‑day implied volatility surface (IVS) increments and the underlying stock’s returns, trained on data from 50 stocks and tested on 50 in‑sample and 50 out‑of‑sample stocks. By demonstrating that the learned dynamics generalize to unseen stocks, the model offers a more reliable tool for option pricing, hedging, and risk management, surpassing the prior VolGAN benchmark in arbitrage reduction and risk prediction. The training objective minimizes MSE, optionally adding smoothness and static‑arbitrage penalties; performance is measured by arbitrage violations, stock risk prediction accuracy, and explained variance ratios of the first three principal components.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: The implied volatility surface (IVS) captures how option implied volatility varies with strike price and maturity, and its dynamics are essential for accurate option pricing and hedging. Prior generative approaches, such as VolGAN, used GANs to model IVS movements but often struggled with generalization across different stocks. Diffusion models, which iteratively denoise noisy data to learn complex distributions, provide a promising alternative for learning shared temporal patterns in high‑dimensional financial data.

**Tags**: `#diffusion models`, `#implied volatility`, `#option pricing`, `#financial machine learning`, `#generative modeling`

---

<a id="item-12"></a>
## [Spread-based temporal hierarchy forecasting boosts day-ahead electricity market profits.](https://arxiv.org/abs/2609.23223) ⭐️ 8.0/10

The study shows that jointly forecasting hourly electricity prices and intraday price spreads using a temporal hierarchy forecasting (THieF) framework improves forecast accuracy and trading profits in European day-ahead markets. Using five years of out‑of‑sample data from Germany and Spain, accuracy rose up to 19.7% and profits up to 10.4% compared with unreconciled hourly price forecasts, across three forecasting architectures and even with a pretrained TabPFN foundation model. The results demonstrate that exploiting coherent relationships between economically relevant forecasting targets can enhance both predictive accuracy and decision‑making value, showing that better statistical forecasts do not automatically translate into better economic outcomes. This insight is valuable for energy traders, battery arbitrage strategies, and forecasting research focused on market‑oriented evaluation. The THieF framework reconciles forecasts of hourly prices and all possible intraday spreads, enforcing coherence across temporal aggregations. Gains persisted across three different model architectures (e.g., statistical, machine learning, and deep learning) and remained significant when the base forecasts were generated by a pretrained TabPFN foundation model, indicating robustness of the approach.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Temporal hierarchy forecasting (THieF) builds forecasts at multiple temporal frequencies (e.g., hourly, daily, weekly) and reconciles them to ensure coherence, a technique originally developed for general time series. Forecast reconciliation adjusts individual forecasts so that they aggregate consistently, which has been shown to improve accuracy in various domains, including energy markets. TabPFN is a transformer‑based foundation model for tabular data that uses in‑context learning to deliver strong performance with minimal training, making it suitable as a high‑quality baseline for electricity price prediction.

<details><summary>References</summary>
<ul>
<li><a href="https://cran.r-project.org/web/packages/thief/thief.pdf">thief : Temporal Hierarchical Forecasting</a></li>
<li><a href="https://business-science.github.io/modeltime/reference/temporal_hierarchy.html">General Interface for Temporal Hierarchical Forecasting ( THIEF )...</a></li>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular...</a></li>

</ul>
</details>

**Tags**: `#electricity price forecasting`, `#temporal hierarchy`, `#day-ahead markets`, `#battery arbitrage`, `#forecast reconciliation`

---

<a id="item-13"></a>
## [Paired-Ambiguity Framework for Optimal Stopping via Deep Learning Reflected BSDE](https://arxiv.org/abs/2609.23768) ⭐️ 8.0/10

The paper introduces a paired-ambiguity framework for optimal stopping under dynamic risk measures, characterizing the stopping value by an upper reflected backward stochastic differential equation (BSDE). It then develops a deep learning scheme to solve reflected quadratic BSDEs and demonstrates the method on American option pricing. The work provides structural properties of the stopping operator, explicit solutions in benchmark cases, and a convergent deep learning algorithm, bridging financial mathematics and machine learning for risk-sensitive optimal stopping problems. It combines Girsanov model uncertainty with cash subadditive risk evaluation, studies quadratic drivers from entropic risk measures, and uses discrete reflection and truncation to reduce the quadratic BSDE to a globally Lipschitz system, whose convergence analysis mixes BSDE discretization errors with neural network approximation errors.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Optimal stopping problems involve choosing the best time to take an action to maximize expected reward or minimize cost. Dynamic risk measures extend classical expectations to account for model uncertainty and time‑consistent risk aversion. Backward stochastic differential equations (BSDEs) provide a powerful tool to represent such risk‑adjusted values, and reflected BSDEs incorporate constraints that prevent the solution from falling below a given barrier, which is essential for American‑style options.

**Tags**: `#risk measures`, `#BSDE`, `#deep learning`, `#optimal stopping`, `#financial mathematics`

---

<a id="item-14"></a>
## [Prediction Markets Outperform Public Weather Forecasts for Daily High Temperatures](https://arxiv.org/abs/2609.23969) ⭐️ 8.0/10

Researchers analyzed five years of hourly temperature prediction market data from Kalshi for seven U.S. cities and found that the market-implied forecast beat the National Blend of Models (NBM) in six cities, delivering about 10% lower root‑mean‑square error after the first hour of trading. The result shows that prediction markets can aggregate dispersed information more quickly and accurately than traditional public weather forecasts, offering a potentially valuable complementary tool for decision‑makers and supporting theories of wisdom‑of‑crowds. The study extracted hourly market‑implied forecasts from Kalshi contracts, compared them to NBM forecasts, and found the market’s information moves four times farther toward the NBM than vice versa; the market does not react to NBM updates, while NBM slowly incorporates information already present in the market.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Prediction markets like Kalshi allow users to trade contracts on future events, with prices reflecting collective beliefs about outcomes. The National Blend of Models (NBM) is a NOAA‑produced forecast that blends multiple weather model outputs to provide a consistent, accurate starting point for gridded forecasts. Forecast accuracy is commonly measured using root‑mean‑square error (RMSE), which quantifies the average magnitude of prediction errors.

<details><summary>References</summary>
<ul>
<li><a href="https://kalshi.com/hub/weather">Weather Forecast Markets | Kalshi</a></li>
<li><a href="https://blend.mdl.nws.noaa.gov/nbm-dashboard">NBM Dashboard - National Oceanic and Atmospheric Administration</a></li>
<li><a href="https://en.wikipedia.org/wiki/Root_mean_square_deviation">Root mean square deviation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#weather forecasting`, `#forecast evaluation`, `#information aggregation`, `#Kalshi exchange`

---

<a id="item-15"></a>
## [Post-trained LLMs increase correlated bias and systemic exclusion in hiring.](https://arxiv.org/abs/2609.22169) ⭐️ 8.0/10

The study finds that post-trained LLMs are 3.6% less likely to callback older applicants and that increased model correlation raises global systemic exclusion from 5.6% to 17.3%. This shows that using LLMs for hiring can amplify bias, leading to unfair exclusion of older workers and intersectional groups, highlighting the need for bias mitigation in AI hiring tools. Across ten LLMs, post‑training reduced the callback rate for older applicants by 3.6%, increased decision correlation among models, and raised overall systemic exclusion from 5.6% to 17.3%, with intersectional exclusion reaching up to 21.7%.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Large language models are increasingly deployed by employers to automate resume screening and interview assessment. Base models are pretrained on broad corpora, while post‑training fine‑tunes them on hiring‑specific data to improve performance. When many post‑trained models are trained on similar data, their decisions become highly correlated, creating monocultural bias that homogenizes exclusion across the labor market and raises systemic discrimination risks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.22169v1">Monocultural Biases: Correlated biases in large language ...</a></li>
<li><a href="https://aichanging.work/zh/blog/monocultural-bias-llm-hiring-systemic-exclusion-2026">AI Hiring Monoculture: Exclusion Triples to 17.3% | AI ...</a></li>
<li><a href="https://arxiv.org/html/2506.07962v1">Correlated Errors in Large Language Models - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#LLM bias`, `#hiring automation`, `#AI ethics`, `#monocultural bias`, `#systemic discrimination`

---

<a id="item-16"></a>
## [Social influence reduces AI agents' selection of diverse scientific papers.](https://arxiv.org/abs/2609.22408) ⭐️ 8.0/10

In an experiment with 1,000 AI agents choosing from 114 economics papers, those in social‑influence communities selected 17.2% fewer papers per agent, focused their choices more narrowly, and collectively covered only 73 distinct papers versus 90 in independent communities. A follow‑up test showed that giving papers an initial boost increased their later selection rate by 45.55 percentage points. The findings demonstrate that simple social signals can markedly distort AI‑driven literature attention, raising concerns about bias and homogenization in automated research evaluation systems. Understanding these dynamics helps design AI agents that better reflect diverse scientific importance rather than popularity cascades. The study comprised five independent and five social‑influence groups, each with 100 sequential agents; social groups chose 17.2% fewer papers per agent, showed higher concentration, and covered 73 versus 90 distinct papers, with greater between‑group variation under social information. In a second experiment, 200 agents across twenty social communities received random initial selections for five papers, which raised those papers’ subsequent selection probability by 45.55 points (95% CI: 41.20–49.90); correlations with external citation counts were modest and with download counts were negligible.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: The paper adapts the Music Lab experimental design, which originally studied how social influence shapes music popularity, to a market for academic attention where AI agents select papers based on titles and abstracts. Sequential decision‑making frameworks describe how each agent’s choice can affect later agents when social information is visible. By treating AI agents as participants in an artificial “market,” the study isolates the effect of simple popularity signals on collective attention patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.simplypsychology.org/experimental-designs.html">Experimental Design - Simply Psychology Research Design and Methods | MUsic Technology Online Repository Experimental Design - Types, Methods, Guide - Research Method Chrome Music Lab - Experiments with Google The studio as experimental lab (Chapter 8) - Music Technology Guide to Experimental Design | Overview, Steps, & Examples</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/sequential-decision-problems-in-ai/">Sequential Decision Problems in AI - GeeksforGeeks</a></li>
<li><a href="https://musiclab.chromeexperiments.com/">Chrome Music Lab</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#social influence`, `#scientific attention`, `#experimental economics`, `#research evaluation`

---

<a id="item-17"></a>
## [Leaky-integrator method tames error accumulation in recursive forecasting.](https://arxiv.org/abs/2609.23378) ⭐️ 8.0/10

The paper introduces leaky-integrator reconstruction, a training‑free technique that moves the integrator pole inside the unit circle (H(z)=1/(1‑γz⁻¹), γ<1) to bound error accumulation in recursive differenced time‑series forecasting. By providing a simple, universal fix that works across neural architectures and datasets, the method reduces forecast error by up to ~50% at long horizons while remaining harmless when no error accumulation exists, making it a safe default for any forecaster. With a fixed γ=0.9 (no retraining, just a two‑line change), mean error gains grow from ~3% at horizon 24 to 51% at horizon 336 across seven diverging architectures and twenty datasets, and the approach is provably inert when the predictor is already stable.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Recursive differenced forecasting predicts one‑step changes and reconstructs the series by cumulative summation, which is mathematically equivalent to a discrete integrator whose pole lies on the unit circle. When a nonlinear model is rolled out recursively, this pole causes error to accumulate and diverge, leading to large forecast errors at long horizons. A leaky integrator replaces the pure integrator by moving the pole inside the unit circle, which damps the accumulation of errors while preserving the ability to reconstruct the signal. This modification can be applied at inference time without retraining the underlying model.

**Tags**: `#time-series forecasting`, `#error accumulation`, `#leaky integrator`, `#recursive differencing`, `#machine learning`

---

<a id="item-18"></a>
## [Time Interpretation Links Expected Utility and Ergodicity Economics](https://arxiv.org/abs/1801.03680) ⭐️ 8.0/10

The paper shows that growth optimality in ergodicity economics corresponds to expected utility theory by identifying the ergodicity transformation as the utility function, extending the approach to a general class of wealth dynamics. This linkage provides a theoretical foundation for selecting utility functions based on underlying wealth dynamics and suggests that risk preferences are shaped by the nature of economic processes, potentially influencing economic modeling and decision theory. The authors extend growth optimality from additive and multiplicative gambles to a broad class of wealth dynamics, showing that the ergodicity transformation plays the role of a utility function and that wealth dynamics strongly determine risk preferences.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Ergodicity economics distinguishes between time averages and expectation values, arguing that agents should maximize the time‑average growth rate of wealth (growth optimality) rather than the expectation of utility. Expected utility theory, the dominant model, assumes agents maximize the expectation of a psychologically transformed wealth outcome. The paper shows that when the ergodicity transformation is taken as the utility function, the two frameworks become equivalent, providing a bridge between the approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ergodicity_economics">Ergodicity economics - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1801.03680">[1801.03680] The time interpretation of expected utility theory The time interpretation of expected utility theory - IDEAS/RePEc Expected Growth Criterion: An Axiomatization - arXiv.org LongEU: Long-Term Expected Utility Analysis Ergodicity Economics in Plain English - Researchers.One</a></li>
<li><a href="https://christophegaron.com/articles/research/understanding-the-time-interpretation-of-expected-utility-theory-in-ergodicity-economics/">Understanding the Time Interpretation of Expected Utility ...</a></li>

</ul>
</details>

**Tags**: `#ergodicity economics`, `#expected utility theory`, `#time averages`, `#wealth dynamics`, `#growth optimality`

---

<a id="item-19"></a>
## [Disproof of Gatheral's Conjecture via Heston Model Integrated Variance](https://arxiv.org/abs/2609.05047) ⭐️ 8.0/10

The author proves that for the Heston model with perfect negative spot--variance correlation, the integrated variance is strictly smaller in convex order than that of its calibrated local-volatility projection, thereby disproving Gatheral's conjecture. This result settles an open question in quantitative finance, showing that local volatility models can overestimate tail risk relative to the Heston model under negative correlation, which affects model calibration and risk management practices. The proof establishes the inequality 𝔼[(I_T^H−K)^+] < 𝔼[(I_T^LV−K)^+] for all T>0 and K>0, which implies strict convex ordering; it relies on the assumption of perfect negative correlation (ρ = −1) between spot and variance processes.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: The Heston model is a stochastic volatility model where variance follows a mean-reverting square‑root process; its local‑volatility projection is the one‑dimensional diffusion that matches the model’s marginal distributions. Convex order compares two random variables by the expectation of convex functions, such as call payoffs (X−K)^+. Gatheral's conjecture posited that the integrated variance of the Heston model is never larger in convex order than that of its local‑volatility projection.

**Tags**: `#quantitative finance`, `#Heston model`, `#local volatility`, `#convex order`, `#Gatheral conjecture`

---

<a id="item-20"></a>
## [LLM text measures boost recidivism prediction and peer effect estimation.](https://arxiv.org/abs/2509.20634) ⭐️ 8.0/10

The authors extracted LLM embeddings and applied zero-shot classification to over 200,000 written exchanges among low‑security prison residents, showing that these text representations improve out‑of‑sample recidivism prediction by up to 30% over baseline models using LASSO and LoRA fine‑tuning. They also introduced a novel instrumental variable estimator for peer effects that handles multivariate outcomes, sparse networks, and multidimensional latent homophily, and combined limited human annotations with LLM zero‑shot vectors in a prediction‑powered peer inference (PPPI) framework to obtain debiased estimates. By linking natural language processing with causal inference and criminology, the work offers a more accurate tool for predicting recidivism and quantifying social influence in correctional settings, which can inform rehabilitation programs and policy decisions. The theoretical guarantees under sparse network conditions extend peer‑effect methodology beyond the dense‑network assumptions that dominate the literature, broadening its applicability to real‑world social networks. The prediction improvement was achieved with LASSO‑regularized logistic regression and LoRA‑adapted LLM fine‑tuning, while the peer‑effect estimator is shown to be √N‑consistent and asymptotically normal under sparsity‑relaxed assumptions. The PPPI approach combines a small set of manually labeled examples with the LLM‑derived zero‑shot vectors to correct bias and produce valid confidence intervals for peer‑effect estimates.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Recidivism prediction aims to forecast whether a released individual will reoffend, traditionally relying on static covariates such as age and criminal history. Peer‑effect estimation seeks to measure how an individual’s behavior is influenced by their peers, but standard methods often assume dense social networks and exogenous network formation. Recent advances in large language models enable the extraction of semantic embeddings and zero‑shot classification from raw text, allowing researchers to turn unstructured prison communications into quantitative behavioral measures.

**Tags**: `#LLM`, `#recidivism prediction`, `#peer effects`, `#instrumental variable`, `#social science`

---

<a id="item-21"></a>
## [Agentic AI Pipeline with 44 Specialized Agents for Institutional Asset Management](https://arxiv.org/abs/2604.02279) ⭐️ 8.0/10

The paper introduces an agentic AI pipeline for strategic asset allocation that employs 44 specialized agents to generate capital market assumptions, construct portfolios using 21 competing methods, and critique and vote on each other's outputs. A researcher agent proposes new portfolio construction methods, while a meta-agent learns from past forecasts to rewrite agent code and prompts, all under the governance of an Investment Policy Statement. This architecture represents a significant interdisciplinary advance by automating complex asset allocation tasks that traditionally require expert human analysts. By enabling self‑improvement through a meta‑agent and constraining behavior with Investment Policy Statements, it offers a pathway toward more efficient, transparent, and governable AI‑driven investment processes for institutions. The system comprises 44 specialized agents, 21 portfolio construction techniques, a researcher agent for method invention, and a meta‑agent that updates agent code and prompts based on forecast errors. All agents operate under the constraints of an Investment Policy Statement, and the paper notes that empirical validation of the pipeline’s performance is still pending.

rss · arXiv Quantitative Finance · Sep 22, 04:00

**Background**: Agentic AI refers to systems that can pursue goals, use tools, and act with autonomy, moving beyond narrow tool‑like AI such as chatbots. In multi‑agent systems, a meta‑agent (or metareasoning layer) monitors and modifies the behavior of other agents, enabling self‑improvement. An Investment Policy Statement (IPS) is the formal document that outlines an investor’s objectives, risk tolerance, time horizon, and constraints, and here it is used to govern the autonomous agents’ actions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.academia.edu/66102021/Metareasoning_Structures_Problems_and_Modes_for_Multiagent_Systems_A_Survey">(PDF) Metareasoning Structures, Problems, and Modes for Multiagent ...</a></li>
<li><a href="https://enterprisedna.co/resources/guides/financial-advisory-automate-ips-creation/">How to Automate Investment Policy Statement Creation ...</a></li>

</ul>
</details>

**Tags**: `#agentic AI`, `#asset allocation`, `#finance`, `#multi-agent systems`, `#machine learning`

---