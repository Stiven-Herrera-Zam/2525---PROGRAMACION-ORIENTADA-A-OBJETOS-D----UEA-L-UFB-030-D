class Producto:

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor que inicializa la clase producto

        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    #Getters
    def get_id(self):
        return self.id_producto   # Retorna el id del producto
    def get_nombre(self):
        return self.nombre        # Retorna el nombre
    def get_cantidad(self):
        return self.cantidad      # Retorna la cantidad
    def get_precio(self):
        return self.precio        # Retorna el precio

    #Setters
    def set_nombre(self, nombre):
        self.nombre = nombre      # Actualiza el nombre del producto
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad  # Actualiza la cantidad del producto
    def set_precio(self, precio):
        self.precio = precio      # Actualiza el precio del producto
    def __str__(self):       # Representación en cadena del producto para impresión amigable
        return (f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}")

class Inventario:

    def __init__(self):      # Inicializa la lista vacia donde se almacenaran los productos
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID del prodcuto sea único antes de agregar.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self,id_producto):
        """
        Elimina un producto del inventario usando su ID.
        Si el producto no existe, muestra un mensaje de error.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None,nuevo_precio=None):
        """
        Actualiza la cantidad y/o precio de un producto dado su ID.
        Si alguna de las actualizaciones no se especifica, se mantiene el valor actual.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                    print("Producto actualizado correctamente.")
                    return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
         Busca productos cuyo nombre contenga la cadena especificada (no sensible a mayúsculas).
        Muestra todos los productos encontrados o un mensaje si no hay coincidencias.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """
        Muestra todos los productos que existen actualmente en el inventario.
        Si no hay productos, indica que el inventario está vacío.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Lista de productos en inventario:")
            for p in self.productos:
                print(p)


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    # Añadir productos
    inventario.añadir_producto(Producto(155017, "Laptop Asus Vivobook", 10, 850.00))
    inventario.añadir_producto(Producto(248932, "Mouse", 50, 10.00))
    inventario.añadir_producto(Producto(364258, "Teclado", 30, 25.00))
    print("Productos añadidos correctamente.")
    # Mostrar inventario
    inventario.mostrar_todos()

    # Buscar producto
    inventario.buscar_por_nombre("Mouse")

    # Actualizar producto
    inventario.actualizar_producto(248932, nueva_cantidad=30, nuevo_precio=12.99)

    # Eliminar producto
    inventario.eliminar_producto(364258)

    # Mostrar inventario final
    inventario.mostrar_todos()












