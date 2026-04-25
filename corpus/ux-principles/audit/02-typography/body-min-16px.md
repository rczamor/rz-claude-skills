---
name: Body Text ≥ 16px
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/caption-min-12px.md, corpus/ux-principles/audit/06-responsive/text-readable-no-zoom.md]
---

# Body Text ≥ 16px

## What it is

Body text — the main reading copy — should be at least 16px (1rem). Smaller body text (14px, 13px, 12px) is harder to read, fatigues users, and on mobile triggers the browser's text-zoom workaround (which interferes with input field focus on iOS).

This is the floor. 17px or 18px body is fine and often better, especially for long-form prose.

## Why it matters

A small body size says "we don't care about readers" or "we're trying to fit too much." Both are bad messages. 16px is the browser default for a reason — it's the threshold below which sustained reading becomes effortful. On phones, anything under 16px causes iOS Safari to auto-zoom the form when focused (which displaces the layout).

This is the single highest-leverage typography fix on most websites.

## How to apply

1. **Set body to 16px+:**
   ```css
   body { font-size: 1rem; }  /* 16px default */
   ```
2. **Or larger for editorial:**
   ```css
   .prose { font-size: 1.125rem; }  /* 18px */
   ```
3. **Don't set the root smaller than 16px.** Some sites do `html { font-size: 14px; }` to scale the whole site down. This breaks accessibility — users who need larger text rely on the 16px default.
4. **Audit:** check `getComputedStyle(p).fontSize` on body paragraphs. If < 16px, fix.

## Examples

- **GOOD:** Stripe's docs at 16px body. Comfortable reading.
- **GOOD:** Medium articles at 21px body. Editorial, generous, easy to read at length.
- **BAD:** A SaaS dashboard with 13px body text. Users squint within minutes.
- **BAD:** A marketing site with 14px body to "fit more above the fold." User leaves before reading.

## Related entries

- `corpus/ux-principles/audit/02-typography/caption-min-12px.md`
- `corpus/ux-principles/audit/06-responsive/text-readable-no-zoom.md`

## Anti-patterns

- Designing on a desktop with sharp eyes and forgetting that real users have varying eyesight, smaller screens, and reflective lighting.
- Setting `html { font-size: 62.5% }` (the "10px rem" trick) — breaks accessibility for users who set a larger default.
