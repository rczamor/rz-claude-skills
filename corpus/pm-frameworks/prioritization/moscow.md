---
name: MoSCoW Method
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 400
related: [corpus/pm-frameworks/prioritization/rice-scoring.md, corpus/pm-frameworks/prioritization/kano-prioritization.md, corpus/pm-frameworks/lifecycle/mvp-to-mlp.md]
---

# MoSCoW Method

## What it is

A release-planning prioritization technique developed by Dai Clegg at Oracle (1994) for the DSDM agile framework. Categorizes requirements into four buckets:

- **Must have:** non-negotiable for the release. Without these, the release fails its purpose.
- **Should have:** important but not critical. Release can ship without them if forced; they're high-priority for the next iteration.
- **Could have:** desirable, included if time and resources allow. The first to drop under pressure.
- **Won't have (this time):** explicitly out of scope for this release. Documented to prevent scope creep and signal future intent.

The first letters spell MoSCoW (the lowercase 'o's are filler).

## Why it matters

MoSCoW's distinctive contribution is the **Won't have** category. Most prioritization frameworks rank what's in; MoSCoW also ranks what's deliberately out. That visibility prevents the silent scope creep where "low priority" items mysteriously appear in the release because nobody documented their exclusion.

The framework is best for fixed-deadline release planning where scope is the variable (not date or quality). It's less useful for continuous delivery contexts where the "release" boundary is fuzzy.

## How to apply

1. **Define the release goal.** What does this specific release exist to accomplish? Without that, the M/S/C/W boundaries are arbitrary.
2. **Categorize requirements.** Rule of thumb: Musts ≤ 60% of effort, Shoulds + Coulds ≈ 40%, Won'ts explicit and listed.
3. **Pressure-test Musts.** A "Must" is something whose absence kills the release. If you could ship without it, it's a Should.
4. **Document Won'ts publicly.** The list is half the value — it commits the team to descope decisions that would otherwise leak in.
5. **Re-evaluate at milestone gates.** Categories drift as you learn; bake reassessment into the release cadence.

## Examples

1. **Suzy quarterly release.** Must: SOC 2 audit-trail logging (compliance non-negotiable). Should: AI-recommended-study templates (high-value but ship-able later). Could: dashboard theming (nice if time). Won't (this release): mobile app — explicitly deferred to prevent the team's recurring "we should also fix mobile" tangent.
2. **Anti-pattern: everything-is-a-Must.** A team where 90% of requirements were tagged Must. Effectively, no prioritization happened; the release shipped late with quality compromises.

## Related entries

- `corpus/pm-frameworks/prioritization/rice-scoring.md` — higher-precision alternative
- `corpus/pm-frameworks/prioritization/kano-prioritization.md` — Must-be Kano category aligns with MoSCoW Must
- `corpus/pm-frameworks/lifecycle/mvp-to-mlp.md` — MoSCoW for MVP scope decisions

## Anti-patterns

- **Must-bucket inflation.** When 80% of requirements are "Must," nothing is. Forcing ≤60% Musts is the discipline.
- **Skipping Won'ts.** Treating MoSCoW as a three-bucket framework. The Won't list is what makes the method work; without it, MoSCoW is just a worse version of priority labeling.
