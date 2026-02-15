import time
import uuid
from cryptography.hazmat.primitives.asymmetric import rsa


class KeyManager:
    def __init__(self):
        self.keys = []
        self.generate_keys()

    def generate_keys(self):
        current_time = int(time.time())

        # valid key (expires in 1 hour)
        valid_key = self.create_key(expires_at=current_time + 3600)

        # expired key (expired 1 hour ago)
        expired_key = self.create_key(expires_at=current_time - 3600)

        self.keys.append(valid_key)
        self.keys.append(expired_key)

    def create_key(self, expires_at):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()

        return {
            "kid": str(uuid.uuid4()),
            "private_key": private_key,
            "public_key": public_key,
            "expires_at": expires_at
        }
