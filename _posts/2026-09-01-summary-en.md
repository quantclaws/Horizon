---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 22 items, 4 important content pieces were selected

---

1. [Community-curated ChatGPT Work tool reference guide with Playwright browser control skill](#item-1) ⭐️ 8.0/10
2. [Google Removes Manifest V2 Extensions from Chrome Web Store](#item-2) ⭐️ 8.0/10
3. [Leakage-safe, search-aware system corrects LLM trading strategy bias](#item-3) ⭐️ 8.0/10
4. [AI Agents Reduce Position Bias in Search, Favoring Page Attributes Over Ranking](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Community-curated ChatGPT Work tool reference guide with Playwright browser control skill](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 8.0/10

A community-curated reference guide for ChatGPT Work has been published, showcasing a skill that uses Playwright to control a browser via Node.js REPL. The guide includes example code that launches Playwright and retrieves browser documentation through ChatGPT Work. The reference provides practical ways to extend ChatGPT Work beyond its default capabilities, highlighting how developers can integrate browser automation and reduce reliance on manual token-heavy interactions. It also sparks discussion about the differences between ChatGPT Work and Codex, and about token usage efficiency. The Playwright skill demonstrates launching a browser instance, writing to its Node.js REPL, and calling browser.documentation() to retrieve detailed usage instructions. The guide is hosted at https://codex-tool-reference.simonw.chatgpt.site/ and includes community comments discussing token costs and comparisons to Codex.

hackernews · ijidak · Aug 31, 14:07 · [Discussion](https://news.ycombinator.com/item?id=49510000)

**Background**: ChatGPT Work is a tool that gathers context, plans actions, and operates across apps, files, and desktop applications to produce spreadsheets, documents, and slides, powered by GPT-5.6. Playwright enables reliable browser control by communicating directly through the DevTools protocol, allowing commands such as navigation and input to execute when the browser is ready. This reduces flakiness compared to abstraction‑layer frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://chatgpt.com/work/">ChatGPT Work for Every Team</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://www.browserstack.com/guide/playwright-vs-robot-framework">Playwright vs Robot Framework: How They Compare... | BrowserStack</a></li>

</ul>
</details>

**Discussion**: Simonw highlighted the browser‑control skill as the most interesting part of the guide. Satvikpendem questioned how this differs from Codex, while darepublic warned that some tools could waste plentiful tokens. Enraged_camel noted that AI‑generated websites often share a uniform look, reminiscent of early Bootstrap‑era sites.

**Tags**: `#ChatGPT`, `#AI tooling`, `#Playwright`, `#developer reference`, `#Hacker News`

---

<a id="item-2"></a>
## [Google Removes Manifest V2 Extensions from Chrome Web Store](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has removed all Manifest V2 extensions from the Chrome Web Store, including the popular ad blocker uBlock Origin. The move affects users who rely on MV2‑based ad blockers, pushing them toward alternatives like Firefox or the MV3‑based uBlock Origin Lite, and highlights Google’s unilateral control over browser extension ecosystems. Manifest V2 is being phased out in favor of Manifest V3, which imposes stricter limits on extension capabilities; uBlock Origin Lite is the MV3‑compatible version now offered in the Chrome Web Store.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**Background**: Manifest V2 is the older extension framework that Chrome has been phasing out since 2020, with the Chrome Web Store no longer accepting new MV2 submissions. According to Google's timeline, support for MV2 extensions will be removed from Chrome starting in June 2025 for enterprise users and gradually for all users thereafter, with warnings appearing in beta channels from June 2026. Over 85% of actively maintained extensions have already migrated to Manifest V3, and major content blockers now offer MV3 versions.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://blog.google/chromium/manifest-v2-phase-out-begins/">Manifest V2 phase-out begins</a></li>
<li><a href="https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en">uBlock Origin Lite - Chrome Web Store</a></li>

</ul>
</details>

**Discussion**: Commenters expressed worry that removing MV2 extensions like uBlock Origin reduces protection against malicious ads, especially for less tech‑savvy users. Many said they would switch to Firefox or use forks to avoid Google’s unilateral control over the browser ecosystem. Some noted that uBlock Origin already works better in Firefox and recommended migrating now.

**Tags**: `#Chrome`, `#Manifest V2`, `#Ad blocking`, `#Browser extensions`, `#Privacy`

---

<a id="item-3"></a>
## [Leakage-safe, search-aware system corrects LLM trading strategy bias](https://arxiv.org/abs/2608.27734) ⭐️ 8.0/10

The paper introduces a leakage-safe, search-aware system for LLM-driven trading strategy discovery that uses registry‑validated tools to exclude look‑ahead bias by construction and applies trial‑count deflation to correct for search intensity. It evaluates the approach on a 453‑stock US equity universe and a 39‑ETF multi‑asset universe with realistic costs, testing two frontier LLMs across up to 100 candidates and five repeated runs. By structurally correcting look‑ahead bias and search overfitting, the work addresses a well‑known methodological flaw in LLM‑based financial research, increasing the credibility of discovered strategies. This benefits both academics developing LLM trading tools and practitioners who rely on robust strategy validation. The system restricts the agent to registry‑validated tools whose feature space deliberately excludes look‑ahead information, and it records every strategy evaluation to deflate reported performance by the total number of trials, using Deflated Sharpe Ratio and probability‑of‑backtest‑overfitting tests. Even a deliberately leaky oracle posting a Sharpe ratio of 35 fails these tests, and honest evaluation rejects all LLM‑discovered strategies across models and search budgets while certifying passive benchmarks and evaluating a human trader’s rule set under the same conditions.

rss · arXiv Quantitative Finance · Aug 31, 04:00

**Background**: Large language models are increasingly employed to mine trading strategies, but typical pipelines generate many candidates, report the best, and ignore look‑ahead bias and the inflation caused by searching over many possibilities. The Deflated Sharpe Ratio adjusts raw performance for the number of independent trials, while the probability of backtest overfitting quantifies the chance that a strategy’s in‑sample superiority is due to luck. Registry‑validated tools restrict the model’s actions to pre‑approved, bias‑free functions, making the correction structural rather than procedural.

<details><summary>References</summary>
<ul>
<li><a href="https://quanterlab.com/articles/qlway-deflated-sharpe">The Deflated Sharpe Ratio: correcting for how many tries you took - QuanterLab</a></li>
<li><a href="https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf">THE PROBABILITY OF BACKTEST OVERFITTING David H. Bailey ∗ Jonathan M. Borwein †</a></li>
<li><a href="https://github.com/TauricResearch/TradingAgents">TauricResearch/TradingAgents: TradingAgents: Multi-Agents LLM ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#trading strategies`, `#look-ahead bias`, `#financial AI`, `#methodology`

---

<a id="item-4"></a>
## [AI Agents Reduce Position Bias in Search, Favoring Page Attributes Over Ranking](https://arxiv.org/abs/2608.22697) ⭐️ 8.0/10

The study randomized the order of 100 hotel listings across 5,000 sessions with four large language models acting as AI agents and compared their behavior to human field data. It found that AI agents inspect results more deeply than humans, never decline to buy, and show a weakened, non‑monotonic position bias where the middle of a list is least likely to be inspected. Understanding how AI agents alter search behavior is crucial for designing recommendation and advertising systems that remain effective when humans delegate search to AI. The results suggest that optimizing page‑level attributes may yield better returns than fine‑tuning positional rankings. The experiment used four LLMs (unspecified versions) to simulate AI agents, each completing 5,000 randomized sessions; agents never opted out of purchasing and converged on the same undominated hotel. Position influenced inspection probability weakly and non‑monotonically, with the lowest inspection rate at the middle of the list, while the bottom was inspected more often than the middle.

rss · arXiv Quantitative Finance · Aug 31, 04:00

**Background**: In traditional web search, higher‑ranked items receive more attention because users scan results sequentially and have limited time, creating a strong position bias. AI agents, powered by large language models, can process an entire results page at once, potentially reducing reliance on position. This study examines whether that capability changes how users (via agents) make choices. It also highlights the growing role of AI‑mediated search in e‑commerce and information retrieval.

**Tags**: `#AI agents`, `#search ranking`, `#position bias`, `#large language models`, `#human-computer interaction`

---