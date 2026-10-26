import psycopg2
connection = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="парольбро",
    database="garage",
)
cursor = connection.cursor()
cursor.execute("SELECT garage_bikes.model FROM riders JOIN garage_bikes ON riders.id = garage_bikes.rider_id WHERE riders.name = %s", ("Настя",))
db_results = cursor.fetchall()
for bike in db_results:
    print(f"Мотоцикл Насти: {bike[0]}")