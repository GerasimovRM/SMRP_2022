from requests import get

base_url = "http://127.0.0.1:8000"
params = {"login": "mail", "password": "123"}
auth_request = get(f"{base_url}/login", params=params)
token = auth_request.json()["access_token"]

headers = {"Authorization": f"Bearer {token}"}
user_request = get(f"{base_url}/user/1", headers=headers)
print(user_request.json())