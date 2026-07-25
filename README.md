# Day 2 · Demo 4 — Hooks

**GHCP constituent:** hooks.

## 🌱 Simplest version first

A hook is **your own little script that the agent runs automatically at a fixed moment.** Think of a
motion-sensor light: at a known moment (someone walks past), a thing you set up (the light) runs on
its own. You don't press anything.

The agent's work has known moments in its loop — "a session just started", "about to use a tool",
"just finished a tool". A hook says: *"at THIS moment, run MY script."*

**The two levels of hook, simplest first:**
1. **Announce (just print).** The script only prints what's happening. It decides nothing. This is
   the Hello-World hook — start here.
2. **Guard (make a decision).** The script looks at what's about to happen and can say **"no, block
   that."** Same idea, plus a decision.

**The line to remember:** instructions *ask* the model to behave; hooks *make* it — with a receipt.

## The moments you can hook (the events)

A hook's JSON file maps an **event name** to a **command to run**. These are the eight events:

| Event | Fires when… |
|---|---|
| `SessionStart` | a new chat/agent session begins |
| `UserPromptSubmit` | you send a message |
| `PreToolUse` | the agent is **about to** use a tool (edit a file, run a command) |
| `PostToolUse` | the agent **just finished** using a tool |
| `PreCompact` | the conversation is about to be summarized to save space |
| `SubagentStart` / `SubagentStop` | a subagent begins / ends |
| `Stop` | the session ends |

`PreToolUse` is the powerful one: a script there can **allow, ask, or deny** the tool call.

## Dependencies

**Assumes `Day1-Demo4-AgentBuild`.** Carried over: the PayLite app (the guard protects
`data/sample_payments.json`) and the instruction files. **Independent of the agents/skills lessons.**

## What's in this branch

| File | Level | Does | New / carried |
|---|---|---|---|
| `.github/hooks/announce.json` | 1 · announce | Wires `announce_event.py` to 3 events | ⭐ new (Hello-World) |
| `scripts/hooks/announce_event.py` | 1 · announce | **Only prints** the event + tool. Decides nothing. | ⭐ new (Hello-World) |
| `.github/hooks/payguard.json` | 2 · guard | Wires the guard + the audit log | ⭐ new |
| `scripts/hooks/protect_files.py` | 2 · guard | **Denies** any edit to `data/sample_payments.json`, `inputs/`, `.env` | ⭐ new |
| `scripts/hooks/audit_log.py` | 2 · guard | Writes every tool call to `.copilot-audit.log` | ⭐ new |
| **`EXERCISE.md`** | 🛠️ | **the 20-minute task the class builds themselves** | ⭐ new |
| `app/`, `data/`, `.github/copilot-instructions.md` | — | the app to protect + standards | carried from D1·4 |

## How to run the demo (~20 min showing + 20 min class exercise)

**Start simple — the announce hook (~5 min).** Show `announce_event.py`: it just prints. Run it by
hand so nobody is scared of it:
```bash
echo '{"hook_event_name":"PreToolUse","tool_name":"editFiles"}' | python scripts/hooks/announce_event.py
```
→ prints `[announce] lifecycle event = PreToolUse | tool = editFiles`. Say: *"That's a hook. The
harness will run this for real at that moment. It changed nothing — it just told us what happened."*

**Then the guard (~10 min).** Walk through `protect_files.py` (it's the announce idea plus a
decision). Prove it:
```bash
echo '{"tool_name":"editFiles","tool_input":{"filePath":"data/sample_payments.json"}}' | python scripts/hooks/protect_files.py
```
→ prints the deny JSON. Then in Agent mode: **"Add a test payment of 50 USD to
data/sample_payments.json."** → the hook denies the edit; Copilot reports it was blocked. Open
`.copilot-audit.log` — every tool call, timestamped. *"Show this to your security officer."*

**Then the class builds their own (~20 min):** hand out **`EXERCISE.md`** — they write a simple
announce-style hook of their own and watch it fire. The goal is *seeing the harness run their script
at a lifecycle event*, not fancy logic.

## What to point out

- Preview feature: check Settings (e.g. `chat.useCustomAgentHooks`); org policy can disable hooks.
- Keep the punchline for the next lesson: this exact guard is about to block a real attack.

## Next

→ `git checkout Day2-Demo5-PromptInjection`
