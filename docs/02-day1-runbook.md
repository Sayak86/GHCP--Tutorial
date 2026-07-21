# Day 1 Run-Book — Foundations: from a Word BRD to a working API

> Format: every block gives you **Say** (talking points), **Do** (exact clicks/commands), and
> **Type into Copilot** (verbatim prompts, in blockquotes). Fallback branch is noted per demo.
> Start state: a clone WITHOUT `.github/` customizations, `app/`, `requirements/` — i.e. the commit
> before `Day1-Demo1-Instructions`.

---

## 00:00–00:30 · Orientation: what is actually happening when you chat

**Say**
- Copilot is three things: inline completions, chat, and an **agent**. This course is about the agent.
- The **agent harness** is a loop, not magic: *your prompt + context → model → tool calls (read
  files, edit files, run terminal) → results go back into the loop → repeat until done*. Everything
  we customize over two days — instructions, prompts, agents, skills, hooks — just changes what
  enters that loop, or intercepts what comes out of it.
- Pega hook for the room: the harness is like a **case lifecycle engine**; instructions are your
  **rulesets**; hooks are your **guardrails**; agents are **personas/portals**.
- Three chat modes: **Ask** (answer questions, touches nothing), **Edit** (proposes edits to files
  you choose), **Agent** (plans, edits, runs commands autonomously — with your approval gates).
- The **model picker**: different models, different strengths, different *cost multipliers*. We
  will come back to money on Day 2.

**Do**
1. Open Copilot Chat. Show the mode dropdown (Ask / Edit / Agent) and the model picker.
2. In **Ask** mode:
   > What files are in this workspace and what do you think this project is?
3. Open the **chat debug view**: `Ctrl+Shift+P` → **"Developer: Show Chat Debug View"**.
   Show the last request: the system prompt, the tools offered to the model, your message, and the
   context that was attached. **Say:** "This view is our X-ray machine. Every time today you wonder
   *why did Copilot do that* — the answer is in here. Notice you're never sending one line; you're
   sending thousands of tokens of context."
4. Type `#` in the chat box — show the popup list (#file, #codebase, #fetch, #changes...). Type `/`
   — show slash commands. Type `@` — show participants. (Cheat sheet: `docs/05-cheatsheet.md`.)

**Land the point:** *Context is the product. The rest of this course is about engineering that context.*

---

## 00:30–01:15 · Demo 1 — Custom instructions (role: Architect)

**Goal:** show that a repo can carry standing orders that shape every single Copilot answer.
**Fallback branch:** `Day1-Demo1-Instructions`

**Say**
- Instructions are the **ruleset** of the repo: always loaded, apply to every chat.
- Two flavors: repo-wide (`.github/copilot-instructions.md`) and **scoped**
  (`.github/instructions/*.instructions.md` with an `applyTo:` glob — only loaded when matching
  files are in play).

**Do — the before/after trick (this sells the whole feature):**
1. BEFORE any instructions exist, in Agent mode ask:
   > Create a single-file FastAPI app with one endpoint that returns a hardcoded list of payments.
2. Let it produce *something* — probably fine but generic. **Discard the edits.** Point out what it
   guessed at: naming, structure, validation, comments.
3. Now build the instructions file **live with the room** — this is the "design together" moment.
   Create `.github/copilot-instructions.md` and ask the room for their standards. Seed with:
   - This is PayLite, a training payments API. Keep all code deliberately simple.
   - Python 3.11+, FastAPI, Pydantic v2. No database — in-memory store only.
   - Currencies limited to USD, EUR, GBP, INR, SGD; amounts 0 < x ≤ 250000.
   - Status lifecycle PENDING → AUTHORIZED → SETTLED / REJECTED, no other transitions.
   - Every endpoint needs a matching pytest test.
   - The audience is a Pega team: when asked to explain code, use Pega analogies.
   - Never modify `data/seed_payments.json` or any file under `inputs/`.
   (Reference result: `.github/copilot-instructions.md` on the fallback branch.)
4. **Tip:** you can even have Copilot draft it: `Ctrl+Shift+P` → *"Chat: Generate Instructions"* —
   mention this exists, but writing it with the room is the teaching moment.
5. Open a **new chat** (fresh context!) and repeat the EXACT prompt from step 1. Watch it now obey
   the rules. Then the kicker — ask:
   > Explain what FastAPI is.
   It should answer with Pega analogies. The room laughs; the feature is sold.
6. Open the **chat debug view** and show the instructions file sitting inside the request. **Say:**
   "You now pay for these tokens on every request. Remember that — it becomes important on Day 2."
7. Quickly add one scoped file, `.github/instructions/tests.instructions.md`:
   ```markdown
   ---
   applyTo: "tests/**"
   ---
   Use pytest, no test classes. One behavior per test. Name tests test_<behavior>.
   Always include one negative test per endpoint.
   ```
   Explain: this only enters context when test files are involved — your first taste of
   *token economics by design*.

**Exercise (10 min):** pairs write one instruction of their own (e.g., "all money amounts are
Decimal, never float"), reload chat, verify Copilot obeys it.

---

## 01:15–01:25 · Break

---

## 01:25–02:10 · Demo 2 — MarkItDown + the BA workflow

**Goal:** requirements locked in Word docs become Copilot-usable markdown; BA generates stories.
**Fallback branch:** `Day1-Demo2-Markitdown`

**Say**
- LLMs eat **markdown**, not .docx. [MarkItDown](https://github.com/microsoft/markitdown) is a
  Microsoft OSS package that converts Office files, PDFs, HTML, even images into markdown.
- This is the bridge between "the business sent us a BRD" and "Copilot can work with it".

**Do**
1. Open `inputs/BRD-PayLite.docx` (show it's a normal Word doc with tables).
2. In the terminal:
   ```bash
   pip install "markitdown[all]"          # already done in prep; show anyway
   markitdown inputs/BRD-PayLite.docx > requirements/BRD-PayLite.md
   ```
3. Open the result — point at the tables that survived conversion. **Say:** "That table of business
   rules is now first-class context."
4. BA moment — in Agent mode:
   > Read #file:requirements/BRD-PayLite.md and produce user stories for every functional
   > requirement. For each story: title, "As a / I want / So that", and acceptance criteria in
   > Given/When/Then form, directly traceable to the BR-numbers in the BRD.
   > Save the result as requirements/user-stories.md.
5. Review the stories WITH the room like a real backlog grooming — fix one AC by hand, ask Copilot
   to renumber. **Say:** "The BA never wrote boilerplate; they spent the time judging content."
6. Bonus if time: `markitdown` also does PDFs and pptx — one-liner mention.

**Exercise (10 min):** attendees ask Copilot to derive a *traceability matrix* (story ↔ BR ↔ future
endpoint) as a markdown table from the two files.

---

## 02:10–02:55 · Demo 3 — Prompt files: reusable prompts per role

**Goal:** turn one-off prompts into versioned, parameterized, shareable team assets.
**Fallback branch:** `Day1-Demo3-PromptFiles`

**Say**
- Yesterday's great prompt dies in someone's chat history. A **prompt file**
  (`.github/prompts/<name>.prompt.md`) is a prompt under version control — run it with
  `/<name>` in chat. Think of it as a **saved, reviewed, reusable work instruction**.
- Instructions = *always on*. Prompt files = *on demand*. Say this twice.

**Do**
1. Create `.github/prompts/user-story.prompt.md` live (reference version on fallback branch):
   ```markdown
   ---
   mode: agent
   description: Turn a raw requirement into a user story with Given/When/Then ACs
   ---
   Turn the following requirement into a user story for the PayLite backlog.
   Requirement: ${input:requirement:Paste the raw requirement text}
   Output: title, As-a/I-want/So-that, acceptance criteria in Given/When/Then,
   and which business rules (BR-x) from requirements/BRD-PayLite.md it touches.
   ```
2. Run it: type `/user-story` in chat, feed it a requirement the room invents (e.g., "cancel a
   pending payment"). Show `${input:...}` prompting for the parameter.
3. Show the other three (create the ones you have time for, show the rest from the fallback branch):
   - `/new-endpoint` (Developer) — scaffold an endpoint per team conventions
   - `/test-plan` (Tester) — test plan + pytest skeletons from a story
   - `/sprint-summary` (Scrum Master) — stand-up/sprint notes from `#changes` and git log
4. Run `/sprint-summary` even though there's little history — it will summarize the morning's
   commits. Scrum Masters in the room see themselves in the course for the first time.

**Exercise (10 min):** each pair writes a prompt file for their own daily chore and demos it.

---

## 02:55–03:05 · Break

---

## 03:05–03:50 · Demo 4 — Agent mode: build PayLite for real

**Goal:** the payoff — from stories to working, tested code, with the human as reviewer.
**Fallback branch:** `Day1-Demo4-AgentBuild`

**Say**
- Agent mode = the harness loop with tools: it will plan, create files, run commands, read errors,
  and retry. Your job shifts from *typing* to *directing and reviewing*.
- We deliberately do this AFTER instructions exist — watch how much steering we *don't* need.

**Do**
1. In Agent mode:
   > Implement the PayLite API from requirements/user-stories.md.
   > Structure: app/main.py (FastAPI app + endpoints), app/store.py (in-memory store seeded from
   > data/seed_payments.json), tests/test_payments.py. Create a small seed file with 5 payments.
   > Follow the repo instructions strictly. Keep it under ~150 lines of app code.
2. **Narrate the loop while it runs** — this is the most important minute of Day 1: "it planned,
   it's creating store.py, now it runs pytest, a test failed, it read the error, it's fixing it."
   Point at the tool-approval prompts: *the human gate*.
3. When done, review the diff like a code review. Ask the room: does BR-4 (lifecycle) hold? Then:
   > Run the tests and show me the results. Then add one negative test proving an AUTHORIZED
   > payment cannot be authorized twice (expect 409).
4. If it runs cleanly, `uvicorn app.main:app` + one curl for applause — optional, not required.
5. Close with the chat debug view again: show how much context an agent-mode turn carries.

**Exercise (if time):** ask agent mode to add `POST /payments/{id}/reject` end-to-end (code + test).

---

## 03:50–04:00 · Recap + homework

- Recap ladder: **harness → instructions (always-on) → prompt files (on-demand) → agent mode (autonomy)**.
- Tomorrow: personas (custom agents), knowledge-on-demand (skills), pipelines (subagents/handoffs),
  guardrails (hooks), and one live attack (prompt injection).
- Homework: bring one repetitive task from your real project — we'll turn some into agents/skills.
