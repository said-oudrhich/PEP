"""
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla
los siguientes requisitos:
    - Entrada: Tiene 3 parámetros de entrada, que serán 3 cadenas de texto: nombre,
    primer apellido, segundo apellido
    - Salida: No tiene parámetros de salida.
    - Funcionalidad: Imprime por pantalla un mensaje saludando a la persona en función
    de los parámetros de entrada.
"""


def saludar(nombre, apellido1, apellido2):
    print(f"Hola {nombre} {apellido1} {apellido2}, encantado de saludarte.")


saludar("Said", "Oudrhich", "Soukrati")
saludar("Ana", "García", "López")
saludar("Luis", "Martínez", "Pérez")
