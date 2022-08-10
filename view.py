import sqlite3 as sql

mock_list =['John Doe', 'doe_john@gmail.com', 123456789, '01/01/2001', 'Active', 'Likes to play soccer.']

#criar conexão
conn = sql.connect('./database.db')

# Read
def read_data():
    query_list = []
    with conn:
        cursor = conn.cursor()
        query = "SELECT * FROM form"
        cursor.execute(query)
        info = cursor.fetchall()
        
        for i in info:
            query_list.append(i)

    return query_list


# Insert
def insert_data(i):
    with conn:
        cursor = conn.cursor()
        query = """INSERT INTO form (name, email, phone, birth_date, status, details) VALUES (?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, i)

# Update
def update_data(i):
    with conn:
        cursor = conn.cursor()
        query = """UPDATE form SET name=?, email=?, phone=?, birth_date=?, status=?, details=? WHERE id=?"""
        cursor.execute(query, i)


# Delete
def delete_data(i):
    with conn:
        cursor = conn.cursor()
        query = """DELETE FROM form WHERE id = ?"""
        cursor.execute(query, i)