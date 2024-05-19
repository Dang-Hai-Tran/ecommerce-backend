from api.services.token_service import TokenService
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.models.token_model import TokenModel
from api.serializers.token_serializer import TokenSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.errors.bad_request import BadRequest
from api.errors.not_found import NotFound
from rest_framework.decorators import action
from api.services.user_service import UserService


class TokenViewSet(viewsets.ViewSet):

    queryset = TokenModel.objects.all()
    serializer_class = TokenSerializer

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def createAccessToken(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = UserService.getUserByUsername(username)
            if user and user.password == password:
                token = TokenService.createToken(user.id)
                return Response({"access": token.token}, status=status.HTTP_200_OK)
            else:
                raise NotFound()
        except Exception as e:
            print(e)
            raise BadRequest()
