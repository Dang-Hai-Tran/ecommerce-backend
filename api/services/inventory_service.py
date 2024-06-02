from api.models.inventory_model import InventoryModel
from api.models.product_model import ProductModel
from api.models.user_model import UserModel


class InventoryService:
    def __init__(self, product_id, stock, seller_id, location='unknown'):
        self.inventory_product = ProductModel.objects.get(id=product_id)
        self.inventory_location = location
        self.inventory_stock = stock
        self.inventory_seller = UserModel.objects.get(id=seller_id)
    
    def create_inventory(self):
        return InventoryModel.objects.create(**self.__dict__)
    
    @staticmethod
    def find_all_inventory():
        return InventoryModel.objects.all()
