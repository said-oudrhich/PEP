millas = float(input("Introduce el número de millas: "))
km = float(input("Introduce el número de kilómetros: "))
millas_a_km = millas * 1.61
km_a_millas = km / 1.61
print(millas, "millas son", round(millas_a_km, 2), "kilómetros.")
print(km, "kilómetros son", round(km_a_millas, 2), "millas.")
