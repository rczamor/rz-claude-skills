---
name: Algorithm Change Response — Observe, Don't Panic-Pivot
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 400-700
related: [corpus/growth/diagnostics/engagement-drop-diagnostic.md, corpus/growth/diagnostics/deplatforming-prep.md, corpus/growth/strategy/owned-vs-rented-channels.md, corpus/growth/strategy/channel-maturity-model.md]
---

# Algorithm Change Response — Observe, Don't Panic-Pivot

## What it is
The protocol when a rented platform (LinkedIn, X, YouTube) materially changes its algorithm and engagement on the channel drops as a result. The protocol is: do NOT immediately overhaul strategy. Observe for 2-4 weeks while holding existing discipline; identify what specifically changed; adjust hooks and formats (small surface), not strategy (deep surface). Most algorithm changes are partially-reversible within 6-12 weeks and most over-reactions to algo changes damage the brand more than the change itself.

## Why it matters
Platform algorithms change frequently. LinkedIn made meaningful changes in 2024 (de-ranking external links), 2024–2025 (down-weighting AI-tagged content), and 2025 (re-prioritizing comments-as-signal). X has made multiple changes since 2022. YouTube updates its recommendation algo continuously.

Each change generates a wave of "the algorithm killed me" creator content suggesting strategic pivots. Most of those pivots are wrong because:

1. **Algo changes often partially reverse.** A 6-week-old change has often been tuned by the platform team after creator backlash. Reactive strategy shifts get locked in just as the algo is being unwound.
2. **Algo changes affect different formats differently.** A change that hurts hot-take posts might not hurt long-form articles. Wholesale strategy changes miss this nuance.
3. **The audience hasn't changed.** The creator's actual audience is still there; the platform's surfacing has changed. Strategy that responds to the audience (segments, voice, narrative) was right before the change and remains right after.

For Riché's brand specifically, the audience-strategy (4 segments, Segment 2 primary, practitioner-first voice, Context Layer thesis) is durable across algo changes. What changes is *how to reach that audience on this platform this quarter* — a tactical problem, not a strategic one.

## How to apply

**Phase 1 — Confirm and characterize (week 1):**

1. **Confirm it's an algo change, not a different cause.** Run `corpus/growth/diagnostics/engagement-drop-diagnostic.md` first. If the drop has a cadence/commenting/mix explanation, fix that — don't blame the algo.
2. **Read 3 industry sources** (Social Media Examiner, Lenny's Newsletter, the platform's official creator blog). Confirm a change has been documented and characterize it specifically: what kind of content is affected, what's not.
3. **Document the baseline.** Note this week's metrics across: impressions, engagement rate, peer comments, follower growth. These become the reference for measuring recovery.

**Phase 2 — Hold discipline + observe (weeks 2-4):**

Do NOT make strategic changes during this phase. Specifically:
- Maintain cadence
- Maintain commenting block
- Maintain content type mix
- Continue narrative discipline
- Don't add new channels in reaction
- Don't drop existing channels in reaction

DO permit small tactical experiments:
- Try one alternative hook format on 1 of 5 weekly posts
- Test a different posting time on 1 post per week
- Vary post length (shorter vs longer) on a small subset

The point: small, isolated, reversible experiments to learn how the changed algo treats different formats. NOT strategic overhauls.

**Phase 3 — Identify and adapt (week 5+):**

After 2-4 weeks of observation, patterns should emerge:
- Some formats recovered to or near baseline → keep them
- Some formats stayed depressed → reduce or refactor them
- New formats outperformed prior baseline → adopt deliberately

Adopt the learnings into the standard cadence. Update `corpus/growth/channels/{channel}.md` if the channel-specific tactics need updating.

**Phase 4 — Re-evaluate stage (quarterly review):**

If the algo change was severe (>40% sustained drop after 3 months of adaptation), re-evaluate the channel's stage in `corpus/growth/strategy/channel-maturity-model.md`. A channel previously at Optimize may need to drop to Invest stage temporarily; in extreme cases, it moves to Harvest as the brand pivots emphasis to other channels.

## Specific guardrails during algo-change response

- **Don't add new channels in months 1-3.** New-channel cost compounds the disruption; the ROI on any new channel is harder to read against the disrupted baseline. Add channels later, after the affected channel stabilizes.
- **Don't change voice in response to algo changes.** Voice is durable; algos are tactical. A voice change in response to algo change is the worst possible reaction.
- **Don't blame the algo publicly.** Posts complaining about the algorithm signal frustration; they don't reach the audience anyway (algorithms de-prioritize platform-criticism). Take the loss; adapt quietly.
- **Document what changed and what worked.** Log the algo-change event, the response, the recovery (or lack of it) in the quarterly review notes. Pattern recognition over multiple events compounds.

## Examples
1. **2024 LinkedIn external-link change (well-handled).** LinkedIn de-ranked posts with external links in late 2024. Riché's response: held cadence, observed 4 weeks, noticed link-free posts recovered while link-included posts stayed depressed. Adapted: moved external links from post-body to first-comment. Recovery within 6 weeks.
2. **2025 hypothetical AI-content de-ranking.** Suppose LinkedIn de-ranks posts that mention "AI" in early 2025. Riché's hypothetical response: holds discipline, observes 3 weeks, notices framework posts (without "AI" in title) recover faster than AI-named posts. Adapts: leads posts with the specific concept (RAG, context layer, agent memory) instead of generic "AI" framing. Recovery within 8 weeks.
3. **Failed pivot (avoided).** Faced with an early 2025 drop, a peer creator pivoted from LinkedIn to YouTube as primary channel within 3 weeks. The LinkedIn drop turned out to be partially reversed by month 4; the YouTube pivot wasted 6 months of investment. Riché's discipline avoided this.

## Related entries
- `corpus/growth/diagnostics/engagement-drop-diagnostic.md` — run this first to confirm cause
- `corpus/growth/diagnostics/deplatforming-prep.md` — for the worst case (channel becomes unviable)
- `corpus/growth/strategy/owned-vs-rented-channels.md` — why owned channels matter as algo-change insurance
- `corpus/growth/strategy/channel-maturity-model.md` — stage re-evaluation if recovery fails

## Anti-patterns
- Pivoting strategy in week 1 of an observed algo change. Pre-mature; under-informed; usually wrong.
- Changing voice or narrative in response to algo. The platform's algo doesn't see voice/narrative; only formats and signals.
- Public algo-blaming posts. Frustration broadcast; doesn't reach audience; signals weak operator.
- Stacking responses (new channel + format change + cadence change all at once). Prevents learning what worked.
