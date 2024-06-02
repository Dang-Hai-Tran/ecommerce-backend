from django.db import models
from api.models.product_model import ProductModel
from api.models.user_model import UserModel


class InventoryModel(models.Model):
    inventory_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    inventory_location = models.CharField(max_length=255, default="unknown")
    inventory_stock = models.IntegerField()
    inventory_seller = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    inventory_reservations = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
