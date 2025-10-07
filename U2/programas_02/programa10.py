"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random

# Pedir número de jugadores
num_jugadores = 0
while num_jugadores <= 0:
    try:
        num_jugadores = int(input("Introduce el número de jugadores: "))
        if num_jugadores <= 0:
            print("Debe haber al menos un jugador.")
    except ValueError:
        print("Entrada no válida. Introduce un número.")

# Puntuación de la banca (una para toda la partida)
puntuacion_banca = random.randint(17, 21)
print(f"\n--- Black Jack Multijugador ---")
print(f"La banca tiene una puntuación de {puntuacion_banca}.")
print("Tus cartas suman valores entre 1 y 5.")

# Bucle principal para cada jugador
for i in range(1, num_jugadores + 1):
    print(f"\n--- Turno del Jugador {i} ---")
    puntuacion_jugador = 0

    while True:
        print(f"Jugador {i}, tu puntuación actual es: {puntuacion_jugador}")

        if puntuacion_jugador > 21:
            print("¡Te has pasado de 21! Has perdido contra la banca.")
            break

        while True:
            decision = input("¿Quieres otra carta? (s/n): ").lower()
            if decision in ["s", "n"]:
                break
            else:
                print("Opción no válida. Introduce 's' para sí o 'n' para no.")

        if decision == "s":
            carta = random.randint(1, 5)
            puntuacion_jugador += carta
            print(f"Ha salido un {carta}.")
        else:  # El jugador se planta
            print(f"\nJugador {i}, te plantas con {puntuacion_jugador}.")
            if puntuacion_jugador > 21:
                print("¡Te has pasado de 21! Has perdido contra la banca.")
            elif puntuacion_jugador > puntuacion_banca:
                print("¡Has ganado a la banca!")
            else:
                print("Has perdido. La puntuación de la banca es igual o superior.")
            break

print("\n--- Fin del juego ---")
