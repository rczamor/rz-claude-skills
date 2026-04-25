---
name: Section 5 — Code Quality Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md, corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md, corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md]
---

# Section 5 — Code Quality Review

## What it is
Section 5 evaluates code-level quality concerns at the plan level: organization and module structure fit, DRY violations, naming, error handling patterns (cross-referenced with Section 2), missing edge cases (cross-referenced with Section 4), over- and under-engineering, and cyclomatic complexity. It is the section where a plan's code-level taste is rendered legible — not by line-by-line review (that's PR review's job) but by surfacing architectural code smells that the plan implies.

## What it evaluates
- Code organization and module structure — does new code fit existing patterns? If it deviates, is there a reason?
- DRY violations — be aggressive. If the same logic exists elsewhere, flag it and reference the file and line
- Naming quality — are new classes, methods, and variables named for what they do, not how they do it?
- Error handling patterns (cross-reference with Section 2 — this section reviews the patterns; Section 2 maps the specifics)
- Missing edge cases — list explicitly: "What happens when X is nil?" "When the API returns 429?" etc.
- Over-engineering check — any new abstraction solving a problem that doesn't exist yet?
- Under-engineering check — anything fragile, assuming happy path only, or missing obvious defensive checks?
- Cyclomatic complexity — flag any new method that branches more than 5 times. Propose a refactor.

## Required output format
A list of findings, each with: file/module reference (or plan-section reference if code doesn't exist yet), category (organization, DRY, naming, error pattern, edge case, over-engineered, under-engineered, complexity), and proposed fix.

```
  FINDING                                          | CATEGORY        | FIX
  -------------------------------------------------|-----------------|------------------------------
  Plan introduces ProjectFetcher AND ProjectLoader | DRY             | Pick one; consolidate
  ExportService#run branches 7 ways                | Complexity      | Extract strategy per branch
  New abstraction "ContextManagerFactory" with     | Over-engineered | Inline; revisit if needed
    one implementation                             |                 |
```

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Code quality findings caught at plan time cost minutes to fix. The same findings caught at PR time cost hours. Caught in production they cost days and trust. Section 5 is the cheap-fix-window: the plan still has fluidity, no engineer is invested in the code yet, the architectural smells are still small. The over- and under-engineering checks are particularly load-bearing: most plans drift toward one of these two failure modes by the time implementation starts.

## Examples
1. **DRY violation**: plan introduces a `UserExporter` and the codebase already has a `UserSerializer` doing 80% of the same work. Flag with file reference; propose consolidation.
2. **Over-engineered**: plan introduces a "ContextManagerFactory" with one production implementation and one test stub. The factory is solving a problem that does not exist. Flag for inlining.
3. **Under-engineered**: plan saves user input directly to DB without nil-check, length-cap, or trim. Section 5 surfaces this; Section 4's data-flow shadow paths confirm the gap.
4. **Complexity**: plan describes a method that handles 7 branching cases inline. Propose strategy pattern or table-dispatch.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/04-focus-as-subtraction.md` — over-engineering check is subtraction applied to code
- `corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md` — Section 2 maps the specifics; Section 5 reviews the pattern
- `corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md` — Section 4's shadow paths feed Section 5's missing-edge-case checks

## Anti-patterns
- Letting "we'll clean it up later" stand. Code quality findings caught at plan time are the cheapest. "Later" rarely arrives.
- Demanding every method be DRY. Premature DRY produces brittle abstractions. The DRY check is for actual duplication, not surface similarity.
