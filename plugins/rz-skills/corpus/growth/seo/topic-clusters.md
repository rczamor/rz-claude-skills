---
name: Priority Context Layer Topic Clusters
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 400-700
related: [corpus/growth/seo/free-stack-overview.md, corpus/growth/seo/keyword-planner-monthly.md, corpus/growth/seo/serp-review-protocol.md, corpus/website-audit/dimensions/categories/keyword-research.md]
---

# Priority Context Layer Topic Clusters

## What it is
The 7 canonical topic areas where richezamor.com is building authority. Every keyword tracked under domain `Context Layer` belongs to exactly one of these clusters. Keyword Planner Discover sessions seed one cluster at a time. K4 (topic cluster gap) fires when any cluster has zero published /thinking articles tagged to it.

| # | Cluster | Example terms |
|---|---|---|
| 1 | Definition & Foundations | "what is a context layer", "context layer vs RAG", "context layer definition" |
| 2 | RAG vs Context Engineering | "context engineering", "naive RAG limitations", "context engineering patterns", "RAG vs context layer" |
| 3 | Agent Memory & Long-Term Context | "agent memory architecture", "long term memory LLM", "agent context retention" |
| 4 | Active Generation Pipeline | "active generation context", "ingest-time processing", "context curation pipeline" |
| 5 | Evaluation & Quality | "evaluating context retrieval", "RAG eval framework", "context quality metrics" |
| 6 | Architecture Decisions | "vector vs hybrid search", "pgvector vs qdrant", "context store architecture" |
| 7 | Production Patterns | "context layer in production", "context management system", "context layer deployment" |

## Why it matters
Without explicit clusters, keyword research drifts toward whatever Keyword Planner surfaces, which is biased toward high-volume generic terms ("AI product management," "machine learning"). The clusters keep the work pointed at Riché's actual authority territory: the Context Layer thesis, the Active Generation pipeline (the moat), and the production-grade architecture decisions that vendors handwave.

The clusters also enforce coverage discipline. K4 treats any zero-article cluster as P1 because the gap is strategic, not tactical. Authority compounds when every cluster has at least one canonical /thinking article that future pieces link back to. A cluster with zero articles is a hole in the moat.

The 7 clusters are intentionally locked. Adding an eighth dilutes focus; removing one abandons authority territory. Revisit the list quarterly during the rebaseline weeks (first Sunday of January, April, July, October), not week to week.

## How to apply

**Seeding Keyword Planner Discover:** Run one cluster per session. Pick 3–5 seed terms from that cluster only, capture candidates with monthly volume between 100 and 5000 and competition Low or Medium, add them to the Target Keywords DB tagged to the cluster.

**SERP review prioritization:** When sorting the DB by `domain_weight × volume` for the top 5, the Context Layer weight (2.5) means cluster-tagged terms naturally float to the top. The cluster tag itself is a tiebreaker when two terms have similar weighted volumes.

**K4 enforcement:** During the audit, query the Content Topics DB (`2c224f29490d44f99e7b58cb2e377086`) for published /thinking articles. Bucket each by cluster. Any cluster with zero articles fires K4 as P1.

**PM and Leadership domains:** PM and Leadership keywords do NOT use the cluster system. Those domains have their own loose taxonomies but K4 only applies to Context Layer. The 7 clusters are Context Layer only.

## Examples
1. **Cluster-balanced quarter.** Q2 2026 ends with all 7 clusters at ≥1 article: Definition (3), RAG vs Context Engineering (4), Agent Memory (2), Active Generation (1), Evaluation (1), Architecture (2), Production (2). K4 fires zero times across the 13 audits in the quarter. The moat is wide.
2. **Single-cluster gap.** Active Generation Pipeline cluster has zero published articles for 6 consecutive audits. K4 fires P1 every Sunday. Recovery: one Wednesday Deep Dive on the 5-step process (curate, synthesize, consolidate, prioritize, store) closes the gap. K4 clears.
3. **Out-of-cluster keyword.** Riché drafts a piece on "AI PM career path." It does not belong in Context Layer; it belongs in Domain = PM in the DB. The cluster system does not apply, but the piece still lands in the Content Topics DB tagged Domain = PM.

## Related entries
- `corpus/growth/seo/free-stack-overview.md`. How clusters fit into the broader methodology
- `corpus/growth/seo/keyword-planner-monthly.md`. Job 2 uses clusters as seed sources
- `corpus/growth/seo/serp-review-protocol.md`. Domain weight comes from cluster membership
- `corpus/website-audit/dimensions/categories/keyword-research.md`. K4 fire criteria and recovery patterns

## Anti-patterns
- Expanding to an eighth cluster without 12 weeks of consistent content in the existing 7. New clusters dilute the moat.
- Tagging PM-domain keywords to a Context Layer cluster to inflate the count. The DB has a Domain column; use it. The 7 clusters are Context Layer only.
- Treating clusters as topic categories on the website. They are research-and-coverage groupings, not site nav. The site IA reflects the audience, not the keyword taxonomy.
