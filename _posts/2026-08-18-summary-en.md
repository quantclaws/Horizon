---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 35 items, 14 important content pieces were selected

---

1. [GPU Offload in Rust: Portable, Safe, and Fast](#item-1) ⭐️ 8.0/10
2. [Preview of DuckDB v2.0 Highlights Upcoming Features](#item-2) ⭐️ 8.0/10
3. [GitHub Service Overload Incident Causes Widespread Disruption](#item-3) ⭐️ 8.0/10
4. [AI-generated Copilot Autofix introduced template injection flaw in Snowflake's Jira workflow](#item-4) ⭐️ 8.0/10
5. [Discussion on AI-generated posts masquerading as human writing sparks debate](#item-5) ⭐️ 8.0/10
6. [Guide and Discussion on Disabling Intrusive AI Features in Software](#item-6) ⭐️ 8.0/10
7. [Qwen 3.8 27B Achieves Score 52 on Artificial Analysis Intelligence Index](#item-7) ⭐️ 8.0/10
8. [AirTag Tracks Rare Books Shipment to Amazon AI Training Facility](#item-8) ⭐️ 8.0/10
9. [Mandatory Structured Payments Cut Pawn Loan Costs by 19% in Mexico City RCT](#item-9) ⭐️ 8.0/10
10. [Study shows Brazil's Pix reduces wage inequality via small-firm wage gains.](#item-10) ⭐️ 8.0/10
11. [Study Tests 'Buy the Rumor, Sell the News' Using LLM-Tagged Financial News](#item-11) ⭐️ 8.0/10
12. [LLMs increase ideological polarization but reduce affective intensity in Reddit political discourse](#item-12) ⭐️ 8.0/10
13. [Survival analysis of 832k pump.fun token launches reveals low graduation rates](#item-13) ⭐️ 8.0/10
14. [Nonstationarity-Complexity Tradeoff Improves Return Prediction](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPU Offload in Rust: Portable, Safe, and Fast](https://arxiv.org/abs/2608.13759) ⭐️ 8.0/10

The paper introduces a portable, safe, and fast GPU offload system for Rust that uses LLVM to enable automatic data movement and lets developers write GPU kernels in safe or unsafe Rust. It enables Rust programmers to target GPUs without vendor‑specific languages or manual bindings, reducing development overhead and promoting safer, more portable high‑performance code. The system relies on LLVM’s Offload infrastructure, employs a two‑pass compilation pipeline to generate native PTX/HIP code for NVIDIA and AMD GPUs, and provides automatic data transfer between host and device.

hackernews · linggen · Aug 17, 17:54 · [Discussion](https://news.ycombinator.com/item?id=49334991)

**Background**: GPU offload refers to executing parts of a program on a graphics processing unit while the rest runs on the CPU. Rust programs are compiled to LLVM Intermediate Representation (IR), which can be targeted to various backends, including GPUs, via LLVM’s Offload infrastructure. Traditionally, Rust developers had to write CUDA/HIP kernels or manage complex bindings to use GPUs, which limited safety and portability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.13759v1">GPU Offload in Rust: Portable, Safe, and Fast - arXiv.org</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/offload/internals.html">GPU offload internals - Rust Compiler Development Guide</a></li>
<li><a href="https://byteiota.com/rust-gpu-offload-hits-rustc-safe-portable-kernels-now/">Rust GPU Offload Hits rustc: Safe, Portable Kernels Now</a></li>

</ul>
</details>

**Discussion**: Commenters expressed enthusiasm for the prospect of writing GPU code directly in Rust to avoid maintaining bindings, while some questioned why the approach goes through LLVM instead of emitting PTX/HIP directly. Others asked whether the implementation code is publicly available and noted the potential impact on HPC and LLM inference workloads.

**Tags**: `#Rust`, `#GPU programming`, `#LLVM`, `#systems programming`, `#parallel computing`

---

<a id="item-2"></a>
## [Preview of DuckDB v2.0 Highlights Upcoming Features](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

On August 17, 2026, DuckDB published a preview blog post outlining the upcoming features and improvements planned for DuckDB v2.0, including new analytics capabilities and runtime enhancements. The preview signals a major upcoming release of a widely used analytical database, promising better performance and broader usability for data engineering and analytics workloads. Highlighted features include the new Quack extension for runtime artifacts, improved out‑of‑core processing, spatial support, tighter dbt integration, and experimental graph capabilities, all built on DuckDB’s columnar storage and vectorized execution engine.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**Background**: DuckDB is an in‑process OLAP database that uses columnar storage with zone maps and lightweight compression to enable fast analytical queries. Its vectorized query execution processes data in fixed‑size chunks (e.g., 1024‑row vectors) allowing operators to apply SIMD and reduce per‑row overhead. Adaptive Radix Tree (ART) indexes are automatically created for primary/unique keys and persisted to speed up selective filters, while the extension system lets users add functionality such as Quack or graph support.

<details><summary>References</summary>
<ul>
<li><a href="https://letsbuildsolutions.com/blog/system-design/how-duckdb-works-internally-vectorized-execution-columnar-storage-and-the-in-process-analytics-engine/">How DuckDB Works Internally: Vectorized Execution, Columnar ...</a></li>
<li><a href="https://www.greybeam.ai/blog/duckdb-internals-part-2">DuckDB Internals: Why is DuckDB Fast? (Part 2 Vectorized Execution) | Greybeam</a></li>
<li><a href="https://duckdb.org/docs/current/guides/performance/indexing">Indexing – DuckDB</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong enthusiasm for DuckDB v2.0, highlighting its speed, spatial support, dbt integration, and the new Quack feature for handling large runtime files. Several users shared real‑world use cases such as real‑time analytics pipelines and out‑of‑core processing on modest hardware, while a few raised questions about whether the recent surge in commits is driven by AI‑assisted development. Overall, the sentiment is positive, with many noting DuckDB’s portability and fun‑to‑use nature as key reasons for adoption.

**Tags**: `#DuckDB`, `#database`, `#analytics`, `#release-preview`, `#data-engineering`

---

<a id="item-3"></a>
## [GitHub Service Overload Incident Causes Widespread Disruption](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) ⭐️ 8.0/10

GitHub users encountered a 'No server is currently available' error, and the platform's status page confirmed an incident (ID: zkxwbgr0cnmx) causing widespread service disruption. The outage underscores GitHub's scaling challenges amid rising traffic, especially from LLM‑generated code, and reignites debate over reliability expectations and possible solutions such as usage‑based pricing. The incident lasted at least three hours, with users unable to view diffs or perform Git operations, while GitHub engineers stated they were still working to identify the root cause.

hackernews · SpyCoder77 · Aug 17, 13:35 · [Discussion](https://news.ycombinator.com/item?id=49330597)

**Background**: GitHub is a widely used code hosting and collaboration platform that aims for high availability, often described as three or four nines of uptime. Its status page provides real‑time incident updates, and past discussions have noted that rapid feature pushes and growth in automated traffic can strain infrastructure.

**Discussion**: Commenters expressed frustration over the prolonged outage, questioned why GitHub has not adopted usage‑based pricing or rate limits to curb LLM‑driven traffic, and some said the incident eroded their confidence in the platform’s reliability.

**Tags**: `#github`, `#outage`, `#scalability`, `#llm-traffic`, `#hackernews`

---

<a id="item-4"></a>
## [AI-generated Copilot Autofix introduced template injection flaw in Snowflake's Jira workflow](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

A security flaw in Snowflake's Jira integration was introduced via an AI-generated code suggestion from GitHub Copilot's Autofix, resulting in template injection within a GitHub Actions workflow. This incident underscores the risks of relying on AI-generated code without proper review, especially in CI/CD pipelines, and highlights the need for static analysis and secure coding practices when using tools like Copilot Autofix. The vulnerable code appeared in the .github/workflows/jira_issue.yml file, where an unsanitized variable expansion allowed template injection; the flaw was introduced in a pull request where Copilot Autofix suggested the problematic line.

hackernews · galnagli · Aug 17, 14:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**Background**: GitHub Copilot Autofix is an AI-powered feature that automatically suggests fixes for code scanning alerts, often generating code changes directly in pull requests. Template injection in GitHub Actions occurs when user‑controlled data is unsafely expanded inside workflow expressions, allowing attackers to execute arbitrary code. Snowflake’s Jira integration uses GitHub Actions workflows to automate issue handling, making such workflows attractive targets for supply‑chain attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/code-security/concepts/code-scanning/copilot-autofix-for-code-scanning">About Copilot Autofix for code scanning - GitHub Docs</a></li>
<li><a href="https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/">How to catch GitHub Actions workflow injections before ...</a></li>
<li><a href="https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/jira-cloud/about">About Openflow Connector for Jira Cloud | Snowflake Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the mistake could easily happen without static analysis, recommended tools like zizmor for CI, criticized YAML’s complexity, and questioned whether the Copilot‑authored commit was actually related to the vulnerability.

**Tags**: `#security`, `#GitHub Actions`, `#AI code generation`, `#GitHub Copilot`, `#vulnerability`

---

<a id="item-5"></a>
## [Discussion on AI-generated posts masquerading as human writing sparks debate](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 8.0/10

A Hacker News post highlights the growing practice of users presenting AI-generated text as if it were written by a human, prompting widespread discussion about authenticity and impact on discourse. This trend raises concerns about eroding trust in online communication, degrading readability, and potentially lowering software quality as AI-generated comments replace meaningful human input. Commenters criticize AI-generated content for being verbose, jargon‑heavy, lacking nuance, and suggest sharing only the prompts used to generate it instead of the full output.

hackernews · mooreds · Aug 17, 19:47 · [Discussion](https://news.ycombinator.com/item?id=49336573)

**Background**: Large language models such as GPT-4 can produce coherent text that mimics human writing, leading to their use in generating comments, documentation, and forum posts. Online communities like Hacker News have long valued authentic human expertise, so the rise of undisclosed AI-generated contributions raises questions about trust, readability, and the value of human‑authored technical communication.

**Discussion**: Many commenters express frustration that AI‑generated posts feel lazy, verbose, and lacking nuance, making them irritating to read. Others acknowledge that AI use is becoming inevitable in workflows, but worry it harms readability and code quality. A recurring suggestion is to share only the AI prompt, as it conveys the actual intent without the filler.

**Tags**: `#AI-generated content`, `#online discourse`, `#readability`, `#software engineering`, `#community reaction`

---

<a id="item-6"></a>
## [Guide and Discussion on Disabling Intrusive AI Features in Software](https://www.librarian.net/notoai/) ⭐️ 8.0/10

A guide hosted at NoToAI.org and an accompanying Hacker News thread detail practical ways to disable or avoid intrusive AI features such as Siri‑dependent CarPlay functions, Microsoft Copilot in Windows 11, Apple Intelligence, and Google AI Overviews in Chrome. As AI becomes deeply embedded in mainstream software, users increasingly seek opt‑out mechanisms to protect privacy, retain control over their workflows, and avoid unwanted automated features. The discussion notes that disabling Siri for CarPlay may break certain functions unless developers provide fallbacks, that Copilot can be turned off via Settings or enterprise policies, that Google AI Overviews can be hidden using the “web” filter or browser extensions, and that switching to Linux or privacy‑focused browsers like LibreWolf and Waterfox removes many AI integrations.

hackernews · ColinWright · Aug 17, 14:07 · [Discussion](https://news.ycombinator.com/item?id=49331220)

**Background**: Modern operating systems and applications increasingly bundle AI assistants—such as Apple’s Siri and Apple Intelligence, Microsoft’s Copilot, and Google’s AI‑powered search overlays—to provide proactive help, but these features often run continuously, collect user data, and cannot be easily disabled without navigating obscure settings or accepting loss of functionality. Privacy advocates argue that forced AI erodes user autonomy and raises concerns about data profiling, prompting a growing demand for transparent opt‑out options and alternative software stacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomsguide.com/computing/software/how-disable-copilot-in-windows-11">How to disable Copilot in Windows 11 | Tom's Guide</a></li>
<li><a href="https://proton.me/blog/turn-off-copilot">How to turn off Copilot AI — and why you should | Proton</a></li>
<li><a href="https://www.wikihow.com/Turn-Off-Google-Ai-Overviews">How to Disable Google AI Overviews & Get Real Search Results</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration that disabling AI sometimes breaks dependent features (e.g., Siri for CarPlay texting) and advocated switching to Linux, using privacy‑focused browsers like LibreWolf and Waterfox, or sticking with older iPhone models that lack newer AI. Some noted that enterprise policies allow full Copilot removal, while others highlighted the guide’s short URL NoToAI.org as a resource for sharing additional opt‑out tips.

**Tags**: `#AI ethics`, `#user privacy`, `#software freedom`, `#open source`, `#AI opt-out`

---

<a id="item-7"></a>
## [Qwen 3.8 27B Achieves Score 52 on Artificial Analysis Intelligence Index](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 8.0/10

Qwen 3.8 27B, a 27-billion-parameter model, scored 52 on the Artificial Analysis Intelligence Index, matching GPT-5.6 Luna's maximum score and trailing only slightly behind larger models such as GLM-5.2 and DeepSeek V4 Pro 0813. This result shows that a relatively compact model can achieve performance comparable to much larger state-of-the-art models, highlighting advances in model efficiency and parameter utilization. The Qwen 3.8 27B model generated 160M tokens during evaluation, far above the median of 43M, indicating verbose output; it is a dense, open-weight vision-language model suited for coding, professional work, research, and long-horizon agentic tasks.

rss · Simon Willison · Aug 17, 23:58

**Background**: The Artificial Analysis Intelligence Index is a composite benchmark that aggregates nine challenging evaluations across mathematics, science, coding, and reasoning to measure overall AI capabilities. Qwen is a series of large language models developed by Alibaba Cloud, with Qwen 3.8 27B being a dense, open-weight vision-language model containing 27 billion parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index</a></li>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen 3 . 8 27 B - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://www.jetson-ai-lab.com/models/qwen3-8-27b/">Qwen 3 . 8 27 B | Jetson AI Lab</a></li>

</ul>
</details>

**Tags**: `#ai`, `#llms`, `#qwen`, `#artificial-analysis`, `#model-efficiency`

---

<a id="item-8"></a>
## [AirTag Tracks Rare Books Shipment to Amazon AI Training Facility](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media placed an Apple AirTag in a shipment of about 1,000 rare books bought on Biblio and traced it to the VGT3 corner of Amazon's LAS8 facility in Las Vegas, revealing the destination as an AI training site. The investigation exposes how AI companies acquire large volumes of potentially copyrighted books for training data, highlighting ethical and copyright concerns and shedding light on opaque data‑sourcing practices in the industry. The AirTag was hidden in one book of the order; the shipment arrived at Amazon's LAS8 facility in northeast Las Vegas, where internal forum posts from Amazon workers indicate destructive scanning of large book volumes for AI training.

rss · Simon Willison · Aug 17, 15:21

**Background**: AI models require vast amounts of text data, leading companies to seek large volumes of books, often through second‑hand marketplaces like Biblio. AirTags are consumer‑grade trackers that can be used to monitor shipments via Apple's Find My network. Prior reports, such as Anthropic’s book scanning in mid‑2025, have suggested similar patterns of AI firms acquiring books for training.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html">Amazon opens $11 billion AI data center in rural Indiana as rivals race to break ground</a></li>
<li><a href="https://ecommerceparadise.com/biblio-review-2026/">Biblio Review 2026: The Best Marketplace for Used and Rare Books ?</a></li>
<li><a href="https://www.strategictracking.com/2026/01/28/why-apples-new-airtag-wont-solve-your-shipment-tracking-problem-part-1/">AirTag for Enterprise? Why Consumer Trackers Fail Supply Chain...</a></li>

</ul>
</details>

**Tags**: `#AI training data`, `#copyright`, `#investigative journalism`, `#Amazon`, `#rare books`

---

<a id="item-9"></a>
## [Mandatory Structured Payments Cut Pawn Loan Costs by 19% in Mexico City RCT](https://arxiv.org/abs/2608.13775) ⭐️ 8.0/10

An RCT in Mexico City assigned borrowers to mandatory frequent-payment structured repayment, flexible repayment, or a choice between the two. Assigning structured payments reduced borrowers' financial cost by 19% on average and lowered default probability by 17.5%. The findings show that mandating structured repayment can significantly lower costs and default risk even when few borrowers would choose it voluntarily, offering policy insights for improving credit contracts in informal lending markets. Only 11% of borrowers voluntarily selected the structured repayment option, yet nearly all borrowers benefited from reduced costs when assigned to it, and the study found no evidence of selection on gains in cost savings.

rss · arXiv Quantitative Finance · Aug 17, 04:00

**Background**: Pawn loans allow borrowers to repay flexibly but impose a harsh penalty—loss of collateral worth more than the loan plus any payments made—if they default. Structured repayment contracts require regular, predetermined payments, reducing flexibility but potentially lowering the risk of default and overall cost. Randomized controlled trials (RCTs) are used to isolate causal effects of contract design by randomly assigning borrowers to different repayment schemes. This study leverages a large RCT in Mexico City to compare mandatory structured payments, the status‑quo flexible payments, and a choice between them.

**Tags**: `#pawnshop lending`, `#randomized controlled trial`, `#credit contracts`, `#financial inclusion`, `#development economics`

---

<a id="item-10"></a>
## [Study shows Brazil's Pix reduces wage inequality via small-firm wage gains.](https://arxiv.org/abs/2608.13871) ⭐️ 8.0/10

The paper finds that Brazil's instant payment system Pix increased wages in small establishments relative to large ones and lowered overall wage inequality, especially in cash-intensive sectors such as retail and services. The results highlight how a fintech innovation can counteract skill‑biased technological change, offering policymakers a tool to reduce wage inequality while boosting demand for low‑skill labor in cash‑intensive industries. Using a triple‑difference design that combines pre‑Pix mobile‑phone penetration, the differential impact of Pix on small versus large firms, and the rollout timing, the authors find significant wage gains in the lower half of the earnings distribution with no effect at the top, and a calibrated monopsony model shows uniform Pix adoption would shrink both within‑ and between‑municipality wage dispersion.

rss · arXiv Quantitative Finance · Aug 17, 04:00

**Background**: Pix is Brazil's instant payment system created by the Central Bank to reduce cash reliance, offering low‑cost, real‑time transfers available 24/7. The study uses a triple‑difference design that interacts pre‑Pix mobile‑phone penetration, the differential effect of Pix on small versus large establishments, and the timing of Pix’s rollout. This approach isolates the causal impact of Pix on wages while controlling for regional trends and firm‑size differences, building on the labor‑economics tradition of difference‑in‑differences methods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pix_(payment_system)">Pix (payment system) - Wikipedia</a></li>
<li><a href="https://mixtape.scunning.com/08b-complex_diff_in_diff">10 Complex Diff -in- Diff Designs – Causal Inference*The Remix</a></li>

</ul>
</details>

**Tags**: `#fintech`, `#labor economics`, `#wage inequality`, `#instant payments`, `#Brazil Pix`

---

<a id="item-11"></a>
## [Study Tests 'Buy the Rumor, Sell the News' Using LLM-Tagged Financial News](https://arxiv.org/abs/2608.14014) ⭐️ 8.0/10

Researchers analyzed 4.57 million financial news articles covering roughly 3,000 US stocks from 2023 to 2026, using an LLM‑derived classifier to tag each article with 17 event types and five attributes, then measured beta‑adjusted abnormal returns around 1.68 million stock‑day events to test the adage. The findings reveal how quickly markets incorporate public information, showing that price moves largely occur before or at news release and that fundamental news continues to drift while story‑driven news reverses, offering actionable insights for traders and improving news‑conditioned forecasting models. Across all signed events, the cumulative price move in the news direction by the close of the publication day is 2.8 times its value 20 days later; for rumor‑flagged events the rumor day captures the entire move while the confirmation day adds nothing. Fundamental news (earnings, dividends, guidance, analyst actions) keeps drifting in the news direction for weeks, whereas soft story‑driven news (launches, macro commentary, leadership) gives back its move, and volatility rises before publication and falls afterward as uncertainty is resolved.

rss · arXiv Quantitative Finance · Aug 17, 04:00

**Background**: Beta‑adjusted abnormal returns measure a stock’s return relative to the market after adjusting for its systematic risk (beta), allowing researchers to isolate the price impact of a specific event. Event study methodology aggregates these abnormal returns around a defined event window to test whether security prices react to news. In this paper, a large language model teacher was distilled into a compact classifier via active learning, which selects the most informative samples for annotation to create an efficient, scalable tagging system for millions of news articles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/a/abnormalreturn.asp">investopedia.com/terms/a/abnormalreturn.asp</a></li>
<li><a href="https://www.academia.edu/97028510/The_Event_Study_Methodology_Since_1969">(PDF) The Event Study Methodology Since 1969</a></li>
<li><a href="https://arxiv.org/pdf/2403.06414">Evolving Knowledge Distillation with Large Language Models and</a></li>

</ul>
</details>

**Tags**: `#finance`, `#market efficiency`, `#natural language processing`, `#event study`, `#abnormal returns`

---

<a id="item-12"></a>
## [LLMs increase ideological polarization but reduce affective intensity in Reddit political discourse](https://arxiv.org/abs/2601.20238) ⭐️ 8.0/10

Analyzing millions of Reddit comments after the release of ChatGPT, researchers found that LLM‑assisted comments made liberal users post more liberal content and conservative users post more conservative content, increasing ideological polarization, while simultaneously lowering measures of hostility and toxicity, indicating reduced affective polarization. The results show that AI can deepen ideological divides while fostering more civil online exchanges, challenging the assumption that extreme views inevitably lead to incivility and informing platform moderation and AI design policies. Mechanism tests indicate the effect stems from LLM‑assisted comments echoing and reinforcing the original post’s viewpoint (algorithmic sycophancy), not from producing more persuasive or extreme original content; falsification tests ruled out confounding events such as the 2022 U.S. midterm elections; affective polarization was measured by declining hostility and toxicity scores.

rss · arXiv Quantitative Finance · Aug 17, 04:00

**Background**: Large language models such as ChatGPT have become widely used for generating text in online forums, influencing how users express political opinions. Ideological polarization measures the extent to which users adopt more extreme liberal or conservative positions, while affective polarization captures the level of hostility, toxicity, or emotional intensity in discourse. Previous research often assumed that increases in ideological extremity accompany rises in incivility, but this study examines whether LLMs can decouple the two phenomena on Reddit’s largest political community.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/23808985.2021.1976070">The role of ( social ) media in political polarization : a systematic review</a></li>
<li><a href="https://academic.oup.com/ej/article/132/643/1037/6490125">Emotion and Reason in Political Language | The Economic Journal | Oxford Academic</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#political discourse`, `#ideological polarization`, `#affective tone`, `#social media analysis`

---

<a id="item-13"></a>
## [Survival analysis of 832k pump.fun token launches reveals low graduation rates](https://arxiv.org/abs/2607.02823) ⭐️ 8.0/10

The study applied Kaplan‑Meier and Cox proportional‑hazards survival analysis to 832,941 Solana pump.fun token launches observed from May 8 to June 10 2026, estimating a fast‑regime graduation rate of 0.198% and releasing the full dataset. It also introduced the Graduation Regime Windows framework to compare launch windows. Providing a rigorous, large‑scale empirical baseline for token graduation rates helps researchers and developers assess tokenomics models and compare across time periods. The released dataset enables further survival‑analysis studies in blockchain ecosystems. The pooled graduation rate is 0.198% (Wilson 95% CI [0.189%,0.208%]), with a steady‑state estimate of 0.207%; Telegram‑channel launches show an 8.94× lift (Cox HR 5.40, 95% CI [4.73,6.17]). Initial market cap above the 30 SOL default is the strongest predictor (Cox HR 4.51) and the model’s concordance is 0.858.

rss · arXiv Quantitative Finance · Aug 17, 04:00

**Background**: Survival analysis studies the time until an event of interest occurs; the Kaplan‑Meier estimator produces a non‑parametric survival curve, while the Cox proportional‑hazards model assesses how covariates affect the hazard rate under a proportional hazards assumption. In the pump.fun ecosystem, a token “graduates” when it meets the platform’s bonding‑curve threshold and transitions to a tradable state. The paper observes launches over a 34‑day window, treating graduation as the event and applying these methods to estimate rates and identify predictive factors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/medicine-and-dentistry/kaplan-meier-method">sciencedirect.com/topics/medicine-and-dentistry/ kaplan - meier -method</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proportional_hazards_model">Proportional hazards model - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2607.02823">Pump.fun Graduation Regime Windows - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#blockchain`, `#tokenomics`, `#survival analysis`, `#Solana`, `#pump.fun`

---

<a id="item-14"></a>
## [Nonstationarity-Complexity Tradeoff Improves Return Prediction](https://arxiv.org/abs/2512.23596) ⭐️ 8.0/10

The paper formalizes the nonstationarity‑complexity tradeoff in financial return prediction and introduces an adaptive selection procedure that jointly optimizes model class and training window length. Empirical tests on three decades of U.S. equity data show a 14% out‑of‑sample R² improvement over fixed‑window and regime‑switching benchmarks. By providing a provable‑guarantee adaptive method, the work offers practitioners a principled way to balance model flexibility against data relevance in non‑stationary markets. The demonstrated gains, especially during recessions, suggest broader applicability for improving asset‑return forecasts and risk‑management models. The adaptive selection procedure uses a tournament‑style evaluation of candidate model‑window pairs on non‑stationary validation data, selecting the pair with the best estimated performance. Theoretical analysis shows the method’s regret is bounded relative to the best fixed pair in hindsight, and empirical results reveal large improvements during periods of high market stress.

rss · arXiv Quantitative Finance · Aug 17, 04:00

**Background**: In financial markets, return‑generating processes often shift over time, making historical data less informative for future predictions—a phenomenon known as non‑stationarity. More complex models can capture intricate patterns but require longer training windows, which risk incorporating outdated regimes, whereas simpler models are less data‑hungry and more robust to such shifts. Prior work has compared fixed‑window estimates and regime‑switching benchmarks, but lacked a joint theory of how model complexity and window length should be tuned together. This paper fills that gap by formalizing the tradeoff and proposing an adaptive selection method.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.23596">The Nonstationarity-Complexity Tradeoff in Return Prediction The Nonstationarity-Complexity Tradeoff in Return Prediction Nonstationarity-Complexity Tradeoff in Return Prediction The Nonstationarity-Complexity Tradeoff in Return Prediction The nonstationarity-complexity tradeoff in return prediction The Nonstationarity-Complexity Tradeoff in Return Prediction</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5980654">The Nonstationarity-Complexity Tradeoff in Return Prediction</a></li>
<li><a href="https://arxiv.org/pdf/2512.23596">The Nonstationarity-Complexity Tradeoff in Return Prediction</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#finance`, `#time series`, `#nonstationarity`, `#model selection`

---