---
name: LinkedIn Relevance Scan
domain: networking
source_skill: networking
entry_type: pattern
length_target: 300-600
related: [corpus/networking/import-pipeline/company-check.md, corpus/networking/import-pipeline/fit-score.md, corpus/networking/import-pipeline/pacing-and-friction.md]
---

# LinkedIn Relevance Scan

## What it is
The activity scan applied to a LinkedIn profile to determine whether a contact is signal-relevant for Riché's positioning. Used by `rz-networking-hand-curated-import` (during initial CSV processing) and `rz-networking-refresh-contacts` (during periodic re-scoring of existing HubSpot contacts).

## Why it matters
Without a structured scan, "relevance" collapses into vibes. A profile feels relevant or it doesn't, and that judgment doesn't survive a second pass. The scan turns each profile into a list of concrete signals with timestamps, which composes into a fit score and informs the warm opener seed.

## How to apply

**Time window:** scan posts, reposts with commentary, and comments on others' posts from the last 30 to 60 days. Older activity is too stale to anchor a current message; older than 90 days reads as cold even if the topic is right.

**Signal categories (any of these counts):**

- RAG, retrieval, embeddings, vector search, hybrid search
- Agents, agent memory, long-horizon reasoning, tool use
- Context engineering, context systems, personalization
- AI product strategy, AI infrastructure, model commoditization, evals

**Capture format per signal:**
```
(signal_type, post_url, posted_at, first_80_chars)
```

Capture up to 3 signals per profile. Stop scanning once you have 3.

**No signal found:** if zero signals appear in the last 60 days, mark `no_signal = true`. Do NOT skip the contact. The downstream skills handle the no-signal case differently (csv-import drafts a company-based opener; refresh-contacts updates last-checked but does not regenerate the opener).

**Pacing:** observes the rules in `corpus/networking/import-pipeline/pacing-and-friction.md`. One profile every 8 to 15 seconds; never parallelize.

## Examples
1. **Three strong signals.** A VP of Product at an AI company posts twice in 14 days about RAG eval limitations and once about agent memory architecture. Captured: 3 signals, all `signal_type=evals` or `agent_memory`. Fit score lookup proceeds with strong-signal weighting.
2. **One weak signal.** A Head of Product posts once 45 days ago about AI infrastructure procurement. One signal captured, weak. Fit score will be 2 or 3 depending on title and company.
3. **Zero signals, qualifying title and company.** A CPO at a Series B AI company has posted nothing about the signal categories in 60 days. `no_signal = true`. Csv-import skill drafts a company-based opener. Refresh skill marks `last_sequence_action_date` and waits.

## Related entries
- `corpus/networking/import-pipeline/company-check.md` runs after this step
- `corpus/networking/import-pipeline/fit-score.md` consumes the signal count and types
- `corpus/networking/import-pipeline/pacing-and-friction.md` governs scan pacing

## Anti-patterns
- Inventing signals not on the profile. If a post is not in the visible activity, it does not count. Mark `no_signal` and move on.
- Scanning beyond 60 days. Stale signal anchors a stale opener.
- Capturing more than 3 signals. The fit score does not improve past 3, and the opener can only reference one.
