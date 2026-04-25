---
name: The Goodwill Reservoir
domain: ux-principles
source_skill: design-review
entry_type: framework
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/18-design-for-trust.md, corpus/ux-principles/principles/law-1-dont-make-me-think.md, corpus/ux-principles/audit/05-interaction/error-messages.md]
---

# The Goodwill Reservoir

## What it is

Every user starts a session with a finite reservoir of goodwill — patience, willingness to forgive, willingness to keep trying. Every friction point depletes that reservoir. Every helpful moment refills it. When the reservoir runs dry, the user leaves, and rarely returns.

The reservoir is invisible. Users don't tell you they've drained it; they just stop showing up. Designing for the reservoir means treating every interaction as either a deposit or a withdrawal.

## Why it matters

Most teams design as if the user starts each session fresh and tolerant. They don't. They've been frustrated by other products, and your interface inherits a small reservoir at best. A single sloppy moment — a confusing error, a phone-number format rejection, a forced tour — drains it faster than three good moments refill it.

The reservoir model also explains why "small" issues compound. One annoying paywall is forgivable. Three annoying paywalls in a row are catastrophic. The user doesn't rationally weigh — they feel depleted and leave.

## How to apply

**Things that deplete the reservoir faster:**

- **Hiding info users want.** Pricing, contact, shipping costs, support hours.
- **Punishing users for not doing things your way.** Strict phone number formatting, password rules nobody can predict, "must be at least 8 characters with one uppercase and one symbol".
- **Asking for unnecessary information.** Every required field that isn't load-bearing is a withdrawal.
- **Putting sizzle in their way.** Splash screens, forced tours, video autoplays, "limited time offer" interstitials.
- **Unprofessional or sloppy appearance.** Typos, broken images, misaligned elements, mobile layouts that don't work.

**Things that replenish:**

- **Know what users want and make it obvious.** The thing they came for is the thing they see first.
- **Tell them what they want to know upfront.** Pricing on the pricing page, not behind "Contact sales".
- **Save them steps wherever possible.** Smart defaults, autofill, remember-me.
- **Make it easy to recover from errors.** Undo windows, autosave, clear error messages with fixes.
- **When in doubt, apologize.** "Sorry, this didn't work. Try again or contact us." beats blame.

## Examples

- **GOOD:** Amazon's "1-Click" purchase. Saves users a 4-step checkout. Massive deposit.
- **BAD:** A booking site that hides total price until step 5, adds fees ("convenience charge") at the end. Reservoir drained.
- **GOOD:** Stripe's error messages — specific, with exactly the line of code or field that's wrong, and what to fix. Refills despite being an error.
- **BAD:** "An error occurred. Please try again." with no detail. Withdrawal, plus the user has lost trust.

## Related entries

- `corpus/evaluation-frameworks/cognitive-patterns/18-design-for-trust.md` — trust is the long-form version of the reservoir
- `corpus/ux-principles/principles/law-1-dont-make-me-think.md` — thinking depletes
- `corpus/ux-principles/audit/05-interaction/error-messages.md` — error messages are reservoir interactions

## Anti-patterns

- Treating user frustration as a marketing problem ("we need to communicate better"). It's a design problem — fix the friction.
- Designing for first-time delight at the expense of repeat-use friction. Users notice the second-day experience.
