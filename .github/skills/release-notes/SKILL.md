---
name: release-notes
description: Produce PayLite release notes in the team's house style from git history and user stories. Use when asked for release notes, a change log, or a "what shipped" summary.
---

# Release notes — house style and procedure

## Procedure

1. Collect: `git log --oneline --no-merges` since the last tag (or all history if no tags), plus
   `requirements/user-stories.md` for story titles.
2. Group commits by user story (US-x). Commits with no story go under "Housekeeping".
3. Drop noise: formatting, typo and merge commits never appear in release notes.
4. Verify claims: only list a feature as shipped if its tests exist and pass.

## House style (strict)

```markdown
# PayLite <version> — <date>

## New
- <User-visible capability, business language, one line> (US-x)

## Changed
- ...

## Fixed
- ...

## Known limitations
- ...
```

- Business language only: "Supervisors can now authorize pending payments", never
  "Added POST endpoint to router".
- Every "New" line cites its story number. No section may be empty — omit unused sections.
- Maximum 12 lines total; release notes are read by operations, not engineers.
