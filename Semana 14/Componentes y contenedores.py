import tkinter as tk
from importlib.metadata import entry_points
from tkinter import ttk, messagebox

#Crear la ventana Principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("800x450")

#Crear Frames (Marcos o Secciones)
frame_eventos = ttk.Frame(root)                     #contiene la lista de eventos.
frame_eventos.pack(fill = "both", expand = True, padx = 10, pady = 10)

frame_formulario = ttk.Frame(root)                  #Contiene los campos de fecha, hora y descripción.
frame_formulario.pack(fill = "x", padx = 10, pady = 5)

frame_botones = ttk.Frame(root)                     #Contiene los botones agregar, eliminar y salir.
frame_botones.pack(fill = "x", padx = 10, pady = 5)

#Lista de eventos
columnas = ("fecha", "hora", "descripcion")
tree = ttk.Treeview(frame_eventos, columns = columnas, show = "headings")

tree.heading("fecha", text = "Fecha")
tree.heading("hora", text = "Hora")
tree.heading("descripcion", text = "Descripción")

tree.pack(fill = "both", expand = True)

#Campos de Entrada
                         #Fecha
ttk.Label(frame_formulario, text = "Fecha (dia, mes, año):").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
entry_fecha = ttk.Entry(frame_formulario)
entry_fecha.grid(row = 0, column = 1, padx = 5, pady = 5)
                         #Hora
ttk.Label(frame_formulario, text = "Hora (Hora: Minutos):").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
entry_hora = ttk.Entry(frame_formulario)
entry_hora.grid(row = 1, column = 1, padx = 5, pady = 5)
                         #Descripción
ttk.Label(frame_formulario, text = "Descripción:").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
entry_descripcion = ttk.Entry(frame_formulario)
entry_descripcion.grid(row = 2, column = 1, padx = 5, pady = 5)

#Funciones
def agregar_evento():
    fecha = entry_fecha.get().strip()
    hora = entry_hora.get().strip()
    descripcion = entry_descripcion.get().strip()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
        return
    tree.insert("", "end", values = (fecha, hora, descripcion))

    #Limpiar entradas
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

def eliminar_eventos():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning ("Sin seleccion", "Selecciona un evento para eliminar.")
        return
    confirmar = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento seleccionado?")
    if confirmar:
        for item in seleccion:
            tree.delete(item)

def salir():
    root.destroy()

#Botones
btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side="left", padx=5)

btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_eventos)
btn_eliminar.pack(side="left", padx=5)

btn_salir = ttk.Button(frame_botones, text="Salir", command=salir)
btn_salir.pack(side="right", padx=5)


root.mainloop()











