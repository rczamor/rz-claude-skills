---
name: Error Recovery Paths
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 600
related: [corpus/ai-product-ux/patterns/graceful-degradation.md, corpus/ai-product-ux/failure/design-the-failure-first.md, corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md, corpus/ai-product-ux/failure/hallucination-handoff.md]
---

# Error Recovery Paths

## What it is
A template: every AI failure must offer at least one of three recovery paths — **retry**, **refine**, **fall back to human**. The user is never trapped at a dead end. The path the product offers depends on the failure type, but the user always has agency.

## Why it matters
A failed AI call without a recovery path is a failed product moment. The user has invested attention, gotten nothing, and has no clear next move. They either abandon (churn) or repeat the same prompt and get the same failure (frustration). Both outcomes degrade trust. Offering a designed recovery path converts a failure into a workflow step — slower than success, but still moving forward.

## How to apply
1. **Retry** — for transient failures (timeout, rate limit, network). One-click, with a brief explanation of why retrying is likely to work this time. Cap automatic retries to avoid loops.
2. **Refine** — for under-specified or ambiguous prompts. Surface what the model couldn't disambiguate ("I wasn't sure whether you meant X or Y") and let the user pick or rephrase.
3. **Fall back to human** — for high-stakes or repeatedly-failing cases. Hand off cleanly: route to support, surface raw source data the user can review directly, or open a workflow that puts a human in the loop.
4. **Choose based on the failure type, not the error code.** Network timeout = retry. Empty model output = refine. Detected hallucination on a high-stakes prompt = fall back to human.

## Examples
1. **Context Layer Demo's three buttons under a failed synthesis.** "Retry synthesis" (transient model issue), "Refine your question" (the prompt was ambiguous and the demo says so), "Show me the raw sources" (fall back — let the user read the underlying context directly). The user is never trapped.
2. **Suzy Decision Engine's "request analyst review" path.** When the automated insight cannot pass the confidence threshold, the system routes the request to a human analyst with full context attached. The fall-back is a feature, not a fail-safe.
3. **GitHub Copilot's "no suggestion + keep typing" path.** When Copilot has nothing useful, the user just keeps typing. The recovery path is invisible by design — the IDE keeps working.

## Related entries
- `corpus/ai-product-ux/patterns/graceful-degradation.md` — the parent pattern
- `corpus/ai-product-ux/failure/design-the-failure-first.md` — the rule that demands these paths exist
- `corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md` — when retry is the right path
- `corpus/ai-product-ux/failure/hallucination-handoff.md` — when fall-back is the right path

## Anti-patterns
- **Retry-only recovery.** Every error gets a retry button regardless of failure type. The user retries the same prompt three times, gets the same failure, and abandons.
- **Fall-back-only recovery.** Every error routes to human support, even transient ones. The support queue floods with retryable issues and trust in the AI drops to zero.
