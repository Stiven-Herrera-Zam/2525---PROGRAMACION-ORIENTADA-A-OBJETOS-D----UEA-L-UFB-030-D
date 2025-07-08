class VentaVehiculo:

# Constructor

    def __init__(self, modelo, año, precio):
        self.modelo = modelo
        self.año = año
        self.precio = precio
        print(f"Vehiculo {self.modelo} registrado correctamente.")

# Metodo

    def mostrar_información(self):
        print("Información del Vehiculo")
        print(f"modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio:$ {self.precio:,.2f}")

# Destructor

    def __del__(self):
        print(f"Vehiculo '{self.modelo}' eliminado del sistema.")

# Instanciación del objeto

vehiculo1 = VentaVehiculo("Suzuki Forza 2", 1993, 4500)
vehiculo2 =  VentaVehiculo("Chevrolet Captiva", 2006, 6400)

# llamada al metodo mostrar informacion

vehiculo1.mostrar_información()

# Eliminacion del objeto

del vehiculo1


