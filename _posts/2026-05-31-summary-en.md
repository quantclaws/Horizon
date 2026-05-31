---
layout: default
title: "Horizon Summary: 2026-05-31 (EN)"
date: 2026-05-31
lang: en
---

> From 16 items, 7 important content pieces were selected

---

1. [: Microsoft to Convert Perpetual Office 2019/2021 for Mac to View‑Only in 2026](#item-1) ⭐️ 8.0/10
2. [: ](#item-2) ⭐️ 8.0/10
3. [Openrsync: OpenBSD's secure reimplementation of rsync using pledge and unveil](#item-3) ⭐️ 8.0/10
4. [OpenRouter Secures $113 Million Series B Funding](#item-4) ⭐️ 8.0/10
5. [: ](#item-5) ⭐️ 8.0/10
6. [Anthropic details sandboxing of Claude across products using gVisor, Seatbelt, Bubblewrap](#item-6) ⭐️ 8.0/10
7. [: Running Python ASGI apps in the browser via Pyodide and service workers](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [: Microsoft to Convert Perpetual Office 2019/2021 for Mac to View‑Only in 2026](https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)) ⭐️ 8.0/10

Microsoft announced that starting in 2026, perpetually licensed Office 2019 and 2021 for Mac will be automatically switched to view‑only mode, disabling editing features while retaining document reading capability. The change undermines the promise of perpetual licenses, pushes users toward subscription‑based Microsoft 365, and raises legal questions under consumer protection laws in jurisdictions such as Australia. View‑only conversion will affect the desktop apps (Word, Excel, PowerPoint, Outlook) but will not remove the software from devices; no further feature updates or security patches will be provided after the switch.

hackernews · antipurist · May 30, 23:26 · [Discussion](https://news.ycombinator.com/item?id=48341578)

**Background**: Perpetual Office licenses are sold as a one‑time purchase with the expectation that the software will continue to work indefinitely without mandatory updates. View‑only mode disables editing capabilities while still allowing users to open and read documents, a restriction often used in trial or evaluation versions. In Australia, consumer law guarantees that products must be fit for the advertised purpose and that buyers have undisturbed possession, which could be violated if Microsoft alters the functionality of already sold perpetual licenses.

<details><summary>References</summary>
<ul>
<li><a href="https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)">Microsoft Office 2019 and 2021 for Mac view - only conversion (2026)</a></li>
<li><a href="https://licendi.com/en/blog/microsoft-office-perpetual-licenses-vs-subscriptions/">Microsoft Office perpetual licenses vs. subscriptions</a></li>
<li><a href="https://www.microsoft.com/licensing/guidance/Office-LTSC">Office LTSC Licensing Guidance - microsoft.com</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong opposition, urging users to stop buying Microsoft software and to switch to alternatives like LibreOffice. Some highlighted potential violations of Australian consumer guarantees, while others speculated that the move is driven by Microsoft’s desire to license each AI agent instance separately. Overall, the discussion frames the change as an anti‑consumer tactic that could accelerate a shift away from perpetual licenses.

**Tags**: `#Microsoft`, `#Office`, `#licensing`, `#consumer rights`, `#SaaS`

---

<a id="item-2"></a>
## [: ](https://ziglang.org/devlog/2026/#2026-05-30) ⭐️ 8.0/10

Zig team shares progress on ELF linker enhancements aimed at faster compilation and positioning Zig as a viable C alternative.

hackernews · kristoff_it · May 30, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48338673)

**Tags**: `#Zig`, `#ELF linker`, `#compiler improvements`, `#systems programming`, `#language development`

---

<a id="item-3"></a>
## [Openrsync: OpenBSD's secure reimplementation of rsync using pledge and unveil](https://github.com/kristapsdz/openrsync) ⭐️ 8.0/10

Openrsync is a new rsync implementation developed by the OpenBSD team that leverages the pledge(2) and unveil(2) system calls to enhance security. It provides a safer alternative to traditional rsync, especially for environments where limiting system access is critical, and showcases OpenBSD's security innovations. Openrsync uses pledge to restrict the program's system capabilities and unveil to limit visible filesystem paths, and it is being developed alongside an RPKI validator project.

hackernews · sph · May 30, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48334854)

**Background**: The pledge() system call in OpenBSD allows a process to promise it will only use a limited set of system resources, reducing the impact of compromises. The unveil() system call restricts which parts of the filesystem a process can access, hiding the rest from view. Together they provide a defense-in-depth mechanism that limits what a program can do even if exploited.

<details><summary>References</summary>
<ul>
<li><a href="https://man.openbsd.org/pledge">pledge (2) - OpenBSD manual pages</a></li>
<li><a href="https://man.openbsd.org/unveil">unveil (2) - OpenBSD manual pages</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD_security_features">OpenBSD security features - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters appreciate Openrsync's progress and security focus, noting its growing usability; some point out minor compatibility gaps with Samba rsync, while others highlight its role in RPKI validator development and discuss the importance of pledge/unveil, with a few questioning pledge availability on Linux.

**Tags**: `#rsync`, `#OpenBSD`, `#security`, `#open-source`, `#file-synchronization`

---

<a id="item-4"></a>
## [OpenRouter Secures $113 Million Series B Funding](https://openrouter.ai/announcements/series-b) ⭐️ 8.0/10

OpenRouter announced a $113 million Series B funding round to scale its LLM proxy service, which offers unified API access to multiple language models and built‑in billing caps. The large investment signals strong investor confidence in LLM aggregation platforms and suggests accelerated adoption of unified model‑access tools among developers. OpenRouter emphasizes that it will remain founder‑led and founder‑controlled, aiming to serve builders worldwide long‑term, while its proxy service provides low‑friction model trial and hard billing limits.

hackernews · freeCandy · May 30, 17:27 · [Discussion](https://news.ycombinator.com/item?id=48338660)

**Background**: An LLM proxy service acts as a gateway that presents a single, often OpenAI‑compatible, API to route requests to various language‑model providers, eliminating the need to manage multiple vendor SDKs. Such proxies can add features like billing caps, caching, failover, and usage analytics without requiring code changes. Examples include LiteLLM Proxy and Arbio’s cloud‑based LLM proxy, which demonstrate how a unified interface simplifies model experimentation and cost control.

<details><summary>References</summary>
<ul>
<li><a href="https://litellm.vercel.app/docs/providers/litellm_proxy">LiteLLM Proxy ( LLM Gateway) | liteLLM</a></li>
<li><a href="https://www.arbio.ai/">Secure LLM Proxy Service | Arbio</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated OpenRouter’s low‑friction way to try many models and its billing caps, with some initially skeptical about the need for a proxy. The co‑founder stressed the company’s founder‑led vision, while users noted the service’s convenience for experimenting with new models but questioned the cost‑effectiveness of routing expensive models through the platform.

**Tags**: `#AI`, `#LLM`, `#funding`, `#developer tools`, `#OpenRouter`

---

<a id="item-5"></a>
## [: ](https://www.economist.com/europe/2026/05/28/leos-first-encyclical-attacks-technological-messianism) ⭐️ 8.0/10

Pope Leo's first encyclical critiques the belief that technology, especially AI, can serve as a messianic savior, urging ethical caution.

hackernews · 1vuio0pswjnm7 · May 30, 10:30 · [Discussion](https://news.ycombinator.com/item?id=48334710)

**Tags**: `#AI ethics`, `#religion`, `#technology criticism`, `#papal encyclical`, `#techno-optimism`

---

<a id="item-6"></a>
## [Anthropic details sandboxing of Claude across products using gVisor, Seatbelt, Bubblewrap](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything) ⭐️ 8.0/10

Anthropic published a detailed explanation of how they sandbox Claude across Claude.ai, Claude Code, and Cowork using gVisor, Seatbelt, and Bubblewrap. The transparency helps developers and security practitioners assess the safety of AI agents and informs best practices for sandboxing generative AI systems. Claude.ai runs under gVisor, Claude Code uses Seatbelt on macOS and Bubblewrap on Linux locally, while Claude Cowork runs a full VM via Apple’s Virtualization framework on macOS and HCS on Windows.

rss · Simon Willison · May 30, 21:36

**Background**: Sandboxing isolates processes to limit their access to system resources, reducing the risk of malicious or unintended actions. gVisor is a user‑space kernel that intercepts system calls, providing container‑like isolation without a full VM. Seatbelt is macOS’s mandatory access control framework that enforces kernel‑level restrictions on file system, network, and system calls, while Bubblewrap uses Linux namespaces to create unprivileged containers. Full VMs, such as those used by Claude Cowork, provide the strongest isolation by running a separate virtual machine via hypervisors like Apple’s Virtualization framework or Windows’ HCS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GVisor">gVisor - Wikipedia</a></li>
<li><a href="https://deepwiki.com/waywardgeek/gemini-cli/11.2-macos-seatbelt-sandboxing">macOS Seatbelt Sandboxing | waywardgeek/gemini-cli | DeepWiki</a></li>
<li><a href="https://wiki.archlinux.org/title/Bubblewrap">Bubblewrap - ArchWiki</a></li>

</ul>
</details>

**Tags**: `#sandboxing`, `#AI safety`, `#Anthropic`, `#Claude`, `#security`

---

<a id="item-7"></a>
## [: Running Python ASGI apps in the browser via Pyodide and service workers](https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything) ⭐️ 8.0/10

Simon Willison demonstrated a method to run Python ASGI applications in the browser by combining Pyodide with a service worker, which overcomes the earlier limitation where JavaScript in <script> tags would not execute. He provided working demos of an ASGI FastCGI app and Datasette 1.0a31 running via this approach. This advancement enables full JavaScript execution in client‑side Python web apps, allowing plugins and interactive features that were previously broken. It broadens the applicability of ASGI frameworks like Datasette for rich browser‑based tools. The solution uses a service worker’s fetch event to intercept network requests, serve HTML generated by an ASGI app running inside Pyodide, and thereby allows <script> tags to execute. Simon built the prototype with assistance from Claude Opus 4.8 and plans to integrate it into Datasette Lite.

rss · Simon Willison · May 30, 21:02

**Background**: Pyodide compiles the CPython interpreter to WebAssembly, enabling Python code to run directly in the browser with access to libraries like NumPy and Pandas. ASGI (Asynchronous Server Gateway Interface) is a standard interface for asynchronous Python web servers, frameworks, and applications, succeeding WSGI. Service workers are scripts that run in the background and can intercept fetch events to modify or serve network responses, allowing client‑side request handling.

<details><summary>References</summary>
<ul>
<li><a href="https://pyodide.com/">Pyodide – Run Python in Browser with WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface">Asynchronous Server Gateway Interface - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event">ServiceWorkerGlobalScope: fetch event - Web APIs | MDN</a></li>

</ul>
</details>

**Tags**: `#Pyodide`, `#ASGI`, `#WebAssembly`, `#Service Workers`, `#Datasette`

---