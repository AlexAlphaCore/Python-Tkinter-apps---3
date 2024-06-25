import tkinter as tk

def texto_a_binario():
    texto = entrada.get()
    binario = ' '.join(format(ord(char), '08b') for char in texto)
    salida.config(text=binario)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Texto a Binario")

# Crear un widget Label para la entrada
etiqueta_entrada = tk.Label(ventana, text="Introduce el texto:", font=("Arial", 12))
etiqueta_entrada.pack(padx=10, pady=5)

# Crear un widget Entry para la entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(padx=10, pady=5)

# Crear un botón para convertir el texto a binario
boton_convertir = tk.Button(ventana, text="Convertir a Binario", font=("Arial", 12), command=texto_a_binario)
boton_convertir.pack(padx=10, pady=10)

# Crear un widget Label para la salida
salida = tk.Label(ventana, text="", font=("Arial", 12))
salida.pack(padx=10, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()