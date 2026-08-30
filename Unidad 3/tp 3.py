print("EJERCICIO 1")
print("     ")

edad=int(input("Escriba su edad: "))
if edad > 18 :
    print("es mayor de edad")

print("     ")
print("EJERCICIO 2")
print("     ")

nota=int(input("Escribe su nota: "))
if nota > 6 :
    print("Aprobado")
elif nota < 6 :
    print("Desaprobado")

print("     ")
print("EJERCICIO 3")
print("     ")

numero=int(input("escriba un numero par: "))

num=numero%2
if num==0:
    print("el numero es par")
else:
    print("Por favor, ingrese un número par")

print("     ")
print("EJERCICIO 4")
print("     ")

edad1=int(input("escriba su edad: "))

if edad1 < 12 :
    print("es Niño/a")
elif edad1 >= 12 and edad1 < 18:
    print("es Adolescente")
elif edad1 >= 18 and edad1 < 30:
    print("Adulto/a joven")
elif edad1 >= 30:
    print("es Adulto/a")

print("     ")
print("EJERCICIO 5")
print("     ")

contraseña=input("Por favor, ingrese su contraseña: ")

if 8<= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("     ")
print("EJERCICIO 7")
print("     ")

texto=input("por favor ingrese un texto: ")
vocales="aeiouAEIOUáéíóúÁÉÍÓÚ"
if len(texto) > 0 and texto[-1] in vocales:
    resultado= texto+"!"
else:
    resultado= texto

print(resultado)

print("     ")
print("EJERCICIO 8")
print("     ")

nombre=input("ingrese su nombre: ")

print("\seleccione una de las opcines escribiendo el numero:")
print("1 nombre en mayusculas")
print("2 nombre en minusculas")
print("3 inicial en mayusculas")

opcion=int(input("eliga una opcion: "))

if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.capitalize())
else:
    print("opcion incorrecta")

print("     ")
print("EJERCICIO 9")
print("     ")

sismo=float(input("ingrese la magnitud del terremoto: "))

if sismo<3:
    print("Muy leve")
elif 3<=sismo<4:
    print("Leve")
elif 4<=sismo<5:
    print("Moderado")
elif 5<=sismo<6:
    print("Fuerte")
elif 6<=sismo<7:
    print("Muy Fuerte")
elif 7<=sismo:
    print("Extremo")

print("     ")
print("EJERCICIO 10")
print("     ")

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = input("Ingresa el mes (ej. enero, febrero...): ").lower()
dia = int(input("Ingresa el día (1-31): "))

estacion = ""

    
if hemisferio == 'N':
    if (mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia < 21) or (mes == 'diciembre' and dia >= 21)):
        estacion = "Invierno"
    elif ((mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia < 21)):
        estacion = "Primavera"
    elif ((mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia < 23)):
        estacion = "Verano"
    else:
        estacion = "Otoño"

    
elif hemisferio == 'S':
    if (mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia < 21) or (mes == 'diciembre' and dia >= 21)):
        estacion = "Verano"
    elif ((mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia < 21)):
     estacion = "Otoño"
    elif ((mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia < 23)):
        estacion = "Invierno"
    else:
            estacion = "Primavera"
else:
        estacion = "Hemisferio no válido"

    
print(f"Estás en {estacion}.")
