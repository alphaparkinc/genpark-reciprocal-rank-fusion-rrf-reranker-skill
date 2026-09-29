# genpark-reciprocal-rank-fusion-rrf-reranker-skill

Agent Skill implementing **Reciprocal Rank Fusion (RRF)** rank aggregation for hybrid search pipelines in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Q["Search Query"] --> R1["Retriever 1 (BM25 Lexical)"]
    Q --> R2["Retriever 2 (Dense Vector)"]
    Q --> R3["Retriever 3 (Graph Knowledge)"]
    R1 --> L1["Ranked List 1"]
    R2 --> L2["Ranked List 2"]
    R3 --> L3["Ranked List 3"]
    L1 & L2 & L3 --> RRF["RRF Formula: Score(d) = Sum 1/(k + r(d))"]
    RRF --> Final["Consensus Ranked Output"]
```
