from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.store import store

ALLOWED_CURRENCIES = {"USD", "EUR", "GBP", "INR", "SGD"}  # BR-2
MAX_AMOUNT = 250_000  # BR-1


class Status(str, Enum):
    PENDING = "PENDING"
    AUTHORIZED = "AUTHORIZED"
    SETTLED = "SETTLED"
    REJECTED = "REJECTED"


class PaymentCreate(BaseModel):
    amount: float = Field(gt=0, le=MAX_AMOUNT)
    currency: str
    beneficiary: str = Field(min_length=3, max_length=80)  # BR-3
    reference: str | None = None


class Payment(PaymentCreate):
    id: str
    status: Status


app = FastAPI(title="PayLite", version="1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/payments", response_model=Payment, status_code=201)
def create_payment(body: PaymentCreate) -> dict:
    if body.currency not in ALLOWED_CURRENCIES:
        raise HTTPException(status_code=422, detail=f"Currency must be one of {sorted(ALLOWED_CURRENCIES)}")
    return store.add({**body.model_dump(), "status": Status.PENDING.value})


@app.get("/payments/search", response_model=list[Payment])
def search_payments(status: Status | None = None, beneficiary: str | None = None,
                    min_amount: float | None = None) -> list[dict]:
    return store.search(status.value if status else None, beneficiary, min_amount)


@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: str) -> dict:
    payment = store.get(payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@app.post("/payments/{payment_id}/authorize", response_model=Payment)
def authorize_payment(payment_id: str) -> dict:
    payment = store.get(payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    if payment["status"] != Status.PENDING.value:  # BR-4: only PENDING -> AUTHORIZED
        raise HTTPException(status_code=409, detail=f"Cannot authorize a {payment['status']} payment")
    payment["status"] = Status.AUTHORIZED.value
    return payment
