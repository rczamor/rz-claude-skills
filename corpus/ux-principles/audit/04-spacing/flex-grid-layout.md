---
name: Flex / Grid for Layout, Not JS Measurement
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/grid-consistent.md, corpus/ux-principles/audit/10-performance/cls-target.md]
---

# Flex / Grid for Layout, Not JS Measurement

## What it is

Use CSS Flexbox and CSS Grid to lay out the page. Do not use JavaScript to measure elements (`getBoundingClientRect`, ResizeObserver, manual width calculations) and apply layout dimensions. CSS layout is faster, more accessible, more responsive, and survives JS failures.

JS measurement is an anti-pattern that emerged before flexbox/grid were widely supported. It's now deprecated in practice — modern CSS handles everything those JS hacks were trying to solve.

## Why it matters

JS-driven layout has multiple failure modes:

- **CLS (Cumulative Layout Shift):** elements jump around as JS measures and applies sizes after initial render.
- **Performance:** layout calculations on every resize / scroll bog down the main thread.
- **Accessibility:** screen readers may read content before JS positions it.
- **Brittleness:** any JS error breaks the entire layout.

CSS layout has none of these problems. It runs natively in the browser, layouts are calculated once and reused, and progressive enhancement means the page works even if JS fails.

## How to apply

1. **Use CSS Grid for two-dimensional layouts:**
   ```css
   .container {
     display: grid;
     grid-template-columns: 1fr 2fr 1fr;
     gap: 24px;
   }
   ```
2. **Use Flexbox for one-dimensional layouts:**
   ```css
   .row {
     display: flex;
     gap: 16px;
     align-items: center;
   }
   ```
3. **Avoid `width: ${jsCalculatedWidth}px` patterns.**
4. **Use `aspect-ratio`** for proportional sizing instead of JS height calculations.
5. **Use container queries** (`@container`) for component-level responsiveness instead of JS resize listeners.

## Examples

- **GOOD:** A 3-column responsive grid:
  ```css
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
  }
  ```
- **BAD:** `useEffect(() => { const width = window.innerWidth; setColumns(width > 1024 ? 3 : 1); })`. Causes CLS, depends on JS.
- **GOOD:** `aspect-ratio: 16 / 9;` on a video container. Reserves space, no layout shift.
- **BAD:** JS measuring video metadata to compute height. Layout shifts when video loads.

## Related entries

- `corpus/ux-principles/audit/04-spacing/grid-consistent.md`
- `corpus/ux-principles/audit/10-performance/cls-target.md`

## Anti-patterns

- Using `<Masonry>` libraries that JS-measure every card. Modern CSS columns or grid handle most cases.
- "We need JS measurement because we support old browsers." All evergreen browsers support flex/grid. IE11 is dead.
