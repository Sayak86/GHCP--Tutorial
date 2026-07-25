# 🛠️ Your turn (20 minutes) — build a Skill from scratch

You have just seen the three example skills in `.github/skills/`. Now **you** build a brand-new one.
Don't copy the examples — start from an empty folder. The trainer will review a few at the end.

## The task

PayLite is getting a **Payment Investigation** capability. Pick **one** of these (both are things
your team does every day in Pega):

- **Option A — Cancel a payment.** A skill that knows the rules for cancelling a payment: which
  statuses can be cancelled, which cannot, and what the investigator must record.
- **Option B — Send a SWIFT message.** A skill that knows how to draft a simple SWIFT MT103
  payment message from a PayLite payment (which fields map where).

You are **not** writing Python. You are writing the *knowledge* Copilot should load when this topic
comes up. Use everything you already know about payment investigation.

## Steps

1. Create the folder and file: `.github/skills/payment-investigation/SKILL.md`.
2. Write the **frontmatter** — just two lines that decide *when* the skill loads:
   ```markdown
   ---
   name: payment-investigation
   description: <one clear sentence with keywords like "cancel", "SWIFT", "investigate a payment" so the agent knows when to use this>
   ---
   ```
3. Write the **body** — 6 to 10 simple bullet points of the rules/steps. Plain English. Example
   shape (fill with your own real knowledge):
   - which payment statuses allow a cancellation, and which are final
   - what reason/reference the investigator must capture
   - (for SWIFT) which PayLite field becomes which SWIFT field
4. **Try it.** In Copilot Chat, ask a question your skill should answer, e.g.
   *"Can I cancel a payment that is already AUTHORIZED? What do I record?"* and check that the
   answer follows YOUR rules. Open the chat debug view to confirm your skill body was loaded.

## What "good" looks like (trainer review checklist)

- The `description` contains the words a user would actually type — so the skill triggers.
- The body is knowledge, not code, and a new joiner could follow it.
- Ask an *unrelated* question (e.g. "what is FastAPI?") and confirm the skill did **not** load —
  proving it only costs tokens when relevant.

> Stuck on format? Peek at `.github/skills/payments-domain/SKILL.md` for the shape only — then
> write your own content.
