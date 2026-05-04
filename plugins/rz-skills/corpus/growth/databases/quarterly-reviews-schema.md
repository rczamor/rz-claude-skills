---
name: Quarterly Reviews Database Schema
domain: growth
source_skill: growth-marketing
entry_type: resource
length_target: 400-700
related: [corpus/growth/playbook/quarterly-channel-review.md, corpus/growth/playbook/quarterly-priorities-template.md, corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/strategy/channel-maturity-model.md, corpus/growth/metrics/channel-roi-calculation.md]
---

# Quarterly Reviews Database Schema

## What it is
The Notion database where each quarterly review (one per quarter, run on the first Sunday of January, April, July, October) lives as a single page. Database ID `f51277cdd4d94f8e83c81cd1c08f82e8`, data source ID `1dadc999-7c9b-42de-98b4-75594c10a4b5`. Lives under Brand → Growth Strategy (page ID `356ac0ea4f6580828e68f93292e3ea9d`). One page per quarter, named `Q{N} {YYYY} Review`. Properties summarize the quarter; the page body holds the full assembled review per `corpus/growth/playbook/quarterly-channel-review.md`.

| Property | Type | Notes |
|---|---|---|
| Name | title | `Q{N} {YYYY} Review` (e.g., `Q4 2026 Review`) |
| Quarter | select | Q1 / Q2 / Q3 / Q4 |
| Year | number | 2026, 2027, etc. |
| Date Conducted | date | The first Sunday the review ran |
| Headline | select | 🟢 Green (on track) / 🟡 Yellow (mixed) / 🔴 Red (off track) |
| Active Channels | number | Total active channels at end-of-quarter |
| Channels Added | number | New channels launched this quarter |
| Channels Cut | number | Channels retired this quarter |
| Stage Transitions | number | Channels that changed maturity stage |
| Owned Channel % | number | % of growth time on owned channels (≥30 floor) |
| Weekly Hours Allocated | number | Sum of channel time allocations (≤5.25 ceiling) |
| LinkedIn Followers | number | End-of-quarter follower count |
| Newsletter Subs | number | If newsletter active; null otherwise |
| Number of Priorities Set | number | Should be 1-3 |
| Priorities Summary | rich_text | One-line per priority (max 3) |
| Linear Tasks Issued | rich_text | TRZ-### links for priority seed tasks |
| Notes | rich_text | Open-ended observations, lessons, anomalies |

The page body, when assembled, contains:
1. Executive summary (1 paragraph)
2. Data pull summary (per-channel ROI table)
3. Active channel scoring (with deltas vs prior quarter)
4. Stage transitions (with date and rationale per channel)
5. Deferred candidate gate progress (per gated channel)
6. Decisions: keep/grow/reduce/cut active; launch/defer candidates
7. Quarterly priorities (1-3 detailed entries per `quarterly-priorities-template.md`)
8. Time allocation lock (per-channel breakdown summing to ≤5.25)
9. Linear tasks issued (with TRZ-### IDs and due dates)

## Why it matters
Quarterly reviews are time-series data at a 4x/year cadence — too sparse for the weekly Audits DB pattern but critical for trend recognition over 4-12 quarters. Without a structured DB, the review either lives in scattered Notion pages (no trend queries possible) or doesn't get written down at all (the review happens but the institutional memory evaporates).

The Headline traffic light works the same way as in the Weekly Audits DB: it's the one-glance signal of "are we on track this quarter?" derived from the combination of cadence held, channel growth, priority progress, and budget discipline. The properties exist so multi-quarter queries work without parsing page bodies.

The Priorities Summary property is critical: it lets future skills (and Riché) instantly see "what was last quarter's bet" without opening the page. The body has the full priority detail; the property has the headline.

## How to apply

**Page creation timing:** Create the page only after the review is complete (all 6 blocks of `quarterly-channel-review.md` done + priorities written). Partial pages corrupt the time series.

**Naming convention:** `Q{N} {YYYY} Review` (e.g., `Q4 2026 Review`). Sortable, queryable, unambiguous.

**Headline computation:**
- 🟢 Green: cadence held all quarter + ≥1 priority moved meaningfully forward + budget within 5.25
- 🟡 Yellow: cadence broken in 1-2 weeks OR priority progress mixed OR owned-channel % below 30
- 🔴 Red: cadence broken 3+ weeks OR no priority progress OR budget exceeded sustainably

**Property population:**
- `Active Channels` / `Channels Added` / `Channels Cut`: from Block 5 decisions
- `Stage Transitions`: count of channels that moved Experiment→Invest, Invest→Optimize, etc.
- `Owned Channel %`: from `corpus/growth/strategy/owned-vs-rented-channels.md` calculation
- `Weekly Hours Allocated`: from Block 5 time allocation lock
- `LinkedIn Followers` / `Newsletter Subs`: end-of-quarter snapshot
- `Number of Priorities Set` / `Priorities Summary`: from Block 5 priority decisions
- `Linear Tasks Issued`: filled after task issuance step (TRZ-### IDs comma-separated)

**Multi-quarter retrospective query:** at each rebaseline (Q1, Q2, Q3, Q4 reviews), query the prior 4 quarters. Look for:
- Headlines trending Green → Yellow → Red (channel portfolio degrading)
- Owned Channel % trending below 30 (rented-channel over-reliance)
- Channels Added > Channels Cut consistently (sprawl signal)
- Same channel appearing as "added" then "cut" within 4 quarters (failed experiment pattern)
- Priorities never marked done (over-ambition or scope drift)

## Examples
1. **Standard green quarter.** Q3 2026 review: cadence held, owned channel % at 32%, 2 priorities advanced (newsletter gates closed, GitHub channel launched), budget at 5.0 hr/week. Page created with Headline = 🟢 Green, Priorities Summary = "Newsletter gates closed; GitHub channel launched as Experiment-stage."
2. **Mixed yellow quarter.** Q2 2026 review: LinkedIn cadence broke 2 weeks during travel, GitHub priority deferred to Q3, but newsletter gates closed and 1 talk delivered. Page created with Headline = 🟡 Yellow, Priorities Summary = "Newsletter gates closed (P1 done); GitHub deferred to Q3 (P2 incomplete)."
3. **Red quarter (rare).** Hypothetical Q1 2027: algo change in mid-quarter, LinkedIn cadence dropped to 1x/week for 6 weeks, priorities stalled, owned channel % dropped to 18% under the floor. Page created with Headline = 🔴 Red, Priorities Summary = "All Q1 priorities stalled; algo recovery work consumed cycles."

## Related entries
- `corpus/growth/playbook/quarterly-channel-review.md` — the 60-min process this DB receives output from
- `corpus/growth/playbook/quarterly-priorities-template.md` — the priority structure that fills Priorities Summary
- `corpus/growth/strategy/channel-evaluation-framework.md` — the scoring used in Block 2
- `corpus/growth/strategy/channel-maturity-model.md` — stage transitions tracked in the Stage Transitions property
- `corpus/growth/metrics/channel-roi-calculation.md` — informs the per-channel ROI table in the page body

## Anti-patterns
- Creating the page before the review is complete. Partial pages corrupt the time series.
- Renaming pages after creation. The `Q{N} {YYYY}` title is the queryable key.
- Skipping the Priorities Summary property because "the body has the detail." The property is what makes future-quarter queries fast.
- Treating Yellow as a problem rather than as the most common state. Most quarters are mixed; Yellow is honest.
- Letting the headline drift to Green by ignoring the budget or owned-channel checks. The headline is multi-criteria; one-criterion success doesn't make the whole quarter green.
