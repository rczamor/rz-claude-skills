---
name: Subtraction Default (Rams)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md, corpus/evaluation-frameworks/cognitive-patterns/15-hierarchy-as-service.md, corpus/evaluation-frameworks/review-sections/11-design-ux-review.md]
---

# Subtraction Default (Rams)

## What it is
"As little design as possible." Dieter Rams' principle: if a UI element doesn't earn its pixels, cut it. Feature bloat kills products faster than missing features. The 10x CEO defaults to removal, not addition. Every element on every screen is guilty until it can show what it earns. The screen with fewer elements is rarely the worse screen — it is usually the calmer, faster, more confident one.

## Why it matters
Plans accumulate UI by addition. Every reviewer adds a request, every stakeholder adds a widget, every retro adds a notification. Without an opposing force, the product accretes interface until the user can't find the thing they came for. Subtraction is the opposing force. It is unglamorous (the deleted element does not appear in the demo), unrewarded (you can't show your boss the thing you removed), and load-bearing — it is what separates products that feel premium from products that feel like dashboards.

## How to apply
1. For every UI element, ask: "What is this element doing? What breaks if we remove it?" If the answer is "the user might miss the link" or "stakeholders asked for it" — flag for removal.
2. Default to fewer: fewer buttons, fewer states, fewer columns, fewer notifications, fewer onboarding steps. The screen earned its complexity by surviving review, not by being added.
3. Apply the 30% rule: if removing 30% of the elements would improve the screen, keep removing. Most screens benefit from the 30% cut.
4. Subtraction works best paired with hierarchy. Cut the elements that don't earn their place; emphasize the ones that do.

## Examples
1. **Settings page** with 40 settings. Subtraction: 7 are used by 80% of users; 33 should live behind "Advanced." The 33 are not deleted — they are removed from the default surface.
2. **Marketing page** with hero, sub-hero, three feature blocks, testimonials, FAQ, CTA, footer, sidebar. Subtraction: keep hero + one CTA above the fold; demote everything else.
3. **Dashboard widget grid**. Subtraction: most widgets are "we built this so we'll show it." Keep the two that operators actually consult; archive the rest.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md` — focus-as-subtraction is the strategy version; this is the design version
- `corpus/evaluation-frameworks/cognitive-patterns/15-hierarchy-as-service.md` — subtraction creates hierarchy by removing competition
- `corpus/evaluation-frameworks/review-sections/11-design-ux-review.md` — Section 11 demands subtraction-default thinking

## Anti-patterns
- Adding "in case" elements. "In case the user wants X" is the most common bloat-justification. The user's actual behavior is the authority, not your imagined edge case.
- Confusing subtraction with austerity. Subtraction is removing what doesn't earn its place. Austerity is removing what does — leaving the screen incapable of doing the user's job.
