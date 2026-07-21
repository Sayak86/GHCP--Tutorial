# This stop: Custom Instructions

**Concept in one line:** a repo can carry *standing orders* that Copilot silently obeys in every
single chat — your team standards, encoded once, applied always.

## What just appeared at this stop

| File | What it is |
|---|---|
| `.github/copilot-instructions.md` | Repo-wide rules: tech stack, domain rules, working agreements. Loaded into **every** Copilot request in this repo. |
| `.github/instructions/python-style.instructions.md` | Scoped rules — the `applyTo: "**/*.py"` frontmatter means it loads only when Python files are involved. |
| `.github/instructions/tests.instructions.md` | Scoped rules for `tests/**` only. |

## Why two flavors

Repo-wide instructions cost tokens on *every* request. Scoped `applyTo:` files load only when
matching files are in play — your first taste of token economics by design.

## Try it (2 minutes)

1. Open Copilot Chat, any mode, and ask: **"Explain what FastAPI is."**
   → The answer uses Pega analogies. It does that because line-for-line, the instructions file
   told it the audience is a Pega team. No prompt engineering needed — the repo did it.
2. Open the X-ray: `Ctrl+Shift+P` → **Developer: Show Chat Debug View** → inspect the last
   request → the instructions file is sitting inside it.

## Teach it

Full live-demo script (including the before/after trick that sells the feature):
`docs/02-day1-runbook.md`, Demo 1. Concept reference: `docs/04-ghcp-concepts.md`.

**See exactly what this demo added:** `git diff Day1-Start..Day1-Demo1-Instructions --stat`
