from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.errors.bad_request import BadRequest
from api.errors.not_found import NotFound
from api.models.token_model import TokenModel
from api.serializers.token_serializer import TokenSerializer
from api.services.token_service import TokenService
from api.services.user_service import UserService
from api.utils.cipher import HSACipher
from api.utils.hash import Hash
from backend.settings import logger


class TokenViewSet(viewsets.ViewSet):

    queryset = TokenModel.objects.all()
    serializer_class = TokenSerializer

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def createAccessToken(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = UserService.find_user_by_username(username)
            if user and Hash.checkHash(password, user.password):
                token = TokenService.createToken(user.id)
                return Response(
                    {"access": HSACipher.decrypt(token.token)},
                    status=status.HTTP_200_OK,
                )
            else:
                raise NotFound()
        except Exception as e:
            logger.error(e)
            raise BadRequest()
