---
name: Channel Evaluation Framework — The 5-Criteria Score
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 500-800
related: [corpus/growth/strategy/channel-maturity-model.md, corpus/growth/strategy/owned-vs-rented-channels.md, corpus/growth/playbook/channel-gates-for-adding.md, corpus/growth/anti-patterns/no-channel-sprawl.md, corpus/growth/playbook/quarterly-channel-review.md]
---

# Channel Evaluation Framework — The 5-Criteria Score

## What it is
A scoring rubric for evaluating any candidate channel before adoption (and any active channel during quarterly review). Five criteria, each scored 0–3, total possible 15. Used to convert "should we add X?" questions from gut-feel debates into explicit comparisons.

| Criterion | What it measures | Scoring |
|---|---|---|
| **Audience overlap** | Density of the 4 segments on this channel | 0 = none / 1 = mostly other audiences / 2 = meaningful presence / 3 = primary surface for ≥1 segment |
| **Time efficiency** | Time required vs reach produced, against 5.25 hr/week ceiling | 0 = breaks the budget / 1 = barely fits with cuts / 2 = fits comfortably / 3 = high reach per hour |
| **Repurposing fit** | Reuses existing content (LinkedIn, articles, talks) vs requires new production | 0 = all new / 1 = some adaptation / 2 = mostly derivatives / 3 = pure derivative channel |
| **Discovery + compounding** | Whether content compounds via search/algorithmic surfacing or dies on publish | 0 = fully ephemeral / 1 = short tail / 2 = multi-month tail / 3 = multi-year compounding |
| **Flywheel contribution** | Feeds peer reshare, segment-2 recognition, speaker pitches, podcast invites | 0 = isolated / 1 = weak fuel / 2 = solid fuel / 3 = primary flywheel ignition |

**Decision rules:**
- **Total ≥12:** strong candidate; pursue if a cut can be funded (per `corpus/growth/anti-patterns/no-channel-sprawl.md`)
- **Total 9–11:** marginal; defer until conditions improve or another channel weakens
- **Total ≤8:** decline. Document the score and the rejection reason; revisit in 6–12 months only on changed conditions
- **Any criterion at 0:** automatic decline regardless of total. A 0 means structural misfit no aggregation can compensate for.

## Why it matters
The default reasoning pattern for new channels is "this looks promising; let's try it." That reasoning loses the comparison: how does the new channel compare to the existing channels' opportunity cost? The framework forces an apples-to-apples score. If LinkedIn scores 14 (current) and Newsletter would score 13 at launch, the comparison is meaningful: Newsletter is a strong candidate but doesn't out-rank LinkedIn, which clarifies that adding it requires a cut, not a free addition.

The framework also defends against two common failure modes:
1. **Overweighting novelty.** New channels feel exciting; the framework keeps existing channels' compounding value visible.
2. **Underweighting opportunity cost.** Time spent on a 9-scoring new channel is time not spent on a 14-scoring existing one. The score makes the trade explicit.

## How to apply

**For a new channel candidate:**
1. Score the candidate channel honestly (don't inflate scores to justify a desire).
2. Score the *cut* required (the channel or activity that would be retired or downgraded). Often the new channel scores lower than what's already there.
3. Compare totals. Net change must be positive AND meaningful (≥2 points).
4. Document the score in the quarterly review log; revisit in 90 days post-launch to validate the projected score.

**For an active channel at quarterly review:**
1. Re-score every active channel with current data.
2. Channels that have dropped ≥3 points since last quarter trigger a `corpus/growth/playbook/cutting-criteria.md` evaluation.
3. Channels at score 13–15 are candidates to *increase* investment (within budget).

## Worked examples (current state, hypothetical 2026)

| Channel | Audience | Time | Repurpose | Discovery | Flywheel | Total | Status |
|---|---|---|---|---|---|---|---|
| LinkedIn (active) | 3 | 3 | 2 | 2 | 3 | **13** | Optimize |
| X (active) | 2 | 3 | 3 | 1 | 2 | **11** | Optimize |
| Speaking/podcasts (active) | 3 | 2 | 2 | 3 | 3 | **13** | Invest |
| richezamor.com (active) | 2 | 1 | 2 | 3 | 2 | **10** | Invest |
| Newsletter (candidate) | 2 | 2 | 2 | 2 | 2 | **10** | Defer (gates) |
| YouTube (candidate) | 2 | 1 | 2 | 3 | 2 | **10** | Defer (gates) |
| GitHub (proposed) | 2 | 3 | 3 | 3 | 2 | **13** | Add (low time cost) |
| Reddit (proposed) | 2 | 2 | 2 | 3 | 1 | **10** | Add cautiously (within commenting block) |
| Show HN (one-shot) | 3 | 2 | 3 | 3 | 3 | **14** | Use opportunistically |
| Own podcast (candidate) | 2 | 0 | 1 | 2 | 3 | **8** | Decline; gates not close |
| TikTok | 0 | 0 | 1 | 2 | 0 | **3** | Decline (auto: criterion 0s) |

The scoring is illustrative, not authoritative — re-score each channel during quarterly review with actual current data.

## Examples
1. **Add decision (GitHub).** Scored 13 with no fund-a-cut requirement (low time cost, fits inside existing /thinking article workflow). Adopted in next quarter.
2. **Defer decision (newsletter).** Scored 10 today; projected to score 13 once gates clear (Q3 2026). Deferred until launch gates met.
3. **Decline decision (TikTok).** Two 0s and a 3 total. Document the rejection; don't revisit unless segment composition shifts.

## Related entries
- `corpus/growth/strategy/channel-maturity-model.md` — what stage each scored channel sits in
- `corpus/growth/strategy/owned-vs-rented-channels.md` — applies a multiplier on owned channels
- `corpus/growth/playbook/channel-gates-for-adding.md` — gates run alongside scoring
- `corpus/growth/anti-patterns/no-channel-sprawl.md` — why scoring matters
- `corpus/growth/playbook/quarterly-channel-review.md` — the review where scoring is re-run

## Anti-patterns
- Scoring to justify a pre-decided answer. The framework is only useful if the score can change the decision.
- Aggregating without checking the 0-criterion rule. A 0 in audience or time efficiency makes the channel structurally infeasible.
- Skipping the cut-required score. The new-channel score in isolation is incomplete; the comparison to what gets cut is the actual decision.
