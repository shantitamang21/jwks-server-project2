
JWKS Server – Project 1
Overview

This project implements a RESTful JWKS (JSON Web Key Set) server using FastAPI.

The server:

Generates RSA key pairs

Assigns each key a unique kid

Associates expiration timestamps with each key

Serves only non-expired public keys via /jwks

Issues signed JWTs via /auth

Supports issuing expired tokens using ?expired=true

This project demonstrates how JWT signing, key rotation, and key expiration work in a real-world authentication system.

Running the Server

1. Install dependencies:
   pip install -r requirements.txt

 2. Activate the virtual environment (Windows):
      venv\Scripts\activate

3. Start the server:
 uvicorn app.main:app --host 0.0.0.0 --port 8080

4.The server runs at:
http://localhost:8080

API Endpoints
GET /jwks

Returns all non-expired public keys in JWKS format.

Expired keys are filtered out and are not included in the response.

POST /auth

Returns a signed JWT using a valid (non-expired) private key.

The JWT:

Is signed using RS256

Contains a kid in the header

Includes iat and exp claims

POST /auth?expired=true

Returns a JWT signed with an expired key and an expired expiration timestamp.

This is used to demonstrate expired token behavior.

Testing

This project includes a pytest test suite located in the tests/ directory.

To run tests:
pytest

## Design Notes

The application is organized into separate modules:
- app/main.py handles the API routes
- app/key_manager.py manages RSA key generation and expiration logic
- tests/ contains automated tests for JWT issuance and JWKS behavior

Keys are generated at startup and stored in memory for simplicity.


To generate coverage report:
pytest --cov=app --cov-report=term
Test coverage exceeds 80% (100% in this implementation).
Screenshots of test execution and coverage results are included in the screenshots/ directory.








