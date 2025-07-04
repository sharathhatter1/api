from  typing import Type, Dict, Any
from pydantic import BaseModel, ValidationError
import allure

class ResponseValidator:
    @staticmethod
    def validate_status_code(response, expected_status: int, message: str = None):
        actual_status = response.status_code
        error_msg = message or f"Expected status {expected_status}, got {actual_status}"
        
        with allure.step(f"Validate status code: {expected_status}"):
            assert actual_status == expected_status, error_msg
    
    @staticmethod
    def validate_schema(response, model: Type[BaseModel], message: str = None):
        try:
            with allure.step(f"Validate response schema: {model.__name__}"):
                return model(**response.json())
        except ValidationError as e:
            error_msg = message or f"Schema validation failed: {e}"
            raise AssertionError(error_msg)
    
    @staticmethod
    def validate_json_contains(response, expected_data: Dict[str, Any]):
        actual_data = response.json()
        with allure.step("Validate response contains expected data"):
            for key, value in expected_data.items():
                assert key in actual_data, f"Key '{key}' not found in response"
                assert actual_data[key] == value, f"Expected {key}={value}, got {actual_data[key]}"
 