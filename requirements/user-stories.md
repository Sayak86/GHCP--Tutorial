# PayLite User Stories

> Reference output of Day 1 · Demo 2 — generated with Copilot from `BRD-PayLite.md`, then groomed
> by the room. Each story traces to FR/BR identifiers in the BRD.

## US-1 · Create a payment (FR-1; BR-1, BR-2, BR-3)

**As an** operations user, **I want** to record a new outbound payment, **so that** it enters the
authorization queue.

- **Given** a valid amount, currency and beneficiary, **when** I POST /payments, **then** the
  payment is created with status PENDING and I receive 201 with its id.
- **Given** an amount of 0, negative, or above 250,000 (BR-1), **when** I POST /payments, **then**
  I receive 422.
- **Given** a currency outside USD/EUR/GBP/INR/SGD (BR-2), **then** I receive 422.
- **Given** a beneficiary name shorter than 3 or longer than 80 characters (BR-3), **then** I
  receive 422.

## US-2 · View a payment (FR-2)

**As an** operations user, **I want** to fetch a payment by id, **so that** I can answer queries.

- **Given** an existing id, **when** I GET /payments/{id}, **then** I receive the full payment.
- **Given** an unknown id, **then** I receive 404.

## US-3 · Search payments (FR-3)

**As a** supervisor, **I want** to search by status, beneficiary and minimum amount, **so that** I
can find work and investigate.

- **Given** payments in several statuses, **when** I GET /payments/search?status=PENDING, **then**
  only PENDING payments return.
- **Given** a beneficiary filter "acme", **then** matching is contains and case-insensitive.
- **Given** min_amount=1000, **then** only payments with amount ≥ 1000 return.
- Filters combine with AND semantics.

## US-4 · Authorize a payment (FR-4; BR-4, BR-5)

**As a** supervisor, **I want** to authorize a pending payment, **so that** four-eyes control holds.

- **Given** a PENDING payment, **when** I POST /payments/{id}/authorize, **then** its status
  becomes AUTHORIZED.
- **Given** a payment in any other status (BR-4), **then** I receive 409 and the payment is
  unchanged (BR-5).
- **Given** an unknown id, **then** I receive 404.

## Traceability

| Story | FR | BR | Endpoint |
|---|---|---|---|
| US-1 | FR-1 | BR-1..3 | POST /payments |
| US-2 | FR-2 | — | GET /payments/{id} |
| US-3 | FR-3 | — | GET /payments/search |
| US-4 | FR-4 | BR-4, BR-5 | POST /payments/{id}/authorize |
