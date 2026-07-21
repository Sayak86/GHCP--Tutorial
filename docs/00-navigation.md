# How to navigate this repo (read me first)

You never need to "know git" for this training. There are 10 stops on a single timeline, and you
move between them. That's all navigation means here.

## The one tool you need

Open a terminal in the repo folder (VS Code: `Terminal → New Terminal`) and type:

```bash
python go.py          # shows all 10 stops and marks where you are
python go.py 0        # jump to the Day 1 starting point
python go.py 4        # jump to the end of Day 1
python go.py hooks    # jump by name — first stop containing "hooks"
```

`go.py` stashes any unsaved edits automatically before jumping, so you can't lose work or get the
dreaded "please commit your changes" error.

## Every stop explains itself

After jumping, open the **`demos/`** folder. The **newest file there** (its name matches the stop,
e.g. `demos/Day1-Demo1-Instructions.md`) tells you: the concept this demo teaches, which files
just appeared, a 2-minute "try it", and where the full teaching script is. The `demos/` folder is
cumulative like everything else — at stop 5 it holds five explainers, at `Day1-Start` it doesn't
exist yet.

## What jumping a stop actually does

Every stop is a git *branch* — a bookmark on the course timeline. When you jump:

- **Files appear or disappear in the Explorer.** That is the whole point: at `Day1-Start` there is
  no `.github/` and no `app/`; at `Day2-Demo5-PromptInjection` everything exists. You are looking
  at the same folder at different moments of the course.
- Nothing is deleted from the repo — the other stops still exist; you just aren't looking at them.

Stops are **cumulative**: stop 6 contains everything from stops 1–5 plus the new demo's files.

## Ways to see where you are

- **VS Code:** bottom-left corner of the window shows the current branch name (e.g.
  `Day1-Start`). Clicking it opens a branch picker — that's the mouse alternative to `go.py`.
- **Terminal:** `python go.py` (the list marks "you are here").

## On github.com

Use the **branch dropdown** (top-left of the file list, usually says the default branch name) to
view any stop in the browser.

> **One-time setup for the repo owner:** GitHub picked an arbitrary default branch when the
> branches were first pushed. Go to *Settings → General → Default branch* and set it to
> **`Day1-Start`** — then everyone who opens or clones the repo lands at the beginning of the
> course, which is what you want.

## During the session — your complete cheat sequence

| Moment | Do |
|---|---|
| Day 1, before the room fills | `python go.py 0` |
| Teaching | build everything live; never touch go.py while a demo is going well |
| A demo goes sideways | `python go.py <that demo's number>` → the finished state appears, keep talking |
| Day 2 morning (fresh start) | `python go.py 4` |
| Someone asks "show me the final version" | `python go.py 9` (or use your second clone) |

## If things ever feel truly broken

```bash
git fetch origin
git reset --hard origin/Day1-Start    # or any other stop name
```

This makes your folder exactly match the published stop, discarding local experiments.
