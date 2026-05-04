---
name: Deep Dive Candidate Selection
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 300-600
related: [corpus/linkedin-audit/deep-dive/trigger-criteria.md, corpus/linkedin-audit/deep-dive/enrichment-checklist.md, corpus/linkedin-audit/methodology/report-assembly.md]
---

# Deep Dive Candidate Selection

## What it is
Step 5 of the audit. Selects the Top 5 posts from the audited period for potential per-post enrichment via the separate Deep Dive sub-workflow. Selection is fast (no API calls); enrichment is slow and manual, so the audit does NOT enrich automatically — it just identifies candidates.

The selection criterion is configurable via the `DEEP_DIVE_CRITERION` constant. Default: top 5 by absolute impressions in the period.

## Why it matters
Deep Dive enrichment requires the LinkedIn Community Management API (or manual click-through) to gather data the bulk export does not provide: engagement-type breakdown (reactions vs. comments vs. bookmarks vs. shares), commenter list with ICP match per commenter, click data, and substantive-vs-drive-by comment classification. This is expensive — 15–30 minutes per post, much of it manual.

Identifying the 5 most-worthwhile candidates per month gates that effort to where it pays back. Riché reviews the candidate list and decides which (if any) to enrich. Often it's 1–2 of 5; sometimes 0; rarely 5.

## Selection criteria options

The default and three alternatives are encoded in `corpus/linkedin-audit/deep-dive/trigger-criteria.md`. The active criterion for the run is set in `DEEP_DIVE_CRITERION`.

| Criterion value | Selection logic | When to prefer |
|---|---|---|
| `top-5-by-absolute-impressions` (default) | Top 5 from `top_posts_by_impressions` in the audited period | Default; surfaces the highest-reach posts for understanding what works |
| `top-5-by-mom-delta` | Top 5 with positive MoM impression delta from Snapshots, period filter applied | Compounder-focused months; understanding tail behavior |
| `top-5-by-engagement-rate` | Top 5 by engagement-rate (engagements/impressions) per post | Engagement-rate diagnostic months |
| `one-per-format` | Top performer in each of 5 formats (Hot Take, Signal, Deep Dive, Framework, Story) | Format-balance investigation months |

## How to apply

1. **Read `DEEP_DIVE_CRITERION`** from the SKILL.md Constants block (or runtime override if Riché passes one in the invocation).
2. **Apply the corresponding selection logic** against the parsed export + updated Master Tracker.
3. **Output 5 post URLs** as an ordered list with the selecting metric value alongside.
4. **Write to Notion audit page property `Deep Dive Candidates`** as comma-separated URLs.
5. **Write to audit narrative** under "Deep Dive Candidates" section: each URL with publish date + selecting metric value + 1-line context.
6. **Do NOT enrich.** Enrichment is manually triggered later via the deep-dive sub-workflow.

## Edge cases

- **Fewer than 5 posts in the period.** Return all available; note in narrative.
- **Tie at the 5th position.** Break by recency (more recent first), then by alphabetic URL. Document the tie-break in the narrative.
- **Same post appears as candidate two months running.** Allowed; deep-dive enrichment for the second occurrence may add value (different commenter cohort, different timing context). Note in narrative: "Re-selected from prior month."

## Examples
1. **Default criterion, May 2026.** Top 5 by absolute impressions: post A (33,148), post B (9,475), post C (4,946), post D (4,826), post E (4,730). Written to Notion property + narrative. Riché reviews next day; selects A and C for enrichment, skips others.
2. **Compounder month.** Riché overrides criterion: `top-5-by-mom-delta`. Selection returns 5 posts with strongest positive deltas. Three are 4+ months old (true late-bloomer compounders).
3. **Format-balance investigation.** P3 fired P1 for Context Layers & AI underperformance. Riché overrides to `one-per-format` to surface the best of each format and inform Deep Dive scope.

## Related entries
- `corpus/linkedin-audit/deep-dive/trigger-criteria.md` — defines the selection logic per criterion
- `corpus/linkedin-audit/deep-dive/enrichment-checklist.md` — what enrichment gathers per candidate (separate manual workflow)
- `corpus/linkedin-audit/methodology/report-assembly.md` — Step 7, narrates the candidate list

## Anti-patterns
- Auto-enriching candidates without Riché's review. Burns time on candidates that don't warrant it.
- Hard-coding the criterion. Different months want different lenses; keep `DEEP_DIVE_CRITERION` overridable.
- Selecting 0 candidates because "nothing stood out." If 5 posts ran, there are 5 candidates to surface; let Riché decide whether to enrich.
- Selecting >5 candidates "to be safe." 5 is the cap; the cap is the discipline.
