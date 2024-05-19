import uuid

from django.db import models
from api.utils.token import JwtToken


class TokenModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(unique=True)
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    isExpired = models.BooleanField(default=False)
    expired_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Token::{self.token}::{self.user}"
