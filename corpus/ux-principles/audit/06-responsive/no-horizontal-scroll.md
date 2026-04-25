---
name: No Horizontal Scroll on Any Viewport
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/04-spacing/no-mobile-horizontal-scroll.md, corpus/ux-principles/audit/04-spacing/max-content-width.md]
---

# No Horizontal Scroll on Any Viewport

## What it is
Outside of intentional carousels and tables marked as scrollable, the page must not horizontally scroll on any viewport from 320px up to ultra-wide. A horizontal scrollbar appearing on mobile is one of the loudest signals that the layout is broken — it usually means an element overflows its container or the viewport meta is missing.

## Why it matters
Horizontal scroll on a body page disorients users (they don't expect to drag sideways to read), hides content (the parts they don't drag to never get seen), and breaks scroll-snap and pull-to-refresh interactions. It often co-occurs with broken padding-inset CTAs that users physically cannot tap.

## How to apply
- Set `overflow-x: hidden` on `body` only as a last-resort safety net — first find the offending element.
- Common culprits: fixed-width images without `max-width: 100%`, `width: 100vw` without accounting for scrollbar, negative margins on cards, raw `<pre>` blocks, embedded iframes, tables without a wrapping `overflow-x: auto` div.
- Check the viewport meta is present: `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Open DevTools, set viewport to 320px, scroll to bottom of every page. Inspect any element whose right edge crosses the viewport.
- For intentional horizontal scroll (carousels, tables), wrap explicitly: `<div style="overflow-x: auto">` so it's contained, not page-level.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
.hero-image { width: 1440px; } /* overflows on every mobile */
.code-block { white-space: pre; } /* long lines push the page wider */
```

GOOD:
```css
.hero-image { width: 100%; max-width: 1440px; height: auto; }
.code-block { overflow-x: auto; white-space: pre; } /* scrolls inside its container */
```

## Related entries
- `corpus/ux-principles/audit/04-spacing/no-mobile-horizontal-scroll.md` — duplicate at spacing layer.
- `corpus/ux-principles/audit/04-spacing/max-content-width.md` — bounding the body width.

## Anti-patterns
- `body { overflow-x: hidden }` with no investigation — the overflowing element still misaligns layout, just silently.
- `width: 100vw` on full-bleed sections — `100vw` includes scrollbar, causing 15px overflow on Windows.
- Tables sized in pixels with no scroll wrapper.
