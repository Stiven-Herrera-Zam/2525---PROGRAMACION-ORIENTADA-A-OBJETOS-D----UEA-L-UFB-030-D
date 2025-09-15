import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Inventario Simple")
root.geometry("800x500")

# Lista para almacenar los productos temporalmente (en memoria)
productos = []


# Función para agregar un producto
def agregar_producto():
    nombre = entry_nombre.get().strip()
    cantidad = entry_cantidad.get().strip()
    precio = entry_precio.get().strip()

    if not nombre or not cantidad or not precio:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error", "Cantidad debe ser entero y Precio debe ser numérico")
        return

    # Agregar producto a la lista
    producto = [nombre, cantidad, precio]
    productos.append(producto)

    # Actualizar la tabla
    actualizar_tabla()

    # Limpiar campos
    limpiar_campos()

    # Guardar en CSV (opcional)
    guardar_en_csv()


# Función para actualizar la tabla
def actualizar_tabla():
    # Limpiar tabla existente
    for item in tabla.get_children():
        tabla.delete(item)

    # Insertar nuevos datos
    for i, producto in enumerate(productos):
        tabla.insert("", "end", values=(i + 1, producto[0], producto[1], producto[2]))


# Función para limpiar campos
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)


# Función para guardar en CSV
def guardar_en_csv():
    with open('inventario.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Cantidad", "Precio"])
        for producto in productos:
            writer.writerow(producto)


# Función para cargar datos desde CSV al iniciar
def cargar_desde_csv():
    if os.path.exists('inventario.csv'):
        with open('inventario.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                if row:  # Evitar filas vacías
                    productos.append([row[0], int(row[1]), float(row[2])])
        actualizar_tabla()


# Crear campos de entrada y etiquetas
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Nombre
tk.Label(frame_entrada, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_entrada, width=20)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# Cantidad
tk.Label(frame_entrada, text="Cantidad:").grid(row=0, column=2, padx=5, pady=5)
entry_cantidad = tk.Entry(frame_entrada, width=10)
entry_cantidad.grid(row=0, column=3, padx=5, pady=5)

# Precio
tk.Label(frame_entrada, text="Precio:").grid(row=0, column=4, padx=5, pady=5)
entry_precio = tk.Entry(frame_entrada, width=10)
entry_precio.grid(row=0, column=5, padx=5, pady=5)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Producto", command=agregar_producto, bg="lightgreen")
btn_agregar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar Campos", command=limpiar_campos, bg="lightcoral")
btn_limpiar.grid(row=0, column=1, padx=5)

# Tabla para mostrar productos
frame_tabla = tk.Frame(root)
frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

columnas = ("#", "Nombre", "Cantidad", "Precio")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

# Configurar columnas
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

# Barra de desplazamiento
scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Cargar datos existentes al iniciar
cargar_desde_csv()

# Ejecutar la aplicación
root.mainloop()