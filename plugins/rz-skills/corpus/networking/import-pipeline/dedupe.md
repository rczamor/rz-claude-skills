---
name: HubSpot Dedupe
domain: networking
source_skill: networking
entry_type: pattern
length_target: 200-400
related: [corpus/networking/import-pipeline/hubspot-write.md]
---

# HubSpot Dedupe

## What it is
The check that prevents `rz-networking-hand-curated-import` from creating duplicate contacts in HubSpot when the CSV includes a person already in the system. Runs as the first per-row step in the csv-import pipeline.

The refresh skill does NOT use this entry. It reads existing contacts directly; dedupe is implicit in its input shape.

## Why it matters
A duplicate contact in HubSpot is harder to fix than a duplicate prevented at write time. Merging contacts loses signal in Notes, breaks property history, and forces Riché to manually reconcile. Better to detect the match at the CSV-row level and skip cleanly.

## How to apply

**Match logic per CSV row:**

Query HubSpot for a contact matching ANY of:
- Full name (`firstname + lastname`) exact match
- `linkedin_url` substring match in any contact's `linkedin_url` property or `Notes` field

If a match is found:
- Log `dedupe_match` for the row, with the existing contact's `hs_lifecyclestage` value
- Skip the rest of the per-row pipeline (no relevance scan, no company check, no write)
- Include the match in the Slack digest under the `DEDUPE MATCHES (N)` section with a link to the existing contact

**No update on dedupe match.** The csv-import skill never updates an existing contact. If the user wants existing contacts refreshed, that is `rz-networking-refresh-contacts`'s job.

**False-positive risk:** name-only matches on common names (e.g., "John Smith") can collide. The `linkedin_url` substring check is the canonical disambiguator. If the CSV includes the same `linkedin_url` as an existing contact, it is the same person regardless of name spelling differences.

## Examples
1. **Clean match on linkedin_url.** CSV row with `linkedin_url=https://linkedin.com/in/jsmith-pm`. Existing HubSpot contact has the same URL in Notes. Logged as `dedupe_match`, lifecycle stage `Engaged`. Skipped.
2. **Name-only match, different person.** CSV row for "John Smith, Acme AI." HubSpot has a "John Smith" already, but at a different company with a different LinkedIn. Without `linkedin_url` overlap, treat as new contact.
3. **No match.** CSV row's linkedin_url and full name appear nowhere in HubSpot. Proceed to step 2 (relevance scan).

## Related entries
- `corpus/networking/import-pipeline/hubspot-write.md` runs only when dedupe returns no match

## Anti-patterns
- Updating contacts on dedupe match. Out of scope for csv-import; that is the refresh skill's job.
- Matching on email. The CSV input contract does not include email; introducing email-matching adds a dependency on a field that may not be present.
- Skipping the dedupe step "because the CSV is fresh." Bulk uploads happen; deduping protects against accidental re-imports.
