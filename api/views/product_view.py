from api.models.product_model import ProductModel
from rest_framework import viewsets
from api.serializers.product_serializer import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.services.product_service import ProductService
from api.errors.bad_request import BadRequest


class ProductViewSet(viewsets.ViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def createNewProduct(self, request):
        try:
            user = request.user
            product_data = request.data
            product = ProductService(
                product_seller=user, **product_data
            ).create_product()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            raise BadRequest()
    
    def get_permissions(self):
        if self.action in ["createNewProduct"]:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
