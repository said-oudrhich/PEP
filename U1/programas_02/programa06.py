fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0 / 9.0
print(
    str(fahrenheit)
    + " grados Fahrenheit son "
    + str(round(celsius, 2))
    + " grados Celsius."
)
