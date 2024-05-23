from api.views.product_view import ProductViewSet
from django.urls import path

urlpatterns = [
    path("products/create/", ProductViewSet.as_view({"post": "createNewProduct"})),
]
