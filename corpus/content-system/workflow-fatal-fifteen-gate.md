---
name: Fatal Fifteen Publish Gate
domain: content-system
source_skill: copywriting
entry_type: pattern
length_target: 300-800
related: [corpus/voice/fatal-fifteen.md, corpus/voice/voice-anti-patterns.md, corpus/content-system/workflow-batch-writing.md, corpus/content-system/pattern-specificity-test.md]
---

# Fatal Fifteen Publish Gate

## What it is
A final check run on every draft immediately before publishing. The draft is read through against all 15 Fatal Fifteen rules plus the additional voice anti-patterns. Anything flagged gets rewritten before the draft ships. The gate is non-negotiable — a draft that fails a rule never publishes with the rule violation intact.

## Why it matters
The Fatal Fifteen are the difference between Riché's voice and generic AI thought leadership voice. Without the gate, drafts drift toward the median LinkedIn voice over time — "in today's AI-driven world," "let's dive in," "key takeaway," every empty signal phrase that makes thought leadership feel like an LLM wrote it. The gate is the active antibody against that drift. It also catches the most frequent voice errors at the cheapest possible point — before the post is live and the algorithm has already cached it.

## How to apply

Immediately before publishing each post, run the gate.

1. **Read through the full draft once.** Just read; don't edit. Note anything that feels off.

2. **Run the Fatal Fifteen checklist.** For each rule, scan for instances. Flag any hit.
   - "In today's..." opener
   - Filler transitions ("Moreover," "Furthermore," "Additionally," "That being said," "It's worth noting")
   - Symmetrical triples ("innovative, transformative, and groundbreaking")
   - Empty superlatives ("game-changing," "revolutionary," "unprecedented")
   - Faux-profound closings ("As we navigate an increasingly AI-driven world...")
   - Hedging ("While it's true that... it's also important to consider...")
   - Performative rhetorical questions ("But what does this mean for the future of work?")
   - Sanitized vocabulary
   - Uniform paragraph length
   - Summarizing instead of extending
   - "Let's dive in" / "Buckle up" / "Here's the thing"
   - "I'm thrilled/excited/honored to announce..."
   - "Navigate" used metaphorically
   - Multiple bolded phrases per paragraph
   - "Key Takeaway" summary blocks

3. **Run the additional anti-patterns.** Em dashes (replace with colons or commas), emoji overuse, performative closers ("Been saying it."), Silicon Valley hipster register.

4. **Run the specificity test.** Does the post contain at least one specific moment, decision, metric, or named tool? If not, it's not done.

5. **Voice test.** Could Riché actually say this out loud at a dinner with three other VPs? If it sounds rehearsed, rewrite the offending section.

6. **Publish only after every gate passes.** If something fails, fix it. If multiple things fail, the draft probably isn't ready — defer to next week.

## Examples

**Draft fails on rule 1.** "In today's AI-driven landscape, retrieval systems often struggle to..." — fails. Rewrite: "Retrieval systems lie. Three weeks after launch, our top user told me ours was lying to her."

**Draft fails on rule 7.** "But what does this mean for product builders going forward?" — performative rhetorical question. Rewrite: "Here's what changes for you on Wednesday morning: rerun the five-step audit with this in mind."

**Draft fails on the specificity test.** A 600-word framework post that names no system and uses no number. Either add a Grandstage or Suzy reference, or kill the post.

**Draft fails on em dash.** "Models get smarter every month — context quality stays the same." Rewrite: "Models get smarter every month. Context quality stays the same." Or: "Models get smarter every month: context quality stays the same."

**Draft passes.** A 220-word Monday hot take with one named system (Grandstage), one number (300%), no Fatal Fifteen hits, voice consistent with prior posts. Ships.

## Related entries
- `corpus/voice/fatal-fifteen.md` — the canonical list of 15 rules
- `corpus/voice/voice-anti-patterns.md` — additional anti-patterns beyond the 15
- `corpus/content-system/workflow-batch-writing.md` — drafts come from the batch; the gate runs separately
- `corpus/content-system/pattern-specificity-test.md` — the specificity test that runs as part of the gate

## Anti-patterns
- Skipping the gate when behind schedule. If a post can't pass the gate, it should defer, not ship with violations.
- Editing for grammar instead of voice at the gate. The gate is voice-specific. Save grammar for a separate pass during drafting.
- Treating the gate as a soft suggestion. The Fatal Fifteen are gates, not preferences.
