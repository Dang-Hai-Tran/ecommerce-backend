from api.models.discount_model import DiscountModel
from django.utils import timezone
from backend.settings import logger
from datetime import datetime


class DiscountService:
    def __init__(
        self,
        discount_name,
        discount_description,
        discount_code,
        discount_type,
        discount_value,
        discount_start_date,
        discount_end_date,
        discount_max_uses,
        discount_max_per_user,
        discount_min_order_value,
        discount_seller,
        discount_is_active=True,
        discount_products_applicable=[],
    ):
        self.validate_data(
            discount_code, discount_seller, discount_start_date, discount_end_date
        )
        self.discount_name = discount_name
        self.discount_description = discount_description
        self.discount_code = discount_code
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.discount_start_date = discount_start_date
        self.discount_end_date = discount_end_date
        self.discount_max_uses = discount_max_uses
        self.discount_max_per_user = discount_max_per_user
        self.discount_min_order_value = discount_min_order_value
        self.discount_seller = discount_seller
        self.discount_is_active = discount_is_active
        self.discount_products_applicable = discount_products_applicable
        self.discount_users = []

    def validate_data(
        self, discount_code, discount_seller, discount_start_date, discount_end_date
    ):
        if DiscountService.find_discount_by_seller_and_code(
            discount_seller, discount_code
        ):
            raise Exception("Discount already exists")
        try:
            start_date = datetime.strptime(discount_start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(discount_end_date, "%Y-%m-%d").date()
        except ValueError:
            raise Exception("Invalid date format. Expected 'YYYY-MM-DD'.")
        if start_date > timezone.now().date() or end_date < timezone.now().date():
            raise Exception("Discount dates are not valid")

    def create_discount(self):
        data = self.__dict__
        discount_products_applicable = data.pop("discount_products_applicable")
        discount_users = data.pop("discount_users")
        discount = DiscountModel.objects.create(**data)
        discount.discount_products_applicable.set(discount_products_applicable)
        discount.discount_users.set(discount_users)
        return discount

    @staticmethod
    def find_all_discounts():
        return DiscountModel.objects.all()

    @staticmethod
    def find_discount_by_id(discount_id):
        return DiscountModel.objects.get(id=discount_id)

    @staticmethod
    def add_product_to_discount(discount_id, product_id):
        discount = DiscountService.find_discount_by_id(discount_id)
        discount.discount_products_applicable.add(product_id)
        discount.save()
        return discount

    @staticmethod
    def add_user_to_discount(discount_id, user_id):
        discount = DiscountService.find_discount_by_id(discount_id)
        discount.discount_users.add(user_id)
        discount.save()
        return discount

    @staticmethod
    def find_discount_by_seller_and_code(discount_seller, discount_code):
        try:
            discount = DiscountModel.objects.get(
                discount_seller=discount_seller,
                discount_code=discount_code,
                discount_is_active=True,
            )
        except DiscountModel.DoesNotExist:
            discount = None
        return discount
