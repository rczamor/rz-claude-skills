---
name: Error Messages — Specific, With Next Step
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/05-interaction/error-messages.md, corpus/ai-product-ux/failure/]
---

# Error Messages Specific

## What it is
Every error message must answer three questions: **what happened** (in plain language), **why** (cause if known), and **what to do next** (concrete action or recovery path). Generic errors like "Something went wrong" or "Error 500" fail all three.

## Why it matters
Errors are friction points where users decide whether to keep trying or churn. A specific error transforms confusion into agency — "Your payment was declined by your bank. Try a different card or contact your bank" gives the user a path. "Something went wrong" gives them nothing but the urge to close the tab. Specific errors also dramatically reduce support load.

## How to apply
- **What happened** — describe the failure in user-language, not stack-trace language. "We couldn't save your changes" — not "Mutation failed: timeout."
- **Why** — when you know the cause, share it. "Your session expired" beats "Authentication error." When you don't know, say "Our team has been notified" honestly rather than fake-blaming the user.
- **Next step** — give them a button, link, or instruction. "Try again" / "Refresh the page" / "Use a different email." Don't leave them at a dead end.
- Differentiate by failure class: validation errors (inline, near the field), recoverable runtime errors (toast with retry), critical errors (full-page state with support link).
- Never blame the user for ambiguous failures. "You entered an invalid value" without saying *which* field is hostile.

## Examples (BAD vs. GOOD pairs)

BAD:
```
Error
Something went wrong. Please try again.
[Dismiss]
```

GOOD:
```
We couldn't save your draft
Your connection dropped. Your text is safe — we'll retry automatically.
[Retry now]   [Save offline]
```

Inline form error — BAD: "Invalid input." GOOD: "Email must include an @ symbol."

## Related entries
- `corpus/ux-principles/audit/05-interaction/error-messages.md` — interaction-state companion.
- `corpus/ai-product-ux/failure/` — AI-specific failure modes (hallucination, refusal, low-confidence).

## Anti-patterns
- "Something went wrong." — the universal error-message smell.
- Showing the raw stack trace in production.
- Errors that auto-dismiss in 2 seconds — users never finish reading them.
