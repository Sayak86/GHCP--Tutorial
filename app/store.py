import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_payments.json"


class PaymentStore:
    """In-memory payment store loaded from a small sample file (our stand-in for a data page)."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        payments = json.loads(DATA_FILE.read_text())
        self._payments: dict[str, dict] = {p["id"]: p for p in payments}
        self._next_seq = 1000 + len(self._payments) + 1

    def add(self, payment: dict) -> dict:
        payment_id = f"PAY-{self._next_seq}"
        self._next_seq += 1
        record = {"id": payment_id, **payment}
        self._payments[payment_id] = record
        return record

    def get(self, payment_id: str) -> dict | None:
        return self._payments.get(payment_id)

    def search(self, status: str | None, beneficiary: str | None, min_amount: float | None) -> list[dict]:
        results = list(self._payments.values())
        if status is not None:
            results = [p for p in results if p["status"] == status]
        if beneficiary is not None:
            results = [p for p in results if beneficiary.lower() in p["beneficiary"].lower()]
        if min_amount is not None:
            results = [p for p in results if p["amount"] >= min_amount]
        return results


store = PaymentStore()
