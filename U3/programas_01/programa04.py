"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""

import math


def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def calcular_area_rectangulo(base, altura):
    return base * altura


def mostrar_menu():
    print("Menú de opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")


def opcion1():
    radio = float(input("Introduce el radio del círculo (mayor que 0): "))
    if radio > 0:
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area}")
    else:
        print("Error: El radio debe ser mayor que 0.")


def opcion2():

    base = float(input("Introduce la base del triángulo (mayor que 0): "))
    altura = float(input("Introduce la altura del triángulo (mayor que 0): "))
    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    else:
        print("Error: La base y la altura deben ser mayores que 0.")


def opcion3():
    base = float(input("Introduce la base del rectángulo (mayor que 0): "))
    altura = float(input("Introduce la altura del rectángulo (mayor que 0): "))
    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area}")
    else:
        print("Error: La base y la altura deben ser mayores que 0.")


continua = True
while continua:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        print("Saliendo del programa.")
        continua = False
    else:
        print("Error: Opción no válida. Por favor, selecciona una opción entre 1 y 4.")
