---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 13 items, 3 important content pieces were selected

---

1. [Chromium 148's Math.tanh now leaks OS via JavaScript fingerprinting.](#item-1) ⭐️ 8.0/10
2. [Terry Tao uses LLM coding agents to build educational apps.](#item-2) ⭐️ 8.0/10
3. [George Hotz critiques LLM hype and inflated valuations.](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Chromium 148's Math.tanh now leaks OS via JavaScript fingerprinting.](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 8.0/10

Starting with Chromium version 148, the V8 engine switched Math.tanh from a bundled fdlibm implementation to the host operating system's native libm, causing OS‑specific floating‑point results that can be read via JavaScript. This subtle difference creates a new browser‑fingerprinting vector that lets websites infer a user's underlying OS, potentially undermining privacy protections and User‑Agent spoofing. The change makes Math.tanh the only standard JavaScript Math function whose output varies by OS in Chromium 148, while other Math functions remain OS‑independent due to the bundled fdlibm.

hackernews · joahnn_s · Jul 12, 21:12 · [Discussion](https://news.ycombinator.com/item?id=48884853)

**Background**: Before Chromium 148, V8 used a portable fdlibm implementation for Math.tanh, giving identical results across all operating systems. Starting with version 148, V8 delegates the calculation to the platform’s libm library, which produces slightly different last‑bit values on Linux, macOS, and Windows for certain inputs. Because the IEEE 754 standard does not require transcendental functions to be correctly rounded, these tiny differences can be measured from JavaScript and used as a fingerprinting signal.

<details><summary>References</summary>
<ul>
<li><a href="https://scrapfly.dev/posts/browser-math-os-fingerprint/">Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev</a></li>
<li><a href="https://geekhaus.club/feed/2026/07/12/chrome-s-switch-to-os-native-math-tanh-exposes-a">Chrome’s switch to OS-native Math.tanh exposes a subtle ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/system.math.tanh?view=net-10.0">Math.Tanh (Double) Method (System) | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: Commenters noted that a single tanh call can reveal the OS and even hint at browser version ranges, while some questioned the article's motives as coming from a scraping‑service company. Others welcomed the technical insight, suggested pushing for correctly rounded transcendental functions, and observed that even privacy‑focused browsers like Tor have largely given up on hiding the OS.

**Tags**: `#browser fingerprinting`, `#JavaScript`, `#privacy`, `#Chromium`, `#OS detection`

---

<a id="item-2"></a>
## [Terry Tao uses LLM coding agents to build educational apps.](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 8.0/10

In his July 2026 blog post, Fields Medalist Terry Tao describes how he employed modern LLM coding agents to create interactive visualizations and small applications for teaching, noting both the productivity gains and the current limitations of the approach. Tao's experience illustrates how LLM-powered coding agents are becoming practical tools for experts outside traditional software engineering, potentially accelerating educational content creation across disciplines. He specifically mentions using Claude to design a simplified 8‑bit computer visualization in a few days, and notes that while LLM‑generated code boosts productivity, it still requires human oversight for correctness and integration.

hackernews · subset · Jul 12, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48880170)

**Background**: Modern LLM coding agents have evolved beyond simple autocomplete, capable of generating entire features from natural language prompts, debugging complex issues, refactoring legacy code, and even deploying changes autonomously. In 2026, a variety of mature tools such as OpenCode, Gemini CLI, and Codex support dozens of LLM providers and local models via platforms like Ollama and LM Studio. These AI‑assisted programming systems aim to augment developer productivity rather than replace human programmers, though they still require verification and integration by humans.

<details><summary>References</summary>
<ul>
<li><a href="https://www.morphllm.com/best-ai-coding-agents-2026">Best AI Coding Agents (June 2026): Scored Leaderboard</a></li>
<li><a href="https://openagents.org/blog/posts/2026-05-21-best-ai-coding-agents">10 Best AI Coding Agents in 2026 — Complete Guide ...</a></li>
<li><a href="https://benchlm.ai/coding">Best LLMs for Coding — July 2026 Leaderboard | BenchLM.ai</a></li>

</ul>
</details>

**Discussion**: Commenters praised the ability of LLM coding agents to quickly create educational visualizations and fill gaps in teaching resources, while also noting the tools are best suited for non‑mission‑critical tasks and require human oversight. Some highlighted the vast untapped demand for software in non‑traditional domains, suggesting that even current capabilities will take years to fully absorb. Others offered humorous analogies, comparing the experience to a gourmet chef embracing microwave meals, underscoring both excitement and skepticism about reliance on AI‑generated code.

**Tags**: `#LLM`, `#coding agents`, `#AI-assisted programming`, `#software engineering`, `#Terry Tao`

---

<a id="item-3"></a>
## [George Hotz critiques LLM hype and inflated valuations.](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

In a July 12, 2026 blog post, George Hotz argues that while large language models are genuinely useful, the surrounding hype inflates the valuations of frontier AI labs and discusses the resulting effects on productivity and open‑source software. His critique highlights a growing disconnect between AI investment hype and actual value capture, warning investors and developers that current valuations may be unsustainable. Hotz points out that frontier labs charge $100–$200 per month for bounded token usage, suggesting users are paying premium rates for limited access, and he notes that productivity gains often manifest as private, one‑off tools rather than widespread software.

hackernews · therepanic · Jul 12, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48883343)

**Background**: Large language models such as GPT‑4 and Claude have driven a surge in AI startup valuations, with investors betting on transformative economic impact. Frontier labs often monetize access via API subscriptions, claiming large productivity gains across industries. Meanwhile, open‑source communities have leveraged LLMs to accelerate software development, though concerns persist about model reliability and the sustainability of hype‑driven funding.

**Discussion**: Commenters generally agree with Hotz’s skepticism about inflated valuations, noting that current subscription prices make frontier models a ‘no‑brainer’ for many users. Several raise open‑source concerns, arguing that the ease of forking LLMs reduces incentives to contribute upstream, while others highlight personal productivity gains from building niche, one‑off tools with LLMs.

**Tags**: `#LLMs`, `#AI hype`, `#valuation`, `#open source`, `#productivity`

---