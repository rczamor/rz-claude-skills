---
name: Caption / Label ≥ 12px
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/body-min-16px.md, corpus/ux-principles/audit/03-color/wcag-aa-contrast.md]
---

# Caption / Label ≥ 12px

## What it is

The smallest text on a page — captions, labels, footnotes, microcopy — should be at least 12px. This is a hard floor. Anything smaller is illegible to a meaningful share of users, especially on smaller screens and in poor lighting.

Most UI text should be larger; 12px is reserved for truly secondary labels (timestamps, byline credits, fine print).

## Why it matters

10px and 11px text is unreadable for many users — older users, anyone with mild visual impairment, anyone in bright sunlight on a phone. Designers with great eyesight on retina monitors don't notice; users do.

This rule pairs with `body-min-16px`: 16px floor for primary reading, 12px floor for everything else. Below 12px is either decoration (acceptable in tiny illustrative legends) or neglect (most cases).

## How to apply

1. **Audit:** find every `font-size` value smaller than 12px. Each is a candidate finding.
2. **For form labels:** 14px+ is better. 12px is the floor, not the target.
3. **For timestamps and microcopy:** 12px is acceptable.
4. **Don't go below 12px** unless the text is decorative and unimportant — and even then, ask if you should remove it instead.
5. **Increase contrast for small text.** WCAG large-text relaxation only kicks in at 18pt+; at 12px you need full 4.5:1 contrast.

## Examples

- **GOOD:** Form labels at 14px, helper text at 12px, body at 16px. Hierarchy by size, no illegibility.
- **BAD:** Helper text at 10px because the designer wanted it "subtle." Result: invisible to users with imperfect vision.
- **GOOD:** A blog post byline at 12px gray. Secondary information, comfortable to read.
- **BAD:** Footer links at 11px. Users trying to find the privacy policy can't read it.

## Related entries

- `corpus/ux-principles/audit/02-typography/body-min-16px.md`
- `corpus/ux-principles/audit/03-color/wcag-aa-contrast.md`

## Anti-patterns

- Going smaller than 12px for "professional density." Density at the cost of legibility is a loss.
- Using 10px text + 30% gray — small + low-contrast = double illegibility.
