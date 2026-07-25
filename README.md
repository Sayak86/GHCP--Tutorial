# Day 2 · Demo 1 — Custom Agents

**GHCP constituent:** custom agents (personas).

## 🌱 Simplest version first

A custom agent is **a Copilot with a job title and only the keys its job needs.** Give someone the
"architect" badge and they can look but not edit. Give someone the "developer" badge and they can
edit and run code. Same building, different door keys.

**In one line:** an agent = a saved persona (a standing prompt) + a limited set of tools it's
allowed to use.

**Why the limited tools matter:** an agent with no "edit" key **cannot change files** — not even if
you ask it to, not even if a sneaky document tells it to. That's real safety, not a polite request.

## Dependencies

**Assumes `Day1-Demo4-AgentBuild`.** Carried over: the PayLite app (`app/`, `data/`, `tests/`) and
the instruction files — the agents operate on this code.

## What's in this branch

| File | Persona | May edit files? | New / carried |
|---|---|---|---|
| `.github/agents/architect.agent.md` | plans & designs | ✖ read-only | ⭐ new |
| `.github/agents/ba.agent.md` | stories & grooming | only `requirements/` | ⭐ new |
| `.github/agents/developer.agent.md` | implements | ✔ full toolbelt | ⭐ new |
| `.github/agents/tester.agent.md` | writes/runs tests | only `tests/` | ⭐ new |
| `.github/agents/scrum-master.agent.md` | status & summaries | ✖ read-only | ⭐ new |
| `app/`, `data/`, `tests/`, `.github/copilot-instructions.md` | the app + standards | — | carried from D1·4 |

> These agents have **no handoffs** yet — that's added in `Day2-Demo3-SubagentsHandoffs`.

## How to run the demo (~20 min)

1. Open `.github/agents/architect.agent.md` — the top part lists its tools; the rest is its
   standing prompt (its "job description").
2. In chat, open the agent dropdown, pick **architect**, ask:
   > Plan "cancel a pending payment". Do not write code.
3. Now try to make it break its role: *"just edit app/main.py yourself"* → it can't; it has no edit
   key. **That's the demo moment** — the limit is real.
4. Switch to **tester** and: *"Write tests for search filters (status + min_amount combined)."*

## What to point out

- Pega frame: personas / portals — each sees only the tools of its job.
- Tool names vary by VS Code build; the gear icon (tools picker) shows the exact ones yours has.

## Next

→ `git checkout Day2-Demo2-Skills`
