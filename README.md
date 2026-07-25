# Day 1 · Demo 3 — Prompt Files

**GHCP constituent:** prompt files (reusable `/commands`).

## 🌱 Simplest version first

A prompt file is a **saved message with a speed-dial button**. Instead of typing the same long
request every day, you save it once and run it by typing `/its-name`.

**Instructions vs prompt files:** instructions are *always on* (the fridge note); a prompt file
runs *only when you ask for it* (the speed-dial button).

## Dependencies

**Assumes `Day1-Demo1-Instructions` and `Day1-Demo2-Markitdown`.** Carried over: the instruction
files and the `requirements/` (BRD + user stories) — the prompts run against them.

## What's in this branch

| File | Run as | For | New / carried |
|---|---|---|---|
| `.github/prompts/user-story.prompt.md` | `/user-story` | BA — requirement → story | ⭐ new |
| `.github/prompts/new-endpoint.prompt.md` | `/new-endpoint` | Developer — scaffold an endpoint | ⭐ new |
| `.github/prompts/test-plan.prompt.md` | `/test-plan` | Tester — test-case table + skeletons | ⭐ new |
| `.github/prompts/sprint-summary.prompt.md` | `/sprint-summary` | Scrum Master — stand-up notes | ⭐ new |
| `.github/copilot-instructions.md`, `.github/instructions/` | — | standards | carried from D1·1 |
| `requirements/` | — | what the prompts read | carried from D1·2 |

## How to run the demo (~20 min)

1. Open `.github/prompts/user-story.prompt.md` — show the `${input:requirement:...}` line. A prompt
   file can ask you for a value when you run it.
2. In chat, type `/user-story`, Enter, and feed it a requirement the room invents:
   *"An operations user can cancel a payment that is still pending."* Watch it produce a story
   traced to the BRD and flag conflicts with the business rules.
3. Show the other three; run `/sprint-summary` — Scrum Masters see themselves in the course.

## What to point out

- One good prompt, written once, becomes a **team asset** — versioned, reviewed, shared.
- The mapping to remember: conventions → instructions · recipes → prompt files.

## Next

→ `git checkout Day1-Demo4-AgentBuild`
