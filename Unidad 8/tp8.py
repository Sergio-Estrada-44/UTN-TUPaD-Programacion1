
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,500.0,15\n")
    archivo.write("Goma,50.0,50\n")


productos = []


print("--- PRODUCTOS ACTUALES ---")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        
        datos = linea.strip().split(",") 
        
        
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        
       
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        
        
        diccionario_prod = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(diccionario_prod)


print("\n--- AGREGAR NUEVO PRODUCTO ---")
nuevo_nombre = input("Ingrese el nombre del producto: ")
nuevo_precio = float(input("Ingrese el precio: "))
nuevo_cantidad = int(input("Ingrese la cantidad: "))


with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}\n")


productos.append({"nombre": nuevo_nombre, "precio": nuevo_precio, "cantidad": nuevo_cantidad})



print("\n--- BUSCAR PRODUCTO ---")
buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False 

for prod in productos:
    
    if prod["nombre"].lower() == buscar.lower():
        print("\n¡Producto Encontrado!")
        print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break 

if not encontrado:
    print("\nError: El producto no existe en el inventario.")



with open("productos.txt", "w") as archivo:
    for prod in productos:
        archivo.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")

print("\n¡Programa finalizado! El archivo productos.txt ha sido sobrescrito con la lista actualizada.")
    