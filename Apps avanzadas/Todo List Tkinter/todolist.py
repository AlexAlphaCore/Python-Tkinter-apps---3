import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="white")

        self.tasks = []

        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.frame, width=50, height=10, font=("Poppins", 12), fg="black", bg="white", yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, font=("Poppins", 12), fg="black", bg="white")
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Agregar Tarea", font=("Poppins", 12), fg="black", bg="white", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Eliminar Tarea", font=("Poppins", 12), fg="black", bg="white", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.calendar_button = tk.Button(self.root, text="Ver Calendario", font=("Poppins", 12), fg="black", bg="white", command=self.show_calendar)
        self.calendar_button.pack(pady=5)

        self.update_listbox()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "☑" if task["completed"] else "☐"
            self.listbox.insert(tk.END, f"{status} {task['task']}")
        self.listbox.bind('<Button-1>', self.toggle_task)

    def toggle_task(self, event):
        widget = event.widget
        index = widget.nearest(event.y)
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()

    def show_calendar(self):
        calendar_window = tk.Toplevel(self.root)
        calendar_window.title("Calendario")
        calendar = Calendar(calendar_window, selectmode='day', year=2023, month=4, day=1)
        calendar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()