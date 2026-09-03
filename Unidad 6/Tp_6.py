print("ACTIVIDAD 1")
print()

def imprimir_hola_mundo ():
    return "hola mundo"

print(imprimir_hola_mundo())

print()
print("ACTIVIDAD 2")
print()

def saludar_usuario(nombre_us):
    return f"Hola {nombre_us}!!!"

nombre = input("Ingrese su nombre: ")
print()
print(saludar_usuario(nombre))

print()
print("ACTIVIDAD 3")
print()

def  informacion_personal(nombre3, apellido3, edad3, residencia3):
    return f"Soy {nombre3} {apellido3}, tengo {edad3} años y vivo en {residencia3}"

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
residencia = input("Por favor ingrese su residencia: ")
print()
print(informacion_personal(nombre, apellido, edad, residencia))

print()
print("ACTIVIDAD 4")
print()

def calcular_area_circulo(radio4) :
    area = 3.14 * (radio4**2)
    return area

def calcular_perimetro_circulo(radio_P_4):
    perimetro = 2 * 3.14 * radio_P_4
    return perimetro
    

radio = int(input("Ingrese el Radio de un circulo: "))
areaResultado=calcular_area_circulo(radio)
perimetroResultado=calcular_perimetro_circulo(radio)

print()
print(f"El area del circulo es {areaResultado} y su perimetro es {perimetroResultado}")

print()
print("ACTIVIDAD 5")
print()

def segundos_a_horas(seg_5):
    horas = seg_5 / 3600
    return f"los {seg_5} seg pasados a horas son {horas:.2f} horas."
    

seg = float(input("Por favor ingrese los segundos: "))
print()
print(segundos_a_horas(seg))

print()
print("ACTIVIDAD 6")
print()

def  tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numeroDeTabla = int(input("Ingre un numero para multiplicar: "))
print("-----------------------------------------------------")
tabla_multiplicar(numeroDeTabla)

print()
print("ACTIVIDAD 7")
print()

def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return (suma, resta, multiplicacion, division)

numA = int(input("Ingrese un primer numero: "))
numB = int(input("Ingrese un segundo numero: "))

respuesta =  operaciones_basicas(numA, numB)
print(f"La suma de los numeros es: {respuesta[0]}")
print(f"La resta de los numeros es: {respuesta[1]}")
print(f"La multiplicacion de los numeros es: {respuesta[2]}")
print(f"La division de los numeros es: {respuesta[3]}")

print()
print("ACTIVIDAD 8")
print()

def calcular_imc(peso, altura):
    IMC = peso / (altura**2)
    return IMC

pesoKilos = float(input("Ingrese su peso en kilogramos: "))
alturaMetros = float(input("Ingrese su altura en metros: "))

print()
print(f"Su indice de masa corporal es: {calcular_imc(pesoKilos, alturaMetros):.2f} IMC")

print()
print("ACTIVIDAD 9")
print()

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print()
print(f"{celsius}°C equivalen a {fahrenheit}°F")

print()
print("ACTIVIDAD 10")
print()

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print()
print(f"El promedio es: {promedio}")
