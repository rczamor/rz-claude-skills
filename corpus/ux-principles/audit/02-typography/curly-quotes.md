---
name: Curly Quotes, Not Straight
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/ellipsis-character.md, corpus/voice/]
---

# Curly Quotes, Not Straight

## What it is

Use typographic ("curly" or "smart") quotes — `"` `"` and `'` `'` — instead of straight ASCII quotes (`"` and `'`). Straight quotes are technical artifacts of typewriters and code; curly quotes are how published prose has been set for centuries.

The Unicode characters:
- Left double quote: `"` (U+201C)
- Right double quote: `"` (U+201D)
- Left single quote: `'` (U+2018)
- Right single quote: `'` (U+2019)

## Why it matters

Curly quotes are a small but unmistakable signal of typographic care. Straight quotes in body copy are like wearing tennis shoes with a suit — technically allowed, immediately noticed by anyone paying attention. Most professional publishing tools auto-convert straight to curly; web teams that ship straight quotes are signaling "we didn't think about this."

Note: code blocks and `<pre>` should use straight quotes — they are syntactic, not typographic.

## How to apply

1. **In published copy:** use curly quotes. Most CMS and editors auto-convert.
2. **Use HTML entities or Unicode characters** in prose: `&ldquo;` `&rdquo;` `&lsquo;` `&rsquo;` or paste the actual characters.
3. **Apostrophes** in contractions: `it's` (curly apostrophe), not `it's` (straight).
4. **Don't curl quotes inside code samples** — code is literal.
5. **Audit:** search the rendered DOM for `"` and `'` in prose contexts. Flag.

## Examples

- **GOOD:** "Don't make me think." (curly double, curly apostrophe)
- **BAD:** "Don't make me think." (straight quotes throughout)
- **GOOD:** A blog post where every quote, contraction, and possessive uses the curly form.
- **BAD:** Marketing copy with straight quotes — "We're the best!" looks unfinished.

## Related entries

- `corpus/ux-principles/audit/02-typography/ellipsis-character.md` — same idea: real character, not ASCII approximation
- `corpus/voice/` — copy quality

## Anti-patterns

- Mixing curly and straight quotes within the same paragraph because the tooling didn't auto-convert.
- Using `&quot;` (which renders as straight) instead of `&ldquo;` / `&rdquo;` in HTML.
