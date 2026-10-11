---
layout: default
title: "Horizon Summary: 2026-10-11 (ZH)"
date: 2026-10-11
lang: zh
---

> From 16 items, 1 important content pieces were selected

---

1. [DuckDB 2.0 为何更快](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DuckDB 2.0 为何更快](https://motherduck.com/blog/why-duckdb-20-is-faster/) ⭐️ 8.0/10

DuckDB 2.0 引入自适应扫描，使递归 CTE 的性能提升最高可达 42 倍，并发布了新的 C++ 扩展 API，共同提升查询执行速度。 这些进步使 DuckDB 更适合处理大规模分析和图形工作负载，同时简化了社区的扩展开发。 自适应扫描将代价模型从全表扫描转为仅依赖实际读取的行数。递归 CTE 优化带来最高 42 倍的加速，而新的 C++ 扩展 API 使原生扩展的开发与分发更加高效。

hackernews · tosh · Oct 10, 18:08 · [社区讨论](https://news.ycombinator.com/item?id=50035530)

**背景**: DuckDB 是一种内置的分析型数据库，以向量化执行和完整的 SQL 支持著称。递归 CTE 使得可以通过反复引用公共表表达式来查询层次或图形数据。其扩展机制允许用户添加新文件格式或领域特定算子，而无需修改内核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0</a></li>
<li><a href="https://github.com/duckdb/duckdb/discussions/14447">CTE optimization via WITH TAIL RECURSIVE · duckdb duckdb ...</a></li>
<li><a href="https://duckdb.org/docs/current/extensions/overview">Extensions – DuckDB</a></li>

</ul>
</details>

**社区讨论**: 有评论者认为文章文风像是 LLM 生成的，难以阅读；也有评论者指出新的图扩展和 C++ 扩展 API 带来的性能提升，并表示计划在 Jupyter Notebook 中尝试 DuckDB，或希望看到更多基于任务的并行设计。

**标签**: `#DuckDB`, `#database performance`, `#query optimization`, `#recursive CTE`, `#extension API`

---