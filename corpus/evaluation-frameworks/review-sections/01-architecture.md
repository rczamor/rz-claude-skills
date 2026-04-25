---
name: Section 1 — Architecture Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md, corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md, corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md]
---

# Section 1 — Architecture Review

## What it is
The first of 11 mandatory review sections. Section 1 evaluates and diagrams overall system design: component boundaries, all four data-flow paths (happy/nil/empty/error), state machines, coupling, scaling characteristics, single points of failure, security architecture, production failure scenarios, and rollback posture. It is the load-bearing section — almost every other section refers back to its diagrams.

## What it evaluates
- Overall system design and component boundaries — draw the dependency graph
- Data flow on all four paths: happy (data flows correctly), nil (input is missing), empty (input is present but empty/zero-length), error (upstream call fails)
- State machines for every new stateful object — include impossible/invalid transitions and what prevents them
- Coupling concerns — which components are now coupled that weren't before? before/after dependency graph
- Scaling: what breaks first under 10x load? Under 100x?
- Single points of failure — map them
- Security architecture — auth boundaries, data access patterns, API surfaces. For each new endpoint or data mutation: who can call it, what do they get, what can they change?
- Production failure scenarios — for each new integration point, describe one realistic production failure (timeout, cascade, data corruption, auth failure) and whether the plan accounts for it
- Rollback posture — if this ships and immediately breaks, what's the rollback procedure? Git revert, feature flag, DB migration rollback? How long?

## Required output format
**Required ASCII diagram**: full system architecture showing new components and their relationships to existing ones. ASCII diagrams for every new data flow (happy / nil / empty / error). ASCII state machine for every new stateful object. Before/after dependency graph for any coupling change.

## Mode-specific additions
**EXPANSION and SELECTIVE EXPANSION**: also evaluate what would make this architecture beautiful — not just correct, but elegant. Ask whether a new engineer joining in 6 months would say "oh, that's clever and obvious at the same time." Ask what infrastructure would make this feature into a platform other features can build on.

**SELECTIVE EXPANSION**: if any cherry-picks accepted in Step 0D affect architecture, evaluate their fit here. Flag any that create coupling concerns or don't integrate cleanly — chance to revisit the Step 0D decision with new information.

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch issues. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.** This is a review skill, not an implementation skill.

## Why it matters
Architecture is the substrate every other concern lives on. Skipping or compressing this section produces reviews that catch surface bugs while missing the structural problems that make those bugs inevitable. The diagram requirement is intentional: forcing the reviewer to draw the system surfaces ambiguity and coupling that prose hides. Many of the most important findings in a review are produced not by reading the plan but by drawing it.

## Examples
1. **New API integration plan**: drawing the data flow surfaces that the "error path" simply propagates the upstream 500 to the user. Section 2 will then map the rescue.
2. **State machine plan**: drawing the state machine reveals two transitions that were not specified — what happens when a paid subscription expires while a refund is in flight? The diagram forces the question.
3. **Rollback posture**: a new schema migration is "tested in staging." Section 1's rollback question demands: how long does the rollback take in production with 10M rows?

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md` — inversion is the underlying instinct for "what breaks first?"
- `corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md` — Section 2 details what Section 1's error path implies
- `corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md` — Section 4 deepens Section 1's data-flow diagrams

## Anti-patterns
- Skipping ASCII diagrams "because the plan is small." Diagrams are not bureaucracy; they are the reviewer's instrument for finding the gaps.
- Treating the security architecture sub-bullet as Section 3's problem. Auth boundaries belong here too — the architectural shape determines what Section 3 can even ask.
