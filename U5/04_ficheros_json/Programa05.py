import json

try:
    with open("paises.json", "r", encoding="utf-8") as f:
        paises = json.load(f)

    continente = input("Introduce un continente: ").strip()

    filtrados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            filtrados.append(pais)

    if filtrados:
        print("\nPaíses encontrados:")
        for p in filtrados:
            print(f"- {p['nombre']} ({p['poblacion']} millones)")
    else:
        print("No se encontraron países en ese continente.")

    # Guardamos los resultados en un nuevo archivo JSON
    with open("paises_filtrados.json", "w", encoding="utf-8") as f:
        json.dump(filtrados, f, ensure_ascii=False, indent=4)

    print("\nArchivo 'paises_filtrados.json' creado correctamente.")

except (FileNotFoundError, json.JSONDecodeError) as e:
    print("Error con el archivo JSON:", e)
except Exception as e:
    print("Error inesperado:", e)
