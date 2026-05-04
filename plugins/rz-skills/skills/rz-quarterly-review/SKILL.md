---
name: rz-quarterly-review
description: >
  Use when invoked via /rz-quarterly-review, when Riché asks to "run the quarterly review", "set Q[N] priorities", "do quarterly planning", "review the quarter", or on the first Sunday of January, April, July, or October. The structured 60-90 minute end-of-quarter process: pull metrics, re-score every active channel against the 5-criteria framework, gate-check deferred candidates (newsletter, YouTube, podcast hosting, etc.), pick 1-3 priorities for the next quarter using the priorities template, write the full review to the Quarterly Reviews Notion DB, and seed Linear tasks for the first concrete action of each priority. Tactical companion to the role-based `rz-growth-marketing`; reads strategic frames from `corpus/growth/` and produces a quarter-specific bet.
---

# Quarterly Review — Riché Zamor

The end-of-quarter strategic review for the personal brand. Runs the 60-min process from `corpus/growth/playbook/quarterly-channel-review.md`, plus 30 min of Notion writing and Linear seeding. Produces one Notion page in the Quarterly Reviews DB, 1-3 named priorities, and 1-3 Linear seed tasks.

This is a tactical skill (sibling to `rz-website-audit`). It executes a process; it does not own the strategic frames. The strategic frames live in `corpus/growth/` and are owned by `rz-growth-marketing`.

## Cross-skill dependencies (read these first)

The review reads from canonical sources owned by other skills.

**Strategic frames are owned by `rz-growth-marketing`.** Pull from `corpus/growth/strategy/` for the channel evaluation framework, channel maturity model, owned-vs-rented allocation rule, audience portability, repurposing matrix, and creator-as-product dynamics. From `corpus/growth/creator-dynamics/` for voice, narrative, and quality-frequency frames. From `corpus/growth/diagnostics/` for engagement-drop and algorithm-change interpretation. The review applies these; it does not redefine them.

**Process and templates are owned by `rz-growth-marketing`.** Pull from `corpus/growth/playbook/quarterly-channel-review.md` for the 60-min Block 1-6 structure, from `corpus/growth/playbook/quarterly-priorities-template.md` for the priority format, from `corpus/growth/playbook/channel-gates-for-adding.md` for deferred-candidate gates, and from `corpus/growth/playbook/cutting-criteria.md` for retirement decisions.

**Channel-ROI methodology is owned by `rz-growth-marketing`.** Pull from `corpus/growth/metrics/channel-roi-calculation.md` for the formula and weights.

**Database schemas:** `corpus/growth/databases/quarterly-reviews-schema.md` defines the output DB structure.

**Recent website audit data** comes from `rz-website-audit`'s most recent Sunday run. The Quarterly Review reads the most recent Weekly Audits DS page (and the prior 12 weekly pages for trend) to inform channel-level signals on richezamor.com performance.

If a strategic frame's text is being applied differently than the canonical corpus says, the canonical corpus wins. Surface drift in `rz-self-improve`.

## Constants

```
RUN_TIMEZONE                   = America/New_York
QUARTERLY_REVIEW_MONTHS        = January, April, July, October (first Sunday)
LINEAR_TEAM_ID                 = 72132418-b477-4450-a30a-77391d5cfc47   (Riche Zamor team)
LINEAR_PROJECT_ID              = 085484ef-b523-4142-bce2-7f9a23a05fa1   (Brand project)
LINEAR_ASSIGNEE_ID             = 646e8aef-65f5-47de-ba40-4f2ad99bbc15   (Riché)
NOTION_BRAND_PARENT_ID         = 333ac0ea4f658086bcafcd3f53299b89       (Brand)
NOTION_GROWTH_STRATEGY_PAGE_ID = 356ac0ea4f6580828e68f93292e3ea9d       (Brand → Growth Strategy)
NOTION_QUARTERLY_REVIEW_DB_ID  = f51277cdd4d94f8e83c81cd1c08f82e8       (Quarterly Reviews DB)
NOTION_QUARTERLY_REVIEW_DS_ID  = 1dadc999-7c9b-42de-98b4-75594c10a4b5   (Quarterly Reviews data source)
NOTION_AUDIT_DS_ID             = 889093b4-fb7d-4db5-a871-19e7bbe159fd   (Weekly Audits — read for trend context)
TARGET_KEYWORDS_DB_ID          = f5521fe72dec42c1808555fbac2d0d62
COMPETITORS_DB_ID              = c99eaa6d2e7448f0859ce6feba22a3ac
CONTENT_STRATEGY_PAGE_ID       = 333ac0ea4f6581518651d730d706e017
SLACK_CHANNEL                  = #brand
MAX_PRIORITIES                 = 3
TIME_BUDGET_CEILING            = 5.25 hrs/week
OWNED_CHANNEL_FLOOR            = 30%
```

## Load from corpus

Read these in order before running. The corpus carries the strategic frames; this file is the orchestrator.

**Process and priority templates (always)**
- `corpus/growth/playbook/quarterly-channel-review.md` — the 60-min Block 1-6 structure
- `corpus/growth/playbook/quarterly-priorities-template.md` — the 1-3 priority format
- `corpus/growth/playbook/channel-gates-for-adding.md` — deferred-candidate gate evaluation
- `corpus/growth/playbook/cutting-criteria.md` — retirement decision rules
- `corpus/growth/playbook/budget-allocation.md` — the 5.25 hr ceiling

**Strategic frames (always)**
- `corpus/growth/strategy/channel-evaluation-framework.md` — the 5-criteria scoring
- `corpus/growth/strategy/channel-maturity-model.md` — Experiment→Cut lifecycle stages
- `corpus/growth/strategy/owned-vs-rented-channels.md` — the 30% owned-channel floor
- `corpus/growth/strategy/audience-portability.md` — email list as the portable asset
- `corpus/growth/strategy/repurposing-matrix.md` — derivative production economics
- `corpus/growth/strategy/creator-as-product.md` — the dynamics that filter every decision

**Creator dynamics (always)**
- `corpus/growth/creator-dynamics/authentic-voice-as-moat.md`
- `corpus/growth/creator-dynamics/founder-narrative-as-product.md`
- `corpus/growth/creator-dynamics/frequency-vs-quality-tradeoff.md`
- `corpus/growth/creator-dynamics/vulnerability-vs-authority-balance.md`

**Diagnostic patterns (always)**
- `corpus/growth/diagnostics/engagement-drop-diagnostic.md` — interpret in-quarter drops
- `corpus/growth/diagnostics/algorithm-change-response.md` — interpret platform shifts
- `corpus/growth/diagnostics/deplatforming-prep.md` — verify Plan B status

**Metrics (always)**
- `corpus/growth/metrics/channel-roi-calculation.md` — the per-channel ROI formula
- `corpus/growth/metrics/content-decay-analysis.md` — half-lives that inform allocation
- `corpus/growth/metrics/repurpose-vs-create-decision.md` — content-mix decisions
- `corpus/growth/metrics/segment-proxies-rollup.md` — the segment outcome metrics
- `corpus/growth/metrics/anti-vanity-metrics.md` — what to exclude from headline metrics

**Channel-specific evaluations (load on demand per gated channel)**
- `corpus/growth/channels/newsletter-evaluation.md`
- `corpus/growth/channels/youtube-evaluation.md`
- `corpus/growth/channels/own-podcast-evaluation.md`
- `corpus/growth/channels/github-as-distribution.md`
- `corpus/growth/channels/reddit-niche-engagement.md`
- `corpus/growth/channels/hackernews-launch-mechanics.md`

**Anti-patterns (always — defends every decision)**
- `corpus/growth/anti-patterns/no-channel-sprawl.md`
- `corpus/growth/anti-patterns/no-time-budget-overrun.md`

**Database schema**
- `corpus/growth/databases/quarterly-reviews-schema.md` — the output DB structure

## Process

### Step 1 — Bootstrap (10 min)
Per `quarterly-channel-review.md` Block 1, plus skill-specific setup:
1. Verify required MCP connectors are reachable (Notion, Linear, Slack, HubSpot — Ahrefs/GSC optional but preferred).
2. Pull the prior quarterly review page from `NOTION_QUARTERLY_REVIEW_DS_ID` (if it exists) for diff baseline. If first run, baseline is "no prior review."
3. Pull the most recent Weekly Audit page from `NOTION_AUDIT_DS_ID` plus the prior 12 weeks (one quarter). Extract per-week traffic light, P0/P1 counts, and recurring dimension reds.
4. Pull current Target Keywords DB and Competitors DB state (high level — not full audit).
5. Initialize empty data buffer for review output.

### Step 2 — Pull data (10 min)
Per `quarterly-channel-review.md` Block 1 data pull. Concurrent reads where possible:
- LinkedIn analytics: per-post engagement rate trend, follower growth, peer comments (last 13 weeks)
- HubSpot: Segment 1 inbound count, Segment 4 invitations, hire-relevant signals (last 13 weeks)
- Google Analytics (or richezamor.com analytics): traffic, signups, traffic sources (last 13 weeks)
- Notion: published /thinking article count, podcast appearances, speaking engagements (last 13 weeks)
- Calendar audit: estimate hours invested per channel (acceptable range ±15%)

Compute per-channel ROI per `corpus/growth/metrics/channel-roi-calculation.md`. Output: a one-page per-channel summary table.

### Step 3 — Score active channels (10 min)
Per `quarterly-channel-review.md` Block 2. Re-score every active channel via `corpus/growth/strategy/channel-evaluation-framework.md`. Compare to last quarter's scores (from prior review page if it exists).
- ↑↑ ≥2 points: strong; consider increasing investment
- → ±1 point: stable; maintain
- ↓↓ ≥2 points: investigate; possible stage transition or cut

### Step 4 — Stage check + gate check (15 min)
Per `quarterly-channel-review.md` Blocks 3 + 4 combined:
- Active channels: confirm/transition stage per `corpus/growth/strategy/channel-maturity-model.md`. Document any transitions with date and rationale.
- Deferred candidates: gate-check per `corpus/growth/playbook/channel-gates-for-adding.md`. Note progress per gated channel; identify any that are now launchable.
- Cut evaluation: any active channel meeting `corpus/growth/playbook/cutting-criteria.md`'s 3-criteria rule? If yes, mark as cut candidate for Block 5.

### Step 5 — Decisions + priority setting (15 min)
Per `quarterly-channel-review.md` Block 5, extended with explicit priority setting:
- **Active channel decisions:** GROW / MAINTAIN / REDUCE / CUT per channel
- **Candidate decisions:** LAUNCH next quarter (with funded cut per `no-channel-sprawl.md`) or DEFER
- **Time allocation lock:** total ≤5.25 hr/week; per-channel breakdown; ~15 min/week buffer
- **Pick 1-3 priorities for next quarter** using `corpus/growth/playbook/quarterly-priorities-template.md`. Each priority must specify: imperative phrase, why-this-quarter, concrete target, strategic frame served, channels involved, time delta, reversal condition, quarterly review check.
- **Compute Headline traffic light** per the rules in `corpus/growth/databases/quarterly-reviews-schema.md`.

### Step 6 — Assemble review (10 min)
Build the full quarterly review page in memory before any Notion write. Sections per `corpus/growth/databases/quarterly-reviews-schema.md`:
1. Executive summary (1 paragraph)
2. Data pull summary (per-channel ROI table)
3. Active channel scoring (with deltas)
4. Stage transitions
5. Deferred candidate gate progress
6. Decisions
7. Quarterly priorities (1-3 detailed)
8. Time allocation lock
9. Linear tasks (filled in next step)

Do not write to Notion yet.

### Step 7 — Issue Linear seed tasks (10 min)
For each priority (max 3 tasks total): create a Linear issue in `LINEAR_PROJECT_ID`, assigned to `LINEAR_ASSIGNEE_ID`, with the first concrete action that advances the priority. Examples:
- Newsletter-launch priority → Linear task: "Set up Beehiiv account and import holding list" with due date in week 1 of the quarter
- GitHub-experiment priority → Linear task: "Publish first companion repo for the most-recent /thinking article" with due date in week 1
- Cadence-rebuild priority → Linear task: "Re-establish Sunday batch session and pre-write 2 weeks ahead" with due date this Sunday

Use the create-then-update pattern (create with title only, then update with full body) — direct create-with-full-payload is unreliable. Capture the TRZ-### IDs.

### Step 8 — Write Notion page (5 min)
Single create to `NOTION_QUARTERLY_REVIEW_DS_ID`. Page name `Q{N} {YYYY} Review`. Properties per `corpus/growth/databases/quarterly-reviews-schema.md`. Body = the assembly from Step 6 with Linear TRZ-### IDs filled in. Set Headline last, after task issuance is confirmed.

### Step 9 — Slack notification (2 min)
One-line post to `SLACK_CHANNEL` (`#brand`):
```
{traffic-light emoji} Q{N} {YYYY} Review complete — {N} priorities set ({TRZ-### IDs}). {Notion page link}
```
Same brevity discipline as the weekly audit Slack: index card + link, never the full body.

### Step 10 — Update growth-marketing reference (1 min)
The growth-marketing skill should know what the current quarter's priorities are. Append a one-line note to a designated location (option A: a Notion sub-page; option B: a `current-priorities.md` file outside corpus that gets refreshed each quarter; option C: simply the most recent Quarterly Review page). The skill defaults to option C; the priorities are always queryable as the most-recent row in the DB.

## Output summary
Every successful run produces:
- One page in the Quarterly Reviews Notion DB (with Headline traffic light, all properties populated, body sections complete)
- 1-3 priorities written into the page body, structured per the priorities template
- 1-3 Linear seed tasks (TRZ-### IDs) — one per priority — with due dates in the first week of the new quarter
- One `#brand` Slack post (one line + Notion link)

## What this skill does NOT do

- It does not own strategic frames. The strategy lives in `corpus/growth/strategy/` and `corpus/growth/creator-dynamics/`. This skill applies them; it does not redefine them.
- It does not modify channels mid-quarter. Decisions made here are next-quarter; in-quarter changes happen via diagnostics or weekly cadence work.
- It does not substitute for the weekly website audit. The weekly audit covers richezamor.com health; this quarterly review covers the broader portfolio across all channels.
- It does not auto-execute priorities. It seeds the first task for each priority; the work itself happens via cadence + targeted skill invocations across the quarter.
- It does not retro-edit prior review pages. Each review lives in its own dated page; the time series is append-only.
- It does not adjust the 5.25 hr/week budget upward to accommodate more priorities. The budget is the binding constraint; if the priorities don't fit, they get cut to ≤3 that do fit.
- It does not add a "stretch goal" 4th priority. MAX_PRIORITIES is 3 by design; 4+ dilutes focus.

## Cross-skill connections

**Upstream (the review reads from these for canonical knowledge):**
- `rz-growth-marketing` — owns all strategic frames, the priority template, the channel evaluation framework, the channel maturity model, the channel-ROI methodology, the cutting criteria, the gate criteria, and the creator-as-product dynamics.
- `rz-website-audit` — provides per-Sunday richezamor.com data via the Weekly Audits DS. The quarterly review reads the prior 13 weekly audit pages for trend context.

**Downstream (the review hands off to these for execution):**
- `rz-website-audit` — quarterly priority adjustments may require updates to the audit's tracked dimensions or competitor list. The review's decisions inform what the audit watches.
- `rz-content-optimize` — when a priority involves shipping content (e.g., "ship 4 GitHub repos this quarter"), the per-article execution routes through content-optimize.
- `rz-draft-content` — content-shipping priorities feed draft-content for the writing itself.
- `rz-self-improve` — runs at end-of-quarter as the corpus-update trigger; if the review revealed a strategic frame that needs refinement, this skill flags it for self-improve.

## Common Mistakes

| Mistake | What goes wrong | Fix |
|---|---|---|
| Setting 4+ priorities | Priority dilution; nothing meaningful moves | MAX_PRIORITIES = 3 by design; pick the 3 that matter most |
| Setting 0 priorities (just doing the channel review) | Quarterly direction stays vague; the corpus alone is too neutral | Even a maintenance quarter has 1-2 priorities (e.g., "hold cadence through Q1 hiring season") |
| Allocating more than 5.25 hr/week to priorities + baseline | Budget breaks; cadence collapses by week 4 | If the priorities don't fit, cut them down or fund them with explicit retirement of an active channel |
| Picking priorities that aren't measurable | Quarterly review check at end-of-quarter has no way to mark done/extended | Every priority must have a single measurable concrete target |
| Writing this run's priorities INTO the corpus | Corpus is evergreen; priorities are dated | Priorities live in the Notion DB; the corpus has the template only |
| Skipping the prior-quarter review of priorities | The done/extended/dropped call is what makes the cycle work | Block 1 of every review starts with "what happened to last quarter's priorities" |
| Treating Yellow as a problem | Yellow is the most common state; honest assessment | Headline is multi-criteria; mixed quarters get Yellow honestly |
