import  os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Environment:
    def __init__(self):
        self.env = os.getenv("ENV", "qa").lower()
        print(f"✅ Loaded ENV: {self.env}")
        print(f"🔑 Loaded API Key: {os.getenv('API_KEY')}")
        
    @property
    def base_url(self) -> str:
        default_url = "https://fakestoreapi.com/products"
        urls = {
            "qa": os.getenv("BASE_URL_QA", default_url),
            "staging": os.getenv("BASE_URL_STAGING", default_url),
            "prod": os.getenv("BASE_URL_PROD", default_url)
        }
        return urls.get(self.env, default_url)
    
    @property
    def api_key(self) -> str:
        return os.getenv("API_KEY", "test-key")
    
    @property
    def timeout(self) -> int:
        return int(os.getenv("TIMEOUT", "30"))

env = Environment()
 