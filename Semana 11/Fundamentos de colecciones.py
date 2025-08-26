import json   #Librería para guardar y leer archivos en formato JSON


#Clase producto     Representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        #Atributos basicos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

   #Representación en texto del prodcuto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


#Clase inventario   Administra una colección de prodcutos
class Inventario:
    def __init__(self):
        #Diccionario donde se guardarán los productos
        self.productos = {}

    #Metodo para añadir un producto nuevo al inventario
    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido con éxito.")

    #Metodo para eliminar un producto usando su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    #Metodo para actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    #Metodo para buscar un producto por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados

    #Metodo para mostrar todos los productos en el inventario
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    #Métodos de almacenamiento en archivos
    def guardar_en_archivos(self, archivo):
        with open(archivo, "w") as f:
            #Se guarda el diccionario con los atributos de cada producto
            json.dump({pid: vars(p) for pid, p in self.productos.items()}, f, indent=4)
            print("Inventario guardado en archivo.")

    #Cargar el inventario desde un archivo JSON
    def cargar_desde_archivos(self, archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                #Reconstruimos los objetos producto a partir de los datos del archivo
                self.productos = {pid: Producto(**p) for pid, p in datos.items()}
                print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo. Se creará uno nuevo.")


# Menú de usuario interactivo
def menu():
    inventario = Inventario()
    archivo = "inventario.json"
    #Intentar cargar datos anteriores del archivo
    inventario.cargar_desde_archivos(archivo)

    #Bucle principal del menú
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

        #Opcion 1 añadir producto
        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))

        #Opcion 2 eliminar producto
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        #Opcion 3 actualizar producto
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad_str = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio_str = input("Nuevo precio (deje en blanco para no cambiar): ")

            cantidad = int(cantidad_str) if cantidad_str else None
            precio = float(precio_str) if precio_str else None

            inventario.actualizar_producto(id_producto, cantidad=cantidad, precio=precio)

        #Opcion 4 buscar por nombre
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("Producto no encontrado.")

        #Opcion 5 mostrar todo
        elif opcion == "5":
            inventario.mostrar_todos()

        #Opcion 6 guardar inventario
        elif opcion == "6":
            inventario.guardar_en_archivos(archivo)

        #Opcion 7 salir
        elif opcion == "7":
            inventario.guardar_en_archivos(archivo)
            print("Saliendo del sistema.")
            break

    #Si el usuario pone otro valor
        else:
            print("Opción no válida. Intente de nuevo.")


# Llamada a la función principal
if __name__ == "__main__":
    menu()