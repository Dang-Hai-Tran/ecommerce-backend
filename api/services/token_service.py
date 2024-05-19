from api.models.token_model import TokenModel
from api.utils.token import JwtToken
from api.models.user_model import UserModel
from django.utils import timezone
from backend.settings import JWT_TOKEN
from uuid import UUID
from api.utils.cipher import HSACipher


class TokenService:
    @staticmethod
    def createToken(userId: UUID):
        token = JwtToken.encode(userId)
        expired_at = timezone.now() + JWT_TOKEN.get("accessTokenLifeTime")
        user = UserModel.objects.get(id=userId)
        token = TokenModel.objects.create(token=HSACipher.encrypt(token), user=user, expired_at=expired_at)
        return token

    @staticmethod
    def deactivateToken(tokenID: UUID):
        token = TokenModel.objects.get(id=tokenID)
        if token.isActive:
            token.isActive = False
            token.save()

    @staticmethod
    def getToken(token: str):
        return TokenModel.objects.get(token=HSACipher.encrypt(token))

    @staticmethod
    def getAllTokensOfUser(user: UserModel):
        return TokenModel.objects.filter(user=user)
