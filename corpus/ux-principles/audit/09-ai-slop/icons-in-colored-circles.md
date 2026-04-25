---
name: Icons in Colored Circles (SaaS-Starter Look)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/identity/imagery-anti-patterns.md, corpus/ux-principles/audit/09-ai-slop/3-column-feature-grid.md]
---

# Icons in Colored Circles

## What it is
Section decoration via small icon (Heroicons / Lucide / Feather) sitting inside a soft pastel circular background (`rounded-full bg-purple-100 p-4`). The "SaaS starter template" look — a visual tic so widespread it now reads as "I downloaded a template and didn't change it." Whether it appears inside the 3-column feature grid or scattered as section accents, it's the same signal.

## Why it matters
The test: would a human designer at a respected studio ship this? Stripe's docs use icons. Apple's marketing uses icons. Neither uses a 32px icon dropped into a 64px pastel circle as if it were a profile picture. The colored-circle treatment tries to make a 16px glyph "feel substantial" by giving it a background — but the bigger problem is that the icon usually doesn't earn its place at all. It's decoration pretending to be hierarchy.

## How to apply
- Search for the pattern: `rounded-full` + `bg-{color}-100` + `flex items-center justify-center` + an SVG or icon child.
- Replacement options:
  - **Drop the icon** — most pages improve when icons disappear. The headline does the work.
  - **Replace icon with a number** — if the section is genuinely sequential (Step 1 / Step 2), use typography (a large "01" / "02") rather than icons-in-circles.
  - **Replace icon with a product screenshot fragment** — a small UI screenshot showing the feature is far more concrete than a generic glyph.
  - **Use the icon without the circle** — if you must keep the icon, drop the pastel background; let the icon sit on the page at proper weight.
- For brand-led design, custom illustrations (not icon-pack glyphs) earn their visual real estate. Icon packs in colored circles never do.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<div class="flex items-center justify-center w-12 h-12 rounded-full bg-blue-100 mb-4">
  <BoltIcon class="w-6 h-6 text-blue-600"/>
</div>
<h3>Lightning Fast</h3>
```

GOOD — replaced with typography:
```html
<span class="font-display text-5xl text-neutral-300">01</span>
<h3>Lightning Fast</h3>
```

GOOD — replaced with product screenshot:
```html
<img src="/screenshots/perf-graph.png" alt="Latency chart" class="rounded-md border" />
<h3>Lightning Fast</h3>
```

## Related entries
- `corpus/brand-system/identity/imagery-anti-patterns.md` — full anti-pattern catalog.
- `corpus/ux-principles/audit/09-ai-slop/3-column-feature-grid.md` — where this pattern most often appears.

## Anti-patterns
- Custom SVG inside the same colored circle — fixes the icon, not the pattern.
- Different-colored circle per feature ("blue for speed, purple for security") — same slop, more colors.
- Animated circles on hover — slop with motion.
