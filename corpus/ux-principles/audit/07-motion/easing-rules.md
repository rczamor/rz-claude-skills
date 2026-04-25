---
name: Easing Rules — Ease-Out / Ease-In / Ease-In-Out
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/07-motion/duration-50-700.md, corpus/ux-principles/audit/07-motion/purpose-rule.md]
---

# Easing Rules

## What it is
Use **ease-out** for elements entering the screen, **ease-in** for elements exiting, and **ease-in-out** for elements moving between two on-screen positions. Linear easing should be reserved for continuous motion (loading spinners), not transitions.

## Why it matters
Easing communicates physics. Things that come into view should arrive *and slow down* (ease-out feels like landing). Things that leave should *accelerate away* (ease-in feels like a release). Items moving from one place to another need both. Linear easing on a transition feels mechanical, robotic, and is the cheapest "I didn't think about motion" tell.

## How to apply
- Entering / appearing — `cubic-bezier(0.16, 1, 0.3, 1)` or `ease-out` (≈0.25, 0.1, 0.25, 1 in CSS keyword form).
- Exiting / dismissing — `cubic-bezier(0.7, 0, 0.84, 0)` or `ease-in`.
- Moving between two states — `cubic-bezier(0.4, 0, 0.2, 1)` or `ease-in-out` (Material's "standard" curve).
- Spring physics (`react-spring`, Framer Motion `spring`) is acceptable for entering/moving where you want a small overshoot — never for pure exits.
- Centralize easing as design tokens: `--ease-out`, `--ease-in`, `--ease-standard` — don't sprinkle bezier values inline.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
.modal { transition: opacity 200ms linear, transform 200ms linear; } /* feels robotic */
.toast-enter { transition: transform 200ms ease-in; } /* enters with deceleration backwards */
```

GOOD:
```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in:  cubic-bezier(0.7, 0, 0.84, 0);
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
}
.toast-enter { transition: transform 240ms var(--ease-out); }
.toast-exit  { transition: transform 180ms var(--ease-in); }
.tab-indicator { transition: transform 200ms var(--ease-standard); }
```

## Related entries
- `corpus/ux-principles/audit/07-motion/duration-50-700.md` — easing without the right duration falls flat.
- `corpus/ux-principles/audit/07-motion/purpose-rule.md` — why motion exists at all.

## Anti-patterns
- Linear on UI transitions — looks like default 1995 web.
- The same easing on enter and exit — kills the hierarchy between the two.
- Springs with high bounce on an exit — looks like a glitch.
