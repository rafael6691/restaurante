import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'restaurante.db')

def ventana_clientes():
    window = tk.Toplevel()
    window.title("Clientes")
    listbox = tk.Listbox(window, width=60)
    listbox.pack(pady=5)
    def listar():
        listbox.delete(0, tk.END)
        conn = sqlite3.connect(DB_PATH)
        for id,nombre,email,telefono in conn.execute("SELECT id,nombre,email,telefono FROM clientes"):
            listbox.insert(tk.END, f"{id}: {nombre} - {email} - {telefono}")
        conn.close()
    def add():
        nombre = simpledialog.askstring("Nombre", "Nombre completo:")
        email = simpledialog.askstring("Email", "Correo electrónico:")
        telefono = simpledialog.askstring("Teléfono", "Teléfono (opcional):")
        if not nombre or not email: return
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO clientes (nombre,email,telefono) VALUES (?,?,?)", (nombre,email,telefono))
            conn.commit()
            conn.close()
            listar()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error","Email ya registrado")
    def edit():
        sel = listbox.get(listbox.curselection())
        id = sel.split(':')[0]
        nombre = simpledialog.askstring("Nombre","Nuevo nombre:")
        email = simpledialog.askstring("Email","Nuevo email:")
        telefono = simpledialog.askstring("Teléfono","Nuevo teléfono:")
        conn = sqlite3.connect(DB_PATH)
        conn.execute("UPDATE clientes SET nombre=?,email=?,telefono=? WHERE id=?", (nombre,email,telefono,id))
        conn.commit(); conn.close(); listar()
    def delete():
        sel = listbox.get(listbox.curselection())
        id = sel.split(':')[0]
        conn = sqlite3.connect(DB_PATH)
        conn.execute("DELETE FROM clientes WHERE id=?", (id,))
        conn.commit(); conn.close(); listar()
    tk.Button(window, text="Añadir", command=add).pack(side=tk.LEFT, padx=5)
    tk.Button(window, text="Editar", command=edit).pack(side=tk.LEFT, padx=5)
    tk.Button(window, text="Eliminar", command=delete).pack(side=tk.LEFT, padx=5)
    tk.Button(window, text="Historial", command=lambda: ver_historial(sel.split(':')[0])).pack(side=tk.LEFT, padx=5)
    listar()
def ver_historial(cliente_id):
    window = tk.Toplevel()
    window.title("Historial")
    listbox = tk.Listbox(window, width=60)
    listbox.pack(pady=5)
    conn = sqlite3.connect(DB_PATH)
    for r in conn.execute("SELECT fecha,hora,num_personas,estado FROM reservas WHERE cliente_id=? ORDER BY fecha", (cliente_id,)):
        listbox.insert(tk.END, f"{r[0]} {r[1]} - {r[2]} pers - {r[3]}")
    conn.close()
