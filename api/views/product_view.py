from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from api.errors.bad_request import BadRequest
from api.models.product_model import ProductModel
from api.serializers.product_serializer import ProductSerializer
from api.services.product_service import ProductService
from backend.settings import logger
from rest_framework.exceptions import PermissionDenied

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
            logger.error(e)
            raise BadRequest()

    @action(detail=True, methods=["get"])
    def getAllDraftProducts(self, request):
        """
        Retrieves all draft products.
        Args:
            request: The HTTP request object.
        Returns:
            Response: A response object containing the serialized draft products data.
        Raises:
            BadRequest: If an exception occurs during the retrieval process.
        """
        try:
            limit = int(request.query_params.get("limit", 10))
            page = int(request.query_params.get("page", 1))
            products = ProductService.find_all_draft_products(limit, page)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    @action(detail=True, methods=["get"])
    def getAllPublishedProducts(self, request):
        """
        Retrieves all published products.
        Args:
            request: The HTTP request object.
        Returns:
            Response: A response object containing the serialized published products data.
        Raises:
            BadRequest: If an exception occurs during the retrieval process.
        """
        try:
            limit = int(request.query_params.get("limit", 10))
            page = int(request.query_params.get("page", 1))
            products = ProductService.find_all_published_products(limit, page)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    @action(detail=True, methods=["post"])
    def draftProduct(self, request, product_id):
        try:
            product_seller = request.user
            product = ProductService.draft_product(product_seller, product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    @action(detail=True, methods=["post"])
    def publishedProduct(self, request, product_id):
        try:
            product_seller = request.user
            product = ProductService.published_product(product_seller, product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    @action(detail=False, methods=["post"])
    def searchProducts(self, request):
        try:
            keyword = request.data.get("keyword")
            limit = int(request.query_params.get("limit", 10))
            page = int(request.query_params.get("page", 1))
            products = ProductService.search_products(keyword, limit, page)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()
    
    @action(detail=False, methods=["post"])
    def findAllProducts(self, request):
        try:
            limit = int(request.query_params.get("limit", 10))
            page = int(request.query_params.get("page", 1))
            products = ProductService.find_all_products(limit, page)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()
    
    def findOneProductById(self, product_id):
        try:
            product = ProductService.find_product_by_id(product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()
    
    @action(detail=True, methods=["put"])
    def updateProduct(self, request, product_id):
        try:
            product = ProductService.find_product_by_id(product_id)
            if product.product_seller != request.user:
                raise PermissionDenied("You don't have permission to edit this product.")
            product = ProductService.update_product(product_id, **request.data)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            raise BadRequest()

    def get_permissions(self):
        if self.action in ["searchProducts", "findAllProducts", "findOneProductById"]:
            self.permission_classes = [AllowAny]
        elif self.action in [
            "createNewProduct",
            "getAllDraftProducts",
            "getAllPublishedProducts",
            "draftProduct",
            "publishedProduct",
            "searchProducts",
            "updateProduct",
        ]:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
