from api.views.user_view import UserViewSet
from django.urls import path

urlpatterns = [
    path("users/register/", UserViewSet.as_view({"post": "register"})),
    path("users/login/", UserViewSet.as_view({"post": "logIn"})),
    path("users/me/", UserViewSet.as_view({"get": "getMe"})),
    path("users/logout/", UserViewSet.as_view({"post": "logOut"})),
    path("users/password/reset/", UserViewSet.as_view({"post": "changePassword"})),
]
