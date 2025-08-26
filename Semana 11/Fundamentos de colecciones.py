import json


# Clase producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Métodos de almacenamiento
    def guardar_en_archivos(self, archivo):
        with open(archivo, "w") as f:
            json.dump({pid: vars(p) for pid, p in self.productos.items()}, f, indent=4)
            print("Inventario guardado en archivo.")

    def cargar_desde_archivos(self, archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {pid: Producto(**p) for pid, p in datos.items()}
                print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo. Se creará uno nuevo.")


# Menú de usuario
def menu():
    inventario = Inventario()
    archivo = "inventario.json"
    inventario.cargar_desde_archivos(archivo)

    while True:
        print("\n=== MENÚ INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad_str = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio_str = input("Nuevo precio (deje en blanco para no cambiar): ")

            cantidad = int(cantidad_str) if cantidad_str else None
            precio = float(precio_str) if precio_str else None

            inventario.actualizar_producto(id_producto, cantidad=cantidad, precio=precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivos(archivo)

        elif opcion == "7":
            inventario.guardar_en_archivos(archivo)
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Llamada a la función principal
if __name__ == "__main__":
    menu()