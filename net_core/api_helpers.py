import requests

def make_api_request(url, headers=None, data=None, method="GET"):
    response = requests.request(method, url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()