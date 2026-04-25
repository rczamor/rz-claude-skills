---
name: Grid Consistent at All Breakpoints
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/breakpoints.md, corpus/ux-principles/audit/04-spacing/alignment-consistent.md, corpus/ux-principles/audit/06-responsive/mobile-design-sense.md]
---

# Grid Consistent at All Breakpoints

## What it is

A grid (column system, gutter widths, container max-widths) should be consistent at every breakpoint. Not the same grid at every screen size — but a coherent system that scales: e.g., 4 columns at mobile, 8 at tablet, 12 at desktop, with proportional gutters. Elements snap to grid lines at every breakpoint; nothing drifts off the system.

Inconsistent grids show up as: containers with different left margins on different pages, columns that don't align between sections, breakpoints where the layout suddenly looks "off."

## Why it matters

The grid is the invisible structure that makes a page feel ordered. When elements align to a shared grid, the eye reads "system." When elements are placed pixel-by-pixel without a grid, the eye reads "chaos" — even if the chaos is subtle and unconscious.

A consistent grid at every breakpoint also makes responsive design predictable. Designers don't redesign each viewport; they apply the grid scaled appropriately.

## How to apply

1. **Define a column system.** Common: 12 columns desktop, 8 tablet, 4 mobile, with consistent gutters (e.g., 24px desktop, 16px tablet, 16px mobile).
2. **Use CSS Grid or a framework's grid utilities.** Tailwind's grid, Bootstrap's grid, or native CSS `grid-template-columns`.
3. **Audit at every breakpoint.** Resize the window from 320px up to 1920px. Do columns hold? Do gutters scale predictably? Do max-widths kick in at the right point?
4. **Snap elements to grid lines.** Avoid arbitrary positioning that doesn't respect the grid.

## Examples

- **GOOD:** A landing page with a 12-column grid where the hero image spans cols 1-7 and the headline spans cols 8-12. Consistent at every breakpoint.
- **BAD:** Sections with different gutter widths — header gutter 32px, content gutter 24px, footer gutter 20px. Eye senses misalignment.
- **GOOD:** Stripe.com — strict grid, columns align across sections perfectly.
- **BAD:** A page where each section is independently centered with random max-width values.

## Related entries

- `corpus/ux-principles/audit/04-spacing/breakpoints.md`
- `corpus/ux-principles/audit/04-spacing/alignment-consistent.md`
- `corpus/ux-principles/audit/06-responsive/mobile-design-sense.md`

## Anti-patterns

- "We don't really have a grid — we just eyeball it." The eye notices the lack of grid.
- Defining a grid in Figma but not enforcing it in CSS. The dev implementation drifts.
