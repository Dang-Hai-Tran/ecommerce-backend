from api.views.token_view import TokenViewSet
from django.urls import path

urlpatterns = [
    path("token/access/", TokenViewSet.as_view({"post": "createAccessToken"})),
]
