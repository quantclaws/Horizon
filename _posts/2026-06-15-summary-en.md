---
layout: default
title: "Horizon Summary: 2026-06-15 (EN)"
date: 2026-06-15
lang: en
---

> From 31 items, 11 important content pieces were selected

---

1. [Formal Methods and the Future of Programming](#item-1) ⭐️ 8.0/10
2. [Alan Perlis's 1982 Programming Epigrams Resurface on Hacker News](#item-2) ⭐️ 8.0/10
3. [Gary Bernhardt’s 2014 Talk Predicts JavaScript’s Shift to Compilation Target](#item-3) ⭐️ 8.0/10
4. [Why AI hasn’t replaced software engineers, and won’t](#item-4) ⭐️ 8.0/10
5. [Estimating Public's Social Welfare Function from UK Life Satisfaction Survey](#item-5) ⭐️ 8.0/10
6. [LANTERN Framework Models Health-State Transitions from Irregular Data.](#item-6) ⭐️ 8.0/10
7. [Geometric Theory Identifies When LLM Proposals Beat Discovery Bottlenecks](#item-7) ⭐️ 8.0/10
8. [Quantum Computing Threat to Bitcoin and Ethereum Evaluated](#item-8) ⭐️ 8.0/10
9. [Detecting Lookahead Bias in LLM Economic Forecasts](#item-9) ⭐️ 8.0/10
10. [Recovering Risk-Neutral Moments from Options](#item-10) ⭐️ 8.0/10
11. [Deep Learning with Elicitability Solves McKean-Vlasov FBSDEs with Common Noise](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Formal Methods and the Future of Programming](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

A Hacker News post shared Jane Street's blog on formal methods, sparking discussion about proof techniques, expressive type systems, and verification's role in AI-assisted programming. The conversation highlights how formal verification can improve reliability of AI-generated code and shift developer effort toward proving correctness rather than just writing code. Commenters noted experiences with Boyer-Moore provers, use of Scala 3's expressive types for compile-time proofs, and concerns that AI-generated code overwhelms manual review, increasing the need for automated verification.

hackernews · eatonphil · Jun 14, 12:35 · [Discussion](https://news.ycombinator.com/item?id=48526633)

**Background**: Formal methods are mathematically rigorous techniques for specifying, developing, and verifying software and hardware systems. Expressive type systems, such as dependent types, allow program properties to be encoded directly in types and checked by the compiler. With the rise of AI-assisted programming, researchers are exploring how large language models can help automate proof generation, such as creating loop invariants or proof scripts for verification languages.

<details><summary>References</summary>
<ul>
<li><a href="https://old.lemmy.sdf.org/post/3148821">The Dafny Programming and Verification Language ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dependent_type">Dependent type - Wikipedia</a></li>
<li><a href="https://roars.dev/pubs/doan2025ai.pdf">PDF AI-Assisted Autoformalization of Combinatorics Problems in Proof Assistants</a></li>

</ul>
</details>

**Discussion**: Commenters generally appreciated the depth of the discussion, sharing personal experiences with older provers and modern type-driven verification, while some expressed skepticism about the overhead of formal specs compared to traditional tests. Several noted that AI-generated code increases the burden on human reviewers, making automated verification more attractive.

**Tags**: `#formal-methods`, `#programming-languages`, `#verification`, `#type-systems`, `#AI-code-generation`

---

<a id="item-2"></a>
## [Alan Perlis's 1982 Programming Epigrams Resurface on Hacker News](https://www.cs.yale.edu/homes/perlis-alan/quotes.html) ⭐️ 8.0/10

The news item shares a compilation of Alan Perlis's 1982 programming aphorisms, known as 'Perlisisms', which have sparked discussion on their relevance today. Perlis's epigrams continue to influence software engineering thinking, offering timeless insights that resonate with modern topics such as language design and AI-driven code generation. The collection originates from the September 1982 ACM SIGPLAN article 'Epigrams in Programming' and includes notable quotes such as 'A language that doesn't affect the way you think about programming, is not worth knowing.'

hackernews · tosh · Jun 14, 14:56 · [Discussion](https://news.ycombinator.com/item?id=48527820)

**Background**: Alan Jay Perlis was an American computer scientist, the first Turing Award recipient, known for his pioneering work in programming languages. The 'Epigrams in Programming' article appeared in ACM's SIGPLAN publication in September 1982, collecting concise, thought‑provoking statements about coding and language design. These epigrams have been widely quoted in computing culture for their wit and insight into programming practice.

<details><summary>References</summary>
<ul>
<li><a href="https://static.hlt.bme.hu/semantics/external/pages/John_McCarthy/en.wikipedia.org/wiki/Alan_Perlis.html">Alan Perlis - Wikipedia</a></li>
<li><a href="http://www.cs.yale.edu/homes/perlis-alan/quotes.html">Perlisisms - "Epigrams in Programming" by Alan J. Perlis</a></li>

</ul>
</details>

**Discussion**: Commenters expressed appreciation for Perlis's wit, noting quotes that remain relevant to contemporary topics like large language models and language design. Some highlighted specific aphorisms about language influence and low‑level programming, while others shared related media or personal projects such as the perl.is domain. The discussion reflected both nostalgic admiration and ongoing engagement with the timeless nature of the epigrams.

**Tags**: `#programming`, `#quotes`, `#Alan Perlis`, `#software engineering`, `#wisdom`

---

<a id="item-3"></a>
## [Gary Bernhardt’s 2014 Talk Predicts JavaScript’s Shift to Compilation Target](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

In a 2014 talk titled 'The Birth and Death of JavaScript,' Gary Bernhardt reviewed the language’s history and forecast its evolution into a compilation target for languages like C/C++ and a broader application platform via tools such as TypeScript and Electron. The talk’s predictions have largely come true, as seen in the adoption of asm.js, WebAssembly, TypeScript, and Electron, demonstrating JavaScript’s lasting influence on modern software development. Bernhardt highlighted asm.js as an early compilation target, noted its later supersession by WebAssembly, and mentioned the rise of TypeScript for safer JavaScript and Electron for desktop apps built with web technologies.

hackernews · subset · Jun 14, 12:38 · [Discussion](https://news.ycombinator.com/item?id=48526661)

**Background**: JavaScript is a high-level, dynamically typed language originally created for adding interactivity to web pages. asm.js is a strict subset of JavaScript designed to enable near‑native performance for code compiled from languages like C and C++, serving as an early compilation target. WebAssembly, announced in 2015 and standardized in 2019, provides a portable binary format that supersedes asm.js as a compilation target for the web and beyond. TypeScript adds static typing to JavaScript, while Electron allows developers to package web‑based applications as cross‑platform desktop apps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emscripten">Emscripten</a></li>

</ul>
</details>

**Discussion**: Commenters praised the talk’s foresight, noting that Bernhardt’s predictions about JavaScript becoming a compilation target (via asm.js and WebAssembly) and its use in desktop apps (Electron) and safer coding (TypeScript) have largely materialized. Some humorously remarked on his joking prediction of a global disaster between 2020‑2025, while others highlighted the recurring pattern of inventing ‘better’ JavaScript that is ultimately transpiled back to JavaScript. Overall, the discussion reflects appreciation for the talk’s lasting relevance and insightful commentary.

**Tags**: `#JavaScript`, `#WebAssembly`, `#TypeScript`, `#Talk`, `#Programming Languages`

---

<a id="item-4"></a>
## [Why AI hasn’t replaced software engineers, and won’t](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

The essay by Arvind Narayanan and Sayash Kapoor argues that current data, including New York’s first‑year AI disclosure WARN filings showing zero AI‑related layoffs, does not support claims that AI will cause mass unemployment in software engineering. By showing that even a highly automatable profession like software engineering is not seeing AI‑driven layoffs, the analysis suggests most other occupations are likely even more resilient, informing career advice and policy debates about AI’s labor impact. In March 2025 New York added an AI disclosure checkbox to WARN Act filings; over 160 companies filed notices in the first year and none checked the AI box. The authors identify three bottlenecks resisting automation: deciding/specifying what to build, verifying/accountability for delivery, and the deep human understanding of codebase, business, and environment required for those tasks.

rss · Simon Willison · Jun 14, 23:54

**Background**: The WARN Act requires employers to give 60‑day advance notice of mass layoffs or plant closings. New York is the first U.S. state to add an AI‑specific disclosure checkbox to those filings, aiming to track whether AI is cited as a cause of layoffs. Software engineering involves more than writing code; tasks such as meetings, debugging, requirement specification, and system accountability rely heavily on human judgment and contextual understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Worker_Adjustment_and_Retraining_Notification_Act_of_1988">Worker Adjustment and Retraining Notification Act of 1988 - Wikipedia</a></li>
<li><a href="https://www.bloomberg.com/news/newsletters/2025-06-12/new-york-state-updates-warn-notices-to-identify-layoffs-tied-to-ai">New York State Updates WARN Notices to Identify Layoffs Tied to AI</a></li>
<li><a href="https://www.softwareseni.com/why-ai-layoff-disclosure-laws-are-not-working-and-what-would-actually-fix-them/">Why AI Layoff Disclosure Laws Are Not Working and... - SoftwareSeni</a></li>

</ul>
</details>

**Tags**: `#AI impact`, `#software engineering`, `#labor market`, `#technology policy`, `#future of work`

---

<a id="item-5"></a>
## [Estimating Public's Social Welfare Function from UK Life Satisfaction Survey](https://arxiv.org/abs/2606.13752) ⭐️ 8.0/10

The study used a novel survey instrument with a representative UK sample (N=2,068) to estimate the public's social welfare function for life satisfaction, finding a median isoelastic parameter α=0.48 and strong aversion to wellbeing inequality. This implies a welfare function roughly proportional to the sum of square roots of individual utilities. The findings provide ethically grounded distributional weights for wellbeing policy evaluation and cost-benefit analysis, bridging theory and practice for policymakers focusing on subjective wellbeing. They show how public preferences over inequality can be quantified for use in social welfare assessments. The median isoelastic parameter of 0.48 indicates that improving the wellbeing of the least satisfied by one unit is valued about twice as much as improving the most satisfied by one unit. The survey instrument elicited preferences over utility measured by life satisfaction scores.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: A social welfare function aggregates individual utilities into a measure of collective wellbeing, often assuming a specific functional form such as the isoelastic (or Cobb‑Douglas) form. The isoelastic parameter α determines inequality aversion: lower α implies greater weight to improvements in the worst‑off individuals. Subjective wellbeing, measured by life satisfaction surveys, provides a cardinal utility proxy that can be used to estimate such functions directly from public preferences.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Social_welfare_function">Social welfare function - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/economics-econometrics-and-finance/social-welfare-function">Social Welfare Function - an overview | ScienceDirect Topics</a></li>
<li><a href="https://cep.lse.ac.uk/_new/publications/abstract.asp?index=12290">What is the public's social welfare function?</a></li>

</ul>
</details>

**Tags**: `#social welfare`, `#subjective wellbeing`, `#inequality aversion`, `#survey methods`, `#public policy`

---

<a id="item-6"></a>
## [LANTERN Framework Models Health-State Transitions from Irregular Data.](https://arxiv.org/abs/2606.13880) ⭐️ 8.0/10

The paper presents LANTERN, a longitudinal attribute-conditioned neural network that estimates multi-state health transition probabilities from temporally irregular longitudinal data, producing calibrated predictions for healthy, mild disability, severe disability, and death states. By improving calibration and transition matrix error over classical actuarial models and machine learning baselines, LANTERN offers a more reliable tool for disability insurance pricing, reserving, and solvency assessment, especially when health observations are irregular. LANTERN conditions transition probabilities on individual health history, time between observations, and demographic/socioeconomic attributes, aggregates individual predictions by age and origin state into actuarial transition matrices, and was evaluated on Health and Retirement Study data against logistic regression, gradient‑boosted trees, a recurrent neural network, and a last‑state persistence benchmark.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Longitudinal health data often contain irregular observation times, where follow‑up visits vary across individuals and may be related to health outcomes, challenging traditional models that assume equally spaced measurements. Classical actuarial multi‑state models typically rely on Markov, semi‑Markov, or proportional‑hazard assumptions, which can be restrictive when aging patterns are nonlinear and covariate histories are heterogeneous. Attribute‑conditioned neural networks extend standard neural architectures by conditioning predictions on external covariates (such as age, gender, or socioeconomic status), enabling them to capture complex, history‑dependent patterns in irregular longitudinal data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.13880">A Longitudinal Attribute-Conditioned Neural Network for ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-022-26933-1">Longitudinal individual predictions from irregular repeated ... Analysis of longitudinal data with irregular observation times Longitudinal individual predictions from irregular repeated ... A Longitudinal Attribute-Conditioned Neural Network for ... Accommodating informative visit times for analysing irregular ... Longitudinal Data Analysis | Springer Nature Link Broken Stick Model for Irregular Longitudinal Data</a></li>
<li><a href="https://www.rgare.com/knowledge-center/article/multi-state-models-and-their-applications-in-(re)insurance">Multi-state Models and their Applications in (Re)insurance - RGA</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#health informatics`, `#actuarial science`, `#longitudinal data`, `#neural networks`

---

<a id="item-7"></a>
## [Geometric Theory Identifies When LLM Proposals Beat Discovery Bottlenecks](https://arxiv.org/abs/2606.14386) ⭐️ 8.0/10

The paper formalizes three geometric conditions—spectral compression, orthogonal escape from the explored span, and residual signal alignment with the target—under which LLM‑generated non‑local hypotheses improve hybrid discovery systems. It validates the theory in synthetic environments, large‑scale A‑share factor discovery, and symbolic‑regression benchmarks. By turning LLM‑guided exploration into a diagnostic procedure, the work tells practitioners exactly when to spend computational budget on non‑local proposals, potentially saving resources in scientific discovery pipelines. The framework bridges geometric theory with practical hybrid search, impacting ML‑driven research across domains. The three conditions are derived theoretically and shown to be necessary for hybrid advantage; experiments reveal that random orthogonal jumps increase coverage but not yield without predictive alignment, and hybrid gains disappear as the hypothesis space approaches full rank. A public tabular sanity check tests the associated budget‑allocation implication.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Hybrid discovery systems combine a structured local search (e.g., gradient‑based or greedy exploration) with LLM‑generated non‑local proposals that can jump far from the current hypothesis span. Scientific discovery stalls when new hypotheses no longer provide independent information, even if the nominal hypothesis space remains large—a phenomenon called a discovery bottleneck. The paper interprets the bottleneck geometrically: spectral compression measures how much the explored subspace captures variance, orthogonal escape quantifies movement outside that subspace, and residual signal alignment checks whether the new direction correlates with the target signal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jmlr.org/papers/volume13/rubinstein12a/rubinstein12a.pdf">A Geometric Approach to Sample Compression</a></li>
<li><a href="https://www.emergentmind.com/topics/spectral-compression-family">Spectral Compression : Frameworks & Applications</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#scientific discovery`, `#large language models`, `#geometric theory`, `#hybrid search`

---

<a id="item-8"></a>
## [Quantum Computing Threat to Bitcoin and Ethereum Evaluated](https://arxiv.org/abs/2606.14484) ⭐️ 8.0/10

The paper analyzes how Shor's algorithm breaks Bitcoin and Ethereum signatures while Grover's algorithm only offers a limited quadratic speedup to proof‑of‑work, and estimates a ~60% probability of a cryptographically relevant quantum computer by 2050. Understanding these quantum risks helps blockchain developers prioritize migration to post‑quantum signatures and informs policymakers that the main barrier is governance rather than technology. Shor's algorithm threatens ECDSA over secp256k1 and BLS over BLS12-381, whereas Grover's algorithm only yields a quadratic speedup for mining, limited by fault‑tolerant costs and difficulty adjustment; the study’s Monte‑Carlo forecast gives a bimodal arrival distribution with about a one‑in‑six chance by 2035, 30% by 2040, and 60% by 2050, and shows that most exposed coins are migratable.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Quantum computers can run Shor's algorithm to factor large integers and break elliptic‑curve signatures such as ECDSA (used by Bitcoin) and BLS (used in Ethereum 2.0), while Grover's algorithm only provides a quadratic speedup for brute‑force tasks like proof‑of‑work mining. Because mining difficulty adjusts and each Grover operation incurs high fault‑tolerant overhead, the impact on Bitcoin's proof‑of‑work is limited, whereas signature schemes are directly vulnerable. The paper combines hardware scaling forecasts, expert surveys, and fault‑tolerance readiness into a Monte‑Carlo model to estimate when a cryptographically relevant quantum computer might appear. It finds that although a significant number of coins are exposed, most can be protected by migrating to post‑quantum signature schemes, making governance the key challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grover's_algorithm">Grover's algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BLS_digital_signature">BLS digital signature - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#blockchain security`, `#cryptocurrency`, `#post‑quantum cryptography`, `#risk assessment`

---

<a id="item-9"></a>
## [Detecting Lookahead Bias in LLM Economic Forecasts](https://arxiv.org/abs/2512.23847) ⭐️ 8.0/10

The paper introduces a Lookahead Propensity (LAP) statistic that estimates the probability an LLM has internalized future information via a date-only recall query, and uses it to detect lookahead bias in LLM-generated economic forecasts. The method is applied to news headlines predicting stock returns and earnings call transcripts predicting capital expenditures. Providing a cost‑efficient diagnostic for lookahead bias helps practitioners assess the reliability of LLM‑based forecasts, which is crucial for financial decision‑making and for ensuring that AI models are not inadvertently leaking future data. The approach highlights a general issue of training‑data contamination in LLMs used for prediction tasks. LAP is estimated by querying the LLM with a date‑only prompt for a firm‑date pair and measuring the likelihood that the prompt appeared in its training data; it remains substantially positive in‑sample and drops to near zero after the model’s training‑data cutoff. A significant positive interaction between LAP and forecast accuracy in a regression indicates lookahead‑bias contamination, and in the paper’s applications roughly 37% of the apparent predictive effect is amplified by memorization.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Lookahead bias occurs when a model inadvertently uses information that would not be available at the time of prediction, inflating its apparent performance. Large language models are trained on vast text corpora that may include future‑dated economic releases, news, or reports, so when prompted for a forecast they can “remember” those outcomes. Detecting such bias is difficult because the contamination is not obvious from the input alone, motivating statistical proxies like LAP that estimate training‑data overlap.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.23847">A Test of Lookahead Bias in LLM Forecasts</a></li>
<li><a href="https://www.emergentmind.com/topics/lookahead-propensity-lap">Lookahead Propensity in Estimation & LLMs</a></li>
<li><a href="https://connect.cfauk.org/discussion/llms-research-lookahead-bias-for-prediction-tasks">LLMs Research - Lookahead Bias for Prediction Tasks | Technology...</a></li>

</ul>
</details>

**Tags**: `#LLM bias detection`, `#economic forecasting`, `#lookahead bias`, `#machine learning`, `#statistical testing`

---

<a id="item-10"></a>
## [Recovering Risk-Neutral Moments from Options](https://arxiv.org/abs/2601.14852) ⭐️ 8.0/10

The paper introduces a projection estimator that uses portfolios of observed options to approximate multi‑asset payoffs, enabling the extraction of risk‑neutral dependence in incomplete markets. Applied to two unexpected Swiss National Bank EUR/CHF floor announcements, the method shows that dependence accounts for about two‑thirds of the change in joint crash probability. Providing a tractable way to measure risk‑neutral dependence improves option pricing, risk management, and the assessment of policy impacts on multi‑asset markets. The finite‑sample error bound also offers practical guidance on estimator reliability. The estimator constructs portfolios whose payoffs approximate functions of two or more underlying assets, derives a finite‑sample error bound, and is validated using SNB announcements where it attributes 66% of the joint crash probability shift to changes in dependence.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: Risk‑neutral moments summarize the distribution of asset prices under the risk‑neutral measure and are traditionally extracted from option prices via techniques such as the Carr–Madan formula. In incomplete markets, where not all payoffs can be replicated, estimating dependence between multiple assets from option data remains challenging. The projection estimator overcomes this by forming portfolios of traded options that approximate multi‑asset payoffs, allowing dependence to be inferred while providing a finite‑sample error bound. This approach builds on the literature that links risk‑neutral cumulants to latent factors in affine stochastic volatility models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.14852">[2601.14852] Beyond Carr Madan: A Projection Approach to Risk-Neutral Moment Estimation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Risk-neutral_measure">Risk-neutral measure - Wikipedia</a></li>
<li><a href="https://www.snb.ch/en/the-snb/mandates-goals/monetary-policy/decisions">The SNB’s monetary policy decisions | Swiss National Bank</a></li>

</ul>
</details>

**Tags**: `#quantitative finance`, `#options pricing`, `#risk-neutral moments`, `#financial econometrics`, `#econometric estimation`

---

<a id="item-11"></a>
## [Deep Learning with Elicitability Solves McKean-Vlasov FBSDEs with Common Noise](https://arxiv.org/abs/2512.14967) ⭐️ 8.0/10

The authors introduce a novel numerical method that combines Picard iterations, elicitability, and deep learning to approximate solutions of McKean-Vlasov forward-backward stochastic differential equations with common noise, validated on an inter-bank borrowing and lending systemic-risk model. By avoiding costly nested Monte Carlo simulations, the method provides an efficient and scalable tool for solving high-dimensional mean-field stochastic systems, with direct applications to systemic risk modeling and mean-field games. The mean-field interaction term is parameterized by a recurrent neural network trained to minimize an elicitable score, while the backward process is approximated by a hybrid feedforward-recurrent network representing the decoupling field; the algorithm is tested on a model with known analytical solution, extended to quantile-mediated interactions, and applied to a non-stationary Aiyagari-Bewley-Huggett economic growth model.

rss · arXiv Quantitative Finance · Jun 15, 04:00

**Background**: McKean-Vlasov forward-backward stochastic differential equations (MV-FBSDEs) describe systems where the dynamics depend on the law of the state itself, often arising in mean-field games and financial modeling. Common noise introduces a source of uncertainty shared by all agents, complicating analysis and requiring specialized techniques such as Malliavin differentiability. Elicitability refers to the property that a statistical functional (e.g., mean, quantile) can be expressed as the unique minimizer of an appropriate score function, enabling the construction of pathwise loss functions for machine learning.

<details><summary>References</summary>
<ul>
<li><a href="https://carmona.princeton.edu/document/351">[PDF] FORWARD-BACKWARD STOCHASTIC DIFFERENTIAL EQUATIONS AND CONTROLLED MCKEAN VLASOV DYNAMICSS The purpose of this paper is to provid - Princeton University</a></li>
<li><a href="https://ai.stanford.edu/~shoham/www+papers/SIGECOM2008-elicitability.pdf">PDF Eliciting Properties of Probability Distributions: the Highlights</a></li>
<li><a href="https://www.researchgate.net/publication/396095149_Malliavin_differentiability_of_McKean-Vlasov_SDEs_with_common_noise">(PDF) Malliavin differentiability of McKean-Vlasov SDEs with common noise</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#McKean-Vlasov FBSDE`, `#elicitiability`, `#stochastic differential equations`, `#systemic risk`

---