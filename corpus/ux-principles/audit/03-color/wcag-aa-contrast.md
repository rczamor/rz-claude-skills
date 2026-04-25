---
name: WCAG AA Contrast — Body 4.5:1, Large 3:1, UI 3:1
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/03-color/no-color-only-encoding.md, corpus/ux-principles/audit/02-typography/caption-min-12px.md, corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md]
---

# WCAG AA Contrast — Body 4.5:1, Large 3:1, UI 3:1

## What it is

WCAG 2.1 Level AA requires minimum contrast ratios between text and its background:

- **Body text:** at least **4.5:1** contrast ratio.
- **Large text** (18pt / 24px+, or 14pt / 18.66px+ bold): at least **3:1**.
- **UI components and graphical objects** (buttons, form fields, icons that convey meaning): at least **3:1** against adjacent colors.

The contrast ratio is a numeric measure of luminance difference — pure black on pure white is 21:1; light gray on white can be under 2:1.

## Why it matters

Insufficient contrast is the most common accessibility failure. It excludes users with low vision, color blindness, and anyone using a screen in bright sunlight. Beyond accessibility, poor contrast also fatigues all users — readability drops sharply below 4.5:1.

Most "minimal" or "elegant" gray-on-light-gray designs fail this test. The aesthetic of low-contrast type is a style choice that punishes users.

## How to apply

1. **Audit:** use a tool — Chrome DevTools, axe, Lighthouse, Stark — to compute ratios.
2. **Body text:** ratio ≥ 4.5:1. `#1F2937` on `#FFF` = 12.6:1 (great). `#9CA3AF` on `#FFF` = 2.5:1 (fails).
3. **Large text:** ratio ≥ 3:1. Slightly more lenient because larger text is more legible at lower contrast.
4. **UI components:** ≥ 3:1 between the component's outline / fill and its surroundings. A pale border `#E5E7EB` on white is 1.3:1 — fails.
5. **Brand colors are no excuse.** If your brand color is light yellow, body text on it must still hit 4.5:1.

## Examples

- **GOOD:** Body text `#111827` on `#FFFFFF` background = 19.6:1 contrast. Far exceeds 4.5:1.
- **GOOD:** Large heading `#374151` on `#FFFFFF` = 9.5:1.
- **BAD:** Body text `#9CA3AF` on `#FFFFFF` = 2.5:1. Fails AA. Common "minimal" design failure.
- **BAD:** Button text `#FFFFFF` on `#FCD34D` (yellow) = 1.7:1. Fails. Yellow buttons need dark text.
- **GOOD:** Button text `#000000` on `#FCD34D` = 12.4:1.

## Related entries

- `corpus/ux-principles/audit/03-color/no-color-only-encoding.md`
- `corpus/ux-principles/audit/02-typography/caption-min-12px.md`
- `corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md`

## Anti-patterns

- "Our brand is light gray; body text in light gray for consistency." Consistency that fails AA is a defect.
- Designing in a perfectly lit office and forgetting that real users use phones in sunlight.
- Using `#FFF` text on `#FFC` yellow (1.04:1, essentially invisible).
