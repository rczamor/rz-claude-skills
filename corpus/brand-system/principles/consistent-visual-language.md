---
name: Consistent Visual Language
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 400-600
related: [corpus/brand-system/principles/medium-determines-spec.md, corpus/brand-system/identity/neural-architect-overview.md, corpus/brand-system/identity/palette.yaml, corpus/brand-system/identity/typography-rules.md, corpus/brand-system/identity/imagery-style.md]
---

# Consistent Visual Language

## What it is
Across every output — slide deck, LinkedIn graphic, website page, email signature, blog inline diagram, conference one-sheet — the same colors, the same type scale, and the same spacing rhythm appear. The medium changes; the visual language doesn't. A viewer should recognize a Riché asset by its visual fingerprint before reading any label.

The five elements that stay consistent:

1. **Color palette** — `#0a0a0a–#1a1a1a` backgrounds, `#2a2a2a` cards, `#f5f5f5` text, `#a0a0a0` secondary, one accent per project.
2. **Type stack** — Inter (sans) and JetBrains Mono (mono); no third font.
3. **Type scale** — proportional sizes within each medium, but consistent ratios (e.g., headline is always ~3x body size).
4. **Spacing rhythm** — multiples of 4 or 8 (4, 8, 16, 24, 32, 48, 64) for all margins and gaps.
5. **Geometric vocabulary** — rectangles with 4–8px corner radius, consistent stroke widths, node-and-edge structures.

## Why it matters
Brand recognition compounds when every asset reinforces the same visual fingerprint. Each post, slide, and page becomes a deposit into the same recognition account. The opposite — assets that share content but vary the visual language — creates a feed where every post looks like it came from a different person. Consistency is the cheapest possible investment in brand equity: it doesn't require new assets, just discipline about reusing the same building blocks.

The rule also protects against decision fatigue. With a fixed palette, a fixed type stack, and a fixed spacing system, the only decisions per asset are about content and composition — never about base aesthetics. That's how a single person ships polished visuals at the volume Riché's content cadence demands.

## How to apply
- **Maintain a shared design token file.** Palette, fonts, spacing scale, corner radii — defined once, referenced everywhere. Tailwind config, CSS variables, or a shared design system file.
- **Audit new assets against the system.** Before shipping a graphic, hold it next to three existing on-brand assets. Does it look like family? If not, identify what drifted (color? type? spacing? geometry?) and fix.
- **Reuse components, not just guidelines.** A "card" component is not just "a rectangle with rounded corners" — it's a specific React or Figma component that ships with the right padding, typography, and color baked in. Reuse the component.
- **Resist medium-specific drift.** When a slide deck "needs more energy," don't add gradients. When a blog post "needs visual interest," don't add stock illustration. The energy and interest come from content density and diagram structure — not from breaking the visual language.
- **Cross-link the canonical references.** When in doubt, the references are: `palette.yaml` for color, `typography-rules.md` for fonts, `imagery-style.md` for vocabulary, `corner-treatment.md` for radius.

## Examples
1. **A LinkedIn post, a slide in next month's keynote, and the new website hero all use the same Five-Step Context Flow diagram** rendered at three different sizes. The colors match, the stage labels are typeset identically, the corner radius is consistent. Same family.
2. **The speaker one-sheet PDF, the conference badge, and the email signature all use the same geometric monogram.** Different sizes, same mark. Same neighborhood.
3. **A talk deck and a blog post use the same accent color (electric blue) on the same load-bearing element (the Synthesis stage).** The talk's visual argument and the blog's visual argument are clearly the same argument.

## Related entries
- `corpus/brand-system/principles/medium-determines-spec.md` — the sibling principle that handles per-medium variation
- `corpus/brand-system/identity/neural-architect-overview.md` — the persona the visual language encodes
- `corpus/brand-system/identity/palette.yaml` — the canonical color/type values
- `corpus/brand-system/identity/typography-rules.md` — the type stack
- `corpus/brand-system/identity/imagery-style.md` — the geometric vocabulary

## Anti-patterns
- "Brand consistency" interpreted as "every asset is identical." Identical isn't consistent — it's monotonous. Consistent means same building blocks, varied composition.
- Drifting the palette "for a single campaign." The campaign ends; the visual confusion persists. Stay in the system.
