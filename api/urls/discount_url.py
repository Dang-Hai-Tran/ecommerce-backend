from api.views.discount_view import DiscountViewSet
from django.urls import path

urlpatterns = [
    path("discounts/create/", DiscountViewSet.as_view({"post": "createNewDiscount"})),
    path("discounts/list/", DiscountViewSet.as_view({"get": "getAllDiscounts"})),
]
