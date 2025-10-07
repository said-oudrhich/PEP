"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random

puntuacion_banca = random.randint(17, 21)
puntuacion_jugador = 0

print("--- Black Jack Simplificado ---")
print(f"La banca tiene una puntuación de {puntuacion_banca}.")
print("Tus cartas suman valores entre 1 y 5.")

while True:
    print(f"\nTu puntuación actual es: {puntuacion_jugador}")
    
    if puntuacion_jugador > 21:
        print("¡Te has pasado de 21! Has perdido.")
        break

    while True:
        decision = input("¿Quieres otra carta? (s/n): ").lower()
        if decision in ['s', 'n']:
            break
        else:
            print("Opción no válida. Introduce 's' para sí o 'n' para no.")

    if decision == 's':
        carta = random.randint(1, 5)
        puntuacion_jugador += carta
        print(f"Ha salido un {carta}.")
    else: # El jugador se planta
        print(f"\nTe plantas con {puntuacion_jugador}.")
        print(f"La banca tenía {puntuacion_banca}.")
        if puntuacion_jugador > puntuacion_banca:
            print("¡Has ganado a la banca!")
        else:
            print("Has perdido. La puntuación de la banca es igual or superior.")
        break
