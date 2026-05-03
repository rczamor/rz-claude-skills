---
name: Engagement Drop Diagnostic — Symptom-First Lookup
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 400-700
related: [corpus/growth/diagnostics/algorithm-change-response.md, corpus/growth/metrics/engagement-quality-vs-count.md, corpus/growth/metrics/leading-vs-lagging.md, corpus/growth/playbook/quarterly-channel-review.md]
---

# Engagement Drop Diagnostic — Symptom-First Lookup

## What it is
The diagnostic to run when LinkedIn impressions, engagement rate, or peer reshare rate drops noticeably (>20% week-over-week, or >30% month-over-month) without an obvious cause. The protocol: check 5 things in a defined order, take action on the first one that explains the drop, do NOT make multiple changes simultaneously (compounds the diagnosis).

## Why it matters
The default reaction to an engagement drop is to "try something new" — change content type, change cadence, change tone. This is the wrong reaction in 4-out-of-5 cases. Most engagement drops have specific, identifiable causes that don't require strategy changes; they require returning to discipline. Strategy changes in response to a drop with a fixable cause produces the worst-of-both: the drop persists AND the strategic foundation gets confused.

The 5 most common causes, in order of frequency observed across 2024–2025 personal brand accounts:

1. **Cadence broke.** A skipped post, a delayed batch session, a week of reactive (not batch-written) content.
2. **Strategic commenting collapsed.** Daily 15–20 min commenting block got crowded out of the calendar.
3. **Content-type mix drifted.** Too many of one type (e.g., 4 hot takes in a row); not enough variety.
4. **Algorithm change.** Platform-side shift in how content gets surfaced.
5. **Audience composition shifted.** Inadvertently attracting the wrong audience (e.g., a viral post pulled in non-Segment-2 followers, diluting the engagement rate).

The diagnostic checks them in this order because (1) and (2) are fixable in the next week without strategic implications; (3) is fixable in 2 weeks with batch planning; (4) requires observation discipline (per `corpus/growth/diagnostics/algorithm-change-response.md`); (5) requires re-anchoring the targeting strategy.

## How to apply

**Step 1 — Cadence audit (2 min):**
Look at the last 4 weeks of LinkedIn posts. Count posts per week. Was any week below 3 posts? Was the prior week below the standard? **If yes:** the drop is likely cadence-explained. Action: re-establish 3-5x/week, batch the next 2 weeks ahead in the next Sunday session, observe for 2 weeks before doing anything else.

**Step 2 — Commenting audit (2 min):**
Open LinkedIn Premium analytics or a manual count of comments-on-others'-posts over the last 2 weeks. Was the daily commenting block held? **If no:** the drop is likely commenting-collapse-explained. Action: re-establish daily 15-20 min block in the calendar; batch comment-target list updates per `corpus/growth/playbook/strategic-commenting.md`.

**Step 3 — Content type audit (3 min):**
Look at the post-type distribution over the last 4 weeks. Mon-Fri content types should appear roughly evenly: hot take, signal, deep dive, framework, story. **If the distribution is skewed** (e.g., 60%+ hot takes, no stories), action: rebalance the next 2 weeks of posts toward the underrepresented types.

**Step 4 — Algorithm change check (5 min):**
Search "LinkedIn algorithm change {current month} {year}" and skim 3 reports. Has there been a documented platform-side shift? **If yes:** route to `corpus/growth/diagnostics/algorithm-change-response.md`. Do NOT make immediate strategic changes; observe for 2-4 weeks before adapting.

**Step 5 — Audience composition check (5 min):**
Look at the last 2 weeks of new followers. Are they Segment 2 (Product leader peers, AI PM, founders) or are they outside the target segments? **If composition shifted toward non-target audience:** action: tighten next-week posts to be sharply Segment-2-targeted (per `corpus/growth/segments/segment-2-channels.md`); avoid viral-bait content for 2-4 weeks.

**Stop at the first explained cause.** Do not stack interventions. If steps 1-2 explain the drop, don't also adjust content mix and audience targeting in the same week — the diagnosis becomes muddled.

## Decision tree

```
Engagement drop >20% WoW or >30% MoM
│
├─ Cadence broke? ──────────► Re-establish cadence; observe 2 weeks; STOP
│
├─ Commenting collapsed? ───► Re-establish block; observe 2 weeks; STOP
│
├─ Content mix skewed? ─────► Rebalance over next 2 weeks; observe; STOP
│
├─ Algorithm change? ───────► Go to algorithm-change-response.md; STOP
│
└─ Audience shift? ─────────► Tighten targeting; observe 4 weeks
```

## Examples
1. **Cadence-explained drop.** Mid-March 2026: LinkedIn impressions down 35% WoW. Audit reveals 2 missed posts the prior week (travel week). Action: rebuild cadence in next batch session; impressions recover to baseline within 2 weeks. No strategy change needed.
2. **Commenting-explained drop.** Engagement rate down 40% over the month of June. Audit reveals strategic commenting block was eaten by PM-job interview prep that month. Action: re-establish block; engagement rate recovers within 3 weeks.
3. **Algorithm-change drop.** Engagement down 30% across 4 consecutive weeks with cadence and commenting both held. No content-type skew. Industry reports confirm a LinkedIn algo change targeting "AI-related accounts." Route to `algorithm-change-response.md` for 2-4 week observation, then format adaptation.
4. **Multi-cause confusion (avoided).** Faced with a 25% drop, Riché could change cadence + content mix + add new format. The diagnostic prevents this: the drop was cadence-explained alone. Single-variable change, single-variable observation.

## Related entries
- `corpus/growth/diagnostics/algorithm-change-response.md` — what to do when step 4 is the cause
- `corpus/growth/metrics/engagement-quality-vs-count.md` — measurement that surfaces the drops
- `corpus/growth/metrics/leading-vs-lagging.md` — leading indicators give earlier warning
- `corpus/growth/playbook/quarterly-channel-review.md` — where systemic patterns get caught

## Anti-patterns
- Skipping the diagnostic and reaching for "let me try something new." 4-out-of-5 drops have fixable causes that don't need strategic change.
- Stacking interventions. Multiple simultaneous changes prevent learning what worked.
- Changing strategy after a single bad week. 2-week observation minimum on any non-trivial change.
- Treating engagement drops as opinion-based ("I think it's the algorithm"). Run the diagnostic; data over instinct.
