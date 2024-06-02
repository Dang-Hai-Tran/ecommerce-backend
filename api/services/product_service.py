from api.errors.bad_request import BadRequest
from api.models.product_model import ProductModel
from django.contrib.postgres.search import SearchVector, SearchQuery
from api.services.inventory_service import InventoryService


class ProductService:
    def __init__(
        self,
        product_name,
        product_description,
        product_thumbnail,
        product_price,
        product_quantity,
        product_seller,
        product_category,
        attributes,
        product_variations,
        is_draft,
        is_published,
        product_rating = 4.5,
        product_slug=None,
    ):
        self.product_name = product_name
        self.product_description = product_description
        self.product_slug = product_slug
        self.product_thumbnail = product_thumbnail
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_seller = product_seller
        self.product_category = product_category
        self.attributes = attributes
        self.product_rating = product_rating
        self.product_variations = product_variations
        self.is_draft = is_draft
        self.is_published = is_published

    def create_product(self):
        product = ProductModel.objects.create(**self.__dict__)
        inventory = InventoryService(
            product_id=product.id,
            stock=product.product_quantity,
            seller_id=product.product_seller.id,
            location="unknown",
        ).create_inventory()
        return product

    @staticmethod
    def find_all_draft_products(limit=10, page=1):
        return ProductModel.objects.filter(is_draft=True).order_by("-updated_at")[
            limit * (page - 1) : limit * page
        ]

    @staticmethod
    def find_all_published_products(limit=10, page=1):
        return ProductModel.objects.filter(is_published=True).order_by("-updated_at")[
            limit * (page - 1) : (limit * page)
        ]

    @staticmethod
    def published_product(product_seller, product_id):
        product = ProductModel.objects.get(product_seller=product_seller, id=product_id)
        if not product.is_published:
            product.is_published = True
            product.is_draft = False
            product.save()
        return product

    @staticmethod
    def draft_product(product_seller, product_id):
        product = ProductModel.objects.get(product_seller=product_seller, id=product_id)
        if product.is_published:
            product.is_published = False
            product.is_draft = True
            product.save()
        return product

    @staticmethod
    def search_products(keyword, limit=10, page=1):
        vector = SearchVector("product_name", "product_description")
        query = SearchQuery(keyword)
        return (
            ProductModel.objects.annotate(search=vector)
            .filter(search=query, is_published=True)
            .order_by("-updated_at")[limit * (page - 1) : limit * page]
        )

    @staticmethod
    def find_all_products(limit=10, page=1):
        return ProductModel.objects.all().order_by("-updated_at")[
            limit * (page - 1) : limit * page
        ]

    @staticmethod
    def update_product(product_id, **data):
        product = ProductModel.objects.get(id=product_id)
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product

    @staticmethod
    def find_product_by_id(product_id):
        return ProductModel.objects.get(id=product_id)
