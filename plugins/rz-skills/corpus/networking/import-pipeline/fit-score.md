---
name: Networking Fit Score
domain: networking
source_skill: networking
entry_type: rule
length_target: 300-600
related: [corpus/networking/import-pipeline/relevance-scan.md, corpus/networking/import-pipeline/company-check.md, corpus/networking/import-pipeline/hubspot-write.md]
---

# Networking Fit Score

## What it is
A 1-to-5 rubric that combines profile signal strength, title fit, and company stage fit into a single score. Used by both networking import skills to decide whether a contact gets auto-created/updated (3+) or sent to the review queue (1-2).

## Why it matters
Without a rubric, every contact looks plausible at the moment of triage and the review queue fills with judgment-call decisions Riché does not have time to make. The 1-5 score forces a defensible call before HubSpot ever sees the contact.

The score also calibrates Riché's response when reviewing the queue. Score 4 contacts deserve fast manual review; score 1 contacts deserve a quick pass-or-skip without deliberation.

## How to apply

**Score definitions:**

- **5**: Strong signal match (3 captured signals, recent, in primary categories) AND title in {VP, CPO, CTO, Founder, Head of Product, Head of AI, Principal PM} AND company is Series A through Series C AI company
- **4**: Moderate signal match (2 signals, recent) AND qualifying title AND qualifying company
- **3**: Either strong signal OR qualifying title plus company, but not both
- **2**: Weak signal (1 stale signal) AND weak title or company fit
- **1**: No signal AND marginal title or company fit

**Routing rule:**
- Auto-create or auto-update for scores 3+
- Scores 1 and 2 go to the review queue (Slack digest with `Flagged: <reason>`)
- Riché replies `approve N` in-thread to force-add a flagged contact

**Refresh skill specifics:** when a contact already in HubSpot is rescored and the new score differs from the existing `relevance_score` by 2 or more, flag the change in the Slack digest. A contact that scored 5 six months ago and now scores 2 is signal worth surfacing.

## Examples
1. **Score 5.** VP of Product at a 51-200 person Series B AI company. Three signals captured in the last 21 days (RAG eval, agent memory, context engineering). Auto-create.
2. **Score 3 split.** Head of Product at a 5000+ person enterprise SaaS company. Three strong signals captured in the last 30 days. Strong signal but weaker company fit. Auto-create.
3. **Score 2 to queue.** Senior PM (not Head of) at a 11-50 person AI startup. One signal from 50 days ago about general AI product strategy. Flagged to review queue with reason `weak signal + non-qualifying title`.
4. **Refresh score drop.** A contact scored 5 six months ago is now at 2 because they changed jobs to a non-AI company and stopped posting on signal topics. Refresh skill flags `score_drop_2plus` in the Slack digest.

## Related entries
- `corpus/networking/import-pipeline/relevance-scan.md` provides signal count and types
- `corpus/networking/import-pipeline/company-check.md` provides headcount and funding stage
- `corpus/networking/import-pipeline/hubspot-write.md` consumes the score for the create/update decision

## Anti-patterns
- Scoring 4 or 5 for "potential" rather than current state. The rubric is descriptive, not aspirational.
- Auto-creating score 1 or 2 contacts without review queue. The queue exists because the data is ambiguous; bypassing it pollutes HubSpot.
- Adjusting the rubric mid-batch to hit a target add count. The score is a leading indicator; if the batch produces too few 3+ scores, the CSV needs better curation, not a softer rubric.
