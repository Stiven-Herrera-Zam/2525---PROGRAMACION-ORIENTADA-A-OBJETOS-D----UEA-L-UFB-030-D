
import tkinter as tk
from tkinter import messagebox, font, ttk

#Creamos una clase que agrupe la ventana, los widgets y la lista de tareas.
class TaskApp:

    def __init__(self,root):
        self.root = root
        self.root.title("Gestion de Tareas con Atajos de Teclado")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        #Lista vacia para almacenar datos
        self.tasks = []

        #Fuentes para estilo visual normal y tachado.
        self.font_normal = font.Font(family = "Helvetica", size = 11)  #Tareas pendientes
        self.font_strike = font.Font(family = "Helvetica", size = 11, overstrike = 1)  #Tareas completadas

        #Crear widgets y atajos
        self.create_widgets()   #Crea y configura todos los elementos visuales de la interfaz
        self.bind_shortcuts()   #Configura los atajos de teclado y eventos como Enter, Escape, etc.

        #Primera renderización
        self.refresh_task_list()  #Para actualizar y volver a dibujar la lista de tareas

    def create_widgets(self):
        #Frame de entrada
        frame_top = tk.Frame(self.root)
        frame_top.pack(padx=10, pady=(10, 6), fill="x")

        self.entry = tk.Entry(frame_top, font=self.font_normal)
        self.entry.pack(side="left", expand=True, fill="x", padx=(0, 6))
        self.entry.focus_set()

        btn_add = tk.Button(frame_top, text="Añadir", width=10, command=self.add_task)
        btn_add.pack(side="left")

        #vincula la tecla Enter (Return) al metodo self.add_task en el campo de entrada.
        self.entry.bind("<Return>", self.add_task)

        #Frame de lista para mostrar las tareas usando Listbox y Scrollbar
        frm_list = tk.Frame(self.root)
        frm_list.pack(padx=10, pady=(0, 6), fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(frm_list, orient="vertical")
        self.listbox = tk.Listbox(frm_list, activestyle="none", selectmode=tk.SINGLE,
                              yscrollcommand=self.scrollbar.set, font=self.font_normal, height=12)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="left", fill="y")

        #Vincula el doble clic en la lista de tareas
        self.listbox.bind("<Double-Button-1>", lambda e: self.toggle_task())

        #Frame de botones de acción
        frm_actions = tk.Frame(self.root)
        frm_actions.pack(padx=10, pady=(6, 10), fill="x")

        btn_toggle = tk.Button(frm_actions, text="Marcar/Desmarcar (C)", command=self.toggle_task)
        btn_toggle.pack(side="left", padx=(0, 6))

        btn_delete = tk.Button(frm_actions, text="Eliminar (D / Del)", command=self.delete_task)
        btn_delete.pack(side="left", padx=(0, 6))

        #Label con contador que muestra información sobre las tareas
        self.lbl_status = tk.Label(frm_actions, text="0 tareas", anchor="e")
        self.lbl_status.pack(side="right")

    #Agregar tareas
    def add_task(self, event=None):
        text = self.entry.get().strip()
        if not text:
            # Evitar tareas vacías
            return
        # Añadir a la estructura
        self.tasks.append({'text': text, 'done': False})
        # Limpiar entrada y actualizar UI
        self.entry.delete(0, tk.END)
        self.refresh_task_list()
        self.entry.focus_set()

    #Actualizar y sincronizar la visualización
    def refresh_task_list(self):
        self.listbox.delete(0, tk.END)   #Elimina todos los items existentes en la Listbox
        #Poblar con tareas actualizadas
        for i, task in enumerate(self.tasks):
            display = task['text']
            if task['done']:
                display = "✓ " + display
            self.listbox.insert(tk.END, display)
            #Aplicar estilos visuales
            try:
                if task['done']:
                    self.listbox.itemconfig(i, fg="gray50", font=self.font_strike)
                else:
                    self.listbox.itemconfig(i, fg="black", font=self.font_normal)
            except Exception:
                # Si itemconfig no está disponible en la plataforma, solo dejamos el prefijo ✓
                pass

        # Actualizar contador de estado
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t['done'])
        self.lbl_status.config(text=f"{total} tareas — {done} completadas")

    #obtiene el índice de la tarea seleccionada en la Listbox
    def get_selected_index(self):
        sel = self.listbox.curselection()
        if not sel:
            return None
        return sel[0]

    #Marca/desmarca una tarea como completada
    def toggle_task(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo("Selecciona una tarea", "Por favor selecciona una tarea para marcar/desmarcar.")
            return
        self.tasks[idx]['done'] = not self.tasks[idx]['done']
        self.refresh_task_list()
        # Mantener la selección en el mismo índice (si existe)
        if idx < len(self.tasks):
            self.listbox.selection_set(idx)

    # elimina una tarea con confirmación del usuario
    def delete_task(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo("Selecciona una tarea", "Por favor selecciona una tarea para eliminar.")
            return
        task_text = self.tasks[idx]['text']
        if messagebox.askyesno("Confirmar eliminación", f"¿Eliminar la tarea?\n\n{task_text}"):
            del self.tasks[idx]
            self.refresh_task_list()

    #configura atajos de teclado globales para la aplicación
    def bind_shortcuts(self):
        # Bind global de teclas: usamos <Key-...>. Comprobamos foco en el handler para ignorar cuando se escribe en Entry.
        # Atajos para marcar/desmarcar: tecla 'c' o 'C'
        self.root.bind("<Key-c>", lambda e: self.on_shortcut(e, "toggle"))
        self.root.bind("<Key-C>", lambda e: self.on_shortcut(e, "toggle"))
        # Atajos para eliminar: 'd', 'D', y la tecla Delete
        self.root.bind("<Key-d>", lambda e: self.on_shortcut(e, "delete"))
        self.root.bind("<Key-D>", lambda e: self.on_shortcut(e, "delete"))
        self.root.bind("<Delete>", lambda e: self.on_shortcut(e, "delete"))
        # Atajo para cerrar: Escape
        self.root.bind("<Escape>", lambda e: self.on_shortcut(e, "escape"))

    #Maneja los atajos de teclado con lógica inteligente para evitar conflictos
    def on_shortcut(self, event, action):
        #Detectar widget con foco
        focused = self.root.focus_get()
        #Lógica de filtrado inteligente
        if focused == self.entry and action != "escape":
            return
        #Ejecutar acciones
        if action == "toggle":
            self.toggle_task()
        elif action == "delete":
            self.delete_task()
        elif action == "escape":
            self.close_app()

    #Cierra la aplicación de manera directa sin confirmación
    def close_app(self):
        self.root.destroy()

#Punto de entrada principal de la aplicación Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
