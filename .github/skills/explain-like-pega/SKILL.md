---
name: explain-like-pega
description: Explain Python, FastAPI or API concepts to a Pega developer audience using Pega analogies. Use whenever explaining code, architecture or open-source concepts to this team, or when someone asks "what is X" about anything in this codebase.
---

# Explaining things to a Pega team

The audience are experienced Pega LSAs/SSAs and case designers, new to Python. Explain by mapping
to what they already know, then note where the analogy breaks.

## Canonical mappings

| They know | We have | Caveat to mention |
|---|---|---|
| Case type + properties | Pydantic model (`Payment`) | No inheritance tree, no clipboard |
| Case lifecycle stages | `Status` enum + transition checks | Transitions are code, not a visual diagram |
| Flow action | Endpoint (`POST /payments/{id}/authorize`) | No UI generated for free |
| Data page (D_PaymentList) | `PaymentStore` in-memory dict | No declarative refresh strategy |
| Report definition | `GET /payments/search` query params | Filters are hand-coded |
| Validate / When rules | Pydantic `Field` constraints + `if` checks | Runs only where you call it |
| Ruleset standards | `.github/copilot-instructions.md` | Not enforced by the platform — hooks are |
| App Studio guardrails | Hooks in `.github/hooks/` | Deterministic scripts, not warnings |

## Style rules

- One analogy per concept — pick the best, don't stack three.
- Always follow the analogy with the *literal* explanation in one plain sentence.
- Never imply Pega and FastAPI are equivalent platforms; this is a bridge, not a comparison.
