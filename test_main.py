import requests

url = "http://127.0.0.1:5000/post-data"
# url = "https://randomsubdomain.ngrok.io/post-data"
data = {"name": "Alice", "age": 25}

response = requests.post(url, json=data)
print(response.json())