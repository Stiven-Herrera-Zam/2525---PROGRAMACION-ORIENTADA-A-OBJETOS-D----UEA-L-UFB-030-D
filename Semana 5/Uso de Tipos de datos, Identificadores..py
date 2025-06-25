# Programa para calcular la edad de una persona

from datetime import date
def calcular_edad(año_nacimiento):
    año_actual = date.today().year
    edad = año_actual - año_nacimiento
    return edad

# Entrada del usuario

nombre_persona = input("Ingrese el nombre de la persona: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# proceso

edad_persona = calcular_edad(año_nacimiento)
print("Hola,",nombre_persona)
print("Tu edad es:", edad_persona, "años")




