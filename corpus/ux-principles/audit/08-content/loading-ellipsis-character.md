---
name: Loading Ellipsis Character (`…`, not `...`)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/02-typography/ellipsis-character.md, corpus/ux-principles/audit/02-typography/curly-quotes.md]
---

# Loading Ellipsis Character

## What it is
Loading state copy uses the single-character ellipsis (`…`, U+2026) — never three dots (`...`). "Saving…" not "Saving..." This is a typographic-quality signal that separates designed products from rushed ones.

## Why it matters
Three dots and an ellipsis look identical at a glance, but they're not. Three dots have inconsistent spacing, can wrap onto a new line mid-sequence, and are slightly wider — they look unintentional. The ellipsis character is an intentional, designed glyph: tighter, won't break across lines, properly typeset. It's the difference between "we know what we're doing" and "we don't sweat the small stuff." Both convey something on a system level.

## How to apply
- In code, store `…` directly as a Unicode character — not as `...`. Most code editors accept it.
- Or use the HTML entity `&hellip;` if your build pipeline can't handle non-ASCII.
- Replace `...` globally with `…` in all UI copy: `git grep -n '\.\.\.'` and audit each match (some are intentional, e.g., code).
- Configure your linter / Prettier hook to flag three-dot strings in JSX text nodes and translation files.
- Same applies to button labels for menus that open: "More…", "Open file…" — convention is the ellipsis indicates more action follows (Apple HIG).

## Examples (BAD vs. GOOD pairs)

BAD:
```jsx
<span>Saving...</span>
<button>Open file...</button>
<span>Loading content...</span>
```

GOOD:
```jsx
<span>Saving…</span>
<button>Open file…</button>
<span>Loading content…</span>
```

## Related entries
- `corpus/ux-principles/audit/02-typography/ellipsis-character.md` — the typography-side rule (parent).
- `corpus/ux-principles/audit/02-typography/curly-quotes.md` — same family of typographic-quality rules.

## Anti-patterns
- "..." in shipped UI copy — three dots, instant amateur hour.
- Mixing both conventions in the same codebase.
- Replacing every `...` blindly — some are correct (in code samples, ranges).
