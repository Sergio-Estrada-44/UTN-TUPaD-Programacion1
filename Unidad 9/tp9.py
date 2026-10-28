def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    if n <= 1:
        return n
    return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if (numero % 10) == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

if __name__ == "__main__":
    limite_fac = int(input("Ejercicio 1 - Ingrese un número entero para calcular factoriales: "))
    for i in range(1, limite_fac + 1):
        print(f"Factorial de {i}: {factorial(i)}")

    pos_fibo = int(input("\nEjercicio 2 - Ingrese la posición de Fibonacci deseada: "))
    print("Serie de Fibonacci:")
    for i in range(pos_fibo + 1):
        print(fibonacci(i), end=" ")
    print()

    base = float(input("\nEjercicio 3 - Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))
    print(f"Resultado de {base}^{exp}: {potencia(base, exp)}")

    num_dec = int(input("\nEjercicio 4 - Ingrese un número entero decimal para convertir a binario: "))
    print(f"Representación binaria: {decimal_a_binario(num_dec)}")

    texto = input("\nEjercicio 5 - Ingrese una palabra para verificar si es palíndromo: ")
    print(f"¿Es palíndromo?: {es_palindromo(texto)}")

    num_suma = int(input("\nEjercicio 6 - Ingrese un número entero positivo para sumar sus dígitos: "))
    print(f"Suma de dígitos: {suma_digitos(num_suma)}")

    bloques = int(input("\nEjercicio 7 - Ingrese la cantidad de bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(bloques)}")

    num_buscar = int(input("\nEjercicio 8 - Ingrese el número completo: "))
    dig_buscar = int(input("Ingrese el dígito a contar: "))
    print(f"El dígito {dig_buscar} aparece {contar_digito(num_buscar, dig_buscar)} veces.")