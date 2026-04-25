---
name: Timeout and Rate-limit UX
domain: ai-product-ux
source_skill: research
entry_type: pattern
length_target: 600
related: [corpus/ai-product-ux/patterns/graceful-degradation.md, corpus/ai-product-ux/failure/design-the-failure-first.md, corpus/ai-product-ux/failure/error-recovery-paths.md, corpus/pm-frameworks/ai-product-pm/non-determinism.md, corpus/ux-principles/audit/05-interaction]
---

# Timeout and Rate-limit UX

## What it is
A pattern for the two most common AI-API failure modes: **timeout** (the model takes too long) and **rate limit** (the API has throttled the request). Neither is in the source skill's list but both bridge from `failure/design-the-failure-first.md`. The pattern: time-box every model call, communicate the wait honestly, and offer a meaningful action when the wait fails. Public AI UX canon — Google PAIR's loading-state guidelines, Anthropic's streaming-response patterns, OpenAI's rate-limit handling docs — converges on the same shape.

## Why it matters
Model calls are slow and bursty. A user who hits a 30-second timeout once and gets no recovery path will not retry. A user who hits "rate limit exceeded — try again later" with no guidance on when later is, will stop relying on the product. These two failures are unavoidable in production; what's avoidable is the trust loss. Designed timeout/rate-limit UX preserves the relationship across the failure.

## How to apply
1. **Time-box every call.** Set a hard ceiling (typically 15–30s for synchronous UI calls). A spinner without a ceiling is worse than a fast no.
2. **Stream when possible.** A streaming response with visible token-by-token output reads as fast even when total latency is high. The perceived wait drops dramatically.
3. **Honest progress, not fake progress.** "Retrieving sources... synthesizing... ~10s remaining" beats a generic spinner. If you can't estimate, show what step is running.
4. **Rate-limit messages must offer a path.** "Rate limit reached. We'll resume in 2 minutes — or queue this request and we'll notify you when it runs." Never just "try again later."
5. **Differentiate transient from systemic.** A one-off timeout = retry. A repeated rate-limit = upgrade tier or queue. Surface the difference.

## Examples
1. **Context Layer Demo's streaming synthesis.** The five-step flow streams progress in real time — retrieve, filter, score, align, synthesize. A 12-second total call reads as continuous progress rather than a single long wait.
2. **Suzy Decision Engine's queue path.** When automated insight generation queues behind capacity, the product surfaces an estimated time and an option to be notified — the wait becomes asynchronous instead of stuck.
3. **Anthropic API's streaming response pattern.** Token-by-token output makes long Claude responses feel responsive. The pattern is borrowed from there.

## Related entries
- `corpus/ai-product-ux/patterns/graceful-degradation.md` — parent pattern
- `corpus/ai-product-ux/failure/design-the-failure-first.md` — the rule
- `corpus/ai-product-ux/failure/error-recovery-paths.md` — retry is the canonical path here
- `corpus/pm-frameworks/ai-product-pm/non-determinism.md` — why this is unavoidable
- `corpus/ux-principles/audit/05-interaction` — general loading-state UX

## Anti-patterns
- **Eternal spinner.** No timeout, no progress, no path. The user assumes the product is broken and reloads — losing context.
- **Generic "try again later."** Rate-limit messages with no time estimate and no queue option. The user has no way to plan around the limit.
