# задача, написать микросервисс для скалодрома, использовать буду fastapi requests и postgresql (сначало импортирую фаст и req, uvi тоже)
import uvicorn
from fastapi import FastAPI
import requests # теперь добовляю sqlpost (сначало написал запрос и удостоврился в том что все получаю)
import psycopg2
app = FastAPI()
@app.post("/import/{user_id}") # условно создаю сайт(маршрут-табличку) по которой будет вся информация о человеке
                       # int означает числовое значение, мол преращает 5 именно в число а не слово "5" str-слова + защита чтобы не упала система
def import_user(user_id: int): # принятие будет только в виде чисел
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url) # гет запрос на получение данных
    data = response.json() # переделываю из json
    name = data['name'] # закидываю данные в переменную
    email = data['email'] # анологично 
    # return {"Статус": name, "Почта": email, "Статус": "Данные успешно получены"} # заканчиваю функцию и закидываю в словарь питона(убрал конец функции: она была как проверочная)
    connection = psycopg2.connect( # подключаюсь к своей бд
        host="127.0.0.1",
        user="имя_sql",
        password="пароль",
        database="garage",
)
    cursor = connection.cursor() # создаю курс для управления 
    cursor.execute("CREATE TABLE IF NOT EXISTS imported_climbers (id SERIAL, name TEXT, email TEXT)") # создаю таблицу и даю id с помощью внутренней команды serial не integer.
    cursor.execute("INSERT INTO imported_climbers (name, email) VALUES (%s, %s)", (name, email)) # команда для добавления информации в таблицу, VALUES чтобы он сам распределил информацию по полочкам, как ? mysql
    connection.commit() # сохроняю
    connection.close() # закрываю
    return {"Статус": "Данные успешно скачены и сохранены в базу PostgreSQL"} # закрываю функцию и добовляю вывод конечного результата
if __name__ == "__main__":
    uvicorn.run("!SQLPost_REQ_FASTAPI:app", host = "127.0.0.1", port=8000, reload=True) # создаю сервер от моего лица