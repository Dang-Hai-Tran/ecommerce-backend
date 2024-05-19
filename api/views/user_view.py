from rest_framework import status, viewsets
from rest_framework.response import Response

from api.errors.bad_request import BadRequest
from api.models import UserModel, TokenModel
from api.serializers.user_serializer import UserSerializer
from api.services.token_service import TokenService
from api.services.user_service import UserService
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.utils import timezone


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.all()

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        try:
            username = request.data.get("username")
            email = request.data.get("email")
            password = request.data.get("password")
            user = UserService.createUser(username, email, password)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            raise BadRequest()

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def logIn(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = UserService.getUserByUsername(username)
            if user and user.password == password:
                user.last_login = timezone.now()
                user.save()
                serializer = self.get_serializer(user)
                token = TokenService.createToken(user.id)
                return Response(
                    {"user": serializer.data, "access": token.token},
                    status=status.HTTP_200_OK,
                )
            else:
                raise BadRequest()
        except Exception as e:
            print(e)
            raise BadRequest()

    @action(methods=["get"], detail=True, permission_classes=[IsAuthenticated])
    def getMe(self, request):
        try:
            user = request.user
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            raise BadRequest()

    @action(methods=["post"], detail=False, permission_classes=[IsAuthenticated])
    def logOut(self, request):
        try:
            user = request.user
            tokens = list(TokenService.getAllTokensOfUser(user))
            for token in tokens:
                TokenService.deactivateToken(token.token)
            return Response({"message": "Logout successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            raise BadRequest()
