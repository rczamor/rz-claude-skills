---
name: rz-networking-hand-curated-import
description: >
  Process a manually-curated Sales Navigator lead CSV through relevance scanning, warm opener drafting, HubSpot dedupe, and contact and deal creation in the Network Building pipeline. Use when Riché provides a CSV of hand-picked leads and wants them enriched and loaded into HubSpot. Trigger when Riché says import this CSV, run hand-curated import, process Sales Nav leads, or load these leads into HubSpot. Stages contacts at the Qualified entry stage with a warm opener seed; never auto-sends DMs.
---

# Networking Hand-Curated Import

Companion to the 6 automated networking prompts. Same HubSpot conventions, different entry point: Riché has already applied judgment in Sales Nav. This skill does the enrichment, the dedupe, and the data entry.

HubSpot portal: `245808914`. Pipeline: `Network Building`. Entry stage: `Qualified`.

## Input contract

A CSV with exact header names:

- `name` (required)
- `title` (required)
- `company` (required)
- `linkedin_url` (required)
- `notes` (optional, Riché's reason for including them)

Skill accepts the path as the first positional argument. Optional `--resume <notion_log_url>` flag skips rows already logged.

## Output contract

1. HubSpot contacts + deals on Network Building at `Qualified` for confident matches
2. Slack digest to #brand (`C0APLNNAGJY`) with per-row status
3. Child page under Notion `Networking Reports` (`34aac0ea-4f65-815e-8e1d-f70598cd7afc`) titled `Manual Import — [Mon date]` with the full run log

## Steps (per row)

### 1. Dedupe
Query HubSpot for a contact matching on full name OR `linkedin_url` in notes. On match: log `dedupe_match` with the existing deal's current stage and skip.

### 2. Open the profile
Use the Claude-in-Chrome MCP to open `linkedin_url`. Wait for DOM to settle before scraping.

### 3. Relevance scan
Scan the last 30 to 60 days of activity (posts, reposts with commentary, comments on others' posts). Signal categories:

- RAG, retrieval, embeddings, vector search, hybrid search
- Agents, agent memory, long-horizon reasoning, tool use
- Context engineering, context systems, personalization
- AI product strategy, AI infrastructure, model commoditization, evals

Capture up to 3 signals as `(signal_type, post_url, posted_at, first_80_chars)`. If zero signals in 60 days, mark `no_signal`. Do not skip, flag in output.

### 4. Company check
Open the company LinkedIn page. Capture: headcount bucket, most recent funding round (stage + date if visible), any pinned news from the last 90 days.

### 5. Fit score (1 to 5)

- **5**: Strong signal match + title in {VP, CPO, CTO, Founder, Head of Product, Head of AI, Principal PM} + Series A–C AI company
- **4**: Moderate signal match + qualifying title + qualifying company
- **3**: Either strong signal OR qualifying title+company, not both
- **2**: Weak signal and weak title/company fit
- **1**: No signal and marginal fit

Auto-create for scores 3+. Scores 1 and 2 go to the review queue for manual approval.

### 6. Warm opener seed
One sentence. References the single strongest signal from step 3. Constraints:

- No em dashes. Use colons or commas.
- No "I noticed", "I wanted to reach out", "just curious", "quick question"
- No hedging
- Specific, not generic
- Riché's voice: direct, practitioner-first, contractions allowed
- Calibrate to his 2025–2026 writing only, not the 2023–2024 articles

If `no_signal`: draft against the company or title instead, and set `seed_basis = company` in the log.

### 7. Create in HubSpot (scores 3+)

1. Create contact with name, title, company, and `linkedin_url` in the Notes field
2. Set custom properties:
   - `trigger_source = Sales Navigator`
   - `warm_opener_seed = <your draft>`
   - `last_sequence_action_date = today`
   - `relevance_score = <1–5>`
3. Append to contact Notes: signals found (URL + date each), company context, Riché's `notes` field from CSV if provided
4. Create deal on `Network Building` at `Qualified`, associated with the new contact
5. Record the HubSpot contact URL: `https://app.hubspot.com/contacts/245808914/record/0-1/<contact_id>`

### 8. Log
Append the row to the Notion run log page with all captured fields.

## Slack output (post after full CSV processed)

```
📥 Manual Import — [date]
CSV: [filename] | Rows: N | Added: N | Skipped: N | Review: N

ADDED TO HUBSPOT (N):
1. [Name] — [Title] at [Company] | Score: X/5
   Seed: [first 100 chars]
   🔗 HubSpot | 🔗 LinkedIn

DEDUPE MATCHES (N):
- [Name] — already in HubSpot at stage [stage] | 🔗 HubSpot

REVIEW QUEUE — score 1 or 2 (N):
- [Name] — [Title] at [Company] | Flagged: [reason]
  Reply `approve N` to force-add to Stage 1 as Sales Nav Manual

NO SIGNAL (N, added with company-based seed):
- [Name] — [Title] at [Company]

🔗 Run log: [Notion link]
```

## On `approve N` reply in-thread
Force-add the flagged row to HubSpot at `Qualified` using the same create pattern as step 7, with `relevance_score = override_approved` and `trigger_source = Sales Navigator`.

## Constraints

- **Human-pace pacing.** One profile every 8 to 15 seconds minimum. Never parallelize profile fetches. Never batch-open tabs.
- **Stop on friction.** CAPTCHA, rate-limit banner, or "unusual activity" warning: stop immediately, post `⚠️ Manual Import stopped at row N: [reason]` to #brand, save progress with the row index, and exit. Riché resumes with `--resume`.
- **Do not invent signals.** If a post isn't on the profile, it isn't there. Mark `no_signal` and move on.
- **Voice guardrails on the seed are hard constraints.** Any draft that violates them is a bug, not a stylistic choice.
- **No auto-DM.** This skill does not send messages. It only stages them in `warm_opener_seed`. Riché sends or edits from HubSpot.

## Required HubSpot property additions (one-time setup)

Verify on the Contact object before first run. If missing, create via the HubSpot MCP:

- `trigger_source` enum: add option `Sales Navigator` if not present
- `relevance_score` enum: values `1`, `2`, `3`, `4`, `5`, `override_approved`

## Related

- Networking Scheduled Task Prompts (Notion page `34aac0ea-4f65-811c-b137-cde78dd064aa`): the 6 automated flows this skill complements
- Networking Reports (Notion page `34aac0ea-4f65-815e-8e1d-f70598cd7afc`): where run logs go
- Networking Approach — Principles & Decisions (Notion page `348ac0ea-4f65-8113-85d6-dee4fa4d7063`): governing doc
