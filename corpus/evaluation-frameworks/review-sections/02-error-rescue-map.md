---
name: Section 2 — Error & Rescue Map
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md, corpus/evaluation-frameworks/review-sections/01-architecture.md, corpus/evaluation-frameworks/review-sections/06-test-review.md]
---

# Section 2 — Error & Rescue Map

## What it is
The section that catches silent failures. It is not optional. For every new method, service, or codepath that can fail, Section 2 produces a two-part table: (a) what can go wrong and which exception class it produces; (b) is each exception rescued, what is the rescue action, and what does the user see. The output is the Error & Rescue Registry — one of the four highest-leverage outputs of the entire review.

## What it evaluates
For every new method or codepath:
- What can go wrong (timeouts, malformed responses, rate limits, pool exhaustion, record-not-found, etc.)
- Which exception class each failure mode produces
- Whether the exception is rescued
- What the rescue action is (retry, backoff, degrade, re-raise with context, return nil, etc.)
- What the user sees (specific message, transparent retry, "service temporarily unavailable," 500 error, etc.)

For LLM/AI service calls specifically: what happens when the response is malformed, empty, hallucinated invalid JSON, or a refusal? Each is a distinct failure mode and gets its own row.

## Required output format
```
  METHOD/CODEPATH          | WHAT CAN GO WRONG           | EXCEPTION CLASS
  -------------------------|-----------------------------|-----------------
  ExampleService#call      | API timeout                 | TimeoutError
                           | API returns 429             | RateLimitError
                           | API returns malformed JSON  | JSONParseError
                           | DB connection pool exhausted| ConnectionPoolExhausted
                           | Record not found            | RecordNotFound

  EXCEPTION CLASS              | RESCUED?  | RESCUE ACTION          | USER SEES
  -----------------------------|-----------|------------------------|------------------
  TimeoutError                 | Y         | Retry 2x, then raise   | "Service temporarily unavailable"
  RateLimitError               | Y         | Backoff + retry         | Nothing (transparent)
  JSONParseError               | N - GAP   | -                      | 500 error - BAD
  ConnectionPoolExhausted      | N - GAP   | -                      | 500 error - BAD
  RecordNotFound               | Y         | Return nil, log warning | "Not found" message
```

Any GAP row demands a follow-up: specify the rescue action and what the user should see.

## Rules in force
- Catch-all error handling (`rescue StandardError`, `catch (Exception e)`, `except Exception`) is ALWAYS a smell. Name the specific exceptions.
- Catching an error with only a generic log message is insufficient. Log the full context: what was being attempted, with what arguments, for what user/request.
- Every rescued error must either: retry with backoff, degrade gracefully with a user-visible message, or re-raise with added context. "Swallow and continue" is almost never acceptable.
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Silent failures are the most expensive bugs because they ship looking healthy. The Error & Rescue Map forces every failure mode to be named, classified, and either rescued or accepted as a known gap. A plan that survives Section 2 has zero unaccounted-for exceptions. A plan that doesn't is borrowing trouble that compounds in production.

## Examples
1. **External API call** with no rescue map: ships, works for weeks, then a vendor outage produces 500s for an hour because malformed responses crash the entire request thread. Section 2 would have caught it.
2. **LLM-backed feature**: response sometimes returns markdown code fences around JSON. Without Section 2, the parse fails silently and the user sees "something went wrong." Section 2 names the failure mode and demands the rescue.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/03-inversion-reflex.md` — Section 2 is inversion-reflex made into a deliverable
- `corpus/evaluation-frameworks/review-sections/01-architecture.md` — Section 1's error-path diagrams seed Section 2's table
- `corpus/evaluation-frameworks/review-sections/06-test-review.md` — every rescued exception in Section 2 should map to a test in Section 6

## Anti-patterns
- Treating "we'll add error handling during implementation" as sufficient. Implementation will add `rescue StandardError` and call it done. The map must exist before the code does.
- Logging without acting. A log line is not a rescue. The map demands what the user actually sees.
