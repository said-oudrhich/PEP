"""
Programa04: Escribir un objeto Python en una cadena JSON
Convierte un diccionario en una cadena JSON con indentación y claves ordenadas.
"""

import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000,
}

cadena_json = json.dumps(pais, indent=2, sort_keys=True)
print(cadena_json)
