---
name: Audit Log
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 600
related: [corpus/ai-product-ux/patterns/context-display.md, corpus/ai-product-ux/context/sources-panel.md, corpus/ai-product-ux/context/correction-interface.md, corpus/ai-product-ux/context/context-quality-display.md, corpus/ai-product-ux/reasoning/sidebar-pattern.md]
---

# Audit Log

## What it is
A template UI for the time-series record of context: what context was used at each decision point, what sources fired, what corrections the user made, and what the synthesis was. Recoverable and attestable. The audit log is the historical view that complements the live sources panel — what was true when, who changed what, and which decision flowed from which context.

## Why it matters
Enterprise buyers require it. Compliance teams require it. Any AI product moving toward autonomy requires it. When something goes wrong — or when something goes right and a stakeholder asks why — the audit log is the only honest answer. Without it, AI decisions are unprovable. With it, every decision is defensible. The log is also the substrate for product improvement: a six-month record of which contexts produced which decisions is a goldmine for eval.

## How to apply
1. **Log at the decision point, not the prompt level.** Every user-visible AI output gets a log entry: timestamp, sources used, corrections applied, output rendered.
2. **Attestation, not just storage.** The log entry should be tamper-evident — hash-chained or signed if the use case warrants. For most products, append-only with timestamps is enough.
3. **Query by user, by decision, by source.** "Show me every decision that used source X." "Show me every decision this user made last quarter." The log is a database; design queries.
4. **Surface a per-decision audit view to the user.** Click any past decision, see the full context that produced it. Most products hide this; surfacing it builds enterprise trust.
5. **Retain per policy.** Match the retention to the buyer's compliance posture. SOC 2 / HIPAA / GDPR shape the schema.

## Examples
1. **Context Layer Demo's decision history.** Every synthesis the user runs is logged with full context attached. A "history" view lets the user replay any past decision, see which sources fired, and re-run with a different correction. The replay is what enterprise buyers ask for first.
2. **Suzy Decision Engine's enterprise audit trail.** All automated insights are logged with respondent-level provenance. When a buyer's compliance team audits an insight six months later, the full panel data, segmentation, and synthesis are recoverable. This was a hard requirement for the 350+ enterprise customer rollout.

## Related entries
- `corpus/ai-product-ux/patterns/context-display.md` — parent pattern
- `corpus/ai-product-ux/context/sources-panel.md` — the live counterpart
- `corpus/ai-product-ux/context/correction-interface.md` — corrections that the log captures
- `corpus/ai-product-ux/context/context-quality-display.md` — the scores at each historical decision point
- `corpus/ai-product-ux/reasoning/sidebar-pattern.md` — the reasoning view at each log entry

## Anti-patterns
- **Log without query.** Storing everything but giving no way to find anything. The log is a tar pit, not a tool.
- **Log without surfacing.** Compliance teams have access; users don't. The user-facing decision is unaccountable to the user.
