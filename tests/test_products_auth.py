import pytest
import allure
from utils.validators import ResponseValidator
from models.products import Product
from api.products_api import ProductsAPI

@allure.story("Authenticated - Get All Products")
@pytest.mark.smoke
def test_get_products_with_auth(http_client, auth_token):
    api = ProductsAPI(client=http_client)

    with allure.step("Get all products with token"):
        response = api.get_all_products()

    ResponseValidator.validate_status_code(response, 200)

@allure.story("Authenticated - Get Product by ID")
def test_get_product_by_id_with_auth(http_client, auth_token):
    api = ProductsAPI(client=http_client)
    response = api.get_product_by_id(1)
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_schema(response, Product)
