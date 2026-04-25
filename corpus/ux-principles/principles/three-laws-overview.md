---
name: Three Laws of Usability
domain: ux-principles
source_skill: design-review
entry_type: framework
length_target: 300-800
related: [corpus/ux-principles/principles/law-1-dont-make-me-think.md, corpus/ux-principles/principles/law-2-clicks-dont-matter-thinking-does.md, corpus/ux-principles/principles/law-3-omit-then-omit-again.md, corpus/evaluation-frameworks/cognitive-patterns/15-hierarchy-as-service.md, corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md]
---

# Three Laws of Usability

## What it is

Three foundational laws that govern how every interface should be designed and evaluated. They are not suggestions — they are observed behavioral truths about how humans interact with screens, distilled into testable rules:

1. **Don't make me think.** Every page should be self-evident. If a user stops to think "What do I click?" or "What does this mean?", the design has failed. Self-evident > self-explanatory > requires explanation.
2. **Clicks don't matter, thinking does.** Three mindless, unambiguous clicks beat one click that requires thought. Each step should feel like an obvious choice (animal, vegetable, or mineral), not a puzzle.
3. **Omit, then omit again.** Get rid of half the words on each page, then get rid of half of what's left. Happy talk (self-congratulatory text) must die. Instructions must die. If they need reading, the design has failed.

## Why it matters

These laws keep designers honest. Most "polish" debates collapse against them. If law 1 fails, no amount of brand voice fixes the page. If law 2 fails, optimizing click count makes the experience worse. If law 3 fails, the page sounds like a marketing brochure when it should be a tool. The laws are diagnostic — they tell you where the failure lives, not just that one exists.

## How to apply

1. **Sequence them.** Apply law 1 first (clarity), then law 2 (mindless choices), then law 3 (omit). Don't skip to typography polish if law 1 fails.
2. **Use them as audit anchors.** When reviewing a page, ask in order: "Did I have to think? Did any click require thought? Are there words or instructions I'd remove?"
3. **Frame findings against them.** "This is a Law 1 violation: the primary CTA is ambiguous" is more actionable than "the CTA is unclear."
4. **Apply at every level.** Not just landing pages — onboarding, settings, errors, modals. The laws don't graduate.

## Examples

- **Law 1 win:** Stripe checkout. Card field, email, pay. No thinking required about what to fill or what happens next.
- **Law 2 win:** TurboTax's question-by-question flow. Many clicks, each unambiguous ("Are you married? Yes/No"), beats one screen with 40 fields.
- **Law 3 win:** Linear's empty state on a new project: "Create your first issue" + button. No "Welcome to Linear, your team's modern issue tracker..."

## Related entries

- `corpus/ux-principles/principles/law-1-dont-make-me-think.md`
- `corpus/ux-principles/principles/law-2-clicks-dont-matter-thinking-does.md`
- `corpus/ux-principles/principles/law-3-omit-then-omit-again.md`
- `corpus/evaluation-frameworks/cognitive-patterns/15-hierarchy-as-service.md` — hierarchy serves the user, not the designer
- `corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md` — removing > adding

## Anti-patterns

- Treating the laws as "best practices" to weigh against business goals. They aren't tradeoffs — violation is failure.
- Applying them only to landing pages. Internal tools, settings panels, and error states violate these laws constantly.
