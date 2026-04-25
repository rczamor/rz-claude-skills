---
name: Outside Voice — Independent Plan Challenge
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/step-0/implementation-alternatives.md, corpus/office-hours/anti-sycophancy/, corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md]
---

# Outside Voice — Independent Plan Challenge

## What it is
After all 11 review sections are complete, the Outside Voice step offers an independent second opinion from a different AI system (typically Codex; Claude subagent as fallback). The premise: two models agreeing on a plan is stronger signal than one model's thorough review. Outside Voice is informational — it does not auto-modify the plan. Every recommendation is presented to the user and decided one-by-one.

## When to invoke
- After Sections 1-11 are complete (not before — outside voice's value is in challenging the review's blind spots, not in pre-empting the review)
- Optional but recommended for any plan above small-bug-fix size
- Always optional for the user; never run without consent

## How it runs
1. Check tool availability (`which codex`).
2. Ask the user: "All review sections complete. Want an outside voice? Different AI system gives a brutally honest, independent challenge of this plan — logical gaps, feasibility risks, blind spots that are hard to catch from inside the review."
3. If accepted, construct the plan-review prompt. Read the plan file, plus the CEO plan document if Step 0D-POST persisted one (EXPANSION/SELECTIVE EXPANSION modes).
4. Execute the outside voice with a focused prompt: find what the multi-section review missed. Logical gaps and unstated assumptions, overcomplexity, feasibility risks the review took for granted, missing dependencies or sequencing issues, strategic miscalibration.
5. Present findings verbatim under a CODEX SAYS or OUTSIDE VOICE banner.
6. Identify cross-model tension — points where the outside voice disagrees with the multi-section review's findings. Flag each one.
7. For each substantive tension point, ask the user via AskUserQuestion to decide. Options: accept outside voice, keep current approach, investigate further, defer to TODOS.

## The integration rule (load-bearing)
Outside voice findings are **INFORMATIONAL until the user explicitly approves each one**. Do NOT incorporate outside voice recommendations into the plan without presenting each finding via AskUserQuestion and getting explicit approval. This applies even when the reviewer agrees with the outside voice. Cross-model consensus is a strong signal — present it as such — but the user makes the decision.

User sovereignty over the plan is non-negotiable. The reviewer may state which argument they find more compelling, but **MUST NOT apply the change without explicit user approval**.

## Cross-model tension format
```
CROSS-MODEL TENSION:
  [Topic]: Review said X. Outside voice says Y.
  [Both perspectives presented neutrally.]
  [What context the reviewer might be missing that would change the answer.]
```

If the outside voice and the section review agree throughout, note: "No cross-model tension — both reviewers agree."

## Required output format
The verbatim outside-voice output, the cross-model tension list, and per-tension AskUserQuestion calls. Persist a log line via `gstack-review-log` with status (clean / issues_found) and source (codex / claude).

## Why it matters
Section reviews are deep but inherit the reviewer's blind spots. The reviewer who built the architecture mental model in Section 1 may be unable to see, in Section 10, that the architecture itself is wrong. Outside voice supplies the fresh-eyes pass that the same-model deep review structurally cannot. The integration rule defends user sovereignty: even strong cross-model consensus does not equal permission to act. The user's decision authority is the boundary.

## When outside voice fails
- Codex auth failure: prompt user to run `codex login`
- Codex timeout (5 min cap): note and fall back to Claude subagent
- Subagent failure: skip with "Outside voice unavailable. Continuing to outputs."

All errors are non-blocking — outside voice is informational, never a gate.

## Examples
1. **Plan passes Section review cleanly**. Outside voice surfaces: "the plan assumes the user wants feature X, but the do-nothing analysis was thin — what's the user signal that this is wanted?" Cross-model tension: review said premise was solid; outside voice questions it. AskUserQuestion: investigate further? Defer? Proceed?
2. **Plan with detailed architecture**. Outside voice: "The two-service split adds operational complexity for a feature that fits in one service. Reconsider." Cross-model tension: Section 1 approved the split; outside voice flags it. The user decides.
3. **No tension**: outside voice and Section reviews fully aligned. Flag the consensus; proceed to outputs with high confidence.

## Related entries
- `corpus/evaluation-frameworks/step-0/implementation-alternatives.md` — alternatives are the within-review counterpart to outside voice's cross-model challenge
- `corpus/office-hours/anti-sycophancy/` — outside voice's "no compliments, just problems" prompt is anti-sycophancy operationalized
- `corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md` — Section 10's strategic miscalibration concern overlaps with outside voice's

## Anti-patterns
- Auto-applying outside voice changes because "the model agreed." The integration rule explicitly forbids this. Every change is a user decision.
- Skipping outside voice because the section review felt thorough. Outside voice's value is precisely in catching what felt thorough. Thoroughness is not the same as completeness.
