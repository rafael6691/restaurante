import sqlite3
import hashlib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'restaurante.db')

def crear_usuario(username, password):
    hash_pw = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect(DB_PATH) as conn:
        try:
            conn.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hash_pw))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

def autenticar(username, password):
    hash_pw = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, hash_pw))
        return cursor.fetchone() is not None
