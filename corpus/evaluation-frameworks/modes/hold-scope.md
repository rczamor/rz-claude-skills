---
name: HOLD SCOPE mode
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: framework
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md, corpus/evaluation-frameworks/modes/scope-reduction.md, corpus/evaluation-frameworks/modes/selective-expansion.md]
---

# HOLD SCOPE mode

## What it is
The mode for plans whose scope is right and needs to stay right. HOLD SCOPE defends the boundary. It runs a complexity check and a minimum-set check, then proceeds to the 11 review sections with maximum rigor — architecture, security, edge cases, observability, deployment — with the goal of making the plan bulletproof, not bigger. **No expansions are surfaced.** Defer surfaced ideas to TODOS.md.

## When to use
- Bug fix or hotfix → default mode
- Refactor → default mode
- Plan whose scope was already decided in `/office-hours` and approved
- User explicitly says "hold scope" or "no scope creep"

## How to apply (the two moves)

**1. Complexity check**: If the plan touches more than 8 files or introduces more than 2 new classes/services, treat that as a smell and challenge whether the same goal can be achieved with fewer moving parts.

**2. Minimum set check**: What is the minimum set of changes that achieves the stated goal? Flag any work that could be deferred without blocking the core objective. Defer flagged work to TODOS.md, not to scope creep.

That's it for Step 0D in HOLD mode. Then proceed directly to Sections 1-11 at full rigor.

## What HOLD SCOPE does NOT do
- Does not run the 10x check
- Does not run delight opportunities
- Does not surface expansion candidates
- Does not run an opt-in or cherry-pick ceremony

The discipline is: the user said hold scope. The reviewer holds scope. Surfacing ideas the user explicitly didn't ask for is a violation of mode contract. The right place for "I noticed this would be cool" is TODOS.md — never in the live plan.

## Required output format
Standard CEO review outputs (Error & Rescue Registry, Failure Modes Registry, Diagrams, TODOS.md updates, NOT in scope section, What already exists section, Dream state delta). No CEO plan document persisted (that's an EXPANSION/SELECTIVE artifact).

## Why it matters
Plans that ship in HOLD mode are plans that ship on time, with high confidence, and to spec. The reviewer's instinct in EXPANSION/SELECTIVE modes is to add value by surfacing options. The reviewer's instinct in HOLD mode is to add value by removing risk. Different modes, different reviewer postures. Misapplying EXPANSION posture in HOLD context produces scope creep, blown deadlines, and reviewer-induced project drift.

## The complexity check, expanded
Why 8 files and 2 new services as the threshold? Because most plans that touch more than that are either (a) rebuilding something that already exists, (b) over-coupling features that could ship separately, or (c) reflecting an unclear problem statement. The threshold is a smell signal, not a hard rule — but every plan above it deserves explicit justification.

```
  PLAN TOUCHES         | SMELL?
  ---------------------|--------
  3 files              | No
  8 files              | Borderline; investigate
  15 files             | Likely; demand a refactoring rationale or scope reduction
  30 files             | Almost certainly; SCOPE REDUCTION is probably the right mode
```

## Examples
1. **Bug fix plan**: HOLD scope. Complexity check confirms it touches 2 files. Minimum set is exactly the bug fix. Proceed to Sections 1-11 with maximum rigor on the specific change.
2. **Refactor plan**: HOLD scope. Complexity check shows 12 files touched — flagged. Refactor justifies it (single coherent renaming + interface update). Approved with scope held.
3. **Wrong mode application**: SELECTIVE EXPANSION applied to a hotfix. Reviewer surfaces 5 cherry-picks; user accepts 2; deadline slips by a week. The hotfix should have been HOLD.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md` — HOLD SCOPE is focus-as-subtraction's defensive form
- `corpus/evaluation-frameworks/modes/scope-reduction.md` — REDUCTION is HOLD's stricter cousin when scope is over-built
- `corpus/evaluation-frameworks/modes/selective-expansion.md` — SELECTIVE is HOLD plus surfacing; pick based on user signal

## Anti-patterns
- Surfacing "just one cool idea" anyway. The user said hold scope; even one expansion violates the contract.
- Treating HOLD as low-effort. HOLD demands the deepest section-by-section rigor of any mode.
