---
name: Parallel Data Collection Step
domain: website-audit
source_skill: website-audit
entry_type: pattern
length_target: 600-900
related: [corpus/website-audit/methodology/bootstrap.md, corpus/website-audit/methodology/severity-scoring.md, corpus/website-audit/dimensions/]
---

# Parallel Data Collection Step

## What it is
The second and largest step of the audit. Runs all dimension-level data collection in parallel where the tool ecosystem allows. If a single sub-step errors, log the failure and continue — the audit doesn't abort on partial failures. Each sub-step is one of 11 parallel tracks.

**The 11 sub-steps:**

- **2a SEO** — Ahrefs GSC tools for keyword/page/performance data
- **2b Backlinks** — Ahrefs Site Explorer for own-domain backlink data
- **2c AIO** — LLM citation tracking against the 20-query set
- **2d Traffic & Engagement** — Zapier → Google Analytics
- **2e Usability** — Vercel runtime logs + Lighthouse + axe-core
- **2f Design** — theme engine smoke test + visual regression
- **2g Brand** — voice violation scan + domain balance + cross-platform consistency
- **2h Technical QA** — broken links + builds + dependencies + headers + SSL + bundles
- **2i Chatbot** — sample 30 conversations + LLM-as-judge across 4 rubrics
- **2j Quarterly re-baseline** — only if `is_quarterly_rebaseline = true`
- **2k Keyword research** — Notion DB read + GSC cross-ref + SERP review

## Why it matters
The audit only finishes in 30 minutes because the data collection runs in parallel. Run sequentially, this step alone would take 2+ hours. Parallel execution is also fault-tolerant: a single tool failure (Ahrefs quota, Lighthouse timeout, Vercel API hiccup) only kills its specific sub-step, not the whole run.

The 11 sub-step structure also lets the audit be partially run when needed. If the next-quarterly check is approaching, the operator can run Step 2j manually without re-running the whole audit. If a deployment broke something and quick visibility is needed, Step 2e can run on its own.

## How to apply
- Run sub-steps in parallel up to the tool ecosystem's concurrency limits.
- For each sub-step, capture both successful results and explicit failure modes. A "Lighthouse timed out on /thinking/foo" finding is different from "Lighthouse data unavailable."
- If a sub-step errors, mark its section as `data unavailable` in the report with the error reason. Log under `Run notes`. Continue to the next.
- Do not retry within a sub-step indefinitely. One retry on transient failures (rate limits, network blips); after that, fail and continue.

For each sub-step, the specific tool calls are:

**2a SEO:** `Ahrefs:gsc-keywords` (last 7d, last 28d), `Ahrefs:gsc-pages` (last 28d), `Ahrefs:gsc-performance-history` (12-week trend), `Ahrefs:gsc-anonymous-queries`, `Ahrefs:gsc-ctr-by-position`, `Ahrefs:gsc-positions-history`. Then compute: top 20 queries by impressions with WoW deltas, pages with rank changes ≥3 WoW, quick-win queries (4-10 with ≥100 impressions), high-impression low-CTR pages, new queries appearing first time this week.

**2b Backlinks:** `Ahrefs:site-explorer-domain-rating`, `Ahrefs:site-explorer-refdomains-history` (90 days), `Ahrefs:site-explorer-domain-rating-history` (90 days), `Ahrefs:site-explorer-all-backlinks` filtered to last 7 days. Capture DR current vs last week, new and lost referring domains.

**2c AIO:** Build the 20-query set per `corpus/growth/seo/free-stack-overview.md`. For each query × 3 LLMs (Claude, ChatGPT, Perplexity) = 60 calls. Parse responses for richezamor.com presence; classify as `cited_first` / `cited` / `mentioned` / `absent`. Compare to last week. Also check AI crawler accessibility (HEAD on robots.txt, render check on home for JS-only content).

**2d Traffic:** `Zapier:list_enabled_zapier_actions` first to confirm available GA actions. Then `Zapier:execute_zapier_read_action` for sessions/users/pageviews, source/medium breakdown, top pages, conversion events, audience signals.

**2e Usability:** `Vercel:get_runtime_logs` (7 days) for 4xx/5xx counts. Lighthouse against 8 critical pages. axe-core/pa11y for accessibility on the same 8 pages.

**2f Design:** Code execution that loads each of 8 pages, cycles 4 theme states, screenshots each, runs pixelmatch diff vs. baseline. Code execution scan of /thinking articles published this week for inline styles. Cross-browser check (monthly only).

**2g Brand:** Regex pass + LLM-as-judge for AI tells in /thinking articles published past 7 days. Content Topics DB query for trailing 30-day domain split. Multi-platform scrape + LLM-as-judge for cross-platform consistency. Full-text site scan for forbidden terminology.

**2h Technical QA:** `lychee` broken-link crawl. `Vercel:list_deployments` last 14 days. `npm audit` and `npm outdated` (clone repo to /tmp). HTTP header fetch. Cert validation. Image optimization spot check.

**2i Chatbot:** Sample 30 conversations from chatbot's logging database. LLM-as-judge each on factual accuracy, voice fidelity, citation correctness, refusal handling. Automated UI test for the comparison toggle.

**2j Quarterly:** Per `corpus/website-audit/competitor-benchmarking/read-protocol.md`.

**2k Keyword research:** Per `corpus/website-audit/dimensions/categories/keyword-research.md`.

## Examples
1. **Standard run, no failures.** All 11 sub-steps complete in 18 minutes total. Step 2 hands off to Step 3 (synthesis) with full data.
2. **Partial failure, audit continues.** Lighthouse times out on 2 of 8 pages. Marked `data unavailable` for those pages; Step 2e completes for the other 6. Audit continues; Run notes flag the gap.
3. **Quarterly run.** Step 2j runs in addition to the standard 10. Total runtime: 52 minutes. Audit still completes; Cowork doesn't time out.

## Related entries
- `corpus/website-audit/methodology/bootstrap.md` — predecessor step
- `corpus/website-audit/methodology/severity-scoring.md` — successor step
- `corpus/website-audit/dimensions/seo/` — what 2a feeds into
- `corpus/website-audit/dimensions/aio/` — what 2c feeds into
- `corpus/website-audit/dimensions/categories/` — what 2d-2i feed into

## Anti-patterns
- Aborting the whole run on a single sub-step failure. The audit is designed to be fault-tolerant.
- Running sub-steps sequentially "to be safe." Parallel is the default; sequential is a 4x slowdown for no benefit.
