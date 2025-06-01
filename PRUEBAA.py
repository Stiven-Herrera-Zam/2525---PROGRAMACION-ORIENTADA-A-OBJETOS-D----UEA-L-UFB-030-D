#Escritura de archivos de texto
with open("my_notes.txt", "w") as file:    #with cierra automáticamente el archivo
    file.write("Hola, Tengo 18 años.\n")   #file.write escribe el texto dentro del archivo
    file.write("Soy del Oriente.\n")       #"\n" es un salto de línea
    file.write("Me gusta el fútbol.\n")

#Lectura de archivo de texto
with open("my_notes.txt", "r") as file:    #abrir el archivo en modo lectura
    for line in file:                      #leer y mostrar cada línea
        print(line.strip())                #strip() elimina saltos de linea extra
