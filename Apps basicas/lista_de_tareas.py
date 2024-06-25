import tkinter as tk
from tkinter import messagebox

# Lista para almacenar las tareas
tareas = []

# Agregar una tarea a la lista
def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        tareas.append(tarea)
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

# Eliminar una tarea de la lista
def eliminar_tarea():
    try:
        seleccionado = lista_tareas.get(lista_tareas.curselection())
        tareas.remove(seleccionado)
        actualizar_lista()
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

# Actualizar la lista de tareas en la interfaz
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Crear un widget Frame para organizar los widgets
frame = tk.Frame(ventana)
frame.pack(pady=10)

# Crear un widget Listbox para mostrar las tareas
lista_tareas = tk.Listbox(frame, width=50, height=10, font=("Arial", 12))
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear un widget Scrollbar para la Listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Configurar la Listbox para usar el Scrollbar
lista_tareas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tareas.yview)

# Crear un widget Entry para ingresar nuevas tareas
entrada = tk.Entry(ventana, font=("Arial", 12), width=40)
entrada.pack(pady=10)

# Crear un botón para agregar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", font=("Arial", 12), command=agregar_tarea)
boton_agregar.pack(pady=5)

# Crear un botón para eliminar tareas
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", font=("Arial", 12), command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Actualizar la lista de tareas al iniciar la aplicación
actualizar_lista()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()