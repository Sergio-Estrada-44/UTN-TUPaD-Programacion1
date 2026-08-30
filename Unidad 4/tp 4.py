print ("        ")
print ("ACTIVIDAD 1")
print ("        ")

for num in range (-100, 101):
    print(num)

print ("        ")
print ("ACTIVIDAD 2")
print ("        ")

num2 = abs(int(input("Ingresa un número entero: ")))

if num2 == 0:
    digitos = 1
else:
    digitos = 0
    while num2 > 0:
        num2 //= 10
        digitos += 1

print("El número tiene", digitos, "dígitos")

print ("        ")
print ("ACTIVIDAD 3")
print ("        ")

a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))

suma3=0

if a > b :
    for c in range(a-1,b,-1):
        suma3 += c
else:
    for c in range(a+1,b):
        suma3 += c

print ("la suma de los numeros es:",suma3)

print ("        ")
print ("ACTIVIDAD 4")
print ("        ")

CORTE=0
sum4 = 0
num4= float("inf")
num32 = int(input("ingrese un numero para la suma: "))
while num4 != 0 :
    num4 = int(input("ingrese el otro numero para sumar(pulse 0 para cortar): "))
    sum4 += num4

print("la suma de los numeros ingresados es:", sum4+num32)

print ("        ")
print ("ACTIVIDAD 5")
print ("        ")

import random
intentos=1
num_respuesta=int(input("Vamos a jugar un juego, escriba un numero del 0 al 9 para ver si le atinaste: "))
num_que_adivinar= random.randint(0, 9)
while num_respuesta != num_que_adivinar:
    intentos += 1
    num_respuesta=int(input("Te equivocaste escribi otro: "))
            
print("Le atinaste al numero",num_que_adivinar,"en ",intentos,"intentos")

print ("        ")
print ("ACTIVIDAD 6")
print ("        ")

for num in range(2,100,2):
    print(num)

print ("        ")
print ("ACTIVIDAD 7")
print ("        ")

print("7)")

alfa=int(input("ingrese un numero positivo del 0 hacia adelante : "))
while alfa <=  0 :
        alfa=int(input("ERROR ingrese un numero positivo del 0 hacia adelante : "))

suma7=0

for c7 in range(alfa):
        suma7 += c7

print ("la suma de los numeros entre 0 y",alfa,"es:",suma7)

print ("        ")
print ("ACTIVIDAD 8")
print ("        ")

num_negativos=0
num_positivos=0
num_pares=0
num_impares=0

for num81 in range (1,101):
    num82 = int(input(f"ingrese un numero entero {num81}: "))
    if num82 < 0 and num82% 2 == 0:
        num_negativos += 1
        num_pares += 1
    elif num82 < 0 and num82% 2 != 0:
        num_negativos += 1
        num_impares += 1
    elif num82 > 0 and num82% 2 ==0:
        num_positivos += 1
        num_pares += 1
    elif num82 > 0 and num82% 2 !=0:
        num_positivos += 1
        num_impares += 1

print("cantidad de numeros positivos: ", num_positivos)
print("cantidad de numeros negativos: ", num_negativos)
print("cantidad de numeros pares: ", num_pares)
print("cantidad de numeros impares: ", num_impares)

print ("        ")
print ("ACTIVIDAD 9")
print ("        ")

cantidad = 100
suma9 = 0

for i in range(1, cantidad + 1):
    numero = int(input(f"Ingrese el número {i}: "))
    suma9 += numero

media = suma9 / cantidad

print("La media de los valores es:", media)

print ("        ")
print ("ACTIVIDAD 10")
print ("        ")

num10 = int(input("Ingresa un número: "))
invertido = 0


while num10 > 0:
    digito = num10 % 10                
    invertido = (invertido * 10) + digito 
    num10 = num10 // 10               

print(f"El número invertido es: {invertido}")