---
name: P3 — Thesis Resonance
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 500-800
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/linkedin-audit/methodology/master-tracker-update.md, corpus/growth/strategy/repurposing-matrix.md, corpus/growth/creator-dynamics/founder-narrative-as-product.md]
---

# P3 — Thesis Resonance

## Purpose
Measures whether the **Context Layers & AI thesis** — Riché's brand moat — is the dominant performer relative to the broader feed. The Context Layers & AI positioning compounds only if it's seen, engaged with, and reshared at meaningful rates. P3 catches when CI underperforms (signaling thesis-market fit problems) or when the format mix has drifted away from the 50/30/20 target (CI/PM/Leadership).

P3 is the most strategically loaded pillar — it's the one most likely to fire actionable findings about *what to write next*.

## Inputs
- `parsed_export.top_posts_by_engagements` — top 50 by engagement
- `parsed_export.top_posts_by_impressions` — top 50 by impressions
- Master Tracker `Posts Master` (joined to URL) for Format + Domain mapping
- Content Topics DB (`CONTENT_TOPICS_DB_ID`) for canonical Format + Domain on new posts
- `DOMAIN_BALANCE_TARGET` constant (50% CI / 30% PM / 20% Leadership)

## Metrics computed

| Metric | Formula | Target |
|---|---|---|
| Engagement rate by domain | sum(engagements) / sum(impressions) per domain | CI ≥ 3% |
| Domain mix (impressions) | impressions per domain / total impressions | 50/30/20 within ±5pp |
| Format performance | impressions per format / posts per format | (qualitative — Frameworks and Deep Dives should top) |
| Unclassified posts | count of period posts not yet tagged Format+Domain in Content Topics DB | 0 |
| Top performing post by domain | URL with highest impressions per domain | (qualitative — surfaces what's working) |

Domain definitions:
- **Context Layers & AI (CI):** posts about context architecture, RAG, agent memory, retrieval, evals, the Five-Step Loop, Active Generation
- **PM:** posts about product management craft (specs, prioritization, frameworks, AI-PM career)
- **Leadership:** posts about teams, founders, decision-making, hiring, building (often crossover)
- **Intersection:** explicit cross-domain posts (e.g., "AI PM career") that don't sit cleanly in one bucket

## Severity rules

| Condition | Severity | Headline pattern |
|---|---|---|
| CI engagement rate is bottom-quartile across domains | **P0** | "Context Layers & AI engagement bottom-quartile ({N}%). Thesis-market fit signal." |
| Domain mix drifts ≥10pp from target on any domain | **P0** | "Domain mix drift: {domain} at {actual}% vs {target}% target." |
| CI engagement rate < 1% | **P1** | "Context Layers & AI engagement at {N}% — below action threshold." |
| Domain mix drifts 5-10pp from target | **P1** | "Domain mix drift: {domain} at {actual}% vs {target}% target." |
| ≥5 unclassified posts in period | **P1** | "{N} period posts unclassified in Content Topics DB — tag before next audit." |
| Format mix heavily skewed (one format >60% of posts) | **P1** | "Format skew: {format} is {pct}% of posts. Mix imbalance." |
| Within tolerances | (no finding) | — |

## Headline format for findings

```
{severity}: {headline}

Evidence:
- CI engagement rate: {N}% ({rank} of 4 domains)
- PM engagement rate: {N}%
- Leadership engagement rate: {N}%
- Intersection engagement rate: {N}%
- Domain mix (by impressions): CI {N}%, PM {N}%, Leadership {N}%, Intersection {N}%
- Top CI post: {URL} ({impressions}, {engagements})
- Top PM post: {URL} ({impressions}, {engagements})
- Unclassified: {N} posts ({URLs if ≤5})
- Format mix: Hot Take {N}, Signal {N}, Deep Dive {N}, Framework {N}, Story {N}

Action:
{recommended-action}
```

## Action recommendations

- **CI engagement bottom-quartile (P0):** "Draft a Context Layers & AI Deep Dive that opens with a counter-claim (per `corpus/voice/` hook patterns). Reference the top-performing peer creators in the Context Layers & AI space (per `corpus/linkedin-audit/pillars/p5-competitive-benchmarking.md`)."
- **Domain mix drift (P0/P1):** "Rebalance next batch toward {underweighted domain}; cut {overweighted domain} by {N} posts. Reach `DOMAIN_BALANCE_TARGET` over 4 weeks."
- **CI <1% engagement (P1):** "Investigate via P5 — what are CI peers doing differently? Likely hook quality or topic specificity issues."
- **Unclassified posts (P1):** "Tag {N} posts in Content Topics DB before next audit. Without classification, P3 narratives miss the actual mix."
- **Format skew (P1):** "Rebalance format mix per `corpus/growth/creator-dynamics/frequency-vs-quality-tradeoff.md` — too many of one format means thinner audience response curves."

## Examples

1. **On-target month.** CI 3.4%, PM 4.1%, Leadership 2.8%, Intersection 2.3%. Mix: CI 52%, PM 28%, Leadership 18%, Intersection 2%. CI is performing; mix on target. No finding fired. Narrative notes top CI post for celebration.
2. **CI underperforming (P1).** CI 1.2% (rank 4 of 4). PM 4.1%, Leadership 2.8%, Intersection 2.3%. P1 fires: "Context Layers & AI engagement at 1.2% — below action threshold." Action: draft a CI Deep Dive with a counter-claim hook.
3. **Domain mix drift + CI collapse (P0 + P0).** CI engagement 0.4% (bottom-quartile P0). Mix: CI 28% (vs 50% target — 22pp drift, P0). Compounding signals: thesis-market fit problem. 2 P0s; first task issued is the CI Deep Dive; second is "Pause non-CI publishing for 2 weeks to rebalance."
4. **Unclassified backlog (P1).** 8 period posts not tagged in Content Topics DB. P1 fires; without tagging, the % computations are degraded estimates.

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — pillar-running protocol
- `corpus/linkedin-audit/methodology/master-tracker-update.md` — produces the joined Posts Master that this pillar reads
- `corpus/growth/strategy/repurposing-matrix.md` — derivative production tied to format mix
- `corpus/growth/creator-dynamics/founder-narrative-as-product.md` — CI is the narrative arc; underperformance = arc weakness
- `corpus/voice/` — hook patterns owned by `rz-copywriting`

## Anti-patterns

- Reading engagement-rate-by-domain without normalizing for impressions. Small-impression domains can show big rates from 1 viral comment thread; weight or sanity-check against impression count.
- Tagging posts as "Intersection" by default when unsure. Better to leave Unclassified and surface in P1 than to corrupt the domain mix metric.
- Reacting to one bad CI month with a strategy pivot. CI is the moat; small-sample variance is expected. Action only on multi-month drift.
- Treating PM outperformance as a problem. PM strongly performing is fine — but if it crowds out CI cadence, the moat erodes. Mix matters.
