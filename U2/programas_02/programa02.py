"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente.
"""

while True:
    try:
        numero = int(input("Introduce un número entre 1 y 10: "))
        if 1 <= numero <= 10:
            print(f"Número correcto: {numero}")
            break
        else:
            print("El número debe estar entre 1 y 10. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")
