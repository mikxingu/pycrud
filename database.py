import sqlite3 as sql

#criar conexão
conn = sql.connect('./database.db')

#criar tabela no db
with conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS form(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        birth_date DATE,
        status TEXT,
        details TEXT
    )""")
