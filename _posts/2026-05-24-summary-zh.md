---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 8 items, 2 important content pieces were selected

---

1. [80386 微码从芯片镜像被反汇编](#item-1) ⭐️ 8.0/10
2. [从第一原理探索深度学习性能基础](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [80386 微码从芯片镜像被反汇编](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

作者获得了英特尔 80386 微码 ROM 的高分辨率芯片镜像，并对其进行了反汇编，公开了微码内容并描述了提取方法。 这项工作揭示了历史悠久的 32 位 CPU 的底层控制逻辑，使研究者和爱好者能够以前所未有的保真度研究、仿真或修改早期 x86 架构。 通过在芯片镜像中识别晶体管模式、解码 ROM 位并将其转换为可读的类汇编列表来提取微码；分析指出，80386 微码充当硬连线执行单元和可编程逻辑阵列之上的编排层。

hackernews · nand2mario · May 23, 12:11 · [社区讨论](https://news.ycombinator.com/item?id=48247004)

**背景**: 英特尔 80386 于 1985 年发布，是首款 32 位 x86 微处理器，引入了分页和保护模式等特性；其微码 ROM 存储实现复杂指令的底层序列，而数据通路的大部分是硬连线的。从芯片镜像逆向工程微码需要高分辨率摄影、晶体管层面的识别以及 ROM 位提取，这一技术之前已在 8086 上得到演示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=48247004">80386 microcode disassembled | Hacker News</a></li>
<li><a href="https://cpumuseum.jimdofree.com/cpu-die-photography/80386/">80386 Die Photography - CPU MUSEUM - MUSEUM OF ... - Jimdo</a></li>

</ul>
</details>

**社区讨论**: 评论者询问了提取过程的细节，强调了要知道所检查的 386 版本修订的重要性，并指向了如 z386 之类的旨在从原始微码重建 CPU 的开源项目。

**标签**: `#80386`, `#microcode`, `#reverse engineering`, `#computer architecture`, `#retro computing`

---

<a id="item-2"></a>
## [从第一原理探索深度学习性能基础](https://horace.io/brrr_intro.html) ⭐️ 8.0/10

Horace 于 2022 年的博客文章从第一原理深入分析了现代深度学习为何如此快速，涵盖了硬件能力、软件栈以及关键优化技术。 理解这些基础有助于研究人员和工程师在硬件选择、模型设计和性能优化方面做出明智决策，凸显了英伟达在 AI 加速领域的持续领先。 文章讨论了 GPU 的 FLOP 速率、内存带宽、互连扩展、Tensor Core 混合精度训练，以及 FlashAttention 和 ZeRO 优化器等降低内存流量、提高吞吐量的算法。

hackernews · tosh · May 23, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48246889)

**背景**: 现代深度学习性能受限于 GPU 高带宽内存（HBM）与片上计算单元之间数据移动的速度，因而需要能够最小化内存流量的算法。FlashAttention 通过分块（tiling）实现精确注意力计算，同时减少 HBM 读写次数；ZeRO 优化器则在多个 GPU 之间划分优化器状态以降低内存冗余。英伟达的 Tensor Core 能够加速混合精度 FP16 矩阵乘法，在配合 PyTorch、TensorFlow 等框架时可实现最高 3× 的加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/flashattention">Designing Hardware-Aware Algorithms : FlashAttention | DigitalOcean</a></li>
<li><a href="https://www.deepspeed.ai/tutorials/zero/">Zero Redundancy Optimizer - DeepSpeed</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html">Train With Mixed Precision - NVIDIA Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这篇文章是经典的深度剖析，并指出英伟达在 FLOPs、带宽和互连方面保持指数级增长。多位评论者指出缺乏可移植的性能建议，强调相同模型在不同运行时（ONNX、TensorRT）和硬件配置下表现可能不同。还有人询问诸如 x.cos().cos() 融合操作为何能比分开调用更快的底层细节。

**标签**: `#deep learning`, `#performance optimization`, `#hardware acceleration`, `#ML systems`, `#neural networks`

---