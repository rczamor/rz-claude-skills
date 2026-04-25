---
name: Generic Font Flag — Inter / Roboto / Open Sans / Poppins
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/blacklisted-fonts.md, corpus/ux-principles/audit/02-typography/font-count-leq-3.md, corpus/brand-system/identity/]
---

# Generic Font Flag — Inter / Roboto / Open Sans / Poppins

## What it is

If the primary font is **Inter**, **Roboto**, **Open Sans**, or **Poppins** with no other distinguishing typographic choices, flag it as potentially generic. These are excellent neutral typefaces — but their ubiquity means a product using them with no further typographic identity reads as "default Tailwind starter" rather than "designed product."

This is not a blacklist. It is a flag: ask whether the typography is doing identity work, or just sitting there.

## Why it matters

Typography is a major identity carrier. Two products that look identical in layout can feel completely different based on type choice. When every SaaS startup uses Inter or Roboto, the typeface stops carrying identity — it becomes wallpaper. The flag is a prompt: did the team make a typographic choice, or did they default?

It's fine to use these fonts. It's not fine to use them and call it your typographic identity.

## How to apply

1. **Detect:** check the primary `font-family`. If it's Inter, Roboto, Open Sans, or Poppins — flag.
2. **Ask:** is anything else doing identity work? A distinctive display face, custom letterspacing on the wordmark, a specific weight choice?
3. **If nothing else:** recommend pairing with a distinctive display face for headings, or switching the body to something quieter (Source Serif, IBM Plex) and using the generic only as a workhorse.
4. **In Riché's brand system context** (Neural Architect): pair Inter body with a more distinctive display face — see `corpus/brand-system/identity/`.

## Examples

- **GENERIC:** Inter 400 body, Inter 600 headings. No display face. Looks like every other SaaS landing page.
- **BETTER:** Inter 400 body, Söhne (or any distinctive display) for headings. Inter does the workhorse job; the display carries identity.
- **GENERIC:** Poppins for everything. The Tailwind starter look.
- **BETTER:** A display face like Migra or Pangram Sans for hero, Inter for body and UI.

## Related entries

- `corpus/ux-principles/audit/02-typography/blacklisted-fonts.md`
- `corpus/ux-principles/audit/02-typography/font-count-leq-3.md`
- `corpus/brand-system/identity/`

## Anti-patterns

- Treating "we use Inter" as a typographic identity. It's a starting point.
- Picking Poppins because "it has rounded shapes that feel friendly" without considering it's the most overused friendly font.
