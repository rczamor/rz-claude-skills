---
name: P2 — Audience Composition
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 400-700
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/linkedin-audit/methodology/export-parsing.md, corpus/growth/segments/segment-1-hiring-managers.md, corpus/growth/segments/segment-2-product-leader-peers.md]
---

# P2 — Audience Composition

## Purpose
Measures whether the LinkedIn audience matches Riché's ICP (Ideal Customer Profile) — VP/CPO/founder-level operators at Series A-C AI companies. Drift in audience composition is silent; without explicit measurement, the brand can be popular among the wrong audience for years. P2 catches that drift early.

## Inputs
- `parsed_export.demographics.seniority` — ranked Seniority distribution (Senior / Director / CXO / Owner / Entry / etc.)
- `parsed_export.demographics.job_titles` — ranked Job Titles
- `parsed_export.demographics.industries` — ranked Industries
- `parsed_export.demographics.locations` — ranked Locations
- `parsed_export.demographics.company_size` — ranked Company Size
- `parsed_export.demographics.companies` — ranked Companies (top names by audience density)
- Last month's Monthly Summary `ICP Match % (Senior+)` for MoM drift

## Metrics computed

| Metric | Formula | Target |
|---|---|---|
| ICP Match % | sum of pcts for Senior + Director + CXO + Owner | ≥ 50% |
| ICP Seniority MoM drift | this month − last month | within ±5pp |
| Tech industry concentration | sum of pcts for "IT Services" + "Software Development" + "Technology, Information and Internet" | ≥ 35% |
| Top 5 job titles | first 5 rows of job_titles | (qualitative — should skew product/founder/PM) |
| Top 5 companies | first 5 rows of companies | (qualitative — should match target-account list when possible) |

The `ICP_SENIORITY_FILTER` constant defines what counts as "Senior+": Senior + Director + CXO + Owner. Configurable in SKILL.md.

## Severity rules

| Condition | Severity | Headline pattern |
|---|---|---|
| Demographics section missing or truncated | **P0** | "Demographics section missing from export. P2 cannot run; re-export required." |
| ICP Match % < 50% | **P0** | "ICP Match collapsed to {N}%. Audience drifted from target." |
| ICP Match % dropped 5+ points MoM | **P1** | "ICP Match down {N}pp MoM (now {N}%, was {N}%)." |
| Top job title not in product/founder/PM cluster | **P1** | "Top job title is {X} ({pct}%) — outside ICP. Audience drifting." |
| Tech industry concentration < 35% | **P1** | "Tech industry concentration at {N}% (target ≥35%)." |
| Demographics shifting but within tolerances | **P2** | "Demographics drifting: {observation}. Within tolerance." |
| Stable composition | (no finding) | — |

## Headline format for findings

```
{severity}: {headline}

Evidence:
- ICP Match (Senior+): {N}% (MoM {Δpp}pp)
- Top 3 seniority: {1: pct}, {2: pct}, {3: pct}
- Top 3 job titles: {1: pct}, {2: pct}, {3: pct}
- Top 3 industries: {1: pct}, {2: pct}, {3: pct}
- Tech industry concentration: {N}%
- Top 5 companies: {names}

Action:
{recommended-action}
```

## Action recommendations

- **ICP collapse (P0):** "Run the audience-composition diagnostic (off-skill); identify the source of audience drift. Likely candidates: a viral post pulled in non-ICP followers, or content topic drifted away from ICP interests."
- **ICP drift (P1):** "Tighten content to ICP-fit topics for the next 4 weeks (per `corpus/growth/segments/segment-2-channels.md`). Re-evaluate next audit."
- **Top job title outside ICP (P1):** "Specific topic drift — recent posts may have attracted {audience}. Check P3 thesis resonance for which content category was off-target."
- **Demographics truncated (P0):** "Re-export the LinkedIn analytics file ensuring full demographics section. Current file truncated at {section}."

## Examples

1. **On-target month.** ICP Match 71% (Senior 30 + Director 15 + CXO 11 + Owner 8 + Entry 14 = excluding Entry → 64% by ICP filter; with Owner included = 64%). Top job title: Founder 8%. Top industry: IT Services 23%. Tech concentration: 48%. No finding fired. Pillar narrates baseline.
2. **ICP drift (P1).** ICP Match drops from 67% to 59% (8pp drop). Top job title shifts to "Marketing Manager" (12%). Tech concentration drops to 31%. P1 fires: "ICP Match down 8pp MoM." Action: tighten content topics for 4 weeks.
3. **Demographics truncated (P0).** Export missing Companies subsection. P0 fires; P2 cannot complete. Audit page goes Yellow at minimum from P2 alone.

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — pillar-running protocol
- `corpus/linkedin-audit/methodology/export-parsing.md` — sources `demographics`
- `corpus/growth/segments/segment-1-hiring-managers.md` — Segment 1 ICP definition
- `corpus/growth/segments/segment-2-product-leader-peers.md` — Segment 2 ICP definition
- `corpus/growth/segments/segment-3-founders.md` — Segment 3 (founder) ICP definition

## Anti-patterns

- Treating demographics as a vanity dimension. Audience composition determines whether engagement = ICP signal vs noise.
- Reacting to one bad month with a strategy pivot. Demographics shift slowly; multi-month drift is the trigger for action.
- Hard-coding ICP titles. The `ICP_SENIORITY_FILTER` constant is overridable; if Riché tightens to "Director+" only, the rule shifts but the methodology stays.
- Counting follower growth in a P2 "Yellow" by default. Audience composition is qualitative; raw growth is P1's domain.
