---
name: Text Readable Without Zoom on Mobile
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/02-typography/body-min-16px.md, corpus/ux-principles/audit/06-responsive/no-user-scalable-no.md]
---

# Text Readable Without Zoom on Mobile

## What it is
Body text on mobile must render at ≥16px so users can read without pinch-zoom. This includes paragraph copy, list items, form-field values, and table cells. Captions and labels can drop to 12px floor, but the bulk of read-mode content is 16px or larger.

## Why it matters
iOS Safari auto-zooms the page when a user focuses an input smaller than 16px — disorienting and often leaves the page mis-scrolled afterward. Anything smaller than 16px on mobile is a readability failure for older users and anyone reading in low light. "It looks fine on my 27-inch monitor" is the wrong test.

## How to apply
- Set base body to `font-size: 16px` (or `1rem` with html at 100%). Don't override smaller for mobile.
- Form inputs specifically: `input, textarea, select { font-size: 16px; }` to prevent iOS zoom.
- For long-form content, consider 17–18px on mobile — actually *larger* than desktop, because it's read closer and at smaller measure.
- Don't use viewport-relative units like `font-size: 2vw` for body — gets unreadable on narrow phones.
- Test at 375px wide (iPhone SE / mini) — if anything's hard to read there, it's a fail.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
body { font-size: 14px; }
.form-input { font-size: 13px; } /* triggers iOS auto-zoom on focus */
```

GOOD:
```css
body { font-size: 16px; line-height: 1.5; }
.form-input { font-size: 16px; }
@media (min-width: 768px) {
  body { font-size: 17px; } /* slight bump on tablet+, not shrinkdown */
}
```

## Related entries
- `corpus/ux-principles/audit/02-typography/body-min-16px.md` — the typography-side rule.
- `corpus/ux-principles/audit/06-responsive/no-user-scalable-no.md` — never block manual zoom either.

## Anti-patterns
- Designing in Figma at 16px desktop and shrinking to 13px mobile because "more fits on screen."
- Form inputs at 13–14px — iOS will zoom on every focus.
- Treating font-size as a styling choice instead of an accessibility floor.
