---
name: Dream State Mapping (Step 0C)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/09-temporal-depth.md, corpus/evaluation-frameworks/step-0/premise-challenge.md, corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md]
---

# Dream State Mapping (Step 0C)

## What it is
Step 0C of CEO plan review. After the premise has been challenged and existing-code leverage has been mapped, dream state mapping locates the current plan on a 12-month arc. It asks: where is the system today, where is it going if this plan ships, and where does the system want to be 12 months from now? The output is a three-state arrow that makes legible whether the plan moves toward or away from the dream state.

## The required structure
```
  CURRENT STATE                  THIS PLAN                  12-MONTH IDEAL
  [describe]          --->       [describe delta]    --->    [describe target]
```

The three boxes:
- **CURRENT STATE**: where the system is today, with honest pain points named. Not aspirational.
- **THIS PLAN**: the delta this plan introduces. What changes? What stays the same? What new capabilities exist after this ships?
- **12-MONTH IDEAL**: where the system wants to be. What does the user feel? What can the team do that they cannot today? What constraints have lifted?

The arrows are the load-bearing element. They force the reviewer to argue: does THIS PLAN move from CURRENT STATE toward 12-MONTH IDEAL, or does it move sideways, or does it move away?

## How to apply
1. Write the 12-MONTH IDEAL first, before re-reading the plan. Anchor on the destination, not the proposal. (If you write the ideal after reading the plan, you'll unconsciously write the ideal that the plan satisfies.)
2. Write CURRENT STATE honestly. Plans frequently misrepresent current state to make the plan look more necessary or more ambitious than it is.
3. Write THIS PLAN as the delta — only what changes. If the delta is small, name that. Small deltas are not failures; cumulative small deltas can compound into the dream state.
4. Evaluate alignment: does the arrow from CURRENT to PLAN point in the same direction as the arrow from PLAN to 12-MONTH IDEAL? If yes, plan is aligned. If no — the plan may be useful but sideways.

## What goes in the 12-MONTH IDEAL
Avoid roadmap-speak. The ideal is not "we'll have shipped features A, B, C." It is the experience or capability that exists in the world. "Users complete checkout in under 30 seconds without friction." "Engineers ship features without writing custom infrastructure for each one." "The product reads as the canonical category answer, not one of three options."

## When the plan is sideways
If dream state mapping reveals that the plan is orthogonal to the 12-month ideal — useful but not on the trajectory — surface this honestly. The plan might still be the right thing to ship (urgent fix, customer commitment, partner integration). But name the orthogonality. Don't pretend the plan moves toward a destination it does not move toward.

## Required output format
The three-state arrow above. Then a one-paragraph alignment assessment:
```
  ALIGNMENT:
  [Does this plan move toward the 12-month ideal? If yes, how directly. If no or sideways, name it.]
```

## Why it matters
Plans get evaluated against immediate criteria — is it shippable, is it correct, is it on time. Dream state mapping forces the additional question: is it on the trajectory? Plans that ship and pass every section can still leave the company in a structurally worse position 12 months out. The arrow makes this visible. The 12-month frame is intentional — long enough to matter, short enough to be concrete.

## Examples
1. **Plan: "add a notification preferences page"**. CURRENT: too many notifications, no controls. PLAN: users can opt out per channel. 12-MONTH IDEAL: users only get notifications they want; we send 60% fewer total. Aligned: yes, plan is a step toward the ideal.
2. **Plan: "add a third payment provider"**. CURRENT: single provider, occasional outages. PLAN: failover capability. 12-MONTH IDEAL: payments are invisible infrastructure; nobody worries about them. Aligned: yes, this plan moves toward invisibility.
3. **Plan: "rewrite the admin dashboard in a new framework"**. CURRENT: dashboard works, ages slowly. PLAN: rewrite. 12-MONTH IDEAL: stronger product surface for users, not internal tooling. Sideways: the rewrite is real work but does not move the dream state. Defer or reduce.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/09-temporal-depth.md` — temporal depth is the underlying instinct for the 12-month frame
- `corpus/evaluation-frameworks/step-0/premise-challenge.md` — premise challenge is the input to dream-state mapping
- `corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md` — Section 10 closes the loop on dream-state delta

## Anti-patterns
- Writing the 12-month ideal after reading the plan. The ideal becomes a rationalization of the plan rather than a destination.
- Treating sideways plans as failures. They are sometimes correct — but they must be named, not dressed up as on-trajectory.
