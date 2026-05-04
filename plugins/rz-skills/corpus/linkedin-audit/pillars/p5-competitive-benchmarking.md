---
name: P5 — Competitive Benchmarking
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 400-700
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/website-audit/competitor-benchmarking/read-protocol.md, corpus/website-audit/databases/competitors-schema.md]
---

# P5 — Competitive Benchmarking

## Purpose
Periodic check on what Direct + Aspirational tier competitors are doing on LinkedIn. Identifies "what to steal" candidates (formats, hook patterns, topics that are working for them) and "what to avoid" (format experiments that are flopping). P5 is the only pillar with no P0/P1 fires — it's purely informational; findings narrate into the audit but don't seed Linear tasks.

P5 is the longest pillar to run (~10 minutes for web fetches across competitors). It runs after the cheaper pillars so a network-related failure doesn't block them.

## Inputs
- Competitors DB (`COMPETITORS_DB_ID`) — pull rows where `Tier ∈ {Direct, Aspirational}`
- Per competitor: their LinkedIn profile URL (from the Competitors DB row)
- web_fetch capability for LinkedIn profile pages

The Competitors DB is shared with `rz-website-audit`; both audits read from it. The DB schema is documented at `corpus/website-audit/databases/competitors-schema.md`.

## Metrics computed (per competitor)

| Metric | Source | Notes |
|---|---|---|
| Follower count | LinkedIn profile header | Snapshot at fetch time |
| Last 10 post titles | LinkedIn activity feed | First 10 visible posts on profile |
| Posting cadence (last 4 weeks) | activity timestamps | posts/week computed |
| Top performing post visible | activity feed | post with most reactions visible |
| Format observation | analysis of last 10 posts | what formats they're using |
| Engagement-to-followers ratio | top post engagement / follower count | proxy for engagement quality |

LinkedIn profile public visibility is limited — fetches may return only what's available without auth. `web_fetch` works for most public profiles; if blocked, fall back to Tavily extract or skip the competitor.

## Severity rules

P5 has no P0/P1 severity — all findings are **informational** (no Linear tasks issued). Findings format:

| Finding type | Headline pattern |
|---|---|
| What-to-steal candidate | "{Competitor} is using {format/pattern}: {evidence}. Worth testing." |
| What-to-avoid signal | "{Competitor} tried {format/pattern}; {observation}. Confirms anti-pattern." |
| Cadence comparison | "{Competitor} at {N}/week (Riché at {N}/week). {gap implication}." |
| Topic gap | "{Competitor} owns {topic} on LinkedIn; Riché has not posted on this. Consider entry." |

## Headline format for the P5 narrative section

```
P5 — Competitive Benchmarking

Direct tier ({N} competitors):
- {Competitor 1}: {follower count}, {posts/wk} cadence, top post {N} reactions. {note}
- {Competitor 2}: ...

Aspirational tier ({N} competitors):
- {Competitor 1}: ...

What to steal:
- {observation 1}
- {observation 2}

What to avoid:
- {observation 1}

Topic gaps Riché should consider:
- {topic 1} (owned by {competitor})
- {topic 2}
```

## Time budget

P5 should complete in ~10 minutes. If the Competitors DB has 14 rows (per the rz-website-audit baseline), Direct + Aspirational tiers are typically ~8 of those. ~75 seconds per fetch + analysis = ~10 min total.

If P5 takes >15 minutes, halt the pillar and note in narrative: "P5 web fetches timed out; competitive benchmarking abbreviated." Don't let P5 block the rest of the audit.

## Examples

1. **Standard P5.** 4 Direct + 4 Aspirational fetched. Direct tier: Aakash Gupta posting daily, top post on AI-PM hiring (3,200 reactions). Lenny posting 2x/week, top post on product strategy (1,800 reactions). What to steal: Aakash's "build in public" weekly cadence on a specific tool. What to avoid: Lenny's twitter-style threadpoof (low engagement). Topic gap: nobody in tier owns "context layer architecture" — Riché's moat is real.
2. **Fetch failure handling.** 2 of 8 fetches return blocked content. Note in P5 narrative: "Skipped {names} — profile fetch blocked." Continue with the 6 successful fetches. No P0/P1 fires; informational only.
3. **All fetches succeed; nothing to steal.** Rare. Narrative: "Competitive landscape steady. Aakash and Lenny holding cadence; no breakout patterns this month."

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — pillar-running protocol
- `corpus/website-audit/competitor-benchmarking/read-protocol.md` — the competitor-benchmarking pattern shared with the website audit
- `corpus/website-audit/databases/competitors-schema.md` — Competitors DB schema (shared)

## Anti-patterns

- Including Adjacent-tier competitors in P5. Adjacent tier is documented in the Competitors DB but only Direct + Aspirational get the per-month attention. Adjacent gets quarterly attention only.
- Letting P5 fire P0 because of a fetch failure. P5 is informational; fetch failures are noted but never block the audit or seed tasks.
- Quoting verbatim from competitor posts. Note format and topic; don't replicate copy.
- Treating competitor underperformance as proof Riché's approach is right. Different audiences; competitive signals are heuristics, not validations.
