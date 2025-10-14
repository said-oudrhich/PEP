from math import sin, cos, sqrt, pow, radians;

print("Seleccione la operación matemática que desea realizar:")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = input("Ingrese el número de la operación (1-4): ")

match opcion:
    case '1':
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = sin(radians(angulo))
        print(f"El seno de {angulo}° es: {resultado}")

    case '2':
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = cos(radians(angulo))
        print(f"El coseno de {angulo}° es: {resultado}")

    case '3':
        numero = float(input("Ingrese un número: "))
        if numero < 0:
            print("No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = sqrt(numero)
            print(f"La raíz cuadrada de {numero} es: {resultado}")

    case '4':
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = pow(base, exponente)
        print(f"{base} elevado a la potencia de {exponente} es: {resultado}")

    case _:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
