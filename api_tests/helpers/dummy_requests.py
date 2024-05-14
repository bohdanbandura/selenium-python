import requests

BASE_URL = 'https://dummyapi.io/data/v1'

headers = { 'app-id': '664227d4bc921f48748be8db' }

def get(endpoint: str):
    return requests.get(f"{BASE_URL}/{endpoint}", headers=headers)

def post(endpoint: str, body):
    return requests.post(f"{BASE_URL}/{endpoint}", headers=headers, data=body)

def put(endpoint: str, body):
    return requests.put(f"{BASE_URL}/{endpoint}", data=body)

def delete(endpoint: str):
    return requests.delete(f"{BASE_URL}/{endpoint}", headers=headers)