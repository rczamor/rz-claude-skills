---
name: Z-Index Clarity — Nothing Unexpectedly Overlapping
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/01-hierarchy/visual-noise.md]
---

# Z-Index Clarity — Nothing Unexpectedly Overlapping

## What it is

Z-index is the layering order of elements on the page. Clarity means: the user can predict what's in front of what, and nothing unexpectedly overlaps. Modals appear above content. Tooltips appear above modals. Sticky headers stay above content. A dropdown menu doesn't accidentally render behind the page's hero image.

When z-index is sloppy, you get common bugs: a modal whose backdrop covers the close button, a sticky banner that hides the top of every form, a tooltip that disappears behind a card.

## Why it matters

Layering is a trust signal. Predictable layering means the interface "behaves." Unpredictable layering means the user encounters glitches — even if rare, glitches drain the goodwill reservoir. Worse, broken z-index can make a page literally unusable: a modal whose Submit button is hidden behind another element.

## How to apply

1. **Use a z-index scale, not arbitrary numbers.** Define tokens like `z-base: 0`, `z-dropdown: 100`, `z-sticky: 500`, `z-modal: 1000`, `z-tooltip: 2000`. No `z-index: 9999` hacks.
2. **Test stacking contexts.** A modal inside a `transform: translate` parent creates a new stacking context that can break z-index. Audit at every interactive moment.
3. **Sticky headers must stay above all page content.** Including any cards or banners in the body.
4. **Modals must trap focus and obscure everything underneath.** Including other floating elements.

## Examples

- **GOOD:** Tailwind's docs site — sticky nav stays above all content, dropdown menus open above the nav, search overlay covers everything when active.
- **BAD:** A SaaS app where opening a date picker partially renders behind a sticky banner, making the bottom half of the picker unreadable.
- **GOOD:** Linear's command bar — Cmd+K overlay appears above all UI, no z-index conflicts.
- **BAD:** Tooltip text that gets clipped by an `overflow: hidden` parent because the tooltip wasn't portaled to the body.

## Related entries

- `corpus/ux-principles/audit/01-hierarchy/visual-noise.md`

## Anti-patterns

- `z-index: 9999;` everywhere. Indicates the team gave up on layering.
- Forgetting that `transform`, `filter`, `opacity < 1`, and `position: fixed` can create stacking contexts.
