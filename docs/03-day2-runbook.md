# Day 2 Run-Book — Scaling up: agents, skills, guardrails, economics

> Start state: end of Day 1 (`Day1-Demo4-AgentBuild`). Same format as Day 1: **Say / Do / Type**.
> Several Day-2 features are marked *Preview* in VS Code — rehearse on your exact build and check
> Settings (search "agent", "skills", "hooks") for flags such as `chat.useCustomAgentHooks`.

---

## 00:00–00:15 · Recap quiz (keep it playful)

Five questions, hands up: Where do repo-wide instructions live? What's the difference between an
instruction and a prompt file? What loop does the agent run? What did the `applyTo:` glob buy us?
Who reviewed the agent's diff yesterday — Copilot or us?

---

## 00:15–01:00 · Demo 1 — Custom agents: one persona per role

**Goal:** package *mode + instructions + allowed tools + model* into named, versioned personas.
**Fallback branch:** `Day2-Demo1-CustomAgents`

**Say**
- A custom agent is a markdown file in `.github/agents/<name>.agent.md`. Frontmatter defines
  **which tools it may use** and optionally which model; the body is its standing prompt.
- Pega frame: personas/portals. The BA portal doesn't show DevStudio; the **ba agent can't edit code**.
- Tool restriction is not decoration — it is **least privilege for AI**. An agent without
  `editFiles` *cannot* touch your files, no matter what the prompt says. (Remember this at the
  injection demo this afternoon.)

**Do**
1. Build `architect.agent.md` live with the room (reference on fallback branch):
   ```markdown
   ---
   name: architect
   description: Planning-only solution architect for PayLite. Produces plans, never edits code.
   tools: ['search', 'codebase', 'usages', 'problems', 'fetch']
   ---
   You are the PayLite solution architect. You produce implementation plans, API designs and
   ADRs. You NEVER edit files — output plans as markdown for humans (or the developer agent)
   to execute. Always check plans against .github/copilot-instructions.md and the BRD.
   Explain trade-offs in Pega terms when useful (stages, flow actions, data pages).
   ```
   Note for the room: the `tools:` list — use the tools picker (gear icon in chat) to see the exact
   tool names your build exposes; the file editor offers completion for them.
2. Select the agent in the chat dropdown and:
   > Plan the implementation of "cancel a pending payment" (story from yesterday). Files to touch,
   > API shape, validation, tests. Do not write code.
   Show that it *plans* but does not edit — try to bully it ("just edit the file") and show it has
   no edit tool at all.
3. Show the other four from the fallback branch (don't build all five live — show, run one prompt each):
   - `ba` — story writing, read-only + fetch
   - `developer` — full toolbelt, must follow architect plans
   - `tester` — writes/runs tests only
   - `scrum-master` — summarizes changes/git history, read-only
4. Run the `tester` agent:
   > Write the missing tests for search filters (status + min_amount combined).

**Exercise (10 min):** attendees pick their real-life role, tweak that agent's body (one rule),
run it once.

---

## 01:00–01:40 · Demo 2 — Skills: knowledge on demand

**Goal:** deep knowledge that loads ONLY when relevant — the token-friendly counterpart to instructions.
**Fallback branch:** `Day2-Demo2-Skills`

**Say**
- A skill is a folder: `.github/skills/<name>/SKILL.md` (+ optional reference files/scripts). Only
  its **name + description** are always visible to the agent; the body is read **when the task
  matches**. Instructions = every request; skills = pay only when used. This is *progressive
  disclosure* — token economics as an architecture principle.
- Rule of thumb for the room: **conventions → instructions; procedures & deep domain knowledge → skills**.

**Do**
1. Show `payments-domain` skill (build the frontmatter live, paste the body):
   - `SKILL.md` — status lifecycle, currency table, limits, ISO-ish edge cases;
     `references/status-lifecycle.md` for detail. Ask the developer agent:
     > Can a SETTLED payment be rejected? Answer from the domain rules.
     Watch it pull the skill (the response cites the lifecycle rules; show the skill being read in
     the chat debug view).
2. The crowd-pleaser — `explain-like-pega`:
   > Explain app/store.py to me.
   With the skill in place, the explanation arrives in data-page/case vocabulary. This lands the
   "skills change behavior without bloating every request" point in one laugh.
3. `release-notes` (Scrum Master): a **procedure** skill — house style + steps to build release
   notes from git log:
   > Prepare release notes for everything we built in this training.
4. Contrast in the debug view: a request where no skill loaded vs one where it did. Show token counts.

**Exercise (10 min):** sketch a SKILL.md for their own domain (frontmatter + 5 bullet body) — e.g.,
"our bank's ISO 20022 conventions". Two volunteers demo.

---

## 01:40–01:50 · Break

---

## 01:50–02:35 · Demo 3 — Subagents & handoffs: the SDLC pipeline

**Goal:** chain the personas into a flow — the training's "aha" for managers.
**Fallback branch:** `Day2-Demo3-SubagentsHandoffs`

**Say**
- **Handoff** = a button that appears when an agent finishes, switching to the *next* agent with a
  pre-filled prompt. Human stays in the loop between stages. Pega frame: **stage change with an
  assignment routed to the next persona**.
- **Subagent** = an agent invoking another agent as a *tool*, in an isolated context, getting back
  only the result. Pega frame: **a subcase / queued background process**. Isolation also means the
  subagent's context doesn't bloat the parent's — token economics again.

**Do**
1. Show the one-line change that wires a handoff — added to `architect.agent.md`:
   ```yaml
   handoffs:
     - label: "Hand off to developer → build this plan"
       agent: developer
       prompt: Implement the plan above exactly. Run tests when done.
       send: false
   ```
   (`send: false` = prompt is pre-filled but the human presses Enter — the approval moment.)
2. Live pipeline run, the centerpiece:
   - `architect`: > Plan "reject a pending payment with a mandatory reason".
   - Click the handoff → `developer` builds it → its own handoff → `tester` verifies →
     handoff → `scrum-master` writes the delta summary.
   - Narrate each transition: "requirement → plan → code → tests → report, four personas, one thread
     of context, a human pressing the button between every stage."
3. Subagents — show `delivery-lead.agent.md`:
   ```yaml
   ---
   name: delivery-lead
   description: Orchestrates PayLite delivery by delegating to developer and tester subagents.
   tools: ['agent']
   agents: ['developer', 'tester']
   ---
   ```
   > Deliver "add a currency field filter to search": have the developer implement it, then have
   > the tester verify it. Report what each subagent did.
   Show the subagent invocations in the UI; emphasize the parent only sees summaries.

**Discussion (5 min):** where would the human gates go in *their* delivery process?

---

## 02:35–03:10 · Demo 4 — Hooks: guardrails and audit

**Goal:** deterministic controls around a non-deterministic agent.
**Fallback branch:** `Day2-Demo4-Hooks`

**Say**
- Hooks = **your scripts, run by the harness at fixed lifecycle points**: `SessionStart`,
  `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `SubagentStart`, `SubagentStop`,
  `Stop`. Config lives in `.github/hooks/*.json`; a `PreToolUse` hook can **deny** a tool call.
- Instructions *ask* the model to behave. Hooks *make* it. Pega frame: instructions are guidance;
  hooks are **validate rules + security policies** — enforced, not suggested.
- Corporate slide: hooks give you **policy enforcement + audit trail** for AI edits.

**Do**
1. Walk through `.github/hooks/payguard.json` and the two tiny scripts in `scripts/hooks/`:
   - `protect_files.py` (PreToolUse): denies any tool call touching `data/seed_payments.json`,
     `.env`, or `inputs/` — returns the documented deny JSON
     (`{"hookSpecificOutput": {"permissionDecision": "deny", ...}}`).
   - `audit_log.py` (PostToolUse): appends every tool use to `.copilot-audit.log`.
2. Prove it — in Agent mode:
   > Add a test payment of 50 USD to data/seed_payments.json.
   The hook denies the edit; Copilot reports it was blocked and (thanks to instructions) explains why.
3. Open `.copilot-audit.log` — scroll the morning's audit trail. "Every tool call, timestamped.
   Show this to your security officer."
4. Note honestly: hooks are Preview; agent-scoped hooks need `chat.useCustomAgentHooks`; an org can
   also disable hooks by policy.

**Exercise (10 min):** modify `protect_files.py` to also protect `README.md`, verify the block.

---

## 03:10–03:35 · Demo 5 — Prompt injection: the live attack

**Goal:** healthy paranoia. Full script in [`docs/07-prompt-injection.md`](07-prompt-injection.md).
**Fallback branch:** `Day2-Demo5-PromptInjection`

**The short version**
1. **Say:** "Everything the agent *reads* is a potential instruction — files, web pages, tool
   output. That's prompt injection: data that talks back."
2. Open `inputs/poisoned/vendor-integration-notes.md` **rendered** (preview mode) — looks like an
  innocent vendor doc. Open it **raw** — show the hidden HTML-comment payload telling the AI to
  add a beneficiary to the seed data and weaken currency validation.
3. In Agent mode, play the naive user:
   > Read inputs/poisoned/vendor-integration-notes.md and apply whatever configuration it asks for.
4. Watch: if the model follows the payload, the **PreToolUse hook from Demo 4 blocks the seed-data
   edit** — defense in depth, live. If it refuses on its own, celebrate that too, then show the
   payload and discuss "would every model, every day, refuse?"
5. Mitigations recap (details in doc 07): review every diff · least-privilege `tools:` on agents ·
   hooks on sensitive paths · treat fetched/external content as hostile · keep approval gates on.

---

## 03:35–03:55 · Token economics + chat debug view, properly

Full notes: [`docs/06-token-economics.md`](06-token-economics.md).

1. **Premium requests:** the model picker shows a **multiplier** per model (included models = 0x,
   premium = 1x or more). One agent-mode *turn* = one premium request of the chosen model —
   but a turn can contain many tool-loop iterations. Show your own usage: VS Code status bar /
   github.com → Settings → Copilot usage.
2. **Chat debug view autopsy** of a heavy request: system prompt + instruction files (paid every
   turn!) + skill bodies (paid only when loaded) + #codebase results + history. This is where the
   room finally *sees* context engineering.
3. Habits to leave them with: new chat per task · `#file` beats `#codebase` when you know the file ·
   scoped instructions & skills over one giant instruction file · plan on a cheap model, build on a
   strong one · summarize long chats and restart.

---

## 03:55–04:00 · Wrap-up

- The ladder, complete: **harness → instructions → prompts → agent mode → custom agents → skills →
  subagents/handoffs → hooks → safety → economics**.
- Adoption checklist for their first real repo: write `copilot-instructions.md` week one; one prompt
  file per recurring chore; one agent per role; hooks on sensitive paths; usage review monthly.
- Leave them the branch map (README §3) for self-replay.
