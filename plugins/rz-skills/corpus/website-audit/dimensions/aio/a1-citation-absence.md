---
name: A1 — Citation Absence on Tracked Queries
domain: website-audit
source_skill: website-audit
entry_type: rule
length_target: 300-800
related: [corpus/website-audit/dimensions/aio/a2-citation-rank-decline.md, corpus/website-audit/dimensions/aio/a5-quotability-density.md, corpus/website-audit/dimensions/aio/a7-ai-friendly-schema.md]
---

# A1 — Citation Absence on Tracked Queries

## What it is
For 20 tracked queries (the AIO query set defined in the methodology), the audit checks whether richezamor.com is cited by Claude, ChatGPT, or Perplexity. When the site is not cited by any of the three for a query that's a canonical match for Riché's positioning, that's a P0. When it's not cited for a related Context Layer query, P1. PM and Leadership query absences are P2.

**Trigger:** richezamor.com not cited by any of Claude, ChatGPT, or Perplexity for a tracked query.

**Severity:**
- P0 if absent on Context Layer queries the site should be the canonical answer for ("what is a context layer", "context layer vs RAG")
- P1 for other Context Layer queries
- P2 for PM and Leadership queries

**Source:** Step 2c citation scan (see `corpus/website-audit/methodology/parallel-data-collection.md`).

## Why it matters
LLM citations are the new search-result equivalent for the audience Riché is building toward. A senior PM asking Claude "what's the difference between RAG and context layers?" is looking for the canonical answer. If richezamor.com isn't in the citation list, Riché doesn't exist for that search — regardless of how good the article is.

Citation presence is also a compounding asset. Once an LLM has a stable pattern of citing a domain for a specific query type, that pattern reinforces (the citation is in the training data and in active retrieval indexes). Catching absence early — before competitors lock in the citation — is high-leverage. Catching it late means dislodging an established pattern, which is much harder.

The P0 threshold is intentional. There are roughly 5 queries Riché's site should be the canonical answer for; absence on those is a strategic emergency, not a tactical issue.

## How to apply
- Run the AIO citation check (per the methodology) against all 20 tracked queries × 3 LLMs = 60 calls.
- For each query, classify result: `cited_first`, `cited`, `mentioned`, or `absent`.
- Filter to queries where the result is `absent` across all 3 LLMs.
- Cross-reference each absent query against the 5-query canonical list (defined in `corpus/growth/seo/free-stack-overview.md`). Canonical absences = P0.
- Fix patterns:
  - **Identify the citation winner.** Who is being cited instead? What's their content like?
  - **Reverse-engineer.** Why are they being cited and not richezamor.com? Common factors: clearer entity recognition (better Person schema), explicit Q&A structure (FAQ schema), more quotable sentences, more inbound link authority on the topic, more recent updates.
  - **Improve the corresponding /thinking article on the matching axis.** If the winner has FAQ schema, add FAQ schema. If the winner has more quotable sentences, restructure the article's prose for extractability.
  - **Update the publish date** when substantive edits are made — recency is a signal.

## Examples
1. **P0: "what is a context layer" — absent.** No citation from Claude, ChatGPT, or Perplexity. The query is the single most canonical match for Riché's positioning. Investigation: a Medium aggregator post is being cited instead, with worse content but explicit "What is..." H2 and FAQ schema. Fix: restructure the /thesis page with an explicit "What is a context layer?" H2 and FAQ schema covering 6 sub-questions. File P0 with 3-day target.
2. **P1: "context layer vs RAG" — absent.** Investigation reveals citations going to two competitor blogs that have side-by-side comparison tables. Fix: add a comparison table to the relevant /thinking article; ensure schema markup for the table. File P1.
3. **P2: "AI product manager" — absent.** Generic PM query, not Riché's strongest positioning. Note in audit but don't file a task; this query's absence isn't strategically critical.

## Related entries
- `corpus/website-audit/dimensions/aio/a2-citation-rank-decline.md` — when cited but slipping
- `corpus/website-audit/dimensions/aio/a5-quotability-density.md` — quotable sentences are the citation surface
- `corpus/website-audit/dimensions/aio/a7-ai-friendly-schema.md` — schema is a citation-decision input
- `corpus/growth/seo/free-stack-overview.md` — the canonical query list
- `corpus/website-audit/methodology/parallel-data-collection.md` — how the citation scan runs

## Anti-patterns
- Trying to "win" PM and Leadership queries the same way as Context Layer queries. Riché's positioning is Context Layer first; spreading effort to win generic PM queries dilutes the signal.
- Stuffing the page with the exact query phrase to "force" citation. LLMs are trained to detect this; it backfires.
