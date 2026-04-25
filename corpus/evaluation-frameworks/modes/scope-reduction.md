---
name: SCOPE REDUCTION mode
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: framework
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md, corpus/evaluation-frameworks/cognitive-patterns/06-speed-calibration.md, corpus/evaluation-frameworks/modes/hold-scope.md]
---

# SCOPE REDUCTION mode

## What it is
The mode for plans that are overbuilt or wrong-headed. SCOPE REDUCTION strips back to the smallest valuable thing that ships value to a user. It runs a ruthless cut and a follow-up-PR separation, then reviews that minimal version against Sections 1-11. The default posture is aggressive deletion: every part of the plan is guilty until it can demonstrate that it must ship in this PR rather than later.

## When to use
- Plan touches >15 files → the system should suggest REDUCTION unless user pushes back
- Plan introduces 3+ new classes/services for a feature that could be expressed in 1
- Wartime context where the team needs to ship something fast and clean rather than something complete
- User says "this is overbuilt," "let's strip it back," "what's the MVP?"

## How to apply (the two moves)

**1. Ruthless cut**: What is the absolute minimum that ships value to a user? Everything else is deferred. No exceptions. Be willing to cut features the team is emotionally invested in. The cut is the work.

**2. Follow-up separation**: For everything cut, decide: is it a follow-up PR (yes-it-belongs-with-this-feature, just not in this PR) or is it a TODO (maybe-later, deserves its own evaluation)? Be specific. "Phase 2 someday" is rarely a real plan; "follow-up PR after this lands" is.

That's Step 0D in REDUCTION mode. Then proceed to Sections 1-11 against the reduced scope.

## What "smallest valuable thing" means
- Ships to a real user (not "ready for users to test in 6 weeks")
- Delivers a concrete benefit they can articulate
- Does NOT include polish, edge cases beyond the 80% path, or platform potential
- Does NOT include nice-to-haves that the team would feel embarrassed to ship without — embarrassment is not a scope criterion
- Does NOT include "while we're in there" cleanup — separate PR

## Required output format
Standard CEO review outputs against the reduced scope. The "NOT in scope" section is unusually long in REDUCTION mode — it documents everything cut. The "What already exists" section is often the load-bearing one — a major reason to reduce is that more exists than the plan accounted for.

## Why it matters
Plans bloat by accretion. Every reviewer adds a concern, every stakeholder adds a feature, every exception adds a guard rail. Without an active reduction force, plans grow until the team can no longer ship them on time or with confidence. SCOPE REDUCTION is the active force. It is unpopular in the short term (the team has to cut things they like) and is the only thing that keeps shipping cadence intact in the long term.

## Examples
1. **Roadmap plan with 12 features for one quarter**: REDUCTION asks — what's the one feature that, if shipped well, would matter? Cut to that. The other 11 become P2/P3 candidates.
2. **Refactor plan that touches 30 files**: REDUCTION asks — can we ship a coherent slice of this in 8 files, then iterate? Almost always yes.
3. **Greenfield feature with full polish from day 1**: REDUCTION asks — what's the version we'd ship to 5 friendly users tomorrow? Build that. Polish is a follow-up.

## The hardest part: defending the cut
SCOPE REDUCTION's hardest move is keeping the cut. The team will lobby to add back. Stakeholders will say "but we promised X." The cut survives only if the rationale is durable and visible. Document why each cut item was cut. When they come back asking, "remember why we deferred this?" you have an answer.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md` — REDUCTION is focus-as-subtraction operationalized
- `corpus/evaluation-frameworks/cognitive-patterns/06-speed-calibration.md` — speed often demands reduction; the slow plan is rarely the right plan
- `corpus/evaluation-frameworks/modes/hold-scope.md` — HOLD is REDUCTION's calmer sibling when the scope is already small

## Anti-patterns
- Reducing then re-adding piece-by-piece during review. The cut must survive the review or the reduction was theater.
- Confusing reduction with under-engineering. Reduction is fewer features at full quality. Under-engineering is the right number of features at insufficient quality.
