import requests
from services.api.api_tests_logger import logger

class BaseApi:
    def __init__(self):
        self.base_url = 'https://conduit.mate.academy/api'
        self.headers = {'Authorization': ''}
        self.log_info = lambda method, url, headers, response: logger.info(f'\n{method} {url}\nHeaders - {headers}\nStatus code: {response.status_code}\nResponse: {response.text if method != "DELETE" else response}')
        
    def get(self, endpoint, headers = None, status_code = 200):
        url = f"{self.base_url}/{endpoint}"
        headers = headers if headers is not None else self.headers
        response = requests.get(url, headers=headers)
        self.log_info('GET', url, headers, response)
        if response.status_code == status_code:
            return response.json()

    def post(self, endpoint, body, headers = None, status_code = 200):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=body)
        self.log_info('POST', url, headers, response)
        if response.status_code == status_code:
            return response.json()

    def put(self, endpoint, body, headers = None, status_code = 200):
        url = f"{self.base_url}/{endpoint}"
        headers = headers if headers is not None else self.headers
        response = requests.put(url, headers=self.headers, json=body)
        self.log_info('PUT', url, headers, response)
        if response.status_code == status_code:
            return response.json()

    def delete(self, endpoint, headers = None, status_code = 200):
        url = f"{self.base_url}/{endpoint}"
        headers = headers if headers is not None else self.headers
        response = requests.delete(url, headers=self.headers)
        self.log_info('DELETE', url, headers, response)
        if response.status_code == status_code:
            return response        
        
