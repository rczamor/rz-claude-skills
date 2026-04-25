---
name: Customer Development
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/thinkers/blank-steve.md, corpus/pm-frameworks/lifecycle/lean-startup.md, corpus/pm-frameworks/discovery/jobs-to-be-done.md, corpus/pm-frameworks/discovery/continuous-discovery-habits.md]
---

# Customer Development

## What it is

Steve Blank's parallel-track methodology to product development: while engineers build the product, founders run a structured discovery process with customers to validate hypotheses. Four sequential stages:

1. **Customer Discovery** — test problem and product hypotheses with target customers; iterate until both are validated.
2. **Customer Validation** — verify a repeatable, scalable sales process exists.
3. **Customer Creation** — build demand; scale acquisition.
4. **Company Building** — transition from learning organization to executing organization.

Codified in Blank's *The Four Steps to the Epiphany* (2005) and *The Startup Owner's Manual* (2012). The famous mandate: "Get out of the building."

## Why it matters

Customer Development inverted the dominant 20th-century model — "build it and they will come" waterfall — and gave startups a structured way to stop building things nobody wanted. It's the intellectual ancestor of Lean Startup (Ries was Blank's student), the Lean Canvas (Ash Maurya), and modern continuous discovery (Torres). The core move: hypotheses are explicit, falsifiable, and tested against real customer behavior, not internal opinions.

For AI products: Customer Development matters more, not less. The build-versus-discover ratio in AI is dangerous — model capability lets you build almost anything in a week, so the temptation to skip discovery is acute. The customers most likely to "buy" an AI prototype during a discovery call are the customers least likely to renew. Customer Development's emphasis on validating *re-purchase intent* and *willingness to pay* — not just initial enthusiasm — is the corrective.

## How to apply

1. **State your hypotheses explicitly.** Problem hypothesis (who has this pain?), product hypothesis (would this solution address it?), business hypothesis (would they pay for it?). Write them down before the first interview.
2. **Run problem interviews first** (no demo, no pitch). Discovery, not validation. Listen for the language of pain, the workarounds in use, and what they've already tried.
3. **Run solution interviews second.** Show a low-fidelity artifact (mockup, prototype, landing page). Test desirability and willingness to pay. The "would you pay" question is weak; "would you pre-pay" is stronger; "give me a check" is strongest.
4. **Pivot on disconfirmation.** When the data invalidates a hypothesis, change the hypothesis — not the data interpretation. The most common Customer Development failure is rationalizing away disconfirming evidence.
5. **Move to validation only when discovery converges.** A consistent customer profile, a repeatable language of pain, and demonstrated willingness to pay.

## Examples

1. **Helm Labs problem interviews.** Riché ran 30+ problem-only conversations with PE-backed CFOs before showing a prototype. The pre-launch pipeline of $3.25M came from those conversations, not from a demo — by the time the demo existed, the problem hypothesis was already validated.
2. **Failure case (industry).** A consumer AI app with 10,000 sign-ups in two weeks, glowing reviews, and zero retention after week four. Customer Development would have caught this in solution interviews — the "I love this!" response correlates poorly with "I'd pay for this monthly."

## Related entries

- `corpus/pm-frameworks/thinkers/blank-steve.md` — Blank's broader contribution including Lean LaunchPad
- `corpus/pm-frameworks/lifecycle/lean-startup.md` — Ries' synthesis of Customer Development with build-measure-learn
- `corpus/pm-frameworks/discovery/jobs-to-be-done.md` — JTBD interviews are a Customer Development variant
- `corpus/pm-frameworks/discovery/continuous-discovery-habits.md` — Torres' modern reformulation
- `corpus/pm-frameworks/discovery/problem-vs-solution-space.md` — the conceptual basis

## Anti-patterns

- **Pitch interviews disguised as discovery.** Founder spends 80% of the interview describing the product. No information is acquired; the founder leaves more confident and less informed.
- **Selection bias in the customer pool.** Interviewing friendlies, advisors, or warm leads who tell you what you want to hear. Find skeptics; their disconfirmation is data, friendlies' enthusiasm is noise.
