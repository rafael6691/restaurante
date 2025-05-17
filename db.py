import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def init_db():
    db_folder = os.path.join(BASE_DIR, "data")
    os.makedirs(db_folder, exist_ok=True)
    db_path = os.path.join(db_folder, "restaurante.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS mesas (
        id_mesa INTEGER PRIMARY KEY AUTOINCREMENT,
        capacidad INTEGER,
        estado TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT UNIQUE,
        telefono TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        mesa_id INTEGER,
        fecha TEXT,
        hora TEXT,
        num_personas INTEGER,
        estado TEXT,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id),
        FOREIGN KEY(mesa_id) REFERENCES mesas(id_mesa)
    )""")
    conn.commit()
    conn.close()
