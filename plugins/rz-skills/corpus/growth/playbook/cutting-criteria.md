---
name: Cutting Criteria — When to Retire a Channel
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 400-700
related: [corpus/growth/strategy/channel-maturity-model.md, corpus/growth/playbook/quarterly-channel-review.md, corpus/growth/playbook/channel-gates-for-adding.md, corpus/growth/anti-patterns/no-channel-sprawl.md, corpus/growth/metrics/channel-roi-calculation.md]
---

# Cutting Criteria — When to Retire a Channel

## What it is
The framework for deciding when an active channel should be retired (cut) rather than continued. Distinct from temporary reduction (an active channel at lower allocation) or stage demotion (Optimize → Harvest at lower investment). Cutting is a permanent decision: the channel goes from active set to retired, with archival of any owned assets and a clean wind-down. Cutting is rare and deliberate; most operators avoid it too long because cuts feel like loss.

## Why it matters
Channels in chronic decay drag the entire portfolio. They consume time (even at minimum allocation), they consume attention (mental overhead of "is this channel working?"), and they prevent the funded-cut requirement from `corpus/growth/anti-patterns/no-channel-sprawl.md` from cleanly enabling new channel additions. Failing to cut is the most common reason operators end up with 6 channels they're each running at 60% effectiveness rather than 3 channels at 95%.

The cutting decision is psychologically hard because:
- The channel may have been formative (LinkedIn for any creator built there)
- The audience on the channel feels "real" even when the engagement isn't
- Sunk cost fallacy on time already invested
- "What if it recovers?" hopes

The criteria below override these psychological pulls with explicit conditions. If the criteria fire, cut.

## The 3-criteria rule

A channel becomes a cut candidate when ALL THREE are true:

1. **ROI below threshold for 2 consecutive quarters.** Specifically: ROI per `corpus/growth/metrics/channel-roi-calculation.md` is below the active-set median for 2 consecutive quarters. One bad quarter is noise; two is a signal.

2. **Audience overlap with the 4 segments shrinking or stagnant.** Either the channel's audience density on the target segments is declining (composition shifting away from Segment 2/3/4) OR audience growth has been <2%/quarter for 2 consecutive quarters. A static audience with declining engagement is a dying channel.

3. **Opportunity cost > continuing cost.** Specifically: there is a credible alternative channel (deferred candidate or expansion of an existing channel) that would produce greater outcomes per hour than this channel does. If no alternative exists, hold the channel at minimum allocation rather than cut it.

If all three are true, the channel is a cut candidate at the quarterly review. The actual cut decision still requires deliberate action (Block 5 of `corpus/growth/playbook/quarterly-channel-review.md`); a candidate isn't auto-cut.

## Why all three must be true

- ROI alone: a temporarily-low ROI channel may recover (algo change, format experimentation in progress). Don't cut on ROI alone.
- Audience overlap alone: a healthy audience with declining engagement might be a fix-the-format problem, not a cut.
- Opportunity cost alone: cutting without a replacement plan reduces total reach without offsetting gain.

The combination of all three indicates the channel has structural problems (not tactical), in a stable-or-declining audience condition, with a credible alternative use of the freed time. That combination is when cutting is right.

## The cut process (when criteria fire)

**Step 1 — Confirmation review (15 min):**
Re-check the criteria with fresh data. Verify all three are still true. Sometimes the quarterly snapshot is misleading; a careful re-check catches false positives.

**Step 2 — Wind-down plan (15 min):**
- Archive owned assets (downloadable content, list backups)
- Identify any in-progress commitments (scheduled posts, planned threads); decide to honor or cancel
- Write a brief "moving on" note for the channel if appropriate (LinkedIn newsletter announcement, X bio update)
- Plan the time reallocation: where does the freed budget go?

**Step 3 — Wind-down execution (over 2-4 weeks):**
- Stop new content production immediately
- Honor in-progress commitments (don't burn relationships)
- Update profile/bio to redirect followers to remaining channels
- Maintain account but mark as inactive (don't delete; archived accounts preserve any future option)

**Step 4 — Documentation (10 min):**
- Document the cut in the quarterly review notes with full reasoning
- Note the freed time allocation
- Set a 12-month "would we revisit?" check (rarely yes, but worth tracking)

## What's NOT a reason to cut

- A single bad quarter (noise, not signal)
- An algorithm change in progress (let it settle per `corpus/growth/diagnostics/algorithm-change-response.md`)
- Frustration with a specific recent piece's performance (one-off, not pattern)
- Peer suggestions that "you should focus on X instead" without ROI/audience evidence
- Wanting to add a new channel and looking for what to cut (cut for the right reasons; the new channel still needs its own gate-passing)

## Cut vs Harvest distinction

A channel doesn't have to be cut to free meaningful time. The Harvest stage (`corpus/growth/strategy/channel-maturity-model.md`) lets a channel coast at ≤30 min/week, preserving the asset and audience without active investment. Harvest is often the right intermediate decision before cutting:

- ROI declining but audience still strong → Harvest (preserve the audience asset)
- Audience declining but ROI still acceptable → Harvest (let it produce while it lasts)
- Both declining + alternative exists → Cut

Most cuts should pass through Harvest first for at least one quarter. Direct Optimize → Cut transitions are unusual and usually indicate a major external event (deplatforming, acquisition).

## Examples
1. **Hypothetical cut decision.** A 2025 Mastodon experiment runs for 3 quarters: ROI consistently below median, audience growth flat at ~30 followers/quarter, no Segment 2 density emerging. Alternative (deeper Reddit engagement) has clearer fit. All 3 criteria met. Cut decision in Q4 2025 review; account preserved with bio redirect.
2. **Cut deferred to Harvest.** Hypothetical X channel review in Q3 2026: ROI below median for 2 consecutive quarters, audience growing slowly. The criteria don't all fire (audience hasn't declined). Decision: move from Optimize to Harvest stage, reduce to 30 min/week, re-evaluate in Q1 2027. Half the cost, most of the asset preservation.
3. **Cut avoided (criteria failed).** A bad quarter on Speaking due to one canceled event prompts cut consideration. Re-check: 1-of-3 criteria (the ROI dip is one quarter, not two; audience strong; opportunity cost not clearly higher). Don't cut; hold and observe Q2 review.

## Related entries
- `corpus/growth/strategy/channel-maturity-model.md` — Cut is the final stage
- `corpus/growth/playbook/quarterly-channel-review.md` — where cut decisions get made
- `corpus/growth/playbook/channel-gates-for-adding.md` — the inverse for additions
- `corpus/growth/anti-patterns/no-channel-sprawl.md` — cuts fund additions
- `corpus/growth/metrics/channel-roi-calculation.md` — Criterion 1 measurement

## Anti-patterns
- Cutting on impulse after a bad week. The criteria require multi-quarter evidence; impulse cuts get reversed and damage the discipline.
- Refusing to cut because "we worked hard on it." Sunk cost; doesn't justify ongoing cost.
- Cutting without an alternative use of the freed time. The freed time gets re-absorbed by other things; net portfolio quality doesn't improve.
- Skipping the wind-down process and just stopping. Leaves loose ends (orphan accounts, broken commitments) that produce brand cost over time.
