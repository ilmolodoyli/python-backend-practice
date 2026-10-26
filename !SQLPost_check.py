import psycopg2 # пишу код для чтения данных
connection = psycopg2.connect(
    host = "127.0.0.1",
    user = "имя_sql",
    password = "пароль",
    database = "garage"
) # подключение к sql
cursor = connection.cursor()
cursor.execute("SELECT * FROM imported_climbers") # лезу в свою таблицу
all_climbers = cursor.fetchall() # вношу данные в переменную
print("Данные в базе PostgreSQL:")
for climber in all_climbers:
    print(f"ID: {climber[0]} Имя: {climber[1]} Почта: {climber[2]}") # вывожу айди имя и почту чтобы бог увидеть кто там находиться
connection.close() # закрываю 