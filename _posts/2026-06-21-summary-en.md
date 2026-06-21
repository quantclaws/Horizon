---
layout: default
title: "Horizon Summary: 2026-06-21 (EN)"
date: 2026-06-21
lang: en
---

> From 13 items, 5 important content pieces were selected

---

1. [Loupe iOS app exposes native app data access to highlight privacy fingerprinting](#item-1) ⭐️ 8.0/10
2. [SMPTE Makes Its Standards Freely Accessible to Global Community](#item-2) ⭐️ 8.0/10
3. [Linux Kernel Removes Unsafe strncpy API After Six‑Year Cleanup](#item-3) ⭐️ 8.0/10
4. [The Wholesale Plagiarism of Obscure Sorrows](#item-4) ⭐️ 8.0/10
5. [Bun proposes shared-memory threads for JavaScriptCore to enable true multithreading](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Loupe iOS app exposes native app data access to highlight privacy fingerprinting](https://github.com/mysk-research/loupe) ⭐️ 8.0/10

Loupe, an iOS/iPadOS app released by mysk-research on GitHub, demonstrates what data native apps can access by reading public iOS APIs and displaying the raw values to users. The app highlights specific iOS privacy leaks—such as volume creation date and last setup timestamp—that enable device fingerprinting, raising user awareness and pressuring Apple to improve privacy protections. Loupe accesses APIs that report volume creation date, device erase/setup time, pasteboard change count, and an installed‑app probe, showing how seemingly innocuous data can be combined for fingerprinting; it does not block or mitigate these leaks, only visualizes them.

hackernews · Cider9986 · Jun 20, 12:08 · [Discussion](https://news.ycombinator.com/item?id=48608645)

**Background**: Device fingerprinting on iOS relies on collecting seemingly innocuous hardware and software signals—such as volume creation dates, pasteboard change counts, and installed app lists—to uniquely identify a device without user consent. Recent research has cataloged these signals and explored detection techniques using static and dynamic analysis of apps. The Loupe app implements this research by directly querying the same public iOS APIs that third‑party apps can call, presenting the raw values to users for transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mysk-research/loupe">GitHub - mysk-research/loupe: A privacy-focused iOS app that ...</a></li>
<li><a href="https://blog.appicaptor.com/2023/06/29/device-fingerprinting-on-ios-apps/">Device Fingerprinting on iOS apps - Appicaptor Blog</a></li>
<li><a href="https://dl.acm.org/doi/fullHtml/10.1145/3590777.3590790">Towards detecting device fingerprinting on iOS with API ...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted troubling leaks such as the iPhone’s last setup or erase timestamp and volume creation date, questioning what users can do to mitigate them. Others praised Loupe for filling a long‑felt need, noted that limiting app installations reduces risk, and warned that embedded SDKs from platforms like TikTok and Facebook can still link activity across reinstalls, urging Apple to randomize these fingerprints.

**Tags**: `#iOS`, `#privacy`, `#security`, `#mobile`, `#fingerprinting`

---

<a id="item-2"></a>
## [SMPTE Makes Its Standards Freely Accessible to Global Community](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community) ⭐️ 8.0/10

SMPTE has opened its entire standards library, providing free access to all published SMPTE Standards, Recommended Practices, Engineering Guidelines, and Registered Disclosure Documents. This move lowers barriers for developers and engineers, fostering innovation and interoperability across the media technology ecosystem, and aligns with the industry trend toward open standards. The library includes over 800 technical standards and related documents, now accessible via the SMPTE website as part of a broader modernization effort that adopts GitHub‑based workflows, HTML authoring, and an integrated publishing pipeline, with future releases also free.

hackernews · zdw · Jun 20, 17:01 · [Discussion](https://news.ycombinator.com/item?id=48610827)

**Background**: SMPTE, founded in 1916, is a global professional association that develops standards for motion picture, television, and digital media technologies. Historically, its standards documents were sold as PDFs or printed copies, limiting accessibility. By making its standards freely available, SMPTE follows the model of open standards bodies like the IETF, aiming to increase adoption and collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Society_of_Motion_Picture_and_Television_Engineers">Society of Motion Picture and Television Engineers - Wikipedia</a></li>
<li><a href="https://www.smpte.org/">SMPTE | The home of media professionals, technologists, and engineers</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the decision, praising the move as long overdue and comparing it to the IETF’s open‑standards model; some shared personal experiences of previously purchasing standards PDFs, while others noted the accompanying modernization efforts such as GitHub workflows, and one off‑topic remark referenced a music album.

**Tags**: `#SMPTE`, `#open standards`, `#media technology`, `#standards accessibility`, `#HackerNews`

---

<a id="item-3"></a>
## [Linux Kernel Removes Unsafe strncpy API After Six‑Year Cleanup](https://www.phoronix.com/news/Linux-7.2-Drops-strncpy) ⭐️ 8.0/10

Linux kernel developers have completely removed the strncpy function from the kernel after a six‑year effort involving roughly 360 patches, with the change merged for Linux 7.2. Eliminating the unsafe strncpy API reduces a long‑standing source of bugs and security vulnerabilities in the kernel, improving overall reliability and safety for systems that rely on it. The removal covered all architecture‑specific strncpy implementations and was achieved through about 362 commits, addressing the function’s failure to guarantee null‑termination and its tendency to zero‑fill destination buffers.

hackernews · simonpure · Jun 20, 20:59 · [Discussion](https://news.ycombinator.com/item?id=48612943)

**Background**: The strncpy function is meant to copy strings with a length limit, but it does not guarantee a null‑terminated result and pads the destination with null bytes, which can lead to bugs and security issues. The Linux kernel maintains a list of deprecated interfaces in Documentation/process/deprecated.html to discourage use of unsafe APIs. Over the past six years, contributors replaced strncpy with safer, explicit length‑checked string copies throughout the kernel.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.2-Drops-strncpy">Linux Finally Eliminates The strncpy API After Six Years Of Work, 360+ Patches - Phoronix</a></li>
<li><a href="https://developer.apple.com/forums/thread/658049">Security threat due to insecure function "strncpy ...</a></li>
<li><a href="https://docs.kernel.org/process/deprecated.html">Deprecated Interfaces, Language Features, Attributes, and Conventions — The Linux Kernel documentation</a></li>

</ul>
</details>

**Discussion**: Commenters praised the multi‑year cleanup as essential systems engineering work, noting that removing bad features is as important as adding new ones for a fundamental project like the kernel. Several suggested alternatives such as pairing a pointer with its length, similar to C++'s std::string, while others criticized null‑terminated strings as a historic mistake.

**Tags**: `#Linux`, `#kernel`, `#strncpy`, `#API removal`, `#systems programming`

---

<a id="item-4"></a>
## [The Wholesale Plagiarism of Obscure Sorrows](https://waxy.org/2026/06/the-wholesale-plagiarism-of-obscure-sorrows/) ⭐️ 8.0/10

A website called Qontour allegedly copied the entire text of John Koenig’s 'The Dictionary of Obscure Sorrows' and used AI tools to rebrand the content, then monetized it via an Amazon Associates affiliate link. The case highlights how AI can facilitate large‑scale plagiarism, testing the limits of DMCA takedowns and raising ethical concerns for developers, publishers, and platforms. The bootleg site reproduced the book’s 800‑word foreword and all 311 neologisms verbatim, used the Amazon Associates tag=promptdigital-20 to earn referral fees, and claimed to be a Webflow premium partner while allegedly just copy‑pasting the text after an AI rebranding step.

hackernews · ridesisapis · Jun 20, 18:05 · [Discussion](https://news.ycombinator.com/item?id=48611411)

**Background**: The Dictionary of Obscure Sorrows is a collection of invented words for nuanced emotions, created by John Koenig and published by Simon & Schuster in 2021. AI rebranding tools such as those offered by Templafy or VIM Group can generate or migrate text while adapting it to a new brand identity, but they can also be used to launder plagiarized content. The DMCA provides a legal mechanism for copyright holders to request removal of infringing material, though enforcement often requires a court order and platforms like Google and Apple may ignore notices without one.

<details><summary>References</summary>
<ul>
<li><a href="https://www.templafy.com/rebranding-in-the-ai-era-key-strategies-and-insights/">Rebranding in the AI era: Key strategies and insights - Templafy</a></li>
<li><a href="https://coderfile.io/dmca">DMCA Policy & Takedown Procedure - CoderFile.io</a></li>
<li><a href="https://copyleaks.com/">AI Content & Text Authenticity Detection | Copyleaks</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar experiences of their work being copied and rebranded with AI, criticized platforms for ineffective DMCA handling, pointed out the affiliate monetization method, and called for accountability, while some noted that DMCA takedowns are exactly intended for such cases.

**Tags**: `#plagiarism`, `#copyright`, `#AI`, `#intellectual property`, `#Hacker News`

---

<a id="item-5"></a>
## [Bun proposes shared-memory threads for JavaScriptCore to enable true multithreading](https://github.com/oven-sh/WebKit/pull/249) ⭐️ 8.0/10

Bun has opened a large pull request to add shared-memory threading to JavaScriptCore, introducing a new Thread() primitive that runs closures on separate OS threads while sharing the same JavaScript heap. The PR aims to bring true multi-threading capabilities to JavaScript. True shared-memory multithreading would allow JavaScript programs to utilize multiple CPU cores without the overhead of message passing, potentially boosting performance for compute‑heavy workloads. If successful, it could influence the broader JavaScript ecosystem and reduce reliance on workarounds like Web Workers or native addons. The PR modifies JavaScriptCore to expose a Thread constructor that accepts a function and runs it on a separate OS thread with full access to the shared JS heap, requiring careful synchronization to avoid data races. It is still under review and has not yet been merged into Bun’s main branch.

hackernews · gr4vityWall · Jun 20, 17:02 · [Discussion](https://news.ycombinator.com/item?id=48610841)

**Background**: Bun is a JavaScript runtime, package manager, and test runner that uses Apple’s JavaScriptCore engine instead of V8, aiming to be a fast drop‑in replacement for Node.js. JavaScriptCore is the JavaScript engine powering Safari and is also used by Bun for its runtime. Shared‑memory threading allows multiple threads to access the same memory space directly, unlike traditional Web Workers which communicate via message passing. Implementing such threads in JavaScriptCore would enable true parallelism within a single JavaScript environment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://byteiota.com/bun-new-thread-javascript-multithreading/">Bun’s new Thread () PR: JS Gets True Multithreading | byteiota</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the prospect of true multithreading in JavaScript, but many raised concerns about trust in the PR, particularly because it was generated with AI assistance and involves a large number of file changes. Others stressed the need for rigorous correctness and warned that AI‑generated code may not be reliable for complex concurrent programming.

**Tags**: `#JavaScript`, `#Bun`, `#multithreading`, `#JavaScriptCore`, `#WebKit`

---