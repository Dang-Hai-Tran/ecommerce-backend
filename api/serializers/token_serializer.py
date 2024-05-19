from api.models.token_model import TokenModel
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenModel
        fields = '__all__'
