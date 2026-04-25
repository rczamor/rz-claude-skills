---
name: No Letterspacing on Lowercase Text
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/scale-ratio.md, corpus/ux-principles/audit/02-typography/weight-contrast.md]
---

# No Letterspacing on Lowercase Text

## What it is

Letterspacing (CSS `letter-spacing`) — increasing the space between characters — is a typographic effect that works on uppercase or all-caps text. It does NOT work on lowercase text. Frederic Goudy's famous line: "Anyone who would letterspace lowercase would steal sheep."

Letterspaced lowercase looks broken: the connections between letters that the typeface designer carefully spaced are torn apart, leaving awkward gaps. It is one of the most visible typography failures.

## Why it matters

Typefaces are designed with specific spacing relationships baked into the glyphs. Lowercase letters are designed to flow into each other; spacing them apart fights the design. Uppercase letters are typically designed standalone (Roman inscriptions, where each capital was carved with space around it), so letterspacing them respects the original.

A small dose of negative letterspacing (`letter-spacing: -0.02em`) is acceptable on large display headlines — it tightens generous default spacing for big sizes. Positive letterspacing on lowercase is almost never correct.

## How to apply

1. **Don't apply positive `letter-spacing` to lowercase text.**
2. **Letterspace uppercase / all-caps freely.** Common values: `letter-spacing: 0.05em` to `0.1em` on uppercase labels.
3. **Slight negative letterspacing on display headlines is fine:** `letter-spacing: -0.01em` to `-0.02em` on h1-sized text.
4. **Audit:** search for `letter-spacing` values. If applied to body or lowercase text with positive value, flag.

## Examples

- **GOOD:** `<span class="label" style="text-transform: uppercase; letter-spacing: 0.08em;">Section</span>` — letterspaced uppercase, looks polished.
- **BAD:** `<p style="letter-spacing: 0.05em;">This is body text...</p>` — letterspaced lowercase, looks broken.
- **GOOD:** Display headline at 64px with `letter-spacing: -0.02em` — tightens for large size.
- **BAD:** Buttons in lowercase with `letter-spacing: 0.1em` — gaps between letters look amateur.

## Related entries

- `corpus/ux-principles/audit/02-typography/scale-ratio.md`
- `corpus/ux-principles/audit/02-typography/weight-contrast.md`

## Anti-patterns

- Letterspacing lowercase to "make it feel airy." It feels broken.
- Applying letterspacing globally via `*` selector — affects every element including lowercase.
