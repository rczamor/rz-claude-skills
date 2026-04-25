---
name: Line-Height — 1.5x Body, 1.15-1.25x Headings
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/measure-45-75.md, corpus/ux-principles/audit/02-typography/scale-ratio.md]
---

# Line-Height — 1.5x Body, 1.15-1.25x Headings

## What it is

Line-height (the vertical space between lines) should be approximately:

- **Body text: 1.5x font-size.** A 16px body gets ~24px line-height.
- **Headings: 1.15-1.25x font-size.** A 32px heading gets 36-40px line-height.

Body text needs generous line-height for legibility on multi-line paragraphs. Headings, which are usually 1-2 lines, need tighter line-height to stay visually unified — wide line-height on a heading makes it read as two separate headings.

## Why it matters

Cramped body text is unreadable; the eye loses its place between lines. Loose body text wastes vertical space and breaks the connection between consecutive lines. Headings with body-style line-height (1.5) look spaced apart instead of unified. The two contexts genuinely need different spacing — there is no one-size-fits-all line-height.

## How to apply

1. **Body:** `line-height: 1.5;` (unitless lets it scale with font-size).
2. **Headings:** `line-height: 1.2;` for most cases, tighter (1.1) for very large display headings.
3. **In CSS:**
   ```css
   body { line-height: 1.5; }
   h1, h2, h3, h4, h5, h6 { line-height: 1.2; }
   ```
4. **Audit:** check `getComputedStyle(p).lineHeight` on body paragraphs. If it's the same as headings or way off, fix.

## Examples

- **GOOD:** Body at `font-size: 16px; line-height: 1.5;` → 24px between lines. Reads comfortably.
- **GOOD:** H1 at `font-size: 48px; line-height: 1.15;` → 55px line-height. Heading reads as one unit.
- **BAD:** Body at `line-height: 1.2;` (the heading value applied to body). Lines feel cramped.
- **BAD:** H1 at `line-height: 1.5;` — a two-line headline looks like two separate headings.

## Related entries

- `corpus/ux-principles/audit/02-typography/measure-45-75.md`
- `corpus/ux-principles/audit/02-typography/scale-ratio.md`

## Anti-patterns

- Using pixel line-heights (`line-height: 24px`) — they don't scale when font-size changes.
- Single `line-height` value for the whole site. Body and headings need different values.
