import time
import jwt
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()


def test_jwks_returns_valid_key():
    response = client.get("/jwks")
    assert response.status_code == 200

    data = response.json()
    assert "keys" in data
    assert isinstance(data["keys"], list)

    # Should only return one valid key
    assert len(data["keys"]) == 1

    key = data["keys"][0]
    assert "kid" in key
    assert key["kty"] == "RSA"


def test_auth_returns_token():
    response = client.post("/auth")
    assert response.status_code == 200

    data = response.json()
    assert "token" in data


def test_auth_expired_token():
    response = client.post("/auth?expired=true")
    assert response.status_code == 200

    token = response.json()["token"]

    # Decode without verifying signature (just checking expiration)
    decoded = jwt.decode(token, options={"verify_signature": False})

    # Token should be expired
    assert decoded["exp"] < int(time.time())


def test_auth_method_not_allowed():
    response = client.get("/auth")
    assert response.status_code == 405
