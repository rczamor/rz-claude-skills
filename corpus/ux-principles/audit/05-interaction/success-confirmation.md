---
name: Success — Confirmation Animation or Color, Auto-Dismiss
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/05-interaction/error-messages.md, corpus/ux-principles/audit/07-motion/duration-50-700.md]
---

# Success — Confirmation Animation or Color, Auto-Dismiss

## What it is

When an action succeeds (form saved, message sent, file uploaded), give the user a clear confirmation: a brief animation (checkmark animating in), a color change (green flash, badge), or a toast notification. The confirmation should auto-dismiss after a few seconds (typically 3-4 seconds for toasts) — the user has been told, no need to make them dismiss it.

The structure: brief, visible, auto-dismissing.

## Why it matters

Without confirmation, users wonder: "Did that work?" They click again, doubting. They refresh the page to verify. Both behaviors waste time and erode trust.

A small green checkmark that animates in for half a second tells the user "yes, it worked" — they move on. The whole interaction takes less mental effort. Trust is built on these microconfirmations.

## How to apply

1. **Toasts** for transient success (saved, copied, sent):
   - Slide in from top or bottom right
   - Green icon + brief message ("Saved" / "Link copied")
   - Auto-dismiss after 3-4 seconds
2. **Inline confirmation** for form submissions:
   - Replace the form with a success state
   - "Thanks! We've sent your reset link to your email."
3. **Animation:** a checkmark that draws in over 200-400ms feels delightful and confirms.
4. **Don't require a click to dismiss** transient successes. The user has confirmed by seeing it.

## Examples

- **GOOD:** Click "Copy link" → small toast slides in: "Link copied" with a green checkmark, dismisses in 3 seconds.
- **BAD:** Click "Copy link" → silent. User has no idea if it worked. Tries pasting; sees old content; tries again.
- **GOOD:** Submit a form → green banner replaces the form: "Thanks, we'll be in touch within 2 business days."
- **BAD:** Submit a form → page reloads silently with no confirmation. User wonders if it submitted.

## Related entries

- `corpus/ux-principles/audit/05-interaction/error-messages.md`
- `corpus/ux-principles/audit/07-motion/duration-50-700.md`

## Anti-patterns

- Persistent success messages that require dismissal. Annoying after the third confirmation.
- Modal success dialogs ("Your form was submitted") that block the user. Use toasts.
- Silent success — "no error means it worked." Users don't trust silence.
