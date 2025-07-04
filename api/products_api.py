from utils.http_client import HTTPClient
import allure
from config.environment import env

class ProductsAPI:
    def __init__(self, client: HTTPClient = None):
        self.client = client or HTTPClient()

    @allure.step("Get all products")
    def get_all_products(self):
        return self.client.get("/products")

    @allure.step("Get product by ID: {product_id}")
    def get_product_by_id(self, product_id: int):
        return self.client.get(f"/products/{product_id}")
