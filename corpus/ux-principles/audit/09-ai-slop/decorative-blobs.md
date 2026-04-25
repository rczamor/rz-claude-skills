---
name: Decorative Blobs, Floating Circles, Wavy SVG Dividers
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/identity/imagery-anti-patterns.md, corpus/ux-principles/audit/09-ai-slop/purple-violet-gradients.md]
---

# Decorative Blobs

## What it is
Floating gradient circles, abstract "blob" SVGs, wavy section dividers, animated mesh gradients in the background — decoration applied to fix a section that "feels empty." If a section feels empty, it needs **better content**, not decoration. This is one of the strongest tells of AI-generated design.

## Why it matters
The audit principle: *"if a section feels empty, it needs better content, not decoration."* Blobs and waves are visual filler — the signal that the designer (or LLM) ran out of meaningful things to put in the section and decided to add gradient noise instead. Real design earns its visual weight through typography, photography, product UI, or charts. Abstract decoration is the visual equivalent of stock-photo handshakes.

## How to apply
- Search for: `<svg>` elements positioned absolutely with no semantic role, gradient mesh backgrounds, wavy `<path>` shapes used as section dividers, animated background blobs (Framer Motion / Lottie animations on idle elements).
- Audit: for every decorative shape, ask: **what content could occupy this space instead?** A customer logo? A real screenshot? A useful stat? Decoration almost always loses to content.
- If a section *genuinely* has nothing to say, **delete the section** rather than adding blobs to fill it.
- Wave-shaped section dividers (the classic SVG curve at the bottom of a hero) are 2017's mistake. Use rectangular, straight, deliberate breaks — or no break at all.
- Background mesh gradients are sometimes used by major brands (Stripe, Linear) — but always in service of brand identity, not as filler. The use is intentional, paired with proper typography and content density.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<section class="relative">
  <div class="absolute -top-16 -left-16 w-96 h-96 rounded-full bg-purple-300 opacity-30 blur-3xl"></div>
  <div class="absolute bottom-0 right-0 w-72 h-72 rounded-full bg-pink-300 opacity-30 blur-3xl"></div>
  <h2>Why teams choose us</h2>
  <p>We're on a mission to...</p>
</section>
```

GOOD:
```html
<section>
  <h2>Why teams choose us</h2>
  <ul class="customer-logos">
    <li><img src="/logos/stripe.svg" alt="Stripe"/></li>
    <li><img src="/logos/linear.svg" alt="Linear"/></li>
    <li><img src="/logos/anthropic.svg" alt="Anthropic"/></li>
  </ul>
  <blockquote>
    "We caught 3 design regressions before merge in the first week." — <cite>Erin, Eng @ Linear</cite>
  </blockquote>
</section>
```

## Related entries
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader catalog.
- `corpus/ux-principles/audit/09-ai-slop/purple-violet-gradients.md` — most blobs are purple.

## Anti-patterns
- Adding blobs to a section to make it "feel less plain" — fix the content, not the background.
- Animated blobs that pulse / drift — slop with motion budget.
- Wavy section dividers between every section — signals "I had no idea where to break the page."
