---
name: Channel Gates for Adding — The Readiness Criteria
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 400-700
related: [corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/strategy/channel-maturity-model.md, corpus/growth/playbook/cutting-criteria.md, corpus/growth/anti-patterns/no-channel-sprawl.md, corpus/growth/playbook/quarterly-channel-review.md]
---

# Channel Gates for Adding — The Readiness Criteria

## What it is
The pre-conditions that must all be true before a candidate channel is added to the active set. Distinct from the channel-evaluation-framework (which scores fit) and the channel-maturity-model (which manages lifecycle). Gates are binary: all true → channel is launchable; any false → defer until conditions change. Prevents "the score looks good, let's add it" decisions from triggering channel sprawl.

## Why it matters
A channel can score well on the evaluation framework AND still be the wrong channel to launch right now. Examples:
- A newsletter scoring 13 (strong) but with no LinkedIn audience baseline to seed it → launches to 50 subs and stagnates
- A YouTube channel scoring 12 (good) but with no recording setup → produces amateur-quality first videos that damage the practitioner positioning
- A podcast scoring 11 (acceptable) but without a 6-episode buffer → cancellations break the cadence in month 2

Gates exist because *good fit* is necessary but not sufficient. The launch conditions also have to be right.

## Channel-specific gates

The gates below cover the major candidate channels Riché has evaluated. Each channel has channel-specific gates because the launch conditions differ.

### Newsletter (Substack/Beehiiv/Kit)
All four must be true:
1. LinkedIn followers ≥1,500
2. Inbound podcast/speaking invites ≥3/month for 2 consecutive months
3. ≥12 published /thinking articles on richezamor.com (source library for repurposing)
4. A monthly cadence Riché can hold for 6 months (calendar capacity test)

### YouTube
All four must be true:
1. ≥3 talks delivered with usable recordings (seed library)
2. ≥10 /thinking articles published
3. Clean recording setup (camera, mic, OBS) at practitioner-peer quality
4. 6-month commitment to monthly cadence with calendar buffer

### Own podcast (hosting)
All four must be true:
1. ≥10 podcast guesting appearances completed (network seed)
2. LinkedIn followers ≥5,000 (host credibility threshold for booking guests)
3. Newsletter launched with ≥1,000 subs (cross-promotion channel for episodes)
4. Differentiated angle locked, not generic

### Show HN (one-shot, not recurring)
All five must be true:
1. Runnable artifact exists (working code, working demo)
2. README quickstart runs in <60 seconds
3. Riché has 6+ hours blocked across the 48 hours after launch
4. HN account ≥1 month old with substantive comment history
5. Launch window is Tuesday or Wednesday morning Pacific (or wait)

### GitHub as distribution channel
All three must be true:
1. The channel doesn't require new content production (artifacts derive from existing /thinking + Helm Labs work)
2. ≤30 min/week in time cost (low-cost addition, no cut required if true)
3. Existing repos meet quality bar (READMEs, working quickstarts) before launching the public profile push

### Reddit niche engagement
All three must be true:
1. Time fits inside existing strategic-commenting block (no new budget required)
2. HN-style account ≥1 month with karma >100 from substantive comments on others' posts
3. 5-of-10 link-discipline ratio committed to (not >2 self-links per 10 substantive comments)

### Bluesky / Mastodon / other emerging social
All three must be true:
1. Documented Segment 2 density on the platform (not just "people are talking about it")
2. The platform is ≥2 years old and has a stable user base (avoid platforms in their first 18 months)
3. A clear cut to fund the addition (per `corpus/growth/anti-patterns/no-channel-sprawl.md`)

### TikTok / Reels / Shorts
**Permanent gate:** Segment 2 density on the platform must exceed 25% before re-evaluation. As of 2026, this is not close to true. Default: do not launch. See `corpus/growth/anti-patterns/no-tiktok-reels.md`.

## Why specific gates beat generic gates

A generic "is there audience there?" gate fails because the answer is almost always "yes, some." Specific gates ask "is there *enough* audience there to compound, AND can the operator sustain the channel-specific cadence requirements, AND is the production quality bar met?"

For each channel, the gates target the specific failure modes most common to that channel. Newsletter dies on small initial list size; YouTube dies on inconsistent cadence; podcast hosting dies on cancellations without buffer. The gates address these specifically.

## How to apply

**At quarterly review, evaluate every deferred channel against its gates:**
- Are all gates closed (deferred)?
- Are some open (closer than last quarter)?
- Are all open (ready to launch)?

If all gates are open AND a cut can be funded (per `no-channel-sprawl.md`), the channel becomes a Q+1 launch candidate. Document the launch decision in the quarterly review notes.

**During the quarter, do NOT relitigate gates.** Gates are set during the quarterly review and held; mid-quarter "let's just try it" decisions undermine the gate discipline.

**Gate evolution:** the gates themselves can be adjusted, but only deliberately during quarterly review and only with a documented reason. Drifting gates downward to enable a launch is a known failure mode.

## Examples
1. **Deferred newsletter (Q2 2026 review).** LinkedIn followers at 1,180 (gate fails). Inbound invites at 2/month for the past 2 months (gate fails). 9 articles published (gate fails). Calendar capacity OK (gate passes). 1-of-4 → defer. Re-evaluate Q3.
2. **GitHub addition approved (Q3 2026 review).** All 3 gates pass; existing /thinking articles already include code (READMEs need polish but the source material exists); ≤30 min/week fits inside the existing batch session. Approved for Q4 launch as Experiment-stage channel.
3. **Show HN opportunistic launch.** Riché has a working agent-memory eval suite ready Tuesday morning. All 5 gates pass. Launch window. Activate immediately.
4. **Bluesky declined (Q3 2026 review).** Platform exists; some PMs migrating; Segment 2 density not yet documented. 2-of-3 gates open. Defer; revisit Q1 2027.

## Related entries
- `corpus/growth/strategy/channel-evaluation-framework.md` — fit scoring (different from gates)
- `corpus/growth/strategy/channel-maturity-model.md` — what stage a launched channel enters
- `corpus/growth/playbook/cutting-criteria.md` — the inverse for retiring channels
- `corpus/growth/anti-patterns/no-channel-sprawl.md` — every gate-passing channel still needs a cut
- `corpus/growth/playbook/quarterly-channel-review.md` — where gates get evaluated

## Anti-patterns
- Drifting gates downward to enable a desired launch. Defeats the purpose of gates entirely.
- Skipping gates "because the framework score is high." Gates and scores serve different purposes.
- Launching when most gates pass but one fails. The gates are AND, not OR.
- Re-evaluating gates mid-quarter on impulse. Quarterly review is the cadence; mid-quarter changes are allowed only on emergency conditions.
