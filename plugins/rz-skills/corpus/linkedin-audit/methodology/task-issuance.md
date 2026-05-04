---
name: Task Issuance
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 400-700
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/linkedin-audit/methodology/report-assembly.md, corpus/linkedin-audit/methodology/slack-notification.md]
---

# Task Issuance

## What it is
Step 8 of the audit. Takes the findings buffer from Step 4 and creates Linear issues for the top P0 + P1 findings, capped at `MAX_MONTHLY_TASKS = 3`. Lower than the website audit's cap of 5 because monthly cadence implies fewer tasks per cycle — accumulating 5 tasks per month would compound into 60/year, far above sustainable execution capacity.

## Why it matters
Tasks are how findings turn into work. Without seed tasks, findings stay in the audit page and get forgotten. The 3-task cap is the discipline that keeps the audit from feeling like a chore generator.

The cap is also a forcing function: when 5+ findings could become tasks, picking 3 forces prioritization. The audit narrative still names all findings, but only the top 3 get the Linear-task signal that demands action.

## How to apply

### 1. Filter to P0 + P1 findings

From the buffer, select only findings with `severity ∈ {P0, P1}`. P2s never become tasks; they live in the narrative only.

### 2. Sort by severity then pillar order

```
sort_key = (severity_rank, pillar_order)
where severity_rank: P0=0, P1=1
      pillar_order: P1=0, P2=1, P3=2, P4=3, P5=4, P6=5
```

P0s come before P1s. Within the same severity, earlier pillars (P1 Reach & Velocity) come before later pillars (P6 Voice). This means cadence/reach issues take precedence over voice issues at the same severity.

### 3. Cap at MAX_MONTHLY_TASKS

Take the top 3. Remaining qualifying findings stay in the audit narrative but don't seed tasks. The cap is hard.

### 4. Assign due dates

Spread the 3 tasks across the first week of the month: Mon, Wed, Fri. If running mid-week, the first available date is Mon of the following week. Example for an audit run on Sunday June 1, 2026:
- Task 1: Mon June 2
- Task 2: Wed June 4
- Task 3: Fri June 6

This pacing gives Riché time to engage one task fully before the next surfaces, avoiding the "all due Monday" pile-up that defeats the discipline.

### 5. Create issues using the create-then-update pattern

Direct create-with-full-payload is unreliable in the Linear API; the recommended pattern is:

1. **Create simple.** Call `save_issue` with only `title` populated. This succeeds reliably.
2. **Update with full body.** Call `save_issue` again with the same `id` (returned from step 1) and the full body, project, assignee, due date, priority. This update succeeds reliably.

For each task, the resulting fields:
- `team` = `LINEAR_TEAM_ID`
- `project` = `LINEAR_PROJECT_ID` (Brand)
- `assignee` = `LINEAR_ASSIGNEE_ID` (Riché)
- `priority` = 1 if severity P0 else 2 (Urgent / High)
- `dueDate` = the assigned spread date
- `title` = the finding's headline (truncate to 100 chars)
- `description`:
  ```
  ## Why this fired
  {finding.evidence}

  ## Recommended action
  {finding.action}

  ## Source
  Surfaced by rz-linkedin-audit on {audit_date}, pillar {pillar}, severity {severity}.
  Audit page: {notion_url} (filled by Step 9)

  ## What "done" looks like
  {finding-specific completion criterion}
  ```

### 6. Capture TRZ-### IDs

Each successful create returns a Linear issue identifier (TRZ-###). Collect these into a list and pass to Step 9 (Write Notion page) for inclusion in the `Linear Tasks Issued` property and the Linear Tasks Issued section of the page body.

## Failure handling

- **Linear API unreachable mid-Step 8.** If task 1 created but task 2 failed: the audit completes with `Linear Tasks Issued = "TRZ-001 (TRZ-002, TRZ-003 failed; rerun task issuance)"`. Step 9 still writes the page; Step 10 still posts Slack. Riché manually creates the missed tasks.
- **Create-simple succeeds but update fails.** The Linear issue exists with title only and no body. Surface as a P2 anomaly in the audit page; Riché edits the body manually.
- **All 3 task creations fail.** Audit page goes to Notion with `Linear Tasks Issued = "(creation failed; rerun)"`. Slack post notes the failure: `🟡 LinkedIn Audit complete (Linear creation failed). {url}`.

## Examples

1. **Standard issuance.** Buffer has 1 P0 (P1 export anomaly) + 3 P1s (P3 thesis, P6 voice, P1 cadence). Sort: [P0-p1, P1-p1, P1-p3, P1-p6]. Cap at 3: [P0-p1, P1-p1, P1-p3]. Issued. P1-p6 stays in narrative.
2. **Light month.** Buffer has 1 P1 (P3 thesis) + 2 P2s. Only the P1 qualifies. 1 task issued. Slack post: "🟡 ... 1 task issued."
3. **Zero-task month.** Buffer has 4 P2s, no P0 or P1. No tasks issued. Slack post: "🟢 ... 0 tasks issued."

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — Step 4; produces the buffer this step consumes
- `corpus/linkedin-audit/methodology/report-assembly.md` — Step 7; provides the headline format
- `corpus/linkedin-audit/methodology/slack-notification.md` — Step 10; uses the TRZ-### IDs

## Anti-patterns

- Issuing more than 3 tasks per audit. Compounds into unmanageable backlog.
- Issuing P2 findings as tasks. P2 is by definition "not actionable this month"; tasks-for-P2 is severity inflation.
- Skipping the create-then-update pattern. Direct create-with-full-payload fails ~10% of the time; the audit can't tolerate that flakiness.
- Pile-up due dates (all 3 due Monday). Defeats the spread-across-the-week pacing intent.
