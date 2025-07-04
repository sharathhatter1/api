import  pytest
from utils import HTTPClient


@pytest.fixture(scope="session") 
def http_client():
    return HTTPClient()

@pytest.fixture
def sample_weather_alert():
    return {
        "city": "Dubai",
        "condition": "temperature",
        "threshold": 40,
        "email": "test@example.com"
    }

@pytest.fixture
def sample_cities():
    return ["Dubai", "London", "New York", "Tokyo"]
 