import  requests
from typing import Optional, Dict, Any
from config import env
import allure
import urllib.parse


class HTTPClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or env.base_url
        self.session = requests.Session()
        self.default_headers = {
            "Content-Type": "application/json"        }
        
    
    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        print("shatter here")
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
        headers.update(self.default_headers)
        print(f"🔸 Headers: {url}")

        # 👇 Build final URL including query parameters
        final_url = url
        if "params" in kwargs:
            final_url += "?" + urllib.parse.urlencode(kwargs["params"])

        # ✅ Print full request
        print(f"\n➡️ Making {method.upper()} request to: {final_url}")
        print(f"🔸 Headers: {headers}")
        if 'json' in kwargs:
            print(f"🔸 Body: {kwargs['json']}")

        with allure.step(f"{method.upper()} {final_url}"):
            response = self.session.request(
                method=method,
                url=url,  # actual request URL should not include params manually
                headers=headers,
                timeout=env.timeout,
                **kwargs
            )
            print(f"📨 Actual request sent: {response.request.url}")  # <-- ADD THIS LINE
            print(f"🔁 Status code: {response.status_code}")
            print(f"📥 Response: {response.text}")
            allure.attach(
                f"Status: {response.status_code}\nResponse: {response.text}",
                name="Response",
                attachment_type=allure.attachment_type.TEXT
            )
            return response
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("PUT", endpoint, **kwargs)
    
    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("PATCH", endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)
 