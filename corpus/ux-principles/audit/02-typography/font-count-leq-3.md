---
name: Font Count ≤ 3
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/blacklisted-fonts.md, corpus/ux-principles/audit/02-typography/generic-font-flag.md, corpus/brand-system/identity/]
---

# Font Count ≤ 3

## What it is

Cap the total number of distinct font families on a page or product at three. Typically: one display/heading face, one body face (often the same family at different weights), and one optional monospace for code or numerical data. More than three font families fragments the visual identity and signals indecision.

## Why it matters

Each font family carries personality. Mixing too many is like wearing four different patterns — every voice fights every other voice. The result: no coherent identity, more cognitive load (the eye has to re-recognize each shift), and a "design by committee" feel.

Most polished products use one or two faces, max. Three is a hard ceiling for almost every case.

## How to apply

1. **Audit:** run `getComputedStyle(e).fontFamily` across the page.
2. **Count distinct families.** If > 3, flag.
3. **Acceptable use of three:** display, body, mono. Anything else is usually waste.
4. **Use weight and size for hierarchy** within a single family rather than introducing a new family.

## Examples

- **GOOD:** Body and headings in `Inter`, code in `JetBrains Mono`. Two families, clear roles.
- **GOOD:** Headings in `Playfair Display`, body in `Inter`, code in `IBM Plex Mono`. Three families, distinct roles.
- **BAD:** Headings in `Montserrat`, body in `Open Sans`, buttons in `Lato`, code in `Source Code Pro`, decorative pull-quotes in `Lora`. Five families = chaos.
- **BAD:** A page where some buttons accidentally inherit `Arial` from a global style and others use `Inter` — invisible inconsistency, but the eye notices.

## Related entries

- `corpus/ux-principles/audit/02-typography/blacklisted-fonts.md`
- `corpus/ux-principles/audit/02-typography/generic-font-flag.md`
- `corpus/brand-system/identity/` — typography is identity

## Anti-patterns

- "We needed a fancy font for the marketing site so we added a fourth." Use the existing display face's heaviest weight at a larger size instead.
- Letting CMS or marketing tools inject extra fonts without auditing.
