import requests 

endpoint = "http://localhost:8000/api/product/1/"

data = {
    'price': 2.9,
    
}

response = requests.patch(endpoint, json=data)   

print(response.json())

print(response.status_code)