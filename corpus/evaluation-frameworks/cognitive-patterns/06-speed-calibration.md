---
name: Speed Calibration (Bezos)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md, corpus/evaluation-frameworks/cognitive-patterns/12-courage-accumulation.md, corpus/evaluation-frameworks/modes/scope-reduction.md]
---

# Speed Calibration (Bezos)

## What it is
Fast is the default. Only slow down for irreversible + high-magnitude decisions. Bezos: 70% of the information you wish you had is enough to decide. The 10x CEO knows that the cost of acting on 70% information is almost always lower than the cost of waiting for 95%, because waiting accrues hidden costs (lost momentum, competitor moves, team disengagement, opportunity decay) that don't show up in the analysis but compound brutally.

## Why it matters
Plans get over-deliberated. Every reviewer wants more confidence; every confidence requires more analysis; analysis takes time; time is the actual cost the team is paying. Without speed calibration, planning becomes the work, and the work becomes the work-around. The 10x CEO sets the cadence: most decisions get 70% deliberation; a few get 95%; the rare ones get exhaustive treatment.

## How to apply
1. Before slowing a plan, classify it (see Classification Instinct). Two-way door at modest magnitude → ship at 70% confidence. One-way door at large magnitude → escalate, generate alternatives, demand 90%+.
2. When you find yourself asking for "more analysis," ask whether the new analysis would actually change the decision. If not, decide.
3. Set a deliberation budget per decision class. "We'll spend a day on this, then ship" is a real plan. "We'll spend whatever it takes to be sure" is not.
4. Speed comes from upstream decisions (clear strategy, clear scope, clear ownership), not from heroic execution. If the plan keeps stalling, the slowness is structural.

## Examples
1. **Feature flag rollout**: 70% confidence is enough. Ship to 5% of traffic, watch metrics for a day, then ramp. The system tells you what the analysis couldn't.
2. **Pricing change for a small segment**: medium magnitude, reversible. Decide in a week, not a month. Lost weeks of revenue exceed the analysis value.
3. **Database vendor for a 5-year product**: irreversible, high magnitude. Slow down. Take the month. Generate alternatives. Write the ADR.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md` — classification IS the input to calibration
- `corpus/evaluation-frameworks/cognitive-patterns/12-courage-accumulation.md` — fast decisions build the courage to make more of them
- `corpus/evaluation-frameworks/modes/scope-reduction.md` — scope reduction often unblocks speed by removing the slow parts

## Anti-patterns
- Treating speed as bravado. Speed without classification is just gambling that looks fast.
- Mistaking analysis paralysis for thoroughness. Thoroughness ends in a decision; paralysis ends in another meeting.
