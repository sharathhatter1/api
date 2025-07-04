import  pytest
from api.weather_api import WeatherAPI
from api.forecast_api import ForecastAPI
from utils import HTTPClient

@pytest.fixture(scope="session")
def weather_api(http_client):
    return WeatherAPI(client=http_client)


@pytest.fixture(scope="session")
def forecast_api(http_client):
    return ForecastAPI(client=http_client)


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
 