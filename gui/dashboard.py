import tkinter as tk
from gui.clientes import ventana_clientes
from gui.reservas import ventana_reservas
from gui.disponibilidad import ventana_disponibilidad

def mostrar_dashboard():
    root = tk.Tk()
    root.title("Panel de Administración")
    tk.Button(root, text="Clientes", width=20, command=ventana_clientes).pack(pady=10)
    tk.Button(root, text="Reservas", width=20, command=ventana_reservas).pack(pady=10)
    tk.Button(root, text="Disponibilidad", width=20, command=ventana_disponibilidad).pack(pady=10)
    tk.Button(root, text="Salir", width=20, command=root.quit).pack(pady=10)
    root.mainloop()
