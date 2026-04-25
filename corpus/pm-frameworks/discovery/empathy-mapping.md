---
name: Empathy Mapping
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/discovery/jobs-to-be-done.md, corpus/pm-frameworks/discovery/core-jobs-framework.md, corpus/pm-frameworks/discovery/continuous-discovery-habits.md]
---

# Empathy Mapping

## What it is

A visualization technique developed by Dave Gray (XPLANE, *Gamestorming*, 2010) for synthesizing what a team learns about a user across four quadrants:

- **Says:** verbatim quotes, public statements, expressed positions.
- **Thinks:** internal thoughts inferred from behavior — what they wonder, worry about, hope for, but don't say aloud.
- **Does:** observed behavior, actions, workarounds, choices.
- **Feels:** emotional state — frustrations, anxieties, satisfactions.

Often paired with two additional sections: **pains** (obstacles, fears) and **gains** (desired outcomes), making it a six-zone map.

The artifact is a single-page synthesis of one user (or one persona derived from many users), used to align cross-functional teams on who they're building for.

## Why it matters

Personas are often hollow — demographic shells with no decision-relevance. Empathy maps force a richer, behavior-and-emotion-grounded picture of the user that designers, engineers, and PMs can all argue from. The Says/Does mismatch (what the user *claims* vs. what they *do*) is especially valuable: it reveals the gap between stated and revealed preferences, which is where most product insights hide.

For AI products, empathy mapping clarifies the emotional layer of AI interactions — anxiety about correctness, embarrassment about not knowing how to prompt, distrust of outputs — which determines whether users adopt or abandon.

## How to apply

1. **Pick one user** (or aggregate persona). Avoid building empathy maps for "all users" — they collapse into platitudes.
2. **Populate from research.** Each quadrant should be filled with evidence: interview quotes (Says), observed actions (Does), inferred thoughts (Thinks), expressed or inferred emotions (Feels). Cite sources.
3. **Surface contradictions.** Says vs. Does mismatches are gold. "I check our metrics every day" (says) but logs show monthly logins (does) — that's a real insight.
4. **Use it as a decision artifact.** When the team is debating a feature, return to the empathy map. Does this user think/feel/do anything that this feature addresses?

## Examples

1. **Suzy enterprise analyst.** Says: "I want faster studies." Does: rejects fast-turnaround studies if results lack stakeholder-friendly framing. Thinks: "If I bring back a result the CMO doesn't trust, I'll be the one explaining it for a week." Feels: anxiety about defensibility, not impatience about speed. The Says/Thinks gap reframes the roadmap from "faster" to "more defensible."
2. **Helm Labs CFO.** Says: "I need better reporting." Does: declines features that increase audit-trail complexity. Feels: existential fear of board-meeting embarrassment. The empathy map redirects feature investment from reporting depth to reporting confidence.

## Related entries

- `corpus/pm-frameworks/discovery/jobs-to-be-done.md` — JTBD provides the job; empathy map enriches the experience around it
- `corpus/pm-frameworks/discovery/core-jobs-framework.md` — pains and gains overlap with the empathy-map quadrants
- `corpus/pm-frameworks/discovery/continuous-discovery-habits.md` — empathy maps live or die on interview cadence

## Anti-patterns

- **Filling quadrants from imagination.** When sourced from team brainstorm rather than customer research, empathy maps become projection. The artifact then justifies whatever the team already wanted to build.
- **Empathy map as deliverable, not artifact.** Built once for an offsite, never updated, framed on a wall. Empathy maps are working documents — if they aren't revised after every interview, they're decoration.
