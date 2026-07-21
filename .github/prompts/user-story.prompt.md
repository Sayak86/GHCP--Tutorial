---
mode: agent
description: BA — turn a raw requirement into a user story with Given/When/Then acceptance criteria
---

Turn the following requirement into a user story for the PayLite backlog.

Requirement: ${input:requirement:Paste the raw requirement text}

Output, in this order:
1. Story title.
2. "As a / I want / So that".
3. Acceptance criteria in Given/When/Then form (include negative cases).
4. Which business rules (BR-x) and functional requirements (FR-x) from
   requirements/BRD-PayLite.md this touches; flag any conflict with them.
Append the result to requirements/user-stories.md with the next US number.
