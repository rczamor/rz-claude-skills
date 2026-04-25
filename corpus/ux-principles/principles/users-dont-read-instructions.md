---
name: Users Don't Read Instructions
domain: ux-principles
source_skill: design-review
entry_type: concept
length_target: 300-800
related: [corpus/ux-principles/principles/law-3-omit-then-omit-again.md, corpus/ux-principles/audit/08-content/instructions-detection.md, corpus/ux-principles/principles/users-muddle-through.md]
---

# Users Don't Read Instructions

## What it is

Users dive in. They do not stop to read documentation, onboarding tours, splash screens, or "before you begin" notices. Guidance must be brief, timely, and unavoidable, or it will not be seen. A help article that explains how the feature works is a tax users refuse to pay; an inline hint that appears at the moment of confusion is sometimes useful, but only sometimes.

The corollary: any design that depends on users reading instructions has already failed. Fix the design, not the instructions.

## Why it matters

Teams routinely respond to user confusion by writing more documentation. They add tooltips. They add onboarding modals. They add "Watch the video" links. None of these get read. The user encounters the same confusion, hits the same wall, and either abandons the product or learns a workaround that the team didn't anticipate.

Documentation is a debt the design owes the user. Every line of help text exists because the interface failed to be self-evident. Treating documentation as the solution prolongs the failure.

## How to apply

1. **Treat instructions as design defects.** When you see explanatory text on a page, ask: "What's broken about the interaction that this text is compensating for?" Fix that.
2. **If guidance is needed, make it timely and unavoidable.** Inline at the moment of decision, in the user's path, brief enough to scan in 2 seconds.
3. **Kill onboarding tours.** Users skip them. Put the same information into the interface itself: defaults, placeholder text, smart empty states.
4. **Audit "Welcome to X" copy.** It's never read. Replace with the first useful action.

## Examples

- **GOOD:** Linear's empty state when you create a new project: "Create your first issue" + a button. No tour, no tutorial.
- **BAD:** A SaaS app that opens with a 5-step modal tour explaining what each menu does. Users press Esc on every screen.
- **GOOD:** Stripe's API docs — every example is copy-pasteable code, no "before you begin" preamble.
- **BAD:** A field labeled "Account ID" with helper text "Your account ID is a 16-character alphanumeric string that can be found in your settings under Account → Identifiers → API Account ID." (Just put a link to "Find my account ID" or pre-fill it.)

## Related entries

- `corpus/ux-principles/principles/law-3-omit-then-omit-again.md` — instructions are the first thing to omit
- `corpus/ux-principles/audit/08-content/instructions-detection.md` — the audit rule
- `corpus/ux-principles/principles/users-muddle-through.md` — muddlers especially skip instructions

## Anti-patterns

- "We documented it in the help center." The help center is a graveyard of unread answers.
- Adding tooltips to compensate for ambiguous labels instead of fixing the labels.
