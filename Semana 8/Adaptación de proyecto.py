import os
# Importa la librería 'os' para trabajar con archivos y comprobar su existencia

# Función que muestra el menú principal en pantalla
def mostrar_menu():
    print("\nMenu Principal – Dashboard")
    print("1 - Ver script: Técnicas de Programación")
    print("2 - Crear nueva tarea")
    print("3 - Ver tareas pendientes")
    print("0 - Salir")

# Función que lee y muestra el contenido de un archivo Python
def ver_script():
    ruta = "UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py"
    try:

        # Intenta abrir el archivo y mostrar su contenido
        with open(ruta, 'r', encoding='utf-8') as archivo:
            print("\n--- Contenido del script ---\n")
            print(archivo.read())
    except FileNotFoundError:

        # Si no se encuentra el archivo, muestra mensaje de error
        print("❌ No se encontró el archivo.")

# Función para crear una nueva tarea y guardarla en un archivo de texto
def crear_tarea():
    tarea = input("📌 Escribe una nueva tarea: ")    # Solicita al usuario que escriba una tarea
    with open("tareas.txt", "a", encoding='utf-8') as archivo:
        archivo.write(tarea + "\n")     # Guarda la tarea en el archivo
    print("✅ Tarea guardada correctamente.")

# Función para leer y mostrar todas las tareas pendientes guardadas en el archivo
def ver_tareas():
    print("\n🗂️ Tareas pendientes:")
    if os.path.exists("tareas.txt"):     # Verifica si el archivo existe
        with open("tareas.txt", "r", encoding='utf-8') as archivo:
            tareas = archivo.readlines()      # Lee todas las líneas del archivo
            if tareas:
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea.strip()}")    # Imprime cada tarea enumerada
            else:
                print("No hay tareas pendientes.")
    else:
        print("No hay archivo de tareas creado.")

# Bucle principal del programa: muestra el menú y responde según la opción elegida
while True:
    mostrar_menu()   # Muestra el menú principal
    opcion = input("Elige una opción: ")   # Solicita una opción al usuario


    if opcion == "1":
        ver_script()   # Muestra el contenido del script
    elif opcion == "2":
        crear_tarea()   # Permite crear una nueva tarea
    elif opcion == "3":
        ver_tareas()   # Muestra las tareas almacenadas
    elif opcion == "0":
        print("👋 Saliendo del Dashboard...")   # Mensaje de salida
        break   # Sale del bucle y termina el programa
    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")  # Mensaje si la opción no es reconocida
