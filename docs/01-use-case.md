# The PayLite Use Case

## Why this use case

The training needs one thread that every role can pull on, small enough that nobody gets lost in
code, and familiar enough that a payments-savvy Pega team can predict what "correct" looks like.
PayLite is that thread: **a four-endpoint payment API with an in-memory store**. The domain
knowledge is theirs already; the only new thing in the room is Copilot.

## Business scope (this is what the BRD says)

PayLite lets an internal operations team record and search outbound payments.

**Functional requirements**

1. **Create a payment** — amount, currency, beneficiary name, optional free-text reference.
   New payments start in status `PENDING`.
2. **Fetch a payment** by its id.
3. **Search payments** by status, beneficiary (contains-match), and minimum amount.
4. **Authorize a payment** — moves `PENDING → AUTHORIZED`. Any other transition is rejected.

**Business rules**

| # | Rule |
|---|---|
| BR-1 | Amount must be greater than 0 and at most 250,000 |
| BR-2 | Currency must be one of: USD, EUR, GBP, INR, SGD |
| BR-3 | Beneficiary name is mandatory, 3–80 characters |
| BR-4 | Status lifecycle: `PENDING → AUTHORIZED → SETTLED`; `PENDING → REJECTED`. No other moves |
| BR-5 | A rejected or settled payment is immutable |

**Non-functional (kept trivial on purpose)**

- Storage: in-memory dictionary, seeded from `data/seed_payments.json`. No database.
- No auth, no logging framework, no docker. This is a classroom, not production.

## The Pega translation table

Use this table constantly — it converts every unfamiliar Python/API concept into something the
team already owns. It is also great material for the *explain-like-pega* skill demo on Day 2.

| Pega concept | PayLite equivalent |
|---|---|
| Case type (Payment case) | The `Payment` resource / Pydantic model |
| Case lifecycle stages | The status enum `PENDING → AUTHORIZED → SETTLED / REJECTED` |
| Flow action (Approve/Reject) | `POST /payments/{id}/authorize` endpoint |
| Data page (D_PaymentList) | The in-memory store in `app/store.py` |
| Report definition | `GET /payments/search` with query parameters |
| Validate rule / When rule | Pydantic field validation + the transition check |
| Ruleset / class hierarchy standards | `.github/copilot-instructions.md` (team standards Copilot must follow) |
| App Studio guardrails | Hooks (`.github/hooks/`) — automated guardrails on the agent |
| Case worker portals per persona | Custom agents — one chat persona per role |

## How each role touches PayLite during the training

| Role | Artifact they produce (with Copilot) | Demo |
|---|---|---|
| BA | `requirements/BRD-PayLite.md` (via MarkItDown) and `requirements/user-stories.md` | Day 1 · 2 |
| Architect | `.github/copilot-instructions.md`, plan for the build, `architect` agent | Day 1 · 1, Day 2 · 1 |
| Developer | `app/` — the API itself, via agent mode and `/new-endpoint` | Day 1 · 3–4 |
| Tester | `tests/test_payments.py`, test plan via `/test-plan`, `tester` agent | Day 1 · 3–4, Day 2 · 1 |
| Scrum Master | Sprint summary via `/sprint-summary`, release notes via the `release-notes` skill | Day 1 · 3, Day 2 · 2 |

## What "done" looks like

By the end of Day 2 the repo contains a complete, coherent set of Copilot customizations for a real
(if tiny) product — and the team has watched every one of them being created, used, and misused
(the injection demo). They leave with a pattern they can copy into any repo on day one.
