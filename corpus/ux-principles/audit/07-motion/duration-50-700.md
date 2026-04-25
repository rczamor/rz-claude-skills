---
name: Animation Duration 50–700ms
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/07-motion/easing-rules.md, corpus/ux-principles/audit/07-motion/purpose-rule.md]
---

# Duration 50–700ms

## What it is
UI transition durations live between 50ms and 700ms. Most micro-interactions land in 150–250ms. Page transitions can stretch toward 700ms when they communicate spatial relationship. Anything longer than 700ms in regular UI is too slow — it makes the product feel sluggish.

## Why it matters
Below ~80ms motion isn't perceived — it just looks like a snap, which is fine for hover states but loses the "physicality" affordance for state changes. Above ~400ms users start tapping again because they think nothing happened. Above 700ms motion becomes the bottleneck — the user is faster than your product, and that's the worst feeling on the web.

## How to apply
- Hover / focus state — 100–150ms.
- Toggle / button press — 100–200ms.
- Toast / popover enter — 200–300ms with ease-out.
- Modal / drawer enter — 250–350ms.
- Page transition (route change with shared element) — up to 500–700ms only when communicating spatial movement.
- Loading spinner — continuous, but each rotation 800–1200ms.
- Centralize as tokens: `--dur-fast: 150ms`, `--dur-base: 250ms`, `--dur-slow: 400ms`.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
.card-flip { transition: transform 1.2s ease-in-out; } /* slow */
.button { transition: background 800ms ease; } /* hover feels broken */
```

GOOD:
```css
:root {
  --dur-fast: 120ms;
  --dur-base: 240ms;
  --dur-slow: 360ms;
}
.button { transition: background var(--dur-fast) var(--ease-standard); }
.modal-enter { transition: transform var(--dur-slow) var(--ease-out), opacity var(--dur-base) var(--ease-out); }
```

## Related entries
- `corpus/ux-principles/audit/07-motion/easing-rules.md` — the curve that fills the duration.
- `corpus/ux-principles/audit/07-motion/purpose-rule.md` — every animation must justify its duration.

## Anti-patterns
- 1000ms+ enter animations as "delight" — actually friction.
- 50ms enter on a modal — looks like a glitch, not a transition.
- Page-load splash that animates for 2s — almost always cuts conversion.
