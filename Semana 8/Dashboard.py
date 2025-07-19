# Importa el módulo 'os' para trabajar con rutas de archivos y carpetas del sistema
import os

# Esta función imprime el menú principal con las opciones disponibles para el usuario
def mostrar_menu():
    print("\nMenu Principal - Dashboard")
    print("1 - Semana 2/Técnicas POO.py")
    print("2 - Semana 3/POO.py")
    print("3 - Semana 3/Programación Tradicional.py")
    print("4 - Semana 4/Ejemplos del mundo real.py")
    print("5 - Semana 5/Uso de Tipos de datos, Identificadores..py")
    print("6 - Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py")
    print("7 - Semana 7/Constructores y Destructores.py")
    print("8 - Semana 8/Dashboard.py")
    print("9 - Salir")  #Para salir del programa

# Define la ruta base absoluta donde está ubicado tu proyecto en PyCharm
ruta_base = r"C:\Users\Usuario\PycharmProjects\2525---PROGRAMACION-ORIENTADA-A-OBJETOS-D----UEA-L-UFB-030-D"

# Diccionario de scripts por opción
scripts = {
    "1": os.path.join(ruta_base, "Semana 2", "Técnicas POO.py"),
    "2": os.path.join(ruta_base, "Semana 3", "POO.py"),
    "3": os.path.join(ruta_base, "Semana 3", "Programación Tradicional.py"),
    "4": os.path.join(ruta_base, "Semana 4", "Ejemplos del mundo real.py"),
    "5": os.path.join(ruta_base, "Semana 5", "Uso de Tipos de datos, Identificadores..py"),
    "6": os.path.join(ruta_base, "Semana 6", "Clases, objetos, herencia, encapsulamiento y polimorfismo.py"),
    "7": os.path.join(ruta_base, "Semana 7", "Constructores y Destructores.py"),
    "8": os.path.join(ruta_base, "Semana 8", "Dashboard.py"),
}

# Función que abre y muestra el contenido del archivo indicado por la ruta
def mostrar_codigo(ruta_script):
    print(f"\nIntentando abrir: {ruta_script}\n")  # Muestra la ruta que se intenta abrir
    try:
        # Intenta abrir el archivo en modo lectura con codificación UTF-8
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(archivo.read())  # Imprime el contenido del archivo
    except FileNotFoundError:
        # Error si no se encuentra el archivo en la ruta especificada
        print("❌ El archivo no se encontró. Verifica que exista en esa ruta.")
    except Exception as e:
        # Muestra cualquier otro error inesperado
        print(f"⚠️ Ocurrió un error: {e}")

# Bucle principal que muestra el menú y permite seleccionar archivos para ver su contenido
while True:
    mostrar_menu()   # Llama a la función que imprime el menú
    opcion = input("Elige una opción (1-8) o 9 para salir: ")  # Solicita al usuario una opción
    if opcion == "9":
        break  # Sale del bucle y finaliza el programa
    elif opcion in scripts:
        mostrar_codigo(scripts[opcion])  # Llama a la función para mostrar el archivo correspondiente
    else:
        print("Opción no válida. Intenta de nuevo.")  # Mensaje si la opción ingresada no es válida