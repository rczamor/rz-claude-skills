---
name: Channel ROI Calculation — Hours In, Segment Outcomes Out
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 400-700
related: [corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/playbook/budget-allocation.md, corpus/growth/playbook/quarterly-channel-review.md, corpus/growth/metrics/anti-vanity-metrics.md, corpus/growth/metrics/segment-proxies-rollup.md]
---

# Channel ROI Calculation — Hours In, Segment Outcomes Out

## What it is
The methodology for computing a comparable ROI score per channel, given the 5.25 hr/week budget. ROI = segment-outcomes produced per hour invested. Used in `corpus/growth/playbook/quarterly-channel-review.md` to compare channels objectively and decide allocation. Distinct from raw vanity metrics (followers, impressions) — ROI tracks outcomes that move the brand forward, not signals that flatter the operator.

## Why it matters
Without an ROI calculation, channel allocation decisions are gut-feel. Gut-feel decisions over-allocate to channels that *feel* productive (high posting cadence, lots of comments) and under-allocate to channels that *are* productive (fewer touchpoints, but each one moves the brand forward). The 5.25 hr ceiling makes this acute: every hour misallocated to a low-ROI channel is an hour not invested in a high-ROI one.

ROI calculation also defends against algo-driven optimization. A channel may produce huge impressions but few segment outcomes (LinkedIn viral posts that reach broad audiences but no Segment 2). Or vice versa: a channel may produce modest impressions but high segment-outcome density (a HN front-page post reaches Segment 3 founders directly). ROI normalizes these.

## The ROI formula

ROI per channel per quarter = (Weighted segment outcomes for the quarter) ÷ (Hours invested in the quarter)

**Weighted segment outcomes:**

| Outcome | Weight | What counts |
|---|---|---|
| **Segment 1 touchpoint** (hiring manager DM, email, intro) | 5 | Inbound contact from VP/CPO-level person at AI-PM target company |
| **Segment 2 reshare or quote** | 3 | Public reshare, quote-tweet, or LinkedIn-share by a Segment 2 peer |
| **Segment 4 invitation** | 4 | Speaking, podcast, or event invitation |
| **Segment 3 inbound** | 2 | DM/email from a Founder (Seed-Series B) |
| **Newsletter signup** | 1 | Email captured to the holding list |
| **/thinking article-driven traffic** | 0.5 per 100 visits | Traffic to richezamor.com from this channel |
| **Direct hire-relevant signal** | 10 | Recruiter contact, role offer, or hiring-process advancement |

**Time investment includes:**
- All publishing time (drafting, batch sessions, derivative production)
- All engagement time (commenting, DMs)
- All admin/analytics time attributable to the channel

Cross-channel time (e.g., a Sunday batch session that produces content for both LinkedIn and X) gets allocated proportionally to the time spent on each channel's output.

## Example calculation (illustrative)

Hypothetical Q2 2026 numbers:

| Channel | Hours | S1 (×5) | S2 reshare (×3) | S4 invite (×4) | S3 inbound (×2) | Signups (×1) | Hire signal (×10) | Total outcomes | ROI |
|---|---|---|---|---|---|---|---|---|---|
| LinkedIn | ~32 | 1 | 28 | 2 | 4 | 12 | 0 | 5+84+8+8+12 = 117 | 3.66/hr |
| LinkedIn comments | ~22 | 0 | 14 | 1 | 2 | 3 | 0 | 0+42+4+4+3 = 53 | 2.41/hr |
| X | ~16 | 0 | 4 | 0 | 6 | 4 | 0 | 0+12+0+12+4 = 28 | 1.75/hr |
| Speaking (1 talk) | ~8 | 1 | 6 | 3 | 1 | 8 | 0 | 5+18+12+2+8 = 45 | 5.63/hr |
| /thinking articles | ~12 | 0 | 4 | 1 | 1 | 18 | 0 | 0+12+4+2+18 = 36 | 3.00/hr |

Read against this: speaking is the highest-ROI channel for Riché; LinkedIn comments are middling but absolute-volume large; X is the lowest. Conclusion: protect the speaking allocation; don't reduce LinkedIn comments (the volume matters); consider whether X allocation can be tightened.

## How to apply

**Quarterly process (~30 min):**

1. Pull the prior quarter's outcome data from HubSpot (Segment 1, Segment 4 inbound), LinkedIn analytics (Segment 2 reshare counts), Notion logs (newsletter signups, podcast invites), Google Analytics (article traffic by source).
2. Pull time investment from calendar blocks + manual estimates for unscheduled work.
3. Apply the formula per channel. Compute ROI/hr for each.
4. Compare quarter-over-quarter:
   - ROI improving? → channel is healthy at current allocation
   - ROI declining? → investigate; may need format adaptation or stage transition
   - ROI consistently high? → consider increasing allocation (within 5.25 budget)
   - ROI consistently low? → use `corpus/growth/playbook/cutting-criteria.md` evaluation
5. Document the calculation in the quarterly review notes; trend across quarters informs the channel maturity model.

## Edge cases and adjustments

- **One-shot channels** (Show HN launches): compute as a one-off ROI; don't average across quarters.
- **Compounding-tail channels** (richezamor.com articles continue to produce traffic and signups months after publishing): credit the originating quarter for outcomes generated in that quarter; outcomes in later quarters credit the quarter they occurred (the channel keeps earning).
- **Lottery-ticket outcomes** (a single Segment 1 contact worth a 50-point spike): note these but don't let one-off spikes drive ongoing allocation. Look at trend across 2-3 quarters.
- **Time investment underestimated**: most operators undercount engagement and admin time. Pad time estimates by 15% if uncertain.

## Related entries
- `corpus/growth/strategy/channel-evaluation-framework.md` — the 5-criteria scoring is qualitative; ROI is quantitative; both feed allocation decisions
- `corpus/growth/playbook/budget-allocation.md` — the 5.25 hr ceiling that ROI defends
- `corpus/growth/playbook/quarterly-channel-review.md` — where ROI gets used
- `corpus/growth/metrics/anti-vanity-metrics.md` — explicitly rejects metrics this calculation excludes
- `corpus/growth/metrics/segment-proxies-rollup.md` — how segment outcomes get measured

## Anti-patterns
- Including impressions or follower count in the ROI numerator. These are vanity metrics; they don't move the brand toward outcomes.
- Computing ROI weekly. Too much variance; quarterly is the right cadence for stability.
- Cutting a channel based on one bad quarter. ROI is multi-quarter signal; one quarter is noise.
- Inflating outcome weights to justify a preferred allocation. Weights are set in advance and held; revising them post-hoc invalidates the comparison.
