---
name: Premise Challenge (Step 0A)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/07-proxy-skepticism.md, corpus/office-hours/forcing-questions/q1-demand-reality.md, corpus/evaluation-frameworks/step-0/dream-state-mapping.md]
---

# Premise Challenge (Step 0A)

## What it is
The first move of every CEO plan review. Three questions that interrogate the plan's premise before any review of its content. The premise challenge runs before the review sections, before mode selection, before architecture diagrams — because if the premise is wrong, everything downstream is decoration on the wrong foundation.

## The three questions
**1. Is this the right problem to solve?** Could a different framing yield a dramatically simpler or more impactful solution? Most plans assume the problem statement; the premise challenge tests it. Often the problem as stated is a symptom of a different, more leveraged problem.

**2. What is the actual user/business outcome?** Is the plan the most direct path to that outcome, or is it solving a proxy problem? Plans drift toward proxies because proxies are easier to measure and execute against. The challenge: name the outcome, then ask whether the plan optimizes for it or for the proxy.

**3. What would happen if we did nothing?** Real pain point or hypothetical one? Plans frequently solve hypothetical problems (theoretical user complaints, anticipated competitor moves, executive imagination). The do-nothing scenario filters: if doing nothing is genuinely fine, the plan is optional and resources are better spent on plans where doing nothing is fatal.

## How to apply
1. Ask each question explicitly. Do not skip even if you "already know" the answer — the answer often shifts when you write it down.
2. For Q1, generate at least one alternative framing of the problem. If the original framing survives the alternative, that's a stronger premise. If the alternative is better, switch.
3. For Q2, name the outcome in user terms ("the user can do X," "the business can measure Y") rather than feature terms ("we ship Z"). The mismatch between feature and outcome is where proxies hide.
4. For Q3, sketch the do-nothing scenario realistically. "Users will complain" is rarely true; "12 users out of 10,000 will complain" might be.

## When the premise fails
If any of the three questions reveals a broken premise, the plan review pauses. The reviewer offers `/office-hours` (the upstream skill that produces design docs) as the right place to re-ground the problem. Do not proceed to Step 0B onward against a plan whose premise hasn't survived the challenge.

The premise challenge is allowed to kill the plan. That's its job.

## Required output format
A short answered-question block:
```
  PREMISE CHALLENGE
  Q1 — Right problem? [answer with alternative framing considered]
  Q2 — Outcome vs. proxy? [outcome named; plan-to-outcome path traced]
  Q3 — Do-nothing scenario? [realistic sketch; pain assessed]

  VERDICT: [premise holds / premise weak / premise broken — recommend re-grounding via /office-hours]
```

## Why it matters
The most expensive plan to review thoroughly is the one that shouldn't have existed. A 4-hour deep review of a misframed plan produces a polished version of the wrong feature. The premise challenge is 5 minutes of work that sometimes saves days. Even when the premise holds, articulating it makes the rest of the review sharper — every section knows what it's defending against.

## Examples
1. **Plan: "build a notification preferences page"**. Premise challenge Q1: is the right problem the preferences page, or is the right problem that we're sending too many notifications? If the latter, the preferences page is a proxy. The fix is fewer notifications, not more controls.
2. **Plan: "redesign onboarding"**. Q2: what's the outcome? "Activation rate up." Does the plan optimize for activation, or for "looks better than current onboarding"? Often the latter, dressed in activation language.
3. **Plan: "migrate to GraphQL"**. Q3: what happens if we don't? Often: nothing for 18 months, then maybe some friction. Plan defers; team works on higher-leverage work.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/07-proxy-skepticism.md` — Q2 IS proxy skepticism applied to the premise
- `corpus/office-hours/forcing-questions/q1-demand-reality.md` — `/office-hours` carries the deeper version of the premise challenge
- `corpus/evaluation-frameworks/step-0/dream-state-mapping.md` — premise challenge sets up dream-state mapping (0C)

## Anti-patterns
- Treating premise challenge as a checkbox. The questions must produce real answers, including occasionally "we should not build this."
- Answering Q3 with "we'd lose competitive position" without evidence. That's a hypothetical; produce the actual user/business signal that doing nothing would harm.
