# GHCP Hands-On Training — PayLite Payments API

**A 2-day (4 hours/day) instructor-led, hands-on training on GitHub Copilot (GHCP) in VS Code, built around one simple payments use case.**

> **Lost, or first time here?** Read [`docs/00-navigation.md`](docs/00-navigation.md) (2 minutes),
> then move around the course with `python go.py` — no git knowledge needed.

This repository is the **trainer's kit**. It is not a software project to run in production — it is a
teaching vehicle. Every file exists to demonstrate one GitHub Copilot capability. The audience is a
**Pega team** (expert in payments, new to Python/open-source), so every concept is anchored in a
payments scenario and mapped to Pega vocabulary where it helps.

---

## 1. What you will teach

How GitHub Copilot supports the **whole SDLC** — not just code completion — across five roles:

| Role | What they do with GHCP in this training |
|---|---|
| **Business Analyst** | Convert a Word BRD to markdown (MarkItDown), generate user stories & acceptance criteria |
| **Architect** | Encode team standards as *instructions*, plan features with a planning-only *agent* |
| **Developer** | Build the API in *agent mode*, use reusable *prompt files*, receive *handoffs* |
| **Tester** | Generate test plans and pytest tests with a *tester agent* |
| **Scrum Master** | Sprint summaries and release notes from git history via prompts and a *skill* |

And **every GHCP constituent** is covered, each with a live demo:

| Constituent | Where it lives | Demo |
|---|---|---|
| Agent harness (the loop) | concept | Day 1 opening |
| Custom instructions | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` | Day 1 · Demo 1 |
| Prompt files | `.github/prompts/*.prompt.md` | Day 1 · Demo 3 |
| Agent mode | built into Copilot Chat | Day 1 · Demo 4 |
| Custom agents | `.github/agents/*.agent.md` | Day 2 · Demo 1 |
| Skills | `.github/skills/<name>/SKILL.md` | Day 2 · Demo 2 |
| Subagents & handoffs | `agents:` / `handoffs:` in agent files | Day 2 · Demo 3 |
| Hooks | `.github/hooks/*.json` + scripts | Day 2 · Demo 4 |
| Prompt injection (safety) | `inputs/poisoned/` | Day 2 · Demo 5 |
| Chat debug view & token economics | VS Code built-in | Day 1 opening + Day 2 closing |

---

## 2. The use case: PayLite

A deliberately tiny **payments API** (Python + FastAPI, in-memory storage, zero frameworks beyond
FastAPI). The team knows payments deeply, so all their attention goes to *Copilot*, not the domain.

- `POST /payments` — create a payment
- `GET /payments/{id}` — fetch one payment
- `GET /payments/search` — search by status / beneficiary / amount
- `POST /payments/{id}/authorize` — move PENDING → AUTHORIZED

Full definition, business rules, and the **Pega-to-Python translation table**: [`docs/01-use-case.md`](docs/01-use-case.md).

> **Important:** you never need to *run* this project during training (though you can). The point is
> watching Copilot **produce and reason about** these artifacts, not executing them.

---

## 3. How this repo is organized

```
README.md                      ← you are here (trainer master guide)
docs/
  01-use-case.md               ← PayLite spec + Pega analogy table
  02-day1-runbook.md           ← minute-by-minute Day 1 script with exact prompts
  03-day2-runbook.md           ← minute-by-minute Day 2 script with exact prompts
  04-ghcp-concepts.md          ← glossary: every constituent, its file, when to use it
  05-cheatsheet.md             ← #-variables, /-commands, @-participants, chat debug view
  06-token-economics.md        ← premium requests, context budget, cost habits
  07-prompt-injection.md       ← the attack demo, step by step, + mitigations
inputs/
  BRD-PayLite.docx             ← Word BRD used in the MarkItDown demo
  poisoned/                    ← files for the prompt-injection demo (harmless payloads)
requirements/                  ← BA outputs: converted BRD + user stories (reference results)
.github/
  copilot-instructions.md      ← repo-wide instructions (reference result of Day 1 Demo 1)
  instructions/                ← scoped instructions (*.instructions.md)
  prompts/                     ← reusable prompt files (*.prompt.md)
  agents/                      ← role agents (*.agent.md) with subagents & handoffs
  skills/                      ← three skills (SKILL.md folders)
  hooks/                       ← hook config (payguard.json)
scripts/hooks/                 ← the Python scripts the hooks execute
app/ · tests/ · data/          ← the tiny PayLite API (reference result of Day 1 Demo 4)
```

### The branch model — your safety net

Every demo is **built live from scratch with the audience** — that is the whole pedagogy. The
branches exist so that (a) you can rehearse, (b) if a live demo goes sideways you `git checkout` the
finished state and keep talking, and (c) attendees can diff branches afterwards to replay the course.

The repo is **one straight line of commits** — one commit per demo. Each branch is simply a
bookmark on that line: **the repo state at the END of that demo**. Branches are therefore
cumulative (`Day1-Demo3-…` contains everything from Demos 1–2 as well). You *teach* on a single
clone starting from `Day1-Start` and build everything live; the demo branches are only your
rehearsal copies and your parachute.

| Branch | State |
|---|---|
| `Day1-Start` | **start here on the projector**: docs + BRD only — no customizations, no code |
| `Day1-Demo1-Instructions` | custom instructions added |
| `Day1-Demo2-Markitdown` | + BRD converted, user stories generated |
| `Day1-Demo3-PromptFiles` | + four reusable prompt files |
| `Day1-Demo4-AgentBuild` | + PayLite API and tests built in agent mode |
| `Day2-Demo1-CustomAgents` | + five role agents |
| `Day2-Demo2-Skills` | + three skills |
| `Day2-Demo3-SubagentsHandoffs` | + handoffs wired, delivery-lead orchestrator |
| `Day2-Demo4-Hooks` | + guardrail & audit hooks |
| `Day2-Demo5-PromptInjection` | + poisoned files (final state, same as main working branch) |

---

## 4. Trainer prep checklist (do this the week before)

1. **VS Code** — latest stable. Several features (custom agents, skills, hooks, handoffs) are recent
   and some are *Preview*: open Settings and search **"agent"**, **"skills"**, **"hooks"** and enable
   what your build gates behind a flag (e.g. `chat.useCustomAgentHooks` for agent-scoped hooks).
   **Rehearse on the exact VS Code version you'll present with** — these features evolve monthly.
2. **Copilot subscription** with access to premium models (you'll show the model picker and
   multipliers — see [`docs/06-token-economics.md`](docs/06-token-economics.md)).
3. **Python 3.11+** and:
   ```bash
   pip install -r requirements.txt
   pip install "markitdown[all]"
   ```
4. **Clone this repo twice**:
   - **Clone A (projector, live building):** `git checkout Day1-Start`. This is your workspace
     for both days — everything is created live on top of it. On Day 2 morning, either continue
     on it, or `git checkout Day1-Demo4-AgentBuild` for a guaranteed-clean Day 2 starting line.
   - **Clone B (second screen, reference):** `git checkout Day2-Demo5-PromptInjection` — the
     finished state, so you can peek at any "solution" file without touching the projector.
   - If a live demo stalls: on Clone A, stash/discard and `git checkout <that demo's branch>` —
     the room sees the finished state and you keep talking.
5. Read the two run-books end to end once. Every prompt you will type is written out verbatim —
   you can literally present from them.
6. Test the MarkItDown conversion once: `markitdown inputs/BRD-PayLite.docx > /tmp/brd.md`.

---

## 5. Agenda at a glance

**Day 1 — Foundations: from a Word BRD to a working API** ([full run-book](docs/02-day1-runbook.md))

| Time | Block |
|---|---|
| 00:00–00:30 | Orientation: the agent harness, Ask/Edit/Agent modes, models, chat debug view |
| 00:30–01:15 | **Demo 1 — Custom instructions** (Architect) |
| 01:15–01:25 | Break |
| 01:25–02:10 | **Demo 2 — MarkItDown + BA workflow** (BRD → stories) |
| 02:10–02:55 | **Demo 3 — Prompt files** (reusable prompts per role) |
| 02:55–03:05 | Break |
| 03:05–03:50 | **Demo 4 — Agent mode**: build PayLite + tests |
| 03:50–04:00 | Recap + Q&A |

**Day 2 — Scaling up: agents, skills, guardrails, economics** ([full run-book](docs/03-day2-runbook.md))

| Time | Block |
|---|---|
| 00:00–00:15 | Day 1 recap quiz |
| 00:15–01:00 | **Demo 1 — Custom agents** (one per role) |
| 01:00–01:40 | **Demo 2 — Skills** (incl. the crowd-pleaser: *explain-like-pega*) |
| 01:40–01:50 | Break |
| 01:50–02:35 | **Demo 3 — Subagents & handoffs** (the SDLC pipeline) |
| 02:35–03:10 | **Demo 4 — Hooks** (guardrails + audit trail) |
| 03:10–03:35 | **Demo 5 — Prompt injection** (attack, then watch the hook block it) |
| 03:35–03:55 | Token economics + chat debug view deep dive |
| 03:55–04:00 | Wrap-up + adoption checklist |

---

## 6. Ground rules you'll repeat all session

- **Copilot output is a draft, not a decision.** Humans review every diff. (Sets up the injection demo.)
- **Context is the product.** Good instructions + right #-mentions beat clever prompt wording.
- **Small asks, verified often** beat one giant ask.
- **Tokens are money.** Every always-on instruction file is paid on every request — skills load on
  demand, which is exactly why they exist. ([details](docs/06-token-economics.md))
