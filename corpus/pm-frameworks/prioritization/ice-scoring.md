---
name: ICE Scoring
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/prioritization/rice-scoring.md, corpus/pm-frameworks/thinkers/ellis-sean.md, corpus/pm-frameworks/prioritization/impact-confidence-ease-matrix.md]
---

# ICE Scoring

## What it is

A three-factor rapid-prioritization formula popularized by Sean Ellis (GrowthHackers, *Hacking Growth*) for ranking growth experiments and product initiatives:

**ICE = (Impact × Confidence × Ease) / 3**

- **Impact:** how big the effect on the target metric will be if the experiment succeeds (1–10).
- **Confidence:** how confident the team is that the experiment will succeed (1–10).
- **Ease:** how easy the experiment is to run (1–10, higher = easier).

The result is a single 1–10 score for fast comparison. Designed to be shouted at the start of a 10-minute growth meeting and produce a defensible queue.

## Why it matters

ICE trades RICE's precision for speed. It's optimized for high-volume experiment cultures (growth teams running 10+ tests per week) where the cost of slow prioritization exceeds the cost of an imperfect rank. The simplification is intentional: when you're choosing the next experiment for next sprint, you don't need person-month effort estimates — you need a quick gut check that all team members can score in 90 seconds.

Best used in tight-loop experimentation. Less useful for major initiatives where Reach and Effort precision matter (use RICE).

For AI products, ICE works well for prompt-experiment, eval-rubric, and onboarding-funnel prioritization — high-volume, fast-cycle work — and breaks down for context-architecture or model-selection decisions, which need richer analysis.

## How to apply

1. **List candidate experiments.** Keep the list to 5–15; longer lists slow the meeting.
2. **Score each on I, C, E** (1–10 per factor). Time-box: 60 seconds per experiment.
3. **Calculate** the average and rank. The top 3–5 go into the next sprint.
4. **Re-rank weekly.** ICE is not a one-time exercise; the queue is dynamic.
5. **Track outcomes** to calibrate: were the I/C/E scores accurate against actuals? Re-tune the team's intuition over time.

## Examples

1. **Riché Helm Labs growth experiments (pre-launch).** Cold outbound to 50 PE-backed CFOs: I=8 (large pipeline impact), C=7 (intro path tested), E=6 (warm-intro coordination). Score: 7.0. Vs. paid LinkedIn ads: I=4, C=3, E=8. Score: 5.0. Outbound clearly wins; the framework confirms the obvious in 90 seconds and unblocks execution.
2. **Cargo-cult ICE.** Scoring 10/10/10 on every experiment because the team is excited. The rubric stops being useful; the queue becomes whatever was suggested most recently.

## Related entries

- `corpus/pm-frameworks/prioritization/rice-scoring.md` — higher-precision variant
- `corpus/pm-frameworks/thinkers/ellis-sean.md` — Ellis' broader growth-hacking practice
- `corpus/pm-frameworks/prioritization/impact-confidence-ease-matrix.md` — visual variant

## Anti-patterns

- **Score inflation.** Default 10s on everything. If every experiment scores 9+, the rubric isn't differentiating; the queue defaults to LIFO.
- **Treating ICE as binding.** ICE is a fast filter, not a contract. The team should still apply judgment when the top-ranked experiment is obviously wrong (high score because of a scoring error, not because it's actually best).
