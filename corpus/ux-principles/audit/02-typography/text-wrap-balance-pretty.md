---
name: text-wrap balance / pretty on Headings
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/scale-ratio.md, corpus/ux-principles/audit/02-typography/measure-45-75.md]
---

# text-wrap balance / pretty on Headings

## What it is

The CSS property `text-wrap: balance` distributes lines of a heading so they have approximately equal lengths, avoiding the "one big line plus one orphan word" problem. `text-wrap: pretty` is similar but for body text and avoids orphans (last-line single words). Modern browsers (Chrome 114+, Safari 17.4+, Firefox 121+) support these.

The rule: apply `text-wrap: balance` to headings and `text-wrap: pretty` to long-form body text.

## Why it matters

Without balanced wrapping, multi-line headings often end with an orphan word on the last line — "this is a really long headline\nthat wraps." Looks awkward. With `balance`, the browser reflows so both lines have similar character counts. Small change, big polish improvement.

## How to apply

1. **CSS:**
   ```css
   h1, h2, h3, h4, h5, h6 {
     text-wrap: balance;
   }
   p, .prose {
     text-wrap: pretty;
   }
   ```
2. **Audit:** in DevTools, run `getComputedStyle(h1).textWrap`. Should be `balance` or `pretty` depending on element type.
3. **Note browser support.** Falls back gracefully — older browsers just don't get the polish.

## Examples

- **GOOD (with balance):**
  ```
  Process payments online
  in any currency
  ```
  Two lines of similar length.
- **BAD (without balance):**
  ```
  Process payments online in any
  currency
  ```
  Orphan word on the last line.
- **GOOD body with pretty:** No orphan single word ending a paragraph.
- **BAD body without pretty:** Last line is just "the." Reads as unfinished.

## Related entries

- `corpus/ux-principles/audit/02-typography/scale-ratio.md`
- `corpus/ux-principles/audit/02-typography/measure-45-75.md`

## Anti-patterns

- Hard-coding `<br>` tags into headings to control wrapping. Brittle — breaks on different viewports.
- Forgetting to apply this — it's a one-line change that immediately raises the polish floor.
