---
layout: default
title: "Horizon Summary: 2026-09-24 (EN)"
date: 2026-09-24
lang: en
---

> From 41 items, 9 important content pieces were selected

---

1. [Qualcomm upstreaming Linux drivers for Snapdragon X2 Series](#item-1) ⭐️ 8.0/10
2. [Claude discovers a novel enzyme system with CRISPR-like repeats.](#item-2) ⭐️ 8.0/10
3. [Google releases Gemini 3.8 text-to-speech with voice cloning and watermarking](#item-3) ⭐️ 8.0/10
4. [Examining 'I don't want the details' in workplace communication](#item-4) ⭐️ 8.0/10
5. [Gemini 3.8 TTS Playground launches with 2,000+ voices and custom voice creation.](#item-5) ⭐️ 8.0/10
6. [Ethereum MEV Transaction Reordering Costs Users $7.2M Monthly](#item-6) ⭐️ 8.0/10
7. [The Virtue of Sparsity in Complexity.](#item-7) ⭐️ 8.0/10
8. [Machine Learning Measures of High-Frequency Trading Liquidity Supply and Demand](#item-8) ⭐️ 8.0/10
9. [Polynomial Scaling Achieved for Neural Operator Approximations of Structured BSDEs](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qualcomm upstreaming Linux drivers for Snapdragon X2 Series](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) ⭐️ 8.0/10

Qualcomm announced it is upstreaming core Linux drivers for the Snapdragon X2 Series, including the Hexagon NPU and Adreno GPU, to enable better GPU, NPU, and hardware support for Linux on these ARM laptops. This step strengthens Linux compatibility on ARM laptops, making Qualcomm a more credible rival to Apple’s M‑series chips and traditional x86 vendors, and could spur broader adoption of Linux on Snapdragon‑based devices. Qualcomm targets Debian support by the end of 2026 and Ubuntu certification by 2027, focusing on GPU and NPU drivers while noting that readiness depends on OEM design and specific X2 variant.

hackernews · aaronday · Sep 23, 22:38 · [Discussion](https://news.ycombinator.com/item?id=49823582)

**Background**: The Snapdragon X2 series is Qualcomm’s latest ARM‑based laptop platform, featuring an integrated Hexagon NPU for AI workloads and an Adreno GPU for graphics. Historically, Linux support on Qualcomm’s mobile‑focused SoCs has been limited to downstream or proprietary drivers, leaving gaps in GPU and NPU functionality. By upstreaming these drivers into the mainline Linux kernel, Qualcomm enables community developers to build on open‑source support and improves long‑term maintainability. This aligns with a broader industry trend of hardware vendors contributing core components to Linux to improve openness and performance on ARM devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/news/999664/qualcomm-snapdragon-x2-linux-support-arm">Qualcomm will finally support Linux on Snapdragon X2 chips. | The Verge</a></li>
<li><a href="https://xenospectrum.com/en/snapdragon-x2-linux-preview-ubuntu/">Snapdragon X2 Laptops Get Linux Roadmap: Debian This Year, Ubuntu Certification by 2027 | XenoSpectrum</a></li>
<li><a href="https://www.xda-developers.com/qualcomm-is-helping-linux-run-better-on-snapdragon-x2-laptops-with-an-early-developer-preview/">Qualcomm is helping Linux run better on Snapdragon X2 laptops with an Early Developer Preview</a></li>

</ul>
</details>

**Discussion**: Commenters praised the performance potential, noting it rivals Apple’s M‑series and exceeds current Intel/AMD offerings, and welcomed the open‑source approach as opposed to semi‑proprietary ChromeOS support. Some expressed concerns about OEM variability, lack of desktop or other form‑factor coverage, and the need for motherboard upgradability, while others highlighted related OpenBSD progress and KVM/EL2 support indicating virtualization capabilities.

**Tags**: `#Linux`, `#ARM`, `#Qualcomm`, `#Snapdragon X2`, `#open-source drivers`

---

<a id="item-2"></a>
## [Claude discovers a novel enzyme system with CRISPR-like repeats.](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic's AI assistant Claude autonomously analyzed genomic data and identified a previously unknown enzyme system that is flanked by a long array of DNA repeats resembling a CRISPR array, located near a reverse transcriptase gene in bacteriophage genomes. The discovery showcases how large language models can accelerate bioinformatics research by revealing novel enzymatic functions that could be harnessed for genome editing or synthetic biology applications. The enzyme system was found adjacent to a tandem repeat array that shares structural features with CRISPR repeats, but the associated enzyme appears to be a reverse transcriptase‑related nuclease rather than a Cas protein; the finding remains computational and awaits experimental validation.

hackernews · raahelb · Sep 23, 18:06 · [Discussion](https://news.ycombinator.com/item?id=49820134)

**Background**: CRISPR systems consist of a Cas nuclease guided by RNA that recognizes short repeat sequences interspersed with spacer DNA derived from foreign genomes. Reverse transcriptases are enzymes that synthesize DNA from an RNA template and are often found in mobile genetic elements such as retrons and bacteriophages. Anthropic’s Claude was trained on scientific literature and tasked to autonomously explore genomic datasets, enabling it to detect patterns like repeat arrays that may be overlooked by conventional methods.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system \ Anthropic</a></li>
<li><a href="https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats">Anthropic says Claude found a new enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about AI uncovering novel biological patterns and appreciated the ability to view Claude’s internal reasoning transcripts, while others questioned how a language model can reason about biochemical structures and warned that the discovery is currently just a computational prediction. Some noted that therapeutic applications would still be limited by delivery challenges, and a few urged Anthropic to clarify its stance on AI‑driven bioengineering.

**Tags**: `#AI`, `#bioinformatics`, `#CRISPR`, `#enzyme discovery`, `#genomics`

---

<a id="item-3"></a>
## [Google releases Gemini 3.8 text-to-speech with voice cloning and watermarking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

Google unveiled the Gemini 3.8 text-to-speech model that can clone a voice from a 30‑second audio sample, includes SynthID watermarking and C2PA credentials, and is available across Google AI Studio, Gemini API, Gemini Enterprise, Gemini Notebook and Google Vids. The release pushes realistic synthetic voice technology forward while adding built‑in consent verification and tamper‑evident watermarks, which could broaden use in content creation, accessibility and media provenance, but also highlights ongoing fragmentation in Google’s AI product rollout. Built on Gemini 3 Pro, the model accepts up to 8 K tokens of text and returns up to 64 K tokens of audio; voice cloning requires a verified consent check, and the audio output carries SynthID watermarks and C2PA metadata for provenance tracking.

hackernews · swolpers · Sep 23, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49817615)

**Background**: Text‑to‑speech (TTS) systems convert written text into spoken audio, and recent advances enable voice cloning—replicating a person’s voice from short samples. Watermarking techniques such as SynthID embed imperceptible signals to identify synthetic audio, while C2PA provides a standard for attaching provenance metadata to media files. Google’s Gemini family includes a series of multimodal models, with the 3.8 series focusing on audio capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 text-to-speech says hello</a></li>
<li><a href="https://www.unite.ai/google-rolls-out-gemini-3-8-speech-models-in-api-and-ai-studio/">Google Rolls Out Gemini 3.8 Speech Models In API And AI Studio – Unite.AI</a></li>

</ul>
</details>

**Discussion**: Commenters praised the voice‑cloning fidelity and local‑hosted use cases, but repeatedly criticized Google for inconsistent availability and differing capabilities across its consumer, prosumer and cloud platforms, noting that features like video output may be missing in certain environments.

**Tags**: `#Gemini`, `#text-to-speech`, `#AI`, `#voice cloning`, `#Google`

---

<a id="item-4"></a>
## [Examining 'I don't want the details' in workplace communication](https://michaelheap.com/i-dont-want-the-details/) ⭐️ 8.0/10

The article explores the phrase 'I don't want the details' used by leaders, analyzing what it signals about trust, competence, and the balance between oversight and autonomy in engineering teams. Understanding this phrase helps leaders recognize how communication styles affect team trust and accountability, offering insights for improving engineering management practices. The discussion highlights contrasting views: some see the phrase as a sign of trust and empowerment, while others warn it can abdicate responsibility and hinder root‑cause analysis.

hackernews · mooreds · Sep 23, 13:04 · [Discussion](https://news.ycombinator.com/item?id=49815466)

**Background**: In software engineering leadership, phrases like 'I don't want the details' often arise when managers delegate authority, reflecting a tension between trusting teams to execute and maintaining oversight for risk management. This dynamic influences decision‑making, incident response, and organizational learning.

**Discussion**: Commenters debated whether the phrase signals genuine trust or a lack of accountability, with some praising its empowerment tone and others arguing it avoids necessary oversight and root‑cause investigation. The conversation also touched on how last‑minute changes and systemic fixes should be addressed rather than blamed on individuals.

**Tags**: `#communication`, `#management`, `#software engineering`, `#leadership`, `#trust`

---

<a id="item-5"></a>
## [Gemini 3.8 TTS Playground launches with 2,000+ voices and custom voice creation.](https://simonwillison.net/2026/Sep/23/gemini-tts-playground/) ⭐️ 8.0/10

Google announced the Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS models, which offer a library of over 2,000 voices and allow users to create a custom voice from just a 30‑second audio sample. Simon Willison also released an interactive playground that lets developers experiment with these models using their own API key. These models lower the barrier for creating expressive, multi‑speaker text‑to‑speech applications, enabling developers to produce realistic character dialogues and custom voices without extensive training data. The release reflects a broader trend toward highly controllable, low‑cost AI voice synthesis in creative and enterprise workflows. The two models are named gemini-3.8-flash-tts and gemini-3.8-flash-lite-tts; the playground shows a direct API connection, keeps the user’s API key in memory only, and demonstrates generating 1 minute 18 seconds of audio for about 2.74 cents using the Flash model. It also supports assigning distinct voices and delivery styles to each speaker in a conversation.

rss · Simon Willison · Sep 23, 17:12

**Background**: Text‑to‑speech (TTS) systems convert written text into spoken audio, and recent advances allow voice cloning from short audio samples. Google’s Gemini family includes multimodal models; the 3.8 Flash variants are optimized for speed and cost while retaining high expressiveness. An open CORS policy on the Gemini API lets web apps make direct cross‑origin requests, enabling Simon Willison’s playground to send API keys securely without storing them.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS - The Keyword</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://toolchase.com/blog/ai-voice-cloning/">AI Voice Cloning in 2026 | ToolChase</a></li>

</ul>
</details>

**Tags**: `#text-to-speech`, `#Gemini`, `#AI models`, `#voice synthesis`, `#developer tools`

---

<a id="item-6"></a>
## [Ethereum MEV Transaction Reordering Costs Users $7.2M Monthly](https://arxiv.org/abs/2508.04003) ⭐️ 8.0/10

The paper finds that two MEV builders now produce nearly 80% of Ethereum blocks, and users would need to pay about $7.2 million per month to ensure their transactions stay in the first quartile of a block. Sandwich attacks occur in more than one out of every two blocks, and the gas fees paid on those attacks cover roughly 9.6% of the MEV extracted by validators. These results quantify the economic burden of MEV on everyday Ethereum users and highlight the concentration of block‑building power, informing both protocol designers and users about where reforms could reduce harmful transaction ordering. The findings support proposals such as gas‑fee priority mechanisms or private transaction pools to mitigate MEV extraction. The study notes that sandwich attacks front‑run and back‑run a transaction, with gas fees on those attacks representing about 9.6% of total MEV payments to validators. It also references the proposer‑builder separation (PBS) roadmap as a potential structural remedy for the observed builder dominance.

rss · arXiv Quantitative Finance · Sep 23, 04:00

**Background**: Maximal Extractable Value (MEV) is the extra profit validators can obtain by reordering, including, or excluding transactions beyond the standard block reward and gas fees. A sandwich attack is a specific MEV strategy where an attacker places a transaction before and after a victim’s trade to profit from price movement. On Ethereum, block builders assemble transactions into blocks and can reorder them to maximize MEV, with the proposer‑builder separation (PBS) upgrade aiming to split block construction from block proposal to reduce such power concentration.

<details><summary>References</summary>
<ul>
<li><a href="https://ethereum.org/developers/docs/mev/">Maximal extractable value (MEV) | ethereum.org</a></li>
<li><a href="https://www.gate.com/learn/articles/what-is-a-sandwich-attack/936">What Is a Sandwich Attack? Definition & How It Works | Gate Learn</a></li>
<li><a href="https://financefeeds.com/how-block-builders-select-transactions/">How Block Builders Order Ethereum Transactions</a></li>

</ul>
</details>

**Tags**: `#Ethereum`, `#MEV`, `#blockchain`, `#transaction ordering`, `#sandwich attacks`

---

<a id="item-7"></a>
## [The Virtue of Sparsity in Complexity.](https://arxiv.org/abs/2604.17166) ⭐️ 8.0/10

The authors show that expanding the candidate factor space while enforcing factor sparsity via basis pursuit yields sparse portfolios with superior out‑of‑sample Sharpe ratios and lower pricing errors than dense ridgeless benchmarks at massive scale. By distinguishing capacity sparsity from factor sparsity, the paper reconciles the apparent tension between model richness and parsimony, showing that enlarging the candidate set and imposing sparsity can be complementary, which impacts both financial modeling and high‑dimensional machine learning. The approach uses basis pursuit optimization combined with nonlinear feature expansions, scales to 432 million candidate factors via column generation and GPU acceleration, and demonstrates that sparse portfolios achieve higher Sharpe ratios and lower pricing errors than dense ridgeless benchmarks at the largest scale.

rss · arXiv Quantitative Finance · Sep 23, 04:00

**Background**: High‑dimensional asset pricing deals with many potential risk factors, where sparsity seeks a parsimonious representation. Basis pursuit is an ℓ₁‑minimization problem that finds the sparsest solution to an underdetermined linear system. Column generation is an iterative algorithm for solving large linear programs by considering only a subset of variables at a time, and GPU acceleration speeds up the computation of pricing kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Basis_pursuit">Basis pursuit - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Column_generation">Column generation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#asset pricing`, `#sparsity`, `#machine learning`, `#high-dimensional statistics`, `#basis pursuit`

---

<a id="item-8"></a>
## [Machine Learning Measures of High-Frequency Trading Liquidity Supply and Demand](https://arxiv.org/abs/2608.00858) ⭐️ 8.0/10

The authors trained machine learning models on proprietary Nasdaq data to create daily measures of liquidity‑supplying and liquidity‑demanding high‑frequency trading for all U.S. stocks from 2010 to 2023, showing the measures outperform standard proxies and generalize to Euronext Paris. The new measures provide researchers with a reliable, high‑frequency‑specific tool to study liquidity dynamics and market quality over a 14‑year panel, improving upon widely used proxies and enabling cross‑market comparisons. The approach uses an ensemble ML model trained on Nasdaq’s proprietary HFT labels to map to public intraday variables, producing daily series that subsume standard proxies and remain predictive years after training; during COVID‑19, liquidity‑supplying HFT was associated with stronger spread‑narrowing.

rss · arXiv Quantitative Finance · Sep 23, 04:00

**Background**: High‑frequency trading (HFT) refers to the use of powerful algorithms to execute a large volume of orders in milliseconds or microseconds, often acting as either liquidity suppliers (providing bid‑ask quotes) or liquidity demanders (taking existing quotes). Public data typically do not label which trades are HFT, and common proxies such as trade volume or turnover cannot distinguish between liquidity‑supplying and liquidity‑demanding strategies. To overcome this, the authors trained machine learning models on a proprietary Nasdaq dataset that identifies HFT activity, mapping it to observable intraday variables so that daily measures can be constructed for all U.S. stocks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High-frequency_trading">High-frequency trading - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/h/high-frequency-trading.asp">Understanding High-Frequency Trading (HFT): Basics, Mechanics ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.00858">Data -Driven Measures of High-Frequency Trading</a></li>

</ul>
</details>

**Tags**: `#high-frequency trading`, `#machine learning`, `#market microstructure`, `#liquidity measurement`, `#financial econometrics`

---

<a id="item-9"></a>
## [Polynomial Scaling Achieved for Neural Operator Approximations of Structured BSDEs](https://arxiv.org/abs/2410.14788) ⭐️ 8.0/10

The paper demonstrates that neural operator architectures can achieve polynomial approximation rates for specific families of non‑Markovian backward stochastic differential equations (BSDEs) by exploiting additional problem structure, namely factoring out the singular part of the associated semilinear elliptic PDE Green’s function and incorporating the Doléans‑Dade exponential of the BSDE’s common non‑Markovian factor into the network’s decoding layers. This result establishes the first polynomial‑scaling regime for neural operator approximations of structured BSDE solution operators, breaking the exponential lower bounds that hold for generic operator classes and thereby advancing the theoretical foundations of operator learning in stochastic analysis and its applications to high‑dimensional PDEs. The authors consider BSDE families with Sobolev‑regular terminal conditions and Sobolev‑regular additive nonlinear perturbations of the generator; they tailor a neural operator by removing the singular Green’s function component and embedding the Doléans‑Dade exponential into the decoder, proving that the number of trainable parameters needed for uniform ε‑accurate approximation grows polynomially in 1/ε.

rss · arXiv Quantitative Finance · Sep 23, 04:00

**Background**: Neural operators are deep learning models designed to learn mappings between infinite‑dimensional function spaces, extending traditional neural networks to operator learning. Backward stochastic differential equations (BSDEs) are a class of stochastic equations where the solution is determined by a terminal condition; non‑Markovian BSDEs involve dependencies on the whole past path, making them harder to approximate. For generic operator classes defined only by regularity, information‑theoretic arguments imply that the optimal approximation error decays only exponentially in the reciprocal accuracy 1/ε, motivating the search for additional structural assumptions that enable polynomial scaling.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2410.14788">Polynomial Scaling is Possible For Neural Operator Approximations of...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_operators">Neural operators - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Backward_stochastic_differential_equation">Backward stochastic differential equation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#neural operators`, `#BSDEs`, `#polynomial scaling`, `#stochastic analysis`, `#machine learning theory`

---