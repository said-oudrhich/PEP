"""
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:

1. Calcular el área de un círculo
2. Calcular el área de un triángulo
3. Calcular el área de un rectángulo
4. Salir

El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.

Hay que diseñar y definir las siguientes funciones:
- calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y retorna su área.
- calcular_area_triangulo: recibe como parámetros de entrada la base y la altura del triángulo y retorna su área.
- calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura del rectángulo y retorna su área.
- mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
- main: lee por teclado la opción seleccionada por el usuario, valida que la opción está entre 1 y 4,
  y llama a la función correspondiente según la opción seleccionada.
- opcion1: lee por teclado el valor del radio del círculo, valida que sea mayor que 0 y llama a calcular_area_circulo.
- opcion2: lee por teclado la base y la altura del triángulo, valida que ambos sean mayores que 0 y llama a calcular_area_triangulo.
- opcion3: lee por teclado la base y la altura del rectángulo, valida que ambos sean mayores que 0 y llama a calcular_area_rectangulo.
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

    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area}")


def opcion2():

    base = float(input("Introduce la base del triángulo (mayor que 0): "))
    altura = float(input("Introduce la altura del triángulo (mayor que 0): "))

    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")


def opcion3():
    base = float(input("Introduce la base del rectángulo (mayor que 0): "))
    altura = float(input("Introduce la altura del rectángulo (mayor que 0): "))

    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")


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
