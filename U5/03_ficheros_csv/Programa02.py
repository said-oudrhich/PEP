from csv import DictReader

try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        campos = ["Ciudad", "País", "Población (millones)"]

        primera_linea = archivo.readline().strip()

        # Reiniciamos la lectura SIEMPRE (esta es la clave)
        archivo.seek(0)

        # Detectamos si la cabecera coincide con los campos esperados
        if primera_linea.split(",") == campos:
            # Tiene cabecera → DictReader normal
            lector = DictReader(archivo)
            print("Nombres de las columnas:", lector.fieldnames)
        else:
            # No tiene cabecera
            lector = DictReader(archivo, fieldnames=campos)
            print("Nombres de las columnas (asignadas manualmente):", campos)

        for fila in lector:
            print(
                f"{fila['Ciudad']} ({fila['País']}) tiene una población aproximada de "
                f"{fila['Población (millones)']} millones."
            )

except FileNotFoundError:
    print("Error: El archivo no existe o no se encuentra en el directorio.")
except PermissionError:
    print("Error: No se tiene permiso para leer el archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
