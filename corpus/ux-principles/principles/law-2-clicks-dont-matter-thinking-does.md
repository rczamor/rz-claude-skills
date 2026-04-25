---
name: "Law 2: Clicks Don't Matter, Thinking Does"
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-800
related: [corpus/ux-principles/principles/three-laws-overview.md, corpus/ux-principles/principles/law-1-dont-make-me-think.md, corpus/ux-principles/audit/05-interaction/mindless-choice-audit.md, corpus/ux-principles/principles/users-satisfice.md]
---

# Law 2: Clicks Don't Matter, Thinking Does

## What it is

Three mindless, unambiguous clicks beat one click that requires thought. The number of steps in a flow is irrelevant — what matters is whether each step feels like an obvious choice (animal, vegetable, or mineral) or a puzzle. The cost of a click is roughly zero. The cost of a thought is enormous.

This law inverts a common designer instinct: "minimize clicks." Optimize for cognitive ease per step, not step count.

## Why it matters

A two-click flow that asks "Did you mean A or B?" at each step depletes the user. A four-click flow where every choice is binary and obvious feels frictionless. Users will happily click through ten screens of a wizard if every screen asks one clear question. They will abandon a single-screen form if it asks them to figure out what each field means.

This is why TurboTax beats spreadsheet-style tax forms. Why airline websites win when they ask "Round-trip or one-way?" first instead of throwing 12 fields on screen. Why command palettes beat dense toolbars.

## How to apply

1. **Audit each decision point.** For every button, link, dropdown, or modal choice — is it instantly obvious what happens? If a user would pause to reread the label, the click is not mindless.
2. **Break dense screens into sequential mindless screens.** A form with 20 fields → a wizard with 5 screens of 4 fields each.
3. **Pre-answer obvious questions.** Default the most common option. Skip steps where there's only one reasonable answer.
4. **Don't conflate clicks with friction.** Friction is mental effort, not motor effort. Clicking a button is free; deciding whether to click it is not.

## Examples

- **GOOD:** Booking.com's flight search — round-trip vs. one-way as first choice. Then dates. Then passengers. Each click trivial; many clicks feel fast.
- **BAD:** A "minimal" landing page with one ambiguous "Get Started" button that drops you into a 14-field form with no guidance.
- **GOOD:** Linear's keyboard shortcuts — 5 keypresses to assign an issue, change its status, and add a comment. Every step a single, obvious action.
- **BAD:** A single mega-modal with 9 dropdowns the user must understand before submitting.

## Related entries

- `corpus/ux-principles/principles/three-laws-overview.md`
- `corpus/ux-principles/principles/law-1-dont-make-me-think.md`
- `corpus/ux-principles/audit/05-interaction/mindless-choice-audit.md` — the operationalized audit rule
- `corpus/ux-principles/principles/users-satisfice.md` — users pick the first reasonable option

## Anti-patterns

- "We reduced the flow from 5 clicks to 2!" — and made each click 3x harder. Net: worse.
- Designing for the click-count metric instead of the thought-count metric.
