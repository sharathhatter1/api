import  pytest
import requests
from config import env
from fixtures import *
import pytest
from dotenv import load_dotenv

load_dotenv()

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
 