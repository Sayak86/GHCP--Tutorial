#!/usr/bin/env python3
"""PayLite training navigator — jump to any point of the course without knowing git.

Usage:
    python go.py            show all stops and where you are now
    python go.py 0          go to the Day 1 starting point
    python go.py 3          go to stop #3 (see the list)
    python go.py hooks      go to the first stop whose name contains "hooks"

Uncommitted changes are stashed automatically (git stash) so nothing is ever lost.
"""
import subprocess
import sys

STOPS = [
    ("Day1-Start",                   "START HERE — docs + BRD only, nothing built yet"),
    ("Day1-Demo1-Instructions",      "after Demo 1: custom instructions"),
    ("Day1-Demo2-Markitdown",        "after Demo 2: BRD converted, user stories written"),
    ("Day1-Demo3-PromptFiles",       "after Demo 3: /user-story /new-endpoint /test-plan /sprint-summary"),
    ("Day1-Demo4-AgentBuild",        "after Demo 4: PayLite API + tests (end of Day 1)"),
    ("Day2-Demo1-CustomAgents",      "after Demo 1: five role agents"),
    ("Day2-Demo2-Skills",            "after Demo 2: three skills"),
    ("Day2-Demo3-SubagentsHandoffs", "after Demo 3: handoff chain + delivery-lead"),
    ("Day2-Demo4-Hooks",             "after Demo 4: payguard hooks"),
    ("Day2-Demo5-PromptInjection",   "FINAL — everything, incl. injection fixture"),
]


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], capture_output=True, text=True)


def show_list() -> None:
    current = git("branch", "--show-current").stdout.strip()
    print("\nPayLite training stops (cumulative — each includes all previous):\n")
    for i, (branch, what) in enumerate(STOPS):
        marker = " <-- you are here" if branch == current else ""
        print(f"  [{i}] {branch:32} {what}{marker}")
    if current not in [b for b, _ in STOPS]:
        print(f"\n  (you are currently on '{current}')")
    print("\nJump anywhere with:  python go.py <number>   or   python go.py <part-of-name>\n")


def pick(arg: str) -> str | None:
    if arg.isdigit() and int(arg) < len(STOPS):
        return STOPS[int(arg)][0]
    matches = [b for b, _ in STOPS if arg.lower() in b.lower()]
    return matches[0] if matches else None


def main() -> None:
    if len(sys.argv) < 2:
        show_list()
        return
    target = pick(sys.argv[1])
    if target is None:
        print(f"No stop matches '{sys.argv[1]}'.")
        show_list()
        sys.exit(1)
    if git("status", "--porcelain").stdout.strip():
        git("stash", "push", "-u", "-m", "go.py auto-stash")
        print("Your unsaved changes were stashed (recover any time with: git stash pop).")
    result = git("checkout", target)
    if result.returncode != 0:
        print(result.stderr.strip())
        sys.exit(1)
    print(f"Now on: {target}")
    print("Files in the explorer just changed to match this point of the course — that is normal.")


if __name__ == "__main__":
    main()
