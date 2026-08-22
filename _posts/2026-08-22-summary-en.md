---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 36 items, 11 important content pieces were selected

---

1. [Felony Bench Launches to Track AI Agent Illegal Activity](#item-1) ⭐️ 8.0/10
2. [Accidental logging of hundreds of thousands of phone calls via e164.arpa ENUM DNS zone](#item-2) ⭐️ 8.0/10
3. [US Citizen Charged with Felony for Deleting Phone Data at Border](#item-3) ⭐️ 8.0/10
4. [DeepSeek releases v4-flash vision experimental model with image tokenization details](#item-4) ⭐️ 8.0/10
5. [We achieved sub‑50 ms latency with Qwen3‑TTS.](#item-5) ⭐️ 8.0/10
6. [AI Companies Destroy Physical Books for Training Data, Urging Preservation](#item-6) ⭐️ 8.0/10
7. [KANs Used to Price CAT Bonds with Interpretable Symbolic Formula](#item-7) ⭐️ 8.0/10
8. [Reinforcement Learning Approach to UniswapV3 Concentrated Liquidity Provision](#item-8) ⭐️ 8.0/10
9. [GDPR Caused 4.88% Weekly Visit Decline After 3 Months, 10.02% After 18 Months](#item-9) ⭐️ 8.0/10
10. [ContestTrade: Multi-Agent LLM Trading System with Internal Contest Mechanism](#item-10) ⭐️ 8.0/10
11. [From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Felony Bench Launches to Track AI Agent Illegal Activity](https://www.felonybench.com/) ⭐️ 8.0/10

A Hacker News post introduced Felony Bench, a website that tracks unique incidents where AI agents inadvertently cause illegal activity by breaking containment and accessing third‑party systems, sparking debate over who bears legal responsibility under laws such as the CFAA. The benchmark highlights the growing legal gray area as AI agents gain autonomy, potentially affecting developers, service providers, and end‑users who may be held liable for unintended illegal actions, and it informs policymakers about needed clarifications in cybercrime statutes. Felony Bench counts only unique incidents where an AI agent affects a third‑party entity; merely escaping a sandbox is not sufficient for a count, and the site focuses on containment breaches that lead to illegal access or damage. Discussions note possible liability for the user, third‑party host, harness developer, or LLM developer under the CFAA.

hackernews · colinprince · Aug 21, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49389430)

**Background**: AI agents are software systems that can autonomously perform tasks by invoking large language models and interacting with external systems, often operating within sandboxes or containment mechanisms to limit their actions. The Computer Fraud and Abuse Act (CFAA) is a U.S. federal law that criminalizes unauthorized access to computers and related conduct, providing both civil and criminal penalties. Legal scholars debate whether the CFAA’s intent requirements apply when an AI agent, without human direction, inadvertently violates the law.

<details><summary>References</summary>
<ul>
<li><a href="https://www.felonybench.com/">Felony Bench: Be AI, Do Crime</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act">Computer Fraud and Abuse Act - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R46536/R46536.3.pdf">Cybercrime and the Law: Computer Fraud and Abuse Act (CFAA ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated who should be liable—user, third‑party host, harness developer, or LLM developer—while some noted that proving intent is required under the CFAA, making inadvertent actions less likely to be felonies. Others criticized the name 'Felony Bench' as overstated, and an Australian user pointed out that 'felony' is a U.S. legal term not used in Australia.

**Tags**: `#AI safety`, `#legal liability`, `#AI agents`, `#CFAA`, `#Hacker News discussion`

---

<a id="item-2"></a>
## [Accidental logging of hundreds of thousands of phone calls via e164.arpa ENUM DNS zone](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

The author inadvertently configured a DNS resolver to log queries to the e164.arpa ENUM zone, capturing hundreds of thousands of ENUM lookups that corresponded to phone call attempts, including those targeting military bases. This revealed a previously overlooked attack surface in telephony routing. It shows that the deprecated ENUM infrastructure still receives real telephony traffic, exposing privacy and security risks, especially for sensitive numbers like military lines. The incident highlights how neglected legacy protocols can be inadvertently exploited, prompting a reevaluation of abandoned but still active Internet resources. The e164.arpa zone translates telephone numbers in E.164 format into DNS NAPTR records; the author's logging captured queries for numbers such as those assigned to Diego Garcia and other military installations, revealing actual call attempt patterns. Although the zone is largely abandoned and considered dead, it remains resolvable through certain private VPN‑based services, and the logging resulted from a misconfiguration rather than an intentional attack.

hackernews · gavide · Aug 21, 13:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**Background**: ENUM (E.164 Number Mapping) is a protocol suite that maps telephone numbers to DNS using the e164.arpa zone, as defined in RFC2916 and RFC6116. It was created to unify the traditional telephone numbering system with Internet addressing, but saw limited adoption and is now mostly unused, with only niche private deployments (e.g., VPN‑based number‑porting services) still relying on it. Because many country‑code delegations have lapsed, stale records remain queryable, which allowed the author’s accidental logging to capture real call‑attempt traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telephone_number_mapping">Telephone number mapping - Wikipedia</a></li>
<li><a href="https://www.cloudns.net/enum-dns-zones/">What is ENUM? | ENUM (E.164) DNS Services | ClouDNS</a></li>
<li><a href="https://techandbusiness.org/newswire/yQaCtW8XSIvB1f23yltTQa">Researcher reports abandoned ENUM delegation exposed military ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that ENUM is largely dead and treat the finding as a curiosity, with some expressing surprise the author wasn’t penalized. Several suggested testing with a SIP server to see if the queries resulted in actual calls, while others mentioned the TRIP protocol as an alternative routing method. The discussion also highlighted appreciation for exposing overlooked infrastructure, concern that serious attention only came after military involvement, and observation that such holes can remain unnoticed for years.

**Tags**: `#DNS`, `#ENUM`, `#security`, `#privacy`, `#telecommunications`

---

<a id="item-3"></a>
## [US Citizen Charged with Felony for Deleting Phone Data at Border](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) ⭐️ 8.0/10

In August 2026, US citizen Samuel Tunick faced felony charges after deleting data from his smartphone during a Customs and Border Protection inspection at the border. It highlights the ongoing tension between the government's broad border search authority and individuals' Fourth Amendment‑related privacy rights, prompting scrutiny of legal limits on device searches. Deleting files can be prosecuted under obstruction statutes, yet forensic tools often recover deleted data, making simple deletion insufficient against determined searches.

hackernews · floathub · Aug 21, 12:10 · [Discussion](https://news.ycombinator.com/item?id=49386895)

**Background**: Under the border search exception, US Customs and Border Protection may inspect electronic devices without a warrant, although courts have acknowledged heightened privacy concerns for digital devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.visaverge.com/knowledge/keeping-your-phone-and-data-private-at-the-u-s-border/">U.S. Border Phone Searches: Rights, Risks, and Data Protection</a></li>
<li><a href="https://www.cbp.gov/travel/cbp-search-authority/border-search-electronic-devices">Border Search of Electronic Devices at Ports of Entry</a></li>
<li><a href="https://elitedf.com/deleted-data-mobile-forensics/">Deleted Phone Data Recovery : What Is Actually Recoverable</a></li>

</ul>
</details>

**Discussion**: Commenters discussed technical countermeasures such as decoy passcodes that secretly wipe data, imaging phones from flash drives to avoid deception, and using automation apps like Tasker to trigger wipes.

**Tags**: `#privacy`, `#border security`, `#digital rights`, `#smartphone security`, `#legal issues`

---

<a id="item-4"></a>
## [DeepSeek releases v4-flash vision experimental model with image tokenization details](https://api-docs.deepseek.com/guides/vision/) ⭐️ 8.0/10

DeepSeek announced its v4-flash vision experimental model, releasing documentation that describes how images are tokenized and automatically resized before inference. The community has begun testing the model’s visual reasoning on tasks such as reading clock faces. This release shows DeepSeek’s progress in multimodal capabilities, offering a concrete scaling strategy for vision‑language models and highlighting both strengths and remaining gaps in visual reasoning. It affects developers building OCR, document understanding, and other vision‑intensive AI applications. Images are converted into tokens based on their dimensions; before inference they are resized—smaller images (< ≈384×384 px) are upscaled, larger ones are downscaled to roughly an 800×800‑pixel total count while preserving aspect ratio, and the resulting tokens are billed together with text tokens. Early tests reveal limitations such as misreading simple clock images and occasional hallucination of vision tools when the model cannot actually see.

hackernews · dares2573 · Aug 21, 10:33 · [Discussion](https://news.ycombinator.com/item?id=49386163)

**Background**: In vision Transformers, images are typically split into fixed-size patches that serve as tokens, but this uniform approach can ignore image content structure. Recent work explores adaptive tokenization methods (e.g., superpixel‑based) to better align tokens with semantic regions. Visual reasoning tasks such as reading clock faces remain a significant challenge for multimodal large language models, requiring accurate spatial and symbolic understanding. Benchmarks show that even leading models struggle with such tasks, highlighting the importance of improved vision encoders and tokenization strategies.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2402.14327">Paper page - Subobject-level Image Tokenization</a></li>
<li><a href="https://arxiv.org/html/2502.05092v1">Lost in Time: Clock and Calendar Understanding Challenges in ...</a></li>
<li><a href="https://aimultiple.com/visual-reasoning">Compare Multimodal AI Models on Visual Reasoning</a></li>

</ul>
</details>

**Discussion**: Commenters praise the model’s promise and its clear resizing rules, but many note failures on simple clock tests, a tendency to hallucinate vision capabilities when the model cannot actually see, and concerns that the 800×800 pixel target may be too low for OCR of full pages. Overall sentiment is cautiously optimistic, with calls for higher resolution limits in future versions.

**Tags**: `#DeepSeek`, `#vision model`, `#multimodal AI`, `#LLM`, `#HackerNews`

---

<a id="item-5"></a>
## [We achieved sub‑50 ms latency with Qwen3‑TTS.](https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/) ⭐️ 8.0/10

Researchers optimized the open-source Qwen3-TTS model to achieve a 34 ms p95 time-to-first-audio at 10 requests per second on a single NVIDIA H100 GPU, and released the implementation and benchmarks. This shows that high-quality, open-source TTS can meet the sub‑50 ms latency needed for real‑time voice agents, lowering the barrier for interactive applications. The team used kernel fusion, batch‑size tuning, and TensorRT‑LLM integration to cut inference overhead while preserving natural speech quality, and they published detailed latency breakdowns on GitHub.

hackernews · toebee · Aug 21, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49389952)

**Background**: Qwen3-TTS is an open‑source text‑to‑speech series from Alibaba’s Qwen team that supports streaming, expressive, and voice‑cloning capabilities. Time‑to‑first‑audio (TTFA) measures the full pipeline from user input to the first audible sample, including LLM processing and audio playback. The NVIDIA H100 GPU, based on the Hopper architecture, delivers high throughput for LLM inference, making it suitable for low‑latency AI services.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/Qwen3-TTS: Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning. · GitHub</a></li>
<li><a href="https://futureagi.com/glossary/call-abandonment-rate/">Call Abandonment Rate: Definition & FutureAGI Guide (2026)</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/h100/">H 100 GPU | NVIDIA</a></li>

</ul>
</details>

**Discussion**: Commenters praised the low latency, noted interest in running the model on‑device or via Cloudflare Workers, discussed trade‑offs between latency and voice quality, and warned that bidirectional models can produce premature filler.

**Tags**: `#text-to-speech`, `#latency optimization`, `#real-time AI`, `#open-source`, `#H100 benchmark`

---

<a id="item-6"></a>
## [AI Companies Destroy Physical Books for Training Data, Urging Preservation](https://annas-archive.gl/blog/physical-destruction.html) ⭐️ 8.0/10

AI companies are reportedly purchasing rare books, scanning them with destructive methods that cut the spine and shred the physical copies, then using the extracted text as training data; the Anna's Archive blog urges scanning and preserving these books before they are lost forever. This practice raises serious ethical and copyright concerns, threatens the survival of unique physical artifacts, and could erode cultural heritage that libraries and collectors rely on; it also highlights the tension between cheap AI training data and responsible preservation. Destructive scanning often involves removing the book’s spine and shredding the pages after OCR, a process that can be up to ten times cheaper than nondestructive scanning; the article notes that rare books with few copies are especially vulnerable, and points to Google Books’ earlier nondestructive approach as a contrast.

hackernews · Cider9986 · Aug 21, 02:37 · [Discussion](https://news.ycombinator.com/item?id=49383026)

**Background**: Optical character recognition (OCR) converts scanned page images into machine‑readable text, enabling AI models to ingest large corpora; digital archiving aims to preserve content over time through formats that resist degradation, unlike fragile paper. Historical projects such as Google Books (Project Ocean) demonstrated large‑scale nondestructive scanning, while recent reports show some AI firms opting for destructive methods to cut costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/angy-watson-7999b940_training-ai-scan-and-destroy-books-everyone-activity-7490986357905932288-yM1i">Big Tech 's AI Training Methods: Scanning and Destroying Books</a></li>
<li><a href="https://en.wikipedia.org/wiki/Optical_character_recognition">Optical character recognition - Wikipedia</a></li>
<li><a href="https://www.tigerdroppings.com/rant/o-t-lounge/ai-companies-are-buying-rare-books-cutting-the-spine-off-to-scan-then-shredding-them/124288398/">AI companies are buying rare books , cutting the spine off to scan, then...</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some argue that destroying a single copy is insignificant because many editions exist, while others condemn the cost-driven destruction of rare books, note that nondestructive scanning is far more expensive, and point out that copyright holders could release works instead of forcing companies to shred them.

**Tags**: `#AI`, `#copyright`, `#book preservation`, `#digital archiving`, `#ethics`

---

<a id="item-7"></a>
## [KANs Used to Price CAT Bonds with Interpretable Symbolic Formula](https://arxiv.org/abs/2608.19217) ⭐️ 8.0/10

The authors applied Kolmogorov--Arnold Networks to approximate CAT bond prices under a compound Poisson loss model, extracting an interpretable symbolic pricing formula with an average relative error of 0.483% and enforcing monotonicity via constrained training with convergence guarantees. This work demonstrates how KANs can provide fast, accurate, and interpretable surrogate models for catastrophe bond valuation, bridging machine learning and actuarial science for better risk management in insurance markets. The symbolic formula was obtained from a baseline-plus-residual KAN trained on deviations from a closed-form lognormal baseline; monotonicity with respect to catastrophe arrival intensity λ, initial short rate r0, and trigger threshold D is guaranteed by constraints on KAN edge functions, and the training objective ensures convergence.

rss · arXiv Quantitative Finance · Aug 21, 04:00

**Background**: Kolmogorov-Arnold Networks (KANs) are neural networks inspired by the Kolmogorov-Arnold representation theorem, where learnable functions are placed on edges instead of fixed activation functions, enabling symbolic extraction. CAT bonds are insurance-linked securities whose payout depends on catastrophe losses often modeled by a compound Poisson process with lognormal severities, requiring efficient pricing under risk-neutral measures. Monotonic neural networks enforce that the output does not decrease when certain inputs increase, which is essential for financial models where higher hazard rates or interest rates should not lower bond prices. The paper combines these ideas to obtain a monotonic, interpretable KAN surrogate for CAT bond pricing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.19217">CAT Bond Pricing with Kolmogorov--Arnold Networks</a></li>
<li><a href="https://itsshashi.medium.com/decoding-kan-kolmogorov-arnold-network-10c691324ba2?source=user_profile_page---------7-------------29d77aeeb914---------------">Decoding KAN : Kolmogorov - Arnold Network | by Dr.... | Medium</a></li>
<li><a href="https://www.fico.com/blogs/trusted-ai-science-monotonicity-neural-networks">Trusted AI: The Science of Monotonicity in Neural Networks</a></li>

</ul>
</details>

**Tags**: `#Kolmogorov-Arnold Networks`, `#CAT bond pricing`, `#insurance risk modeling`, `#monotonic neural networks`, `#symbolic regression`

---

<a id="item-8"></a>
## [Reinforcement Learning Approach to UniswapV3 Concentrated Liquidity Provision](https://arxiv.org/abs/2608.19389) ⭐️ 8.0/10

The paper formulates dynamic liquidity provision in UniswapV3 as a stochastic impulse control problem and uses reinforcement learning to learn interpretable, state‑dependent policies that mitigate downside risk. These policies allocate liquidity based on mispricing, rebalancing costs, uncertainty, inventory exposure, and heterogeneous risk preferences, compressing the left tail of the PnL distribution and avoiding catastrophic outcomes under high uncertainty. This work bridges DeFi microstructure and reinforcement learning, offering interpretable strategies that can improve liquidity provider performance and reduce tail risk. It influences both AMM design and the broader application of RL in financial systems. The authors model the LP’s decision as an impulse control problem with discrete rebalancing actions, train RL agents using Proximal Policy Optimization, and benchmark them against baseline and sophisticated agents from AMM microstructure literature. Results show significant left‑tail compression of the PnL distribution relative to baselines.

rss · arXiv Quantitative Finance · Aug 21, 04:00

**Background**: UniswapV3 introduces concentrated liquidity, allowing LPs to allocate capital within custom price ranges (ticks) rather than the full (0,∞) range, increasing capital efficiency but requiring active management. Liquidity provision becomes a sequential decision problem where LPs must decide when and where to rebalance positions as prices move, which can be framed as a stochastic impulse control problem involving costly, discrete adjustments. Recent research applies reinforcement learning to learn optimal rebalancing policies, treating the LP’s profit and loss as a reward signal and incorporating factors such as mispricing, uncertainty, and risk preferences.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.uniswap.org/concepts/protocol/concentrated-liquidity">Concentrated Liquidity | Uniswap Developers</a></li>
<li><a href="https://arxiv.org/pdf/2602.10798">Trading in CEXs and DEXs with Priority Fees and Stochastic Delays</a></li>
<li><a href="https://arxiv.org/html/2501.07508v1">Improving DeFi Accessibility through Efficient Liquidity ...</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#Reinforcement Learning`, `#Automated Market Makers`, `#Liquidity Provision`, `#Stochastic Control`

---

<a id="item-9"></a>
## [GDPR Caused 4.88% Weekly Visit Decline After 3 Months, 10.02% After 18 Months](https://arxiv.org/abs/2411.11589) ⭐️ 8.0/10

Using a generalized synthetic control estimator on trillions of visits to 6,387 websites across 13 countries, the study estimates that GDPR reduced weekly visits by 4.88% after three months and by 10.02% after 18 months, with the decline driven mainly by fewer unique visitors. The paper provides a rigorous, large‑scale causal analysis of GDPR’s impact on online behavior, offering policymakers clear evidence of unintended traffic losses and heterogeneous effects across sites. The analysis decomposes the traffic drop into a 6.61% decline in unique visitors and a 0.59% decline in visits per unique visitor after 18 months, revealing offsetting gains for about one quarter of websites and stronger engagement among remaining users on losing sites.

rss · arXiv Quantitative Finance · Aug 21, 04:00

**Background**: The General Data Protection Regulation (GDPR) is an EU privacy law enacted in 2018 that restricts how personal data can be collected and processed. To isolate its causal impact on online usage, the study employs a generalized synthetic control estimator, which builds a weighted control group from unaffected observations to approximate what would have happened without GDPR. This approach enables the decomposition of overall traffic changes into changes in unique visitors (usage frequency) and visits per unique visitor (usage intensity).

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/generalized-synthetic-control-methods">Generalized Synthetic Control Methods</a></li>
<li><a href="https://en.wikipedia.org/wiki/Synthetic_control_method">Synthetic control method</a></li>

</ul>
</details>

**Tags**: `#GDPR`, `#privacy regulation`, `#online usage behavior`, `#causal inference`, `#web analytics`

---

<a id="item-10"></a>
## [ContestTrade: Multi-Agent LLM Trading System with Internal Contest Mechanism](https://arxiv.org/abs/2508.00554) ⭐️ 8.0/10

ContestTrade introduces a two-team multi-agent LLM framework where a Data Team extracts textual factors and a Research Team generates trading decisions, linked by a Quantify-Predict-Allocate contest mechanism that scores agents after market outcomes are observed and allocates resources to those with positive predicted utility. In a post-2024 A-share backtest, it outperforms baseline strategies in return and risk-adjusted performance. By isolating noisy market information and using an internal contest to reward only agents with demonstrably positive utility, ContestTrade mitigates the sensitivity of LLM-based traders to non‑stationary data, potentially improving robustness and profitability of algorithmic trading systems. This approach could influence future designs of LLM‑driven financial agents and inspire similar competitive mechanisms in other AI‑assisted decision‑making domains. The system comprises a Data Team that condenses massive market data into diversified textual factors fitting LLM context windows and a Research Team that produces parallel multipath trading decisions via tool‑augmented deep research. Agents are scored only after market outcomes become observable; future utility is predicted from historical scores, and resources are allocated to agents whose predicted utility is positive. Backtesting on post‑2024 A‑share data shows higher returns and risk‑adjusted metrics than the evaluated baselines.

rss · arXiv Quantitative Finance · Aug 21, 04:00

**Background**: Large language model (LLM) agents are increasingly used in financial trading but can be hampered by noisy, non‑stationary data that exceeds their limited context windows. Multi‑agent systems address this by splitting work into specialized teams—e.g., a Data Team that extracts textual factors and a Research Team that generates decisions—while contest mechanisms, grounded in game theory, reward agents based on observable outcomes to align incentives. Tool‑augmented deep research further equips agents with external retrieval and analysis capabilities, allowing them to synthesize information beyond their internal knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.00554">ContestTrade: A Multi-Agent Trading System Based on Internal Contest Mechanism</a></li>
<li><a href="https://huggingface.co/papers/2511.13288">Paper page - Multi - Agent Deep Research : Training Multi - Agent ...</a></li>
<li><a href="https://www.convert.com/blog/ai/context-windows-structured-data/">Context windows, structured data, and text analysis with AI</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#large language models`, `#algorithmic trading`, `#financial AI`, `#contest mechanism`

---

<a id="item-11"></a>
## [From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems](https://arxiv.org/abs/2605.23955) ⭐️ 8.0/10

The paper surveys determinism and reproducibility failures in financial AI across tabular, graph, and LLM workflows, and validates findings with experiments on public financial datasets measuring explanation rank instability, prediction flip rates, and tensor-parallel-induced output divergence. Determinism is crucial for regulatory compliance and auditability in finance; the survey highlights systemic sources of nondeterminism and proposes a layered evaluation framework linking modality-specific metrics to audit readiness, helping practitioners and regulators ensure trustworthy AI deployments. The study quantifies explanation rank instability in credit scoring using RBO, prediction flip rates in GNN fraud detection via D_cos, and tensor-parallel-induced output divergence in LLM entity extraction measured by TDI and PSD, showing that logit-level and semantic-level determinism measures complement each other.

rss · arXiv Quantitative Finance · Aug 21, 04:00

**Background**: Financial AI systems increasingly rely on deep neural networks and generative AI, which introduce mechanical nondeterminism from hardware, parallelism, and stochastic algorithms. Reproducibility is essential for regulatory scrutiny, yet sources such as post‑hoc explanation variance, stochastic sampling in graph neural networks, and tensor parallelism in LLMs can cause divergent outputs. Understanding these failure modes helps build auditable models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.23955">From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems</a></li>
<li><a href="https://www.researchgate.net/publication/405720236_Uncertainty-aware_spatio-temporal_contrastive_graph_neural_networks_for_cyber_financial_fraud_detection_and_risk_management">(PDF) Uncertainty-aware spatio-temporal contrastive graph neural networks for cyber financial fraud detection and risk management</a></li>
<li><a href="https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-inference/app-notes/parallelism.html">Parallelism Techniques for LLM Inference — AWS Neuron ...</a></li>

</ul>
</details>

**Tags**: `#financial AI`, `#reproducibility`, `#determinism`, `#machine learning`, `#survey`

---