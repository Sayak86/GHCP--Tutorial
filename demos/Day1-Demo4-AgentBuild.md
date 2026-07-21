# This stop: Agent Mode built the app

**Concept in one line:** agent mode is the harness loop with hands — it plans, creates files,
runs tests, reads failures and fixes them, while you approve and review; here it built all of
PayLite from the user stories.

## What just appeared at this stop

| File | What it is |
|---|---|
| `app/main.py` | The FastAPI app: 4 endpoints + health, validation per BR-1..4 |
| `app/store.py` | In-memory store seeded from JSON (the "data page") |
| `data/seed_payments.json` | 5 seed payments covering every status |
| `tests/test_payments.py` | 9 passing tests incl. negative cases (409 on illegal transition, 422 on bad input) |

Everything here follows `.github/copilot-instructions.md` — that's why the build needed so little
steering. That is the payoff of Demo 1.

## Try it (2 minutes)

1. `pip install -r requirements.txt` then `python -m pytest -q` → 9 passed.
2. In Agent mode:
   > Add POST /payments/{id}/reject with a mandatory reason, per BR-4. Include tests. Run them.
   Narrate the loop while it works: plan → edit → run → read failure → fix.

## Teach it

Live script: `docs/02-day1-runbook.md`, Demo 4 — including what to narrate while the agent runs
(that narration is the most important minute of Day 1).

**See exactly what this demo added:** `git diff Day1-Demo3-PromptFiles..Day1-Demo4-AgentBuild --stat`
