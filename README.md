# Day 1 · Demo 1 — Custom Instructions

**GHCP constituent:** custom instructions.

## 🌱 Simplest version first

Instructions are a **sticky note on the fridge** that everyone reads before they cook. You write the
house rules once; Copilot then follows them in **every** chat, without you repeating yourself.

**In one line:** a repo can carry standing rules that Copilot silently obeys in every chat.

## Dependencies

**None — this is the first lesson.** Start the course here. Nothing carried over.

## What's in this branch

| File | Role | New / carried over |
|---|---|---|
| `.github/copilot-instructions.md` | Repo-wide rules (tech, domain, agreements) — loaded into **every** request | ⭐ new (the star) |
| `.github/instructions/python-style.instructions.md` | Simple, plain-English coding rules (written for "John") — load only for Python files | ⭐ new |
| `.github/instructions/tests.instructions.md` | Rules for `tests/**` only | ⭐ new |
| `requirements/BRD-PayLite.md` | The business rules the instructions cite | context |

> Open `python-style.instructions.md` — notice it is written in plain English for a teammate named
> John, with no Python jargon. Instructions should be readable by the whole team, not just coders.

## How to run the demo (~15 min)

1. **Before/after — this sells the feature.** Open a *new* Copilot Chat, Agent mode, and ask:
   > Create a single-file FastAPI app with one endpoint returning a hardcoded list of payments.
   Note what it guesses (naming, structure). **Discard the edits.**
2. Read `.github/copilot-instructions.md` with the room — these are *their* standards.
3. Open a **fresh chat** and repeat the exact prompt. Watch it now obey the rules.
4. The kicker — ask: **"Explain what FastAPI is."** It answers with Pega analogies, because the
   instructions told it the audience is a Pega team.
5. Open the **chat debug view** (`Ctrl+Shift+P` → *Developer: Show Chat Debug View*) → show the
   instructions file sitting inside the request. Say: *"You pay these tokens on every request."*

## What to point out

- **Repo-wide vs scoped:** repo-wide is always loaded; `applyTo:` files load only for matching
  files — your first taste of paying for context only when you need it.
- Instructions **ask** the model to behave. (On `Day2-Demo4-Hooks` you'll see what *enforces* it.)

## Next

→ `git checkout Day1-Demo2-Markitdown`
