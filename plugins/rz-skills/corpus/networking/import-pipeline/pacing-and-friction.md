---
name: Pacing and Friction Stops
domain: networking
source_skill: networking
entry_type: rule
length_target: 300-500
related: [corpus/networking/import-pipeline/relevance-scan.md]
---

# Pacing and Friction Stops

## What it is
The hard rules that govern how fast either networking import skill scans LinkedIn profiles and what happens when LinkedIn shows friction signals (CAPTCHA, rate-limit banner, "unusual activity" warning). These are not stylistic preferences; they are the difference between a working pipeline and a flagged or banned LinkedIn account.

Applies to both `rz-networking-hand-curated-import` and `rz-networking-refresh-contacts`.

## Why it matters
LinkedIn rate-limits aggressively against scraping behavior. A run that opens 20 profiles in 2 minutes triggers anti-bot detection regardless of what the script does between opens. The cost of triggering that detection is escalating: rate-limit banner, then "unusual activity" warning, then session lock, then account flag, then permanent restriction. Each step compounds the cost; the last one is unrecoverable without LinkedIn intervention.

Riché's account is the trigger source for both skills. If the account gets flagged, both skills are dead until LinkedIn restores access, and "restore" is not guaranteed.

## How to apply

**Human-pace pacing rules:**

- **One profile every 8 to 15 seconds minimum.** Random jitter inside that range is fine; faster than 8 seconds is forbidden.
- **Never parallelize profile fetches.** One tab at a time. No batch-open of multiple LinkedIn URLs.
- **Wait for DOM to settle before scraping.** Use the Claude-in-Chrome MCP's wait-for-selector or wait-for-network-idle, not a fixed sleep.

**Stop-on-friction rules:**

If LinkedIn shows ANY of:
- CAPTCHA
- "Verify you are a human" interstitial
- Rate-limit banner
- "Unusual activity detected" warning

Then immediately:
1. Stop the run.
2. Post `⚠️ Manual Import stopped at row N: <reason>` to `#brand` in Slack (csv-import skill) or `⚠️ Refresh stopped at contact N: <reason>` (refresh-contacts skill).
3. Save progress with the row index or contact ID.
4. Exit the skill cleanly.

Riché resumes manually with `--resume <run_log_url>` (csv-import) or `--resume <contact_id>` (refresh-contacts).

**Do not push through.** Never click through a CAPTCHA, never refresh past a warning banner, never wait and retry. These are LinkedIn telling you to stop; the correct response is to stop.

**Time of day:** prefer running these skills during normal business hours in Riché's timezone. Off-hours scans (3am ET) read more obviously as automated and trigger detection faster.

## Examples
1. **Routine pacing.** A 30-row CSV processes in approximately 4 to 7 minutes (8-15 seconds per row times 30). One run completes without friction.
2. **CAPTCHA on row 18.** Skill stops, posts to Slack with `row 18: CAPTCHA`. Riché solves the CAPTCHA in his browser, then resumes with `--resume`. The skill picks up at row 19.
3. **Rate-limit at row 24.** Skill stops, posts `row 24: rate-limit banner`. Riché does not resume that day; waits 24 hours minimum before resuming. The cost of pushing through is account flag.

## Related entries
- `corpus/networking/import-pipeline/relevance-scan.md` is the LinkedIn-touching step subject to these rules
- HubSpot writes are not LinkedIn-touching and not subject to these rules

## Anti-patterns
- Parallel profile fetches "to save time." Saves no time; triggers detection faster.
- Fixed sleep instead of DOM-settle wait. Misses dynamic content and produces partial scans.
- Resuming the same day after a rate-limit banner. The banner clears slowly; resuming early reactivates the flag.
- Treating these as stylistic preferences. Every rule here protects the trigger account.
