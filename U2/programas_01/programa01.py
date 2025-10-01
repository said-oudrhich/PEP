numero_par = int(input("Introduce un número par: "))

# Verificar si el número es par
if numero_par % 2 != 0:
    print("Error: El número introducido no es par.")
else:
    # Solicitar un número impar al usuario
    numero_impar = int(input("Introduce un número impar: "))
    # Verificar si el número es impar
    if numero_impar % 2 == 0:
        print("Error: El número introducido no es impar.")
    else:
        print("Has introducido correctamente un número par y un número impar.")
