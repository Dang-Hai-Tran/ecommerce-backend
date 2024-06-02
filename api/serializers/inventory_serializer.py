from api.models.inventory_model import InventoryModel
from rest_framework import serializers

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = '__all__'
