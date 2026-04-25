---
name: Section 3 — Security & Threat Model
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/02-paranoid-scanning.md, corpus/evaluation-frameworks/review-sections/01-architecture.md, corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md]
---

# Section 3 — Security & Threat Model

## What it is
Security is not a sub-bullet of architecture. It gets its own section. Section 3 evaluates the attack surface introduced by the plan, input validation, authorization scoping, secrets handling, dependency risk, data classification, injection vectors (SQL, command, template, LLM prompt), and audit logging. Every finding is rated for likelihood and impact, and the plan must show how each is mitigated.

## What it evaluates
- Attack surface expansion — what new attack vectors does this plan introduce? New endpoints, new params, new file paths, new background jobs?
- Input validation — for every new user input: validated, sanitized, rejected loudly on failure? What happens with: nil, empty string, string when integer expected, string exceeding max length, unicode edge cases, HTML/script injection attempts?
- Authorization — for every new data access: scoped to the right user/role? Direct object reference vulnerability? Can user A access user B's data by manipulating IDs?
- Secrets and credentials — new secrets? In env vars, not hardcoded? Rotatable?
- Dependency risk — new gems/npm packages? Security track record?
- Data classification — PII, payment data, credentials? Handling consistent with existing patterns?
- Injection vectors — SQL, command, template, LLM prompt injection — check all
- Audit logging — for sensitive operations: is there an audit trail?

## Required output format
For each finding: threat description, likelihood (High/Med/Low), impact (High/Med/Low), and whether the plan mitigates it. Findings without explicit mitigation become a flagged gap.

```
  THREAT                                | LIKELIHOOD | IMPACT | MITIGATED?
  --------------------------------------|------------|--------|-----------
  IDOR on /api/projects/{id}            | High       | High   | N - GAP
  SQL injection on search param         | Low        | High   | Y (parameterized)
  Prompt injection on user-supplied text| Med        | Med    | N - GAP
  Hardcoded API key in config           | Low        | High   | Y (env var)
```

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Security failures are reputational accelerators. A plan that ships with an IDOR or a prompt-injection vulnerability does not just produce a bug — it produces a story. Section 3 forces the threat-modeling work that teams under deadline pressure default to skipping. The likelihood/impact format prevents both over-paranoia (rejecting plans for theoretical low-impact issues) and under-paranoia (waving away high-impact issues because they're "edge cases").

## Examples
1. **New API endpoint** that takes a project ID. Section 3 surfaces the IDOR question: can user A pass user B's project ID? If yes, mitigation is server-side authorization — not client-side filtering.
2. **LLM-backed feature** where users submit prompts. Section 3 surfaces prompt injection — what happens when a user pastes "ignore previous instructions"? Mitigation is structured prompts, sanitization, and bounded outputs.
3. **New dependency** for PDF generation. Section 3 surfaces: dependency risk (last release? CVE history?), command-injection vectors (does the library shell out?), file-system access scope.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/02-paranoid-scanning.md` — Section 3 is paranoid scanning operationalized
- `corpus/evaluation-frameworks/review-sections/01-architecture.md` — Section 1's security architecture sub-bullet seeds Section 3
- `corpus/evaluation-frameworks/review-sections/04-data-flow-edge-cases.md` — Section 4's input-validation shadow paths overlap with Section 3's input validation

## Anti-patterns
- Treating "we'll do a security review before launch" as Section 3's mitigation. The threat model must be explicit in the plan, not deferred to a future review.
- Listing threats without mitigations. A threat without a mitigation is a known gap, not a complete row.
