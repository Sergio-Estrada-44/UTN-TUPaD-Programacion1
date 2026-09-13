print()
print("ACTIVIDAD 1")
print()

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print(precios_frutas)

print()
print("ACTIVIDAD 2")
print()

precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

print(precios_frutas)

print()
print("ACTIVIDAD 3")
print()

frutas_sin_precio = list(precios_frutas.keys())

print(frutas_sin_precio)

print()
print("ACTIVIDAD 4")
print()

Contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")

    Contactos [nombre] = numero

nombre_buscar = input("Ingrese el nombre del contacto a buscar su numero: ")

telefono = Contactos.get(nombre_buscar)

print(f"El Telefono de {nombre_buscar} es: {telefono}")

print()
print("ACTIVIDAD 5")
print()

frase = input("Escriba una frase: ")

palabras_unicas = frase.split()

mi_set = set(palabras_unicas)
diccionario_palabras = {}


for palabra in palabras_unicas:
    diccionario_palabras[palabra] = diccionario_palabras.get(palabra, 0) + 1


print("\n--- Resultados ---")
print("Palabras unicas:")
print(mi_set)

print("\nFrecuencia de palabras:")
print(diccionario_palabras)

print()
print("ACTIVIDAD 6")
print()

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    
    nota1 = float(input(f"Ingresa la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingresa la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingresa la nota 3 de {nombre}: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)
    print("-" * 25)


print("\n--- Promedios Finales ---")
for nombre, notas in alumnos.items():
    
    promedio = sum(notas) / len(notas)
    
    print(f"Alumno: {nombre} | Notas: {notas} | Promedio: {promedio:.2f}")

print()
print("ACTIVIDAD 7")
print()

parcial1 = {2, 7, 8, 6, 9}
parcial2 = {4, 8, 9, 5, 7}

aprobaron_ambos_parciales = parcial1 & parcial2
aprobaron_un_parciales1 = parcial1 - parcial2
aprobaron_un_parciales2 = parcial2 - parcial1
todos_aprobaron_un_parciales = parcial1 | parcial2

print(f"Los alumnos que aprobaron ambos parciales: {aprobaron_ambos_parciales}")
print(f"Los alumnos que aprobaron solo el parcial 1: {aprobaron_un_parciales1}")
print(f"Los alumnos que aprobaron solo el parcial 2: {aprobaron_un_parciales2}")
print(f"Todos los alumnos que aprobaron al menos 1 parcial: {todos_aprobaron_un_parciales}")

print()
print("ACTIVIDAD 8")
print()

inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "peras": 15
}

while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock o un nuevo producto")
    print("3. Salir")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    if opcion == '1':
        producto = input("Ingresa el nombre del producto a consultar: ").lower()
        
        if producto in inventario:
            print(f" El stock actual de '{producto}' es: {inventario[producto]} unidades.")
        else:
            print(f" El producto '{producto}' no existe en el inventario.")
            
    elif opcion == '2':
        producto = input("Ingresa el nombre del producto: ").lower()
        cantidad = int(input("Ingresa la cantidad a sumar/agregar: "))
        
        if producto in inventario:
           
            inventario[producto] += cantidad
            print(f" Se agregaron {cantidad} unidades. Nuevo stock de '{producto}': {inventario[producto]}")
        else:
            
            inventario[producto] = cantidad
            print(f" Producto nuevo agregado. Stock inicial de '{producto}': {inventario[producto]}")
            
    elif opcion == '3':
        print("Saliendo del programa... ¡Hasta luego!")
        break
        
    else:
        print(" Opción no válida. Por favor, intenta de nuevo.")

print()
print("ACTIVIDAD 9")
print()    

agenda = {
    ("lunes", "09:00"): "Reunión de equipo",
    ("martes", "14:30"): "Clase de Python",
    ("miércoles", "18:00"): "Ir al gimnasio",
    ("viernes", "20:00"): "Cena con amigos"
}

print("--- BÚSQUEDA EN LA AGENDA ---")
print("Días disponibles para prueba: lunes, martes, miércoles, viernes.")

while True:

    dia = input("\nIngresa el día (o 'salir' para terminar): ").lower().strip()
    
    if dia == 'salir':
        print("Cerrando la agenda...")
        break
        
    hora = input("Ingresa la hora (formato HH:MM, ej. 09:00): ").strip()
    
    
    clave_busqueda = (dia, hora)
    evento = agenda.get(clave_busqueda)
    
    
    if evento is not None:
        print(f" El {dia} a las {hora} tienes agendado: {evento}")
    else:
        print(f" No tienes ninguna actividad agendada el {dia} a las {hora}.")

print()
print("ACTIVIDAD 10")
print()      

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print(capitales_paises)
