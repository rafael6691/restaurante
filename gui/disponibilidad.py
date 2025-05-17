import tkinter as tk
import sqlite3, os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'restaurante.db')

def ventana_disponibilidad():
    window = tk.Toplevel()
    window.title("Disponibilidad")
    tk.Label(window, text="Fecha (YYYY-MM-DD)").pack(); e1=tk.Entry(window); e1.pack()
    tk.Label(window, text="Hora (HH:MM)").pack(); e2=tk.Entry(window); e2.pack()
    listbox = tk.Listbox(window, width=60); listbox.pack(pady=5)
    def check():
        listbox.delete(0, tk.END)
        fecha, hora = e1.get(), e2.get()
        conn = sqlite3.connect(DB_PATH)
        total = conn.execute("SELECT COUNT(*) FROM mesas").fetchone()[0]
        ocup = conn.execute("SELECT COUNT(*) FROM reservas WHERE fecha=? AND hora=? AND estado='confirmada'",(fecha,hora)).fetchone()[0]
        free = total-ocup
        listbox.insert(tk.END, f"Mesa totales: {total}, ocupadas: {ocup}, libres: {free}")
        conn.close()
    tk.Button(window, text="Consultar", command=check).pack(pady=5)
