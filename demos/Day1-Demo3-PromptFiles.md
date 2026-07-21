# This stop: Prompt Files

**Concept in one line:** a great prompt should not die in someone's chat history — a prompt file
is a prompt under version control that anyone runs by typing `/its-name` in chat.

**Instructions vs prompt files:** instructions are *always on*; prompt files are *on demand*.

## What just appeared at this stop

| File | Run as | For |
|---|---|---|
| `.github/prompts/user-story.prompt.md` | `/user-story` | BA — requirement → story with Given/When/Then |
| `.github/prompts/new-endpoint.prompt.md` | `/new-endpoint` | Developer — scaffold an endpoint per conventions |
| `.github/prompts/test-plan.prompt.md` | `/test-plan` | Tester — test-case table + pytest skeletons |
| `.github/prompts/sprint-summary.prompt.md` | `/sprint-summary` | Scrum Master — stand-up notes from git history |

Open any of them: frontmatter (`mode`, `description`) + body. Note `${input:requirement:...}` in
`user-story` — prompt files take parameters.

## Try it (2 minutes)

In Copilot Chat type `/user-story`, press Enter, and feed it: *"An operations user can cancel a
payment that is still pending."* Watch it produce a story traced to the BRD — and flag anything
that conflicts with the business rules.

## Teach it

Live script: `docs/02-day1-runbook.md`, Demo 3. Best exercise of Day 1: each pair turns one of
their real daily chores into a prompt file.

**See exactly what this demo added:** `git diff Day1-Demo2-Markitdown..Day1-Demo3-PromptFiles --stat`
