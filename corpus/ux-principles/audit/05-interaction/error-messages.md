---
name: Error Messages — Specific + Include Fix or Next Step
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/08-content/error-messages-specific.md, corpus/ux-principles/principles/goodwill-reservoir.md, corpus/ai-product-ux/]
---

# Error Messages — Specific + Include Fix or Next Step

## What it is

Error messages should:

1. **Specifically say what went wrong** — not "An error occurred."
2. **Explain why** — when relevant ("The email field is required" / "Server timed out").
3. **Tell the user what to do next** — the fix or workaround.

The structure: **what happened + why + what to do**.

A good error message respects the user's time and protects the goodwill reservoir. A bad error message — generic, blame-shifting, or actionless — drains the reservoir fast.

## Why it matters

Errors are the most fragile moments in any interaction. The user is already partially blocked, partially frustrated. The error message is the product's chance to either repair the moment ("Sorry — here's how to fix it") or compound it ("Something went wrong"). Most products choose the second.

Vague errors tell the user "we don't know what happened either, good luck." Specific errors with a path forward tell the user "we got you, here's the fix."

## How to apply

1. **Be specific:**
   - **BAD:** "An error occurred."
   - **GOOD:** "Couldn't reach the payment processor."
2. **Explain why if it adds value:**
   - **GOOD:** "Couldn't reach the payment processor. The connection timed out."
3. **Include the fix or next step:**
   - **GOOD:** "Couldn't reach the payment processor. The connection timed out. Try again, or contact support if this persists."
4. **For form errors, name the field and the fix:**
   - **BAD:** "Invalid input."
   - **GOOD:** "Email must include @ — try `name@example.com`."
5. **Apologize when uncertain.** "Sorry, this didn't work. We're looking into it."

## Examples

- **GOOD:** Stripe API errors — `"You passed an empty string for 'amount'. We assume empty values are an attempt to unset a parameter; however 'amount' cannot be unset. You should remove 'amount' from your request or supply a non-empty value."`
- **BAD:** "Validation failed."
- **GOOD form error:** "Password must be at least 8 characters. Yours is 6." (specific count)
- **BAD form error:** "Invalid password."
- **GOOD network error:** "Couldn't load your projects. Check your connection and try again." + Retry button.
- **BAD network error:** "Error 500."

## Related entries

- `corpus/ux-principles/audit/08-content/error-messages-specific.md` — content version of the rule
- `corpus/ux-principles/principles/goodwill-reservoir.md`
- `corpus/ai-product-ux/`

## Anti-patterns

- Generic catch-all errors ("Something went wrong"). Users learn the product is opaque and unreliable.
- Blaming the user ("You did X wrong") instead of explaining the system state.
- Showing developer-facing stack traces in production. Users don't need (or want) to see line numbers.
