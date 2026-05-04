---
name: Deep Dive Trigger Criteria
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 300-600
related: [corpus/linkedin-audit/methodology/deep-dive-candidate-selection.md, corpus/linkedin-audit/deep-dive/enrichment-checklist.md]
---

# Deep Dive Trigger Criteria

## What it is
The selection logic for picking 5 Top Deep Dive candidates each month. Selection is configurable via the `DEEP_DIVE_CRITERION` constant in SKILL.md; Riché can also override per-run by passing the criterion in the invocation prompt.

## Why it matters
Deep dive enrichment costs 15-30 minutes per post (manual or browser-assisted, since the bulk export does not include engagement-type breakdown, commenter list, or comment classification). Picking the right 5 — the ones most worth enriching — gates that effort to where it pays back.

Different months call for different lenses. Sometimes the question is "what's working at scale?" (top by impressions). Sometimes "what's compounding?" (top by MoM delta). Sometimes "where's the engagement quality high?" (top by engagement rate). The criterion should match the question.

## The 4 criteria options

### `top-5-by-absolute-impressions` (default)
**Selection logic:** Pull `top_posts_by_impressions` from the parsed export, take the top 5 by impressions, period filter applied (publish_date in [Period Start, Period End]).

**When to use:** Default. Surfaces the highest-reach posts of the month for understanding what's earning attention.

**Pros:** Aligns with the most common question — "what worked?"
**Cons:** Can over-index on viral one-offs that don't reflect the broader trend. May miss high-engagement-low-reach posts.

### `top-5-by-mom-delta`
**Selection logic:** Pull from Snapshots tab where MoM Impression Delta > 0 AND publish_date in current period (or older — late bloomers also qualify). Take top 5 by absolute delta.

**When to use:** Compounder-focused months — when the question is "what's still growing?" or "which posts have legs?"

**Pros:** Surfaces compounding patterns and late bloomers worth republishing.
**Cons:** Skewed toward older posts; misses fresh-period analysis.

### `top-5-by-engagement-rate`
**Selection logic:** For each post in `top_posts_by_engagements` ∩ `top_posts_by_impressions`, compute engagements/impressions. Take top 5 by rate, with a minimum-impressions floor (e.g., ≥500) to filter out 1-engagement-on-30-impressions noise.

**When to use:** Engagement-rate diagnostic months (when P3 fired or when newsletter Gate 2 is approaching). Surfaces what types of posts trigger high engagement quality.

**Pros:** Engagement quality is the newsletter gate signal; this lens directly informs gate strategy.
**Cons:** Floor selection matters; too low = noise, too high = excludes legitimate small-reach high-engagement posts.

### `one-per-format`
**Selection logic:** For each Format (Hot Take, Signal, Deep Dive, Framework, Story), select the top performer by impressions in the period. Returns 5 posts, one per format.

**When to use:** Format-balance investigation months (when P3 fired for format skew, or when production allocation is being revisited).

**Pros:** Forces format-diverse Deep Dive scope; avoids 5-Hot-Takes-in-a-row analysis.
**Cons:** May surface a "winner" in a format with only 1 post — small-sample bias.

## How to apply

1. **Read `DEEP_DIVE_CRITERION`** from SKILL.md Constants (default: `top-5-by-absolute-impressions`).
2. **Check for runtime override.** If the invocation includes "deep dive criterion: X", use X.
3. **Apply the selection logic** corresponding to the active criterion.
4. **Output 5 URLs ordered by the selecting metric**, with the metric value alongside.
5. **Write to the audit page** (Notion property `Deep Dive Candidates` and the Deep Dive Candidates body section).

## Edge cases

- **Fewer than 5 posts qualify** (e.g., `top-5-by-mom-delta` and only 3 posts have positive delta). Surface what's available; note in narrative: "Only {N} candidates met criterion {X}."
- **Tie at the 5th position.** Break by recency (more recent first), then by alphabetic URL.
- **Same post appears as candidate two months running.** Allowed; deep-dive enrichment for the second occurrence may add value (different commenter cohort, different timing context). Note in narrative: "Re-selected from prior month."

## Examples

1. **Default criterion, May 2026.** Top 5 by absolute impressions: post A (33,148), B (9,475), C (4,946), D (4,826), E (4,730). Riché reviews; selects A and C for enrichment.
2. **Engagement-rate criterion, June 2026.** P3 fired P1 last month for CI underperformance. Riché overrides criterion. Top 5 by rate (≥500 floor): post X (8.2%), Y (6.4%), Z (5.9%), W (4.1%), V (3.8%). All 5 are CI Deep Dives — informs the Deep Dive enrichment of "what makes a high-rate CI post?"
3. **One-per-format, July 2026.** P3 fired for format skew (60% Hot Takes). Riché overrides. Top performer per format: Hot Take 12K imp, Signal 4K, Deep Dive 8K, Framework 22K, Story 6K. Surfaces Framework as the under-leveraged format.

## Related entries
- `corpus/linkedin-audit/methodology/deep-dive-candidate-selection.md` — Step 5 of the audit; this entry defines the selection logic
- `corpus/linkedin-audit/deep-dive/enrichment-checklist.md` — what enrichment gathers per selected candidate

## Anti-patterns

- Hard-coding the criterion in the skill. Different months call for different lenses; keep it overridable.
- Auto-enriching all 5 candidates. Enrichment is manual / partially automated; Riché reviews the candidate list and picks 0-5 for enrichment.
- Using criterion X to "validate" a hypothesis. Don't pick the criterion that surfaces what you want to find; pick the criterion that matches the month's question.
