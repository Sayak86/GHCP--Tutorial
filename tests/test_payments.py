import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.store import store

client = TestClient(app)


@pytest.fixture(autouse=True)
def reseed():
    store.reset()


def test_create_payment_starts_pending():
    body = {"amount": 500.0, "currency": "USD", "beneficiary": "Test Vendor"}

    response = client.post("/payments", json=body)

    assert response.status_code == 201
    payment = response.json()
    assert payment["status"] == "PENDING"
    assert payment["id"].startswith("PAY-")


def test_create_payment_rejects_amount_above_limit():
    body = {"amount": 250001, "currency": "USD", "beneficiary": "Test Vendor"}

    response = client.post("/payments", json=body)

    assert response.status_code == 422


def test_create_payment_rejects_unknown_currency():
    body = {"amount": 10, "currency": "ZZZ", "beneficiary": "Test Vendor"}

    response = client.post("/payments", json=body)

    assert response.status_code == 422


def test_get_payment_returns_seeded_record():
    response = client.get("/payments/PAY-1001")

    assert response.status_code == 200
    assert response.json()["beneficiary"] == "Acme Supplies Ltd"


def test_get_unknown_payment_returns_404():
    response = client.get("/payments/PAY-9999")

    assert response.status_code == 404


def test_search_combines_filters_with_and():
    response = client.get("/payments/search", params={"status": "PENDING", "min_amount": 100})

    assert response.status_code == 200
    results = response.json()
    assert [p["id"] for p in results] == ["PAY-1001"]


def test_search_beneficiary_is_case_insensitive_contains():
    response = client.get("/payments/search", params={"beneficiary": "acme"})

    assert [p["id"] for p in response.json()] == ["PAY-1001"]


def test_authorize_pending_payment():
    response = client.post("/payments/PAY-1001/authorize")

    assert response.status_code == 200
    assert response.json()["status"] == "AUTHORIZED"


def test_authorize_non_pending_payment_returns_409():
    response = client.post("/payments/PAY-1003/authorize")

    assert response.status_code == 409
