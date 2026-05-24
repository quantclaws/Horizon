---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 8 items, 2 important content pieces were selected

---

1. [: 80386 microcode disassembled from die images](#item-1) ⭐️ 8.0/10
2. [Deep learning performance fundamentals explored from first principles](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [: 80386 microcode disassembled from die images](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

The author obtained a high‑resolution die image of the Intel 80386 microcode ROM and reverse‑engineered its contents, publishing the disassembled microcode and describing the extraction methodology. This work reveals the low‑level control logic of a historic 32‑bit CPU, enabling researchers and hobbyists to study, emulate, or modify early x86 architecture with unprecedented fidelity. The microcode was extracted by identifying transistor patterns in the die image, decoding the ROM bits, and translating them into a human‑readable assembly‑like listing; the analysis notes that the 80386 microcode acts as an orchestration layer atop hardwired execution units and PLAs.

hackernews · nand2mario · May 23, 12:11 · [Discussion](https://news.ycombinator.com/item?id=48247004)

**Background**: The Intel 80386, released in 1985, was the first 32‑bit x86 microprocessor and introduced features such as paging and protected mode; its microcode ROM stores the low‑level sequences that implement complex instructions, while much of the datapath is hardwired. Reverse‑engineering microcode from die images requires high‑resolution photography, transistor‑level recognition, and ROM bit extraction, a technique previously demonstrated on the 8086.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=48247004">80386 microcode disassembled | Hacker News</a></li>
<li><a href="https://cpumuseum.jimdofree.com/cpu-die-photography/80386/">80386 Die Photography - CPU MUSEUM - MUSEUM OF ... - Jimdo</a></li>

</ul>
</details>

**Discussion**: Commenters asked for clarification on the extraction process, noted the importance of knowing which 386 revision was examined, and pointed to related open‑source projects such as z386 that aim to rebuild the CPU from its original microcode.

**Tags**: `#80386`, `#microcode`, `#reverse engineering`, `#computer architecture`, `#retro computing`

---

<a id="item-2"></a>
## [Deep learning performance fundamentals explored from first principles](https://horace.io/brrr_intro.html) ⭐️ 8.0/10

The 2022 blog post by Horace provides an in‑depth, first‑principles analysis of why modern deep learning is so fast, covering hardware capabilities, software stacks, and key optimization techniques. Understanding these fundamentals helps researchers and engineers make informed decisions about hardware selection, model design, and performance optimization, highlighting NVIDIA’s sustained lead in AI acceleration. The post discusses GPU FLOP rates, memory bandwidth, interconnect scaling, Tensor Core mixed‑precision training, and algorithms like FlashAttention and ZeRO optimizer that reduce memory traffic and improve throughput.

hackernews · tosh · May 23, 11:50 · [Discussion](https://news.ycombinator.com/item?id=48246889)

**Background**: Modern deep learning performance is limited by how quickly data can be moved between GPU high‑bandwidth memory (HBM) and on‑chip compute units, motivating algorithms that minimize memory traffic. Techniques such as FlashAttention use tiling to perform exact attention with fewer HBM reads/writes, while ZeRO optimizer partitions optimizer states across GPUs to cut memory redundancy. NVIDIA’s Tensor Cores accelerate mixed‑precision FP16 matrix multiplications, delivering up to 3× speedup when combined with software support from frameworks like PyTorch and TensorFlow.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/flashattention">Designing Hardware-Aware Algorithms : FlashAttention | DigitalOcean</a></li>
<li><a href="https://www.deepspeed.ai/tutorials/zero/">Zero Redundancy Optimizer - DeepSpeed</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html">Train With Mixed Precision - NVIDIA Docs</a></li>

</ul>
</details>

**Discussion**: Commenters praised the post as a classic deep‑dive and highlighted NVIDIA’s continued exponential growth in FLOPs, bandwidth and interconnect. Several noted the lack of portable performance advice, pointing out that the same model can behave differently across runtimes (ONNX, TensorRT) and hardware configurations. Others asked about low‑level details such as why fused operations like x.cos().cos() can be faster than separate calls.

**Tags**: `#deep learning`, `#performance optimization`, `#hardware acceleration`, `#ML systems`, `#neural networks`

---