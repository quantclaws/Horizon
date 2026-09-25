---
layout: default
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25
lang: en
---

> From 45 items, 11 important content pieces were selected

---

1. [F-Droid 2.0 Released with Redesigned UI and Removal of Privileged Extension](#item-1) ⭐️ 8.0/10
2. [Whiteboard: Open‑Source IDE for Human‑AI Collaborative Software Design](#item-2) ⭐️ 8.0/10
3. [Google announces Project Suncatcher to place ML infrastructure in space.](#item-3) ⭐️ 8.0/10
4. [Apple Withdraws Advanced Data Protection in UK, Creating Two‑Tier Encryption](#item-4) ⭐️ 8.0/10
5. [California targets wealthy residents amid wealth and talent flight](#item-5) ⭐️ 8.0/10
6. [Experimental Study Shows Rule-Based Pricing Design Raises Market Prices](#item-6) ⭐️ 8.0/10
7. [Sovereign Grassroots Currencies: A CBDC Architecture for Credit and Monetary Policy](#item-7) ⭐️ 8.0/10
8. [Frozen Statistical Referee Boosts LLM-Driven Investment Factor Discovery](#item-8) ⭐️ 8.0/10
9. [Local Weak Limits Prove Convergence of Equilibrium and Risk in Sparse Economic Networks.](#item-9) ⭐️ 8.0/10
10. [Proof of Stake economy under centralized exchanges--a mean field model](#item-10) ⭐️ 8.0/10
11. [Leaky-integrator reconstruction: taming error accumulation in recursive differenced time-series forecasting](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [F-Droid 2.0 Released with Redesigned UI and Removal of Privileged Extension](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

F-Droid announced version 2.0, a major overhaul featuring a redesigned user interface and the phasing out of the privileged extension that previously required root access for automatic app installs. The update improves usability and security by replacing the privileged extension with Android's standard session installer, making the app store more accessible to non‑rooted devices and aligning with mainstream Android practices. F-Droid 2.0 drops support for Android 6, introduces a new UI based on Material Design guidelines, and relies on the session installer introduced in Android 6.0 for background updates without user interaction.

hackernews · daveoc64 · Sep 24, 15:26 · [Discussion](https://news.ycombinator.com/item?id=49831968)

**Background**: F-Droid is an open-source app store for Android that distributes free and libre software. The privileged extension allowed F-Droid to install, update, and remove apps without enabling 'Unknown Sources' or user confirmation, but required root access or special setup. With version 2.0, the project replaces this extension with Android's standard session installer, which works on non‑rooted devices and follows Google Play's update model.

<details><summary>References</summary>
<ul>
<li><a href="https://f-droid.org/packages/org.fdroid.fdroid.privileged/">F - Droid Privileged Extension | F - Droid - Free and Open Source...</a></li>
<li><a href="https://daily.dev/posts/f-droid-2-0-what-changed-in-the-biggest-overhaul-in-a-decade-jega3om7h">F-Droid 2.0: what changed in the biggest overhaul in a decade</a></li>
<li><a href="https://github.com/f-droid/privileged-extension">F-Droid Privileged Extension - GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the UI redesign and the removal of the privileged extension, noting improvements over the previous clunky interface. However, several users criticized the new design for lacking visual separation, unclear tappable elements, and poor text alignment. Some mentioned using alternatives like Droid-ify or NeoStore, and expressed concerns about future restrictions from Google.

**Tags**: `#F-Droid`, `#Android`, `#open source`, `#app store`, `#UI redesign`

---

<a id="item-2"></a>
## [Whiteboard: Open‑Source IDE for Human‑AI Collaborative Software Design](https://github.com/devdotfast/whiteboard) ⭐️ 8.0/10

Whiteboard, a YC W26‑backed open‑source desktop app, lets humans and AI agents co‑design software architecture on a shared visual canvas using an agent SDK. It tackles the cognitive debt that arises when AI agents write code without human oversight, providing a concrete workspace for architecture review and iterative design. Built on CodeOSS, Whiteboard offers clickable diagrams that jump to source code, a Rust‑based semantic AST‑aware diff viewer with WASM plugins, and a decision log that links agent traces to design decisions.

hackernews · sidharthkmenon · Sep 24, 17:21 · [Discussion](https://news.ycombinator.com/item?id=49833867)

**Background**: CodeOSS is the open‑source core of Visual Studio Code, providing a familiar editor foundation with LSP and keybindings. Whiteboard leverages this base to give agents an SDK for drawing on an in‑app canvas, enabling them to express design intent visually. By integrating with tools like Claude Code and offering semantic diff viewing, it bridges high‑level architecture discussions with low‑level code changes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Visual_Studio_Code">Visual Studio Code - Wikipedia</a></li>
<li><a href="https://www.morphllm.com/ai-agent-framework">AI Agent Frameworks (2026 Update): 8 SDKs Compared + the Claude Agent SDK Primitive Reference</a></li>
<li><a href="https://code.claude.com/docs/en/vs-code">Use Claude Code in VS Code - Claude Code Docs</a></li>

</ul>
</details>

**Discussion**: Commenters praised the concept as a promising direction for human‑AI collaboration, while noting that the macOS notice should be more prominent and questioning the absence of file editing. Some raised concerns about diagram accuracy and LLM hallucinations, but many highlighted the usefulness of the semantic diff viewer for reviewing code changes.

**Tags**: `#software-design`, `#AI-agent`, `#open-source`, `#IDE`, `#collaborative-development`

---

<a id="item-3"></a>
## [Google announces Project Suncatcher to place ML infrastructure in space.](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) ⭐️ 8.0/10

Google unveiled Project Suncatcher, a research initiative to deploy machine learning hardware—including Tensor Processing Units—on solar‑powered satellites for in‑orbit AI processing, and announced an orbital data‑center test launch scheduled for October 1, 2026. Space‑based machine learning could harness constant solar energy and the cold vacuum for efficient AI computation, potentially reducing the energy footprint of ground data centers. However, overcoming thermal dissipation, radiation hardening, and high‑cost launch economics remains difficult, sparking debate over feasibility and possible military overlap. Project Suncatcher plans to use Google’s TPU AI chips mounted on satellites equipped with solar arrays, requiring radiation‑hardened packaging and active thermal‑control systems to manage heat in vacuum. The inaugural orbital test will carry four TPUs and run for only 15 minutes at a time, while related efforts like the Starcloud startup have already flown a proof‑of‑concept unit to validate similar hardware and economics.

hackernews · xnx · Sep 24, 13:53 · [Discussion](https://news.ycombinator.com/item?id=49830606)

**Background**: Machine learning infrastructure today relies on power‑hungry GPUs and TPUs housed in terrestrial data centers that consume significant electricity and generate heat. Placing similar hardware in orbit offers access to near‑constant solar power and a cold environment for heat rejection, but introduces challenges such as thermal management in a vacuum, radiation‑induced bit flips, and the need for high‑bandwidth downlink/uplink links. Google’s research explores solar‑powered satellite networks, TPU‑based AI nodes, and technologies like radiation‑hardened chips to address these hurdles before a scalable space‑based AI fabric can be realized.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/">Learn about Google’s Project Suncatcher to put ML ...</a></li>
<li><a href="https://arstechnica.com/google/2026/09/googles-first-suncatcher-orbital-data-center-test-launches-october-1/">Google's first Suncatcher orbital data center test launches ...</a></li>
<li><a href="https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/">Exploring a space-based, scalable AI infrastructure system design</a></li>

</ul>
</details>

**Discussion**: Commenters generally expressed doubt that the physics and economics of space‑based data centers favor them over ground facilities, citing worse heat dissipation and launch costs. Several noted parallels with existing efforts such as the Starcloud startup, which has flown a proof‑of‑concept unit, and pointed out Alphabet’s sizable stake in SpaceX as a potential enabler. Others raised questions about thermal solutions, possible dual‑use defense applications, and drew analogies to covert projects like the Glomar Explorer, highlighting both excitement and caution.

**Tags**: `#space computing`, `#machine learning`, `#data centers`, `#AI infrastructure`, `#Google`

---

<a id="item-4"></a>
## [Apple Withdraws Advanced Data Protection in UK, Creating Two‑Tier Encryption](https://macanorak.com/two-tier-encryption-in-the-uk/) ⭐️ 8.0/10

Apple withdrew its Advanced Data Protection (ADP) feature for UK users after facing legal pressure, causing iCloud data that was previously fully end‑to‑end encrypted to revert to Standard Data Protection for some categories while other categories remain end‑to‑end encrypted. The move creates a two‑tier encryption system in the UK, raising concerns about user privacy, setting a precedent for government access to cloud data, and affecting the global debate on corporate resistance to surveillance laws. ADP originally expanded end‑to‑end encryption from 14 default iCloud categories to 23; without ADP, the additional nine categories (Backup, Photos, Notes, iCloud Drive, etc.) revert to Standard Data Protection where Apple holds the decryption keys, while the original 14 categories (Keychain, Health, etc.) stay end‑to‑end encrypted.

hackernews · ReturnoftheHack · Sep 24, 10:39 · [Discussion](https://news.ycombinator.com/item?id=49828731)

**Background**: Advanced Data Protection is an optional iCloud feature that stores encryption keys only on the user’s trusted devices, providing end‑to‑end encryption for data such as backups, photos, and notes. When ADP is not enabled, iCloud uses Standard Data Protection, where Apple retains the encryption keys and can access user data in response to lawful requests. In the UK, laws such as the Investigatory Powers Act allow authorities to compel companies to hand over data, creating the legal pressure that led Apple to withdraw ADP for UK users.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/legal/privacy/data/en/advanced-data-protection/">Legal - Advanced Data Protection Analytics & Privacy- Apple</a></li>
<li><a href="https://www.idownloadblog.com/2025/02/26/how-to-turn-on-advanced-data-protection-for-icloud/">Why and how to enable Advanced Data Protection for iCloud</a></li>
<li><a href="https://www.macworld.com/article/1439693/how-to-enable-manage-advanced-data-protection-icloud-data.html">How to enable and manage Apple 's Advanced Data Protection for...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed disappointment that Apple yielded to legal pressure, contrasting it with its earlier stance against the FBI, and warned that conceding once opens the door to further demands. Some noted that the baseline 14 categories remain end‑to‑end encrypted, but the loss of ADP expands government‑accessible data. A few urged Apple to exit the UK market or stop selling to the government as a stronger response.

**Tags**: `#encryption`, `#privacy`, `#Apple`, `#UK law`, `#data protection`

---

<a id="item-5"></a>
## [California targets wealthy residents amid wealth and talent flight](https://blog.landeconomics.org/p/california-is-chasing-wealth-that) ⭐️ 8.0/10

California policymakers are considering or implementing wealth taxes on high-net-worth individuals, prompting concerns that affluent residents may relocate to lower-tax states, taking their assets and talent with them. The debate highlights how tax policy can influence where wealthy individuals and skilled workers choose to live, affecting state revenue, economic growth, and competitiveness in sectors like technology. Proposals include a net wealth tax above a certain threshold and a land value tax that targets only the unimproved value of land, both aimed at capturing immobile wealth while avoiding easy avoidance through relocation.

hackernews · idbnstra · Sep 24, 20:34 · [Discussion](https://news.ycombinator.com/item?id=49836419)

**Background**: A wealth tax is levied on an individual's net assets above a set threshold, while a land value tax taxes only the value of land itself, excluding buildings and improvements. Economists argue that land value taxes are efficient and hard to evade because land cannot be moved. In California, high earners and tech talent have shown a tendency to migrate to states with lower taxes, raising concerns about the effectiveness of such tax measures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wealth_tax">Wealth tax - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Land_value_tax">Land value tax - Wikipedia</a></li>
<li><a href="https://cepr.org/voxeu/columns/global-talent-mobility-and-human-capital-agglomeration">Global talent mobility and human capital agglomeration - CEPR</a></li>

</ul>
</details>

**Discussion**: Commenters discuss the merits of land value tax, noting it cannot be avoided by leaving and questioning whether it can be passed to renters. Others warn that wealth taxes are ineffective because the ultra‑wealthy can simply relocate or fight in court, and some point out practical issues with assessing land versus improvement values in practice.

**Tags**: `#wealth tax`, `#land value tax`, `#California policy`, `#talent migration`, `#economics`

---

<a id="item-6"></a>
## [Experimental Study Shows Rule-Based Pricing Design Raises Market Prices](https://arxiv.org/abs/2609.26861) ⭐️ 8.0/10

In a controlled market experiment, participants used dashboards to build pricing algorithms that competed in a sequential Bertrand game over multiple periods, with treatments varying warnings about price wars, pre-configured strategies, and advice from a large language model. Most treatment variations led to higher market prices, driven by increased starting prices and more cooperative algorithm designs. The findings reveal how design features of widely used rule-based pricing tools can influence market outcomes, offering direct guidance for competition policy and platform regulators seeking to curb anticompetitive effects of algorithmic pricing. It underscores the need to consider algorithm design, not just outcomes, in antitrust analysis. The experiment employed a sequential Bertrand game where participants set prices via rule-based algorithms; treatments included warnings, pre‑configured strategies, and LLM‑generated advice. Higher market prices emerged primarily from higher initial price settings and a shift toward more cooperative algorithmic strategies.

rss · arXiv Quantitative Finance · Sep 24, 04:00

**Background**: Rule-based pricing tools are common in digital commerce, allowing sellers to automate price adjustments using simple if‑then rules. A sequential Bertrand game models price competition where firms choose prices in order, potentially leading to different outcomes than simultaneous price setting. Large language models can generate strategic advice that influences how participants design their pricing rules.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bertrand_competition">Bertrand competition - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2609.26861">Rule - Based Pricing Algorithms and Market Outcomes: An...</a></li>
<li><a href="https://sloanreview.mit.edu/article/how-to-use-generative-ai-for-pricing/">How to Use Generative AI for Pricing | MIT Sloan Management Review</a></li>

</ul>
</details>

**Tags**: `#algorithmic pricing`, `#market experiments`, `#competition policy`, `#LLM advice`, `#Bertrand competition`

---

<a id="item-7"></a>
## [Sovereign Grassroots Currencies: A CBDC Architecture for Credit and Monetary Policy](https://arxiv.org/abs/2609.27727) ⭐️ 8.0/10

The paper proposes a CBDC architecture built on grassroots currencies and bonds that enables credit creation, reduces deposit flight risk, and integrates directly with monetary policy operations. By solving two key limitations of existing CBDC designs—deposit flight and exclusion from credit creation—the approach could shape future central bank digital currency frameworks and monetary policy tools. The architecture comprises sovereign grassroots coins (direct CBDC), non‑sovereign grassroots coins (credit issuance by any entity), and grassroots bonds (sovereign and non‑sovereign) that provide interest; the central bank can lend, absorb liquidity, set rates, and trade securities in these instruments without converting bank deposits.

rss · arXiv Quantitative Finance · Sep 24, 04:00

**Background**: A central bank digital currency (CBDC) is a digital form of fiat money issued by the central bank and held by the public. Existing CBDC designs risk accelerating deposit flight as users shift bank deposits to CBDC, and they typically remain outside the credit creation process, limiting their use in monetary policy. Grassroots currencies are digital tokens issued by trusted community members that can be redeemed at par, enabling local credit creation without external capital. Grassroots bonds extend this concept by adding maturity and interest, allowing the instruments to function like standard banking tools.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2202.05619v17">Grassroots Currencies: Foundations for Grassroots Digital ...</a></li>
<li><a href="https://arxiv.org/html/2609.27727v1">Sovereign Grassroots Currencies: A CBDC Architecture for ...</a></li>
<li><a href="https://arxiv.org/html/2603.13671v3">Grassroots Bonds as a Foundation for Market Liquidity - arXiv</a></li>

</ul>
</details>

**Tags**: `#CBDC`, `#digital currency`, `#monetary policy`, `#grassroots currency`, `#central banking`

---

<a id="item-8"></a>
## [Frozen Statistical Referee Boosts LLM-Driven Investment Factor Discovery](https://arxiv.org/abs/2609.27051) ⭐️ 8.0/10

The paper introduces a frozen statistical referee that uses anytime-valid betting strategies to validate investment factors proposed by LLM agents, showing it admits far fewer false factors than leaky referees. By providing strong false-discovery guarantees, the approach mitigates overfitting in automated quantitative research and could improve the reliability of LLM‑generated factor models. The referee scores each candidate only on market outcomes revealed after submission via betting, guaranteeing false‑discovery control at any stopping time; under a scripted proposer it admits 5‑11 times fewer sub‑threshold factors than leaky referees, while the LLM proposer matches a bandit and can write its own diagnostic probes.

rss · arXiv Quantitative Finance · Sep 24, 04:00

**Background**: Anytime-valid betting strategies are sequential testing procedures that maintain type‑I error control at any stopping time, allowing continuous monitoring of hypotheses without pre‑specified sample sizes. False discovery rate (FDR) control, exemplified by the Benjamini‑Hochberg procedure, limits the expected proportion of false positives among declared discoveries in multiple hypothesis testing. In quantitative finance, language‑model agents can autonomously propose, backtest, and select investment factors, but they risk overfitting without rigorous statistical safeguards. The paper combines these ideas by placing a frozen, anytime‑valid referee outside the agent’s influence to judge factor proposals.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.06521v1">Time-sensitive anytime-valid testing</a></li>
<li><a href="https://en.wikipedia.org/wiki/False_discovery_rate">False discovery rate - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2609.27051">Propose, Don’t Judge: An Anytime-Valid Referee for LLM Agents That...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#quantitative finance`, `#anytime-valid inference`, `#factor mining`, `#false discovery control`

---

<a id="item-9"></a>
## [Local Weak Limits Prove Convergence of Equilibrium and Risk in Sparse Economic Networks.](https://arxiv.org/abs/2609.27107) ⭐️ 8.0/10

The authors prove local weak limit theorems for equilibrium distributions and risk measures in large sparse economic networks, showing convergence in probability under uniformly contractive responses and bounded monotone nonexpansive responses whose lower and upper root iterations coalesce, and illustrate the results with numerical experiments on production and payment clearing systems. This provides a rigorous theoretical foundation for analyzing systemic risk in large economic networks, enabling scalable approximations of equilibrium outcomes and law-invariant risk measures such as conditional value‑at‑risk, which are essential for regulators and financial institutions. The proof relies on marked local weak convergence, establishing convergence in probability for uniformly contractive responses and for bounded monotone nonexpansive responses where lower and upper root iterations coalesce; the result extends to law-invariant risk measures with recursion‑depth error bounds under additional regularity assumptions.

rss · arXiv Quantitative Finance · Sep 24, 04:00

**Background**: Local weak convergence is a notion of convergence for sequences of random rooted graphs, where the distribution of neighborhoods around a randomly chosen node stabilizes as the graph size grows. In sparse economic networks, it allows the global equilibrium distribution to be approximated by local computations on a limiting rooted network. Equilibrium refers to a state where agents' decisions (e.g., production, payments) are mutually consistent given bilateral exposures and shocks, while risk measures such as conditional value‑at‑risk evaluate tail risk and are law‑invariant when they depend only on the distribution of outcomes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convergence_of_measures">Convergence of measures - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2609.27107">Local Weak Limits for Equilibrium and Risk in Economic Networks</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6759138">Local Approximation of Systemic Risk in Large Sparse Economic ...</a></li>

</ul>
</details>

**Tags**: `#economic networks`, `#local weak convergence`, `#equilibrium analysis`, `#risk measures`, `#systemic risk`

---

<a id="item-10"></a>
## [Proof of Stake economy under centralized exchanges--a mean field model](https://arxiv.org/abs/2606.09003) ⭐️ 8.0/10

The paper introduces a continuous-time mean-field model where participants act as both PoS validators and traders on centralized exchanges, showing that exchange trading can increase staking participation and promote decentralization of token holdings. By challenging the common view that centralized exchanges undermine blockchain decentralization, the work offers new insights for designing tokenomics and exchange integration that can actually strengthen network security. The model establishes local well-posedness under mild assumptions, derives a semi-explicit equilibrium trading strategy, and examines how transaction costs and token supply mechanisms affect the equilibrium staking ratio and concentration profile.

rss · arXiv Quantitative Finance · Sep 24, 04:00

**Background**: Proof-of-Stake (PoS) is a consensus mechanism where validators lock up tokens to secure the blockchain and earn rewards proportional to their stake. Centralized exchanges (CEXs) dominate crypto trading volume and can influence token prices through their order flow and liquidity provision. Mean-field games model large populations of interacting agents, allowing analysis of how individual trading strategies aggregate to affect system-wide outcomes such as staking distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.09003v2">Proof of Stake economy under centralized exchanges - arXiv</a></li>
<li><a href="https://www.investopedia.com/terms/p/proof-stake-pos.asp">Understanding Proof-of-Stake: How PoS Transforms Cryptocurrency</a></li>
<li><a href="https://ideas.repec.org/a/spr/digfin/v6y2024i3d10.1007_s42521-024-00113-4.html">A mean field game model of staking system - IDEAS/RePEc</a></li>

</ul>
</details>

**Tags**: `#Proof of Stake`, `#Centralized Exchanges`, `#Mean Field Game`, `#Blockchain Economics`, `#Cryptocurrency`

---

<a id="item-11"></a>
## [Leaky-integrator reconstruction: taming error accumulation in recursive differenced time-series forecasting](https://arxiv.org/abs/2609.23378) ⭐️ 8.0/10

The paper introduces leaky-integrator reconstruction, a training‑free method that replaces the pure cumulative sum in recursive differenced forecasting with a first‑order IIR filter H(z)=1/(1−γz⁻¹) (γ<1) to move the integrator pole inside the unit circle. Applying it post‑hoc with a fixed γ=0.9 requires only a two‑line code change and improves rollout stability without retraining. Error accumulation causes divergent forecasts in recursive differenced models, limiting their usefulness for long horizons; the leaky‑integrator fix bounds this error and yields consistent gains across architectures and datasets. Because it needs no retraining and works with any existing one‑step or foundation model forecaster, it offers a simple, practical improvement for real‑world time‑series applications. Experiments show that with γ=0.9 the normalized MAE drops from 1.6‑3.8 (unstable) to 0.87‑0.97, and the relative improvement grows from ~3% at horizon 24 to 51% at horizon 336 (up to 78% with an optimal pole). These results hold across seven different neural architectures and twenty diverse datasets, confirming the method’s robustness.

rss · arXiv Quantitative Finance · Sep 24, 04:00

**Background**: Recursive differenced forecasting handles non‑stationarity by predicting one‑step changes and reconstructing the series through cumulative summation, which is mathematically a discrete integrator with a pole on the unit circle. Because the learned increment model is biased, its errors accumulate without bound during rollout, causing the forecast to diverge as the horizon grows. A leaky integrator replaces the pure integrator with a first‑order low‑pass filter H(z)=1/(1−γz⁻¹) (γ<1), moving the pole inside the unit circle and thus damping the accumulated error.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.23378v2">[2609.23378v2] Leaky-integrator reconstruction: taming error accumulation in recursive differenced time-series forecasting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leaky_integrator">Leaky integrator - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#time-series forecasting`, `#recursive differencing`, `#leaky integrator`, `#error accumulation`, `#machine learning`

---