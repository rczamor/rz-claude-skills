---
name: Section 6 — Test Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/16-edge-case-paranoia-design.md, corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md, corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md]
---

# Section 6 — Test Review

## What it is
Section 6 makes a complete diagram of every new thing the plan introduces — UX flows, data flows, codepaths, background jobs, integrations, error/rescue paths — and then demands a happy-path test, failure-path test, and edge-case test for each. It includes the test ambition check ("what's the test that would make you confident shipping at 2am on a Friday?") and the chaos test. Section 6 is the section that ensures the plan doesn't ship with a smoke-test surface and a pile of unmonitored failure modes.

## What it evaluates
For every new feature in the plan, generate the diagram:
```
  NEW UX FLOWS:
    [list each new user-visible interaction]

  NEW DATA FLOWS:
    [list each new path data takes through the system]

  NEW CODEPATHS:
    [list each new branch, condition, or execution path]

  NEW BACKGROUND JOBS / ASYNC WORK:
    [list each]

  NEW INTEGRATIONS / EXTERNAL CALLS:
    [list each]

  NEW ERROR/RESCUE PATHS:
    [list each — cross-reference Section 2]
```

For each item:
- What type of test covers it? (Unit / Integration / System / E2E)
- Does a test for it exist in the plan? If not, write the test spec header.
- Happy path test — what is it?
- Failure path test — be specific (which failure?)
- Edge case test — nil, empty, boundary values, concurrent access

**Test ambition check** (all modes):
- What's the test that would make you confident shipping at 2am on a Friday?
- What's the test a hostile QA engineer would write to break this?
- What's the chaos test?

**Test pyramid check**: Many unit, fewer integration, few E2E? Or inverted?
**Flakiness risk**: flag any test depending on time, randomness, external services, or ordering.
**Load/stress test requirements**: for any new codepath called frequently or processing significant data.

For LLM/prompt changes: check CLAUDE.md for the "Prompt/LLM changes" file patterns. If this plan touches any of those patterns, state which eval suites must be run, which cases should be added, and what baselines to compare against.

## Required output format
The complete diagram above, plus per-item test specs (happy / failure / edge), plus the three test-ambition answers (2am Friday, hostile QA, chaos), plus the test-pyramid assessment, plus flakiness-risk flags.

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Tests written from a "list every codepath" inventory are robust. Tests written from "let me re-read the plan and write what comes to mind" are decorative. Section 6's diagram-first approach is what produces tests that actually catch regressions. The 2am Friday question is intentional: it filters out unit tests that pass on the happy path but tell you nothing about whether the system is healthy.

## Examples
1. **Plan adds a new background job**. Section 6 surfaces: happy path (job runs successfully), failure path (job fails after 3 of 10 items processed — does it resume or restart?), edge case (job runs twice due to retry — is it idempotent?), 2am Friday (queue backed up 2 hours — what alerts fire?).
2. **LLM-backed plan**. Section 6 demands: which eval suite, which new cases, which baseline. "We'll write evals later" is not a Section 6-pass.
3. **Inverted pyramid**: plan describes 14 E2E tests and 0 unit tests. Section 6 flags the inversion and proposes refactoring tests downward.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/16-edge-case-paranoia-design.md` — pattern 16 supplies Section 6's edge-case inventory
- `corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md` — every rescued exception in Section 2 should map to a Section 6 test
- `corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md` — Section 4's interaction edge cases become Section 6 test cases

## Anti-patterns
- Listing tests without specifying what each one asserts. "Test the happy path" is not a test spec.
- Skipping the chaos test because "it's hard to write." That difficulty IS the signal that the system is fragile.
