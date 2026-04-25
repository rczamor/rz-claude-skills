---
name: Weighted Shortest Job First (WSJF)
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/prioritization/rice-scoring.md, corpus/pm-frameworks/prioritization/ice-scoring.md, corpus/pm-frameworks/lifecycle/dual-track-agile.md]
---

# Weighted Shortest Job First (WSJF)

## What it is

A prioritization formula from the Scaled Agile Framework (SAFe) for ranking features in queue:

**WSJF = Cost of Delay / Job Size**

Where **Cost of Delay** decomposes into three components, summed:

- **User-Business Value:** revenue, retention, or strategic value impact.
- **Time Criticality:** how the value decays if delayed (e.g. competitive window, regulatory deadline, market timing).
- **Risk Reduction or Opportunity Enablement:** does shipping this de-risk future work or unlock new opportunities?

**Job Size** is a relative effort estimate (story points, person-weeks).

The formula prioritizes features with high cost-of-delay relative to their build cost — the queue analog of "expected value per unit of capacity consumed."

From SAFe's *Scaled Agile Framework* literature; rooted in Reinertsen's *Principles of Product Development Flow* (2009).

## Why it matters

WSJF's contribution is making **cost of delay** explicit. Most prioritization frameworks treat all features as roughly time-neutral — a feature shipped in Q1 vs Q3 is treated as equivalent. But many features have time-dependent value: a regulatory feature that misses a deadline is worth zero; a holiday-season retail feature shipped in January is worth a fraction; a competitive-response feature shipped after the window closes is worth nothing.

By forcing teams to estimate time criticality alongside business value, WSJF surfaces the time dimension other frameworks hide. It's especially useful in regulated or seasonally-driven industries.

For AI products, time criticality is high — model capability evolves quarterly, competitive windows are short. WSJF captures that better than Reach × Impact / Effort, which can rank a "high-impact, low-time-pressure" feature ahead of a "moderate-impact but closing-window" feature.

## How to apply

1. **Define the queue.** All features under consideration for the program-increment (typically 8–12 weeks in SAFe).
2. **Score each on the three Cost of Delay components** using a Fibonacci scale (1, 2, 3, 5, 8, 13, 20). Relative scoring beats absolute.
3. **Sum to Cost of Delay.** UBV + TC + RR-OE = CoD.
4. **Score Job Size** on the same Fibonacci scale.
5. **Calculate WSJF = CoD / Job Size** and rank.
6. **Re-rank at every program-increment planning event.** WSJF is dynamic; time criticality changes as deadlines approach.

## Examples

1. **Regulated industry release.** Feature A (SOC 2 audit logging): UBV 5, TC 13 (deadline in 90 days), RR 8. CoD = 26. Size 8. WSJF = 3.25. Feature B (analytics dashboard): UBV 13, TC 2, RR 1. CoD = 16. Size 5. WSJF = 3.2. Tied on WSJF — but the time-criticality of A makes the deadline failure mode catastrophic, so A sequences first.
2. **Cargo-cult WSJF.** A team scoring TC = 1 on every feature (because nothing has a hard deadline). The framework collapses into UBV / Size, equivalent to a worse RICE.

## Related entries

- `corpus/pm-frameworks/prioritization/rice-scoring.md` — adjacent formula without time criticality
- `corpus/pm-frameworks/prioritization/ice-scoring.md` — simpler three-factor variant
- `corpus/pm-frameworks/lifecycle/dual-track-agile.md` — SAFe context

## Anti-patterns

- **Time criticality ignored.** Defaulting TC to a low number on everything because nothing has a literal deadline. Re-frame: what's the cost of delay in months of compounding lost value? That number is rarely zero.
- **Size estimates inflated by stakeholder pressure.** When features stakeholders want are scored as "small" regardless of actual size, the queue becomes politically rigged. Ground sizes in engineering estimates, not stakeholder optimism.
