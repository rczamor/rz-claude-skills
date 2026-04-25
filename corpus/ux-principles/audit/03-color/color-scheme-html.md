---
name: color-scheme — dark on html if Dark Mode Present
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/dark-mode-elevation.md, corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md]
---

# color-scheme — dark on html if Dark Mode Present

## What it is

Set `color-scheme: dark` (or `light dark`) on the `<html>` element when dark mode is active. This CSS property tells the browser to render system UI elements (scrollbars, form controls, default widgets, the address bar) in dark variants matching the page.

Without `color-scheme`, the page may render in dark mode while the browser's scrollbars stay white — a visible mismatch that signals incompleteness.

## Why it matters

A dark-mode page with white scrollbars is the design equivalent of wearing a tuxedo with white socks. The browser provides this hook specifically so dark-mode designers can make the entire viewport — chrome and all — match. Skipping it is neglect.

## How to apply

1. **In CSS:**
   ```css
   :root { color-scheme: light dark; }
   [data-theme="dark"] { color-scheme: dark; }
   [data-theme="light"] { color-scheme: light; }
   ```
2. **Or via meta tag:**
   ```html
   <meta name="color-scheme" content="dark light">
   ```
3. **Audit:** in dark mode, scroll a long page. Are scrollbars dark? If white, missing `color-scheme`.
4. **Test form elements.** Native inputs, selects, date pickers — do they pick up dark styling?

## Examples

- **GOOD:** GitHub in dark mode — scrollbars dark, form controls dark, everything cohesive.
- **BAD:** A site that styles every element to dark mode but forgets the scrollbar — bright white track on dark page.
- **GOOD CSS:**
  ```css
  html[data-theme="dark"] {
    color-scheme: dark;
  }
  ```
- **BAD:** Custom-styling scrollbars with `::-webkit-scrollbar` to fake dark mode instead of using `color-scheme`. Doesn't work on Firefox, breaks on form widgets.

## Related entries

- `corpus/ux-principles/audit/03-color/dark-mode-elevation.md`
- `corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md`

## Anti-patterns

- Forgetting this and shipping dark mode with white scrollbars. Users notice.
- Trying to manually style every native control with custom CSS. `color-scheme` is the supported way.
