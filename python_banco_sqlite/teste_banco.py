import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""CREATE DATABASE users(
    id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOOT NULL,
    pontos INTEGER,
    cpf TEXT NOT NULL UNIQUE
)
""")

connect.commit()
