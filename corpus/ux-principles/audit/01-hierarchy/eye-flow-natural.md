---
name: Eye Flow — Natural Top-Left to Bottom-Right
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/principles/users-scan-not-read.md, corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md]
---

# Eye Flow — Natural Top-Left to Bottom-Right

## What it is

In left-to-right reading cultures, eyes scan in F-shaped or Z-shaped patterns: top-left first, then across, then down to the next line. Layouts should align with this pattern. The most important content goes top-left or follows the F-shape; conclusions, summaries, or primary CTAs land at the natural end of the eye's path (often bottom-right of a section).

Designs that fight the F-pattern — important content in the bottom-left, primary CTA hidden in the top-right of a long page — make the user work to find what matters.

## Why it matters

Eye-tracking research is unambiguous: users do not scan reading-equally across the page. Heatmaps show concentrated attention at the top-left and along the F-shape. Putting key content outside that pattern means it gets less attention. Designing with the pattern means scarce attention lands where you want it.

## How to apply

1. **Top-left = highest attention.** Logo, page title, primary headline.
2. **Follow the F-shape down.** Section headings on the left, body text spreading right.
3. **End each section with the action.** Bottom-right of a card or section is where the eye naturally lands; place the CTA there.
4. **Audit by tracing the eye path.** Where would your eye go first? Second? Third? Are those the three things the designer intended?

## Examples

- **GOOD:** A landing page with logo top-left, headline next, body text in F-pattern, "Get started" CTA at the bottom-right of the hero. Natural flow.
- **BAD:** A pricing page where the "Most popular" tier is leftmost (out of view in F-shape) instead of center-right where eyes land.
- **GOOD:** A dashboard with primary metric top-left, secondary metrics flowing right, recent activity cascading down — eye gets the headline first, drills in by choice.
- **BAD:** A form where "Submit" is top-left, above the fields. Eye skips it on first scan, finds it after reading the form.

## Related entries

- `corpus/ux-principles/principles/users-scan-not-read.md`
- `corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md`

## Anti-patterns

- "We center everything for visual balance." Centering everywhere defeats the F-pattern and creates ambiguous flow.
- RTL layouts forced into LTR design — reverse for RTL users instead of fighting it.
