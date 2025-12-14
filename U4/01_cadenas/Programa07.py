
"""
Programa07: Métodos de cadena

Escribe un programa en Python que realice las siguientes operaciones con cadenas:
- Declara una cadena "  Hola Mundo  ".
- Aplica y muestra los resultados de: upper(), lower(), capitalize(), title().
- Elimina espacios con strip().
- Sustituye "Mundo" por "Python" con replace().
- Divide la cadena en palabras con split().
- Une una lista de palabras con join().
"""

cadena = "  Hola Mundo  "
print('Cadena original:', repr(cadena))

print('upper():', cadena.upper())
print('lower():', cadena.lower())
print('capitalize():', cadena.capitalize())
print('title():', cadena.title())

print('strip():', repr(cadena.strip()))

reemplazada = cadena.replace('Mundo', 'Python')
print('replace():', reemplazada)

palabras = cadena.split()
print('split():', palabras)

unida = '-'.join(palabras)
print('join() con "-":', unida)

