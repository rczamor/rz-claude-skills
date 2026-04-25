# Corpus Inventory — Master Worklist

**Status:** Phase 0 complete. All 10 domain slices filled. **STOP gate before authoring** — user reviews this file and the per-domain slices before Phase 1 dispatches authoring agents.

## Summary

| # | Domain                   | Entries | Inventory slice |
|---|--------------------------|---------|-----------------|
| 1 | voice                    | 60      | [INVENTORY/voice.md](INVENTORY/voice.md) |
| 2 | content-system           | 31      | [INVENTORY/content-system.md](INVENTORY/content-system.md) |
| 3 | pm-frameworks            | 110     | [INVENTORY/pm-frameworks.md](INVENTORY/pm-frameworks.md) |
| 4 | growth                   | 70      | [INVENTORY/growth.md](INVENTORY/growth.md) |
| 5 | networking               | 30      | [INVENTORY/networking.md](INVENTORY/networking.md) |
| 6 | office-hours             | 30      | [INVENTORY/office-hours.md](INVENTORY/office-hours.md) |
| 7 | brand-system             | 30      | [INVENTORY/brand-system.md](INVENTORY/brand-system.md) |
| 8 | ux-principles            | 100     | [INVENTORY/ux-principles.md](INVENTORY/ux-principles.md) |
| 9 | ai-product-ux            | 30      | [INVENTORY/ai-product-ux.md](INVENTORY/ai-product-ux.md) |
| 10| evaluation-frameworks    | 40      | [INVENTORY/evaluation-frameworks.md](INVENTORY/evaluation-frameworks.md) |
|   | **Total**                | **531** | |

The total exceeds the 450 estimate from the previous session because the granular per-audit-item approach in `ux-principles` (one entry per atomic rule) and the deeper PM/Growth coverage are richer than the original ballpark. If 531 is too many, the natural levers to reduce:

1. **Collapse audit items into category-level entries.** ux-principles drops from 100 → ~25 (one entry per audit category instead of per item). Total → ~456.
2. **Drop the AI-PM bridge from pm-frameworks.** pm-frameworks drops from 110 → 100. Total → ~521.
3. **Combine related thinkers.** thinkers/ collapses by 5–10 entries. Total → ~520.
4. **Merge growth `target-accounts` markdowns into the YAML files.** growth drops from 70 → ~66. Total → ~525.

## Per-domain summary

### 1. voice (60 entries)
Core attributes (5), Fatal Fifteen (15), anti-patterns (7), sentence/paragraph patterns (4), three-domain balance (4), terminology (2 + YAML), proof points (8), the Hook (5), process (2), voice principles synthesized (7).

### 2. content-system (31 entries)
5 content types (5), six-step story arc (6), hook library rotation (5), content pillars/formats (8), production workflow (4), cross-format patterns (3).

### 3. pm-frameworks (110 entries)
Discovery (10), prioritization (11), strategy (14), lifecycle (11), metrics (15), monetization (14), thinkers (25), AI-product-PM bridge (10), index file (1).

### 4. growth (70 entries)
4 segments × 4 entries each (16), engagement flywheel (6), weekly playbook 5.25 hrs/week (8), channel-specific tactics (12), target accounts (4 markdown + 2 YAML), speaking & podcasts (8), growth metrics & loops (10), what-NOT-to-do guardrails (8), hooks/differentiation (4).

### 5. networking (30 entries)
Networking philosophy (3), relationship tiers (4), outreach templates (5), conference preparation (6), community engagement (6), relationship CRM (4), cross-skill principles (2).

### 6. office-hours (30 entries)
Six forcing questions + smart-routing (7), startup-mode operating principles (6), anti-sycophancy rules (5), pushback patterns (5), builder-mode operating principles (4), founder signal synthesis (3).

### 7. brand-system (30 entries)
Neural Architect identity (8 + YAML), diagram templates (4), presentation design (6), social media graphics (6), implementation notes (4), cross-medium principles (2).

### 8. ux-principles (100 entries) — deepest domain
Foundational principles (12), 10 audit categories totaling ~80 atomic items, Trunk Test + scoring (2). The atomic-entry approach lets a skill pull just the rule it needs (e.g. `corpus/ux-principles/audit/02-typography/no-skipped-heading-levels.md`).

### 9. ai-product-ux (30 entries)
Core AI UX patterns (6), confidence & calibration (4), failure & graceful degradation (4), context display patterns (5), reasoning transparency (4), progressive autonomy (4), design-system defaults for AI products (3).

### 10. evaluation-frameworks (40 entries)
18 cognitive patterns (Great-CEO thinking instincts), 11 review sections (architecture → design), 4 review modes (SCOPE EXPANSION / SELECTIVE / HOLD / REDUCTION), Step-0 framework (4), design rating rubric (3).

## Source attribution summary

- `source: skill` — language pulled directly from the source `SKILL.md` during authoring. Most entries.
- `source: research` — derived from public canon (JTBD, Wardley, AARRR, Cynefin, Cold Start, growth loops, etc.). Authoring agent must cite the canonical reference. Concentrated in `pm-frameworks/` (~80 of 110 entries) and parts of `ai-product-ux/` and `growth/metrics/`.

## Filename conventions

- Lowercase, kebab-case.
- Sub-domains use directory prefixes (`pm-frameworks/discovery/`, `growth/segments/`, `audit/02-typography/`).
- Series get numeric prefixes (`fatal-fifteen-01-...`, `cognitive-patterns/01-...`, `forcing-questions/q1-...`).
- Thinkers: `pm-frameworks/thinkers/lastname-firstname.md`.
- YAML resources colocate with markdown counterparts where appropriate (`growth/target-accounts/linkedin.yaml` next to `growth/target-accounts/linkedin-targets.md`).

## Entry schema (every `.md` file)

```markdown
---
name: {entry name}
domain: {domain slug}
source_skill: {originating skill(s), or "research"}
entry_type: {rule | framework | pattern | template | concept | person | resource | metric}
length_target: 300-800
related: [{paths}]
---

# {Entry Name}

## What it is
## Why it matters
## How to apply
## Examples
## Related entries
## Anti-patterns
```

## What user review should look at

1. **Total count** — 531 acceptable, or trim per the levers above?
2. **Domain boundaries** — is `content-system` really separate from `voice`, or merge? Is `ai-product-ux` separate from `ux-principles`?
3. **PM-frameworks granularity** — 110 entries with thinkers split out. Acceptable, or collapse thinkers into framework entries?
4. **ux-principles atomic-entry approach** — 80+ audit items as individual entries. Acceptable, or roll up to per-category entries?
5. **Open questions surfaced in each slice** — listed at the bottom of each `INVENTORY/{domain}.md` file. Worth resolving before authoring.

## What happens after approval

Phase 1 dispatches **3 authoring agents in parallel** for Batch A (voice, content-system, pm-frameworks). Each agent receives its INVENTORY slice + the entry schema + the source-skill paths and writes 25–60 entries per turn. Commits after each batch. Verification (file count, frontmatter validity, word-count range) between batches.

If pm-frameworks (110 entries) doesn't fit in a single agent turn, its slice splits into 2 agents (~55 entries each). Same for ux-principles (100 entries) in Batch D — splits into 2 agents (foundational + audit-categories).
