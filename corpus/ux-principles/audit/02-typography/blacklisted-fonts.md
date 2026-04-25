---
name: Blacklisted Fonts — Papyrus, Comic Sans, Lobster, Impact, Jokerman
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/font-count-leq-3.md, corpus/ux-principles/audit/02-typography/generic-font-flag.md, corpus/ux-principles/audit/09-ai-slop/system-ui-as-display.md]
---

# Blacklisted Fonts — Papyrus, Comic Sans, Lobster, Impact, Jokerman

## What it is

A small list of fonts that should not appear in any production design except as a deliberate ironic statement. The blacklist:

- **Papyrus** — synonymous with bad design (the Avatar font)
- **Comic Sans** — historically maligned for misuse in serious contexts
- **Lobster** — overused script font, signals "free template"
- **Impact** — meme font, screams "I made this in PowerPoint"
- **Jokerman** — actively unreadable

Seeing any of these in a design is a strong signal that no typographer was involved.

## Why it matters

Typography is the most direct trust signal a product offers. The blacklisted fonts carry such strong cultural negative associations that their presence undermines whatever the design is trying to communicate. A serious B2B product using Comic Sans reads as a joke; a luxury site using Papyrus reads as parody.

## How to apply

1. **Audit `font-family` declarations.** Search for any blacklisted face.
2. **Check fallback chains.** Sometimes the primary font fails to load and the system falls back to something blacklisted.
3. **Replace with a real typeface.** For body, use Inter / Source Sans / Helvetica Neue. For display, pick something the brand actually owns.
4. **Treat any blacklisted font as a HIGH-impact finding.**

## Examples

- **BAD:** A wedding planner's site in Lobster. (Cliché, signals "DIY template.")
- **BAD:** A serious enterprise tool with section headings in Impact. (Reads as ironic / dated.)
- **GOOD:** Replace the offender with the brand's chosen display font, or drop to a clean sans-serif if no display face exists.

## Related entries

- `corpus/ux-principles/audit/02-typography/font-count-leq-3.md`
- `corpus/ux-principles/audit/02-typography/generic-font-flag.md`
- `corpus/ux-principles/audit/09-ai-slop/system-ui-as-display.md` — system-ui as display is the modern equivalent

## Anti-patterns

- "It's our brand font and we love it" — defending Comic Sans because of personal attachment. Cultural associations don't care.
- Including blacklisted fonts in the system font fallback stack. Pick a better fallback.
