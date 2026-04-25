---
name: Design Rubric — Dimensions
domain: evaluation-frameworks
source_skill: plan-design-review
entry_type: resource
length_target: 300-800
related: [corpus/evaluation-frameworks/design-rubric/0-10-anchors.md, corpus/evaluation-frameworks/design-rubric/explain-then-improve.md, corpus/ux-principles/]
---

# Design Rubric — Dimensions

## What it is
The seven dimensions evaluated by `/plan-design-review`'s 7-pass rubric. Each dimension receives a 0-10 rating with anchors, an explanation of the gap, and a proposed improvement. The dimensions are not interchangeable — they target distinct failure modes, and a plan that scores 10 across six of them but 0 on the seventh has a structural flaw, not a polish gap.

## The seven dimensions

**1. Information Architecture (Pass 1)**
What does the user see first, second, third? Apply "constraint worship" — if you can only show 3 things, which 3? Per-screen and per-flow.

**2. Interaction State Coverage (Pass 2)**
Loading, empty, error, success, partial states specified per feature. Empty states are first-class features — they need warmth, primary action, context. Not afterthoughts.

**3. User Journey & Emotional Arc (Pass 3)**
Storyboard the full emotional arc. Apply time-horizon design: 5-second visceral, 5-minute behavioral, 5-year reflective. Plans that ignore the emotional arc ship products that work but don't resonate.

**4. AI Slop Risk (Pass 4)**
Does the plan describe specific, intentional UI — or generic patterns? "Clean, modern UI" is not a design decision. Name the font, the spacing scale, the interaction pattern. The AI Slop blacklist (purple/violet gradients, 3-column feature grid, icons-in-circles, system-ui as primary font, etc.) is the concrete check.

**5. Design System Alignment (Pass 5)**
Does the plan align with DESIGN.md? Annotate with specific tokens/components. If no DESIGN.md exists, flag the gap and recommend `/design-consultation`. New components must fit the existing vocabulary.

**6. Responsive & Accessibility (Pass 6)**
Mobile/tablet specified per viewport — not "stacked on mobile" but intentional layout changes. A11y: keyboard nav patterns, ARIA landmarks, touch target sizes (44px min), color contrast requirements (4.5:1 on body text).

**7. Unresolved Design Decisions (Pass 7)**
Surface ambiguities that will haunt implementation. Specifically: type scale not defined, color system not defined, motion not specified, copy in placeholder state. Plans that leave these unresolved produce implementation drift.

## Why these seven (and not others)
The seven dimensions cover the orthogonal failure modes a UI plan can have. A plan can fail on hierarchy (Dimension 1) while passing every other dimension — the result ships looking polished but users can't find anything. A plan can fail on AI slop (Dimension 4) while having pristine accessibility — the result is correct and forgettable. The seven dimensions don't substitute for each other.

## How they interact
- Information architecture (Dim 1) and AI slop risk (Dim 4) are inversely related: the more specific the IA, the lower the slop risk
- Interaction state coverage (Dim 2) and accessibility (Dim 6) overlap on error states (a screen-reader-friendly error message is both a state and an a11y concern)
- Design system alignment (Dim 5) supplies the vocabulary for everything else; weak DESIGN.md → harder to score 10 on the others
- Unresolved decisions (Dim 7) is the catch-all — anything specific the other dimensions surface that's not yet decided

## What is NOT a dimension
- Aesthetic preferences ("does this look modern?") — too vibes-based; absorbed into AI slop and design system alignment
- Component architecture ("should this be one component or two?") — engineering, not design
- Business logic accuracy — that's the spec, not the design
- Motion polish (specific easing curves) — too granular for plan-level review; lives in `/design-review`

## Scoring across dimensions
Each dimension scores independently. A plan's overall design completeness is roughly the average — but the average lies. A 10/10 average across 6 dimensions and a 2/10 on the seventh is a structurally broken plan. Rate each, fix each, then look at the overall.

```
  DIMENSION                          | RATING | GAP                             | FIX
  -----------------------------------|--------|---------------------------------|------
  Information architecture           | 8/10   | Mobile nav not specified        | Add mobile IA
  Interaction state coverage         | 6/10   | Partial state missing           | Specify
  User journey                       | 7/10   | 5-min behavioral arc unstated   | Add storyboard
  AI slop risk                       | 4/10   | "Clean, modern UI"              | Name specifics
  Design system alignment            | 9/10   | One new component undefined     | Annotate
  Responsive/a11y                    | 5/10   | Touch targets not specified     | Add 44px rule
  Unresolved decisions               | 3/10   | Type scale, color system        | Resolve now

  OVERALL: 6/10 (NOT shippable — fix Dimensions 4 and 7 before implementation)
```

## Required output format
Per-dimension rating with gap and fix proposal, applied iteratively (per the explain-then-improve rule). Final overall rating with shippability assessment.

## Why it matters
The seven-dimension rubric is what separates "design feedback" from "design review." Feedback is impressions; review is structured. The dimensions are not opinions — they are the orthogonal axes a plan must hit to ship a complete design. Plans evaluated against the rubric, with anchors and the explain-then-improve cycle, arrive at 10s in days. Plans evaluated by vibes drift indefinitely.

## Related entries
- `corpus/evaluation-frameworks/design-rubric/0-10-anchors.md` — the anchor system that gives each dimension its rating scale
- `corpus/evaluation-frameworks/design-rubric/explain-then-improve.md` — the iteration rule applied to each dimension
- `corpus/ux-principles/` — the underlying UX laws that inform what "10" looks like per dimension

## Anti-patterns
- Treating one dimension as the master and ignoring the others. A plan can score 10 on aesthetic alignment and ship as a hostile product because accessibility was 2.
- Over-emphasizing AI slop risk to the point of avoiding decisive design choices. The dimension is a guard rail, not a brake. Specific, intentional, opinionated UI is the goal — not pattern-avoidance for its own sake.
