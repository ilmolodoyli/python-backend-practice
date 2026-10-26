from fastapi import FastAPI
import uvicorn
import sqlite3
app = FastAPI()
@app.get("/users")
def get_all_users():
    conection = sqlite3.connect("client.db")
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM users")
    users_data = cursor.fetchall()
    conection.close()
    return {"clients": users_data}
if __name__ == "__main__":
    uvicorn.run("client:app", host="127.0.0.1", port=8000, reload=True)
