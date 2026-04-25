---
name: "Mobile: Same Rules, Higher Stakes"
domain: ux-principles
source_skill: design-review
entry_type: framework
length_target: 300-800
related: [corpus/ux-principles/audit/05-interaction/touch-targets-44px.md, corpus/ux-principles/principles/billboard-design-overview.md, corpus/ai-product-ux/]
---

# Mobile: Same Rules, Higher Stakes

## What it is

Every UX principle that applies on desktop applies on mobile — only more so. Mobile is not a separate design discipline; it is the same design discipline run on a smaller screen with no cursor, smaller targets, less attention, and worse network conditions. The rules don't change. The cost of breaking them gets steeper.

Real estate is scarce, but you never sacrifice usability for space savings. Affordances must be VISIBLE — no cursor means no hover-to-discover. Touch targets must be big enough (44px minimum). Flat design can strip away useful visual signals. Prioritize ruthlessly: things needed in a hurry go close at hand; everything else is a few taps away with an obvious path.

## Why it matters

Teams routinely treat mobile as "the version where we cut things." That's the wrong frame. Mobile is the version where the rules are enforced more strictly because the user has less patience, less room, and no fallback. A button slightly too small on desktop is a polish issue; on mobile, it's a tap-failure that drains the goodwill reservoir.

Most users access most products primarily on mobile. If mobile is the cut-down version, you've cut down the experience for most of your users.

## How to apply

1. **Affordances must be VISIBLE without interaction.** No cursor on mobile. If the only signal that something is clickable is a hover state, it's invisible to most users. Use shape, color, underlining, position.
2. **Touch targets ≥ 44×44px.** Apple's HIG and Material Design agree. Anything smaller is a tap-error machine.
3. **Don't sacrifice usability for space.** The temptation to shrink padding, fonts, or targets to fit "just one more thing" is the road to mobile death.
4. **Prioritize ruthlessly.** What does the user need in 3 seconds? Put it in the thumb zone (bottom half of screen). Everything else is acceptable as a tap or two away — as long as the path is obvious.
5. **Don't use `user-scalable=no` or `maximum-scale=1`.** Users need to zoom. This breaks accessibility and trust.
6. **Forms: correct input types** (`type="email"`, `type="tel"`, `type="number"`, `inputmode="numeric"`). No autoFocus on mobile (it pops the keyboard before the user is ready).

## Examples

- **GOOD:** Instagram's bottom navigation — five large tap targets in the thumb zone. Always visible. Zero hover dependency.
- **BAD:** A web app that puts the primary action in a top-right hamburger menu on mobile. Top-right is the worst thumb-reach zone on a phone.
- **GOOD:** Apple Pay — large tappable button, clear affordance, works one-handed.
- **BAD:** A mobile checkout with a "Submit" button below the fold, a 12px font, and no `inputmode` set so the user has to switch keyboards manually.

## Related entries

- `corpus/ux-principles/audit/05-interaction/touch-targets-44px.md` — the operational rule
- `corpus/ux-principles/principles/billboard-design-overview.md` — billboard design is even more critical on mobile
- `corpus/ai-product-ux/` — AI products on mobile face the same rules

## Anti-patterns

- "We'll just stack the desktop columns vertically." That's not mobile design — that's mobile abdication.
- Disabling pinch-zoom to "preserve the layout." You preserved the layout and broke accessibility.
- Putting primary actions in top corners on mobile. Thumbs don't reach there comfortably.
