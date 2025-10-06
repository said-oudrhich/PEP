"""
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.

Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""

import random

# Jugador 1
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
total_j1 = dado1_j1 + dado2_j1
max_dado_j1 = max(dado1_j1, dado2_j1)
print(f"Jugador 1: {dado1_j1} y {dado2_j1} (Total: {total_j1}) (Dado más alto: {max_dado_j1})")

# Jugador 2
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
total_j2 = dado1_j2 + dado2_j2
max_dado_j2 = max(dado1_j2, dado2_j2)
print(f"Jugador 2: {dado1_j2} y {dado2_j2} (Total: {total_j2}) (Dado más alto: {max_dado_j2})")

# Determinar ganador
if total_j1 > total_j2:
    print("\nGana el Jugador 1 por puntuación total.")
elif total_j2 > total_j1:
    print("\nGana el Jugador 2 por puntuación total.")
else: # Empate en puntuación total
    if max_dado_j1 > max_dado_j2:
        print("\nGana el Jugador 1 por tener el dado más alto.")
    elif max_dado_j2 > max_dado_j1:
        print("\nGana el Jugador 2 por tener el dado más alto.")
    else:
        print("\nEmpate.")
