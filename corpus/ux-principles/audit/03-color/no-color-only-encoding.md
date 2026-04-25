---
name: No Color-Only Encoding — Always Add Labels, Icons, or Patterns
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/03-color/no-red-green-only.md, corpus/ux-principles/audit/03-color/semantic-colors.md, corpus/ux-principles/audit/03-color/wcag-aa-contrast.md]
---

# No Color-Only Encoding — Always Add Labels, Icons, or Patterns

## What it is

Never rely on color alone to convey meaning. If a chart, badge, status, or differentiation depends entirely on color to be understood, it fails colorblind users (~8% of men, 0.5% of women have some form of color vision deficiency) and users in monochrome conditions (printing, e-ink readers, high-contrast modes).

Always pair color with a redundant cue: a label, an icon, a pattern, a position, or a shape.

## Why it matters

Roughly 1 in 12 men cannot reliably distinguish red from green. A "green = good, red = bad" signal that has no icon or label is invisible to them. The same applies to status badges, chart legends, form validation, and any UI element where color is the only differentiator.

This is a WCAG 2.1 Level A requirement — the most basic level. Failing it is not a polish issue; it's an accessibility defect.

## How to apply

1. **Pair color with a non-color cue:**
   - Status badges: color + icon + text label.
   - Chart series: color + dashed/solid line patterns + labeled directly on the chart.
   - Form errors: red border + error icon + descriptive text below the field.
   - Required fields: red asterisk + the word "required" or aria-required.
2. **Audit every color-encoded element.** Remove the color (mentally render in grayscale). Is the meaning still clear? If no, add a redundant cue.
3. **Use Chrome DevTools' "Emulate vision deficiency" feature** to test grayscale, protanopia, deuteranopia views.

## Examples

- **GOOD:** Status pill: green background + checkmark icon + "Active" label. Three redundant cues.
- **BAD:** Three colored dots (red, yellow, green) as status indicators with no labels. Colorblind users see three identical-looking dots.
- **GOOD:** A line chart where each series has a different color AND a different line style (solid, dashed, dotted) AND is labeled directly on the line.
- **BAD:** A chart where the legend says "blue = revenue, red = costs" — colorblind users can't distinguish the lines.
- **GOOD:** Form error: `aria-invalid="true"`, red border, an error icon, and "Email is required" text below.
- **BAD:** Form error: red border only. Colorblind users see... a border.

## Related entries

- `corpus/ux-principles/audit/03-color/no-red-green-only.md`
- `corpus/ux-principles/audit/03-color/semantic-colors.md`
- `corpus/ux-principles/audit/03-color/wcag-aa-contrast.md`

## Anti-patterns

- "We use red for errors so users know it's an error." Not all users can see red.
- Charts with default color palettes that use red and green adjacent to each other.
- Status indicators that are "subtle" — color only, no label, "to keep the UI clean."
