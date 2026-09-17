---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
lang: en
---

> From 31 items, 8 important content pieces were selected

---

1. [Nvidia Announces Native CUDA Rust Support for GPU Kernels](#item-1) ⭐️ 8.0/10
2. [Researchers Break 1.58-bit Barrier for Ternary LLMs Using Weight Sparsity](#item-2) ⭐️ 8.0/10
3. [Backups Aren't Simple](#item-3) ⭐️ 8.0/10
4. [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](#item-4) ⭐️ 8.0/10
5. [AI Outperforms Statistics but Costs More; Gains vs Scientific Computing Since 2020](#item-5) ⭐️ 8.0/10
6. [Diffusion Models Generate Dynamic Volatility Surfaces for Improved Hedging](#item-6) ⭐️ 8.0/10
7. [Exploring hydrogen pipeline costs by considering regional geographical and political characteristics](#item-7) ⭐️ 8.0/10
8. [Strategic Manipulation of Grid Constraints by Energy Storage Aggregator](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Nvidia Announces Native CUDA Rust Support for GPU Kernels](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia introduced CUDA Rust, a feature that lets developers write GPU kernels directly in the Rust programming language, compiling them to PTX without needing another language. This development brings the safety and modern abstractions of Rust to GPU programming, potentially reducing bugs and vendor lock‑in while broadening Rust’s reach in high‑performance computing. CUDA Rust offers two programming tracks—SIMT (like traditional CUDA C++) and Tile (a newer model)—and compiles standard Rust code directly to PTX via the cuda‑oxide compiler, without DSLs or foreign language bindings.

hackernews · nonmaskable · Sep 16, 11:15 · [Discussion](https://news.ycombinator.com/item?id=49724881)

**Background**: CUDA is Nvidia’s parallel computing platform and programming model for writing GPU kernels, traditionally done in C++ or other languages. GPU kernels are small programs that run many threads in parallel on the graphics processor. PTX is an intermediate assembly‑like language that Nvidia’s GPU driver compiles to binary machine code. Rust is a systems language known for memory safety and zero‑cost abstractions.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/">Introducing CUDA Rust: Two Tracks for Writing GPU Kernels | NVIDIA Technical Blog</a></li>
<li><a href="https://github.com/NVlabs/cuda-oxide">GitHub - NVlabs/cuda-oxide: cuda-oxide is a Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust.</a></li>
<li><a href="https://developer.nvidia.com/blog/translating-cuda-tile-operations-from-python-to-rust-using-agentic-ai/">Translating CUDA Tile Operations from Python to Rust Using Agentic AI</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed feelings: some criticized CUDA’s vendor lock‑in and advocated for separate‑file kernels or DSLs like Triton, while others welcomed the Rust integration, noting HuggingFace’s Candle crate. A few remarked on the blog’s tone, asked about alternatives such as Vectorware, and viewed Nvidia’s move as part of a strategy to keep the AI ecosystem tied to its hardware.

**Tags**: `#CUDA`, `#Rust`, `#GPU programming`, `#Nvidia`, `#systems programming`

---

<a id="item-2"></a>
## [Researchers Break 1.58-bit Barrier for Ternary LLMs Using Weight Sparsity](https://arxiv.org/abs/2609.16338) ⭐️ 8.0/10

Researchers have surpassed the theoretical 1.58‑bit limit for ternary large language models by exploiting weight sparsity, achieving an average of 1.48 bits per weight. This advancement reduces memory and compute requirements for LLMs, making on‑device and edge deployment more feasible and potentially lowering energy consumption. The method leverages the observation that roughly 51% of weights are near zero, allowing them to be pruned and encoded more efficiently than the standard ternary {-1,0,+1} representation.

hackernews · matt_d · Sep 16, 20:59 · [Discussion](https://news.ycombinator.com/item?id=49732931)

**Background**: Ternary neural networks restrict weights to three discrete values (−1, 0, +1), which theoretically limits storage to log2(3) ≈ 1.58 bits per weight. Weight sparsity refers to setting a fraction of model parameters to zero via pruning, reducing redundancy and memory footprint. Measuring bits per weight quantifies how many bits are needed on average to store each weight after compression, with lower values indicating greater efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.activeloop.ai/resources/glossary/ternary-neural-networks/">What is Ternary Neural Networks? | Activeloop Glossary</a></li>
<li><a href="https://wisegen.medium.com/less-is-more-unlocking-efficiency-in-large-language-models-with-sparsity-802549b4fd66">Less is More: Unlocking Efficiency in Large Language Models with...</a></li>
<li><a href="https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters/">Model Quantization: Concepts, Methods, and Why It Matters | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the improvement stems from the high prevalence of near‑zero weights (~51%), which allows further compression beyond the ternary limit. Some questioned whether the gains translate to actual memory usage, while others highlighted the potential for ASIC‑optimized, low‑power edge inference. A few expressed skepticism, arguing that other quantization methods may be more effective in this range.

**Tags**: `#machine learning`, `#model quantization`, `#ternary neural networks`, `#LLM compression`, `#edge AI`

---

<a id="item-3"></a>
## [Backups Aren't Simple](https://filipovski.net/2026/09/16/backups-arent-simple.html) ⭐️ 8.0/10

The article explains that backups are more complex than they seem, using real‑world loss stories to illustrate pitfalls and offering advice on robust backup strategies. It highlights that effective data protection requires more than copying files, affecting anyone responsible for data integrity and reinforcing industry best practices such as the 3‑2‑1 rule and a restoration‑focused mindset. The piece cites personal anecdotes (lightning strike, OneDrive term changes), references Veritas/Backup Exec and jwz’s backup guide, and describes a user’s plan to use Restic + Backrest on CoreOS for container volume backups.

hackernews · afilipovski · Sep 16, 20:27 · [Discussion](https://news.ycombinator.com/item?id=49732513)

**Discussion**: Commenters share personal data loss experiences, stress that backups must enable restoration, share useful links such as jwz’s backup guide, and discuss implementing Restic+Backrest on CoreOS, reflecting broad agreement that effective backup strategies require careful design.

**Tags**: `#backups`, `#data protection`, `#system administration`, `#best practices`, `#HN discussion`

---

<a id="item-4"></a>
## [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) ⭐️ 8.0/10

The paper introduces Dream-RSI, a framework that combines evolving world models with multiple agents to enable recursive self‑improvement in reinforcement learning via a lightweight orchestration layer that makes exploration explicit and programmable. Dream-RSI advances the goal of continual self‑improvement in AI, offering a concrete path toward more autonomous agents while also highlighting safety and controllability challenges that must be addressed. The framework builds on Danijar Hafner’s Dreamer world model, adds a replay simulator for off‑policy evaluation, and coordinates multiple agents that each undergo limited refinement steps before sharing improvements.

hackernews · bananaflag · Sep 16, 13:44 · [Discussion](https://news.ycombinator.com/item?id=49726955)

**Background**: Recursive self‑improvement (RSI) refers to a system’s ability to improve its own learning or reasoning capabilities repeatedly, a concept central to theories of artificial general intelligence. World models are learned predictive models of an environment that allow agents to plan and act without interacting directly with the real world; Dreamer is a prominent algorithm that learns such models from raw visual inputs and uses them for model‑based reinforcement learning. By combining evolving world models with multiple agents and an orchestration layer, Dream‑RSI aims to make exploration more efficient and enable continual self‑improvement loops.

<details><summary>References</summary>
<ul>
<li><a href="https://dream-rsi.com/">Dream-RSI: Recursive Self-Improvement through Evolving Worlds</a></li>
<li><a href="https://arxiv.org/abs/2609.14858">[2609.14858] Dream-RSI: Recursive Self-Improvement through ...</a></li>
<li><a href="https://worldmodels.github.io/">World Models</a></li>

</ul>
</details>

**Discussion**: Commenters praised the technical novelty, noting the clever replay simulator and connection to Dreamer, while some questioned whether the work truly constitutes recursive self‑improvement and raised safety concerns about uncontrolled self‑improvement loops.

**Tags**: `#recursive self-improvement`, `#reinforcement learning`, `#world models`, `#Dreamer`, `#AI safety`

---

<a id="item-5"></a>
## [AI Outperforms Statistics but Costs More; Gains vs Scientific Computing Since 2020](https://arxiv.org/abs/2609.16258) ⭐️ 8.0/10

The study analyzed 2,507 head-to-head comparisons of AI versus traditional statistics and scientific computing across 27 disciplines from 2000 to early 2025, finding AI often outperforms statistics but at significantly higher computational cost, while its performance against scientific computing has improved since 2020 and now exceeds half of comparisons. Providing empirical evidence on where AI excels and where it falls short, the work helps researchers choose appropriate methods based on performance and cost tradeoffs, guiding efficient resource allocation in interdisciplinary science. AI outperforms traditional statistics in many cases but incurs significantly higher computational cost; about 25% of comparisons show AI both more expensive and worse than statistics, a proportion stable over the past decade. Against scientific computing, AI previously underperformed but since 2020 now outperforms in more than half of the comparisons.

rss · arXiv Quantitative Finance · Sep 16, 04:00

**Background**: Artificial intelligence is increasingly promoted as a general-purpose scientific method capable of tasks ranging from data analysis to simulation. Traditional statistics encompasses techniques such as regression, hypothesis testing, and probabilistic modeling, while scientific computing involves numerical solutions of differential equations, simulations, and high-performance computing. Evaluating AI against these baselines requires measuring both predictive accuracy and computational resources like runtime or energy consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/389078797_A_Comparative_Study_of_Traditional_Statistical_Methods_and_Machine_Learning_Techniques_for_Improved_Predictive_Models">A Comparative Study of Traditional Statistical Methods and ...</a></li>
<li><a href="https://epoch.ai/benchmarks">AI Benchmarks & Capabilities | Epoch AI</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/resources/mlperf-benchmarks/">NVIDIA: MLPerf AI Benchmarks</a></li>

</ul>
</details>

**Tags**: `#AI`, `#scientific methods`, `#statistics`, `#computational cost`, `#interdisciplinary research`

---

<a id="item-6"></a>
## [Diffusion Models Generate Dynamic Volatility Surfaces for Improved Hedging](https://arxiv.org/abs/2609.13402) ⭐️ 8.0/10

The authors introduce AD-Seq-Vol and AD-Seq-Vol-FT, two diffusion models that jointly learn the evolution of asset returns and high-dimensional implied-volatility surfaces to generate coherent dynamic scenarios and improve data-driven hedging, showing reduced arbitrage violations versus training data and GAN baselines. This work presents a novel diffusion‑model framework for dynamic implied‑volatility surface generation and evaluates its economic utility through data‑driven hedging, demonstrating superior performance over GAN‑based methods and near‑elimination of static‑arbitrage violations, which advances market‑consistent scenario generation in quantitative finance. Using daily SPX option data from 2000 to 2023, AD-Seq-Vol learns the conditional evolution of returns and the volatility surface, while AD-Seq-Vol-FT adds post‑training penalties for static no‑arbitrage violations, reducing them to nearly zero; the resulting diffusion‑based hedges achieve near‑zero tracking error, substantially lower tail risk, and remain stable during the COVID‑19 market turmoil.

rss · arXiv Quantitative Finance · Sep 16, 04:00

**Background**: Diffusion models are generative models that iteratively denoise data to produce high‑quality samples, increasingly applied to financial time series. An implied‑volatility surface represents option implied volatilities across strikes and maturities and must satisfy static no‑arbitrage constraints to avoid risk‑free profit opportunities. Data‑driven hedging uses historical market data to construct hedge portfolios without relying on parametric pricing models, often leveraging generative models to simulate future market scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.13402">[2609.13402] Diffusion models for dynamic volatility surface generation and data-driven hedging</a></li>
<li><a href="https://arxiv.org/html/2609.13402">Diffusion models for dynamic volatility surface generation and data-driven hedging</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#volatility surface`, `#data-driven hedging`, `#machine learning`, `#quantitative finance`

---

<a id="item-7"></a>
## [Exploring hydrogen pipeline costs by considering regional geographical and political characteristics](https://arxiv.org/abs/2505.01124) ⭐️ 8.0/10

The study presents a geographic information system (GIS) model that incorporates regional land use, topography, existing infrastructure, and country-specific weighted average cost of capital to estimate hydrogen pipeline transportation costs, revealing that costs can vary up to threefold compared with uniform cost approaches. By providing more realistic cost estimates, the work improves the economic assessment of hydrogen infrastructure, influencing energy system models, trade flow predictions, and investment decisions for hydrogen as a clean energy carrier. The GIS-based analysis covers 4,900 potential global pipeline routes and shows that the regional levelized cost of transportation can differ by a factor of up to three; it also demonstrates substantial deviations in trade flows when compared with conventional uniform detour factor methods within a European energy system analysis framework.

rss · arXiv Quantitative Finance · Sep 16, 04:00

**Background**: Hydrogen is increasingly seen as a key future energy carrier, and pipelines are a primary means of transporting it over long distances. Current cost estimates often rely on uniform assumptions that ignore local geographical and political-economic conditions, which can lead to inaccurate assessments. Incorporating factors such as land use, topography, existing infrastructure, and country-specific cost of capital via GIS allows for a more spatially resolved and realistic cost evaluation.

**Tags**: `#hydrogen`, `#pipeline cost`, `#geographic information systems`, `#energy systems`, `#techno-economic analysis`

---

<a id="item-8"></a>
## [Strategic Manipulation of Grid Constraints by Energy Storage Aggregator](https://arxiv.org/abs/2609.15755) ⭐️ 8.0/10

The paper models a monopolistic energy storage aggregator's participation in a day-ahead electricity market as a Stackelberg game, using constraint-binding-pattern decomposition to characterize equilibrium and show how inducing or avoiding specific network constraints can raise the aggregator's profit while affecting social welfare. By linking strategic behavior to constraint patterns, the work offers a new methodological tool for analyzing market power in network‑constrained electricity markets and reveals that certain FTR holdings can overturn the usual welfare‑improving effect of storage, potentially lowering welfare below the no‑storage baseline. The framework derives the Stackelberg equilibrium via decomposition of the market‑clearing problem into constraint‑binding patterns, quantifies profit gains from strategic pattern induction or avoidance, and proposes two system‑operator mechanisms to curb undesirable ESA behavior and its welfare impacts.

rss · arXiv Quantitative Finance · Sep 16, 04:00

**Background**: A Stackelberg game models a leader‑follower interaction where the leader (the energy storage aggregator) anticipates the follower’s (system operator’s) response. Energy storage aggregators coordinate distributed storage units and may hold financial transmission rights (FTRs), which are contracts that pay holders for congestion‑related price differences between grid nodes. Network‑constrained economic dispatch determines generation, load, nodal prices and FTR payoffs while respecting transmission limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/400104022_The_Biddings_of_Energy_Storage_in_Multi-Microgrid_Market_Based_on_Stackelberg_Game_Theory">(PDF) The Biddings of Energy Storage in Multi-Microgrid Market...</a></li>
<li><a href="https://arxiv.org/pdf/2609.15755">Storage-Based Strategic Manipulation of Constraint - Binding Patterns ...</a></li>
<li><a href="https://diversegy.com/financial-transmission-rights/">Financial Transmission Rights in Power Markets | Diversegy</a></li>

</ul>
</details>

**Tags**: `#power systems`, `#energy markets`, `#game theory`, `#energy storage`, `#constraint analysis`

---