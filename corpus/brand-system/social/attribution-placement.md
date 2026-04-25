---
name: Attribution Placement
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/social/non-templated-feel.md, corpus/brand-system/identity/typography-rules.md, corpus/brand-system/identity/logo-feel.md, corpus/growth/]
---

# Attribution Placement

## What it is
Every social graphic includes Riché's name or handle subtly placed in the corner. Typically lower-right at 40–60% opacity, in JetBrains Mono at the smallest readable size for the asset. This is so when the image gets shared — pulled out of the original post, reposted, screenshotted into a thread — the attribution travels with it.

**The standard treatment:**
- Position: **lower-right corner**, with consistent margin (typically 24px from edges in 1080x1080, scaling proportionally for other ratios).
- Font: **JetBrains Mono**, weight 400, size 12–14px (at 1080x1080 export).
- Color: `#a0a0a0` at 60% opacity, or `#f5f5f5` at 40% opacity — whichever sits more quietly against the asset.
- Format: **`richezamor`** or **`@richezamor`** — short, recognizable, no full URLs.

## Why it matters
Visual content gets stripped from its post and re-shared more than text content. A diagram that goes viral without attribution earns Riché nothing. The attribution mark is small enough not to compete with the visual but legible enough that someone screenshotting the image still gets the credit signal. Over time, the recurring `richezamor` mark in the corner of every diagram becomes part of the brand recognition itself.

## How to apply
- **Always include attribution.** No social graphic ships without it. The only exception is co-branded assets where attribution is handled by the host brand's footer system.
- **Lower-right by default.** This is the standard convention; viewers' eyes already know to check there.
- **Subtle, not loud.** The mark should not compete with the diagram or the headline. Reduce opacity until it sits quietly.
- **Consistent margin.** 24px from edges at 1080x1080. Scale proportionally for other dimensions. Don't crowd the edge.
- **Match the type stack.** JetBrains Mono is the attribution font. Never script, never decorative, never the main asset's headline font.
- **No full URLs.** "richezamor.com" is too long; "richezamor" or "@richezamor" is the right size.

## Examples
1. **A 1080x1080 LinkedIn carousel slide.** Attribution: `richezamor` in JetBrains Mono 14px, `#a0a0a0` 60% opacity, lower-right with 24px margin from edges.
2. **A 1200x627 LinkedIn feed graphic.** Attribution: `@richezamor` in JetBrains Mono 12px, lower-right with 32px margin (scales with the larger canvas).
3. **A talk slide.** Attribution can be omitted from individual slides; instead, the title slide and closing slide carry the mark. Internal slides stay clean.

## Related entries
- `corpus/brand-system/social/non-templated-feel.md` — attribution is part of the crafted feel
- `corpus/brand-system/identity/typography-rules.md` — the mono font for attribution
- `corpus/brand-system/identity/logo-feel.md` — the geometric mark that can replace the text in some assets
- `corpus/growth/` — the audience-attribution loop that makes this rule pay off

## Anti-patterns
- Watermark across the entire image. Defensive, ugly, ineffective. A subtle corner mark is enough.
- Attribution as a loud branded footer ("Created by Riché Zamor • richezamor.com • Connect with me!"). Reads as templated/desperate. Keep it to the handle.
