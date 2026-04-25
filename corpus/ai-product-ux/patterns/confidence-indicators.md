---
name: Confidence Indicators
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 700
related: [corpus/ai-product-ux/confidence/visual-encoding.md, corpus/ai-product-ux/confidence/textual-encoding.md, corpus/ai-product-ux/confidence/calibration-anti-patterns.md, corpus/ai-product-ux/patterns/reasoning-transparency.md, corpus/pm-frameworks/ai-product-pm/evals-framework.md]
---

# Confidence Indicators

## What it is
Confidence indicators signal whether an AI output is high-confidence, hedged, or uncertain. The signal can be visual (color, opacity, iconography) or textual (qualifying language: "I'm confident...", "This is uncertain...", "Verify before acting..."). The job of the indicator is to give the user a fast read on how much trust to extend, before they read the substance of the output.

## Why it matters
AI systems produce output at a uniform visual weight. A confident answer and a wild guess look identical on the page. Without confidence indicators, users either (a) trust everything equally and get burned, or (b) distrust everything equally and stop using the product. Indicators preserve the upside of high-confidence outputs while protecting users from low-confidence ones. This is the calibration layer between model probabilities and user action.

## How to apply
1. **Map model signal to a small, fixed scale.** Three levels — known good, hedged, uncertain — covers most cases. More levels overwhelm.
2. **Pair visual and textual encoding.** Color alone fails accessibility; text alone fails scannability. Use both.
3. **Calibrate against eval data.** A "high-confidence" indicator that is wrong 30% of the time is worse than no indicator. Tie display to measured precision/recall.
4. **Never inflate confidence.** If the model is uncertain, say so. Users notice when "high confidence" outputs miss; trust collapses faster than it builds.

## Examples
1. **Context Layer Demo confidence chips.** Each synthesized recommendation in the demo carries a chip: green ("known good — three independent sources agree"), amber ("hedged — partial evidence"), or gray ("uncertain — verify"). The chip color maps to whether the underlying context passed the five-step quality bar.
2. **Suzy Decision Engine readout.** Insights surface to enterprise users with confidence framing tied to sample size and consistency across the research panel — buyers need to know the difference between an insight backed by 200 verified consumers and one extrapolated from 8.
3. **Linear's AI features hedge in language** — "I think this is a P1, but verify" — rather than asserting. The hedge is the indicator.

## Related entries
- `corpus/ai-product-ux/confidence/visual-encoding.md` — color, opacity, icon templates
- `corpus/ai-product-ux/confidence/textual-encoding.md` — qualifying language templates
- `corpus/ai-product-ux/confidence/calibration-anti-patterns.md` — how teams break this
- `corpus/ai-product-ux/patterns/reasoning-transparency.md` — confidence + reasoning calibrate trust together
- `corpus/pm-frameworks/ai-product-pm/evals-framework.md` — the PM-side discipline that makes confidence indicators honest

## Anti-patterns
- **Performative humility.** Slapping "AI may be wrong" on every output is noise. Indicators must vary with actual model signal, or they teach users to ignore them.
- **Hidden confidence.** Some products compute confidence internally but never surface it to the user. The user is left to guess. Surface it or stop computing it.
