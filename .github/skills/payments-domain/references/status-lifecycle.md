# Status transition matrix

Rows = current status, columns = requested action.

| From \ Action | authorize | settle | reject |
|---|---|---|---|
| PENDING | → AUTHORIZED ✔ | ✖ 409 | → REJECTED ✔ |
| AUTHORIZED | ✖ 409 (already authorized) | → SETTLED ✔ | ✖ 409 (must be rejected before authorization) |
| SETTLED | ✖ 409 (immutable) | ✖ 409 | ✖ 409 (immutable) |
| REJECTED | ✖ 409 (immutable) | ✖ 409 | ✖ 409 |

Why so strict: PayLite models a four-eyes payment control. Once value has moved (SETTLED) or the
control refused it (REJECTED), history must never be rewritten — corrections are new payments,
never edits. (Pega framing: terminal stages resolve the case; you open a new case, you don't
reopen a resolved one.)

Release 1 exposes only the *authorize* action as an endpoint; *settle* and *reject* are
candidates for release 2 — a ready-made exercise for the training room.
