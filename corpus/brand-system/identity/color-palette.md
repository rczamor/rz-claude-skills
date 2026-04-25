---
name: Color Palette
domain: brand-system
source_skill: graphic-design
entry_type: resource
length_target: 300-800
related: [corpus/brand-system/identity/palette.yaml, corpus/brand-system/identity/accent-colors.md, corpus/brand-system/identity/color-anti-patterns.md, corpus/brand-system/identity/neural-architect-overview.md, corpus/ux-principles/]
---

# Color Palette

## What it is
The base color system for every Riché visual asset. Three layers: backgrounds in the near-black range, secondary surfaces in dark gray, and a high-contrast text pair (white + muted gray). This palette is intentionally narrow so the accent color (chosen per project) carries all the visual energy.

**Concrete values:**
- Primary backgrounds: `#0a0a0a` to `#1a1a1a` (near-black, slightly off pure black so it doesn't crush)
- Secondary backgrounds: `#2a2a2a` (cards, panels, lifted surfaces)
- Primary text: `#f5f5f5` (high-contrast white, slightly off pure white to reduce glare)
- Secondary text: `#a0a0a0` (muted gray for captions, metadata, deprioritized labels)

## Why it matters
A consistent dark palette does three jobs: it signals "technical practitioner" before any text is read, it provides high contrast for diagrams (the white nodes pop against near-black), and it removes a category of decisions every time a new asset is made. The narrow range also makes the single accent color land — on a near-black field, a single electric-blue node reads as the answer.

## How to apply
- **Pick a background per asset.** `#0a0a0a` for hero/full-bleed surfaces, `#1a1a1a` for slide bodies, `#2a2a2a` for cards layered on top.
- **Keep text contrast above 7:1.** `#f5f5f5` on `#0a0a0a` clears WCAG AAA. `#a0a0a0` on `#1a1a1a` is for secondary metadata only — never body copy.
- **Never use pure black or pure white.** `#000000` crushes shadows and looks cheap; `#ffffff` glares on screens. The slight offset reads as intentional and easier on the eyes.
- **Layer surfaces by lightening, not by adding borders.** A `#2a2a2a` card on a `#1a1a1a` background needs no border — the value step does the separation.

## Examples
1. **LinkedIn diagram graphic.** `#0a0a0a` canvas, `#2a2a2a` containers for each of the five stages, `#f5f5f5` stage labels, `#a0a0a0` micro-captions under each label.
2. **Conference slide.** `#1a1a1a` background, `#f5f5f5` headline, single accent color on the focus element, `#a0a0a0` slide number in the corner.
3. **richezamor.com card.** `#0a0a0a` page background, `#2a2a2a` card, `#f5f5f5` heading, `#a0a0a0` body copy and metadata.

## Related entries
- `corpus/brand-system/identity/palette.yaml` — same values in machine-readable form
- `corpus/brand-system/identity/accent-colors.md` — the per-project accent rule
- `corpus/brand-system/identity/color-anti-patterns.md` — what never appears in this palette
- `corpus/ux-principles/` — accessibility and contrast rules that this palette is calibrated against

## Anti-patterns
- Using `#000000` and `#ffffff` because "dark mode means black and white." The off-black/off-white pair is the deliberate choice.
- Adding a fourth gray shade because a designer wanted "more depth." Three values handle every layering need; a fourth muddies the system.
