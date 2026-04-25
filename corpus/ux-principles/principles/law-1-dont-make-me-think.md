---
name: "Law 1: Don't Make Me Think"
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-800
related: [corpus/ux-principles/principles/three-laws-overview.md, corpus/ux-principles/principles/users-scan-not-read.md, corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md, corpus/ux-principles/audit/05-interaction/mindless-choice-audit.md]
---

# Law 1: Don't Make Me Think

## What it is

Every page should be self-evident. If a user stops to think "What do I click?" or "What does this mean?", the design has failed. The hierarchy of clarity is:

1. **Self-evident** — the user knows without effort what to do.
2. **Self-explanatory** — the user can figure it out by reading the labels.
3. **Requires explanation** — the user needs documentation, a tour, or a second pair of eyes.

Aim for self-evident. Settle for self-explanatory. Treat "requires explanation" as a defect to be fixed, not a feature to be documented.

## Why it matters

Thinking is the most expensive thing a user can do on your interface. Every micro-pause — "Is this a button or a label?", "Does this mean save or send?", "Where do I go from here?" — depletes attention, builds frustration, and increases the chance of the user bouncing or making a wrong choice. Cognitive load is the budget every interface spends; clarity is how you save it.

## How to apply

1. **Watch a real user (or imagine one).** If their eyes pause anywhere, that's a thinking moment. Annotate it.
2. **Replace ambiguous labels with verbs + nouns.** "Continue" → "Save API Key". "Submit" → "Send Invoice". The user should know what happens before clicking.
3. **Use convention, not invention.** Logo top-left, search top-right, primary action high-contrast. Don't reinvent placement to be clever.
4. **Test the page area test.** Point at each clearly defined region. Can you instantly name its purpose ("Things I can buy", "How to search")? Areas you can't name in 2 seconds are poorly defined.

## Examples

- **GOOD:** "Save API Key" button in a settings page — explicit verb + object, the user knows exactly what is being saved.
- **BAD:** "OK" / "Continue" / "Submit" — generic labels that force the user to mentally reconstruct what's about to happen.
- **GOOD:** Linear's command bar (Cmd+K) shows "Create issue", "Assign to me", "Change status" — each a verb + noun, no ambiguity.
- **BAD:** A modal with "Yes" / "No" / "Cancel" buttons against a question phrased as "Would you like to discard your unsaved changes and proceed?" — the user has to re-read the question to map "Yes" to an action.

## Related entries

- `corpus/ux-principles/principles/three-laws-overview.md` — the framework this law belongs to
- `corpus/ux-principles/principles/users-scan-not-read.md` — why scannable trumps verbose
- `corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md` — one primary CTA per view
- `corpus/ux-principles/audit/05-interaction/mindless-choice-audit.md` — every click should be obvious

## Anti-patterns

- "We'll fix it with a tooltip / onboarding tour / help article." Documentation is a tax users pay because the design failed.
- "It's intuitive once you learn it." Intuitive things don't require learning.
