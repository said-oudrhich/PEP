from matematicas import operaciones, figuras

def menu_principal():
    print("==== Menú Principal ====")
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    print("0. Salir")
    return input("Elige una opción: ")

def menu_operaciones():
    print("==== Operaciones matemáticas ====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    opcion = input("Elige la operación: ")
    if opcion == "1":
        print("Resultado:", operaciones.suma(a, b))
    elif opcion == "2":
        print("Resultado:", operaciones.resta(a, b))
    elif opcion == "3":
        print("Resultado:", operaciones.multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", operaciones.division(a, b))
    else:
        print("Opción no válida")

def menu_areas():
    print("==== Áreas geométricas ====")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")
    opcion = input("Elige la figura: ")
    if opcion == "1":
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", figuras.area_rectangulo(b, h))
    elif opcion == "2":
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", figuras.area_triangulo(b, h))
    elif opcion == "3":
        r = float(input("Radio: "))
        print("Área:", figuras.area_circulo(r))
    else:
        print("Opción no válida")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            menu_operaciones()
        elif opcion == "2":
            menu_areas()
        elif opcion == "0":
            print("Adiós!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
