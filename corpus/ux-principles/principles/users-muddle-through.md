---
name: Users Muddle Through
domain: ux-principles
source_skill: design-review
entry_type: concept
length_target: 300-800
related: [corpus/ux-principles/principles/users-dont-read-instructions.md, corpus/ux-principles/principles/law-1-dont-make-me-think.md, corpus/ux-principles/principles/billboard-design-overview.md]
---

# Users Muddle Through

## What it is

Users don't figure out how things work. They wing it. They click whatever looks plausibly right, watch what happens, and adjust. If they accomplish their goal by accident — even via a path the designer would consider wrong — they will not seek the "correct" way. Once they find something that works, no matter how badly, they stick to it forever.

This is not a failure of users. It is a feature of human behavior under time pressure. Designers must build for the muddler, not the careful learner.

## Why it matters

A designer who builds for the careful learner imagines a user who reads instructions, explores menus, and finds the elegant path. The actual user clicks the first button they see, gets a result that's 80% right, and stops. If the elegant path requires understanding the product, the elegant path is invisible. If the muddled path produces a workable result, that's the path the user will take for years.

The implication: every plausible-looking action should produce a reasonable outcome. Dead-ends, error states, and "you can't do that here" responses are punishments for muddling — and users punish back by leaving.

## How to apply

1. **Audit every plausible click.** What happens if a user clicks the thing that looks right but isn't the intended path? Does the system handle it gracefully?
2. **Make wrong-but-plausible actions recoverable.** Saved state, undo, "did you mean..." prompts.
3. **Don't optimize the elegant path at the expense of the muddled path.** Most users take the muddled path; the elegant path is for power users.
4. **Watch real users muddle.** What do they click first? Where do they get stuck? Where do they accidentally succeed?

## Examples

- **GOOD:** Gmail's "Undo send" — assumes users will hit Send before they meant to, gives them a graceful escape.
- **BAD:** A workflow that requires the user to follow steps in order; if they click step 3 first, they get an error modal explaining what they should have done. The user gives up.
- **GOOD:** Slack's slash commands — typing `/giphy` works, typing `/gif` shows a "did you mean /giphy?" hint. Muddling rewarded.
- **BAD:** A billing portal where the only path to upgrade goes through a settings menu the user never finds. They cancel instead.

## Related entries

- `corpus/ux-principles/principles/users-dont-read-instructions.md` — muddlers especially skip instructions
- `corpus/ux-principles/principles/law-1-dont-make-me-think.md` — muddlers can't afford to think
- `corpus/ux-principles/principles/billboard-design-overview.md` — visible paths are the only paths

## Anti-patterns

- "Users will figure it out." They will figure out something — possibly not what you intended.
- Designing the happy path beautifully and leaving every other path as an error.
