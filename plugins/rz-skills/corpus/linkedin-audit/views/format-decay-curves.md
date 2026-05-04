---
name: Format Decay Curves View
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: framework
length_target: 300-600
related: [corpus/linkedin-audit/databases/master-tracker-sheet-schema.md, corpus/growth/metrics/content-decay-analysis.md, corpus/growth/creator-dynamics/frequency-vs-quality-tradeoff.md, corpus/linkedin-audit/methodology/report-assembly.md]
---

# Format Decay Curves View

## What it is
The Master Tracker tab that pivots `Snapshots` by Format × Days-Since-Publish bucket and computes average impressions per bucket. Shows which formats decay fastest (typically Hot Takes, half-life ≤3 days) vs slowest (typically Frameworks and Deep Dives, half-life 30+ days). Informs production effort allocation.

## Why it matters
Riché's 5.25 hr/week growth budget (per `corpus/growth/playbook/budget-allocation.md`) is finite. Format decay tells him which formats earn back their production cost over what timeframe:

- **Hot Take:** 30 min to write, 80% of impressions in first 48 hours
- **Signal:** 20 min to write, 80% in first 24 hours
- **Deep Dive:** 2-3 hrs to write, decay over 30+ days; can compound into late bloomers
- **Framework:** 1-2 hrs to write, longest tail (search-surfaced)
- **Story:** 30-45 min to write, varies wildly (some viral, most short tail)

If the budget overweights short-tail formats, the brand is on a treadmill. If it overweights long-tail, cadence breaks. The Format Decay Curves view makes this trade visible monthly.

## Definition (Sheet formula)

In the `Format Decay Curves` tab, pivot:

- **Rows:** Format (Hot Take / Signal / Deep Dive / Framework / Story)
- **Columns:** Days-Since-Publish bucket — 0-7, 8-14, 15-30, 31-60, 61+
- **Values:** AVERAGE of impressions per Snapshots row matching (Format, bucket)

Implementation via pivot table or QUERY:

```
=QUERY({Snapshots, Posts_Master Format column},
  "SELECT Format,
     AVG(CASE WHEN Days BETWEEN 0 AND 7 THEN Impressions END),
     AVG(CASE WHEN Days BETWEEN 8 AND 14 THEN Impressions END),
     AVG(CASE WHEN Days BETWEEN 15 AND 30 THEN Impressions END),
     AVG(CASE WHEN Days BETWEEN 31 AND 60 THEN Impressions END),
     AVG(CASE WHEN Days >= 61 THEN Impressions END)
   GROUP BY Format",
  -1)
```

(Implementation may need a helper column joining Posts Master Format onto Snapshots; details in `databases/master-tracker-sheet-schema.md`.)

## Output for the audit

The audit page's "Format Decay Observation" section gets a 1-paragraph synthesis from this view:

```
Format decay observation:

{Format with longest tail} continues to compound — averaging {N} impressions
in the 31-60 day bucket vs {N} in 0-7 day. This {N}x ratio confirms
{Framework/Deep Dive} as the highest leverage format for the {goal: SEO/
authority/long-term reach}.

{Format with shortest tail} averages {N} impressions in 0-7 days but
collapses to {N} in 8-14 days — a {N}x drop. Confirms {Hot Take/Signal} as
the cadence-feeder format, not the compounder.

Production allocation implication: {N} hr/week on {long-tail format} +
{N} posts/week on {short-tail format} matches the empirical decay curves.
```

If the data is too sparse to compute meaningful averages (early audits with few snapshots), narrate accordingly: "Format Decay Curves view has insufficient data; revisit after 3+ snapshots."

## Minimum data threshold

The view needs at least:
- 3 monthly snapshots (so 31-60 day bucket has data)
- 3+ posts in each Format (so averages aren't single-post outliers)

Below either threshold, surface in narrative as "data sparse" rather than computing misleading averages.

## Examples

1. **Mature data month.** 6 monthly snapshots accumulated. Frameworks: 800 / 700 / 600 / 550 / 480 (slow decay). Hot Takes: 1,200 / 400 / 200 / 100 / 80 (steep decay). Narrative: "Frameworks at 60% retention 31-60 days vs Hot Takes at 8%. Confirmed leverage on Frameworks."
2. **Sparse data month.** 2 monthly snapshots. View can compute 0-7 and 8-14 buckets only. Narrative: "Format Decay Curves view has insufficient data for the 30+ day buckets; revisit at month 4."
3. **Anomaly month.** A single Story format post went viral (3 weeks of high impressions). Narrative: "Story format averages distorted by {URL}. Excluding outlier, Story still trends shorter-tail than Deep Dive."

## Related entries
- `corpus/linkedin-audit/databases/master-tracker-sheet-schema.md` — Snapshots structure
- `corpus/growth/metrics/content-decay-analysis.md` — broader decay rates by channel
- `corpus/growth/creator-dynamics/frequency-vs-quality-tradeoff.md` — frequency vs depth balance
- `corpus/linkedin-audit/methodology/report-assembly.md` — Step 7 surfaces this view

## Anti-patterns

- Computing averages with <3 posts per format. Single-post outliers distort the curve.
- Treating the view as a fixed truth. Decay curves shift over time as audience composition changes; re-evaluate quarterly.
- Letting the "long tail favors Frameworks" insight drive 100% Framework production. Frequency still matters; the budget allocation honors the cadence target plus the long-tail bias.
- Forgetting that the curves are LinkedIn-specific. Same Format on richezamor.com or YouTube has different decay; don't generalize.
