import json
import os

class Producto:
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """Clase que representa un producto en el inventario."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self) -> dict:
        """Convierte el producto a diccionario (para guardar en JSON)."""
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data: dict):
        """Crea un objeto Producto desde un diccionario."""
        return Producto(
            data["id"], data["nombre"], data["cantidad"], data["precio"]
        )

    def __str__(self) -> str:
        return (f"ID: {self.id_producto}, "
                f"Nombre: {self.nombre}, "
                f"Cantidad: {self.cantidad}, "
                f"Precio: ${self.precio:.2f}")

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """Clase que gestiona el inventario y lo guarda en un archivo."""
        self.archivo = archivo
        self.productos = {}    #Diccionario de productos, clave = ID
        self.cargar_desde_archivo()   #Al iniciar, intentamos cargar productos desde archivo

    def guardar_en_archivo(self):
        """Guarda los productos en un archivo JSON."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:   #Abrimos el archivo en modo escritura

                # Convertimos los objetos productos es diccionario y guardamos en formato JSON
                json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
            print("Inventario guardado en archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:

            #Captura cualquier error inesperado y lo muestra
            print(f"Error inesperado al guardar: {e}")

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo si existe."""
        if not os.path.exists(self.archivo):

            #Si el archivo no existe, lo creamos vacio para evitar errores futuros
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
            self.guardar_en_archivo()
            return

        try:

            #Abrimos el archivo en modo lectura
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)  #Leemos y convertimos el JSON en una lista de diccionarios

                #Convertimos cada diccionario en un objeto producto
                self.productos = {p["id"]: Producto.from_dict(p) for p in data}
            print("Inventario cargado desde archivo.")
        except json.JSONDecodeError:

            #Esto ocurre si el archivo está vacío, corupto o no tiene un formato válido de JSON
            print("El archivo está corrupto o vacío, iniciando inventario nuevo.")
            self.productos = {}
        except Exception as e:

            #Capturamos cualquierer error inesperado
            print(f"Error inesperado al cargar inventario: {e}")

    def añadir_producto(self, producto: Producto):
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()  #Guardamos inmediatamente los cambios
            print("Producto añadido y guardado en archivo.")

    def eliminar_producto(self, id_producto: int):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado y cambios guardados en archivo.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None):
        producto = self.productos.get(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            self.guardar_en_archivo()
            print("Producto actualizado y guardado en archivo.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre: str):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Lista de productos en inventario:")
            for p in self.productos.values():
                print(p)

# Ejemplo de uso del programa
if __name__ == "__main__":
    inventario = Inventario()   #Se carga el inventario desde archivo si existe

    #Añadimos productos
    inventario.añadir_producto(Producto(155017, "Laptop Asus Vivobook", 10, 850.00))
    inventario.añadir_producto(Producto(248932, "Mouse", 50, 10.00))
    inventario.añadir_producto(Producto(364258, "Teclado", 30, 25.00))

    #Mostrar inventario
    inventario.mostrar_todos()

    #Buscar un producto por nombre
    inventario.buscar_por_nombre("Mouse")

    #Actualizar un producto existente
    inventario.actualizar_producto(248932, nueva_cantidad=30, nuevo_precio=12.99)

    #Eliminar un producto
    inventario.eliminar_producto(364258)

    #Mostrar inventario final
    inventario.mostrar_todos()