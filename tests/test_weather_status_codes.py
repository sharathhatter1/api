import  pytest
import allure
from models.current import WeatherCurrent


from utils import ResponseValidator

@allure.feature("Weather API Status Codes")
class TestWeatherStatusCodes:
    
    @allure.story("Current Weather Status Codes")
    @pytest.mark.parametrize("city,expected_status", [
        ("Dubai", 200),
        ("", 400),
        ("InvalidCity123", 400)
    ])
    def test_current_weather_status_codes(self, weather_api, city, expected_status):
        response = weather_api.get_current_weather(city)
        ResponseValidator.validate_status_code(response, expected_status)
        
        if expected_status == 200:
            ResponseValidator.validate_schema(response, WeatherCurrent)

    @pytest.mark.schema
    @allure.story("Forecast Status Codes")
    def test_forecast_unauthorized(self, forecast_api):
        response = forecast_api.get_forecast("Dubai", 5, include_key=True)
        ResponseValidator.validate_status_code(response, 200)
