---
applyTo: "tests/**"
---

- pytest style: plain functions, no test classes. Name tests `test_<behavior>`.
- One behavior per test. Arrange–act–assert, separated by blank lines.
- Every endpoint needs at least one negative test (bad input, unknown id, or illegal transition).
- Use FastAPI's TestClient; reset or re-seed the store between tests so order never matters.
