from api.models.product_model import ProductModel
from api.errors.bad_request import BadRequest


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
    ):
        self.product_name = product_name
        self.product_description = product_description
        self.product_thumbnail = product_thumbnail
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_seller = product_seller
        self.product_category = product_category
        self.attributes = attributes

    def create_product(self):
        return ProductModel.objects.create(**self.__dict__)
