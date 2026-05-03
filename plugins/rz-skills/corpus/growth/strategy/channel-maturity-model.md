---
name: Channel Maturity Model — Experiment → Invest → Optimize → Harvest → Cut
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 500-800
related: [corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/playbook/quarterly-channel-review.md, corpus/growth/playbook/cutting-criteria.md, corpus/growth/playbook/channel-gates-for-adding.md]
---

# Channel Maturity Model — Experiment → Invest → Optimize → Harvest → Cut

## What it is
A 5-stage lifecycle for every channel in the active set. Each stage has different goals, time allocations, success criteria, and decision triggers. The model exists so that channels are managed by stage (with stage-specific expectations) rather than treated uniformly. A 12-month-old LinkedIn channel and a 2-month-old Reddit channel both deserve attention, but for different reasons and with different metrics.

| Stage | Duration | Time allocation | Goal | Success metric | Failure exit |
|---|---|---|---|---|---|
| **Experiment** | 1–3 months | ≤15% of channel-time budget | Validate audience-channel fit; learn the platform | Measurable engagement signal (any) | If zero signal at month 3 → exit |
| **Invest** | 3–6 months | Up to 30% of channel-time budget | Build cadence + format + audience baseline | Cadence held + audience growth ≥10%/mo | If cadence breaks twice → revert to Experiment |
| **Optimize** | 6–18 months | Steady-state allocation | Refine for compounding return; lock format | Quarter-over-quarter improvement on segment metric | If no improvement 2Q → consider Harvest |
| **Harvest** | 18–36 months | Reduced; coast on existing equity | Maintain compounding return at lower marginal cost | Stable engagement at lower input | If decline >25% in 1Q → consider Cut |
| **Cut** | One-off | One quarter of wind-down | Retire cleanly; preserve owned assets | Asset archived; followers told (if applicable) | N/A |

## Why it matters
Most personal-brand failure modes come from stage-mismatch: treating an Experiment-stage channel like an Optimize-stage one (expecting too much too fast and quitting), treating a Harvest-stage channel like an Invest-stage one (over-investing on a channel that's already returned its peak value), or never explicitly cutting (channels in chronic decay drag the entire portfolio).

The model also enforces honest accounting. A channel that's been "in experiment" for 14 months is not in experiment; it's in chronic underperformance. The model forces the question.

## How to apply

**Stage assignment at the quarterly review:**
- Plot every active channel on the model. Most are obvious (LinkedIn = Optimize). Edge cases force a decision.
- Stage transitions are explicit: written down with date and rationale.
- A channel can move backward (Optimize → Invest if format is changing) but only deliberately, not through neglect.

**Stage-specific budget weights:**

For a 5.25 hr/week budget across the channel set:
- **Experiment-stage channels:** total ≤45 min/week across all such channels (no single experiment >30 min/week)
- **Invest-stage channels:** ~1–1.5 hrs/week each
- **Optimize-stage channels:** ~1.5–2.5 hrs/week each
- **Harvest-stage channels:** ≤30 min/week each (auto-routine, batch with admin block)

If the active set's allocations exceed 5.25 hrs, the model forces a decision: bump something to Harvest, or Cut something, or shrink the experiment count.

**Stage-specific metrics:**
- Experiment: engagement rate vs zero. Just "is anyone responding?"
- Invest: cadence held + audience growth rate
- Optimize: segment-specific outcomes (peer reshares, podcast invites, segment-2 followers/mo)
- Harvest: maintenance cost vs continued return
- Cut: clean exit

## Current channel state (illustrative, 2026)

| Channel | Stage | Started | Time/week | Next decision point |
|---|---|---|---|---|
| LinkedIn | Optimize | 2024 | ~2.5 hrs | Q3 2026 review: still optimizing or moving to Harvest? |
| X | Optimize | 2024 | ~1.25 hrs | Q3 2026 review: stable; defend the cadence |
| Speaking/podcasts (guesting) | Invest | 2025 | ~0.75 hrs | Q4 2026 review: candidate for Optimize stage |
| richezamor.com | Invest | 2025 | ~0.5 hrs (writing rolls into batch block) | Q1 2027 review: candidate for Optimize |
| Strategic commenting | Optimize | 2024 | ~1.75 hrs | Stable; review only on engagement collapse |
| GitHub (proposed) | Pre-Experiment | — | 30 min/week if added | Add as Experiment for 90 days |
| Reddit (proposed) | Pre-Experiment | — | 30 min/week within commenting block | Add as Experiment for 90 days |
| Newsletter | Pre-Experiment (gated) | — | 0 (deferred) | Q3 2026 gate review |
| YouTube | Pre-Experiment (gated) | — | 0 (deferred) | Q1 2027 gate review |
| Own podcast | Pre-Experiment (gated) | — | 0 (deferred) | Q1 2027+ gate review |

## Examples
1. **Stage transition (Invest → Optimize).** Speaking went from 1 talk/quarter (Invest, learning the format) to 3 talks/quarter with stable inbound pipeline. Q4 review moves to Optimize; allocation increases from 0.5 → 1 hr/week.
2. **Stage exit (Experiment → Cut).** A 90-day Mastodon experiment in 2025 produced 3 followers and zero meaningful engagement. Cut at month 3 per the model's rule. Account preserved (cleared bio, redirect to richezamor.com); 30 min/week reclaimed.
3. **Stage regression (Optimize → Invest).** LinkedIn algo change in mid-2026 broke the existing cadence's reach by 35%. Riché moves LinkedIn back to Invest stage for one quarter while testing new hook formats; then re-promotes to Optimize once the new format stabilizes.

## Related entries
- `corpus/growth/strategy/channel-evaluation-framework.md` — scoring informs stage assignment
- `corpus/growth/playbook/quarterly-channel-review.md` — where stage transitions get decided
- `corpus/growth/playbook/cutting-criteria.md` — Harvest → Cut decision rules
- `corpus/growth/playbook/channel-gates-for-adding.md` — pre-Experiment gates

## Anti-patterns
- Treating every channel as Optimize from day one. New channels need Experiment-stage tolerance for variability.
- Letting a channel sit in Experiment for >6 months. If it can't graduate to Invest, it's a Cut.
- Skipping Harvest by going Optimize → Cut directly. Most channels have a long tail of value worth maintaining at low cost before retiring.
- Promoting a channel to Optimize without sustained Invest-stage signal. Premature optimization is more damaging than slow promotion.
