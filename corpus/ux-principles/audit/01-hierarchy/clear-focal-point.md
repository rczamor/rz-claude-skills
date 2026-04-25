---
name: Clear Focal Point — One Primary CTA Per View
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/principles/users-satisfice.md, corpus/ux-principles/principles/billboard-design-overview.md, corpus/ux-principles/audit/01-hierarchy/squint-test.md]
---

# Clear Focal Point — One Primary CTA Per View

## What it is

Every view should have exactly one primary call-to-action that is visually dominant — larger, higher-contrast, and more weighted than every other interactive element on screen. Secondary actions exist, but they recede. The user's eye should land on the primary CTA without searching.

If a view has two equally weighted CTAs, the design has two primary CTAs — which means it has none.

## Why it matters

Users satisfice: they pick the first reasonable option, not the best. If two options look equally important, the user either picks the leftmost one (often wrong) or pauses to decide (Law 1 violation). One dominant CTA per view eliminates that pause and routes the satisficing user into the intended path.

## How to apply

1. **Identify the one action you want this view to drive.** Sign up. Save. Purchase. Continue. Pick one.
2. **Make it visually loudest.** Solid background color, larger size, more prominent position (often bottom-right of forms, center of hero sections).
3. **Demote secondary actions.** Outline buttons, text links, smaller font weight.
4. **Run the squint test.** Blur the page; the primary CTA should still be visible.

## Examples

- **GOOD:** A signup page with a solid `#2563EB` "Create account" button (44×200px) and a small text link "Already have an account? Sign in." underneath.
- **BAD:** Two equally-sized buttons side by side: "Sign up" and "Sign in" — equal weight forces the user to think.
- **GOOD:** Stripe checkout — one black "Pay" button, every other element a quiet form field or secondary text link.
- **BAD:** A pricing page with three identical "Get started" buttons across three tiers. No focal point, user paralyzes.

## Related entries

- `corpus/ux-principles/principles/users-satisfice.md`
- `corpus/ux-principles/principles/billboard-design-overview.md`
- `corpus/ux-principles/audit/01-hierarchy/squint-test.md`

## Anti-patterns

- Making "Sign up" and "Sign in" equally prominent because "we don't want to bias users." The user wants to be biased toward the path you want them to take.
- Branded buttons everywhere — five primary-color buttons on a page = no primary at all.
