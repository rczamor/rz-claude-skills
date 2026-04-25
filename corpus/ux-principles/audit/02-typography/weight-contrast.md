---
name: Weight Contrast — Two or More Weights for Hierarchy
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/scale-ratio.md, corpus/ux-principles/audit/01-hierarchy/squint-test.md]
---

# Weight Contrast — Two or More Weights for Hierarchy

## What it is

Use at least two font weights — typically a regular (400) for body and a semibold/bold (600/700) for emphasis and headings. Weight is one of the cheapest, most effective tools for establishing hierarchy. Single-weight pages (everything regular, or everything bold) read as flat.

## Why it matters

Weight is a faster hierarchy signal than size for inline emphasis. Bolding a key term in a paragraph makes it scannable without restructuring. A heading at the same size as body text but bolder still reads as a heading. Without weight contrast, the only hierarchy tools left are size, color, and position — fewer levers to pull.

## How to apply

1. **Use at least two weights:** regular (400) for body, semibold (600) or bold (700) for headings/emphasis.
2. **Three or four weights are common:** light (300) for de-emphasized labels, regular (400) for body, semibold (600) for emphasis, bold (700) for headings. Don't overuse light — it's a polish weight, not a body weight.
3. **Audit:** count distinct `font-weight` values across the page. If only one (everything 400 or everything 600), introduce contrast.
4. **Make sure the font ships the weights.** Variable fonts give you all weights; older webfonts may only ship 400 and 700.

## Examples

- **GOOD:** Body text in regular (400), headings in semibold (600), emphasized terms inline in bold (700). Three-step hierarchy.
- **BAD:** Everything in regular 400. Hierarchy depends entirely on size; the page reads as a flat document.
- **GOOD:** Inter at 400 for body, 600 for buttons, 700 for headings. Clear three-level system.
- **BAD:** Using a font that only ships 400 weight, then trying to fake bold with `font-weight: bold` (browser synthesizes a fake bold that looks ugly).

## Related entries

- `corpus/ux-principles/audit/02-typography/scale-ratio.md`
- `corpus/ux-principles/audit/01-hierarchy/squint-test.md`

## Anti-patterns

- "We use only the regular weight to keep things minimal." Minimalism is a result of restraint elsewhere; weight contrast helps the user.
- Bolding everything for emphasis. If everything is bold, nothing is.
