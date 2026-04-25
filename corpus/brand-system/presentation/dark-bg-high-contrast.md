---
name: Dark Background, High Contrast
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/identity/color-palette.md, corpus/brand-system/identity/palette.yaml, corpus/brand-system/identity/neural-architect-overview.md, corpus/ux-principles/]
---

# Dark Background, High Contrast

## What it is
Slide backgrounds default to the Neural Architect dark palette: `#0a0a0a` to `#1a1a1a`. Text is `#f5f5f5` (high-contrast white). Secondary metadata uses `#a0a0a0`. The dark-on-light convention used in most corporate decks is explicitly avoided.

## Why it matters
Two reasons. First, brand consistency: a deck that matches the palette of richezamor.com, the LinkedIn graphics, and the website hero is one cohesive system — the audience sees the same visual identity from feed to talk to follow-up. Second, projection physics: dark backgrounds with high-contrast text project better in conference rooms with mixed lighting. White slides bloom and wash out; dark slides hold their contrast. Code snippets — a frequent slide element — also read better on dark backgrounds because the syntax-highlight palette is calibrated for dark.

## How to apply
- **Default background: `#1a1a1a`.** The slightly lifted near-black is easier on eyes than `#0a0a0a` for full slides; reserve `#0a0a0a` for hero/title slides.
- **Headline text: `#f5f5f5`.** Don't use pure white — too glaring at projection scale.
- **Secondary text: `#a0a0a0`.** Use for slide numbers, attribution, eyebrow labels — never for body or headlines.
- **Single accent per deck.** Pick one accent (electric blue, emerald, or amber) at the start of the deck and hold it across every slide.
- **Test in the actual room.** If possible, project the deck before the talk. Adjust accent saturation if the projector washes out cool colors.

## Examples
1. **Title slide.** `#0a0a0a` background, talk title in Inter Bold 64pt `#f5f5f5`, framework name in JetBrains Mono 18pt `#a0a0a0` below. Single accent on a small geometric mark in the lower-right corner.
2. **Body slide with diagram.** `#1a1a1a` background, diagram rendered in `#f5f5f5` strokes with one electric-blue accent node, slide number in `#a0a0a0` lower-right.
3. **Section break slide.** `#0a0a0a` background, single section title in Inter SemiBold 80pt centered, no other elements.

## Related entries
- `corpus/brand-system/identity/color-palette.md` — the full palette spec
- `corpus/brand-system/identity/palette.yaml` — machine-readable values
- `corpus/brand-system/identity/neural-architect-overview.md` — why dark is the brand default
- `corpus/ux-principles/` — accessibility and contrast standards

## Anti-patterns
- Switching to white backgrounds "for the section about positive metrics." Brand consistency outweighs section theming. Use accent color for sentiment, not the entire background.
- Pure black (`#000000`) backgrounds that crush projection. The slight offset to `#0a0a0a` reads as intentional and projects cleaner.
