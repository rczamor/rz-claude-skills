---
name: Pillar Analysis
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 400-700
related: [corpus/linkedin-audit/pillars/p1-reach-velocity.md, corpus/linkedin-audit/pillars/p2-audience-composition.md, corpus/linkedin-audit/pillars/p3-thesis-resonance.md, corpus/linkedin-audit/pillars/p4-conversion-north-star.md, corpus/linkedin-audit/pillars/p5-competitive-benchmarking.md, corpus/linkedin-audit/pillars/p6-voice-brand-hygiene.md, corpus/linkedin-audit/methodology/task-issuance.md]
---

# Pillar Analysis

## What it is
Step 4 of the audit. Iterates through 6 pillars in fixed order, evaluating each against the parsed export and updated Master Tracker. Each pillar reads its own corpus entry under `corpus/linkedin-audit/pillars/`, computes its dimension-specific metrics, applies its severity rules, and writes findings to the buffer initialized in Bootstrap.

## Why it matters
Pillars are atomic — one pillar can fire P0 without polluting other pillars. The fixed order matters: P1 surfaces export integrity (parse anomalies fire here as P0), P2 establishes audience baseline before P3 looks at content fit, P5 is the longest pillar (network calls to competitors) so P6 runs last so we can early-exit on a fatal P1/P2 if needed.

## The 6 pillars in order

| # | Pillar | What it measures | Compute time |
|---|---|---|---|
| P1 | Reach & Velocity | Cadence, impressions, follower growth | <1 min |
| P2 | Audience Composition | ICP match, demographics drift | <1 min |
| P3 | Thesis Resonance | Engagement by domain, format mix vs target | 1-2 min |
| P4 | Conversion & North Star | Inbound from content, opportunity quality | <1 min (manual log read) |
| P5 | Competitive Benchmarking | Direct + Aspirational tier scan | ~10 min (web fetches) |
| P6 | Voice & Brand Hygiene | Fatal Fifteen lint on 4 random posts + profile audit | 2-3 min |

Total budget: ~20 minutes for the analysis itself, dominated by P5.

## Severity rules (uniform across pillars)

Each pillar entry defines its own P0/P1/P2 thresholds. The general principle:

- **P0:** structural problem; the audit cannot honestly produce its normal output for this dimension. Fires Linear task, fires Red traffic light contribution. Examples: parse anomaly in P1 (export broken); ICP collapse in P2 (audience drifted away from target).
- **P1:** notable problem; warrants attention this month or next. Fires Linear task (within `MAX_MONTHLY_TASKS = 3` cap), fires Yellow traffic light contribution. Examples: cadence below 80% of target; engagement rate trend down 0.5pp.
- **P2:** minor signal; logged for narrative but no task. Examples: 1 voice anti-pattern in 1 post; small demographic drift within tolerance.

## Finding shape

Each finding written to the buffer:
```
{
  pillar: "p3",
  severity: "P1",
  headline: "Context Intelligence engagement rate at 1.2% (target 3%; ranks 3rd of 4 domains)",
  evidence: "Period engagement breakdown: PM 4.1%, Leadership 2.8%, Intersection 2.3%, Context Intelligence 1.2%. The Context Intelligence thesis underperforms the broader feed.",
  action: "Draft a Context Intelligence Deep Dive that opens with a counter-claim (per voice/fatal-fifteen.md hook patterns)."
}
```

## How to apply

For each pillar P1-P6 in order:

1. **Load pillar corpus.** `corpus/linkedin-audit/pillars/{pX}-{name}.md` defines the inputs, metrics, and severity rules.
2. **Compute metrics.** Apply the pillar's specific computations against `parsed_export` and the updated Master Tracker.
3. **Apply severity rules.** Determine P0/P1/P2 per the rules in the pillar entry.
4. **Write finding(s).** Append to `findings_buffer[pillar_id]`. A pillar can produce 0–N findings; common cases produce 0–2.
5. **Continue.** Even if the pillar fires P0, continue to the next pillar — partial-pillar exits corrupt the rollup.

After all 6 pillars run, the buffer holds 0–~10 findings total across pillars. Step 7 (report assembly) consumes this buffer.

## Cross-pillar dependencies

Pillars are mostly independent. Two soft dependencies:

- **P3 depends on P2's demographics** for context: low engagement in a domain becomes more interesting if the audience is heavy on that domain's job titles. P3 may quote P2 in its evidence.
- **P6 may reference P5's competitor finds** when "what to steal" candidates emerge in voice patterns from peer creators.

These are quotation references, not data dependencies. P3 still runs even if P2 fired P0.

## Examples
1. **Standard run.** P1 fires 1 P1 (cadence at 18 posts vs 22 target). P2 clean. P3 fires 1 P1 (Context Intelligence engagement underperforms). P4 fires 1 P2 (recruiter inbound steady, content-cited inbound zero). P5 informational. P6 fires 1 P2 (1 Fatal Fifteen tell in a Tuesday post). Buffer: 4 findings, 2 P1s, 2 P2s. Step 8 will issue 2 Linear tasks.
2. **P0 in P1.** Export parse anomaly detected — TOP POSTS schema changed. P1 fires P0. Steps 5-6 still run on what data is available. Audit page goes Red. Linear task: "Update export-parsing.md to handle new TOP POSTS schema."
3. **Heavy-finding month.** 2 P0s (P1 export issue + P3 thesis collapse). 4 P1s. Step 8 caps tasks at 3 per `MAX_MONTHLY_TASKS`. Picks the 3 worst (2 P0s + 1 highest P1). Other findings narrate but don't seed tasks.

## Related entries
- `corpus/linkedin-audit/pillars/p1-reach-velocity.md` through `pillars/p6-voice-brand-hygiene.md` — the 6 pillar entries themselves
- `corpus/linkedin-audit/methodology/task-issuance.md` — Step 8, consumes the buffer
- `corpus/linkedin-audit/methodology/report-assembly.md` — Step 7, narrates the buffer

## Anti-patterns
- Skipping a pillar because it "shouldn't have anything." Always run; the audit's value is in the consistent check.
- Letting one pillar's P0 halt the audit. Continue; produce the page; surface what the audit could measure.
- Inflating P2s to P1s "because they feel important." Severity is rule-based; importance perception drifts and corrupts the time series of severity counts.
