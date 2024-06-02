from api.views.product_view import ProductViewSet
from django.urls import path

urlpatterns = [
    path("products/create/", ProductViewSet.as_view({"post": "createNewProduct"})),
    path("products/draft/", ProductViewSet.as_view({"get": "getAllDraftProducts"})),
    path(
        "products/published/",
        ProductViewSet.as_view({"get": "getAllPublishedProducts"}),
    ),
    path(
        "products/draft/<uuid:product_id>/",
        ProductViewSet.as_view({"post": "draftProduct"}),
    ),
    path(
        "products/published/<uuid:product_id>/",
        ProductViewSet.as_view({"post": "publishedProduct"}),
    ),
    path("products/search/", ProductViewSet.as_view({"post": "searchProducts"})),
    path("products/", ProductViewSet.as_view({"get": "findAllProducts"})),
    path("products/<uuid:product_id>/", ProductViewSet.as_view({"get": "findOneProductById"})),
    path("products/<uuid:product_id>/update/", ProductViewSet.as_view({"put": "updateProduct"})),
]
