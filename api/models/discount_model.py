from django.db import models
import uuid
from api.models.user_model import UserModel
from api.models.product_model import ProductModel


class DiscountModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount_name = models.CharField(max_length=255)
    discount_description = models.CharField(max_length=255, null=True, blank=True, default=None)
    discount_code = models.CharField(max_length=255)
    type_choices = (("Percentage", "Percentage"), ("Fixed", "Fixed"))
    discount_type = models.CharField(
        choices=type_choices, max_length=255, default="Fixed"
    )
    discount_value = models.IntegerField()
    discount_start_date = models.DateField()
    discount_end_date = models.DateField()
    discount_max_uses = models.IntegerField()
    discount_uses_count = models.IntegerField()
    discount_users = models.ManyToManyField(UserModel, related_name="discount_users")
    discount_max_per_user = models.IntegerField(default=1)
    discount_min_order_value = models.IntegerField(default=50)
    discount_seller = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    discount_is_active = models.BooleanField(default=True)
    discount_products_applicable = models.ManyToManyField(ProductModel, related_name="discount_products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
