---
name: Motion Rules (AI Products)
domain: ai-product-ux
source_skill: product-design
entry_type: rule
length_target: 500
related: [corpus/ai-product-ux/design-system/web-stack.md, corpus/ai-product-ux/design-system/admin-ui-stack.md, corpus/ai-product-ux/reasoning/sidebar-pattern.md, corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md, corpus/brand-system]
---

# Motion Rules (AI Products)

## What it is
A rule set for motion in Riché's AI product surfaces. **Subtle, purposeful, never decorative.** Motion communicates state change — a synthesis arriving, a confidence chip flipping, a tier promotion offer appearing — and never exists for ornament. Default to fast (≤200ms), ease-out, and minimal displacement.

## Why it matters
AI products live or die on perceived responsiveness. A surface that animates aggressively reads as slow even when it isn't. A surface that animates purposefully reads as fast and trustworthy. The wrong motion choices undercut the streaming-response work that makes the model itself feel responsive. Motion is also a trust signal: confident products move with restraint, hesitant products try to entertain.

## How to apply
1. **Communicate state, don't decorate.** If a motion isn't telling the user something changed, it doesn't ship.
2. **Default to fast.** ≤200ms for most transitions. ≤400ms for major surface shifts (sidebar opening, full-pane swap). Anything longer feels sluggish.
3. **Ease-out, not ease-in-out.** Things should arrive sharply and settle. Ease-in-out gives that draggy "slow start, slow end" quality that reads as performance theater.
4. **Streaming output beats progress bars.** When the model is producing content, stream the content. The motion of arriving text is the progress indicator. (Pairs with `failure/timeout-and-rate-limit-ux.md`.)
5. **Match motion across surfaces.** The same kind of transition (panel open, chip flip, content arrival) should look the same in the customer-facing demo and the admin UI. Inconsistent motion fragments the brand.

## Examples
1. **Context Layer Demo's reasoning sidebar opening.** 180ms slide-in from right with content fade. The sidebar arrives, the content materializes, the user reads. No bounce, no overshoot, no swoosh.
2. **Confidence chip state changes.** When a chip flips from "synthesizing" to "high confidence," it transitions in 120ms with a subtle background fade. The user sees the state change without being interrupted.
3. **Counter-example: every "look at our AI" demo with floating particle backgrounds.** Decorative motion that signals "we have a designer" but communicates nothing about state. Riché's products explicitly avoid this register.

## Related entries
- `corpus/ai-product-ux/design-system/web-stack.md` — the surface motion runs on
- `corpus/ai-product-ux/design-system/admin-ui-stack.md` — sparser motion in admin contexts
- `corpus/ai-product-ux/reasoning/sidebar-pattern.md` — the canonical motion-bearing surface
- `corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md` — streaming as motion
- `corpus/brand-system` — visual identity that motion expresses

## Anti-patterns
- **Decorative motion.** Particle effects, floating gradients, springy bounces. Communicates nothing; signals "we mistook polish for restraint."
- **Slow motion as gravitas.** 600ms eases that try to feel "premium." Read as sluggish; users notice the latency before the polish.
