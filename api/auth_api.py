import allure
from utils.http_client import HTTPClient

class AuthAPI:
    def __init__(self, client: HTTPClient = None):
        self.client = client or HTTPClient()

    @allure.step("Authenticate and retrieve token")
    def login(self, username: str, password: str):
        payload = {
            "username": username,
            "password": password
        }
        response = self.client.post("/auth/login", json=payload)
        return response
