import sqlite3

class autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor(id_autor={self.id_autor}, nombre='{self.nombre}', nacionalidad='{self.nacionalidad}')"

class libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor 

    def __str__(self):
        return f"Libro(id_libro={self.id_libro}, titulo='{self.titulo}', anio_publicacion={self.anio_publicacion}, autor={self.autor})"

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        nacionalidad TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        anio_publicacion INTEGER,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autores(id)
    )
''')

conexion.commit()
conexion.close()

def registrar_autor(nombre, nacionalidad):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    
    cursor.execute('INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)', (nombre, nacionalidad))
    conexion.commit()
    id_autor = cursor.lastrowid
    conexion.close()
    
    return autor(id_autor, nombre, nacionalidad)

def registrar_libro(titulo, anio_publicacion, autor):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    
    cursor.execute('INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES (?, ?, ?)', (titulo, anio_publicacion, autor.id_autor))
    conexion.commit()
    id_libro = cursor.lastrowid
    conexion.close()
    
    return libro(id_libro, titulo, anio_publicacion, autor)

def actualizar_titulo_libro(id_libro, nuevo_titulo):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    
    cursor.execute('UPDATE libros SET titulo = ? WHERE id = ?', (nuevo_titulo, id_libro))
    conexion.commit()
    conexion.close()

import sqlite3

def listar_libros():
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    consulta = '''
        SELECT libros.titulo, libros.anio_publicacion, autores.nombre 
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    '''
    
    cursor.execute(consulta)
    resultados = cursor.fetchall() 

    print("--- Catálogo de Libros ---")
    for fila in resultados:
        titulo = fila[0]
        anio = fila[1]
        autor = fila[2]
        print(f"'{titulo}' ({anio}) - Escrito por: {autor}")

    conexion.close()

def eliminar_libro(id_libro):
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute('DELETE FROM libros WHERE id = ?', (id_libro,))
    conexion.commit()
    conexion.close()

if __name__ == "__main__":

    print("---1. Base de datos inicializada---")

    print("\n---2. Registarndo 2 autores y 3 libros---")

    autor1 = registrar_autor("Gabriel García Márquez", "Colombiana")
    autor2 = registrar_autor("J.R.R. Tolkien", "El senor de los anillos")
    print("Autores registrados con exito.")

    registrar_libro("Cien años de soledad", 1967, autor1)
    registrar_libro("El amor en los tiempos del cólera", 1985, autor1)
    registrar_libro("El Hobbit", 1937, autor2)
    print("Registro completados con exito.")

    print("\n---3. Listando libros---")
    listar_libros() 

    print("\n---4. Actualizando el título de un libro (Modificando libro ID 3)---")
    actualizar_titulo_libro(3, "El Hobbit: Un viaje inesperado")
    listar_libros()

    print("\n---5. Eliminando un libro (Eliminando libro ID 2)---")
    eliminar_libro(2)
    listar_libros()