from csv import DictReader

try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        campos = ["Ciudad", "País", "Población (millones)"]

        # Leemos la primera línea del archivo
        primera_linea = archivo.readline().strip()

        # Detectamos si contiene cabecera REAL
        if primera_linea.split(",") == campos:
            # Tiene cabecera → DictReader normal
            lector = DictReader(archivo)
            print("Nombres de las columnas:", lector.fieldnames)
        else:
            # No tiene cabecera → usamos la primera línea como datos
            archivo.seek(0)  # Volvemos al inicio
            lector = DictReader(archivo, fieldnames=campos)
            print("Nombres de las columnas (asignadas manualmente):", campos)

        for fila in lector:
            print(
                f"{fila['Ciudad']} ({fila['País']}) tiene una población aproximada de {fila['Población (millones)']} millones."
            )

except FileNotFoundError:
    print("Error: El archivo no existe o no se encuentra en el directorio.")
except PermissionError:
    print("Error: No se tiene permiso para leer el archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
