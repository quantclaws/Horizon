---
layout: default
title: "Horizon Summary: 2026-08-04 (EN)"
date: 2026-08-04
lang: en
---

> From 48 items, 13 important content pieces were selected

---

1. [Optuna 5.0.0-rc1 Released with New Multivariate TPE Default Sampler](#item-1) ⭐️ 8.0/10
2. [LLMs reward expertise](#item-2) ⭐️ 8.0/10
3. [OpenAI Highlights Ten Recent Advances in Math and Theoretical CS](#item-3) ⭐️ 8.0/10
4. [Devtools Must Be Open Source: LLMs Enable End‑User Customization](#item-4) ⭐️ 8.0/10
5. [Cloudflare scales Kimi and GLM models with KV cache quantization](#item-5) ⭐️ 8.0/10
6. [ComfyUI Adds Day‑0 Support for MiniMax H3 Open‑Weights 2K Video Model](#item-6) ⭐️ 8.0/10
7. [Andy Pavlo joins ClickHouse to establish ClickHouse Labs.](#item-7) ⭐️ 8.0/10
8. [Pandoc Celebrates 20 Years of Document Conversion Excellence](#item-8) ⭐️ 8.0/10
9. [Study finds India's latrine subsidy raises river fecal contamination by 72%](#item-9) ⭐️ 8.0/10
10. [Paper analyzes AI supply-chain chokepoints and industrial policy impact.](#item-10) ⭐️ 8.0/10
11. [Policy Iteration Scheme for Semilinear Stochastic HJB Equations with Exponential Convergence](#item-11) ⭐️ 8.0/10
12. [Wrong and More Confident: LLMs on Graduate Economics Exam](#item-12) ⭐️ 8.0/10
13. [Unified Continuous-Time Q-Learning for Mean-Field Games and Control](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Optuna 5.0.0-rc1 Released with New Multivariate TPE Default Sampler](https://github.com/optuna/optuna/releases/tag/v5.0.0-rc1) ⭐️ 8.0/10

Optuna 5.0.0-rc1 makes multivariate TPE with a constant liar strategy the default sampler for single-objective optimization and adopts multi-objective TPE as the default for multi-objective tasks, replacing NSGA-II. It also introduces Conditional PED-ANOVA as the default hyperparameter importance algorithm and adds new APIs for constrained optimization. These changes bring state-of-the-art Bayesian optimization techniques to Optuna’s defaults, improving efficiency and scalability for high-dimensional and conditional hyperparameter searches. Practitioners will benefit from better out-of-the-box performance without needing to manually tune samplers. The multivariate TPE incorporates Watanabe 2023’s enhanced bandwidth computation and uses a constant liar strategy; multi-objective TPE replaces NSGA-II as the default multi-objective sampler; Conditional PED-ANOVA from the KDD 2026 paper becomes the default importance evaluator. Breaking changes include removal of the optuna.multi_objective module and deprecation of the constraints_func argument.

github · c-bata · Aug 3, 05:30

**Background**: Optuna is an open-source hyperparameter optimization framework that uses Tree-structured Parzen Estimator (TPE) as its default sampler for single-objective tasks. For multi-objective optimization, it previously relied on NSGA-II by default, though a multi-objective variant of TPE (MOTPE) has been available. Hyperparameter importance methods like PED-ANOVA help users understand which parameters affect the objective most, especially in conditional or hierarchical search spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/optuna/multivariate-tpe-makes-optuna-even-more-powerful-63c4bfbaebe2">“ Multivariate ” TPE Makes Optuna Even More Powerful | Medium</a></li>
<li><a href="https://arxiv.org/pdf/2304.11127">Tree-Structured Parzen Estimator: Understanding Its Algorithm ...</a></li>
<li><a href="https://medium.com/optuna/significant-speed-up-of-multi-objective-tpesampler-in-optuna-v4-0-0-2bacdcd1d99b">Significant Speed Up of Multi-Objective TPESampler in Optuna v4.0.0 | by Shuhei Watanabe | Optuna | Medium</a></li>

</ul>
</details>

**Tags**: `#optuna`, `#hyperparameter optimization`, `#TPE`, `#multi-objective optimization`, `#software release`

---

<a id="item-2"></a>
## [LLMs reward expertise](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 8.0/10

The article argues that large language models amplify the abilities of users who already possess domain expertise, rather than replacing skill. This highlights that expertise remains crucial in AI-assisted work, affecting how developers and professionals should approach LLMs and skill development. It notes that effective prompting requires understanding of the model’s behavior and that users with deeper domain knowledge craft better prompts, leading to superior outputs.

hackernews · MaxMussio · Aug 3, 21:13 · [Discussion](https://news.ycombinator.com/item?id=49161518)

**Background**: Large language models (LLMs) generate text based on patterns learned from vast datasets, and their outputs heavily depend on the quality of input prompts. Prompt engineering is the practice of designing prompts to guide LLMs toward desired results, involving techniques such as few-shot and chain-of-thought prompting. The article suggests that users who already understand a domain can better leverage these techniques, making LLMs an amplifier of existing expertise.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_engineering">Prompt engineering</a></li>
<li><a href="https://www.promptingguide.ai/">Prompt Engineering Guide | Prompt Engineering Guide</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that LLMs act as a mirror of the user’s expertise, noting that effective use requires familiarity with specific codebases and careful prompting, while some warn against confirmation bias and overreliance on the model.

**Tags**: `#LLMs`, `#AI`, `#software development`, `#prompt engineering`, `#expertise`

---

<a id="item-3"></a>
## [OpenAI Highlights Ten Recent Advances in Math and Theoretical CS](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 8.0/10

OpenAI published an article outlining ten recent advances in mathematics and theoretical computer science, emphasizing AI-driven progress such as language‑model‑assisted theorem proving and open problems. These advances illustrate how AI is reshaping mathematical research, potentially accelerating proof discovery and influencing fields like cryptography and algorithm design. The article cites developments such as AI‑driven formal theorem proving in Lean, neural‑symbolic integration for math reasoning, and OpenAI’s GPT‑f model for automated conjecture generation.

hackernews · milkshakes · Aug 3, 16:27 · [Discussion](https://news.ycombinator.com/item?id=49157930)

**Background**: Recent work shows that large language models can assist formal theorem provers like Lean by generating proof steps and checking correctness, as explored in the Lean Ecosystem initiative. Neural‑symbolic approaches combine symbolic reasoning with deep learning to improve mathematical reasoning, a technique described in surveys of neuro‑symbolic AI. Additionally, models such as OpenAI’s GPT‑f have been used to automatically generate conjectures, expanding the scope of AI‑driven discovery in mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuro-symbolic_AI">Neuro-symbolic AI - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2404.09939v1">A Survey on Deep Learning for Theorem Proving</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about AI’s exponential progress in math while questioning what aspects of human creativity might remain untouched, noted the post’s unusual promotion on Hacker News, and discussed practical implications such as impacts on post‑quantum cryptography and the role of models in disproving conjectures.

**Tags**: `#mathematics`, `#theoretical computer science`, `#AI`, `#research advances`, `#OpenAI`

---

<a id="item-4"></a>
## [Devtools Must Be Open Source: LLMs Enable End‑User Customization](https://blog.exe.dev/devtools-must-be-open-source) ⭐️ 8.0/10

The blog post argues that all developer tools should be open source and claims that large language models now make it practical for end‑users to inspect, modify, and rebuild those tools themselves. If developer tools become open source and LLM‑assisted customization spreads, it could lower barriers to tool adaptation, foster innovation, and shift the economics of software tooling toward more user‑driven development. Commenters note that while open source gives freedom to modify code, most users rely on others to do so. They debate whether LLMs rebuilding tools on each change is efficient, reliable, or hypocritical given the author's own use of closed‑source services.

hackernews · bryanmikaelian · Aug 3, 14:15 · [Discussion](https://news.ycombinator.com/item?id=49156111)

**Background**: Developer tools are software applications such as editors, compilers, and debuggers that programmers use to create and maintain other software. Open source means the source code is publicly available, allowing anyone to study, modify, and redistribute it. Large language models (LLMs) are AI systems trained on massive text corpora that can generate or transform code when prompted. By interpreting natural‑language instructions, LLMs can potentially automate the process of fetching source code, applying changes, and rebuilding tools, making end‑user customization more feasible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree that developer tools should be open source, but they disagree on the practicality of using LLMs to constantly rebuild tools for minor changes, citing inefficiency and reliability worries. Some point out the irony that the author promotes open‑source ideals while relying on many closed‑source services, and others warn that automated nightly updates could break workflows.

**Tags**: `#open-source`, `#developer-tools`, `#LLMs`, `#software-engineering`, `#hackernews`

---

<a id="item-5"></a>
## [Cloudflare scales Kimi and GLM models with KV cache quantization](https://blog.cloudflare.com/smaller-faster-safer-models/) ⭐️ 8.0/10

Cloudflare published a blog detailing how they deploy the Kimi and GLM large language models at scale using KV cache quantization techniques to achieve smaller, faster, and safer AI inference. This demonstrates practical LLM optimization strategies that can reduce latency and cost for developers using AI APIs, while highlighting trade-offs in model quality. They applied FP8 quantization to the key-value cache, focusing tests on Kimi K2.6, and noted that KV quantization can degrade output quality more than weight quantization.

hackernews · ascorbic · Aug 3, 17:08 · [Discussion](https://news.ycombinator.com/item?id=49158581)

**Background**: Kimi is a series of long-context large language models developed by Moonshot AI, accessible via the Kimi API platform. GLM (General Language Model) is an open-weight LLM series from Z.ai, first released as ChatGLM in 2023. KV cache quantization reduces memory bandwidth and compute by storing key and value activations in lower precision, a technique explored in works like KVQuant.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/models">Model List - Kimi API Platform</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2401.18079">[2401.18079] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization</a></li>

</ul>
</details>

**Discussion**: Commenters raised privacy and transparency concerns, asked for more detailed evaluation across model families and clearer pricing, while some suggested alternative quantization formats like NF4 and inquired about hiring needs.

**Tags**: `#LLM inference`, `#model quantization`, `#Cloudflare`, `#AI optimization`, `#KV cache`

---

<a id="item-6"></a>
## [ComfyUI Adds Day‑0 Support for MiniMax H3 Open‑Weights 2K Video Model](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 8.0/10

ComfyUI now includes native support for the newly released MiniMax H3 model, providing open‑weights, multimodal input, native stereo audio and generation of up to 15‑second 2K video clips. This integration brings high‑fidelity video synthesis to consumer GPUs, lowering the barrier for creators to produce professional‑grade audiovisual content locally. The model’s modulation weights (~40% of parameters) can be replaced by a lookup table, cutting memory use by ~66% (from 123.6 GB to 42.5 GB) and enabling 2K generation on an RTX 3060 via dynamic VRAM offloading; user reports show ~10 minutes for a 10‑second 480p clip on an RTX 4070 Ti Super.

hackernews · vblanco · Aug 3, 13:34 · [Discussion](https://news.ycombinator.com/item?id=49155629)

**Background**: ComfyUI is an open‑source, node‑based interface that lets users build and run generative AI workflows for images, video, 3D and audio using diffusion models. MiniMax H3 is a recently released open‑weights general‑purpose multimodal model that accepts text, image, video and audio as joint context and outputs coherent audiovisual video clips, including native stereo audio and up to 2K resolution. The model is designed to run on consumer hardware when optimized with techniques such as weight pruning and VRAM offloading.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video Model | fal</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>

</ul>
</details>

**Discussion**: Commenters noted that pruning ~40% of modulation weights into a lookup table can cut memory by two‑thirds with no quality loss, and reported that a 10‑second 480p clip takes about ten minutes on an RTX 4070 Ti Super. They praised the model’s mouse rendering and overall quality but pointed out occasional AI‑smooth artifacts and instability with unusual prompts, suggesting a hybrid workflow with traditional close‑up rendering.

**Tags**: `#generative-video`, `#AI-models`, `#ComfyUI`, `#open-weights`, `#video-synthesis`

---

<a id="item-7"></a>
## [Andy Pavlo joins ClickHouse to establish ClickHouse Labs.](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 8.0/10

Andy Pavlo, a renowned database researcher from Carnegie Mellon University, has joined ClickHouse as Vice President of Database Research to establish ClickHouse Labs, a new research organization focused on foundational database and data architecture work. This move signals ClickHouse's commitment to long-term, fundamental database research beyond immediate product cycles, potentially advancing OLAP performance and benefiting the broader data infrastructure ecosystem. ClickHouse Labs will conduct research on query processing, systems performance, and infrastructure for both ClickHouse and PostgreSQL, aiming to become a best‑in‑class industry research organization.

hackernews · nikolay_sivko · Aug 3, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49156011)

**Background**: ClickHouse is an open‑source column‑oriented OLAP database management system that stores data in columns to enable fast analytical queries. Andy Pavlo is a professor at Carnegie Mellon University known for his database systems course, research on adaptive indexing, OLTP, and his popular lecture series. Corporate research labs like ClickHouse Labs aim to bridge academic insights with industrial development, focusing on long‑term technical challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://clickhouse.com/docs/en/faq/general/columnar-database">What is a columnar database ? | ClickHouse Docs</a></li>
<li><a href="https://clickhouse.com/blog/andy-pavlo-founding-clickhouse-labs">ClickHouse launches ClickHouse Labs with Andy Pavlo as VP of Database Research | ClickHouse</a></li>
<li><a href="https://www.businesswire.com/news/home/20260803890510/en/ClickHouse-Launches-ClickHouse-Labs-With-Andy-Pavlo-as-VP-of-Database-Research">ClickHouse Launches ClickHouse Labs With Andy Pavlo as VP of Database Research</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the move, praising Pavlo’s teaching and expressing hope that his lectures would continue in a sponsored format. Some urged ClickHouse to fund academic DB research and wondered about the impact of decoupled compute/storage trends (e.g., Trino, Iceberg) on ingestion and indexing.

**Tags**: `#databases`, `#ClickHouse`, `#research`, `#Andy Pavlo`, `#OLAP`

---

<a id="item-8"></a>
## [Pandoc Celebrates 20 Years of Document Conversion Excellence](https://pandoc.org/twenty-years-of-pandoc.html) ⭐️ 8.0/10

The Pandoc project marked its 20th anniversary with a retrospective highlighting its modular N×M reader‑writer architecture, broad adoption across academia and industry, and enduring utility as a document conversion tool. As a free‑software converter that bridges dozens of markup formats, Pandoc underpins countless scholarly publishing workflows and demonstrates how a well‑designed open‑source tool can remain relevant for two decades. Its design separates N parsers (readers) from M writers, enabling N×M conversions; it supports Lua and JSON filters that manipulate the intermediate AST, and can produce clean HTML, LaTeX or Markdown output.

hackernews · fiddlosopher · Aug 3, 15:04 · [Discussion](https://news.ycombinator.com/item?id=49156750)

**Background**: Pandoc is a free, open‑source document converter written in Haskell that can read one markup format and write another. It supports a wide range of input and output formats, including Markdown, LaTeX, HTML, reStructuredText, EPUB, and Microsoft Word docx. Because of its modular reader‑writer architecture and extensible filter system, Pandoc serves as a foundational tool in academic publishing, technical documentation, and web‑content workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pandoc">Pandoc - Wikipedia</a></li>
<li><a href="https://opensource.com/article/20/5/pandoc-cheat-sheet">Convert documents with Pandoc like a pro | Opensource.com</a></li>
<li><a href="https://pandoc.org/">Pandoc - index</a></li>

</ul>
</details>

**Discussion**: Commenters praised Pandoc’s clean output, its usefulness for daily tasks like moving content between email and code, and highlighted the achievement of a philosophy professor creating a tool used by millions. Several shared personal scripts, such as a minimal static site generator, illustrating Pandoc’s flexibility and enduring appeal.

**Tags**: `#pandoc`, `#document conversion`, `#open source`, `#software longevity`, `#markup`

---

<a id="item-9"></a>
## [Study finds India's latrine subsidy raises river fecal contamination by 72%](https://arxiv.org/abs/2607.29371) ⭐️ 8.0/10

The study estimates that India's subsidy for over 100 million latrines increased river fecal contamination by 72%, offsetting child health benefits where upstream wastewater infrastructure is inadequate. It shows that sanitation policies can generate unintended water pollution externalities that undermine health gains unless paired with adequate fecal sludge treatment infrastructure. Using soil‑characteristic variation as an instrumental variable, the analysis finds a 72% rise in river fecal contamination and that the mortality benefit disappears in areas lacking upstream wastewater treatment.

rss · arXiv Quantitative Finance · Aug 3, 04:00

**Background**: Many developing countries subsidize latrine construction to reduce open defecation and improve child health. Without proper fecal sludge management, waste from pit latrines can leach into groundwater and surface waters, especially in soils with high permeability or shallow water tables. These unintended pollution externalities can offset health gains by increasing exposure to pathogens.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fecal_sludge_management">Fecal sludge management - Wikipedia</a></li>
<li><a href="https://www.wateraid.org/in/sites/g/files/jkxoof336/files/strategy-for-faecal-sludge-management-in-rural-india-.pdf">Strategy for Faecal Sludge Management in Rural India</a></li>
<li><a href="https://sswm.info/sites/default/files/reference_attachments/pit+latrines.pdf">Pit Latrines and Their Impacts on Groundwater</a></li>

</ul>
</details>

**Tags**: `#sanitation`, `#water quality`, `#public health`, `#development economics`, `#environmental policy`

---

<a id="item-10"></a>
## [Paper analyzes AI supply-chain chokepoints and industrial policy impact.](https://arxiv.org/abs/2607.29572) ⭐️ 8.0/10

The study uses the Herfindahl-Hirschman Index to measure concentration at each layer of the AI stack, finding low downstream HHI below 1,800 but extreme upstream values. Advanced packaging scores 8,100, leading-edge lithography reaches the maximum 10,000, and critical minerals such as gallium are near‑monopolized by a single country. The results show that upstream layers are strategic chokepoints beyond the reach of antitrust enforcement, meaning export controls and domestic industrial policy are the main tools to secure AI supply chains. This highlights where policymakers should focus intervention to mitigate concentration risks in the AI economy. Downstream layers such as model usage and cloud services register HHI values below the 1,800 threshold used by U.S. agencies to denote high concentration, indicating modest market power. In contrast, upstream layers show extreme concentration, with advanced packaging at 8,100, leading‑edge lithography at the maximum 10,000, and near‑monopoly control of minerals like gallium; moreover, a price increase in these upstream inputs barely affects final product cost, making the risk of input loss the real concern.

rss · arXiv Quantitative Finance · Aug 3, 04:00

**Background**: Artificial intelligence depends on a layered supply chain where models run on compute hardware that relies on advanced semiconductor chips made through processes such as advanced packaging and leading‑edge lithography, and those chips require electricity and refined minerals. The study employs the Herfindahl‑Hirschman Index (HHI), a standard measure of market concentration where values below 1,500 indicate competitive markets, 1,500‑2,500 moderate concentration, and above 2,500 high concentration, with U.S. agencies treating 1,800 as the threshold for highly concentrated markets. Advanced packaging integrates multiple chips into a single package to improve performance and reduce signal paths, while extreme‑ultraviolet (EUV) lithography, supplied almost exclusively by ASML, enables patterning of the smallest transistors needed for cutting‑edge AI chips, and critical minerals such as gallium are refined in only a few countries, giving those nations disproportionate control over an essential upstream input.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_(semiconductors)">Advanced packaging (semiconductors) - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://en.wikipedia.org/wiki/Herfindahl–Hirschman_index">Herfindahl–Hirschman index - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#supply chain`, `#industrial policy`, `#HHI`, `#semiconductors`

---

<a id="item-11"></a>
## [Policy Iteration Scheme for Semilinear Stochastic HJB Equations with Exponential Convergence](https://arxiv.org/abs/2607.29024) ⭐️ 8.0/10

The authors propose a policy iteration algorithm that linearizes semilinear stochastic Hamilton-Jacobi-Bellman equations into a sequence of linear PDEs and prove monotone exponential convergence of the approximations to the value function in mean-square sense. This provides the first provably exponentially convergent policy iteration method for non‑Markovian stochastic optimal control, offering a theoretically sound and computationally tractable approach to a class of problems that were previously difficult to solve. The algorithm relies on successive linearization of the semilinear SHJB equation, yielding a sequence of linear backward stochastic differential equations whose solutions converge monotonically and at an exponential rate in the L² norm.

rss · arXiv Quantitative Finance · Aug 3, 04:00

**Background**: Stochastic Hamilton-Jacobi-Bellman (SHJB) equations arise in stochastic optimal control when the value function depends on a random field; in the non‑Markovian case they become semilinear PDEs with measurable randomness, making direct numerical solution challenging. Policy iteration is a classical technique for solving Markov decision processes and continuous‑time control problems, where a policy is evaluated and improved iteratively. Exponential convergence means the error decreases proportionally to a constant raised to the negative iteration count, a strong guarantee rarely available for nonlinear stochastic PDEs.

<details><summary>References</summary>
<ul>
<li><a href="http://www.math.univ-brest.fr/perso/rainer.buckdahn/March+2010/presentation/School/RoscoffFuhrman2010.pdf">Hamilton - Jacobi - Bellman equations</a></li>
<li><a href="https://arxiv.org/html/2508.01718v1">Neural Policy Iteration for Stochastic Optimal Control ...</a></li>
<li><a href="https://www.researchgate.net/publication/341299714_Exponential_Convergence_and_Stability_of_Howard's_Policy_Improvement_Algorithm_for_Controlled_Diffusions">Exponential Convergence and Stability of Howard's Policy ...</a></li>

</ul>
</details>

**Tags**: `#stochastic optimal control`, `#Hamilton-Jacobi-Bellman equations`, `#policy iteration`, `#exponential convergence`, `#stochastic PDEs`

---

<a id="item-12"></a>
## [Wrong and More Confident: LLMs on Graduate Economics Exam](https://arxiv.org/abs/2607.23424) ⭐️ 8.0/10

The study adds irrelevant distractors (red herrings) to sixty graduate-level microeconomics problems in the new Graduate Economic Reasoning Benchmark (GERB) and finds that LLMs' correct answer rate drops by about 12.3 percentage points on average. It shows that LLMs are highly sensitive to irrelevant information, which undermines their reliability in noisy real-world settings, and provides GERB as a benchmark to measure reasoning robustness. On the clean problems the models averaged 52.5% accuracy; the red herring reduced this by 12.3 points, roughly a quarter of their mean performance, with no detectable difference between models with or without reasoning ability, though reasoning models showed wavering answers while non‑reasoning models repeated the same wrong answer; open‑weight models achieved similar accuracy at lower cost per correct answer.

rss · arXiv Quantitative Finance · Aug 3, 04:00

**Background**: Large language models (LLMs) are AI systems that generate text by predicting the next token; they are often tested on reasoning tasks to assess their ability to follow logical steps. A 'red herring' is an irrelevant piece of information inserted into a problem to see whether the model’s reasoning is distracted by noise. Evaluating robustness to such distractors is important because real‑world inputs frequently contain irrelevant content that can degrade performance. The study uses a within‑subject 2×2 factorial design, meaning each model answers every problem under four conditions (with/without red herring and with/without request for explanation), allowing direct comparison of the same model across treatments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Di-viner/LLM-Robustness-to-Irrelevant-Information">GitHub - Di-viner/LLM-Robustness-to-Irrelevant-Information: [COLM'24] "How Easily do Irrelevant Inputs Skew the Responses of Large Language Models?"</a></li>
<li><a href="https://blog.mirkopeters.com/decoding-the-intricacies-an-in-depth-exploration-of-within-subject-design-0b0c31712527">Decoding the Intricacies: An In-depth Exploration of Within - Subject ...</a></li>

</ul>
</details>

**Tags**: `#LLM robustness`, `#reasoning`, `#economics benchmark`, `#AI evaluation`, `#experimental study`

---

<a id="item-13"></a>
## [Unified Continuous-Time Q-Learning for Mean-Field Games and Control](https://arxiv.org/abs/2407.04521) ⭐️ 8.0/10

The paper introduces a unified continuous-time Q-learning method that uses a decoupled integrated Q-function (decoupled Iq-function) to solve both mean-field game (MFG) and mean-field control (MFC) problems. By providing a martingale characterization and a parametric algorithm, the work bridges reinforcement learning and mean-field control theory, offering a single framework applicable to a broad class of stochastic multi-agent systems. The decoupled Iq-function is shown to be a martingale, enabling policy evaluation without direct access to the population distribution; the resulting algorithm employs test policies and an averaged martingale orthogonality condition to learn MFG and MFC policies, demonstrated in LQ and non-LQ settings.

rss · arXiv Quantitative Finance · Aug 3, 04:00

**Background**: Mean-field games study strategic interactions of many agents via a representative agent's Hamilton–Jacobi–Bellman equation coupled with a Fokker–Planck equation for the population distribution. Mean-field control, in contrast, optimizes a cost functional for a single agent influencing the distribution. Continuous-time Q-learning extends temporal-difference learning to stochastic differential equations, often applied to jump-diffusion models where dynamics include both diffusion and sudden jumps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mean-field_game_theory">Mean-field game theory - Wikipedia</a></li>
<li><a href="https://bactra.org/notebooks/mean-field-games-and-control.html">Mean Field Games and Mean Field Control</a></li>
<li><a href="https://arxiv.org/html/2407.03888v4">Continuous - time q - learning in jump - diffusion models under Tsallis...</a></li>

</ul>
</details>

**Tags**: `#mean-field games`, `#reinforcement learning`, `#continuous-time control`, `#Q-learning`, `#stochastic systems`

---