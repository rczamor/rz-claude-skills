---
name: Users Satisfice
domain: ux-principles
source_skill: design-review
entry_type: concept
length_target: 300-800
related: [corpus/ux-principles/principles/users-scan-not-read.md, corpus/ux-principles/principles/law-2-clicks-dont-matter-thinking-does.md, corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md]
---

# Users Satisfice

## What it is

"Satisfice" is Herbert Simon's term: users pick the first reasonable option, not the best one. They are not optimizers — they are time-constrained humans who stop searching the moment they find something that plausibly works. This means whatever appears first, biggest, brightest, or most salient is usually the choice that gets made, regardless of whether better options exist further down.

The design implication: make the right choice the most visible choice. Don't expect users to scan the full menu and pick optimally.

## Why it matters

If a user is choosing between three plans and the middle plan is most prominent, that's the plan they pick — not because it's best for them, but because it's loudest. Designers who treat users as careful comparison shoppers consistently produce pages where the wrong path wins. Worse: when the prominent path is the wrong one, the user ends up frustrated and blames the product, not their snap decision.

## How to apply

1. **Make the recommended action the visually dominant one.** One primary CTA per view, distinctly more prominent than secondary actions.
2. **Order options intentionally.** First option in a list, leftmost tab, top-of-screen card — these get disproportionate clicks. Put the right thing there.
3. **Don't bury the answer.** If users want pricing, put pricing where they look first. Don't make them satisfice on the wrong page.
4. **Test by removing.** If you removed every secondary option, would users still find what they need via the primary path? If yes, the hierarchy is correct.

## Examples

- **GOOD:** A SaaS pricing page with the recommended tier visually elevated (border, "Most popular" badge, slightly larger card). Users satisfice into the right choice.
- **BAD:** Three identical pricing cards with equal weight. Users default to the cheapest or leftmost without comparing — designer's intended path lost.
- **GOOD:** Apple's checkout — "Continue with Apple Pay" rendered as the dominant button, "Continue with credit card" as a secondary text link. Most users pick Apple Pay because it satisfices visually.
- **BAD:** A signup screen with three equally weighted options: "Sign in with Google", "Sign in with email", "Sign in with SSO". User pauses, must compare, picks wrong, abandons.

## Related entries

- `corpus/ux-principles/principles/users-scan-not-read.md` — scanning + satisficing reinforce each other
- `corpus/ux-principles/principles/law-2-clicks-dont-matter-thinking-does.md` — satisficing means each step needs an obvious answer
- `corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md` — one primary CTA per view

## Anti-patterns

- "Users should compare options carefully." Users won't. Make the comparison unnecessary.
- A/B testing equal-weight options forever instead of admitting the design has not picked a winner.
