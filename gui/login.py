import tkinter as tk
from tkinter import messagebox
from auth import autenticar
from gui.dashboard import mostrar_dashboard

def iniciar_login():
    root = tk.Tk()
    root.title("Login - Restaurante")
    tk.Label(root, text="Usuario").grid(row=0, column=0)
    tk.Label(root, text="Contraseña").grid(row=1, column=0)
    entry_user = tk.Entry(root)
    entry_pw = tk.Entry(root, show="*")
    entry_user.grid(row=0, column=1)
    entry_pw.grid(row=1, column=1)
    def login():
        if autenticar(entry_user.get(), entry_pw.get()):
            root.destroy()
            mostrar_dashboard()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
    tk.Button(root, text="Ingresar", command=login).grid(row=2, column=0, columnspan=2, pady=5)
    root.mainloop()
