"""
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 < num2:
    print(f"{num1} es menor que {num2}")
    print(f"{num2} es mayor que {num1}")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
    print(f"{num2} es menor que {num1}")
else:
    print("Ambos números son iguales.")
