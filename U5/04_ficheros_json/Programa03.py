"""
Programa03: Cargar un objeto desde una cadena JSON
Convierte una cadena JSON en un objeto Python y muestra su contenido.
"""

import json

cadena_json = """
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
"""

try:
    paises = json.loads(cadena_json)
    print("Tipo de dato obtenido:", type(paises))
    for pais in paises:
        print(f"{pais['nombre']} usa la moneda {pais['moneda']}.")
except json.JSONDecodeError:
    print("Error: La cadena JSON no es válida.")
except Exception as e:
    print("Ocurrió un error:", e)
