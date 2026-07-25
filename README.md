# Day 1 · Demo 2 — MarkItDown + the BA Workflow

**GHCP constituent:** context ingestion (MarkItDown) + the Business Analyst role.

## 🌱 Simplest version first

Copilot reads **plain text**, not Word files. MarkItDown is a **photocopier that turns a Word / PDF /
PowerPoint into plain text** Copilot can actually read. Once the BRD is readable, the Business
Analyst asks Copilot to turn it into user stories.

**In one line:** convert the business document to markdown, then let Copilot work with it.

## Dependencies

**Assumes you've completed `Day1-Demo1-Instructions`.** The instruction files are **carried over**
so the stories Copilot generates already follow team conventions.

## What's in this branch

| File | Role | New / carried over |
|---|---|---|
| `inputs/BRD-PayLite.docx` | The source Word BRD from the business | ⭐ new (the input) |
| `requirements/BRD-PayLite.md` | The BRD converted by MarkItDown — note tables survived | ⭐ new (the output) |
| `requirements/user-stories.md` | User stories Copilot generated, groomed, traced to FR/BR | ⭐ new (the output) |
| `.github/copilot-instructions.md`, `.github/instructions/` | Team standards | carried from D1·1 |

## How to run the demo (~20 min)

1. Open `inputs/BRD-PayLite.docx` — a normal Word doc with tables.
2. Convert it live in the terminal:
   ```bash
   pip install "markitdown[all]"
   markitdown inputs/BRD-PayLite.docx > requirements/BRD-PayLite.md
   ```
   Open the result — point at the **business-rules table that survived** the conversion.
3. BA moment — in Agent mode:
   > Read #file:requirements/BRD-PayLite.md and produce user stories for every functional
   > requirement. For each: title, As-a/I-want/So-that, and acceptance criteria in Given/When/Then,
   > traceable to the BR-numbers. Save as requirements/user-stories.md.
4. Groom the output with the room like a real backlog session — fix one AC, ask Copilot to renumber.

## What to point out

- The BA never wrote boilerplate; their time went to **judging** the stories, not typing them.
- MarkItDown also handles PDF, PPTX, XLSX, HTML, images — same one-liner.

## Next

→ `git checkout Day1-Demo3-PromptFiles`
