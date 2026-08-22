# UTN-TUPaD-Programacion1

print("ACTIVIDAD 1")
print("     ")

print("Hola mundo")

print("     ")
print("ACTIVIDAD 2")
print("     ")

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!!.")

print("     ")
print("ACTIVIDAD 3")
print("     ")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Hola, soy {nombre} {apellido} de {edad} años, y vivo en {residencia}. ")

print("     ")
print("ACTIVIDAD 4")
print("     ")

radio = int(input("Ingrese el Radio del circulo: "))

area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio

print(f"El area del circulo es {area} y su perimetro es {perimetro} .")

print("     ")
print("ACTIVIDAD 5")
print("     ")

seg = int(input("escriba los segundos que quiera ver en horas: "))
hora = seg / 3600
print(f"Las cantidad sde horas segun los segundos es {hora} horas")

print("     ")
print("ACTIVIDAD 6")
print("     ")

num_tabla = int(input("Ingrese un numero para ver su tabla: "))

for i in range (1,11):
    resultado = num_tabla * i
    print(f" {num_tabla} x {i} = {resultado}")

print("     ")
print("ACTIVIDAD 7")
print("     ")

num_1 = float(input("Ingrese un primer numero(distinto de 0): "))
num_2 = float(input("Ingrese un segundo numero(distinto de 0): "))

interruptor = False

while interruptor == False:
    
    
    if num_1 == 0 :
        print("Error ingreso un 0 ")
        num_1 = float(input("Por favor ingrese un primer numero(distinto de 0): "))
    elif num_2 == 0 : 
        print("Error ingreso un 0")
        num_2 = float(input("Por favor ingrese un segundo numero(distinto de 0): "))
    else:
        result_sum = num_1 + num_2
        result_divi = num_1 / num_2
        result_multi = num_1 * num_2
        result_resta = num_1 - num_2
        print(f"Resultado de: {num_1} + {num_2} = {result_sum}")
        print(f"Resultado de: {num_1} / {num_2} = {result_divi:.2f}")
        print(f"Resultado de: {num_1} * {num_2} = {result_multi}")
        print(f"Resultado de: {num_1} - {num_2} = {result_resta}")
        interruptor = True

print("     ")
print("ACTIVIDAD 8")
print("     ")

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

IMC = peso / (altura ** 2)

print(f"Su indice de masa corporal es: {IMC:.2f} IMC.")

print("     ")
print("ACTIVIDAD 9")
print("     ")

gracelsius=float(input("Ingrese la temperatura en grados Celsius: "))

grafahrenheit = (1.8 * gracelsius) + 32

print(f"La temperatura en grados Fahrenheit es: {grafahrenheit}")

print("     ")
print("ACTIVIDAD 10")
print("     ")

nume1 = float(input("Ingrese el primer número: "))
nume2 = float(input("Ingrese el segundo número: "))
nume3 = float(input("Ingrese el tercer número: "))

promedio = (nume1 + nume2 + nume3) / 3

print("El promedio es:", promedio)