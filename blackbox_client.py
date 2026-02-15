import requests

response = requests.post("http://localhost:8000/auth")

print("Status Code:", response.status_code)
print("Response Body:", response.json())
