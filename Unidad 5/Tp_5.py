print("1)")
print()

mutiplosDe4 = []
for i in range(4, 101, 4):
    mutiplosDe4.append(i)

print(mutiplosDe4)

print()
print("2)")
print()

listaFavorita = ["Halo", "Counter 1.6", "Terraria", "Persona 3", "GTA San andreas"]

print(f"El penultimo elemento de mi lista es {listaFavorita[-2]}")

print()
print("3)")
print()

listaVacia = []

listaVacia.append("auto")
listaVacia.append("moto")
listaVacia.append("bici")

print(listaVacia)

print()
print("4)")
print()

animales = ["perro", "gato", "conejo", "pez"]
print(f"lista sin modificar: {animales}")
animales[-3] = "loro"
animales[-1] = "oso"
print(f"Lista modificada {animales}")

print()
print("5)")
print()

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
print("este codigo remueve el numero mas grande de la lista")

print()
print("6)")
print()

lista30 = []

for i in range(10, 31, 5):
    lista30.append(i)

print(lista30)

print()
print("7)")
print()

autos = ["sedan", "polo", "suran", "gol"]

print(autos)

autos[1] = "renault"
autos[2] = "fiat"

print(autos)

print()
print("8)")
print()

dobles = []

dobles.append(5*2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

print()
print("9)")
print()

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print(compras)

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

print()
print("10)")
print()

lista_anidada = [15, True, [25.5, 57.9, 30.6], False ]

print(lista_anidada)