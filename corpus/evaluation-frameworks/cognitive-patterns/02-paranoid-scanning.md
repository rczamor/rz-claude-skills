---
name: Paranoid Scanning (Grove)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md, corpus/evaluation-frameworks/review-sections/03-security-threat-model.md, corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md]
---

# Paranoid Scanning (Grove)

## What it is
Continuously scan for strategic inflection points, cultural drift, talent erosion, and process-as-proxy disease. Andy Grove's "Only the paranoid survive" wasn't pessimism — it was a discipline. The CEO who scans for the small signals (a key engineer's energy dropping, a competitor's hire, a process meeting that is no longer about the work) catches structural problems while they are still cheap to fix. The CEO who waits for the dashboard to turn red catches them when they are catastrophic.

## How it shows up in plan review
On a plan review, paranoid scanning means looking past the stated scope to ask: what is shifting underneath this plan that the plan itself doesn't address? Is this plan drifting toward process worship — adding layers and meetings without changing outcomes? Is the plan evidence of a hire who's no longer aligned? Is the proposed metric a signal of "we've stopped knowing why we're building this"?

## Why it matters
Plans that pass a happy-path review can still be failing the company. The 10x CEO reads a plan for what it betrays about the underlying organism — confidence, focus, hunger, drift. Paranoid scanning is the muscle that turns a technical review into a leadership instrument.

## How to apply
1. Before reviewing the plan's content, ask: "What does the existence of this plan tell me about the team that wrote it?"
2. Look for: scope creep that's actually a hedge, abstractions that smell like resume-driven design, tests deferred without protest (sign of low ownership), retries on integrations that should have been removed.
3. Probe drift: "Is this plan doing what we said our strategy was 6 months ago, or is it doing something subtly different that nobody has named out loud?"
4. Check talent signal: who is writing this? Is it the person who should be writing it, or the person who has the slot open?

## Examples
1. **Process-as-proxy**: a plan that adds a "review meeting" for every deploy. The plan doesn't reduce incidents — it performs reduction. Flag.
2. **Drift signal**: a roadmap plan that lists 12 items, none of which are the thing the team said was its top priority last quarter. Surface the gap.
3. **Talent signal**: a junior engineer assigned the architecture decision because seniors are too busy. The plan is not the problem — the staffing is.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md` — paranoid scanning generates the inputs inversion uses
- `corpus/evaluation-frameworks/review-sections/03-security-threat-model.md` — Section 3 is paranoid scanning made explicit for security
- `corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md` — drift questions live in Section 10

## Anti-patterns
- Performing paranoia by listing every theoretical risk without weighting any of them. Paranoia is signal-detection, not catastrophizing.
- Confusing trust with attention. Trusting the team does not mean skipping the scan — it means scanning faster.
