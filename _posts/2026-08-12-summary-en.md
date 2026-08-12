---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 63 items, 12 important content pieces were selected

---

1. [Compression and Prediction Are Fundamentally Equivalent](#item-1) ⭐️ 8.0/10
2. [Researchers Steal Reasoning Traces from Proprietary LLM APIs](#item-2) ⭐️ 8.0/10
3. [British Transport Police Expand Live Facial Recognition Trial to London Underground](#item-3) ⭐️ 8.0/10
4. [Formalizing the Information Gap in Conformal Prediction](#item-4) ⭐️ 8.0/10
5. [LLM Agents in Supply Chain Negotiations Show Capability-Driven Efficiency and Distributional Bias](#item-5) ⭐️ 8.0/10
6. [Telemetry Framework for Self-Adapting Generative AI with Tamper-Evident Logging](#item-6) ⭐️ 8.0/10
7. [Joint Lyapunov Certificates Enable Zero-Knowledge Governance for Multi-Agent Generative AI](#item-7) ⭐️ 8.0/10
8. [Data Segmentation Leads AI to Tacit Collusion in Pricing Games](#item-8) ⭐️ 8.0/10
9. [ParlayMarket Introduces AMM for Joint Contracts with Coherent Pricing](#item-9) ⭐️ 8.0/10
10. [Extended State-dependent Hawkes Process Models Limit Order Book Dynamics](#item-10) ⭐️ 8.0/10
11. [AI Scaling Only Helps Human Teams When Humans Perceive AI Accurately](#item-11) ⭐️ 8.0/10
12. [Paper Proposes Four-Layer Governance Framework for Agentic AI in Finance](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Compression and Prediction Are Fundamentally Equivalent](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

The ngrok blog article argues that data compression and prediction are fundamentally equivalent processes, explaining that efficient compression relies on predicting patterns in data, a concept rooted in information theory and machine learning. This insight unifies concepts from information theory, machine learning, and artificial intelligence, suggesting that understanding compression can lead to better predictive models and more intelligent systems, with implications for data efficiency and AI development. The article connects compression to prediction through concepts like Kolmogorov complexity, Normalized Compression Distance (NCD), and Prediction by Partial Matching (PPM), emphasizing that compression works by modeling and predicting data patterns.

hackernews · nikolay · Aug 11, 19:49 · [Discussion](https://news.ycombinator.com/item?id=49263497)

**Background**: In information theory, data compression reduces redundancy by encoding information using fewer bits, while prediction involves forecasting future data points based on past patterns. Kolmogorov complexity measures the intrinsic complexity of data as the length of the shortest program that can generate it, linking compressibility to predictability. These ideas form a theoretical foundation for understanding how learning and intelligence may emerge from compression-like processes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov_complexity">Kolmogorov complexity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_compression">Data compression - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the nuance between compression and prediction, noting that equivalence holds only when training data represents the full future distribution; some referenced academic courses, videos by Grant Sanderson, and related concepts like PPM and Kolmogorov complexity, while others suggested compression is more about abstraction and decompression about extrapolation.

**Tags**: `#information theory`, `#machine learning`, `#data compression`, `#prediction`, `#Kolmogorov complexity`

---

<a id="item-2"></a>
## [Researchers Steal Reasoning Traces from Proprietary LLM APIs](https://stolen-thoughts.com/) ⭐️ 8.0/10

Researchers demonstrated a method to extract internal reasoning traces from frontier LLMs by replaying model outputs into weaker models and using jailbreaking or tool-use tricks to recover chain-of-thought reasoning. This technique raises significant concerns for AI safety, intellectual property protection, and model distillation, as it enables unauthorized extraction of proprietary reasoning capabilities from LLM APIs, potentially undermining competitive advantages and safety guardrails. The attack involves replaying outputs from a frontier model into a weaker sibling model, then applying jailbreaking or tool-use prompts to elicit the internal chain-of-thought reasoning that was otherwise hidden in the API response.

hackernews · quantumgarbage · Aug 11, 13:22 · [Discussion](https://news.ycombinator.com/item?id=49257876)

**Background**: Reasoning traces are intermediate reasoning steps that large language models generate before producing a final answer, often encouraged by chain-of-thought prompting to improve performance on complex tasks. Proprietary LLM APIs typically hide these traces, exposing only the final output to users. Model extraction attacks aim to replicate a model's behavior or knowledge through API queries, posing risks to intellectual property and AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.23163v1">Probing the Trajectories of Reasoning Traces in Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2506.22521v1">A Survey on Model Extraction Attacks and Defenses for</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**Discussion**: Commenters debated the ethics of the technique, with some arguing that extracting reasoning traces from models one has paid to use is not truly 'stealing,' while others highlighted the novelty of replaying outputs across models and noted that similar effects could be achieved via tool use or disabling thinking modes in certain models.

**Tags**: `#LLM security`, `#AI safety`, `#model extraction`, `#reasoning traces`, `#proprietary models`

---

<a id="item-3"></a>
## [British Transport Police Expand Live Facial Recognition Trial to London Underground](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 8.0/10

British Transport Police are expanding their live facial recognition (LFR) trial to Transport for London Underground stations, deploying cameras to scan passengers' faces in real time against a police watchlist. The expansion raises significant privacy and civil liberties concerns, as it enables mass surveillance in public transit without explicit public consent, potentially chilling anonymous movement and setting a precedent for broader state surveillance. The LFR system is designed to identify individuals on a police watchlist for 'high harm' offenses such as sexual offences, robbery, and knife crime, with the trial having begun on 11 February 2026 at selected transport hubs before expanding to Underground stations.

hackernews · BlueBerry2001 · Aug 11, 09:40 · [Discussion](https://news.ycombinator.com/item?id=49255496)

**Background**: Live Facial Recognition (LFR) technology uses AI-powered cameras to analyze facial features in real time and compare them against databases of wanted individuals. While proponents argue it enhances public safety by enabling faster suspect identification, critics warn it poses risks of misidentification, function creep, and erosion of anonymity in public spaces. The UK has been a leader in deploying LFR in public areas, despite ongoing legal challenges and public debate over its necessity and proportionality.

<details><summary>References</summary>
<ul>
<li><a href="https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/">BTP expands Live Facial Recognition (LFR) trial into London Underground stations | British Transport Police</a></li>
<li><a href="https://www.btp.police.uk/police-forces/british-transport-police/areas/about-us/about-us/facial-recognition-technology/">British Transport Police use of Live Facial Recognition Technology | British Transport Police</a></li>
<li><a href="https://www.mylondon.news/news/british-transport-police-trial-live-34435589">British Transport Police to trial live facial recognition cameras at London Tube stations - My London</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong concerns about privacy erosion, with some noting that anonymous travel on the Underground had already declined due to contactless payment systems, while others criticized the trial as Orwellian and questioned its effectiveness and democratic legitimacy, suggesting it enables surveillance overreach rather than genuine crime prevention.

**Tags**: `#facial recognition`, `#surveillance`, `#privacy`, `#civil liberties`, `#public safety`

---

<a id="item-4"></a>
## [Formalizing the Information Gap in Conformal Prediction](https://arxiv.org/abs/2608.07479) ⭐️ 8.0/10

The paper formalizes the residual-information gap in conformal prediction, showing that log-score regret relative to the oracle equals the mutual information between residuals and inputs, which conformalization cannot reduce. This work clarifies a fundamental limitation of conformal prediction: it guarantees coverage but cannot improve forecast sharpness, addressing a common misinterpretation in uncertainty quantification and guiding better evaluation of predictive systems. For a single-shape residual predictive system, the log-score regret relative to the oracle is exactly the mutual information I(R;X) between residual R and input X; conformalization affects coverage but not this quantity, as it depends on the predictor's shape class, not calibration.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Conformal prediction provides finite-sample, distribution-free marginal coverage guarantees under exchangeability, producing valid prediction regions for any point predictor. However, this validity does not imply forecast quality or sharpness, and the method is often misinterpreted as indicating good predictive performance. The paper distinguishes between coverage (guaranteed by conformalization) and sharpness (unaffected by it), using information theory to formalize the gap.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.07479">[2608.07479] Marginally Useful: Formalizing the Information Gap in Conformal Prediction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2608.07479">Marginally Useful Formalizing the Information Gap in Conformal Prediction</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#uncertainty quantification`, `#machine learning theory`, `#information theory`, `#calibration`

---

<a id="item-5"></a>
## [LLM Agents in Supply Chain Negotiations Show Capability-Driven Efficiency and Distributional Bias](https://arxiv.org/abs/2608.07538) ⭐️ 8.0/10

A study evaluated nine LLMs from OpenAI, Google, and Alibaba in 9,840 autonomous supply chain negotiations with asymmetric information, finding high-capability models achieve near-optimal surplus but require more negotiation rounds, while weaker models accept irrational contracts at significant rates. The findings reveal critical tradeoffs in deploying LLM agents for autonomous procurement: capability affects both value creation and reliability, while provider identity and prompting significantly influence surplus division, necessitating capability-based safeguards and strategic deployment choices. High-capability LLMs captured 95.4% of first-best surplus but averaged 2.98 negotiation rounds (vs. 1.25 in equilibrium), eroding 21-34% of surplus due to delay; baseline models accepted individually irrational contracts in 19.2% of cases, versus 0.0-0.6% for mid-tier and flagship models.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: The study models a canonical supply chain bargaining scenario where a buyer with private demand information negotiates a quantity-payment contract with an uninformed seller, using Perfect Bayesian Equilibrium as a benchmark for rational behavior under asymmetric information. LLM-to-LLM negotiations were conducted to isolate agent behavior from human influence, testing whether deployed agents can replicate economically rational outcomes in autonomous settings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perfect_Bayesian_equilibrium">Perfect Bayesian equilibrium - Wikipedia</a></li>
<li><a href="https://pubsonline.informs.org/doi/10.1287/mnsc.2014.1938">Dynamic Bargaining in a Supply Chain with Asymmetric Demand Information | Management Science</a></li>
<li><a href="https://www.labarna.ai/blog/autonomous-agent-negotiation-protocols-strategies">Autonomous Agent Negotiation: Protocols and Strategies</a></li>

</ul>
</details>

**Tags**: `#LLM Agents`, `#Multi-agent Systems`, `#Game Theory`, `#Supply Chain Optimization`, `#Autonomous Negotiation`

---

<a id="item-6"></a>
## [Telemetry Framework for Self-Adapting Generative AI with Tamper-Evident Logging](https://arxiv.org/abs/2608.09069) ⭐️ 8.0/10

The paper proposes a dual-regime telemetry architecture for self-adapting generative AI systems, combining discrete Merkle chains for weight sequence logging and continuous-time generalization via Ito formula to enable auditability and detect unauthorized model changes. This framework addresses a critical gap in model risk management by providing verifiable logging for continually self-adapting models, which violate traditional static model assumptions and require new governance approaches for AI safety and regulatory compliance. The architecture establishes a Minimal Sufficient Statistic for audit, uses Merkle chains for tamper-evident discrete logging, derives continuous-time telemetry via Ito formula with quadratic variation as the telemetry scalar, and employs KL divergence stopping times for event-driven logging, while formalizing six adversarial model hiding strategies with corresponding countermeasures.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Model risk management traditionally assumes models are static after deployment, but self-adapting generative AI systems continuously update their own weights during operation, making point-in-time validation ineffective. This creates a governance challenge where unauthorized or harmful model changes could go undetected without continuous monitoring and tamper-evident logging mechanisms.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.09069">Telemetry and Concealment in Self - Adapting Generative AI : Logging...</a></li>
<li><a href="https://speytech.com/insights/merkle-chains-ml-audit/">Merkle Chains for ML Audit Trails | SpeyTech</a></li>
<li><a href="https://arxiv.org/html/2608.09069">Telemetry and Concealment in Self-Adapting Generative AI: Logging...</a></li>

</ul>
</details>

**Tags**: `#AI Governance`, `#Model Risk Management`, `#Telemetry`, `#Self-Adapting Systems`, `#Adversarial Robustness`

---

<a id="item-7"></a>
## [Joint Lyapunov Certificates Enable Zero-Knowledge Governance for Multi-Agent Generative AI](https://arxiv.org/abs/2608.09087) ⭐️ 8.0/10

The paper introduces Joint Lyapunov Certificates (JLC) to govern K-agent generative AI systems by proving stochastic stability and detecting emergent ensemble-level risks through a cryptographic protocol that attests to Model Risk Management compliance without revealing proprietary model weights. This framework addresses a critical gap in AI governance where individual model stability does not guarantee system-level stability in coupled generative AI, enabling verifiable, privacy-preserving compliance for regulatory standards in multi-agent AI systems. The work derives the exact critical coupling threshold for mean-square stability loss, establishes a Noise-Floor Theorem for zero-knowledge attestation targets, and constructs a per-epoch SNARK on live weights, validated across five numerical studies using a multi-agent softmax system.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Model Risk Management (MRM) traditionally relies on per-agent Lyapunov analysis to ensure stability of individual AI models, but this approach fails when models are coupled through interaction matrices, as emergent risks can arise even if each model appears stable in isolation. Joint Lyapunov Analysis extends this by examining the collective dynamics of interconnected systems, particularly relevant for self-adapting generative AI that shares meta-learning couplings. Zero-knowledge proofs, such as SNARKs, allow one party to prove the validity of a statement without revealing underlying data, making them suitable for attesting to AI system compliance while protecting intellectual property.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.09087v1">Joint Lyapunov Certificates for 𝐾-Agent Generative AI ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.09087">Joint Lyapunov Certificates for K-Agent Generative AI Governance...</a></li>
<li><a href="https://www.nist.gov/itl/ai-risk-management-framework">AI Risk Management Framework | NIST</a></li>

</ul>
</details>

**Tags**: `#AI Governance`, `#Lyapunov Stability`, `#Multi-Agent Systems`, `#Zero-Knowledge Proofs`, `#Model Risk Management`

---

<a id="item-8"></a>
## [Data Segmentation Leads AI to Tacit Collusion in Pricing Games](https://arxiv.org/abs/2403.06150) ⭐️ 8.0/10

The study shows that when consumer data is labeled and segmented, AI pricing algorithms can tacitly collude through market allocation or bait-and-restraint-exploit strategies, even without direct communication. This challenges the assumption that more data always improves competition, revealing how data advantages can enable harmful AI behaviors that regulators must monitor to protect consumers. Under symmetric segmentation, each AI monopolizes high-willingness-to-pay segments with supra-competitive prices; under asymmetric segmentation, the AI with finer segmentation uses a bait-and-restraint-exploit strategy to induce collusion in the other.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Multimarket contact occurs when firms compete in multiple markets, which can facilitate tacit collusion. In AI pricing games, algorithms learn from data to set prices, and when data labeling creates artificial market segments, it increases the strategic interdependence between AIs, making coordinated outcomes more likely even without explicit communication.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.06150">[2403.06150] Artificial Intelligence, Data and Competition</a></li>
<li><a href="https://arxiv.org/html/2403.06150">Artificial Intelligence, Data and CompetitionThis paper was previously circulated as “Algorithmic Collusion and Price Discrimination: the Over-Useage of Data.” We thank Giacomo Calzolari, Jean-Edouard Colliard, Francesco Decarolis, Bo Hu, Bruno Jullien, Sanxi Li, Tristan Tomala, Daniel Yi Xu, Jidong Zhou for their valuable comments and suggestions. We also thank seminar audiences at Fudan University, Nanjing University, Shandong University, University of International Business and Economics, the 2024 Be</a></li>
<li><a href="https://arxiv.org/pdf/2403.06150">Artificial Intelligence, Data and Competition - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#AI and competition`, `#algorithmic collusion`, `#market segmentation`, `#pricing games`, `#data strategy`

---

<a id="item-9"></a>
## [ParlayMarket Introduces AMM for Joint Contracts with Coherent Pricing](https://arxiv.org/abs/2603.22596) ⭐️ 8.0/10

ParlayMarket proposes an automated market-maker for parlay-style joint contracts that maintains a shared pairwise exponential-family belief state, enabling coherent pricing across base and parlay markets using only O(M²) sufficient statistics. This addresses a key limitation in prediction markets by enabling efficient trading of correlated joint outcomes without fragmenting liquidity, with theoretical guarantees on convergence and loss scaling quadratically in the number of base events rather than exponentially. The mechanism compresses the 2^M outcome space into O(M²) sufficient statistics, ensures prices are marginals of a coherent distribution, and shows that parlay trades reduce steady-state error compared to learning from marginals alone, with quadratic loss being worst-case optimal for dense pairwise dependence.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Prediction markets aggregate information but are typically limited to single-event contracts; parlay-style joint contracts (e.g., sports parlays) involve betting on multiple correlated outcomes, which current platforms often prohibit or price inefficiently due to ignored correlations. Exponential-family distributions provide a flexible way to model beliefs, and sufficient statistics allow compact representation of complex distributions. Automated market makers like LMSR update prices based on trades to maintain liquidity and incentivize truthful information revelation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.22596">ParlayMarket: Automated Market Making for Parlay-style Joint ...</a></li>
<li><a href="https://arxiv.org/html/2603.22596v1">ParlayMarket: Automated Market Making for Parlay-style Joint ...</a></li>
<li><a href="https://www.emergentmind.com/topics/parlaymarket">ParlayMarket: AMM for Joint Contracts - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#automated market making`, `#parlay contracts`, `#exponential family`, `#mechanism design`

---

<a id="item-10"></a>
## [Extended State-dependent Hawkes Process Models Limit Order Book Dynamics](https://arxiv.org/abs/2604.23961) ⭐️ 8.0/10

The paper introduces an Extended State-Dependent Hawkes Process (ExsdHawkes) that models limit order book dynamics by allowing state disappearances and proves MLE separability using KKT conditions. Empirically, it reproduces volatility signature plots by identifying Marketable Limit Orders as drivers of local super-criticality in disequilibrium states. This model addresses a key gap in financial mathematics by providing a physically consistent framework that accurately captures macro-level volatility patterns in high-frequency trading. It offers quantitative finance practitioners a theoretically grounded tool for simulating limit order books with improved stability and realism. ExsdHawkes enforces physical geometry to pause residual accumulation during inadmissible periods, preventing explosive branching ratios seen in unconstrained models. The model was validated on three months of high-frequency tick data from Mitsubishi UFJ Financial Group (8306), showing unique reproduction of the upward slope in volatility signature plots.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Limit Order Books (LOBs) represent the list of buy and sell orders for a financial asset, updated in real time during trading. Hawkes processes are self-exciting temporal point processes used to model clustered events, such as trades or order submissions, where past events increase the likelihood of future ones. State-dependent variants allow the process intensity to change based on the current state of the system, such as order book imbalance or price pressure.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.23961">[2604.23961] Extended State-dependent Hawkes Process for ...</a></li>
<li><a href="https://arxiv.org/html/2604.23961v2">Extended State-dependent Hawkes Process for Limit Order Books ...</a></li>
<li><a href="https://www.semanticscholar.org/paper/Extended-State-dependent-Hawkes-Process-for-Limit-Kimura/2da2e0d216ccdd84275a129633eadc572cdc11cc">Extended State-dependent Hawkes Process for Limit Order Books ...</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#high-frequency trading`, `#Hawkes process`, `#limit order book`, `#market microstructure`

---

<a id="item-11"></a>
## [AI Scaling Only Helps Human Teams When Humans Perceive AI Accurately](https://arxiv.org/abs/2608.00818) ⭐️ 8.0/10

A new arXiv paper shows that scaling AI improves human-AI team performance only when humans accurately perceive the AI's capabilities; otherwise, overestimation leads to a 'scaling paradox' where better AI worsens outcomes, while underestimation slows gains. This challenges the assumption that larger AI systems always improve performance, highlighting that managing human perception and trust is as important as technical scaling for real-world AI deployment. The study models how over-perception causes a scaling paradox with declining joint performance and profit loss, while under-perception yields slower gains; it suggests operational policies like perception alignment can mitigate these effects.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: AI scaling laws describe how model capabilities improve predictably with increased compute, data, or parameters. However, real-world AI systems often operate in collaboration with humans, where trust, bias, and perception of AI ability can influence outcomes beyond raw performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.00818">[2608.00818] The Scaling Paradox in Human - AI Collaboration</a></li>
<li><a href="https://ideas.repec.org/p/arx/papers/2608.00818.html">The Scaling Paradox in Human - AI Collaboration</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7207559">The Scaling Paradox in Human - AI Collaboration by Anyan... :: SSRN</a></li>

</ul>
</details>

**Tags**: `#human-AI collaboration`, `#AI scaling laws`, `#cognitive modeling`, `#system performance`, `#trust and perception`

---

<a id="item-12"></a>
## [Paper Proposes Four-Layer Governance Framework for Agentic AI in Finance](https://arxiv.org/abs/2608.02311) ⭐️ 8.0/10

The arXiv paper identifies a governance gap for agentic AI in finance, noting 88% of surveyed professionals lack operational frameworks, and proposes a four-layer framework (Policy, Engineering, Composition, Systemic) supported by synthetic simulations and real cases. The framework addresses risks from continuously learning AI systems in finance, offering practical guidance for institutions to manage systemic risks like joint drawdown, which simulations show could rise from 39.2% to 79.3% without proper governance. The framework is grounded in two synthetic illustrations (a regret-covariance drift monitor and a crowding simulation) and three real cases, including an LLM-embedding trading strategy and a $45 billion fund's blowup, with a proposed 90-day implementation sequence.

rss · arXiv Quantitative Finance · Aug 11, 04:00

**Background**: Agentic AI refers to autonomous AI systems that can make decisions and take actions with minimal human oversight, increasingly used in finance for trading and asset management. Traditional governance frameworks, designed for static models, fail to address risks from continuously retrained policies, creating a need for adaptive, system-level oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iofm.com/ap/webinars/agentic-ai-boardroom-building-governance-framework-for-autonomous-finance">Agentic AI & The Boardroom: Building a Governance Framework for...</a></li>
<li><a href="https://pub.towardsai.net/agentic-ai-and-the-smb-banking-advantage-0e75e0514707">Agentic AI and the SMB Banking Advantage | Towards AI</a></li>
<li><a href="https://www.omniscient.media/post/the-market-already-voted-on-agentic-ai-regulators-are-still-finding-their-seats">The Market Already Voted on Agentic AI .... | Omniscient Media</a></li>

</ul>
</details>

**Tags**: `#AI Governance`, `#Agentic AI`, `#Finance`, `#Financial Regulation`, `#Systemic Risk`

---