import requests 

endpoint = "http://localhost:8000/api/product/2/"



response = requests.get(endpoint)   

print(response.json())

print(response.status_code)