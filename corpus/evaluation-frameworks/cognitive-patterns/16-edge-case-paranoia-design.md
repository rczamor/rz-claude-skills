---
name: Edge Case Paranoia (Design)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md, corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md, corpus/ai-product-ux/failure/]
---

# Edge Case Paranoia (Design)

## What it is
What if the name is 47 characters? Zero results? Network fails mid-action? First-time user vs. power user? Empty states are features, not afterthoughts. The 10x CEO instinctively asks the questions designers default to ignoring. Most UI breaks not on the happy path but on the realistic-but-rare path: the long name that overflows the card, the empty list that shows a sad-face placeholder, the third connection retry, the user who arrives via a direct link with no context.

## Why it matters
Plans default to designing the happy path because the happy path is what gets demoed. The realistic-but-rare path is what gets shipped and breaks for actual users. Edge case paranoia is the discipline of designing the rare paths with the same care as the common ones, because (a) every user hits the rare path eventually, and (b) the user who hits it is forming their judgment of the product in that exact moment.

## How to apply
1. For every feature, walk through the standard adversarial inventory: What if the input is null? Empty string? 47 characters? 470 characters? Unicode? Right-to-left? Missing entirely?
2. Walk through the network inventory: What if the call takes 30 seconds? Times out? Returns 500? Returns 200 with empty body? Fails midway through a multi-step interaction?
3. Walk through the user-state inventory: First-time user, returning user with state, power user with mountains of data, user on mobile with intermittent connection, user with screen reader, user on slow CPU.
4. Empty states are first-class. Specify them as fully as you specify success states — warmth, primary action, and a path forward, not just a sad-face placeholder.

## Examples
1. **List view plan**: specifies the populated state. Edge case paranoia surfaces: zero results (with what message? what action?), one result (does the layout still feel intentional?), 10,000 results (is there pagination, virtualization?), results loading slowly (what does the skeleton look like?), results changing while the user is reading them (does the page jump?).
2. **Form submission**: happy path saves. Paranoia: double-click submit (idempotent?), submit during deploy (graceful?), network drops mid-submit (retry?), validation error after partial fill (does it preserve their work?).
3. **Onboarding**: power user vs. first-time user — does the welcome screen waste the power user's time, or skip past the first-time user too fast?

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md` — inversion at the UI layer is edge-case paranoia
- `corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md` — Section 4 IS this pattern made into a section
- `corpus/ai-product-ux/failure/` — AI product failure modes lean heavily on this pattern

## Anti-patterns
- Treating edge cases as "v2 polish." They are v1 quality. The user does not care which release made them feel cared about.
- Listing edge cases without designing them. Naming the case is step one; the design must specify the experience.
