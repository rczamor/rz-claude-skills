# Corpus — Canonical Knowledge for Riché's Skills

A shared knowledge base referenced by the skills in this repo. One edit here updates every skill that imports from it. The corpus holds the dense, load-bearing material — voice rules, product-management frameworks, audience segments, UX principles, evaluation rubrics — that previously lived inline across multiple `SKILL.md` files and drifted as it was updated in one place but not others.

## Layout

Ten domains, one subdirectory each. Each contains 300–800-word markdown deep-dives, one file per canonical entry (rule / framework / pattern / template / concept / person / resource / metric).

```
corpus/
├── README.md                                 (this file)
├── INVENTORY.md                              master worklist — every entry, mapped to source
├── INVENTORY/                                per-domain inventory slices
│   ├── voice.md
│   ├── content-system.md
│   ├── pm-frameworks.md
│   ├── growth.md
│   ├── networking.md
│   ├── office-hours.md
│   ├── brand-system.md
│   ├── ux-principles.md
│   ├── ai-product-ux.md
│   └── evaluation-frameworks.md
├── voice/                    Voice rules, Fatal Fifteen, terminology, three-domain balance
├── content-system/           5 content types, story arcs, hook library, content pillars
├── pm-frameworks/            Discovery, prioritization, strategy, lifecycle, metrics, monetization + thinkers
├── growth/                   4 audience segments, weekly playbook, flywheel, growth loops, metrics
├── networking/               Relationship tiers, outreach templates, conference playbook, CRM
├── office-hours/             Six forcing questions, design doc templates, operating principles
├── brand-system/             Neural Architect palette, typography, diagrams, talk arc
├── ux-principles/            5 UX laws, audit categories, mobile, wayfinding, goodwill reservoir
├── ai-product-ux/            Reasoning transparency, confidence indicators, graceful degradation
└── evaluation-frameworks/    CEO cognitive patterns, 11 review sections, rubrics + anchors
```

## Entry schema (every `.md` file)

```markdown
---
name: {entry name}
domain: {domain slug}
source_skill: {originating skill(s), or "research"}
entry_type: {rule | framework | pattern | template | concept | person | resource | metric}
length_target: 300-800
related: [{other entry file paths}]
---

# {Entry Name}

## What it is
One-paragraph definition. Dense and concrete.

## Why it matters
The failure mode it prevents or outcome it enables. Grounded.

## How to apply
2–4 bullets or a short numbered procedure. Should read like a checklist.

## Examples
1–3 concrete examples — prefer Riché's context (Grandstage, Helm Labs, IBM, LinkedIn, conference talks), otherwise named industry examples with attribution.

## Related entries
- `corpus/{domain}/{other-entry}.md` — why it connects
- Cross-domain links welcome.

## Anti-patterns
1–2 bullets on how teams get this wrong.
```

## Referencing convention — from skills into corpus

A skill that previously held the content inline now holds a pointer block instead:

```markdown
## {Section Title}
Canonical reference in `corpus/`:
- corpus/{domain}/{file}.md — one-line hook
- corpus/{domain}/{file}.md — one-line hook
```

**Rule:** if content is used by ≥2 skills, it belongs in corpus. Skill-unique prose stays in the `SKILL.md`.

## Self-improvement

`skills/self-improve/SKILL.md` observes sessions and can propose refinements to corpus + skills via **draft PRs**. Two modes:

- **retrospective** — triggered automatically by the SessionEnd hook (`scripts/self_improve_hook.sh`). Reviews the just-ended session for user corrections, contradicted facts, or repeated proof points. Opens a draft PR only if the conservative gate passes.
- **curate** — manual or scheduled. Invoke with `claude -p "Run the self-improve skill in curate mode"` or inside a session with `/loop 24h`. Scans for duplication, drift, broken cross-references.

All self-improve PRs open as draft; the user merges.
