---
name: SELECTIVE EXPANSION mode
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: framework
length_target: 300-800
related: [corpus/evaluation-frameworks/modes/scope-expansion.md, corpus/evaluation-frameworks/modes/hold-scope.md, corpus/office-hours/anti-sycophancy/]
---

# SELECTIVE EXPANSION mode

## What it is
The mode for plans whose stated scope is the baseline, but the user wants to see what else is possible. SELECTIVE EXPANSION runs the HOLD SCOPE analysis FIRST (complexity check + minimum-set check), then surfaces expansion candidates without bias. The cherry-pick ceremony presents each candidate individually with **neutral recommendation posture** — vivid, but not over-sold.

## When to use
- Feature enhancement or iteration on existing system → default mode
- User says "hold scope but tempt me," "show me options," "cherry-pick" → no question, SELECTIVE
- The plan is reasonable; the user wants to see what's adjacent without committing

## How to apply (the four moves)

**1. Complexity check (HOLD analysis first)**: If the plan touches more than 8 files or introduces more than 2 new classes/services, treat that as a smell. Challenge whether the same goal can be achieved with fewer moving parts.

**2. Minimum set check**: What is the minimum set of changes that achieves the stated goal? Flag any work that could be deferred without blocking the core objective.

**3. Expansion scan (candidates, not recommendations)**:
- 10x check: what's the version that's 10x more ambitious? Describe concretely.
- Delight opportunities: 30-minute improvements that would make the feature sing. List at least 5.
- Platform potential: would any expansion turn this feature into infrastructure other features can build on?

**4. Cherry-pick ceremony**:
- Present each expansion opportunity as its **own AskUserQuestion**
- **Neutral recommendation posture** — present opportunity, state effort (S/M/L) and risk, let the user decide without bias
- Options: **A)** Add to this plan's scope, **B)** Defer to TODOS.md, **C)** Skip
- If more than 8 candidates, present top 5-6 and note remainder as lower-priority
- Accepted items become plan scope for all remaining review sections
- Rejected items go to "NOT in scope"

## Critical: neutral posture ≠ flat prose
SELECTIVE EXPANSION's neutral recommendation posture is about not over-selling. It is NOT about being boring. Present vivid options, then let the user decide. The 0D-prelude framing rule still applies: lead with felt experience, close with effort. "Makes the product feel 10x more alive" is vivid (allowed). "This would 10x your revenue" is over-sell (forbidden). Evocative, not promotional.

## Required output format
Same CEO plan document as SCOPE EXPANSION (persisted to `~/.gstack/projects/$SLUG/ceo-plans/`), with the difference that the 10x check is the only Vision section (no Platonic ideal — that's an EXPANSION-only move). Scope Decisions table records each cherry-pick decision.

## Why it matters
Most plans don't deserve SCOPE EXPANSION's full treatment, but most plans also have 1-2 high-value adjacent moves the team would never surface unprompted. SELECTIVE EXPANSION is the mode that finds those moves without forcing them on the plan. The neutral posture is what makes the mode useful: aggressive recommendations would corrupt the user's judgment; flat prose would underweight the opportunities. Vivid + neutral is the sweet spot.

## Examples
1. **Plan refactors auth**: HOLD analysis shows the refactor touches 11 files (smell). Cherry-pick scan surfaces: refresh-token rotation (delight, ~1h CC), session-management UI (M effort), OAuth2 client surface (platform potential, L effort). Each presented neutrally; user picks zero or any subset.
2. **Plan adds a webhook receiver**: HOLD analysis confirms scope is right. Cherry-picks: structured retry visualization (delight), HMAC signature verification (security baseline), webhook replay UI (platform potential).

## Related entries
- `corpus/evaluation-frameworks/modes/scope-expansion.md` — EXPANSION is SELECTIVE's bigger sibling; pick based on context
- `corpus/evaluation-frameworks/modes/hold-scope.md` — HOLD is what runs first in SELECTIVE; SELECTIVE adds the surfacing
- `corpus/office-hours/anti-sycophancy/` — the neutral-posture rule defends against sycophantic over-selling

## Anti-patterns
- Defaulting to enthusiastic recommendation posture out of habit. SELECTIVE explicitly requires neutral posture; that's its differentiator.
- Surfacing candidates without running HOLD analysis first. The cherry-picks must be evaluated against an established baseline, not a fluid one.
- Batching the cherry-picks. Each one is its own AskUserQuestion; user sovereignty depends on it.
