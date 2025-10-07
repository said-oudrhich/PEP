"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""

# --- Versión 1: Con break ---
print("--- Versión 1: Con break ---")
suma = 0
contador = 0
while True:
    num = float(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
    contador += 1


if contador > 0:
    media = suma / contador
    print(f"La suma es: {suma}")
    print(f"La media es: {media}")
else:
    print("No se introdujeron números.")


# --- Versión 2: Sin break ---
print("\n--- Versión 2: Sin break ---")
suma = 0
contador = 0
num = -1  # Inicializar con un valor que no sea 0

num = float(input("Introduce un número (0 para terminar): "))


while num != 0:
    suma += num
    contador += 1
    num = float(input("Introduce un número (0 para terminar): "))

if contador > 0:
    media = suma / contador
    print(f"La suma es: {suma}")
    print(f"La media es: {media}")
else:
    print("No se introdujeron números (o el primero fue 0).")
