from django.utils import timezone
from backend.settings import JWT_TOKEN, PUBLIC_KEY, PRIVATE_KEY
import jwt


class JwtToken:
    @staticmethod
    def encode(userId):
        payload = {
            "sub": "ecommerce",
            "userId": str(userId),
            "exp": timezone.now() + JWT_TOKEN.get("accessTokenLifeTime"),
            "iat": timezone.now(),
        }
        token = jwt.encode(payload, PRIVATE_KEY, algorithm=JWT_TOKEN.get("algorithm"))
        return token

    @staticmethod
    def decode(token):
        return jwt.decode(token, PUBLIC_KEY, algorithms=JWT_TOKEN.get("algorithm"))
