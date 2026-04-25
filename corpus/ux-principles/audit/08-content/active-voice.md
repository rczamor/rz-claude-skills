---
name: Active Voice in UI Copy
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/principles/law-3-omit-then-omit-again.md, corpus/voice/]
---

# Active Voice

## What it is
UI copy uses active voice and direct address: "Install the CLI" not "The CLI will be installed by you." "We sent you an email" not "An email has been sent." The user is the actor; the product is the helper. Passive voice is wordy, vague, and bureaucratic.

## Why it matters
Active voice is shorter (the Third Law: "Omit needless words"), clearer (always names the actor), and warmer (sounds human, not legal). Passive voice is the linguistic equivalent of an institutional-blue government website — it puts distance between the user and the action. Microsoft, Apple, Stripe, and Linear all converged on active voice for a reason.

## How to apply
- Subject performs verb: "Install X" / "Save changes" / "We sent the link."
- Direct address — call the user "you," not "the user." Refer to the product as "we" or by name, not "the system."
- Passive smell test: any sentence with "be", "been", "being", "is/was/will be {verb}-ed" — re-cast in active.
- Imperative for actions ("Sign in", "Read the docs"). Declarative for state ("You're signed in", "The build finished").
- Avoid auxiliary clutter: "You may want to consider clicking" → "Click."
- This is part of the Three Laws — see related principle.

## Examples (BAD vs. GOOD pairs)

BAD:
```
A confirmation email has been sent to your inbox.
The form must be filled out by you before submission.
Your account will be deleted in 30 days.
```

GOOD:
```
We sent a confirmation email to your inbox.
Fill out the form to continue.
We'll delete your account in 30 days. [Cancel deletion]
```

## Related entries
- `corpus/ux-principles/principles/law-3-omit-then-omit-again.md` — active voice tends to be shorter.
- `corpus/voice/` — Riché's voice-system rules (warmth + clarity + economy).

## Anti-patterns
- "Errors have been encountered" — passive AND vague.
- "The system requires that you..." — robotic and distancing.
- Long subordinate clauses to soften imperatives — clarity over politeness.
