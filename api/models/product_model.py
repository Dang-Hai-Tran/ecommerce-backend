from django.db import models
import uuid


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_thumbnail = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_seller = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    category_choices = (
        ("Electronics", "Electronics"),
        ("Furniture", "Furniture"),
        ("Clothing", "Clothing"),
        ("Books", "Books"),
        ("Sports", "Sports"),
        ("Other", "Other"),
    )
    product_category = models.CharField(max_length=255, choices=category_choices)
    attributes = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
