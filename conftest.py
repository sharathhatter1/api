import  pytest
import requests
from config import env
from fixtures import *

# def pytest_configure(config):
#     config.addinivalue_line("markers", "smoke: smoke tests")
#     config.addinivalue_line("markers", "regression: regression tests") 
#     config.addinivalue_line("markers", "e2e: end-to-end tests")
#     config.addinivalue_line("markers", "schema: schema validation tests")

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    print(f"\nRunning tests against: {env.base_url}")
    print(f"Environment: {env.env}")

@pytest.fixture(scope="session")
def session():
    return requests.Session()

@pytest.fixture(scope="session")
def base_url():
    return env.base_url

@pytest.fixture(scope="session")
def headers():
    return {
        "Content-Type": "application/json",
        "X-API-Key": env.api_key
    }

@pytest.fixture
def weather_alert_payload():
    return {
        "city": "Dubai",
        "condition": "temperature",
        "threshold": 40,
        "email": "test@example.com"
    }
 