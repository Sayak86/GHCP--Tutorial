# 🛠️ Your turn (20 minutes) — write your own simple hook

You have seen two hooks in this branch:
- `announce.json` + `announce_event.py` — the **Hello-World** hook that only *prints* what happens.
- `payguard.json` + `protect_files.py` — the **real guard** that *blocks* edits to protected files.

Now build a small hook of your own. **Start from the announce example**, not the guard.

## Pick one (both are easy)

- **Option A — A friendly greeting hook.** On `SessionStart`, print a welcome line like
  `Welcome to PayLite. Remember: review every diff before you keep it.`
- **Option B — A "watcher" hook.** On every `PreToolUse`, print the tool name and the file it is
  about to touch (read it out of the event JSON), so you can watch the agent work.

You are only *printing*. You are **not** blocking anything (that is what the guard already does).

## Steps

1. Copy `scripts/hooks/announce_event.py` to `scripts/hooks/my_hook.py` and edit the `print(...)`
   line to say what you want. (For Option B, also pull the file path out of the event JSON —
   look at how `announce_event.py` reads fields.)
2. Create `.github/hooks/my_hook.json` that wires your script to the event you chose:
   ```json
   {
     "hooks": {
       "SessionStart": [
         { "type": "command", "command": "python scripts/hooks/my_hook.py" }
       ]
     }
   }
   ```
   (Swap `SessionStart` for `PreToolUse` if you picked Option B.)
3. **Test it without VS Code** first — feed the script a fake event and see your line print:
   ```bash
   echo '{"hook_event_name":"PreToolUse","tool_name":"editFiles"}' | python scripts/hooks/my_hook.py
   ```
4. Then start a Copilot session / ask the agent to do something small, and watch your hook fire.

## The point (this matters more than the code)

The lesson is **seeing the harness map your script to a lifecycle event**. When your line prints,
you have proved: *the agent, at a known moment in its loop, ran my code and handed it a description
of what it was doing.* Everything fancy (blocking, auditing, auto-formatting) is just that same
idea plus a decision.

## The eight lifecycle events you can hook

`SessionStart` · `UserPromptSubmit` · `PreToolUse` · `PostToolUse` · `PreCompact` ·
`SubagentStart` · `SubagentStop` · `Stop`. Try wiring your print to two different ones and watch
when each fires.
