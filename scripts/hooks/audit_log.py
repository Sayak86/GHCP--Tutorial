"""PostToolUse audit: append every tool call to .copilot-audit.log (gitignored).

Show this file to the room after a working session: a timestamped trail of every
action the agent took. This is the governance story for security officers.
"""
import datetime
import json
import sys

LOG_FILE = ".copilot-audit.log"


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}

    tool = event.get("tool_name", event.get("toolName", "unknown-tool"))
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    detail = json.dumps(event.get("tool_input", event.get("toolInput", {})))[:200]

    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(f"{stamp}  {tool}  {detail}\n")


if __name__ == "__main__":
    main()
