---
applyTo: "**/*.py"
---

- Type hints on every function signature.
- Pydantic models for all request/response bodies; never raw dicts across the API boundary.
- Constants (currency list, amount limit, status names) live in one place and are imported.
- No comments that restate the code; comment only non-obvious business rules, citing BR numbers.
