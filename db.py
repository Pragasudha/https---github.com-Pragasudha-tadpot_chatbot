import sqlite3

def init_db():
    conn = sqlite3.connect("data/tadpot.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()
