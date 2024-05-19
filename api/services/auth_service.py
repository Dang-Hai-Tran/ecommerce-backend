from datetime import datetime
import uuid
from django.contrib.auth import get_user_model
from api.services.token_service import TokenService
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.utils.token import JwtToken
from django.utils import timezone
from api.models.token_model import TokenModel


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authHeader = request.headers.get("Authorization")
        if not authHeader:
            return None
        if len(authHeader.split(" ")) != 2:
            raise AuthenticationFailed("Invalid token format")
        try:
            token = authHeader.split(" ")[1]
            prefix = authHeader.split(" ")[0]
            if prefix != "Bearer":
                raise AuthenticationFailed("Invalid token prefix")
            payload = JwtToken.decode(token)
            userId = uuid.UUID(payload.get("userId", None))
            sub = payload.get("sub", None)
            exp = payload.get("exp", None)
            if sub != "ecommerce" or userId is None:
                raise AuthenticationFailed("Invalid token payload")
            if exp < timezone.now().timestamp():
                raise AuthenticationFailed("Token expired")
            user = get_user_model().objects.get(id=userId)
            token = TokenService.getToken(token)
            if not token.isActive:
                raise AuthenticationFailed("Token deactivated")
            if token.user != user:
                raise AuthenticationFailed("Invalid token")
            return (user, token)
        except Exception as e:
            print(e)
            raise AuthenticationFailed("Invalid token")
