"""
Programa02: Escritura de un fichero JSON
Crea el archivo capitales.json con información de países y capitales.
Usa json.dump() con ensure_ascii=False y indent=4.
"""

import json

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"},
]

try:
    with open("capitales.json", "w", encoding="utf-8") as archivo:
        json.dump(capitales, archivo, ensure_ascii=False, indent=4)
    print("Archivo 'capitales.json' creado correctamente.")
except Exception as e:
    print("Ocurrió un error al crear el archivo:", e)
