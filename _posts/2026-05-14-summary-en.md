---
layout: default
title: "Horizon Summary: 2026-05-14 (EN)"
date: 2026-05-14
lang: en
---

> From 39 items, 5 important content pieces were selected

---

1. [Author Migrates Personal Repos from GitHub to Self-Hosted Forgejo](#item-1) ⭐️ 8.0/10
2. [: Author Moves Personal Digital Stack to European Cloud Providers](#item-2) ⭐️ 8.0/10
3. [: Deep Learning Framework Prices Convertible Bonds with Reset and Call Provisions](#item-3) ⭐️ 8.0/10
4. [:GeomHerd uses Ricci curvature to predict herding in LLM-simulated markets](#item-4) ⭐️ 8.0/10
5. [: Bayesian Dynamic Modeling of Realized Volatility in Financial Asset Price Forecasting](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Author Migrates Personal Repos from GitHub to Self-Hosted Forgejo](https://jorijn.com/en/blog/leaving-github-for-forgejo/) ⭐️ 8.0/10

The author describes moving their personal Git repositories from GitHub to a self-hosted Forgejo instance, outlining motivations such as decentralization and concerns about AI scrapers, and notes community reactions. The move reflects growing interest in decentralizing code hosting and highlights the relevance of federation efforts like ActivityPub for reducing reliance on centralized platforms. Forgejo is a lightweight, self-hosted Git forge that is actively implementing federation via the ForgeFed extension of ActivityPub, and the author mentions tools like GitSocial for preserving social graphs and mirrors.

hackernews · jorijn · May 13, 12:54 · [Discussion](https://news.ycombinator.com/item?id=48121266)

**Background**: GitHub is a widely used centralized platform for hosting Git repositories, offering issue tracking, pull requests, and CI/CD integration. Forgejo is a community-driven fork of Gitea, designed as a lightweight, self-hosted Git service that can be run on personal hardware or via Docker. Self-hosting allows individuals to control their data and avoid reliance on third-party services, while federation protocols like ActivityPub aim to enable interoperability between different code forges.

<details><summary>References</summary>
<ul>
<li><a href="https://forgejo.org/faq/">Forgejo FAQ | Forgejo – Beyond coding. We forge.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://antoniosarro.dev/blogs/forgejo-homelab">Self - Hosted Git with Forgejo : Your Own GitHub Alternative in Docker</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a desire to return to Git's decentralized roots, criticized the centralization of tooling around GitHub, and highlighted the importance of federation support in Forgejo. Several noted concerns about AI scrapers consuming self-hosted content and the need to block them, while others praised tools like GitSocial for preserving social graphs and encouraged donations to accelerate federation development.

**Tags**: `#GitHub`, `#Forgejo`, `#self-hosting`, `#decentralization`, `#federation`

---

<a id="item-2"></a>
## [: Author Moves Personal Digital Stack to European Cloud Providers](https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/) ⭐️ 8.0/10

The author migrated their personal digital infrastructure to European providers, outlining motivations, challenges, and the Terraform configuration they built for cross‑region high availability. The move highlights growing concerns over data sovereignty, EU regulations like GDPR and the CLOUD Act, and shows how developers can diversify infrastructure to reduce reliance on US‑based clouds. Using Terraform, the author set up cross‑provider, cross‑region high availability, mapping services such as Cloudflare to Bunny CDN and leveraging EU‑native hosts like OVHcloud and Hetzner for bare‑metal and managed services.

hackernews · monokai_nl · May 13, 11:42 · [Discussion](https://news.ycombinator.com/item?id=48120629)

**Background**: European data sovereignty efforts, reinforced by GDPR and rulings such as Schrems II, require personal and organizational data to be stored within the EU to avoid extraterritorial access under laws like the US CLOUD Act. Providers such as OVHcloud and Hetzner operate data centers exclusively in Europe and offer compliance certifications that make them attractive for sovereignty‑focused workloads. Terraform is commonly used to define cross‑region, multi‑provider architectures that meet high‑availability and disaster‑recovery requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hivenet.com/post/understanding-european-tech-sovereignty-challenges-and-opportunities">Understanding European Tech Sovereignty : Challenges and...</a></li>
<li><a href="https://gartsolutions.com/ovh-vs-hetzner/">OVH vs Hetzner: Which European CloudProvider Wins? - Gart</a></li>
<li><a href="https://foggykitchen.com/2025/09/20/oci-data-guard-terraform/">OCI Data Guard Terraform : Cross - Region Setup (2025 Guide)</a></li>

</ul>
</details>

**Discussion**: Commenters observed that EU government officials increasingly demand that services be hosted entirely within the EU, reflecting heightened data‑localization pressure. While many praised the move for diversification and improved privacy, others warned that Europe is not a perfect sanctuary, citing potential VPN restrictions and continued cooperation with the US, suggesting that geographic shifts may trade one set of risks for another.

**Tags**: `#data sovereignty`, `#cloud infrastructure`, `#EU regulations`, `#DevOps`, `#digital migration`

---

<a id="item-3"></a>
## [: Deep Learning Framework Prices Convertible Bonds with Reset and Call Provisions](https://arxiv.org/abs/2605.12189) ⭐️ 8.0/10

The paper introduces a deep learning-based framework that prices convertible bonds with downward conversion price reset and issuer call provisions under rolling-window trigger rules by formulating the valuation as a path-dependent PDE and approximating conditional expectations with neural networks. The method provides an efficient, flexible tool for pricing complex path-dependent convertible bonds, impacting quantitative finance and machine learning communities and improving pricing accuracy for widely used securities. The study derives consistent PPDE formulations for geometric Brownian motion, constant elasticity of variance, and Heston stochastic volatility dynamics; empirical tests on China CITIC Bank Convertible Bond show stable and accurate prices and sensitivities, and three economic insights reveal that contractual features dominate value, the call provision truncates upside gains, and the downward reset provision counterintuitively lowers the price by reducing the effective call threshold.

rss · arXiv Quantitative Finance · May 13, 04:00

**Background**: Convertible bonds are hybrid securities that can be converted into a predetermined number of the issuer's equity shares. Their valuation becomes challenging when they contain path‑dependent features such as downward conversion price reset and issuer call provisions that depend on the historical path of the underlying stock price. A path‑dependent partial differential equation (PPDE) captures this dependence by conditioning the bond value on the entire history of the underlying asset and the evolving conversion price. Rolling‑window trigger rules determine when these contractual features are activated based on recent price movements over a specified window.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12189">[2605.12189] A deep learning approach for pricing convertible bonds with path-dependent reset and call provisions</a></li>
<li><a href="https://www.investopedia.com/terms/c/convertiblebond.asp">investopedia.com/terms/c/convertiblebond.asp</a></li>
<li><a href="https://scispace.com/pdf/a-neural-rde-based-model-for-solving-path-dependent-pdes-2ef6q6tk.pdf">A Neural RDE-based model for solving path - dependent PDEs</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#convertible bonds`, `#pricing`, `#path‑dependent PDE`, `#financial engineering`

---

<a id="item-4"></a>
## [:GeomHerd uses Ricci curvature to predict herding in LLM-simulated markets](https://arxiv.org/abs/2605.11645) ⭐️ 8.0/10

The paper introduces GeomHerd, a forward-looking framework that computes discrete Ollivier--Ricci curvature on agent interaction graphs generated by an LLM-driven multi-agent simulator to quantify herding before it impacts market returns. Empirically, the detector fires a median of 272 steps before order-parameter onset and a contagion detector recalls 65% of critical trajectories 318 steps early. GeomHerd provides an early-warning signal for systemic risk, overcoming the lag of traditional price-correlation methods and offering a geometric alternative that can be integrated into risk monitoring systems. Its ability to anticipate herd behavior could help regulators and traders mitigate market fragility before losses materialize. The method tracks discrete Ollivier--Ricci curvature on action graphs, establishes a mean-field bridge to the classical CSAD herding statistic, and notes that the effective vocabulary of agent actions contracts during cascades. A curvature-conditioned forecasting head reduces cascade-window log-return MAE over detector-conditioned and price-only baselines.

rss · arXiv Quantitative Finance · May 13, 04:00

**Background**: Herding occurs when agents align their actions, amplifying market fragility; traditional metrics rely on price correlations that only detect coordination after it has affected returns. Ollivier--Ricci curvature measures how probability masses on a graph diverge or converge, providing a geometric proxy for local network topology. The Cividino--Sornette continuous-spin agent-based substrate serves as a testbed, modeling financial markets with noise-trader herding via an n-vector Ising model.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ricci_curvature">Ricci curvature - Wikipedia</a></li>
<li><a href="https://doi.org/10.2139/ssrn.3960979">Multi-asset financial bubbles in an agent-based model with noise traders’ herding described by an n-vector Ising model by Davide Cividino, Rebecca Westphal, Didier Sornette :: SSRN</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S000187081930369X">Ollivier Ricci curvature for general graph Laplacians: Heat ...</a></li>

</ul>
</details>

**Tags**: `#herding detection`, `#Ricci curvature`, `#agent-based simulation`, `#LLM multi-agent`, `#financial systemic risk`

---

<a id="item-5"></a>
## [: Bayesian Dynamic Modeling of Realized Volatility in Financial Asset Price Forecasting](https://arxiv.org/abs/2605.12099) ⭐️ 8.0/10

The paper introduces a new class of Bayesian dynamic models that combine a dynamic gamma process for realized volatility with traditional Bayesian dynamic linear models (DLMs) for asset price series, aiming to improve equity return forecasting using high‑frequency intraday data. By integrating volatility leverage and feedback effects through realized volatility proxies, the model offers methodological innovation and empirical validation on S&P sector ETFs, potentially enhancing quantitative finance forecasting and risk management practices. The model employs a conjugate-form dynamic gamma process for realized volatility paired with DLMs for prices, enabling simple sequential filtering, low computational overhead, and straightforward simulation‑based forecasting; empirical tests show improved forecast accuracy relative to standard models.

rss · arXiv Quantitative Finance · May 13, 04:00

**Background**: Bayesian dynamic linear models (DLMs) are state‑space models that use a modified Kalman filter with discounting to update linear Gaussian relationships over time for time‑series forecasting. A gamma process is a non‑decreasing Lévy process often used to model positive‑valued quantities such as realized volatility, capturing its jumps and continuous accumulation. Realized volatility, computed from high‑frequency intraday returns, serves as an observable proxy for latent volatility and exhibits a leverage effect where negative returns tend to increase volatility more than positive returns of equal magnitude. The leverage effect creates asymmetric volatility dynamics that are important for accurate forecasting and risk modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://pydlm.github.io/pydlm_user_guide.html">Dynamic linear models — user manual — PyDLM 0.1.1.13 documentation</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/full/10.1002/fut.22241">Forecasting realized volatility: The role of implied volatility, leverage effect, overnight returns, and volatility of realized volatility - Kambouroudis - 2021 - Journal of Futures Markets - Wiley Online Library</a></li>
<li><a href="https://arxiv.org/abs/2605.12099">[2605.12099] Bayesian Dynamic Modeling of Realized Volatility in Financial Asset Price Forecasting</a></li>

</ul>
</details>

**Tags**: `#Bayesian statistics`, `#financial econometrics`, `#realized volatility`, `#dynamic linear models`, `#time series forecasting`

---