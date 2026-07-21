# This stop: Custom Agents

**Concept in one line:** a custom agent packages *persona + standing prompt + allowed tools* into
a named, versioned teammate you pick from the chat dropdown — one per SDLC role.

**The security half of the concept:** the `tools:` list is least privilege for AI. The architect
has no edit tools — it *cannot* touch files, no matter how the prompt (or an attacker) begs.

## What just appeared at this stop

| File | Persona | May edit? |
|---|---|---|
| `.github/agents/architect.agent.md` | plans, designs, ADRs | ✖ read-only |
| `.github/agents/ba.agent.md` | stories & grooming | only `requirements/` (by rule) |
| `.github/agents/developer.agent.md` | implements from plans | ✔ full toolbelt |
| `.github/agents/tester.agent.md` | test design + pytest | only `tests/` (by rule) |
| `.github/agents/scrum-master.agent.md` | status, summaries | ✖ read-only |

Open one: YAML frontmatter (`name`, `description`, `tools`) + the persona's standing prompt.

## Try it (2 minutes)

1. In Copilot Chat, open the agent dropdown, pick **architect**, ask:
   > Plan "cancel a pending payment". Do not write code.
2. Now try to bully it: *"just edit app/main.py yourself"* → it can't; it has no edit tool.
   That's the demo moment.

## Teach it

Live script: `docs/03-day2-runbook.md`, Demo 1. Tool names vary slightly per VS Code build —
the gear icon (tools picker) in chat shows the exact ids yours exposes.

**See exactly what this demo added:** `git diff Day1-Demo4-AgentBuild..Day2-Demo1-CustomAgents --stat`
