---
name: P6 — Voice & Brand Hygiene
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 400-700
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/growth/creator-dynamics/authentic-voice-as-moat.md, corpus/growth/channels/linkedin-profile-optimization.md]
---

# P6 — Voice & Brand Hygiene

## Purpose
Catches voice drift before it metastasizes. Voice is the creator brand's moat (per `corpus/growth/creator-dynamics/authentic-voice-as-moat.md`); voice drift compounds silently across many posts, and by the time it's obvious, the audience has noticed and disengaged. P6 runs the Fatal Fifteen lint on a small random sample each month plus a profile-level audit; this is enough to surface drift without becoming a tedious every-post review.

P6 reads from `corpus/voice/` which is owned by `rz-copywriting`. P6 detects drift; rz-copywriting fixes it.

## Inputs
- 4 randomly sampled posts from this month's `top_posts_by_engagements` (sample size = `VOICE_DRIFT_SAMPLE_SIZE`, default 4)
- The Fatal Fifteen list from `corpus/voice/fatal-fifteen.md` (owned by `rz-copywriting`)
- Riché's LinkedIn profile state via `web_fetch`:
  - Headline (the line under the name)
  - About section
  - Featured section (which posts/articles are pinned)
  - Banner image (alt or visible text if present)

## Metrics computed

| Metric | Formula | Threshold |
|---|---|---|
| Fatal Fifteen tells per post | count of voice anti-patterns in each sampled post | ≤ 1 per post |
| Total tells across sample | sum across 4 posts | ≤ 2 |
| Profile sections last updated | for each: Headline, About, Featured | ≤ 90 days each |
| Voice consistency across sample | qualitative — do all 4 sound like Riché? | (binary judgment) |

## Severity rules

| Condition | Severity | Headline pattern |
|---|---|---|
| ≥2 Fatal Fifteen tells in any one sampled post | **P0** | "Voice drift in {URL}: {N} Fatal Fifteen tells. Likely AI-flat draft." |
| 1 tell in any sampled post OR a profile section >90 days stale | **P1** | "Voice tell in {URL}: {tell}." OR "Profile section {Headline/About/Featured} stale ({N} days)." |
| Sample is clean and profile current | **P2** (no finding) | — |
| 1 tell across the whole sample | **P2** (narrative only) | "Sample mostly clean; 1 minor tell in {URL}." |

## Headline format for findings

```
{severity}: {headline}

Voice Drift Sample (4 posts graded):

1. {URL}
   - Fatal Fifteen tells: {N} ({list if any})
   - Verdict: {Clean / Minor drift / AI-flat}

2. {URL}
   - Fatal Fifteen tells: {N}
   - Verdict: {...}

3. {URL}
   - Fatal Fifteen tells: {N}
   - Verdict: {...}

4. {URL}
   - Fatal Fifteen tells: {N}
   - Verdict: {...}

Profile audit:
- Headline: "{current headline}" — last updated {N} days
- About: last updated {N} days, length {N} chars
- Featured: {N} pinned items, oldest {N} days

Action:
{recommended-action}
```

## Action recommendations

- **Voice drift in a post (P0):** "Edit the offending post per `corpus/voice/`. The post is live and accumulating impressions; correction matters. After edit, run a voice-drift retro for the week to identify whether AI-assist drafted without voice constraints."
- **Single tell (P1):** "Surface the post URL to Riché; he edits manually. Track whether the tell is recurring across multiple weeks (escalates to a P0 if so)."
- **Stale profile section (P1):** "Update {section}. Reference the latest career narrative. Don't let stale headers become a signal of inattention."

## Examples

1. **Clean month.** 4 posts sampled, 0 Fatal Fifteen tells, profile sections all updated within 60 days. No finding (or P2 narrative only). Narrative: "Voice sample clean. Profile current."
2. **One tell (P1).** Sample has 0/0/1/0 tells across 4 posts. The 1 tell is "the truth is" hedge in a Wednesday deep-dive. P1 fires: "Voice tell in {URL}: 'the truth is' hedge phrase." Action: edit the post, surface to Riché.
3. **AI-flat post (P0).** Sample has 2/0/0/0 tells; the 2-tell post has both "in today's fast-paced world" and "leverage synergies." P0 fires: "Voice drift in {URL}: 2 Fatal Fifteen tells. Likely AI-flat draft." Action: edit the post, retro the week.
4. **Stale Featured (P1).** Profile audit shows Featured section last updated 4 months ago with a post from before the Helm Labs pivot. P1 fires: "Featured section stale (123 days)." Action: refresh with current top-CI piece.

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — pillar-running protocol
- `corpus/growth/creator-dynamics/authentic-voice-as-moat.md` — why voice = moat
- `corpus/voice/fatal-fifteen.md` (owned by `rz-copywriting`) — the lint list
- `corpus/growth/channels/linkedin-profile-optimization.md` — profile section standards

## Anti-patterns

- Sampling >4 posts per month. The discipline is small-sample-but-honest; large samples turn voice review into a chore.
- Auto-editing posts. P6 detects; it doesn't fix. rz-copywriting fixes when invoked.
- Treating "1 tell per post" as the threshold for P0. The compound rule (≥2 in one post) is what flags an AI-flat draft; isolated single tells are P1.
- Skipping profile audit "because the posts are fine." Profile and posts drift independently; check both.
