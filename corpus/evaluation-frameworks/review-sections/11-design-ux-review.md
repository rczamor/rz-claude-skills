---
name: Section 11 — Design & UX Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/15-hierarchy-as-service.md, corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md, corpus/evaluation-frameworks/cognitive-patterns/18-design-for-trust.md]
---

# Section 11 — Design & UX Review

## What it is
The CEO calling in the designer. Section 11 is NOT a pixel-level audit — that's `/plan-design-review` and `/design-review`. Section 11 ensures the plan has design intentionality at the plan level: information architecture, interaction state coverage, user-journey coherence, AI slop risk, DESIGN.md alignment, responsive intention, and accessibility basics. It runs only when frontend/UI scope is detected.

## What it evaluates
- Information architecture — what does the user see first, second, third?
- Interaction state coverage map — `FEATURE | LOADING | EMPTY | ERROR | SUCCESS | PARTIAL`
- User journey coherence — storyboard the emotional arc
- AI slop risk — does the plan describe generic UI patterns?
- DESIGN.md alignment — does the plan match the stated design system?
- Responsive intention — is mobile mentioned, or an afterthought?
- Accessibility basics — keyboard nav, screen readers, contrast, touch targets

## Required output format
The interaction state coverage map populated for every UI feature:
```
  FEATURE              | LOADING | EMPTY | ERROR | SUCCESS | PARTIAL
  ---------------------|---------|-------|-------|---------|--------
  Project list         | spinner | "create your first" CTA | error toast + retry | populated grid | skeleton pre-load
  Settings save        | save btn shows "saving..." | (n/a) | inline error | saved toast | disabled while in flight
```

Plus the **required ASCII diagram**: user flow showing screens/states and transitions.

## Mode-specific additions
**EXPANSION and SELECTIVE EXPANSION**:
- What would make this UI feel inevitable?
- What 30-minute UI touches would make users think "oh nice, they thought of that"?

## Linkage to deeper review
If this plan has significant UI scope, Section 11 recommends: **"Consider running /plan-design-review for a deep design review of this plan before implementation."** Section 11 catches the plan-level intentionality gaps; `/plan-design-review` runs the 7-pass rubric (information architecture, interaction state coverage, user journey, AI slop, design system, responsive/a11y, unresolved decisions) with 0-10 ratings per dimension.

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**
- Skip Section 11 entirely if no UI scope detected (no new screens, no UI changes, no user-visible state changes, no responsive/mobile concerns).

## Why it matters
Plans that pass technical review and fail design review ship as functional but uncared-for products. Users perceive the gap immediately even if they cannot articulate it. Section 11 ensures the plan has at least named its design choices — empty states designed, error states designed, mobile considered, accessibility checked. The deeper rubric lives in `/plan-design-review`; Section 11 is the gate that says "we've done enough plan-level design thinking to merit running it."

## Examples
1. **Plan adds a new dashboard**. Section 11 demands the interaction state coverage map. Plan shows only the populated state. Surface the gaps: empty state (first-time user), error state (API down), partial state (some widgets loading).
2. **Plan describes "clean, modern UI"**. Section 11 flags AI slop risk — the description is generic. Demand specificity: which font, which spacing, which interaction pattern.
3. **Plan is desktop-first**. Section 11 surfaces responsive intention gap. Mobile isn't mentioned. Either commit to desktop-only with rationale, or specify the mobile experience.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/15-hierarchy-as-service.md` — Section 11's IA question IS hierarchy-as-service
- `corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md` — Section 11's AI-slop check applies subtraction-default
- `corpus/evaluation-frameworks/cognitive-patterns/18-design-for-trust.md` — Section 11's a11y/error-state lens is design-for-trust

## Anti-patterns
- Skipping Section 11 because "design is happening separately." If the plan touches UI, Section 11's plan-level intentionality must be in the plan, not in a parallel doc that may or may not arrive.
- Performing design review at this layer (going pixel-deep). That is `/plan-design-review`'s job. Section 11 is a gate, not the deep treatment.
