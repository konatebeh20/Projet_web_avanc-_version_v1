import requests 

endpoint = "http://localhost:8000/api/product/"

data = {
    'name': "anananas",
    'price': 1000,
    'description': "fruit",
    'email': "konatebeh20@gmail.com",
}

response = requests.post(endpoint, json=data)   

print(response.json())

print(response.status_code)
