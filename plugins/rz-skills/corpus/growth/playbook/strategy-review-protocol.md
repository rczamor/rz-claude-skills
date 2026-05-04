---
name: Strategy Review Protocol — The 4-Axis Quarterly Assessment
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 600-1000
related: [corpus/growth/playbook/quarterly-channel-review.md, corpus/growth/playbook/quarterly-priorities-template.md, corpus/growth/strategy/creator-as-product.md, corpus/growth/databases/quarterly-reviews-schema.md]
---

# Strategy Review Protocol — The 4-Axis Quarterly Assessment

## What it is
The methodology for reviewing the 5 strategy documents that govern the personal brand at every quarterly review. Each document gets scored on 4 axes (Effectiveness, Alignment, Drift, Cross-doc misalignment), findings are synthesized into the Quarterly Review page, and a quarter-level "Strategy Drift" headline is computed. Surfaces strategy updates that should become quarterly priorities or P2 backlog items.

## The 5 strategy documents

These live in Notion under Brand → Growth Strategy → individual pages:

| Strategy | Notion page | Owns |
|---|---|---|
| **Product Strategy** | `333ac0ea-4f65-8165-b821-ceecca624346` | Market, positioning, ICP, value proposition for "Riché Zamor as a Brand" — treats the brand as a product |
| **Growth Strategy** | `356ac0ea-4f65-8082-8e68-f93292e3ea9d` | Growth model, segment focus, flywheel, time budget — the page that holds the Quarterly Reviews DB |
| **Content Strategy** | `333ac0ea-4f65-8151-8651-d730d706e017` | Editorial planning, format templates, voice, content calendar — extends Channel Strategy into content |
| **Channel Strategy** | `331ac0ea-4f65-81fe-af8f-e37afebaeaf5` | Where to publish, Context Layers positioning, channel-specific decisions |
| **Audience Development** | `33aac0ea-4f65-814f-8b22-f45410901cf6` | Who we're reaching, where they gather, how to reach them — sits above Channel Strategy |

The hierarchy is explicit: **Audience Development** answers *who*; **Channel Strategy** answers *where*; **Content Strategy** answers *what*; **Growth Strategy** answers *how* (loops, segments, budget); **Product Strategy** answers *what brand we're building*.

## Why it matters
Strategy documents go stale fast — faster than people notice. A strategy that defined Segment 2 as primary 6 months ago may quietly get out of sync with actual activity that has tilted toward Segment 3. Without an explicit quarterly check, the documents become aspirational rather than operational. Worse: documents start contradicting each other when one gets updated and the others don't, and nobody catches it until a major decision exposes the conflict.

The strategy review forces quarterly honesty:
- Are we doing what the strategy says? (Drift)
- Are we getting what the strategy predicted? (Effectiveness)
- Do this quarter's priorities match the strategy? (Alignment)
- Do the 5 docs say compatible things? (Cross-doc misalignment)

The point is not to be slavishly faithful to the docs — strategies evolve. The point is to make changes deliberate (update the doc) rather than incidental (drift while the doc stays stale).

## The 4 axes

For each of the 5 strategy documents, score on these axes during the quarterly review:

### Axis 1: Effectiveness
**Question:** Is the strategy producing the outcomes it predicted?

Compare the strategy's stated outcome targets (e.g., "drive Segment 2 reach via LinkedIn") against actual outcome data pulled in Step 2 of the quarterly review (channel ROI, segment-proxy metrics, audience composition).

- 🟢 Effective: outcomes within 20% of strategy targets
- 🟡 Mixed: outcomes 20–50% below targets, or no clear targets defined
- 🔴 Ineffective: outcomes >50% below targets, or moving in wrong direction

### Axis 2: Alignment
**Question:** Do the prior-quarter priorities and current channel mix match what the strategy says?

Cross-reference the prior Quarterly Review's priorities + the current active channel set against the strategy's stated focus areas.

- 🟢 Aligned: priorities and channels reflect strategy
- 🟡 Partial: ≤1 priority or channel doesn't fit the strategy
- 🔴 Misaligned: ≥2 priorities or channels contradict the strategy

### Axis 3: Drift
**Question:** Has actual activity drifted from the strategy without an explicit update?

Check the document's Last Modified date against significant decisions made in the prior quarter. If decisions were made that should have updated the strategy but the doc is stale, that's drift.

- 🟢 Current: doc updated within the last quarter, or no material decisions warranted update
- 🟡 Stale: doc not updated in 2+ quarters AND material decisions were made
- 🔴 Frozen: doc not updated in 4+ quarters AND multiple material decisions were made

### Axis 4: Cross-doc misalignment
**Question:** Do the 5 documents say compatible things, or do they contradict each other?

Read each document's stated focus and check for contradictions:
- Audience Development claims primary segment X, but Channel Strategy primarily targets Y
- Product Strategy positions for segment A, but Growth Strategy targets segment B
- Content Strategy tone differs from Product Strategy voice
- Channel Strategy includes a channel that Growth Strategy excluded as anti-pattern

- 🟢 Compatible: docs reinforce each other
- 🟡 Minor conflict: 1 contradiction between two docs
- 🔴 Major conflict: ≥2 contradictions, or a foundational contradiction (e.g., audience definition)

## Computing the Strategy Drift headline

The quarter's overall Strategy Drift headline is computed from per-document scores:

- 🟢 **Aligned**: every doc 🟢 on every axis OR exactly one doc has one 🟡 and zero 🔴
- 🟡 **Minor drift**: 2-3 🟡s across axes/docs, but zero 🔴s
- 🔴 **Major misalignment**: any 🔴 on any axis OR ≥4 🟡s across docs

This headline gets stored in the Quarterly Reviews DB's `Strategy Drift` property (when added) and surfaces at the headline level so trends across quarters are queryable.

## How to apply

**During the quarterly review (Step 5 of `rz-quarterly-review`):**

1. **Read each of the 5 strategy docs** via Notion MCP `notion-fetch`. Capture: stated targets, current focus, named segments/channels/priorities, last modified date.

2. **Per-doc 4-axis assessment** (4 min each × 5 = 20 min total cap):
   - Effectiveness vs Step 2 data
   - Alignment vs prior priorities + current channel set
   - Drift vs last-modified date + decisions taken
   - Cross-doc misalignment vs the other 4 docs

3. **Surface findings.** For each doc, note the worst axis score. Examples:
   - "Product Strategy is 🟢 across all 4 axes — no concerns"
   - "Channel Strategy is 🟡 on Drift — last modified 4 months ago, but the Reddit/Discord channel additions in Q4 weren't reflected"
   - "Content Strategy is 🔴 on Cross-doc misalignment — names voice attributes that contradict the Voice corpus and Audience Development tone guidance"

4. **Aggregate to Strategy Drift headline** per the rules above.

5. **Decide on strategy-update priorities:**
   - 🔴 findings → strategy-update task becomes a candidate quarterly priority (counts against MAX_PRIORITIES = 3)
   - 🟡 findings → strategy-update task becomes a P2 backlog item (does NOT count against priority cap)
   - 🟢 findings → no action

6. **Write findings into the Quarterly Review page body** under a "Strategy Review" section. Format:
   ```
   ## Strategy Review
   
   **Overall: 🟢 Aligned / 🟡 Minor drift / 🔴 Major misalignment**
   
   ### Product Strategy — 🟢
   - Effectiveness: 🟢 Segment 2 reach metrics within 12% of target
   - Alignment: 🟢 Q1 priorities reflect strategy
   - Drift: 🟢 Updated 3 weeks ago after Q4 decisions
   - Cross-doc: 🟢 Compatible with all 4 other strategies
   
   ### Channel Strategy — 🟡
   - Effectiveness: 🟢 LinkedIn cadence and engagement on track
   - Alignment: 🟡 Active channels include Reddit (Experiment), but doc doesn't mention it
   - Drift: 🟡 Last modified 4 months ago; Reddit added Q4
   - Cross-doc: 🟢
   - **Recommended:** P2 backlog — update Channel Strategy to include Reddit as Experiment-stage
   
   ... (3 more docs)
   
   ### Strategy update priorities for next quarter
   - [None / Priority N: Update {doc} ... / P2 backlog: ...]
   ```

## When to skip

- **Never skip the strategy review.** Even if no changes are expected, the review surfaces silent drift.
- **First-quarter caveat:** if a strategy doc was just created this quarter, score it 🟢 on Drift by default and on Cross-doc only if it actively contradicts an existing doc.
- **Blank docs:** treat empty pages as 🟡 on Effectiveness (no targets to measure against) and 🔴 on Drift (no current content). The recommendation is to either populate or retire the doc.

## Examples
1. **Aligned quarter (rare).** All 5 docs 🟢 across all axes. Strategy Review section is brief: "All strategies aligned and effective; no updates needed." Quarterly Reviews DB Strategy Drift = 🟢 Aligned.
2. **Standard quarter.** 4 docs 🟢, 1 doc 🟡 (Channel Strategy on Drift, missing recent channel additions). Strategy Review section names the gap and recommends a P2 backlog task. Strategy Drift = 🟡 Minor drift.
3. **Misalignment quarter.** Audience Development was updated to focus on Segment 1 hiring managers, but Content Strategy still leads with Segment 2 peers, and Growth Strategy still names Segment 2 as primary. Two contradictions. Strategy Review proposes a quarterly priority: "Reconcile audience focus across Audience Development, Content, and Growth strategies." Strategy Drift = 🔴 Major misalignment.

## Related entries
- `corpus/growth/playbook/quarterly-channel-review.md` — the broader quarterly review process this nests inside
- `corpus/growth/playbook/quarterly-priorities-template.md` — strategy-update findings can become priorities
- `corpus/growth/strategy/creator-as-product.md` — the framing that justifies strategy-as-evolving-document
- `corpus/growth/databases/quarterly-reviews-schema.md` — the DB property that captures the headline

## Anti-patterns
- Treating the strategy docs as authoritative when they're stale. The data wins; if the data contradicts the doc, the doc is wrong.
- Treating the data as authoritative when it's a 1-quarter sample. Two consecutive quarters of evidence is the threshold for proposing a strategy change.
- Updating one strategy doc without checking the others. Cross-doc misalignment usually starts here.
- Letting strategy review become a rumination session. 20-minute cap; surface findings, propose actions, move to priority setting.
- Recommending strategy updates without naming the specific edit. "Update Channel Strategy" is too vague; "Add Reddit as Experiment-stage channel under section X" is actionable.
