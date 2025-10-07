"""
Escribe un programa que realice las siguientes operaciones:
- Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
- Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
- Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.
"""

while True:
    # 1. Leer y validar el número
    numero = 0
    while not (1 <= numero <= 10):
        numero = int(input("Introduce un número entre 1 y 10: "))
        if not (1 <= numero <= 10):
            print("El número debe estar entre 1 y 10. Inténtalo de nuevo.")

    # 2. Mostrar la tabla de multiplicar
    print(f"\n--- Tabla de multiplicar del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    # 3. Preguntar si desea continuar
    while True:
        continuar = input("\n¿Deseas introducir otro número? (s/n): ").lower()
        if continuar in ["s", "n"]:
            break
        else:
            print("Opción no válida. Introduce 's' para sí o 'n' para no.")

    if continuar == "n":
        print("¡Hasta luego!")
        break
