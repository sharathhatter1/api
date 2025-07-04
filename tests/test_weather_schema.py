import  pytest
import allure
from models.forecast import WeatherForecast
from utils import ResponseValidator

@pytest.mark.smoke
@allure.feature("Schema Validation")
class TestWeatherSchema:

    @pytest.mark.schema
    @allure.story("Forecast Schema")
    def test_forecast_schema(self, forecast_api):
        response = forecast_api.get_forecast("Dubai", 5, include_key=True)
        ResponseValidator.validate_status_code(response, 200)
        forecast_data = ResponseValidator.validate_schema(response, WeatherForecast)
        assert len(forecast_data.forecast.forecastday) == 5
        assert forecast_data.location.name == "Dubai"
 