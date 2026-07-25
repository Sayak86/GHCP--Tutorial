# Copilot Chat Cheat Sheet — #, /, @, modes, debug view

Print this or keep it on the second screen. Note: the exact lists evolve with every VS Code release —
typing `#`, `/`, or `@` in the chat box always shows the live list on YOUR build. Teach that habit
first; the tables below are the stable core.

## Modes

| Mode | What it may do | Use when |
|---|---|---|
| **Ask** | Answer only, touches nothing | learning, exploring, reviews |
| **Edit** | Propose edits to files you select | surgical multi-file changes |
| **Agent** | Plan, edit, run commands, iterate | features, refactors, anything multi-step |

## `#` — context variables & tools (the most important column in this file)

| Mention | Attaches |
|---|---|
| `#file` (or drag a file in) | one file — the precision tool, cheapest good context |
| `#codebase` | search over the whole workspace — powerful, token-heavy |
| `#selection` / `#editor` | current selection / visible editor |
| `#changes` | current git diff — gold for reviews and sprint summaries |
| `#problems` | the Problems panel (errors/warnings) |
| `#testFailure` | last test failure details |
| `#terminalSelection` / `#terminalLastCommand` | terminal context for "why did this fail" |
| `#fetch <url>` | fetch a web page as context — **treat as untrusted input** (see doc 07) |
| `#githubRepo owner/repo` | search another GitHub repo |
| `#usages` | references/implementations of a symbol |
| `#extensions` | search/ask about VS Code extensions |
| `#new` | scaffold a new project/workspace |

> Trainer note: attendees often ask about a specific `#tool` they saw in a blog (the set is
> extensible — MCP servers and extensions add more). Demo: type `#` and scroll; then open the
> tools picker (gear icon in agent mode) to show/enable/disable the full tool set.

## `/` — slash commands

| Command | Does |
|---|---|
| `/explain` | explain selection/file |
| `/fix` | propose a fix |
| `/tests` | generate tests |
| `/doc` | add documentation comments |
| `/new` | scaffold project |
| `/clear` | new chat — **fresh context, fresh token budget** |
| `/<your-prompt-file>` | run a team prompt file — the point of Day 1 Demo 3 |

## `@` — participants

| Participant | Ask it about |
|---|---|
| `@workspace` | your code (Ask mode's codebase expert) |
| `@terminal` | shell commands, errors |
| `@vscode` | VS Code itself, settings |
| `@github` | issues/PRs/repos (when the GitHub integration is enabled) |

## Chat debug view (the X-ray)

- Open: `Ctrl+Shift+P` → **Developer: Show Chat Debug View**.
- Inspect per request: system prompt · instruction files attached · skills loaded · tools offered ·
  conversation history · payload sizes.
- Use in training at three moments: orientation ("look how much you actually send"), after adding
  instructions ("there's our file, on every request"), and in the token-economics close ("this is
  what a heavy turn costs").

## Ten habits to project on the wall at the end

1. New chat per task (`/clear`) — history is paid context.
2. Know the file? `#file` it. Don't make `#codebase` guess.
3. Write it once, run it forever: prompt files for recurring asks.
4. Conventions → instructions. Knowledge → skills. Recipes → prompts. Roles → agents.
5. Give agents only the tools their job needs.
6. Review every diff. You are the merge gate, not Copilot.
7. Hooks on anything you'd never want an AI to touch.
8. External content (`#fetch`, vendor docs) is input, never instructions.
9. Watch the model multiplier; plan cheap, build strong.
10. When Copilot surprises you — open the debug view before blaming the model.
