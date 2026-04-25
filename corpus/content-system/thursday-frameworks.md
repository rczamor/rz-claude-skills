---
name: Thursday Frameworks
domain: content-system
source_skill: copywriting
entry_type: pattern
length_target: 300-800
related: [corpus/voice/the-hook.md, corpus/content-system/arc-step-3-introduce-alternative.md, corpus/content-system/pattern-practitioner-credibility.md, corpus/pm-frameworks/]
---

# Thursday Frameworks

## What it is
A 400-700 word post that names a framework, explains the problem it solves, walks through how to apply it, and closes with one real example. The framework should be reusable — something a reader can take into their next sprint, design review, or roadmap call. Practical and structured, but not sterile. Every framework comes from something Riché has had to figure out himself, not pattern-matched from a textbook.

## Why it matters
Frameworks are the most-saved content type on LinkedIn. They get added to people's bookmark folders, screenshot into Slack threads, and reused in slide decks. A good framework with Riché's name on it travels further than a hot take and lives longer than a signal. They also reinforce the Product Management 30% domain — Riché is a builder who systematizes, not a PM who collects frameworks.

## How to apply
1. Name the framework. The name should describe what it does, not be cute. ("Five-Step Context Generation," not "The CGE.")
2. State the problem in one paragraph. What goes wrong when teams don't have this framework.
3. Walk through the framework — usually 3-7 steps or components. Each gets a one-paragraph explanation.
4. Give one real example. Riché's preferred sources: Grandstage, Helm Labs, IBM, Suzy, Context Layer Engine.
5. Close with a constraint or a "when not to use this" note. Frameworks without limits feel like sales copy.

## Examples

**Topic: The Five-Step Context Generation Process.** Names the framework explicitly. Problem: teams pipe raw data into LLMs and call it RAG. Walks through curate, synthesize, consolidate, prioritize, store intelligently — each step gets a 60-80 word paragraph. Real example: Grandstage's market intelligence pipeline cut retrieval from 50 docs to 4, accuracy up, latency down. Constraint at the close: don't use this for one-shot tasks where a single document is enough.

**Topic: The Decision-Readiness Test.** A framework for filtering which information should reach the LLM and which shouldn't. Three questions: would an expert use this to decide? does it survive consolidation with adjacent context? does it change the answer? Real example: how Suzy's Decision Engine reduced context size 4x without quality loss. Constraint: this works for decision-support agents, not creative-writing assistants.

**Topic: The Three-Domain Balance for Personal Brand Content.** A framework not about products but about thought leadership: every piece reinforces Context Layers (50%), Product Management (30%), or Leadership (20%). Real example: how Riché audits his own monthly post mix.

## Related entries
- `corpus/content-system/arc-step-3-introduce-alternative.md` — frameworks often map to step 3 of the context architecture story arc
- `corpus/content-system/pattern-practitioner-credibility.md` — every framework points to something Riché has built
- `corpus/pm-frameworks/` — when the framework is product-management substance, the corpus version lives there
- `corpus/voice/terminology.md` — "five-step context generation" is preferred terminology; don't drift

## Anti-patterns
- Framework with no real example. If Riché can't point to a system that uses it, it's an idea, not a framework. Don't ship.
- Framework as listicle. "Seven things to think about when..." isn't a framework — it's a checklist with a fancy intro. A framework has structure: a sequence, a decision tree, a 2x2, an evaluation rubric.
- Renaming an existing framework with a slight tweak. If it's 80% Lenny's framework with a Riché coat of paint, credit Lenny and add the 20%.
