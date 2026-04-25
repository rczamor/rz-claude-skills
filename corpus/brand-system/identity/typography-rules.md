---
name: Typography Rules
domain: brand-system
source_skill: graphic-design
entry_type: resource
length_target: 300-800
related: [corpus/brand-system/identity/palette.yaml, corpus/brand-system/identity/neural-architect-overview.md, corpus/brand-system/presentation/minimal-text-max-impact.md, corpus/brand-system/social/mobile-thumbnail-readability.md, corpus/ux-principles/]
---

# Typography Rules

## What it is
A two-font system: a clean modern sans-serif (Inter, system-ui fallbacks) for body text and headlines, and a monospace (JetBrains Mono, Fira Code) for technical elements — code snippets, framework names, stage labels in diagrams, structured data callouts. No third font ever enters the system. Script and decorative fonts are categorically banned.

**The full stack:**
- **Body / headline sans-serif:** `Inter`, with `system-ui`, `-apple-system`, `Segoe UI`, `Roboto` as fallbacks.
- **Technical monospace:** `JetBrains Mono`, with `Fira Code`, `Menlo`, `Consolas` as fallbacks.
- **Blacklist:** script fonts, hand-drawn fonts, decorative serifs, slab serifs with personality, anything with novelty ligatures used as branding.

## Why it matters
The two-font pairing is the verbal counterpart to the visual identity: clean sans for general legibility, monospace for "this is a system / this is code." A single sans-monospace pair makes every asset look like it came out of an IDE or a technical doc — which is exactly the practitioner signal. Adding a third font (a serif for "warmth," a script for "personality") collapses that signal into a generic content-creator template.

## How to apply
- **Inter for everything legible.** Headlines, body, slide text, social copy. Weights: 400 for body, 500 for emphasis, 600 for headlines, 700 sparingly for hero text.
- **Mono for technical anchors.** Stage labels in diagrams, framework names ("Five-Step Context Flow"), code snippets, terminal output, structured key/value pairs.
- **Large sizes for projection, dense sizes for diagrams.** Slide headlines at 48–64pt; diagram labels at 14–18pt. Never go below 14px in a social asset that needs to be readable on mobile.
- **Never script, never decorative.** No "handwritten" fonts for personality, no slab serifs as a "brand differentiator." The two-font system is the differentiator.

## Examples
1. **Conference talk title slide.** Inter Bold 64pt headline, JetBrains Mono 24pt framework subtitle ("CONTEXT QUALITY FRAMEWORK"), no third font.
2. **LinkedIn diagram with five stage labels.** Inter Medium 16pt for the stage name, JetBrains Mono 12pt for the technical descriptor below it.
3. **richezamor.com section header.** Inter SemiBold 32pt H2, JetBrains Mono 14pt eyebrow label above it (e.g., `// section-02`).

## Related entries
- `corpus/brand-system/identity/neural-architect-overview.md` — why the two-font system encodes "practitioner"
- `corpus/brand-system/presentation/minimal-text-max-impact.md` — type scale for slides
- `corpus/brand-system/social/mobile-thumbnail-readability.md` — minimum sizes for social assets
- `corpus/brand-system/identity/palette.yaml` — the same font stack in machine-readable form

## Anti-patterns
- Pulling in a serif (Playfair, Georgia) "for elegance." Elegance in this system comes from spacing, not from typeface variety.
- Using monospace for body copy because it "feels technical." Mono is reserved for technical anchors — overusing it makes everything feel like a terminal log and hurts readability.
