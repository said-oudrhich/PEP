"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.

Ten en cuenta que:
- La piedra gana a la tijera pero pierde contra el papel.
- El papel gana a la piedra pero pierde contra la tijera.
- La tijera gana al papel pero pierde contra la piedra.
"""

import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
opcion_usuario = int(input("Seleccione una opción (1, 2 o 3): "))
opcion_maquina = random.randint(1, 3)
opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
print(f"La máquina ha elegido: {opciones[opcion_maquina]}")
if opcion_usuario == opcion_maquina:
    print("Empate")
elif (opcion_usuario == 1 and opcion_maquina == 3) or \
     (opcion_usuario == 2 and opcion_maquina == 1) or \
     (opcion_usuario == 3 and opcion_maquina == 2):
    print("¡Has ganado!")
else:
    print("Has perdido.")
