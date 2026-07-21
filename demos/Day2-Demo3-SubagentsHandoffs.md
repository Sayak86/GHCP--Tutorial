# This stop: Subagents & Handoffs

**Two concepts, one demo:**

- **Handoff** — when an agent finishes, a button offers to switch to the *next* agent with a
  pre-filled prompt. Human presses the button = human approval gate between SDLC stages.
- **Subagent** — an agent invokes another agent *as a tool*, in an isolated context, and gets
  back only a summary. Delegation without context bloat.

Pega frame: handoff = stage change routing an assignment to the next persona; subagent = subcase.

## What changed at this stop (it's tiny — that's the point)

| File | Change |
|---|---|
| `architect.agent.md` | + `handoffs:` → developer ("build this plan") |
| `developer.agent.md` | + `handoffs:` → tester ("verify this change") |
| `tester.agent.md` | + `handoffs:` → scrum-master ("report this") |
| `delivery-lead.agent.md` | **new** — orchestrator: `tools: ['agent']`, `agents: ['developer', 'tester']` |

A few YAML lines turned five personas into a pipeline:
**architect → developer → tester → scrum-master**, human button between every stage.

## Try it (3 minutes)

1. Pick **architect**, ask it to plan *"reject a pending payment with a mandatory reason"*.
   When it finishes — there's the handoff button. Click through the whole chain.
2. Pick **delivery-lead**, ask it to deliver a small change — watch it call developer and tester
   as subagents and report only their summaries.

## Teach it

Live script: `docs/03-day2-runbook.md`, Demo 3 (the centerpiece of Day 2).

**See exactly what this demo added:** `git diff Day2-Demo2-Skills..Day2-Demo3-SubagentsHandoffs`
(view the full diff, not just --stat — it's short and very teachable.)
