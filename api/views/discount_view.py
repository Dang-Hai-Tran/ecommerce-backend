from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from api.errors.bad_request import BadRequest

from api.models.discount_model import DiscountModel
from api.serializers.discount_serializer import DiscountSerializer
from api.services.discount_service import DiscountService
from backend.settings import logger


class DiscountViewSet(viewsets.ViewSet):
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer

    @action(detail=True, methods=["post"])
    def createNewDiscount(self, request):
        try:
            data = request.data
            discount_seller = request.user
            discount = DiscountService(
                discount_seller=discount_seller, **data
            ).create_discount()
            serializer = DiscountSerializer(discount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    @action(detail=False, methods=["get"])
    def getAllDiscounts(self, request):
        try:
            discounts = DiscountService.find_all_discounts()
            serializer = DiscountSerializer(discounts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    def get_permissions(self):
        if self.action in ["getAllDiscounts"]:
            self.permission_classes = [AllowAny]
        elif self.action in ["createNewDiscount"]:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
