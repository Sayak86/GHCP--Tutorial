# Day 1 · Demo 4 — Agent Mode Builds the API (and how it differs from Plan mode)

**GHCP constituents:** Agent mode and Plan mode.

## 🌱 Simplest version first

Compare two ways of asking Copilot to build something:

- **Plan mode = the architect who writes the recipe.** You ask "how would you build this?" and it
  gives you a **written plan** — the steps, the files it *would* touch, how it would test. **It does
  not change any files.** You read the plan and approve it.
- **Agent mode = the cook who actually cooks.** You give it the task and it **does the work**:
  creates files, runs the tests, sees a test fail, fixes it, runs again — repeating until it's done
  or it needs to ask you something. You approve each risky step and review the result.

One picture to keep:

| | Plan mode | Agent mode |
|---|---|---|
| Produces | a written plan only | actual file changes |
| Touches your files? | **No** | **Yes** (with your approval) |
| Good for | thinking before doing, big/risky changes | getting the work done |
| Typical flow | plan first… | …then switch to Agent to build it |

**Normal chat (Ask mode)** is a third, simpler thing: it just answers a question and you do the
work yourself. So the ladder is: **Ask** (answers) → **Plan** (writes the recipe) → **Agent** (cooks).

## Dependencies

**Assumes `Day1-Demo1-Instructions` and `Day1-Demo2-Markitdown`.** Carried over: the instruction
files (so the build follows conventions with little steering) and `requirements/` (the stories it
builds from). This branch is the **first time application code exists** — it's the built result.

## What's in this branch

| File | Role | New / carried |
|---|---|---|
| `app/main.py` | The API: 4 endpoints + health, validation per BR-1..4 | ⭐ new |
| `app/store.py` | In-memory store loaded from `data/sample_payments.json` (the "data page") | ⭐ new |
| `data/sample_payments.json` | 5 example payments to start with, covering every status | ⭐ new |
| `tests/test_payments.py` | 9 tests: happy paths + negative cases (409, 422, 404) | ⭐ new |
| `requirements.txt`, `.gitignore` | run/test deps | ⭐ new |
| `.github/copilot-instructions.md`, `.github/instructions/` | standards | carried from D1·1 |
| `requirements/` | the stories built from | carried from D1·2 |

## How to run the demo (~25 min)

1. **Show Plan mode first (5 min).** Switch the chat mode to **Plan** and ask:
   > Plan how to build the PayLite API from requirements/user-stories.md.
   Read the plan it produces. Point out: *it wrote a recipe but changed nothing.*
2. **Now Agent mode does it.** Switch to **Agent** mode and:
   > Implement the PayLite API from requirements/user-stories.md. Structure: app/main.py
   > (endpoints), app/store.py (store loaded from data/sample_payments.json),
   > tests/test_payments.py. Follow the repo instructions. Keep app code under ~150 lines.
3. **Narrate the loop while it runs** — the most important minute of Day 1: "it planned, it's
   creating store.py, it ran the tests, one failed, it read the error, it's fixing it." Point at the
   approval prompts: *that is the human gate.*
4. Review the diff like a code review. Then: **"Run the tests and show me the results."**
5. Optional applause: `pip install -r requirements.txt && python -m pytest -q` → 9 passed.

## What to point out

- Because instructions existed (D1·1), the build needed almost no correction — the payoff of writing
  instructions first.
- Your job shifted from *typing* to *directing and reviewing*.
- Plan → Agent is the safest habit for anything big: **read the recipe before you let it cook.**

## Next

→ Day 2. `git checkout Day2-Demo1-CustomAgents`
