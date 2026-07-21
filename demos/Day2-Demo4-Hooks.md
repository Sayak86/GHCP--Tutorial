# This stop: Hooks

**Concept in one line:** hooks are *your scripts, run deterministically by the harness* at fixed
lifecycle points — instructions **ask** the model to behave; hooks **make** it.

Events: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`,
`SubagentStart`, `SubagentStop`, `Stop`. A `PreToolUse` hook can **deny** a tool call outright.

## What just appeared at this stop

| File | What it does |
|---|---|
| `.github/hooks/payguard.json` | Wires two hooks: PreToolUse guard + PostToolUse audit |
| `scripts/hooks/protect_files.py` | Denies any mutating tool call touching `data/seed_payments.json`, `inputs/`, `.env` — returns the official deny JSON |
| `scripts/hooks/audit_log.py` | Appends every tool call to `.copilot-audit.log` (timestamped audit trail — the governance story) |

## Try it (2 minutes)

1. In Agent mode: **"Add a test payment of 50 USD to data/seed_payments.json."**
   → the hook denies the edit; Copilot reports it was blocked and why.
2. Look at `.copilot-audit.log` afterwards — every tool call of your session, timestamped.
3. No VS Code needed to understand the script:
   ```bash
   echo '{"tool_name":"editFiles","tool_input":{"filePath":"data/seed_payments.json"}}' | python scripts/hooks/protect_files.py
   ```

> Preview feature: check Settings for hook flags (e.g. `chat.useCustomAgentHooks` for agent-scoped
> hooks); org policy can disable hooks entirely. Rehearse on your build.

## Teach it

Live script: `docs/03-day2-runbook.md`, Demo 4. Keep the punchline for Demo 5: this exact hook is
about to catch a prompt-injection attack.

**See exactly what this demo added:** `git diff Day2-Demo3-SubagentsHandoffs..Day2-Demo4-Hooks --stat`
