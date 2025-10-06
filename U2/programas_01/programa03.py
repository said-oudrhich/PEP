"""
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""

num1 = float(input("Introduce el dividendo: "))
num2 = float(input("Introduce el divisor: "))

if num2 == 0:
    print("Error: No se puede dividir por cero.")
else:
    print(f"La división es: {num1 / num2}")
