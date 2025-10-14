def a_binario(n):
    try:
        return bin(n)[2:]
    except TypeError:
        return "Error: no es un entero válido"

def a_hexadecimal(n):
    try:
        return hex(n)[2:].upper()
    except TypeError:
        return "Error: no es un entero válido"

def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return "Error: la cadena no es un número entero válido"
