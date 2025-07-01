
#Clase empleado

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre            #Encapsulacion
        self.__salario = salario          #Encapsulacion

    def obtener_informacion(self):
        return f"Empleado:{self.__nombre}, Salario: ${self.__salario}"

    def obtener_salario(self):
        return self.__salario

    def actualizar_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario

#Herencia de empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

# Polimorfismo

    def obtener_informacion(self):
        return f"Gerente del departamento de {self.departamento}, " + super().obtener_informacion()

empleado1 = Empleado("Adrian", 500)
gerente1 = Gerente("Jorge", 1800, "Contabilidad")

print(empleado1.obtener_informacion())
print(gerente1.obtener_informacion())

empleado1.actualizar_salario(800)
print("Nuevo salario de Adrian:", empleado1.obtener_salario())