"""
Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.
"""

numero = 0
while not (1 <= numero <= 10):
    numero = int(input("Introduce un número entre 1 y 10: "))
    if not (1 <= numero <= 10):
        print("El número debe estar entre 1 y 10. Inténtalo de nuevo.")

print(f"\nLista de números desde 1 hasta {numero}:")
for i in range(1, numero + 1):
    print(i, end=" ")
print()
