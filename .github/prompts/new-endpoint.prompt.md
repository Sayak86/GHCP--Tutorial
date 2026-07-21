---
mode: agent
description: Developer — scaffold a new PayLite endpoint following team conventions
---

Add a new endpoint to the PayLite API.

Endpoint purpose: ${input:purpose:e.g. cancel a pending payment}

Steps:
1. Restate which user story / business rules apply; if none exist, say so and stop.
2. Implement in app/main.py (route) and app/store.py (state change) following the repo
   instructions — validation, status lifecycle, HTTP codes.
3. Add one happy-path and one negative test in tests/test_payments.py.
4. Run the tests and report results.
