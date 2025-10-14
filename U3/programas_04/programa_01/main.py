# imports de módulos propios
from matematicas import suma, resta, multiplicacion, division
from matematicas import area_rectangulo, area_triangulo, area_circulo
from matematicas import a_binario, a_hexadecimal, a_entero

def menu_principal():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    print("3. Conversiones de números")
    print("0. Salir")
    return input("Elige una opción: ")

def operaciones_matematicas():
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    print("Suma:", suma(a, b))
    print("Resta:", resta(a, b))
    print("Multiplicación:", multiplicacion(a, b))
    print("División:", division(a, b))

def calculo_areas():
    print("Áreas disponibles: rectángulo, triángulo, círculo")
    tipo = input("Introduce tipo de figura: ").lower()
    if tipo == "rectángulo":
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", figuras.area_rectangulo(b, h))
    elif tipo == "triángulo":
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", figuras.area_triangulo(b, h))
    elif tipo == "círculo":
        r = float(input("Radio: "))
        print("Área:", figuras.area_circulo(r))
    else:
        print("Figura no reconocida")

def conversiones_numeros():
    print("Conversiones: binario, hexadecimal, entero")
    opcion = input("Elige conversión: ").lower()
    valor = input("Introduce el valor: ")
    if opcion == "binario":
        print(a_binario(a_entero(valor)))
    elif opcion == "hexadecimal":
        print(a_hexadecimal(a_entero(valor)))
    elif opcion == "entero":
        print(a_entero(valor))
    else:
        print("Opción no reconocida")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            operaciones_matematicas()
        elif opcion == "2":
            calculo_areas()
        elif opcion == "3":
            conversiones_numeros()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo")

if __name__ == "__main__":
    main()
