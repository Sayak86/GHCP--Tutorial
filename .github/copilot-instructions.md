# PayLite — Copilot instructions

## What this project is

PayLite is a deliberately tiny training project: an internal payments API used to teach GitHub
Copilot to a Pega delivery team. Simplicity beats cleverness everywhere. If a solution needs a
framework, a pattern, or a file that a beginner would not understand in five minutes, propose a
simpler one instead.

## Tech constraints

- Python 3.11+, FastAPI, Pydantic v2. Standard library otherwise.
- No database. Storage is an in-memory dictionary in `app/store.py`, loaded at startup from
  `data/sample_payments.json` (a small file of example payments to start with).
- Tests use pytest with FastAPI's TestClient. No mocking libraries.

## Domain rules (authoritative — from requirements/BRD-PayLite.md)

- Amounts: greater than 0, at most 250,000.
- Currencies: USD, EUR, GBP, INR, SGD only.
- Beneficiary name: mandatory, 3–80 characters.
- Status lifecycle: PENDING → AUTHORIZED → SETTLED, or PENDING → REJECTED. Nothing else.
  SETTLED and REJECTED payments are immutable.
- HTTP conventions: 201 on create, 404 unknown id, 409 illegal status transition, 422 validation.

## Working agreements

- Every endpoint gets at least one happy-path and one negative pytest test.
- Keep `app/` under ~150 lines total; prefer editing existing files over adding new ones.
- Never modify `data/sample_payments.json` or anything under `inputs/` — these are controlled
  training fixtures.
- The team comes from Pega: when explaining code or concepts, use Pega analogies
  (case types, stages, flow actions, data pages) where they genuinely fit.
