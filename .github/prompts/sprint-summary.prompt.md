---
mode: agent
description: Scrum Master — stand-up / sprint summary from recent changes and git history
---

Produce a sprint summary for PayLite.

1. Run `git log --oneline -20` and look at #changes for uncommitted work.
2. Summarize: what was delivered (link to US-x stories), what is in progress, and anything
   that looks risky or unfinished (failing tests, TODOs).
3. Format as a stand-up note: **Done / In progress / Risks & asks** — short bullets a Scrum
   Master can read aloud in under a minute. No code blocks.
