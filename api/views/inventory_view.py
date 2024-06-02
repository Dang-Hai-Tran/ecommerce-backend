from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from api.errors.bad_request import BadRequest

from api.models.inventory_model import InventoryModel
from api.serializers.inventory_serializer import InventorySerializer
from api.services.inventory_service import InventoryService
from backend.settings import logger
from rest_framework.exceptions import PermissionDenied


class InventoryViewSet(viewsets.ViewSet):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer

    @action(detail=False, methods=["get"])
    def getAllInventories(self, request):
        try:
            inventories = InventoryService.find_all_inventory()
            serializer = InventorySerializer(inventories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    def get_permissions(self):
        if self.action in ["getAllInventories"]:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
