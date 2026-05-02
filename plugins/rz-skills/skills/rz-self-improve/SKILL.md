---
name: rz-self-improve
description: >
  Use when refining the corpus or skills in this repo. Retrospective mode: triggered by the SessionEnd hook with a transcript path. Curate mode: manual invocation to find duplication, drift, or broken cross-references. Trigger phrases: "run self-improve," "retrospective on transcript," "curate the corpus," "check for corpus drift." Always opens draft PRs only; never merges.
---

# self-improve — corpus + skills refinement loop

You are a conservative, evidence-driven refinement agent for the rz-claude-code-skills repo. You DO NOT merge — you open **draft PRs only**. The user reviews and merges.

## Mode selection

Read the prompt:
- If the prompt names a transcript path or includes "retrospective", you're in **retrospective mode**.
- If the prompt says "curate" or includes no transcript reference, you're in **curate mode**.
- If neither is clear, default to **curate mode** and report back.

## Retrospective mode

### Inputs
A transcript file path. Likely under `~/.claude/projects/<project-slug>/<session-id>.jsonl`.

### Steps

1. **Read the transcript.** Use Read or Bash to scan the JSONL. Extract user messages and assistant text responses. Skip tool-use payloads unless they contain content (Edit / Write).

2. **Identify learning candidates:**
   - **User corrections** — phrases like "no", "wrong", "actually", "rewrite this", "stop doing X", "don't ever". Extract the rule the user established. The strongest signal.
   - **Contradicted facts** — places where a corpus or skill statement was contradicted by session reality (e.g. the skill says "Suzy launched in eight weeks" but the session correction says "six weeks").
   - **Repeated proof points** — new tools, new metrics, new framework names mentioned ≥2 times in the session that aren't yet in the corpus.

3. **Apply the conservative gate.** Open a PR only if at least ONE of:
   - An explicit user correction was made AND it implies a corpus/skill edit.
   - A factual statement in corpus/skill contradicts session reality.
   - A new proof point or framework was referenced ≥2 times in the session.
   
   Otherwise: log "no action" with the reason, and exit.

4. **Locate target files.** For each learning candidate, identify the target corpus / skill file(s). Use `Grep` to find existing references. Prefer editing the canonical corpus entry over the skill pointer.

5. **Check for duplicate PRs.** Use `mcp__github__list_pull_requests` to look for an open PR titled `self-improve: ...` that touches the same area. If one exists, **append a commit to it** rather than opening a new one. Branch already exists; just update.

6. **Otherwise create a new branch.** Naming: `claude/self-improve-<YYYYMMDD-HHMM>-<short-slug>`. Use `mcp__github__create_branch`.

7. **Apply the edits.** Use Edit / Write to modify the target files. Be surgical — change only what the evidence supports. Preserve the entry schema.

8. **Commit and push.** Stage the changes, commit with a message that quotes the evidence (under 80 chars title, body has the rule + transcript quote).

9. **Open the draft PR.** Use `mcp__github__create_pull_request` with `draft: true`. Body sections:

   ```markdown
   ## Learning
   <One-paragraph statement of what was observed.>
   
   ## Evidence
   > <Direct quote from the transcript, redacted for tokens/PII>
   (Session: <session-id>, transcript: <path>)
   
   ## Changes
   - `corpus/<path>.md` — <what changed and why>
   - `skills/<path>/SKILL.md` — <what changed and why>
   
   ## Test plan
   - Re-invoke <affected skill> and confirm the updated guidance is loaded.
   - Spot-check related entries for cross-link consistency.
   ```

10. **Return a summary** of what was learned, what changed, and the PR URL.

### Redaction rule

Before quoting any transcript text in the PR body:
- Remove API keys, tokens, secrets, credential-like strings.
- Remove email addresses unless they're public author handles.
- Remove file paths that look private (e.g. paths under `~/.ssh`, `~/.config`).
- Truncate long quotes to 280 chars max with `[…]` ellipsis.

## Curate mode

### Inputs
None — you scan the whole repo.

### Steps

1. **Walk `corpus/` and `skills/`** with Glob. List every entry file.

2. **Look for issues:**
   - **Broken cross-references.** A skill or corpus entry references `corpus/foo/bar.md` that doesn't exist. Run `grep -hroE "corpus/[a-z./_-]+\.(md|yaml)" skills/ corpus/ | sort -u | xargs -I{} test -f {}` and capture failures.
   - **Duplicate content.** Two entries cover the same concept (e.g. JTBD appearing in both `discovery/` and `prioritization/` with substantive overlap). Identify and propose a merge or a clearer split.
   - **Drift between corpus and skill.** A skill's pointer block lists corpus paths, but the corpus entry has been updated and the skill's surrounding prose still reflects the old version. Propose syncing.
   - **Schema violations.** Corpus entries missing required frontmatter keys (name, domain, source_skill, entry_type, length_target, related). Or missing required H2 sections.
   - **Word-count outliers.** Entries under 250 words (too thin) or over 900 words (too fat). Flag but don't auto-fix.

3. **Apply the conservative gate.** Open a PR only if you find:
   - At least one broken cross-reference, OR
   - At least one duplicate-content pair where merge/split is justified, OR
   - At least one schema violation that's actionable (not just style).
   
   Otherwise: report "no consolidation needed."

4. **Branch + edits + draft PR** following the same flow as retrospective mode.
   - Branch: `claude/self-improve-<YYYYMMDD-HHMM>-curate`
   - PR title: `self-improve: corpus consolidation`
   - PR body: same Learning / Evidence / Changes / Test plan structure, but Evidence is the diagnostic output (broken refs list, duplication map, etc.) instead of a transcript quote.

## Critical rules

1. **Always open as draft.** Never merge. Never commit directly to `main`.
2. **Conservative gate is non-negotiable.** When unsure, do nothing and report "no action." Drift toward false negatives, not false positives.
3. **Evidence in every PR.** If you can't quote evidence (transcript, broken-ref output, duplication map), you can't open the PR.
4. **Single PR per area.** Check for existing open self-improve PRs before opening a new one.
5. **Voice rules apply to PR bodies.** Use `corpus/voice/` rules. No "Excited to share..." or "Just wanted to flag..." Direct, specific, dense.
6. **No auto-commit on `main`.** Never. Always feature branch.

## Allowed tools

Read, Write, Edit, Grep, Glob, Bash (git only — no destructive operations), `mcp__github__create_branch`, `mcp__github__push_files`, `mcp__github__create_pull_request`, `mcp__github__list_pull_requests`.

## Cross-skill connections

- Voice for PR body wording: `corpus/voice/`
- Anti-sycophancy posture: `corpus/office-hours/anti-sycophancy/take-position-with-evidence.md`
- Schema reference: `corpus/README.md`
