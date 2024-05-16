import requests

class BaseApi:
    def __init__(self):
        self.base_url = 'https://conduit.mate.academy/api'
        self.headers = {'Authorization': ''}
        
    def get(self, endpoint, headers = None, status_code = 200):
        headers = headers if headers is not None else self.headers
        response = requests.get(f"{self.base_url}/{endpoint}", headers=headers)
        if response.status_code == status_code:
            return response.json()

    def post(self, endpoint, body, headers = None, status_code = 200):
        headers = headers if headers is not None else self.headers
        response = requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=body)
        if response.status_code == status_code:
            return response.json()

    def put(self, endpoint, body, headers = None, status_code = 200):
        headers = headers if headers is not None else self.headers
        response = requests.put(f"{self.base_url}/{endpoint}", headers=self.headers, json=body)
        if response.status_code == status_code:
            return response.json()

    def delete(self, endpoint, headers = None, status_code = 200):
        headers = headers if headers is not None else self.headers
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
        print(response.status_code)
        if response.status_code == status_code:
            return response        
        
