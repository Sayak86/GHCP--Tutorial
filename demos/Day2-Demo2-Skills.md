# This stop: Skills

**Concept in one line:** a skill is deep knowledge that loads **only when the task needs it** —
the token-friendly opposite of instructions (which are paid on every request).

Only a skill's `name` + `description` are always visible to the agent; the body is read on
demand. That's *progressive disclosure* — token economics as architecture.

**Rule of thumb:** conventions → instructions · knowledge & procedures → skills · recipes → prompt files.

## What just appeared at this stop

| Skill folder | Kind | What it knows |
|---|---|---|
| `.github/skills/payments-domain/` | knowledge | currencies, limits, the full status-transition matrix (see its `references/` file) |
| `.github/skills/explain-like-pega/` | style | how to explain Python/FastAPI to THIS team, with the canonical Pega mapping table |
| `.github/skills/release-notes/` | procedure | step-by-step + strict house style for release notes |

## Try it (2 minutes)

1. Ask in Agent mode: **"Can a SETTLED payment be rejected? Answer from the domain rules."**
   → the answer cites the lifecycle from the `payments-domain` skill.
2. Ask: **"Explain app/store.py to me."**
   → the explanation arrives in data-page/case vocabulary, courtesy of `explain-like-pega`.
   This is the crowd-pleaser of Day 2.
3. Open the chat debug view and see which skill bodies were actually loaded — and that they cost
   nothing on unrelated requests.

## Teach it

Live script: `docs/03-day2-runbook.md`, Demo 2.

**See exactly what this demo added:** `git diff Day2-Demo1-CustomAgents..Day2-Demo2-Skills --stat`
