---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
---

> From 12 items, 4 important content pieces were selected

---

1. [Andrej Karpathy's Pelican Drawing Sparks AI Benchmark Debate](#item-1) ⭐️ 8.0/10
2. [Kakehashi: Experimental Userspace Layer to Run macOS Binaries on Linux ARM](#item-2) ⭐️ 8.0/10
3. [How Essential Vocabulary for English Learners Shifted from 1953 to 2023](#item-3) ⭐️ 8.0/10
4. [eBay harassment campaign leads to $56M settlement and criminal convictions](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Andrej Karpathy's Pelican Drawing Sparks AI Benchmark Debate](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

Andrej Karpathy tweeted a prompt to draw a pelican, which ignited a Hacker News discussion about using such drawing tasks to benchmark multimodal AI models' grasp of physics and spatial reasoning. The debate highlights growing interest in simple, qualitative benchmarks that reveal how well AI models understand real‑world physics and spatial relationships, guiding future evaluation methods. Commenters referenced Simon Willison’s 'pelican on a bicycle' SVG benchmark, noted that current models produce similar pelican drawings making the test less discriminative, and stressed the need for reproducible prompts and qualitative/subjective scoring.

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: Multimodal models are increasingly evaluated with tasks that require generating or interpreting visual outputs, such as drawing animals in SVG, to test their understanding of anatomy, physics, and spatial layout. Recent benchmarks like PhysUniBench assess undergraduate‑level physics reasoning using text‑diagram pairs, while SpatiaLab focuses on spatial reasoning in vision‑language models. The pelican drawing task sits at the intersection of these efforts, serving as a lightweight probe of a model’s ability to convey coherent, physically plausible imagery.

<details><summary>References</summary>
<ul>
<li><a href="https://gigazine.net/gsc_news/en/20250609-llms-pelicans-on-bicycles/">Here's what happens when you run the AI benchmark ' Draw ...</a></li>
<li><a href="https://arxiv.org/abs/2506.17667">[2506.17667] PhysUniBench: A Multi-Modal Physics Reasoning ... PhysUniBench: Multimodal Benchmark for Physics Reasoning PhysUniBench: A Multi-Modal Physics Reasoning Benchmark at ... Images PHYSUNIBENCH: A MULTI-MODALPHYSICSREA SONINGBENCHMARK ... GitHub - PrismaX-Team/PhysUniBenchmark PhysUniBench: An Undergraduate-Level Physics Reasoning ... PhysUniBench: An Undergraduate-Level Physics Reasoning ...</a></li>
<li><a href="https://arxiv.org/abs/2602.03916v1">SpatiaLab: Can Vision-Language Models Perform Spatial Reasoning in the ...</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that the pelican task exposes model understanding of the physical world, but note issues with prompt reproducibility and the subjective nature of scoring; some liken it to earlier unicorn‑in‑TikZ benchmarks and call for qualitative measurement to track progress.

**Tags**: `#AI`, `#multimodal models`, `#benchmarking`, `#Andrej Karpathy`, `#pelican`

---

<a id="item-2"></a>
## [Kakehashi: Experimental Userspace Layer to Run macOS Binaries on Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Show HN post introduces Kakehashi, an experimental userspace compatibility layer that aims to run macOS CLI binaries on Linux ARM64, with working prototypes for tools such as 7‑Zip and curl. If successful, Kakehashi could let Linux ARM users run macOS command‑line utilities without virtualization or dual‑boot, broadening software availability on devices like Raspberry Pi and Linux‑on‑Mac hardware. The project translates Darwin system calls to Linux in userspace, loads Mach‑O executables, provides a freestanding libSystem, and currently shows 7‑Zip running ~5.2× slower than native Linux while curl passes over 200 command‑line tests.

hackernews · vlad_kalinkin · Aug 2, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49145937)

**Background**: A compatibility layer translates system calls from one operating system to another, allowing foreign binaries to run on a host OS without full emulation. macOS executables use the Mach‑O format, which differs from Linux’s ELF, requiring a layer that can parse Mach‑O and map its libraries. Running macOS binaries on Linux ARM adds the complexity of translating both the executable format and the underlying system call interface across different CPU architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Compatibility_layer">Compatibility layer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mach-O">Mach-O - Wikipedia</a></li>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the project’s potential, compared it to the Darling project and wondered about collaboration, while some criticized the project’s name. Others noted the early stage of the work, asked about future plans, and debated whether a virtualization‑free approach could simplify the task.

**Tags**: `#macOS`, `#Linux`, `#ARM`, `#compatibility layer`, `#userspace`

---

<a id="item-3"></a>
## [How Essential Vocabulary for English Learners Shifted from 1953 to 2023](https://pudding.cool/2026/07/essential-words/) ⭐️ 8.0/10

The Pudding article analyzes how the core vocabulary taught to English language learners has evolved, comparing the 1953 General Service List with a 2023 update and highlighting which words were dropped and added. This shift reveals broader sociolinguistic trends, helping educators and curriculum designers align teaching materials with contemporary cultural priorities such as identity, gender, and global communication. Nearly a quarter of the 1953 words disappeared, while 39% of the 2023 list are new; examples include humility, loyalty, and fellowship being replaced by community, identity, organization, ethnic, gender, and narrative, with the Social‑Communicative category staying roughly the same size.

hackernews · c-oreills · Aug 2, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49145590)

**Background**: The General Service List (GSL), first published by Michael West in 1953, contains about 2,000 high‑frequency words deemed essential for everyday English. Updated versions such as the New General Service List and related resources like the Academic Word List and Oxford 3000 provide reference points for vocabulary selection in language teaching and learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_Service_List">General Service List - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/New_General_Service_List">New General Service List - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Academic_Word_List">Academic Word List</a></li>

</ul>
</details>

**Discussion**: Commenters noted that useful vocabulary depends on the learner’s goal—travel, media, or academics—and highlighted the lack of a single “right” list. Some linked the shift from words like humility and loyalty to identity‑focused terms to growing social inequality, while others expressed frustration with presentation issues or the difficulty of creating unbiased frequency‑based lists for other languages.

**Tags**: `#language learning`, `#linguistics`, `#education`, `#vocabulary`, `#sociolinguistics`

---

<a id="item-4"></a>
## [eBay harassment campaign leads to $56M settlement and criminal convictions](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 8.0/10

eBay’s former security team members conducted a coordinated harassment campaign against a critic couple, leading to guilty pleas, prison sentences, and a $56 million settlement with the victims. The case underscores how internal security teams can be misused for intimidation, raising concerns about corporate oversight and the need for stronger accountability mechanisms in large tech firms. Seven eBay security employees, including former police captains, were charged in the harassment campaign; Brian Gilbert was sentenced to time served and a $20,000 fine, Jim Baugh received 57 months in prison, and David Harville was given a prison term (length not disclosed in the excerpt). The victims ultimately settled with eBay for $56 million.

hackernews · JumpCrisscross · Aug 2, 19:19 · [Discussion](https://news.ycombinator.com/item?id=49147435)

**Background**: eBay’s Global Security Team is responsible for protecting the company’s assets and investigating threats, but in this case members allegedly used their authority to intimidate critics. Harassment campaigns by corporate security personnel are rare but can involve surveillance, doxxing, and legal threats. The case drew attention after victims reported the abuse to law enforcement, leading to a federal investigation. Such incidents highlight risks when security functions lack proper oversight and accountability.

**Discussion**: Commenters noted the detailed sentences handed to eBay security staff and expressed doubt that the harassment was limited to the Steiner couple, calling for investigations into other potential targets. Some discussed broader implications, such as the need to monitor former law‑enforcement officers in corporate security roles, while others veered into unrelated topics like eBay’s fee structure or general observations about unsupervised bad behavior.

**Tags**: `#eBay`, `#corporate misconduct`, `#harassment`, `#legal settlement`, `#tech ethics`

---