from django.db import models
import uuid
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255, db_index=True)
    product_description = models.CharField(max_length=255, db_index=True)
    product_slug = models.CharField(max_length=255, default=None, null=True, blank=True)
    product_thumbnail = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
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
    product_rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5,
        validators=[
            MinValueValidator(Decimal("1.0")),
            MaxValueValidator(Decimal("5.0")),
        ],
    )
    product_variations = models.JSONField(default=list)
    is_draft = models.BooleanField(default=True, db_index=True)
    is_published = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.product_slug:
            self.product_slug = slugify(self.product_name)
        super().save(*args, **kwargs)
