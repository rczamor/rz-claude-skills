---
name: Every Animation Must Have a Purpose
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/07-motion/easing-rules.md, corpus/ux-principles/audit/07-motion/prefers-reduced-motion.md]
---

# The Purpose Rule

## What it is
Every animation must communicate one of three things: **state change** (toggle on/off, loading → loaded), **attention** (new item arriving, error needing focus), or **spatial relationship** (this element came from there, this drawer slid in from the right). Animation without a purpose is decoration, and decoration is friction.

## Why it matters
Motion is the most expensive design choice in terms of attention and battery. Every gratuitous animation steals focus from the next user action, and on lower-end devices it stutters and degrades the entire impression. The test: if you remove the animation, does the user lose information? If no — delete it.

## How to apply
- Audit every transition / animation in the codebase against the three purposes:
  - **State change** — checkbox toggling, button press feedback, optimistic UI.
  - **Attention** — toast appearing, badge incrementing, error shake.
  - **Spatial relationship** — modal sliding in from a card, item moving in a list, route transition.
- If it doesn't fit, ask: would a hard cut work just as well? If yes, hard-cut.
- Animations on idle decorative elements (rotating gradients, floating blobs, pulsing icons "to add life") almost always fail this rule. They're the visual equivalent of fidget spinners.
- Onboarding "delight" animations are the most common offender — users see them once and tolerate them; on the 50th login they're pure friction.

## Examples (BAD vs. GOOD pairs)

BAD: a continuously pulsing gradient on the hero "to add motion." Communicates nothing, distracts everywhere, depletes battery.

GOOD: a tab indicator slides under the active tab when the user taps a different one — communicates *"this is now selected and it came from there."*

## Related entries
- `corpus/ux-principles/audit/07-motion/easing-rules.md` — once you've decided motion belongs, give it correct physics.
- `corpus/ux-principles/audit/07-motion/prefers-reduced-motion.md` — even purposeful motion must be opt-out-able.

## Anti-patterns
- Pulsing / glowing CTAs to "draw attention" — ends up looking like an ad.
- Animated number counters on every metric card — once is delightful, on the dashboard it's noise.
- Page transitions that animate the entire layout on every route change — users wait for the product instead of using it.
