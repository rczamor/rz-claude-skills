---
name: Warm Opener Seed
domain: networking
source_skill: networking
entry_type: template
length_target: 400-700
related: [corpus/networking/import-pipeline/relevance-scan.md, corpus/networking/import-pipeline/hubspot-write.md, corpus/voice/anti-pattern-em-dashes.md]
---

# Warm Opener Seed

## What it is
A one-sentence draft that sits in the contact's HubSpot `warm_opener_seed` property. References the single strongest captured signal. Riché reviews and sends or edits from HubSpot; the skill never auto-DMs.

Used by `rz-networking-hand-curated-import` (drafts unconditionally on create) and `rz-networking-refresh-contacts` (conditional: drafts only if the existing seed is empty; preserves the seed otherwise).

## Why it matters
The seed is the bridge from "captured signal" to "sent message." Without it, every contact in HubSpot is a name and a score with no concrete starting point for outreach. Riché's actual send time per contact compresses from 5 minutes (cold draft) to 30 seconds (review-and-send) because the seed has already done the read-and-anchor work.

The seed is voice-locked. A draft that violates the constraints below is a bug, not a stylistic choice; HubSpot ends up full of openers that read like generic LinkedIn outreach, which kills the open rate Riché has built.

## How to apply

**Constraints (hard, not stylistic):**

- One sentence. Period or comma terminus, not multiple sentences glued together.
- References the single strongest signal from the relevance scan.
- No em dashes. Use commas, colons, or parentheses if separation is needed.
- No filler openers: no "I noticed," "I wanted to reach out," "just curious," "quick question."
- No hedging.
- Specific, not generic. The signal must be quotable from the post or comment, not paraphrased.
- Riché's voice: direct, practitioner-first, contractions allowed.
- Calibrate to his 2025-2026 writing only, not the 2023-2024 articles. Voice has tightened since then.

**No-signal fallback:**
If `no_signal = true` (zero relevance signals in 60 days), draft against the company or title instead. Set `seed_basis = company` in the run log. The constraints still apply; the source is just structural rather than activity-based.

**Conditional regeneration (refresh skill):**
The refresh skill checks `warm_opener_seed` on the existing HubSpot contact:
- If empty or null: draft a fresh seed using the rules above.
- If populated: preserve the existing seed. Update other fields normally.

This rule preserves Riché's edits. If he tightened a draft seed in HubSpot, the refresh skill never overwrites his version.

If a contact's seed needs explicit regeneration (e.g., the original signal is now stale), that is a separate user intent: invoke the refresh skill with `--regenerate-opener` (skill flag) or run the csv-import skill against a one-row CSV.

## Examples
1. **Strong signal, recent.** Profile post 7 days ago says "we shipped a hybrid retrieval setup that reduced hallucinations 40 percent on our eval set." Seed: "Saw your hybrid retrieval drop in eval hallucinations 40 percent, would love to compare notes on how you weighted lexical vs vector."
2. **No-signal, company fallback.** Company raised Series B last month. Title is Head of Product. Seed: "Caught your Series B last month, the context layer thesis behind your product positioning sounds aligned with how I framed it at Suzy."
3. **Refresh, existing seed preserved.** Contact in HubSpot already has `warm_opener_seed = "Your context layer eval framework piece is the cleanest writeup I have seen on the topic."` Refresh skill scans, finds new signals, updates `relevance_score` and `last_sequence_action_date`, leaves the seed untouched.

## Related entries
- `corpus/networking/import-pipeline/relevance-scan.md` provides the signal that anchors the seed
- `corpus/networking/import-pipeline/hubspot-write.md` writes the seed to the contact property
- `corpus/voice/anti-pattern-em-dashes.md` and the broader `corpus/voice/` rules apply to every seed
- `corpus/voice/fatal-fifteen-12-thrilled-excited-honored.md` for announcement-style openers to avoid

## Anti-patterns
- "I noticed your post about..." Reads as templated outreach, signals "I want something."
- Two sentences. The seed is one sentence; the second sentence is what Riché writes when he sends.
- Paraphrasing the signal. Quote the post specifically; paraphrasing strips the anchor that made the seed worth opening.
- Auto-overwriting an existing seed in refresh mode. Riché's edits are higher signal than the skill's regeneration.
