"""The simplest possible hook — it changes nothing. It just ANNOUNCES what happened.

Use this to SEE the agent lifecycle with your own eyes: every time the agent is about to
use a tool (or has just used one), the harness runs this script and hands it a little packet
of JSON describing the event. We print two things from that packet: which lifecycle event
fired, and which tool was involved.

Think of it as a doorbell: it rings and tells you who is at the door, but it never decides
whether to open it. (Deciding is what protect_files.py does — that is the next step up.)
"""
import json
import sys

# The harness sends the event as JSON on stdin. Read it (if there's nothing, use an empty dict).
try:
    event = json.load(sys.stdin)
except (json.JSONDecodeError, ValueError):
    event = {}

# Two useful fields (names vary slightly between VS Code builds, so we check both spellings).
which_event = event.get("hook_event_name") or event.get("hookEventName") or "UnknownEvent"
which_tool = event.get("tool_name") or event.get("toolName") or "(no tool)"

# Just print it. This shows up in the hook output — no allow/deny decision is made.
print(f"[announce] lifecycle event = {which_event} | tool = {which_tool}")
