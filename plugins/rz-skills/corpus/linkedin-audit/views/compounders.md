---
name: Compounders View
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: framework
length_target: 300-500
related: [corpus/linkedin-audit/databases/master-tracker-sheet-schema.md, corpus/linkedin-audit/views/late-bloomers.md, corpus/growth/metrics/content-decay-analysis.md, corpus/linkedin-audit/methodology/report-assembly.md]
---

# Compounders View

## What it is
The Master Tracker tab that surfaces posts still accumulating impressions month-over-month — proof of long-tail compounding. Defined as: posts where the most recent `Snapshots` row has a positive MoM Impression Delta AND the post is more than 7 days old. Sorted descending by MoM delta, top 5 surfaced into the audit.

## Why it matters
Most LinkedIn posts decay fast (24-hour half-life per `corpus/growth/metrics/content-decay-analysis.md`). When a post breaks that pattern — gaining impressions weeks or months after publish — it's a compounding asset. Identifying these posts tells Riché:

1. **Which formats compound.** Frameworks and Deep Dives often, Hot Takes rarely.
2. **Which topics compound.** Context Layers & AI Deep Dives that get linked to, Suzy stories cited in conversations, framework explainers that get search-surfaced.
3. **What to amplify.** A compounding post is often worth republishing on richezamor.com or referencing in a newsletter once active.

Without an explicit Compounders view, these posts get lost in the sea of TOP POSTS by raw impressions and Riché never names what's working over time.

## Definition (Sheet formula)

In the `Compounders` tab, filter `Snapshots` joined to `Posts Master`:

```
=QUERY(Snapshots,
  "SELECT * WHERE MoM_Impression_Delta > 0
   AND Days_Since_Publish_at_Snapshot > 7
   ORDER BY MoM_Impression_Delta DESC
   LIMIT 50",
  -1)
```

Or in plain language: rows where this month's impressions exceeded last month's for a post older than a week, sorted by the absolute delta.

## Output for the audit

The audit page's "Top 5 Compounders" section narrates the top 5 from this view:

```
{N} posts continued accumulating impressions this month.

The top compounder is {URL} ({first 60 chars of post commentary or title}),
which gained {delta} impressions despite being published {days_since_publish}
days ago. This pattern suggests {format} content has {short/medium/long} tail.

#2: {URL} (+{delta} impressions, {days} old)
#3: {URL} (+{delta} impressions, {days} old)
#4: {URL} (+{delta} impressions, {days} old)
#5: {URL} (+{delta} impressions, {days} old)
```

If fewer than 5 compounders exist, surface all and note in narrative: "Only {N} posts compounded this month."

## Examples

1. **Strong compounder month.** 12 posts compounded. Top is a 3-month-old Deep Dive on Active Generation pipelines, gaining 1,840 impressions this month vs last. Narrative: "Active Generation Deep Dive continues to compound — 5,400 cumulative impressions over 4 months."
2. **Quiet compounder month.** 2 posts compounded. Both 7-14 days old (early-tail bumps, not true compounding). Narrative: "Limited compounding this month; surface candidates with weak signal."
3. **Single breakout compounder.** 1 post — a 6-month-old Suzy story — gained 8,200 impressions after a peer reshared it in a viral thread. Narrative: "{URL} broke through 6 months post-publish via {peer reshare/inferred mechanism}. Late-life surge."

## Related entries
- `corpus/linkedin-audit/databases/master-tracker-sheet-schema.md` — Snapshots and Posts Master schemas
- `corpus/linkedin-audit/views/late-bloomers.md` — adjacent view (different selection criteria)
- `corpus/growth/metrics/content-decay-analysis.md` — half-life context for why compounding matters
- `corpus/linkedin-audit/methodology/report-assembly.md` — Step 7 narrates this view

## Anti-patterns

- Counting tail-bumps in week 1-2 as "compounders." The 7-day floor exists to filter out normal first-week impression growth.
- Overweighting compounders against fresh-post performance. Compounders are a signal, not a strategy — most output should still be fresh content.
- Republishing compounders verbatim. The compound signal is "this post earned a long tail"; the action is usually adjacent (write more like it), not literal re-share.
