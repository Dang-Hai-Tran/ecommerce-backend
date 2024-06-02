from api.models.discount_model import DiscountModel
from rest_framework import serializers

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountModel
        fields = '__all__'
