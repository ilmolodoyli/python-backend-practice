import requests
url = f"https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
for user in data:
    name = user['name']
    email = user['email']
    town = user['address']['city']
    print(f"Имя: {name}, Email: {email}, Город: {town}.")