---
name: Section 4 — Data Flow & Interaction Edge Cases
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/16-edge-case-paranoia-design.md, corpus/evaluation-frameworks/review-sections/01-architecture.md, corpus/evaluation-frameworks/review-sections/05-code-quality.md]
---

# Section 4 — Data Flow & Interaction Edge Cases

## What it is
Section 4 traces data through the system and interactions through the UI with adversarial thoroughness. It produces two outputs: an ASCII diagram of every new data flow showing shadow paths at each node (nil, empty, wrong type, exception, timeout, conflict, dup key, encoding) and an interaction edge case table for every new user-visible interaction. Every unhandled edge case is flagged as a gap with a specified fix.

## What it evaluates
**Data Flow Tracing** — for every new data flow:
```
  INPUT --> VALIDATION --> TRANSFORM --> PERSIST --> OUTPUT
    |            |              |            |           |
    v            v              v            v           v
  [nil?]    [invalid?]    [exception?]  [conflict?]  [stale?]
  [empty?]  [too long?]   [timeout?]    [dup key?]   [partial?]
  [wrong    [wrong type?] [OOM?]        [locked?]    [encoding?]
   type?]
```
For each node: what happens on each shadow path? Is it tested?

**Interaction Edge Cases** — for every new user-visible interaction:
```
  INTERACTION          | EDGE CASE              | HANDLED? | HOW?
  ---------------------|------------------------|----------|--------
  Form submission      | Double-click submit    | ?        |
                       | Submit with stale CSRF | ?        |
                       | Submit during deploy   | ?        |
  Async operation      | User navigates away    | ?        |
                       | Operation times out    | ?        |
                       | Retry while in-flight  | ?        |
  List/table view      | Zero results           | ?        |
                       | 10,000 results         | ?        |
                       | Results change mid-page| ?        |
  Background job       | Job fails after 3 of   | ?        |
                       | 10 items processed     |          |
                       | Job runs twice (dup)   | ?        |
                       | Queue backs up 2 hours | ?        |
```
Any unhandled edge case becomes a flagged gap with a specified fix.

## Required output format
ASCII data-flow diagram with shadow paths annotated under each node. Interaction edge case table with HANDLED? marked Y/N/? and the HOW? column populated for every Y. Every N or ? becomes a gap to address.

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Section 4 is where most plans break. Plans look good when reviewed against the happy path. Section 4's adversarial thoroughness — every shadow path at every node, every interaction edge case — produces the gaps that determine whether the feature ships robustly or ships and immediately starts generating support tickets. The shadow-path notation is intentional: it forces the reviewer to physically write `[nil?]` under each node, which surfaces gaps that prose review will skip.

## Examples
1. **Plan**: "User submits a form, server saves, redirects to confirmation." Section 4 surfaces: what about double-click submit? Form submitted during deploy (old code receives, new code persists)? CSRF token expired by the time they submit? None of these are addressed in the plan; each becomes a gap.
2. **Async operation plan**: "User starts a long-running export." Section 4 surfaces: user navigates away mid-export — does it cancel or continue? User retries while the first request is in flight — duplicate work or idempotent? Operation times out at 30s — what does the user see at 31s?
3. **List view plan** for "show recent items." Section 4 surfaces: zero items (empty state), 10k items (pagination/virtualization), items added while user is reading (does the page jump?).

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/16-edge-case-paranoia-design.md` — pattern 16 is the underlying instinct for Section 4
- `corpus/evaluation-frameworks/review-sections/01-architecture.md` — Section 1's data-flow diagrams are the input to Section 4's shadow-path treatment
- `corpus/evaluation-frameworks/review-sections/05-code-quality.md` — Section 5's "missing edge cases" check overlaps with Section 4

## Anti-patterns
- Treating empty states and zero-result paths as "polish for later." They are first-class in Section 4 and ship with v1.
- Filling the table with `Y` based on wishful thinking. Section 4 demands the HOW? column — `Y` without a specified handling pattern is functionally `?`.
