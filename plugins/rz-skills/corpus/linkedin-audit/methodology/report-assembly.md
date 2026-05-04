---
name: Report Assembly
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: template
length_target: 500-900
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/linkedin-audit/methodology/task-issuance.md, corpus/linkedin-audit/methodology/slack-notification.md, corpus/linkedin-audit/databases/monthly-audits-notion-schema.md]
---

# Report Assembly

## What it is
Step 7 of the audit. Composes the full Notion audit page in memory before any Notion write. Sets the `Overall Status` (traffic-light) per the rule below. Reads the findings buffer, the Master Tracker views, the Deep Dive candidate list, and the newsletter gate state, and assembles them into a structured page body.

The assembly is read-only — no Notion writes, no Linear writes, no Slack writes happen here. Step 8 issues tasks; Step 9 writes Notion; Step 10 posts Slack.

## Why it matters
Every audit page is a snapshot. The structure is fixed so that month-over-month comparison is possible by reading the same section across months. Drift in section order or naming destroys that comparability.

Assembly happens in memory first because Notion writes are atomic-per-page-create — partial assembly + partial write produces a malformed page that's hard to repair. By assembling fully first, we either succeed cleanly or fail before touching Notion.

## Page sections in fixed order

```
# LinkedIn Audit — {Month YYYY}

## Headline
{traffic-light emoji} {one-line verdict}

## Period Summary
- Period: {Period Start} – {Period End}
- Posts published: {N} (target 22 = 5x/week × 4.4 weeks)
- Total impressions: {N}
- Engagement rate: {N.NN%}
- Avg impressions/post: {N}
- Net follower growth: +{N}
- Total followers (EOP): {N}
- ICP match (Senior+): {N.N%}

## Pillar Findings

### P1 — Reach & Velocity {status emoji}
{findings_buffer.p1 narrated}

### P2 — Audience Composition {status emoji}
{findings_buffer.p2 narrated}

### P3 — Thesis Resonance {status emoji}
{findings_buffer.p3 narrated}

### P4 — Conversion & North Star {status emoji}
{findings_buffer.p4 narrated}

### P5 — Competitive Benchmarking
{findings_buffer.p5 narrated; informational; no status emoji}

### P6 — Voice & Brand Hygiene {status emoji}
{findings_buffer.p6 narrated}

## Master Tracker Highlights

### Top 5 Compounders
{from Compounders view; see views/compounders.md for narrative shape}

### Late Bloomers
{from Late Bloomers view; see views/late-bloomers.md for narrative shape}

### Format Decay Observation
{1-paragraph synthesis from format-decay-curves.md}

## Deep Dive Candidates
{5 URLs with selecting metric and 1-line context per deep-dive-candidate-selection.md}

## Newsletter Gate Check
- Gate 1 (Impressions ≥5,000 sustained 8 weeks): {Met / Approaching / Not Met} — current {N} avg, sustained {N} weeks
- Gate 2 (Engagement ≥3% sustained 8 weeks): {status} — current {N%}, sustained {N} weeks
- Gate 3 (ICP Quality manually confirmed): {status}
- Gate 4 (Waitlist ≥200 signups): {status} — current {N}
- Trajectory: {if any gate is approaching, 1-line trend statement}

## Voice Drift Sample
{4 random posts from this month's TOP POSTS, graded against fatal-fifteen.md per p6-voice-brand-hygiene.md}

## Linear Tasks Issued
- {TRZ-###}: {title}
- {TRZ-###}: {title}
- {TRZ-###}: {title}
(0–3 entries; populated by Step 8 before this section is finalized in Step 9)
```

## Headline computation

```
status = "🔴 Red"     if any P0 finding fires OR ≥2 newsletter gates regressed vs prior month
       = "🟡 Yellow"  if 1–2 P1 findings OR a single newsletter gate regressed
       = "🟢 Green"   if all pillars at P2 or better AND no gate regressed
```

The 1-line verdict accompanying the emoji synthesizes the dominant signal:
- Green: "Cadence held, engagement rate at {N%}, on track for newsletter gate 2."
- Yellow: "Engagement at {N%} — Context Intelligence underperforming target. {N} task(s) issued."
- Red: "{primary P0 description}. {N} tasks issued including {top task title}."

Avoid hedge phrases ("things are looking…"). State the verdict.

## Notion property population

Set the following from the assembled body:
- `Title`: `LinkedIn Audit — {Month YYYY}`
- `Audit Date`: today's date
- `Period Start`, `Period End`: from parsed export
- `Overall Status`: per headline computation above
- All numeric properties from Period Summary
- `Top Format`, `Top Domain`: from Master Tracker `Monthly Summary` row's Top Format / Top Domain
- `Domain Mix Drift`: derived from comparing actual mix vs `DOMAIN_BALANCE_TARGET`
- 4 `Newsletter Gate *` checkboxes per the Gate Check section
- `Linear Tasks Issued`: comma-separated TRZ-### IDs (filled in Step 9 after Step 8)
- `Deep Dive Candidates`: comma-separated URLs from Step 5

## Anti-patterns

- Writing to Notion before assembly is complete. Atomic-per-page-create means a partial write is a half-formed audit. Always assemble in memory, then write once.
- Re-ordering sections "for variety." The order is the discipline; comparability requires it.
- Letting the Headline contradict the body. The 1-line verdict must reflect the worst signal in the body.
- Embedding raw data tables in the Notion page instead of referencing the Master Tracker. The Tracker is the source of truth for time-series data; the audit page references it via link, doesn't duplicate.

## Examples
1. **Green month.** All 6 pillars P2 or better; no gate regression; engagement rate at 2.1% (up 0.3pp). Headline: "🟢 Cadence held at 23 posts; engagement rate at 2.1%, trending toward gate 2." Body cleanly populated; 0 Linear tasks.
2. **Yellow month.** P3 fires P1 (CI engagement at 1.2%); P6 fires P1 (2 Fatal Fifteen tells across 4-post sample). Headline: "🟡 Engagement at 1.4% — Context Intelligence underperforming. 2 tasks issued." 2 Linear tasks; gates unchanged.
3. **Red month.** P1 fires P0 (export schema changed; partial parse). Headline: "🔴 Export parse failed mid-DEMOGRAPHICS — re-export required. P1 task issued; remaining pillars degraded." 1 Linear task; gates show "data unavailable."

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — Step 4; produces the buffer this step narrates
- `corpus/linkedin-audit/methodology/task-issuance.md` — Step 8; runs after assembly to fill Linear Tasks Issued
- `corpus/linkedin-audit/methodology/slack-notification.md` — Step 10; uses the headline from this step
- `corpus/linkedin-audit/databases/monthly-audits-notion-schema.md` — defines the properties this step populates
