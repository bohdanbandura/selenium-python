import requests

BASE_URL = 'https://conduit.mate.academy/api'

headers = {
    'Authorization': ''
}

def get(endpoint: str):
    return requests.get(f"{BASE_URL}/{endpoint}")

def post(endpoint: str, body, token=False):
    if token:
        headers['Authorization'] = f'Token {token}'
    return requests.post(f"{BASE_URL}/{endpoint}", json=body, headers=headers)

def put(endpoint: str, body, token=False):
    if token:
        headers['Authorization'] = f'Token {token}'
    return requests.put(f"{BASE_URL}/{endpoint}", json=body, headers=headers)

def delete(endpoint: str, token=False):
    if token:
        headers['Authorization'] = f'Token {token}'
    return requests.delete(f"{BASE_URL}/{endpoint}", headers=headers)