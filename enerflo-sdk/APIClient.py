import requests


class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get(self, endpoint, params=None):
        headers = {'api-key': self.api_key}
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return response.json()
