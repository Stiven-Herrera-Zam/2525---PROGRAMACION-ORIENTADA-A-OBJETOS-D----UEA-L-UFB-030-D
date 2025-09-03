#Clase libro Usando Tupla para datos inmutables
class Libro:
    def __init__ (self, titulo, autor, categoria, isbn):
        self.datos_principales = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def __str__(self):
        return f"'{self.datos_principales[0]}' por {self.datos_principales[1]} - ISBN {self.isbn}"

    @property
    def titulo(self):
        return self.datos_principales[0]

    @property
    def autor(self):
        return self.datos_principales[1]


#Clase Usuario usando lista para libros prestados
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []    #Lista para libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def agregar_libro_prestado(self, libro):
        self.libros_prestados.append(libro)

    def remover_libro_prestado(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]


#Clase Biblioteca usando diccionario y conjunto para rendimiento
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}   #Diccionario para búsquedas rápidas
        self.ids_usuarios = set()      #Conjunto para IDs de usuarios únicos
        self.usuarios_registrados = {} #Diccionario para usuarios registrados
        self.historial_prestamos = []  #Lista para historial de préstamos

    # ======= Gestión de libros =======
    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
            return False
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido correctamente.")
        return True

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            if libro.prestado:
                print(f"No se puede quitar el libro '{libro.titulo}' porque está prestado.")
                return False
            del self.libros_disponibles[isbn]
            print(f"Libro '{libro.titulo}' eliminado correctamente.")
            return True
        else:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return False

    # ======= Gestión de usuarios =======
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El ID {usuario.id_usuario} ya está registrado.")
            return False
        self.ids_usuarios.add(usuario.id_usuario)
        self.usuarios_registrados[usuario.id_usuario] = usuario
        print(f"Usuario {usuario.nombre} registrado correctamente.")
        return True

    def dar_baja_usuario(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return False
        usuario = self.usuarios_registrados[id_usuario]
        if usuario.libros_prestados:
            print(f"No se puede dar de baja al usuario {usuario.nombre} porque tiene libros prestados.")
            return False
        self.ids_usuarios.remove(id_usuario)
        del self.usuarios_registrados[id_usuario]
        print(f"Usuario {usuario.nombre} dado de baja correctamente.")
        return True

    # ======= Préstamos y devoluciones =======
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return False
        if id_usuario not in self.ids_usuarios:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return False
        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]
        if libro.prestado:
            print(f"El libro '{libro.titulo}' ya está prestado.")
            return False
        libro.prestado = True
        usuario.agregar_libro_prestado(libro)
        self.historial_prestamos.append({
            'accion': 'préstamo',
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha': '2025-09-02'
        })
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        return True

    def devolver_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return False
        if id_usuario not in self.ids_usuarios:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return False
        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]
        if not libro.prestado:
            print(f"El libro '{libro.titulo}' no está prestado.")
            return False
        if libro not in usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene prestado este libro.")
            return False
        libro.prestado = False
        usuario.remover_libro_prestado(isbn)
        self.historial_prestamos.append({
            'accion': 'devolución',
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha': '2025-09-02'
        })
        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
        return True

    # ======= Búsquedas =======
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros_disponibles.values()
                if titulo.lower() in libro.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros_disponibles.values()
                if autor.lower() in libro.autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros_disponibles.values()
                if libro.categoria.lower() == categoria.lower()]

    def buscar_por_isbn(self, isbn):
        return self.libros_disponibles.get(isbn)

    # ======= Listados =======
    def listar_libros_prestados_usuario(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            return None
        return self.usuarios_registrados[id_usuario].libros_prestados

    def listar_todos_libros_prestados(self):
        return [libro for libro in self.libros_disponibles.values() if libro.prestado]

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros_disponibles.values() if not libro.prestado]


# ================== Ejemplo de uso ==================
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-1234567890")
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "978-0987654321")
libro3 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "978-1122334455")

biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Luisa García", "U001")
usuario2 = Usuario("Adrian López", "U002")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Préstamos
biblioteca.prestar_libro("978-1234567890", "U001")
biblioteca.prestar_libro("978-0987654321", "U002")

# Búsqueda
print("\n Búsqueda por autor 'García':")
for libro in biblioteca.buscar_por_autor("García"):
    print(f" - {libro}")

# Listado
print("\n Libros prestados actualmente:")
for libro in biblioteca.listar_todos_libros_prestados():
    print(f" - {libro}")

# Devolución
biblioteca.devolver_libro("978-1234567890", "U001")





















