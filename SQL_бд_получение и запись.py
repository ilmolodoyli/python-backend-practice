import sqlite3
import requests
connection = sqlite3.connect("doi.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT)")
url = "https://jsonplaceholder.typicode.com/users"
gogo = requests.get(url)
hoho = gogo.json()
for hil in hoho:
    user_name = hil['name']
    user_email = hil['email']
    cursor.execute("INSERT INTO users (name, email) VALUES (?,?)", (user_name, user_email))
cursor.execute("SELECT * FROM users")
namess = cursor.fetchall()
for joj in namess:
    print(joj[0], joj[1])
connection.commit()
connection.close()