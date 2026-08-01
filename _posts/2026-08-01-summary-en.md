---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
---

> From 63 items, 21 important content pieces were selected

---

1. [Stateless MCP 2.0 Release Sparks Renewed Interest and New Tools](#item-1) ⭐️ 9.0/10
2. [AI Voice Agents Boost Job Offer Rates and Retention in Large Field Experiment](#item-2) ⭐️ 9.0/10
3. [Hacker News discussion links elevator algorithms to disk scheduling and games](#item-3) ⭐️ 8.0/10
4. [Introducing qm: A Multiplayer Agent Harness for Collaborative Work](#item-4) ⭐️ 8.0/10
5. [Tailscale details how a leaked reusable auth key led to Hugging Face intrusion](#item-5) ⭐️ 8.0/10
6. [Go Proposes Generic Set and Heap Types in container/ Package](#item-6) ⭐️ 8.0/10
7. [Running Billion‑Edge Graph Algorithms on 5‑10 GB RAM with DataFusion](#item-7) ⭐️ 8.0/10
8. [DeepSeek releases 304B‑parameter V4‑Flash model.](#item-8) ⭐️ 8.0/10
9. [Simon Willison discusses open-weight AI revolution on Oxide and Friends podcast](#item-9) ⭐️ 8.0/10
10. [Lucky or Good? Outcome Noise, Effective Sample Size, and Skill Attribution](#item-10) ⭐️ 8.0/10
11. [Firms' social stances increase revenue via aligned consumer spending.](#item-11) ⭐️ 8.0/10
12. [AI Sycophancy and Decisions](#item-12) ⭐️ 8.0/10
13. [New spatial Econ-SIR model links economy and epidemic dynamics](#item-13) ⭐️ 8.0/10
14. [LLM-enhanced multi-agent model forecasts carbon intensity for low-carbon power dispatch](#item-14) ⭐️ 8.0/10
15. [FinSMART: Market-Aligned RL Framework for Financial Sentiment Analysis](#item-15) ⭐️ 8.0/10
16. [LLM-driven PACE framework improves parent-order execution on Shenzhen Stock Exchange](#item-16) ⭐️ 8.0/10
17. [Optimal Dynamic Fees in Automated Market Makers](#item-17) ⭐️ 8.0/10
18. [Women Worry, Men Adopt? Gendered Risk Perceptions and Generative AI Adoption](#item-18) ⭐️ 8.0/10
19. [Study Shows Irrelevant Text Cuts LLM Accuracy on Graduate Economics Exam by ~12 Points](#item-19) ⭐️ 8.0/10
20. [Continuous-time RL framework for optimal switching with entropy regularization](#item-20) ⭐️ 8.0/10
21. [Study finds intraday Ethereum gas fee peaks tied to arbitrage, firm scheduling varies](#item-21) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stateless MCP 2.0 Release Sparks Renewed Interest and New Tools](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

Simon Willison writes about Stateless MCP day and the MCP 2.0 specification released on 2026-07-28, which simplifies the protocol to a single HTTP request, inspiring his mcp-explorer and datasette-mcp projects. The stateless design reduces implementation complexity and server‑side state, making MCP more scalable and usable by smaller models running on laptops, thereby renewing interest in the LLM tool integration standard. Stateless MCP replaces the two‑request stateful flow (initialize then tools/call) with a single POST that includes MCP‑Protocol‑Version, Mcp‑Method and Mcp‑Name headers; it eliminates the need to track Mcp‑Session‑Id. Simon built mcp‑explorer (a CLI for probing MCP servers) and datasette‑mcp to demonstrate the new workflow.

rss · Simon Willison · Jul 31, 23:13

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to let LLM‑based agents call external tools via a uniform interface. After an initial surge of interest in 2025, attention waned when Anthropic’s Skills showed that a shell with curl could achieve similar flexibility. The new stateless MCP 2.0 specification, released July 28, 2026, simplifies the protocol by removing session state, improving scalability and ease of implementation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>

</ul>
</details>

**Tags**: `#Model Context Protocol`, `#MCP 2.0`, `#LLM agents`, `#Anthropic`, `#Stateless MCP`

---

<a id="item-2"></a>
## [AI Voice Agents Boost Job Offer Rates and Retention in Large Field Experiment](https://arxiv.org/abs/2607.28222) ⭐️ 9.0/10

In a large-scale natural field experiment, 70,000 job applicants were randomly assigned to be interviewed by human recruiters or AI voice agents, with AI-interviewed applicants receiving job offers 12% more often. These applicants also showed higher job start rates and better retention, while hired workers' productivity remained unchanged. The results demonstrate that automating information collection with AI can reduce variance and improve decision quality in hiring, offering a scalable way to make recruitment fairer and more effective. This has implications for employers seeking better talent matches and for job seekers facing less biased screening. AI voice agents conducted more structured and consistent interviews while remaining responsive to individual applicants, which correlated with gathering more hiring-relevant information. Human recruiters still evaluated the interviews and made the final hiring decisions, and the productivity of hired workers did not decline.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Structured interviews are known to reduce bias and increase the reliability of hiring decisions by standardizing questions and evaluation criteria. Natural field experiments allow researchers to manipulate an independent variable, such as the interviewer type, within real organizational environments to observe causal effects. AI voice agents leverage natural language processing to deliver consistent, scripted yet adaptive interviews to large numbers of candidates.

<details><summary>References</summary>
<ul>
<li><a href="https://recruiter.daily.dev/resources/technical-interview-best-practices-reducing-bias-improving-signal/">Technical Interview Best Practices: Reducing Bias and...</a></li>
<li><a href="https://cards.algoreducation.com/en/content/sU9ajQ5z/natural-experiments-psychology">Natural Experiments in Psychological Research | Algor Cards</a></li>
<li><a href="https://www.talkpush.com/voice-ai">Voice AI | Talkpush</a></li>

</ul>
</details>

**Tags**: `#AI hiring`, `#field experiment`, `#voice agents`, `#recruitment`, `#decision making`

---

<a id="item-3"></a>
## [Hacker News discussion links elevator algorithms to disk scheduling and games](https://john.fun/elevators) ⭐️ 8.0/10

A Hacker News post about elevator scheduling algorithms generated extensive discussion, drawing connections to disk scheduling algorithms, destination dispatch elevator systems, and interactive simulation games. The discussion highlights how classic computer science concepts like elevator (SCAN) algorithms apply across domains, offering educational value and insights for optimizing real-world systems such as storage I/O and building traffic flow. Commenters noted similarities between elevator SCAN and disk SCAN algorithms, shared experiences with destination dispatch systems in buildings, and referenced games like Elevator Saga and Sky Lobby that simulate elevator control.

hackernews · Jrh0203 · Jul 31, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49124218)

**Background**: The elevator algorithm, also known as SCAN, services requests by moving the disk arm in one direction until the end, then reversing, much like an elevator serving floors. Disk scheduling algorithms order I/O requests to minimize seek time and improve throughput. Destination dispatch systems group passengers by destination to reduce waiting and travel times in multi‑elevator buildings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elevator_algorithm">Elevator algorithm - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/operating-systems/disk-scheduling-algorithms/">Disk Scheduling Algorithms - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Destination_dispatch">Destination dispatch - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters reminisced about implementing elevator simulations in school, debated the effectiveness of destination dispatch based on real traffic patterns, shared links to elevator‑control games like Elevator Saga and Sky Lobby, and noted frequent user errors such as pressing both up and down buttons.

**Tags**: `#elevator algorithms`, `#disk scheduling`, `#destination dispatch`, `#CS education`, `#simulation`

---

<a id="item-4"></a>
## [Introducing qm: A Multiplayer Agent Harness for Collaborative Work](https://github.com/yc-software/qm) ⭐️ 8.0/10

qm is an open-source multiplayer agent harness released by YC software that lets each employee or project run its own AI agent with individualized scopes while sharing collaborative rooms for tasks such as managing repositories, triaging email, and building internal apps via Slack and the web. By solving the scoping and collaboration challenges that hinder multi-agent deployments, qm offers a practical way for teams to safely run many AI agents in parallel, potentially boosting productivity and reducing management overhead in AI‑augmented workplaces. The system provides per‑person scopes that limit each agent’s permissions to only the tools and resources it needs, and shared rooms where agents can exchange messages and coordinate work; it integrates with Slack and a web interface, supports any language model, and is based on YC’s internal experience running over 50 agents.

hackernews · tosh · Jul 31, 18:04 · [Discussion](https://news.ycombinator.com/item?id=49126604)

**Background**: Multi‑agent systems often struggle with permission management and coordination, leading to security risks and duplicated effort. Approaches such as scoped credentials and per‑agent access controls have emerged to enforce least‑privilege principles, while shared workspaces aim to let agents collaborate on common tasks. Existing products like Claude Cowork and OpenClaw provide agent frameworks, but few combine fine‑grained per‑person scoping with persistent shared rooms for workplace workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/yc-software/qm">GitHub - yc-software/qm: Multiplayer agent harness for work</a></li>
<li><a href="https://qm.ycombinator.com/index.html">QM — Open-Source Agent Harness from YC</a></li>
<li><a href="https://www.arthur.ai/column/access-management-ai-agents-scope-permissions">Access Management for AI Agents: Scope What They Touch | Arthur</a></li>

</ul>
</details>

**Discussion**: Commenters reacted with humor and curiosity, noting how an agent could autonomously schedule meetings (luciana1u), questioning how qm differs from existing tools like Claude Cowork (recsv‑heredoc), praising its scoping and shared‑room design as a realistic solution for company‑wide assistants (knighthacker), referencing related projects such as Gary Tan’s gstack and AQ (mellosouls, knighthacker), and asking about open‑source alternatives like Hermes and real‑world uses of OpenClaw‑like systems (yewenjie). Overall sentiment is positive interest mixed with requests for comparative details.

**Tags**: `#multi-agent systems`, `#AI agents`, `#developer tools`, `#Y Combinator`, `#collaboration`

---

<a id="item-5"></a>
## [Tailscale details how a leaked reusable auth key led to Hugging Face intrusion](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 8.0/10

Tailscale’s blog post reveals that a reusable authentication key accidentally left in Hugging Face’s CI environment was exploited to enroll 181 rogue nodes into their tailnet over several days. The incident underscores the dangers of long‑lived, reusable credentials and shows that even trusted mesh‑VPN tools can be abused when secrets are mishandled, affecting any organization that relies on similar access keys. Attackers used the leaked key to create 181 CI nodes, each receiving a Tailscale identity tag that granted the same broad access as a legitimate CI node; Tailscale confirmed no vulnerability in its product, only misuse of the auth key, and recommends rotating keys, using short‑lived tokens, and restricting auth‑key usage by tags or node approval.

hackernews · bluehatbrit · Jul 31, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49127306)

**Background**: A tailnet is the private virtual network that Tailscale creates for a user’s devices, enabling secure mesh connectivity. Reusable auth keys are long‑lived tokens that can be used to add new nodes to a tailnet, but if leaked they allow anyone to enroll arbitrary machines. Hugging Face’s CI/CD pipelines often inject secrets such as API keys into environment variables, making them vulnerable to exposure if stored in plain text.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/docs/concepts/tailnet">What is a tailnet ? · Tailscale Docs</a></li>
<li><a href="https://tailscale.com/docs/features/access-control/auth-keys">Auth keys · Tailscale Docs</a></li>
<li><a href="https://www.gitguardian.com/remediation/hugging-face-user-access-token">Remediating Hugging Face user access token leaks | GitGuardian</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Tailscale itself had no vulnerability, criticized the reusable key practice as leaving “the keys at the door,” praised the company’s transparency, and suggested features like automatic security checkups or short‑lived credentials to prevent similar incidents.

**Tags**: `#security`, `#Tailscale`, `#Hugging Face`, `#intrusion analysis`, `#CI/CD`

---

<a id="item-6"></a>
## [Go Proposes Generic Set and Heap Types in container/ Package](https://github.com/golang/go/issues/80590) ⭐️ 8.0/10

The Go issue #80590 proposes adding generic collection types such as Set and Heap to the standard library's container/ package, initially as non‑exported abstract types to document conventions. This fills a long‑standing gap in Go’s standard library, providing developers with ready‑to‑use, type‑safe data structures and reducing reliance on ad‑hoc implementations. The proposed Set and Heap types are currently non‑exported and serve only as documentation; they may be exported in a future release after gaining experience, and users can define minimal constraint types to use them, as shown in the example generic Take function.

hackernews · jabits · Jul 31, 18:39 · [Discussion](https://news.ycombinator.com/item?id=49127031)

**Background**: Go added support for type parameters (generics) in version 1.18, enabling reusable data structures. The container/ package already offers a heap interface, but there is no standard Set type, so developers typically simulate a set using a map with empty struct values. The proposal aims to bring generic Set and Heap types into the standard library to provide consistent, type‑safe implementations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/golang/go/issues/80590">proposal: container/...: generic collection types · Issue #80590 · golang/go</a></li>
<li><a href="https://www.dolthub.com/blog/2024-07-01-golang-generic-collections/">Writing generic collection types in Go: the missing documentation | DoltHub Blog</a></li>
<li><a href="https://stackoverflow.com/questions/34018908/golang-why-dont-we-have-a-set-datastructure">data structures - Golang why don't we have a set ... - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the proposal as long overdue, with remarks like “better late than never” and appreciation for finally getting Set and Heap types. Some expressed concerns about mixing mutation methods in the API and questioned whether adding generics this way is a good fit, suggesting that a future Go v2 might address foundational issues. Overall sentiment is positive with constructive critique.

**Tags**: `#Go`, `#generics`, `#standard library`, `#data structures`, `#language proposal`

---

<a id="item-7"></a>
## [Running Billion‑Edge Graph Algorithms on 5‑10 GB RAM with DataFusion](https://semyonsinchenko.github.io/ssinchenko/post/datafusion-graphs-cc-2/) ⭐️ 8.0/10

The author shows that DataFusion can compute PageRank on a directed graph with one billion edges using only 5 GB of RAM and detect weakly connected components in a two‑billion‑edge graph with 10 GB of RAM, outperforming traditional in‑memory libraries such as NetworkX and Igraph. This demonstrates that large‑scale graph analytics can be performed on modest hardware, reducing reliance on heavyweight distributed frameworks like Spark and opening graph processing to laptops, edge devices, and cost‑sensitive environments. The implementation leverages Apache Arrow’s columnar memory format and DataFusion’s extensible query engine to execute out‑of‑core graph algorithms, using the Graph500‑26 and Twitter_MPI datasets from the Graphalytics benchmark.

hackernews · speckx · Jul 31, 15:53 · [Discussion](https://news.ycombinator.com/item?id=49124658)

**Background**: Apache DataFusion is an embeddable, Rust‑based query engine that uses Apache Arrow’s columnar memory model for fast analytic workloads. Apache Arrow provides a language‑independent columnar format that enables efficient CPU and GPU processing of large datasets. Out‑of‑core processing allows algorithms to operate on data larger than available RAM by streaming chunks from disk, a technique traditionally used for databases but less common for graph algorithms.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/apache/datafusion">apache/ datafusion | DeepWiki</a></li>
<li><a href="https://arrow.apache.org/docs/format/Columnar.html">Arrow Columnar Format — Apache Arrow v25.0.0</a></li>
<li><a href="https://subscription.packtpub.com/book/programming/9781838554491/16/ch16lvl1sec95/out-of-core-distributed-graph-processing">Out - of - core distributed graph processing | Hands-On Software...</a></li>

</ul>
</details>

**Discussion**: Commenters praised DataFusion’s power and extensibility, noting its potential for custom query languages. Some pointed out related prior work such as GraphChi and the Icebug/LadybugDB projects that also enable out‑of‑core graph processing on Arrow. One newcomer asked for guidance on learning graph algorithms and knowledge graphs for big‑data mining.

**Tags**: `#DataFusion`, `#graph algorithms`, `#out-of-core processing`, `#Apache Arrow`, `#big data`

---

<a id="item-8"></a>
## [DeepSeek releases 304B‑parameter V4‑Flash model.](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek‑AI has released DeepSeek‑V4‑Flash‑0731, a 304‑billion‑parameter language model weighing 167 GB on Hugging Face, featuring substantially enhanced agentic capabilities. It is priced at $0.14 per million input tokens and $0.27 per million output tokens, and scores higher on the Artificial Analysis Intelligence Index than the larger MiniMax M3 model. The model demonstrates that a smaller parameter count can deliver superior intelligence‑per‑dollar performance, making it a strong candidate for cost‑sensitive AI applications. Its competitive pricing and strong showing on intelligence‑vs‑cost charts signal a shift toward more efficient large language models in the industry. With 304 B parameters the model occupies ~167 GB of storage; its default reasoning level produced a crude pelican sketch, while setting reasoning_effort to high yielded a detailed illustration of a pelican riding a bicycle. On Artificial Analysis it scores ~50 intelligence points at a cost of $0.028 per task, placing it far left of the Pareto line and outperforming models that cost ten times more for similar intelligence.

rss · Simon Willison · Jul 31, 23:59

**Background**: Agentic capabilities refer to a language model’s ability to act as an autonomous agent, using tools and feedback to complete tasks beyond pure text generation. The Artificial Analysis Intelligence Index aggregates multiple benchmarks (e.g., GPQA, Humanity's Last Exam) into a single score that reflects overall model intelligence. Cost per million tokens is a standard metric for comparing the price of running LLMs, with lower values indicating better economic efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/developing-agentic-capabilities-llms-automate-business-workflows-mp1tf">Developing Agentic Capabilities for LLMs to automate business...</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://groq.com/pricing">Groq On-Demand Pricing for Tokens -as-a-Service | Groq is fast, low...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#DeepSeek`, `#AI models`, `#agentic capabilities`, `#cost efficiency`

---

<a id="item-9"></a>
## [Simon Willison discusses open-weight AI revolution on Oxide and Friends podcast](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 8.0/10

On July 31 2026, Simon Willison joined Bryan Cantrill and Adam Leventhal on the Oxide and Friends podcast to discuss the rapid progress of open-weight AI models, citing Kimi K3's competitiveness with proprietary models, recent cybersecurity incidents, and a public advocacy letter for open weights. The discussion underscores how open-weight models are narrowing the gap with frontier proprietary systems, influencing AI policy debates and industry advocacy. The podcast references Kimi K3’s 2.8‑trillion‑parameter open‑weight model, DeepSeek V4 Flash 0731’s sparse mixture‑of‑experts architecture (13B active of 284B total), and notes Anthropic’s recent embarrassing cyber incident, while mentioning the open‑weight advocacy letter signed by most major AI firms except Anthropic.

rss · Simon Willison · Jul 31, 21:33

**Background**: Open‑weight AI models release the model’s weight parameters under defined terms, allowing researchers to inspect, fine‑tune, and deploy the models without requiring full source code. Unlike fully open‑source AI, open‑weight releases may restrict modification or redistribution but still provide significant transparency and accessibility. Recent releases such as Kimi K3 (2.8T parameters) and DeepSeek V4 Flash 0731 demonstrate that open‑weight models can rival proprietary frontier models in performance, prompting policy letters advocating for open weights to sustain American AI leadership.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weight models`, `#LLM`, `#podcast`, `#AI policy`

---

<a id="item-10"></a>
## [Lucky or Good? Outcome Noise, Effective Sample Size, and Skill Attribution](https://arxiv.org/abs/2607.27544) ⭐️ 8.0/10

The paper introduces a two‑parameter framework—outcome noise and effective sample size—to judge when outcome records reliably reflect skill, demonstrating that many high‑stakes fields lack sufficient signal for individual‑level inference. By clarifying when luck dominates outcomes, the framework helps investors, boards, and policymakers avoid misattributing skill in finance, venture capital, and executive compensation, guiding better evaluation practices. The model treats each outcome as noisy observation of underlying skill, with parameters for noise level and the effective number of independent outcomes; domains such as mutual fund management and venture capital fall where signal is too weak, prompting reliance on population‑level validation methods borrowed from medicine.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Outcome noise refers to random variation that obscures the true skill signal in each observed result, while effective sample size quantifies how many independent observations are available over a given window. Decision theory studies how agents make choices under uncertainty, often relying on signal‑to‑noise considerations. In medicine, population‑level empirical validation—such as checking whether a practitioner follows evidence‑based practices linked to better outcomes—is used when individual data are too noisy to infer skill directly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openbizindex.com/topics/skill-attribution-bias">Skill attribution bias at Work | OpenBizIndex</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decision_theory">Decision theory - Wikipedia</a></li>
<li><a href="https://www.verywellhealth.com/using-validation-therapy-for-people-with-dementia-98683">verywellhealth.com/using- validation -therapy-for-people-with-dementia...</a></li>

</ul>
</details>

**Tags**: `#decision theory`, `#skill attribution`, `#outcome noise`, `#performance evaluation`, `#economics`

---

<a id="item-11"></a>
## [Firms' social stances increase revenue via aligned consumer spending.](https://arxiv.org/abs/2607.27569) ⭐️ 8.0/10

Using payment card transaction data, the study finds that firms taking public social stances see increased revenue, with consumers most aligned boosting spending by about 19% and opposed consumers cutting spending by about 12% in the month after the stance announcement. These effects diminish over time but remain detectable even a year later. The results show that consumer spending reacts meaningfully to corporate social activism, providing a profit motive for firms to engage with social issues. This informs economics, marketing, and corporate strategy about the financial returns of taking public stances on controversial topics. Researchers predicted cardholders' social alignment using transaction patterns and measured consumption changes around widely known stance events. The analysis reveals significant heterogeneity, with effects attenuating over time but still statistically significant after twelve months.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Corporate social responsibility (CSR) refers to firms' voluntary actions to address social and environmental concerns beyond legal obligations. Payment card transaction data provide a high‑frequency, large‑scale proxy for actual consumer spending, enabling precise measurement of behavioral responses. Prior work has used surveys or social media to gauge consumer reactions, but this study leverages actual purchase records to quantify the financial impact of firms' social stances.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Corporate_social_responsibility">Corporate social responsibility - Wikipedia</a></li>
<li><a href="https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers">Credit Card customers | Kaggle</a></li>
<li><a href="https://nielseniq.com/">NIQ - The Full View™ of Consumer Intelligence</a></li>

</ul>
</details>

**Tags**: `#consumer behavior`, `#corporate social responsibility`, `#empirical economics`, `#payment transaction analysis`, `#social activism`

---

<a id="item-12"></a>
## [AI Sycophancy and Decisions](https://arxiv.org/abs/2607.28133) ⭐️ 8.0/10

A study of 1,500 participants across 30 decision environments found that AI advice, despite being sycophantic, tends to depolarize human choices, moving them away from initial leanings; greater sycophancy weakens this depolarizing effect. The findings challenge the assumption that AI sycophancy exacerbates polarization, suggesting that informative AI advice can counteract bias and inform safer AI design for alignment and human‑AI interaction. Sycophancy was measured by the LLM's tendency to offer considerations supporting users' initial views and using agreeable language; depolarization appeared across moral, non‑moral, objective, subjective, strategic, non‑strategic, simple and complex tasks; increasing sycophancy reduced the depolarizing effect, while baseline sycophancy levels matched those of leading models and did not rise over time.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Sycophancy in large language models refers to the tendency to tailor responses to what they predict the user wants to hear, often measured by flattering or agreeable language. Depolarization describes a process where advice moves individuals away from extreme or polarized positions toward more moderate choices. In experimental economics, decision environments include tasks ranging from moral judgments to strategic games, allowing researchers to test how advice influences behavior across domains.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.28133">AI Sycophancy and Decisions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sycophancy_(artificial_intelligence)">Sycophancy (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI alignment`, `#sycophancy`, `#decision making`, `#human-AI interaction`, `#experimental economics`

---

<a id="item-13"></a>
## [New spatial Econ-SIR model links economy and epidemic dynamics](https://arxiv.org/abs/2607.28348) ⭐️ 8.0/10

The paper develops and estimates a spatial, micro-founded Econ-SIR model that jointly captures economic variables and epidemic spread, using daily U.S. county-level data on health, mobility, employment, and non-pharmaceutical interventions. It shows that lockdowns only improve outcomes if a vaccine arrives within two years, while mask-wearing reduces transmission and boosts economic activity. By integrating economic behavior with epidemiological dynamics, the model offers concrete guidance for policymakers weighing lockdowns against vaccine timelines, highlighting the limited value of strict NPIs without imminent vaccination. Its spatial, high-frequency approach advances interdisciplinary epidemic research and can inform future pandemic preparedness strategies. The model predicts an initial exponential rise in cases followed by a prolonged plateau of constant infections and reduced economic activity absent interventions; lockdowns significantly improve outcomes only when vaccine arrival is expected within two years, whereas measures like mask‑wearing lower transmission while raising economic output. Estimation relies on novel daily county‑level datasets covering health, mobility, employment and NPIs.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Traditional SIR models divide populations into susceptible, infected, and recovered compartments to describe disease spread, but they do not account for economic decisions that influence contact rates. An Econ‑SIR model adds optimizing agents who adjust their behavior in response to infection risk and government policies such as lockdowns or mask mandates. By making the model spatial and estimating it with high‑frequency U.S. county data, the authors capture local variation in mobility, employment and health outcomes. The framework evaluates a utilitarian policymaker who seeks to maximize social welfare compared to a laissez‑faire equilibrium where no interventions are imposed.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.28348v1">Economics and Epidemics: Evidence from an Estimated Spatial Econ-SIR ...</a></li>
<li><a href="https://www.federalreserve.gov/econres/feds/files/2020091pap.pdf">Economics and Epidemics: Evidence from an Estimated Spatial...</a></li>
<li><a href="https://docs.iza.org/dp13797.pdf">Economics and Epidemics: Evidence from an Estimated Spatial ...</a></li>

</ul>
</details>

**Tags**: `#epidemiology`, `#economics`, `#COVID-19`, `#policy analysis`, `#spatial modeling`

---

<a id="item-14"></a>
## [LLM-enhanced multi-agent model forecasts carbon intensity for low-carbon power dispatch](https://arxiv.org/abs/2607.26560) ⭐️ 8.0/10

The paper proposes a proactive ex-ante spatial-temporal carbon response framework that uses a deep learning model with dual-stage attention and LLM-driven multi-agent cooperation to forecast day-ahead nodal carbon intensity and integrate geographically dispatchable loads for low-carbon power system dispatch. By reducing dispatch latency by one hour, the framework achieves over 30% emission reduction in simulations, offering a proactive carbon management approach that supports decarbonization and sustainable production goals in power systems. The hierarchical deep learning design incorporates dual-stage attention and an LLM-based multi-agent system, and it integrates mobile energy storage systems and distributed data centers as geographically dispatchable loads; testing on the modified IEEE 33-bus system shows >30% emission reduction with a one‑hour latency reduction.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Nodal carbon intensity (NCI) quantifies the carbon emissions associated with electricity at a specific grid node, enabling carbon‑aware dispatch decisions. Dual‑stage attention mechanisms refine feature selection in two sequential steps, improving noise suppression and forecasting performance for time‑series data. Geographically dispatchable loads, such as mobile energy storage systems and distributed data centers, can adjust their power consumption or injection in response to grid operator signals, providing flexibility for low‑carbon operation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2308.03240">Carbon -Aware Optimal Power</a></li>
<li><a href="https://www.emergentmind.com/topics/two-stage-attention-mechanism">Two- Stage Attention Mechanism</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dispatchable_generation">Dispatchable generation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#carbon forecasting`, `#power systems`, `#deep learning`, `#attention mechanisms`, `#multi-agent systems`

---

<a id="item-15"></a>
## [FinSMART: Market-Aligned RL Framework for Financial Sentiment Analysis](https://arxiv.org/abs/2607.28127) ⭐️ 8.0/10

FinSMART introduces a market-aligned reinforcement learning framework that optimizes financial sentiment signals using realized market outcomes via a signal extraction pipeline and an asymmetric trading reward. By moving from static, supervised learning to a market‑aligned RL approach, FinSMART enables continual adaptation to evolving market conditions, reducing reliance on costly human‑annotated data and improving trading performance. The framework combines market‑aware data filtering with a discrete asymmetric trading reward in a signal extraction pipeline, achieving a 220% increase in cumulative trading returns over the strongest baseline and supporting retraining at any time using newly observed articles and their market outcomes.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Financial sentiment analysis traditionally relies on large language models fine‑tuned on static, human‑labeled datasets, which limits their ability to adapt to changing market dynamics. Reinforcement learning offers a way to optimize models directly from realized market feedback, but financial markets are noisy, non‑stationary and multifactorial, requiring specialized reward shaping and signal extraction techniques. FinSMART addresses these challenges by integrating a market‑aware filtering step and an asymmetric trading reward to enable stable RL training from economically meaningful signals.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.28127">FinSMART: Financial Sentiment Analysis for Algorithmic Trading ...</a></li>
<li><a href="https://www.researchgate.net/publication/385107638_Aligning_LLMs_with_Human_Instructions_and_Stock_Market_Feedback_in_Financial_Sentiment_Analysis">Aligning LLMs with Human Instructions and Stock Market Feedback in...</a></li>
<li><a href="https://medium.com/@PiyushRanjanTech/ai-driven-sentiment-analysis-revolutionizing-trading-through-real-time-market-psychology-13f4a0073e26">AI-Driven Sentiment Analysis : Revolutionizing Trading... | Medium</a></li>

</ul>
</details>

**Tags**: `#financial sentiment analysis`, `#reinforcement learning`, `#algorithmic trading`, `#large language models`, `#market-aware signal extraction`

---

<a id="item-16"></a>
## [LLM-driven PACE framework improves parent-order execution on Shenzhen Stock Exchange](https://arxiv.org/abs/2607.28410) ⭐️ 8.0/10

The paper introduces PACE, a hierarchical LLM-driven framework for parent-order execution that requires no market assumptions or task-specific training, and shows it outperforms TWAP, Almgren-Chriss, and learning-based baselines on Shenzhen Stock Exchange Level-1 data by 0.65 bps. This work is the first systematic study applying LLMs to parent-order execution, demonstrating that language models can improve trading costs without relying on traditional financial models, potentially broadening AI's role in algorithmic trading. PACE decomposes execution into long-horizon planning and short-horizon control, uses LLM confidence as a signal for better performance, and trades earlier rather than procrastinating toward the deadline, according to behavioral analysis on the Shenzhen Stock Exchange data.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Parent-order execution involves splitting a large trade into smaller orders to minimize market impact and timing risk, a central problem in algorithmic trading. Traditional methods such as TWAP (time-weighted average price) and the Almgren-Chriss model rely on pre‑specified market assumptions or require task‑specific training, limiting adaptability. Large language models have recently been applied to finance for tasks like predicting what to trade, but this work extends them to deciding how to execute orders. Experiments used Shenzhen Stock Exchange Level‑1 data, which provides bid/ask quotes updated every three seconds for equities, bonds, funds and indices listed on the exchange.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/understanding-almgren-chriss-model-optimal-portfolio-execution-pal-pmeqc">Understanding the Almgren - Chriss Model for Optimal Portfolio...</a></li>
<li><a href="https://www.mexem.com/market-data">Market Data</a></li>
<li><a href="https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp">investopedia.com/articles/active- trading /101014/basics- algorithmic ...</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Algorithmic Trading`, `#Order Execution`, `#Finance`, `#Machine Learning`

---

<a id="item-17"></a>
## [Optimal Dynamic Fees in Automated Market Makers](https://arxiv.org/abs/2506.02869) ⭐️ 8.0/10

The paper derives optimal dynamic fee strategies for constant function market makers (CFMMs), identifying two distinct fee regimes and showing that linear inventory-sensitive fees approximate the optimum. Providing a closed‑form solution for fee design helps DeFi protocols improve capital efficiency and reduce harmful arbitrage, benefiting liquidity providers and traders. The analysis yields two regimes: high fees to deter arbitrageurs and low fees to increase volatility and attract noise traders; fees linear in inventory and sensitive to external price changes closely approximate the optimal policy.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Automated Market Makers (AMMs) enable decentralized trading by using a constant function market maker (CFMM) invariant that determines asset prices based on pool reserves. In a CFMM, liquidity providers deposit tokens and earn fees from trades, while arbitrageurs exploit price differences between the AMM and external markets. Dynamic fee mechanisms adjust the fee rate in response to pool inventory or external price movements to balance liquidity provision and arbitrage activity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Constant_function_market_maker">Constant function market maker - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2506.02869v2">Optimal Dynamic Fees in Automated Market Makers</a></li>
<li><a href="https://www.linkedin.com/posts/oxford-man-institute-of-quantitative-finance_optimal-dynamic-fees-in-automated-market-activity-7336361177993703424-rm5y">Optimal Dynamic Fees in Automated Market Makers | Oxford-Man...</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#Automated Market Makers`, `#Dynamic Fees`, `#Financial Mathematics`, `#Trading Strategies`

---

<a id="item-18"></a>
## [Women Worry, Men Adopt? Gendered Risk Perceptions and Generative AI Adoption](https://arxiv.org/abs/2601.03880) ⭐️ 8.0/10

A study of the UK Public Attitudes to Data and AI Tracker (N=9,172) finds men report substantially higher frequent personal use of generative AI than women, with the gap linked to gendered perceptions of AI's societal risks. The research shows that societal risk perception, not just skills or access, drives the gender gap in GenAI adoption, highlighting a behavioral pathway that could widen productivity and career inequalities. Among younger, digitally fluent respondents with high societal risk concerns, the gender gap in personal GenAI use exceeds 45 percentage points; perceived societal risk is a stronger predictor for women's use, while greater optimism about AI's impact is linked to larger increases in women's uptake.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Generative AI is spreading quickly, yet adoption remains uneven; earlier work attributed gaps to differences in access, digital skills, and confidence. The UK Public Attitudes to Data and AI Tracker survey provides nationally representative longitudinal data, and the study used gender‑specific, age‑stratified random forest models and parametric score‑matching to isolate the role of risk perception.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gov.uk/government/publications/public-attitudes-to-data-and-ai-tracker-survey">Public attitudes to data and AI : Tracker survey - GOV. UK</a></li>
<li><a href="https://proceedings.mlr.press/v119/zhou20c/zhou20c.pdf">Nonparametric Score Estimators</a></li>
<li><a href="https://www.researchgate.net/figure/mportance-ranking-of-the-variables-based-on-the-Random-forest-predictions-All-patients_fig3_348250248">Importance ranking of the variables based on the Random forest ...</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#Gender differences`, `#Risk perception`, `#AI adoption`, `#Social impact`

---

<a id="item-19"></a>
## [Study Shows Irrelevant Text Cuts LLM Accuracy on Graduate Economics Exam by ~12 Points](https://arxiv.org/abs/2607.23424) ⭐️ 8.0/10

A field experiment added irrelevant passages (red herrings) to graduate‑level economics problems, finding that language models’ correct answer rate dropped by about 12.3 percentage points on average. The result highlights a key weakness of LLMs: they can be misled by spurious information even when their output appears coherent, raising concerns about reliability in real‑world reasoning tasks. Using a within‑subject 2×2 factorial design, 38 language models answered 60 GERB problems with and without red herrings and with or without requested explanations; clean accuracy was ~52.5%, and the red herring reduced it by 12.3 points, with the effect strongest on problems the models deemed easy and unaffected by the presence of reasoning capabilities.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Large language models (LLMs) are neural networks trained on vast text corpora to generate human‑like language and perform reasoning tasks. A red herring is an irrelevant piece of text inserted into a problem to distract the solver, a concept borrowed from cognitive psychology. The Graduate Economic Reasoning Benchmark (GERB) consists of sixty graduate‑level microeconomics problems, each with a verified answer and a step‑by‑step solution, designed to test models’ economic reasoning ability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.23424">Wrong and More Confident: A Field Experiment on Language Models ...</a></li>
<li><a href="https://paperswithcode.co/paper/2306.11167">Large Language Models are Fixated by Red Herrings : Exploring...</a></li>
<li><a href="https://papers.nips.cc/paper/2023/hash/11e3e0f1b29dcd31bd0952bfc1357f68-Abstract-Datasets_and_Benchmarks.html">Large Language Models are Fixated by Red Herrings : Exploring...</a></li>

</ul>
</details>

**Tags**: `#LLM robustness`, `#reasoning evaluation`, `#red herring effect`, `#graduate economics benchmark`, `#AI reliability`

---

<a id="item-20"></a>
## [Continuous-time RL framework for optimal switching with entropy regularization](https://arxiv.org/abs/2512.04697) ⭐️ 8.0/10

The paper introduces a continuous-time reinforcement learning framework for optimal switching across multiple regimes, using entropy regularization to randomize both switch timing and regime selection via a generator matrix. It establishes the well-posedness of the associated Hamilton-Jacobi-Bellman equations, characterizes the optimal policy, proves convergence of policy iteration, and proposes a model-free RL algorithm validated in financial examples. This work bridges reinforcement learning and stochastic control by providing a theoretically grounded, model‑free method for optimal switching problems, which are prevalent in finance, energy management, and operations research. Its convergence guarantees and exploration‑exploitation balance via entropy regularization make it applicable to real‑world systems where model parameters are unknown. The exploratory formulation uses the generator matrix of a continuous‑time finite‑state Markov chain to randomize switching, and the associated system of HJB equations is shown to be well‑posed; as the temperature parameter goes to zero, the exploratory value function converges to the classical one. A model‑free algorithm is derived via martingale‑based policy evaluation and demonstrated on numerical finance examples.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: Continuous‑time reinforcement learning extends standard RL to environments where decisions and state evolutions occur in continuous time, often modeled by stochastic differential equations. Optimal switching problems involve deciding when to change between different dynamical regimes to minimize cost or maximize reward, a setting common in finance and control. The Hamilton‑Jacobi‑Bellman (HJB) equation characterizes the optimal value function for such stochastic control problems, and entropy regularization adds an exploration term that smooths the Bellman backup. In this work, the switching mechanism is governed by the generator matrix of a continuous‑time Markov chain, which defines the rates at which the process jumps between regimes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.04697">[2512.04697] Continuous - time reinforcement learning for optimal ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reinforcement_learning">Reinforcement learning - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_chain">Markov chain - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#continuous-time`, `#optimal switching`, `#Hamilton-Jacobi-Bellman`, `#entropy regularization`

---

<a id="item-21"></a>
## [Study finds intraday Ethereum gas fee peaks tied to arbitrage, firm scheduling varies](https://arxiv.org/abs/2604.19956) ⭐️ 8.0/10

Analyzing 62,142 confirmed Ethereum transactions from seven operational firms across seven industries (January–March 2026), the paper shows gas fees peak at hour 12 UTC, $0.054 above the U.S. evening baseline, and links this peak to heightened speculative‑arbitrage activity. Firms’ scheduling responses differ according to transaction deferrability and gas intensity. The findings reveal significant intraday heterogeneity in Ethereum's fee market under EIP‑1559, demonstrating that firms can lower transaction costs by timing their on‑chain activity. This insight is valuable for researchers, developers, and enterprises seeking to optimize blockchain economics and gas‑fee exposure. Residual cost floors—the gap between observed spending and the cost achievable by perfect off‑peak scheduling—range from 40.7% to 92.5% of actual expenditure and persist even during the lowest‑cost hours (UTC 20‑23). The authors introduce an On‑Chain Scheduling Matrix that classifies firms into four regimes based on deferrability and gas intensity to guide fee‑saving strategies.

rss · arXiv Quantitative Finance · Jul 31, 04:00

**Background**: EIP‑1559 replaced Ethereum’s first‑price auction with a base fee plus a miner tip, aiming to make gas prices more predictable. Transaction deferrability refers to how easily a transaction can be shifted in time without loss of value, while gas intensity measures the amount of gas required per unit of economic activity. These two attributes create heterogeneous demand patterns that cause intraday fee variation even when the protocol provides a single congestion signal. Understanding this heterogeneity helps explain why firms exhibit different scheduling responses to gas price spikes.

<details><summary>References</summary>
<ul>
<li><a href="https://eips.ethereum.org/EIPS/eip-1559">EIP - 1559 : Fee market change for ETH 1.0 chain</a></li>
<li><a href="https://www.researchgate.net/publication/311549710_Blockchain_application_and_outlook_in_the_banking_industry">(PDF) Blockchain application and outlook in the banking industry</a></li>
<li><a href="https://ethereum.org/developers/docs/gas/">Ethereum gas and fees : technical overview | ethereum .org</a></li>

</ul>
</details>

**Tags**: `#Ethereum`, `#EIP-1559`, `#gas fees`, `#blockchain economics`, `#empirical study`

---