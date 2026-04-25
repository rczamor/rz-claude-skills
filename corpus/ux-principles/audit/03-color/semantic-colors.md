---
name: Semantic Colors — Success Green, Error Red, Warning Amber/Yellow
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/no-color-only-encoding.md, corpus/ux-principles/audit/03-color/no-red-green-only.md, corpus/ux-principles/audit/05-interaction/error-messages.md]
---

# Semantic Colors — Success Green, Error Red, Warning Amber/Yellow

## What it is

Semantic colors should follow universal conventions:

- **Success:** green (typically `#10B981`, `#22C55E`, or similar).
- **Error / destructive:** red (typically `#EF4444`, `#DC2626`).
- **Warning / caution:** amber or yellow (typically `#F59E0B`, `#EAB308`).
- **Info / neutral notification:** blue (typically `#3B82F6`).

Use these consistently across the entire product. Don't surprise users by using red for success or blue for warning — they have decades of cultural learning that wires green = good, red = bad.

## Why it matters

Color is a fast cognitive signal. Users don't read "Success" — they see green and know it worked. Inverting these conventions (using purple for success, orange for error) forces users to read each label, slowing recognition and breaking trust. Worse: colorblind users rely on the additional cue (icon, label) but expect it to align with conventional color where they can perceive it.

Consistency within the product is also critical. If success is green on one page and emerald on another, the system reads as careless.

## How to apply

1. **Define semantic tokens:** `--color-success`, `--color-error`, `--color-warning`, `--color-info`.
2. **Use them universally.** Toasts, badges, form states, status indicators — all draw from the same tokens.
3. **Pair color with icon and label.** Don't rely on color alone (see `no-color-only-encoding`).
4. **Audit:** find every red, green, yellow, blue use across the product. Are they all serving their semantic role consistently?

## Examples

- **GOOD:** Toast: green checkmark + "Saved" / red X + "Failed to save" / yellow triangle + "Connection unstable".
- **BAD:** Toast that uses purple for success because "purple is on-brand." User has no instant signal.
- **GOOD:** Form validation — green checkmark next to valid email, red message next to invalid.
- **BAD:** Using red for "limited stock" and red for "error" — same color, different meanings, confusion.

## Related entries

- `corpus/ux-principles/audit/03-color/no-color-only-encoding.md`
- `corpus/ux-principles/audit/03-color/no-red-green-only.md`
- `corpus/ux-principles/audit/05-interaction/error-messages.md`

## Anti-patterns

- "Our brand is green so everything is green, including errors." Brand doesn't override convention.
- Using semantic colors decoratively (a green border on a non-success card). Diluted signal.
