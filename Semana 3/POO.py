class RegistroClima:
    def __init__(self):
        self.temperaturas = []
        self.dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    def ingresar_temperaturas(self):
        for dia in self.dias_semana:
            temp = float(input(f"Ingrese la temperatura del dia {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"/nEl Promedio semanal de temperaturas es: {promedio: .2f}°C")

# Crear un objeto de la clase y crear un programa

def main():
    print("Programa con POO para calcular el promedio semanal de temperaturas")
    clima = RegistroClima()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()

main()

