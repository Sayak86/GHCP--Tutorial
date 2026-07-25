# Token Economics — what Copilot costs, in credits (AIC)

This is the session most managers remember. Keep it concrete. Throughout, we'll talk in **credits**
— your organisation may call them **AIC (AI Credits)** or "premium requests"; the idea is the same:
**a pool of paid units you spend every time you use a strong model.**

> Before the session, replace "credit / AIC" below with your team's exact term, the monthly
> allowance per person, and the cost per unit if you have it. Real numbers land harder than "a credit".

## 1. The billing unit: one request = some credits

- Copilot plans include **unlimited use of "included" models** (they cost **0 credits**) and a
  **monthly pool of credits** for the stronger models.
- Every model in the picker shows a **multiplier** — that's its **price in credits**. A 1× model
  costs 1 credit per request; a heavier model might cost more; an included model costs 0.
- **One request = one message you send** (in Agent mode, one *turn* — your message until the agent
  finishes) **× the model's credit price.** Note: a single Agent turn may loop through many tool
  steps internally but still counts as **one** request.
- Where to see it live: the model picker shows the multiplier; your spend is on github.com →
  Settings → Copilot, and organisations get usage reports. **Show your own usage page** — nothing
  teaches like real numbers.

**The one sentence for leadership:** *every strong-model message spends credits from a monthly pool;
the customisations in this course are how you spend fewer of them.*

## 2. What's actually inside one request (why some cost more)

Everything you send is measured in **tokens** (think: pieces of words). A request carries:

- the hidden system prompt,
- **your instruction files** (paid on **every** request),
- any **skill** bodies that loaded (paid **only** when relevant),
- your `#`-mentions (`#codebase` is big; `#file` is small),
- the chat history so far, and the tool results.

The model has a fixed room (the "context window"). Fill it and old content gets summarized or
dropped. **Proof, not claims:** open the chat debug view on a heavy Agent turn and read the sizes.
A token ≈ ¾ of an English word; a 300-line file ≈ 3–4k tokens.

## 3. Where credits leak (and the demo that fixes each)

| Leak | Fix (and where you taught it) |
|---|---|
| One giant always-on instructions file | Scoped `applyTo:` instructions (D1·1); move knowledge to skills (D2·2) |
| `#codebase` for everything | `#file` the file you already know |
| One endless chat all day | New chat per task; summarize & restart long threads |
| Strong model for trivial asks | Model picker discipline: **Plan/ask on a cheap model, build on a strong one** |
| Re-explaining the task each time | Prompt files (D1·3), agents with standing prompts (D2·1) |
| A manager agent drowning in detail | Subagents return only summaries (D2·3) |

## 4. The design insight to land

The whole customisation system **is** a credit-economics system:

- **Instructions** — small, paid every time → put only conventions here.
- **Skills** — big, paid only when used → put knowledge & procedures here.
- **Prompt files** — paid only when you run them → recipes.
- **Subagents** — separate private budget, only a summary comes back → heavy lifting.

If the room remembers one sentence: **"Put context where it's paid for least often."**

## 5. Talking points for leadership

- Cost control is **architectural** (the table above), not just policing quotas.
- Usage reports show credits per user/model — watch the trend, not individuals.
- The audit hook (D2·4) + usage reports = the governance story security will ask for.
