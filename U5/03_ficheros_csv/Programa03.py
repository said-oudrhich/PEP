from csv import writer

capitales = [
    ["Ciudad", "País", "Continente"],
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"],
]

try:
    with open("capitales.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = writer(archivo_csv)
        escritor_csv.writerow(capitales[0])  # Escribir la cabecera
        escritor_csv.writerows(capitales[1:])  # Escribir los datos
except OSError as e:
    print(f"Error de E/S: {e.strerror}")
else:
    print("Archivo 'capitales.csv' creado correctamente.")
