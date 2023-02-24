from fastapi import FastAPI
import sqlite3 as sql

app = FastAPI()

def db_insert(name: str, role: str): #add users to bd
    conn = sql.connect("website.db", check_same_thread=False)
    cursor = conn.cursor()
    # SQL Injection
    cursor.execute('INSERT INTO users (name, role) VALUES (?, ?)', (name, role))
    conn.commit()
    cursor.close()

def db_read():
    conn = sql.connect("website.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * from users')
    records = cursor.fetchall()
    cursor.close()
    return records

@app.get('/users/{user_id}')
def get_user(user_id: int):
    users = db_read()
    for user in users:        
        if user[0] == user_id: #user[0] this id in db
            return f"Welcome {user[1]}"



#uvicorn main:app --reload - start server

