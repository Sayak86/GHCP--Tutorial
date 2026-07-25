# GitHub Copilot Hands-On Training — PayLite (Trainer Hub)

**A 2-day (4 hrs/day) instructor-led, hands-on course teaching GitHub Copilot (GHCP) in VS Code to a
Pega team, built around one tiny payments API called PayLite.**

You are on the **`main` branch — the hub**. Read this page first. It tells you what the course
covers, how the branches are organized, and how to move through them. Every *lesson* lives on its
own branch with its own README.

---

## How this repository works (read this once)

- **`main`** (here) = overview + the reference docs in `docs/`. No demo code lives here.
- **Each lesson is a separate branch.** You `git checkout` a lesson branch and that branch is
  **self-contained**: it holds everything that lesson needs and a **README.md that explains it in
  simple terms** — starting with a "🌱 Simplest version first" analogy before any PayLite detail.
- **Branches are never merged.** They are independent snapshots, not a running codebase.
- **Dependencies are handled by copying.** If a lesson builds on an earlier one, the earlier files
  are already copied in — you never assemble anything by hand. Each README's **Dependencies**
  section names the lesson to teach first and what was carried over.
- **Two lessons include a `EXERCISE.md`** — a 20-minute task the class does themselves, then you
  review (Skills and Hooks).

To teach a lesson: `git checkout <branch>` → open its `README.md` → follow it.

---

## The use case: PayLite

A deliberately tiny payments API (Python + FastAPI, in-memory storage). Your team already knows
payments deeply, so all attention goes to Copilot, not the domain. Four operations: create a
payment, fetch one, search transactions, authorize (PENDING → AUTHORIZED). Full spec, business
rules, and the **Pega-to-Python translation table**: [`docs/01-use-case.md`](docs/01-use-case.md).

> You never need to *run* the app to teach. The point is watching Copilot **produce and reason
> about** these artifacts.

---

## The lessons (branches) and their dependencies

Read top to bottom — it's the teaching order. "Depends on" means: teach that lesson first (its files
are already carried over for you).

| # | Branch | GHCP constituent | Depends on | Class exercise? |
|---|---|---|---|---|
| D1·1 | `Day1-Demo1-Instructions` | Custom instructions | — (start here) | |
| D1·2 | `Day1-Demo2-Markitdown` | MarkItDown + BA workflow | D1·1 | |
| D1·3 | `Day1-Demo3-PromptFiles` | Prompt files (`/commands`) | D1·1, D1·2 | |
| D1·4 | `Day1-Demo4-AgentBuild` | Agent mode **and Plan mode** builds the API | D1·1, D1·2 | |
| D2·1 | `Day2-Demo1-CustomAgents` | Custom agents (personas) | D1·4 | |
| D2·2 | `Day2-Demo2-Skills` | Skills (knowledge on demand) | D1·4 (indep. of D2·1) | 🛠️ `EXERCISE.md` |
| D2·3 | `Day2-Demo3-SubagentsHandoffs` | Subagents & handoffs | **D2·1**, D1·4 | |
| D2·4 | `Day2-Demo4-Hooks` | Hooks (guardrails + audit) | D1·4 | 🛠️ `EXERCISE.md` |
| D2·5 | `Day2-Demo5-PromptInjection` | Prompt injection (safety) | **D2·4**, D1·4 | |

Two dependency chains worth noting: **D2·3 extends the agents from D2·1** (handoffs are added to
them), and **D2·5 relies on the guard hook from D2·4** to block the attack live. Everything else only
needs the PayLite app from D1·4.

---

## What each GHCP constituent is (one line each)

| Constituent | Lesson | One line (the simple version) |
|---|---|---|
| Custom instructions | D1·1 | A fridge note every chat reads |
| Prompt files | D1·3 | A saved message you run with `/name` |
| Plan mode | D1·4 | Writes the recipe, changes nothing |
| Agent mode | D1·4 | Actually cooks: edits, runs, fixes, repeats |
| Custom agents | D2·1 | A Copilot with a job title and limited keys |
| Skills | D2·2 | A binder opened only when the topic comes up |
| Subagents & handoffs | D2·3 | A manager delegating vs passing a folder desk-to-desk |
| Hooks | D2·4 | Your script auto-runs at a set moment (motion-sensor light) |
| Prompt injection | D2·5 | Hidden instructions inside something the agent reads |

Deep reference for all of them: [`docs/04-ghcp-concepts.md`](docs/04-ghcp-concepts.md).

---

## The reference library on this branch (`docs/`)

| File | For |
|---|---|
| [`01-use-case.md`](docs/01-use-case.md) | PayLite spec + Pega translation table |
| [`02-day1-runbook.md`](docs/02-day1-runbook.md) | Full minute-by-minute Day 1 script |
| [`03-day2-runbook.md`](docs/03-day2-runbook.md) | Full minute-by-minute Day 2 script |
| [`04-ghcp-concepts.md`](docs/04-ghcp-concepts.md) | Glossary of every constituent + file locations |
| [`05-cheatsheet.md`](docs/05-cheatsheet.md) | `#` / `/` / `@` reference + chat debug view |
| [`06-token-economics.md`](docs/06-token-economics.md) | **Credits / AIC**, context budget, cost habits |
| [`07-prompt-injection.md`](docs/07-prompt-injection.md) | The attack demo, step by step, + mitigations |

The per-branch READMEs give the focused "how to run *this* demo" steps; the run-books above are the
fuller trainer scripts for prep.

---

## Trainer prep checklist (do the week before)

1. **VS Code**, latest stable. Some features (custom agents, skills, hooks, handoffs, Plan mode) are
   recent and partly *Preview* — open Settings, search "agent", "skills", "hooks", enable what's
   gated (e.g. `chat.useCustomAgentHooks`). **Rehearse on the exact version you'll present with.**
2. **Copilot** subscription with premium-model access (you'll show the model picker + credit cost).
3. **Python 3.11+** and `pip install fastapi uvicorn pytest httpx` plus `pip install "markitdown[all]"`.
4. **Clone the repo.** For each lesson: `git checkout <branch>`, read the README, rehearse once.
5. Read the two run-books here on `main` end to end once.

---

## Agenda at a glance

**Day 1 — from a Word BRD to a working API:** orientation (Ask/Plan/Agent modes, chat debug view) →
D1·1 Instructions → D1·2 MarkItDown/BA → D1·3 Prompt files → D1·4 Plan & Agent build.

**Day 2 — scaling up:** D2·1 Custom agents → D2·2 Skills (+ class exercise) → D2·3 Subagents &
handoffs → D2·4 Hooks (+ class exercise) → D2·5 Prompt injection → close on token economics.

## Ground rules you'll repeat all course

- Copilot output is a **draft**, not a decision — humans review every change.
- **Context is the product** — good instructions + the right `#`-mentions beat clever wording.
- **Small asks, verified often** beat one giant ask.
- **Credits are money** — always-on instructions are paid every request; skills load on demand.
