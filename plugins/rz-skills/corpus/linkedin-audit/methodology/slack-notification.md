---
name: Slack Notification
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: template
length_target: 200-500
related: [corpus/linkedin-audit/methodology/report-assembly.md, corpus/linkedin-audit/methodology/task-issuance.md]
---

# Slack Notification

## What it is
Step 10 (final step) of the audit. Posts a one-line traffic-light headline to `#brand` with a link to the Notion audit page. The format is fixed; brevity is the discipline. Slack is the index card; Notion is the report.

## Why it matters
Slack rewards brevity. A multi-line audit summary spammed to `#brand` reads as noise and gets muted. A single line that says "what color, what mattered, where to read" is what gets opened. The discipline of one-line-only forces the audit's headline to be honest and specific.

## Format

```
{emoji} LinkedIn Audit — {Month YYYY}: {key finding}. {N} tasks issued. {notion_url}
```

Components:
- **Emoji**: 🟢 / 🟡 / 🔴 from the page's Overall Status
- **Period name**: `{Month YYYY}` (the period being audited, not the audit run date)
- **Key finding**: the single most important signal in 1 short clause. Examples:
  - Green: "Cadence held; engagement at 2.1%."
  - Yellow: "Engagement at 0.66% (target 3%+)."
  - Red: "Export parse failed mid-DEMOGRAPHICS."
- **Task count**: `{N} tasks issued` — even when N=0 (`0 tasks issued`)
- **Notion URL**: the URL to the page created in Step 9; the canonical link for follow-up

## How to apply

1. **Compose the message** from the headline (already computed in Step 7) and the task count (returned from Step 8).
2. **Truncate if needed.** The message should be ≤140 chars before the URL. If it exceeds, shorten the key finding clause until it fits.
3. **Post via Slack MCP** to `SLACK_CHANNEL` (`#brand`). Use `slack_send_message` (not `slack_send_message_draft` — drafts require manual approval and break the cron-fire flow).
4. **Capture the Slack permalink** for cross-reference in self-improve logging if needed.

## What does NOT go in Slack

- The full audit body. That's in Notion.
- Per-pillar findings. Those are in Notion.
- Multi-line elaboration. The discipline is one line.
- Threads or follow-up posts in the same `#brand` channel. The audit is one post per month.
- @-mentions of others. Riché is the assignee; no need to summon attention.

## Examples

1. **Green.** `🟢 LinkedIn Audit — May 2026: Cadence held at 23 posts; engagement at 2.1%. 0 tasks issued. https://notion.so/...`
2. **Yellow.** `🟡 LinkedIn Audit — May 2026: Engagement at 0.66% (target 3%+). 2 tasks issued. https://notion.so/...`
3. **Red.** `🔴 LinkedIn Audit — May 2026: Export parse failed mid-DEMOGRAPHICS. 1 task issued. https://notion.so/...`
4. **Zero-task green.** `🟢 LinkedIn Audit — June 2026: All pillars steady. 0 tasks issued. https://notion.so/...`

## Failure handling

- **Slack API unreachable.** Audit completes in Notion + Linear; the Slack post fails silently with a log entry. Riché sees the audit page in Notion via direct check (the cron firing is the only signal he relies on; if Slack fails, the audit still happened).
- **Channel `#brand` not accessible.** Same handling. Don't fall back to a different channel.

## Related entries
- `corpus/linkedin-audit/methodology/report-assembly.md` — produces the headline this step uses
- `corpus/linkedin-audit/methodology/task-issuance.md` — produces the task count this step uses

## Anti-patterns
- Posting a multi-line summary. Defeats the discipline.
- Adding @-mentions. The audit's signal is the page; @-mentions create alert fatigue.
- Suppressing the Slack post when N=0 tasks. The post itself is the cadence signal — even a quiet month gets a post so the channel knows the audit ran.
- Posting before Notion + Linear completed. Slack must be the last step; if Notion fails, the audit pretends it succeeded if Slack already posted.
