# Curate mode

Manual invocation to find duplication, drift, or broken cross-references in the corpus and skills.

## Inputs

None. You scan the whole repo.

## Steps

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
