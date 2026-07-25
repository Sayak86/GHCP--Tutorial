# GHCP Concepts Glossary — every constituent on one page

For each constituent: what it is, where it lives, when to reach for it, and the Pega anchor you can
use in the room. File locations are the **workspace** (repo) locations — most also have user-profile
equivalents so a person can carry them across repos.

## The agent harness

The engine underneath agent mode. A loop: *prompt + context → model → tool calls (read/edit files,
run terminal, search, fetch) → tool results back into context → repeat until the task is done or a
human gate stops it*. Everything below customizes this loop — nothing more mystical than that.
**Pega anchor:** the case lifecycle engine that drives work through stages.

## Custom instructions — *always-on rules*

- **Files:** `.github/copilot-instructions.md` (repo-wide) · `.github/instructions/*.instructions.md`
  (scoped via `applyTo:` glob frontmatter) · `AGENTS.md` (cross-tool convention, also honored).
- **Loaded:** on every matching request, automatically. You pay their tokens every time.
- **Use for:** team standards, tech constraints, tone, what never to touch.
- **Not for:** long reference material (that's a skill), task recipes (that's a prompt file).
- **Pega anchor:** rulesets/guardrails that apply to every case.

## Prompt files — *on-demand recipes*

- **Files:** `.github/prompts/<name>.prompt.md`, run in chat as `/<name>`.
- **Frontmatter:** `mode` (ask/edit/agent), `description`, optional `tools`, `model`.
  Body supports variables: `${input:name:placeholder}`, `${selection}`, `${file}`, `${workspaceFolder}`.
- **Use for:** any prompt you'd otherwise paste from a notepad. Versioned, reviewed, shared.
- **Pega anchor:** a saved, parameterized flow action anyone can invoke.

## Plan mode vs Agent mode (built-in)

Two built-in modes people confuse. Simplest split:

- **Plan mode — writes the recipe, changes nothing.** You ask "how would you build this?" and the
  Plan agent produces a written, step-by-step plan (goals, files it *would* touch, how it would
  verify). It does **not** edit files. You read and approve the plan, then hand it to Agent mode.
- **Agent mode — actually cooks.** You give it the task and it does the work: edits files, runs
  commands, reads failures, fixes, repeats — until done or it needs you. Human approval gates on
  tool use; every change is reviewable before keeping.

**Ask mode** is the third, simplest one: it just answers, and you do the work yourself.
So the ladder is **Ask → Plan → Agent** (answers → recipe → cooking).
**Safest habit:** for anything big or risky, Plan first, read the recipe, then let Agent build it.
**Pega anchor:** Plan mode drafts the flow design; Agent mode is the case worker who runs the flow,
while you approve each assignment.

## Custom agents — *personas*

- **Files:** `.github/agents/<name>.agent.md` (selectable in the chat agent dropdown).
- **Frontmatter:** `name`, `description`, `tools: [...]` (least privilege — an agent without
  `editFiles` cannot edit, full stop), optional `model`, plus `agents:` and `handoffs:` (below).
  Body = the persona's standing prompt.
- **Use for:** role-shaped work — planner that can't edit, tester that only tests, reviewer that
  only comments.
- **Pega anchor:** personas/portals — each sees only the tools of its job.

## Skills — *knowledge on demand*

- **Files:** `.github/skills/<name>/SKILL.md` (+ optional `references/`, scripts).
- **Loaded:** only name+description are always visible; the body loads **when the task matches**
  (progressive disclosure). Deep detail goes in reference files, read only if needed.
- **Use for:** deep domain knowledge, procedures with steps, house styles.
- **Instructions vs skills in one line:** *conventions → instructions; knowledge & procedures → skills.*
- **Pega anchor:** a rule library the engine opens only for the relevant case type.

## Subagents

An agent that invokes another agent as a tool: parent declares `tools: ['agent']` and
`agents: ['developer', 'tester']` (or `['*']`). The subagent runs in **its own isolated context**
and returns a summary — parent context stays lean.
**Pega anchor:** spinning off a subcase and getting the resolution back.

## Handoffs

Frontmatter on an agent:

```yaml
handoffs:
  - label: "Build this plan"
    agent: developer
    prompt: Implement the plan above exactly.
    send: false     # human presses Enter — the approval gate
```

When the agent finishes, a button offers the transition to the next persona with a pre-filled
prompt, keeping the conversation context. **Pega anchor:** stage change routing an assignment to
the next persona's worklist.

## Hooks — *deterministic guardrails*

- **Files:** `.github/hooks/*.json`; also per-agent via `hooks:` frontmatter
  (needs `chat.useCustomAgentHooks`). Preview feature — verify on your build; org policy can
  disable hooks entirely.
- **Events:** `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`,
  `SubagentStart`, `SubagentStop`, `Stop`.
- **Mechanics:** your script gets event JSON on stdin; a `PreToolUse` hook can return
  `{"hookSpecificOutput": {"permissionDecision": "deny", "permissionDecisionReason": "..."}}`
  (or `allow` / `ask`). Most restrictive decision wins.
- **Use for:** blocking edits to sensitive paths, audit logging, auto-format after edits, env setup.
- **The line to say:** *instructions ask; hooks enforce.*
- **Pega anchor:** validate rules + security policies — engine-enforced, not model-suggested.

## Chat debug view

`Ctrl+Shift+P` → **Developer: Show Chat Debug View**. Shows each request's system prompt, attached
instructions/skills, offered tools, messages, and sizes. Your X-ray for "why did it do that" and
your evidence for token economics.

## MarkItDown (guest star)

Microsoft OSS package (`pip install "markitdown[all]"`) converting docx/pptx/xlsx/pdf/html/images
to markdown: `markitdown file.docx > file.md`. The bridge from business documents to LLM context.

## One-table summary

| Constituent | File | Loaded | One-liner |
|---|---|---|---|
| Instructions | `.github/copilot-instructions.md`, `instructions/*.instructions.md` | always / by glob | standing rules |
| Prompt files | `.github/prompts/*.prompt.md` | when you type `/name` | saved recipes |
| Custom agents | `.github/agents/*.agent.md` | when selected | personas w/ least-privilege tools |
| Skills | `.github/skills/*/SKILL.md` | when relevant | knowledge on demand |
| Subagents | `agents:` in agent file | when parent delegates | isolated worker, summary back |
| Handoffs | `handoffs:` in agent file | when agent finishes | staged pipeline w/ human gate |
| Hooks | `.github/hooks/*.json` | on lifecycle events | enforced guardrails + audit |
