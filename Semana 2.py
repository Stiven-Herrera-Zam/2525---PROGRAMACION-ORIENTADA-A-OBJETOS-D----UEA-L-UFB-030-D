class Persona:
    def __init__(self , nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
            print("Hola mucho gusto, mi nombre es", self.nombre)

#CREAR OBJETO

persona1 = Persona("Stiven", 20)
persona1.saludo()

class Estudiante(Persona):       ## Nota: HERENCIA
    def __init__(self , nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_info(self):
        print(f"{self.nombre} tiene {self.edad} años y estudia {self.carrera}")

#CREAR OBJETO

estudiante1 = Estudiante("Angel", 18, "Ing. TIC")
estudiante1.mostrar_info()

class CuentaBancaria:      ## Nota: ENCAPSULAMIENTO
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  ## Nota: atributo privado

    def mostrar_saldo(self):
        print("Saldo de" , self.titular, "es" , self.__saldo)

#CREAR OBJETO

cuenta = CuentaBancaria("Carlos" , 560)
cuenta.mostrar_saldo()

class Animal:    ## Nota: POLIMORFISMO
    def hablar(self):
        print("Hace sonidos")

class Perro(Animal):
    def hablar(self):
        print("ladra")

class Gato(Animal):
    def hablar(self):
        print("maulla")

#LISTA DE ANIMALES
animales = [Perro(), Gato(), Animal()]

for animal in animales:
    animal.hablar()







