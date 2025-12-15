"""
═══════════════════════════════════════════════════════════════════════════
GUÍA COMPLETA: CADENAS DE CARACTERES (STRINGS) EN PYTHON
═══════════════════════════════════════════════════════════════════════════

Este archivo contiene TODOS los ejemplos y operaciones con cadenas que necesitas
para el examen. Usa Ctrl+F para buscar rápidamente lo que necesites.

ÍNDICE RÁPIDO (busca estos títulos):
1. CREACIÓN DE CADENAS
2. ACCESO POR ÍNDICES Y SLICING
3. OPERACIONES BÁSICAS (concatenación, repetición, comparación)
4. MÉTODOS DE CADENAS (upper, lower, strip, split, join, replace, etc.)
5. BÚSQUEDA Y CONTEO (find, index, count, startswith, endswith)
6. FORMATEO DE CADENAS (f-strings, format, %)
7. UNICODE Y ASCII (ord, chr)
8. VALIDACIÓN DE CADENAS (isdigit, isalpha, etc.)
9. SECUENCIAS DE ESCAPE

═══════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1. CREACIÓN DE CADENAS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("1. CREACIÓN DE CADENAS")
print("=" * 80)

# Comillas simples
cadena_simple = 'Esta es una cadena con comillas simples.'
print("Comillas simples:", cadena_simple)

# Comillas dobles
cadena_doble = "Esta es una cadena con comillas dobles."
print("Comillas dobles:", cadena_doble)

# Comillas triples (multilinea)
cadena_triple = '''Esta es una cadena con comillas triples.
Puede abarcar múltiples líneas.
Muy útil para documentación.'''
print("Comillas triples:", cadena_triple)

# Cadena vacía
cadena_vacia = ""
print("Cadena vacía:", repr(cadena_vacia), "| Longitud:", len(cadena_vacia))

# Longitud de cadena
print("Longitud de 'Python':", len("Python"))

print()

# ═══════════════════════════════════════════════════════════════════════════
# 2. ACCESO POR ÍNDICES Y SLICING
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("2. ACCESO POR ÍNDICES Y SLICING")
print("=" * 80)

cadena = "Python"
print(f"Cadena de ejemplo: '{cadena}'")

# Acceso por índice positivo
print(f"Primer carácter [0]: {cadena[0]}")
print(f"Tercer carácter [2]: {cadena[2]}")
print(f"Último carácter [len-1]: {cadena[len(cadena)-1]}")

# Acceso por índice negativo
print(f"Último carácter [-1]: {cadena[-1]}")
print(f"Penúltimo carácter [-2]: {cadena[-2]}")
print(f"Primer carácter [-6]: {cadena[-6]}")

# SLICING [inicio:fin:paso]
print(f"\nSlicing de '{cadena}':")
print(f"[0:3] -> '{cadena[0:3]}'  # Primeros 3 caracteres")
print(f"[2:5] -> '{cadena[2:5]}'  # Desde índice 2 hasta 4")
print(f"[:3] -> '{cadena[:3]}'    # Desde el principio hasta índice 2")
print(f"[3:] -> '{cadena[3:]}'    # Desde índice 3 hasta el final")
print(f"[::2] -> '{cadena[::2]}'  # Caracteres en posiciones pares")
print(f"[1::2] -> '{cadena[1::2]}'  # Caracteres en posiciones impares")
print(f"[::-1] -> '{cadena[::-1]}'  # Cadena invertida")

# Iteración carácter por carácter
print("\nRecorrido carácter a carácter:")
for i, c in enumerate(cadena):
    print(f"  Índice {i}: '{c}'")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 3. OPERACIONES BÁSICAS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("3. OPERACIONES BÁSICAS")
print("=" * 80)

cadena1 = "Hola"
cadena2 = "Mundo"

# Concatenación
concatenada = cadena1 + " " + cadena2
print(f"Concatenación: '{cadena1}' + ' ' + '{cadena2}' = '{concatenada}'")

# Repetición
repetida = cadena1 * 3
print(f"Repetición: '{cadena1}' * 3 = '{repetida}'")

# Comparación lexicográfica
print(f"\nComparación lexicográfica:")
print(f"'{cadena1}' < '{cadena2}' -> {cadena1 < cadena2}")
print(f"'{cadena1}' > '{cadena2}' -> {cadena1 > cadena2}")
print(f"'{cadena1}' == '{cadena2}' -> {cadena1 == cadena2}")

# Operador 'in' (subcadena)
sub = "la"
print(f"\nOperador 'in':")
print(f"¿'{sub}' está en '{concatenada}'? -> {sub in concatenada}")
print(f"¿'xyz' está en '{concatenada}'? -> {'xyz' in concatenada}")

# Operador 'not in'
print(f"¿'xyz' NO está en '{concatenada}'? -> {'xyz' not in concatenada}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 4. MÉTODOS DE CADENAS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("4. MÉTODOS DE CADENAS")
print("=" * 80)

cadena = "  Hola Mundo  "
print(f"Cadena original: {repr(cadena)}\n")

# Cambio de mayúsculas/minúsculas
print("MAYÚSCULAS/MINÚSCULAS:")
print(f"  upper(): '{cadena.upper()}'")
print(f"  lower(): '{cadena.lower()}'")
print(f"  capitalize(): '{cadena.capitalize()}'  # Primera letra mayúscula")
print(f"  title(): '{cadena.title()}'  # Primera letra de cada palabra")
print(f"  swapcase(): '{cadena.swapcase()}'  # Intercambia mayús/minus")

# Eliminación de espacios
print("\nELIMINACIÓN DE ESPACIOS:")
print(f"  strip(): {repr(cadena.strip())}  # Elimina espacios al inicio y final")
print(f"  lstrip(): {repr(cadena.lstrip())}  # Elimina espacios a la izquierda")
print(f"  rstrip(): {repr(cadena.rstrip())}  # Elimina espacios a la derecha")

# Reemplazo
print("\nREEMPLAZO:")
reemplazada = cadena.replace('Mundo', 'Python')
print(f"  replace('Mundo', 'Python'): {repr(reemplazada)}")

cadena_multiple = "banana"
print(f"  '{cadena_multiple}'.replace('a', 'o'): '{cadena_multiple.replace('a', 'o')}'")
print(f"  '{cadena_multiple}'.replace('a', 'o', 2): '{cadena_multiple.replace('a', 'o', 2)}'  # Solo 2 veces")

# División y unión
print("\nDIVISIÓN Y UNIÓN:")
palabras = cadena.strip().split()
print(f"  split(): {palabras}")

csv_texto = "manzana,pera,uva,plátano"
print(f"  '{csv_texto}'.split(','): {csv_texto.split(',')}")

print(f"  join() con '-': '{'-'.join(palabras)}'")
print(f"  join() con ', ': '{', '.join(['Python', 'Java', 'C++'])}'")

# Alineación y relleno
print("\nALINEACIÓN Y RELLENO:")
texto = "Python"
print(f"  center(20, '*'): '{texto.center(20, '*')}'")
print(f"  ljust(20, '-'): '{texto.ljust(20, '-')}'")
print(f"  rjust(20, '-'): '{texto.rjust(20, '-')}'")
print(f"  zfill(10): '{'42'.zfill(10)}'  # Rellena con ceros a la izquierda")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 5. BÚSQUEDA Y CONTEO
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("5. BÚSQUEDA Y CONTEO")
print("=" * 80)

cadena = "programacion en python"
print(f"Cadena: '{cadena}'\n")

# find() - devuelve -1 si no encuentra
print("MÉTODO find():")
print(f"  find('python'): {cadena.find('python')}  # Posición donde empieza")
print(f"  find('java'): {cadena.find('java')}  # Devuelve -1 si no encuentra")
print(f"  find('o'): {cadena.find('o')}  # Primera ocurrencia de 'o'")
print(f"  find('o', 5): {cadena.find('o', 5)}  # Busca desde el índice 5")

# index() - lanza excepción si no encuentra
print("\nMÉTODO index():")
print(f"  index('python'): {cadena.index('python')}")
# cadena.index('java')  # Esto daría ValueError

# count() - cuenta ocurrencias
print("\nMÉTODO count():")
print(f"  count('o'): {cadena.count('o')}")
print(f"  count('on'): {cadena.count('on')}")
print(f"  count('z'): {cadena.count('z')}")

# startswith() y endswith()
print("\nMÉTODOS startswith() y endswith():")
print(f"  startswith('pro'): {cadena.startswith('pro')}")
print(f"  startswith('java'): {cadena.startswith('java')}")
print(f"  endswith('on'): {cadena.endswith('on')}")
print(f"  endswith('python'): {cadena.endswith('python')}")

# rfind() y rindex() - buscan desde el final
print("\nBÚSQUEDA DESDE EL FINAL:")
print(f"  rfind('o'): {cadena.rfind('o')}  # Última ocurrencia de 'o'")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 6. FORMATEO DE CADENAS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("6. FORMATEO DE CADENAS")
print("=" * 80)

nombre = "Carlos"
edad = 25
altura = 1.75
precio = 19.99

# f-strings (Python 3.6+) - RECOMENDADO
print("F-STRINGS (RECOMENDADO):")
print(f"  Hola, me llamo {nombre} y tengo {edad} años.")
print(f"  Mi altura es {altura:.2f} metros.")  # 2 decimales
print(f"  Precio: {precio:.2f}€")
print(f"  Operación: 5 + 3 = {5 + 3}")
print(f"  {nombre:>10}  # Alineado a la derecha en 10 espacios")
print(f"  {nombre:<10}  # Alineado a la izquierda en 10 espacios")
print(f"  {nombre:^10}  # Centrado en 10 espacios")

# format()
print("\nMÉTODO format():")
print("  Hola, me llamo {} y tengo {} años.".format(nombre, edad))
print("  {0} tiene {1} años, y {0} mide {2:.2f}m.".format(nombre, edad, altura))
print("  {n} tiene {e} años.".format(n=nombre, e=edad))

# Formateo antiguo con % (estilo C)
print("\nFORMATEO CON % (ANTIGUO):")
print("  Hola, me llamo %s y tengo %d años." % (nombre, edad))
print("  Precio: %.2f€" % precio)

# Casos especiales
print("\nCASOS ESPECIALES:")
binario = 42
print(f"  Decimal: {binario}, Binario: {binario:b}, Hexadecimal: {binario:x}")
print(f"  Número con separador de miles: {1234567:,}")
print(f"  Porcentaje: {0.85:.2%}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 7. UNICODE Y ASCII
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("7. UNICODE Y ASCII")
print("=" * 80)

# ord() - código Unicode de un carácter
print("FUNCIÓN ord() - Carácter a código:")
print(f"  ord('A'): {ord('A')}")
print(f"  ord('a'): {ord('a')}")
print(f"  ord('0'): {ord('0')}")

emoji = '😄'
codigo = ord(emoji)
print(f"  ord('{emoji}'): {codigo} (hex: {hex(codigo)})")

# chr() - carácter desde código Unicode
print("\nFUNCIÓN chr() - Código a carácter:")
print(f"  chr(65): '{chr(65)}'")
print(f"  chr(97): '{chr(97)}'")
print(f"  chr(9731): '{chr(9731)}'  # U+2603 → ☃")

# Dígitos ASCII del 48 al 57
print("\nDÍGITOS ASCII (48-57):")
digitos = ''.join(chr(i) for i in range(48, 58))
print(f"  {digitos}")

# Letras mayúsculas ASCII (65-90)
print("\nLETRAS MAYÚSCULAS ASCII (65-90):")
mayusculas = ''.join(chr(i) for i in range(65, 91))
print(f"  {mayusculas}")

# Encoding y decoding
print("\nENCODING Y DECODING:")
texto = "Hola España"
codificado = texto.encode('utf-8')
print(f"  '{texto}'.encode('utf-8'): {codificado}")
print(f"  {codificado}.decode('utf-8'): '{codificado.decode('utf-8')}'")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 8. VALIDACIÓN DE CADENAS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("8. VALIDACIÓN DE CADENAS")
print("=" * 80)

# Métodos de validación
print("MÉTODOS is...():")
print(f"  '123'.isdigit(): {'123'.isdigit()}")
print(f"  'abc'.isdigit(): {'abc'.isdigit()}")

print(f"  'abc'.isalpha(): {'abc'.isalpha()}")
print(f"  'abc123'.isalpha(): {'abc123'.isalpha()}")

print(f"  'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"  'abc 123'.isalnum(): {'abc 123'.isalnum()}")

print(f"  'PYTHON'.isupper(): {'PYTHON'.isupper()}")
print(f"  'Python'.isupper(): {'Python'.isupper()}")

print(f"  'python'.islower(): {'python'.islower()}")
print(f"  'Python'.islower(): {'Python'.islower()}")

print(f"  'Python Programming'.istitle(): {'Python Programming'.istitle()}")
print(f"  'Python programming'.istitle(): {'Python programming'.istitle()}")

print(f"  '   '.isspace(): {'   '.isspace()}")
print(f"  'a b'.isspace(): {'a b'.isspace()}")

print(f"  '42'.isdecimal(): {'42'.isdecimal()}")
print(f"  '3.14'.isdecimal(): {'3.14'.isdecimal()}")

# Validación práctica
print("\nEJEMPLOS PRÁCTICOS DE VALIDACIÓN:")

def validar_dni(dni):
    """Valida formato básico de DNI: 8 dígitos + letra"""
    return len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha()

def validar_email_simple(email):
    """Validación MUY simple de email"""
    return '@' in email and '.' in email.split('@')[1]

print(f"  validar_dni('12345678A'): {validar_dni('12345678A')}")
print(f"  validar_dni('1234567A'): {validar_dni('1234567A')}")
print(f"  validar_email_simple('test@example.com'): {validar_email_simple('test@example.com')}")
print(f"  validar_email_simple('test@'): {validar_email_simple('test@')}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 9. SECUENCIAS DE ESCAPE
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("9. SECUENCIAS DE ESCAPE")
print("=" * 80)

print("SECUENCIAS DE ESCAPE COMUNES:")
print("  \\n - Salto de línea")
print("Primera línea\nSegunda línea")

print("\n  \\t - Tabulador")
print("Columna1\tColumna2\tColumna3")

print("\n  \\\\ - Backslash literal")
print("Ruta de Windows: C:\\Users\\nombre")

print("\n  \\' y \\\" - Comillas literales")
print('Texto con "comillas dobles" dentro')
print("Texto con 'comillas simples' dentro")

print("\n  \\r - Retorno de carro")
print("Línea completa\rNuevo texto")

# Raw strings (r"...")
print("\nRAW STRINGS (r'...'):")
print("  Sin raw string: 'C:\\nueva\\carpeta'")
print(r"  Con raw string: r'C:\nueva\carpeta'")
print(r"  Útil para regex: r'\d{3}-\d{2}-\d{4}'")

print()

# ═══════════════════════════════════════════════════════════════════════════
# 10. EJERCICIOS PRÁCTICOS ADICIONALES
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("10. EJERCICIOS PRÁCTICOS")
print("=" * 80)

# Ejercicio 1: Contar vocales
def contar_vocales(texto):
    """Cuenta el número de vocales en un texto"""
    vocales = 'aeiouAEIOU'
    return sum(1 for c in texto if c in vocales)

texto_prueba = "Programación en Python"
print(f"Vocales en '{texto_prueba}': {contar_vocales(texto_prueba)}")

# Ejercicio 2: Palíndromo
def es_palindromo(texto):
    """Verifica si un texto es palíndromo (ignora espacios y mayúsculas)"""
    limpio = ''.join(texto.lower().split())
    return limpio == limpio[::-1]

print(f"\n¿'anita lava la tina' es palíndromo? {es_palindromo('anita lava la tina')}")
print(f"¿'python' es palíndromo? {es_palindromo('python')}")

# Ejercicio 3: Invertir palabras
def invertir_palabras(frase):
    """Invierte el orden de las palabras en una frase"""
    return ' '.join(frase.split()[::-1])

frase_original = "Hola mundo desde Python"
print(f"\nFrase original: '{frase_original}'")
print(f"Invertida: '{invertir_palabras(frase_original)}'")

# Ejercicio 4: Capitalizar nombres
def capitalizar_nombre_completo(nombre):
    """Capitaliza correctamente un nombre completo"""
    return ' '.join(palabra.capitalize() for palabra in nombre.split())

nombre = "juan PÉREZ garcía"
print(f"\nNombre original: '{nombre}'")
print(f"Capitalizado: '{capitalizar_nombre_completo(nombre)}'")

# Ejercicio 5: Eliminar duplicados manteniendo orden
def eliminar_caracteres_duplicados(texto):
    """Elimina caracteres duplicados manteniendo el orden"""
    vistos = set()
    resultado = []
    for c in texto:
        if c not in vistos:
            vistos.add(c)
            resultado.append(c)
    return ''.join(resultado)

texto_dup = "programacion"
print(f"\nTexto con duplicados: '{texto_dup}'")
print(f"Sin duplicados: '{eliminar_caracteres_duplicados(texto_dup)}'")

print("\n" + "=" * 80)
print("FIN DE LA GUÍA DE CADENAS")
print("=" * 80)
print("Usa Ctrl+F para buscar rápidamente cualquier operación que necesites.")
print("=" * 80)
