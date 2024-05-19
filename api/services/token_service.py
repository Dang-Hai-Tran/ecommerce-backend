from api.models.token_model import TokenModel
from api.utils.token import JwtToken
from api.models.user_model import UserModel
from django.utils import timezone
from backend.settings import JWT_TOKEN
from uuid import UUID


class TokenService:
    @staticmethod
    def createToken(userId: UUID):
        token = JwtToken.encode(userId)
        expired_at = timezone.now() + JWT_TOKEN.get("accessTokenLifeTime")
        user = UserModel.objects.get(id=userId)
        token = TokenModel.objects.create(
            token=token, user=user, expired_at=expired_at
        )
        return token

    @staticmethod
    def deactivateToken(token: str):
        tokenModel = TokenModel.objects.get(token=token)
        tokenModel.isActive = False
        tokenModel.save()
