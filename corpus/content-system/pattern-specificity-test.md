---
name: Specificity Test
domain: content-system
source_skill: copywriting
entry_type: rule
length_target: 300-800
related: [corpus/voice/proof-points.md, corpus/content-system/pattern-show-dont-tell.md, corpus/content-system/pattern-practitioner-credibility.md, corpus/content-system/workflow-fatal-fifteen-gate.md]
---

# Specificity Test

## What it is
A binary test applied to every draft: does the post contain at least one specific moment, decision, metric, or named tool? If yes, the draft can ship. If no, the draft gets rewritten until it does — or it kills. There are no exceptions. A post without a specific anchor reads like AI thought leadership, which is the opposite of the voice.

## Why it matters
Specificity is the single most reliable proxy for practitioner credibility. A 600-word post that names "Grandstage," "$0 CAC," "300% growth," "Letta," or "Klein's recognition-primed decision making" reads as substantive. A 600-word post that says "many AI products struggle with context" reads as commentary. The same person can write both kinds of post; the specificity test forces the practitioner version every time.

## How to apply

1. **Read the draft and underline every specific anchor.** Specifics qualify if they fall into one of four categories:
   - **Specific moment:** "Three weeks after launch," "Tuesday afternoon," "the first user who churned."
   - **Specific decision:** "We chose to consolidate before retrieving," "I rejected the longer context window approach."
   - **Specific metric:** Numbers, percentages, time-to-decision, customer counts. From the canonical proof inventory only.
   - **Specific named tool/system:** Grandstage, Suzy Decision Engine, Letta, Context Layer Engine, Claude Code Auto Dream, IBM personalization platform, Helm Labs pre-launch pipeline.

2. **Count anchors.** A hot take needs at least 1. A signal needs at least 1. A deep dive needs at least 3. A framework needs at least 1 named example. A story needs at least 1 specific moment.

3. **If under-anchored, find the specific.** What was the actual number? Which exact system? What was the moment that triggered the thought? Add it. If the answer is "I don't have a specific anchor here," the post isn't ready — defer.

4. **Run as part of the publish gate.** The specificity test is part of the Fatal Fifteen gate (`workflow-fatal-fifteen-gate.md`). It's not optional and it's not a soft check.

## Examples

**Pass.** "Retrieval without consolidation is just efficient delivery of noise. Grandstage v1 retrieved 50 docs and got the wrong answer. Grandstage v2 retrieved 4 and shipped." — Three anchors: named system (Grandstage v1, v2), specific metric (50 → 4), specific decision (consolidation).

**Fail.** "Many teams struggle with context architecture. The fix is consolidation." — Zero anchors. Vague, abstract, generic. Rewrite or kill.

**Borderline (deep dive that's under-anchored at 3).** A 900-word deep dive with one named system (Grandstage), one number (300%), and no specific moments. Two anchors total — under the deep dive minimum. Add the failure scene at step 1 of the story arc with a specific date or stakeholder, and the cognitive science citation by name (e.g., Klein's recognition-primed decision making) to push past three anchors.

**Story-specific test.** A Friday Story about leaving IBM that doesn't have a specific moment ("I knew I had to make a change"). Fails. Rewrite to a specific Tuesday afternoon, a specific Slack message, a specific door opened or closed.

**Signal test.** A Tuesday Signal reacting to an Anthropic release that says "this is interesting because context matters." Fails — no specific anchor beyond the news itself. Add the specific Grandstage example or the Klein finding the context window doesn't fix.

## Related entries
- `corpus/voice/proof-points.md` — the canonical inventory of named systems and metrics
- `corpus/content-system/pattern-show-dont-tell.md` — the show, don't tell rule (closely related)
- `corpus/content-system/pattern-practitioner-credibility.md` — specificity is the credibility move
- `corpus/content-system/workflow-fatal-fifteen-gate.md` — specificity is part of the publish gate

## Anti-patterns
- Specificity that isn't real. Inventing a number to pass the test is worse than failing it. Use only canonical proofs.
- Treating the test as a soft suggestion. A draft that fails specificity should not ship under any circumstance.
- Over-counting. A post that says "Grandstage" five times has one anchor, not five. Distinct anchors only.
