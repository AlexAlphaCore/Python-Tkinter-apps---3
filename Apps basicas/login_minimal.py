import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    
    if usuario == "admin" and contrasena == "123":
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x150")

# Crear un widget Label para el usuario
etiqueta_usuario = tk.Label(ventana, text="Usuario:", font=("Arial", 12))
etiqueta_usuario.pack(padx=10, pady=5)

# Crear un widget Entry para el usuario
entrada_usuario = tk.Entry(ventana, font=("Arial", 12))
entrada_usuario.pack(padx=10, pady=5)

# Crear un widget Label para la contraseña
etiqueta_contrasena = tk.Label(ventana, text="Contraseña:", font=("Arial", 12))
etiqueta_contrasena.pack(padx=10, pady=5)

# Crear un widget Entry para la contraseña
entrada_contrasena = tk.Entry(ventana, show="*", font=("Arial", 12))
entrada_contrasena.pack(padx=10, pady=5)

# Crear un botón para iniciar sesión
boton_login = tk.Button(ventana, text="Iniciar Sesión", font=("Arial", 12), command=verificar_login)
boton_login.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()