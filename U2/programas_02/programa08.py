"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.

Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).

Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""

import random

numero_secreto = random.randrange(1, 21)
acertado = False

print("He pensado un número entre 1 y 20. Tienes 3 intentos para adivinarlo.")

for intento in range(1, 4):
    print(f"\n--- Intento {intento} ---")

    intento_usuario = int(input("¿Cuál es tu número?: "))

    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! ¡Has acertado! El número era {numero_secreto}.")
        acertado = True
        break
    elif intento_usuario < numero_secreto:
        print("El número que he pensado es MAYOR.")
    else:
        print("El número que he pensado es MENOR.")


if not acertado:
    print(f"\nLo siento, has agotado tus 3 intentos. El número era {numero_secreto}.")
