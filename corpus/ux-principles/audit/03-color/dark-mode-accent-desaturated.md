---
name: Dark Mode — Primary Accent Desaturated 10-20%
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/dark-mode-elevation.md, corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md]
---

# Dark Mode — Primary Accent Desaturated 10-20%

## What it is

Brand accent colors that look right in light mode usually need to be desaturated by 10-20% in dark mode. A vibrant `#3B82F6` blue that pops on a white background looks neon and vibrating on a dark background — the eye's perception shifts in low-light environments, and saturated colors appear hyper-saturated against dark surfaces.

The fix: define a dark-mode variant of every brand accent that's slightly toned down.

## Why it matters

Saturated colors against dark backgrounds produce a glowing, eye-fatiguing effect — especially blues, purples, and reds. The same hue at lower saturation reads as confident and professional in dark mode. This is why most well-designed dark themes feel calm, while auto-inverted dark themes feel jarring.

This is one of the highest-leverage dark-mode tweaks. Single-line CSS change, instant polish improvement.

## How to apply

1. **Define light + dark variants of every accent token:**
   ```css
   :root {
     --color-primary: #3B82F6;
   }
   [data-theme="dark"] {
     --color-primary: #60A5FA;  /* desaturated, slightly lighter */
   }
   ```
2. **Use HSL to make the desaturation explicit:**
   ```css
   /* light */ --color-primary: hsl(217, 91%, 60%);
   /* dark */  --color-primary: hsl(217, 75%, 65%);  /* lower saturation, slightly higher lightness */
   ```
3. **Audit:** in dark mode, do brand colors look "neon" or "buzzing"? Desaturate.
4. **Test on actual hardware.** OLED panels render saturated colors more intensely than LCD.

## Examples

- **GOOD:** Light mode primary `#3B82F6` → dark mode primary `#60A5FA` (slightly lighter, lower sat). Same hue, different intensity.
- **BAD:** Using the same `#3B82F6` in both modes. In dark mode, looks fluorescent.
- **GOOD:** Linear's dark mode — purples and blues clearly toned down from the brand palette.
- **BAD:** A brand violet `#7C3AED` used as-is in dark mode. Vibrates.

## Related entries

- `corpus/ux-principles/audit/03-color/dark-mode-elevation.md`
- `corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md`

## Anti-patterns

- Using identical accent colors across light and dark modes. Saves time, costs polish.
- Boosting saturation in dark mode "to make it pop." Already pops; you're making it scream.
