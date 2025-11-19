from csv import DictWriter

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"},
]

try:
    with open("patrimonios.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        fieldnames = ["Ciudad", "País", "Lugar emblemático"]
        escritor_csv = DictWriter(archivo_csv, fieldnames=fieldnames, delimiter=";")
        escritor_csv.writeheader()  # Escribir la cabecera
        escritor_csv.writerows(patrimonios)  # Escribir los datos
except OSError as e:
    print(f"Error de E/S: {e.strerror}")
else:
    print("Archivo 'patrimonios.csv' generado correctamente.")
