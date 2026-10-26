import sqlite3
connection = sqlite3.connect("shop.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS TOOLS (name TEXT, price INTEGER)")
cursor.execute("INSERT INTO tools (name, price) VALUES ('Молоток', 500)")
connection.commit()
connection.close()
print("Инуструменты успешно добавлены в базу!")