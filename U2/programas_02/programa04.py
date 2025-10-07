"""
Escribe un programa que use un bucle while y le pida continuamente al usuario que
introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo
caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle
debe terminar.

Haz dos dos versiones del programa:
- Versión 1: Utiliza el concepto de ejecución condicional y la instrucción break. En
este caso el bucle no evaluará ninguna condición, es decir, será un bucle infinito.
- Versión 2: Realmente no es necesario usar la instrucción break. Diseña una
solución donde no se use break y el bucle while controle la condición de salida.
"""

print("--- Versión 1: Bucle infinito con break ---")
while True:
    try:
        numero = int(input("Introduce un número (45 para salir): "))
        if numero == 45:
            print("¡Has dejado el bucle con éxito!")
            break
        else:
            print("Número incorrecto, intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")

print("\n--- Versión 2: Bucle controlado por condición ---")
numero = 0
while numero != 45:
    numero = int(input("Introduce un número (45 para salir): "))
    if numero != 45:
        print("Número incorrecto, intenta de nuevo.")

    numero = 0

print("¡Has dejado el bucle con éxito!")
