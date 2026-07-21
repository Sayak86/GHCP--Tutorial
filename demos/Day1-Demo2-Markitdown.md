# This stop: MarkItDown + the BA workflow

**Concept in one line:** business documents (Word, PDF, PPT) become Copilot-usable the moment you
convert them to markdown — MarkItDown is the bridge, and the BA is the first role it empowers.

## What just appeared at this stop

| File | What it is |
|---|---|
| `requirements/BRD-PayLite.md` | The Word BRD (`inputs/BRD-PayLite.docx`) converted by MarkItDown — note the tables survived. |
| `requirements/user-stories.md` | User stories generated *by Copilot from that markdown*, groomed by a human, with FR/BR traceability. |

## Try it (2 minutes)

1. Reproduce the conversion yourself:
   ```bash
   pip install "markitdown[all]"
   markitdown inputs/BRD-PayLite.docx
   ```
2. BA moment — ask Copilot Chat:
   > Using #file:requirements/BRD-PayLite.md and #file:requirements/user-stories.md, build a
   > traceability matrix (story ↔ FR ↔ BR) as a markdown table.

## Teach it

Live script: `docs/02-day1-runbook.md`, Demo 2. The point to land: the BA never wrote
boilerplate — their time went into *judging* the stories, not typing them.

**See exactly what this demo added:** `git diff Day1-Demo1-Instructions..Day1-Demo2-Markitdown --stat`
