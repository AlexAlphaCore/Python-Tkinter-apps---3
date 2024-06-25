import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hola Mundo")

# Configurar el fondo de la ventana a negro
ventana.configure(bg='black')

# Crear un widget Label con el texto "Hola Mundo", fuente Arial, color de fondo negro y color de texto blanco
etiqueta = tk.Label(ventana, text="Hola Mundo", font=("Arial", 16), bg='black', fg='white')
etiqueta.pack(padx=20, pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()