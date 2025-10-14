# imports de la librería estándar
# (ninguno necesario en este caso)
# imports de librerías de terceros
# (ninguno)
# imports de módulos propios
import operaciones

# Definición de funciones principales
def main():
    """Función principal del programa"""
    print("Programa de operaciones básicas")
    
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    print(f"Suma: {operaciones.suma(num1, num2)}")
    print(f"Resta: {operaciones.resta(num1, num2)}")
    print(f"Multiplicación: {operaciones.multiplicacion(num1, num2)}")
    print(f"División: {operaciones.division(num1, num2)}")

# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    main()
