---
layout: default
title: "Horizon Summary: 2026-10-11 (EN)"
date: 2026-10-11
lang: en
---

> From 16 items, 1 important content pieces were selected

---

1. [Why DuckDB 2.0 is faster](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Why DuckDB 2.0 is faster](https://motherduck.com/blog/why-duckdb-20-is-faster/) ⭐️ 8.0/10

DuckDB 2.0 introduces adaptive scanning, achieves up to 42× speedup for recursive CTEs, and releases a new C++ extension API, collectively boosting query execution speed. These advances make DuckDB more suitable for heavy analytical and graph workloads, while simplifying extension development for the community. Adaptive scanning changes the cost model to depend on the rows actually touched rather than scanning entire tables. Recursive CTE optimizations deliver up to 42× speedup, and the new C++ extension API enables faster development and distribution of native extensions.

hackernews · tosh · Oct 10, 18:08 · [Discussion](https://news.ycombinator.com/item?id=50035530)

**Background**: DuckDB is an in‑process analytical database known for its vectorized execution and SQL support. Recursive CTEs allow querying hierarchical or graph‑like data by repeatedly referencing a common table expression. The extension mechanism lets users add functionality such as new file formats or domain‑specific operators without modifying the core.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0</a></li>
<li><a href="https://github.com/duckdb/duckdb/discussions/14447">CTE optimization via WITH TAIL RECURSIVE · duckdb duckdb ...</a></li>
<li><a href="https://duckdb.org/docs/current/extensions/overview">Extensions – DuckDB</a></li>

</ul>
</details>

**Discussion**: Some commenters criticized the article's LLM‑like prose, while others highlighted the new graph extension and the speed benefits of the C++ extension API, and expressed interest in trying DuckDB in Jupyter notebooks or wished for a more task‑based parallelism design.

**Tags**: `#DuckDB`, `#database performance`, `#query optimization`, `#recursive CTE`, `#extension API`

---