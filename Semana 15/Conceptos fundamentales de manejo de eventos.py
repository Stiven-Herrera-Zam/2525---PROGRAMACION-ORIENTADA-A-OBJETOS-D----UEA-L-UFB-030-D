import tkinter as tk
from tkinter import messagebox, ttk

#Defino una clase
class ListaTareasApp:
    def __init__(self):

        # Crear ventana principal
        #Self se usa cuando tenemos clases
        self.ventana = tk.Tk()
        self.ventana.title("Lista de Tareas")
        self.ventana.geometry("600x450")
        self.ventana.configure(bg='#f0f0f0')

        #Lista para almacenar las tareas
        self.tareas = []

        #Crear interfaz
        self.crear_interfaz()

        #Vincular evento con la tecla enter
        self.ventana.bind('<Return>',lambda event: self.añadir_tareas())

    def crear_interfaz(self):
        #Frame principal
        main_frame = tk.Frame(self.ventana, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Título
        titulo = tk.Label(main_frame, text="LISTA DE TAREAS",
                          font=('Arial', 16, 'bold'), bg='#f0f0f0')
        titulo.pack(pady=10)

        # Frame de entrada
        frame_entrada = tk.Frame(main_frame, bg='#f0f0f0')
        frame_entrada.pack(fill='x', pady=10)

        # Campo de entrada
        self.entrada_tarea = tk.Entry(frame_entrada, font=('Arial', 12), width=30)
        self.entrada_tarea.pack(side='left', padx=(0, 10))
        self.entrada_tarea.focus()  # Poner foco automáticamente

        # Botón Añadir
        btn_añadir = tk.Button(frame_entrada, text="➕ Añadir",
                               command=self.añadir_tarea,
                               bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
        btn_añadir.pack(side='left')

        # Frame de botones
        frame_botones = tk.Frame(main_frame, bg='#f0f0f0')
        frame_botones.pack(fill='x', pady=10)

        # Botón Marcar Completada
        btn_completar = tk.Button(frame_botones, text="Completada",
                                  command=self.marcar_completada,
                                  bg='#2196F3', fg='white', font=('Arial', 10, 'bold'))
        btn_completar.pack(side='left', padx=(0, 10))

        # Botón Eliminar
        btn_eliminar = tk.Button(frame_botones, text="Eliminar",
                                 command=self.eliminar_tarea,
                                 bg='#f44336', fg='white', font=('Arial', 10, 'bold'))
        btn_eliminar.pack(side='left')

        # Lista de tareas (Listbox)
        frame_lista = tk.Frame(main_frame, bg='#f0f0f0')
        frame_lista.pack(fill='both', expand=True, pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side='right', fill='y')

        # Listbox para mostrar tareas
        self.lista_tareas = tk.Listbox(frame_lista, font=('Arial', 12),
                                       yscrollcommand=scrollbar.set,
                                       selectbackground='#E3F2FD',
                                       selectmode='single')
        self.lista_tareas.pack(side='left', fill='both', expand=True)

        # Vincular scrollbar
        scrollbar.config(command=self.lista_tareas.yview)

        # Vincular doble clic para marcar como completada
        self.lista_tareas.bind('<Double-Button-1>', lambda event: self.marcar_completada())

        # Información
        info = tk.Label(main_frame, text="Doble clic en una tarea para marcarla como completada",
                        font=('Arial', 9), bg='#f0f0f0', fg='#666')
        info.pack(pady=5)

    def añadir_tarea(self):
        """Añade una nueva tarea a la lista"""
        texto = self.entrada_tarea.get().strip()

        if texto:  # Verificar que no esté vacío
            # Añadir a la lista interna
            self.tareas.append({"texto": texto, "completada": False})

            # Añadir a la Listbox
            self.lista_tareas.insert(tk.END, f"○ {texto}")

            # Limpiar campo de entrada
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada"""
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]

            # Actualizar estado en la lista interna
            self.tareas[indice]["completada"] = True

            # Actualizar visualización en Listbox
            texto_original = self.tareas[indice]["texto"]
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, f"{texto_original}")

            # Deseleccionar
            self.lista_tareas.selection_clear(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]

            # Confirmar eliminación
            respuesta = messagebox.askyesno(
                "Confirmar",
                f"¿Eliminar la tarea: '{self.tareas[indice]['texto']}'?"
            )

            if respuesta:
                # Eliminar de ambas listas
                self.tareas.pop(indice)
                self.lista_tareas.delete(indice)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()

    # Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = ListaTareasApp()
    app.ejecutar()
