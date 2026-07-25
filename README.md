# Day 2 · Demo 2 — Skills

**GHCP constituent:** skills (knowledge on demand).

## 🌱 Simplest version first

A skill is a **reference binder on the shelf** that Copilot only pulls down when the topic comes up.
Compare:
- **Instructions** = the fridge note, read **every** time (so you pay for it every time).
- **Skill** = a binder that sits quietly until a matching question appears, then Copilot opens it.

So deep knowledge goes in **skills** (opened only when relevant), not in one giant instructions file
(paid on every request).

**In one line:** a skill is knowledge Copilot loads only when the task matches it.

## Dependencies

**Assumes `Day1-Demo4-AgentBuild`.** Carried over: the PayLite app and instruction files (the skills
answer questions about this code). **Independent of `Day2-Demo1` (Custom Agents)** — plain chat is
enough.

## What's in this branch

| File | Kind | Knows | New / carried |
|---|---|---|---|
| `.github/skills/payments-domain/SKILL.md` (+ `references/`) | knowledge | currencies, limits, full status-transition matrix | ⭐ new |
| `.github/skills/explain-like-pega/SKILL.md` | style | how to explain Python/FastAPI to THIS team | ⭐ new |
| `.github/skills/release-notes/SKILL.md` | procedure | steps + house style for release notes | ⭐ new |
| **`EXERCISE.md`** | 🛠️ hands-on | **the 20-minute task the class builds themselves** | ⭐ new |
| `app/`, `data/`, `tests/`, `.github/copilot-instructions.md` | — | the app + standards | carried from D1·4 |

## How to run the demo (~20 min showing + 20 min class exercise)

**You show the examples (~15 min):**
1. Ask: **"Can a SETTLED payment be rejected? Answer from the domain rules."** → the answer cites the
   lifecycle from `payments-domain` (open the chat debug view to watch the skill body get loaded).
2. **The crowd-pleaser:** **"Explain app/store.py to me."** → the explanation arrives in
   data-page / case vocabulary, courtesy of `explain-like-pega`.
3. **"Prepare release notes for the PayLite pilot."** → the `release-notes` procedure kicks in.

**Then the class builds their own (~20 min):** open **`EXERCISE.md`** and hand it to the room. They
build a brand-new *payment-investigation* skill (cancel a payment, or send a SWIFT message) — a
domain they know cold from Pega. Review a few at the end.

## What to point out

- Instructions are paid on every request; skills are paid only when used. That's *why* deep
  knowledge belongs in skills.

## Next

→ `git checkout Day2-Demo3-SubagentsHandoffs`
