from  utils import HTTPClient, ResponseValidator
import allure
from config.environment import env



class ForecastAPI:
    def __init__(self, client: HTTPClient = None):
        self.client = client or HTTPClient()
        self.validator = ResponseValidator()
    
    @allure.step("Get forecast for {city} ({days} days)")
    def get_forecast(self, city: str, days: int, include_key: bool = True):
        params = {"q": city, "days": days}
        if include_key:
            params["key"] = env.api_key
        response = self.client.get("/forecast.json", params=params)
        return response
