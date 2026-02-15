from fastapi import FastAPI, Query
from typing import Optional
from app.key_manager import KeyManager
import time
import jwt

# Create FastAPI application
app = FastAPI()

# Create KeyManager instance
key_manager = KeyManager()


# Health check endpoint
@app.get("/")
def check_server():
    return {"status": "Server is up and running"}


# JWKS endpoint
@app.get("/jwks")
def get_jwks():
    current_time = int(time.time())
    public_keys = []

    for key in key_manager.keys:
        # Only return keys that have not expired
        if key["expires_at"] > current_time:
            public_numbers = key["public_key"].public_numbers()

            public_keys.append({
                "kty": "RSA",
                "kid": key["kid"],
                "use": "sig",
                "n": format(public_numbers.n, "x"),
                "e": format(public_numbers.e, "x")
            })

    return {"keys": public_keys}


# Authentication endpoint
@app.post("/auth")
def authenticate(expired: Optional[bool] = Query(False)):
    current_time = int(time.time())

    selected_key = None

    if expired:
        # Use expired key
        for key in key_manager.keys:
            if key["expires_at"] < current_time:
                selected_key = key
                break
    else:
        # Use valid key
        for key in key_manager.keys:
            if key["expires_at"] > current_time:
                selected_key = key
                break

    payload = {
        "sub": "user123",
        "iat": current_time,
        "exp": selected_key["expires_at"]
    }

    token = jwt.encode(
        payload,
        selected_key["private_key"],
        algorithm="RS256",
        headers={"kid": selected_key["kid"]}
    )

    return {"token": token}
