
"""
Programa09: Unicode y ASCII

Escribe un programa en Python que realice las siguientes operaciones con cadenas:
- Muestra el código Unicode de un emoji (ord(), hex()).
- Crea un carácter a partir de un código numérico (chr()).
- Imprime los caracteres ASCII del 48 al 57 (dígitos) en una línea.
"""

emoji = '😄'
codigo = ord(emoji)
print(f"Código Unicode de {emoji}: {codigo} (hex: {hex(codigo)})")

# Crear carácter a partir de código numérico
car = chr(9731)  # U+2603 → ☃ (muñeco de nieve)
print('Carácter desde código 9731:', car)

# Imprimir dígitos ASCII del 48 al 57
digitos = ''.join(chr(i) for i in range(48, 58))
print('Dígitos ASCII 48-57:', digitos)

