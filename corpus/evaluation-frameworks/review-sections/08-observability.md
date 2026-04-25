---
name: Section 8 — Observability & Debuggability Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/07-proxy-skepticism.md, corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md, corpus/evaluation-frameworks/review-sections/07-performance.md]
---

# Section 8 — Observability & Debuggability Review

## What it is
New systems break. Section 8 ensures you can see why. It evaluates structured logging, metrics, distributed tracing, alerting, dashboards, debuggability ("can you reconstruct what happened from logs alone, 3 weeks post-ship?"), admin tooling, and runbooks. The principle is "observability is not optional — new codepaths need logs, metrics, or traces." A plan that ships without Section 8's outputs is a plan whose bugs will be diagnosed by reading Slack messages from confused users.

## What it evaluates
- Logging — for every new codepath: structured log lines at entry, exit, and each significant branch?
- Metrics — for every new feature: what metric tells you it's working? What tells you it's broken?
- Tracing — for new cross-service or cross-job flows: trace IDs propagated?
- Alerting — what new alerts should exist?
- Dashboards — what new dashboard panels do you want on day 1?
- Debuggability — if a bug is reported 3 weeks post-ship, can you reconstruct what happened from logs alone?
- Admin tooling — new operational tasks that need admin UI or rake tasks?
- Runbooks — for each new failure mode: what's the operational response?

## Required output format
```
  CODEPATH                    | LOGS | METRICS                      | TRACE | ALERT
  ----------------------------|------|------------------------------|-------|------------------
  ExportService#run           | Y    | exports.duration, exports.errors | Y | exports.errors > 5/min
  WebhookProcessor#process    | Y    | webhooks.processed, webhooks.failed | Y | failed > 10/min
  PaymentService#charge       | Y    | payments.success, payments.failure | Y | failure rate > 1%
```

Plus runbooks per failure mode:
```
  FAILURE MODE                       | OPERATIONAL RESPONSE
  -----------------------------------|-----------------------------------------
  Webhook backlog > 1000             | Scale workers; check vendor incident page
  Payment gateway error spike        | Check Stripe status; failover to backup
  Export job > 10 min                | Investigate query; toggle feature flag
```

## Mode-specific addition
**EXPANSION and SELECTIVE EXPANSION**: also evaluate what observability would make this feature a joy to operate. (For SELECTIVE EXPANSION, include observability for any accepted cherry-picks.)

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
The most expensive bugs are the ones you can't see. A plan that ships without observability is a plan whose failure modes ship into the dark. Section 8's structured-log + metric + trace + alert combination is what makes "the system tells you when it breaks, before users do." The runbook requirement is intentional: every alert that fires without a runbook produces a 2am scramble. Every alert with a runbook produces a 5-minute mitigation.

## Examples
1. **Plan ships a new background job** with no metrics. 3 weeks later, queue backs up; nobody notices for hours. Section 8 would have demanded `jobs.queued`, `jobs.processed`, `jobs.failed`, plus an alert on backlog growth.
2. **New webhook receiver**: plan logs nothing structured. A vendor changes their payload format; failures are silent for days. Section 8 demands structured logs at receive/parse/dispatch with full payload context.
3. **Cross-service flow**: plan ships without trace ID propagation. Debugging requires correlating timestamps across 4 services. Section 8 would have demanded trace IDs at the entry point.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/07-proxy-skepticism.md` — Section 8's metric choices need proxy-skepticism applied
- `corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md` — every Section 2 rescue should produce a Section 8 metric
- `corpus/evaluation-frameworks/review-sections/07-performance.md` — Section 7's slow paths must be observable per Section 8

## Anti-patterns
- "We'll add metrics post-launch." Almost never happens. Plans that ship without observability operate without it for years.
- Logging without structure (printf-style messages with no fields). Unsearchable, uncorrelatable, useless 3 weeks later.
