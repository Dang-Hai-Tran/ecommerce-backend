from api.models.product_model import ProductModel
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
