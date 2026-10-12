---
layout: default
title: "Horizon Summary: 2026-10-12 (EN)"
date: 2026-10-12
lang: en
---

> From 39 items, 9 important content pieces were selected

---

1. [Gap in shared understanding of LLM capabilities is widening.](#item-1) ⭐️ 8.0/10
2. [Terence Tao unveils 'Math 2.0' vision for AI-driven mathematics](#item-2) ⭐️ 8.0/10
3. [Passkeys Are a Trap: Vendor Lock‑In and Usability Concerns Spark Debate](#item-3) ⭐️ 8.0/10
4. [Reverse engineering a commercial spatial audio effect.](#item-4) ⭐️ 8.0/10
5. [This paper shows linear demand systems are microfounded by heterogeneous discrete-choice consumers.](#item-5) ⭐️ 8.0/10
6. [AI-Mediation in Retail Markets: Revenue Effects and Assortment Optimization](#item-6) ⭐️ 8.0/10
7. [CorrFlow: Exact and Permutation-Equivariant Flow Matching on the Correlation Elliptope](#item-7) ⭐️ 8.0/10
8. [Backward Actor-Critic PPO Scheme for Robust Option Pricing under Uncertain Volatility.](#item-8) ⭐️ 8.0/10
9. [Study finds generative AI mostly complements, augments U.S. federal jobs](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Gap in shared understanding of LLM capabilities is widening.](https://twitter.com/karpathy/status/2109361546505966046) ⭐️ 8.0/10

A tweet by Andrej Karpathy sparked a Hacker News discussion revealing that experts are increasingly skeptical about what LLMs can reliably do, while many members of the public hold overly optimistic views about AI agents completing complex tasks. This divergence can lead to mismatched expectations, flawed investment decisions, and policy challenges as organizations adopt LLMs based on inaccurate perceptions of their capabilities. Commenters highlighted concerns about needing to understand codebases for maintenance, potential future token costs, code erosion, and the tendency of LLMs to make assumptions or mistakes that require verification, suggesting that only verifiable or low‑risk tasks are currently suitable for agentic use.

hackernews · albertzeyer · Oct 11, 20:20 · [Discussion](https://news.ycombinator.com/item?id=50047422)

**Background**: Large language models are evaluated using benchmarks such as MMLU and HellaSwag, which measure performance on standardized tasks but may not reflect real‑world reliability. Surveys show AI experts tend to be more optimistic about AI’s potential than the general public, yet recent expert commentary reveals growing caution about overestimating LLM abilities in complex, unverified contexts. Evaluation frameworks like MLflow LLM Evaluate help practitioners assess model capabilities, but the interpretation of results varies across technical and non‑technical audiences.

<details><summary>References</summary>
<ul>
<li><a href="/url?opi=89978449&q=https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/&sa=U&ved=2ahUKEwiNhN2w0bOXAxU6KkQIHXBfANkQFnoECAkQAg&usg=AOvVaw0fan4gWsva5ODn7DMB9o9g">How the US Public and AI Experts View Artificial Intelligence | Pew Research Center</a></li>
<li><a href="https://www.comet.com/site/blog/llm-evaluation-frameworks/">LLM Evaluation Frameworks: Head-to-Head Comparison</a></li>
<li><a href="https://www.evidentlyai.com/llm-guide/llm-benchmarks">30 LLM evaluation benchmarks and how they work</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread shows a split: expert commenters urge caution, stressing the need for code review, cost awareness, and verification, while other participants express confidence that AI agents can handle complex projects with simple prompts. Overall sentiment reflects a widening trust gap between technical skeptics and optimistic lay users.

**Tags**: `#LLM`, `#AI perception`, `#AI capabilities`, `#community discussion`, `#AI adoption`

---

<a id="item-2"></a>
## [Terence Tao unveils 'Math 2.0' vision for AI-driven mathematics](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf) ⭐️ 8.0/10

Terence Tao released a set of slides titled 'Math 2.0' for a Caltech talk in October 2026, describing how AI and computational tools are reshaping mathematical research and practice. The talk highlights a potential shift in how mathematicians create and verify knowledge, suggesting AI could accelerate proof discovery while raising questions about understanding and elegance in mathematics. The slides discuss AI's role in drug discovery, critique the current generation of math AI for not aiming at elegant additions to the mathematical 'codebase', and reference tools like Lean proof assistant and neural theorem provers.

hackernews · Anon84 · Oct 11, 13:16 · [Discussion](https://news.ycombinator.com/item?id=50043026)

**Background**: Mathematics has traditionally relied on human intuition and rigorous proof, a state Tao refers to as 'Math 1.0'. Recent advances in AI, including neural theorem provers and interactive proof assistants like Lean, enable computers to assist in formal verification and proof search. These technologies are beginning to change how conjectures are explored and theorems are produced, prompting discussions about the future of the discipline.

<details><summary>References</summary>
<ul>
<li><a href="https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf">Math 2 . 0</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_theorem_proving">Neural theorem proving</a></li>

</ul>
</details>

**Discussion**: Several commenters worried that AI‑generated drugs might be prescribed without understanding their mechanisms, while others argued Tao was speaking outside his area of expertise. Many lamented that AI could erase the joy of solving problems, likening mathematics to a codebase that should be extended elegantly.

**Tags**: `#mathematics`, `#AI`, `#Terence Tao`, `#Math 2.0`, `#AI in science`

---

<a id="item-3"></a>
## [Passkeys Are a Trap: Vendor Lock‑In and Usability Concerns Spark Debate](https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them) ⭐️ 8.0/10

The article "Passkeys are a trap" published on nonfunctional.substack.com argues that passkeys create vendor lock‑in and usability problems, prompting a detailed Hacker News discussion with 390 points and 216 comments. It highlights real‑world trade‑offs of passkey adoption that affect developers, security professionals, and end users, especially regarding portability, attestation, and resistance to phishing. Attestation can only be required during credential registration; browsers show a permission prompt if requested, and passkeys are domain‑bound, making them resistant to man‑in‑the‑middle attacks in most use cases.

hackernews · laurex · Oct 11, 21:59 · [Discussion](https://news.ycombinator.com/item?id=50048312)

**Background**: Passkeys are a passwordless authentication method based on public‑key cryptography, using the WebAuthn API in the browser and the CTAP protocol to communicate with authenticators such as smartphones or security keys. They are part of the FIDO2 standard, which ties each credential to a specific web domain, providing strong resistance to phishing and man‑in‑the‑middle attacks. Users can store passkeys on platform authenticators (built‑into devices) or roaming authenticators (external security keys).

<details><summary>References</summary>
<ul>
<li><a href="https://clerk.com/blog/what-are-passkeys">What are passkeys and how do they work ?</a></li>
<li><a href="https://blog.pwnsy.com/webauthn-explained">WebAuthn Explained : The FIDO 2 Standard Behind Passkeys</a></li>
<li><a href="https://passkeys.dev/docs/reference/specs/">Specifications - passkeys.dev</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about lack of portability and the inability to back up passkeys, wishing to control credential strength and avoid vendor lock‑in. Some noted that attestation is only enforceable at registration and triggers browser prompts, while others praised the article’s writing and pointed out a missed footnote about passkeys’ domain‑bound MITM resistance. Overall sentiment was mixed, balancing security benefits against usability and lock‑in worries.

**Tags**: `#passkeys`, `#authentication`, `#security`, `#privacy`, `#web standards`

---

<a id="item-4"></a>
## [Reverse engineering a commercial spatial audio effect.](http://epestr.com/blog/reverse-engineering-a-commercial-spatial-audio-effect/) ⭐️ 8.0/10

The author measured the stereo impulse responses of a commercial spatial audio processor and rebuilt the effect as a convolution filter on Linux. He documented the analysis, implementation, and listening results of the recreated effect. This work shows how proprietary audio effects can be inspected and reproduced with open‑source tools, providing a valuable learning resource for DSP engineers. It also highlights the growing accessibility of spatial audio techniques for hobbyists and professionals alike. The effect was captured by measuring left and right channel impulse responses, then implemented using convolution; the author notes that the replica lacks perfect fidelity and sounds subjectively colored. No source code or exact parameters of the original processor were disclosed.

hackernews · epestr · Oct 11, 15:21 · [Discussion](https://news.ycombinator.com/item?id=50044272)

**Background**: Spatial audio effects simulate how sound changes as it travels from a source to the listener, often using head‑related transfer functions (HRTFs) and reverberation to create localization cues. Convolution with measured impulse responses can reproduce linear time‑invariant audio processing, a common technique in DSP. The article focuses on a commercial spatial audio processor whose internal algorithm was unknown, prompting the reverse‑engineering effort.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/3D_audio_effect">3D audio effect - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Head-related_transfer_function">Head-related transfer function - Wikipedia</a></li>
<li><a href="http://epestr.com/blog/reverse-engineering-a-commercial-spatial-audio-effect/">Reverse engineering a commercial spatial audio effect</a></li>

</ul>
</details>

**Discussion**: Commenters praised the educational journey and curiosity shown, while some criticized the audio quality as overly processed (“Bose barf”) and noted the difficulty of finding neutral‑sounding devices. Others shared related experiences, such as writing similar blog posts or using tools like Fruity Convolver.

**Tags**: `#reverse engineering`, `#audio processing`, `#spatial audio`, `#DSP`, `#hackernews`

---

<a id="item-5"></a>
## [This paper shows linear demand systems are microfounded by heterogeneous discrete-choice consumers.](https://arxiv.org/abs/2610.13785) ⭐️ 8.0/10

The paper demonstrates that aggregate linear demand systems can be micro-founded by a population of heterogeneous consumers making discrete choices, and that this framework can be estimated using only market-level data without fixing market size. By linking linear demand to discrete choice models, the approach retains the analytical simplicity of linear systems while gaining the flexibility and welfare analysis capabilities of BLP, offering a significant methodological advance for econometrics and industrial organization. The model recovers the distribution of consumer preferences by disciplining corner solutions with aggregate terms, allows heterogeneity in choice sets, yields endogenous substitution matrices, and enables markup and cost pass‑through measurement using only market‑level data.

rss · arXiv Quantitative Finance · Oct 12, 04:00

**Background**: Linear demand systems relate quantities demanded to prices through linear equations and are widely used for their analytical tractability. Discrete choice models, such as the Berry‑Levinsohn‑Pakes (BLP) framework, derive demand from individual utility maximization but typically require microdata or an exogenous market size. This paper shows how heterogeneous discrete‑choice consumers can generate aggregate linear demand, providing a microfoundation that lets researchers estimate rich demand structures from market‑level observations alone.

<details><summary>References</summary>
<ul>
<li><a href="https://cris.maastrichtuniversity.nl/ws/files/32336680/RM19004.pdf">On the Microfoundation of Linear Oligopoly Demand</a></li>
<li><a href="https://academic.oup.com/princeton-scholarship-online/book/58615/chapter/485712701">Demand Estimation Using Market—Level Data | Structural ...</a></li>

</ul>
</details>

**Tags**: `#econometrics`, `#discrete choice`, `#demand estimation`, `#industrial organization`, `#linear demand systems`

---

<a id="item-6"></a>
## [AI-Mediation in Retail Markets: Revenue Effects and Assortment Optimization](https://arxiv.org/abs/2610.12917) ⭐️ 8.0/10

The study examines how AI shopping assistants influence consumer choice and shows that ignoring AI mediation in assortment optimization can lead to substantial revenue losses, with mean losses between 2.5% and 11.4% if mediation is omitted, while a simple deterministic plug‑in based on AI utility ordering reduces losses to at most 0.53%. It underscores the financial significance of AI‑mediated recommendation systems for retailers, demonstrating that failing to account for AI‑generated shortlists can cause notable revenue erosion and that incorporating AI behavior improves assortment decisions and profitability. The authors construct product‑ranking data from leading AI models, fit Plackett‑Luce models to estimate AI utilities, combine these with synthetic customer preferences modeled via a multinomial logit choice process, and show that deterministic mediation admits a fully polynomial‑time approximation scheme for any fixed number of customer segments.

rss · arXiv Quantitative Finance · Oct 12, 04:00

**Background**: AI mediation occurs when an AI shopping assistant creates a shortlist of products that consumers then choose from, often modeled as a sequential choice process. The Plackett‑Luce model is a probabilistic framework that represents ranking data as a series of binary choices using item‑specific support parameters, commonly used to infer underlying utilities from observed rankings. In retail assortment planning, the multinomial logit (MNL) model captures consumer choice among a set of products, assuming independence of irrelevant alternatives, and is widely used to predict demand and optimize product selection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/plackett-luce-model-framework">Plackett - Luce Model Framework</a></li>
<li><a href="https://www.researchgate.net/publication/319904943_Multinomial_Logit_Models_in_Marketing_-_From_Fundamentals_to_State-of-the-Art">(PDF) Multinomial Logit Models in Marketing - From ...</a></li>
<li><a href="https://www.retailscrape.com/ai-assortment-optimization.php">AI-Powered Assortment Optimization | Retail Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI mediation`, `#retail assortment optimization`, `#Plackett-Luce model`, `#revenue management`, `#empirical analysis`

---

<a id="item-7"></a>
## [CorrFlow: Exact and Permutation-Equivariant Flow Matching on the Correlation Elliptope](https://arxiv.org/abs/2610.13606) ⭐️ 8.0/10

CorrFlow introduces a permutation‑equivariant flow‑matching model that uses a bijective generalized Fisher transform to map full‑rank correlation matrices to unconstrained coordinates, guaranteeing valid outputs without any post‑hoc projection. By separating the validity constraint from distribution learning, CorrFlow enables reliable generation of correlation matrices for financial and statistical modeling, improving sample quality and eliminating costly projection steps. Experiments on 80×80 Taiwan equity matrices (five seeds per method) show CorrFlow yields 100% valid draws and a feature sliced‑Wasserstein distance of 0.712 ± 0.141, substantially lower than CorrGAN (4.339 ± 0.252) and image diffusion (4.610 ± 0.191) after their invalid outputs are projected back.

rss · arXiv Quantitative Finance · Oct 12, 04:00

**Background**: A correlation matrix must be symmetric, positive‑semidefinite and have unit diagonal, defining a convex set known as the correlation elliptope; this set simultaneously enforces positive‑definiteness and invariance under simultaneous row‑column permutations. The Fisher transform (or its generalized version) provides a bijective mapping from the interior of the elliptope to an unconstrained Euclidean space, turning the nonlinear validity constraint into simple coordinates. Permutation‑equivariant flow matching builds generative models whose outputs reorder exactly when the input variables are permuted, allowing the model to respect the symmetry of the elliptope while learning the data distribution in the transformed space.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.04162">Correlation Matrices in High Dimensions:The Elliptope as...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fisher_transformation">Fisher transformation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#correlation matrices`, `#flow matching`, `#generative models`, `#permutation equivariance`, `#financial modeling`

---

<a id="item-8"></a>
## [Backward Actor-Critic PPO Scheme for Robust Option Pricing under Uncertain Volatility.](https://arxiv.org/abs/2605.06670) ⭐️ 8.0/10

The paper proposes a backward actor‑critic stochastic policy‑gradient algorithm that combines Proximal Policy Optimization (PPO) with one‑hidden‑layer neural networks to approximate the value function and control policy for robust option pricing in the multidimensional uncertain volatility model. It also derives an approximate superhedging strategy from the spatial gradient of the trained critic. Addressing the curse of dimensionality in robust pricing, the method offers a computationally efficient alternative to traditional Monte Carlo and machine‑learning baselines while delivering both accurate prices and usable superhedging strategies. This bridges reinforcement learning techniques with financial engineering, opening new pathways for high‑dimensional derivative valuation under model uncertainty. The control policy is parameterized as a squashed Gaussian policy built on a C‑vine representation of the correlation matrix, which guarantees positive definiteness by construction. A dual formulation is used to assess the learned gradient and to produce a numerical dual estimate of the robust price, and experiments show the approach yields accurate prices, remains efficient, and compares favorably with existing benchmarks.

rss · arXiv Quantitative Finance · Oct 12, 04:00

**Background**: The Uncertain Volatility Model (UVM) treats asset volatility and correlation as unknown but bounded processes, leading to a robust option pricing problem that requires solving a high‑dimensional stochastic control problem. To handle correlation uncertainty, the paper parameterizes correlation matrices using a C‑vine decomposition, which expresses any positive‑definite correlation matrix through a set of partial correlations and guarantees positive definiteness by construction. In reinforcement learning, a squashed Gaussian policy (a Gaussian distribution passed through a tanh squashing function) is commonly used to represent continuous actions, ensuring outputs lie in a valid action space.

<details><summary>References</summary>
<ul>
<li><a href="https://www.academia.edu/2671953/Uncertain_Volatility_Model">(PDF) Uncertain Volatility Model</a></li>
<li><a href="https://www.researchgate.net/publication/262641840_Parsimonious_parameterization_of_correlation_matrices_using_truncated_vines_and_factor_analysis">Parsimonious parameterization of correlation matrices using...</a></li>
<li><a href="https://www.kinetiqvision.com/learn/deep-reinforcement-learning/continuous-control/continuous-action-spaces">Continuous action spaces – Deep Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#stochastic control`, `#option pricing`, `#uncertain volatility model`, `#policy gradient`

---

<a id="item-9"></a>
## [Study finds generative AI mostly complements, augments U.S. federal jobs](https://arxiv.org/abs/2503.09637) ⭐️ 8.0/10

A multi-stage Retrieval-Augmented Generation (RAG) system was used to assess generative AI's impact on hundreds of U.S. federal occupational series, scoring each role on complementarity, augmentation, and substitutivity. The results indicate that generative AI is unlikely to fully replace federal jobs, highlighting the importance of targeted reskilling and human‑AI collaboration over broad workforce reductions. Even occupations scoring highest on substitutivity showed only partial automation of routine subtasks rather than whole‑job elimination, and the RAG approach anchored LLM judgments in curated evidence to limit hallucination.

rss · arXiv Quantitative Finance · Oct 12, 04:00

**Background**: Retrieval‑Augmented Generation (RAG) combines a large language model with an external knowledge base, allowing the model to retrieve up‑to‑date information before generating responses. In the U.S. federal system, occupations are described using Knowledge, Skills, and Abilities (KSAs) – narrative statements required for job applications. The study applied a multi‑stage RAG pipeline to ground LLM assessments of each occupation’s KSAs in curated evidence, enabling systematic scoring of AI’s complementarity, augmentation, and substitutivity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval - Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Essay">Essay - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#workforce impact`, `#federal employment`, `#AI augmentation`, `#policy analysis`

---