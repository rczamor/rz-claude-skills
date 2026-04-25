---
name: Mobile Thumbnail Readability
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/social/aspect-ratios.md, corpus/brand-system/social/non-templated-feel.md, corpus/brand-system/identity/typography-rules.md, corpus/brand-system/social/diagrams-over-abstract.md]
---

# Mobile Thumbnail Readability

## What it is
Every social graphic must be readable at 375px width — the standard mobile thumbnail. Text that disappears or blurs at that size is functionally invisible on the platform where the majority of feed views happen. This rule overrides aesthetic preference for dense layouts.

## Why it matters
Most LinkedIn and X views happen on mobile. A graphic that looks elegant on a desktop preview but loses its labels at 375px wastes the post — the audience scrolls past because there's nothing readable to anchor on. Designing for mobile-first reading isn't a constraint, it's the platform reality.

## How to apply
- **Test at 375px.** Before exporting, scale the asset to 375px wide on screen and confirm every label is readable. If anything goes muddy, redesign.
- **Minimum readable text size: 14px at 375px width.** That translates to ~32px in a 1080x1080 export, ~25px in a 1200x627 export. Anything smaller is decorative — it cannot be the primary label.
- **Limit on-graphic text to 5–7 short lines.** More than that and individual lines get squeezed.
- **Headline first, supporting text second.** The largest text on the graphic should carry the message alone. Supporting text adds nuance for the audience that zooms in.
- **No body paragraphs on graphics.** Long prose doesn't survive thumbnail compression. If the post needs prose, put it in the caption, not the image.

## Examples
1. **Strong: a 1080x1080 carousel slide with the headline "Data is not context." in Inter Bold 72pt and a single supporting line in Inter Medium 28pt below.** Both readable at 375px scale.
2. **Strong: a 1200x627 diagram with stage labels in Inter Medium 32pt.** Each label readable in the feed preview.
3. **Weak: a 1080x1080 slide with a 4-paragraph quote rendered at 18pt.** Unreadable at 375px — looks like gray noise.

## Related entries
- `corpus/brand-system/social/aspect-ratios.md` — the canvases mobile readability applies to
- `corpus/brand-system/social/non-templated-feel.md` — sibling rule on visual quality
- `corpus/brand-system/identity/typography-rules.md` — the type stack and weights that hold up at small sizes
- `corpus/brand-system/social/diagrams-over-abstract.md` — diagrams that pass the readability test by design

## Anti-patterns
- "It's readable if you tap to expand." Most viewers don't tap. Design for the scroll-past view.
- Cramming all the supporting evidence into one image because "the algorithm prefers single posts." If the evidence doesn't fit, split into a carousel.
