import pytest
from api.products_api import ProductsAPI
import allure


@allure.feature("Forecast")
@pytest.fixture(scope="module")
def api():
    return ProductsAPI()

def test_get_all_products_returns_200(api):
    response = api.get_all_products()
    assert response.status_code == 200, "Expected status code 200"

def test_get_single_product_returns_200(api):
    response = api.get_product_by_id(1)
    assert response.status_code == 200, "Expected status code 200"
