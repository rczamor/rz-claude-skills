---
name: Textual Encoding (Confidence)
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 500
related: [corpus/ai-product-ux/patterns/confidence-indicators.md, corpus/ai-product-ux/confidence/visual-encoding.md, corpus/ai-product-ux/confidence/expressing-uncertainty.md, corpus/voice]
---

# Textual Encoding (Confidence)

## What it is
A template for qualifying language that signals confidence in AI outputs. "I'm confident..." / "This is likely..." / "This is uncertain — verify before acting." Text encoding is the always-on partner to visual encoding; even users who can't see color still get the signal.

## Why it matters
Visual cues are scanned; text is read. When a user reads "this is uncertain" they hold the output differently than when they read "this is the answer." The framing shapes downstream action. Textual encoding also creates a written record — when an AI output is screenshotted, forwarded, or pasted into a doc, the qualifying language travels with it. Color does not.

## How to apply
1. **Lead with the qualifier, not bury it.** "I'm confident: X." beats "X. (I'm fairly confident.)" The frame must precede the claim.
2. **Three registers, matching the visual scale.** "Known good" → assertive ("X."). "Hedged" → soft hedge ("X is likely. Verify if it matters."). "Uncertain" → explicit caveat ("This is a guess — confirm before acting.").
3. **Avoid the safety-blanket caveat.** "AI may be wrong" stapled to every output is noise. Caveats must vary with actual confidence.
4. **Match Riché's voice.** Direct, no hedging where confidence is real; honest hedging where it isn't. (See `corpus/voice/`.)

## Examples
1. **Context Layer Demo synthesized recommendation.** High confidence: "Three independent panels agree: launch in Q3." Hedged: "Two panels suggest Q3 — one outlier favors Q4. Verify before locking the date." Uncertain: "Insufficient consistency — pull more sources before deciding."
2. **Suzy insight readout.** "Backed by 250 verified consumers" (high). "Directional signal — n=40, treat as hypothesis" (hedged). "Insufficient sample for confident insight" (uncertain).
3. **Anthropic Claude's hedging in the wild.** "I'd estimate..." / "I'm not certain, but..." / "I don't have enough information to..." — three calibrated registers in active use.

## Related entries
- `corpus/ai-product-ux/patterns/confidence-indicators.md` — parent pattern
- `corpus/ai-product-ux/confidence/visual-encoding.md` — the always-paired visual partner
- `corpus/ai-product-ux/confidence/expressing-uncertainty.md` — the three-level taxonomy
- `corpus/voice` — Riché's voice rules; textual encoding inherits from them

## Anti-patterns
- **Uniform hedging.** Every output starts "I think...". The hedge becomes wallpaper and the user tunes out.
- **No hedging at all.** The model is confident in tone even when uncertain in fact. Trust collapses on the first miss.
