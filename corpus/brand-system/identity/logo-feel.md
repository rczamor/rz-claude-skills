---
name: Logo Feel
domain: brand-system
source_skill: graphic-design
entry_type: concept
length_target: 300-800
related: [corpus/brand-system/identity/neural-architect-overview.md, corpus/brand-system/identity/typography-rules.md, corpus/brand-system/identity/imagery-style.md, corpus/brand-system/implementation/svg-for-diagrams.md]
---

# Logo Feel

## What it is
When any branded mark is needed — a favicon, a section badge, a watermark, an avatar — it should feel like an IDE icon or a developer-tool logo. Geometric, monochromatic or single-accent, comfortable next to a VS Code icon or a GitHub mark. Never a wordmark in a script font, never a glossy logotype, never an abstract "swoosh."

**The reference set:** the icons of GitHub, Vercel, Linear, Raycast, Anthropic. Spare, geometric, recognizable at 16x16. That is the visual neighborhood the Neural Architect identity lives in.

## Why it matters
A wordmark or logo is a compressed signal of the entire brand. If the favicon looks like a personal-coach logo, every page on richezamor.com inherits "personal coach." If the favicon looks like a developer tool, every page inherits "this is built by an operator." Marks live in tabs, in app docks, in slide footers — places where they're seen at small sizes and quickly. The IDE-icon feel is what makes a tiny mark still read as practitioner.

## How to apply
- **Geometric over typographic.** Prefer a geometric mark (a single-letter monogram, a structural shape) over a wordmark. If the mark must include text, use the monospace stack at the smallest weight that holds.
- **Monochromatic by default.** White on dark, or dark on white. The accent color appears in marks only at large sizes, never at favicon scale.
- **Recognizable at 16x16.** The mark must hold its silhouette at favicon size. No internal detail that disappears below 24px.
- **No glossy treatment.** No drop shadows, no gradients, no inner glow, no chrome. The mark is flat or has a single 1.5px stroke.

## Examples
1. **Favicon for richezamor.com.** A geometric monogram in white on `#0a0a0a`, 32x32 base, holds at 16x16. Sits comfortably next to the GitHub tab icon.
2. **Section badge in a slide deck.** A small geometric mark in the lower-right corner at 60% opacity, white on dark, no embellishment.
3. **Avatar on social platforms.** Same monogram in white on `#0a0a0a` background, square crop, no decorative ring or border.

## Related entries
- `corpus/brand-system/identity/neural-architect-overview.md` — the persona the mark is signaling
- `corpus/brand-system/identity/typography-rules.md` — type rules that govern any wordmark
- `corpus/brand-system/identity/imagery-style.md` — geometric vocabulary the mark draws from
- `corpus/brand-system/implementation/svg-for-diagrams.md` — how to render the mark cleanly

## Anti-patterns
- A handwritten signature mark for "personality." Signatures collapse to noise at favicon size and signal lifestyle brand.
- A glossy three-color emblem with a tagline ribbon. The brand neighborhood is dev tools, not corporate insurance.
