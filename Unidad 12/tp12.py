import sqlite3
from flask import Flask, request, jsonify

# --- Inicialización de la BD y Clases ---

class autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor 

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, nacionalidad TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, anio_publicacion INTEGER, autor_id INTEGER, FOREIGN KEY (autor_id) REFERENCES autores(id))''')
conexion.commit()
conexion.close()



def get_db_connection():
    conexion = sqlite3.connect('biblioteca.db')
    conexion.row_factory = sqlite3.Row 
    return conexion

def obtener_autores_db():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM autores')
    autores = cursor.fetchall()
    conexion.close()
    return [dict(a) for a in autores]

def obtener_autor_db(id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM autores WHERE id = ?', (id,))
    autor_db = cursor.fetchone()
    conexion.close()
    return dict(autor_db) if autor_db else None

def insertar_autor_db(nombre, nacionalidad):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)', (nombre, nacionalidad))
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return nuevo_id

def obtener_libros_db():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    
    consulta = '''
        SELECT libros.id, libros.titulo, libros.anio_publicacion, 
               autores.nombre AS autor_nombre, autores.nacionalidad AS autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    '''
    cursor.execute(consulta)
    libros = cursor.fetchall()
    conexion.close()
    return [dict(l) for l in libros]

def obtener_libro_db(id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM libros WHERE id = ?', (id,))
    libro_db = cursor.fetchone()
    conexion.close()
    return dict(libro_db) if libro_db else None

def insertar_libro_db(titulo, anio, autor_id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES (?, ?, ?)', (titulo, anio, autor_id))
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return nuevo_id

def actualizar_libro_db(id, titulo, anio, autor_id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('UPDATE libros SET titulo = ?, anio_publicacion = ?, autor_id = ? WHERE id = ?', (titulo, anio, autor_id, id))
    conexion.commit()
    conexion.close()

def eliminar_libro_db(id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()



app = Flask(__name__)


@app.route('/api/autores', methods=['GET'])
def get_autores():
    return jsonify(obtener_autores_db()), 200

@app.route('/api/autores', methods=['POST'])
def create_autor():
    datos = request.get_json()
    if not datos or 'nombre' not in datos or 'nacionalidad' not in datos:
        return jsonify({"error": "Faltan campos obligatorios (nombre, nacionalidad)"}), 400
    
    nuevo_id = insertar_autor_db(datos['nombre'], datos['nacionalidad'])
    return jsonify(obtener_autor_db(nuevo_id)), 201


@app.route('/api/libros', methods=['GET'])
def get_libros():
    return jsonify(obtener_libros_db()), 200

@app.route('/api/libros/<int:id>', methods=['GET'])
def get_libro(id):
    libro = obtener_libro_db(id)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(libro), 200

@app.route('/api/libros', methods=['POST'])
def create_libro():
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({"error": "Faltan campos obligatorios (titulo, anio, autor_id)"}), 400
    
    
    if not obtener_autor_db(datos['autor_id']):
        return jsonify({"error": f"El autor_id {datos['autor_id']} no existe en la base de datos"}), 404

    nuevo_id = insertar_libro_db(datos['titulo'], datos['anio'], datos['autor_id'])
    return jsonify(obtener_libro_db(nuevo_id)), 201

@app.route('/api/libros/<int:id>', methods=['PUT'])
def update_libro(id):
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({"error": "Faltan campos obligatorios (titulo, anio, autor_id)"}), 400
    
    if not obtener_libro_db(id):
        return jsonify({"error": "Libro no encontrado para actualizar"}), 404
    
    actualizar_libro_db(id, datos['titulo'], datos['anio'], datos['autor_id'])
    return jsonify(obtener_libro_db(id)), 200

@app.route('/api/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    if not obtener_libro_db(id):
        return jsonify({"error": "Libro no encontrado para eliminar"}), 404
    
    eliminar_libro_db(id)
    return jsonify({"mensaje": "Libro eliminado correctamente"}), 200

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)
