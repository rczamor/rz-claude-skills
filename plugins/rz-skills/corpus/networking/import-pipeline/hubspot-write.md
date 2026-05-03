---
name: HubSpot Contact Write Pattern
domain: networking
source_skill: networking
entry_type: pattern
length_target: 500-800
related: [corpus/networking/import-pipeline/fit-score.md, corpus/networking/import-pipeline/warm-opener-seed.md, corpus/networking/import-pipeline/dedupe.md]
---

# HubSpot Contact Write Pattern

## What it is
The canonical pattern for creating or updating a contact in HubSpot from a networking pipeline run. Used by `rz-networking-hand-curated-import` (create) and `rz-networking-refresh-contacts` (update).

Both skills write to the **contact** record only. Networking does not use the HubSpot deals object. The contact IS the unit of relationship; deals are for revenue opportunities, which networking is not.

HubSpot portal: `245808914`.

## Why it matters
Earlier versions of this pipeline created a deal per contact in a `Network Building` pipeline, mapping deal stage to relationship state. That doubled every record (contact plus deal), forced relationship cadence into a deal-progression model that does not fit, and created two competing answers to "where is this person?". The contact-only pattern collapses that to one record with one canonical answer: the HubSpot **Lifecycle Stage** field.

Lifecycle Stage progression is a Riché judgment call after first reply, not skill automation. Skills only ever set `Lead` (entry stage). Everything beyond `Lead` requires human signal.

## How to apply

**Lifecycle Stage values (Riché's custom set):**

| Stage | Meaning | Set by |
|---|---|---|
| Subscriber | Low-touch, on the radar | Manual or external import only |
| Lead | Qualified, signals captured, opener drafted | Both skills set this on create or refresh |
| Engaged | Riché reached out (sent the opener) | Manual after send |
| Active | Ongoing dialogue, both sides exchanging | Manual after second substantive exchange |
| Opportunity | Identified opportunity for value exchange | Manual when scope clarifies |
| Customer | They may purchase something | Manual at commercial intent |
| Evangelist | They promote Riché's content | Manual when amplification behavior shows |
| Dormant | Lapsed in communication or engagement | Manual or auto-set after 90 days no contact |

**Skills only ever set `Lead`.** Both create and refresh paths land on `Lead`. Stage progression beyond `Lead` is manual, period.

**Contact properties to set on create (csv-import skill):**

```
hs_lifecyclestage = lead
firstname, lastname        (parsed from CSV name field)
jobtitle                   (from CSV title)
company                    (from CSV company)
linkedin_url               (custom property; from CSV)
trigger_source             (custom enum; set to "Sales Navigator")
warm_opener_seed           (custom rich_text; from corpus/.../warm-opener-seed.md)
last_sequence_action_date  (custom date; today)
relevance_score            (custom enum; 1-5 or "override_approved")
```

Append to the `Notes` property on the contact (not the deal):
- Signals found, with `(post_url, posted_at, first_80_chars)` for each
- Company context: headcount, funding stage, recent news headline
- Riché's `notes` field from the CSV if provided

**Contact properties to set on update (refresh-contacts skill):**

```
warm_opener_seed           (CONDITIONAL: only if currently empty; preserve otherwise)
last_sequence_action_date  (today)
relevance_score            (refresh; flag if changed by 2+ in Slack digest)
```

Append to `Notes`:
- New signals found this run (do not overwrite prior signals)
- Updated company context if changed materially (funding round, headcount bucket shift)

Do NOT overwrite `firstname`, `lastname`, `jobtitle`, `company`, `linkedin_url` on refresh unless the LinkedIn profile reveals a change. Title or company changes are flagged in the Slack digest as `job_change` and applied if the change is unambiguous.

**Lifecycle Stage on refresh:** never auto-progress past `Lead`. If the contact is already `Engaged` or `Active`, the refresh skill leaves Lifecycle Stage alone. The refresh updates content (signals, score, opener if missing), not stage.

**Required HubSpot setup (one-time):** the custom properties `linkedin_url`, `trigger_source`, `warm_opener_seed`, `last_sequence_action_date`, `relevance_score` must exist on the Contact object. Verify via the HubSpot MCP before first run; create if missing.

**Record URL format:** `https://app.hubspot.com/contacts/245808914/record/0-1/<contact_id>`. Used in the Slack digest output.

## Examples
1. **Create from CSV.** New contact: `firstname=Alex, lastname=Chen, jobtitle=Head of Product, company=Acme AI, hs_lifecyclestage=lead, trigger_source=Sales Navigator, warm_opener_seed=<draft>, relevance_score=4`. Notes contain 2 signals plus company context. No deal created.
2. **Refresh, opener empty.** Existing contact has `warm_opener_seed = ""`. Refresh skill drafts a new seed using the latest signals, sets it, updates `last_sequence_action_date` and `relevance_score`. Lifecycle Stage stays at `Engaged` (Riché had already moved them).
3. **Refresh, opener populated.** Existing contact has `warm_opener_seed = "Your essay on context architecture..."`. Refresh skill updates `last_sequence_action_date` and `relevance_score`. Seed untouched. New signals appended to Notes.

## Related entries
- `corpus/networking/import-pipeline/dedupe.md` runs before this on csv-import (skip if exists)
- `corpus/networking/import-pipeline/fit-score.md` provides the score this writes
- `corpus/networking/import-pipeline/warm-opener-seed.md` provides the opener content (and the conditional rule)

## Anti-patterns
- Creating deals. The deals object is for revenue opportunities; networking is not revenue. Use Lifecycle Stage on the contact.
- Auto-progressing Lifecycle Stage past `Lead`. Skills cannot tell when Riché has actually engaged a contact. Setting `Engaged` automatically generates false signal in HubSpot reports.
- Overwriting `warm_opener_seed` on refresh. Riché's manual edits are higher signal than the skill's regeneration.
- Mass-updating fields without diffing. Refresh writes only fields that changed; otherwise Notes blow up with redundant entries.
