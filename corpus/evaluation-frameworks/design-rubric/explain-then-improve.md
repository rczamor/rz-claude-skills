---
name: Explain-Then-Improve Rule
domain: evaluation-frameworks
source_skill: plan-design-review
entry_type: rule
length_target: 300-800
related: [corpus/evaluation-frameworks/design-rubric/0-10-anchors.md, corpus/evaluation-frameworks/design-rubric/dimensions.md, corpus/office-hours/anti-sycophancy/]
---

# Explain-Then-Improve Rule

## What it is
The rule that governs every design rating in `/plan-design-review`. Rate, then explain, then propose specific improvements. Never rate without explanation; never explain without a fix path. The rating is a triage signal; the explanation is the diagnosis; the improvement is the deliverable. Plans that survive the rule arrive at 10/10 not because the reviewer was generous but because the reviewer kept fixing.

## The required sequence
1. **Rate** the dimension 0-10. Not a feeling — a comparison to the anchor (see 0-10 Rating Anchors).
2. **Explain** why it's not a 10. Specifically. "It's a 4 because the plan doesn't define content hierarchy. A 10 would have clear primary/secondary/tertiary for every screen."
3. **Propose** specific improvements. Not "improve hierarchy" — name the change. "Add an ASCII diagram of the dashboard screen showing what the user sees first (today's count), second (urgent items), third (everything else)."
4. **Apply** the improvement. Edit the plan.
5. **Re-rate**. "Now 8/10 — still missing mobile nav hierarchy."
6. Repeat 2-5 until 10/10 or user says "good enough, move on."

## What "specific improvements" means
Vague: "Add more design specificity." Specific: "Replace 'clean, modern UI' with 'Inter Display 32/28/20 type scale; 8pt spacing grid; one accent color (#EF6A2D); cards earn their existence — no decorative grids.'"

The improvement must be concrete enough that a different designer reading the plan tomorrow could implement it without asking what was meant.

## Why "explain" is its own step
Rating without explaining produces feedback that the team can't engage with. They get a number; they don't know why. The explanation step forces the reviewer to articulate the gap, which (a) makes the gap legible, (b) often reveals to the reviewer that the gap was different from what they first thought, and (c) gives the team something to push back on.

## Why "improve" is its own step
Explaining without proposing produces feedback that's accurate but inert. The team agrees there's a problem; nobody knows what to do about it. The improvement step forces the reviewer to make the call: this is what should change, and here's how. Sometimes this surfaces that the reviewer doesn't actually know how to fix it — which is also useful information.

## How it ties to AskUserQuestion
The improve step sometimes encounters a genuine design choice — two valid paths, neither obviously better. That triggers AskUserQuestion (per `/plan-design-review`'s STOP rule):
- Present both options
- Recommend one with reasoning
- Wait for user decision
- Apply the chosen option
- Re-rate

When there's no genuine choice (the fix is obvious), state what you'll do and apply it. Don't waste an AskUserQuestion.

## Required output format per dimension
```
DIMENSION: [name]
RATE: [N]/10
EXPLAIN: [what makes it less than 10, anchored to the dimension's 10 anchor]
IMPROVE: [specific edit to apply]

[apply the edit]

RE-RATE: [N]/10
[gap remaining, if any]

[repeat until 10 or "good enough"]
```

## Why it matters
Design reviews drift toward two failure modes: (a) ratings without explanations (vibe-based, unactionable), or (b) explanations without improvements (accurate but inert). The explain-then-improve rule is what produces actual improvement, not just diagnosis. The iteration step (re-rate → still gap → fix → re-rate) is what bends the curve from "rated and shrugged" to "rated and shipped at 10."

## Examples
1. **Information Architecture: 4/10**. Explain: dashboard plan lists 14 widgets without priority. Improve: edit plan to specify "Two top-row widgets are 'today's count' and 'urgent items.' All others below the fold." Re-rate: 8/10 — desktop hierarchy clear, mobile not specified. Improve: "On mobile, only show 'today's count' above the fold; everything else accessible via the secondary tab." Re-rate: 10/10.
2. **Empty State Coverage: 3/10**. Explain: empty list shows generic "no items." Improve: "Replace with: heading 'Your first project is a click away,' subheading explaining what a project is, primary CTA 'Create project,' optional secondary 'Import existing.'" Re-rate: 9/10 — needs micro-illustration but functional.

## Related entries
- `corpus/evaluation-frameworks/design-rubric/0-10-anchors.md` — anchors are the rubric the rating compares against
- `corpus/evaluation-frameworks/design-rubric/dimensions.md` — the seven dimensions the rule iterates through
- `corpus/office-hours/anti-sycophancy/` — explain-then-improve is anti-sycophancy in the design domain

## Anti-patterns
- Rating, explaining, but skipping improve. The team agrees with the diagnosis and ships unchanged. The improve step is where the value is.
- Improving without explaining. The team applies the fix without understanding the principle. Next plan repeats the same mistake.
