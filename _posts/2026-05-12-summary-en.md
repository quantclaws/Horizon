---
layout: default
title: "Horizon Summary: 2026-05-12 (EN)"
date: 2026-05-12
lang: en
---

> From 38 items, 14 important content pieces were selected

---

1. [: ](#item-1) ⭐️ 9.0/10
2. [: ](#item-2) ⭐️ 9.0/10
3. [: ](#item-3) ⭐️ 8.0/10
4. [:If AI writes your code, why use Python?](#item-4) ⭐️ 8.0/10
5. [Ratty – A terminal emulator with inline 3D graphics](#item-5) ⭐️ 8.0/10
6. [: Google claims criminal hackers used AI to uncover major software flaw](#item-6) ⭐️ 8.0/10
7. [Thinking Machines AI Unveils Real-Time Multimodal Transformer Interaction Model](#item-7) ⭐️ 8.0/10
8. [:James Shore Warns AI Coding Agents Must Cut Maintenance Costs Inversely to Productivity Gains](#item-8) ⭐️ 8.0/10
9. [AI Overload Fuels the Rise of the 'Zombie Internet'](#item-9) ⭐️ 8.0/10
10. [: Stochastic Game-Theoretic Model for Intraday Battery Storage Dispatch Using Riccati Equations](#item-10) ⭐️ 8.0/10
11. [: ](#item-11) ⭐️ 8.0/10
12. [: Study shows first-price auctions boost ad revenue 25‑75% initially.](#item-12) ⭐️ 8.0/10
13. [:Forecasting implied volatility surface with generative diffusion models](#item-13) ⭐️ 8.0/10
14. [:General-Purpose Technology Distorts Standard Bubble Tests, New Decomposition Finds No AI Rally Speculation](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [: ](https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage) ⭐️ 9.0/10

UCLA researchers have identified a drug that promotes brain repair after stroke by restoring connectivity in surviving neural networks.

hackernews · bookofjoe · May 11, 17:53 · [Discussion](https://news.ycombinator.com/item?id=48098261)

**Tags**: `#stroke`, `#neurorehabilitation`, `#drug discovery`, `#neuroscience`, `#brain repair`

---

<a id="item-2"></a>
## [: ](https://nvlabs.github.io/cuda-oxide/index.html) ⭐️ 9.0/10

Nvidia's CUDA-oxide provides an official Rust compiler that targets CUDA PTX, allowing Rust developers to write GPU kernels with better safety and tooling.

hackernews · adamnemecek · May 11, 15:55 · [Discussion](https://news.ycombinator.com/item?id=48096692)

**Tags**: `#Rust`, `#CUDA`, `#GPU programming`, `#Nvidia`, `#compiler`

---

<a id="item-3"></a>
## [: ](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 8.0/10

TanStack's postmortem explains how an npm supply-chain compromise installed a dead-man's switch to exfiltrate GitHub tokens and the challenges faced due to npm's unpublish policy and Trusted Publishing limitations.

hackernews · varunsharma07 · May 11, 21:08 · [Discussion](https://news.ycombinator.com/item?id=48100706)

**Tags**: `#supply-chain security`, `#npm`, `#security incident`, `#postmortem`, `#trusted publishing`

---

<a id="item-4"></a>
## [:If AI writes your code, why use Python?](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055) ⭐️ 8.0/10

The Medium article questions Python's continued relevance in an era where AI models like GitHub Copilot and OpenAI Codex can generate code from natural language prompts. It highlights how language choice can still affect developer productivity, debugging, and trust in AI‑generated code, shaping the adoption of programming languages as AI tools evolve. The article notes that AI models are trained on vast amounts of Python code, giving them an edge in Python generation, while developers value Python for its familiarity, readability, and ease of debugging, even when AI writes the code.

hackernews · indigodaddy · May 11, 20:45 · [Discussion](https://news.ycombinator.com/item?id=48100433)

**Background**: AI code generation tools such as GitHub Copilot and OpenAI Codex are large language models trained on publicly available code repositories, enabling them to suggest or generate code snippets from natural language descriptions. Their performance is strongly influenced by the prevalence of each language in the training data, which can create a bias toward languages like Python that appear frequently. While these tools can produce code in many programming languages, the quality and reliability of the output vary with the amount and diversity of training examples for each target language.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters joked about using constructed languages like Lojban if AI handled communication, while many pointed out that AI’s training data is heavily skewed toward Python, giving it better performance in that language. Several developers said they prefer Python because their long‑term familiarity and debugging confidence let them spot potential issues in AI‑generated code, warning that over‑reliance could lead to ‘vibecoding’ without real understanding.

---

<a id="item-5"></a>
## [Ratty – A terminal emulator with inline 3D graphics](https://ratty-term.org/) ⭐️ 8.0/10

Ratty is a GPU‑rendered terminal emulator that enables developers to render 3D models directly inside the command line using its own Ratty Graphics Protocol. By bringing inline 3D graphics to the terminal, Ratty opens new possibilities for developer workflows, data visualization, and immersive CLI experiences, challenging the traditional text‑only paradigm. Ratty uses the Ratty Graphics Protocol (RGP) to register .obj and .glb assets, supports multiple 3D presentation modes, and features a spinning rat cursor as its UI hallmark.

hackernews · orhunp_ · May 11, 10:13 · [Discussion](https://news.ycombinator.com/item?id=48093100)

**Background**: Traditional terminal emulators display only text and rely on character cells for output. Recent innovations like Kitty and iTerm2 have introduced inline images and graphics protocols to extend terminal capabilities. Ratty builds on this trend by leveraging GPU acceleration and its own graphics protocol to render 3D models directly within the terminal window, drawing inspiration from TempleOS’s graphical approach and being implemented in Rust with the Ratatui library.

<details><summary>References</summary>
<ul>
<li><a href="https://ratty-term.org/">Ratty — A GPU-rendered terminal emulator with inline 3D graphics</a></li>
<li><a href="https://github.com/orhun/ratty">GitHub - orhun/ratty: A GPU-rendered terminal emulator with inline 3D graphics 🐀🧀</a></li>
<li><a href="https://www.theregister.com/software/2026/05/11/ratty-terminal-emulator-brings-3d-graphics-to-the-command-line/5238299">Ratty terminal emulator brings 3D graphics to the command line</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about Ratty’s novelty, with some envisioning VR or shallow‑3D uses for reduced eye strain, while others placed it in a historical lineage of inline graphics dating back to 1980s workstations. Several praised the idea as “gloriously bonkers” and noted its potential for data‑science workflows, but also raised practical concerns about 2D rendering quality and how GPU‑accelerated rendering behaves over SSH.

**Tags**: `#terminal-emulator`, `#3D-graphics`, `#VR`, `#developer-tools`, `#UI-innovation`

---

<a id="item-6"></a>
## [: Google claims criminal hackers used AI to uncover major software flaw](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html) ⭐️ 8.0/10

Google told the New York Times that criminal hackers employed an AI model to discover and weaponize a significant software vulnerability, as detailed in a report released May 11, 2026. The allegation underscores the growing threat of AI‑assisted cyber attacks, showing how attackers can accelerate vulnerability discovery and exploit development. Google’s report states investigators have “high confidence” that the hackers leveraged an AI model, possibly similar to Anthropic’s Mythos or Google’s own Big Sleep and CodeMender agents, to find the flaw.

hackernews · donohoe · May 11, 13:20 · [Discussion](https://news.ycombinator.com/item?id=48094641)

**Background**: Large language models are increasingly applied to software security tasks, such as automated fuzzing and vulnerability discovery, by generating test inputs or analyzing code for weaknesses. Google’s Big Sleep, developed with DeepMind and Project Zero, is an AI agent that actively searches for unknown security flaws, while CodeMender uses Gemini Deep Think models to debug and fix complex vulnerabilities. Researchers have also shown LLMs can drive fuzz driver generation, reducing manual effort in finding bugs. These capabilities, while beneficial for defenders, can also be repurposed by attackers to accelerate exploit development.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access?hl=en">Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access | Google Cloud Blog</a></li>
<li><a href="https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/">Introducing CodeMender: an AI agent for code security — Google DeepMind</a></li>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/defending-enterprise-ai-vulnerabilities/">Defending Your Enterprise When AI Models Can Find Vulnerabilities Faster Than Ever | Google Cloud Blog</a></li>

</ul>
</details>

**Discussion**: Commenters questioned the basis for Google’s “high confidence” claim, wondering what distinguishes an AI‑assisted zero‑day from a traditional one. Others warned that framing AI as a cyber threat could be used to justify restricting open‑weight and local LLMs, echoing past debates over encryption and anonymity tools. A few noted the discussion reflects a broader trend of invoking security to demand user identification online.

**Tags**: `#AI security`, `#cybersecurity`, `#vulnerability discovery`, `#AI-assisted hacking`, `#Google`

---

<a id="item-7"></a>
## [Thinking Machines AI Unveils Real-Time Multimodal Transformer Interaction Model](https://thinkingmachines.ai/blog/interaction-models/) ⭐️ 8.0/10

Thinking Machines AI announced a multimodal transformer interaction model that accepts text, image, and audio inputs and generates text and audio outputs in real time using interleaved 200‑ms micro‑turns. The model’s real‑time, modality‑fusion architecture enables more natural, low‑latency AI assistants and could become a building block for robotics, healthcare, and immersive applications. It processes 200 ms chunks of input and generates 200 ms of output in a continuous loop, using a single transformer trained jointly on text, image, and audio data; demos show the model waiting silently during user pauses.

hackernews · smhx · May 11, 20:53 · [Discussion](https://news.ycombinator.com/item?id=48100524)

**Background**: Multimodal transformer models combine different data types (e.g., text, image, audio) within a single architecture, often using cross‑attention layers to fuse modalities. The interaction model introduces time‑aligned micro‑turns, where short input windows are processed and output generated in an interleaved fashion to achieve low latency. Prior work such as Google’s Multimodal Bottleneck Transformer and recent models like Gemma 3 and Reka Core illustrate the growing trend toward real‑time multimodal AI.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/multimodal-bottleneck-transformer-mbt-a-new-model-for-modality-fusion/">Multimodal Bottleneck Transformer (MBT): A New Model for Modality Fusion</a></li>
<li><a href="https://huggingface.co/blog/gemma3">Welcome Gemma 3: Google's all new multimodal , multilingual, long...</a></li>
<li><a href="https://toolsstackai.com/reka-ai-launches-reka-core-api-multimodal-streaming/">Reka AI Launches Reka Core API With Multimodal ... - Tools Stack AI</a></li>

</ul>
</details>

**Discussion**: Commenters praised the model’s impressive demos and its ability to wait silently during user pauses, highlighting the natural interaction feel. Some questioned the economic model, sought clarification on training data and skill retention, and wondered about practical commercial applications beyond the showcased demos.

**Tags**: `#AI`, `#multimodal`, `#transformer`, `#real-time interaction`, `#research`

---

<a id="item-8"></a>
## [:James Shore Warns AI Coding Agents Must Cut Maintenance Costs Inversely to Productivity Gains](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 8.0/10

On May 11, 2026, software thought leader James Shore published a blog post arguing that AI coding agents must reduce maintenance costs in exact inverse proportion to any productivity gains they provide, otherwise overall burden increases. This insight highlights a hidden trade‑off of AI‑assisted coding: speed gains can be erased or reversed by rising maintenance effort, guiding teams to evaluate AI tools holistically. Shore’s formula states that if code output doubles, maintenance costs must halve; if output triples, maintenance must fall to one‑third, otherwise net maintenance rises proportionally to the productivity gain.

rss · Simon Willison · May 11, 19:48

**Background**: AI coding agents such as GitHub Copilot and CodeGPT accelerate code generation by suggesting snippets and automating repetitive tasks. Software maintenance often accounts for 2‑10 times the initial development cost, making long‑term expenses critical. Therefore, any productivity boost from AI must be offset by a proportional reduction in ongoing maintenance to avoid increasing total cost of ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://www.index.dev/blog/ai-agents-for-coding">5 Best AI Agents for Coding in 2026 [Tried & Tested]</a></li>
<li><a href="https://openreview.net/forum?id=4UeopY7Ogl">FrugalGPT: How to Use Large Language Models While Reducing ...</a></li>
<li><a href="https://cacm.acm.org/research/measuring-productivity-in-the-software-industry/">Measuring Productivity in the Software Industry</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#coding agents`, `#maintenance cost`, `#productivity`

---

<a id="item-9"></a>
## [AI Overload Fuels the Rise of the 'Zombie Internet'](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 8.0/10

Jason Koebler's article, highlighted by Simon Willison on May 11 2026, argues that pervasive AI use online is mentally exhausting and introduces the term 'Zombie Internet' to describe the tangled mix of human and AI interactions. The concept highlights how AI-generated content is altering human writing styles and causing cognitive fatigue, affecting creators, platforms, and everyday users. Koebler describes the Zombie Internet as people talking to bots, AI agents, influencer hustlebros running automated channels, AI‑generated summaries sold as books, and marketing‑firm accounts posing as genuine advice givers.

rss · Simon Willison · May 11, 19:21

**Background**: The Dead Internet theory posits that since around 2016 most online activity is bot‑driven, while the newer ‘Zombie Internet’ concept adds layers of human‑AI interaction. Recent coverage in outlets like The Guardian and Medium explains how AI‑generated slop fuels this phenomenon.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/majordigest/the-rise-of-the-zombie-internet-and-its-impact-c31e2b5190ec">The Rise of the Zombie Internet and Its Impact | by Valentin... | Medium</a></li>
<li><a href="https://www.theguardian.com/technology/article/2024/may/19/spam-junk-slop-the-latest-wave-of-ai-behind-the-zombie-internet">Spam, junk … slop? The latest wave of AI behind the ‘ zombie internet</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#internet culture`, `#media critique`, `#Zombie Internet`, `#human-AI interaction`

---

<a id="item-10"></a>
## [: Stochastic Game-Theoretic Model for Intraday Battery Storage Dispatch Using Riccati Equations](https://arxiv.org/abs/2605.01178) ⭐️ 8.0/10

We develop a stochastic game-theoretic model for intraday dispatch of grid-scale battery energy storage systems, where each operator manages its state-of-charge to maximize arbitrage revenue given an endogenously determined price that depends on aggregate charging rates. The Nash equilibrium of the resulting finite-player linear-quadratic differential game with a shared stochastic driver is characterized via a system of Riccati equations, yielding semi-explicit feedback controls and equilibrium prices. The model provides a quantitative testbed to study how decentralized BESS deployment affects daily price spreads and grid operations, offering insights into market power, coordination benefits, and the marginal impact of additional storage entry. These results are relevant for energy market design, control theory, and the integration of renewable resources. The analysis covers both heterogeneous and homogeneous BESS settings, derives equilibrium strategies through coupled Riccati equations, evaluates the marginal externality of new entrants, quantifies coordination gains, and examines the large-number asymptotic limit. The framework also extends to hybrid-type storage units to capture supply effects.

rss · arXiv Quantitative Finance · May 11, 04:00

**Background**: Grid-scale battery energy storage systems can shift electricity consumption from low-price to high-price periods, earning revenue through energy arbitrage in intraday markets. When many storage operators act simultaneously, their collective charging and discharging decisions influence the market price, creating a strategic interdependence that can be modeled as a linear-quadratic differential game. In such games, each player’s state (state-of-charge) evolves linearly, the cost is quadratic in state and control, and the equilibrium can be obtained by solving associated Riccati equations. This approach yields feedback controls that depend on the current state and captures the dynamic competition among storage providers.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.01178">Modeling Stochastic Multi-Agent Interaction in Intraday Battery ...</a></li>
<li><a href="https://www.researchgate.net/publication/272504766_Linear_Quadratic_Differential_Games_An_Overview">(PDF) Linear Quadratic Differential Games : An Overview</a></li>
<li><a href="https://www.academia.edu/63369723/Algorithms_for_computing_Nash_equilibria_in_deterministic_LQ_games">Algorithms for computing Nash equilibria in deterministic LQ games</a></li>

</ul>
</details>

**Tags**: `#energy storage`, `#game theory`, `#stochastic control`, `#electricity markets`, `#battery dispatch`

---

<a id="item-11"></a>
## [: ](https://arxiv.org/abs/2605.06818) ⭐️ 8.0/10

The authors propose a Bayesian low-rank factor model with dynamic shrinkage priors to estimate time-varying correlation matrices, offering adaptive regularization and proving posterior contraction rates.

rss · arXiv Quantitative Finance · May 11, 04:00

**Tags**: `#Bayesian statistics`, `#time-varying correlation`, `#shrinkage priors`, `#stochastic volatility`, `#posterior contraction`

---

<a id="item-12"></a>
## [: Study shows first-price auctions boost ad revenue 25‑75% initially.](https://arxiv.org/abs/2110.13814) ⭐️ 8.0/10

The study shows that moving from second‑price to first‑price auctions increases publisher revenue per impression by 25‑75%, though the effect fades over time for later adopters.

rss · arXiv Quantitative Finance · May 11, 04:00

**Tags**: `#auction theory`, `#online advertising`, `#first-price auction`, `#second-price auction`, `#difference-in-differences`

---

<a id="item-13"></a>
## [:Forecasting implied volatility surface with generative diffusion models](https://arxiv.org/abs/2511.07571) ⭐️ 8.0/10

The authors introduce a conditioned Denoising Diffusion Probabilistic Model (DDPM) that incorporates a signal-to-noise ratio (SNR)-based arbitrage penalty to forecast one‑day‑ahead arbitrage‑free implied volatility surfaces from historical market data. Generating arbitrage‑free volatility surfaces is crucial for accurate derivatives pricing and risk management; this work shows that diffusion models can outperform prior GAN‑based methods, offering a more stable and financially consistent forecasting tool. The model conditions on exponentially weighted moving averages of past volatility surfaces, asset returns, squared returns, and scalar risk indicators, and uses a parameter‑free SNR weighting scheme to dynamically adjust the arbitrage penalty throughout the diffusion process; numerical experiments demonstrate superior forecasting performance.

rss · arXiv Quantitative Finance · May 11, 04:00

**Background**: Implied volatility surfaces represent market expectations of future volatility across strikes and maturities, but they must satisfy arbitrage‑free constraints such as calendar spread and butterfly conditions to avoid mispricing. Denoising Diffusion Probabilistic Models (DDPMs) generate data by iteratively denoising noise, and have been applied to volatility forecasting, yet ensuring arbitrage‑freeness remains challenging. Prior work often relied on GANs, which can be unstable and may produce surfaces violating arbitrage constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.07571">Forecasting implied volatility surface with generative diffusion models</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5740265">Forecasting Implied Volatility Surface with Generative Diffusion ...</a></li>
<li><a href="https://diamhomes.ewi.tudelft.nl/~kvuik/numanal/ma_afst.pdf">Diffusion probabilistic model for implied volatility surface generation...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#diffusion models`, `#implied volatility`, `#quantitative finance`, `#arbitrage-free`

---

<a id="item-14"></a>
## [:General-Purpose Technology Distorts Standard Bubble Tests, New Decomposition Finds No AI Rally Speculation](https://arxiv.org/abs/2604.25826) ⭐️ 8.0/10

The paper (arXiv:2604.25826v2) shows that standard bubble tests suffer size distortion when fundamentals include general-purpose technology shocks; it proposes a fundamental-versus-speculative decomposition that projects prices onto observable technology proxies and applies the test to the residual. After adjustment, the 2020‑2025 AI rally shows no evidence of speculation, while the dot‑com bubble retains a speculative peak confined to December 1999–March 2000. The corrected bubble test reduces false positives caused by technology‑driven price explosions, providing a more reliable tool for investors, regulators, and researchers to identify genuine speculative episodes. Its application to the recent AI investment surge and the historic dot‑com episode demonstrates broad relevance to finance, econometrics, and technology‑policy analysis. The authors embed a hump‑shaped general‑purpose technology shock into the Campbell‑Shiller present‑value model, proving that the fundamental price becomes locally explosive during adoption, which introduces a non‑centrality parameter proportional to the shock’s peak into the test’s limit distribution. By projecting asset prices onto observable technology proxies and testing the residuals, the decomposition isolates speculative components; empirically it removes speculation signals from the 2020‑2025 AI rally while confirming a dot‑com speculative peak limited to Dec 1999‑Mar 2000.

rss · arXiv Quantitative Finance · May 11, 04:00

**Background**: Bubble tests, such as those based on the Campbell‑Shiller present‑value model, assess whether asset prices contain explosive components beyond fundamentals. General‑purpose technology (GPT) shocks—widespread innovations like AI that affect many sectors—can cause fundamentals to exhibit temporary explosive behavior, thereby distorting standard bubble tests. The paper’s decomposition separates the price into a fundamental part driven by observable GPT proxies and a residual speculative part, allowing a clean test of speculation.

<details><summary>References</summary>
<ul>
<li><a href="https://ideas.repec.org/p/arx/papers/2604.25826.html">General-Purpose Technology and Speculative Bubble Detection</a></li>
<li><a href="https://www.academia.edu/130318911/Technology_Shocks_Technological_Collaboration_and_Innovation_Outcomes">(PDF) Technology Shocks , Technological Collaboration, and...</a></li>

</ul>
</details>

**Tags**: `#finance`, `#bubble detection`, `#general purpose technology`, `#AI rally`, `#econometrics`

---