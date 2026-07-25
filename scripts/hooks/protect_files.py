"""PreToolUse guard: deny any tool call that touches a protected path.

The harness sends the event as JSON on stdin. We don't depend on the exact
payload shape: we serialize whatever arrived and string-match the protected
paths anywhere in the tool input, which survives schema differences between
versions. Exit with the deny JSON on stdout to block the call.
"""
import json
import sys

PROTECTED = ["data/sample_payments.json", "inputs/", ".env"]

# Tools that only read may touch anything; only mutating tools are gated.
MUTATING_HINTS = ["edit", "write", "create", "delete", "run", "terminal", "command", "apply"]


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return  # no decision -> allow

    tool_name = str(event.get("tool_name", event.get("toolName", ""))).lower()
    if not any(hint in tool_name for hint in MUTATING_HINTS):
        return

    haystack = json.dumps(event.get("tool_input", event.get("toolInput", event)))
    hit = next((p for p in PROTECTED if p in haystack), None)
    if hit is None:
        return

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"'{hit}' is a protected training fixture. Policy payguard blocks agent "
                "modifications to the sample data, inputs/ and secrets. Ask a human to change it."
            ),
        }
    }))


if __name__ == "__main__":
    main()
