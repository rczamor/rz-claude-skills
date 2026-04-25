---
name: Breakpoints — Mobile 375 / Tablet 768 / Desktop 1024 / Wide 1440
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/grid-consistent.md, corpus/ux-principles/audit/06-responsive/mobile-design-sense.md]
---

# Breakpoints — Mobile 375 / Tablet 768 / Desktop 1024 / Wide 1440

## What it is

Use a small, consistent set of breakpoints across the design system:

- **Mobile:** 375px (iPhone SE / 13 mini width)
- **Tablet:** 768px (iPad portrait)
- **Desktop:** 1024px (small laptop / iPad landscape)
- **Wide:** 1440px (typical desktop monitor)

These cover ~95% of real device viewports. Avoid creating dozens of bespoke breakpoints — most designs need only 3-4. Tailwind's defaults (`sm: 640`, `md: 768`, `lg: 1024`, `xl: 1280`, `2xl: 1536`) align closely with this set.

## Why it matters

Inconsistent breakpoints across a product produce sites where some pages reflow at 800px and others at 850px — small, visible, and disorienting. A shared breakpoint set means designers and devs use the same mental model and the product reflows predictably everywhere.

The specific values matter less than the consistency. Tailwind's, Bootstrap's, or these — pick a set, stick to it.

## How to apply

1. **Define breakpoints once in CSS or design tokens:**
   ```css
   :root {
     --bp-mobile: 375px;
     --bp-tablet: 768px;
     --bp-desktop: 1024px;
     --bp-wide: 1440px;
   }
   ```
2. **Use them in media queries:**
   ```css
   @media (min-width: 768px) { ... }
   @media (min-width: 1024px) { ... }
   ```
3. **Mobile-first.** Start with mobile styles and progressively add larger breakpoints.
4. **Audit:** scan all media queries. Are values consistent? `@media (min-width: 768px)` everywhere, not random `@media (min-width: 800px)` mixed in.

## Examples

- **GOOD CSS:**
  ```css
  /* mobile-first */
  .card { padding: 16px; }
  @media (min-width: 768px) { .card { padding: 24px; } }
  @media (min-width: 1024px) { .card { padding: 32px; } }
  ```
- **BAD:** Random breakpoints — `@media (min-width: 750px)`, `@media (min-width: 950px)`, `@media (min-width: 1180px)`. No system.
- **GOOD:** Tailwind config using the standard breakpoints, applied consistently across all components.
- **BAD:** Each component defining its own breakpoints inline.

## Related entries

- `corpus/ux-principles/audit/04-spacing/grid-consistent.md`
- `corpus/ux-principles/audit/06-responsive/mobile-design-sense.md`

## Anti-patterns

- Creating a unique breakpoint for every component. You don't need 14 breakpoints — you need 4.
- Breakpoints too close together (`640px`, `680px`, `720px`). Reflowing in narrow ranges is jarring.
