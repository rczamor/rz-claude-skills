---
name: Touch Targets ≥44px on Mobile
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/05-interaction/touch-targets-44px.md, corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md]
---

# Touch Targets ≥44px on Mobile

## What it is
Every interactive element on a mobile viewport must present a touch target of at least 44×44 CSS pixels (Apple HIG) or 48dp (Material). This applies to icon-only buttons, link rows, checkboxes, segment-control items, and tab bars — not just the primary CTA.

## Why it matters
The average adult fingerpad is ~10mm, which translates to roughly 38–44 CSS pixels. Targets smaller than 44px increase mistap rate, force users to zoom, and disproportionately fail users with motor impairments or larger hands. On mobile this is not a polish item — it is a baseline accessibility requirement and Apple/Google rejection criterion for native apps.

## How to apply
- Audit every clickable element on the mobile breakpoint. If the *visible* element is smaller than 44px (e.g., a 16px close icon), expand the *hit area* with padding, not just the rendered glyph.
- Use `min-height: 44px; min-width: 44px;` on icon-only buttons.
- For inline text links inside paragraphs, increase line-height to at least 24px and ensure the link is selectable across its full row when it sits in a list.
- Space adjacent targets at least 8px apart so a misaim on one doesn't trigger the other.
- Verify with a real thumb on a real device — devtools simulators lie about hit accuracy.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
.icon-button { width: 24px; height: 24px; padding: 0; } /* 24px hit area */
```

GOOD:
```css
.icon-button {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.icon-button svg { width: 20px; height: 20px; } /* visual icon stays small, hit area is 44 */
```

## Related entries
- `corpus/ux-principles/audit/05-interaction/touch-targets-44px.md` — the universal rule.
- `corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md` — why mobile mistakes cost more.

## Anti-patterns
- Tiny social-icon row in the footer — 16px icons, 4px apart. Untappable.
- Increasing icon size instead of expanding hit area, leaving giant ugly icons in the layout.
- Using `transform: scale()` to fake a larger target — the hit-test region doesn't follow.
