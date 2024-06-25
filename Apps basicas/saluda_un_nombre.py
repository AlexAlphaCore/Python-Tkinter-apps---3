import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola, {nombre}!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludar por Nombre")

# Crear un widget Label
etiqueta = tk.Label(ventana, text="Introduce tu nombre:", font=("Arial", 16))
etiqueta.pack(padx=20, pady=10)

# Crear un widget Entry para ingresar el nombre
entrada = tk.Entry(ventana, font=("Arial", 16))
entrada.pack(padx=20, pady=10)

# Crear un botón para saludar
boton = tk.Button(ventana, text="Saludar", font=("Arial", 16), command=saludar)
boton.pack(padx=20, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()