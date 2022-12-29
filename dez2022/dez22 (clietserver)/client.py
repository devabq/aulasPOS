import requests

user_id = 1

apiUrl = f"http://localhost:5000/users/{user_id}"
response = requests.get(apiUrl)
print(response.json())
