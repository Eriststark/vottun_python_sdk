import requests
from .exceptions import VottunAPIException

class BaseClient:
    def __init__(self, api_key: str, app_id: str, base_url: str = 'https://api.vottun.tech'):
        self.api_key = api_key
        self.app_id = app_id
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "x-application-vkn": self.app_id,
            "Content-Type": "application/json"
        }

    def _make_request(self, endpoint: str, method: str, data: dict = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data, timeout=10)
        
        if response.status_code > 201:
            raise VottunAPIException(response.json().get('message', 'API request failed'))
        
        return response.json()
