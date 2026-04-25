---
name: Calibration Anti-patterns (Confidence)
domain: ai-product-ux
source_skill: product-design
entry_type: rule
length_target: 500
related: [corpus/ai-product-ux/patterns/confidence-indicators.md, corpus/ai-product-ux/confidence/visual-encoding.md, corpus/ai-product-ux/confidence/textual-encoding.md, corpus/pm-frameworks/ai-product-pm/evals-framework.md, corpus/pm-frameworks/ai-product-pm/non-determinism.md]
---

# Calibration Anti-patterns (Confidence)

## What it is
A rule. Don't pretend AI is always right. Users notice and trust drops faster than it can be rebuilt. Calibration is the discipline of matching displayed confidence to measured accuracy — and the anti-patterns are the systematic ways teams break it.

## Why it matters
A "high-confidence" badge that is right 99% of the time is a feature. The same badge right 70% of the time is a defect that destroys the product's credibility. Once a user catches a confidently-wrong output, every subsequent confident output gets discounted — even the ones that are right. Miscalibration is one-way damage; you cannot reset the trust meter on the same user.

## How to apply
1. **Tie display to measured precision.** "High confidence" means precision ≥ X% on eval. If you can't measure it, you can't display it.
2. **Re-run eval after every model swap or prompt change.** Calibration drifts. Yesterday's high-confidence threshold may be today's hedge.
3. **Surface the threshold, not just the chip.** "High confidence (97% precision on eval set)" beats "High confidence" alone. Buyers notice the difference.
4. **Drop the chip when sample is too small.** If you've never tested this category, say "untested" — not "high confidence by analogy."

## Examples
1. **Context Layer Demo's confidence is tied to retrieval consistency.** A green chip means three or more independent sources agree; amber means partial; gray means inconsistent. The display is a function of measured agreement, not a vibe.
2. **Suzy Decision Engine's panel-size threshold.** Insight cards switch from confident to directional language at n<150. The threshold came from eval data, not designer intuition.

## Related entries
- `corpus/ai-product-ux/patterns/confidence-indicators.md` — parent pattern
- `corpus/ai-product-ux/confidence/visual-encoding.md` — what gets miscalibrated
- `corpus/ai-product-ux/confidence/textual-encoding.md` — the language version
- `corpus/pm-frameworks/ai-product-pm/evals-framework.md` — the PM-side discipline
- `corpus/pm-frameworks/ai-product-pm/non-determinism.md` — why this is non-trivial

## Anti-patterns (the ones to avoid)
- **Confidence theater.** Displaying confidence chips with no eval backing them. Users assume they mean something; they don't; trust collapses.
- **Static thresholds.** Setting "high = 90%" once and never re-measuring. Model updates silently shift the actual precision.
- **Performative humility.** "AI may make mistakes" boilerplate on every output. It's neither a real hedge nor a useful disclaimer — it's noise.
- **Confidence inflation under pressure.** When sales pushes for "make it sound more confident," the calibration discipline dies. Hold the line.
