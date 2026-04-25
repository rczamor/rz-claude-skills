---
name: Dark Mode — Text ~#E0E0E0, Not Pure White
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/dark-mode-elevation.md, corpus/ux-principles/audit/03-color/wcag-aa-contrast.md]
---

# Dark Mode — Text ~#E0E0E0, Not Pure White

## What it is

In dark mode, body text should be off-white — typically around `#E0E0E0` to `#EDEDED` — not pure `#FFFFFF`. Pure white on dark backgrounds creates excessive contrast, causing eye strain (the white "burns" the eye), and visual halation where letterforms appear to glow at their edges.

Material Design recommends `rgba(255, 255, 255, 0.87)` for high-emphasis text — about 87% opacity, equivalent to `#DEDEDE`-ish.

## Why it matters

The whole point of dark mode is to reduce eye strain in low-light conditions. Pure white text on near-black backgrounds defeats that goal — the contrast (21:1) is uncomfortable for sustained reading. Slightly off-white text (~14:1 contrast) is easier on the eyes while still well above the WCAG AA 4.5:1 floor.

This is a small detail that distinguishes a designed dark mode from an auto-generated inversion.

## How to apply

1. **Body text in dark mode:** `color: #E5E5E5` or `color: rgba(255, 255, 255, 0.87)`.
2. **Headings:** `#F5F5F5` (slightly brighter than body) or `rgba(255, 255, 255, 0.95)`.
3. **De-emphasized text:** `rgba(255, 255, 255, 0.6)` — about `#999`.
4. **Verify contrast** still hits 4.5:1 against the surface. On `#121212` background, `#E0E0E0` text = ~14:1. Fine.
5. **Audit:** check `getComputedStyle(p).color` on body text in dark mode. If it's `rgb(255, 255, 255)`, fix.

## Examples

- **GOOD:**
  ```css
  [data-theme="dark"] body {
    color: rgba(255, 255, 255, 0.87);
    background: #121212;
  }
  ```
- **BAD:**
  ```css
  [data-theme="dark"] body {
    color: #FFFFFF;
    background: #000000;
  }
  ```
  Pure white on pure black — burns the eye after a paragraph.
- **GOOD:** GitHub's dark mode — text at `#E6EDF3`, base at `#0D1117`. Comfortable for long reading.
- **BAD:** A dark mode toggle that just sets `color: #FFF` on the body. Eye strain in 30 seconds.

## Related entries

- `corpus/ux-principles/audit/03-color/dark-mode-elevation.md`
- `corpus/ux-principles/audit/03-color/wcag-aa-contrast.md`

## Anti-patterns

- "We want maximum contrast in dark mode for accessibility." Excess contrast hurts; aim for AAA-comfortable, not eye-burning.
- Using `#FFF` text everywhere because the design system defaults to `white` in dark mode.
