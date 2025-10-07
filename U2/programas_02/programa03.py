"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue.
"""

print("1. Bucle for sin continue:")
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n")

print("2. Bucle for con continue:")
for i in range(0, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print("\n")

print("3. Bucle while sin continue:")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 2
print("\n")

print("4. Bucle while con continue:")
i = -1
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()
