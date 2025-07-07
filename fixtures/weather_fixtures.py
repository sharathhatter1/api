import  pytest
from utils import HTTPClient
from api.auth_api import AuthAPI
from config.environment import env
import allure

@pytest.fixture(scope="session") 
def http_client():
    return HTTPClient()


@pytest.fixture(scope="session")
def auth_token(http_client):
    auth_api = AuthAPI(client=http_client)
    # response = auth_api.login("mor_2314", "83r5^_")
    response = auth_api.login(env.username, env.password)
    assert response.status_code == 200, f"Login failed: {response.text}"

    token = response.json().get("token")
    assert token, f"No token found in response: {response.text}"

    # 🔐 Attach token to Allure report (truncated for safety)
    allure.attach(token, name="Session Token", attachment_type=allure.attachment_type.TEXT)

    http_client.set_auth_token(token)
    return token


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
 