---
name: P4 — Conversion & North Star
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 400-700
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/growth/strategy/audience-portability.md, corpus/growth/segments/segment-4-event-organizers.md]
---

# P4 — Conversion & North Star

## Purpose
Measures whether LinkedIn engagement is converting into Riché's actual goals: substantive inbound (recruiter, advisor, speaker, founder), opportunities that explicitly cite his content (the gold signal), and trajectory toward 30/90/180-day targets. Distinguishes "vanity engagement" (likes from peers) from "load-bearing engagement" (an inbound DM that turns into a real opportunity).

P4 is the only pillar that uses data not in the LinkedIn export — it reads from a manual log Riché maintains, classifying inbound by category.

## Inputs
- Manual inbound log — kept in HubSpot (`HUBSPOT_PORTAL_ID`, contact tag `linkedin-inbound`) OR a Slack thread Riché updates — covering the audited 30-day window
- Inbound categories: recruiter, advisor, speaker, peer, founder, fan, spam (one per inbound)
- Substantive opportunities: an inbound that progressed to a real conversation (not just a "great post" comment)
- Content-cited inbound: an inbound that referenced a specific Riché post or article. **The gold signal.**
- 30/90/180-day targets — from `corpus/growth/segments/segment-4-event-organizers.md` and from career planning context

## Metrics computed

| Metric | Formula | Target |
|---|---|---|
| Inbound count by category | count of log entries grouped by category | trending up |
| Substantive opportunity count | count where status ≠ "drive-by" or "spam" | ≥ 3/month |
| Content-cited inbound count | count where content reference is named | ≥ 1/month |
| Recruiter inbound count | count where category = "recruiter" | ≥ 1/month |
| Speaker/advisor inbound count | count where category ∈ {speaker, advisor} | ≥ 1/quarter |
| Months since last content-cited inbound | gap | < 2 months |

## Severity rules

| Condition | Severity | Headline pattern |
|---|---|---|
| Zero content-cited inbound for 2 consecutive months | **P0** | "Zero content-cited inbound for {N} months. Audience is engaging but not converting." |
| Recruiter inbound = 0 this month | **P1** | "Zero recruiter inbound this month (target ≥1)." |
| Substantive opportunities <2 this month | **P1** | "Only {N} substantive opportunities (target ≥3)." |
| Inbound log not maintained (no entries) | **P1** | "Inbound log empty — likely tracking gap, not actual zero." |
| All targets met | (no finding) | — |

## Headline format for findings

```
{severity}: {headline}

Evidence:
- Substantive opportunities: {N} (target ≥3)
- Content-cited inbound: {N} (target ≥1)
- Recruiter inbound: {N} (target ≥1)
- Speaker/advisor inbound: {N} (target ≥1/quarter)
- Months since last content-cited: {N}
- Inbound by category:
  - recruiter: {N}
  - advisor: {N}
  - speaker: {N}
  - peer: {N}
  - founder: {N}
  - fan: {N}
  - spam: {N}

Action:
{recommended-action}
```

## Action recommendations

- **Zero content-cited inbound (P0):** "Audit the gap. Either content isn't reaching ICP (P2 audience signal), or content isn't 'cite-worthy' (P3 thesis signal). Run both diagnostics before pivoting strategy."
- **Zero recruiter inbound (P1):** "Verify LinkedIn 'open to work' setting is on. Verify profile reflects target role per `corpus/growth/channels/linkedin-profile-optimization.md`. Recruiter sourcing is signal-driven; signals may be weak."
- **Sub-target substantive opps (P1):** "Increase DM cadence from 2/week to 3/week per `corpus/growth/playbook/dm-relationship-building.md`; warmer outreach correlates with better inbound."
- **Empty inbound log (P1):** "Maintain the inbound log going forward. P4 needs the data to function."

## Examples

1. **Healthy month.** 5 substantive opps (1 recruiter, 2 speaker, 2 founder), 2 content-cited (one referenced the Suzy post, one the Active Generation thesis). No finding. Narrative celebrates the cited posts.
2. **Recruiter-light month (P1).** 0 recruiter inbound this month (1 last month). P1 fires: "Zero recruiter inbound." Action: profile + open-to-work check. Often a small tweak fixes the signal.
3. **Content-cited drought (P0).** 0 content-cited inbound for 2 consecutive months. P0 fires. Cross-reference P2 (audience composition healthy?) and P3 (CI engagement healthy?) — drought is usually downstream of one of those.
4. **Empty log.** Riché skipped the log this month. P1 fires noting tracking gap, not "actual zero." Audit narrative defers P4 conclusions until next month.

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — pillar-running protocol
- `corpus/growth/strategy/audience-portability.md` — content-cited inbound is the portable-asset signal
- `corpus/growth/segments/segment-4-event-organizers.md` — speaker/advisor targets
- `corpus/growth/playbook/dm-relationship-building.md` — DM cadence affects inbound

## Anti-patterns

- Inflating "substantive" count by including "great post!" comments. The bar is "could turn into a conversation about a real opportunity."
- Treating fan and peer engagement as content-cited. They aren't; the cite must be specific (named the post or framework).
- Skipping the log. Without it, P4 is blind for that month.
- Reacting to one zero-recruiter month with a profile rewrite. The signal is inherently noisy at low monthly counts; act on 2-month patterns, not 1.
