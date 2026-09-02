---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 58 items, 16 important content pieces were selected

---

1. [Hold Onto Firefox to Preserve Browser Engine Diversity](#item-1) ⭐️ 8.0/10
2. [Anthropic Releases Claude Fable 5.1 and Mythos 5.1 Updates](#item-2) ⭐️ 8.0/10
3. [Slotstream runs 125B Qwen3.8‑Flash‑Next on 48GB Mac via expert offloading](#item-3) ⭐️ 8.0/10
4. [Play Store blocks AuroraStore, impacting GrapheneOS users](#item-4) ⭐️ 8.0/10
5. [Atlas: A World Model for Spatial Intelligence](#item-5) ⭐️ 8.0/10
6. [Sharp convergence rates for stochastic tracking applied to optimal execution.](#item-6) ⭐️ 8.0/10
7. [The Price of Intelligence: A Quality-Adjusted Price Index for AI Services](#item-7) ⭐️ 8.0/10
8. [Jump‑Diffusion Model Shows LVR Has Non‑Zero Lower Bound as Block Time Shrinks.](#item-8) ⭐️ 8.0/10
9. [LLM Multi-Agent Model Simulates Household Expectations Under Tariff Threats](#item-9) ⭐️ 8.0/10
10. [Battery storage's growing role in GB balancing mechanism price formation](#item-10) ⭐️ 8.0/10
11. [Risk-Adjusted Harm Score and FinRedTeamBench Improve LLM Safety in Financial Services](#item-11) ⭐️ 8.0/10
12. [Performance Manipulation in AI-Augmented Labor Markets: Theory and Evidence](#item-12) ⭐️ 8.0/10
13. [Data-Driven Stochastic Optimal Control Model for Intraday Electricity Trading by Renewable Producers](#item-13) ⭐️ 8.0/10
14. [Modeling Peer Review vs AI Screening for Journal Stamp Value](#item-14) ⭐️ 8.0/10
15. [PortBench: A Correlation-Aware Full-Pipeline Benchmark for LLM-Driven Portfolio Management](#item-15) ⭐️ 8.0/10
16. [Fund2Persona Framework Builds Financial Advisor Personas from Fund Disclosures](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Hold Onto Firefox to Preserve Browser Engine Diversity](https://www.newsonaut.com/articles/hang-on-to-your-firefox) ⭐️ 8.0/10

The article urges users to keep using Firefox as a way to maintain browser engine diversity and resist the dominance of Chrome and WebKit-based browsers. Browser engine diversity is crucial for innovation, privacy, and preventing a single vendor from dictating web standards, affecting developers and end‑users alike. Firefox remains the only major desktop browser using Mozilla’s Gecko engine, while most competitors rely on Blink (Chrome) or WebKit (Safari); the piece also notes criticism of Mozilla’s ad‑tech moves and data collection practices.

hackernews · speckx · Sep 1, 20:30 · [Discussion](https://news.ycombinator.com/item?id=49527748)

**Background**: Browser engines such as Blink, Gecko, and WebKit render web pages and implement standards; diversity among them fosters innovation by allowing different approaches to features and performance. Firefox’s Gecko engine, developed by Mozilla, is the only major independent engine not derived from Chromium or WebKit, providing a counterbalance to the dominance of Chrome and Safari. Maintaining multiple engines helps prevent a single vendor from controlling web standards and encourages competition in areas like privacy and ad blocking.

<details><summary>References</summary>
<ul>
<li><a href="https://css-tricks.com/browser-engine-diversity/">Browser Engine Diversity | CSS-Tricks</a></li>
<li><a href="https://blog.mozilla.org/netpolicy/2026/03/23/competition-innovation-and-the-future-of-the-web/">Competition, Innovation, and the Future of the Web - Why Independent Browser Engines Matter - Open Policy & Advocacy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Comparison_of_browser_engines">Comparison of browser engines - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised Firefox as the last major browser offering engine diversity and effective ad‑blocking, calling it essential for a competitive web. At the same time, many criticized Mozilla’s recent moves—such as acquiring an ad‑tech firm and collecting user data—that push users away. Others emphasized that despite disagreements with Mozilla, supporting Firefox on the issue of engine diversity is worthwhile and suggested building coalitions around shared goals.

**Tags**: `#Firefox`, `#browser diversity`, `#web privacy`, `#ad blocking`, `#open web`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Fable 5.1 and Mythos 5.1 Updates](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 8.0/10

Anthropic released Claude Fable 5.1 and Claude Mythos 5.1, featuring improved writing style, adjustable reasoning effort levels (low, medium, high, xhigh), and a reduction in cache‑read pricing from $1 per million tokens to $0.25 per million tokens. The update addresses user feedback on Claude’s stereotypical tone, gives developers fine‑grained control over model reasoning cost, and lowers operating expenses, making the model more competitive for production workloads. The system card for the models is available at https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf, and the price cut brings Fable 5.1’s cache‑read cost to half that of Opus. Adjustable effort levels let users trade latency for deeper reasoning.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**Background**: Anthropic’s Claude family includes models such as Opus, Sonnet, and the earlier Fable line, which are accessed via API with token‑based pricing. Cache‑read pricing refers to the cost of retrieving previously computed model states, a factor that affects latency‑sensitive applications. Reasoning effort levels allow users to specify how much computational work the model should devote to thinking before answering, influencing both quality and response time.

**Discussion**: Felix (an Anthropic employee) praised Fable 5.1’s more natural style and better adherence to style instructions. SimonW demonstrated the new effort levels (low, medium, high, xhigh) and shared tooling that captures reasoning traces, noting the xhigh setting took about 14 minutes. GodelNumbering highlighted the cache‑read price cut but questioned benchmark improvements, while exabrial joked that the update felt like a nerf and a marketing stunt for Mythos.

**Tags**: `#Claude`, `#LLM`, `#Anthropic`, `#AI models`, `#price reduction`

---

<a id="item-3"></a>
## [Slotstream runs 125B Qwen3.8‑Flash‑Next on 48GB Mac via expert offloading](https://github.com/carloslfu/slotstream) ⭐️ 8.0/10

Slotstream enables running a 125‑parameter Qwen3.8‑Flash‑Next model on low‑memory Macs by offloading inactive experts to SSD and streaming them on demand, achieving roughly 12 tokens per second. It shows that massive mixture‑of‑experts models can be inference‑run on consumer‑grade hardware, lowering the barrier for developers who lack GPU servers. Built with Apple’s MLX framework and Swift, the tool offers an auto‑mode that balances memory usage and speed, runs the model in 4‑bit quantization, and can be installed with a simple pip‑like command.

hackernews · carloslfu · Sep 1, 16:42 · [Discussion](https://news.ycombinator.com/item?id=49524447)

**Background**: Qwen3.8‑Flash‑Next is a mixture‑of‑experts (MoE) language model with 125 billion parameters, where only a subset of experts is active for each token. Expert offloading stores the inactive experts on slower storage (such as an SSD) and streams them into memory when needed, dramatically reducing RAM requirements. MLX is Apple’s open‑source machine learning framework that enables efficient GPU‑like computation on Macs using unified memory, and 4‑bit quantization further cuts the model’s memory footprint.

**Discussion**: Commenters praised the achievement but pointed out that the README is cluttered and needs a clearer introduction for newcomers. Several users with similar Mac hardware asked how to increase the context window beyond the current 71,680‑token limit, while others expressed skepticism about achieving high token rates on 16 GB machines without thermal throttling. Some discussed hardware ideas such as adding DDR5 to GPUs and hoped that upcoming Macs with more unified memory would benefit from techniques like Slotstream.

**Tags**: `#LLM inference`, `#model offloading`, `#Mac MLX`, `#SSD streaming`, `#open-source tool`

---

<a id="item-4"></a>
## [Play Store blocks AuroraStore, impacting GrapheneOS users](https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566) ⭐️ 8.0/10

Google Play Store has blocked the AuroraStore client, preventing users from updating apps without a Google account, as noted in the AuroraOSS GitLab work item. The block affects privacy‑conscious users who rely on AuroraStore to avoid Google tracking, sparking debate in the GrapheneOS community about security versus usability trade‑offs. AuroraStore is an open‑source frontend for the Google Play Store that allows anonymous app downloads, while GrapheneOS officially recommends using a sandboxed Play Store for better security; some users prefer Aurora for its lack of ads and dark patterns.

hackernews · erikvanoosten · Sep 1, 15:55 · [Discussion](https://news.ycombinator.com/item?id=49523754)

**Background**: AuroraStore provides a way to browse and install apps from Google Play without signing into a Google account, offering a privacy‑focused alternative to the official client. GrapheneOS is a hardened, open‑source Android‑based operating system designed for security and privacy, officially supported on Google Pixel devices and built on AOSP. The OS encourages users to employ the sandboxed Play Store via Play Integrity APIs to minimize attack surface while maintaining app compatibility.

<details><summary>References</summary>
<ul>
<li><a href="https://frr.wikipedia.org/wiki/Aurora_Store">Aurora Store – Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**Discussion**: Commenters note that GrapheneOS actually advises against AuroraStore and prefers the sandboxed Play Store, while others value Aurora for its lack of toxic UI and dark patterns; some remain uncertain whether the block is intentional or a bug, and several users report being stuck with outdated apps or relying on Aurora for relatives who lack Google accounts.

**Tags**: `#Android`, `#GrapheneOS`, `#AuroraStore`, `#Privacy`, `#Google Play Store`

---

<a id="item-5"></a>
## [Atlas: A World Model for Spatial Intelligence](https://www.worldlabs.ai/blog/atlas) ⭐️ 8.0/10

World Labs unveiled Atlas, an omni world model for spatial intelligence that learns from sparse images to enable high‑fidelity 3D scene reconstruction and generates up to one minute of controllable 1440p video. By providing a compact, predictive representation of 3D environments, Atlas can accelerate robotics simulation, game‑level prototyping, and autonomous perception, bridging the gap between raw perception and actionable spatial intelligence. Atlas is a multimodal autoregressive diffusion transformer that outperforms open‑source specialists on DTU, ETH3D and ScanNet benchmarks for sparse‑view 3D reconstruction, though community notes suggest its temporal consistency may be limited when the camera moves.

hackernews · johnsutor · Sep 1, 17:36 · [Discussion](https://news.ycombinator.com/item?id=49525160)

**Background**: A world model in AI is a machine learning system that builds an internal representation of an environment and predicts how it changes over time in response to actions. Spatial intelligence refers to the ability to understand and reason about physical spaces, which world models aim to achieve by maintaining a coherent, temporally consistent map of the world. Sparse‑view 3D reconstruction is challenging because few overlapping images make traditional structure‑from‑motion and multiview stereo methods fail, motivating learning‑based approaches like Atlas.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.worldlabs.ai/blog/atlas">Atlas: A World Model for Spatial Intelligence | World Labs</a></li>
<li><a href="https://arxiv.org/html/2507.16406v1">Sparse-View 3D Reconstruction: Recent Advances and Open ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised Atlas for its potential in rapid game prototyping and house‑scale reconstruction, while some questioned the meaning of “world model” and noted possible weaknesses in temporal consistency when the camera moves. Others highlighted the value of extracting semantic information from the model’s latent space, and a cofounder invited further questions.

**Tags**: `#world model`, `#spatial intelligence`, `#3D reconstruction`, `#robotics`, `#AI`

---

<a id="item-6"></a>
## [Sharp convergence rates for stochastic tracking applied to optimal execution.](https://arxiv.org/abs/2608.29468) ⭐️ 8.0/10

The authors derive explicit non‑asymptotic upper bounds for a quadratic stochastic tracking problem using a Besov‑type modulus of the target, and apply these bounds to a generalized Obizhaeva–Wang execution model with random terminal inventory. These results provide the first sharp rates for stochastic tracking, yielding implementable near‑optimal strategies that improve practical execution costs and advance theory in quantitative finance and stochastic control. The bounds specialize to the square‑root order O(√ε) for semimartingale targets; the regularized optimal execution cost converges at this rate, and a constructible nearly optimal strategy attains the same approximation rate despite lacking a closed form.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Stochastic tracking problems involve controlling a process to follow a random target, often appearing in finance as optimal execution of trades. The Obizhaeva–Wang model describes price impact from trading, and adding a quadratic rate penalty with parameter ε regularizes the problem to avoid unrealistic trading spikes. A Besov‑type modulus measures the roughness of the target process and governs the convergence speed of tracking errors.

**Tags**: `#stochastic control`, `#optimal execution`, `#convergence rates`, `#Besov modulus`, `#quantitative finance`

---

<a id="item-7"></a>
## [The Price of Intelligence: A Quality-Adjusted Price Index for AI Services](https://arxiv.org/abs/2608.29843) ⭐️ 8.0/10

The paper builds a quality‑adjusted price index for AI inference using 21,024 posted‑price observations from 3,208 models and 86 providers linked to 4,605 benchmark scores via a latent quality index. It shows that standard matched‑model methods measure only a 0.10 log‑point annual price decline, while the quality‑adjusted index falls 0.73 log‑points per year, meaning 87% of the decline is hidden by quality gains. By revealing that most observed price drops are masked by quality improvements, the index changes how economists and policymakers measure competition, concentration, and productivity in the fast‑growing AI market. It provides a more accurate tool for assessing whether AI services are truly becoming cheaper or merely more capable. The index uses matched‑model methods employed by statistical agencies for software, constructs a latent quality index from benchmark response patterns, and includes a pre‑registered validity audit that excludes contamination‑flagged benchmarks. All data, code, and results are publicly reproducible at zero cost.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: A quality‑adjusted price index (or hedonic index) adjusts raw price changes for changes in product quality, allowing economists to separate pure price movements from improvements in performance. In AI inference, quality is not captured by simple specifications but must be inferred from benchmark scores that measure model capabilities. Matched‑model methods, which compare identical models over time, are the standard approach used by agencies such as the BLS for software and other tech products.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.29843">The Price of Intelligence:A Quality-Adjusted Price Index for AI Services</a></li>
<li><a href="https://cemmap.ac.uk/wp-content/uploads/2021/02/CWP0421-Hedonic-prices-and-quality-adjusted-price-indices-powered-by-AI-1.pdf">Hedonic prices and quality</a></li>
<li><a href="https://benchlm.ai/">LLM Leaderboard & AI Model Benchmarks — September 2026</a></li>

</ul>
</details>

**Tags**: `#AI economics`, `#price index`, `#hedonic pricing`, `#AI inference`, `#measurement`

---

<a id="item-8"></a>
## [Jump‑Diffusion Model Shows LVR Has Non‑Zero Lower Bound as Block Time Shrinks.](https://arxiv.org/abs/2608.30321) ⭐️ 8.0/10

The paper models AMM liquidity‑provider costs using a jump‑diffusion price process and finds that the loss‑versus‑rebalancing (LVR) rate splits into a diffusion term that vanishes with block time and a jump term independent of block time, giving LVR a non‑vanishing lower bound that scales as √Δt. Consequently, even as block time → 0, LVR does not go to zero. The result shows that shortening blocks cannot eliminate the dominant adverse‑selection cost for LPs, shifting the focus of block‑time design to volatility, fee tier, and consensus cost rather than block duration alone. It provides a quantitative bound for the LP‑side contribution to block‑time welfare, informing optimal block‑time selection in DeFi protocols such as Ethereum and Solana. The LVR rate is expressed as F(γ/(σ√Δt)) + λV·G(γ;m,δ²) plus an explicitly bounded remainder; for symmetric jump laws the jump channel λV·G is an exact lower bound, so LVR ≥ λV·G > 0 and decays as √Δt. At Ethereum’s 12‑second slot the LVR rate is 471 bp/yr versus a floor of 125 bp/yr, while at Solana’s 400 ms slot the jump channel already dominates. Optimizing LVR against per‑block consensus cost yields an LP‑side optimal block time of about 8 seconds, independent of pool size and jump parameters (λ,m,δ).

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Automated market makers (AMMs) such as Uniswap allow users to trade against a pooled reserve, and liquidity providers (LPs) earn fees but suffer loss‑versus‑rebalancing (LVR) when arbitrageurs exploit price differences between the AMM and external markets. Under a geometric Brownian motion price model, the probability of a profitable arbitrage block shrinks with block time Δt, making LVR vanish as Δt→ 0, which has motivated the drive toward ever‑shorter blocks. A jump‑diffusion model adds a Poisson‑driven jump component to the price process, representing sudden large price moves that are not smoothed out by shorter blocks.

**Tags**: `#AMM`, `#LVR`, `#blockchain`, `#DeFi`, `#jump-diffusion`

---

<a id="item-9"></a>
## [LLM Multi-Agent Model Simulates Household Expectations Under Tariff Threats](https://arxiv.org/abs/2608.30522) ⭐️ 8.0/10

Researchers created a multi-agent system that turns 300 households from the Michigan Surveys of Consumers into persistent large-language-model agents exposed to social‑media information over several simulated months. Calibrated agents reproduce distributional and demographic patterns from human survey data after the Liberation Day tariff announcement, and experiments show how tariff threats and central‑bank explanations shape inflation and unemployment expectations and their dispersion. The framework provides a disciplined, AI‑driven way to study how policy communication influences household beliefs, bridging computational social science and economics. It offers policymakers and researchers a testbed for evaluating the effects of tariff threats and central‑bank messages before actual policy implementation. Agents were exposed to varied message attributes—immediacy, rate salience, semantic progression, complexity, narrative, and sender identity—which jointly affected expectations and dispersion; open‑ended responses linked these effects to attention, ambiguity, credibility, and causal narratives. A second experiment found that central‑bank explanations can coordinate beliefs, although their impact on average expectations depends on the specific content of the explanation.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: The Michigan Surveys of Consumers regularly measure household expectations of inflation and unemployment, which are key indicators for macroeconomic forecasting. Tariff threats, such as those announced on “Liberation Day,” can shift these expectations even before policies are enacted, but their rapidly changing wording makes them hard to capture with traditional surveys. Multi‑agent systems simulate interacting entities, and large language models enable agents to generate human‑like text responses, allowing researchers to model how information spreads and influences beliefs in a controlled, repeatable environment.

**Tags**: `#multi-agent systems`, `#large language models`, `#economic expectations`, `#policy communication`, `#computational social science`

---

<a id="item-10"></a>
## [Battery storage's growing role in GB balancing mechanism price formation](https://arxiv.org/abs/2608.29818) ⭐️ 8.0/10

The study reconstructs the price-ranked edge of the GB Balancing Mechanism bid/offer stack across 50,684 half‑hourly settlement periods from 2023 to 2025 and attributes marginal price‑setting to individual units. Battery storage’s share rose from 0.8% to 36.2% on the bid side and from 3.2% to 26.9% on the offer side, displacing combined‑cycle gas and pumped storage. The findings show that flexible battery storage is increasingly setting real‑time prices in a renewables‑dominated system, which has direct implications for market design, decarbonisation policies, and the valuation of storage assets. Policymakers and market operators can use this evidence to anticipate how storage will influence balancing costs and price signals as the grid decarbonises. The analysis uses 50,684 half‑hourly periods, finds capacity‑normalised marginal capture increased on both sides, and estimates that each additional 100 MW of BM‑active capacity raises quarterly bid‑ and offer‑side marginal share by 0.55 and 0.48 percentage points, respectively. By 2025 battery actions were about £9–10/MWh more favourable than volume‑matched non‑battery alternatives, yet batteries were under‑represented by 12.9 pp in the highest‑priced 5 % of short‑system periods.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: The GB Balancing Mechanism (BM) is the primary tool used by the National Energy System Operator to match electricity supply and demand in near‑real time, accepting bids and offers from generators and storage assets. The imbalance price (or cash‑out price) is determined from the accepted BM bids and offers and reflects the cost of settling system imbalances each half‑hour. In a system with high renewable generation, flexible technologies such as batteries can become marginal price‑setters when they are the most expensive (or cheapest) unit needed to balance the grid. This study provides unit‑level evidence of how battery storage’s marginal share has evolved in the BM from 2023 to 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://www.neso.energy/what-we-do/systems-operations/what-balancing-mechanism">What is the Balancing Mechanism? | National Energy System Operator</a></li>
<li><a href="https://www.elexon.co.uk/bsc/settlement/imbalance-pricing/">Imbalance Pricing - Elexon BSC</a></li>
<li><a href="https://arxiv.org/abs/2608.29818">[2608.29818] Decarbonising price formation: unit-level evidence on battery storage and the imbalance price in the GB Balancing Mechanism</a></li>

</ul>
</details>

**Tags**: `#energy markets`, `#battery storage`, `#GB Balancing Mechanism`, `#renewables integration`, `#electricity price formation`

---

<a id="item-11"></a>
## [Risk-Adjusted Harm Score and FinRedTeamBench Improve LLM Safety in Financial Services](https://arxiv.org/abs/2603.10807) ⭐️ 8.0/10

The paper introduces RAHS, a risk‑adjusted harm score that captures disclosure severity, disclaimer mitigation, and inter‑judge agreement, and FinRedTeamBench, a 989‑prompt benchmark covering seven BFSI risk areas and 34 sub‑categories mapped to regulatory frameworks. By providing a nuanced, risk‑sensitive metric and a domain‑specific red‑teaming benchmark, the work enables more realistic safety testing of LLMs in regulated finance, helping institutions meet compliance requirements and reduce exposure to legally plausible harms. RAHS combines disclosure severity, disclaimer presence, and agreement among an ensemble of three heterogeneous LLM judges; FinRedTeamBench includes multi‑turn red‑teaming prompts and was validated against human experts, showing stable rankings under hyperparameter sweeps and higher severity disclosures than single‑turn tests.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Large language model safety is often measured by binary attack success rates (ASR) that treat any jailbreak as equal, ignoring the varying harm of disclosed information. In regulated sectors such as banking, financial services, and insurance (BFSI), harmful outputs can arise from seemingly legitimate or professionally framed requests, which generic benchmarks miss. Risk‑adjusted harm scoring refines ASR by weighting disclosures according to their operational severity, presence of mitigating disclaimers, and consensus among multiple LLM judges. FinRedTeamBench provides a curated set of prompts aligned with BFSI regulatory categories to capture these nuanced failure modes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.10807">Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in...</a></li>
<li><a href="https://www.researchgate.net/publication/401833402_Risk-Adjusted_Harm_Scoring_for_Automated_Red_Teaming_for_LLMs_in_Financial_Services">(PDF) Risk - Adjusted Harm Scoring for Automated Red Teaming for...</a></li>
<li><a href="https://www.themoonlight.io/en/review/risk-adjusted-harm-scoring-for-automated-red-teaming-for-llms-in-financial-services">[Literature Review] Risk - Adjusted Harm Scoring for Automated Red...</a></li>

</ul>
</details>

**Tags**: `#LLM safety`, `#red teaming`, `#financial services`, `#risk assessment`, `#benchmark`

---

<a id="item-12"></a>
## [Performance Manipulation in AI-Augmented Labor Markets: Theory and Evidence](https://arxiv.org/abs/2604.22230) ⭐️ 8.0/10

The paper introduces a game‑theoretic model where agents split effort between creative and mechanistic tasks under AI augmentation, showing that performance‑based screening collapses into a pooling equilibrium once AI sufficiently crowds out creative effort. The findings clarify when AI‑augmented labor markets can still rely on observable performance for hiring or promotion, and when such screening becomes misleading, informing policymakers and firms about the design of reward structures and evaluation criteria. The model proves a symmetric monotone pure‑strategy equilibrium exists, shows low‑type agents systematically over‑invest in mechanistic effort while high‑type agents do not, and demonstrates that more skewed reward schedules reduce this manipulation; empirical validation uses a language‑model‑based effort measure on nearly 1,500 Kaggle competition scripts.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Performance manipulation occurs when workers focus on easily measurable, routine tasks to inflate observable outputs without contributing genuine innovation. In AI‑assisted settings, AI augments mechanistic (rule‑based) tasks, making them cheaper and potentially crowding out the scarce, expertise‑complementary creative effort that employers truly value. The paper uses a game‑theoretic framework to analyze effort allocation and shows that when AI capability becomes large enough, the equilibrium shifts to a pooling state where performance scores no longer reveal worker type.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.22230">Performance Manipulation: Labor Market Implications in AI-assisted Era</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pooling_equilibrium">Pooling equilibrium - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2604.22230">On Benchmark Hacking in ML Contests: Modeling , Insights and Design</a></li>

</ul>
</details>

**Tags**: `#AI economics`, `#labor market`, `#game theory`, `#performance manipulation`, `#screening mechanisms`

---

<a id="item-13"></a>
## [Data-Driven Stochastic Optimal Control Model for Intraday Electricity Trading by Renewable Producers](https://arxiv.org/abs/2604.27700) ⭐️ 8.0/10

The authors propose a continuous-time stochastic optimal control framework for intraday electricity trading where renewable generation follows a Jacobi diffusion and prices follow an asymmetric jump-diffusion to capture heavy-tailed behavior. The model incorporates gate closure and energy-based imbalance settlement via state augmentation, and is solved with a monotone IMEX finite-difference scheme; numerical tests on German market data show the strategy outperforms the TWAP benchmark and nears the perfect-foresight benchmark. This framework provides renewable producers with a data‑driven tool to manage price volatility and imbalance risk, potentially increasing profits and facilitating higher renewable penetration in power markets. By linking advanced stochastic modeling with realistic market mechanics, it bridges the gap between theoretical control theory and practical intraday trading operations. The production process uses a bounded Jacobi diffusion, while price dynamics employ an asymmetric jump‑diffusion with season‑dependent jump intensity; path‑dependent imbalance costs are handled by augmenting the state to preserve Markovian structure, leading to a three‑stage dynamic programming solution consisting of two linear Kolmogorov backward equations and a nonlinear Hamilton‑Jacobi‑Bellman partial integro‑differential equation. Efficient solution is achieved via a monotone IMEX finite‑difference scheme with operator splitting, semi‑implicit linearization, and a differential formulation for the jump operator.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Intraday electricity markets allow participants to trade power close to real‑time delivery, helping to correct forecast errors from day‑ahead markets and reduce imbalance penalties. Renewable generation’s dependence on weather creates volatile output and price spikes, motivating the need for sophisticated trading strategies that can hedge against uncertainty. Stochastic optimal control formulates trading as a continuous‑time decision problem where the state evolves according to stochastic differential equations, and the objective is to maximize expected profit. Jacobi diffusions are bounded processes often used to model variables that stay within a fixed range, while asymmetric jump‑diffusions capture the heavy‑tailed, spike‑prone behavior observed in electricity prices.

<details><summary>References</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s00477-024-02849-2">Stochastic modeling with time-inhomogeneous Jacobi diffusions ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0378437113002434">A jump diffusion model for spot electricity prices and market price of risk - ScienceDirect</a></li>
<li><a href="https://www.emissions-euets.com/internal-electricity-market-glossary/1486-intraday-electricity-market">Intraday electricity market - Emissions-EUETS.com</a></li>

</ul>
</details>

**Tags**: `#stochastic optimal control`, `#electricity trading`, `#renewable energy`, `#intraday markets`, `#jump-diffusion`

---

<a id="item-14"></a>
## [Modeling Peer Review vs AI Screening for Journal Stamp Value](https://arxiv.org/abs/2607.13844) ⭐️ 8.0/10

The paper arXiv:2607.13844v3 presents a formal model that compares rejecting unread submissions versus using fast but less accurate AI screening to preserve the value of a journal’s stamp of approval. It shows that the optimal choice depends on the prevalence of high‑quality work and identifies the exact switching point where one strategy outperforms the other. Understanding how peer review and AI screening affect the perceived value of a journal’s stamp helps editors, publishers, and researchers design better evaluation systems as AI tools become more prevalent in academia. The insights also inform reputation‑based incentives for authors and institutions. The model derives a switching threshold based on the fraction of high‑quality submissions; below that threshold rejecting unread papers yields higher stamp value, above it AI screening is preferable. When authors can run the screen themselves, the stamp’s value is set by the cost of passing the screen rather than its detection ability, whereas expert review prevents such gaming.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Peer review is the traditional process where experts evaluate manuscripts to confer a journal’s stamp of approval, signaling quality to readers. When submission volume exceeds reviewer capacity, editors may either reject unread papers or employ faster AI screening tools that approximate review but with lower accuracy. The value of the journal’s stamp depends on the perceived quality of stamped versus unstamped works, influencing authors’ reputations and institutional standing. Reputation systems in scholarly publishing measure and reinforce these signals through metrics such as impact factor, prizes, and community rankings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thesify.ai/blog/ai-tools-academic-peer-review">AI Tools for Academic Peer Review: What They Actually Check ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rankings_of_academic_publishers">Rankings of academic publishers - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#peer review`, `#academic publishing`, `#AI screening`, `#reputation systems`, `#scholarly communication`

---

<a id="item-15"></a>
## [PortBench: A Correlation-Aware Full-Pipeline Benchmark for LLM-Driven Portfolio Management](https://arxiv.org/abs/2605.27887) ⭐️ 8.0/10

The paper introduces PortBench, a benchmark covering six heterogeneous asset classes from 2015 to 2025, comprising a static QA dataset of 6,269 questions and a dynamic five‑stage allocation pipeline, and proposes two novel metrics: a dual‑layer correlation score and CEPS to measure cascading reasoning errors. PortBench fills critical gaps in LLM‑driven portfolio evaluation by incorporating cross‑asset correlations and assessing the full decision pipeline, enabling more realistic stress testing and guiding researchers and practitioners toward better model design. The benchmark includes six asset classes, a static QA set (6,269 questions across seven templates), a dynamic five‑stage pipeline, a dual‑layer correlation score for inter‑class hedging and intra‑class concentration, and CEPS to quantify error propagation; evaluations were run under three stress windows, three risk profiles, and with real‑time testing to reduce pretraining contamination, showing that only 32.5% of 120 LLM evaluations beat equal‑weight Sharpe across four market periods.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Large language models have excelled at many financial tasks, but portfolio management lacks a comprehensive benchmark. Existing tests often focus solely on equities, ignore correlations between different asset classes, and evaluate only isolated components rather than the full pipeline from analysis to allocation. This limits the ability to gauge how well LLMs can construct diversified, risk‑adjusted portfolios under realistic market conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://portbench.github.io/">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>
<li><a href="https://arxiv.org/html/2605.27887">PortBench : A Correlation-Aware, Full-Pipeline Benchmark for...</a></li>
<li><a href="https://www.emergentmind.com/topics/portbench">PortBench : LLM -Driven Portfolio Benchmark</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#portfolio management`, `#benchmark`, `#finance`, `#AI`

---

<a id="item-16"></a>
## [Fund2Persona Framework Builds Financial Advisor Personas from Fund Disclosures](https://arxiv.org/abs/2606.29793) ⭐️ 8.0/10

The paper introduces Fund2Persona, a framework that constructs financial-advisor personas from real-world fund disclosure data and refines them through an actor–scorer–patcher loop, demonstrating superior prediction of portfolio changes and more specific advice than generic LLM advisors. By grounding LLM‑based advisors in actual fund manager expertise, Fund2Persona fills a key gap in personalized financial AI, potentially improving the quality and scalability of automated advisory services. The framework incorporates holdings transitions, market context, and manager commentary, validates personas via active‑delta accuracy and commentary alignment, and evaluates them in market‑scenario generation and multi‑turn investor‑advisor dialogues.

rss · arXiv Quantitative Finance · Sep 1, 04:00

**Background**: Large language models often produce generic financial advice when prompted with simple persona descriptions, lacking the depth of real‑world expertise. Fund disclosure data—such as portfolio holdings, trading activity, and manager narratives—encodes the specific investment reasoning of fund managers. The actor‑scorer‑patcher loop is an iterative scheme where an actor generates advice, a scorer scores its fidelity to the source data, and a patcher updates the persona to reduce errors.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.29793">[2606.29793] Fund2Persona: A Framework for Building and ...</a></li>
<li><a href="https://arxiv.org/html/2606.29793v3">Fund2Persona: A Framework for Building and Refining Financial ...</a></li>

</ul>
</details>

**Tags**: `#AI in Finance`, `#LLM Personas`, `#Fund Disclosure`, `#Personalized Advisory`, `#Actor-Scorer-Patcher`

---