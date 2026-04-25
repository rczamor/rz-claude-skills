---
name: Respect `prefers-reduced-motion`
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/07-motion/purpose-rule.md, corpus/ux-principles/audit/07-motion/easing-rules.md]
---

# `prefers-reduced-motion` Respected

## What it is
The `prefers-reduced-motion: reduce` media query lets users with vestibular disorders, migraine triggers, or general sensitivity opt out of motion. Sites that ignore it can literally make users physically ill. Honoring it is an accessibility requirement (WCAG 2.1 SC 2.3.3) and a baseline-quality signal.

## Why it matters
Vestibular disorders affect ~35% of adults at some point. Parallax scrolling, full-page transitions, and bouncing animations can trigger nausea, dizziness, and migraines. Respecting `prefers-reduced-motion` doesn't mean "no motion ever" — it means *replace large/complex motion with subtle alternatives* (cross-fade instead of slide, instant state-change instead of bounce).

## How to apply
- Wrap non-essential motion in:
  ```css
  @media (prefers-reduced-motion: no-preference) {
    .modal-enter { animation: slide-in 320ms var(--ease-out); }
  }
  @media (prefers-reduced-motion: reduce) {
    .modal-enter { animation: fade-in 100ms linear; } /* still gives state-change cue */
  }
  ```
- For Framer Motion / React Spring: use `useReducedMotion()` and serve a non-motion variant.
- Check at build time:
  ```js
  matchMedia('(prefers-reduced-motion: reduce)').matches
  ```
- Always preserve essential motion *information* — don't just kill the animation and leave users without state-change feedback. Replace it with a subtle fade or instant change.
- Test by enabling Reduce Motion in System Preferences (macOS) or Accessibility Settings (iOS/Android).

## Examples (BAD vs. GOOD pairs)

BAD: parallax-scrolling hero with floating elements that ignore `prefers-reduced-motion` and continue to animate. Migraine machine.

GOOD:
```css
.hero-parallax { transform: translateY(var(--scroll-offset)); }
@media (prefers-reduced-motion: reduce) {
  .hero-parallax { transform: none; }
}
```

## Related entries
- `corpus/ux-principles/audit/07-motion/purpose-rule.md` — purposeful motion still needs an opt-out.
- `corpus/ux-principles/audit/07-motion/easing-rules.md` — when reducing, prefer fades to slides.

## Anti-patterns
- Suppressing motion globally with `* { animation: none !important }` — kills loading spinners and essential feedback too.
- Implementing `prefers-reduced-motion` only on marquee marketing animations and ignoring product UI.
- Believing "no one uses this setting" — over 18% of macOS users have it on.
