import requests

response = requests.get("https://api.github.com")
print("satus code: ", response.status_code)
