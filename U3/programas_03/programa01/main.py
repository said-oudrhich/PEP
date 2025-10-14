import operaciones

def main():
    print("Programa de operaciones básicas")
    
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    print(f"Suma: {operaciones.suma(num1, num2)}")
    print(f"Resta: {operaciones.resta(num1, num2)}")
    print(f"Multiplicación: {operaciones.multiplicacion(num1, num2)}")
    print(f"División: {operaciones.division(num1, num2)}")

if __name__ == "__main__":
    main()
