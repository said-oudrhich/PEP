
"""
Programa06: Slicing e iteración

Escribe un programa en Python que realice las siguientes operaciones con cadenas:
- Crea una cadena "Python".
- Extrae la subcadena "Pyt" con slicing.
- Extrae los caracteres en posiciones pares con slicing ::2.
- Invierte la cadena con slicing [::-1].
- Recorre la cadena carácter por carácter e imprímelos.
"""

cadena = "Python"
print("Cadena:", cadena)

# Slicing
sub = cadena[0:3]
print('Subcadena [0:3]:', sub)
pares = cadena[::2]
print('Caracteres en posiciones pares [::2]:', pares)
invertida = cadena[::-1]
print('Cadena invertida [::-1]:', invertida)

# Iteración carácter por carácter
print('\nRecorrido carácter a carácter:')
for c in cadena:
	print(c)

