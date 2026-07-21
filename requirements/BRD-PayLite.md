**PayLite Payment Services**

Business Requirements Document (BRD)

|  |  |
| --- | --- |
| **Field** | **Value** |
| Document ID | BRD-PAYLITE-001 |
| Version | 1.0 (Approved) |
| Author | Business Analysis Team |
| Sponsor | Payment Operations |
| Status | Baseline for training build |

# 1. Purpose

Payment Operations needs a lightweight internal service, PayLite, to record and search outbound payments during the pilot phase. This document defines the business requirements for the first release. The solution will be implemented as a small HTTP API; no user interface is in scope.

# 2. Scope

* Record a new outbound payment submitted by an operations user.
* Retrieve an individual payment by its identifier.
* Search payments by status, beneficiary name and minimum amount.
* Authorize a pending payment (four-eyes step performed by a supervisor).

Out of scope for release 1: settlement with clearing systems, user authentication, reporting exports, and any persistent database.

# 3. Functional Requirements

|  |  |
| --- | --- |
| **ID** | **Requirement** |
| FR-1 | The system shall create a payment with amount, currency, beneficiary name and an optional free-text reference. A new payment always starts in status PENDING. |
| FR-2 | The system shall return the full details of a payment when queried by its identifier, or a clear not-found response otherwise. |
| FR-3 | The system shall search payments filtered by any combination of: status, beneficiary name (contains match, case-insensitive), and minimum amount. |
| FR-4 | The system shall allow a PENDING payment to be authorized, changing its status to AUTHORIZED. Authorizing a payment in any other status shall be rejected with a conflict response. |

# 4. Business Rules

|  |  |
| --- | --- |
| **ID** | **Rule** |
| BR-1 | Payment amount must be greater than 0 and must not exceed 250,000. |
| BR-2 | Currency must be one of: USD, EUR, GBP, INR, SGD. |
| BR-3 | Beneficiary name is mandatory and must be between 3 and 80 characters. |
| BR-4 | Status lifecycle: PENDING to AUTHORIZED to SETTLED; PENDING to REJECTED. No other transitions are permitted. |
| BR-5 | A SETTLED or REJECTED payment is immutable. |

# 5. Non-Functional Requirements

* NFR-1: Data may be held in memory; a small seed data set is sufficient for the pilot.
* NFR-2: Responses shall use conventional HTTP status codes (201 created, 404 not found, 409 conflict, 422 validation error).
* NFR-3: The service shall expose a basic health endpoint for monitoring.

# 6. Acceptance

Each functional requirement shall be covered by at least one automated test, including one negative test per endpoint. The Business Analysis team will trace user stories to the FR and BR identifiers in this document.

|  |  |  |
| --- | --- | --- |
| **Role** | **Name** | **Approval** |
| Business Sponsor | Head of Payment Operations | Approved |
| Business Analyst | BA Team Lead | Approved |
| Solution Architect | Platform Architecture | Approved |
