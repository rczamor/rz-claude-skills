---
name: Content Type Decision Workflow
domain: content-system
source_skill: copywriting
entry_type: pattern
length_target: 300-800
related: [corpus/content-system/monday-hot-takes.md, corpus/content-system/wednesday-deep-dives.md, corpus/content-system/workflow-batch-writing.md, corpus/voice/three-domain-balance.md]
---

# Content Type Decision Workflow

## What it is
A decision tree for choosing which of the five content types — hot take, signal, deep dive, framework, story — fits a given topic in a given week. Not every topic fits every type. A topic that's actually a story shouldn't be forced into a framework. A topic that's a hot take shouldn't get expanded to a deep dive just because it's Wednesday. The right mapping makes the difference between a post that lands and a post that reads as a shape-mismatch.

## Why it matters
The five content types are not interchangeable formats — they're different rhetorical structures with different reader expectations. A deep dive opens with a failure scene and walks through six story-arc steps. A hot take opens with a claim and lands in 200 words. A topic written in the wrong shape underperforms regardless of substance. The decision tree forces a 60-second triage during batch writing so the right topic goes in the right slot.

## How to apply

Walk the decision tree for each topic during Sunday batch writing.

1. **Is the topic triggered by news this week?** Yes → Tuesday Signal. No → continue.

2. **Is the topic a single sharp claim that fits in 200 words?** Yes → Monday Hot Take. No → continue.

3. **Is the topic a personal moment with a distilled lesson?** Yes → Friday Story. No → continue.

4. **Is the topic a reusable structure (steps, decision tree, evaluation rubric)?** Yes → Thursday Framework. No → continue.

5. **Is the topic a long-form architectural narrative with a failure → assumption → alternative → science → outcome → named-system arc?** Yes → Wednesday Deep Dive. No → the topic isn't ready; defer.

6. **Three-domain balance check.** Across the week, the mix should hit ~50% Context Layers, ~30% Product Management, ~20% Leadership. If two posts in the week cluster the same domain, swap one topic.

7. **Hook anchor check.** Which hook is anchoring the week? The deep dive should align with it. If the topic doesn't fit the anchor, either swap the topic or accept that this week's deep dive uses a different hook.

## Examples

**Topic: "Anthropic just announced a longer context window."**
- Triggered by news this week → Tuesday Signal. Done.

**Topic: "The first time Grandstage's retrieval system lied to a user."**
- Not news. Single claim? No, it's a moment. Personal moment with a distilled lesson? Yes → Friday Story. Done.

**Topic: "The five-step context generation process."**
- Not news. Single claim? No. Personal moment? No. Reusable structure? Yes → Thursday Framework. (Or Wednesday Deep Dive if expanded with a failure scene; in practice, this topic has shipped as both, with the Thursday version compressed and the Wednesday version full-arc.)

**Topic: "Models get smarter every month. Context quality stays the same."**
- Not news. Single claim? Yes → Monday Hot Take. Done.

**Topic: "How the Suzy Decision Engine launched in six weeks."**
- Not news (unless tied to a recent Suzy announcement). Single claim? No. Personal moment? Partially. Reusable structure? Could be — the six-week timeline is a framework. Long-form narrative with full arc? Yes → Wednesday Deep Dive. Decision: deep dive with the timeline as a structural beat in the body.

**Topic that defers.** "Something interesting happened in a meeting last week" — too vague. The topic isn't ready; sharpen first or defer.

## Related entries
- `corpus/content-system/monday-hot-takes.md` through `friday-stories.md` — the five types
- `corpus/content-system/workflow-batch-writing.md` — the decision happens during the Sunday block
- `corpus/voice/three-domain-balance.md` — the 50/30/20 weekly mix
- `corpus/content-system/hook-rotation-weekly.md` — hook anchoring decisions

## Anti-patterns
- Forcing a topic into the wrong shape. A story written as a framework reads cold; a hot take expanded to a deep dive reads padded.
- Skipping step 7 (the anchor check). Mismatching the deep dive to the week's hook fragments the editorial calendar.
- Treating the tree as rigid. Sometimes a topic is a hot take that wants to grow into a deep dive — that's fine, just commit before drafting.
