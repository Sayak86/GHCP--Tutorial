---
mode: agent
description: Tester — produce a test plan and pytest skeletons for a user story
---

Create a test plan for this user story: ${input:story:e.g. US-4 Authorize a payment}

Output:
1. A test-case table: id, scenario, input, expected result, BR/FR reference.
   Cover happy path, each validation boundary (test both sides), unknown ids, and illegal
   status transitions.
2. pytest skeletons for every case (named test_<behavior>, plain functions), added to
   tests/test_payments.py but left failing with `pytest.fail("TODO")` bodies — implementation
   is a separate step.
Do not modify application code.
