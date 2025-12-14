("""
Programa05: Operaciones básicas

Escribe un programa en Python que realice las siguientes operaciones con cadenas:
- Declara dos cadenas y únelas con concatenación (+).
- Repite una cadena tres veces con *.
- Compara dos cadenas lexicográficamente e indica cuál es mayor.
- Comprueba si una subcadena pertenece a otra con in.
""")

cadena1 = "Hola"
cadena2 = "Mundo"

# Concatenación
concatenada = cadena1 + " " + cadena2
print("Concatenación:", concatenada)

# Repetición
repetida = cadena1 * 3
print("Repetición (tres veces):", repetida)

# Comparación lexicográfica
if cadena1 < cadena2:
	print(f'"{cadena1}" es menor que "{cadena2}" (lexicográficamente)')
elif cadena1 > cadena2:
	print(f'"{cadena1}" es mayor que "{cadena2}" (lexicográficamente)')
else:
	print(f'"{cadena1}" y "{cadena2}" son iguales')

# Comprobación de subcadena
sub = "la"
print(f'¿"{sub}" está en "{concatenada}"? ->', sub in concatenada)

