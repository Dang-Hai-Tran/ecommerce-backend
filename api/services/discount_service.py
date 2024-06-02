from api.models.discount_model import DiscountModel


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
        discount_is_active,
    ):
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
        self.discount_products_applicable = []
        self.discount_users = []
