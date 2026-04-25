---
name: No `transition: all`
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/07-motion/animate-only-transform-opacity.md, corpus/ux-principles/audit/07-motion/duration-50-700.md]
---

# No `transition: all`

## What it is
List the properties you intend to animate explicitly — never use `transition: all`. The `all` shorthand transitions every animatable property change, which causes unintended motion on layout shifts, font loads, and class toggles, and silently kills performance.

## Why it matters
`transition: all` is the lazy-developer special. It looks tidy but causes three problems: (1) layout properties accidentally animate (top, left, width), forcing layout recalc on every frame; (2) font-load triggers an unintended typography transition; (3) unrelated class changes (e.g., adding a `disabled` state) cascade through every transitionable property in unexpected ways. Explicit lists are deliberate and faster.

## How to apply
- Replace `transition: all <duration> <easing>` with explicit property lists:
  ```css
  transition:
    background-color 150ms var(--ease-standard),
    transform 150ms var(--ease-standard),
    box-shadow 150ms var(--ease-standard);
  ```
- Stick to GPU-cheap properties: `transform`, `opacity`, `background-color`, `color`, `border-color`, `box-shadow`, `filter`. Avoid layout properties (width, height, top, left, margin, padding) — see the related rule.
- Lint rule: ESLint with `stylelint-no-unknown-syntax` or a custom rule flagging `transition: all`.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
.button { transition: all 200ms ease; }
/* hover state changes background, transform, box-shadow — but font-display swap also briefly transitions, and a width recalc on resize causes a frame-stall */
```

GOOD:
```css
.button {
  transition:
    background-color 150ms var(--ease-standard),
    box-shadow 150ms var(--ease-standard),
    transform 150ms var(--ease-standard);
}
```

## Related entries
- `corpus/ux-principles/audit/07-motion/animate-only-transform-opacity.md` — the property-choice rule.
- `corpus/ux-principles/audit/07-motion/duration-50-700.md` — duration rule.

## Anti-patterns
- `transition: all 0.3s ease` on every button — what most CSS tutorials still ship.
- Adding a `transition: all` to a parent and finding child elements have unrelated 300ms delays.
- Using `transition: all` for "future-proofing" — actually un-future-proofs everything.
