"""
Programa01: Lectura de un fichero JSON
Lee el archivo paises.json y muestra cada país con su continente y población.
Controla posibles errores con try/except.
"""

import json

try:
    with open("paises.json", "r", encoding="utf-8") as archivo:
        paises = json.load(archivo)
        for pais in paises:
            print(
                f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes."
            )
except FileNotFoundError:
    print("Error: El archivo 'paises.json' no se encuentra.")
except json.JSONDecodeError:
    print("Error: El archivo contiene un JSON inválido.")
except Exception as e:
    print("Ocurrió un error:", e)
