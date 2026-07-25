---
name: payments-domain
description: Authoritative PayLite payments domain rules — currency list, amount limits, payment status lifecycle and allowed transitions, validation edge cases. Use when designing, implementing, reviewing or testing any payment feature, or when answering questions about what a payment may or may not do.
---

# PayLite payments domain rules

## Amounts (BR-1)

- Valid range: `0 < amount <= 250000` in the payment's own currency.
- Boundary cases testers must cover: 0 (invalid), 0.01 (valid), 250000 (valid), 250000.01 (invalid).

## Currencies (BR-2)

| Code | Notes |
|---|---|
| USD, EUR, GBP, INR, SGD | The only accepted values. Uppercase ISO-style codes. |

Anything else — including lowercase variants — is a 422 validation error. Never "helpfully"
normalize or extend this list; it is a business decision, not a formatting one.

## Status lifecycle (BR-4, BR-5)

Allowed transitions ONLY:

- `PENDING → AUTHORIZED` (supervisor authorize — the four-eyes step)
- `AUTHORIZED → SETTLED`
- `PENDING → REJECTED`

`SETTLED` and `REJECTED` are terminal and immutable (BR-5). Any other requested transition is a
409 conflict and must leave the payment unchanged. See `references/status-lifecycle.md` for the
full transition matrix and the reasoning behind it.

## Beneficiary (BR-3)

Mandatory, 3–80 characters. Search matches are contains + case-insensitive.

## HTTP conventions

201 create · 404 unknown id · 409 illegal transition · 422 validation failure.
