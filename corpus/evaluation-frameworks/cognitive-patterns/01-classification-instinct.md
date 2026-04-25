---
name: Classification Instinct (Bezos)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/06-speed-calibration.md, corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md, corpus/evaluation-frameworks/modes/scope-reduction.md]
---

# Classification Instinct (Bezos)

## What it is
Categorize every decision by reversibility x magnitude. Bezos called this the one-way door vs. two-way door distinction. A two-way door decision can be unwound — you walk through, look around, and walk back if it's wrong. A one-way door cannot — once you ship it, the cost of reversal is high or terminal. Most decisions are two-way doors and should be made fast. The few that are one-way deserve heavyweight deliberation.

## Why it matters
Without this instinct, teams treat every decision with the same gravity, which produces two failure modes: (1) trivial choices stall in committees because they feel important; (2) load-bearing choices get rubber-stamped because the team is exhausted from over-deliberating the trivial ones. Classifying first lets you spend deliberation budget where it actually matters. The 10x CEO instinctively asks "what kind of door is this?" before debating the answer.

## How to apply
1. Before discussing any decision, ask: "If we ship this and it's wrong, what does it cost to undo?"
2. If the answer is "a few hours of work" or "a flag flip" — it is a two-way door. Decide in this meeting. Move.
3. If the answer is "we eat the architecture for years" or "the migration is irreversible" — it is a one-way door. Slow down, gather more signal, generate alternatives, escalate.
4. Beware false one-way doors: most things people frame as irreversible are actually reversible at modest cost. Push back on the framing.

## Examples
1. **Two-way door**: feature flag a new onboarding flow, watch the metrics for a week, roll back if it underperforms. Decide in 20 minutes.
2. **One-way door**: pick a primary database vendor for a new product. Migration cost is months of engineering. Demand alternatives, write an ADR, escalate.
3. **False one-way door**: "we have to lock in this pricing model forever." Almost always reversible — you can grandfather customers and migrate. Don't let pricing freeze you.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/06-speed-calibration.md` — speed calibration is the operational consequence of classification
- `corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md` — Section 10 explicitly asks "rate reversibility 1-5"
- `corpus/evaluation-frameworks/modes/scope-reduction.md` — scope reduction is often the right move on two-way doors disguised as one-way

## Anti-patterns
- Treating reversible product launches like irreversible architecture decisions, padding them with months of pre-launch deliberation that the market signal would have answered in two weeks.
- Treating database choices, API contracts, or schema decisions as two-way doors because "we can always migrate later" — these are usually one-way doors and the migration cost is real.
