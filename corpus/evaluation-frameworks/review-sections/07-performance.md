---
name: Section 7 — Performance Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/14-leverage-obsession.md, corpus/evaluation-frameworks/review-sections/01-architecture.md, corpus/evaluation-frameworks/review-sections/08-observability.md]
---

# Section 7 — Performance Review

## What it is
Section 7 evaluates the plan's performance posture: N+1 queries, memory usage, database indexes, caching opportunities, background job sizing, slow paths, and connection-pool pressure. The output is a concrete list of performance concerns with proposed fixes — not a benchmark suite, but the design-time review that prevents the plan from shipping with foreseeable performance issues.

## What it evaluates
- N+1 queries — for every new ActiveRecord association traversal: is there an `includes`/`preload`?
- Memory usage — for every new data structure: what's the maximum size in production?
- Database indexes — for every new query: is there an index?
- Caching opportunities — for every expensive computation or external call: should it be cached?
- Background job sizing — for every new job: worst-case payload, runtime, retry behavior?
- Slow paths — top 3 slowest new codepaths and estimated p99 latency
- Connection pool pressure — new DB connections, Redis connections, HTTP connections?

## Required output format
A findings list:
```
  CONCERN                                    | LOCATION              | FIX
  -------------------------------------------|-----------------------|----------------------
  N+1 in ProjectsController#index            | projects_controller.rb| Add includes(:owner)
  No index on jobs.user_id + jobs.created_at | jobs table            | Composite index
  Worst-case 50MB JSON payload in memory     | ExportJob             | Stream to file
  10x DB connections per request peak        | new sync flow         | Move to background
```

Plus the slow-paths estimate:
```
  CODEPATH                       | ESTIMATED p99
  -------------------------------|---------------
  ExportService#run_full         | ~8s
  AnalyticsAggregator#compute    | ~4s
  WebhookProcessor#process_batch | ~12s
```

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Performance issues caught at plan time are cheap design changes. The same issues caught after launch require P99 emergencies, schema migrations under load, and emergency cache rollouts. Section 7's fixed inventory (N+1, indexes, memory, caching, jobs, slow paths, pools) catches 80% of foreseeable performance problems with a 5-minute review. The other 20% are caught in production by Section 8's observability — but only if the design didn't preclude observability (it sometimes does).

## Examples
1. **Plan adds a new index page**: Section 7 surfaces N+1 because the plan iterates `projects.each { |p| p.owner.name }` without preload. Fix: add `.includes(:owner)`.
2. **New background job processes user data**: Section 7 surfaces — worst case 100k records per job. The plan loads them all into memory. Fix: batch in chunks of 1k, stream to output.
3. **New endpoint hits a third-party API**: Section 7 surfaces — no caching, called on every request. Fix: cache for the natural lifetime of the data (5 minutes? 1 hour?), with explicit invalidation.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/14-leverage-obsession.md` — Section 7's caching wins are pure leverage
- `corpus/evaluation-frameworks/review-sections/01-architecture.md` — Section 1's "what breaks first under 10x load?" feeds Section 7
- `corpus/evaluation-frameworks/review-sections/08-observability.md` — Section 8 ensures Section 7's slow paths are measurable in production

## Anti-patterns
- Premature optimization (over-caching, over-indexing). Section 7 is for known concerns, not theoretical ones.
- Treating "we have monitoring" as Section 7's substitute. Monitoring catches what shipped; Section 7 prevents it from shipping.
