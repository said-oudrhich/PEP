"""Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla."""

import math

print("Seleccione la operación matemática que desea realizar:")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = input("Ingrese el número de la operación (1-4): ")

match opcion:
    case '1':
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = math.sin(math.radians(angulo))
        print(f"El seno de {angulo}° es: {resultado}")

    case '2':
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = math.cos(math.radians(angulo))
        print(f"El coseno de {angulo}° es: {resultado}")

    case '3':
        numero = float(input("Ingrese un número: "))
        if numero < 0:
            print("No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = math.sqrt(numero)
            print(f"La raíz cuadrada de {numero} es: {resultado}")

    case '4':
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = math.pow(base, exponente)
        print(f"{base} elevado a la potencia de {exponente} es: {resultado}")

    case _:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
