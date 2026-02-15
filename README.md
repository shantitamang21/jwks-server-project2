\# JWKS Server – Project 1



\## Overview



This project implements a RESTful JWKS (JSON Web Key Set) server using FastAPI.



The server:

\- Generates RSA key pairs

\- Associates each key with a unique `kid`

\- Includes key expiry timestamps

\- Serves only non-expired public keys via `/jwks`

\- Issues signed JWTs via `/auth`

\- Supports issuing expired tokens using `?expired=true`



---



\## Running the Server



```bash

cd jwks-server

venv\\Scripts\\activate

uvicorn app.main:app --host 0.0.0.0 --port 8080



