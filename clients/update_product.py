import requests 

endpoint = "http://localhost:8000/api/product/1/"

data = {
    'name': "anananas",
    'price': 1000,
    'description': "fruit",
    'email': "konatebeh20@gmail.com",
}

response = requests.put(endpoint, json=data)   

print(response.json())

print(response.status_code)
