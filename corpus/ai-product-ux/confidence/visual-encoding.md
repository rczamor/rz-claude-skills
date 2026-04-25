---
name: Visual Encoding (Confidence)
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 500
related: [corpus/ai-product-ux/patterns/confidence-indicators.md, corpus/ai-product-ux/confidence/textual-encoding.md, corpus/ai-product-ux/confidence/calibration-anti-patterns.md, corpus/brand-system, corpus/ai-product-ux/design-system/web-stack.md]
---

# Visual Encoding (Confidence)

## What it is
A template for visual confidence indicators using color, opacity, iconography, and weight. The job: give the user a fast, pre-attentive read on output trustworthiness before they engage with content. Visual encoding works with — never instead of — textual encoding, because color alone fails accessibility.

## Why it matters
Users skim. A scannable visual cue lets them allocate attention to outputs that warrant it and skip outputs that need verification. Without visual encoding, every AI output sits at the same weight and the user must read every word to gauge trust — exactly the cognitive tax AI was supposed to eliminate.

## How to apply
1. **Three-step scale, mapped to brand color.** Known good (Neural Architect accent green / amber for caution / muted gray for uncertain). Don't invent a five-step scale — users can't distinguish.
2. **Pair color with iconography.** Solid check, hollow check, question mark. Icons survive grayscale and color blindness.
3. **Use opacity for hedging, not for failure.** Lower opacity (~70%) signals "tentative output, treat as draft." Don't drop opacity below 50% — it reads as disabled.
4. **Reserve high-saturation accent for high-confidence outputs only.** If everything is bright, nothing is.

## Examples
1. **Context Layer Demo confidence chip.** Solid filled green pill = known good. Outlined amber pill = hedged. Gray ghost pill = uncertain. Sits next to every synthesized recommendation.
2. **Suzy Decision Engine insight cards.** A small confidence ring (filled / half-filled / empty) sits in the card header. Filled = backed by ≥150 verified consumers; empty = directional insight only.
3. **Linear's AI labels.** A small "AI" badge with subtle color shift signals "this came from the model, treat accordingly." The visual weight is intentionally lower than human-authored content.

## Related entries
- `corpus/ai-product-ux/patterns/confidence-indicators.md` — the parent pattern
- `corpus/ai-product-ux/confidence/textual-encoding.md` — the always-paired companion
- `corpus/ai-product-ux/confidence/calibration-anti-patterns.md` — how this fails
- `corpus/brand-system` — palette source for accent colors
- `corpus/ai-product-ux/design-system/web-stack.md` — Tailwind classes for the chip

## Anti-patterns
- **Color-only encoding.** Fails red/green color blindness (~8% of male users). Always pair with icon or text.
- **Inflated saturation everywhere.** When every output is bright accent, the user learns to ignore the cue.
