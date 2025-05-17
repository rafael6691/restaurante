import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3, os
from datetime import datetime
from emailer import enviar_confirmacion

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'restaurante.db')

def ventana_reservas():
    window = tk.Toplevel()
    window.title("Reservas")
    listbox = tk.Listbox(window, width=80)
    listbox.pack(pady=5)
    def listar():
        listbox.delete(0, tk.END)
        conn = sqlite3.connect(DB_PATH)
        for r in conn.execute("SELECT r.id,c.nombre,m.id_mesa,r.fecha,r.hora,r.num_personas,r.estado FROM reservas r JOIN clientes c ON r.cliente_id=c.id JOIN mesas m ON r.mesa_id=m.id_mesa"):
            listbox.insert(tk.END, f"{r[0]}: {r[1]} - Mesa {r[2]} - {r[3]} {r[4]} - {r[5]} pers - {r[6]}")
        conn.close()
    def add():
        cliente_id = simpledialog.askinteger("Cliente ID","ID cliente:")
        fecha = simpledialog.askstring("Fecha","YYYY-MM-DD:")
        hora = simpledialog.askstring("Hora","HH:MM:")
        num = simpledialog.askinteger("Personas","Número de personas:")
        # disponibilidad
        conn = sqlite3.connect(DB_PATH)
        mesas = [m[0] for m in conn.execute("SELECT id_mesa FROM mesas WHERE capacidad>=? AND id_mesa NOT IN (SELECT mesa_id FROM reservas WHERE fecha=? AND hora=?)",(num,fecha,hora))]
        if not mesas:
            messagebox.showinfo("No hay mesas","No hay mesas disponibles")
            return
        mesa_id = mesas[0]
        conn.execute("INSERT INTO reservas (cliente_id,mesa_id,fecha,hora,num_personas,estado) VALUES (?,?,?,?,?,?)",(cliente_id,mesa_id,fecha,hora,num,"confirmada"))
        conn.commit()
        # enviar email
        c = conn.execute("SELECT email FROM clientes WHERE id=?", (cliente_id,)).fetchone()[0]
        enviar_confirmacion(c,"Reserva Confirmada",f"Reserva: {fecha} {hora}, mesa {mesa_id}, {num} personas")
        conn.close()
        listar()
    def edit():
        sel = listbox.get(listbox.curselection())
        rid = sel.split(':')[0]
        # similar a add: reask fields...
        messagebox.showinfo("Info","Función editar no implementada")
    def cancel():
        sel = listbox.get(listbox.curselection()); rid = sel.split(':')[0]
        conn = sqlite3.connect(DB_PATH)
        conn.execute("UPDATE reservas SET estado='cancelada' WHERE id=?", (rid,))
        conn.commit(); conn.close(); listar()
    tk.Button(window, text="Nueva", command=add).pack(side=tk.LEFT,padx=5)
    tk.Button(window, text="Cancelar", command=cancel).pack(side=tk.LEFT,padx=5)
    listar()
