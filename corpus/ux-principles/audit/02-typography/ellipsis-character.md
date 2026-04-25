---
name: Ellipsis Character — … Not Three Dots
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/curly-quotes.md, corpus/ux-principles/audit/08-content/loading-ellipsis-character.md]
---

# Ellipsis Character — … Not Three Dots

## What it is

Use the proper ellipsis character `…` (U+2026, HTML `&hellip;`) instead of three periods `...`. The ellipsis is a single typographic character with correct kerning; three dots are three separate periods that the rendering engine spaces somewhat arbitrarily.

## Why it matters

Subtle but unmistakable. Three dots look slightly off — too tight, too wide, or kerning inconsistent across fonts. The proper ellipsis sets correctly because it's designed as a single glyph. Loading states, truncation, and rhetorical pauses all benefit.

## How to apply

1. **Use `…` directly** in copy. Most editors auto-convert `...` to `…`.
2. **HTML entity:** `&hellip;`
3. **CSS for truncation:** `text-overflow: ellipsis;` uses the proper character automatically.
4. **Loading states:** "Saving…" not "Saving..."
5. **Audit:** search for literal `...` in rendered text.

## Examples

- **GOOD:** "Loading…" (single ellipsis character)
- **BAD:** "Loading..." (three periods)
- **GOOD:** Quote with omitted middle: "The user clicks, sees the result… and stops."
- **BAD:** "The user clicks, sees the result... and stops." (three periods, slightly off)
- **GOOD CSS truncation:**
  ```css
  .truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  ```

## Related entries

- `corpus/ux-principles/audit/02-typography/curly-quotes.md`
- `corpus/ux-principles/audit/08-content/loading-ellipsis-character.md` — specific to loading states

## Anti-patterns

- Hardcoding `...` in copy because "you can't tell the difference." You can.
- Using `....` (four dots) for emphasis — that's not a thing in formal typography.
