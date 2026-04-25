---
name: Trust-Building Pattern (Autonomy)
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 600
related: [corpus/ai-product-ux/patterns/progressive-autonomy.md, corpus/ai-product-ux/autonomy/three-tier-model.md, corpus/ai-product-ux/autonomy/cagan-empowerment-mapping.md, corpus/ai-product-ux/autonomy/revoke-autonomy-ux.md, corpus/pm-frameworks/strategy/trust-barrier.md]
---

# Trust-Building Pattern (Autonomy)

## What it is
The operational mechanics of moving a user up the autonomy tiers: start AI-assisted, log accuracy, prompt the user to grant autonomy when accuracy crosses a threshold. The pattern is the *how* behind progressive autonomy — the loop that converts observed behavior into earned trust into expanded scope.

## Why it matters
Without an explicit trust-building loop, users either stay forever at the lowest tier (because the product never invites them up) or get auto-promoted (and feel ambushed when something breaks). The loop must be visible to the user — they need to see that their accept/edit/reject choices are being counted, that a threshold exists, and that crossing it is the reason for the promotion offer. Visible mechanics build trust faster than invisible ones, because users understand what they're agreeing to.

## How to apply
1. **Track three signals: accept, edit, reject.** Per action type. Per user. Surfaces the precision of the AI for that user's particular work.
2. **Set a promotion threshold per action type.** Common heuristic: ≥90% accept rate over ≥50 actions. Lower stakes can move on less data; higher stakes require more.
3. **Surface the meter to the user.** "47 of 50 suggestions accepted. 3 more accepts and we'll offer auto-confirm." The visibility is itself trust-building.
4. **Prompt at the threshold, don't promote silently.** "You've accepted most of our suggestions for this task. Want to switch to one-click confirm?" The user grants the promotion.
5. **Re-evaluate continuously.** A user whose accept rate drops gets a quiet prompt to step back to a lower tier. The loop runs both directions.

## Examples
1. **Suzy Decision Engine's per-buyer autonomy meter.** Each enterprise account had a per-insight-type accept-rate meter. Buyers saw their own usage data and were prompted to enable autonomous insight generation only after the meter crossed threshold. Six-week ramp from launch to first autonomous insight types.
2. **Context Layer Demo's "we noticed..." prompt.** After ~10 successful synthesis runs in suggested mode, the demo prompts: "We noticed you've accepted most of our recent syntheses. Want to enable one-click confirm?" The prompt is the promotion.
3. **GitHub Copilot's quiet ratcheting in agent mode.** As accept rates climb, the agent takes more autonomous steps without explicit promotion prompts. Lower-stakes implementation; same pattern shape.

## Related entries
- `corpus/ai-product-ux/patterns/progressive-autonomy.md` — parent pattern
- `corpus/ai-product-ux/autonomy/three-tier-model.md` — the framework this loop moves users through
- `corpus/ai-product-ux/autonomy/cagan-empowerment-mapping.md` — the cross-domain analogue
- `corpus/ai-product-ux/autonomy/revoke-autonomy-ux.md` — the demotion side of the loop
- `corpus/pm-frameworks/strategy/trust-barrier.md` — the conceptual basis

## Anti-patterns
- **Silent promotion.** AI auto-promotes the user without telling them. First failure feels like betrayal.
- **No demotion path.** Promotion is sticky; users can move up but not down without contact-sales friction. Trust collapses on first error.
