from django.urls import path
from api.views.inventory_view import InventoryViewSet

urlpatterns = [
    path(
        "products/inventory/",
        InventoryViewSet.as_view({"get": "getAllInventories"}),
    ),
]
