---
layout: default
title: "Horizon Summary: 2026-07-25 (EN)"
date: 2026-07-25
lang: en
---

> From 39 items, 15 important content pieces were selected

---

1. [Anthropic releases Claude Opus 5 with improved capabilities and no data retention](#item-1) ⭐️ 8.0/10
2. [Postgres LISTEN/NOTIFY actually scales](#item-2) ⭐️ 8.0/10
3. [Security camera vendor leaked GitHub admin token.](#item-3) ⭐️ 8.0/10
4. [Why Software Quality Declines Despite Solved Coding](#item-4) ⭐️ 8.0/10
5. [Nvidia, Microsoft, Meta Warn Against Overregulating Open-Weight AI Models](#item-5) ⭐️ 8.0/10
6. [Buz: Bun fork in Zig achieves sub‑second incremental builds](#item-6) ⭐️ 8.0/10
7. [Electricity demand has not become more price-responsive despite ninety years of technological change](#item-7) ⭐️ 8.0/10
8. [From Keyword Links to AI-Agent Delegated Decision-Making in Digital Search.](#item-8) ⭐️ 8.0/10
9. [Group boarding for airplanes: benchmarking static policies and optimizing dynamic assignment with deep reinforcement learning](#item-9) ⭐️ 8.0/10
10. [Human-AI Substitution Principle Predicts AI Replacement in Hierarchical Organizations](#item-10) ⭐️ 8.0/10
11. [Study Finds No Grade Inflation from Generative AI Availability in University Courses](#item-11) ⭐️ 8.0/10
12. [Resume audit links hiring discrimination to job task content.](#item-12) ⭐️ 8.0/10
13. [Uniform-Loss AMM Framework for Prediction Markets Introduced](#item-13) ⭐️ 8.0/10
14. [DatedGPT: Preventing Lookahead Bias in LLMs with Time-Aware Pretraining](#item-14) ⭐️ 8.0/10
15. [Study Shows AI Progress Follows Rising Tide, Not Abrupt Waves](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic releases Claude Opus 5 with improved capabilities and no data retention](https://www.anthropic.com/news/claude-opus-5) ⭐️ 8.0/10

Anthropic unveiled Claude Opus 5, the latest version of its flagship large language model, delivering improved reasoning, coding, and agentic abilities while keeping the $5/$25 per million token pricing and a 1M-token context window. Importantly, the model retains the no-data-retention policy for general access, addressing privacy concerns. By eliminating data retention requirements, Claude Opus 5 appeals to enterprises in regulated sectors that need strict data privacy, while its strong performance on coding and agentic tasks makes it a competitive choice for complex AI workflows. The release also highlights the growing importance of model routing and pricing transparency in the expanding LLM marketplace. According to its system card, Claude Opus 5 supports multilingual text-only output, features a 1,000,000‑token context window with a maximum output of 128,000 tokens, and is offered via API at $5 per million input tokens and $25 per million output tokens. The model is multilingual, typically responding in the same language as the user's input, and does not retain user data for general access.

hackernews · alvis · Jul 24, 16:57 · [Discussion](https://news.ycombinator.com/item?id=49038433)

**Background**: Claude is Anthropic's family of large language models designed for reasoning, coding, and agentic tasks, with earlier versions such as Claude Opus 4 and Opus 4.5 setting benchmarks in helpfulness and safety. The Opus series is known for its strong performance on expert uplift trials and agentic coding evaluations, while maintaining a commitment to minimal data retention. Claude Opus 5 continues this lineage, offering a 1M-token context window and unchanged pricing, while emphasizing text‑only, multilingual output. Its release reflects Anthropic's strategy of delivering frontier‑class capabilities without imposing data storage obligations on users.

<details><summary>References</summary>
<ul>
<li><a href="https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude+Opus+5+System+Card.pdf">Claude Opus 5 System Card</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.marktechpost.com/2026/07/24/meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing/">Meet the New Claude Opus 5: Frontier-Class Agentic Coding and Computer Use at Unchanged Opus Pricing - MarkTechPost</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the lack of data retention as the model's most important advantage over competitors like Fable. Some noted Opus 5's superior image‑to‑HTML conversion accuracy compared to Fable, while others observed that its writing style retains characteristic 'Claude‑isms' from earlier Opus releases. A few users pointed out the rapid growth of model routing as a response to the increasing variety of models, modalities, and pricing options.

**Tags**: `#Claude Opus 5`, `#Anthropic`, `#LLM release`, `#AI models`, `#data retention`

---

<a id="item-2"></a>
## [Postgres LISTEN/NOTIFY actually scales](https://www.dbos.dev/blog/postgres-listen-notify-scalability) ⭐️ 8.0/10

The DBOS blog shows that Postgres LISTEN/NOTIFY can sustain 60,000 writes per second on a single server with millisecond latency, demonstrating it can handle high‑throughput pub/sub workloads. This challenges the common belief that LISTEN/NOTIFY doesn’t scale, opening the door for using Postgres as a low‑latency durable message broker in real‑time applications without external queues. The benchmark was achieved by optimizing locking and batching, while respecting the 8000‑byte payload limit and same‑database restriction; earlier versions suffered from poor locking that has since been corrected.

hackernews · KraftyOne · Jul 24, 19:05 · [Discussion](https://news.ycombinator.com/item?id=49040296)

**Background**: PostgreSQL LISTEN/NOTIFY is an asynchronous server‑to‑client notification mechanism: a session executes NOTIFY channel [payload] and any session that has previously executed LISTEN channel receives the event. The payload is limited to 8000 bytes and the feature works only within the same database instance. Traditionally used for lightweight pub/sub, it was thought not to scale because all notifications share a single database instance and can suffer from locking contention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dbos.dev/blog/postgres-listen-notify-scalability">Postgres LISTEN/NOTIFY Actually Scales | DBOS</a></li>
<li><a href="https://www.postgresql.org/docs/current/sql-notify.html">PostgreSQL: Documentation: 18: NOTIFY</a></li>
<li><a href="https://www.cybertec-postgresql.com/en/listen-notify-automatic-client-notification-in-postgresql/">LISTEN / NOTIFY: Automatic client notification in PostgreSQL</a></li>

</ul>
</details>

**Discussion**: Commenters noted that scalability is a continuum, with jerf emphasizing that 60K writes/s may be ample for some workloads and insufficient for others. nzoschke praised DBOS for leveraging Postgres effectively, while dang linked to an earlier HN post questioning LISTEN/NOTIFY scaling. vhiremath4 shared experience building a queue on LISTEN/NOTIFY for strong consistency, and dietr1ch recalled early locking issues that have since been corrected. Overall, the discussion reflects interest in the new benchmarks, acknowledgment of limits, and appreciation for DBOS’s optimizations.

**Tags**: `#Postgres`, `#LISTEN/NOTIFY`, `#scalability`, `#pub/sub`, `#database`

---

<a id="item-3"></a>
## [Security camera vendor leaked GitHub admin token.](https://hhh.hn/hanwha-github-token/) ⭐️ 8.0/10

A security camera vendor inadvertently embedded a GitHub admin token in the login page of its device, making the token visible in the page’s source code. The exposed token granted admin‑level access to the vendor’s GitHub repositories. This incident shows how hardcoded credentials in IoT hardware can lead to supply‑chain compromises, allowing attackers to steal source code, manipulate CI/CD pipelines, or inject malicious code. It underscores the need for rigorous secret‑management practices in device firmware. The token appeared as a plaintext string in the login page’s HTML/JavaScript, providing admin scopes that could read, modify, or delete private repositories and trigger GitHub Actions. Revoking the token and auditing all systems that relied on it are essential mitigation steps.

hackernews · hhh · Jul 24, 11:54 · [Discussion](https://news.ycombinator.com/item?id=49034292)

**Background**: IoT devices frequently ship with hardcoded credentials such as default passwords or API keys, which attackers can extract from firmware or web interfaces to gain unauthorized access. A GitHub personal access token (PAT) functions like a password for API access, and if it possesses admin scopes, it can read, modify, or delete repositories and trigger CI/CD jobs. Supply‑chain attacks that embed such tokens in consumer hardware can therefore compromise both the vendor’s internal development environment and any downstream users who rely on that code.

<details><summary>References</summary>
<ul>
<li><a href="https://aiespionage.net/cybersecurity/my-security-camera-shipped-a-github-admin-token-in-its-login-page/">My Security Camera Shipped A GitHub Admin Token In Its Login Page</a></li>
<li><a href="https://www.techtarget.com/searchsecurity/tip/How-hard-coded-credentials-threaten-industrial-control-systems">How hard - coded credentials threaten ICS security | TechTarget</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the widespread problem of hardcoded secrets in IoT firmware, recommended placing cameras on a VLAN without internet access, and questioned the availability of white‑label cameras with open or customizable firmware. Some expressed distrust of Korean security products and recalled historical workarounds for private IP address allocation.

**Tags**: `#IoT security`, `#supply chain`, `#hardcoded credentials`, `#GitHub token`, `#vulnerability`

---

<a id="item-4"></a>
## [Why Software Quality Declines Despite Solved Coding](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/) ⭐️ 8.0/10

The essay argues that, although coding problems are largely solved, software quality is deteriorating because of misaligned incentives, constant tool churn, and non-technical decision‑makers driving change. It highlights how systemic incentive structures in tech companies undermine product reliability, affecting developers and end‑users alike, and suggests a need to realign rewards toward quality rather than novelty. The post cites examples such as engineers being promoted for building shiny new tools, the proliferation of overlapping tools within organizations, and specific frustrations like macOS focus‑stealing bugs that erode user trust.

hackernews · pchm · Jul 24, 09:08 · [Discussion](https://news.ycombinator.com/item?id=49033004)

**Discussion**: Commenters largely agree that incentives drive wasteful tool creation, express dread over software updates, and criticize non‑technical leaders for prioritizing novelty over stability, while also noting concrete annoyances such as focus‑stealing in Slack.

**Tags**: `#software engineering`, `#software quality`, `#incentives`, `#tech industry`, `#productivity`

---

<a id="item-5"></a>
## [Nvidia, Microsoft, Meta Warn Against Overregulating Open-Weight AI Models](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) ⭐️ 8.0/10

Nvidia, Microsoft, and Meta jointly released a letter urging the U.S. government to avoid overregulating open-weight AI models to protect innovation and maintain American leadership. The joint stance signals major tech industry influence on AI policy and could shape future U.S. regulation, affecting developers, startups, and global competitiveness in AI. The letter is available as a PDF from Nvidia's site, was highlighted by Jensen Huang's tweet, and references related debates about open-weight versus open-source models.

hackernews · louiereederson · Jul 24, 13:32 · [Discussion](https://news.ycombinator.com/item?id=49035303)

**Background**: Open-weight models release the learned parameters (weights) publicly, allowing anyone to download and use them, though they may not include the model's source code, training data, or training process. In contrast, open-source models provide the weights together with full source code, training scripts, and often the dataset, enabling users to study, modify, and retrain the model from scratch. U.S. policymakers are currently weighing AI regulation, and companies warn that excessive restrictions could stifle innovation and weaken America's position in the global AI race.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://medium.com/lets-code-future/open-weight-ai-models-what-they-are-and-why-openais-next-move-matters-f86fe481973a">Open-Weight AI Models: What They Are, and Why OpenAI’s Next Move Matters</a></li>
<li><a href="https://www.linkedin.com/posts/wisestack-ai_gptoss-opensource-openweight-activity-7359896881591701504-jEyz">Open weight models vs open source models : what's the... | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Commenters pointed out Anthropic's lobbying for regulation and noted the irony of using models like Kimi while advocating restrictions. Others warned that closed‑source interests are trying to ban open weights, drawing parallels to past debates like SOPA, and speculated about behind‑the‑scenes motives for the joint letter. Some referenced related HN discussions where startup founders urged the U.S. not to cut off Chinese open‑weight AI.

**Tags**: `#AI regulation`, `#open-weight models`, `#tech policy`, `#Nvidia`, `#Microsoft`, `#Meta`

---

<a id="item-6"></a>
## [Buz: Bun fork in Zig achieves sub‑second incremental builds](https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891) ⭐️ 8.0/10

Buz is a WIP fork of Bun rewritten in modern Zig that removes over 11,000 lines of dead code and delivers sub‑second incremental builds by leveraging Zig’s standard library. The project shows that significant performance gains in JavaScript tooling are possible today by cleaning up dead code and adopting Zig, potentially influencing future Bundler and runtime designs. Buz currently lacks production readiness, does not support Zig incremental compilation on aarch64, and only the Linux linker supports binary patching; it relies on Zig stdlib and has removed over 11k lines of dead code.

hackernews · kristoff_it · Jul 24, 09:26 · [Discussion](https://news.ycombinator.com/item?id=49033099)

**Background**: Bun is a fast JavaScript runtime and toolchain that aims to replace Node.js with quicker startup and built-in transpilation. Zig is a general‑purpose system programming language emphasizing safety, performance, and seamless C interoperability, with a growing standard library. Incremental builds reuse previous build outputs to recompile only changed files, dramatically reducing rebuild times during development.

<details><summary>References</summary>
<ul>
<li><a href="https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891">Buz - A drop-in replacement for Bun using modern Zig, with sub-1s incremental builds - Showcase - Ziggit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://rushjs.io/pages/advanced/incremental_builds/">Incremental builds | Rush</a></li>

</ul>
</details>

**Discussion**: Commenters were astonished that over 11,000 lines of dead code had accumulated in Bun, seeing the fork as proof that faster builds were possible all along. They also pointed out remaining hurdles such as lack of aarch64 support for Zig incremental compilation and Linux‑only binary patching, while some humorously noted the irony of using LLMs to clean up LLM‑generated mess.

**Tags**: `#JavaScript tooling`, `#Zig`, `#Bun`, `#incremental builds`, `#open-source fork`

---

<a id="item-7"></a>
## [Electricity demand has not become more price-responsive despite ninety years of technological change](https://arxiv.org/abs/2607.21285) ⭐️ 8.0/10

A meta‑analysis of 4,720 own‑price elasticity estimates from 462 studies covering 1934‑2024 finds that the best‑identified short‑run elasticity is about –0.09, statistically indistinguishable from zero, and shows no upward trend over nine decades. The result challenges a core assumption in decarbonization planning that electricity demand will grow more price‑responsive with metering, automation, and storage, indicating that price alone cannot deliver the needed flexibility and must be supplemented by engineered solutions. After correcting for publication bias, naive estimates give a short‑run elasticity of –0.16 (a 10% price rise cuts consumption by <2%), while the best‑identified studies yield –0.09; long‑run elasticity is about –0.38, and the pattern of increasing responsiveness with adjustment time has been stable for decades, with technology‑rich settings actually showing the lowest total responsiveness.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: Price elasticity of electricity demand measures the percentage change in consumption resulting from a one percent change in price, a key input for energy system models and decarbonization scenarios. Economists assess the credibility of elasticity estimates using an identification quality ladder that ranges from simple regressions to randomized experiments, with higher rungs providing more credible causal inference. Publication bias—where statistically significant results are more likely to be published—can inflate average elasticity estimates in meta‑analyses, necessitating correction techniques to obtain unbiased results.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/269693689_Price_Elasticity_of_Demand_for_Electricity_A_Primer_and_Synthesis">(PDF) Price Elasticity of Demand for Electricity : A Primer and...</a></li>
<li><a href="https://www.aje.com/arc/assessing-and-avoiding-publication-bias-in-meta-analyses">Assessing and Avoiding Publication Bias in Meta - analyses | AJE</a></li>
<li><a href="https://openlibrary.org/works/OL1906567W/The_identification_problem_in_econometrics">The identification problem in econometrics by... | Open Library</a></li>

</ul>
</details>

**Tags**: `#energy economics`, `#electricity demand`, `#price elasticity`, `#decarbonization`, `#meta-analysis`

---

<a id="item-8"></a>
## [From Keyword Links to AI-Agent Delegated Decision-Making in Digital Search.](https://arxiv.org/abs/2607.21459) ⭐️ 8.0/10

The paper announces arXiv:2607.21459v1, describing how digital search is shifting from traditional keyword-based queries and ranked link lists to AI-agent mediated delegated decision-making, where users state goals in natural language and agents execute decisions. This change moves search from a link-based interface to an embedded system component affecting transparency, competition, and monetization. This transformation matters because it redefines how information quality, trust, and incentive alignment are managed in search, with small design choices having first‑order effects on efficiency, competition, and consumer and firm welfare. It highlights the need for open, transparent, and competitive agentic systems to shape future market structure and policy. The authors note that design elements such as how stakeholders access information, how options are surfaced, and how actions are executed critically influence outcomes, supported by early evidence from experimental agent‑mediated marketplaces and economic theory. These findings suggest that incremental ranking improvements are less impactful than the architecture of the agentic decision‑making system.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: In traditional digital search, users translate intent into keyword‑based queries, evaluate ranked lists of links, and act on decisions outside the search interface. In an AI‑native setting, users express goals in natural language, agents interpret these intentions, and return recommendations or execute decisions directly, embodying delegated decision‑making. This shift raises concerns about transparency, bias, and market power, while agent‑mediated marketplaces automate matchmaking, scheduling, and pricing, influencing competition and welfare.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.21459">The Evolution of Digital Search: From Blue Links to Delegated ...</a></li>
<li><a href="https://medium.com/@drjohnmillar/when-the-buyer-is-a-machine-why-agentic-commerce-threatens-the-trillion-dollar-advertising-model-d8a03a583ffc">When the Buyer Is a Machine: Why Agentic Commerce... | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/umeshkribanandan_agenticcommerce-ecommerce-ai-activity-7414969236885942272-Ve9T">#agenticcommerce #ecommerce # ai #retail #digitalcommerce # search ...</a></li>

</ul>
</details>

**Tags**: `#information retrieval`, `#AI agents`, `#search engines`, `#market design`, `#human-computer interaction`

---

<a id="item-9"></a>
## [Group boarding for airplanes: benchmarking static policies and optimizing dynamic assignment with deep reinforcement learning](https://arxiv.org/abs/2607.21512) ⭐️ 8.0/10

The paper introduces a dynamic airplane boarding group assignment formulated as a Markov decision process and solved with proximal policy optimization (PPO) using a convolutional neural network to encode the seat‑assignment state. It outperforms static back‑to‑front boarding by up to 9.8% in total time and 22.8% in average individual boarding time across six aircraft layouts. Improving boarding efficiency directly reduces aircraft turnaround time, lowers operational costs, and enhances passenger experience, making the approach valuable for airlines and airports. By bridging reinforcement learning with operations research, the work showcases how AI can optimize real‑world stochastic processes such as passenger boarding. The policy uses a CNN to process a binary matrix representing occupied seats, groups, and luggage, and is trained with PPO to maximize a reward that balances total boarding time and average individual boarding time. Experiments cover six single‑ and double‑aisle configurations, varying load factors, companion sizes, and luggage loads, showing robustness under out‑of‑distribution conditions.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: Airplane boarding typically assigns passengers to a few sequential groups based on static rules such as back‑to‑front or optimized block patterns, which ignore the randomness of arrival times and seat choices. Reinforcement learning formulates decision‑making as a Markov decision process where an agent learns a policy to maximize cumulative reward through interaction with an environment. Proximal policy optimization (PPO) is a widely used RL algorithm that stabilizes training via a clipped surrogate objective, and convolutional neural networks excel at extracting spatial patterns from grid‑like inputs such as seat maps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proximal_policy_optimization">Proximal policy optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Convolutional_neural_network">Convolutional neural network - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2607.21512">Group boarding for airplanes : benchmarking static policies and...</a></li>

</ul>
</details>

**Tags**: `#airplane boarding`, `#reinforcement learning`, `#operations research`, `#deep learning`, `#dynamic assignment`

---

<a id="item-10"></a>
## [Human-AI Substitution Principle Predicts AI Replacement in Hierarchical Organizations](https://arxiv.org/abs/2607.20781) ⭐️ 8.0/10

The paper (arXiv:2607.20781v1) introduces an analytical Human‑AI Task Allocation (HAT) model for hierarchical organizations and derives a Human‑AI Substitution Principle that specifies when AI will replace human labor based on the economic asymmetry between human skill acquisition and AI capability scaling. By providing a formal condition for AI‑driven labor substitution, the model offers a rigorous tool for predicting workforce transitions, guiding organizational redesign, and informing AI governance and policy decisions. The HAT model encodes the asymmetry between costly human skill acquisition and scalable AI capabilities, showing that AI adoption can cause abrupt workforce shifts, sustain hybrid human‑AI roles without a minimum‑human fraction, flatten managerial hierarchies, and make middle‑management jobs especially vulnerable, while the vulnerability of highly skilled workers depends on a skill threshold shaped by organizational depth, baseline costs, and risk differentials.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: Hierarchical organizations consist of multiple layers where tasks are allocated based on skill and cost considerations. Human skill acquisition typically involves significant time and investment, whereas AI capabilities can be scaled rapidly with relatively lower marginal cost. This economic asymmetry creates conditions under which AI may become more cost‑effective than human labor for certain tasks. The HAT model formalizes this asymmetry to predict when and where AI will substitute human workers in such structures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.20781">The Human - AI Substitution Principle : When will you be replaced by...</a></li>
<li><a href="https://arxiv.org/abs/2607.20781">The Human-AI Substitution Principle: When will you be replaced by AI in ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Human-AI collaboration`, `#Organizational economics`, `#Task allocation`, `#Substitution principle`

---

<a id="item-11"></a>
## [Study Finds No Grade Inflation from Generative AI Availability in University Courses](https://arxiv.org/abs/2607.21534) ⭐️ 8.0/10

The study analyzed syllabus and administrative data from a large U.S. university (2015‑2025, 156,135 students) using a differences‑in‑differences design and a human‑validated LLM pipeline to assess courses’ susceptibility to generative AI, finding no significant effect on grades or student‑reported understanding and only a transient‑pandemic‑dependent effect on interest. It provides rigorous evidence on whether generative AI leads to grade inflation or reduced satisfaction, informing educators and policymakers about the actual impact of AI on learning outcomes in higher education. The analysis covered 87,936 course offerings, used an LLM‑based pipeline validated by humans to extract assessment types from syllabi, and modeled COVID‑19 effects as either persistent or transient, with interest effects significant only under the transient assumption.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: Differences‑in‑differences (DiD) is a quasi‑experimental method that compares changes over time between a treatment group exposed to an intervention and a control group not exposed, aiming to isolate causal effects. In this study, the treatment is the post‑ChatGPT availability period, and susceptibility is measured by extracting assessment types (e.g., take‑home problem sets, essays) from syllabi using an LLM pipeline that has been validated by human reviewers. This approach allows researchers to test whether courses more amenable to AI assistance show different grade or satisfaction trends after AI becomes widely available.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences - Wikipedia</a></li>
<li><a href="https://python.useinstructor.com/">Instructor - Multi-Language Library for Structured LLM Outputs</a></li>
<li><a href="https://www.researchgate.net/publication/388313672_Appraising_higher_education_assessment_validity_Development_of_the_PANDORA_GenAI_Susceptibility_Rubric">(PDF) Appraising higher education assessment validity: Development...</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#higher education`, `#student performance`, `#AI impact`, `#differences-in-differences`

---

<a id="item-12"></a>
## [Resume audit links hiring discrimination to job task content.](https://arxiv.org/abs/2604.01933) ⭐️ 8.0/10

Researchers submitted 36,880 fake resumes of new college graduates to 9,220 U.S. job advertisements, measuring callback rates by race, gender, and job ad text. They found that callback gaps for Black and Hispanic applicants and women were 28‑43% lower in management occupations and were largest in jobs with high analytical and interpersonal demands but low routine content. The study reveals that discrimination is not uniform across occupations but varies with the specific tasks a job requires, highlighting where bias is most likely to occur. This insight can help employers design more objective hiring practices and guide policymakers targeting interventions to reduce labor market inequities. Using O*NET task measures, the authors defined evaluative discretion as the proportion of hiring decisions based on subjective assessment; they found that subjective evaluation widens callback gaps while objective precision narrows them, and that customer contact amplifies this effect in non‑routine jobs. In management occupations, callback rates were 28‑43% lower for Black men, Black women, White women, and Hispanic men compared with otherwise identical White men.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: O*NET is a U.S. Department of Labor database that provides standardized measures of the tasks, skills, and abilities associated with occupations, which researchers use to quantify job content such as analytical, interpersonal, and routine demands. Evaluative discretion in hiring refers to the share of decisions that rely on subjective judgment rather than objective, verifiable criteria, and prior work shows that greater discretion can allow bias to influence outcomes. A resume audit sends fictitious applications that differ only in protected characteristics (e.g., name signaling race or gender) to real job openings, measuring differences in callback rates as a direct test of discrimination.

<details><summary>References</summary>
<ul>
<li><a href="https://www.onetcenter.org/overview.html">About O * NET at O * NET Resource Center</a></li>
<li><a href="https://arxiv.org/pdf/2604.01933">Hiring Discrimination and the Task Content of Jobs: Evidence from...</a></li>
<li><a href="https://www.nber.org/system/files/working_papers/w21709/w21709.pdf">Discretion in Hiring</a></li>

</ul>
</details>

**Tags**: `#hiring discrimination`, `#resume audit`, `#labor economics`, `#task content`, `#O*NET`

---

<a id="item-13"></a>
## [Uniform-Loss AMM Framework for Prediction Markets Introduced](https://arxiv.org/abs/2607.17428) ⭐️ 8.0/10

The paper introduces uniform automated market makers (AMMs) for prediction markets, defined by the condition that instantaneous loss-versus-rebalancing (LVR) is proportional to pool value and independent of the current token price. It characterizes these AMMs using win-martingale processes and extends the framework to dynamic liquidity management. By providing a theoretical tool to shape how subsidization costs are distributed across price states and over time, the work helps AMM designers and liquidity providers better manage inevitable losses in prediction markets. This advances DeFi market design and could improve the efficiency of belief aggregation mechanisms. Uniform AMMs satisfy LVR ∝ pool value, price‑independent; for any sufficiently regular win‑martingale there exists a pricing function achieving uniform LVR, and conversely such a pricing function induces a win‑martingale. The framework also shows how liquidity levels can be adjusted over time to follow a target expected cumulative loss schedule.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: Automated market makers (AMMs) enable token trading via smart‑contract pools without order books, and in prediction markets they subsidize trading to aggregate beliefs about future events. Loss‑versus‑rebalancing (LVR) measures the cost liquidity providers incur when AMM prices lag behind external markets. A win‑martingale is a stochastic process that models the evolving probability of an event outcome, converging to 0 or 1 at a fixed resolution time.

<details><summary>References</summary>
<ul>
<li><a href="https://cow.fi/learn/what-is-loss-versus-rebalancing-lvr">What is Loss - Versus - Rebalancing ( LVR )? - CoW DAO</a></li>
<li><a href="https://www.emergentmind.com/topics/win-martingales">Win - Martingales : Models and Fluctuation Analysis</a></li>
<li><a href="https://formo.so/glossary/automated-market-maker-amm">Automated Market Maker ( AMM ) | Web3 & DeFi Data Glossary</a></li>

</ul>
</details>

**Tags**: `#Automated Market Makers`, `#Prediction Markets`, `#Loss-Versus-Rebalancing`, `#DeFi`, `#Market Design`

---

<a id="item-14"></a>
## [DatedGPT: Preventing Lookahead Bias in LLMs with Time-Aware Pretraining](https://arxiv.org/abs/2603.11838) ⭐️ 8.0/10

DatedGPT introduces twelve 1.3B‑parameter language models trained from scratch on ~100 B tokens each with strict yearly data cutoffs from 2013 to 2024, paired with a yearly instruction dataset (DatedInstruct) to avoid leakage. On a stock‑return prediction task using 61 k firm‑day news headlines, DatedGPT‑instruct achieves an annualised Sharpe ratio of 3.20, while lookahead‑biased models add a 26.4 b.p. premium per standard deviation. By eliminating lookahead bias, DatedGPT enables trustworthy financial forecasting and provides a controllable benchmark for studying temporal knowledge leakage in LLMs. This approach can be extended to other time‑sensitive domains such as economics, public policy, and scientific discovery. Each model is a 1.3B‑parameter transformer trained on ~100 B tokens; perplexity‑based probing confirms that knowledge is bounded by its cutoff year. Lookahead‑biased models (trained on future data) exhibit a statistically significant 26.4 b.p. Sharpe‑ratio increase per standard deviation, demonstrating the magnitude of the bias.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: Lookahead bias occurs when a language model inadvertently learns future information during training, compromising its usefulness for forecasting tasks. Time‑aware pretraining mitigates this by restricting training data to a specific cutoff and, in some methods, injecting explicit time tokens so the model learns a temporal embedding. Prior work such as ChronoLLM and TiMoE has explored similar strategies, while perplexity‑based probing is a standard technique to verify a model’s effective knowledge cutoff. DatedGPT combines strict annual cutoffs with a matched instruction dataset to ensure both pretraining and post‑training remain leakage‑free.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2512.23847">Detecting Lookahead Bias in LLM Forecasts</a></li>
<li><a href="https://www.researchgate.net/publication/389510389_Chronologically_Consistent_Large_Language_Models">(PDF) Chronologically Consistent Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2508.08827">TiMoE: Time - Aware Mixture of Language Experts</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#lookahead bias`, `#time-aware pretraining`, `#financial forecasting`, `#research paper`

---

<a id="item-15"></a>
## [Study Shows AI Progress Follows Rising Tide, Not Abrupt Waves](https://arxiv.org/abs/2604.01363) ⭐️ 8.0/10

The paper analyzed over 6,000 text‑based tasks from the O*NET database and more than 60,000 worker evaluations, finding that AI performance follows a rising‑tide pattern rather than abrupt crashing waves, with success rates climbing from ~60% in 2024‑Q2 to >70% by 2025‑Q3 and projected to reach 88‑97% by 2030. This challenges the prevailing view that AI capabilities jump in narrow bursts, suggesting instead a broad, steady improvement that affects workforce planning, education, and policy decisions about AI automation. The study used 6,000+ O*NET‑derived tasks and 60,000+ evaluations by experienced workers, measuring success on tasks that take humans ~1.5 hours; in 2024‑Q2 frontier LLMs achieved ~60% success, rising above 70% by 2025‑Q3, and if trends continue they could reach 88‑97% success by 2030.

rss · arXiv Quantitative Finance · Jul 24, 04:00

**Background**: O*NET is the U.S. Department of Labor’s occupational information network, providing a standardized taxonomy of job tasks that researchers use to map AI‑assailable work. The study frames AI automation as a continuum between “crashing waves” (sudden, narrow capability jumps) and “rising tides” (broad, continuous improvement). Large language models (LLMs) are the primary AI systems evaluated, with performance measured by success rates on realistic, time‑bound tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/epoch-ai-taxonomy-ai-rd-automation/">Epoch AI proposes O * NET -style taxonomy for AI R&D automation...</a></li>
<li><a href="https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-1.pdf">AI Use Taxonomy : A Human-Centered Approach</a></li>

</ul>
</details>

**Tags**: `#AI automation`, `#labor market`, `#large language models`, `#task performance`, `#AI impact`

---