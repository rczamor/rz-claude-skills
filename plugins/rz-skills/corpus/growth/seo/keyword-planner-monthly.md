---
name: Keyword Planner Monthly Refresh
domain: growth
source_skill: growth-marketing
entry_type: template
length_target: 500-800
related: [corpus/growth/seo/free-stack-overview.md, corpus/growth/seo/topic-clusters.md, corpus/growth/seo/target-keywords-schema.md, corpus/website-audit/dimensions/categories/keyword-research.md]
---

# Keyword Planner Monthly Refresh

## What it is
Riché's once-a-month, ~15 minute workflow for refreshing search volumes on existing Target Keywords and discovering new candidates, using Google Keyword Planner inside a Google Ads account with no spend. The session has two jobs and produces a single output: an updated Target Keywords DB in Notion.

| Job | Time | Output |
|---|---|---|
| Job 1 — Refresh volumes on tracked keywords | 5–7 min | All Researching/Targeting/Ranking rows have current `Monthly Volume` and `Volume Last Updated` |
| Job 2 — Discover new candidates from seed searches | 7–10 min | 5–15 new rows added with status `Researching` |

The workflow is manual on purpose. Browser-automating Keyword Planner risks Google Ads account suspension under the Terms of Service, and the 15-minute monthly cost is below the threshold where automation pays back.

## Why it matters
Stale volume data is the silent failure mode of free-stack keyword research. Keyword Planner volumes update monthly. If Riché skips two months, K1 (stale data) fires across the board and the priority-score sort that drives K3 (SERP review) becomes unreliable. The monthly cadence is the cheapest possible insurance against that.

The seed-search half of the session is what keeps the Target Keywords DB from going stale in a different way: relevant. New terms emerge in the AI/context engineering space every month. Without active discovery, the tracked set ossifies around terms from when the DB was first seeded.

## How to apply

**Pre-session checklist (1 min)**
- Open Google Ads → Tools → Keyword Planner
- Open Notion Target Keywords DB in a second tab
- Have the last 7 Daily Briefings loaded (for seed terms)

**Job 1 — Refresh volumes (5–7 min)**

1. In Notion, filter Target Keywords DB to status `Researching`, `Targeting`, or `Ranking`. Copy the keyword column.
2. In Keyword Planner, choose `Get search volume and forecasts`. Paste the keyword list. Set location: United States. Set language: English. Run.
3. Export the volumes view (download CSV) or copy each row.
4. For each row in Notion: update `Monthly Volume`, set `Volume Source` to `Google Keyword Planner`, set `Volume Last Updated` to today.
5. Spot-check 2–3 keywords for outlier shifts (>50% change up or down). Note any in the `Notes` field.

**Job 2 — Discover new candidates (7–10 min)**

1. Pick 3–5 seed terms from the last 7 Daily Briefings. Examples of strong seeds: terms that appeared in 2+ briefings, terms tied to a Top Signal, or terms matching one of the 7 priority topic clusters that's underweight in the tracked set.
2. In Keyword Planner, choose `Discover new keywords`. Enter the seeds. Run.
3. Scan the results. Filter for relevance to one of the three domains (Context Layer, PM, Leadership). Ignore high-volume tangents (e.g., generic "machine learning" terms).
4. For each viable candidate (typically 5–15 per session): add a new row in Target Keywords DB with status `Researching`, the seeded domain, current Monthly Volume, today's Volume Last Updated, and the seed term in `Notes`.

**Post-session (1 min)**
- In Notion, verify all Researching/Targeting/Ranking rows have `Volume Last Updated` within the last 30 days.
- The audit's K1 dimension will read this field next Sunday and reset to clean if the refresh held.

## When to skip
- Status `Won` and `Deprioritized` rows do not need volume refreshes (they're frozen).
- If the previous month's session was within 14 days, defer to the next cycle.
- Travel weeks: defer to the following Sunday. K1 will fire once at >30 days; that's the design, not a failure.

## Examples
1. **Routine session.** First Sunday of the month, 4pm. 30 tracked keywords refreshed in 6 min; 4 seed terms run; 9 new Researching rows added. Total 14 min.
2. **Discovery-heavy session.** Quarterly rebaseline week (January, April, July, October — first Sunday). Same Job 1, but Job 2 expands to 8 seeds and adds 25–30 new Researching rows. Total ~30 min, allocated.
3. **Defer-and-recover.** Two months skipped due to travel. K1 fires on all 30 rows for two consecutive audits. Single recovery session takes 20 min (Job 1 only); Job 2 deferred one more week.

## Related entries
- `corpus/growth/seo/free-stack-overview.md` — the full free-stack methodology
- `corpus/growth/seo/topic-clusters.md` — the 7 priority topics that anchor seed selection
- `corpus/growth/seo/target-keywords-schema.md` — the Notion DB structure
- `corpus/website-audit/dimensions/categories/keyword-research.md` — K1 (stale data) and the audit dimensions

## Anti-patterns
- Browser-automating Keyword Planner. TOS violation, account suspension risk, no payback at this cadence.
- Adding new keywords without a seed source. Discovery without grounding pulls the tracked set toward generic AI/PM terms that don't differentiate Riché's positioning.
- Skipping Job 2 "this month, just to refresh." Two consecutive Job-2 skips and the DB is locked in the past.
