"""
Programa01: Creación, longitud y acceso Básico

Escribe un programa en Python que realice las siguientes operaciones con cadenas:
- Define tres cadenas con comillas simples, dobles y triples.
- Muestra en pantalla cada una.
- Accede y muestra el primer y último carácter de una cadena mediante índices
	positivo y negativo.
"""

cadena_simple = 'Esta es una cadena con comillas simples.'
cadena_doble = "Esta es una cadena con comillas dobles."
cadena_triple = '''Esta es una cadena con comillas triples.
Puede abarcar múltiples líneas.'''

print(cadena_simple)
print(cadena_doble)
print(cadena_triple)

# Acceso por índices (positivo y negativo)
cadena = "Python"
print('\nCadena de ejemplo:', cadena)
print('Primer carácter (índice 0):', cadena[0])
print('Último carácter (índice positivo len-1):', cadena[len(cadena)-1])
print('Primer carácter (índice negativo -6):', cadena[-6])
print('Último carácter (índice negativo -1):', cadena[-1])
