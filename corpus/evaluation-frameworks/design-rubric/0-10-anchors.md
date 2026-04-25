---
name: 0-10 Rating Anchors
domain: evaluation-frameworks
source_skill: plan-design-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/design-rubric/dimensions.md, corpus/evaluation-frameworks/design-rubric/explain-then-improve.md, corpus/evaluation-frameworks/review-sections/11-design-ux-review.md]
---

# 0-10 Rating Anchors

## What it is
The rating method used in `/plan-design-review` and `/design-review`. Each design dimension (information architecture, interaction states, journey, AI slop risk, design system alignment, responsive/a11y, unresolved decisions) gets a 0-10 rating anchored at 0, 5, and 10. The anchors make the ratings legible — not feelings, but observable properties. A 4 means something specific. A 10 means something specific. The reviewer's job is to compare the plan to the anchors, not to introspect.

## The anchor pattern (per dimension)
Every rating sits between three reference points:

**0 anchor** — the dimension is absent or actively broken. No information hierarchy at all; every empty state is a sad-face placeholder; mobile is "stacked," with no real responsive thinking; AI slop everywhere.

**5 anchor** — the dimension is partially present but not load-bearing. Some hierarchy exists but it's inconsistent; empty states are styled but not designed (no warmth, no primary action); mobile is functional but uninspiring; some originality, some generic patterns.

**10 anchor** — the dimension is fully realized; this is the version that makes a new engineer reading the plan in 6 months say "oh, that's clever and obvious at the same time." Hierarchy is clear on every screen. Empty states feel warm and offer a primary action. Mobile is intentionally re-laid-out, not just stacked. Every UI choice is specific and defensible.

## How to apply
1. For each dimension, name the 0, 5, and 10 anchors before rating. The anchors are the rubric. Without them, rating is noise.
2. Compare the plan to the anchors. Is it closer to 0, 5, or 10? Then refine: 4? 6? 7?
3. **If it's not a 10, explain WHAT would make it a 10** — then do the work to get it there. The rating is not the deliverable; the gap-and-fix is.
4. Re-rate after the fix. "Now 8/10 — still missing mobile nav hierarchy." Iterate until 10 or the user says "good enough, move on."

## The pattern in practice
```
1. Rate: "Information Architecture: 4/10"
2. Gap: "It's a 4 because the plan doesn't define content hierarchy.
        A 10 would have clear primary/secondary/tertiary for every screen."
3. Fix: Edit the plan to add what's missing.
4. Re-rate: "Now 8/10 — still missing mobile nav hierarchy."
5. AskUserQuestion if there's a genuine design choice to resolve.
6. Fix again → repeat until 10 or user says "good enough."
```

## Per-dimension anchor examples

**Information Architecture**:
- 0: no hierarchy specified; every element competes
- 5: H1/H2 named but inconsistent across screens
- 10: every screen specifies what user sees first/second/third; mobile and desktop hierarchies are explicitly different

**Interaction State Coverage**:
- 0: only happy path designed
- 5: loading and error states styled; empty and partial unstated
- 10: loading, empty, error, success, partial all specified per feature; empty states have warmth and a primary action

**Mobile Responsive**:
- 0: mobile not mentioned
- 5: "stacked on mobile"
- 10: mobile-specific layout, navigation, and interactions specified per viewport breakpoint

**Accessibility**:
- 0: not mentioned
- 5: "we'll do a11y pass before launch"
- 10: keyboard nav patterns, ARIA landmarks, touch target sizes (44px min), color contrast requirements specified in the plan

## Required output format
Per dimension: numeric rating, gap statement, proposed fix, re-rate after fix. No prose-only ratings — the rating must come with the anchor reference and the fix path.

## Why it matters
Design feedback drifts toward vibes ("this feels off") without anchored ratings. The 0-10 anchor system forces the reviewer to name what makes a 10 a 10 — which (a) is itself a design exercise, (b) makes feedback actionable rather than impressionistic, and (c) lets the team know what "done" looks like. The pattern's iteration step (rate → gap → fix → re-rate) is what turns rating into improvement.

## Related entries
- `corpus/evaluation-frameworks/design-rubric/dimensions.md` — the seven dimensions the anchors apply to
- `corpus/evaluation-frameworks/design-rubric/explain-then-improve.md` — the rate-then-explain-then-fix pattern
- `corpus/evaluation-frameworks/review-sections/11-design-ux-review.md` — Section 11 calls into `/plan-design-review` which uses these anchors

## Anti-patterns
- Rating without anchors. "I'd give this a 6" without naming what 6 means is just a vibe with a number on it.
- Stopping at the rating. The rating is the diagnosis; the fix is the deliverable.
