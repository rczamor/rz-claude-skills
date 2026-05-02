---
name: Target Keywords Database Schema
domain: growth
source_skill: growth-marketing
entry_type: resource
length_target: 400-700
related: [corpus/growth/seo/free-stack-overview.md, corpus/growth/seo/keyword-planner-monthly.md, corpus/growth/seo/topic-clusters.md, corpus/website-audit/dimensions/categories/keyword-research.md]
---

# Target Keywords Database Schema

## What it is
The Notion database that holds every keyword the audit tracks. Database ID `f5521fe72dec42c1808555fbac2d0d62`, data source ID `df1d8efa-ff31-4b18-beb5-0998e9dd9bc2`. Eleven properties, one row per keyword, lifecycle tracked via Status. The audit reads this DB at the start of every run and writes back ranking and timestamp data after the dimension scoring step.

| Property | Type | Notes |
|---|---|---|
| Keyword | title | The term as searched |
| Domain | select | Context Layer / PM / Leadership |
| Monthly Volume | number | From Keyword Planner |
| Volume Source | select | Keyword Planner / GSC / Manual |
| Volume Last Updated | date | Reset on monthly refresh |
| Competition | select | Low / Medium / High |
| Status | status | Researching / Targeting / Ranking / Won / Deprioritized |
| Target Page URL | url | The richezamor.com page targeting this term |
| Current Position | number | From GSC; null if not ranking |
| Last Checked | date | Reset by the audit each run |
| Notes | rich_text | Seed term, qualitative observations |

## Why it matters
A database is the only thing that survives between weekly audits. Treating Notion as an ad-hoc scratchpad means losing the longitudinal view of which keywords are moving and which have plateaued. The Target Keywords DB is the time-series spine of the keyword research dimension; without it K1 (stale data), K2 (targeted but invisible), and K5 (intent mismatch) all become unfireable.

The Status field is the lifecycle signal. Each transition is meaningful: Researching → Targeting commits content investment; Targeting → Ranking marks the first GSC impression; Ranking → Won marks a top-10 placement. The Won state is the end-state for celebration, not abandonment; Won keywords still get position checks in case they regress.

## How to apply

**Status enum semantics (strict):**

- **Researching**. Candidate term, not yet committed to a content plan. New rows from Keyword Planner Discover land here.
- **Targeting**. Actively building content for it. The Content Queue has a slot assigned; the Target Page URL may or may not exist yet.
- **Ranking**. Page exists, position 11–100. GSC has registered impressions. The piece is in the index but not yet on page 1.
- **Won**. Position 1–10. Top-of-page-1 placement.
- **Deprioritized**. Abandoned, with a reason in Notes. Do not delete; archive via status so the historical record stays intact.

**Audit read at start of run:** filter status != Deprioritized. Cross-reference each row with this run's GSC data (via Ahrefs MCP).

**Audit write back after scoring:**

- `Current Position` and `Last Checked` always update for every non-Deprioritized row.
- Status transitions are automatic when the rule fires:
  - `Targeting` → `Ranking` when first GSC impression appears in the last 28 days.
  - `Ranking` → `Won` when position ≤10 sustained for 2 consecutive audits.
- Status transitions never go backward automatically. Won → Ranking on regression is a manual call by Riché.

**Auto-deprioritization guardrail:** do NOT auto-deprioritize keywords without 90 days of zero impressions. The recovery cost (re-research, re-targeting) outweighs the small DB hygiene cost.

## Examples
1. **New row creation.** Riché's monthly Keyword Planner Discover surfaces "context engineering patterns" with volume 720 and competition Medium. New row: Keyword = "context engineering patterns", Domain = Context Layer, Monthly Volume = 720, Volume Source = Keyword Planner, Volume Last Updated = today, Competition = Medium, Status = Researching, Notes = "Seed: context engineering. Cluster: RAG vs Context Engineering."
2. **Targeting → Ranking transition.** "what is a context layer" has been at status Targeting for 6 weeks. This week's GSC pull shows 47 impressions at average position 38. Audit transitions status to Ranking, sets Current Position = 38, Last Checked = today.
3. **Won → Ranking regression.** "context layer vs RAG" was at Won (position 7) for 4 weeks. This run shows position 14. Audit does NOT auto-transition the status; instead it logs the regression in the Weekly Audit page under Notable Movements and surfaces it for Riché to review.

## Related entries
- `corpus/growth/seo/free-stack-overview.md`. How the DB integrates with GSC and Keyword Planner
- `corpus/growth/seo/keyword-planner-monthly.md`. When new rows are created and volumes refreshed
- `corpus/growth/seo/topic-clusters.md`. The cluster taxonomy that anchors Domain = Context Layer rows
- `corpus/website-audit/dimensions/categories/keyword-research.md`. The K1–K5 checks that read this DB

## Anti-patterns
- Creating new keywords mid-audit. That work belongs to the monthly refresh; mid-audit insertions corrupt the time series.
- Deleting Deprioritized rows. The historical record matters for retrospectives; archive via status, never delete.
- Letting Volume Source drift to "Manual" silently. Manual entries break the K1 staleness check; if you have to enter a volume by hand, note the source in Notes.
