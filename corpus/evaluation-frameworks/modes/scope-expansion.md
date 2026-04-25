---
name: SCOPE EXPANSION mode
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: framework
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/13-willfulness-as-strategy.md, corpus/evaluation-frameworks/modes/selective-expansion.md, corpus/pm-frameworks/strategy/]
---

# SCOPE EXPANSION mode

## What it is
The mode for plans that are good but could be great. SCOPE EXPANSION asks: what's the version that's 10x more ambitious and delivers 10x more value for 2x the effort? It runs three vision moves (10x check, Platonic ideal, delight opportunities) and then runs an opt-in ceremony — every expansion proposal presented individually, recommended enthusiastically, but the user decides one-by-one.

## When to use
- Greenfield feature → default mode
- User says "go big," "ambitious," "cathedral" → no question, EXPANSION
- The plan exists but feels like it's leaving the magic on the table

## How to apply (the four moves)

**1. 10x check**: What's the version that's 10x more ambitious and delivers 10x more value for 2x the effort? Describe it concretely. Not "make it bigger" — what would the user feel that they don't feel in the current plan?

**2. Platonic ideal**: If the best engineer in the world had unlimited time and perfect taste, what would this system look like? What would the user feel when using it? Start from experience, not architecture.

**3. Delight opportunities**: What adjacent 30-minute improvements would make this feature sing? Things where a user would think "oh nice, they thought of that." List **at least 5**.

**4. Expansion opt-in ceremony**:
- Describe the vision first (10x check, platonic ideal)
- Then distill concrete scope proposals from those visions
- Present each proposal as its **own AskUserQuestion** (not batched)
- Recommend **enthusiastically** — explain why it's worth doing
- The user decides per proposal: **A)** Add to this plan's scope, **B)** Defer to TODOS.md, **C)** Skip
- Accepted items become plan scope for all remaining review sections (1-11)
- Rejected items go to "NOT in scope"

## Required output format
A CEO plan document persisted to `~/.gstack/projects/$SLUG/ceo-plans/{date}-{feature-slug}.md` with sections: Vision (10x check + Platonic ideal), Scope Decisions table (proposal | effort | decision | reasoning), Accepted Scope, Deferred to TODOS.md.

## Framing pattern (the 0D-prelude rule)
Avoid flat prose. Lead with the felt experience, close with concrete effort:

FLAT: "Add real-time notifications. Users would see workflow results faster — latency drops from 30s polling to <500ms push. Effort: ~1 hour CC."

EXPANSIVE: "Imagine the moment a workflow finishes — the user sees the result instantly, no tab-switching, no polling, no 'did it actually work?' anxiety. Real-time feedback turns a tool they check into a tool that talks to them. Concrete shape: WebSocket channel + optimistic UI + desktop notification fallback. Effort: human ~2 days / CC ~1 hour. Makes the product feel 10x more alive."

Both are outcome-framed. Only one makes the user feel the cathedral.

## Why it matters
Plans default to "ship the requested thing." SCOPE EXPANSION mode interrupts that default — for the plans that deserve it — to ask whether the requested thing is the right thing or just the obvious thing. The opt-in ceremony preserves user sovereignty: every expansion is a decision, not a default. The user is in control. Recommend enthusiastically; the user decides.

## Examples
1. **Greenfield onboarding plan**: 10x check produces "what if onboarding teaches the user one productive action and they leave the session having done it?" Platonic ideal produces "feels like a conversation with the smartest user in the room." Delight ops: keyboard shortcut hints contextually, sample data preloaded, undo on any setup decision, progress saved across sessions, end with a "you just did X" moment. Each becomes an opt-in ask.
2. **API-first product**: 10x check shifts from "build a feature" to "build infrastructure other features ride on." Platform potential becomes the lens.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/13-willfulness-as-strategy.md` — willfulness underwrites EXPANSION's posture
- `corpus/evaluation-frameworks/modes/selective-expansion.md` — selective is the cousin mode that holds scope as default
- `corpus/pm-frameworks/strategy/` — strategic options thinking informs which expansions to surface

## Anti-patterns
- Auto-incorporating expansions without the opt-in ceremony. The user sovereignty rule is non-negotiable.
- Generating 30 vague expansions. Generate few specific expansions (5+ delight ops, 1 10x vision, 1 Platonic ideal). Quality over quantity.
- Flat-prose pitching. The 0D-prelude framing rule exists because expansion proposals must be felt, not just described.
