---
name: Instructions Detection
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/principles/users-dont-read-instructions.md, corpus/ux-principles/principles/law-1-dont-make-me-think.md]
---

# Instructions Detection

## What it is
Any visible block of instructions longer than one sentence is a design-failure signal. If users need to be told how to use the interface, the interface didn't do its job. Flag both the instructions *and* the interaction they are compensating for — fixing one without the other just hides the symptom.

## Why it matters
Krug's principle: users don't read instructions. They scan, they muddle through, they wing it. Instructions are written by designers desperate to compensate for a flow they couldn't make obvious. Users either skip them entirely (most common) or feel stupid for needing them (worse). Either way, the interface lost. Every instruction block is technical debt with a friendly font.

## How to apply
- Scan the page for instructional blocks: "How it works," "Getting started," tooltips longer than 6 words, helper text under inputs that explains *what the field is* rather than format hints, modal walkthroughs, "first time here?" overlays.
- For each, ask: **what interaction is this paragraph compensating for?** Then ask: **can the interaction be redesigned so the instruction is no longer needed?**
- Flag in audit reports as a *paired finding*: ❶ instructions block at `<selector>`, ❷ interaction it's compensating for (the actual root cause).
- Acceptable instructions: brief, timely, unavoidable (e.g., "We just sent a 6-digit code to your phone" right above the OTP field). These are scoping context, not instructions.
- Unacceptable: paragraph above a form explaining how to fill it out. Redesign the form.
- For AI products: tooltips explaining "what the AI is doing" usually mean the AI's behavior is opaque — surface confidence indicators or trace links instead of writing instructions about it.

## Examples (BAD vs. GOOD pairs)

BAD:
```
How it works
1. First, click the "+" icon in the top right corner to create a new project.
2. Once your project is created, you can invite team members from the Settings tab.
3. Use the Inbox tab to see updates from your team. Be sure to mark items as read!
```
The "be sure to mark items as read" block is compensating for an interaction that doesn't make read-state obvious.

GOOD:
- "+" icon has the label "New project" on hover; primary CTA in empty state for first-time users says "Create your first project" with the same icon.
- Read-state shown via clear unread indicator + auto-mark-as-read on view.
- Zero instruction blocks remain.

## Related entries
- `corpus/ux-principles/principles/users-dont-read-instructions.md` — Krug's primary source.
- `corpus/ux-principles/principles/law-1-dont-make-me-think.md` — the umbrella principle.

## Anti-patterns
- Onboarding overlays that explain every UI element — users dismiss without reading.
- "Pro tip" tooltips that exist because the feature isn't discoverable.
- Help text under every form field — find the 1–2 fields that genuinely need format hints, kill the rest.
