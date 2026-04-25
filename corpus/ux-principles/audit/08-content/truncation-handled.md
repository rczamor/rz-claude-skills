---
name: Truncation Handled (`ellipsis` / `line-clamp` / `break-words`)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/02-typography/measure-45-75.md, corpus/ux-principles/audit/06-responsive/no-horizontal-scroll.md]
---

# Truncation Handled

## What it is
Long text in constrained containers must have explicit overflow handling: single-line truncation with `text-overflow: ellipsis`, multi-line clamping with `-webkit-line-clamp`, or word-breaking with `overflow-wrap: anywhere`. Text that simply overflows its container or pushes the layout horizontally is a bug.

## Why it matters
Real user data is messy: long email addresses, Slavic last names, German compound nouns, URLs, raw transaction IDs. If your design only handles "Sarah Chen" and "myproject," it breaks on first contact with production data. Untruncated text causes horizontal scroll, breaks card grids, and pushes other elements off-screen — all on the user's first encounter.

## How to apply
- Single-line truncation:
  ```css
  .one-line {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  ```
- Multi-line truncation:
  ```css
  .clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  ```
- Long unbreakable strings (URLs, hashes):
  ```css
  .can-break { overflow-wrap: anywhere; word-break: break-word; }
  ```
- For truncated text, expose the full value on hover (`title="..."`) or via expansion (a click-to-show-more affordance for long content).
- Test with the worst real-world strings you can find: longest customer name in the DB, longest project title, a raw URL.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<li class="card-title">Internal Project: Q3 Migration to Postgres + Cassandra Hybrid Architecture (Phase 2 of 4)</li>
<!-- card-title has no overflow rule — pushes layout sideways -->
```

GOOD:
```css
.card-title {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```
Hover reveals full title via `title` attribute.

## Related entries
- `corpus/ux-principles/audit/02-typography/measure-45-75.md` — measure rule shapes line length in the first place.
- `corpus/ux-principles/audit/06-responsive/no-horizontal-scroll.md` — untruncated text is a top cause.

## Anti-patterns
- Trusting that "names won't be that long" — they will be.
- Truncating without preserving the full value (no `title`, no expand interaction).
- Using `overflow: hidden` alone, which silently chops text mid-character with no visual signal.
