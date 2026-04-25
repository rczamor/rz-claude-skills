---
name: Animate Only `transform` and `opacity`
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/07-motion/no-transition-all.md, corpus/ux-principles/audit/10-performance/cls-target.md]
---

# Animate Only `transform` and `opacity`

## What it is
For motion that runs at 60fps on every device, the only safe properties to animate are `transform` (translate, scale, rotate) and `opacity`. Animating layout properties (`width`, `height`, `top`, `left`, `margin`, `padding`) forces layout recalculation on every frame and ships at jittery 20–30fps on lower-end devices.

## Why it matters
The browser composites `transform` and `opacity` on the GPU without involving the main thread — they're "free" in animation terms. Every other property requires re-layout (geometry recalc) or repaint, both of which run on the main thread alongside JavaScript. On a busy app this is the difference between buttery and broken. A modal that animates `top: 100% → top: 0` on a mid-tier Android phone ships at 25fps; the same modal animating `transform: translateY(100%) → translateY(0)` ships at 60fps.

## How to apply
- Animate position with `transform: translate()`, not `top` / `left`.
- Animate size with `transform: scale()` (combined with `transform-origin`), not `width` / `height`. If you need actual layout-aware size animation (e.g., expanding card), use the FLIP technique or animate from a `transform: scale()` with the final size already laid out behind a clip.
- Animate appearance with `opacity`, not `visibility` or `display`.
- For background reveals, animate a child's `transform: translate()` behind a clip — don't animate the parent's `height`.
- For collapsible panels, prefer `max-height` with a known target value plus `opacity`, or use a JS-driven `height` only after measuring — never animate `height: auto`.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
.drawer { transition: left 300ms ease-out; left: -320px; }
.drawer.open { left: 0; }
/* runs layout on every frame — janky on mid-tier phones */
```

GOOD:
```css
.drawer {
  transform: translateX(-100%);
  transition: transform 300ms var(--ease-out);
  will-change: transform;
}
.drawer.open { transform: translateX(0); }
```

## Related entries
- `corpus/ux-principles/audit/07-motion/no-transition-all.md` — explicit property lists prevent layout-property animation.
- `corpus/ux-principles/audit/10-performance/cls-target.md` — layout shifts and animations are part of the same budget.

## Anti-patterns
- Animating `width`/`height` "because it's simpler than scale + transform-origin."
- `will-change: auto` on everything — loses the optimization signal.
- Forgetting `transform-origin` and watching scale animations grow from the wrong corner.
