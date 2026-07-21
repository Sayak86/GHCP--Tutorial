# Token Economics — what Copilot actually costs, and how to spend well

This is the session most managers remember. Keep it concrete: numbers on screen, debug view open.

## 1. The billing unit: premium requests

- Copilot plans include **unlimited use of "included" models** (multiplier **0x**) and a monthly
  allowance of **premium requests** for stronger models.
- Every model in the picker has a **multiplier**. One user message in chat = 1 request × the
  model's multiplier. Agent mode: one *turn* (your message until the agent finishes) counts as one
  premium request — even if the harness loops through many tool calls inside it.
- Where to look it up live: the model picker shows multipliers; usage is on github.com →
  Settings → Copilot, and organizations get usage reports. **Show your own usage page** — nothing
  teaches like real numbers.
- Multipliers and allowances change; don't hardcode them on slides — open the picker and read them
  with the room.

## 2. The physical unit: tokens and the context window

- Everything in a request is tokens: system prompt, **your instruction files**, loaded skills,
  #-mentions, chat history, tool results. The model has a fixed context window; when it fills,
  older context gets compressed or dropped (that's what `PreCompact` hooks fire around).
- Rough intuition for the room: a token ≈ ¾ of an English word; a 300-line file ≈ 3–4k tokens.
- **Proof, not claims:** open the chat debug view on a heavy agent turn and read the sizes.

## 3. Where the money leaks (map each to a fix we taught)

| Leak | Fix (and the demo that taught it) |
|---|---|
| Giant always-on instruction file | Scoped `applyTo:` instructions (D1·1), move knowledge to skills (D2·2) |
| `#codebase` for everything | `#file` the file you already know (orientation) |
| One endless chat for the whole day | `/clear` per task; summarize & restart long threads |
| Strong model for trivial asks | Model picker discipline: plan/explain on included models, build on premium |
| Re-explaining the task every time | Prompt files (D1·3), agents with standing prompts (D2·1) |
| Orchestrator drowning in detail | Subagents return summaries, isolated context (D2·3) |

## 4. The design insight to land

The customization system IS a token-economics system:

- **Instructions** — small, always paid → only conventions.
- **Skills** — big, paid on use → knowledge and procedures.
- **Prompt files** — paid when invoked → recipes.
- **Subagents** — separate budget, summary back → heavy lifting.

If attendees remember one sentence: **"Put context where it's paid for least often."**

## 5. Talking points for leadership (they will ask)

- Cost control is *architectural* (the table above), not just quota policing.
- Usage reports show requests per user/model — watch trend, not individual policing.
- The audit hook (D2·4) plus usage reports = the governance story security will ask about.
