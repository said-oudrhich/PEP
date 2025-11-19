from csv import reader

try:
    with open("ciudades.csv", "r", encoding="utf-8") as archivo:
        lector_csv = reader(archivo)

        # Saltar la primera línea (cabecera)
        next(lector_csv, None)
        for fila in lector_csv:
            print(
                f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes."
            )

except FileNotFoundError:
    print("Error: El archivo no existe o no se encuentra en el directorio.")
except PermissionError:
    print("Error: No se tiene permiso para leer el archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
