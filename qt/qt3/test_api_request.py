import requests


response = requests.get("https://jsonplaceholder.typicode.com/users").json()
for user in response:
    print(user)