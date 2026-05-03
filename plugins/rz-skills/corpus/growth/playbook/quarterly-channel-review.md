---
name: Quarterly Channel Review — The 60-Minute Process
domain: growth
source_skill: growth-marketing
entry_type: template
length_target: 400-700
related: [corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/strategy/channel-maturity-model.md, corpus/growth/playbook/channel-gates-for-adding.md, corpus/growth/playbook/cutting-criteria.md, corpus/growth/metrics/channel-roi-calculation.md, corpus/growth/metrics/quarterly-review-checklist.md]
---

# Quarterly Channel Review — The 60-Minute Process

## What it is
The structured 60-minute end-of-quarter review where every active channel gets re-evaluated, every deferred channel gets gate-checked, and the next quarter's channel allocation gets locked. Bound to 60 minutes by design; longer reviews drift into rumination, shorter reviews skip critical decisions. Runs the first Sunday of January, April, July, and October.

## Why it matters
Without a structured review cadence, channel decisions happen reactively — adding when something looks promising, cutting when something looks broken, never with a comparative view across the full set. The 60-minute quarterly cadence forces explicit decisions: this quarter's channels stay or go, this quarter's deferred candidates advance or wait, this quarter's allocation gets locked.

The 60-minute bound is not arbitrary. Most operators either skip the review (no structure) or do it at 4-hour depth (turns into ruminative re-strategizing). 60 minutes is enough to apply the framework, score every channel, make the decisions, and document them — without becoming a meta-task that swallows other work.

## The 60-minute structure

| Block | Time | Activity |
|---|---|---|
| 1 | 10 min | Pull data: per-channel ROI, segment outcomes, follower growth, time invested |
| 2 | 10 min | Re-score every active channel via `channel-evaluation-framework.md` |
| 3 | 10 min | Check each active channel's stage per `channel-maturity-model.md`; note any transitions |
| 4 | 10 min | Gate-check each deferred channel per `channel-gates-for-adding.md` |
| 5 | 10 min | Make decisions: keep/grow/reduce/cut active; launch/defer candidates; allocate next quarter's hours |
| 6 | 10 min | Document in the quarterly review notes; update Notion if applicable; close |

## Block 1 — Data pull (10 min)

Pull from existing sources (don't recompute):
- LinkedIn analytics: per-post engagement rate trend, follower growth, peer comments
- HubSpot: Segment 1 inbound count, Segment 4 invitations, hire-relevant signals
- Google Analytics: richezamor.com traffic, signups, traffic sources
- Notion: published /thinking article count, podcast appearances, speaking engagements
- Calendar audit: estimate hours invested per channel (approximate is fine)

Compute (rough):
- ROI per channel per `corpus/growth/metrics/channel-roi-calculation.md`
- Cadence held / missed (posts per channel per week)
- Quarter-over-quarter trend on each metric

Output: a one-page summary table.

## Block 2 — Active channel scoring (10 min)

Re-score every active channel via `corpus/growth/strategy/channel-evaluation-framework.md`. Note score changes from last quarter:
- ↑↑ (≥2 points improvement): strong signal; consider increasing investment
- → (within ±1 point): stable; maintain
- ↓↓ (≥2 points decline): investigate; may indicate stage transition or cutting evaluation

Don't agonize over scoring — the comparison to last quarter matters more than absolute precision.

## Block 3 — Stage check (10 min)

For each active channel, confirm the stage per `corpus/growth/strategy/channel-maturity-model.md`:
- Experiment → Invest: graduation if 90-day signal is positive
- Invest → Optimize: graduation if cadence held + audience growth ≥10%/mo
- Optimize → Harvest: demotion if no improvement 2 consecutive quarters
- Harvest → Cut: demotion if decline >25% in one quarter

Stage transitions are documented with date and rationale.

## Block 4 — Deferred candidate gate check (10 min)

For each deferred channel (newsletter, YouTube, podcast hosting, etc.):
- Run the channel's specific gates per `corpus/growth/playbook/channel-gates-for-adding.md`
- All gates open → candidate is launchable next quarter (see Block 5)
- Some gates open → note progress; check next quarter
- All gates closed → defer; note any conditions changed

## Block 5 — Decisions (10 min)

The decisions block produces 4 outputs:

**Active channel decisions:**
- Channels to GROW (increase time allocation): note the new allocation
- Channels to MAINTAIN (current allocation): default state
- Channels to REDUCE (decrease time allocation): note the new allocation
- Channels to CUT (retire): trigger `corpus/growth/playbook/cutting-criteria.md` evaluation if not already done

**Candidate channel decisions:**
- Channels to LAUNCH next quarter (with funded cut from active set per `no-channel-sprawl.md`)
- Channels to DEFER (revisit next quarter)

**Quarterly priorities:**
- The 1-3 highest-leverage things to do this quarter (e.g., "increase /thinking article cadence to 1/week," "ship newsletter Issue 1 if gates clear")

**Time allocation lock:**
- Total ≤5.25 hr/week
- Per-channel breakdown
- Buffer (~15 min/week) for ad-hoc opportunities

## Block 6 — Documentation (10 min)

Write into the quarterly review notes (in Notion or the file system):
- The data pull summary
- Score changes per channel (with directional indicator)
- Stage transitions (with date and rationale)
- Gate progress per deferred channel
- Decisions made
- Next-quarter allocation
- 1-3 priorities

Tag the note with the quarter and the date. The trail matters; pattern recognition over 4-8 quarters informs strategic decisions.

## Examples
1. **Standard quarterly review.** Q3 2026 review (early October). Active channels: LinkedIn (score 13, stable, Optimize), X (score 11, stable, Optimize), Speaking (score 14, ↑, Invest→Optimize transition), richezamor.com (score 11, ↑, Invest), Reddit (score 10, ↑, Experiment month 3, graduating to Invest). Deferred: Newsletter (3-of-4 gates open, ≥1,500 followers reached this quarter — launching Q4), YouTube (1-of-4, defer), Podcast hosting (1-of-4, defer). Decision: launch newsletter Q4; cut: drop 30 min/week from X to fund. Total 65 min.
2. **Stage demotion.** Q2 2026 review. LinkedIn engagement rate has declined for 2 quarters; score dropped from 13 → 10. Stage demotion: Optimize → Invest. Action: pivot the next quarter to format-experimentation per `algorithm-change-response.md`; re-evaluate next quarter for Optimize re-promotion.
3. **Deferred candidate progress.** Q1 2026 review. Newsletter gates last quarter were 1-of-4. This quarter: 2-of-4 (LinkedIn followers approaching threshold; podcast invites still below). Note progress; defer to Q2 review. The progress trend itself is the signal.

## Related entries
- `corpus/growth/strategy/channel-evaluation-framework.md` — Block 2 scoring
- `corpus/growth/strategy/channel-maturity-model.md` — Block 3 stage check
- `corpus/growth/playbook/channel-gates-for-adding.md` — Block 4 gate check
- `corpus/growth/playbook/cutting-criteria.md` — Block 5 cut decisions
- `corpus/growth/metrics/channel-roi-calculation.md` — Block 1 ROI methodology
- `corpus/growth/metrics/quarterly-review-checklist.md` — broader quarterly checklist this nests under

## Anti-patterns
- Letting the review run to 4 hours. Becomes ruminative; doesn't produce better decisions.
- Skipping the data pull "because I roughly know the numbers." The data is what makes the review objective; gut estimates produce same-as-last-quarter decisions.
- Treating the review as optional. Skipped reviews → channel sprawl, allocation drift, no quarterly course corrections.
- Deferring decisions past the review. The review IS the decision moment; deferring decisions to "after I think about it more" usually means the decision doesn't get made.
