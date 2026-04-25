---
name: Progressive Autonomy
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 700
related: [corpus/ai-product-ux/autonomy/three-tier-model.md, corpus/ai-product-ux/autonomy/trust-building-pattern.md, corpus/ai-product-ux/autonomy/cagan-empowerment-mapping.md, corpus/ai-product-ux/autonomy/revoke-autonomy-ux.md, corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md, corpus/pm-frameworks/strategy/trust-barrier.md]
---

# Progressive Autonomy

## What it is
Progressive autonomy is the pattern of letting users start with AI-assisted workflows — where the human reviews every output — and graduate to fully autonomous workflows as observed accuracy builds trust. The user is in control of how much rope the AI gets, and the rope extends only after the AI earns it. Early in the relationship, the AI suggests; later, it confirms; eventually, it acts.

## Why it matters
Users do not arrive at an AI product trusting it. Trust is earned through repeated, observed, accurate behavior — exactly the same way trust is earned between humans. A product that demands full autonomy on day one fails the trust check and gets relegated to "interesting demo." A product that scales autonomy with observed accuracy gets promoted from "tool I check" to "system I rely on." This is the AI-product mirror of Cagan's empowerment ladder — the trust barrier between feature teams and empowered teams.

## How to apply
1. **Default to suggested mode.** New users see AI output as suggestions they accept, edit, or reject. Track every accept/edit/reject.
2. **Graduate to confirmed mode after observed accuracy crosses a threshold.** The AI proposes an action and asks for one-click confirmation. The user is still in the loop, but the loop is shorter.
3. **Offer autonomous mode opt-in only after sustained accuracy in confirmed mode.** Never default-on. The user grants the autonomy explicitly.
4. **Always provide a one-click revoke.** When the AI errs in autonomous mode, the user must be able to drop back to confirmed or suggested mode without friction.

## Examples
1. **Suzy Decision Engine launch (350+ enterprise customers, six-week transformation).** The launch sequenced from AI-assisted research synthesis (analysts review every insight) toward semi-autonomous insight generation (system surfaces, analyst confirms). Full autonomy was reserved for high-confidence, low-stakes insight types.
2. **Context Layer Demo's "let me drive" toggle.** Users can flip the demo between "show me the synthesis" (suggested) and "act on the synthesis automatically" (autonomous), but only after they've seen the reasoning chain enough times to trust it.
3. **Cursor's agent mode.** Default is line-by-line suggestions. Agent mode (autonomous multi-file edits) is opt-in and revocable. The product graduates with the user.

## Related entries
- `corpus/ai-product-ux/autonomy/three-tier-model.md` — the suggested → confirmed → autonomous framework
- `corpus/ai-product-ux/autonomy/trust-building-pattern.md` — the operational mechanics
- `corpus/ai-product-ux/autonomy/cagan-empowerment-mapping.md` — the cross-link to product strategy
- `corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md` — Cagan's source framework
- `corpus/pm-frameworks/strategy/trust-barrier.md` — the trust dynamic this pattern operationalizes

## Anti-patterns
- **Autonomy by default.** Shipping the AI in full-autonomy mode and asking the user to opt out. Users feel ambushed when the AI errs and trust never recovers.
- **No revoke path.** Granting autonomy with no way to claw it back. The first error becomes the last interaction.
