# Sistema de una tienda online

# Clase cliente

class cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def realizar_Pedido(self,producto ):
        return f"{self.nombre} ha comprado {producto}."

cliente_1 = cliente("Angel", "Av. 09 de Octubre")
cliente_2 = cliente("Jordi", "Av. 15 de Noviembre")
print(cliente_1.realizar_Pedido("un computador"))

# Clase producto

class producto:
    def __init__(self,nombre,precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        if self.stock + cantidad >= 0:
            self.stock += cantidad
            return True
        return False

    def __str__(self):
        return f"producto: {self.nombre},Precio: ${self.precio}, stock: {self.stock}"

producto_1 = producto("Computador", 1500, 4)
producto_2 = producto("Ventilador", 45, 6 )

print("\nEstado actual de los productos:")
print(producto_1)
print(producto_2)




