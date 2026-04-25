---
name: Kano Model
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/thinkers/kano-noriaki.md, corpus/pm-frameworks/prioritization/kano-prioritization.md, corpus/pm-frameworks/discovery/jobs-to-be-done.md]
---

# Kano Model

## What it is

Noriaki Kano's 1984 framework for classifying product features by the relationship between feature presence and customer satisfaction. Five categories:

- **Must-be (Basic):** Expected. Absence causes dissatisfaction; presence is taken for granted. (Hotel: hot water.)
- **One-dimensional (Performance):** Linear. More is better; less is worse. (Laptop: battery life.)
- **Attractive (Delighter):** Asymmetric. Absence is fine; presence delights. (Free upgrade at hotel check-in.)
- **Indifferent:** Customer doesn't care.
- **Reverse:** Customer prefers absence.

Determined empirically through a paired-question survey: how do you feel if the feature is present? How do you feel if it's absent?

From Kano, Seraku, Takahashi, Tsuji, "Attractive Quality and Must-Be Quality" (1984).

## Why it matters

Treating all features as if they're on the same satisfaction curve is the McNamara fallacy applied to discovery. Must-bes can't differentiate (every competitor has them); delighters can't carry a product alone (without must-bes, the product is broken). The model also captures temporal drift: today's delighter becomes tomorrow's must-be — Wi-Fi at hotels in 2005 was a delighter; in 2025 its absence triggers complaints.

For AI products, Kano explains why "AI features" stop delighting fast. ChatGPT-style summarization was a delighter in 2023; by 2025 it's a must-be in any analytics tool. The drift compresses on AI-product timescales.

## How to apply

1. **Run a Kano survey** with paired functional/dysfunctional questions for each candidate feature. (e.g. "If product had X, how would you feel?" / "If product didn't have X, how would you feel?")
2. **Tabulate responses** into the five categories using Kano's response matrix.
3. **Sequence the roadmap:** must-bes first (table stakes), one-dimensionals as core differentiation, delighters as competitive bets. Do not invest in indifferent or reverse categories.
4. **Re-run quarterly.** Categories drift. A feature that was attractive last year may now be must-be.

## Examples

1. **Suzy Decision Engine onboarding.** Survey of 40 enterprise analysts revealed "AI-recommended studies" as attractive (delighter) but "results in under 24 hours" as must-be. The roadmap led with reliable speed (must-be) before investing in recommendation quality (delighter).
2. **B2B SaaS auth.** SSO is a must-be in mid-market; absence loses deals. SSO presence wins zero deals on its own.

## Related entries

- `corpus/pm-frameworks/thinkers/kano-noriaki.md` — Kano's broader contribution
- `corpus/pm-frameworks/prioritization/kano-prioritization.md` — using Kano for sequencing
- `corpus/pm-frameworks/discovery/jobs-to-be-done.md` — JTBD identifies the job; Kano classifies the features that satisfy it

## Anti-patterns

- **Skipping must-bes for delighters.** Teams chase the differentiating feature while ignoring the boring expectations that determine table-stakes credibility. Delighters atop broken must-bes don't compute.
- **Treating Kano as static.** Categorizing once and treating it as permanent. The category drift is the second-most useful thing the model gives you, after the categorization itself.
