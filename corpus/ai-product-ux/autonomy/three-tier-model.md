---
name: Three-Tier Autonomy Model
domain: ai-product-ux
source_skill: research
entry_type: framework
length_target: 600
related: [corpus/ai-product-ux/patterns/progressive-autonomy.md, corpus/ai-product-ux/autonomy/trust-building-pattern.md, corpus/ai-product-ux/autonomy/cagan-empowerment-mapping.md, corpus/ai-product-ux/autonomy/revoke-autonomy-ux.md, corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md]
---

# Three-Tier Autonomy Model

## What it is
A framework: **suggested → confirmed → autonomous**. Three discrete tiers of AI autonomy, each defined by the user's role in the loop and promoted on observed accuracy. The framework adapts public AI UX canon — Google PAIR's "calibrate trust" guidance, Anthropic's agent autonomy levels in Constitutional AI, OpenAI's tool-use opt-in patterns — into a product-shippable shape that the source skill's "progressive autonomy" pattern only sketches.

## Why it matters
The source skill describes progression but doesn't enumerate the tiers. A team without enumerated tiers tends to build either a binary (assistant on / agent on) or a continuous slider (which users can't reason about). Three discrete tiers give designers and PMs a vocabulary to hold positions in roadmaps, eval thresholds to gate promotion, and copy patterns the user can learn. The discrete model travels.

## How to apply
1. **Suggested.** AI proposes; user accepts, edits, or rejects. AI does not act. Track every accept/edit/reject as eval signal.
2. **Confirmed.** AI proposes an action and asks for one-click confirmation. Faster than suggested, still human-in-the-loop. Promote here only after sustained accuracy in suggested mode (typical threshold: ≥90% accept rate over ~50 actions).
3. **Autonomous.** AI acts; user is notified after the fact and can revoke. Promote here only after sustained accuracy in confirmed mode and only as opt-in. Never default-on.
4. **Promotion is per-action-type, not per-user.** A user might be in autonomous mode for "summarize meeting notes" and suggested mode for "draft customer email." Granularity matters.
5. **Demotion is one-click and immediate.** See `revoke-autonomy-ux.md`.

## Examples
1. **Suzy Decision Engine's tier sequencing.** Launch sequence (350+ enterprise customers, six-week transformation) explicitly mapped insight types to tiers: high-volume / low-stakes insights moved to autonomous; novel / high-stakes insights stayed at suggested. Buyers controlled the tier per insight type.
2. **Cursor's three modes.** Tab completion (suggested) → composer with confirm (confirmed) → agent mode (autonomous). The same framework, applied to coding.
3. **Anthropic's tool use defaults.** Tools default to "ask user" (confirmed) and can be promoted to "auto-execute" (autonomous) per tool. The framework's principles in production.

## Related entries
- `corpus/ai-product-ux/patterns/progressive-autonomy.md` — parent pattern
- `corpus/ai-product-ux/autonomy/trust-building-pattern.md` — the mechanics of promotion
- `corpus/ai-product-ux/autonomy/cagan-empowerment-mapping.md` — the cross-domain analogue
- `corpus/ai-product-ux/autonomy/revoke-autonomy-ux.md` — the demotion path
- `corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md` — Cagan's parallel framework

## Anti-patterns
- **Binary autonomy.** "AI on / AI off." Users have no graceful path between tiers and feel they must choose between low utility and high risk.
- **Continuous slider.** A 0-100 autonomy dial. Users have no idea where to set it; the granularity is fake.
