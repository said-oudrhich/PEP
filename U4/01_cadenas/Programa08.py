
"""
Programa08: Búsqueda y conteo

Escribe un programa en Python que realice las siguientes operaciones con cadenas:
- Declara una cadena "programacion en python".
- Busca la posición de "python" con find() o index().
- Cuenta cuántas veces aparece la letra "o".
- Verifica si comienza por "pro" y termina por "on".
"""

cadena = "programacion en python"
print('Cadena:', cadena)

pos = cadena.find('python')
print("Posición de 'python' (find):", pos)

veces_o = cadena.count('o')
print("Número de veces que aparece 'o':", veces_o)

print("Comienza por 'pro'? ->", cadena.startswith('pro'))
print("Termina por 'on'? ->", cadena.endswith('on'))

