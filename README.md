# Day 2 · Demo 3 — Subagents & Handoffs

**GHCP constituents:** handoffs and subagents.

## 🌱 Simplest version first — agent vs handoff vs subagent

You already know **agents** (Demo 1): a Copilot with a job title. Now two ways to make agents work
*together*. Use this everyday-office picture:

- **Handoff = passing a folder to the next desk, in person.** The architect finishes the plan, then
  a button appears: *"Hand off to developer."* You (the human) click it, and the same conversation
  continues at the developer's desk with the plan already pasted in. **You are in the room for every
  pass.** You see everything.

- **Subagent = a manager delegating to an assistant in another room.** The manager (an agent called
  `delivery-lead`) sends a small job to an assistant (the `developer` agent) working **in a separate
  room**. The assistant does the work privately and comes back with a **one-paragraph summary**. The
  manager never sees the assistant's messy desk — just the result.

Side-by-side:

| | Handoff | Subagent |
|---|---|---|
| Who moves the work | **you** click a button | an **agent** delegates automatically |
| Same conversation? | yes — one continuous thread | no — the subagent works in its own private thread |
| What comes back | the whole conversation continues | only a short **summary** |
| Human in the loop | at every step | at the start and the end |
| Office picture | passing a folder desk to desk | a manager assigning work to an assistant |

**Rule of thumb:** handoffs keep *you* driving between stages; subagents let *one agent* run a small
team and report back. Both keep the main conversation clean.

## Dependencies

**Assumes `Day2-Demo1-CustomAgents` — this lesson EXTENDS those agents.** The five role agents are
carried over and now have `handoffs:` added, plus a new `delivery-lead` agent that uses subagents.
Also carried from `Day1-Demo4`: the PayLite app + instructions.

> Compare an agent file here with the same file on `Day2-Demo1` to see exactly what a handoff adds —
> it is just a few lines at the top of the file.

## What's in this branch

| File | Change vs Day2-Demo1 | New / carried |
|---|---|---|
| `.github/agents/architect.agent.md` | + a **handoff** button → developer | extended |
| `.github/agents/developer.agent.md` | + a **handoff** button → tester | extended |
| `.github/agents/tester.agent.md` | + a **handoff** button → scrum-master | extended |
| `.github/agents/ba.agent.md`, `scrum-master.agent.md` | unchanged | carried |
| `.github/agents/delivery-lead.agent.md` | **the subagent manager** — see below | ⭐ new |
| `app/`, `data/`, `tests/`, `.github/copilot-instructions.md` | the app + standards | carried from D1·4 |

### What `delivery-lead.agent.md` actually is (read this before class)

Open the file. Two lines make it a manager:

```yaml
tools: ['agent']                      # "you are allowed to call other agents"
agents: ['developer', 'tester']       # "these are the assistants you may call"
```

That's the whole trick. `delivery-lead` writes no code itself. When you give it a job, it calls the
`developer` agent to build, waits for the summary, then calls the `tester` agent to verify, waits
for that summary, and finally tells **you** what happened. Each assistant runs in its own private
room, so the delivery-lead's conversation stays short and readable.

## How to run the demo (~25 min)

### Part A — Handoffs (the human-driven pipeline)
1. Pick the **architect** agent, ask it to plan *"reject a pending payment with a mandatory reason"*.
2. When it finishes, a **handoff button** appears. Click it → you're now at the **developer**, plan
   pre-filled. Let it build. → its button → **tester** verifies. → its button → **scrum-master**
   writes the summary.
3. Narrate: *requirement → plan → code → tests → report, four desks, and I clicked the button
   between each one.*

### Part B — Subagent ("Deliver 'add a currency filter to search'")
1. Pick the **delivery-lead** agent and type exactly:
   > Deliver "add a currency filter to search": have the developer implement it, then the tester
   > verify it. Report what each did.
2. **What is happening on screen:** delivery-lead reads the request, decides "this is build + verify."
   It calls the **developer** subagent with a small brief ("add a `currency=` filter to
   `/payments/search`"). The developer works privately and returns a summary. delivery-lead then
   calls the **tester** subagent ("check the new currency filter"), gets its summary, and finally
   prints one combined report to you. You did **not** click between steps — the manager handled it,
   and you only see the two summaries, not the two private conversations.
3. In plain words for the room: *"'Deliver add a currency filter' means: one agent just ran a
   two-person team for me and handed me the result."*

## What to point out

- Pega frame: **handoff** = a stage change that routes the assignment to the next persona's worklist;
  **subagent** = spinning off a subcase and getting the resolution back.
- Subagents keep the manager's context short — which also keeps token cost down (see token economics).

## Next

→ `git checkout Day2-Demo4-Hooks`
