---
name: Button Labels — Specific, Verb-Based
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/05-interaction/mindless-choice-audit.md, corpus/ux-principles/principles/law-1-dont-make-me-think.md]
---

# Button Labels Specific

## What it is
Button labels should describe the *action* the user is taking — "Save API Key", "Delete project", "Subscribe to weekly digest" — not generic verbs like "Continue", "Submit", "OK", or "Yes/No." Specific labels let users predict what happens before they click.

## Why it matters
The First Law of Usability (`law-1-dont-make-me-think.md`) says self-evident beats self-explanatory. A button labeled "Continue" forces the user to remember context: continue what? Continue to where? "Save API Key" answers both at once. Generic labels also make confirmation modals worse — the choice "Yes / No" tells you nothing about the consequences. Specificity is the cheapest, highest-impact microcopy change.

## How to apply
- Lead with a verb that names the action: Save / Send / Delete / Publish / Subscribe / Cancel.
- Add the object when it's not obvious: "Delete account" not just "Delete."
- For confirmations, match the action: instead of "Yes / No" use "Delete project / Keep project."
- For destructive actions, restate the object so muscle-memory doesn't bypass intent: "Delete repository: rczamor/skills" not "Delete."
- Avoid labels that require scanning around for context. Each button should be readable on its own.
- Accessibility bonus: screen readers announce the button label out of context. "Continue" sounds the same on every page.

## Examples (BAD vs. GOOD pairs)

BAD:
```
[ Continue ]    [ Submit ]    [ OK ]    [ Yes ]
```

GOOD:
```
[ Continue to billing ]   [ Save API key ]   [ Got it, dismiss ]   [ Delete project ]
```

Modal — BAD: "Are you sure? [Yes] [No]" — GOOD: "Delete this project? Files will be removed in 30 days. [Delete project] [Cancel]"

## Related entries
- `corpus/ux-principles/audit/05-interaction/mindless-choice-audit.md` — generic labels force thinking.
- `corpus/ux-principles/principles/law-1-dont-make-me-think.md` — the umbrella principle.

## Anti-patterns
- "Submit" on every form — what's being submitted?
- "Continue" / "Next" with no object — Continue to what?
- Identical "Cancel" buttons that mean different things in different modals.
