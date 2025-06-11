# Función para ingresar temperaturas de cada día

def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    for dia in dias_semana:
        temp = float(input(f"Ingrese la temperatura del día {dia}:"))
        temperaturas.append(temp)
    return temperaturas

#Función para calcular el promedio de una lista de temperaturas

def calcular_promedio(temperaturas):
    suma = 0
    for temp in temperaturas:
        suma += temp
    promedio = suma / len(temperaturas)
    return promedio

#Función principal

def main():
    print("Programa para calcular el promedio semanal de temperaturas")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"/nEl promedio semanal de temperatutas es {promedio: .2f}°c ")

#Ejecutar el programa

main()








